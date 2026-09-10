# Registro de riesgos

## Riesgo de prueba — PRUEBA-001

| Campo                | Valor                                                                    |
| -------------------- | ------------------------------------------------------------------------ |
| Asunto               | Acceso no autorizado a historias clínicas electrónicas                   |
| Categoría            | Sensitive Data Management                                                |
| Activo afectado      | Historias clínicas electrónicas                                          |
| Método de puntuación | Classic                                                                  |
| Probabilidad actual  | Credible                                                                 |
| Impacto actual       | Major                                                                    |
| Propietario          | analista_riesgos                                                         |
| Propósito            | Validar el registro de riesgos y la configuración inicial de SimpleRisk. |

### Evaluación

Un empleado podría consultar historias clínicas de pacientes sin una necesidad asistencial o administrativa válida. Esto comprometería la confidencialidad de datos médicos sensibles y podría ocasionar consecuencias legales, pérdida de confianza y daño reputacional para la clínica.

### Nota

Este registro corresponde únicamente a la prueba inicial de funcionamiento de SimpleRisk. Los siete riesgos que integran el análisis formal se documentan a continuación.

### Evidencia

`../informe/capturas/04-riesgo-prueba.png`

---

# Registro inicial de riesgos — Clínica privada

## Criterio de evaluación

Se utiliza el método **Classic** de SimpleRisk con una escala de 1 a 5.

El valor de riesgo se calcula mediante:

`Probabilidad × Impacto`

Para este análisis se utilizan los siguientes rangos:

| Valor | Nivel   |
| ----: | ------- |
|   1–4 | Bajo    |
|   5–9 | Medio   |
| 10–15 | Alto    |
| 16–25 | Crítico |

Los controles existentes y algunos supuestos sobre la infraestructura se consideran **controles iniciales asumidos a partir del escenario de la consigna**. En una evaluación real deberían validarse con las áreas responsables de la clínica.

La evaluación de probabilidad e impacto representa una **valoración inicial académica**. El objetivo es establecer una línea base para priorizar el tratamiento de los riesgos.

---

# Resumen

| ID   | Riesgo                                               | Categoría                          | Fuente   |  P |  I | Valor | Nivel   | Tratamiento | Propietario                                           |
| ---- | ---------------------------------------------------- | ---------------------------------- | -------- | -: | -: | ----: | ------- | ----------- | ----------------------------------------------------- |
| R-01 | Ransomware sobre sistemas de historias clínicas      | Technical Vulnerability Management | External |  4 |  5 |    20 | Crítico | Mitigar     | Responsable de Seguridad de la Información            |
| R-02 | Acceso no autorizado a historias clínicas            | Access Management                  | People   |  4 |  5 |    20 | Crítico | Mitigar     | Responsable de Seguridad de la Información            |
| R-03 | Indisponibilidad del sistema de historias clínicas   | Monitoring                         | System   |  3 |  5 |    15 | Alto    | Mitigar     | Director de Sistemas / Responsable de Infraestructura |
| R-04 | Phishing y robo de credenciales de empleados         | Access Management                  | External |  4 |  4 |    16 | Crítico | Mitigar     | Responsable de Seguridad de la Información            |
| R-05 | Fuga de información de pacientes y obras sociales    | Sensitive Data Management          | People   |  3 |  5 |    15 | Alto    | Mitigar     | Responsable de Seguridad de la Información            |
| R-06 | Alteración no autorizada de información clínica      | Access Management                  | People   |  3 |  5 |    15 | Alto    | Mitigar     | Director Médico                                       |
| R-07 | Incendio o inundación de infraestructura tecnológica | Environmental Resilience           | External |  2 |  5 |    10 | Alto    | Mitigar     | Responsable de Infraestructura                        |

---

# R-01 — Ransomware sobre sistemas de historias clínicas

