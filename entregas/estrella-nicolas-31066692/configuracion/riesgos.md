# Registro de Riesgos — Clínica Privada

**Contexto:** Clínica privada de 120 empleados, ~800 pacientes/día, con historias clínicas electrónicas (HCE), datos de obras sociales y facturación tercerizada parcialmente.

---

## Riesgo 1 (ID SimpleRisk: 1002)

- **Nombre:** Ransomware en servidor de historias clínicas electrónicas
- **Descripción:** Un ataque de ransomware cifra el servidor donde se almacenan las HCE, impidiendo el acceso durante la atención de pacientes.
- **Categoría:** Disponibilidad / Integridad
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 4/5 (Probable) — el sector salud es uno de los más atacados por ransomware a nivel mundial (Verizon DBIR), y la clínica no cuenta con área de seguridad dedicada ni monitoreo continuo.
- **Impacto:** 5/5 (Extremo/Catastrófico) — imposibilita la atención de pacientes y puede implicar pérdida irrecuperable de historias clínicas.
- **Nivel de riesgo:** Alto (20/25 — puntaje SimpleRisk: 8)
- **Controles existentes:** Ninguno formal (sin backups aislados, sin EDR).
- **Plan de tratamiento:** Mitigar — backups automatizados diarios con almacenamiento aislado (air-gapped/inmutable), EDR en el servidor, segmentación de red.
- **Propietario:** Nicolás Estrella (Responsable de IT)

---

## Riesgo 2 (ID SimpleRisk: 1009)

- **Nombre:** Acceso indebido a historias clínicas por personal sin necesidad de conocer
- **Descripción:** Personal administrativo y de enfermería accede a historias clínicas de pacientes sin relación con su función, por curiosidad o falta de restricciones.
- **Categoría:** Confidencialidad
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 4/5 (Probable) — no existen controles de acceso basados en necesidad de conocer (need-to-know).
- **Impacto:** 4/5 (Importante) — vulnera la confidencialidad de datos sensibles de salud y puede derivar en responsabilidad legal bajo la Ley 25.326.
- **Nivel de riesgo:** Alto (16/25 — puntaje SimpleRisk: 6.4)
- **Controles existentes:** Ninguno; acceso amplio sin segmentación por rol.
- **Plan de tratamiento:** Mitigar — control de acceso basado en roles (RBAC), registro y auditoría periódica de accesos.
- **Propietario:** Nicolás Estrella

---

## Riesgo 3 (ID SimpleRisk: 1010)

- **Nombre:** Pérdida de datos por backups inexistentes o nunca probados
- **Descripción:** Ante una falla de hardware, error humano o ataque, la clínica podría perder de forma irrecuperable historias clínicas, datos de facturación y obras sociales.
- **Categoría:** Disponibilidad / Integridad
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 3/5 (Creíble) — no existe política formal de backups ni pruebas de restauración.
- **Impacto:** 5/5 (Extremo/Catastrófico) — afecta continuidad asistencial y cumplimiento legal de conservación de registros médicos.
- **Nivel de riesgo:** Alto (15/25 — puntaje SimpleRisk: 6)
- **Controles existentes:** Ninguno documentado.
- **Plan de tratamiento:** Mitigar — implementación de backups automatizados con pruebas de restauración periódicas.
- **Propietario:** Nicolás Estrella

---

## Riesgo 4 (ID SimpleRisk: 1005)

- **Nombre:** Filtración de datos por proveedor tercerizado de facturación
- **Descripción:** El proveedor externo que gestiona la facturación con obras sociales sufre una brecha o mal manejo de credenciales, exponiendo datos de pacientes y afiliación.
- **Categoría:** Confidencialidad / Legal
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas (datos compartidos con el proveedor)
- **Probabilidad:** 3/5 (Creíble) — no hay cláusulas contractuales específicas de protección de datos ni auditorías periódicas al proveedor.
- **Impacto:** 4/5 (Importante) — expone datos de pacientes/afiliación y genera responsabilidad legal por falta de debida diligencia sobre terceros.
- **Nivel de riesgo:** Medio (12/25 — puntaje SimpleRisk: 4.8)
- **Controles existentes:** Ninguno formal.
- **Plan de tratamiento:** Transferir/Mitigar — incorporar cláusulas de protección de datos en el contrato y auditorías periódicas al proveedor.
- **Propietario:** Nicolás Estrella

