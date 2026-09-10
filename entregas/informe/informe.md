# Informe Técnico de Gestión de Riesgos - Cátedra de Seguridad de Sistemas

## 1. Introducción y Alcance
El presente trabajo documenta la implementación de la herramienta SimpleRisk para la gestión de riesgos de una clínica privada que cuenta con 120 empleados y atiende aproximadamente 800 pacientes al día. El alcance abarca la infraestructura tecnológica, los sistemas de Historias Clínicas Electrónicas (HCE), los procesos de facturación/obras sociales y la continuidad operativa.

## 2. Configuración de SimpleRisk y Roles
Se definieron tres perfiles de usuario para garantizar la separación de funciones:
1. **`sec_admin` (Admin):** Administración de la plataforma.
2. **`analyst_med` (User):** Carga, análisis y planificación de mitigaciones.
3. **`auditor_ext` (Read-Only):** Auditoría e inspección de reportes.

## 3. Planes de Acción para Riesgos Altos y Críticos

### Plan 1: Despliegue de EDR y Segmentación de Red (Asociado a R01 - Ransomware)
* **Descripción:** Instalación de solución EDR en endpoints y servidores, junto con la segmentación por VLANs del servidor HCE.
* **Fecha de vencimiento:** 30/11/2026
* **Responsable:** Jefe de Infraestructura TI
* **Presupuesto Estimado:** $4,500 USD
* **Estado Inicial:** Planificado

### Plan 2: Implementación de MFA y Capacitación Antiphishing (Asociado a R02 - Phishing)
* **Descripción:** Configuración obligatoria de Autenticación de Doble Factor (MFA) para las 120 cuentas de correo y talleres de concientización.
* **Fecha de vencimiento:** 15/10/2026
* **Responsable:** Oficial de Seguridad (CISO)
* **Presupuesto Estimado:** $2,000 USD
* **Estado Inicial:** Aprobado

### Plan 3: Adquisición de UPS Redundante para Datacenter (Asociado a R07 - Energía)
* **Descripción:** Instalación de una UPS Online de 10kVA en el rack principal para absorber microcortes y dar autonomía.
* **Fecha de vencimiento:** 20/12/2026
* **Responsable:** Director de Mantenimiento
* **Presupuesto Estimado:** $6,000 USD
* **Estado Inicial:** En Cotización

---

## 4. Análisis Crítico: Comparación Metodológica

### SimpleRisk (Matriz $5 \times 5$) vs. FAIR (Factor Analysis of Information Risk)

* **Matriz Tradicional de SimpleRisk:**
  * **Ventajas:** Simplicidad, rapidez de despliegue, comprensión inmediata por parte de perfiles no técnicos.
  * **Desventajas:** La asignación de valores de probabilidad e impacto es altamente subjetiva. No mide las pérdidas en términos monetarios directos.
* **Metodología FAIR:**
  * **Ventajas:** Cuantifica el riesgo en valores financieros (pérdida esperada en USD/año) mediante modelado probabilístico y simulación Monte Carlo. Facilita justificar el ROI de controles ante el directorio.
  * **Desventajas:** Requiere un alto nivel de madurez organizacional, recolección exhaustiva de datos históricos y mayor tiempo de análisis.

**Conclusión:** Para la etapa actual de la clínica, la matriz semicuantitativa de SimpleRisk es la opción adecuada para construir el inventario inicial rápidamente. A futuro, FAIR puede complementarla para evaluar inversiones críticas de infraestructura.

---

## 5. Propuesta de Integración Externa
Para optimizar el tiempo de respuesta ante nuevos riesgos críticos identificados, se plantea la integración de SimpleRisk con **Slack / Microsoft Teams** mediante **Webhooks**.

* **Mecanismo:** Configurar las alertas salientes en SimpleRisk para que, ante la creación o elevación de un riesgo a nivel "Alto" o "Crítico" ($\ge 10$), el sistema envíe un payload JSON al canal de comunicación del equipo de respuesta a incidentes (`#seguridad-alertas`).
