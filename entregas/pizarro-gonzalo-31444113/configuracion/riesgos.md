# Registro de riesgos: Clínica UCH

## Escala

Probabilidad e impacto se valoran de 1 a 5. El nivel es `P × I`: bajo (1–4), medio (5–9), alto (10–16) y crítico (17–25). La valoración es inicial y debe actualizarse con evidencia de la Clínica UCH.

| Valor | Probabilidad | Impacto |
|---:|---|---|
| 1 | Rara: no se espera durante el año | Menor: afecta una tarea sin interrumpir la atención |
| 2 | Improbable: podría ocurrir, pero no es habitual | Moderado: degradación localizada y recuperación simple |
| 3 | Posible: escenario plausible durante el año | Significativo: interrupción o exposición que requiere gestión directiva |
| 4 | Probable: existen condiciones que favorecen el evento | Grave: afecta varios servicios o datos sensibles |
| 5 | Casi cierta: exposición frecuente o controles insuficientes | Crítico: compromete atención, datos sanitarios o continuidad institucional |

| ID | Riesgo y activos afectados | Categoría | P | I | Nivel | Controles existentes | Tratamiento y propietario |
|---|---|---|---:|---:|---:|---|---|
| R-01 | Ransomware que cifra historias clínicas y servidores de admisión. Activos: HCE, servidores, backups y puestos administrativos. | Disponibilidad / integridad | 4 | 5 | Crítico (20) | Antivirus y copias de seguridad declaradas; falta verificar aislamiento y restauración. | Mitigar: segmentación, EDR, backups offline y pruebas de restore. Propietario: Infraestructura. |
| R-02 | Phishing que roba credenciales de profesionales y permite consultar historias clínicas. Activos: cuentas, HCE y correo. | Confidencialidad | 4 | 5 | Crítico (20) | Contraseñas y correo institucional; MFA y capacitación pendientes de confirmar. | Mitigar: MFA, filtro antiphishing, capacitación y revisión de accesos. Propietario: Seguridad de la información. |
| R-03 | Caída del sistema de historias clínicas durante la atención. Activos: HCE, agenda, admisión y continuidad asistencial. | Disponibilidad / operativo | 3 | 5 | Alto (15) | Soporte técnico y procedimiento manual no probado. | Mitigar: redundancia, monitoreo, SLA y procedimiento de contingencia probado. Propietario: Sistemas. |
| R-04 | Acceso indebido de un empleado a historias clínicas fuera de su función. Activos: HCE y datos personales/sanitarios. | Confidencialidad / legal | 3 | 5 | Alto (15) | Usuarios por rol y registro de actividad, con revisión no confirmada. | Mitigar: mínimo privilegio, recertificación trimestral y alertas de acceso anómalo. Propietario: Dirección médica. |
| R-05 | Error de integración que modifica importes de obras sociales o facturación. Activos: sistema de facturación, liquidaciones y registros contables. | Integridad / financiero | 3 | 4 | Alto (12) | Validaciones en la aplicación y controles manuales. | Mitigar: pruebas de integración, doble revisión y conciliación diaria. Propietario: Administración y Finanzas. |
| R-06 | Pérdida o filtración de backups con historias clínicas. Activos: repositorios de backup, cintas/discos y datos sanitarios. | Confidencialidad / disponibilidad | 3 | 5 | Alto (15) | Copias periódicas; cifrado, retención y ubicación deben verificarse. | Mitigar: cifrado, control de acceso, regla 3-2-1 y prueba de recuperación. Propietario: Infraestructura. |
| R-07 | Incendio o corte prolongado de energía en el área de servidores. Activos: red, servidores, almacenamiento y equipamiento de atención. | Continuidad / disponibilidad | 2 | 5 | Alto (10) | UPS y mantenimiento edilicio declarados; falta validar autonomía. | Transferir y mitigar: seguro, UPS/generador, sitio alternativo y plan de continuidad. Propietario: Operaciones. |

## Justificación de las valoraciones

