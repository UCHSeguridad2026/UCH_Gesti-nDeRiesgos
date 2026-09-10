# Registro de riesgos

Este documento contiene los riesgos identificados y registrados en SimpleRisk para el escenario de la clínica privada.

---

## R01 — Ataque de ransomware al sistema de historias clínicas

| Campo | Valor |
|---|---|
| **ID** | R01 |
| **Asunto** | Ataque de ransomware al sistema de historias clínicas |
| **Categoría SimpleRisk** | Technical Vulnerability Management |
| **Clasificación** | Confidencialidad / Integridad / Disponibilidad |
| **Fuente del riesgo** | External |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Likely — 4/5 |
| **Impacto actual** | Extreme/Catastrophic — 5/5 |
| **Valoración académica** | 20 — Crítico |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

Un ataque de ransomware podría comprometer el sistema de historias clínicas digitales mediante el cifrado de servidores y estaciones de trabajo, impidiendo el acceso del personal médico a información crítica de los pacientes.

La probabilidad se considera **4/5 (Probable)** debido a la exposición a amenazas como phishing, malware y explotación de vulnerabilidades. El impacto se considera **5/5 (Catastrófico)** debido a las consecuencias que una indisponibilidad prolongada podría tener sobre la atención de pacientes.

### Controles existentes

- Antivirus tradicional.
- Firewall perimetral.
- Copias de seguridad periódicas.

### Tratamiento propuesto

- Implementar EDR.
- Implementar MFA.
- Segmentar la red.
- Fortalecer la gestión de parches.
- Mantener backups aislados e inmutables.
- Realizar pruebas periódicas de restauración.
- Capacitar al personal frente a phishing.

---

## R02 — Acceso no autorizado mediante credenciales comprometidas

| Campo | Valor |
|---|---|
| **ID** | R02 |
| **Asunto** | Acceso no autorizado mediante credenciales comprometidas |
| **Categoría SimpleRisk** | Access Management |
| **Clasificación** | Confidencialidad / Legal |
| **Fuente del riesgo** | External |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Likely — 4/5 |
| **Impacto actual** | Extreme/Catastrophic — 5/5 |
| **Valoración académica** | 20 — Crítico |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

Un atacante podría obtener las credenciales de un empleado mediante phishing, reutilización de contraseñas o ingeniería social y utilizarlas para acceder sin autorización al sistema de historias clínicas.

La probabilidad se considera **4/5** por la exposición habitual de los usuarios a intentos de robo de credenciales. El impacto se considera **5/5** debido a la sensibilidad de los datos médicos.

### Controles existentes

- Usuario y contraseña.
- Permisos de acceso.
- Firewall perimetral.

### Tratamiento propuesto

- MFA.
- Principio de mínimo privilegio.
- Políticas seguras de contraseñas.
- Bloqueo ante intentos fallidos.
- Revisión periódica de permisos.
- Monitoreo de accesos.

---

## R03 — Pérdida o corrupción de datos clínicos

| Campo | Valor |
|---|---|
| **ID** | R03 |
| **Asunto** | Pérdida o corrupción de datos clínicos |
| **Categoría SimpleRisk** | Sensitive Data Management |
| **Clasificación** | Integridad / Operativo |
| **Fuente del riesgo** | System |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Credible — 3/5 |
| **Impacto actual** | Extreme/Catastrophic — 5/5 |
| **Valoración académica** | 15 — Alto |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

La pérdida o corrupción de información podría producirse por fallas en la base de datos, errores de software, fallas de almacenamiento o acciones humanas accidentales.

### Controles existentes

- Base de datos centralizada.
- Copias de seguridad periódicas.

### Tratamiento propuesto

- Backups automatizados y aislados.
- Pruebas de restauración.
- Validación de integridad.
- Auditoría de modificaciones.
- Redundancia de almacenamiento.
- Procedimientos documentados de recuperación.

---

## R04 — Caída de la infraestructura de red de la clínica

