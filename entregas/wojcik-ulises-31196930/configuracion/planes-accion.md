# Planes de acción y mitigación

Los planes están asociados al registro de riesgos de la clínica y adaptados a la estructura del sistema de gestión de riesgos (SimpleRisk). Los presupuestos se indican en moneda local estimada y su rango operativo correspondiente.

---

## PA-01 — Recuperación confiable ante ransomware

* **Riesgos asociados:** R01 (Ransomware / phishing dirigido) | R06 (Backups no recuperables)
* **Planning Strategy:** Mitigate
* **Mitigation Owner:** Responsable de Infraestructura
* **Mitigation Team:** Responsable de Seguridad, Proveedor de backup
* **Planned Mitigation Date:** 15/10/2026 (Inicio: 16/09/2026)
* **Mitigation Effort:** Medium / High
* **Mitigation Cost:** $0 to $100,000 (ARS 3.500.000 estimado)
* **Mitigation Percent:** 25% (En progreso)

### Current Solution
Reducir la probabilidad de cifrado exitoso y garantizar la restauración operativa de la HCE y facturación dentro de una ventana de tiempo aceptable mediante las siguientes actividades:
1. Inventariar servidores, estaciones y datos que deben recuperarse prioritariamente.
2. Configurar backups bajo el estándar 3-2-1: tres copias, dos soportes distintos y una copia offline o inmutable.
3. Activar protección EDR y restringir la ejecución de archivos sospechosos en estaciones administrativas.
4. Configurar alertas para fallas de backup y accesos anómalos.
5. Ejecutar una restauración controlada de la HCE y del sistema de facturación.
6. Documentar el procedimiento de recuperación y capacitar al personal técnico.

### Security Requirements
* Al menos una copia de respaldo debe ser offline o inmutable.
* El backup de la HCE debe finalizar correctamente durante cinco días consecutivos.
* La prueba de restauración debe recuperar una muestra de datos sin errores ni pérdidas de integridad.
* Procedimiento operativo documentado con responsables claros, orden de prelación y contactos de emergencia.

### Security Recommendations & Residual Risk
* Realizar simulacros integrales de recuperación con periodicidad semestral.
* **Riesgo residual:** R01 desciende de 20 (Crítico) a 10 (Alto) tras la fase de pruebas; R06 desciende de 10 (Alto) a 5 (Medio) al institucionalizarse la prueba mensual.

---

## PA-02 — Identidad segura y mínimo privilegio

* **Riesgos asociados:** R02 (Acceso no autorizado a HCE) | R05 (Uso indebido de privilegios)
* **Planning Strategy:** Mitigate
* **Mitigation Owner:** Responsable de Seguridad
* **Planned Mitigation Date:** 30/10/2026
* **Mitigation Effort:** Medium
* **Mitigation Cost:** $0 to $100,000 (ARS 900.000 estimado)
* **Mitigation Percent:** 0% (Pendiente)

### Current Solution
Fortalecer la autenticación y limitar el acceso a la información clínica según la función de cada usuario:
1. Activar autenticación multifactor (MFA).
2. Revisar y depurar perfiles y roles en el sistema clínico.
3. Eliminar cuentas de usuario inactivas o desvinculadas.

### Security Requirements
* MFA obligatorio para accesos remotos y cuentas administrativas.
* Proceso formal de recertificación trimestral de cuentas y privilegios.

### Security Recommendations & Residual Risk
* Ejecutar programas continuos de capacitación y simulaciones anti-phishing.
* **Riesgo residual:** R02 y R05 reducen su probabilidad de ocurrencia a niveles controlados (Bajo/Medio).

---

## PA-03 — Continuidad de servicios clínicos

* **Riesgos asociados:** R04 (Caída de enlaces/red) | R08 (Falla de suministro eléctrico/físico)
* **Planning Strategy:** Mitigate
* **Mitigation Owner:** Responsable de Infraestructura y Mantenimiento
* **Planned Mitigation Date:** 15/11/2026
* **Mitigation Effort:** Medium
* **Mitigation Cost:** $0 to $100,000 (ARS 2.000.000 estimado)
* **Mitigation Percent:** 0% (Pendiente)

### Current Solution
Mantener disponibles los servicios clínicos ante incidentes de red, energía o infraestructura física:
1. Mantenimiento, calibración y testeo de autonomía de UPS y sistemas auxiliares.
2. Implementación de sensores ambientales en sala técnica.
3. Establecimiento de redundancia en enlaces críticos.

### Security Requirements
* Existencia y difusión de manuales de contingencia para operación asistencial en modo manual (papel).
* Procedimientos operativos claros para restauración gradual de servidores ante cortes de suministro.

### Security Recommendations & Residual Risk
* Inspecciones técnicas programadas bimestralmente sobre el estado de baterías y fuentes de poder.
* **Riesgo residual:** R04 y R08 mitigan su impacto operativo directo sobre la atención del paciente.