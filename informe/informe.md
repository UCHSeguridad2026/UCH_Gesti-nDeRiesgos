
# Informe de Gestión de Riesgos - Clínica Privada

**Alumno:** Fabricio Hugo Funes (DNI: 45447810)  
**Materia:** Seguridad - Gestión de Riesgos  
**Herramienta:** SimpleRisk  

## 1. Introducción y Objetivo General
El presente trabajo práctico tiene como objetivo familiarizar a los estudiantes con las funcionalidades de SimpleRisk como herramienta de gestión de riesgos en una organización. El escenario plantea una clínica privada de 120 empleados que atiende 800 pacientes por día, manejando historias clínicas digitales, datos de obras sociales y facturación.

## 2. Escenario Real: Registro de los 7 Riesgos de la Clínica

1. **R01: Ransomware en base de datos clínica**
   - **Descripción:** Ataque de software malicioso que cifra los registros de la base de datos de pacientes, exigiendo un rescate económico.
   - **Categoría:** Integridad / Disponibilidad (Sensitive Data Management)
   - **Activos afectados:** Base de Datos H.C., Servidor principal
   - **Probabilidad:** 5 (Almost Certain) - **Impacto:** 5 (Catastrophic) -> **Nivel: Alto (10)**
   - **Controles existentes:** Antivirus básico.
   - **Plan de tratamiento:** Mitigar (Implementar respaldos inmutables y segmentación).
   - **Propietario:** Fabricio Hugo Funes

2. **R02: Robo de credenciales médicas - Phishing**
   - **Descripción:** Campaña de suplantación de identidad dirigida al personal médico para robar credenciales de acceso al portal.
   - **Categoría:** Confidencialidad (Access Management)
   - **Activos afectados:** Credenciales de usuarios, Portal Médico
   - **Probabilidad:** 4 (Almost Certain) - **Impacto:** 4 (Major) -> **Nivel: Alto (8)**
   - **Controles existentes:** Filtro de spam básico.
   - **Plan de tratamiento:** Mitigar (Implementar MFA y capacitación).
   - **Propietario:** Fabricio Hugo Funes

3. **R03: Caída del enlace de internet principal**
   - **Descripción:** Interrupción del servicio del proveedor ISP que impide la validación en línea con obras sociales y facturación.
   - **Categoría:** Disponibilidad (Third-Party Management)
   - **Activos afectados:** Conectividad, Sistema de Facturación
   - **Probabilidad:** 4 (Likely) - **Impacto:** 4 (Major) -> **Nivel: Medio (6.4)**
   - **Controles existentes:** Conexión única ISP.
   - **Plan de tratamiento:** Mitigar (Contratar enlace redundante).
   - **Propietario:** Fabricio Hugo Funes

4. **R04: Acceso no autorizado a red Wi-Fi interna**
   - **Descripción:** Pacientes o visitantes externos acceden a la red administrativa debido al uso de una contraseña compartida y débil.
   - **Categoría:** Confidencialidad (Technical Vulnerability Management)
   - **Activos afectados:** Red Wi-Fi Administrativa
   - **Probabilidad:** 4 (Almost Certain) - **Impacto:** 3 (Moderate) -> **Nivel: Medio (6)**
   - **Controles existentes:** Contraseña compartida genérica.
   - **Plan de tratamiento:** Mitigar (Implementar WPA2/3 Enterprise 802.1X).
   - **Propietario:** Fabricio Hugo Funes

5. **R05: Pérdida de datos por falla de hardware del servidor**
   - **Descripción:** Fallo físico en el almacenamiento del servidor principal sin redundancia.
   - **Categoría:** Disponibilidad (Physical Security)
   - **Activos afectados:** Servidor de Base de Datos
   - **Probabilidad:** 2 (Unlikely) - **Impacto:** 5 (Catastrophic) -> **Nivel: Medio (4)**
   - **Controles existentes:** Almacenamiento simple.
   - **Plan de tratamiento:** Mitigar (Configurar arreglos RAID y respaldos periódicos).
   - **Propietario:** Fabricio Hugo Funes

6. **R06: Filtración accidental de datos por correo**
   - **Descripción:** Envío erróneo de historias clínicas o datos de facturación a destinatarios externos por error humano.
   - **Categoría:** Confidencialidad (Sensitive Data Management)
   - **Activos afectados:** Datos de pacientes (PHI)
   - **Probabilidad:** 3 (Credible) - **Impacto:** 3 (Moderate) -> **Nivel: Bajo (3.6)**
   - **Controles existentes:** Ninguno.
   - **Plan de tratamiento:** Mitigar (Establecer políticas DLP en correo electrónico).
   - **Propietario:** Fabricio Hugo Funes

7. **R07: Daño físico a equipos por inundación/incendio**
   - **Descripción:** Daños a los servidores debido a incidentes físicos en el centro de datos local.
   - **Categoría:** Disponibilidad (Environmental Resilience)
   - **Activos afectados:** Infraestructura Física, Servidores
   - **Probabilidad:** 1 (Remote) - **Impacto:** 5 (Catastrophic) -> **Nivel: Bajo (2)**
   - **Controles existentes:** Extintores portátiles.
   - **Plan de tratamiento:** Aceptar / Monitorear.
   - **Propietario:** Fabricio Hugo Funes

## 3. Planes de Acción Asociados (Riesgos Altos)
1. **PA-01: Despliegue de Respaldos Inmutables (R01)**
   - *Fecha límite:* 30/10/2026
   - *Responsable:* Área de Infraestructura
   - *Presupuesto:* $1,200 USD
   - *Estado inicial:* New / Open
2. **PA-02: Implementación de MFA Institucional (R02)**
   - *Fecha límite:* 15/11/2026
   - *Responsable:* Seguridad Informática
   - *Presupuesto:* $800 USD
   - *Estado inicial:* New / Open
3. **PA-03: Redundancia de Enlace de Internet (R03)**
   - *Fecha límite:* 30/11/2026
   - *Responsable:* Redes y Comunicaciones
   - *Presupuesto:* $500 USD
   - *Estado inicial:* New / Open

## 4. Análisis Crítico y Profundización (Parte C)
- **Comparación Metodológica (SimpleRisk vs. NIST SP 800-30):** 
  - SimpleRisk destaca por su agilidad, rapidez de despliegue y una interfaz web intuitiva basada en una matriz clásica de probabilidad e impacto, ideal para organizaciones que necesitan un registro operativo inicial rápido.
  - NIST SP 800-30 ofrece un enfoque altamente granular, formal y exhaustivo para la evaluación detallada de amenazas, vulnerabilidades y el impacto operativo, siendo más adecuado para entornos con alta madurez en cumplimiento normativo.
- **Integración Tecnológica:** Se documenta la integración de SimpleRisk mediante webhooks hacia herramientas externas de tickets o mensajería (como Slack, Jira o sistemas de SIEM) para notificar de forma automatizada la apertura de riesgos críticos a los equipos de respuesta.
