# Registro de Riesgos — Clínica Privada "Vida Sana" (escenario simulado)

> TP SimpleRisk — Seguridad de Sistemas — Cangialosi Leonardo Arturo — LU 31041361 — Comisión G

## Contexto del escenario

Clínica privada de **120 empleados** que atiende **~800 pacientes/día** y maneja
**historias clínicas electrónicas (HCE)**, **datos de obras sociales** y **facturación**.
La clínica acaba de atravesar una **auditoría externa** que identificó debilidades en su
gestión de riesgos. Este documento constituye el **registro inicial de riesgos** cargado en
SimpleRisk.

## Metodología de valoración

Se utiliza la matriz clásica **Probabilidad × Impacto** de SimpleRisk, con escalas 1–5
alineadas a la *Plantilla de Matriz de Riesgos* de la cátedra:

**Probabilidad:** 1 Raro · 2 Improbable · 3 Posible · 4 Probable · 5 Casi seguro
**Impacto:** 1 Insignificante · 2 Menor · 3 Moderado · 4 Mayor · 5 Catastrófico

**Niveles de riesgo (Valor = P × I):**

| Nivel | Rango | Acción requerida |
|-------|-------|------------------|
| 🟢 Bajo | 1 – 4 | Monitorear. Puede aceptarse. |
| 🟡 Medio | 5 – 9 | Plan de acción a mediano plazo. |
| 🟠 Alto | 10 – 15 | Tratamiento prioritario a corto plazo. |
| 🔴 Crítico | 16 – 25 | Acción inmediata. Escalar a dirección. |

Las probabilidades se justifican, cuando aplica, con datos del **Verizon Data Breach
Investigations Report (DBIR)** y con el hecho concreto de que el sector salud es uno de los
más atacados y regulados. El escenario asume el marco legal argentino: **Ley 25.326 de
Protección de los Datos Personales (Habeas Data)** y el deber de **secreto médico**.

---

## Inventario de activos (resumen)

| ID | Activo | Tipo | Clasificación | Criticidad |
|----|--------|------|---------------|------------|
| A01 | Servidor y base de datos de Historia Clínica Electrónica (HCE) | Software/Información | Restringida | Alta |
| A02 | Datos de obras sociales y facturación | Información | Confidencial | Alta |
| A03 | Sala de servidores / datacenter on-premise | Hardware/Físico | Interna | Alta |
| A04 | Red interna (incluye equipos médicos conectados) | Red | Interna | Alta |
| A05 | Estaciones de trabajo y notebooks del personal | Hardware | Interna | Media |
| A06 | Cuentas de correo y credenciales de usuarios | Información | Confidencial | Alta |
| A07 | Backups de la base de datos | Información | Restringida | Alta |

---

## Riesgos identificados

### R01 — Ransomware sobre las historias clínicas digitales
- **Descripción:** Cifrado malicioso de la base de datos de HCE y de los backups, dejando a la
  clínica sin acceso a las historias clínicas y exigiendo un rescate.
- **Categoría:** Disponibilidad / Integridad
- **Activos afectados:** A01, A07, A04
- **Probabilidad:** **4 — Probable.** El sector salud es uno de los más golpeados por
  ransomware a nivel mundial (el DBIR ubica al ransomware entre las principales acciones en
  brechas, y el healthcare entre los sectores más afectados). Sumado a sistemas legacy y a
  phishing frecuente, es esperable que ocurra.
- **Impacto:** **5 — Catastrófico.** Paraliza la atención de 800 pacientes/día, puede implicar
  pérdida definitiva de HCE, daño reputacional grave y responsabilidad legal por datos de salud.
- **Valor de riesgo:** 4 × 5 = **20 → 🔴 Crítico**
- **Controles existentes:** Backup diario a NAS local (sin pruebas de restauración); antivirus
  tradicional en algunos equipos.
