# Registro de riesgos de la clínica

## Contexto y criterio de valoración

La organización es una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día. Utiliza historias clínicas electrónicas, sistemas de turnos, integraciones con obras sociales y plataformas de facturación.

La valoración manual utiliza una matriz de probabilidad por impacto de 1 a 5:

- **1–4:** Bajo — monitorear o aceptar con aprobación.
- **5–9:** Medio — planificar tratamiento.
- **10–15:** Alto — tratar prioritariamente.
- **16–25:** Crítico — escalar y actuar inmediatamente.

El valor manual se calcula como `Probabilidad × Impacto`. Para este trabajo práctico se utiliza además una escala simulada de SimpleRisk de 1 a 10. Los IDs y valores de SimpleRisk son ficticios, pero deben cargarse de forma consistente en la instancia local.

Para la escala simulada de SimpleRisk se usa: **1–3 Bajo**, **4–6 Medio** y **7–10 Alto**.

## Resumen de prioridades

| Riesgo | Valor manual | Nivel manual | Prioridad |
|---|---:|---|---|
| R01 — Ransomware / phishing dirigido | 20 | Crítico | Inmediata |
| R05 — Compromiso de correo y credenciales | 16 | Crítico | Inmediata |
| R04 — Caída de red o servidores | 15 | Alto | Corto plazo |
| R02 — Acceso indebido a HCE | 12 | Alto | Corto plazo |
| R06 — Backups no recuperables | 10 | Alto | Corto plazo |
| R08 — Daño físico de sala técnica | 10 | Alto | Mediano plazo |
| R07 — Documentación clínica impresa | 9 | Medio | Mediano plazo |
| R03 — Exposición con obras sociales | 8 | Medio | Mediano plazo |

---

## R01 — Ransomware / phishing dirigido a personal administrativo

**Categoría:** Confidencialidad / Disponibilidad / Integridad  
**Activos afectados:** Servidor de historias clínicas electrónicas (HCE), servidor de facturación y estaciones administrativas.  
**Probabilidad:** **4 (Probable)** — el sector salud es un objetivo frecuente de ransomware y la clínica no cuenta con filtrado de correo avanzado ni capacitación formal para todo el personal.  
**Impacto:** **5 (Catastrófico)** — el cifrado de la HCE puede paralizar la atención de aproximadamente 800 pacientes diarios, impedir el acceso a información clínica y generar consecuencias legales y reputacionales.  
**Valor / Nivel (matriz manual):** **20 / Crítico**  
**Valor / Nivel (SimpleRisk, ID 1001):** **9 / Alto**  
**Controles existentes:** Antivirus/EDR básico y backups periódicos sin verificación documentada.  
**Tratamiento:** **Mitigar** — EDR administrado, filtrado de correo, MFA, backups 3-2-1 con una copia offline o inmutable y capacitación anti-phishing.  
**Propietario:** Responsable de Infraestructura / Seguridad.

## R02 — Acceso indebido a historias clínicas electrónicas

**Categoría:** Confidencialidad / Cumplimiento legal  
**Activos afectados:** Sistema de HCE, cuentas de usuarios, registros de auditoría y datos personales de pacientes.  
**Probabilidad:** **3 (Posible)** — la clínica tiene numerosos usuarios con funciones diferentes y existe riesgo de permisos excesivos, cuentas obsoletas o accesos compartidos, pero no se cuenta con evidencia de accesos indebidos previos.  
**Impacto:** **4 (Mayor)** — una exposición relevante puede afectar a pacientes, generar sanciones y provocar pérdida de confianza, aunque se supone que existen registros y posibilidad de limitar el incidente.  
**Valor / Nivel (matriz manual):** **12 / Alto**  
**Valor / Nivel (SimpleRisk, ID 1002):** **6 / Medio**  
**Controles existentes:** Usuarios nominales y permisos básicos.  
**Tratamiento:** **Mitigar** — RBAC, MFA, mínimo privilegio, recertificación trimestral, baja inmediata de cuentas y revisión de logs.  
**Propietario:** Responsable de Seguridad.

## R03 — Exposición de datos en el intercambio con obras sociales

**Categoría:** Confidencialidad / Cumplimiento legal / Terceros  
**Activos afectados:** Integraciones con obras sociales, archivos de afiliados, información de facturación y credenciales de proveedores.  
**Probabilidad:** **2 (Improbable)** — existen intercambios frecuentes con terceros, pero los canales seguros y los contratos reducen la probabilidad de una exposición.  
**Impacto:** **4 (Mayor)** — una filtración puede exponer datos personales, interrumpir la facturación y provocar reclamos contractuales.  
**Valor / Nivel (matriz manual):** **8 / Medio**  
**Valor / Nivel (SimpleRisk, ID 1003):** **5 / Medio**  
**Controles existentes:** Contratos con proveedores y transferencia mediante canales seguros.  
**Tratamiento:** **Mitigar / Transferir** — cifrado, minimización de datos, evaluación de proveedores, cláusulas de notificación y seguro cuando corresponda.  
**Propietario:** Responsable de Sistemas.

## R04 — Indisponibilidad de red o servidores durante la atención

