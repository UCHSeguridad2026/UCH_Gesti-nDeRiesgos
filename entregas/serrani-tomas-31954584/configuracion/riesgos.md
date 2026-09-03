# Registro de Riesgos — Clínica Privada

Este documento contiene la identificación, evaluación cualitativa y tratamiento de riesgos de ciberseguridad e infraestructura para la clínica (120 empleados, ~800 pacientes/día, Historias Clínicas Digitales).

## Escalas de Valoración (Matriz 5x5)

* **Probabilidad:** 1 (Raro), 2 (Improbable), 3 (Posible), 4 (Probable), 5 (Casi seguro).
* **Impacto:** 1 (Insignificante), 2 (Menor), 3 (Moderado), 4 (Mayor), 5 (Catastrófico).
* **Nivel de Riesgo ($P \times I$):** 
  * **Bajo (1–4):** Verde | Monitoreo periódico.
  * **Medio (5–9):** Amarillo | Plan de acción a mediano plazo.
  * **Alto (10–15):** Naranja | Tratamiento prioritario a corto plazo.
  * **Crítico (16–25):** Rojo | Acción e intervención inmediata.

---

## Tabla de Riesgos Identificados

| ID | Nombre y Descripción del Riesgo | Categoría | Activos Afectados | Prob. (1-5) | Imp. (1-5) | Nivel Resultante | Controles Existentes | Plan de Tratamiento | Propietario del Riesgo |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **R01** | **Ransomware en HCD:** Infección por malware que cifra la base de datos principal de historias clínicas y bloquea la atención. | Disponibilidad / Integridad | Servidores de BD, Historias Clínicas Digitales | 4 | 5 | **Crítico (20)** | Antivirus básico en endpoints | **Mitigar:** Implementar EDR y copias de seguridad inmutables (WORM). | Director de IT |
| **R02** | **Phishing a personal administrativo:** Robo de credenciales de acceso al sistema de facturación y turnos mediante ingeniería social. | Confidencialidad | Cuentas de usuario, Sistema de Facturación | 4 | 4 | **Crítico (16)** | Filtro de correo electrónico estándar | **Mitigar:** Desplegar MFA obligatorio y capacitación en concientización. | CISO / Resp. Seguridad |
| **R03** | **Acceso no autorizado a HCD por falta de MFA:** Terceros acceden al portal médico desde redes externas usando claves vulneradas. | Confidencialidad / Legal | Portal Web Médico, BD de Pacientes | 3 | 5 | **Alto (15)** | Autenticación basada únicamente en contraseña | **Mitigar:** Forzar segundo factor de autenticación (TOTP/SMS) para accesos remotos. | Director de IT |
| **R04** | **Corte de energía prolongado:** Caída de los servidores principales de turnos y recepción por agotamiento de UPS. | Disponibilidad | Racks de Servidores, Red LAN | 3 | 4 | **Alto (12)** | UPS de pequeña capacidad en el rack principal | **Mitigar:** Instalación de grupo electrógeno con transferencia automática. | Jefe de Mantenimiento |
| **R05** | **Falla en restauración de backups:** Imposibilidad de recuperar datos por copias de seguridad corruptas o no probadas. | Disponibilidad / Integridad | Almacenamiento NAS, Copias en disco | 3 | 4 | **Alto (12)** | Copia de seguridad semanal programada | **Mitigar:** Automatización de pruebas periódicas de restauración de datos. | Administrador de BD |
| **R06** | **Sanciones por fuga de datos de salud:** Demandas o multas por vulnerar la Ley de Protección de Datos Personales. | Legal / Reputacional | Registros de Pacientes, Datos Financieros | 2 | 5 | **Alto (10)** | Políticas de privacidad firmadas en papel | **Transferir:** Contratación de póliza de seguro contra ciberriesgos (*Cyber Insurance*). | Asesoría Letrada |
| **R07** | **Alteración de recetas electrónicas:** Manipulación de fármacos prescriptos por falta de firmado criptográfico en tránsito. | Integridad / Legal | Módulo de Prescripciones Médicas | 2 | 4 | **Medio (8)** | Registro básico de auditoría en logs | **Mitigar:** Implementar Firma Digital con token criptográfico para profesionales. | Jefe de Farmacia |

---

## Resumen de Planes de Acción Asociados (Nivel Alto/Crítico)

1. **PA-01 (Asociado a R01):** Despliegue de solución EDR + Almacenamiento de Backups Inmutables.
   * *Responsable:* Director de IT | *Vencimiento:* 30 días | *Presupuesto:* USD 4,500 | *Estado:* Planificado.
2. **PA-02 (Asociado a R02 y R03):** Implementación de Autenticación de Doble Factor (MFA) institucional.
   * *Responsable:* Administrador de Sistemas | *Vencimiento:* 15 días | *Presupuesto:* USD 1,200 | *Estado:* En progreso.
3. **PA-03 (Asociado a R02):** Programa de Concientización y Simulaciones de Phishing.
   * *Responsable:* CISO | *Vencimiento:* 45 días | *Presupuesto:* USD 800 | *Estado:* Planificado.