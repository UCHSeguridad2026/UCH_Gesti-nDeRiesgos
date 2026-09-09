#!/usr/bin/env python3
"""
notificar_riesgos.py — Integración SimpleRisk → Discord

Consulta el registro de riesgos de SimpleRisk y notifica por webhook de Discord
aquellos que superan el umbral de nivel Alto (valor >= 10 en la escala 1-25
configurada para este trabajo).

Uso:
    export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
    python3 notificar_riesgos.py

    python3 notificar_riesgos.py --dry-run      # muestra sin enviar
    python3 notificar_riesgos.py --umbral 16    # solo nivel Crítico

La URL del webhook NUNCA se escribe en este archivo ni se versiona en el
repositorio: se lee de una variable de entorno.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

CONTENEDOR = "simplerisk"
BASE_DATOS = "simplerisk"
UMBRAL_POR_DEFECTO = 10

# Bandas de nivel configuradas en SimpleRisk para este trabajo,
# alineadas con la plantilla de matriz de riesgos de la cátedra.
NIVELES = [
    (16, "Crítico", 0xD32F2F),
    (10, "Alto", 0xE64A19),
    (5, "Medio", 0xF9A825),
    (1, "Bajo", 0x7CB342),
]


def nivel_de(valor):
    """Devuelve (nombre, color) del nivel correspondiente a un valor de riesgo."""
    for minimo, nombre, color in NIVELES:
        if valor >= minimo:
            return nombre, color
    return "Insignificante", 0x9E9E9E


def ejecutar_en_contenedor(comando):
    """Ejecuta un comando dentro del contenedor de SimpleRisk."""
    resultado = subprocess.run(
        ["docker", "exec", CONTENEDOR, "sh", "-c", comando],
        capture_output=True,
    )

    def decodificar(datos):
        # MySQL puede devolver la salida en latin-1 según la codificación de
        # la conexión, por lo que se intenta UTF-8 y se recurre a latin-1.
        try:
            return datos.decode("utf-8")
        except UnicodeDecodeError:
            return datos.decode("latin-1")

    if resultado.returncode != 0:
        error = decodificar(resultado.stderr).strip()
        raise RuntimeError(error or "fallo al ejecutar en el contenedor")
    return decodificar(resultado.stdout)


def consultar_riesgos(umbral):
    """
    Consulta la base de datos de SimpleRisk y devuelve los riesgos abiertos
    cuyo valor calculado alcanza o supera el umbral indicado.

    La contraseña de MySQL es generada por el contenedor en el arranque y
    reside en /passwords/pass_mysql_root.txt dentro del propio contenedor;
    nunca se transporta fuera de él ni se almacena en este script.
    """
    consulta = (
        "SELECT r.id, r.subject, rs.calculated_risk, "
        "rs.CLASSIC_likelihood, rs.CLASSIC_impact "
        "FROM risks r "
        "JOIN risk_scoring rs ON r.id = rs.id "
        f"WHERE rs.calculated_risk >= {umbral} AND r.status <> 'Closed' "
        "ORDER BY rs.calculated_risk DESC;"
    )
    comando = (
        'mysql -u root -p"$(cat /passwords/pass_mysql_root.txt)" '
        f'--default-character-set=utf8mb4 {BASE_DATOS} -N -B -e "{consulta}"'
    )

    salida = ejecutar_en_contenedor(comando)

    riesgos = []
    for linea in salida.strip().splitlines():
        if not linea.strip():
            continue
        partes = linea.split("\t")
        if len(partes) < 5:
            continue
        riesgos.append({
            "id": int(partes[0]),
            "asunto": partes[1],
            "valor": float(partes[2]),
            "probabilidad": partes[3],
            "impacto": partes[4],
        })
    return riesgos


def construir_mensaje(riesgos, umbral):
    """Arma el cuerpo JSON del mensaje para el webhook de Discord."""
    if not riesgos:
        return {
            "content": f"Sin riesgos abiertos por encima del umbral {umbral}.",
            "embeds": [],
        }

    embeds = []
    for riesgo in riesgos[:10]:  # Discord admite hasta 10 embeds por mensaje
        nombre_nivel, color = nivel_de(riesgo["valor"])
        embeds.append({
            "title": f"[{nombre_nivel}] {riesgo['asunto']}",
            "color": color,
            "fields": [
                {"name": "Valor", "value": f"{riesgo['valor']:.0f}", "inline": True},
                {"name": "Probabilidad", "value": riesgo["probabilidad"], "inline": True},
                {"name": "Impacto", "value": riesgo["impacto"], "inline": True},
            ],
            "footer": {"text": f"SimpleRisk · ID {riesgo['id'] + 1000}"},
        })

    plural = "s" if len(riesgos) != 1 else ""
    return {
        "content": (
            f"**Alerta de gestión de riesgos**\n"
            f"{len(riesgos)} riesgo{plural} abierto{plural} con valor >= {umbral} "
            f"requiere{'n' if len(riesgos) != 1 else ''} tratamiento prioritario."
        ),
        "embeds": embeds,
    }


def enviar_a_discord(url, mensaje):
    """Publica el mensaje en el webhook de Discord."""
    # Discord opera detrás de Cloudflare, que rechaza con HTTP 403 las
    # peticiones que llegan con el User-Agent por defecto de urllib. Se
    # identifica la integración explícitamente, como exige su documentación.
    datos = json.dumps(mensaje).encode("utf-8")
    peticion = urllib.request.Request(
        url,
        data=datos,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "SimpleRisk-Discord-Integration/1.0 (TP Seguridad de Sistemas)",
        },
        method="POST",
    )
    with urllib.request.urlopen(peticion, timeout=15) as respuesta:
        return respuesta.status


def main():
    parser = argparse.ArgumentParser(
        description="Notifica por Discord los riesgos de SimpleRisk que superan un umbral."
    )
    parser.add_argument(
        "--umbral",
        type=int,
        default=UMBRAL_POR_DEFECTO,
        help=f"Valor mínimo de riesgo a notificar (por defecto {UMBRAL_POR_DEFECTO}, nivel Alto)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra los riesgos por consola sin enviar nada a Discord",
    )
    args = parser.parse_args()

    try:
        riesgos = consultar_riesgos(args.umbral)
    except FileNotFoundError:
        sys.exit("Error: no se encontró el comando 'docker'. ¿Está instalado?")
    except RuntimeError as error:
        sys.exit(f"Error al consultar SimpleRisk: {error}")

    print(f"Riesgos encontrados con valor >= {args.umbral}: {len(riesgos)}\n")
    for riesgo in riesgos:
        nombre_nivel, _ = nivel_de(riesgo["valor"])
        print(f"  [{nombre_nivel:>8}] {riesgo['valor']:>5.0f}  {riesgo['asunto']}")

    if args.dry_run:
        print("\nModo dry-run: no se envió nada a Discord.")
        return

    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        sys.exit(
            "\nError: falta la variable de entorno DISCORD_WEBHOOK_URL.\n"
            "  export DISCORD_WEBHOOK_URL=\"https://discord.com/api/webhooks/...\""
        )

    # discordapp.com es el dominio antiguo; el vigente es discord.com.
    url = url.replace("discordapp.com", "discord.com")

    mensaje = construir_mensaje(riesgos, args.umbral)

    try:
        estado = enviar_a_discord(url, mensaje)
    except urllib.error.HTTPError as error:
        sys.exit(f"\nDiscord rechazó la petición (HTTP {error.code}): {error.reason}")
    except urllib.error.URLError as error:
        sys.exit(f"\nNo se pudo contactar a Discord: {error.reason}")

    print(f"\nNotificación enviada correctamente (HTTP {estado}).")


if __name__ == "__main__":
    main()
