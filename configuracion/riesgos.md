# Riesgos - Gestión de Riesgos con SimpleRisk

# 1. Contexto

El escenario analizado corresponde a una clínica privada con aproximadamente 120 empleados y una atención de alrededor de 800 pacientes por día. La organización utiliza sistemas digitales para gestionar historias clínicas, información personal y médica de pacientes, datos de seguros y facturación.

Una auditoría externa identificó debilidades en la gestión de riesgos, por lo que se realizó una identificación inicial de riesgos tecnológicos y operativos, considerando principalmente los criterios de confidencialidad, integridad y disponibilidad de la información.

Se registraron siete riesgos en SimpleRisk y se definieron tratamientos orientados principalmente a la mitigación.

---

# 2. Criterio de evaluación

Para el análisis metodológico se utilizó una escala de 1 a 5 para probabilidad e impacto.

### Probabilidad

| Valor | Nivel       | Descripción                                                      |
| ----- | ----------- | ---------------------------------------------------------------- |
| 1     | Raro        | El evento solo ocurriría en circunstancias excepcionales.        |
| 2     | Improbable  | Podría ocurrir, pero no se espera que suceda.                    |
| 3     | Posible     | Existe una posibilidad real de que ocurra.                       |
| 4     | Probable    | Es muy probable que ocurra en algún momento.                     |
| 5     | Casi seguro | Se espera que ocurra frecuentemente o ha ocurrido recientemente. |


### Impacto

| Valor | Nivel          | Descripción                                                                     |
| ----- | -------------- | ------------------------------------------------------------------------------- |
| 1     | Insignificante | Impacto mínimo, sin consecuencias operativas ni económicas relevantes.          |
| 2     | Menor          | Alteración leve de la operación, costo bajo.                                    |
| 3     | Moderado       | Impacto operativo y económico apreciable, recuperable.                          |
| 4     | Mayor          | Impacto significativo, pérdida de operación o datos, costo alto.                |
| 5     | Catastrófico   | Paralización total, pérdida crítica de datos, daño reputacional o legal severo. |


El nivel de riesgo inherente se obtiene mediante:

**Riesgo = Probabilidad × Impacto**

Criterio utilizado:

* 1 a 4: Bajo
* 5 a 9: Medio
* 10 a 15: Alto
* 16 a 25: Crítico

> Nota: estos valores corresponden a la evaluación metodológica utilizada para documentar el escenario. SimpleRisk utiliza su propia escala y método de puntuación Classic, por lo que el valor mostrado por la herramienta puede diferir del cálculo 1–5 documentado en este archivo.

---

# 3. Matriz de calor

La matriz de calor permite visualizar el nivel de riesgo resultante de combinar la probabilidad y el impacto de cada evento identificado.

| Prob. \\ Impacto | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| **5 - Casi seguro** | 5 - Medio | 10 - Alto | 15 - Alto | 20 - Crítico | 25 - Crítico |
| **4 - Probable** | 4 - Bajo | 8 - Medio | 12 - Alto | 16 - Crítico | 20 - Crítico |
| **3 - Posible** | 3 - Bajo | 6 - Medio | 9 - Medio | 12 - Alto | 15 - Alto |
| **2 - Improbable** | 2 - Bajo | 4 - Bajo | 6 - Medio | 8 - Medio | 10 - Alto |
| **1 - Raro** | 1 - Bajo | 2 - Bajo | 3 - Bajo | 4 - Bajo | 5 - Medio |

**Referencias:** Bajo = 1–4; Medio = 5–9; Alto = 10–15; Crítico = 16–25.

Los riesgos identificados en este trabajo se ubican en la matriz de acuerdo con los valores de probabilidad e impacto definidos en la evaluación metodológica.

---

# 4. Inventario y clasificación de activos

La identificación de activos permite determinar qué recursos de información, tecnología, infraestructura y personas podrían verse afectados por los riesgos identificados.

