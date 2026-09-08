# Informe Técnico de Gestión de Riesgos - SimpleRisk

**Institución:** Universidad Champagnat  
**Cátedra:** Seguridad de Sistemas (4to Año)  
**Estudiante:** Facundo Del Valle (LU: 31057801)  
**Fecha:** 2026-08-30  

---

## 1. Introducción y Contexto Organizacional
El presente informe documenta el proceso de implantación del sistema de gestión de riesgos de seguridad de la información para una **clínica médica privada** compuesta por:
* **Personal:** 120 empleados (personal médico, enfermería, administrativo y directivo).
* **Volumen de atención:** 800 pacientes diarios.
* **Activos críticos:** Historias Clínicas Electrónicas (HCE), portal web de turnos, sistemas de facturación y liquidación con obras sociales.
* **Contexto de negocio:** Reciente auditoría externa que identificó debilidades en la gestión y trazabilidad de riesgos tecnológicos.

---

## 2. Parte A: Configuración de la Plataforma
* **Despliegue:** Se implementó una instancia de SimpleRisk contenerizada sobre Docker en un entorno Linux, garantizando reproducibilidad y aislamiento de servicios mediante el script `entorno/setup.sh`.
* **Usuarios y Control de Acceso:** Se definieron perfiles bajo el principio de mínimo privilegio:
  * `admin_sec`: Administrador global para gobierno de seguridad.
  * `analista_riesgos`: Analista con permisos de carga y planificación de mitigaciones.
  * `auditor_ext`: Auditor con permisos de solo lectura para fiscalización externa.

---

## 3. Parte B: Matriz de Riesgos y Justificaciones

### Criterio de Evaluación (Escala 1 a 5)
* **Probabilidad (P):** 1 (Muy Rara), 2 (Poco Probable), 3 (Posible), 4 (Probable / Frecuente), 5 (Casi Segura). Justificada en base a estadísticas de incidentes del sector salud (Verizon DBIR) y factores humanos.
* **Impacto (I):** 1 (Insignificante), 2 (Menor), 3 (Moderado), 4 (Mayor), 5 (Catastrófico / Riesgo de Vida o Parálisis Total).

### Resumen de Riesgos Evaluados

| ID | Riesgo Identificado | Cat. | P | I | Nivel | Tratamiento |
|---|---|---|:---:|:---:|:---:|---|
| **R1** | Ransomware en Servidor de HCE | Disp. / Conf. | 4 | 5 | **Crítico (20)** | **Mitigar:** Backups inmutables WORM, segmentación de VLAN y EDR. |
| **R2** | Filtración por Phishing a Empleados | Conf. / Legal | 4 | 5 | **Crítico (20)** | **Mitigar:** MFA obligatorio en correo/HCE y concientización continua. |
| **R3** | Falla en Facturación con Obras Sociales | Oper. / Integ. | 3 | 4 | **Medio-Alto (12)** | **Mitigar:** Mecanismo transaccional asíncrono y monitoreo de APIs. |
| **R4** | Acceso a Terminales Desatendidas | Confidencialidad | 4 | 3 | **Medio (12)** | **Mitigar:** Bloqueo por inactividad a 2 min y credenciales físicas. |
| **R5** | Pérdida de Enlace de Internet | Disponibilidad | 3 | 3 | **Medio (9)** | **Mitigar/Transferir:** Enlace secundario 4G/5G con failover automático. |
| **R6** | Fuga de Información Contable Interna | Confidencialidad | 2 | 4 | **Medio (8)** | **Mitigar:** DLP en endpoints y auditoría de exportaciones masivas. |
| **R7** | Explotación Web en Portal de Turnos | Int. / Disp. | 3 | 3 | **Medio (9)** | **Mitigar:** WAF perimetral, pentesting y sanitización de inputs. |

---

## 4. Parte C: Análisis Crítico y Profundización

### 4.1 Comparación Metodológica: SimpleRisk (Matriz Cualitativa) vs. FAIR (*Factor Analysis of Information Risk*)

