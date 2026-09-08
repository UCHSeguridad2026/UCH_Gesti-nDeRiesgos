# Registro de Riesgos — Clínica privada (escenario del TP)

## Contexto

Clínica privada, 120 empleados, 800 pacientes/día. Maneja historias clínicas
digitales, datos de obras sociales y facturación. Viene de una auditoría externa
que detectó debilidades en la gestión de riesgos.

Los supuestos asumidos sobre la organización —que sostienen las valoraciones de
este registro— están detallados en `../informe/informe.md`, sección "Contexto y
supuestos".

## Escalas

Se aplica la escala de la plantilla A03. Entre paréntesis se indica la
denominación equivalente de SimpleRisk (método *Classic*), de modo que esta
tabla sea contrastable contra las capturas de la aplicación.

**Probabilidad (1–5):** Raro (*Remote*) · Improbable (*Unlikely*) ·
Posible (*Credible*) · Probable (*Likely*) · Casi seguro (*Almost Certain*)

**Impacto (1–5):** Insignificante (*Insignificant*) · Menor (*Minor*) ·
Moderado (*Moderate*) · Mayor (*Major*) · Catastrófico (*Extreme/Catastrophic*)

**Niveles:** Bajo 1–4 (*Low*) · Medio 5–9 (*Medium*) · Alto 10–15 (*High*) ·
Crítico 16–25 (*Very High*)

> La instancia de SimpleRisk fue configurada para que el valor y el nivel
> coincidan con esta escala: se desactivó la normalización a 0–10 y se
> redefinieron los umbrales de nivel. El detalle está en el README, sección 3.4.

## Riesgos identificados

| ID | Nombre | Dimensión | Activos afectados | P | I | Valor | Nivel | Tratamiento | Propietario |
|---|---|---|---|:-:|:-:|:-:|---|---|---|
| R01 | Ransomware que cifra el sistema de historias clínicas | Disponibilidad · Integridad | Servidor HCE, base de datos clínica, estaciones de consultorio, backups locales | 4 | 5 | 20 | Crítico | Mitigar | Responsable de Sistemas |
| R02 | Acceso de personal a historias clínicas ajenas a su función | Confidencialidad | Base de datos clínica, sistema HCE | 4 | 4 | 16 | Crítico | Mitigar | Dirección Médica |
| R03 | Compromiso de credenciales por phishing al área administrativa | Confidencialidad · Integridad | Cuentas de correo, credenciales HCE, sistema de facturación | 4 | 4 | 16 | Crítico | Mitigar | Jefe de Administración |
| R04 | Fuga de datos de obras sociales por envío inseguro de planillas | Confidencialidad · Legal | Planillas de facturación, padrones de afiliados | 4 | 4 | 16 | Crítico | Mitigar | Jefe de Administración |
| R05 | Imposibilidad de restaurar los backups ante un incidente | Disponibilidad | Backups diarios, base de datos clínica | 3 | 5 | 15 | Alto | Mitigar | Responsable de Sistemas |
| R07 | Incumplimiento de la Ley 25.326 en el tratamiento de datos sensibles | Legal | Historias clínicas, procesos de tratamiento de datos, contratos con proveedores | 3 | 4 | 12 | Alto | Mitigar | Dirección General |
| R06 | Interrupción del servicio por falla eléctrica o de climatización | Disponibilidad · Operativo | Sala de servidores, servidor HCE, equipamiento de red | 3 | 3 | 9 | Medio | Mitigar | Jefe de Mantenimiento |

*Ordenados por nivel de riesgo descendente. La numeración de ID responde al orden
de identificación, no a la severidad.*

### Distribución por nivel

| Nivel | Cantidad | % del total |
|---|:-:|:-:|
| Crítico | 4 | 57 % |
| Alto | 2 | 29 % |
| Medio | 1 | 14 % |
| Bajo | 0 | 0 % |
| **Total** | **7** | **100 %** |

