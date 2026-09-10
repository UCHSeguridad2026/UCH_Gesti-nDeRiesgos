# Matriz y Registro de Riesgos - SimpleRisk

**Organización:** Clínica Médica Privada  
**Alcance Asistencial y Operativo:** 120 empleados en planta (médicos, enfermeros, personal técnico y administrativo), ~800 pacientes ambulatorios e internados atendidos por día. Infraestructura basada en Historias Clínicas Digitales (HCE), validación online de obras sociales, farmacia interna y facturación médica.  
**Plataforma de Gestión:** SimpleRisk v2026  

---

## Resumen de la Matriz de Riesgos

| ID | Riesgo Identificado | Categoría | Probabilidad (1-5) | Impacto (1-5) | Nivel Inmanente (SimpleRisk) | Estrategia de Tratamiento | Propietario del Riesgo |
|---|---|---|:---:|:---:|:---:|---|---|
| **1001** | Secuestro de datos (Ransomware) en servidores principales | Disponibilidad / Integridad / Confidencialidad | 4 | 5 | **8.0 (Alto)** | Mitigar (Plan 1) | Laura Gómez (IT Clínica) |
| **1005** | Robo de credenciales administrativas por correos de suplantación | Confidencialidad / Integridad | 4 | 4 | **6.4 (Medio-Alto)** | Mitigar (Plan 2) | Dr. Roberto Sánchez / Laura Gómez |
| **1003** | Pérdida de trazabilidad por cuentas compartidas en consultorios | Integridad / Legal | 4 | 3 | **6.0 (Medio)** | Mitigar | Dr. Roberto Sánchez (Dirección Médica) |
| **1002** | Interrupción del centro de datos por fallo eléctrico y climático | Disponibilidad / Operativo | 3 | 4 | **4.8 (Medio)** | Mitigar (Plan 3) | Laura Gómez (Data Center & Storage) |
| **1006** | Interrupción del enlace de telecomunicaciones con el ISP | Disponibilidad / Operativo | 3 | 3 | **3.6 (Medio-Bajo)** | Mitigar / Transferir | Laura Gómez (IT Clínica) |
| **1004** | Corrupción de datos y daño de almacenamiento en base de datos | Integridad / Disponibilidad | 2 | 4 | **3.2 (Bajo-Medio)** | Mitigar | Laura Gómez (Data Center & Storage) |
| **1007** | Sustracción de notebooks en áreas de atención y recepción | Confidencialidad / Disponibilidad | 3 | 2 | **2.4 (Bajo)** | Mitigar | Laura Gómez / Seguridad Patrimonial |

---

## Detalle Exhaustivo de los 7 Riesgos

### 1. Riesgo ID 1001: Secuestro de datos (Ransomware) en servidores principales
* **Descripción:** Infección por código malicioso de tipo ransomware que cifra las bases de datos de Historias Clínicas Electrónicas (HCE) y los repositorios de imágenes médicas (DICOM/PACS), paralizando la atención de 800 pacientes diarios y exigiendo rescate financiero en criptoactivos.
* **Categoría:** Disponibilidad, Integridad y Confidencialidad.
* **Activos Afectados:**
  * Cluster de Servidores de Base de Datos MySQL/MSSQL (HCE y Facturación).
  * Servidor PACS de Diagnóstico por Imágenes.
  * Almacenamiento NAS/SAN central de la clínica.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (4 - Alta):** El sector de la salud es el principal blanco de ataques dirigidos de ransomware a nivel global (evidenciado en informes como Verizon DBIR y Sophos State of Ransomware in Healthcare). Con 120 empleados accediendo a internet y recibiendo correos externos, la superficie de exposición es elevada.
  * **Impacto (5 - Catastrófico):** La imposibilidad de acceder a antecedentes de pacientes, cirugías programadas, medicación administrada y prescripciones pone en riesgo vital inminente la salud de los pacientes internados y genera una contingencia legal severa bajo la Ley de Protección de Datos Personales (Ley 25.326 y normativa de Salud Pública). Costo económico crítico por lucro cesante y multas regulatorias.
* **Nivel de Riesgo Inmanente:** **8.0 (Alto / Rojo)**.
* **Controles Existentes:** Antivirus basado en firmas en estaciones de trabajo y copias de seguridad locales en el mismo segmento de red sin inmutabilidad ni desconexión física (air-gap).
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Laura Gómez (IT Clínica).
* **Plan de Acción Vinculado:** Implementación de respaldos inmutables (WORM/Object Lock) offsite, microsegmentación de red para aislar servidores de HCE, y despliegue corporativo de solución EDR con aislamiento de endpoints en tiempo real.

---