| ID | Activo | Tipo | Responsable | Clasificación | Criticidad |
|---|---|---|---|---|---|
| A01 | Historias clínicas digitales de pacientes | Información | Responsable de Sistemas | Restringida | Alta |
| A02 | Datos personales y de seguros de pacientes | Información | Responsable de Sistemas | Restringida | Alta |
| A03 | Sistema de gestión de historias clínicas | Software | Responsable de Sistemas | Interna | Alta |
| A04 | Sistema de facturación y gestión de cobros | Software | Administración | Confidencial | Alta |
| A05 | Servidores y equipos de infraestructura | Hardware | Responsable de Sistemas | Interna | Alta |
| A06 | Infraestructura de red y conectividad | Red | Responsable de Sistemas | Interna | Alta |
| A07 | Personal de la clínica con acceso a sistemas | Humano | Recursos Humanos / Sistemas | Interna | Alta |
| A08 | Imagen y reputación de la clínica | Imagen | Dirección | Interna | Alta |

### Criterios de clasificación

- **Información:** datos clínicos, personales, médicos y de seguros.
- **Software:** aplicaciones utilizadas para gestionar historias clínicas y facturación.
- **Hardware:** servidores y equipos necesarios para el funcionamiento de los sistemas.
- **Red:** infraestructura de conectividad utilizada por los sistemas y usuarios.
- **Humano:** personas que utilizan o administran los sistemas de información.
- **Imagen:** confianza y reputación de la organización frente a pacientes y terceros.

La clasificación de criticidad se considera **Alta** para estos activos debido a su importancia para la atención de pacientes, la continuidad operativa, el cumplimiento legal y la protección de información sensible.

---

# 5. Identificación de amenazas y vulnerabilidades

La identificación de amenazas y vulnerabilidades permite relacionar los eventos que podrían afectar a la clínica con las condiciones que podrían facilitar su ocurrencia. Se consideran tanto amenazas intencionales como fallas técnicas, errores humanos y problemas de infraestructura.

| ID | Activo relacionado | Amenaza | Vulnerabilidades o condiciones |
|---|---|---|---|
| T01 | A01, A03 | Acceso no autorizado a historias clínicas | Permisos excesivos, ausencia o cobertura insuficiente de MFA, cuentas que no se revocan oportunamente y revisiones de acceso insuficientes. |
| T02 | A01, A03 | Ransomware sobre el sistema de historias clínicas | Sistemas vulnerables o desactualizados, exposición a phishing, segmentación insuficiente y respaldos que podrían no estar adecuadamente protegidos. |
| T03 | A01, A03 | Pérdida o corrupción de historias clínicas | Fallas técnicas, errores humanos, respaldos insuficientes o no verificados y procedimientos de restauración no probados. |
| T04 | A03, A05 | Indisponibilidad del sistema de historias clínicas | Dependencia de servicios críticos, puntos únicos de falla, mantenimiento insuficiente y falta de mecanismos de contingencia adecuados. |
| T05 | A01, A02, A03 | Filtración de datos personales y médicos | Controles de acceso insuficientes, protección inadecuada de información sensible, monitoreo limitado y capacitación insuficiente del personal. |
| T06 | A04 | Manipulación no autorizada de datos de facturación | Privilegios excesivos, falta de segregación de funciones, controles de aprobación insuficientes y registro limitado de modificaciones. |
| T07 | A05, A06 | Falla de infraestructura eléctrica y de red | Dependencia de energía y conectividad, ausencia de redundancia suficiente, fallas de equipamiento y procedimientos de contingencia insuficientes. |

### Criterio utilizado

Las vulnerabilidades identificadas no se consideran necesariamente vulnerabilidades técnicas de software. El término se utiliza en sentido amplio para incluir debilidades técnicas, organizativas, físicas y de procedimiento que pueden facilitar la materialización de una amenaza.

La auditoría externa mencionada en el escenario constituye un antecedente relevante para considerar la existencia de debilidades en la gestión de riesgos y controles de la organización.

---

# 6. Registro de riesgos

