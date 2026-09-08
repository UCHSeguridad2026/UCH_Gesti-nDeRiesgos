# Usuarios y permisos

Se crearon 3 usuarios con roles diferenciados en SimpleRisk, aplicando el principio de menor privilegio y, cuando fue posible, separación de funciones entre carga/análisis y aprobación de riesgos.

> Nota: las contraseñas no se documentan en este archivo ni en ningún otro del repositorio. Se usaron credenciales ficticias solo para el entorno de demo.

## 1. admin_demo — Administrador de seguridad

- **Email:** admin_demo@clinica-demo.local
- **Nombre:** Administrador Demo
- **Permisos:** Grant Admin (acceso total: todas las teams, todos los módulos, configuración del sistema).

Es el único usuario con acceso a Configure y con visibilidad total sobre la instalación.

## 2. analista_demo — Analista de riesgos

- **Email:** analista_demo@clinica-demo.local
- **Nombre:** Analista de Riesgos Demo
- **Permisos (Risk Management):**
  - Allow Access to "Risk Management" Menu
  - Able to Submit New Risks
  - Able to Modify Risk Details
  - Able to Plan Mitigations
  - Able to Comment Risk Management
  - Able to Add Projects
  - Able to Add Saved Risk Reports
  - Able to Review Insignificant Risks
  - Able to Review Low Risks
  - Able to Review Medium Risks
  - Able to Review High Risks
  - Able to Review Very High Risks
- **Sin permisos de:** Close Risks, Accept Mitigations, Delete/Manage Projects, Delete Saved Risk Reports, y todo lo de Governance / Compliance / Asset Management / Assessments / Artificial Intelligence.

**Justificación:** el analista es quien carga, mantiene y planifica el tratamiento de los riesgos del día a día, y además puede revisar riesgos de cualquier nivel para tener visibilidad completa del registro. Se decidió no darle permiso de cierre ni de aceptación de mitigaciones: esas decisiones quedan reservadas al administrador/dueño del riesgo, para mantener un control cruzado sobre las decisiones finales de tratamiento.

## 3. auditor_demo — Auditor

- **Email:** auditor_demo@clinica-demo.local
- **Nombre:** Auditor Demo
- **Permisos (Risk Management):**
  - Allow Access to "Risk Management" Menu
  - Able to Review Insignificant Risks
  - Able to Review Low Risks
  - Able to Review Medium Risks
  - Able to Review High Risks
  - Able to Review Very High Risks
  - Able to Comment Risk Management
- **Permisos (Compliance):**
  - Allow Access to "Compliance" Menu
  - Able to Initiate Audits
  - Able to Approve Tests
- **Sin permisos de:** cualquier acción de creación/edición/cierre sobre riesgos, tests o auditorías (Submit/Modify/Close Risks, Plan/Accept Mitigations, Edit/Delete Tests, Modify/Reopen/Delete Audits), ni de Governance / Asset Management / Assessments / Artificial Intelligence.

**Justificación:** el auditor necesita ver el estado real de los riesgos y dejar comentarios de revisión, y puede iniciar y aprobar auditorías de compliance, pero no puede modificar los riesgos ni los tests que está evaluando. Esto preserva la independencia de la auditoría: quien audita no es quien genera lo auditado.

## Resumen de segregación de funciones

| Acción | admin_demo | analista_demo | auditor_demo |
|---|---|---|---|
| Configurar el sistema | Sí | No | No |
| Cargar / modificar riesgos | Sí | Sí | No |
| Cerrar riesgos / aceptar mitigaciones | Sí | No | No |
| Revisar riesgos por nivel | Sí | Sí | Sí |
| Iniciar / aprobar auditorías de compliance | Sí | No | Sí |