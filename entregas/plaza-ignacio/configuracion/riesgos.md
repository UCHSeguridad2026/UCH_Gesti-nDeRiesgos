# Registro de riesgos

Los siguientes riesgos fueron identificados a partir del escenario de la clínica privada y registrados en SimpleRisk.

La probabilidad y el impacto se expresan también en una escala de 1 a 5 para documentar el análisis solicitado. El nivel y la puntuación resultante corresponden a la valoración realizada en SimpleRisk mediante su método de puntuación Classic.

## Riesgo 1001

**Subject:** Prueba de funcionamiento - acceso no autorizado

**Descripción:**  
Riesgo ficticio creado para comprobar el correcto funcionamiento del registro de riesgos, la evaluación y la asignación de responsables en SimpleRisk.

**Categoría:** Access Management

**Activo afectado:** No se especificó un activo concreto.

**Probabilidad:** 2/5 - Unlikely

**Justificación de la probabilidad:**  
Se asignó un nivel bajo porque se trata de un riesgo de prueba creado únicamente para verificar el funcionamiento de la herramienta y no de un evento real del escenario.

**Impacto:** 2/5 - Minor

**Justificación del impacto:**  
El impacto se considera bajo porque el riesgo fue creado como una prueba de funcionamiento y no representa un incidente real de la clínica.

**Nivel de riesgo en SimpleRisk:** 1.6 - Low

**Controles existentes:** No especificados.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

---

## Riesgo 1002

**Subject:** Uso indebido de cuentas con acceso a historias clínicas

**Descripción:**  
Un empleado con acceso legítimo al sistema puede consultar historias clínicas de pacientes que no están relacionados con sus tareas, generando una exposición no autorizada de información sensible.

**Categoría:** Access Management

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 3/5 - Credible

**Justificación de la probabilidad:**  
Se considera Credible debido a que la clínica cuenta con 120 empleados, utiliza historias clínicas digitales y depende del sistema para gestionar información clínica. La existencia de múltiples usuarios y la dependencia del sistema hacen posible que se produzca un acceso indebido.

**Impacto:** 4/5 - Major

**Justificación del impacto:**  
Se considera Major porque un acceso indebido podría exponer información contenida en las historias clínicas digitales, afectando la confidencialidad de los pacientes y pudiendo generar consecuencias operativas, legales y reputacionales para la clínica.

**Nivel de riesgo en SimpleRisk:** 4.8 - Medium

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mitigation Planned

---

## Riesgo 1003

**Subject:** Modificación incorrecta de una historia clínica

**Descripción:**  
Un usuario puede modificar información de una historia clínica de forma incorrecta o no autorizada, afectando la integridad de la información utilizada durante la atención de un paciente.

**Categoría:** Sensitive Data Management

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 3/5 - Credible

**Justificación de la probabilidad:**  
Se considera Credible debido a que la clínica utiliza historias clínicas digitales y cuenta con 120 empleados. La existencia de múltiples usuarios y la dependencia del sistema para gestionar información clínica hacen posible que se produzcan modificaciones incorrectas o no autorizadas.

**Impacto:** 5/5 - Extreme/Catastrophic

**Justificación del impacto:**  
Se considera Extreme/Catastrophic porque una modificación incorrecta de información clínica puede afectar directamente la integridad de las historias clínicas y generar consecuencias graves para la atención de los pacientes y el funcionamiento de la clínica.

**Nivel de riesgo inherente en SimpleRisk:** 6 - Medium

**Nivel de riesgo residual en SimpleRisk:** 3 - Low

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mgmt Reviewed

---

## Riesgo 1004

**Subject:** Exposición de información de pacientes mediante exportaciones

**Descripción:**  
Un empleado puede exportar información de pacientes para realizar una tarea y el archivo puede quedar guardado o compartido de una forma insegura.

**Categoría:** Sensitive Data Management

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 3/5 - Credible

**Justificación de la probabilidad:**  
Se considera Credible porque la clínica trabaja con historias clínicas digitales y puede necesitar exportar información para distintas tareas. El escenario no indica que exista un control específico sobre estas exportaciones.

**Impacto:** 4/5 - Major

**Justificación del impacto:**  
Se considera Major porque una exposición de información de pacientes puede afectar la confidencialidad de los datos y generar problemas para la clínica.

**Nivel de riesgo en SimpleRisk:** 4.8 - Medium

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mitigation Planned

---

## Riesgo 1005

**Subject:** Interrupción del sistema de historias clínicas durante la atención

**Descripción:**  
El sistema de historias clínicas puede quedar temporalmente fuera de servicio y dificultar el acceso a la información necesaria durante la atención de pacientes.

**Categoría:** Technical Vulnerability Management

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 4/5 - Likely

