#!/bin/bash

echo "Iniciando entorno de SimpleRisk..."

if ! command -v docker >/dev/null 2>&1; then
    echo "Error: Docker no está instalado."
    exit 1
fi

docker compose up -d

echo ""
echo "SimpleRisk iniciado correctamente."
echo "Acceder desde: https://localhost/"