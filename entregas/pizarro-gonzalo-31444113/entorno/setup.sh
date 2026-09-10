#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
COMPOSE_FILE="$SCRIPT_DIR/docker-compose.yml"

docker compose -f "$COMPOSE_FILE" pull
docker compose -f "$COMPOSE_FILE" up -d

echo "SimpleRisk esta disponible en http://localhost:8080/"
echo "HTTPS (certificado autofirmado): https://localhost:8443/"
echo "Consultar el estado con: docker compose -f entorno/docker-compose.yml ps"