### 2. Riesgo ID 1005: Robo de credenciales administrativas por correos de suplantación
* **Descripción:** Campañas de ingeniería social y phishing dirigidas a personal administrativo, de facturación y jefes de guardia para capturar credenciales de acceso a la red interna, sistemas de liquidación con obras sociales o cuentas con privilegios de Active Directory.
* **Categoría:** Confidencialidad e Integridad.
* **Activos Afectados:**
  * Directorio Activo (AD / Servidor de Dominio).
  * Cuentas de correo institucional de los 120 empleados.
  * Módulo de facturación y convenios de obras sociales/prepagas.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (4 - Alta):** El personal administrativo y de mesa de entradas recibe cientos de correos con adjuntos (estudios médicos externos, autorizaciones de prepagas, comprobantes). La tasa de clics en enlaces sospechosos sin entrenamiento es alta.
  * **Impacto (4 - Crítico):** El acceso ilegítimo de un atacante con credenciales válidas permite el movimiento lateral no detectado, exfiltración masiva de bases de datos de pacientes para posterior extorsión y modificación fraudulenta de datos bancarios de facturación.
* **Nivel de Riesgo Inmanente:** **6.4 (Medio-Alto / Naranja)**.
* **Controles Existentes:** Filtro antispam nativo provisto por el proveedor de correo y contraseñas simples sin renovación obligatoria.
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Dr. Roberto Sánchez / Laura Gómez (Information Security).
* **Plan de Acción Vinculado:** Implementación obligatoria de autenticación multifactor (MFA/2FA) para el acceso al correo institucional y VPN, reforzamiento de registros SPF/DKIM/DMARC en el servidor de correo, y programa permanente de simulaciones y concientización sobre phishing para los 120 colaboradores.

---

### 3. Riesgo ID 1003: Pérdida de trazabilidad por cuentas compartidas en consultorios
* **Descripción:** Práctica operativa en la cual médicos de guardia, enfermeros y secretarias de consultorios externos utilizan usuarios genéricos (ej: `consultorio1`, `guardia_tarde`) para agilizar el ingreso a las computadoras y al sistema de evolución de pacientes.
* **Categoría:** Integridad, Confidencialidad y Cumplimiento Legal.
* **Activos Afectados:**
  * Sistema de Historias Clínicas Electrónicas (HCE).
  * Trazabilidad médico-legal de evoluciones, indicaciones de medicamentos e ingresos/egresos de pacientes.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (4 - Alta):** Es un hábito profundamente arraigado por la rotación constante del personal de guardia y la presión por atender ~800 pacientes diarios de forma célere.
  * **Impacto (3 - Moderado/Grave):** Destruye el no repudio: ante un error médico o prescripción errónea que derive en mala praxis o demanda judicial, es técnicamente imposible determinar qué profesional realizó la modificación. Incumple directamente el marco regulatorio médico y de auditoría.
* **Nivel de Riesgo Inmanente:** **6.0 (Medio / Naranja)**.
* **Controles Existentes:** Bloqueo de sesión por inactividad tras 30 minutos (tiempo excesivo para un box de atención médica compartida).
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Dr. Roberto Sánchez (Dirección Médica).
* **Plan de Acción:** Migración a autenticación ágil mediante tarjetas de proximidad (RFID/NFC) vinculadas a la credencial médica individual (tap-in / tap-out), cierre de sesión inmediato al retirar la tarjeta y sanción disciplinaria por uso compartido de claves.

---

### 4. Riesgo ID 1002: Interrupción del centro de datos por fallo eléctrico y climático
* **Descripción:** Interrupción intempestiva del suministro eléctrico de red o avería en el sistema de aire acondicionado de precisión del centro de cómputos de la clínica, provocando caída en caliente de los servidores y riesgo de choque térmico en los discos duros.
* **Categoría:** Disponibilidad y Operatividad.
* **Activos Afectados:**
  * Sala de Racks / Datacenter central.
  * Servidores físicos y switches troncales de distribución de red.
  * Dispositivos UPS y climatizadores de sala.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (3 - Media):** Microcortes recurrentes en la red de distribución eléctrica urbana y sobrecarga en temporadas de alta temperatura estival.
  * **Impacto (4 - Crítico):** Una interrupción no programada apaga los servidores de soporte asistencial, quirófanos, farmacia y recepción, deteniendo de inmediato el flujo de atención de los 800 pacientes y corrompiendo transacciones en curso.
* **Nivel de Riesgo Inmanente:** **4.8 (Medio / Naranja)**.
* **Controles Existentes:** Dos unidades UPS de 3 kVA con baterías con más de 3 años de antigüedad sin reemplazo programado.
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Laura Gómez (Data Center & Storage).
* **Plan de Acción Vinculado:** Instalación y mantenimiento preventivo de un grupo electrógeno (generador diésel) de arranque automático por transferencia (ATS) dedicado para el datacenter, recambio del banco de baterías de la UPS para 30 minutos de autonomía y script de apagado ordenado automático (graceful shutdown).

