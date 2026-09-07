# Planes de Acción — Fiambrería Punta Pueyrredón

Se definieron 3 planes de mitigación para los riesgos de nivel Alto, cargados directamente en SimpleRisk (pestaña "Mitigation" de cada riesgo). Detalle extraído de [`informe/informe.md`](../informe/informe.md), sección 3.2.

| # | Riesgo asociado | Descripción del plan de mitigación | Estrategia | Responsable |
|---|---|---|---|---|
| Plan 1 | R01 — Robo de credenciales del sistema de gestión (EPyme) | Implementar 2FA (si el proveedor del EPyme lo permite), política de contraseñas fuertes, y capacitación al personal sobre phishing. | Mitigar | admin (representando al dueño/responsable) |
| Plan 2 | R02 — Pérdida de datos por falta de backup del sistema EPyme | Configurar backup automático diario con copia en la nube o disco externo. | Mitigar | admin (responsable técnico) |
| Plan 3 | R06 — Fuga de datos de empleados por mal manejo de archivos | Restringir acceso a legajos/sueldos solo al responsable de RRHH; eliminar el intercambio de archivos sin protección por WhatsApp/email. | Mitigar | admin (responsable administrativo) |

**Nota:** los 3 planes corresponden a los 3 riesgos de nivel Alto identificados en [`riesgos.md`](riesgos.md) (R01, R02, R06). Evidencia de carga en SimpleRisk disponible en `informe/capturas/03-plan-mitigacion.png`.