| Campo                   | Valor                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| **ID**                  | R-01                                                                                                   |
| **Categoría**           | Technical Vulnerability Management                                                                     |
| **Fuente del riesgo**   | External                                                                                               |
| **Activos afectados**   | Sistema de historias clínicas digitales; información clínica de pacientes; infraestructura tecnológica |
| **Probabilidad actual** | 4 — Likely                                                                                             |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                               |
| **Valor de riesgo**     | 20                                                                                                     |
| **Nivel**               | Crítico                                                                                                |
| **Tratamiento**         | Mitigar                                                                                                |
| **Propietario**         | Responsable de Seguridad de la Información                                                             |

### Evaluación

Existe el riesgo de que un ataque de ransomware afecte los sistemas utilizados para almacenar y consultar las historias clínicas digitales de la clínica. El atacante podría cifrar archivos o impedir el acceso a los sistemas, afectando la continuidad de la atención médica y de los procesos administrativos.

### Justificación de probabilidad

**4/5 — Likely (Alta).**

La probabilidad se considera alta debido a la elevada dependencia de la clínica de los sistemas digitales, la existencia de aproximadamente 120 empleados y la posibilidad de ingreso de malware mediante phishing, explotación de vulnerabilidades o compromiso de credenciales.

No se asigna el valor máximo porque no existe certeza de ocurrencia frecuente.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

La indisponibilidad de las historias clínicas podría afectar directamente la atención de aproximadamente 800 pacientes diarios. También podría generar interrupciones administrativas, pérdida de productividad, dificultades para acceder a antecedentes médicos y consecuencias económicas y reputacionales.

### Controles existentes asumidos

* Protección básica de endpoints.
* Copias de seguridad.
* Mecanismos de autenticación.
* Infraestructura tecnológica para soportar los sistemas.

Estos controles deben ser validados durante una evaluación real.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Implementar copias de seguridad offline o inmutables.
* Implementar MFA.
* Mantener sistemas y aplicaciones actualizados.
* Implementar segmentación de red.
* Fortalecer la protección de endpoints.
* Realizar capacitaciones contra phishing.
* Probar periódicamente los procedimientos de recuperación.

---

# R-02 — Acceso no autorizado a historias clínicas

| Campo                   | Valor                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------------- |
| **ID**                  | R-02                                                                                    |
| **Categoría**           | Access Management                                                                       |
| **Fuente del riesgo**   | People                                                                                  |
| **Activos afectados**   | Sistema de historias clínicas digitales; historias clínicas; datos personales y médicos |
| **Probabilidad actual** | 4 — Likely                                                                              |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                |
| **Valor de riesgo**     | 20                                                                                      |
| **Nivel**               | Crítico                                                                                 |
| **Tratamiento**         | Mitigar                                                                                 |
| **Propietario**         | Responsable de Seguridad de la Información                                              |

### Evaluación

Existe el riesgo de que un empleado, contratista o atacante que obtenga credenciales válidas acceda a historias clínicas sin autorización o consulte información que no necesita para desempeñar sus funciones.

### Justificación de probabilidad

**4/5 — Likely (Alta).**

La clínica cuenta con aproximadamente 120 empleados y múltiples usuarios que necesitan acceder a información para realizar sus tareas. Una administración inadecuada de permisos o el compromiso de credenciales podría facilitar accesos indebidos.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

Las historias clínicas contienen información altamente sensible. Un acceso no autorizado podría producir una violación de privacidad, consecuencias legales y regulatorias, pérdida de confianza de los pacientes y daño reputacional.

### Controles existentes

* Usuarios individuales.
* Roles y permisos de acceso.
* Autenticación mediante credenciales.
* Administración de usuarios.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Implementar autenticación multifactor.
* Aplicar el principio de mínimo privilegio.
* Revisar periódicamente los permisos.
* Eliminar cuentas de empleados desvinculados.
* Mantener cuentas individuales.
* Monitorear los accesos a historias clínicas.

---

# R-03 — Indisponibilidad del sistema de historias clínicas

