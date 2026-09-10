# Usuarios y roles - SimpleRisk

## 1. Objetivo

Este documento describe los usuarios creados en SimpleRisk para el desarrollo del Trabajo Práctico de Gestión de Riesgos.

Se configuraron tres usuarios con responsabilidades diferenciadas, aplicando el principio de separación de funciones y otorgando a cada usuario los permisos necesarios para desarrollar su función.

Por seguridad, **no se almacenan ni documentan contraseñas, tokens ni credenciales de acceso** en este repositorio.

---

## 2. Usuarios configurados

| Usuario         | Nombre           | Rol / función               | Administrador |
| --------------- | ---------------- | --------------------------- | ------------- |
| `admin_demo`    | Laura Fernández  | Administrador de SimpleRisk | Sí            |
| `analista_demo` | Martín Rodríguez | Analista de Riesgos         | No            |
| `auditor_demo`  | Sofía González   | Auditor                     | No            |

---

## 3. Usuario administrador

### `admin_demo`

**Nombre:** Laura Fernández
**Función:** Administrador de SimpleRisk
**Administrador:** Sí
**Equipo:** Information Security

El usuario administrador posee los permisos necesarios para administrar la plataforma y configurar los elementos generales de SimpleRisk.

Sus responsabilidades principales son:

* Administrar usuarios.
* Configurar permisos.
* Gestionar la configuración general de SimpleRisk.
* Supervisar la gestión de riesgos.
* Revisar y aprobar acciones de tratamiento cuando corresponda.
* Administrar la información necesaria para el funcionamiento de la herramienta.

Este usuario se utiliza como cuenta administrativa de la instalación.

---

## 4. Analista de Riesgos

### `analista_demo`

**Nombre:** Martín Rodríguez
**Función:** Analista de Riesgos
**Administrador:** No
**Equipo:** Information Security
**Responsable superior:** Laura Fernández - Administrador

### Permisos asignados

El usuario tiene acceso al módulo de **Risk Management** y cuenta con permisos relacionados con el ciclo de gestión de riesgos.

Permisos principales:

* Allow Access to "Risk Management" Menu
* Able to Submit New Risks
* Able to Modify Risk Details
* Able to Close Risks
* Able to Plan Mitigations
* Able to Accept Mitigations
* Able to Review Insignificant Risks
* Able to Review Low Risks
* Able to Review Medium Risks
* Able to Review High Risks
* Able to Review Very High Risks
* Able to Comment Risk Management

### Justificación

Los permisos asignados permiten que Martín Rodríguez desempeñe el rol de analista de riesgos, pudiendo registrar nuevos riesgos, modificar su información, evaluarlos, participar en su tratamiento y realizar seguimiento.

No posee permisos administrativos generales ni permisos relacionados con otras áreas que no forman parte de su responsabilidad.

---

## 5. Auditor

### `auditor_demo`

**Nombre:** Sofía González
**Función:** Auditor
**Administrador:** No
**Equipo:** Information Security
**Responsable superior:** Laura Fernández - Administrador

### Permisos asignados

El usuario posee permisos relacionados con auditoría y revisión de riesgos.

#### Compliance

* Allow Access to "Compliance" Menu
* Able to Comment Compliance
* Able to Initiate Audits
* Able to Modify Audits
* Able to Reopen Audits
* Able to Approve Tests

#### Risk Management

* Allow Access to "Risk Management" Menu
* Able to Review Insignificant Risks
* Able to Review Low Risks
* Able to Review Medium Risks
* Able to Review High Risks
* Able to Review Very High Risks

### Justificación

Los permisos asignados permiten que Sofía González realice tareas de auditoría y supervisión sin disponer de permisos administrativos ni de modificación directa del ciclo de vida de los riesgos.

El usuario puede revisar riesgos de todos los niveles y trabajar con auditorías y controles de cumplimiento, manteniendo una separación respecto de las funciones administrativas.

---

## 6. Separación de funciones

La configuración de usuarios busca evitar la concentración de responsabilidades en una única cuenta.

La distribución adoptada es:

**Administrador → Administración de la plataforma**

El administrador configura usuarios, permisos y elementos generales de SimpleRisk.

**Analista de Riesgos → Gestión de riesgos**

El analista registra, modifica, evalúa y trata riesgos.

**Auditor → Revisión y cumplimiento**

El auditor revisa riesgos y administra actividades relacionadas con auditorías y cumplimiento.

Esta separación permite reducir el riesgo de modificaciones no autorizadas y facilita la trazabilidad de las actividades realizadas dentro de la herramienta.

---

## 7. Criterios de seguridad

Para la documentación y entrega del trabajo se aplican los siguientes criterios:

* No se almacenan contraseñas.
* No se almacenan tokens ni claves de API.
* No se incluyen credenciales reales en el repositorio.
* Cada usuario posee permisos acordes a su función.
* Las cuentas no administrativas no poseen privilegios de administrador.
* Se utiliza el principio de mínimo privilegio.
* Se mantiene separación de funciones entre administración, análisis y auditoría.

---

## 8. Evidencia

La configuración de los usuarios fue realizada directamente en SimpleRisk.

Las capturas correspondientes a la configuración de usuarios se incorporarán posteriormente en:

`informe/capturas/`

Los nombres definitivos de las capturas serán revisados al finalizar el trabajo para asegurar que coincidan con los archivos existentes.

---

## 9. Verificación

La configuración fue verificada mediante el acceso a SimpleRisk y la revisión de los permisos asignados a cada usuario.

Como parte de las decisiones de diseño del trabajo se considera el principio de mínimo privilegio y la separación de funciones.

**Palabra de verificación del TP: girasol.**
