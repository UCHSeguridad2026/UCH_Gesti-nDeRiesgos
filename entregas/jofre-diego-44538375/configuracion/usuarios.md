# Usuarios y roles

A continuación se detallan los usuarios creados en SimpleRisk, junto con el rol asignado y sus permisos principales:

| Usuario | Rol asignado | Permisos principales |
|---|---|---|
| `admin_demo` | Administrador | Administración general de SimpleRisk |
| `analista_demo` | Analista de riesgos | Alta, evaluación y gestión de riesgos |
| `auditor_demo` | Auditor | Consulta y revisión de riesgos |

## Criterio de asignación de roles

Los usuarios fueron configurados con responsabilidades diferenciadas para evitar que una única cuenta concentre todas las funciones del proceso de gestión de riesgos.

Se aplicó un criterio de mínimo privilegio, asignando a cada rol únicamente los accesos necesarios para su función principal:

- El Administrador gestiona la configuración general de SimpleRisk.
- El Analista de Riesgos registra, evalúa y mantiene los riesgos.
- El Auditor realiza tareas de consulta y revisión independiente.

Las contraseñas utilizadas pertenecen exclusivamente al entorno de laboratorio y no se documentan ni almacenan en el repositorio.

Evidencias:
- `18-Roles creados`
- `19-Permisos para analista de riesgo`
- `20-permisos para auditor`
- `21-Usuarios creados`