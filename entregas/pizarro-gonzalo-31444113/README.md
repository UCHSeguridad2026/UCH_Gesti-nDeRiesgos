
# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- **Nombre:** Gonzalo Pizarro
- **LU:** 31444113
- **Email institucional:** pizarrogonzalo@uch.edu.ar
- **Comisión:** G - Plan de estudio 2016
- **Rama:** entrega/pizarro-gonzalo-31444113

## Objetivo y escenario

Se analiza la **Clínica UCH**, una clínica privada de 120 empleados, aproximadamente 800 pacientes diarios y sistemas de historias clínicas digitales, obras sociales y facturación. El registro considera confidencialidad, integridad, disponibilidad, cumplimiento legal y continuidad operativa.

## Cómo levantar el entorno

1. Instalar y abrir Docker Desktop, con Docker Compose disponible.
2. Clonar el repositorio y ubicarse en `entregas/pizarro-gonzalo-31444113`.
3. Ejecutar `docker compose -f entorno/docker-compose.yml pull` para descargar la imagen oficial.
4. Ejecutar `docker compose -f entorno/docker-compose.yml up -d`.
5. Consultar los contenedores con `docker compose -f entorno/docker-compose.yml ps`.
6. Abrir `http://localhost:8080/` en el navegador y completar el instalador inicial de SimpleRisk. También se puede usar `https://localhost:8443/`; el navegador advertirá sobre el certificado autofirmado.
7. Crear los usuarios indicados en `configuracion/usuarios.md`, sin documentar contraseñas.
8. Cargar los riesgos de `configuracion/riesgos.md` y asociar los planes de acción definidos allí.
9. Verificar que SimpleRisk muestre los riesgos, niveles y responsables esperados.

También se puede ejecutar `bash entorno/setup.sh` desde la raíz del trabajo; el script descarga la imagen, levanta el contenedor y muestra las URLs de acceso. La configuración de SimpleRisk, su base de datos y las credenciales internas se almacenan en los volúmenes nombrados `simplerisk_data`, `simplerisk_database` y `simplerisk_passwords`.

Para detener el entorno: `docker compose -f entorno/docker-compose.yml down`. Este comando conserva los volúmenes y permite recuperar la instalación al ejecutar nuevamente `up -d`. No ejecutar `docker compose -f entorno/docker-compose.yml down -v` salvo que se quiera eliminar la configuración y los datos; realizar respaldos de los volúmenes antes de cualquier operación destructiva.

## Decisiones de diseño

- Se utiliza una matriz cualitativa de probabilidad por impacto, ambos en escala de 1 a 5.
- El nivel se calcula como `probabilidad × impacto`: bajo, medio, alto y crítico.
- Se priorizan riesgos que afectan historias clínicas, continuidad de atención y obligaciones de privacidad.
- Los valores son una evaluación inicial del escenario y deben revisarse con evidencia de incidentes, auditorías y métricas reales.
- GIRASOL!!!! casi me lo olvido xD

## Archivos de la entrega

- `entorno/`: definición del entorno reproducible.
- `configuracion/usuarios.md`: roles y permisos, sin contraseñas.
- `configuracion/riesgos.md`: registro inicial y planes de acción.
- `informe/informe.md`: desarrollo, comparación metodológica e integración.
- `informe/capturas/`: evidencias sin secretos ni datos personales.
- `reporte-ejecutivo/reporte.pdf`: resumen para el directorio.

## Checklist de auto-revisión

- [x] No hay credenciales, tokens ni claves en el repositorio.
- [x] El `.gitignore` excluye secretos, dumps y archivos sensibles.
- [x] Las capturas no muestran datos sensibles.
- [x] No se subieron archivos SQL ni dumps.
- [x] El informe está completo y legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] La rama fue probada desde cero.
