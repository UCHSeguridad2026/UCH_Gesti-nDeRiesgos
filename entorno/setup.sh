#!/usr/bin/env bash
# setup.sh — Instalación reproducible de SimpleRisk sobre Ubuntu con Docker
# Probado en Ubuntu 22.04 / 24.04 LTS (VirtualBox).
# Ejecutar:  chmod +x setup.sh && ./setup.sh
set -euo pipefail

echo "==> [1/4] Actualizando el sistema e instalando dependencias..."
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg lsb-release

echo "==> [2/4] Instalando Docker Engine + Docker Compose plugin (si faltan)..."
if ! command -v docker >/dev/null 2>&1; then
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  sudo chmod a+r /etc/apt/keyrings/docker.gpg
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
  sudo apt-get update -y
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin
  sudo usermod -aG docker "$USER" || true
fi

echo "==> [3/4] Levantando SimpleRisk con Docker Compose..."
# Ejecutar desde la carpeta que contiene docker-compose.yml (esta misma).
cd "$(dirname "$0")"
sudo docker compose up -d

echo "==> [4/4] Esperando a que el servicio esté disponible..."
sleep 20
sudo docker compose ps

cat <<'EOF'

============================================================
  SimpleRisk levantado correctamente.
  Abrí en el navegador:   https://localhost/
  (aceptá el certificado autofirmado)

  Login inicial:  usuario = admin   contraseña = admin
  --> Cambiá la contraseña en el primer ingreso.

  Comandos útiles:
    sudo docker compose ps        # estado
    sudo docker compose logs -f   # ver logs
    sudo docker compose down      # detener (conserva datos)
============================================================
EOF
