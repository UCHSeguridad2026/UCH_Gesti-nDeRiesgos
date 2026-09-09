# Planes de acción

Los siguientes planes se cargaron en SimpleRisk como mitigaciones. Todos se encuentran en estado inicial **Planificado**; no fueron aceptados como mitigaciones implementadas porque los controles aún no se aplicaron.

| ID | Riesgo asociado | Plan | Responsable | Fecha objetivo | Esfuerzo | Presupuesto estimado | Reducción estimada | Estado |
|---|---|---|---|---|---|---:|---:|---|
| PA-01 | R-01 | MFA y fortalecimiento contra phishing | Responsable de Seguridad y TI | 15/10/2026 | Significativo | $500.000 | 65% | Planificado |
| PA-02 | R-02 | Protección contra ransomware y recuperación operativa | Jefatura de TI | 15/11/2026 | Excepcional | $1.000.000 | 70% | Planificado |
| PA-03 | R-04 | Respaldo resiliente y pruebas de recuperación | Jefatura de TI | 31/10/2026 | Significativo | $500.000 | 70% | Planificado |

## PA-01 — MFA y fortalecimiento contra phishing

**Riesgo asociado:** R-01 — Phishing y robo de credenciales de acceso clínico.

**Descripción:** implementar autenticación multifactor para las cuentas clínicas y administrativas, reforzar el filtrado de correo y ejecutar capacitación inicial con simulaciones trimestrales de phishing. También se revisarán las cuentas con privilegios elevados.

**Controles esperados:** MFA, filtro de correo, formación de usuarios y revisión de accesos privilegiados.

**Estado:** planificado; las medidas aún no se implementaron, por lo cual el riesgo residual no fue aceptado.

## PA-02 — Protección contra ransomware y recuperación operativa

**Riesgo asociado:** R-02 — Ransomware sobre historias clínicas y sistema de turnos.

**Descripción:** implementar EDR o antimalware avanzado en servidores y estaciones, segmentar la red clínica, mantener copias de respaldo inmutables y probar un procedimiento de respuesta y recuperación ante ransomware.

**Controles esperados:** EDR, segmentación de red, backups inmutables y plan de respuesta a incidentes.

**Estado:** planificado; las medidas aún no se implementaron, por lo cual el riesgo residual no fue aceptado.

## PA-03 — Respaldo resiliente y pruebas de recuperación

**Riesgo asociado:** R-04 — Recuperación fallida de copias de respaldo.

**Descripción:** aplicar la regla 3-2-1, mantener al menos una copia fuera de línea o inmutable, monitorear la ejecución de backups y realizar pruebas trimestrales de restauración documentadas.

**Controles esperados:** copias en medios diferenciados, copia externa o inmutable, monitoreo y pruebas de restauración.

**Estado:** planificado; las medidas aún no se implementaron, por lo cual el riesgo residual no fue aceptado.

## Evidencias

- `../informe/capturas/09-tabla-mitigaciones-planificadas.png`: los tres riesgos aparecen con la mitigación planificada.
- `../informe/capturas/10-mitigacion-r01-phishing.png`: detalle de PA-01.
- `../informe/capturas/11-mitigacion-r02-ransomware.png`: detalle de PA-02.
- `../informe/capturas/12-mitigacion-r04-backups.png`: detalle de PA-03.
