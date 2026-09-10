# Informe TP — Gestión de Riesgos con SimpleRisk
**Alumno:** Nicolás Estrella | **Legajo:** 31066692
**Materia:** Seguridad de Sistemas — Cátedra Ing. Rodrigo Atilio Elgueta

## Parte A — Instalación y Configuración Básica

Se instaló SimpleRisk mediante la imagen oficial de Docker (`simplerisk/simplerisk`), levantada con:
Se creó la cuenta de administrador predeterminada y se configuraron 3 usuarios con roles diferenciados y permisos ajustados al principio de menor privilegio (detalle en `configuracion/usuarios.md`). Se creó un riesgo de prueba (ID 1001) para validar el funcionamiento del sistema.

## Parte B — Escenario Real: Clínica Privada

**Contexto:** Clínica privada de 120 empleados, ~800 pacientes/día, con historias clínicas electrónicas (HCE), datos de obras sociales y facturación tercerizada.

### Riesgos identificados

| ID | Riesgo | Categoría | Prob. | Impacto | Nivel |
|---|---|---|---|---|---|
| 1002 | Ransomware en servidor de HCE | Gestión de vulnerabilidades técnicas | Probable | Extremo/Catastrófico | Alto (8) |
| 1009 | Acceso indebido a HCE por personal sin necesidad de conocer | Gestión de acceso | Probable | Importante | Medio (6.4) |
| 1010 | Pérdida de datos por backups inexistentes/no probados | Gestión de vulnerabilidades técnicas | Creíble | Extremo/Catastrófico | Medio (6) |
| 1007 | Phishing dirigido a personal administrativo | Política y procedimiento | Probable | Importante | Medio (6.4) |
| 1005 | Filtración de datos por proveedor tercerizado de facturación | Gestión de terceros | Creíble | Importante | Medio (4.8) |
| 1006 | Caída del sistema por falta de UPS/redundancia eléctrica | Resiliencia ambiental | Probable | Moderado | Medio (4.8) |
| 1008 | Incumplimiento de la Ley 25.326 por falta de procedimientos formales | Política y procedimiento | Creíble | Importante | Medio (4.8) |

*(Ver justificación completa de cada riesgo y evidencia de carga en SimpleRisk en `capturas/`)*

### Planes de acción (riesgos de mayor nivel)

1. **Ransomware (1002):** Backups automatizados diarios con almacenamiento aislado (air-gapped/inmutable) + EDR en servidor de HCE + segmentación de red. Esfuerzo: Significativo. Vencimiento: 08/11/2026.
2. **Phishing (1007):** Capacitación periódica en concientización de seguridad + simulacros de phishing trimestrales + MFA obligatorio. Esfuerzo: Considerable. Vencimiento: 12/10/2026.
3. **Acceso indebido (1009):** Control de acceso basado en roles (RBAC) + registro y auditoría periódica de accesos. Esfuerzo: Considerable. Vencimiento: 12/09/2026.

## Parte C — Análisis Crítico y Profundización

### Comparación metodológica: SimpleRisk (matriz clásica) vs. FAIR

SimpleRisk utiliza el enfoque clásico de **matriz de probabilidad × impacto**, con escalas cualitativas (ej. "Probable" × "Importante" = nivel numérico 1-25). FAIR (*Factor Analysis of Information Risk*) en cambio descompone el riesgo en factores cuantificables (frecuencia de eventos de pérdida, magnitud de la pérdida en términos monetarios) para expresar el riesgo como una **pérdida económica estimada** (ej. "entre USD 50.000 y USD 200.000 anuales").

**Ventajas de SimpleRisk (clásico) frente a FAIR:**
- Mucho más rápido de implementar; no requiere datos históricos de incidentes ni expertise estadístico.
- Más intuitivo para comunicar a un directorio no técnico ("riesgo Alto" se entiende sin explicación).
- Adecuado para organizaciones chicas/medianas (como la clínica del caso) sin área de riesgo dedicada.

**Desventajas frente a FAIR:**
- La subjetividad en la asignación de "Probable" o "Importante" varía según quién complete el formulario, afectando la consistencia entre analistas.
- No permite justificar económicamente una inversión en seguridad (ej. "gastar $150.000 en backups para evitar una pérdida esperada de $2.000.000") — algo que FAIR sí resuelve, siendo más útil para decisiones de presupuesto ante la dirección.
- Dos riesgos con el mismo puntaje numérico (ej. 12) pueden tener naturalezas de pérdida completamente distintas, cosa que FAIR distingue mejor.

**¿Cuándo conviene cada una?** El enfoque clásico de SimpleRisk es preferible para una primera pasada de gestión de riesgos o en organizaciones sin madurez en seguridad (como la clínica del caso). FAIR conviene cuando ya existe un programa de riesgos maduro y se necesita justificar inversiones concretas ante la dirección con cifras económicas defendibles.

### Integración con herramienta externa

Se propone integrar SimpleRisk con **Slack** mediante un webhook: cuando se crea o actualiza un riesgo de nivel **Alto o Crítico**, SimpleRisk podría disparar una notificación automática a un canal `#seguridad-riesgos` del equipo de IT, usando la funcionalidad de "Incoming Webhooks" de Slack. Esto acortaría el tiempo de respuesta ante riesgos críticos (como el ransomware, ID 1002), que hoy dependen de que alguien revise manualmente el panel de SimpleRisk.

*(No implementado por limitaciones de tiempo — SimpleRisk soporta webhooks salientes configurables desde Ajustes → Extras, que podrían apuntar a la URL del webhook de Slack)*