**Categoría:** Disponibilidad / Continuidad operativa  
**Activos afectados:** Red interna, servidores, sistema de turnos, HCE y puestos de atención.  
**Probabilidad:** **3 (Posible)** — una falla de red, hardware, energía o configuración puede afectar una operación altamente dependiente de servicios digitales.  
**Impacto:** **5 (Catastrófico)** — la caída puede retrasar la atención, impedir consultar antecedentes y obligar a utilizar procedimientos manuales.  
**Valor / Nivel (matriz manual):** **15 / Alto**  
**Valor / Nivel (SimpleRisk, ID 1004):** **7 / Alto**  
**Controles existentes:** Mantenimiento y soporte técnico.  
**Tratamiento:** **Mitigar** — redundancia, UPS, monitoreo, repuestos críticos y procedimiento de contingencia en papel.  
**Propietario:** Responsable de Infraestructura.

## R05 — Compromiso del correo y robo de credenciales

**Categoría:** Confidencialidad / Operativa  
**Activos afectados:** Correo institucional, identidad digital, HCE, información administrativa y cuentas de proveedores.  
**Probabilidad:** **4 (Probable)** — el correo es un canal habitual de phishing y la cantidad de empleados amplía la superficie de exposición.  
**Impacto:** **4 (Mayor)** — una cuenta comprometida puede permitir fraude, acceso lateral, suplantación y robo de información.  
**Valor / Nivel (matriz manual):** **16 / Crítico**  
**Valor / Nivel (SimpleRisk, ID 1005):** **9 / Alto**  
**Controles existentes:** Filtros antispam y capacitación informal.  
**Tratamiento:** **Mitigar** — MFA, filtrado avanzado, simulaciones de phishing, bloqueo de autenticación débil y canal de reporte de incidentes.  
**Propietario:** Responsable de Seguridad.

## R06 — Backups incompletos o no recuperables

**Categoría:** Disponibilidad / Integridad / Continuidad  
**Activos afectados:** Backups, HCE, facturación, configuraciones de servidores y documentación de recuperación.  
**Probabilidad:** **2 (Improbable)** — existen copias periódicas, por lo que una falla total de recuperación no se considera frecuente; sin embargo, nunca se verificó formalmente una restauración.  
**Impacto:** **5 (Catastrófico)** — la clínica podría no recuperar información crítica después de ransomware, una falla grave o un desastre físico.  
**Valor / Nivel (matriz manual):** **10 / Alto**  
**Valor / Nivel (SimpleRisk, ID 1006):** **6 / Medio**  
**Controles existentes:** Copias periódicas sin prueba documentada de restauración.  
**Tratamiento:** **Mitigar** — regla 3-2-1, copia offline/inmutable, monitoreo de resultados y pruebas mensuales de restauración.  
**Propietario:** Responsable de Infraestructura.

## R07 — Pérdida o divulgación de documentación clínica impresa

**Categoría:** Confidencialidad / Cumplimiento legal  
**Activos afectados:** Formularios, órdenes médicas, archivo físico, impresoras y residuos documentales.  
**Probabilidad:** **3 (Posible)** — la documentación circula entre áreas y puede quedar expuesta en escritorios, impresoras o residuos.  
**Impacto:** **3 (Moderado)** — una divulgación aislada puede afectar la privacidad de pacientes y requerir investigación, aunque su alcance esperado es menor que una exposición masiva de la HCE.  
**Valor / Nivel (matriz manual):** **9 / Medio**  
**Valor / Nivel (SimpleRisk, ID 1007):** **4 / Medio**  
**Controles existentes:** Archivo físico y políticas generales de manejo documental.  
**Tratamiento:** **Mitigar** — custodia, destrucción segura, registro de retiro y capacitación del personal.  
**Propietario:** Responsable de Administración.

## R08 — Incendio, corte eléctrico o daño físico en la sala técnica

**Categoría:** Disponibilidad / Continuidad operativa / Físico  
**Activos afectados:** Servidores, red, almacenamiento, comunicaciones y equipamiento eléctrico.  
**Probabilidad:** **2 (Improbable)** — es un evento menos frecuente, pero posible por fallas edilicias, eléctricas o ambientales.  
**Impacto:** **5 (Catastrófico)** — puede inutilizar infraestructura y provocar una interrupción prolongada de la atención.  
**Valor / Nivel (matriz manual):** **10 / Alto**  
**Valor / Nivel (SimpleRisk, ID 1008):** **5 / Medio**  
**Controles existentes:** Extintores y mantenimiento edilicio.  
**Tratamiento:** **Mitigar / Transferir** — UPS, sensores ambientales, respaldo externo, plan de recuperación ante desastres y seguro.  
**Propietario:** Responsable de Mantenimiento.

## Tratamiento prioritario

1. **R05:** escalar a dirección y comenzar tratamiento inmediato.
2. **R01, R02, R04 y R06:** implementar controles y realizar pruebas en el corto plazo.
3. **R03 y R08:** formalizar controles y seguimiento en el corto plazo/mediano plazo.
4. **R07:** mantener controles y revisar periódicamente el riesgo residual.

Los planes PA-01, PA-02 y PA-03 se encuentran documentados en `configuracion/planes-accion.md`.

## Supuestos y limitaciones

- Los controles existentes son supuestos iniciales y deben verificarse durante la configuración de SimpleRisk.
- Las puntuaciones representan una evaluación cualitativa inicial, no una medición estadística.
- Los IDs y valores de SimpleRisk son simulados para la empresa ficticia y deben coincidir con la carga realizada en la instancia local.
- El riesgo residual debe actualizarse después de implementar y probar los controles.
- La aceptación de un riesgo residual alto o crítico requiere aprobación documentada de la dirección.
