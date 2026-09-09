# Parte A — Instalación y configuración

## A.1 Instalación de SimpleRisk

Se utilizó Docker Compose para implementar un entorno reproducible
compuesto por dos contenedores:

- SimpleRisk
- MySQL 8.0


## A.2 Levantamiento del entorno

Desde la carpeta `entorno/` se ejecutaron:

```bash
docker compose pull
docker compose up -d
docker compose ps
```

### Acceso a SimpleRisk

La aplicación utiliza HTTPS. Para permitir el acceso desde el
host se publicaron los siguientes puertos:

- `8080` → HTTP
- `8443` → HTTPS

El acceso principal al sistema se realiza mediante:

`https://localhost:8443`

Al tratarse de un entorno local de laboratorio, el certificado
HTTPS no corresponde a una autoridad certificadora pública.