Las valoraciones combinan el contexto de 800 atenciones diarias, la concentración de información sanitaria y los controles declarados pero aún no auditados. No representan estadísticas reales de la Clínica UCH; son supuestos explícitos para el ejercicio y deben validarse durante la revisión de riesgos.

### R-01: Ransomware en sistemas clínicos

- **Probabilidad 4:** la clínica tiene numerosos puestos, usuarios y servicios conectados; un único equipo comprometido podría propagar malware. La falta de verificación de segmentación y de pruebas de restauración eleva la exposición.
- **Impacto 5:** la indisponibilidad de HCE y admisión afecta directamente la atención de 800 pacientes diarios y puede comprometer integridad y recuperación de información sanitaria.

### R-02: Phishing y robo de credenciales

- **Probabilidad 4:** 120 empleados y el uso cotidiano del correo amplían la superficie de ingeniería social; no está confirmada la existencia de MFA ni de capacitación periódica.
- **Impacto 5:** una cuenta comprometida podría permitir acceso masivo a historias clínicas y otros sistemas, con consecuencias legales, reputacionales y asistenciales.

### R-03: Caída del sistema de historias clínicas

- **Probabilidad 3:** las fallas de infraestructura o software son posibles, pero existe soporte técnico; el procedimiento manual todavía no fue probado.
- **Impacto 5:** la caída afecta simultáneamente admisión, consultas y continuidad de atención, por lo que requiere operación de contingencia.

### R-04: Acceso indebido a historias clínicas

- **Probabilidad 3:** existen roles y registros, pero la recertificación y la revisión de actividad no están confirmadas; el volumen de empleados hace plausible un exceso de permisos.
- **Impacto 5:** los datos sanitarios son sensibles y su consulta injustificada puede producir daño a pacientes, sanciones y pérdida de confianza.

### R-05: Error en facturación u obras sociales

- **Probabilidad 3:** las integraciones y cargas de convenios pueden contener errores; las validaciones actuales reducen, pero no eliminan, la posibilidad.
- **Impacto 4:** un error puede generar pérdidas económicas, reclamos y trabajo de corrección, aunque no detendría necesariamente la atención clínica.

### R-06: Pérdida o filtración de backups

- **Probabilidad 3:** se realizan copias, pero el cifrado, el acceso, la retención y la ubicación todavía deben verificarse.
- **Impacto 5:** una copia contiene historias clínicas y, al mismo tiempo, es necesaria para recuperarse de un incidente; su filtración o pérdida afecta confidencialidad y disponibilidad.

### R-07: Incendio o corte prolongado de energía

- **Probabilidad 2:** existe UPS y mantenimiento edilicio, por lo que el evento no es frecuente; se mantiene como posibilidad por la concentración de infraestructura en el área de servidores.
- **Impacto 5:** un evento físico prolongado puede dejar fuera de servicio sistemas críticos y equipamiento de atención durante un período significativo.

## Planes de acción iniciales

| ID | Riesgo | Acción | Responsable | Vencimiento | Presupuesto estimado | Estado |
|---|---|---|---|---|---:|---|
| PA-01 | R-01 | Diseñar backups 3-2-1, aislar una copia y ejecutar una restauración documentada. | Infraestructura | 09/10/2026 | USD 1000 | No iniciado |
| PA-02 | R-02 | Habilitar MFA para cuentas privilegiadas y profesionales, junto con una campaña de phishing simulado. | Seguridad de la información | 23/10/2026 | USD 750 | No iniciado |
| PA-03 | R-03 | Documentar y probar el procedimiento de atención manual y recuperación del sistema de HCE. | Sistemas y Dirección médica | 06/11/2026 | USD 600 | No iniciado |

## Validación en SimpleRisk

- Riesgo de prueba creado: pendiente de carga manual en SimpleRisk.
- IDs de SimpleRisk asociados a R-01 a R-07: se completarán después de la carga manual.
- Planes PA-01 a PA-03 cargados: pendiente de carga manual en SimpleRisk.