| ID | Activo ID | Amenaza | Prob. | Impacto | Valor | Nivel | Justificación breve |
|---|---|---|---:|---:|---:|---|---|
| R1 | A01, A03 | Acceso no autorizado a historias clínicas | 4 | 5 | 20 | Crítico | Alta cantidad de usuarios y debilidades identificadas en la gestión de accesos. |
| R2 | A01, A03 | Ransomware sobre el sistema de historias clínicas | 4 | 5 | 20 | Crítico | Dependencia del sistema digital y posible interrupción de la atención ante un ataque. |
| R3 | A01, A03 | Pérdida o corrupción de historias clínicas | 3 | 5 | 15 | Alto | Fallas técnicas, errores humanos o respaldos insuficientes podrían afectar la integridad y disponibilidad. |
| R4 | A03, A05 | Indisponibilidad del sistema de historias clínicas | 4 | 5 | 20 | Crítico | La dependencia del sistema digital hace que una interrupción afecte directamente la continuidad operativa. |
| R5 | A01, A02, A03 | Filtración de datos personales y médicos | 3 | 5 | 15 | Alto | Se gestiona un volumen elevado de información sensible y existen debilidades de gestión identificadas. |
| R6 | A04 | Manipulación no autorizada de datos de facturación | 3 | 4 | 12 | Alto | Múltiples usuarios gestionan información de facturación y seguros, generando riesgo de modificaciones indebidas. |
| R7 | A05, A06 | Falla de infraestructura eléctrica y de red | 3 | 4 | 12 | Alto | Los sistemas dependen de energía y conectividad; una falla puede afectar simultáneamente múltiples servicios. |

---

# 7. Detalle de los riesgos

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
**Probabilidad:** 4/5 - Probable
**Impacto:** 5/5 - Catastrófico
**Riesgo inherente:** 20 - Crítico

### Descripción y evaluación

La clínica cuenta con aproximadamente 120 empleados y atiende alrededor de 800 pacientes por día, por lo que existe una cantidad significativa de usuarios con acceso a información clínica. Una auditoría externa identificó debilidades en la gestión de riesgos, aumentando la necesidad de fortalecer los controles de acceso.

La probabilidad se considera **4/5 (Probable)** debido a la cantidad de usuarios y a la necesidad de fortalecer los mecanismos de control y gestión de permisos.

El impacto se considera **5/5 (Crítico)** debido a que un acceso no autorizado podría exponer historias clínicas y datos personales y médicos de pacientes, generando consecuencias legales, reputacionales y pérdida de confianza.

**Nivel inherente: 4 × 5 = 20 (Crítico).**

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
**Probabilidad:** 4/5 - Probable
**Impacto:** 5/5 - Catastrófico
**Riesgo inherente:** 20 - Crítico

### Descripción y evaluación

Un ataque de ransomware podría cifrar o bloquear el acceso al sistema de historias clínicas digitales, impidiendo al personal médico consultar la información de los pacientes y afectando la continuidad de la atención.

La probabilidad se considera **4/5 (Probable)** porque la clínica depende de sistemas digitales para gestionar las historias clínicas y atiende aproximadamente 800 pacientes por día. Además, la auditoría externa identificó debilidades en la gestión de riesgos.

El impacto se considera **5/5 (Crítico)** debido a que un ataque de ransomware podría impedir el acceso a las historias clínicas, interrumpir la atención de los pacientes, afectar la continuidad operativa y generar pérdidas económicas y daños reputacionales.

**Nivel inherente: 4 × 5 = 20 (Crítico).**

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
**Probabilidad:** 3/5 - Posible
**Impacto:** 5/5 - Catastrófico
**Riesgo inherente:** 15 - Alto

### Descripción y evaluación

Las historias clínicas digitales podrían perderse o sufrir corrupción de datos debido a fallas técnicas, errores humanos, problemas de almacenamiento o copias de seguridad insuficientes, afectando la disponibilidad y la integridad de la información de los pacientes.

La probabilidad se considera **3/5 (Posible)** debido a la dependencia de la información digital y al volumen de información clínica que debe mantenerse disponible y correcta. Las debilidades identificadas por la auditoría aumentan la posibilidad de que los controles de respaldo y recuperación sean insuficientes.

El impacto se considera **5/5 (Crítico)** debido a que la pérdida o corrupción de historias clínicas podría impedir el acceso a antecedentes médicos necesarios para la atención, afectar la integridad de la información y generar consecuencias operativas, legales y reputacionales.

**Nivel inherente: 3 × 5 = 15 (Alto).**

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
**Probabilidad:** 4/5 - Probable
**Impacto:** 5/5 - Catastrófico
**Riesgo inherente:** 20 - Crítico

### Descripción y evaluación

El sistema de historias clínicas podría quedar temporalmente indisponible debido a fallas técnicas, problemas de infraestructura, errores de configuración o interrupciones de servicios necesarios para su funcionamiento.

