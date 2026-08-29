#!/usr/bin/env python3
"""
notificar_riesgos.py — Prueba de concepto (Parte D2/D3)
TP SimpleRisk — Seguridad de Sistemas — Cangialosi Leonardo (LU 31041361)

Consulta la API de SimpleRisk y notifica a un webhook de Slack/Discord los
riesgos de nivel Alto o Crítico.

SEGURIDAD:
  - Ni la API key ni la URL del webhook se escriben en el código ni se versionan.
  - Se leen desde variables de entorno (o un archivo .env, excluido por .gitignore):
        SIMPLERISK_URL       (ej: https://localhost)
        SIMPLERISK_API_KEY   (API key generada en SimpleRisk)
        WEBHOOK_URL          (Incoming Webhook de Slack o Discord)

Uso:
    export SIMPLERISK_URL="https://localhost"
    export SIMPLERISK_API_KEY="****"
    export WEBHOOK_URL="https://hooks.slack.com/services/****"
    python3 notificar_riesgos.py

Nota: contra localhost con certificado autofirmado se usa verify=False solo para
la demo. En producción usar un certificado válido y verify=True.
"""
import os
import sys
import json
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

UMBRAL_VALOR = 10  # Valor P*I >= 10 => Alto o Crítico (según la tabla de niveles)


def env(nombre: str) -> str:
    valor = os.environ.get(nombre)
    if not valor:
        sys.exit(f"[ERROR] Falta la variable de entorno {nombre}")
    return valor


def obtener_riesgos(base_url: str, api_key: str) -> list:
    """Consulta la API de SimpleRisk. Ajustar el endpoint segun la version."""
    url = f"{base_url.rstrip('/')}/api/management/risk/all"
    resp = requests.get(url, headers={"Authorization": api_key},
                        verify=False, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    # SimpleRisk suele devolver {"status":..., "data":[...]}
    return data.get("data", data if isinstance(data, list) else [])


def es_alto_o_critico(riesgo: dict) -> bool:
    """Filtra por valor de riesgo (P*I) >= umbral, tolerando distintos nombres de campo."""
    for campo in ("calculated_risk", "risk_level", "residual_risk"):
        try:
            return float(riesgo.get(campo, 0)) >= UMBRAL_VALOR
        except (TypeError, ValueError):
            continue
    return False


def notificar(webhook_url: str, riesgos: list) -> None:
    if not riesgos:
        print("[OK] No hay riesgos Alto/Crítico para notificar.")
        return
    lineas = ["*⚠️ Riesgos ALTO/CRÍTICO en SimpleRisk:*"]
    for r in riesgos:
        nombre = r.get("subject") or r.get("name") or f"ID {r.get('id', '?')}"
        valor = r.get("calculated_risk") or r.get("risk_level") or "?"
        lineas.append(f"• {nombre} — valor {valor}")
    payload = {"text": "\n".join(lineas)}   # Slack usa 'text'; Discord usa 'content'
    payload["content"] = payload["text"]     # compatibilidad con ambos
    resp = requests.post(webhook_url, data=json.dumps(payload),
                         headers={"Content-Type": "application/json"}, timeout=15)
    resp.raise_for_status()
    print(f"[OK] Notificados {len(riesgos)} riesgos al webhook.")


def main() -> None:
    base_url = env("SIMPLERISK_URL")
    api_key = env("SIMPLERISK_API_KEY")
    webhook_url = env("WEBHOOK_URL")
    riesgos = obtener_riesgos(base_url, api_key)
    criticos = [r for r in riesgos if es_alto_o_critico(r)]
    notificar(webhook_url, criticos)


if __name__ == "__main__":
    main()
