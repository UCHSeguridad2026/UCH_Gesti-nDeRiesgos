# TP SimpleRisk — Seguridad de Sistemas

## Datos del estudiante
- Nombre completo: [Federico Diego Anguita]
- D.N.I: [44.404.612]
- Email institucional: [fdanguita@gmail.com]
- Comisión: [Comisión G]

## Objetivo
El trabajo implementa un registro inicial de riesgos para una clínica privada de 120 empleados y aproximadamente 800 pacientes por día, utilizando SimpleRisk como herramienta de gestión.

## Cómo levantar el entorno

### Requisitos
- Docker Desktop o Docker Engine + Docker Compose.
- Navegador web.

### Instalación
1. Ubicarse en la carpeta "entorno".
2. Ejecutar:

```bash
docker compose up -d
```

3. Verificar:

```bash
docker compose ps
```

4. Abrir en el navegador "http://localhost/".
5. Completar el asistente inicial de SimpleRisk.
6. Crear los tres usuarios indicados en "configuracion/usuarios.md".
7. Crear el riesgo de prueba.
8. Cargar los siete riesgos del escenario según "configuracion/riesgos.md".
9. Crear los tres planes de acción.
10. Tomar capturas de pantalla y guardarlas en "informe/capturas/".

> La instalación reproducible se documenta con Docker Compose. La documentación oficial de SimpleRisk ofrece una imagen Docker y recomienda persistencia de datos para despliegues reales.

## Decisiones de diseño
- Se utiliza una matriz cualitativa de probabilidad × impacto de 1 a 5, coherente con la consigna.
- El nivel de riesgo se calcula como "Probabilidad × Impacto".
- Se considera alto un resultado de 15 a 25.
- Los riesgos fueron diseñados específicamente para el contexto de una clínica y no como riesgos genéricos.
- Los valores son estimaciones académicas y deben validarse con datos reales antes de utilizarse en una organización.
- Se eligió FAIR como metodología alternativa para la comparación metodológica.
- La integración externa propuesta utiliza un sistema de tickets/webhook como mecanismo de seguimiento de planes de acción.

## Verificación
Palabra clave solicitada por la cátedra: **girasol**.

## Checklist de auto-revisión
- [ ] No hay credenciales en el repositorio.
- [ ] El ".gitignore" está configurado.
- [ ] Las capturas no muestran datos sensibles.
- [ ] No hay archivos ".sql" o dumps reales.
- [ ] El informe es legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] La branch está actualizada y funciona.
- [ ] Se reemplazaron los datos personales de este README.
- [ ] Se ejecutó realmente la instalación de SimpleRisk y se agregaron capturas.

## Nota de entrega
Los documentos de análisis y planificación están preparados. La parte que necesariamente debe realizarse en el equipo del estudiante es la ejecución de SimpleRisk, creación de usuarios/riesgos/planes dentro de la interfaz y obtención de capturas reales. No deben presentarse como realizadas si todavía no fueron ejecutadas.
