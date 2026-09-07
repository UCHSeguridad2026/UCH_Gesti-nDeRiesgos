#!/usr/bin/env python3
"""
notify_slack_risks.py

Script de integración SimpleRisk -> Slack para el TP de Seguridad de Sistemas.

CONTEXTO:
La API REST de SimpleRisk ("API Extra") es una funcionalidad de pago, no
disponible en la instalación Community/Docker usada en este TP. Por lo tanto,
este script simula el paso de "consultar riesgos" leyendo un archivo JSON
local (riesgos_actuales.json) en lugar de consultar la API de SimpleRisk
directamente. La lógica de notificación a Slack (la parte más importante de
la integración) es 100% real y funcional: usa un Incoming Webhook real de
Slack para mandar un mensaje real al canal #seguridad-riesgos.

Si en el futuro se adquiriera la "API Extra" de SimpleRisk, solo habría que
reemplazar la función `obtener_riesgos()` para que haga un GET a
`{SIMPLERISK_URL}/api/risks` en lugar de leer el JSON local. El resto del
script (filtrado por nivel y envío a Slack) funcionaría sin cambios.

USO:
    python notify_slack_risks.py

REQUISITOS:
    pip install requests python-dotenv --break-system-packages

CONFIGURACION:
    Crear un archivo .env (NUNCA subir a git) con:
        SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
        SIMPLERISK_URL=https://localhost
"""

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (que está en .gitignore)
load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SIMPLERISK_URL = os.getenv("SIMPLERISK_URL", "https://localhost")

# Niveles que se consideran dignos de notificación inmediata
NIVELES_A_NOTIFICAR = {"Alto", "Crítico"}

RUTA_RIESGOS = Path(__file__).parent / "riesgos_actuales.json"


def obtener_riesgos():
    """
    Obtiene la lista de riesgos actuales.

    NOTA: En una integración real con la API Extra de SimpleRisk, esta
    función haría algo como:

        resp = requests.get(
            f"{SIMPLERISK_URL}/api/risks",
            headers={"X-API-KEY": API_KEY, "X-API-AUTH": API_SECRET},
            verify=False,  # solo por el certificado autofirmado local
        )
        return resp.json()

    Como esa API requiere una extensión paga, leemos un JSON local que
    representa el estado actual de los riesgos cargados manualmente en
    SimpleRisk (ver riesgos_actuales.json).
    """
    if not RUTA_RIESGOS.exists():
        print(f"ERROR: no se encontró {RUTA_RIESGOS}")
        sys.exit(1)

    with open(RUTA_RIESGOS, "r", encoding="utf-8") as f:
        return json.load(f)


def formatear_mensaje_slack(riesgos_criticos):
    """Arma el payload de Slack con los riesgos de nivel Alto/Crítico."""
    if not riesgos_criticos:
        texto = "✅ No hay riesgos de nivel Alto o Crítico pendientes en este momento."
    else:
        lineas = [f"🚨 *{len(riesgos_criticos)} riesgo(s) de nivel Alto/Crítico requieren atención:*\n"]
        for r in riesgos_criticos:
            lineas.append(
                f"• *{r['nombre']}* — Nivel: *{r['nivel']}* (Valor: {r['valor']})\n"
                f"   _Categoría: {r['categoria']} | Propietario: {r['propietario']}_"
            )
        texto = "\n".join(lineas)

    return {"text": texto}


def enviar_a_slack(payload):
    """Envía el mensaje al canal de Slack vía Incoming Webhook."""
    if not SLACK_WEBHOOK_URL:
        print("ERROR: SLACK_WEBHOOK_URL no está configurado en el archivo .env")
        sys.exit(1)

    respuesta = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)

    if respuesta.status_code == 200:
        print("✅ Notificación enviada correctamente a Slack.")
    else:
        print(f"❌ Error al enviar a Slack: {respuesta.status_code} - {respuesta.text}")


def main():
    print("Leyendo riesgos actuales...")
    riesgos = obtener_riesgos()

    riesgos_criticos = [r for r in riesgos if r["nivel"] in NIVELES_A_NOTIFICAR]

    print(f"Se encontraron {len(riesgos_criticos)} riesgo(s) de nivel Alto/Crítico de un total de {len(riesgos)}.")

    payload = formatear_mensaje_slack(riesgos_criticos)
    enviar_a_slack(payload)


if __name__ == "__main__":
    main()
