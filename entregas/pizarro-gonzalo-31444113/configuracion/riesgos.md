# Registro de riesgos: Clínica UCH

## Criterio de valoración

La clínica privada tiene 120 empleados, atiende aproximadamente 800 pacientes por día y administra historias clínicas electrónicas (HCE), datos de obras sociales y facturación. La probabilidad y el impacto se califican de 1 a 5. Para coincidir con el valor ya cargado en SimpleRisk, el nivel se calcula como `P × I / 2,5`. No hay mitigaciones planificadas ni revisión de gerencia aprobada al 09/09/2026.

| Puntaje | Interpretación de probabilidad | Interpretación de impacto |
|---:|---|---|
| 1 | Raro durante el año | Consecuencia menor, sin afectar la atención |
| 2 | Improbable, aunque posible | Afectación localizada y recuperable |
| 3 | Posible en las condiciones actuales | Interrupción o exposición que requiere gestión |
| 4 | Probable por la superficie y controles insuficientes | Afectación grave a varios servicios o datos sensibles |
| 5 | Casi cierto o recurrente | Compromete atención, datos sanitarios o continuidad institucional |

## Registro para SimpleRisk

| ID | Riesgo | Categoría | Activos afectados | P | I | Nivel registrado | Tratamiento | Propietario |
|---:|---|---|---|---:|---:|---:|---|---|
| 1002 | Acceso no autorizado a Historias Clínicas Electrónicas (HCE) | Confidencialidad | HCE, base de datos clínica, directorio de usuarios, terminales de consultorios y personal médico, de enfermería y de admisión | 4 | 5 | 8,0 (Crítico) | Mitigar | Jefe de Sistemas |
| 1003 | Phishing dirigido al área de Facturación | Integridad | Correo, cuentas del personal de facturación, sistema de facturación, datos de obras sociales y equipo de Tesorería | 3 | 4 | 4,8 (Alto) | Mitigar | Jefe de Facturación |
| 1004 | Falla de infraestructura y ausencia de backups probados | Disponibilidad | Servidores de HCE, almacenamiento, red, UPS, repositorios de backup, admisión y personal de Sistemas | 3 | 5 | 6,0 (Alto) | Mitigar | Jefe de Sistemas |
| 1005 | Ransomware en la red clínica | Disponibilidad | Red clínica, HCE, servidores de admisión, puestos de atención, servidores de archivos y copias de seguridad | 3 | 5 | 6,0 (Alto) | Mitigar | Responsable de Seguridad de la Información |
| 1006 | Error humano en carga de datos clínicos críticos | Integridad | HCE, módulos de laboratorio e imágenes, órdenes médicas, estaciones de enfermería y personal asistencial | 3 | 4 | 4,8 (Alto) | Mitigar | Director Médico |
| 1007 | Incumplimiento normativo de protección de datos de salud | Legal-Cumplimiento | HCE, legajos de pacientes, registros de acceso, contratos con proveedores y Compliance Officer | 3 | 4 | 4,8 (Alto) | Mitigar | Compliance Officer |
| 1008 | Dependencia de proveedor externo de facturación (SaaS) | Operativo | Plataforma SaaS, integración contable, datos de facturación y obras sociales, contrato y personal de Administración | 2 | 4 | 3,2 (Medio) | Mitigar | Jefe de Facturación |

## Fichas de riesgo y justificaciones

### 1002 - Acceso no autorizado a Historias Clínicas Electrónicas (HCE)

**Descripción:** un empleado, tercero o cuenta comprometida consulta HCE fuera de su función, por ejemplo accediendo a la historia de un paciente que no atiende o usando una sesión compartida en un consultorio. La exposición afecta datos de salud identificables y puede vulnerar el secreto profesional.

