# TP — Gestión de Riesgos con SimpleRisk

**Alumno:** Nicolás Estrella
**Legajo:** 31.066.692
**Materia:** Seguridad de Sistemas
**Email institucional:** [completar con mail de la facultad]
**Comisión:** [completar]

## Decisiones de diseño

- Se optó por representar una clínica privada de 120 empleados (según el escenario propuesto por la cátedra), con foco en el servidor de historias clínicas electrónicas (HCE) como activo crítico central, dado que es el eje de la mayoría de los riesgos relevados.
- La metodología de riesgos utilizada es la matriz clásica de probabilidad × impacto (escala 1-5) provista por SimpleRisk, justificando cada valor con el contexto específico de la clínica (falta de área de IT dedicada, ausencia de controles formales) en lugar de usar valores genéricos.
- Se priorizaron los 7 riesgos elegidos por representar las categorías principales de un análisis de seguridad (confidencialidad, integridad, disponibilidad, legal y operativo), evitando repetir riesgos redundantes sobre el mismo activo.
- Para la comparación metodológica de la Parte C se eligió FAIR por ser la que más contrasta con el enfoque cualitativo de SimpleRisk, al expresar el riesgo en términos de pérdida económica estimada.

## Contenido de esta entrega

- `configuracion/` — Documentación de usuarios/roles (usuarios.md) y del registro completo de riesgos (riesgos.md).
- `informe/` — Informe completo del TP (Partes A, B y C) y capturas de pantalla como evidencia.
- `reporte-ejecutivo/` — Reporte ejecutivo en PDF (resumen para dirección).
- `entorno/` — (sin uso adicional; el entorno se levanta con el comando de Docker detallado abajo).

## Cómo levantar el entorno

Este TP utiliza la imagen oficial de SimpleRisk sobre Docker. Para replicar el entorno, ejecutar:

docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk

Luego de unos minutos (inicialización de la base de datos interna), acceder desde el navegador a:

https://localhost/

El certificado es autofirmado, por lo que el navegador va a mostrar una advertencia de conexión no segura — es esperable, hay que aceptar avanzar igual.

## Resumen de lo realizado

- **Parte A:** Instalación de SimpleRisk vía Docker, creación de 3 usuarios con roles diferenciados (Administrador, Analista de Riesgos, Auditor) bajo el principio de menor privilegio, y carga de un riesgo de prueba para validar el sistema.
- **Parte B:** Identificación y carga de 7 riesgos reales para un escenario de clínica privada (120 empleados, ~800 pacientes/día, historias clínicas electrónicas), y definición de 3 planes de acción para los riesgos más críticos.
- **Parte C:** Comparación entre el enfoque clásico de SimpleRisk (matriz probabilidad × impacto) y la metodología FAIR, más una propuesta de integración con Slack mediante webhooks.

## Checklist de auto-revisión

- [x] Rama propia creada dentro del repositorio del curso (`entrega/estrella-nicolas-31066692`)
- [x] Estructura de carpetas completa dentro de `entregas/`
- [x] `.gitignore` configurado en la raíz del repositorio
- [x] SimpleRisk instalado y funcionando (Docker)
- [x] 3 usuarios con roles y permisos diferenciados
- [x] 7 riesgos cargados y documentados
- [x] 3 planes de acción para los riesgos más críticos
- [x] Informe completo (`informe/informe.md`) con Partes A, B y C
- [x] Capturas de evidencia en `informe/capturas/`
- [x] Reporte ejecutivo en PDF (máx. 3 páginas) en `reporte-ejecutivo/`
- [x] Sin contraseñas ni credenciales reales subidas al repositorio