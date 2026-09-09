# Parte C - Análisis Crítico y Profundización

## 1. Comparación Metodológica: SimpleRisk vs. ISO/IEC 27005

SimpleRisk implementa una matriz cualitativa estándar de 5x5 (Probabilidad x Impacto). A continuación, se compara con el estándar **ISO/IEC 27005**:

| Criterio | SimpleRisk (Matriz Tradicional) | ISO/IEC 27005 |
|---|---|---|
| **Enfoque** | Cualitativo / Semi-cuantitativo rápido. | Proceso estructurado y sistemático de gestión del riesgo. |
| **Ventajas** | Alta usabilidad, implementación rápida y visualización directa para la gerencia. | Análisis exhaustivo, contemplando el contexto organizacional, valor de activos y salvaguardas iterativas. |
| **Desventajas** | Subjetividad en la asignación de valores de 1 a 5 y sesgo de valoración. | Alta complejidad administrativa y mayor requerimiento de horas de consultoría. |
| **Contexto Ideal** | PyMEs, clínicas privadas de tamaño medio o arranques rápidos de gestión de riesgos. | Grandes corporaciones, sectores altamente regulados (banca, infraestructura crítica) o certificaciones ISO 27001. |

## 2. Integración con Herramientas Externas

Para automatizar la respuesta e incidentes, SimpleRisk se puede integrar mediante **Webhooks / API REST** con un sistema de comunicación como **Slack/Teams** o ticketing como **Jira**:

* **Flujo de Integración con Slack:**
  1. Cuando un analista registra un riesgo de nivel **Crítico** o **Alto** (P x I >= 10) en SimpleRisk.
  2. Un script en Python escucha el evento API o recibe la notificación Webhook de SimpleRisk.
  3. Se envía un payload JSON a la API de Slack que publica una alerta inmediata en el canal `#seguridad-alertas` con el ID del riesgo, propietario y enlace directo para iniciar el tratamiento.
