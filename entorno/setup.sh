#!/bin/sh
set -eu

echo "Levantando SimpleRisk..."
docker compose up -d

echo "Estado de los servicios:"
docker compose ps

echo "Abrir http://localhost/ en el navegador y completar el asistente inicial."
