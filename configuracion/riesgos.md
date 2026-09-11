# Registro de riesgos — Clínica privada

## Escala
- Probabilidad: 1 muy baja — 5 muy alta.
- Impacto: 1 muy bajo — 5 crítico.
- Nivel = Probabilidad × Impacto.
- 1–4: Bajo.
- 5–9: Medio.
- 10–14: Significativo.
- 15–25: Alto.

> Las valoraciones son académicas y se justifican mediante razonamiento explícito. Deben validarse con información real de la organización.

| ID | Riesgo | Categoría | Activos afectados | P | I | Nivel | Tratamiento | Propietario |
|---|---|---|---|---:|---:|---:|---|---|
| R01 | Ransomware sobre servidores de historias clínicas | Disponibilidad / Operativo | Servidores, BD, historias clínicas | 4 | 5 | 20 Alto | Mitigar | Jefe de Infraestructura |
| R02 | Phishing contra personal administrativo | Confidencialidad / Operativo | Cuentas, correo, datos de pacientes | 4 | 4 | 16 Alto | Mitigar | Responsable de Seguridad |
| R03 | Acceso indebido a historias clínicas por empleados | Confidencialidad / Legal | Historias clínicas, cuentas de usuarios | 3 | 5 | 15 Alto | Mitigar | Responsable de Seguridad |
| R04 | Caída del sistema de historias clínicas | Disponibilidad / Operativo | Aplicación, BD, red | 3 | 5 | 15 Alto | Mitigar | Jefe de Infraestructura |
| R05 | Alteración accidental o maliciosa de datos de facturación | Integridad / Legal | BD de facturación, comprobantes | 3 | 4 | 12 Significativo | Mitigar | Responsable Administrativo |
| R06 | Fuga de datos de obras sociales | Confidencialidad / Legal | Datos de afiliados y convenios | 3 | 5 | 15 Alto | Mitigar | Responsable de Datos |
| R07 | Incendio/inundación en sala de servidores | Disponibilidad / Físico | Servidores, almacenamiento, red | 2 | 5 | 10 Significativo | Evitar/Mitigar | Jefe de Infraestructura |

## Justificaciones

### R01 — Ransomware
**Probabilidad 4/5:** la clínica depende de múltiples equipos y sistemas conectados; el phishing, credenciales comprometidas y software vulnerable son vías plausibles de entrada.  
**Impacto 5/5:** la indisponibilidad de historias clínicas puede afectar la continuidad operativa y la atención de pacientes.

### R02 — Phishing
**Probabilidad 4/5:** una organización con 120 empleados tiene una superficie humana relevante y correo electrónico como canal habitual.  
**Impacto 4/5:** el compromiso de una cuenta puede habilitar acceso a información sensible y fraude.

### R03 — Acceso indebido
**Probabilidad 3/5:** requiere abuso de privilegios, errores de asignación o controles insuficientes.  
**Impacto 5/5:** las historias clínicas contienen información altamente sensible y el acceso indebido puede generar consecuencias legales y reputacionales.

### R04 — Caída del sistema
**Probabilidad 3/5:** fallas de hardware, software, red o mantenimiento pueden producir indisponibilidad.  
**Impacto 5/5:** la clínica atiende alrededor de 800 pacientes diarios y depende del sistema para operar.

### R05 — Fuga de datos de obras sociales
**Probabilidad 3/5:** existen múltiples procesos y usuarios con acceso a información de afiliados.  
**Impacto 5/5:** una divulgación puede producir consecuencias legales, contractuales y reputacionales.

### R06 — Alteración de facturación
**Probabilidad 3/5:** puede ocurrir por error humano, privilegios excesivos o compromiso de una cuenta.  
**Impacto 4/5:** afecta ingresos, conciliaciones, información administrativa y trazabilidad.

### R07 — Incendio/inundación
**Probabilidad 2/5:** es menos frecuente que un incidente lógico, pero físicamente posible.  
**Impacto 5/5:** una pérdida de infraestructura puede interrumpir servicios críticos si no existe redundancia.

## Controles existentes asumidos para el ejercicio
- Antivirus/antimalware.
- Backups periódicos.
- Control de acceso por usuario.
- Firewall.
- Capacitación básica.
- UPS.
- Mantenimiento de infraestructura.

Estos controles se consideran supuestos del escenario académico y deben verificarse durante una evaluación real.

## Planes de tratamiento
- R01: copias offline/inmutables, segmentación, EDR, MFA y procedimiento de recuperación.
- R02: MFA, capacitación anti-phishing, filtros de correo y simulaciones.
- R03: mínimo privilegio, RBAC, revisión periódica de permisos y auditoría de accesos.
- R04: alta disponibilidad, monitoreo, mantenimiento preventivo y pruebas de recuperación.
- R05: segregación de funciones, logs, controles de cambios y revisión.
- R06: cifrado, mínimo privilegio, DLP donde corresponda y monitoreo.
- R07: reubicar/evitar exposición a fuentes de incendio o agua, sensores, UPS y sitio alternativo.
