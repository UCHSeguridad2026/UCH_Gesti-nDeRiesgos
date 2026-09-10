# Riesgos definidos

> Las evidencias visuales de esta sección se encuentran en el directorio `informe/capturas/`.
*RECOMENDACIÓN: Abrir una pestaña en paralelo para visualizar las cpturas.*

## Riesgo de prueba

**Nombre:** Riesgo de prueba - indisponibilidad del sistema

**Objetivo:** Validar el funcionamiento del flujo de gestión de riesgos en SimpleRisk.

**Categoría:** Environmental Resilience

**Activo afectado:** Sistema de gestión clínica

**Fuente del riesgo:** System

**Probabilidad:** Unlikely (equivalente a 2/5)

**Impacto:** Minor (equivalente a 2/5)

**Propietario:** Analista de Riesgos

**Evaluación:**

Este riesgo fue creado exclusivamente como prueba funcional para validar el alta, clasificación, asignación y evaluación de riesgos dentro de SimpleRisk.

Los valores de probabilidad e impacto utilizados no representan una evaluación realista de la indisponibilidad del sistema de gestión de la clínica. La valoración definitiva de riesgos se realizará en la Parte B del trabajo, utilizando criterios acordes al contexto organizacional.

## Evidencia

La evidencia visual del riesgo de prueba creado en SimpleRisk se encuentra en:

`informe/capturas/22-riesgo de prueba creado`

## Riesgo 1 - Ransomware sobre el sistema de gestión clínica

**Nombre:** Ransomware sobre el sistema de gestión clínica

**Descripción:**  
Un equipo de la clínica podría verse comprometido mediante phishing, archivos maliciosos o explotación de vulnerabilidades, permitiendo que un ransomware afecte estaciones de trabajo y se propague hacia el sistema de gestión clínica o recursos asociados. Esto podría provocar cifrado de información, interrupción de servicios y pérdida temporal de disponibilidad.

**Categoría:** Disponibilidad

**Activos afectados:**
- Sistema de gestión clínica
- Historias clínicas digitales
- Estaciones de trabajo del personal
- Sistema de backups

**Probabilidad:** 4/5 - Likely

**Justificación de probabilidad:**  
Se considera una probabilidad alta debido a la existencia de múltiples vectores potenciales de entrada asociados al uso cotidiano de estaciones de trabajo y sistemas digitales, como phishing, archivos maliciosos o explotación de vulnerabilidades.

**Impacto:** 5/5 - Extreme / Catastrophic

**Justificación de impacto:**  
Una interrupción prolongada del sistema de gestión clínica podría impedir o dificultar el acceso a historias clínicas, afectar la atención de aproximadamente 800 pacientes diarios y comprometer procesos administrativos y de facturación.

**Nivel de riesgo resultante:** 20 - Muy alto

**Controles existentes:**  
Se asume la existencia de protección antivirus básica en las estaciones de trabajo. No se asumen controles avanzados como EDR, segmentación de red o backups inmutables, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Implementar protección EDR/antimalware.
- Mantener sistemas y estaciones actualizados mediante gestión de parches.
- Segmentar la red para limitar movimientos laterales.
- Capacitar al personal frente a phishing.
- Mantener backups aislados o inmutables.
- Realizar pruebas periódicas de restauración.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/28- riesgo Ransomware sobre el sistema de gestión clínica`

## Riesgo 2 - Acceso no autorizado a historias clínicas digitales

**Nombre:** Acceso no autorizado a historias clínicas digitales

**Descripción:**  
Un usuario interno o externo podría obtener acceso no autorizado a historias clínicas digitales mediante credenciales comprometidas, permisos excesivos o uso indebido de cuentas.

**Categoría:** Confidencialidad

**Activos afectados:**
- Historias clínicas digitales
- Base de datos de pacientes
- Credenciales y cuentas de empleados

**Probabilidad:** 3/5 - Credible

**Justificación de probabilidad:**  
Se considera una probabilidad media debido a la cantidad de usuarios que requieren acceso frecuente a información clínica y a la posibilidad de que existan credenciales comprometidas o permisos excesivos.

**Impacto:** 4/5 - Major

**Justificación de impacto:**  
El impacto se considera alto debido a la sensibilidad de los datos clínicos y personales involucrados. Un acceso no autorizado podría comprometer la confidencialidad de los pacientes, generar incidentes de seguridad y afectar la confianza en la organización.

**Nivel de riesgo resultante:** 12 - Alto

**Controles existentes:**  
Se asume la existencia de autenticación mediante usuario y contraseña y una asignación básica de permisos por rol. No se asumen controles avanzados como autenticación multifactor, monitoreo detallado de accesos o revisiones periódicas de privilegios, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Implementar autenticación multifactor.
- Aplicar el principio de mínimo privilegio.
- Revisar periódicamente permisos y privilegios.
- Registrar y monitorear accesos a historias clínicas.
- Deshabilitar rápidamente cuentas que ya no sean necesarias.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/25- riesgo Acceso no autorizado a historias clínicas digitales`

