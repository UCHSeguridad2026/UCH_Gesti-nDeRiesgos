# Informe - Trabajo Practico Gestion de Riesgos con SimpleRisk

## Escenario

Clinica privada de 120 empleados que atiende aproximadamente 800 pacientes por dia. Maneja historias clinicas digitales, datos de obras sociales y facturacion. La clinica sufrio recientemente una auditoria externa que identifico debilidades en su gestion de riesgos.

## Riesgos identificados

Se identificaron 7 riesgos especificos del contexto de la clinica. El detalle completo (probabilidad, impacto, nivel, tratamiento y propietario) se encuentra documentado en `configuracion/riesgos.md`.

## Planes de accion

Se definieron 3 planes de mitigacion para los riesgos de mayor nivel:

### Plan 1 - Ransomware en servidores de facturacion (R02, Critico)
- Fecha planificada: 15/11/2026
- Esfuerzo: Significant
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: backups offline inmutables, segmentacion de red, solucion EDR

### Plan 2 - Acceso no autorizado a historias clinicas digitales (R01, Alto)
- Fecha planificada: 30/10/2026
- Esfuerzo: Considerable
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: control de acceso basado en roles (RBAC), logs de auditoria, revision periodica de permisos

### Plan 3 - Phishing dirigido al personal administrativo (R04, Alto)
- Fecha planificada: 15/10/2026
- Esfuerzo: Minor
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: autenticacion multifactor (MFA), filtrado anti-phishing, capacitacion periodica al personal