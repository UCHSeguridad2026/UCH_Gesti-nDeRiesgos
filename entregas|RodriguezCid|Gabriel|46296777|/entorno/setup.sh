#!/bin/bash

# ======================================================
# Script Automatizado: Despliegue de SimpleRisk (GRC)
# Entorno: Kali Linux / Contenedores Docker
# ======================================================

# Colores para la terminal
VERDE="\033[1;32m"
ROJO="\033[1;31m"
AZUL="\033[1;34m"
RESET="\033[0m"

echo -e "${AZUL}======================================================${RESET}"
echo -e "${AZUL}    CONFIGURANDO ENTORNO DE GESTIÓN DE RIESGOS       ${RESET}"
echo -e "${AZUL}======================================================${RESET}"

# Verificar si se ejecuta con privilegios necesarios
if [ "$EUID" -ne 0 ]; then
  echo -e "${ROJO}[!] Advertencia: Se recomienda ejecutar este script con privilegios adecuados (sudo).${RESET}"
fi

# Comprobar si Docker está activo
if ! command -v docker &> /dev/null; then
    echo -e "${ROJO}[X] Error crítico: Docker no se encuentra instalado.${RESET}"
    exit 1
fi

# Comprobar si Docker Compose está disponible
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo -e "${ROJO}[X] Error crítico: Docker Compose no está disponible.${RESET}"
    exit 1
fi

echo -e "\n${VERDE}[*] Paso 1 de 3: Desplegando servicios mediante contenedores...${RESET}"
docker-compose up -d

echo -e "\n${VERDE}[*] Paso 2 de 3: Aguardando inicialización de la base de datos (20 segundos)...${RESET}"
sleep 20

echo -e "\n${VERDE}[*] Paso 3 de 3: Comprobando estado actual de los contenedores...${RESET}"
docker-compose ps

echo -e "\n${AZUL}======================================================${RESET}"
echo -e "${VERDE}    ¡Despliegue finalizado de forma exitosa!          ${RESET}"
echo -e "${VERDE}    Plataforma disponible en: http://localhost:8080   ${RESET}"
echo -e "${AZUL}======================================================${RESET}"