Mateo Agustin Falanti - 31645404 - mateofalantiuch@gmail.com 

comision: G

# Instalación de SimpleRisk (Parte A)

## Requisitos previos

- Docker Desktop instalado y corriendo (Windows, con el motor de Linux containers habilitado).
- Puertos `8080` y `8443` libres en el host.

## Pasos para levantar el entorno

1. Ubicate en la carpeta del proyecto que contiene `entorno/docker-compose.yml`.

   ```
   cd entrega/<apellido>-<nombre>-<lu>/entorno
   ```

2. Levantá el contenedor:

   ```
   docker compose up -d
   ```

3. Verificá que esté corriendo:

   ```
   docker ps
   ```

   Deberías ver el contenedor `simplerisk` con estado `Up` y los puertos `8080->80` y `8443->443`.

4. Esperá 1-2 minutos a que Apache y MySQL terminen de inicializar dentro del contenedor.

5. Abrí el navegador en:

   ```
   https://localhost:8443/
   ```

   El navegador va a advertir que el certificado es autofirmado y no confiable. Es esperable en este entorno de prueba: aceptá la excepción para continuar.

6. `index.php` detecta que no hay instalación previa y te redirige automáticamente al wizard de configuración inicial (selección de idioma, chequeo de requisitos, configuración de base de datos, creación de la cuenta de administrador, etc.). Completá los 6 pasos.

7. Al finalizar el wizard, vas a llegar a la pantalla de login de SimpleRisk con la cuenta de administrador que acabás de crear.

## Decisiones de diseño

- **Imagen utilizada:** `simplerisk/simplerisk` (imagen oficial *all-in-one*, incluye Apache + PHP + MySQL en un solo contenedor), en lugar de `simplerisk-minimal` + MySQL separado. Se eligió por simplicidad: un solo servicio, sin necesidad de coordinar variables de entorno entre contenedores ni de un servicio SMTP adicional.
- **Puertos:** se mapearon `8080` y `8443` en el host (en vez de `80`/`443`) para evitar conflictos con otros servicios que suelen ocupar esos puertos en Windows (IIS, otros contenedores, etc.).
- **Persistencia:** esta imagen no documenta oficialmente un volumen externo para los datos; mientras no se elimine el contenedor (`docker rm`) los datos persisten entre `docker compose stop` / `up`. Se documenta esta limitación en vez de asumir una ruta de volumen no confirmada.

## Verificación de reproducibilidad

Para confirmar que la instalación es reproducible sin intervención manual adicional:

```
docker compose down
docker compose up -d
```

El entorno debe volver a estar disponible en `https://localhost:8443/` sin pasos extra más allá de esperar a que el contenedor inicialice.

## Problemas conocidos

- Si el puerto `8080` u `8443` ya está en uso en tu máquina, cambiá el mapeo en `docker-compose.yml` (por ejemplo `"8081:80"`) y volvé a levantar el entorno.
- Si la página no carga al primer intento, esperá unos segundos más: MySQL puede tardar en inicializar dentro del contenedor la primera vez.