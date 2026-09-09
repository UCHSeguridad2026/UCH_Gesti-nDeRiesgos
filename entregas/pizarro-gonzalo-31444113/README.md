
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

1. Clonar el repositorio y ubicarse en `entregas/pizarro-gonzalo-31444113`.
2. Revisar `entorno/docker-compose.yml` y completar cualquier variable local requerida sin subir archivos `.env`.
3. Ejecutar `docker compose -f entorno/docker-compose.yml up -d`.
4. Consultar los contenedores con `docker compose -f entorno/docker-compose.yml ps`.
5. Abrir en el navegador la URL publicada por Docker, completar el instalador de SimpleRisk y conservar la URL local: `[COMPLETAR]`.
6. Crear los usuarios indicados en `configuracion/usuarios.md`, sin documentar contraseñas.
7. Cargar los riesgos de `configuracion/riesgos.md` y asociar los planes de acción definidos allí.
8. Verificar que SimpleRisk muestre los riesgos, niveles y responsables esperados.

Para detener el entorno: `docker compose -f entorno/docker-compose.yml down`. Para conservar los datos, no eliminar los volúmenes sin respaldo.

## Decisiones de diseño

- Se utiliza una matriz cualitativa de probabilidad por impacto, ambos en escala de 1 a 5.
- El nivel se calcula como `probabilidad × impacto`: 1–4 bajo, 5–9 medio, 10–16 alto y 17–25 crítico.
- Se priorizan riesgos que afectan historias clínicas, continuidad de atención y obligaciones de privacidad.
- Los valores son una evaluación inicial del escenario y deben revisarse con evidencia de incidentes, auditorías y métricas reales.
- girasol xD

## Archivos de la entrega

- `entorno/`: definición del entorno reproducible.
- `configuracion/usuarios.md`: roles y permisos, sin contraseñas.
- `configuracion/riesgos.md`: registro inicial y planes de acción.
- `informe/informe.md`: desarrollo, comparación metodológica e integración.
- `informe/capturas/`: evidencias sin secretos ni datos personales.
- `reporte-ejecutivo/reporte.pdf`: resumen para el directorio.

## Checklist de auto-revisión

- [ ] No hay credenciales, tokens ni claves en el repositorio.
- [x] El `.gitignore` excluye secretos, dumps y archivos sensibles.
- [ ] Las capturas no muestran datos sensibles.
- [x] No se subieron archivos SQL ni dumps.
- [ ] El informe está completo y legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] La rama fue probada desde cero.