## Riesgo 3 - Pérdida o corrupción de backups de la clínica

**Nombre:** Pérdida o corrupción de backups de la clínica

**Descripción:**  
Una falla técnica, error de configuración o corrupción de los respaldos podría impedir la recuperación de información clínica ante un incidente, afectando la continuidad operativa de la organización.

**Categoría:** Disponibilidad

**Activos afectados:**
- Sistema de backups
- Historias clínicas digitales
- Base de datos de pacientes

**Probabilidad:** 3/5 - Credible

**Justificación de probabilidad:**  
Se considera una probabilidad media debido a que los respaldos pueden verse afectados por fallas técnicas, errores de configuración, problemas de almacenamiento o procedimientos de copia inadecuados.

**Impacto:** 4/5 - Major

**Justificación de impacto:**  
El impacto se considera alto porque la imposibilidad de recuperar información crítica podría prolongar una interrupción de servicios y afectar el acceso a datos necesarios para la atención y la operación administrativa de la clínica.

**Nivel de riesgo resultante:** 12 - Alto

**Controles existentes:**  
Se asume la existencia de un esquema básico de copias de seguridad. No se asumen controles avanzados como backups inmutables, copias offline, redundancia geográfica o pruebas periódicas de restauración, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Mantener múltiples copias de respaldo.
- Incorporar al menos una copia aislada o inmutable.
- Definir una política formal de backups.
- Verificar periódicamente la integridad de los respaldos.
- Realizar pruebas de restauración.
- Restringir el acceso administrativo al sistema de backups.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/26- riesgo Pérdida o corrupción de backups`

## Riesgo 4 - Caída de la red interna de la clínica

**Nombre:** Caída de la red interna de la clínica

**Descripción:**  
Una falla en la infraestructura de red podría impedir el acceso de los usuarios a los sistemas clínicos y administrativos de la organización, afectando la continuidad de la atención y de los procesos internos.

**Categoría:** Disponibilidad

**Activos afectados:**
- Infraestructura de red
- Sistema de gestión clínica
- Sistema de facturación

**Probabilidad:** 3/5 - Credible

**Justificación de probabilidad:**  
Se considera una probabilidad media debido a la dependencia de la organización de equipos de red, conectividad interna y componentes de infraestructura que pueden presentar fallas técnicas o de configuración.

**Impacto:** 4/5 - Major

**Justificación de impacto:**  
El impacto se considera alto porque una caída de la red puede impedir que múltiples usuarios accedan simultáneamente a sistemas esenciales para la atención clínica y la gestión administrativa.

**Nivel de riesgo resultante:** 12 - Alto

**Controles existentes:**  
Se asume la existencia de una infraestructura de red básica operativa. No se asumen controles avanzados como redundancia de enlaces, alta disponibilidad, monitoreo centralizado o equipamiento duplicado, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Incorporar monitoreo de disponibilidad de la red.
- Documentar la topología y los equipos críticos.
- Implementar redundancia en componentes esenciales.
- Mantener configuraciones de respaldo de los dispositivos de red.
- Definir procedimientos de recuperación ante fallas de conectividad.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/27- riesgo Caída de la red interna`

## Riesgo 5 - Compromiso de credenciales de empleados mediante phishing

**Nombre:** Compromiso de credenciales de empleados mediante phishing

