#TP: SimpleRisk — Seguridad de Sistemas

## Datos del estudiante

- **Nombre completo:** Julian Greco
- **D.N.I:** 39169367
- **Email:** julian_greco@hotmail.com
- **Comisión:** G

## Descripción 

Este repositorio contiene el desarrollo individual del trabajo práctico de la materia Seguridad de Sistemas, orientado al análisis y gestión de riesgos utilizando SimpleRisk.

El trabajo se desarrolla sobre el escenario de una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día y gestiona historias clínicas digitales, información de obras sociales y datos de facturación.

El objetivo principal es identificar, analizar, evaluar y tratar riesgos de seguridad de la información considerando el contexto particular de la organización.


## Estructura del repositorio

- entorno/: archivos necesarios para levantar el entorno de SimpleRisk.
- informe/: desarrollo completo del trabajo y capturas de pantalla.
- configuracion/: documentación de usuarios, permisos y riesgos definidos.
- scripts/: scripts auxiliares utilizados durante el desarrollo, si corresponde.
- reporte-ejecutivo/: reporte resumido destinado a la gerencia de la clínica.

## Para reproducir el entorno se requiere:
 
- Docker
- Docker Compose
- Git
- Navegador web

## Para reproducir el entorno se requiere:

Desde la carpeta entorno/:

- `cd entorno`
- `docker compose up -d`

Verificar que los contenedores se encuentren funcionando:

- `docker compose ps`

Una vez iniciado el entorno, acceder desde el navegador a:

- `http://localhost:[PUERTO]`

El puerto y los pasos específicos pueden modificarse según la configuración utilizada en docker-compose.yml.

## Detención del entorno

Para detener el entorno:

- `docker compose down`

Si se requiere eliminar también los volúmenes asociados:

- `docker compose down -v`

## Supuestos del escenario

Para realizar el análisis se consideran los siguientes supuestos:

La clínica posee aproximadamente 120 empleados.
Se atienden aproximadamente 800 pacientes por día.
Las historias clínicas son gestionadas digitalmente.
La organización almacena información médica y datos personales de pacientes.
Se procesan datos relacionados con obras sociales y facturación.
Existen sistemas informáticos críticos para la atención de pacientes.
La clínica depende de la disponibilidad de sus sistemas para mantener parte de su operación normal.
La auditoría externa detectó debilidades en la gestión de riesgos.
No se presume la existencia de controles de seguridad avanzados salvo que sean indicados explícitamente en el análisis.
Los controles existentes y las medidas de tratamiento propuestas se documentan como parte del análisis de cada riesgo.
Estos supuestos permiten construir un escenario consistente sin asumir información que no fue proporcionada explícitamente.

## Riesgos

Se definieron riesgos específicos relacionados con el funcionamiento de una clínica y sus activos de información.

Cada riesgo incluye:

- Nombre y descripción.
- Categoría.
- Activos afectados.
- Probabilidad.
- Impacto.
- Nivel de riesgo.
- Justificación de la valoración.
- Controles existentes.
- Tratamiento propuesto.
- Propietario del riesgo.

El detalle completo se encuentra en:

configuracion/riesgos.md

Los riesgos también fueron registrados en SimpleRisk.

## Planes de acción
Para los riesgos identificados como de nivel alto se definieron planes de acción destinados a reducir la exposición de la organización.

Cada plan incluye:

- Título.
- Descripción.
- Responsable.
- Fecha de vencimiento.
- Presupuesto estimado.
- Estado inicial.
- Riesgo asociado.
  
Los avances y evidencias correspondientes se encuentran documentados en el informe.

## Análisis metodológico
Además de la utilización de la matriz de Probabilidad × Impacto, se analiza una metodología alternativa de gestión de riesgos.

Se comparan las ventajas y limitaciones del enfoque utilizado por SimpleRisk con la metodología seleccionada, considerando aspectos como:

- Facilidad de implementación.
- Nivel de subjetividad.
- Reproducibilidad de las evaluaciones.
- Necesidad de datos cuantitativos.
- Aplicabilidad a una organización como la clínica.
- Utilidad para la toma de decisiones.
- El análisis completo se encuentra en:

informe/informe.md

## Decisiones de diseño y seguridad

- Se trabajará exclusivamente en la branch `entrega/julian-greco-39169367`.
- Se utilizarán datos de demostración y contraseñas locales, nunca credenciales reales.
- Los secretos, archivos de entorno, respaldos y dumps de bases de datos permanecerán fuera del repositorio mediante `.gitignore`.
- Las capturas serán revisadas antes de incorporarlas para evitar exponer contraseñas, tokens, direcciones IP reales o datos personales.
- Verificación de lectura de la consigna: **girasol**.


## 📌 Checklist de Auto-Revisión
*Por favor, marca las casillas correspondientes antes de realizar tu entrega:*

- [ ] No hay credenciales en el repositorio.
- [ ] El archivo `.gitignore` está correctamente configurado.
- [ ] Las capturas de pantalla no muestran datos sensibles.
- [ ] Los archivos `.sql` o dumps no están subidos.
- [ ] El informe está en un formato legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] Mi branch está actualizada y funciona correctamente.


