# Gestión de Usuarios y Permisos — SimpleRisk

Se configuraron tres cuentas en SimpleRisk aplicando el **principio de menor privilegio** y separación de funciones entre administración, análisis y auditoría.

> **Nota de seguridad:** no se documentan contraseñas ni hashes de autenticación en este repositorio, tal como exige la consigna.

## Tabla de Usuarios Configurados

| Nombre de Usuario | Rol Funcional | Descripción |
| :--- | :--- | :--- |
| `admin1` | Administrador | Cuenta de administración global del sistema (creada por defecto al instalar SimpleRisk). Gestión de usuarios, configuración y parámetros del sistema. |
| `analista de riesgo` | Analista de Riesgos | Encargado de identificar, cargar y dar seguimiento a los riesgos de la clínica y sus planes de mitigación. |
| `auditor` | Auditor | Acceso de solo revisión, para controlar el proceso de gestión de riesgos sin poder modificarlo. |

## Matriz de Permisos (User Responsibilities)

SimpleRisk en esta versión no usa roles predefinidos con nombre — el control de acceso se implementa mediante checkboxes individuales de responsabilidades ("User Responsibilities"), que permiten construir permisos a medida en lugar de asignar un rol genérico.

### `analista de riesgo` — Analista de Riesgos

| Sección | Permiso otorgado |
| :--- | :--- |
| Governance | Allow Access to "Governance" Menu, Able to View Exceptions |
| Risk Management | Allow Access to "Risk Management" Menu, Able to Submit New Risks, Able to Modify Risk Details, Able to Plan Mitigations, Able to Comment Risk Management, Able to Add Projects, Able to Manage Projects, Able to Add Saved Risk Reports |

**Justificación:** puede identificar y documentar riesgos, y proponer mitigaciones, pero no tiene permiso para cerrar riesgos (`Close Risks`) ni aceptar mitigaciones (`Accept Mitigations`) — esas decisiones quedan reservadas a un nivel de aprobación superior (administrador), evitando que la misma persona que carga un riesgo lo pueda dar por resuelto sin revisión.

### `auditor` — Auditor

| Sección | Permiso otorgado |
| :--- | :--- |
| Governance | Allow Access to "Governance" Menu, Able to View Exceptions |
| Risk Management | Allow Access to "Risk Management" Menu, Able to Comment Risk Management |
| Compliance | Allow Access to "Compliance" Menu, Able to Initiate Audits, Able to Approve Tests |

**Justificación:** puede revisar el registro de riesgos, comentar y ejecutar auditorías de cumplimiento, pero no tiene ningún permiso de creación, edición o borrado sobre riesgos, mitigaciones ni proyectos — coherente con el rol de un auditor externo que debe mantener independencia respecto de lo que audita.

### `admin1` — Administrador

Cuenta con permisos completos de administración del sistema (gestión de usuarios, configuración global). Uso restringido a tareas de mantenimiento de la plataforma, no para la operación diaria de gestión de riesgos.
