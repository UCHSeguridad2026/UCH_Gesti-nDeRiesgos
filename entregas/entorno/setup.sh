#!/bin/bash


echo "======================================================"
echo "   Iniciando Despliegue de SimpleRisk (Seguridad)    "
echo "======================================================"

if ! command -v docker &> /dev/null
then
    echo "[ERROR] Docker no está instalado. Por favor instala Docker antes de continuar."
    exit 1
fi

if ! command -v docker-compose &> /dev/null
then
    echo "[ERROR] Docker Compose no está instalado."
    exit 1
fi

echo "[1/3] Levantando contenedores con Docker Compose..."
docker-compose up -d

echo "[2/3] Esperando 15 segundos a que la base de datos inicialice..."
sleep 15

echo "[3/3] Verificando estado de los servicios..."
docker-compose ps

echo "======================================================"
echo "   ¡Entorno desplegado con éxito!                     "
echo "   Accede a SimpleRisk en: http://localhost:8080      "
echo "======================================================"
open http://localhost
