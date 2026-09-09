# Usuarios y Roles Configurados en SimpleRisk

Trabajo Práctico: Gestión de Riesgos con SimpleRisk
Parte A — Punto 2: Usuarios y permisos

> **Nota de seguridad.** Este documento no contiene contraseñas. Las credenciales utilizadas en el entorno son ficticias y de uso exclusivo para la validación académica del trabajo.

---

## 1. Criterio de diseño

Los tres usuarios corresponden a los cargos definidos en el análisis de riesgos como propietarios de riesgo (ver `configuracion/riesgos.md`, sección 7.1). La decisión de hacer coincidir usuarios del sistema con propietarios de riesgo busca que la configuración de la herramienta refleje la estructura de responsabilidades del análisis y no una asignación arbitraria.

La separación entre los tres cargos responde a un criterio de segregación de funciones: **quien administra la infraestructura no es quien audita los accesos**. Si el Jefe de Sistemas ejerciera además la función de auditoría, estaría revisando su propio trabajo, lo que anula el valor de la revisión.

---

## 2. Usuarios del escenario

| Usuario | Nombre completo / Cargo | Correo (ficticio) | Rol asignado |
|---|---|---|---|
| `admin_demo` | Jefe de Sistemas | admin_demo@clinica-demo.local | Administrator |
| `analista_demo` | Responsable de Seguridad de la Información | analista_demo@clinica-demo.local | Analista de Riesgos |
| `auditor_demo` | Responsable de Cumplimiento y Protección de Datos | auditor_demo@clinica-demo.local | Auditor |

Los correos utilizan el dominio `.local`, reservado por convención para redes internas y no resoluble en internet, a fin de dejar constancia explícita de que se trata de direcciones ficticias.

### Cuenta administrativa inicial

| Usuario | Nombre completo | Rol | Observación |
|---|---|---|---|
| `Admin` | Lautaro Barbero | Administrator | Cuenta administrativa creada durante el despliegue del entorno, previa a la configuración del escenario |

Esta cuenta se conserva documentada por transparencia: es la utilizada para el despliegue inicial y la configuración de roles, y no forma parte del escenario simulado de la clínica. En un entorno productivo correspondería deshabilitarla una vez transferida la administración a las cuentas nominales, conforme a la recomendación de gestión de cuentas del propio análisis.

---

## 3. Roles y permisos

SimpleRisk incorpora únicamente el rol **Administrator** en su instalación por defecto. Los roles **Analista de Riesgos** y **Auditor** fueron creados específicamente para este trabajo, definiendo sus permisos uno por uno sobre el catálogo de 46 responsabilidades que ofrece la herramienta.

### 3.1. Administrator

Rol provisto por la herramienta. Otorga la totalidad de los permisos disponibles, incluido el acceso al menú de configuración del sistema (gestión de usuarios, roles, escalas de riesgo y parámetros generales).

**Asignado a:** Jefe de Sistemas.

**Fundamento.** El cargo tiene a su cargo la infraestructura, la red, los servidores, los respaldos y la base de datos, y es propietario de los riesgos R01, R02, R05 y R06. Requiere capacidad de configuración sobre la herramienta.

### 3.2. Analista de Riesgos

Rol creado para el escenario. Perfil operativo sobre la gestión de riesgos, sin capacidad de configuración del sistema ni de eliminación de registros.

| Módulo | Permisos otorgados |
|---|---|
| Risk Management | Acceso al menú; enviar nuevos riesgos; modificar detalles; cerrar riesgos; planificar mitigaciones; aceptar mitigaciones; revisar riesgos de todos los niveles; comentar; agregar proyectos; gestionar proyectos; agregar reportes guardados |
| Governance | Acceso al menú; ver excepciones; actualizar excepciones |
| Compliance | Acceso al menú; comentar |
| Asset Management | Acceso al menú |
| Assessments | Acceso al menú |
| Artificial Intelligence | Ninguno |

**Permisos deliberadamente excluidos:** eliminar proyectos, eliminar reportes guardados, aprobar excepciones, y toda modificación sobre frameworks, controles y documentación de gobierno.

**Asignado a:** Responsable de Seguridad de la Información.

**Fundamento.** El cargo identifica y evalúa riesgos, define salvaguardas y da seguimiento a los planes de acción; es propietario de R03, R07 y R08. Necesita operar plenamente sobre el registro de riesgos, pero no configurar la herramienta ni aprobar sus propias excepciones, lo que constituiría un conflicto de funciones.

### 3.3. Auditor

Rol creado para el escenario. Perfil de **solo lectura y comentario**, sin capacidad de crear, modificar ni eliminar registro alguno.

| Módulo | Permisos otorgados |
|---|---|
| Governance | Acceso al menú; ver excepciones |
| Risk Management | Acceso al menú; comentar |
| Compliance | Acceso al menú; comentar |
| Asset Management | Acceso al menú |
| Assessments | Acceso al menú |
| Artificial Intelligence | Ninguno |