La probabilidad se considera **4/5 (Probable)** porque la clínica depende del sistema digital para gestionar información de aproximadamente 800 pacientes diarios. La dependencia tecnológica y las debilidades detectadas por la auditoría aumentan la posibilidad de interrupciones.

El impacto se considera **5/5 (Crítico)** debido a que la indisponibilidad podría impedir al personal médico consultar información necesaria para la atención, retrasar procedimientos y afectar significativamente la continuidad operativa.

**Nivel inherente: 4 × 5 = 20 (Crítico).**

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
**Probabilidad:** 3/5 - Posible
**Impacto:** 5/5 - Catastrófico
**Riesgo inherente:** 15 - Alto

### Descripción y evaluación

Información personal, médica y de seguros de los pacientes podría ser expuesta a personas no autorizadas mediante accesos indebidos, vulnerabilidades técnicas, errores humanos o filtraciones de información.

La probabilidad se considera **3/5 (Posible)** debido al volumen de información sensible almacenada y a la cantidad de usuarios que interactúan con ella. Las debilidades identificadas por la auditoría también incrementan la exposición.

El impacto se considera **5/5 (Crítico)** debido a que la exposición de información médica y personal puede afectar gravemente la privacidad de los pacientes, generar consecuencias legales y económicas y producir daño reputacional.

**Nivel inherente: 3 × 5 = 15 (Alto).**

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
**Probabilidad:** 3/5 - Posible
**Impacto:** 4/5 - Mayor
**Riesgo inherente:** 12 - Alto

### Descripción y evaluación

Un empleado o tercero con acceso al sistema podría modificar de manera no autorizada información de facturación, cobros o datos relacionados con seguros, generando pérdidas económicas o registros incorrectos.

La probabilidad se considera **3/5 (Posible)** debido a que la clínica gestiona diariamente información de facturación y seguros asociada a un volumen elevado de pacientes. La existencia de múltiples usuarios y las debilidades de gestión detectadas aumentan la posibilidad de modificaciones indebidas.

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
**Probabilidad:** 3/5 - Posible
**Impacto:** 4/5 - Mayor
**Riesgo inherente:** 12 - Alto

### Descripción y evaluación

Una interrupción del suministro eléctrico o una falla de la infraestructura de red podría dejar temporalmente inaccesibles los sistemas digitales utilizados por la clínica, afectando la atención y las operaciones administrativas.

La probabilidad se considera **3/5 (Posible)** porque los sistemas tecnológicos dependen de energía eléctrica y conectividad de red para funcionar. Una falla en estos servicios puede afectar simultáneamente distintos sistemas y usuarios.

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

# 8. Tratamiento de riesgos y riesgo residual

El tratamiento definido para los siete riesgos es **Mitigar**, debido a que se considera necesario reducir la probabilidad de ocurrencia mediante controles técnicos, físicos y administrativos. El riesgo residual representa la exposición estimada luego de implementar las salvaguardas propuestas.

| ID | Estrategia | Salvaguardas principales | Tipo de salvaguarda | Prob. residual | Imp. residual | Valor residual | Nivel residual |
|---|---|---|---|---:|---:|---:|---|
| R1 | Mitigar | MFA, mínimo privilegio, revisión periódica de permisos, baja inmediata de cuentas y monitoreo de accesos. | Técnica / Administrativa | 2 | 5 | 10 | Alto |
| R2 | Mitigar | Backups offline o inmutables, segmentación de red, actualización de sistemas, EDR, capacitación y recuperación ante incidentes. | Técnica / Administrativa | 2 | 5 | 10 | Alto |
| R3 | Mitigar | Backups periódicos verificados, copias offline o inmutables, pruebas de restauración y control de acceso a respaldos. | Técnica / Administrativa | 2 | 5 | 10 | Alto |
| R4 | Mitigar | Redundancia de servicios, monitoreo, UPS, mecanismos de recuperación y procedimientos de contingencia. | Técnica / Física / Administrativa | 2 | 4 | 8 | Medio |
| R5 | Mitigar | Mínimo privilegio, cifrado, MFA, monitoreo de accesos, capacitación y respuesta ante incidentes. | Técnica / Administrativa | 2 | 5 | 10 | Alto |
| R6 | Mitigar | Segregación de funciones, mínimo privilegio, registro de modificaciones, revisiones periódicas y aprobación de cambios sensibles. | Técnica / Administrativa | 2 | 4 | 8 | Medio |
| R7 | Mitigar | UPS, redundancia de conectividad, monitoreo de infraestructura, mantenimiento preventivo y procedimientos de contingencia. | Técnica / Física / Administrativa | 2 | 4 | 8 | Medio |

