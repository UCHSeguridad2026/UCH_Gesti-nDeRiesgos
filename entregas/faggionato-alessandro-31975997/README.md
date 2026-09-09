# Trabajo Práctico — Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- **Nombre completo:** Alessandro Faggionato
- **LU:** 31975997
- **Email:** alefaggionato@gmail.com
- **Comisión:** G

## Descripción y objetivo

Este trabajo presenta el análisis y tratamiento inicial de riesgos de seguridad de la información para una clínica privada ficticia de 120 empleados. La clínica atiende aproximadamente 800 pacientes por día y utiliza historias clínicas digitales, información de obras sociales y sistemas de facturación.

El objetivo es identificar riesgos realistas para la operación de la clínica, evaluarlos de manera consistente y proponer acciones de tratamiento fundamentadas. Se utiliza SimpleRisk para registrar y gestionar esos riesgos.

## Cómo levantar el entorno

El entorno utiliza Docker Compose para ejecutar SimpleRisk y MySQL 8. Los datos, archivos cargados y logs se conservan en volúmenes de Docker; por lo tanto, la inicialización de la base se realiza solamente una vez.

1. Abrir Docker Desktop y esperar que indique el estado **Running**.
2. Abrir PowerShell en la carpeta `entorno/` de esta entrega.
3. Crear la configuración local a partir del ejemplo:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Editar `.env` y reemplazar los valores que comienzan con `CAMBIAR_` por claves locales largas y diferentes. No usar contraseñas reales.
5. Solo en una instalación nueva, inicializar la base de datos:

   ```powershell
   docker compose up -d mysql
   docker compose --profile setup run --rm setup
   ```

6. Iniciar SimpleRisk:

   ```powershell
   docker compose up -d simplerisk
   docker compose ps
   ```

7. Abrir [https://localhost](https://localhost) e iniciar sesión con `ADMIN_USERNAME` y `ADMIN_PASSWORD` definidos en `.env`. El certificado es autofirmado para este entorno local, por lo que el navegador mostrará una advertencia de seguridad que debe aceptarse únicamente para esta práctica.

En inicios posteriores no se repite la inicialización: alcanza con `docker compose up -d`.

Para diagnóstico y apagado:

```powershell
docker compose logs simplerisk
docker compose logs mysql
docker compose down
```

`docker compose down` conserva los datos. No ejecutar `docker compose down -v` salvo que se quiera borrar intencionalmente la instalación y los riesgos cargados.

## Decisiones de diseño y seguridad

- Se trabajó exclusivamente en la branch `entrega/faggionato-alessandro-31975997`.
- Se utilizaron datos de demostración y contraseñas locales, nunca credenciales reales.
- Los secretos, archivos de entorno, respaldos y dumps de bases de datos permanecerán fuera del repositorio mediante `.gitignore`.
- Las capturas fueron revisadas antes de incorporarlas para evitar exponer contraseñas, tokens, direcciones IP reales o datos personales.
- Verificación de lectura de la consigna: **girasol**.

## Checklist de seguridad y entrega

- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona correctamente.