**Descripción:**  
Un empleado podría ser víctima de un intento de phishing y entregar sus credenciales a un atacante, permitiendo accesos no autorizados a sistemas clínicos o administrativos.

**Categoría:** Confidencialidad

**Activos afectados:**
- Credenciales y cuentas de empleados
- Sistema de gestión clínica
- Sistema de facturación

**Probabilidad:** 4/5 - Likely

**Justificación de probabilidad:**  
Se considera una probabilidad alta debido a la exposición habitual de los usuarios a correos, enlaces y mensajes potencialmente maliciosos, sumada a la posibilidad de errores humanos durante el uso cotidiano de los sistemas.

**Impacto:** 4/5 - Major

**Justificación de impacto:**  
El impacto se considera alto porque unas credenciales comprometidas podrían permitir acceso a información sensible y a sistemas críticos, facilitando además otras acciones maliciosas dentro de la organización.

**Nivel de riesgo resultante:** 16 - Muy alto

**Controles existentes:**  
Se asume la existencia de autenticación mediante usuario y contraseña. No se asumen controles adicionales como autenticación multifactor, filtros avanzados de correo o campañas periódicas de concientización, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Implementar autenticación multifactor.
- Capacitar periódicamente al personal sobre phishing e ingeniería social.
- Incorporar filtros de correo y protección contra enlaces maliciosos.
- Aplicar políticas de contraseñas seguras.
- Monitorear intentos de acceso anómalos.
- Facilitar mecanismos para reportar correos sospechosos.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/24- riesgo Compromiso de credenciales de empleados mediante phishing`

## Riesgo 6 - Indisponibilidad de servicios externos de facturación u obras sociales

**Nombre:** Indisponibilidad de servicios externos de facturación u obras sociales

**Descripción:**  
La caída o indisponibilidad de un servicio externo utilizado para facturación o validación con obras sociales podría interrumpir procesos administrativos y generar demoras en la gestión de coberturas.

**Categoría:** Disponibilidad

**Activos afectados:**
- Sistema de facturación
- Datos de obras sociales
- Servicios externos de facturación y obras sociales

**Probabilidad:** 3/5 - Credible

**Justificación de probabilidad:**  
Se considera una probabilidad media debido a que la clínica depende de servicios externos cuya disponibilidad no controla directamente y que pueden sufrir interrupciones o degradaciones.

**Impacto:** 3/5 - Moderate

**Justificación de impacto:**  
El impacto se considera moderado porque una interrupción de estos servicios puede afectar procesos administrativos, validaciones y facturación, aunque no necesariamente detenga por completo la atención clínica.

**Nivel de riesgo resultante:** 9 - Medio

**Controles existentes:**  
Se asume la existencia de conectividad con proveedores externos y procedimientos operativos básicos. No se asumen mecanismos avanzados de contingencia, redundancia de proveedores o acuerdos específicos de continuidad, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Definir procedimientos de contingencia ante indisponibilidad de proveedores.
- Mantener canales alternativos de contacto y gestión.
- Monitorear la disponibilidad de servicios externos críticos.
- Establecer acuerdos de nivel de servicio cuando corresponda.
- Evaluar alternativas manuales temporales para procesos administrativos esenciales.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/29- riesgo Indisponibilidad de servicios externos`

## Riesgo 7 - Modificación no autorizada de datos clínicos o administrativos

**Nombre:** Modificación no autorizada de datos clínicos o administrativos

**Descripción:**  
Un usuario interno o una cuenta comprometida podría modificar información clínica o administrativa sin autorización, afectando la integridad de los datos y la trazabilidad de las operaciones.

**Categoría:** Integridad

**Activos afectados:**
- Historias clínicas digitales
- Base de datos de pacientes
- Sistema de facturación

**Probabilidad:** 3/5 - Credible

**Justificación de probabilidad:**  
Se considera una probabilidad media debido a que múltiples usuarios acceden a sistemas con información sensible y existe la posibilidad de errores, abuso de privilegios o utilización de cuentas comprometidas.

**Impacto:** 4/5 - Major