---

## Justificación de valoraciones

### R01 — Ransomware que cifra el sistema de historias clínicas

**Descripción.** Cifrado del servidor de historia clínica electrónica y de las
estaciones de trabajo conectadas mediante software malicioso, con exigencia de
rescate para recuperar el acceso. El vector de entrada más probable es una
estación de consultorio o administrativa comprometida, con posterior propagación
lateral por la red interna.

**Activos afectados.** Servidor de HCE, base de datos clínica, estaciones de
trabajo de consultorios y admisión, backups alojados en disco local.

**Probabilidad: 4 (Probable).** El sector salud es sistemáticamente uno de los
verticales más afectados por ransomware, por la combinación de alta criticidad
operativa —que aumenta la disposición a pagar— y madurez de seguridad
habitualmente menor que la de sectores como el financiero. En esta clínica
concurren además tres condiciones que elevan la exposición: una superficie de
ataque amplia (120 empleados con estaciones distribuidas en consultorios), un
área de sistemas de dos a tres personas sin rol dedicado a seguridad, y ausencia
de segmentación de red entre el segmento clínico y el administrativo. No se
asigna 5 porque no consta un incidente previo en la organización.

Los datos del sector respaldan esta valoración. El *2026 Data Breach
Investigations Report* de Verizon registra 1.492 incidentes en Healthcare, de los
cuales 1.438 constituyeron brechas confirmadas. *System Intrusion* es el patrón
más frecuente del sector por segundo año consecutivo y el informe lo atribuye
principalmente a ransomware, describiendo una secuencia idéntica a la planteada
aquí: acceso mediante credenciales robadas o explotación de vulnerabilidades,
despliegue del cifrado y posterior exfiltración de datos como palanca de presión.
A escala global, el ransomware pasó del 44 % al 48 % del total de brechas
respecto del informe anterior. El 99 % de los ataques al sector tuvo motivación
financiera, lo que confirma que una clínica no necesita ser un objetivo
seleccionado para ser alcanzada.

**Impacto: 5 (Extremo/Catastrófico).** La indisponibilidad del sistema de
historias clínicas interrumpe la atención de 800 pacientes diarios: sin acceso a
antecedentes, medicación habitual ni alergias, la atención segura se vuelve
inviable y obliga a suspender turnos o derivar pacientes. Si además fallara la
restauración de los backups (ver R05), la pérdida de historias clínicas sería
irreversible, con consecuencias asistenciales, legales y reputacionales
permanentes.

**Controles existentes.** Antivirus de endpoint estándar. Backups diarios a
disco local, sin copia offline ni prueba de restauración documentada.

**Plan de tratamiento: Mitigar.** Ver plan de acción PA01. La transferencia
mediante seguro no es alternativa suficiente: una póliza puede cubrir el costo
económico, pero no restituye la disponibilidad asistencial ni las historias
clínicas perdidas.

---

### R02 — Acceso de personal a historias clínicas ajenas a su función

**Descripción.** Consulta de historias clínicas por parte de personal de la
clínica sin relación asistencial con el paciente. Comprende tanto la curiosidad
sobre pacientes conocidos o de perfil público como la consulta de registros
fuera del servicio de pertenencia.

**Activos afectados.** Base de datos clínica, sistema HCE.

**Probabilidad: 4 (Probable).** A diferencia de un ataque externo, este riesgo no
requiere capacidad técnica alguna: basta con una sesión legítima. En esta clínica
la exposición se agrava por tres condiciones concurrentes: existen usuarios
compartidos por turno en algunos sectores, lo que impide atribuir una consulta a
una persona determinada; el sistema no restringe el acceso por servicio, de modo
que cualquier usuario autenticado puede consultar cualquier historia clínica; y
los registros de acceso, si bien se generan, no se revisan, por lo que el efecto
disuasivo es nulo.

