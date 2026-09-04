# Registro de Riesgos

## Contexto

El análisis corresponde a una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día y gestiona historias clínicas digitales, datos de obras sociales y procesos de facturación.

Para la valoración se utilizó una escala de probabilidad e impacto de 1 a 5. El valor académico del riesgo se obtiene mediante:

Valor de riesgo = Probabilidad × Impacto

Los niveles utilizados son:

- Bajo: 1 a 4
- Medio: 5 a 9
- Alto: 10 a 15
- Crítico: 16 a 25

SimpleRisk utiliza el método Classic y normaliza el resultado a una escala de 10 mediante la fórmula:

(Likelihood × Impact) × (10 / 25)

Por este motivo, el valor visualizado por SimpleRisk puede diferir del valor de la matriz 5x5 utilizada para la evaluación académica. En este documento se mantiene la clasificación solicitada por la cátedra.

---

## R01 - Acceso no autorizado a historias clínicas digitales

**Descripción:**  
Un atacante externo o una cuenta interna comprometida podría acceder sin autorización al sistema de historias clínicas y consultar información médica y datos personales de pacientes.

**Categoría:** Confidencialidad / Gestión de accesos.

**Activos afectados:** Historias clínicas digitales, datos personales de pacientes y aplicación clínica.

**Probabilidad:** 4 - Probable.

**Justificación de probabilidad:**  
La clínica cuenta con 120 empleados y múltiples usuarios que acceden diariamente a los sistemas. La cantidad de cuentas y el uso cotidiano de credenciales incrementan la exposición frente a phishing, compromiso de contraseñas o utilización indebida de cuentas.

**Impacto:** 5 - Catastrófico.

**Justificación de impacto:**  
El acceso no autorizado podría provocar la exposición de información médica y datos personales sensibles, además de consecuencias legales, reputacionales y operativas severas.

**Valor:** 20.

**Nivel:** Crítico.

**Controles existentes:**  
Autenticación mediante usuario y contraseña y permisos de acceso asociados a cada usuario.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar autenticación multifactor (MFA), aplicar el principio de mínimo privilegio, realizar revisiones periódicas de permisos y monitorear accesos y comportamientos anómalos.

**Propietario:** Martina López - Analista de Riesgos.

---

## R02 - Ransomware en sistemas clínicos

**Descripción:**  
Un ataque de ransomware podría cifrar servidores o estaciones utilizadas para acceder a historias clínicas, turnos y otros sistemas necesarios para la atención de pacientes.

**Categoría:** Disponibilidad / Integridad.

**Activos afectados:** Sistemas clínicos, historias clínicas digitales, servidores y estaciones de trabajo.

**Probabilidad:** 4 - Probable.

**Justificación de probabilidad:**  
La utilización de múltiples estaciones de trabajo, correo electrónico y servicios digitales genera diferentes posibles puntos de entrada para archivos maliciosos, phishing u otras técnicas utilizadas para distribuir ransomware.

**Impacto:** 5 - Catastrófico.

**Justificación de impacto:**  
La indisponibilidad de los sistemas clínicos podría impedir el acceso a información necesaria para atender aproximadamente 800 pacientes diarios y afectar gravemente la continuidad de la operación.

**Valor:** 20.

**Nivel:** Crítico.

**Controles existentes:**  
Antivirus en estaciones de trabajo, cuentas individuales y copias de seguridad periódicas.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar EDR, segmentación de red, copias de seguridad offline o inmutables, filtrado de correo y capacitación del personal frente a phishing y archivos maliciosos.

**Propietario:** Martina López - Analista de Riesgos.

---

## R03 - Indisponibilidad del sistema de turnos e historias clínicas

**Descripción:**  
Una falla de infraestructura, software o comunicaciones podría impedir temporalmente el acceso a los sistemas utilizados para administrar turnos y consultar historias clínicas.

**Categoría:** Disponibilidad.

**Activos afectados:** Sistema de turnos, aplicación de historias clínicas, servidores y red.

**Probabilidad:** 3 - Posible.

**Justificación de probabilidad:**  
Los servicios dependen de diferentes componentes tecnológicos y existe una posibilidad real de que una falla de infraestructura, software o comunicaciones afecte su funcionamiento.

**Impacto:** 5 - Catastrófico.

**Justificación de impacto:**  
Una interrupción prolongada podría afectar la atención de cientos de pacientes e impedir el acceso a información necesaria para las actividades asistenciales.

**Valor:** 15.

**Nivel:** Alto.

**Controles existentes:**  
Copias de seguridad y soporte técnico.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar redundancia de componentes críticos, monitoreo de disponibilidad, procedimientos de contingencia y pruebas periódicas de recuperación.

**Propietario:** Administrador de Seguridad.

---

## R04 - Alteración indebida de información clínica

**Descripción:**  
Un usuario con permisos excesivos o una cuenta comprometida podría modificar información contenida en una historia clínica de manera accidental o intencional.

**Categoría:** Integridad.