**Justificación de impacto:**  
El impacto se considera alto porque la alteración de información clínica podría afectar decisiones de atención, mientras que la modificación de datos administrativos o de facturación podría generar errores operativos, financieros y de trazabilidad.

**Nivel de riesgo resultante:** 12 - Alto

**Controles existentes:**  
Se asume la existencia de autenticación de usuarios y permisos básicos de acceso. No se asumen controles avanzados como segregación estricta de privilegios, monitoreo de cambios, trazabilidad detallada o revisiones periódicas de accesos, ya que el escenario no los especifica.

**Tratamiento:** Mitigar

**Plan de tratamiento propuesto:**
- Aplicar el principio de mínimo privilegio.
- Revisar periódicamente los permisos de acceso.
- Implementar registros de auditoría sobre modificaciones de datos sensibles.
- Monitorear cambios anómalos o no autorizados.
- Separar funciones críticas entre distintos perfiles.
- Establecer procedimientos de revisión y corrección de modificaciones indebidas.

**Propietario del riesgo:** Responsable de TI / Seguridad de la Información

**Evidencia:**  
`informe/capturas/30- riesgo Modificación no autorizada de datos clínicos o administrativos`

# Planes de acción

Como parte del tratamiento de los riesgos identificados, se definieron tres planes de acción asociados a riesgos de nivel alto o muy alto.

## Plan de acción 1 - Protección contra ransomware

**Riesgo asociado:** Ransomware sobre el sistema de gestión clínica

**Título:** Implementación de controles de protección contra ransomware

**Descripción:**  
Implementar medidas preventivas y de recuperación para reducir la probabilidad e impacto de un ataque de ransomware, incluyendo protección de endpoints, gestión de parches, segmentación de red y fortalecimiento de la estrategia de backups.

**Responsable:** Responsable IT

**Fecha de vencimiento:** 10/10/2026

**Presupuesto estimado:** USD 3.000

**Estado inicial:** Planificado

**Acciones propuestas:**
- Implementar protección EDR/antimalware.
- Mantener sistemas y estaciones actualizados mediante gestión de parches.
- Segmentar la red para limitar movimientos laterales.
- Capacitar al personal frente a phishing.
- Mantener backups aislados o inmutables.
- Realizar pruebas periódicas de restauración.

**Evidencia:**  
`informe/capturas/31-Mitigation ransomware`


## Plan de acción 2 - Fortalecimiento de autenticación y prevención de phishing

**Riesgo asociado:** Compromiso de credenciales de empleados mediante phishing

**Título:** Fortalecimiento de autenticación y prevención de phishing

**Descripción:**  
Implementar controles orientados a reducir la probabilidad de robo y uso indebido de credenciales de empleados mediante ataques de phishing.

**Responsable:** Responsable IT

**Fecha de vencimiento:** 10/10/2026

**Presupuesto estimado:** USD 2.000

**Estado inicial:** Planificado

**Acciones propuestas:**
- Implementar autenticación multifactor.
- Capacitar periódicamente al personal sobre phishing e ingeniería social.
- Incorporar filtros de correo y protección contra enlaces maliciosos.
- Monitorear accesos anómalos.
- Implementar mecanismos simples para reportar mensajes sospechosos.

**Evidencia:**  
`informe/capturas/32- mitigation para phishing`


## Plan de acción 3 - Fortalecimiento de la estrategia de backups

**Riesgo asociado:** Pérdida o corrupción de backups de la clínica

**Título:** Fortalecimiento de la estrategia de backups

**Descripción:**  
Mejorar la estrategia de copias de seguridad para asegurar la disponibilidad, integridad y recuperabilidad de la información crítica ante fallas, corrupción de datos o incidentes de seguridad.

**Responsable:** Responsable IT

**Fecha de vencimiento:** 10/10/2026

**Presupuesto estimado:** USD 2.500

**Estado inicial:** Planificado

**Acciones propuestas:**
- Mantener múltiples copias de respaldo.
- Incorporar al menos una copia aislada o inmutable.
- Verificar periódicamente la integridad de los backups.
- Realizar pruebas periódicas de restauración.
- Restringir el acceso administrativo al sistema de backups.

**Evidencia:**  
`informe/capturas/33-mitigation backups`