---

### 5. Riesgo ID 1006: Interrupción del enlace de telecomunicaciones con el ISP
* **Descripción:** Corte de conectividad a internet provisto por el proveedor de telecomunicaciones por corte físico de fibra óptica o caída en su infraestructura troncal.
* **Categoría:** Disponibilidad.
* **Activos Afectados:**
  * Router de borde y firewall perimetral.
  * Enlace a sistemas de validación online de obras sociales y prepagas.
  * Acceso a recetas electrónicas nacionales y facturación electrónica con el fisco.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (3 - Media):** Obras viales en la vía pública o fallos periódicos del operador de telecomunicaciones local.
  * **Impacto (3 - Moderado):** La falta de validación online impide cobrar coseguros o autorizar prácticas médicas para los 800 pacientes diarios, generando largas colas en recepción y demoras administrativas severas.
* **Nivel de Riesgo Inmanente:** **3.6 (Medio-Bajo / Amarillo)**.
* **Controles Existentes:** Contrato de enlace único con un solo ISP corporativo.
* **Plan de Tratamiento:** **Mitigar y Transferir**.
* **Propietario del Riesgo:** Laura Gómez (IT Clínica).
* **Plan de Acción:** Contratación de un enlace secundario redundante por tecnología heterogénea (proveedor alternativo vía microondas o radioenlace con backup 4G/5G) y renegociación de SLA contractual con penalizaciones por caída superior a 2 horas anuales.

---

### 6. Riesgo ID 1004: Corrupción de datos y daño de almacenamiento en base de datos
* **Descripción:** Fallo de hardware en los arreglos de discos (RAID degradado no advertido) o inconsistencias a nivel de motor de base de datos durante operaciones de mantenimiento nocturnas, provocando pérdida de integridad o tablas huérfanas en la HCE.
* **Categoría:** Integridad y Disponibilidad.
* **Activos Afectados:**
  * Controladora RAID y discos SAS/SSD del almacenamiento principal.
  * Base de datos relacional de pacientes y registros clínicos.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (2 - Baja):** Los sistemas cuentan con redundancia RAID 5, aunque sin monitoreo activo de alertas de fallo inminente (S.M.A.R.T.).
  * **Impacto (4 - Crítico):** Datos de laboratorio o diagnósticos desarticulados de las fichas de los pacientes impiden decisiones clínicas seguras y requieren restauración de emergencia.
* **Nivel de Riesgo Inmanente:** **3.2 (Bajo-Medio / Amarillo)**.
* **Controles Existentes:** Arreglo de discos RAID básico en el servidor de base de datos.
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Laura Gómez (Data Center & Storage).
* **Plan de Acción:** Migración a RAID 6 o RAID 10 con disco hot-spare, configuración de monitoreo SNMP para fallo de hardware con alertas automáticas y verificación periódica automatizada de integridad de checksums y restauración de backups.

---

### 7. Riesgo ID 1007: Sustracción de notebooks en áreas de atención y recepción
* **Descripción:** Hurto de computadoras portátiles o tablets asignadas a personal de triaje, mesa de entrada o mostradores de atención ambulatoria debido al alto tránsito público de personas (800 pacientes y acompañantes diarios).
* **Categoría:** Confidencialidad y Disponibilidad (Seguridad Patrimonial).
* **Activos Afectados:**
  * Laptops y terminales móviles en puestos de atención al público.
  * Datos temporales en caché local de navegadores y credenciales recordadas.
* **Evaluación Cuali-Cuantitativa:**
  * **Probabilidad (3 - Media):** Ambientes públicos con flujo constante de personas y distracciones habituales en recepción.
  * **Impacto (2 - Menor):** Pérdida del valor del hardware ($500 - $1.000 USD por equipo); si el disco no está cifrado, existe riesgo de fuga de datos de pacientes abiertos en sesión.
* **Nivel de Riesgo Inmanente:** **2.4 (Bajo / Amarillo)**.
* **Controles Existentes:** Cámaras de videovigilancia (CCTV) en pasillos y recepciones.
* **Plan de Tratamiento:** **Mitigar**.
* **Propietario del Riesgo:** Laura Gómez / Responsable de Seguridad Patrimonial.
* **Plan de Acción:** Aseguramiento físico mediante cables con cerradura de seguridad Kensington a los escritorios, cifrado total de disco obligatorio con BitLocker (claves custodiadas en servidor central) y bloqueo automático de pantalla tras 2 minutos de inactividad.