| Campo                   | Valor                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| **ID**                  | R-03                                                                                                |
| **Categoría**           | Monitoring                                                                                          |
| **Fuente del riesgo**   | System                                                                                              |
| **Activos afectados**   | Sistema de historias clínicas digitales; servidores; infraestructura de almacenamiento; red interna |
| **Probabilidad actual** | 3 — Credible                                                                                        |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                            |
| **Valor de riesgo**     | 15                                                                                                  |
| **Nivel**               | Alto                                                                                                |
| **Tratamiento**         | Mitigar                                                                                             |
| **Propietario**         | Director de Sistemas / Responsable de Infraestructura                                               |

### Evaluación

Existe el riesgo de que una falla de infraestructura, software, almacenamiento o algún servicio dependiente provoque la indisponibilidad temporal del sistema de historias clínicas.

### Justificación de probabilidad

**3/5 — Credible (Media).**

Los sistemas informáticos pueden experimentar fallas de hardware, software, almacenamiento o conectividad. La probabilidad se considera media porque no se dispone de evidencia que permita asumir una frecuencia elevada de incidentes.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

La clínica atiende aproximadamente 800 pacientes diariamente. Una interrupción prolongada podría afectar la atención, generar demoras y obligar al personal a utilizar procedimientos manuales.

### Controles existentes

* Procedimientos básicos de recuperación.
* Infraestructura tecnológica para soportar los sistemas.
* Copias de seguridad.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Implementar monitoreo de infraestructura.
* Incorporar redundancia en componentes críticos.
* Definir procedimientos formales de contingencia.
* Realizar pruebas periódicas de recuperación.
* Establecer objetivos de recuperación RTO/RPO.

---

# R-04 — Phishing y robo de credenciales de empleados

| Campo                   | Valor                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| **ID**                  | R-04                                                                                      |
| **Categoría**           | Access Management                                                                         |
| **Fuente del riesgo**   | External                                                                                  |
| **Activos afectados**   | Cuentas de usuarios; sistemas clínicos; sistemas administrativos; sistemas de facturación |
| **Probabilidad actual** | 4 — Likely                                                                                |
| **Impacto actual**      | 4 — Major                                                                                 |
| **Valor de riesgo**     | 16                                                                                        |
| **Nivel**               | Crítico                                                                                   |
| **Tratamiento**         | Mitigar                                                                                   |
| **Propietario**         | Responsable de Seguridad de la Información                                                |

### Evaluación

Existe el riesgo de que un atacante externo utilice correos electrónicos fraudulentos u otras técnicas de ingeniería social para obtener credenciales de empleados o instalar software malicioso.

### Justificación de probabilidad

**4/5 — Likely (Alta).**

La cantidad de empleados incrementa la superficie de exposición a campañas de phishing. Además, una única cuenta comprometida podría ser utilizada como punto de entrada hacia otros sistemas.

### Justificación de impacto

**4/5 — Major (Mayor).**

El compromiso de credenciales podría permitir el acceso no autorizado a información sensible y sistemas internos, además de facilitar ataques posteriores como ransomware.

### Controles existentes

* Correo electrónico institucional.
* Credenciales individuales.
* Capacitación básica del personal.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Implementar capacitación periódica.
* Realizar simulaciones de phishing.
* Implementar MFA.
* Fortalecer filtros antispam y antiphishing.
* Establecer mecanismos de reporte de correos sospechosos.

---

# R-05 — Fuga de información de pacientes y obras sociales

| Campo                   | Valor                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **ID**                  | R-05                                                                                                              |
| **Categoría**           | Sensitive Data Management                                                                                         |
| **Fuente del riesgo**   | People                                                                                                            |
| **Activos afectados**   | Base de datos de pacientes y obras sociales; información médica; información personal; información de facturación |
| **Probabilidad actual** | 3 — Credible                                                                                                      |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                                          |
| **Valor de riesgo**     | 15                                                                                                                |
| **Nivel**               | Alto                                                                                                              |
| **Tratamiento**         | Mitigar                                                                                                           |
| **Propietario**         | Responsable de Seguridad de la Información                                                                        |

