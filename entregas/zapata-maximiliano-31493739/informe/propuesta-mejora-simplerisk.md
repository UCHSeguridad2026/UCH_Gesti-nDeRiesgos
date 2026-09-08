# D4 — Propuesta de Mejora a SimpleRisk (formato Issue de GitHub)

## Título
Agregar soporte nativo de Webhooks salientes en la versión Community (sin requerir la API Extra de pago)

## Tipo
Feature Request / Mejora

## Descripción del problema

Actualmente, para integrar SimpleRisk con herramientas externas de notificación (Slack, Discord, Microsoft Teams, sistemas de tickets), es necesario adquirir la "API Extra" de pago para poder consultar programáticamente los riesgos vía REST API.

Esto genera una barrera de entrada significativa para pymes, estudiantes y equipos pequeños que quieren automatizar notificaciones básicas (por ejemplo, "avisar cuando se crea un riesgo de nivel Alto") sin necesitar todo el poder de una API REST completa.

## Propuesta

Agregar una funcionalidad nativa y gratuita de Webhooks salientes configurables, disponible en Settings → Notifications, con:

- Un campo para pegar una URL de webhook (compatible con el formato estándar de Slack/Discord/Teams)
- Un selector de eventos que disparan la notificación (ej: "Riesgo creado", "Riesgo cambia a nivel Alto/Crítico", "Plan de mitigación vencido")
- Una plantilla de mensaje simple y editable (texto plano con variables como {{risk_name}}, {{risk_level}})

Esto no requeriría exponer toda la superficie de una API REST (que sí justifica ser una funcionalidad paga por su alcance), sino únicamente un mecanismo de notificación saliente de un solo sentido, de bajo riesgo y alto valor para equipos pequeños.

## Valor / Justificación

Durante este TP universitario, se necesitó integrar SimpleRisk con Slack para notificar riesgos críticos, pero al no contar con la API Extra se tuvo que simular la integración leyendo un archivo JSON local en lugar de consultar SimpleRisk directamente. Un webhook nativo básico habría resuelto esto de forma completamente funcional, sin necesidad de sortear la limitación.

## Alternativas consideradas
- Usar la API Extra de pago (no viable para uso educativo/pyme de bajo presupuesto)
- Modificar el código fuente para agregar un hook personalizado (requiere mantenimiento propio en cada actualización de SimpleRisk)

## Contexto adicional
Propuesta elaborada en el marco de un TP de Seguridad de Sistemas, donde se implementó una integración funcional con Slack como prueba de concepto (ver scripts/notify_slack_risks.py en este mismo repositorio).
