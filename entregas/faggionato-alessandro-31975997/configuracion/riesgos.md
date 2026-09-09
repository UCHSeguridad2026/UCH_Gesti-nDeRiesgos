# Registro de riesgos

## Riesgo de prueba — PRUEBA-001

| Campo | Valor |
|---|---|
| Asunto | Acceso no autorizado a historias clínicas electrónicas |
| Categoría | Sensitive Data Management |
| Activo afectado | Historias clínicas electrónicas |
| Método de puntuación | Classic |
| Probabilidad actual | Credible |
| Impacto actual | Major |
| Propietario | Alessandro Faggionato |
| Propósito | Validar el registro de riesgos y la configuración inicial de SimpleRisk. |

### Evaluación

Un empleado podría consultar historias clínicas de pacientes sin una necesidad asistencial o administrativa válida. Esto comprometería la confidencialidad de datos médicos sensibles y podría ocasionar sanciones regulatorias, pérdida de confianza y daño reputacional para la clínica.

### Nota

Este registro es una prueba de funcionamiento. Los siete riesgos que integrarán el análisis formal se documentarán y justificarán en las siguientes etapas.

### Evidencia

`../informe/capturas/04-riesgo-prueba.png`

---

# Registro inicial de riesgos — Clínica privada

## Criterio de evaluación

Se utiliza el método **Classic** de SimpleRisk con una escala de 1 a 5. El valor de riesgo es `probabilidad × impacto`: bajo (1–4), medio (5–9), alto (10–15) y crítico (16–25).

Los controles existentes son supuestos iniciales basados en el escenario de la consigna. Deberán validarse con las áreas responsables durante una evaluación real.

## Resumen

| ID | Riesgo | Categoría | P | I | Valor | Nivel | Propietario |
|---|---|---|---:|---:|---:|---|---|
| R-01 | Phishing y robo de credenciales de acceso clínico | Confidencialidad | 4 | 5 | 20 | Crítico | Responsable de Seguridad / TI |
| R-02 | Ransomware sobre historias clínicas y turnos | Disponibilidad e integridad | 4 | 5 | 20 | Crítico | Jefatura de TI |
| R-03 | Consulta interna indebida de historias clínicas | Confidencialidad y legal | 3 | 5 | 15 | Alto | Dirección Médica |
| R-04 | Recuperación fallida de copias de respaldo | Disponibilidad | 3 | 5 | 15 | Alto | Jefatura de TI |
| R-05 | Exposición de datos de pacientes por configuración insegura | Confidencialidad y legal | 3 | 5 | 15 | Alto | Responsable de Seguridad / TI |
| R-06 | Indisponibilidad de la plataforma clínica o conectividad | Disponibilidad y operativo | 3 | 4 | 12 | Alto | Jefatura de TI |
| R-07 | Equipos clínicos o administrativos sin parches | Integridad, disponibilidad y operativo | 3 | 4 | 12 | Alto | Jefatura de TI |

## R-01 — Phishing y robo de credenciales de acceso clínico

- **Descripción:** un atacante envía correos que simulan provenir de una obra social, proveedor o área interna para obtener las credenciales de personal administrativo o médico y acceder al sistema de historias clínicas.
- **Activos afectados:** cuentas de usuario, historias clínicas electrónicas, sistema de facturación y correo institucional.
- **Probabilidad: 4 (probable).** La clínica recibe correos externos de pacientes, proveedores y obras sociales; sin MFA ni capacitación periódica, el engaño a usuarios es factible.
- **Impacto: 5 (catastrófico).** Una cuenta comprometida puede permitir acceso masivo a datos de salud y afectar la atención, la privacidad y la reputación.
- **Controles existentes asumidos:** usuario y contraseña, filtro básico de correo y antivirus de estaciones de trabajo.
- **Tratamiento:** mitigar mediante MFA, capacitación anti-phishing, filtro de correo reforzado y revisión de accesos privilegiados.
- **Propietario:** Responsable de Seguridad / TI.

## R-02 — Ransomware sobre historias clínicas y turnos

- **Descripción:** malware de cifrado se propaga desde una estación de trabajo comprometida y deja inaccesibles las historias clínicas, los turnos y los archivos compartidos.
- **Activos afectados:** servidores de historias clínicas, sistema de turnos, bases de datos, estaciones de trabajo y copias de respaldo.
- **Probabilidad: 4 (probable).** El vector de phishing, los equipos heterogéneos y el intercambio diario de archivos incrementan la posibilidad de ingreso de malware.
- **Impacto: 5 (catastrófico).** La indisponibilidad puede retrasar atención, obligar a operar manualmente y generar pérdida o exposición de información crítica.
- **Controles existentes asumidos:** antivirus tradicional y backups sin prueba periódica de restauración.
- **Tratamiento:** mitigar con EDR/antimalware, segmentación de red, backups inmutables y ejercicios de recuperación.
- **Propietario:** Jefatura de TI.