### Justificación del riesgo residual

Los valores residuales suponen que las salvaguardas propuestas se encuentran correctamente implementadas y operativas. La reducción se concentra principalmente en la **probabilidad**, debido a que los controles preventivos y de detección disminuyen la posibilidad de ocurrencia.

En los riesgos que afectan directamente a historias clínicas y datos personales, el impacto residual permanece elevado debido a la naturaleza sensible de la información y a las posibles consecuencias legales, operativas y reputacionales ante un incidente.

Los valores residuales deberán ser revisados periódicamente, especialmente cuando se produzcan cambios en la infraestructura, los sistemas, los procesos o las amenazas existentes.

---

# 9. Resumen de resultados

La evaluación metodológica de los siete riesgos identificados presenta la siguiente distribución:

| Nivel de riesgo | Cantidad | Porcentaje |
|---|---:|---:|
| Crítico | 3 | 42,86 % |
| Alto | 4 | 57,14 % |
| Medio | 0 | 0 % |
| Bajo | 0 | 0 % |
| **Total** | **7** | **100 %** |

El **100 % de los riesgos identificados se encuentra en nivel Alto o Crítico**, por lo que requieren tratamiento y seguimiento prioritario.

Los riesgos críticos corresponden al acceso no autorizado a historias clínicas, ransomware e indisponibilidad del sistema de historias clínicas. Los riesgos altos corresponden a pérdida o corrupción de historias clínicas, filtración de datos personales y médicos, manipulación no autorizada de datos de facturación y fallas de infraestructura eléctrica y de red.

Esta distribución refleja que la continuidad operativa, la confidencialidad de la información clínica y la integridad de los datos constituyen las principales áreas de exposición de la organización.

---

# 10. Relación con SimpleRisk

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

### Riesgos registrados en SimpleRisk

#### R01 - Acceso no autorizado a historias clínicas digitales
- `15-R01_acceso_no_autorizado_historias_clinicas.png`
- `16-R01_acceso_no_autorizado_historias_clinicas.png`
- `17-R01_acceso_no_autorizado_historias_clinicas.png`
- `18R01_acceso_no_autorizado_historias_clinicaspng`

#### R02 - Ransomware sobre el sistema de historias clínicas
- `19-R02_ransomware_historias_clinicas.png`
- `20-R02_ransomware_historias_clinicas.png`
- `21-R02_ransomware_historias_clinicas.png`
- `22-R02_ransomware_historias_clinicas.png`

#### R03 - Pérdida o corrupción de historias clínicas digitales
- `23-R03_perdida_corrupcion_historias_clinicas.png`
- `24-R03_perdida_corrupcion_historias_clinicas.png`
- `25-R03_perdida_corrupcion_historias_clinicas.png`
- `26-R03_perdida_corrupcion_historias_clinicas.png`

#### R04 - Indisponibilidad del sistema de historias clínicas
- `27-R04_indisponibilidad_historias_clinicas.png`
- `28-R04_indisponibilidad_historias_clinicas.png`
- `29-R04_indisponibilidad_historias_clinicas.png`
- `30-R04_indisponibilidad_historias_clinicas.png`

#### R05 - Filtración de datos personales y médicos
- `R05_filtracion_datos_personales_medicos_01.png`
- `R05_filtracion_datos_personales_medicos_02.png`
- `R05_filtracion_datos_personales_medicos_03.png`

#### R06 - Manipulación no autorizada de datos de facturación
- `R06_manipulacion_facturacion_01.png`
- `R06_manipulacion_facturacion_02.png`
- `R06_manipulacion_facturacion_03.png`

#### R07 - Falla de infraestructura eléctrica y de red
- `R07_falla_infraestructura_red_resumen.png`
- `R07_falla_infraestructura_red_detalle.png`
- `R07_falla_infraestructura_red_evaluacion.png`

### Planes de mitigación

