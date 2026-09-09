# Parte A — Instalación y configuración

## A.1 Instalación de SimpleRisk

Se utilizó Docker Compose para implementar un entorno reproducible
compuesto por dos contenedores:

- SimpleRisk
- MySQL 8.0

La aplicación se expone localmente mediante el puerto 8080.

## A.2 Levantamiento del entorno

Desde la carpeta `entorno/` se ejecutaron:

```bash
docker compose pull
docker compose up -d
docker compose ps
