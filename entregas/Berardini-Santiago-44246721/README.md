# TP Gestión de Riesgos con SimpleRisk

## Datos personales

- **Nombre completo:** Santiago Berardini
- **LU:** 44246721
- **Email:** santiagoberardini02@hotmail.com
- **Comisión:** G

## Instrucciones para levantar el entorno

1. Tener Docker Desktop instalado y corriendo.
2. Ubicarse en la carpeta `entorno/` de esta entrega:

cd entregas/Berardini-Santiago-44246721/entorno

3. Levantar el contenedor:

docker compose up -d

4. Esperar a que termine de descargar la imagen 
5. Acceder desde el navegador a `https://localhost/` 
6. Iniciar sesión con el usuario administrador creado durante la instalación.

## Decisiones de diseño

- Se usó la imagen oficial `simplerisk/simplerisk` de Docker Hub, que incluye la aplicación completa junto con su base de datos en un solo contenedor, simplificando el despliegue para este TP.
- Se definieron 2 roles adicionales al de Administrador por defecto: **Analista de Riesgos** y **Auditor**.
- Los 7 riesgos se pensaron con niveles de gravedad variados (2 Medio-bajo, 2 Medio, 3 Alto) para un análisis más realista.
- Se utilizó el método de puntuación "Classic" que trae SimpleRisk por defecto.
- Para la Parte C, se comparó SimpleRisk con la metodología FAIR (ver `informe/informe.md`, sección 6).

### Verificación

Se realizó la lectura completa del enunciado del TP. Palabra clave: girasol.

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio
- [x] El .gitignore está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos .sql o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona
