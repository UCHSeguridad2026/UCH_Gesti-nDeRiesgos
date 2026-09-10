# Riesgos - Gestión de Riesgos con SimpleRisk

## 1. Contexto

El escenario analizado corresponde a una clínica privada con aproximadamente 120 empleados y una atención de alrededor de 800 pacientes por día. La organización utiliza sistemas digitales para gestionar historias clínicas, información personal y médica de pacientes, datos de seguros y facturación.

Una auditoría externa identificó debilidades en la gestión de riesgos, por lo que se realizó una identificación inicial de riesgos tecnológicos y operativos, considerando principalmente los criterios de confidencialidad, integridad y disponibilidad de la información.

Se registraron siete riesgos en SimpleRisk y se definieron tratamientos orientados principalmente a la mitigación.

---

## 2. Criterio de evaluación

Para el análisis metodológico se utilizó una escala de 1 a 5 para probabilidad e impacto.

### Probabilidad

| Valor | Nivel    |
| ----- | -------- |
| 1     | Muy baja |
| 2     | Baja     |
| 3     | Media    |
| 4     | Alta     |
| 5     | Muy alta |

### Impacto

| Valor | Nivel          |
| ----- | -------------- |
| 1     | Insignificante |
| 2     | Menor          |
| 3     | Moderado       |
| 4     | Alto           |
| 5     | Crítico        |

El nivel de riesgo inherente se obtiene mediante:

**Riesgo = Probabilidad × Impacto**

Criterio utilizado:

* 1 a 4: Bajo
* 5 a 9: Medio
* 10 a 14: Alto
* 15 a 25: Muy Alto / Crítico

> Nota: estos valores corresponden a la evaluación metodológica utilizada para documentar el escenario. SimpleRisk utiliza su propia escala y método de puntuación Classic, por lo que el valor mostrado por la herramienta puede diferir del cálculo 1–5 documentado en este archivo.

---

# 3. Registro de riesgos

| ID | Riesgo                                                | Categoría                          | Prob. | Impacto | Riesgo inherente | Tratamiento | Responsable    |
| -- | ----------------------------------------------------- | ---------------------------------- | ----: | ------: | ---------------: | ----------- | -------------- |
| R1 | Acceso no autorizado a historias clínicas digitales   | Access Management                  |   4/5 |     5/5 |               20 | Mitigar     | Sofía González |
| R2 | Ransomware sobre el sistema de historias clínicas     | Technical Vulnerability Management |   4/5 |     5/5 |               20 | Mitigar     | Sofía González |
| R3 | Pérdida o corrupción de historias clínicas digitales  | Sensitive Data Management          |   3/5 |     5/5 |               15 | Mitigar     | Sofía González |
| R4 | Indisponibilidad del sistema de historias clínicas    | Environmental Resilience           |   4/5 |     5/5 |               20 | Mitigar     | Sofía González |
| R5 | Filtración de datos personales y médicos de pacientes | Sensitive Data Management          |   3/5 |     5/5 |               15 | Mitigar     | Sofía González |
| R6 | Manipulación no autorizada de datos de facturación    | Access Management                  |   3/5 |     4/5 |               12 | Mitigar     | Sofía González |
| R7 | Falla de infraestructura eléctrica y de red           | Environmental Resilience           |   3/5 |     4/5 |               12 | Mitigar     | Sofía González |

---

# 4. Detalle de los riesgos

## R1 - Acceso no autorizado a historias clínicas digitales

**Risk Mapping:** R-AC-4 - Unauthorized access
**Threat Mapping:** MT-2 - Hacking & Other Cybersecurity Crimes
**Categoría:** Access Management
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 4/5 - Alta
**Impacto:** 5/5 - Crítico
**Riesgo inherente:** 20 - Muy Alto / Crítico

### Descripción y evaluación

La clínica cuenta con aproximadamente 120 empleados y atiende alrededor de 800 pacientes por día, por lo que existe una cantidad significativa de usuarios con acceso a información clínica. Una auditoría externa identificó debilidades en la gestión de riesgos, aumentando la necesidad de fortalecer los controles de acceso.

La probabilidad se considera **4/5 (Alta)** debido a la cantidad de usuarios y a la necesidad de fortalecer los mecanismos de control y gestión de permisos.

El impacto se considera **5/5 (Crítico)** debido a que un acceso no autorizado podría exponer historias clínicas y datos personales y médicos de pacientes, generando consecuencias legales, reputacionales y pérdida de confianza.

**Nivel inherente: 4 × 5 = 20 (Muy Alto / Crítico).**

### Controles existentes

La clínica utiliza cuentas individuales y permisos de acceso para los usuarios. Estos controles requieren revisión y fortalecimiento.

### Tratamiento

**Mitigar.**

Se propone:

* Implementar autenticación multifactor para accesos sensibles.
* Aplicar el principio de mínimo privilegio.
* Revisar periódicamente los permisos.
* Revocar inmediatamente las cuentas de empleados desvinculados.
* Monitorear los registros de acceso.

**Tags:** `historias-clinicas, acceso-no-autorizado, confidencialidad`

---

## R2 - Ransomware sobre el sistema de historias clínicas

**Risk Mapping:** R-BC-4 - Information loss / corruption or system compromise due to technical attack
**Threat Mapping:** MT-2 - Hacking & Other Cybersecurity Crimes
**Categoría:** Technical Vulnerability Management
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 4/5 - Alta
**Impacto:** 5/5 - Crítico
**Riesgo inherente:** 20 - Muy Alto / Crítico

### Descripción y evaluación

Un ataque de ransomware podría cifrar o bloquear el acceso al sistema de historias clínicas digitales, impidiendo al personal médico consultar la información de los pacientes y afectando la continuidad de la atención.

La probabilidad se considera **4/5 (Alta)** porque la clínica depende de sistemas digitales para gestionar las historias clínicas y atiende aproximadamente 800 pacientes por día. Además, la auditoría externa identificó debilidades en la gestión de riesgos.

El impacto se considera **5/5 (Crítico)** debido a que un ataque de ransomware podría impedir el acceso a las historias clínicas, interrumpir la atención de los pacientes, afectar la continuidad operativa y generar pérdidas económicas y daños reputacionales.

**Nivel inherente: 4 × 5 = 20 (Muy Alto / Crítico).**

### Controles existentes

La clínica cuenta con mecanismos de respaldo de información, pero requieren revisión y fortalecimiento.

### Tratamiento

**Mitigar.**

Se propone:

* Implementar copias de seguridad periódicas.
* Mantener copias protegidas y fuera de línea.
* Implementar segmentación de red.
* Mantener los sistemas actualizados y parcheados.
* Implementar protección antimalware/EDR.
* Capacitar al personal frente al phishing.
* Establecer un plan de recuperación ante incidentes.

**Tags:** `ransomware, historias-clinicas, disponibilidad, continuidad-operativa`

---

## R3 - Pérdida o corrupción de historias clínicas digitales

**Risk Mapping:** R-BC-2 - Data loss / corruption
**Threat Mapping:** MT-7 - Utility Service Disruption
**Categoría:** Sensitive Data Management
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 3/5 - Media
**Impacto:** 5/5 - Crítico
**Riesgo inherente:** 15 - Muy Alto / Crítico

### Descripción y evaluación

Las historias clínicas digitales podrían perderse o sufrir corrupción de datos debido a fallas técnicas, errores humanos, problemas de almacenamiento o copias de seguridad insuficientes, afectando la disponibilidad y la integridad de la información de los pacientes.

La probabilidad se considera **3/5 (Media)** debido a la dependencia de la información digital y al volumen de información clínica que debe mantenerse disponible y correcta. Las debilidades identificadas por la auditoría aumentan la posibilidad de que los controles de respaldo y recuperación sean insuficientes.

El impacto se considera **5/5 (Crítico)** debido a que la pérdida o corrupción de historias clínicas podría impedir el acceso a antecedentes médicos necesarios para la atención, afectar la integridad de la información y generar consecuencias operativas, legales y reputacionales.

**Nivel inherente: 3 × 5 = 15 (Muy Alto / Crítico).**

### Controles existentes

Se dispone de mecanismos de respaldo de información, aunque requieren revisión y fortalecimiento.

### Tratamiento

**Mitigar.**

Se propone:

* Implementar copias de seguridad periódicas y verificadas.
* Mantener copias fuera de línea o inmutables.
* Realizar pruebas de restauración.
* Controlar el acceso a los respaldos.
* Documentar procedimientos de recuperación.

**Tags:** `historias-clinicas, perdida-de-datos, integridad, backups`

---

## R4 - Indisponibilidad del sistema de historias clínicas

**Risk Mapping:** R-BC-1 - Business interruption
**Threat Mapping:** MT-7 - Utility Service Disruption
**Categoría:** Environmental Resilience
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 4/5 - Alta
**Impacto:** 5/5 - Crítico
**Riesgo inherente:** 20 - Muy Alto / Crítico

### Descripción y evaluación

El sistema de historias clínicas podría quedar temporalmente indisponible debido a fallas técnicas, problemas de infraestructura, errores de configuración o interrupciones de servicios necesarios para su funcionamiento.

La probabilidad se considera **4/5 (Alta)** porque la clínica depende del sistema digital para gestionar información de aproximadamente 800 pacientes diarios. La dependencia tecnológica y las debilidades detectadas por la auditoría aumentan la posibilidad de interrupciones.

El impacto se considera **5/5 (Crítico)** debido a que la indisponibilidad podría impedir al personal médico consultar información necesaria para la atención, retrasar procedimientos y afectar significativamente la continuidad operativa.

**Nivel inherente: 4 × 5 = 20 (Muy Alto / Crítico).**

### Controles existentes

Actualmente se dispone del sistema digital para gestionar las historias clínicas, pero es necesario fortalecer los mecanismos de redundancia, monitoreo y contingencia.

### Tratamiento

**Mitigar.**

Se propone:

* Implementar redundancia de servicios críticos.
* Monitorear la disponibilidad.
* Implementar mecanismos de recuperación ante fallas.
* Implementar UPS para equipos críticos.
* Establecer procedimientos de contingencia.
* Mantener procedimientos manuales temporales para situaciones de interrupción.

**Tags:** `disponibilidad, historias-clinicas, continuidad-operativa, infraestructura`

---

## R5 - Filtración de datos personales y médicos de pacientes

**Risk Mapping:** R-EX-7 - System compromise
**Threat Mapping:** MT-2 - Hacking & Other Cybersecurity Crimes
**Categoría:** Sensitive Data Management
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 3/5 - Media
**Impacto:** 5/5 - Crítico
**Riesgo inherente:** 15 - Muy Alto / Crítico

### Descripción y evaluación

Información personal, médica y de seguros de los pacientes podría ser expuesta a personas no autorizadas mediante accesos indebidos, vulnerabilidades técnicas, errores humanos o filtraciones de información.

La probabilidad se considera **3/5 (Media)** debido al volumen de información sensible almacenada y a la cantidad de usuarios que interactúan con ella. Las debilidades identificadas por la auditoría también incrementan la exposición.

El impacto se considera **5/5 (Crítico)** debido a que la exposición de información médica y personal puede afectar gravemente la privacidad de los pacientes, generar consecuencias legales y económicas y producir daño reputacional.

**Nivel inherente: 3 × 5 = 15 (Muy Alto / Crítico).**

### Controles existentes

La clínica dispone de mecanismos de control de acceso a la información, pero requiere fortalecer los controles de protección y monitoreo.

### Tratamiento

**Mitigar.**

Se propone:

* Aplicar controles de acceso basados en mínimo privilegio.
* Cifrar información sensible.
* Implementar autenticación multifactor.
* Monitorear accesos.
* Capacitar al personal.
* Establecer procedimientos de respuesta ante incidentes.

**Tags:** `datos-personales, datos-medicos, filtracion, confidencialidad`

---

## R6 - Manipulación no autorizada de datos de facturación

**Risk Mapping:** R-AM-2 - Loss of integrity through unauthorized changes
**Threat Mapping:** MT-5 - Physical Crime
**Categoría:** Access Management
**Activo afectado:** Application
**Tecnología:** Web
**Equipo:** Information Security
**Fuente del riesgo:** PEOPLE
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 3/5 - Media
**Impacto:** 4/5 - Alto
**Riesgo inherente:** 12 - Alto

### Descripción y evaluación

Un empleado o tercero con acceso al sistema podría modificar de manera no autorizada información de facturación, cobros o datos relacionados con seguros, generando pérdidas económicas o registros incorrectos.

La probabilidad se considera **3/5 (Media)** debido a que la clínica gestiona diariamente información de facturación y seguros asociada a un volumen elevado de pacientes. La existencia de múltiples usuarios y las debilidades de gestión detectadas aumentan la posibilidad de modificaciones indebidas.

El impacto se considera **4/5 (Alto)** porque la manipulación de información de facturación podría generar pérdidas económicas, errores contables, reclamos de pacientes o aseguradoras y afectar la integridad de los registros.

**Nivel inherente: 3 × 4 = 12 (Alto).**

### Controles existentes

La clínica utiliza cuentas y permisos de acceso para gestionar la información de facturación, pero se requiere fortalecer la segregación de funciones y los controles sobre modificaciones.

### Tratamiento

**Mitigar.**

Se propone:

* Aplicar segregación de funciones.
* Utilizar permisos mínimos.
* Registrar las modificaciones.
* Realizar revisiones periódicas de operaciones de facturación.
* Implementar controles de aprobación para cambios sensibles.

**Tags:** `facturacion, fraude, integridad, control-de-acceso`

---

## R7 - Falla de infraestructura eléctrica y de red

**Risk Mapping:** R-BC-1 - Business interruption
**Threat Mapping:** MT-7 - Utility Service Disruption
**Categoría:** Environmental Resilience
**Activo afectado:** Network
**Tecnología:** Network
**Equipo:** Information Security
**Fuente del riesgo:** System
**Responsable:** Sofía González
**Responsable superior:** Laura Fernández - Administrador
**Probabilidad:** 3/5 - Media
**Impacto:** 4/5 - Alto
**Riesgo inherente:** 12 - Alto

### Descripción y evaluación

Una interrupción del suministro eléctrico o una falla de la infraestructura de red podría dejar temporalmente inaccesibles los sistemas digitales utilizados por la clínica, afectando la atención y las operaciones administrativas.

La probabilidad se considera **3/5 (Media)** porque los sistemas tecnológicos dependen de energía eléctrica y conectividad de red para funcionar. Una falla en estos servicios puede afectar simultáneamente distintos sistemas y usuarios.

El impacto se considera **4/5 (Alto)** debido a que una interrupción prolongada podría impedir el acceso a historias clínicas, sistemas de facturación y otros servicios necesarios para la atención de pacientes y la operación de la clínica.

**Nivel inherente: 3 × 4 = 12 (Alto).**

### Controles existentes

La infraestructura tecnológica depende del suministro eléctrico y de la conectividad de red. Se requiere fortalecer la redundancia y los mecanismos de continuidad.

### Tratamiento

**Mitigar.**

Se propone:

* Implementar UPS para equipos críticos.
* Implementar redundancia de conectividad.
* Monitorear la infraestructura.
* Realizar mantenimiento preventivo.
* Establecer procedimientos de contingencia.

**Tags:** `infraestructura, red, energia, disponibilidad, continuidad-operativa`

---

# 5. Tratamiento general

Los siete riesgos identificados fueron clasificados con tratamiento **Mitigar**, debido a que la clínica necesita reducir la probabilidad de ocurrencia y/o el impacto de los eventos mediante controles técnicos, organizativos y de continuidad.

Las principales líneas de tratamiento son:

* Fortalecimiento de controles de acceso.
* Autenticación multifactor.
* Principio de mínimo privilegio.
* Copias de seguridad protegidas y verificadas.
* Protección frente a ransomware.
* Redundancia de servicios críticos.
* Monitoreo de infraestructura y accesos.
* Capacitación del personal.
* Segregación de funciones.
* Procedimientos de continuidad y recuperación.

---

# 6. Relación con SimpleRisk

Los siete riesgos fueron registrados en SimpleRisk utilizando el método de puntuación **Classic**.

La herramienta permite asociar cada riesgo con:

* Categoría.
* Risk Mapping.
* Threat Mapping.
* Activos afectados.
* Tecnología.
* Equipo responsable.
* Propietario del riesgo.
* Fuente del riesgo.
* Probabilidad.
* Impacto.
* Evaluación del riesgo.
* Tratamiento y mitigaciones.
* Tags.

Las capturas de pantalla correspondientes a cada riesgo se encuentran en `informe/capturas/`.

## Capturas asociadas

* `R01_acceso_no_autorizado_historias_clinicas.png`
* `R02_ransomware_historias_clinicas.png`
* `R03_perdida_corrupcion_historias_clinicas.png`
* `R04_indisponibilidad_historias_clinicas.png`
* `R05_filtracion_datos_personales_medicos.png`
* `R06_manipulacion_facturacion.png`
* `R07_falla_infraestructura_red.png`
* `PA01_backups_recuperacion_ransomware.png`
* `PA02_mfa_revision_permisos.png`
* `PA03_redundancia_continuidad_operativa.png`