*Consideración sobre la evidencia sectorial.* El *2026 DBIR* de Verizon asigna al
patrón *Privilege Misuse* sólo el 3 % de las brechas del sector, en descenso desde
el 7 % y el 8 % de los dos informes previos. Tomado aisladamente, ese dato
sugeriría una probabilidad menor. Se mantiene la valoración en 4 por dos razones.
Primero, el DBIR contabiliza brechas confirmadas y divulgadas, mientras que el
acceso indebido interno sólo se detecta si alguien revisa los registros, práctica
que en esta clínica no existe: la ausencia de detección no equivale a ausencia de
ocurrencia. Segundo, el mismo informe atribuye el 19 % de las brechas del sector
a actores internos, de modo que la vía interna dista de ser marginal. Se deja
constancia de la tensión entre el dato sectorial y la valoración adoptada, que
descansa en las condiciones específicas de esta organización.

**Impacto: 4 (Mayor).** Los datos de salud son datos sensibles bajo la Ley
25.326 y su tratamiento indebido está sujeto a un régimen agravado. Un caso
divulgado produciría daño reputacional severo en una institución cuyo activo
principal es la confianza del paciente, además de exposición a sanciones y
reclamos individuales. No se asigna 5 porque el alcance se limita a los registros
efectivamente consultados y no compromete la continuidad operativa.

**Controles existentes.** Autenticación nominal en el HCE, parcialmente
desvirtuada por los usuarios compartidos. Registros de acceso generados por el
sistema, no revisados.

**Plan de tratamiento: Mitigar.** Ver plan de acción PA02.

---

### R03 — Compromiso de credenciales por phishing al área administrativa

**Descripción.** Obtención de credenciales de personal administrativo mediante
correos fraudulentos que suplantan a obras sociales, proveedores o al propio
sector de sistemas, con acceso posterior al correo institucional, al sistema de
facturación o al HCE.

**Activos afectados.** Cuentas de correo institucional, credenciales del HCE,
sistema de facturación.

**Probabilidad: 4 (Probable).** El phishing es el vector de acceso inicial más
frecuente en incidentes de seguridad. El área administrativa de la clínica recibe
correo externo de forma constante y legítima —obras sociales, prestadores,
proveedores—, lo que vuelve difícil distinguir un mensaje fraudulento de uno
esperado. No existe programa de concientización ni segundo factor de
autenticación, de modo que una credencial obtenida es directamente utilizable.

Según el *2026 DBIR* de Verizon, el phishing representa el 14 % de los vectores
de acceso inicial conocidos en el sector Healthcare, por detrás de la explotación
de vulnerabilidades (20 %) y por delante del abuso de credenciales (11 %). El
elemento humano interviene en el 54 % de las brechas del sector, y el patrón de
*Social Engineering* reingresó este año entre los tres más frecuentes.

**Impacto: 4 (Mayor).** Una credencial administrativa comprometida habilita el
acceso a datos de facturación y de obras sociales, y puede constituir el paso
previo a un incidente de mayor alcance como R01. No se asigna 5 porque el
compromiso de una cuenta no interrumpe por sí solo la operación asistencial.

**Controles existentes.** Filtro antispam provisto por el servicio de correo.

**Plan de tratamiento: Mitigar.** Ver plan de acción PA03.

---

### R05 — Imposibilidad de restaurar los backups ante un incidente

**Descripción.** Falla en la recuperación de la información al intentar
restaurar una copia de seguridad, por corrupción de los archivos, cobertura
incompleta de los datos o inaccesibilidad del medio de respaldo.

**Activos afectados.** Backups diarios, base de datos clínica.

**Probabilidad: 3 (Posible).** El proceso de backup existe y se ejecuta
diariamente, lo que reduce la probabilidad respecto de una organización sin
respaldos. Sin embargo, nunca se realizó una prueba de restauración documentada:
un backup cuya recuperación no fue verificada es una suposición, no un control.
Se suma que las copias residen en disco local dentro de la misma red, por lo que
un ransomware que alcance el servidor puede cifrarlas junto con los datos de
producción.

