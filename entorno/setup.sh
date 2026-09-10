#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

echo "=============================================="
echo "   SimpleRisk - Levantamiento del entorno"
echo "=============================================="
echo

echo "[1/4] Verificando Docker..."
if ! command -v docker >/dev/null 2>&1; then
    echo "ERROR: Docker no está instalado o no está disponible."
    exit 1
fi
echo "OK: Docker disponible."

echo
echo "[2/4] Verificando Docker Compose..."
if ! docker compose version >/dev/null 2>&1; then
    echo "ERROR: Docker Compose no está disponible."
    exit 1
fi
echo "OK: Docker Compose disponible."

echo
echo "[3/4] Verificando archivo de configuración..."
if [ ! -f "entorno/.env" ]; then
    echo "ERROR: No se encontró entorno/.env"
    echo "Creá el archivo con las variables de entorno requeridas."
    exit 1
fi
echo "OK: entorno/.env encontrado."

echo
echo "[4/4] Levantando SimpleRisk..."
docker compose --env-file entorno/.env -f entorno/docker-compose.yml up -d

echo
echo "=============================================="
echo "   Estado del entorno"
echo "=============================================="
docker compose --env-file entorno/.env -f entorno/docker-compose.yml ps

echo
echo "SimpleRisk debería estar disponible en:"
echo "https://localhost"
echo
echo "Entorno levantado correctamente."