### Evaluación

Existe el riesgo de que información médica, datos personales, información de obras sociales o datos relacionados con facturación sean divulgados, extraídos o expuestos de manera accidental o intencional.

### Justificación de probabilidad

**3/5 — Credible (Media).**

La clínica posee múltiples usuarios y procesos que requieren manipular información sensible. Esto genera posibilidades de errores humanos, uso indebido de información o divulgación accidental.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

La exposición de información médica y personal podría producir consecuencias legales, regulatorias, económicas y reputacionales importantes, además de afectar directamente la privacidad de los pacientes.

### Controles existentes

* Control de acceso mediante usuarios y permisos.
* Almacenamiento centralizado de la información.
* Procedimientos internos para manejo de información.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Clasificar la información según sensibilidad.
* Aplicar controles de acceso.
* Cifrar información sensible.
* Monitorear accesos y transferencias.
* Implementar medidas de prevención de fuga de información.
* Capacitar al personal sobre protección de datos.

---

# R-06 — Alteración no autorizada de información clínica

| Campo                   | Valor                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| **ID**                  | R-06                                                                                                    |
| **Categoría**           | Access Management                                                                                       |
| **Fuente del riesgo**   | People                                                                                                  |
| **Activos afectados**   | Sistema de historias clínicas digitales; historias clínicas; información de diagnósticos y tratamientos |
| **Probabilidad actual** | 3 — Credible                                                                                            |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                                |
| **Valor de riesgo**     | 15                                                                                                      |
| **Nivel**               | Alto                                                                                                    |
| **Tratamiento**         | Mitigar                                                                                                 |
| **Propietario**         | Director Médico                                                                                         |

### Evaluación

Existe el riesgo de que un usuario autorizado abuse de sus permisos o que un atacante que haya comprometido una cuenta modifique información contenida en las historias clínicas.

### Justificación de probabilidad

**3/5 — Credible (Media).**

Para modificar información es necesario obtener acceso al sistema, por lo que se considera menos probable que un intento genérico de phishing. Sin embargo, la cantidad de usuarios y la sensibilidad de la información justifican mantener una probabilidad media.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

La alteración de diagnósticos, tratamientos, antecedentes u otros datos clínicos podría afectar la toma de decisiones de los profesionales y generar consecuencias sobre la atención de los pacientes.

### Controles existentes

* Usuarios individuales.
* Roles y permisos.
* Control de acceso al sistema.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Aplicar mínimo privilegio.
* Implementar separación de funciones.
* Mantener registros de auditoría.
* Registrar las modificaciones realizadas sobre historias clínicas.
* Revisar periódicamente los permisos.
* Implementar mecanismos de detección de modificaciones anómalas.

---

# R-07 — Incendio o inundación de infraestructura tecnológica

| Campo                   | Valor                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| **ID**                  | R-07                                                                                         |
| **Categoría**           | Environmental Resilience                                                                     |
| **Fuente del riesgo**   | External                                                                                     |
| **Activos afectados**   | Infraestructura de servidores y almacenamiento; equipamiento de red; sistemas de información |
| **Probabilidad actual** | 2 — Unlikely                                                                                 |
| **Impacto actual**      | 5 — Extreme/Catastrophic                                                                     |
| **Valor de riesgo**     | 10                                                                                           |
| **Nivel**               | Alto                                                                                         |
| **Tratamiento**         | Mitigar                                                                                      |
| **Propietario**         | Responsable de Infraestructura                                                               |

### Evaluación

Existe el riesgo de que un incendio, pérdida de agua o inundación afecte físicamente los servidores, sistemas de almacenamiento y equipamiento de red utilizado por la clínica.

### Justificación de probabilidad

**2/5 — Unlikely (Baja).**

