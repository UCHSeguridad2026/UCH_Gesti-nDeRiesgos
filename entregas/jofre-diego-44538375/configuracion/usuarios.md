# Usuarios y roles

A continuación se detallan los usuarios creados en SimpleRisk, junto con el rol asignado y sus permisos principales:

| Usuario | Rol asignado | Permisos principales |
|---|---|---|
| `admin_demo` | Administrador | Administración general de SimpleRisk |
| `analista_demo` | Analista de riesgos | Alta, evaluación y gestión de riesgos |
| `auditor_demo` | Auditor | Consulta y revisión de riesgos |
| `responsable_ti` | Responsable de TI | Revisión y seguimiento de riesgos tecnológicos asignados |

## Criterio de asignación de roles

Los usuarios fueron configurados con responsabilidades diferenciadas para evitar que una única cuenta concentre todas las funciones del proceso de gestión de riesgos.

Se aplicó un criterio de mínimo privilegio, asignando a cada rol únicamente los accesos necesarios para su función principal:

- El Administrador gestiona la configuración general de SimpleRisk.
- El Analista de Riesgos registra, evalúa y mantiene los riesgos.
- El Auditor realiza tareas de consulta y revisión independiente.
- El Responsable de TI realiza el seguimiento de los riesgos tecnológicos asignados, puede revisar y comentar riesgos y aceptar mitigaciones, sin disponer de permisos administrativos ni modificar la valoración realizada por el analista.

Las contraseñas utilizadas pertenecen exclusivamente al entorno de laboratorio y no se documentan ni almacenan en el repositorio.

> Las evidencias visuales de esta sección se encuentran en el directorio `informe/capturas/`.

*RECOMENDACIÓN: Abrir una pestaña en paralelo para visualizar las capturas.*

## Evidencias

- `18-Roles creados`
- `19-Permisos para analista de riesgo`
- `20-permisos para auditor`
- `21-Usuarios creados`
- `23-Permisos asignados al Responsable de TI`