**Asignado a:** Responsable de Cumplimiento y Protección de Datos.

**Fundamento.** El cargo revisa los registros de auditoría de accesos y verifica el cumplimiento normativo sobre historias clínicas; es propietario de R04. La restricción a solo lectura es deliberada: un auditor con capacidad de modificar aquello que audita pierde independencia, y su función es constatar el estado del sistema, no alterarlo. La facultad de comentar le permite dejar observaciones formales sin intervenir sobre los registros.

---

## 4. Verificación de los permisos

La configuración fue verificada de dos maneras.

### 4.1. Reporte de permisos por usuario

Desde `Configure → User Management → User Reports`, con el reporte *Users of Permissions*, se constató la diferenciación efectiva entre roles. Ejemplos representativos:

| Permiso | Usuarios que lo poseen |
|---|---|
| Approve Exceptions | Solo cuentas administrativas |
| Add Projects | Cuentas administrativas y `analista_demo` |
| Comment Risk Management | Los cuatro usuarios |
| Define Tests | Solo cuentas administrativas |

La progresión confirma que los tres perfiles tienen alcances distintos y no se trata de tres cuentas con idénticos privilegios.

**Evidencia:** `informe/capturas/usuarios-permisos-reporte-*.png`

### 4.2. Prueba de acceso efectivo

Se inició sesión con `auditor_demo` para comprobar el comportamiento real del rol. Diferencias observadas respecto de una sesión administrativa:

- **No se muestra el ícono de configuración** en la barra superior: el usuario no accede al menú `Configure` y, por lo tanto, no puede gestionar usuarios, roles ni parámetros del sistema
- El panel *What's Next?* presenta únicamente dos acciones disponibles, frente a las cuatro de una sesión administrativa, al omitir las tareas de registro de la instancia y configuración
- Los menús de Governance, Risk Management, Compliance, Asset Management y Assessments permanecen accesibles, conforme a lo definido para el rol

Esta verificación es relevante porque comprueba el comportamiento efectivo del sistema y no únicamente la configuración declarada.

**Evidencia:** `informe/capturas/permisos-verificacion-auditor-*.png`

---

## 5. Observaciones sobre la herramienta

Durante la configuración se identificaron funcionalidades de SimpleRisk que implementan controles equivalentes a los propuestos en el plan de tratamiento de la clínica.

**Autenticación multifactor.** El formulario de alta de usuarios incluye la opción *Multi-Factor Authentication*. Corresponde a la salvaguarda propuesta en R07 y en el plan PA-02 para los perfiles con acceso a historia clínica. Se mantiene desactivada en este entorno para permitir la reproducción del trabajo por parte del docente sin requerir la configuración de un dispositivo autenticador; en un despliegue productivo correspondería activarla para los perfiles de mayor privilegio.

**Granularidad de permisos.** El catálogo de 46 responsabilidades individuales permite implementar el principio de mínimo privilegio con precisión, que es el control central del plan PA-03. La herramienta no obliga a elegir entre perfiles predefinidos: cada permiso se otorga o deniega de forma independiente.

**Registro de auditoría.** El módulo `Configure → Audit Trail` registra y permite exportar las acciones de los usuarios sobre el sistema. Es la implementación directa del registro de auditoría de accesos que el plan PA-03 propone para el sistema de gestión clínica.

**Deshabilitación frente a eliminación.** La sección *Enable and Disable Users* permite desactivar el acceso de un usuario conservando el rastro de auditoría de su actividad previa. Esta distinción refina la recomendación formulada en PA-03 sobre la baja de cuentas al egreso del personal: la revocación debe implementarse como **deshabilitación y no como eliminación**, dado que borrar la cuenta destruiría la trazabilidad histórica de las acciones realizadas por esa persona, que es precisamente la evidencia que el control busca preservar.

---

## 6. Evidencia documental

| Archivo | Contenido |
|---|---|
| `rol-administrator-1.png`, `rol-administrator-2.png` | Permisos del rol Administrator |
| `rol-analista-riesgos-1.png`, `rol-analista-riesgos-2.png` | Permisos del rol Analista de Riesgos |
| `rol-auditor-1.png`, `rol-auditor-2.png` | Permisos del rol Auditor |
| `usuario-alta-admin.png`, `usuario-alta-analista.png`, `usuario-alta-auditor.png` | Formularios de alta de los tres usuarios |
| `usuario-detalle-admin-*.png`, `usuario-detalle-analista-*.png`, `usuario-detalle-auditor-*.png` | Detalle de cada usuario con su rol asignado |
| `usuarios-permisos-reporte-*.png` | Reporte comparativo de permisos por usuario |
| `permisos-verificacion-auditor-*.png` | Sesión iniciada con el rol Auditor |