- **Plan de tratamiento:** **Mitigar** — backups inmutables con estrategia 3-2-1 (copia
  off-site cifrada), EDR/antimalware moderno, segmentación de red, MFA y capacitación
  anti-phishing.
- **Propietario del riesgo:** Responsable de Seguridad de la Información (CISO) / Jefe de Sistemas.

### R02 — Acceso indebido / fuga de datos de pacientes por control de acceso deficiente
- **Descripción:** Personal que accede a historias clínicas que no le corresponden, o
  extracción no autorizada de datos, por falta de roles con mínimo privilegio y uso de cuentas
  compartidas.
- **Categoría:** Confidencialidad / Legal
- **Activos afectados:** A01, A02, A06
- **Probabilidad:** **4 — Probable.** Con 120 empleados, sin RBAC granular y con cuentas
  compartidas, el uso indebido de privilegios (*misuse*) es un patrón habitual en salud según el
  DBIR (alta proporción de incidentes por actores internos en el sector).
- **Impacto:** **4 — Mayor.** Violación del secreto médico, sanciones bajo Ley 25.326 y daño
  reputacional.
- **Valor de riesgo:** 4 × 4 = **16 → 🔴 Crítico**
- **Controles existentes:** Usuarios nominales parciales; sin revisión periódica de accesos.
- **Plan de tratamiento:** **Mitigar** — RBAC con mínimo privilegio, eliminación de cuentas
  compartidas, registro (logging) de accesos a HCE y revisión trimestral de permisos.
- **Propietario del riesgo:** Oficial de Protección de Datos / Sistemas.

### R03 — Phishing y robo de credenciales al personal administrativo
- **Descripción:** Correos fraudulentos que capturan credenciales o inducen a ejecutar malware,
  usados como puerta de entrada a ransomware o a fraude en facturación (BEC).
- **Categoría:** Confidencialidad / Operativo
- **Activos afectados:** A06, A02, A01
- **Probabilidad:** **5 — Casi seguro.** El elemento humano y el phishing son el vector inicial
  más frecuente de las brechas según el DBIR; el personal administrativo no es técnico y recibe
  gran volumen de correo externo (obras sociales, proveedores).
- **Impacto:** **4 — Mayor.** Habilita compromisos mayores (ransomware, fraude), robo de datos.
- **Valor de riesgo:** 5 × 4 = **20 → 🔴 Crítico**
- **Controles existentes:** Filtro antispam básico del proveedor de correo.
- **Plan de tratamiento:** **Mitigar** — MFA obligatorio, programa de concientización con
  simulacros de phishing, y protección de dominio de correo (SPF, DKIM, DMARC).
- **Propietario del riesgo:** Responsable de Seguridad de la Información.

### R04 — Pérdida de datos por backups no verificados
- **Descripción:** Los backups existen pero nunca se probó su restauración; ante un fallo de
  disco, corrupción o ataque, la recuperación podría fallar.
- **Categoría:** Disponibilidad / Integridad
- **Activos afectados:** A07, A01
- **Probabilidad:** **3 — Posible.** Un backup sin prueba de restore es una falla latente común;
  el disco/NAS puede fallar o corromperse.
- **Impacto:** **5 — Catastrófico.** Pérdida irrecuperable de historias clínicas.
- **Valor de riesgo:** 3 × 5 = **15 → 🟠 Alto**
- **Controles existentes:** Backup diario local, sin copia off-site ni pruebas de restauración.
- **Plan de tratamiento:** **Mitigar** — estrategia 3-2-1, copia off-site cifrada y pruebas de
  restauración mensuales documentadas.
- **Propietario del riesgo:** Jefe de Sistemas.

### R05 — Indisponibilidad por falla eléctrica o infraestructura del datacenter
- **Descripción:** Cortes de energía o incidentes ambientales (incendio, inundación) en la sala
  de servidores que interrumpen el acceso a HCE y a los sistemas clínicos.