Los eventos de incendio o inundación son menos frecuentes que las amenazas informáticas consideradas en este registro. Sin embargo, la posibilidad no es inexistente y debe ser contemplada debido a las consecuencias potenciales sobre la infraestructura crítica.

### Justificación de impacto

**5/5 — Extreme/Catastrophic (Extremo/Catastrófico).**

La destrucción o indisponibilidad de infraestructura tecnológica podría provocar una interrupción significativa de los sistemas clínicos y administrativos. Si las copias de seguridad también fueran afectadas, podría producirse una pérdida importante de información.

### Controles existentes

* Protección física básica de los equipos.
* Copias de seguridad.
* Infraestructura eléctrica de la organización.

### Tratamiento propuesto

**Mitigar.**

Se propone:

* Mantener copias de seguridad fuera del sitio.
* Implementar sensores de humo, temperatura y agua.
* Contar con mecanismos adecuados de protección contra incendios.
* Evaluar periódicamente las instalaciones.
* Ubicar los equipos críticos en áreas protegidas.
* Contar con infraestructura alternativa para recuperación.

---

# Planes de acción

## PA-01 — Implementación de estrategia de backups resilientes contra ransomware

| Campo                    | Valor                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Riesgo asociado**      | R-01 — Ransomware sobre sistemas de historias clínicas                                                                                                                                                                                                                                                                                                            |
| **Título**               | Implementación de estrategia de backups resilientes contra ransomware                                                                                                                                                                                                                                                                                             |
| **Descripción**          | Implementar una estrategia de copias de seguridad que incluya respaldos periódicos de los sistemas de historias clínicas, almacenamiento separado de la infraestructura productiva y al menos una copia offline o inmutable. Se realizarán pruebas periódicas de restauración para verificar que los respaldos puedan utilizarse ante un incidente de ransomware. |
| **Fecha de vencimiento** | 30/11/2026                                                                                                                                                                                                                                                                                                                                                        |
| **Responsable**          | Director de Sistemas / Responsable de Infraestructura                                                                                                                                                                                                                                                                                                             |
| **Presupuesto estimado** | USD 8.000                                                                                                                                                                                                                                                                                                                                                         |
| **Estado inicial**       | Not Started                                                                                                                                                                                                                                                                                                                                                       |

---

## PA-02 — Implementación de MFA para sistemas críticos

| Campo                    | Valor                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Riesgo asociado**      | R-02 — Acceso no autorizado a historias clínicas                                                                                                                                                                                                                                                                                                                  |
| **Título**               | Implementación de MFA para sistemas críticos                                                                                                                                                                                                                                                                                                                      |
| **Descripción**          | Implementar autenticación multifactor para el acceso a los sistemas que contienen historias clínicas y otra información sensible. La medida deberá aplicarse prioritariamente a cuentas administrativas y usuarios con acceso a información clínica. También se deberá establecer un procedimiento para altas, bajas y recuperación de factores de autenticación. |
| **Fecha de vencimiento** | 31/10/2026                                                                                                                                                                                                                                                                                                                                                        |
| **Responsable**          | Responsable de Seguridad de la Información                                                                                                                                                                                                                                                                                                                        |
| **Presupuesto estimado** | USD 4.000                                                                                                                                                                                                                                                                                                                                                         |
| **Estado inicial**       | Not Started                                                                                                                                                                                                                                                                                                                                                       |

---

## PA-03 — Programa de capacitación y simulación de phishing