#### Enfoque SimpleRisk (Matriz P x I)
* **Ventajas:** Rápida adopción, interfaz visual intuitiva, baja curva de aprendizaje y comprensión inmediata por personal no técnico.
* **Desventajas:** Alta subjetividad al asignar números del 1 al 5 ("¿Qué diferencia real hay entre impacto 4 y 5?"), efecto de agrupación (muchos riesgos caen en 'Medio') y falta de estimación financiera real.
* **Contexto ideal:** Fases iniciales de madurez de seguridad, pymes y priorización ágil de incidentes cotidianos.

#### Enfoque FAIR (Cuantitativo)
* **Ventajas:** Modela el riesgo como una distribución probabilística en términos económicos ($/año en pérdida esperada), separando la frecuencia de eventos de amenaza (*Threat Event Frequency*) de la magnitud de la pérdida (*Loss Magnitude*).
* **Desventajas:** Requiere datos históricos precisos, mayor tiempo de análisis y herramientas estadísticas complejas.
* **Contexto ideal:** Presentación de justificación de inversiones ante juntas directivas, sector bancario/financiero y cálculo de pólizas de ciberseguro.

---

### 4.2 Integración Externa: SimpleRisk con Jira Software

#### Arquitectura de la Integración
Para organizaciones con equipos ágiles de desarrollo e infraestructura, SimpleRisk se conecta bidireccionalmente con **Jira Software** mediante Webhooks y API REST:
[200~1. **Flujo de Creación:** Al planificar una mitigación en SimpleRisk (ej. "Desplegar MFA"), el sistema envía un payload JSON al endpoint de Jira creando automáticamente una tarea en el backlog del equipo de infraestructura.
2. **Sincronización:** Cuando el responsable en Jira marca la tarea como *Done*, un Webhook notifica a SimpleRisk actualizando el estado del plan de mitigación a *Implemented*.
3. **Beneficio:** Elimina el desfase entre la planificación de seguridad y la ejecución técnica real.
EOF~
cat << 'EOF' > reporte-ejecutivo/reporte.md
# INFORME EJECUTIVO DE RIESGOS DE CIBERSEGURIDAD
**Dirigido a:** Directorio y Gerencia General  
**Organización:** Clínica Privada  
**Fecha:** Agosto 2026  
**Elaborado por:** Área de Seguridad de la Información  

---

## 1. Resumen Ejecutivo
Luego de la reciente auditoría externa, se llevó a cabo una evaluación integral sobre la postura de seguridad y continuidad operativa de la clínica (120 colaboradores y 800 pacientes diarios). 

Se relevaron **7 riesgos prioritarios**, detectando que el **57% de los activos críticos** presenta un nivel de exposición que requiere asignación presupuestaria urgente, principalmente en la protección de las Historias Clínicas Electrónicas (HCE) y la facturación médica.

---

## 2. Top 5 Riesgos por Criticidad
## 3. Estado de los Planes de Acción y Presupuesto

Se estructuraron 3 proyectos de mitigación para los riesgos de mayor impacto:

1. **Plan R1 - Resiliencia y Backups Inmutables (HCE):**
   * *Acción:* Despliegue de esquema 3-2-1 con tecnología WORM y EDR.
   * *Presupuesto estimado:* **USD 4.500** | *Plazo:* 30 días.
2. **Plan R2 - Control de Identidad y MFA Corporativo:**
   * *Acción:* Doble factor de autenticación para 120 empleados y taller de concientización.
   * *Presupuesto estimado:* **USD 1.800** | *Plazo:* 15 días.
3. **Plan R3 - Módulo Asíncrono de Obras Sociales:**
   * *Acción:* Caché transaccional para contingencia en mesa de entrada.
   * *Presupuesto estimado:* **USD 2.200** | *Plazo:* 45 días.

**Inversión Total Solicitada:** **USD 8.500**

---

## 4. Recomendaciones Prioritarias para el Directorio
1. **Aprobar de manera inmediata** los fondos para los Planes R1 y R2 para neutralizar el riesgo de secuestro y fuga de datos médicos.
2. **Instituir la política de bloqueo automático** de terminales en áreas públicas y consultorios.
3. **Establecer una revisión trimestral** del inventario de riesgos con reporte directo a la Dirección.