- **Activos afectados:** HCE y base clínica; directorio y credenciales; terminales de consultorios; registros de auditoría; médicos, enfermeros, administrativos y personal de Sistemas.
- **Probabilidad: 4.** Con 120 empleados, múltiples turnos y acceso cotidiano a información sanitaria, hay una superficie amplia de cuentas y sesiones. La auditoría externa detectó debilidades y todavía no hay evidencia de recertificación periódica, MFA universal ni alertas revisadas; por eso el evento es probable.
- **Impacto: 5.** Una cuenta con permisos excesivos puede exponer muchas historias clínicas. La sensibilidad del dato de salud, el deber de confidencialidad, el daño al paciente y las posibles sanciones justifican impacto crítico.
- **Cálculo SimpleRisk:** `4 × 5 / 2,5 = 8,0`.
- **Controles existentes actuales:** perfiles de usuario y registro de actividad de la HCE, aunque la revisión de permisos, la detección de accesos anómalos y la cobertura de MFA no están demostradas.
- **Tratamiento:** **Mitigar**, porque el acceso es necesario para atender pacientes, pero debe limitarse mediante mínimo privilegio, MFA, recertificación y monitoreo; evitarlo impediría la atención digital.
- **Propietario:** Jefe de Sistemas.

### 1003 - Phishing dirigido al área de Facturación

**Descripción:** un correo dirigido a facturación suplanta a una obra social, proveedor o directivo y obtiene credenciales, modifica datos de pago o induce a transferir fondos. El escenario combina ingeniería social con información de obras sociales y facturación.

- **Activos afectados:** correo y cuentas del área; sistema de facturación; datos de obras sociales; órdenes de pago; equipos del personal de Facturación y Tesorería.
- **Probabilidad: 3.** El área recibe comunicaciones externas y maneja pagos, pero el evento es plausible, no constante. Los 120 empleados amplían la posibilidad de que un mensaje dirigido encuentre una cuenta sin capacitación o sin MFA.
- **Impacto: 4.** La alteración de facturas, cuentas bancarias o liquidaciones puede causar pérdidas, reclamos y fraude, además de comprometer datos comerciales. Puede afectar la operación administrativa, aunque no necesariamente detiene la atención.
- **Cálculo SimpleRisk:** `3 × 4 / 2,5 = 4,8`.
- **Controles existentes actuales:** correo institucional, contraseñas y revisión manual de pagos; no se confirmó MFA, filtrado avanzado, doble aprobación ni simulaciones de phishing.
- **Tratamiento:** **Mitigar**, con MFA resistente al phishing, reglas de verificación de cambios bancarios, doble aprobación, filtrado y capacitación específica.
- **Propietario:** Jefe de Facturación.

### 1004 - Falla de infraestructura y ausencia de backups probados

**Descripción:** falla un servidor, almacenamiento, red o suministro eléctrico y la clínica no puede recuperar HCE, admisión o facturación porque las copias no fueron restauradas previamente o están incompletas.

- **Activos afectados:** servidores de HCE y admisión; almacenamiento; red; UPS; repositorios de backup; procedimientos de contingencia; personal de Sistemas, admisión y atención.
- **Probabilidad: 3.** El hardware, el software y la energía pueden fallar durante el año y la concentración de servicios en la infraestructura clínica aumenta la exposición. La ausencia de pruebas de restauración impide demostrar que los controles actuales funcionan.
- **Impacto: 5.** Sin HCE ni admisión, la atención de unos 800 pacientes diarios se ralentiza o pasa a registros manuales; también se comprometen continuidad, integridad y recuperación de datos sanitarios.
- **Cálculo SimpleRisk:** `3 × 5 / 2,5 = 6,0`.
- **Controles existentes actuales:** copias declaradas, UPS y soporte de Sistemas; no existe evidencia de restauraciones documentadas, objetivos RTO/RPO ni copia aislada e inmutable.
- **Tratamiento:** **Mitigar**, mediante estrategia 3-2-1, copias cifradas e inmutables, monitoreo, redundancia y pruebas periódicas de recuperación.
- **Propietario:** Jefe de Sistemas.

