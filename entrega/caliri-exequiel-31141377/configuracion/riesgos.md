# Registro de Riesgos — Clínica Privada

Este documento contiene la identificación, evaluación cualitativa y tratamiento de riesgos de ciberseguridad e infraestructura para la clínica (120 empleados, ~800 pacientes/día, Historias Clínicas Digitales).

## Escalas de Valoración (Matriz 5x5)

- **Probabilidad:** 1 (Raro), 2 (Improbable), 3 (Posible), 4 (Probable), 5 (Casi seguro).
- **Impacto:** 1 (Insignificante), 2 (Menor), 3 (Moderado), 4 (Mayor), 5 (Catastrófico).
- **Nivel de Riesgo (P × I):**
  - **Bajo (1–4):** Verde — Monitoreo periódico.
  - **Medio (5–9):** Amarillo — Plan de acción a mediano plazo.
  - **Alto (10–15):** Naranja — Tratamiento prioritario a corto plazo.
  - **Crítico (16–25):** Rojo — Acción e intervención inmediata.

---

## Tabla de Riesgos Identificados

| ID | Nombre y Descripción del Riesgo | Categoría | Activos Afectados | Prob. (1-5) | Imp. (1-5) | Nivel Resultante | Controles Existentes | Plan de Tratamiento | Propietario del Riesgo |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **R01** | **Acceso indebido por curiosidad del personal:** empleados con permisos amplios consultan historias clínicas de pacientes sin motivo laboral. | Confidencialidad | Historias Clínicas Digitales, Base de Datos de Pacientes | 4 | 3 | **Alto (12)** | Ninguno — acceso amplio sin logs de auditoría | **Mitigar:** implementar control de acceso basado en roles (RBAC), habilitar logs de auditoría y revisiones periódicas de accesos. | Responsable de Seguridad |
| **R02** | **Pérdida o robo de dispositivos móviles:** notebooks o tablets del personal médico usadas para consultar HCD fuera del consultorio se pierden o son robadas. | Confidencialidad / Disponibilidad | Dispositivos móviles, Historias Clínicas Digitales | 3 | 4 | **Alto (12)** | Ninguno — sin cifrado ni gestión centralizada | **Mitigar:** cifrado de disco, gestión centralizada (MDM) con borrado remoto y política de uso de dispositivos. | Jefe de IT |
| **R03** | **Cuentas activas de ex-empleados:** al desvincularse personal, sus credenciales no se revocan de inmediato y quedan accesos huérfanos. | Confidencialidad / Integridad | Cuentas de usuario, HCD, Sistema de Facturación | 3 | 4 | **Alto (12)** | Proceso informal, sin checklist de baja | **Mitigar:** checklist formal de offboarding y auditoría trimestral de cuentas activas. | RRHH / Jefe de IT |
| **R04** | **Dispositivos médicos conectados sin segmentar:** monitores y bombas de infusión en red plana, con firmware desactualizado, vulnerables a explotación remota. | Disponibilidad / Integridad | Equipos médicos IoT, Red interna | 2 | 5 | **Alto (10)** | Red plana, sin VLAN ni actualización de firmware | **Mitigar:** segmentación de red (VLAN dedicada) y plan de actualización de firmware. | Jefe de IT / Ingeniería Biomédica |
| **R05** | **Baja insegura de equipos:** discos y servidores dados de baja se descartan sin borrado seguro ni destrucción certificada. | Confidencialidad / Legal | Hardware dado de baja, archivo físico | 2 | 4 | **Medio (8)** | Ninguno definido | **Mitigar:** política de baja segura (wipe certificado o destrucción física). | Jefe de IT |
| **R06** | **Dependencia de proveedor único de facturación con obras sociales:** caída de la API externa detiene la facturación y liquidación de prestaciones. | Disponibilidad / Operativo | Sistema de Facturación, Integración con obras sociales | 3 | 3 | **Medio (9)** | Sin SLA definido ni plan de contingencia | **Mitigar:** negociar SLA con el proveedor e implementar procedimiento manual de contingencia. | Responsable Administrativo |
| **R07** | **Ataque de denegación de servicio (DDoS) al portal de turnos online:** satura el servidor web, impidiendo reservas y sobrecargando la atención telefónica. | Disponibilidad | Portal Web de turnos, Servidor web | 2 | 3 | **Medio (6)** | Sin protección anti-DDoS ni CDN | **Mitigar:** contratar mitigación DDoS/CDN e implementar procedimiento de contingencia telefónica. | Jefe de IT |

---

## Resumen de Planes de Acción Asociados (Nivel Alto)

1. **PA-01 (Asociado a R01):** Implementación de RBAC y logs de auditoría sobre HCD.
2. **PA-02 (Asociado a R02):** Cifrado de disco y MDM con borrado remoto para dispositivos móviles.
3. **PA-03 (Asociado a R03):** Checklist formal de offboarding y auditoría trimestral de cuentas.

*(El detalle de cada plan — fecha de vencimiento, responsable, presupuesto y estado — se documenta directamente en SimpleRisk.)*
