# Parte C: Análisis Crítico y Profundización

## 1. Comparación Metodológica: SimpleRisk vs. ISO 27005

SimpleRisk basa su evaluación en una matriz clásica cualitativa o semi-cuantitativa de Probabilidad por Impacto (PxI). Por otro lado, la metodología basada en la norma **ISO 27005** propone un enfoque mucho más exhaustivo y estructurado, centrado fuertemente en el valor de los activos de información, las vulnerabilidades específicas y las amenazas del entorno.

**Ventajas y Desventajas:**
*   **Enfoque SimpleRisk (Matriz PxI):**
    *   *Ventajas:* Alta velocidad de adopción, interfaz intuitiva y curva de aprendizaje baja. Ideal para obtener una foto rápida del estado de seguridad.
    *   *Desventajas:* Puede resultar subjetivo si los criterios de evaluación no están bien calibrados, limitando el análisis de escenarios de riesgo complejos.
*   **Enfoque ISO 27005:**
    *   *Ventajas:* Rigurosidad técnica, alineación directa con sistemas de gestión (SGSI - ISO 27001) y trazabilidad completa de los controles.
    *   *Desventajas:* Requiere una madurez organizacional alta y una inversión significativa de tiempo para identificar y clasificar cada activo antes de poder evaluar el riesgo.

**Contextos de Uso Ideales:**
El enfoque de **SimpleRisk** es perfecto para pymes, clínicas (como el escenario evaluado) o áreas de implementación TI que necesitan un registro inicial rápido y accionable. En cambio, **ISO 27005** es el estándar indispensable para entornos corporativos de gran escala, sector financiero o instituciones gubernamentales sometidas a auditorías internacionales estrictas.

---

## 2. Estrategia de Integración

Para potenciar la gestión de vulnerabilidades, la integración ideal de SimpleRisk se plantearía en dos niveles:

1.  **Gestión Operativa (Jira/Ticketing):** 
    Mediante la API REST de SimpleRisk o webhooks, se puede configurar que cada vez que un riesgo pase a nivel "Crítico", se genere automáticamente un ticket en **Jira**. Esto permite que los equipos de infraestructura y soporte TI gestionen la mitigación (ej. parcheo de servidores) dentro de su flujo de trabajo habitual sin necesidad de acceder al sistema de riesgos.
2.  **Reportes y Data Analytics:**
    Conectando la base de datos de SimpleRisk (MySQL/MariaDB) de forma directa a herramientas de Business Intelligence, es posible limpiar los datos (ej. mediante Power Query) y aplicar métricas avanzadas (con lenguaje DAX) para crear dashboards dinámicos. Esto transformaría el registro de riesgos estático en un tablero interactivo para la toma de decisiones gerenciales en tiempo real.