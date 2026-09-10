#!/usr/bin/env bash
# Script de instalación reproducible de SimpleRisk para el TP.
# Requiere: Docker y Docker Compose instalados.
set -euo pipefail

echo "== TP SimpleRisk - Instalación del entorno =="

if ! command -v docker &> /dev/null; then
  echo "ERROR: Docker no está instalado. Instalar desde https://docs.docker.com/get-docker/"
  exit 1
fi

echo "-> Levantando contenedores (MySQL + SimpleRisk)..."
docker compose up -d

echo "-> Esperando a que la base de datos esté lista (30s)..."
sleep 30

echo "-> Entorno levantado. Acceder a: http://localhost:8080"
echo "-> Completar el instalador web de SimpleRisk con credenciales DEMO (no reales)."