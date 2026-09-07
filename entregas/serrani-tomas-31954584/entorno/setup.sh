#!/usr/bin/env bash

# ==============================================================================
# Script de Despliegue Automatizado - SimpleRisk
# Estudiante: Tomas Serrani
# ==============================================================================

set -e

echo "=== Iniciando despliegue de SimpleRisk con Docker Compose ==="


if ! command -v docker &> /dev/null; then
    echo "[ERROR] Docker no está instalado o no se encuentra en el PATH."
    exit 1
fi
# 2. Levantar los contenedores en segundo plano
echo "[+] Desplegando contenedor de SimpleRisk..."
docker compose up -d

echo "[+] Esperando a que el servicio esté listo (30 segundos)..."
sleep 30

echo "=== Estado de los Contenedores ==="
docker compose ps

echo ""
echo "=============================================================================="
echo " Despliegue completado exitosamente."
echo " Accede a SimpleRisk desde tu navegador en: http://localhost:8080" o "https://localhost:8443"
echo "=============================================================================="