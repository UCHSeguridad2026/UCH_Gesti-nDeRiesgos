# Registro de Usuarios y Permisos

A continuación se detallan los usuarios creados en el sistema SimpleRisk para la gestión de la clínica, cumpliendo con el principio de separación de roles. No se incluyen credenciales por motivos de seguridad.

| Usuario | Rol Asignado | Nivel de Permisos / Justificación |
| :--- | :--- | :--- |
| `admin_clinica` | Administrator | Control total del sistema. Encargado de la configuración general y altas/bajas. |
| `analista_sistemas` | Risk User / Analyst | Capacidad para cargar, evaluar y proponer mitigaciones para los riesgos de la clínica. (Permisos customizados en responsabilidades). |
| `auditor_ext` | Reader / Auditor | Permisos de solo lectura para revisar el estado de los riesgos sin capacidad de modificación. (Permisos customizados en responsabilidades). |

Detalle de Permisos por Rol en SimpleRisk
1. Usuario: admin_clinica (Rol: Administrator)

Este usuario cuenta con la casilla "Check All" activada, lo que le otorga control total e irrestricto sobre la plataforma.

Posee acceso y capacidad de edición (agregar, modificar, eliminar y aprobar) en absolutamente todos los módulos del sistema: Governance, Risk Management, Compliance, Asset Management, Assessments y Artificial Intelligence.

2. Usuario: analista_sistemas (Rol: Risk User / Analyst)

Tiene acceso habilitado únicamente a los menús de "Risk Management" y "Asset Management".

Dentro del módulo de riesgos, está autorizado para ingresar nuevos riesgos (Submit New Risks), modificar sus detalles (Modify Risk Details), planificar mitigaciones (Plan Mitigations) y agregar comentarios (Comment Risk Management).

Posee permisos de revisión para visualizar riesgos de todos los niveles (desde Insignificant hasta Very High).

Para mantener la segregación de funciones, no se le otorgaron permisos para cerrar riesgos (Close Risks), aceptar mitigaciones (Accept Mitigations), ni administrar proyectos o reportes.

3. Usuario: auditor_ext (Rol: Reader / Auditor)

Este perfil está configurado estrictamente como solo lectura, permitiéndole el acceso a los menús de "Governance", "Risk Management", "Compliance" y "Asset Management".

En el módulo de gestión de riesgos, sus permisos se limitan de forma exclusiva a revisar los riesgos en todas sus criticidades (Review Insignificant a Very High Risks).

No tiene habilitada ninguna casilla de acción, lo que significa que no puede enviar (Submit), modificar, cerrar, planificar mitigaciones, ni comentar sobre ningún riesgo o control dentro de la plataforma.