- `PA01_backups_recuperacion_ransomware.png`
- `PA02_mfa_revision_permisos.png`
- `PA02_mfa_revision_permisos_configuracion.png`
- `PM03_redundancia_continuidad_operativa.png`


# 11. Conclusiones y Recomendaciones

El análisis realizado para la clínica permitió identificar siete riesgos relevantes asociados principalmente con la confidencialidad, integridad y disponibilidad de la información y de los servicios críticos. Los resultados muestran que tres riesgos se encuentran en nivel Crítico y cuatro en nivel Alto, por lo que no se identificaron riesgos que puedan ser considerados Bajo o Medio dentro del escenario analizado.

Los riesgos de mayor prioridad están relacionados con el acceso no autorizado a historias clínicas, los ataques de ransomware y la indisponibilidad del sistema de historias clínicas. Estos eventos podrían afectar directamente la atención de los pacientes, comprometer información sensible y generar consecuencias operativas, legales y reputacionales para la organización.

Como estrategia general se seleccionó **Mitigar**, ya que los riesgos identificados pueden reducirse mediante la implementación y fortalecimiento de controles técnicos, físicos y administrativos. Entre las principales medidas recomendadas se encuentran la autenticación multifactor, el principio de mínimo privilegio, las revisiones periódicas de permisos, la realización de copias de seguridad protegidas y verificadas, la redundancia de servicios críticos, el monitoreo de infraestructura y la definición de procedimientos de continuidad y recuperación.

Se recomienda priorizar inicialmente las medidas asociadas a los riesgos críticos y establecer responsables y fechas de seguimiento para verificar su implementación. Asimismo, el análisis de riesgos debería actualizarse periódicamente y ante cambios significativos en los sistemas, procesos, infraestructura o amenazas que afecten a la clínica.

Finalmente, la utilización de SimpleRisk permite centralizar el registro, evaluación y tratamiento de los riesgos, facilitando su seguimiento y proporcionando una base para mejorar progresivamente la gestión de riesgos de seguridad de la información.


# 12. Declaración de Buenas Prácticas

## Compromiso profesional

Como estudiante de Seguridad Aplicada a Sistemas de Información, declaro que el presente análisis de riesgos fue elaborado aplicando las buenas prácticas de la disciplina, con criterio ético, fundamentos técnicos y respetando el marco normativo vigente.

Asimismo, se procuró proteger la información sensible utilizada durante el desarrollo del trabajo, evitando incluir contraseñas, tokens, credenciales u otros datos que puedan comprometer la seguridad del entorno.

# 13. Planes de acción y mitigación

Para los riesgos considerados prioritarios se definieron tres planes de acción en SimpleRisk. Los planes fueron orientados principalmente a reducir la probabilidad de ocurrencia y fortalecer la capacidad de recuperación de la clínica.

| Plan | Riesgo asociado | Acción principal | Responsable | Fecha límite | Tratamiento | Presupuesto | Estado inicial |
|---|---|---|---|---|---|---|---|
| Mitigation 1 | R02 - Ransomware sobre el sistema de historias clínicas | Fortalecer la estrategia de backups y recuperación | Sofía González | 31/10/2026 | Mitigar | $0 - $100.000 | 0% |
| Mitigation 2 | R01 - Acceso no autorizado a historias clínicas digitales | Implementar MFA y revisar permisos | Sofía González | 30/11/2026 | Mitigar | $0 - $100.000 | 0% |
| Mitigation 3 | R04 - Indisponibilidad del sistema de historias clínicas | Implementar redundancia y fortalecer la continuidad operativa | Sofía González | 31/12/2026 | Mitigar | $100.001 - $200.000 | 0% |

Los tres planes fueron aceptados en SimpleRisk por la responsable superior y quedaron registrados para su posterior seguimiento.

Las medidas fueron priorizadas considerando que R01, R02 y R04 presentan nivel de riesgo inherente **Crítico** según la matriz de Probabilidad × Impacto utilizada en este trabajo.

# 14. Fuentes y Referencias

- NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments.
- SimpleRisk - Documentación oficial de la API REST v2.
- SimpleRisk - Documentación oficial sobre autenticación y API Keys.
- SimpleRisk - Documentación oficial sobre integraciones mediante API.
- Consigna del Trabajo Práctico: Gestión de Riesgos con SimpleRisk, Seguridad de Sistemas, 2026.