### 1005 - Ransomware en la red clínica

**Descripción:** malware distribuido desde un puesto de atención o administrativo cifra servidores, archivos y HCE, impidiendo consultas, admisión y facturación durante la jornada clínica.

- **Activos afectados:** red clínica, HCE, servidores de admisión, puestos de consultorios, servidores de archivos, backups y personal asistencial y administrativo.
- **Probabilidad: 3.** La cantidad de puestos y usuarios conectados crea varias vías de entrada y propagación. El evento es posible en el contexto sanitario, pero se valora 3 porque existen antivirus y soporte técnico declarados, aunque la segmentación y la respuesta no están validadas.
- **Impacto: 5.** La indisponibilidad simultánea puede interrumpir la atención de 800 pacientes por día, forzar procedimientos manuales y poner en riesgo la recuperación de historias clínicas; el impacto asistencial es crítico.
- **Cálculo SimpleRisk:** `3 × 5 / 2,5 = 6,0`.
- **Controles existentes actuales:** antivirus, copias de seguridad y soporte técnico; no se verificaron EDR, segmentación, bloqueo de macros, aislamiento de backups ni simulacro de respuesta.
- **Tratamiento:** **Mitigar**, con segmentación, EDR, mínimo privilegio, filtrado, backups inmutables, aislamiento rápido y ejercicios de respuesta; no es viable evitar el uso de la red clínica.
- **Propietario:** Responsable de Seguridad de la Información.

### 1006 - Error humano en carga de datos clínicos críticos

**Descripción:** durante la carga o transcripción, un profesional ingresa una dosis, resultado, identidad de paciente o indicación incorrecta en la HCE, y el dato llega a otro módulo clínico.

- **Activos afectados:** HCE, módulos de laboratorio e imágenes, órdenes médicas, estaciones de enfermería, interfaces y médicos, enfermeros y administrativos autorizados.
- **Probabilidad: 3.** La carga ocurre diariamente en un entorno de alta demanda y con múltiples turnos; los errores son posibles por fatiga, urgencia o identificación incorrecta, aunque existen validaciones y revisión clínica.
- **Impacto: 4.** Un dato clínico incorrecto puede provocar una decisión asistencial equivocada, repetición de estudios y reclamos. Se valora grave, pero no 5 porque la revisión profesional y la posibilidad de corrección reducen la extensión esperada.
- **Cálculo SimpleRisk:** `3 × 4 / 2,5 = 4,8`.
- **Controles existentes actuales:** validaciones de campos, usuarios individuales y revisión del profesional; no se confirmó doble control para datos críticos ni trazabilidad uniforme de correcciones.
- **Tratamiento:** **Mitigar**, con identificación de paciente, campos obligatorios, alertas, doble verificación de dosis y resultados críticos, capacitación y auditoría de cambios.
- **Propietario:** Director Médico.

### 1007 - Incumplimiento normativo de protección de datos de salud

**Descripción:** la clínica conserva, comparte o permite consultar datos de salud sin base documentada, minimización, retención, respuesta a incidentes o evidencia de control suficiente, incumpliendo obligaciones de protección de datos y secreto profesional.

- **Activos afectados:** HCE, legajos y consentimientos; registros de acceso; contratos y transferencias a proveedores; políticas; Compliance Officer, Dirección y personal con acceso a datos.
- **Probabilidad: 3.** La auditoría externa ya identificó debilidades de gestión y aún no hay revisión de gerencia aprobada. La cantidad de pacientes y proveedores hace posible que falte evidencia o que un acceso no esté adecuadamente justificado.
- **Impacto: 4.** Una infracción puede generar requerimientos, sanciones, reclamos, daño reputacional y pérdida de confianza, además de costos de remediación. Se valora 4 porque el impacto legal es serio aunque no todo incumplimiento detiene la atención.
- **Cálculo SimpleRisk:** `3 × 4 / 2,5 = 4,8`.
- **Controles existentes actuales:** políticas generales de confidencialidad, contratos y registros técnicos parciales; no se comprobó inventario de tratamientos, retención aprobada, recertificación ni pruebas de respuesta a incidentes.
- **Tratamiento:** **Mitigar**, con inventario, análisis de brechas, políticas aprobadas, capacitación, contratos con encargados, retención y evidencias de auditoría.
- **Propietario:** Compliance Officer.

