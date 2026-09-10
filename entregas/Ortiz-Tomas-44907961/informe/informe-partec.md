
# Parte C - Análisis Crítico y Profundización

## Comparación metodológica: SimpleRisk vs. NIST SP 800-30

### Enfoque de SimpleRisk (Matriz clásica Probabilidad × Impacto)

SimpleRisk utiliza el método de "Puntuación de riesgo clásica", donde el nivel de riesgo se calcula
como `(Probabilidad × Impacto) × (10/25)`, usando escalas simples de 1 a 5 para cada variable. Es un
enfoque **cualitativo/semicuantitativo**: los valores de probabilidad e impacto se asignan según
criterio del analista (o categorías descriptivas como "Improbable", "Probable", "Extremo"), sin
requerir datos históricos ni cálculos financieros.

### Enfoque de NIST SP 800-30

NIST SP 800-30 propone un proceso de gestión de riesgos más estructurado y en varias etapas: 
identificación de amenazas, identificación de vulnerabilidades, determinación de probabilidad de 
ocurrencia considerando la capacidad del atacante y las vulnerabilidades explotables, determinación 
del impacto sobre confidencialidad/integridad/disponibilidad, y cálculo del riesgo combinando estos 
factores con una escala de niveles (Muy Bajo a Muy Alto). A diferencia de SimpleRisk, NIST separa
explícitamente el análisis de la **fuente de amenaza** (humana, ambiental, estructural) del análisis 
de vulnerabilidad, y exige documentar la evidencia que sustenta cada estimación.

### Ventajas y desventajas

| Aspecto | SimpleRisk (clásico) | NIST SP 800-30 |
|---|---|---|
| Velocidad de implementación | Alta — matriz simple, apta para equipos pequeños | Baja — requiere proceso documentado y más tiempo |
| Rigor y trazabilidad | Bajo — depende del criterio subjetivo del analista | Alto — exige justificar cada estimación con evidencia |
| Curva de aprendizaje | Baja | Media/alta — requiere conocer el framework completo |
| Escalabilidad en organizaciones grandes | Limitada | Alta — pensado para entornos gubernamentales/corporativos complejos |
| Cuantificación financiera del riesgo | No | Parcial (no tan cuantitativo como FAIR) |
| Costo de adopción | Bajo (herramienta gratuita, proceso simple) | Medio/alto (capacitación, tiempo de analistas) |

### ¿En qué contexto conviene cada una?

- **SimpleRisk / matriz clásica** conviene en organizaciones pequeñas o medianas (como la clínica de 
  este TP, con 120 empleados) que necesitan un punto de partida ágil para gestionar riesgos sin 
  contar con un equipo de seguridad dedicado ni presupuesto para consultoría especializada. Permite
  iterar rápido y priorizar acción sobre análisis exhaustivo.

- **NIST SP 800-30** conviene en organizaciones grandes, entidades gubernamentales, o sectores 
  fuertemente regulados donde se necesita trazabilidad y justificación documentada de cada decisión 
  de riesgo (por ejemplo, ante auditorías externas o cumplimiento normativo estricto). Para la clínica 
  del escenario, sería el paso lógico a seguir una vez que el programa de gestión de riesgos madure 
  y necesite responder ante reguladores de salud o aseguradoras.

## Integración con herramienta externa

### Herramienta elegida: Slack (vía webhook)

Se propone integrar SimpleRisk con Slack para notificar automáticamente al equipo de seguridad 
cuando se registre o actualice un riesgo de nivel Alto o superior, reduciendo el tiempo de respuesta 
ante nuevos hallazgos críticos.

**Cómo funcionaría:**
1. Crear un canal dedicado en Slack (ej. `#riesgos-seguridad`) y generar un Incoming Webhook desde
   la configuración de la app de Slack para ese canal (Slack provee una URL única tipo 
   `https://hooks.slack.com/services/...`).
2. SimpleRisk permite configurar notificaciones salientes; en su defecto (si la versión no lo soporta 
   nativamente), se puede implementar un script que consulte periódicamente la API de SimpleRisk 
   (o lea la base de datos) buscando riesgos nuevos o modificados con score ≥ 4.8 (nivel Alto), y 
   dispare un POST HTTP al webhook de Slack con el detalle del riesgo.
3. El mensaje en Slack incluiría: ID del riesgo, sujeto, score, propietario y un link directo al 
   riesgo en SimpleRisk, permitiendo que el equipo actúe sin necesidad de ingresar manualmente al 
   sistema a revisar.

**Beneficio concreto para la clínica:** dado que el personal de TI es reducido, una notificación 
push evita que un riesgo crítico (como el de ransomware, identificado en este TP) pase desapercibido 
hasta la próxima revisión manual periódica.