# Informe Técnico: Análisis Crítico e Integraciones - SimpleRisk

## 1. Comparación Metodológica: SimpleRisk (Matriz Tradicional) vs. FAIR

### Análisis Comparativo
SimpleRisk utiliza de forma predeterminada una matriz cualitativa/semicuantitativa basada en **Probabilidad x Impacto (1-5)**. En contraste, la metodología **FAIR (Factor Analysis of Information Risk)** descompone el riesgo en variables cuantitativas probabilísticas (frecuencia de amenaza, vulnerabilidad, pérdida primaria y secundaria) expresadas en términos monetarios.

| Criterio | SimpleRisk (Matriz Cualitativa) | FAIR (Factor Analysis of Information Risk) |
| :--- | :--- | :--- |
| **Enfoque** | Semicuantitativo / Subjetivo | Cuantitativo Financiero |
| **Complejidad** | Baja (Fácil implementación) | Alta (Requiere modelos matemáticos/Monte Carlo) |
| **Uso Ideal** | Priorización rápida e inventario inicial | Toma de decisiones sobre inversiones de capital (ROI) |
| **Comunicación** | Excelente para equipos técnicos | Excelente para Directorio y C-Level (expresado en USD) |

### Contexto de Aplicación
* **SimpleRisk:** Ideal para el escenario actual de la clínica al iniciar la gestión de riesgos. Permite catalogar rápidamente amenazas y establecer un orden de prioridad inmediato sin ralentizar la operación.
* **FAIR:** Recomendado para etapas maduras, especialmente cuando se deba justificar ante el Directorio la compra de hardware/software costoso mediante la pérdida monetaria esperada (ALE - Annualized Loss Expectancy).

---

## 2. Propuesta de Integración con Sistemas Externos

Para optimizar la respuesta ante incidentes, se propone integrar SimpleRisk con **Jira Software / Slack** mediante Webhooks automáticos.

### Arquitectura de Integración
1. **Disparador (Trigger):** Alta o modificación de un riesgo en SimpleRisk con Nivel $\ge 15$ (Riesgo Alto).
2. **Acción:** Un script intermedio pasa los datos JSON de la API REST de SimpleRisk a la API de Slack/Jira.
3. **Resultado:** 
   * Se crea automáticamente un ticket en Jira asignado al CISO/CTO.
   * Se envía una alerta inmediata al canal `#seguridad-alertas` en Slack.