### 1008 - Dependencia de proveedor externo de facturación (SaaS)

**Descripción:** una indisponibilidad, cambio contractual o incidente del SaaS de facturación impide emitir comprobantes, liquidar obras sociales o consultar información administrativa en la clínica.

- **Activos afectados:** plataforma SaaS, integración contable, datos de facturación y obras sociales, contrato, interfaces y personal de Administración y Facturación.
- **Probabilidad: 2.** El proveedor especializado reduce la probabilidad de falla interna y el servicio normalmente está disponible, pero una caída, cambio de API o incidente del tercero sigue siendo posible.
- **Impacto: 4.** La interrupción retrasa cobros, presentaciones a obras sociales y cierre administrativo, con impacto financiero y operativo. No se valora 5 porque la atención clínica y la HCE pueden continuar por separado durante una indisponibilidad breve.
- **Cálculo SimpleRisk:** `2 × 4 / 2,5 = 3,2`.
- **Controles existentes actuales:** contrato, soporte del proveedor y exportaciones operativas; deben verificarse SLA, portabilidad, backup independiente, notificación de incidentes y plan manual.
- **Tratamiento:** **Mitigar**, fortaleciendo SLA, evaluación del proveedor, exportaciones, pruebas de continuidad y alternativa manual. Transferir mediante cláusulas o seguro puede complementar, pero no elimina la dependencia.
- **Propietario:** Jefe de Facturación.

## Planes de acción para SimpleRisk

Los tres planes están asociados a los riesgos de mayor nivel priorizados por la dirección. Su estado inicial es **No iniciado** y requieren aprobación de gerencia antes de comprometer presupuesto.

### PA-01 - Recuperación probada de HCE y servicios críticos (riesgo 1004)

- **Descripción:** implementar backup 3-2-1 con una copia cifrada e inmutable fuera del entorno productivo, definir RTO/RPO para HCE y admisión, y ejecutar una restauración documentada de prueba con evidencia de resultados.
- **Vencimiento:** 09/10/2026.
- **Responsable:** Jefe de Sistemas.
- **Presupuesto estimado:** USD 4.500 (almacenamiento inmutable, configuración y horas de prueba).
- **Estado inicial:** No iniciado.

### PA-02 - Contención de ransomware en la red clínica (riesgo 1005)

- **Descripción:** separar la red clínica de la administrativa, desplegar EDR en servidores y puestos críticos, bloquear ejecución de macros no confiables y realizar un ejercicio de aislamiento y respuesta con Sistemas y Dirección Médica.
- **Vencimiento:** 23/10/2026.
- **Responsable:** Responsable de Seguridad de la Información.
- **Presupuesto estimado:** USD 7.500 (licencias EDR, segmentación, configuración y ejercicio).
- **Estado inicial:** En planificación.

### PA-03 - Control de acceso a HCE (riesgo 1002)

- **Descripción:** activar MFA para cuentas con acceso a HCE, recertificar permisos por rol y servicio, eliminar cuentas compartidas y configurar una revisión mensual de accesos anómalos con evidencia para Compliance.
- **Vencimiento:** 06/11/2026.
- **Responsable:** Jefe de Sistemas, con validación del Director Médico.
- **Presupuesto estimado:** ARS 3.200.000 (MFA, gestión de identidades, configuración y capacitación).
- **Estado inicial:** No iniciado.