| Campo | Valor |
|---|---|
| **ID** | R04 |
| **Asunto** | Caída de la infraestructura de red de la clínica |
| **Categoría SimpleRisk** | Environmental Resilience |
| **Clasificación** | Disponibilidad / Operativo |
| **Fuente del riesgo** | System |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Credible — 3/5 |
| **Impacto actual** | Major — 4/5 |
| **Valoración académica** | 12 — Alto |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

Una falla en switches, routers, enlaces, configuraciones o suministro eléctrico podría interrumpir la conectividad entre las estaciones de trabajo y los sistemas utilizados por la clínica.

### Controles existentes

- Equipamiento de red convencional.
- Firewall perimetral.
- Soporte técnico.

### Tratamiento propuesto

- Redundancia de equipos y enlaces.
- UPS.
- Monitoreo de infraestructura.
- Documentación de configuraciones.
- Procedimientos de recuperación.

---

## R05 — Acceso no autorizado a la base de datos clínica

| Campo | Valor |
|---|---|
| **ID** | R05 |
| **Asunto** | Acceso no autorizado a la base de datos clínica |
| **Categoría SimpleRisk** | Sensitive Data Management |
| **Clasificación** | Confidencialidad / Legal |
| **Fuente del riesgo** | External |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Credible — 3/5 |
| **Impacto actual** | Extreme/Catastrophic — 5/5 |
| **Valoración académica** | 15 — Crítico |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

Un atacante podría obtener acceso no autorizado a la base de datos mediante vulnerabilidades, configuraciones inseguras, permisos excesivos o credenciales comprometidas.

### Controles existentes

- Autenticación mediante usuario y contraseña.
- Permisos de acceso.
- Firewall perimetral.
- Copias de seguridad.

### Tratamiento propuesto

- MFA para accesos administrativos.
- Cifrado de datos.
- Mínimo privilegio.
- Revisión periódica de permisos.
- Gestión de parches.
- Monitoreo y alertas.

---

## R06 — Divulgación accidental de información clínica

| Campo | Valor |
|---|---|
| **ID** | R06 |
| **Asunto** | Divulgación accidental de información clínica |
| **Categoría SimpleRisk** | Sensitive Data Management |
| **Clasificación** | Confidencialidad / Legal |
| **Fuente del riesgo** | People |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Credible — 3/5 |
| **Impacto actual** | Major — 4/5 |
| **Valoración académica** | 12 — Alto |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

La información clínica podría ser divulgada accidentalmente debido a errores humanos, como envíos a destinatarios incorrectos, sesiones abiertas o manejo inadecuado de documentación.

### Controles existentes

- Autenticación.
- Permisos de acceso.
- Procedimientos básicos para el manejo de información.

### Tratamiento propuesto

- Capacitación periódica.
- Mínimo privilegio.
- Bloqueo automático de sesiones.
- Procedimientos seguros para compartir información.
- Revisión de permisos.
- Registro de accesos.

---

## R07 — Interrupción de servicios de un proveedor tecnológico

| Campo | Valor |
|---|---|
| **ID** | R07 |
| **Asunto** | Interrupción de servicios de un proveedor tecnológico |
| **Categoría SimpleRisk** | Third-Party Management |
| **Clasificación** | Disponibilidad / Terceros |
| **Fuente del riesgo** | External |
| **Activo afectado** | Sistema de Historias Clínicas Digitales |
| **Método de puntuación** | Classic |
| **Probabilidad actual** | Credible — 3/5 |
| **Impacto actual** | Major — 4/5 |
| **Valoración académica** | 12 — Alto |
| **Propietario** | Analista de riesgos |
| **Tratamiento** | Mitigar |

### Evaluación

Una interrupción de un proveedor tecnológico externo podría afectar servicios de conectividad, infraestructura, hosting o soporte necesarios para el funcionamiento de los sistemas clínicos.

### Controles existentes

- Contratos de servicio.
- Soporte técnico.
- Procedimientos básicos de contingencia.

### Tratamiento propuesto

- Acuerdos de nivel de servicio (SLA).
- Evaluaciones periódicas de proveedores.
- Servicios o enlaces alternativos.
- Monitoreo de disponibilidad.
- Planes de contingencia y recuperación.