## R-03 — Consulta interna indebida de historias clínicas

- **Descripción:** un empleado consulta la historia clínica de una persona sin participar en su atención ni contar con una necesidad administrativa legítima.
- **Activos afectados:** historias clínicas electrónicas, datos personales sensibles, trazabilidad de accesos y reputación de la clínica.
- **Probabilidad: 3 (posible).** Muchos perfiles internos necesitan acceso al sistema y pueden existir permisos amplios o falta de monitoreo de consultas.
- **Impacto: 5 (catastrófico).** El acceso indebido a datos de salud puede derivar en denuncias, sanciones, pérdida de confianza y perjuicio a pacientes.
- **Controles existentes asumidos:** autenticación individual y registro técnico básico de inicio de sesión.
- **Tratamiento:** mitigar con mínimo privilegio, revisión de perfiles, auditoría de accesos a historias y sanciones formalizadas.
- **Propietario:** Dirección Médica.

## R-04 — Recuperación fallida de copias de respaldo

- **Descripción:** ante una falla, borrado accidental o ransomware, la clínica descubre que sus backups son incompletos, están dañados o no pueden restaurarse dentro del tiempo requerido.
- **Activos afectados:** bases de datos de pacientes, facturación, configuración de sistemas y continuidad operativa.
- **Probabilidad: 3 (posible).** Tener backups sin verificación ni simulacros no demuestra que puedan recuperarse de forma efectiva.
- **Impacto: 5 (catastrófico).** La pérdida prolongada de información clínica puede impedir la atención y afectar obligaciones de conservación de registros.
- **Controles existentes asumidos:** copias programadas en un único destino y sin prueba documentada de restauración.
- **Tratamiento:** mitigar mediante regla 3-2-1, copia fuera de línea o inmutable, monitoreo de backups y pruebas trimestrales de restauración.
- **Propietario:** Jefatura de TI.

## R-05 — Exposición de datos de pacientes por configuración insegura

- **Descripción:** un recurso de almacenamiento, exportación, backup o servicio web queda accesible a usuarios no autorizados por permisos incorrectos o configuraciones por defecto.
- **Activos afectados:** datos de pacientes, archivos de facturación, respaldos y documentación clínica.
- **Probabilidad: 3 (posible).** Los cambios operativos frecuentes y la falta de revisiones de configuración pueden introducir permisos excesivos.
- **Impacto: 5 (catastrófico).** La filtración de información médica es un incidente grave de privacidad con consecuencias legales y reputacionales.
- **Controles existentes asumidos:** autenticación de aplicaciones y permisos configurados manualmente.
- **Tratamiento:** mitigar con revisiones de configuración, mínimo privilegio, cifrado, inventario de repositorios y monitoreo de accesos anómalos.
- **Propietario:** Responsable de Seguridad / TI.

## R-06 — Indisponibilidad de la plataforma clínica o conectividad

- **Descripción:** una caída del proveedor de sistema clínico, servidor local, enlace de Internet o energía vuelve inaccesibles turnos, historias clínicas o facturación durante la jornada.
- **Activos afectados:** sistema de historias clínicas, sistema de turnos, conectividad, atención a pacientes y facturación.
- **Probabilidad: 3 (posible).** La operación depende de servicios tecnológicos continuos y una falla de proveedor o conectividad puede ocurrir.
- **Impacto: 4 (mayor).** La clínica puede continuar de forma manual temporalmente, pero con demoras, errores de transcripción y pérdida de productividad.
- **Controles existentes asumidos:** UPS básica y soporte del proveedor, sin enlace alternativo ni procedimiento manual probado.
- **Tratamiento:** mitigar con enlace redundante, procedimientos de contingencia en papel, UPS verificada y acuerdos de nivel de servicio.
- **Propietario:** Jefatura de TI.

## R-07 — Equipos clínicos o administrativos sin parches

- **Descripción:** estaciones de trabajo, servidores o equipos conectados a la red clínica conservan sistemas operativos y aplicaciones desactualizadas con vulnerabilidades explotables.
- **Activos afectados:** estaciones de enfermería, PCs administrativas, servidores, red interna y disponibilidad de atención.
- **Probabilidad: 3 (posible).** Los equipos que no pueden detenerse fácilmente suelen postergar actualizaciones; la diversidad tecnológica dificulta el control centralizado.
- **Impacto: 4 (mayor).** Una explotación puede servir de puerta de entrada para malware, alterar la operación o afectar sistemas críticos.
- **Controles existentes asumidos:** actualizaciones manuales y antivirus básico, sin inventario ni calendario de parches centralizado.
- **Tratamiento:** mitigar con inventario de activos, gestión centralizada de parches, ventanas de mantenimiento, segmentación y seguimiento de vulnerabilidades críticas.
- **Propietario:** Jefatura de TI.
