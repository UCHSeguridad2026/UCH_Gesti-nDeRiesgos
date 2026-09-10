# Usuarios y Permisos

Se crearon 3 usuarios con roles diferenciados en el entorno local de SimpleRisk, aplicando el principio de menor privilegio y la separación de funciones entre la carga operativa, el análisis y la aprobación de riesgos de la clínica.

*Nota: Las contraseñas no se documentan en este archivo ni en ningún otro del repositorio por normativas de seguridad. Se utilizaron credenciales exclusivas para el entorno local, cumpliendo la política mínima de complejidad configurada en el sistema.*

### 1. juanceto01 (admin) — Administrador de Seguridad
* **Email:** admin@clinica.local
* **Nombre:** Administrador Sistema
* **Permisos:** Grant Admin (acceso total: todos los módulos, todas las áreas, configuración del sistema).
* **Justificación:** Es el único perfil con acceso al panel de "Configure" y visibilidad total sobre la instalación. Su responsabilidad principal, además del mantenimiento de la plataforma, es la de revisar y ejecutar el "Accept Mitigation" sobre los planes propuestos (ej. licencias EDR, Backup WAN), garantizando un control cruzado de los presupuestos asignados.

### 2. analista01 (Analista de Riesgos)
* **Email:** analista@clinica.local
* **Nombre:** Analista de Riesgos
* **Permisos (Risk Management):**
  * Allow Access to "Risk Management" Menu
  * Able to Submit New Risks
  * Able to Modify Risk Details
  * Able to Plan Mitigations
* **Restricciones:** Sin permisos para *Close Risks*, *Accept Mitigations*, revisión de riesgos por nivel (*Review Insignificant/Low/Medium/High/Very High*), comentarios, gestión de proyectos, ni acceso a Governance / Compliance.
* **Justificación:** El analista es el encargado operativo del día a día. Su función es identificar las vulnerabilidades de la clínica (ej. Phishing, Ransomware), cargarlas en el sistema y planificar las estrategias de mitigación ("Plan Mitigations"). Se decidió no darle permisos de revisión, cierre ni aceptación de mitigaciones para que esas evaluaciones queden reservadas a otros roles, manteniendo así el control cruzado.

### 3. auditor01 (Auditor Externo)
* **Email:** auditor@clinica.local
* **Nombre:** Auditor Externo
* **Permisos (Risk Management):**
  * Allow Access to "Risk Management" Menu
  * Able to Review Insignificant / Low / Medium / High / Very High Risks
* **Restricciones:** Sin permisos para creación, modificación, planificación, cierre o aceptación de riesgos (*Submit/Modify/Close Risks*, *Plan/Accept Mitigations*), sin comentarios, sin gestión de proyectos, y sin acceso al módulo de Compliance en esta etapa del proyecto.
* **Justificación:** Al tratarse de un auditor externo, se prioriza su total independencia respecto a la operación diaria de la clínica: su única función es revisar el estado y nivel de todos los riesgos cargados (desde Insignificante hasta Muy Alto), sin capacidad de alterar riesgos ni planes de acción, preservando así que quien audita no sea quien genera lo auditado.