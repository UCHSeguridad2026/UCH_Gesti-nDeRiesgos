# Integración externa propuesta

## Objetivo
Integrar SimpleRisk con un sistema de tickets para convertir riesgos de nivel alto en tareas gestionables.

## Flujo
1. Analista crea/actualiza un riesgo.
2. SimpleRisk determina nivel de riesgo.
3. Si el riesgo es alto, se genera un evento.
4. Un webhook envía el evento al sistema de tickets.
5. Se crea un ticket con ID, descripción, nivel, propietario y fecha.
6. El responsable actualiza el estado.
7. El cierre del ticket queda como evidencia del tratamiento.

## Ejemplo de payload conceptual

```json
{
  "risk_id": "R01",
  "title": "Ransomware sobre servidores de historias clínicas",
  "risk_level": 20,
  "owner": "Jefe de Infraestructura",
  "treatment": "Mitigar",
  "action_due": "2026-10-15"
}
```

## Seguridad
- Usar HTTPS.
- No incluir contraseñas ni secretos en el payload.
- Autenticar el webhook.
- Rotar tokens.
- Registrar errores sin exponer credenciales.
- Validar que el evento provenga del origen esperado.

## Estado
**Propuesta documentada; no se presenta como integración implementada.**