**Impacto: 5 (Extremo/Catastrófico).** Es un riesgo amplificador: su
materialización convierte un incidente recuperable en una pérdida definitiva de
historias clínicas, con las consecuencias asistenciales y legales descritas en
R01. La historia clínica es además documentación de conservación obligatoria.

Un dato del *2026 DBIR* refuerza la importancia de este control: el 69 % de las
víctimas de ransomware no pagó el rescate. La capacidad de no pagar depende
directamente de poder restaurar, de modo que la verificación del respaldo es lo
que determina si la organización conserva margen de decisión frente a un
incidente.

**Controles existentes.** Backup diario automatizado a disco local.

**Plan de tratamiento: Mitigar.** Incluido en el plan de acción PA01, dado que
la copia offline y la prueba de restauración periódica atienden simultáneamente
este riesgo y la recuperación ante R01.

---

### R04 — Fuga de datos de obras sociales por envío inseguro de planillas

**Descripción.** Exposición de datos de afiliados durante el intercambio mensual
de planillas de facturación con obras sociales, por envío a destinatario
equivocado, uso de medios no cifrados o almacenamiento en servicios personales.

**Activos afectados.** Planillas de facturación, padrones de afiliados.

**Probabilidad: 4 (Probable).** El intercambio es una práctica mensual y
sostenida, de modo que la oportunidad de error se repite con regularidad. No
existe procedimiento formal ni cifrado de los archivos, y el envío queda librado
al criterio de cada administrativo.

La evidencia sectorial es contundente en este punto y motivó elevar la valoración
inicialmente asignada. El *2026 DBIR* identifica *Misdelivery* —la entrega de
datos al destinatario equivocado, en cualquier formato— como el error más
frecuente del sector Healthcare. El informe señala además que el patrón de
*Miscellaneous Errors* figura entre los tres principales del sector de forma
sostenida desde 2014, y lo caracteriza como un problema crónico. Es decir que el
error humano en el manejo de información no es un supuesto teórico sino el modo
documentado en que las organizaciones de salud pierden datos con mayor
regularidad.

**Impacto: 4 (Mayor).** Los datos comprometidos pertenecen a afiliados de un
tercero, lo que suma responsabilidad contractual frente a la obra social a la
exposición legal propia bajo la Ley 25.326. Puede derivar en la pérdida del
convenio con el financiador, con impacto económico directo.

**Controles existentes.** Ninguno formalizado.

**Plan de tratamiento: Mitigar.** Ver plan de acción PA04.

---

### R07 — Incumplimiento de la Ley 25.326 en el tratamiento de datos sensibles

**Descripción.** Incumplimiento de las obligaciones que impone la Ley 25.326 de
Protección de Datos Personales respecto de datos de salud, que revisten carácter
de datos sensibles: falta de registro de las bases de datos, ausencia de política
de privacidad formal, y ausencia de cláusulas de confidencialidad y tratamiento
en los contratos con el proveedor del HCE.

**Activos afectados.** Historias clínicas, procesos de tratamiento de datos,
contratos con proveedores.

**Probabilidad: 3 (Posible).** La auditoría externa reciente ya detectó
debilidades en la gestión de riesgos, lo que sugiere que las brechas documentales
son preexistentes y persistentes. El riesgo no depende de un evento externo sino
del estado actual de la organización: la exposición es permanente y se
materializa ante cualquier inspección, denuncia de un paciente o incidente que
active una investigación.

**Impacto: 4 (Mayor).** Sanciones de la autoridad de aplicación, obligación de
remediación en plazos acotados y daño reputacional. No se asigna 5 porque el
efecto es administrativo y legal, sin interrupción inmediata de la operación
asistencial.