**Justificación de la probabilidad:**  
Se considera Likely porque la clínica depende diariamente de las historias clínicas digitales para atender a aproximadamente 800 pacientes por día y cualquier falla del sistema puede afectar directamente su funcionamiento.

**Impacto:** 4/5 - Major

**Justificación del impacto:**  
Se considera Major porque la falta de acceso a las historias clínicas puede afectar la atención de pacientes y generar problemas operativos para la clínica.

**Nivel de riesgo inherente en SimpleRisk:** 6.4 - Medium

**Nivel de riesgo residual en SimpleRisk:** 3.2 - Low

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mitigation Planned

---

## Riesgo 1006

**Subject:** Error en la facturación de prestaciones a obras sociales

**Descripción:**  
Puede producirse un error en la información utilizada para facturar prestaciones a las obras sociales, generando diferencias en la facturación.

**Categoría:** Policy and Procedure

**Activo afectado:** Datos de obras sociales

**Probabilidad:** 3/5 - Credible

**Justificación de la probabilidad:**  
Se considera Credible porque la clínica maneja información de obras sociales y realiza procesos de facturación. Un error en la carga o procesamiento de los datos es posible.

**Impacto:** 4/5 - Major

**Justificación del impacto:**  
Se considera Major porque los errores de facturación pueden generar problemas económicos y administrativos para la clínica.

**Nivel de riesgo en SimpleRisk:** 4.8 - Medium

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

---

## Riesgo 1007

**Subject:** Acceso de personal que ya no debería tener permisos

**Descripción:**  
Un empleado puede cambiar de función o dejar de trabajar en la clínica y mantener durante un tiempo permisos de acceso a sistemas con información sensible.

**Categoría:** Access Management

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 4/5 - Likely

**Justificación de la probabilidad:**  
Se considera Likely porque la clínica cuenta con 120 empleados y utiliza sistemas con distintos niveles de acceso. El escenario no indica que exista un proceso específico para revisar o retirar permisos cuando cambia la situación de un empleado.

**Impacto:** 4/5 - Major

**Justificación del impacto:**  
Se considera Major porque mantener permisos que ya no corresponden puede permitir el acceso a historias clínicas y otra información sensible de la clínica.

**Nivel de riesgo en SimpleRisk:** 6.4 - Medium

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mitigation Planned

---

## Riesgo 1008

**Subject:** Indisponibilidad de información por fallas en las copias de respaldo

**Descripción:**  
Las copias de respaldo de la información de la clínica pueden fallar y no estar disponibles cuando sea necesario recuperar información.

**Categoría:** Environmental Resilience

**Activo afectado:** Historias clínicas digitales

**Probabilidad:** 4/5 - Likely

**Justificación de la probabilidad:**  
Se considera Likely porque la clínica depende de información digital para sus actividades y el escenario no indica que exista un control específico sobre las copias de respaldo o su recuperación.

**Impacto:** 5/5 - Extreme/Catastrophic

**Justificación del impacto:**  
Se considera Extreme/Catastrophic porque una falla en la recuperación podría dejar inaccesible información importante, especialmente las historias clínicas digitales, afectando seriamente el funcionamiento de la clínica.

**Nivel de riesgo inherente en SimpleRisk:** 8 - High

**Nivel de riesgo residual en SimpleRisk:** 4 - Medium

**Controles existentes:** No especificados en el escenario.

**Plan de tratamiento:** Mitigar.

**Propietario:** Analista de Riesgos Demo

**Estado en SimpleRisk:** Mitigation Planned

---

## Planes de acción

Los siguientes planes de acción se definieron para el tratamiento del riesgo 1008 - Indisponibilidad de información por fallas en las copias de respaldo.

### Plan de acción 1

**Título:** Verificar las copias de respaldo

**Descripción:**  
Revisar que las copias de respaldo se estén realizando correctamente y que no tengan errores.

**Fecha de vencimiento:** 30/09/2026

**Responsable:** Analista de Riesgos Demo

**Presupuesto estimado:** USD 300

**Estado inicial:** No iniciado

### Plan de acción 2

**Título:** Realizar una prueba de recuperación

**Descripción:**  
Realizar una prueba para comprobar que una copia de respaldo pueda recuperarse correctamente.

**Fecha de vencimiento:** 15/10/2026

**Responsable:** Analista de Riesgos Demo

**Presupuesto estimado:** USD 500

**Estado inicial:** No iniciado

### Plan de acción 3

**Título:** Mejorar el esquema de respaldo

**Descripción:**  
Revisar el esquema actual de respaldo y realizar las mejoras necesarias para reducir el riesgo de pérdida o indisponibilidad de información.

**Fecha de vencimiento:** 31/10/2026

**Responsable:** Analista de Riesgos Demo

**Presupuesto estimado:** USD 700

**Estado inicial:** No iniciado