- **Categoría:** Disponibilidad / Operativo
- **Activos afectados:** A03, A01, A04
- **Probabilidad:** **3 — Posible.** Cortes de luz habituales, un solo UPS antiguo y sala de
  servidores mal ubicada respecto de riesgos físicos.
- **Impacto:** **4 — Mayor.** La atención se detiene sin acceso a historias clínicas.
- **Valor de riesgo:** 3 × 4 = **12 → 🟠 Alto**
- **Controles existentes:** Un UPS antiguo sin mantenimiento.
- **Plan de tratamiento:** **Mitigar** — UPS correctamente dimensionado + grupo electrógeno,
  reubicación de la sala de servidores lejos de fuentes de incendio (cocinas) e inundación
  (piletas/tanques), y monitoreo ambiental (temperatura/humedad/humo).
- **Propietario del riesgo:** Jefe de Infraestructura / Mantenimiento.

### R06 — Incumplimiento normativo de protección de datos de salud
- **Descripción:** Falta de políticas formales de privacidad y de tratamiento de datos
  sensibles, ya señalada por la auditoría externa, que expone a sanciones legales.
- **Categoría:** Legal / Cumplimiento
- **Activos afectados:** A01, A02
- **Probabilidad:** **3 — Posible.** La auditoría ya identificó debilidades; sin política formal
  el hallazgo regulatorio es concreto.
- **Impacto:** **4 — Mayor.** Multas bajo Ley 25.326, acciones legales de pacientes y riesgo
  sobre la habilitación.
- **Valor de riesgo:** 3 × 4 = **12 → 🟠 Alto**
- **Controles existentes:** Consentimientos informados en papel; sin política digital.
- **Plan de tratamiento:** **Mitigar + Transferir (parcial)** — política de protección de datos,
  designación de un DPO, cláusulas de confidencialidad con proveedores y contratación de un
  **seguro de ciberriesgo** para transferir parte del impacto económico.
- **Propietario del riesgo:** Dirección Médica / Legales.

### R07 — Propagación de malware por equipos no gestionados en red plana
- **Descripción:** Equipos médicos con sistemas operativos obsoletos y sin parches, junto a una
  red interna sin segmentar, permiten la propagación lateral de malware.
- **Categoría:** Integridad / Disponibilidad
- **Activos afectados:** A04, A05, A01
- **Probabilidad:** **4 — Probable.** Equipos de diagnóstico con SO viejos no parchables y red
  plana son un foco de propagación habitual.
- **Impacto:** **3 — Moderado.** Interrupciones parciales y foco de contagio hacia sistemas
  clínicos.
- **Valor de riesgo:** 4 × 3 = **12 → 🟠 Alto**
- **Controles existentes:** Antivirus en algunas estaciones de trabajo.
- **Plan de tratamiento:** **Mitigar** — segmentación de red (VLAN separada para equipos
  médicos), control de acceso a red (NAC) e inventario/gestión de activos.
- **Propietario del riesgo:** Jefe de Sistemas / Redes.

### R08 — Robo o pérdida de equipos con datos de pacientes
- **Descripción:** Notebooks del personal médico o discos de backup físicos sin cifrado que, ante
  robo o extravío, exponen datos de pacientes.
- **Categoría:** Confidencialidad
- **Activos afectados:** A05, A07
- **Probabilidad:** **3 — Posible.** Movilidad del personal y ausencia de cifrado de disco.
- **Impacto:** **3 — Moderado.** Exposición de datos de un subconjunto de pacientes.
- **Valor de riesgo:** 3 × 3 = **9 → 🟡 Medio**
- **Controles existentes:** Ninguno formal.
- **Plan de tratamiento:** **Mitigar** — cifrado de disco (FileVault/BitLocker), gestión de
  dispositivos (MDM) y política de escritorio/pantalla limpios.
- **Propietario del riesgo:** Responsable de Seguridad / RRHH.

---

## Matriz de calor — riesgos ubicados

