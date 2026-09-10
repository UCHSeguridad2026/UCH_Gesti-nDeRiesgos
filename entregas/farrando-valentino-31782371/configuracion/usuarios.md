# Usuarios y permisos

Todas las cuentas corresponden a una clínica ficticia.
Las contraseñas se definen durante la instalación y no se incluyen
en este documento ni en el repositorio.

## Cuentas creadas

| Usuario | Función | Permisos |
|---|---|---|
| admin_clinica | Administrador de SimpleRisk | Administración completa del sistema. |
| analista_riesgos | Analista de riesgos | Acceder a gestión de riesgos, crear riesgos, modificar sus detalles, planificar mitigaciones y comentar. |
| auditor_riesgos | Auditor de consulta | Acceder al módulo de gestión de riesgos para consultar registros. |
| direccion_medica | Propietario de R01 y R04 | Acceder al módulo de gestión de riesgos. |
| responsable_administracion | Propietario de R02, R03 y R05 | Acceder al módulo de gestión de riesgos. |
| responsable_sistemas | Propietario de R06 y R07 y responsable de PA01–PA03 | Acceder al módulo de gestión de riesgos. |

## Configuración de permisos

El administrador se creó durante el primer acceso a SimpleRisk.

Las otras cinco cuentas se crearon desde:
Settings → User Management → Add Users.

Se seleccionó:
- Type: SimpleRisk.
- Role: sin rol predefinido seleccionado.
- Manager y Team: sin asignación.
- Sin privilegios de administrador.

Las funciones de la tabla describen responsabilidades organizacionales.
Para estas cuentas se configuraron permisos individuales mediante
User Responsibilities; no se crearon roles personalizados.

## Permisos del analista

Se habilitaron únicamente:

- Allow Access to "Risk Management" Menu.
- Able to Submit New Risks.
- Able to Modify Risk Details.
- Able to Plan Mitigations.
- Able to Comment Risk Management.

No se concedieron permisos de revisión formal, aceptación de
mitigaciones ni cierre de riesgos.

## Permisos del auditor y los propietarios

Se habilitó únicamente:

- Allow Access to "Risk Management" Menu.

Ser propietario de un riesgo o responsable de una mitigación
representa una responsabilidad asignada, pero no concede por sí
solo permisos adicionales de edición o aprobación.

En este ejercicio, el administrador registra las asignaciones
y los planes en nombre de los responsables.

## Prueba de permisos del auditor

Se utilizó el riesgo de prueba ID 1001:
[PRUEBA] Indisponibilidad del sistema de turnos.

Resultados observados:

1. El auditor pudo consultar el listado y abrir el detalle.
2. El menú Actions ofreció únicamente Printable View.
3. El botón Update Classic Score permitió abrir un formulario.
4. Al intentar guardar un cambio, el sistema rechazó la operación
   mediante un mensaje de permisos insuficientes.

La prueba verifica el rechazo de esa modificación de puntuación;
no constituye una auditoría completa de todos los permisos.

Mejora identificada: ocultar o deshabilitar los controles de edición
para usuarios sin autorización, manteniendo la validación del servidor.

## Criterios de seguridad

- Mínimo privilegio: se asignan únicamente los permisos necesarios.
- Separación entre administración, análisis y consulta.
- Contraseñas distintas para las cuentas del ejercicio.
- Cuentas locales de SimpleRisk independientes de Ubuntu y GitHub.
- Segundo factor y cambio obligatorio de contraseña al ingresar
  no se habilitaron durante esta práctica inicial.
- Las capturas de evidencia deben excluir contraseñas y tokens.
