# Registro de Riesgos — Clínica Privada "Centro Médico del Valle"

> Documento de trabajo que respalda la carga de riesgos en SimpleRisk (Parte B del TP).
> Contexto: clínica privada de **120 empleados**, ~**800 pacientes/día**, que maneja
> **historias clínicas digitales, datos de obras sociales y facturación**. Recientemente
> sufrió una **auditoría externa** que identificó debilidades en la gestión de riesgos.

## Metodología de valoración

Se utiliza la matriz clásica **Probabilidad × Impacto** de SimpleRisk, con escalas 1–5
(idénticas a la plantilla A03 de la cátedra) para mantener consistencia entre ambos trabajos.

**Escala de Probabilidad (P):** 1 Raro · 2 Improbable · 3 Posible · 4 Probable · 5 Casi seguro
**Escala de Impacto (I):** 1 Insignificante · 2 Menor · 3 Moderado · 4 Mayor · 5 Catastrófico

**Nivel de riesgo (P×I):** 1–4 Bajo · 5–9 Medio · 10–15 Alto · 16–25 Crítico

**Criterio de justificación:** las probabilidades se apoyan en evidencia del sector salud
—principal blanco de ataques según el *Verizon Data Breach Investigations Report (DBIR)*,
que año a año ubica a *Healthcare* entre las industrias más atacadas y con mayor peso del
"elemento humano" (phishing y errores) y del ransomware— y en el hecho de que una auditoría
externa **ya detectó debilidades**, lo que eleva la probabilidad de materialización mientras
no se implementen controles.

---

## Tabla resumen de riesgos

| ID  | Riesgo | Categoría | P | I | Valor | Nivel | Propietario |
|-----|--------|-----------|---|---|-------|-------|-------------|
| R01 | Ransomware sobre servidores de historias clínicas | Disponibilidad / Integridad | 4 | 5 | 20 | **Crítico** | Gerencia de TI |
| R02 | Exfiltración de datos de pacientes (PHI) | Confidencialidad | 3 | 5 | 15 | **Alto** | Responsable de Seguridad |
| R03 | Phishing dirigido al personal administrativo | Confidencialidad / Integridad | 4 | 4 | 16 | **Crítico** | Responsable de Seguridad |
| R04 | Ausencia de backups probados y plan de recuperación | Disponibilidad | 3 | 5 | 15 | **Alto** | Gerencia de TI |
| R05 | Accesos con privilegios excesivos y cuentas compartidas | Confidencialidad / Integridad / Legal | 4 | 3 | 12 | **Alto** | Administrador de Sistemas |
| R06 | Exposición de datos en la interfaz de facturación con obras sociales | Confidencialidad / Integridad | 3 | 4 | 12 | **Alto** | Jefe de Facturación |
| R07 | Incumplimiento de la Ley 25.326 de Protección de Datos Personales | Legal / Cumplimiento | 3 | 4 | 12 | **Alto** | Dirección Médica |
| R08 | Robo o pérdida de dispositivos sin cifrado | Confidencialidad | 3 | 3 | 9 | Medio | Administrador de Sistemas |
| R09 | Interrupción del servicio por falla de infraestructura sin redundancia | Disponibilidad / Operativo | 3 | 3 | 9 | Medio | Gerencia de TI |

**Distribución:** 2 Críticos · 5 Altos · 2 Medios · 0 Bajos (9 riesgos identificados).

---

## Detalle de cada riesgo

### R01 — Ransomware sobre servidores de historias clínicas
- **Descripción:** Cifrado malicioso de los servidores que alojan las historias clínicas
  digitales, dejando a la clínica sin acceso a información crítica para la atención de
  ~800 pacientes/día y con posible extorsión por rescate y publicación de datos.
- **Activos afectados:** Servidor de historias clínicas (HCE), base de datos MySQL/SQL Server,
  almacenamiento de estudios por imágenes, disponibilidad de la atención asistencial.
- **Probabilidad (4 – Probable):** El sector salud es uno de los más golpeados por ransomware
  a nivel mundial (DBIR); la criticidad de la atención hace que estas organizaciones tiendan
  a pagar, lo que las vuelve blanco preferente.
- **Impacto (5 – Catastrófico):** Paralización de la atención, riesgo para la vida de pacientes,
  pérdida potencial de datos, daño reputacional y legal severo.