| Campo                    | Valor                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Riesgo asociado**      | R-04 — Phishing y robo de credenciales de empleados                                                                                                                                                                                                                                                                                                                                                      |
| **Título**               | Programa de capacitación y simulación de phishing                                                                                                                                                                                                                                                                                                                                                        |
| **Descripción**          | Implementar un programa de concientización en seguridad destinado a los 120 empleados de la clínica. El programa incluirá capacitación sobre reconocimiento de correos fraudulentos, ingeniería social, manejo seguro de credenciales y mecanismos de reporte. Se realizarán campañas de simulación de phishing para medir la efectividad de la capacitación y detectar sectores que requieran refuerzo. |
| **Fecha de vencimiento** | 15/10/2026                                                                                                                                                                                                                                                                                                                                                                                               |
| **Responsable**          | Responsable de Seguridad de la Información / Recursos Humanos                                                                                                                                                                                                                                                                                                                                            |
| **Presupuesto estimado** | USD 2.000                                                                                                                                                                                                                                                                                                                                                                                                |
| **Estado inicial**       | Not Started                                                                                                                                                                                                                                                                                                                                                                                              |

---

# Resumen de planes de acción

| ID    | Riesgo                      | Plan                                  | Responsable                            | Vencimiento | Presupuesto | Estado      |
| ----- | --------------------------- | ------------------------------------- | -------------------------------------- | ----------- | ----------: | ----------- |
| PA-01 | R-01 — Ransomware           | Backups resilientes contra ransomware | Director de Sistemas / Infraestructura | 30/11/2026  |   USD 8.000 | Not Started |
| PA-02 | R-02 — Acceso no autorizado | Implementación de MFA                 | Seguridad de la Información            | 31/10/2026  |   USD 4.000 | Not Started |
| PA-03 | R-04 — Phishing             | Capacitación + simulación de phishing | Seguridad + RR.HH.                     | 15/10/2026  |   USD 2.000 | Not Started |

**Presupuesto total estimado: USD 14.000.**

---

# Priorización

De acuerdo con la valoración obtenida mediante la metodología Classic:

1. **R-01 — Ransomware sobre sistemas de historias clínicas:** 20 — Crítico.
2. **R-02 — Acceso no autorizado a historias clínicas:** 20 — Crítico.
3. **R-04 — Phishing y robo de credenciales:** 16 — Crítico.
4. **R-03 — Indisponibilidad del sistema de historias clínicas:** 15 — Alto.
5. **R-05 — Fuga de información de pacientes y obras sociales:** 15 — Alto.
6. **R-06 — Alteración no autorizada de información clínica:** 15 — Alto.
7. **R-07 — Incendio o inundación de infraestructura tecnológica:** 10 — Alto.

Los riesgos **R-01, R-02 y R-04** requieren tratamiento prioritario debido a que se encuentran dentro del rango crítico de la matriz utilizada.

---

# Consideraciones metodológicas

Los valores de probabilidad e impacto corresponden a una **evaluación inicial del escenario académico** y no representan estadísticas reales de incidentes de la clínica.

La probabilidad se determinó considerando factores como la cantidad de usuarios, la dependencia de sistemas digitales, la exposición a amenazas externas, la sensibilidad de la información y la existencia asumida de controles básicos.

El impacto se determinó considerando principalmente:

* Continuidad de la atención médica.
* Confidencialidad de las historias clínicas.
* Integridad de diagnósticos y tratamientos.
* Protección de datos personales.
* Consecuencias económicas.
* Consecuencias legales y regulatorias.
* Reputación de la organización.

Los controles existentes indicados en este documento son supuestos derivados de la información disponible en el escenario y deberán validarse en una evaluación real.

El nivel de riesgo visualizado en SimpleRisk puede depender de la configuración de la matriz de scoring de la instalación. Para la documentación formal se toman como referencia los valores de **Current Likelihood** y **Current Impact** cargados en SimpleRisk y la matriz Classic definida para este análisis.

---

# Evidencias

Las capturas de la configuración y carga de los riesgos en SimpleRisk se almacenarán en:

`../informe/capturas/`

Ejemplos:

* `06-riesgo-prueba.png`
* `07-riesgo-r01.png`
* `08-riesgo-r02.png`
* `09-tabla-riesgos.png`
* `10-mitigacion-ramsonware.png`
* `11-mitigacion-acceso.png`
* `12-mitigacion-phising.png`
* `13-tabla-mitigaciones.png`