---

## Riesgo 5 (ID SimpleRisk: 1006)

- **Nombre:** Caída prolongada del sistema por falta de UPS y redundancia eléctrica
- **Descripción:** Cortes de energía frecuentes provocan caídas del sistema de turnos e historias clínicas durante horario de atención.
- **Categoría:** Disponibilidad / Operativo
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 4/5 (Probable) — no hay UPS de respaldo suficiente ni generador propio.
- **Impacto:** 3/5 (Moderado) — obliga a volver a registros en papel de forma improvisada, con demoras en la atención.
- **Nivel de riesgo:** Medio (12/25 — puntaje SimpleRisk: 4.8)
- **Controles existentes:** UPS insuficiente, sin generador.
- **Plan de tratamiento:** Mitigar — incorporar UPS de mayor capacidad y evaluar generador de respaldo.
- **Propietario:** Nicolás Estrella

---

## Riesgo 6 (ID SimpleRisk: 1007)

- **Nombre:** Phishing dirigido al personal administrativo
- **Descripción:** Un correo fraudulento logra robar credenciales de acceso al sistema de HCE o facturación.
- **Categoría:** Confidencialidad / Operativo
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 4/5 (Probable) — el personal no recibe capacitación periódica ni hay simulacros de phishing.
- **Impacto:** 4/5 (Importante) — puede derivar en accesos no autorizados, fraude con datos de obras sociales, o ser punto de entrada para ransomware.
- **Nivel de riesgo:** Alto (16/25 — puntaje SimpleRisk: 6.4)
- **Controles existentes:** Ninguno (sin MFA, sin capacitación).
- **Plan de tratamiento:** Mitigar — capacitación periódica, simulacros de phishing trimestrales, MFA obligatorio.
- **Propietario:** Nicolás Estrella

---

## Riesgo 7 (ID SimpleRisk: 1008)

- **Nombre:** Incumplimiento de la Ley de Protección de Datos Personales (25.326)
- **Descripción:** No existe un procedimiento documentado de resguardo, acceso y eliminación de HCE conforme a la normativa vigente.
- **Categoría:** Legal
- **Activos afectados:** Servidor de Historias Clínicas Electrónicas
- **Probabilidad:** 3/5 (Creíble) — no hay responsable formal designado para el tratamiento de datos sensibles de salud.
- **Impacto:** 4/5 (Importante) — expone a la clínica a sanciones administrativas y daño reputacional ante una inspección o denuncia.
- **Nivel de riesgo:** Medio (12/25 — puntaje SimpleRisk: 4.8)
- **Controles existentes:** Ninguno formal.
- **Plan de tratamiento:** Mitigar — documentar procedimientos de resguardo y designar responsable de tratamiento de datos.
- **Propietario:** Nicolás Estrella

---

## Resumen

| ID | Riesgo | Nivel | Tratamiento |
|---|---|---|---|
| 1002 | Ransomware en servidor HCE | Alto (8) | Mitigar |
| 1009 | Acceso indebido por personal | Alto (6.4) | Mitigar |
| 1010 | Pérdida de datos (backups) | Alto (6) | Mitigar |
| 1007 | Phishing al personal | Alto (6.4) | Mitigar |
| 1005 | Filtración por proveedor externo | Medio (4.8) | Transferir/Mitigar |
| 1006 | Caída del sistema (UPS) | Medio (4.8) | Mitigar |
| 1008 | Incumplimiento Ley 25.326 | Medio (4.8) | Mitigar |