En cuanto a la dimensión contractual, el *2026 DBIR* atribuye a la participación
de terceros el 32 % de las brechas del sector Healthcare y señala expresamente
que los fundamentos de seguridad deben quedar incorporados en los contratos
celebrados con proveedores y asociados de negocio, y no limitarse a la propia
organización. La ausencia de cláusulas de confidencialidad y tratamiento de datos
en el contrato con el proveedor del HCE es, por lo tanto, una brecha con
correlato empírico además de normativo.

**Controles existentes.** Consentimiento informado de pacientes, con cobertura
parcial y sin verificación sistemática.

**Plan de tratamiento: Mitigar.**

---

### R06 — Interrupción del servicio por falla eléctrica o de climatización

**Descripción.** Indisponibilidad del servidor de HCE y del equipamiento de red
por corte prolongado del suministro eléctrico o falla del sistema de
refrigeración de la sala de servidores.

**Activos afectados.** Sala de servidores, servidor HCE, equipamiento de red.

**Probabilidad: 3 (Posible).** La infraestructura reside en una sala propia
dentro del edificio y no en un centro de datos con redundancia. Los cortes de
suministro y las fallas de equipos de climatización son eventos ordinarios, no
excepcionales, y el UPS existente sostiene la operación por un lapso limitado sin
generador de respaldo.

**Impacto: 3 (Moderado).** La interrupción afecta la operación digital durante
horas, pero la clínica conserva la capacidad de operar transitoriamente con
procedimientos manuales de registro. El evento es recuperable sin pérdida
permanente de información, siempre que el apagado no corrompa la base de datos.

**Controles existentes.** UPS que protege el servidor principal.

**Plan de tratamiento: Mitigar.**

---

## Planes de acción

Se definen cuatro planes de acción, uno por cada riesgo de nivel Crítico. PA01
atiende simultáneamente R01 y R05, dado que ambos comparten la copia de respaldo
verificada como control determinante.

| ID | Riesgo | Título | Vencimiento | Responsable | Presupuesto | Estado |
|---|---|---|---|---|---|---|
| PA01 | R01, R05 | Esquema de respaldo verificado y contención de propagación | 90 días | Responsable de Sistemas | USD 12.000 | No iniciado |
| PA02 | R02 | Trazabilidad y perfilado de accesos a la historia clínica | 60 días | Responsable de Sistemas | USD 3.500 | No iniciado |
| PA03 | R03 | Segundo factor de autenticación y concientización del personal | 120 días | Jefe de Administración | USD 5.000 | No iniciado |
| PA04 | R04 | Procedimiento seguro de intercambio con obras sociales | 45 días | Jefe de Administración | USD 1.500 | No iniciado |

### PA01 — Esquema de respaldo verificado y contención de propagación

**Riesgos que atiende:** R01 (Crítico, 20) y R05 (Alto, 15).

**Descripción.** Incorporación de una copia de respaldo fuera de línea y fuera
de la red de producción, con prueba de restauración trimestral documentada y
firmada. En paralelo, segmentación de la red que separe el segmento clínico del
administrativo, de modo que el compromiso de una estación no alcance al servidor
de HCE, e incorporación de una solución de detección y respuesta en endpoints.

**Justificación de la prioridad.** Es el plan de mayor urgencia porque atiende el
riesgo de mayor valor del registro y, simultáneamente, el único control que
convierte un incidente de ransomware de catastrófico en recuperable.

**Vencimiento:** 90 días. **Responsable:** Responsable de Sistemas.
**Presupuesto estimado:** USD 12.000. **Estado inicial:** No iniciado.

### PA02 — Trazabilidad y perfilado de accesos a la historia clínica

**Riesgo que atiende:** R02 (Crítico, 16).

**Descripción.** Eliminación de los usuarios compartidos por turno y asignación
de credenciales nominales a cada agente. Definición de perfiles de acceso por
servicio, de manera que un usuario sólo consulte historias clínicas del área en
que se desempeña. Establecimiento de una revisión mensual de los registros de
acceso, con reporte a Dirección Médica.

