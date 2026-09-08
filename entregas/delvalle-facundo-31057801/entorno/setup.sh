#!/bin/bash
# Script de despliegue de SimpleRisk en Docker para entorno local

echo "Verificando instalación y servicio de Docker..."
if ! command -v docker &> /dev/null; then
    echo "Docker no está instalado. Instálelo antes de continuar."
    exit 1
fi

sudo systemctl start docker

# Verificar si el contenedor ya existe
if [ "$(docker ps -aq -f name=simplerisk)" ]; then
    echo "Iniciando contenedor existente simplerisk..."
    docker start simplerisk
else
    echo "Creando e iniciando contenedor simplerisk..."
    docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk
fi

echo "SimpleRisk iniciado correctamente."
echo "Acceda mediante el navegador a: https://localhost/"
