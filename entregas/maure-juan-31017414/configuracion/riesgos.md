# Registro de Riesgos - Clínica Privada

A continuación se detallan los 7 riesgos específicos identificados para el contexto de la clínica (120 empleados, 800 pacientes diarios), documentados previo a su carga en la plataforma SimpleRisk.

## R01: Acceso indebido a expedientes electrónicos
*   **Descripción:** Personal administrativo o no médico accediendo a las historias clínicas de los pacientes sin justificación clínica, vulnerando la confidencialidad.
*   **Categoría:** Access Management (Gestión de Accesos).
*   **Activos afectados:** Base de datos de pacientes, Historias Clínicas Electrónicas.
*   **Probabilidad e Impacto:** Probabilidad 4 (Probable, debido a que actualmente los accesos son genéricos) x Impacto 5 (Catastrófico, por tratarse de datos de salud altamente sensibles).
*   **Nivel de riesgo resultante:** 20 (Crítico).
*   **Controles existentes:** Ninguno formal. El sistema actual carece de segregación de roles.
*   **Plan de tratamiento propuesto:** Mitigar (Implementación de Control de Accesos Basado en Roles - RBAC).
*   **Propietario del riesgo:** Director Médico / Administrador.

## R02: Interrupción del sistema por falla de servidor
*   **Descripción:** Caída del servidor físico principal que detiene por completo la visualización de historias clínicas y la atención en consultorios.
*   **Categoría:** Environmental Resilience (Disponibilidad).
*   **Activos afectados:** Servidor principal, red local de la clínica.
*   **Probabilidad e Impacto:** Probabilidad 3 (Creíble, al no tener redundancia de hardware) x Impacto 5 (Catastrófico, frena la atención de 800 pacientes diarios).
*   **Nivel de riesgo resultante:** 15 (Alto).
*   **Controles existentes:** Copias de seguridad manuales semanales en disco duro externo.
*   **Plan de tratamiento propuesto:** Mitigar (Implementación de Alta Disponibilidad y respaldos automatizados en la nube).
*   **Propietario del riesgo:** Responsable de IT / Infraestructura.

## R03: Corrupción de datos con Obras Sociales
*   **Descripción:** Errores en la base de datos o fallos de red al momento de sincronizar las liquidaciones de facturación con las API de las obras sociales.
*   **Categoría:** Sensitive Data Management (Integridad).
*   **Activos afectados:** Módulo de facturación, integraciones de red.
*   **Probabilidad e Impacto:** Probabilidad 3 (Creíble) x Impacto 3 (Moderado, genera demoras en cobros pero no detiene la clínica).
*   **Nivel de riesgo resultante:** 9 (Medio).
*   **Controles existentes:** Revisión y corrección manual de lotes de facturación por parte del equipo administrativo.
*   **Plan de tratamiento propuesto:** Aceptar (el control manual actual es suficiente por el momento).
*   **Propietario del riesgo:** Responsable de Sistemas / Integraciones.

## R04: Vulneración de la base de facturación
*   **Descripción:** Modificación no autorizada de montos o registros de pagos por parte de un usuario interno malintencionado.
*   **Categoría:** Access Management (Integridad).
*   **Activos afectados:** Base de datos de facturación y finanzas.
*   **Probabilidad e Impacto:** Probabilidad 2 (Poco probable) x Impacto 4 (Mayor, impacto financiero directo).
*   **Nivel de riesgo resultante:** 8 (Medio).
*   **Controles existentes:** Uso de contraseñas locales en las computadoras del área contable.
*   **Plan de tratamiento propuesto:** Mitigar (revisión de permisos a largo plazo).
*   **Propietario del riesgo:** Responsable Administrativo / IT.

## R05: Compromiso de credenciales por ataques de phishing
*   **Descripción:** Empleados de la clínica entregan sus contraseñas al caer en correos electrónicos fraudulentos, permitiendo el acceso de atacantes a la red.
*   **Categoría:** Policy and Procedure (Concientización).
*   **Activos afectados:** Credenciales de usuarios, correos corporativos.
*   **Probabilidad e Impacto:** Probabilidad 4 (Probable, al no existir un programa de capacitación) x Impacto 3 (Moderado).
*   **Nivel de riesgo resultante:** 12 (Alto).
*   **Controles existentes:** Filtro antispam básico provisto por el servidor de correo.
*   **Plan de tratamiento propuesto:** Mitigar (Desarrollar un plan de concientización y capacitación obligatoria).
*   **Propietario del riesgo:** Responsable de Seguridad de la Información.

## R06: Infección por ransomware por falta de parches
*   **Descripción:** Un software malicioso (malware/ransomware) cifra los sistemas de la clínica explotando vulnerabilidades conocidas de Windows que no fueron actualizadas.
*   **Categoría:** Technical Vulnerability Management (Disponibilidad / Confidencialidad).
*   **Activos afectados:** 120 estaciones de trabajo y servidores.
*   **Probabilidad e Impacto:** Probabilidad 3 (Creíble) x Impacto 5 (Catastrófico, pérdida total de acceso a datos operativos).
*   **Nivel de riesgo resultante:** 15 (Alto).
*   **Controles existentes:** Antivirus tradicional básico en las estaciones de trabajo.
*   **Plan de tratamiento propuesto:** Mitigar (Despliegue de gestión de parches centralizada y Antivirus EDR).
*   **Propietario del riesgo:** Responsable de IT / Infraestructura.

## R07: Incumplimiento de la Ley de Protección de Datos Personales
*   **Descripción:** Sanciones legales y multas regulatorias por el manejo inseguro y sin auditoría de los datos de salud de los pacientes.
*   **Categoría:** Policy and Procedure (Legal / Cumplimiento).
*   **Activos afectados:** Reputación institucional, finanzas (multas).
*   **Probabilidad e Impacto:** Probabilidad 4 (Probable, dados los hallazgos de accesos indebidos) x Impacto 4 (Mayor, posibles demandas legales).
*   **Nivel de riesgo resultante:** 16 (Crítico).
*   **Controles existentes:** Acuerdos de confidencialidad genéricos firmados durante el ingreso de los empleados.
*   **Plan de tratamiento propuesto:** Mitigar (Formalizar políticas de seguridad y aplicar controles técnicos de privacidad).
*   **Propietario del riesgo:** Director Médico / Oficial de Cumplimiento.