**Justificación de la prioridad.** Es el plan de menor costo del conjunto y
actúa sobre un riesgo crítico. La trazabilidad nominal, además, tiene efecto
disuasivo inmediato: el acceso indebido deja de ser anónimo.

**Vencimiento:** 60 días. **Responsable:** Responsable de Sistemas.
**Presupuesto estimado:** USD 3.500. **Estado inicial:** No iniciado.

### PA03 — Segundo factor de autenticación y concientización del personal

**Riesgo que atiende:** R03 (Crítico, 16).

**Descripción.** Habilitación de segundo factor de autenticación en el correo
institucional y en los accesos remotos. Programa de concientización con
capacitación inicial obligatoria y campañas de phishing simulado con periodicidad
trimestral, incorporando a la inducción del personal ingresante.

**Justificación de la prioridad.** El segundo factor neutraliza el valor de una
credencial robada, que es el objetivo del phishing. El plazo es mayor porque el
componente de concientización requiere sostenerse en el tiempo para producir
efecto medible.

**Vencimiento:** 120 días. **Responsable:** Jefe de Administración.
**Presupuesto estimado:** USD 5.000. **Estado inicial:** No iniciado.

### PA04 — Procedimiento seguro de intercambio con obras sociales

**Riesgo que atiende:** R04 (Crítico, 16).

**Descripción.** Formalización del procedimiento de envío de planillas: cifrado
de los archivos con clave comunicada por canal distinto al del envío, lista de
destinatarios autorizados verificada y actualizada por obra social, doble
verificación del destinatario antes de cada envío y prohibición expresa del uso
de servicios personales de almacenamiento o correo. Se complementa con una
instrucción breve al personal administrativo sobre el procedimiento.

**Justificación de la prioridad.** Es el plan de menor costo y menor plazo del
conjunto, y sin embargo atiende un riesgo de nivel Crítico. La desproporción no
es casual: los riesgos derivados de error humano en procedimientos administrativos
suelen mitigarse con controles de proceso antes que con inversión tecnológica.
Esto lo convierte en la acción de mayor retorno inmediato del plan de tratamiento.

**Vencimiento:** 45 días. **Responsable:** Jefe de Administración.
**Presupuesto estimado:** USD 1.500. **Estado inicial:** No iniciado.

---

## Correspondencia con la carga en SimpleRisk

Valores utilizados al registrar cada riesgo en la aplicación. La columna
*Propietario* de la tabla principal indica el rol organizacional responsable
dentro del escenario; el campo *Owner* de SimpleRisk se completa con el usuario
de la plataforma que gestiona el riesgo, dado que la aplicación sólo admite
usuarios registrados en ese campo.

| ID | Category | Risk Source | Technology | Likelihood | Impact |
|---|---|---|---|---|---|
| R01 | Technical Vulnerability Management | System | All | Likely | Extreme/Catastrophic |
| R02 | Access Management | People | All | Likely | Major |
| R03 | Policy and Procedure | People | Mail Routing | Likely | Major |
| R04 | Sensitive Data Management | Process | Mail Routing | Likely | Major |
| R05 | Environmental Resilience | Process | Backups | Credible | Extreme/Catastrophic |
| R06 | Physical Security | External | Datacenter | Credible | Moderate |
| R07 | Policy and Procedure | Process | All | Credible | Major |

En todos los casos: **Site/Location** All Sites, **Team** Information Security,
**Risk Scoring Method** Classic, **Owner** `analista_riesgos`,
**Owner's Manager** `admin_sistemas_clinica`.

## Referencias

- Ley 25.326 de Protección de los Datos Personales (Argentina).
- Verizon Business (2026). *2026 Data Breach Investigations Report — Healthcare
  snapshot*. Disponible en:
  https://www.verizon.com/business/resources/reports/2026-dbir-healthcare-snapshot.pdf
- ISO/IEC 27005: Information security risk management.
- NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments.