- **Controles existentes:** Antivirus de escritorio básico; sin EDR ni segmentación de red.
- **Plan de tratamiento:** **Mitigar** → ver Plan de Acción PA-01.
- **Propietario:** Gerencia de TI.

### R02 — Exfiltración de datos de pacientes (PHI)
- **Descripción:** Acceso no autorizado y extracción de datos sensibles de salud
  (diagnósticos, estudios, datos de obra social) por atacante externo o interno.
- **Activos afectados:** Base de datos de pacientes, repositorio de estudios, credenciales.
- **Probabilidad (3 – Posible):** Existe superficie de exposición real (interfaces con obras
  sociales, accesos amplios); la auditoría detectó debilidades que lo facilitan.
- **Impacto (5 – Catastrófico):** Los datos de salud son categoría **sensible** (Ley 25.326):
  su fuga implica sanciones, demandas y daño reputacional grave.
- **Controles existentes:** Login con usuario/contraseña; sin cifrado en reposo ni DLP.
- **Plan de tratamiento:** **Mitigar** → ver Plan de Acción PA-02.
- **Propietario:** Responsable de Seguridad.

### R03 — Phishing dirigido al personal administrativo
- **Descripción:** Correos fraudulentos que engañan al personal para robar credenciales o
  ejecutar malware; principal vector de entrada de R01 y R02.
- **Activos afectados:** Credenciales, estaciones de trabajo administrativas, correo corporativo.
- **Probabilidad (4 – Probable):** El "elemento humano" participa en la mayoría de las brechas
  (DBIR); 120 empleados con baja concientización = superficie amplia y frecuente.
- **Impacto (4 – Mayor):** Compromiso de cuentas que habilita movimientos laterales, fraude en
  facturación y acceso a datos de pacientes.
- **Controles existentes:** Filtro antispam del proveedor de correo; sin capacitación formal ni MFA.
- **Plan de tratamiento:** **Mitigar** → ver Plan de Acción PA-03.
- **Propietario:** Responsable de Seguridad.

### R04 — Ausencia de backups probados y plan de recuperación
- **Descripción:** No existen copias de seguridad verificadas ni un plan de continuidad, por lo
  que un incidente (ransomware, falla de hardware) puede provocar pérdida definitiva de datos.
- **Activos afectados:** Historias clínicas, base de datos de facturación, configuración.
- **Probabilidad (3 – Posible):** La debilidad ya existe (confirmada por auditoría); la
  "materialización" depende de que ocurra el evento disparador.
- **Impacto (5 – Catastrófico):** Sin backup, un ransomware o falla mayor implica pérdida
  irreversible de información asistencial y legal.
- **Controles existentes:** Copias manuales esporádicas a disco externo, sin prueba de restauración.
- **Plan de tratamiento:** **Mitigar** (backups 3-2-1 y pruebas periódicas de restauración).
- **Propietario:** Gerencia de TI.

### R05 — Accesos con privilegios excesivos y cuentas compartidas
- **Descripción:** Usuarios con más permisos de los necesarios y cuentas compartidas entre
  personal, impidiendo trazabilidad y ampliando el impacto de un compromiso.
- **Activos afectados:** Sistema de HCE, base de datos, módulo de facturación.
- **Probabilidad (4 – Probable):** Práctica muy habitual en clínicas sin gestión de identidades;
  detectada como debilidad.
- **Impacto (3 – Moderado):** Facilita fraude interno y dificulta auditoría, aunque acotable.
- **Controles existentes:** Roles básicos del sistema, sin revisión periódica de accesos.
- **Plan de tratamiento:** **Mitigar** (RBAC con mínimo privilegio, baja de cuentas compartidas).
- **Propietario:** Administrador de Sistemas.

### R06 — Exposición de datos en la interfaz de facturación con obras sociales
- **Descripción:** La integración con obras sociales transmite datos de pacientes; interfaces
  mal configuradas o sin cifrado pueden exponer o alterar información.
- **Activos afectados:** Módulo de facturación, API/interfaz con obras sociales, datos de afiliados.
- **Probabilidad (3 – Posible):** Integraciones externas suelen tener configuraciones heredadas.
- **Impacto (4 – Mayor):** Fuga de datos de afiliados y errores de facturación con impacto económico.
- **Controles existentes:** Transmisión por VPN en algunos casos; sin inventario de interfaces.
- **Plan de tratamiento:** **Mitigar** (cifrado TLS extremo a extremo, validación y monitoreo).
- **Propietario:** Jefe de Facturación.