**Activos afectados:** Historias clínicas digitales y aplicación clínica.

**Probabilidad:** 3 - Posible.

**Justificación de probabilidad:**  
La información clínica es utilizada diariamente por múltiples profesionales y empleados, por lo que una gestión inadecuada de permisos puede permitir modificaciones que no correspondan.

**Impacto:** 5 - Catastrófico.

**Justificación de impacto:**  
La existencia de información médica incorrecta podría afectar decisiones asistenciales y generar consecuencias graves para los pacientes y para la organización.

**Valor:** 15.

**Nivel:** Alto.

**Controles existentes:**  
Cuentas individuales y permisos básicos de acceso.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar control de acceso basado en roles, mínimo privilegio, registros de auditoría, trazabilidad de modificaciones y alertas ante cambios críticos.

**Propietario:** Martina López - Analista de Riesgos.

---

## R05 - Filtración de datos de pacientes por error del personal

**Descripción:**  
Un empleado podría enviar documentación médica o administrativa a un destinatario incorrecto, utilizar un canal inadecuado para compartir información o exponer accidentalmente datos de pacientes.

**Categoría:** Confidencialidad.

**Activos afectados:** Historias clínicas, datos personales y datos de obras sociales.

**Probabilidad:** 3 - Posible.

**Justificación de probabilidad:**  
La clínica cuenta con 120 empleados y existe manipulación cotidiana de información correspondiente a aproximadamente 800 pacientes diarios, por lo que los errores humanos representan una posibilidad real.

**Impacto:** 4 - Mayor.

**Justificación de impacto:**  
La exposición de información sensible podría generar reclamos, consecuencias regulatorias y daño reputacional para la clínica.

**Valor:** 12.

**Nivel:** Alto.

**Controles existentes:**  
Cuentas individuales y procedimientos internos básicos para el manejo de información.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar capacitación periódica, clasificación de información, mecanismos DLP y procedimientos seguros para compartir información sensible.

**Propietario:** Administrador de Seguridad.

---

## R06 - Falla del almacenamiento sin recuperación adecuada

**Descripción:**  
Una falla de hardware o corrupción del almacenamiento podría ocasionar pérdida de información si las copias disponibles no permiten recuperar correctamente los sistemas.

**Categoría:** Operativo / Disponibilidad.

**Activos afectados:** Historias clínicas, bases de datos de pacientes, sistema de turnos y facturación.

**Probabilidad:** 2 - Improbable.

**Justificación de probabilidad:**  
Una falla crítica de almacenamiento no se espera con frecuencia, aunque continúa siendo posible dentro de una infraestructura tecnológica.

**Impacto:** 5 - Catastrófico.

**Justificación de impacto:**  
La pérdida permanente de información clínica y administrativa podría producir consecuencias operativas, legales y reputacionales severas.

**Valor:** 10.

**Nivel:** Alto.

**Controles existentes:**  
Copias de seguridad periódicas.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar una estrategia de copias 3-2-1, mantener backups offline o inmutables, realizar pruebas periódicas de restauración y definir objetivos RPO y RTO.

**Propietario:** Administrador de Seguridad.

---

## R07 - Interrupción temporal del sistema de facturación con obras sociales

**Descripción:**  
Una falla de la aplicación, de conectividad o de la integración con servicios externos podría impedir temporalmente registrar o procesar prestaciones para su posterior facturación a obras sociales.

**Categoría:** Operativo.

**Activos afectados:** Sistema de facturación, información administrativa, datos de obras sociales e interfaces con terceros.

**Probabilidad:** 3 - Posible.

**Justificación de probabilidad:**  
El proceso depende de sistemas internos y servicios externos cuya disponibilidad no se encuentra completamente bajo control de la clínica.

**Impacto:** 3 - Moderado.

**Justificación de impacto:**  
La interrupción podría generar demoras administrativas y financieras apreciables, aunque las operaciones podrían reprocesarse una vez restablecido el servicio.

**Valor:** 9.

**Nivel:** Medio.

**Controles existentes:**  
Procedimientos administrativos y posibilidad de reprocesamiento de operaciones.

**Tratamiento:** Mitigar.

**Tratamiento propuesto:**  
Implementar monitoreo de integraciones, registro de operaciones pendientes, procedimientos manuales de contingencia y acuerdos de nivel de servicio con proveedores.

**Propietario:** Martina López - Analista de Riesgos.

---

## Resumen de resultados

| Nivel | Cantidad | Porcentaje |
|---|---:|---:|
| Crítico | 2 | 28,6 % |
| Alto | 4 | 57,1 % |
| Medio | 1 | 14,3 % |
| Bajo | 0 | 0 % |
| **Total** | **7** | **100 %** |

La evaluación muestra una concentración significativa de riesgos altos y críticos. Los riesgos relacionados con acceso no autorizado y ransomware presentan la mayor prioridad y requieren tratamiento inmediato. También se considera necesario fortalecer la continuidad operativa, la integridad de la información clínica y los mecanismos de recuperación ante fallas.
