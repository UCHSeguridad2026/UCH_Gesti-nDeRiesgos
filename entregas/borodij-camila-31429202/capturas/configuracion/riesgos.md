# Matriz Inicial de Riesgos - Clínica Privada

### Riesgo 1: Infección por Ransomware en Servidor de Historias Clínicas (HC)
* **Categoría:** Disponibilidad / Confidencialidad
* **Activos Afectados:** Base de Datos SQL, Servidor de Aplicación de HC
* **Probabilidad:** 4 (Alta - Incremento de ataques de phishing al personal administrativo)
* **Impacto:** 5 (Muy Alto - Parálisis operativa total y pérdida temporal de fichas médicas)
* **Nivel de Riesgo:** 20 (Riesgo Alto)
* **Controles Existentes:** Antivirus básico en endpoints
* **Plan de Tratamiento:** Mitigar (Implementación de backups inmutables EDR y segmentación de red)
* **Propietario:** Director de Tecnología (CTO)

---

### Riesgo 2: Exfiltración de Datos Personales y de Obras Sociales por Phishing
* **Categoría:** Confidencialidad / Legal
* **Activos Afectados:** Correos corporativos, Padrón de afiliados
* **Probabilidad:** 4 (Alta) | **Impacto:** 4 (Alto) | **Nivel de Riesgo:** 16 (Riesgo Alto)
* **Controles Existentes:** Filtro de SPAM estándar en servidor de correo
* **Plan de Tratamiento:** Mitigar (Despliegue de MFA obligatorio y concientización)
* **Propietario:** Oficial de Seguridad de la Información (CISO)

---

### Riesgo 3: Acceso No Autorizado a Historias Clínicas por Módulos sin MFA
* **Categoría:** Confidencialidad
* **Activos Afectados:** Portal Web de Médicos
* **Probabilidad:** 3 (Media) | **Impacto:** 5 (Muy Alto) | **Nivel de Riesgo:** 15 (Riesgo Alto)
* **Controles Existentes:** Autenticación por usuario y contraseña simple
* **Plan de Tratamiento:** Mitigar (Integración con proveedor de credenciales y MFA)
* **Propietario:** Jefe de Desarrollo de Software

---

### Riesgo 4: Interrupción de Servicios por Falla en Sistema Eléctrico sin UPS Adecuada
* **Categoría:** Disponibilidad
* **Activos Afectados:** Data Center Local, Routers de Quirófano
* **Probabilidad:** 3 (Media) | **Impacto:** 4 (Alto) | **Nivel de Riesgo:** 12 (Riesgo Medio)
* **Controles Existentes:** Grupo electrógeno para áreas críticas de la clínica
* **Plan de Tratamiento:** Mitigar (Adquisición e instalación de UPS redundantes)
* **Propietario:** Gerente de Infraestructura y Mantenimiento

---

### Riesgo 5: Indisponibilidad de Facturación Electrónica con Obras Sociales
* **Categoría:** Operativo / Financiero
* **Activos Afectados:** API Gateway de Facturación, Web Services AFIP/Obras Sociales
* **Probabilidad:** 3 (Media) | **Impacto:** 3 (Medio) | **Nivel de Riesgo:** 9 (Riesgo Medio)
* **Controles Existentes:** Reintento manual de peticiones
* **Plan de Tratamiento:** Aceptar (Asumir la demora operativa según SLAs del proveedor)
* **Propietario:** Jefe de Facturación

---

### Riesgo 6: Alteración de Registros Médicos por Mala Gestión de Permisos Internos
* **Categoría:** Integridad
* **Activos Afectados:** Base de Datos de Historias Clínicas
* **Probabilidad:** 2 (Baja) | **Impacto:** 4 (Alto) | **Nivel de Riesgo:** 8 (Riesgo Medio)
* **Controles Existentes:** Autenticación básica
* **Plan de Tratamiento:** Mitigar (Auditoría de roles y matriz RBAC estricta)
* **Propietario:** Administrador de Base de Datos

---

### Riesgo 7: Multas por Incumplimiento de la Ley de Protección de Datos Personales
* **Categoría:** Legal / Regulatorio
* **Activos Afectados:** Repositorio Documental y Base de Datos
* **Probabilidad:** 2 (Baja) | **Impacto:** 4 (Alto) | **Nivel de Riesgo:** 8 (Riesgo Medio)
* **Controles Existentes:** Cláusulas de confidencialidad en contratos
* **Plan de Tratamiento:** Transferir (Contratación de seguro de responsabilidad cibernética)
* **Propietario:** Apoderado Legal / Director Risk Management