### R07 — Incumplimiento de la Ley 25.326 de Protección de Datos Personales
- **Descripción:** No cumplir las obligaciones legales sobre datos personales **sensibles**
  (salud), incluyendo registro de bases, medidas de seguridad y derechos de los titulares.
- **Activos afectados:** Todas las bases con datos de pacientes; reputación institucional.
- **Probabilidad (3 – Posible):** Brechas de cumplimiento frecuentes; la auditoría ya lo señaló.
- **Impacto (4 – Mayor):** Sanciones de la autoridad de aplicación, demandas y pérdida de confianza.
- **Controles existentes:** Consentimiento en admisión; sin política formal de datos ni DPO.
- **Plan de tratamiento:** **Mitigar** (programa de cumplimiento y designación de responsable).
- **Propietario:** Dirección Médica.

### R08 — Robo o pérdida de dispositivos sin cifrado
- **Descripción:** Notebooks, tablets o pendrives con datos de pacientes que se pierden o son
  robados y no están cifrados.
- **Activos afectados:** Datos locales de pacientes, credenciales cacheadas.
- **Probabilidad (3 – Posible):** Movilidad del personal médico y administrativo.
- **Impacto (3 – Moderado):** Fuga acotada al contenido del dispositivo.
- **Controles existentes:** Ninguno específico (sin cifrado de disco).
- **Plan de tratamiento:** **Mitigar** (cifrado de disco BitLocker/LUKS y MDM básico).
- **Propietario:** Administrador de Sistemas.

### R09 — Interrupción del servicio por falla de infraestructura sin redundancia
- **Descripción:** Caída de energía, hardware o red que deja sin sistema a la clínica por falta
  de redundancia y UPS adecuada.
- **Activos afectados:** Disponibilidad del HCE, turnos, facturación.
- **Probabilidad (3 – Posible):** Cortes de energía habituales; infraestructura sin redundancia.
- **Impacto (3 – Moderado):** Interrupción temporal de la atención, recuperable.
- **Controles existentes:** UPS parcial en sala de servidores.
- **Plan de tratamiento:** **Aceptar/Mitigar** (UPS dimensionada, generador, alta disponibilidad).
- **Propietario:** Gerencia de TI.

---

## Planes de acción (asociados a riesgos Alto/Crítico)

### PA-01 — Programa de defensa contra ransomware (R01)
- **Descripción:** Desplegar EDR en endpoints y servidores, segmentar la red (aislando la red
  clínica de la administrativa), aplicar parcheo mensual y hardening de servidores.
- **Fecha de vencimiento:** 90 días desde el inicio.
- **Responsable:** Gerencia de TI.
- **Presupuesto estimado:** USD 12.000 (licencias EDR + horas de implementación).
- **Estado inicial:** Planificado / No iniciado.

### PA-02 — Protección de datos de pacientes (R02)
- **Descripción:** Cifrado en reposo de la base de datos, control de acceso por mínimo privilegio,
  registro y monitoreo de accesos (logs) y reglas DLP básicas en salidas de correo.
- **Fecha de vencimiento:** 120 días desde el inicio.
- **Responsable:** Responsable de Seguridad.
- **Presupuesto estimado:** USD 8.000.
- **Estado inicial:** Planificado / No iniciado.

### PA-03 — Concientización y MFA contra phishing (R03)
- **Descripción:** Campaña de capacitación trimestral con simulacros de phishing y despliegue de
  autenticación multifactor (MFA) en correo y en el sistema clínico.
- **Fecha de vencimiento:** 60 días desde el inicio.
- **Responsable:** Responsable de Seguridad.
- **Presupuesto estimado:** USD 4.000.
- **Estado inicial:** En curso (piloto con área administrativa).

---

## Decisiones de diseño y supuestos del escenario

- Se asignó a la clínica el nombre ficticio **"Centro Médico del Valle"** para dar contexto.
- Se priorizó la tríada CIA con foco en **Confidencialidad** (datos sensibles de salud) y
  **Disponibilidad** (continuidad asistencial), por ser las más críticas en el rubro.
- Se mantuvieron las mismas escalas 1–5 que la plantilla A03 para reutilizar el análisis.
- Todos los usuarios, IPs y credenciales usados en SimpleRisk son **ficticios** (ver `usuarios.md`).
- **Verificación:** girasol (palabra clave de lectura completa del enunciado).