```
IMPACTO →           1        2        3        4        5
P  5 Casi seguro                              R03(20)
R  4 Probable                        R07(12)  R01/R02(16-20)
O  3 Posible                         R08(9)   R05/R06(12) R04(15)
B  2 Improbable
   1 Raro
```

## Resumen de resultados (riesgo inherente)

| Nivel | Cantidad | Riesgos | % |
|-------|----------|---------|---|
| 🔴 Crítico | 3 | R01, R02, R03 | 37,5 % |
| 🟠 Alto | 4 | R04, R05, R06, R07 | 50 % |
| 🟡 Medio | 1 | R08 | 12,5 % |
| 🟢 Bajo | 0 | — | 0 % |
| **Total** | **8** | | **100 %** |

El perfil (mayoría Crítico/Alto) es coherente con una organización que **acaba de reprobar una
auditoría** y presenta controles inmaduros.

---

## Planes de acción (riesgos de nivel alto/crítico)

### PA-01 — Blindaje anti-ransomware y backups inmutables *(mitiga R01, R04)*
- **Descripción:** Implementar estrategia de backup 3-2-1 con al menos una copia inmutable y
  off-site cifrada, desplegar EDR en servidores y endpoints, y establecer pruebas de
  restauración mensuales.
- **Fecha de vencimiento:** 60 días desde el inicio.
- **Responsable:** Jefe de Sistemas.
- **Presupuesto estimado:** USD 8.000 (solución de backup + licencias EDR año 1).
- **Estado inicial:** *Planificado / No iniciado.*

### PA-02 — MFA + programa de concientización anti-phishing *(mitiga R03, R01)*
- **Descripción:** Habilitar MFA obligatorio en correo y sistemas clínicos, configurar
  SPF/DKIM/DMARC, y ejecutar un programa trimestral de concientización con simulacros de phishing.
- **Fecha de vencimiento:** 45 días desde el inicio.
- **Responsable:** Responsable de Seguridad de la Información.
- **Presupuesto estimado:** USD 3.500 (plataforma de MFA + concientización, año 1).
- **Estado inicial:** *Planificado / No iniciado.*

### PA-03 — Control de acceso con mínimo privilegio y trazabilidad *(mitiga R02)*
- **Descripción:** Definir roles (RBAC) sobre la HCE, eliminar cuentas compartidas, activar el
  registro de accesos a datos de pacientes y revisar permisos trimestralmente.
- **Fecha de vencimiento:** 90 días desde el inicio.
- **Responsable:** Oficial de Protección de Datos + Sistemas.
- **Presupuesto estimado:** USD 2.000 (configuración + horas de consultoría).
- **Estado inicial:** *En análisis.*

---

## Tratamiento y riesgo residual (estimado tras los planes)

| Riesgo | Estrategia | P res. | I res. | Valor res. | Nivel res. |
|--------|-----------|:------:|:------:|:----------:|:----------:|
| R01 | Mitigar | 2 | 4 | 8 | 🟡 Medio |
| R02 | Mitigar | 2 | 4 | 8 | 🟡 Medio |
| R03 | Mitigar | 3 | 3 | 9 | 🟡 Medio |
| R04 | Mitigar | 2 | 4 | 8 | 🟡 Medio |
| R05 | Mitigar | 2 | 3 | 6 | 🟡 Medio |
| R06 | Mitigar+Transferir | 2 | 3 | 6 | 🟡 Medio |
| R07 | Mitigar | 2 | 3 | 6 | 🟡 Medio |
| R08 | Mitigar | 1 | 3 | 3 | 🟢 Bajo |

Los planes reducen todo el registro a nivel **Medio o Bajo**: ningún riesgo residual permanece
en Alto o Crítico, lo que constituye el objetivo del tratamiento.

---

> **Nota de autoría:** los valores de probabilidad e impacto reflejan un criterio profesional
> aplicado al escenario. Deben revisarse y ajustarse según el juicio del analista antes de la
> entrega final.
