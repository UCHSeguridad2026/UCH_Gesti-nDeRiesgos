#!/usr/bin/env bash
# ==========================================================
# setup.sh - Levantamiento reproducible de SimpleRisk
# TP Seguridad de Sistemas - Cangialosi Leonardo (LU 31041361)
# ==========================================================
# Este script instala/levanta SimpleRisk en un entorno local con Docker.
# Probado en macOS (Apple Silicon) con Docker Desktop.
#
# Uso:
#   chmod +x setup.sh
#   ./setup.sh
#
set -euo pipefail

CONTAINER_NAME="simplerisk"
IMAGE="simplerisk/simplerisk:latest"
PLATFORM="linux/amd64"   # requerido en Apple Silicon (emulacion)

echo "==> Verificando que Docker este instalado y corriendo..."
if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: Docker no esta instalado. Instala Docker Desktop primero."
  exit 1
fi
if ! docker info >/dev/null 2>&1; then
  echo "ERROR: Docker no esta corriendo. Abri Docker Desktop y reintenta."
  exit 1
fi

echo "==> Descargando imagen ($IMAGE) para $PLATFORM..."
docker pull --platform "$PLATFORM" "$IMAGE"

# Si ya existe un contenedor con el mismo nombre, lo removemos.
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
  echo "==> Removiendo contenedor previo '$CONTAINER_NAME'..."
  docker rm -f "$CONTAINER_NAME"
fi

echo "==> Levantando el contenedor..."
docker run --platform "$PLATFORM" \
  --name "$CONTAINER_NAME" \
  -d \
  -p 80:80 -p 443:443 \
  --restart unless-stopped \
  "$IMAGE"

echo "==> Esperando a que el servicio este saludable..."
sleep 10
docker ps --filter "name=${CONTAINER_NAME}"

cat <<'EOF'

==========================================================
 SimpleRisk levantado.
 Abri en el navegador:  https://localhost/
 (Aceptar la advertencia de certificado autofirmado)

 Credenciales iniciales por defecto: admin / admin
 >>> CAMBIAR LA CONTRASENA de admin de inmediato <<<
==========================================================
EOF
