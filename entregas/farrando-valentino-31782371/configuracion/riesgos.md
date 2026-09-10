# Registro y evaluación de riesgos

## Alcance

Escenario académico de una clínica privada ficticia con 120 empleados
y 800 pacientes diarios.

Se evalúan siete riesgos sobre los activos A01–A07.
Los controles existentes y las condiciones descritas son supuestos
del ejercicio, no hallazgos sobre una organización real.

El riesgo de prueba ID 1001 se excluye del análisis definitivo.

## Método de evaluación

Se utiliza el método Classic de SimpleRisk:

Puntuación = Probabilidad × Impacto

Ambas variables se valoran entre 1 y 5.
La normalización a escala 0–10 está desactivada.

La probabilidad se estima cualitativamente para los próximos
12 meses. Las valoraciones no representan frecuencias medidas.

### Probabilidad

| Valor | Opción en SimpleRisk | Interpretación |
|---|---|---|
| 1 | Remote | Remota |
| 2 | Unlikely | Poco probable |
| 3 | Credible | Posible |
| 4 | Likely | Probable |
| 5 | Almost Certain | Casi cierta |

### Impacto

| Valor | Opción en SimpleRisk | Interpretación |
|---|---|---|
| 1 | Insignificant | Insignificante |
| 2 | Minor | Menor |
| 3 | Moderate | Moderado |
| 4 | Major | Mayor |
| 5 | Extreme/Catastrophic | Extremo o catastrófico |

### Niveles de riesgo

| Puntuación | Nivel del informe | Color |
|---|---|---|
| 1–4 | Bajo | Verde |
| 5–9 | Medio | Amarillo |
| 10–15 | Alto | Naranja |
| 16–25 | Crítico | Rojo |

El nivel Very High de SimpleRisk corresponde a Crítico en este informe.

## Resumen

| ID | Riesgo | P | I | Puntuación | Nivel | Propietario | Estrategia |
|---|---|---|---|---|---|---|---|
| R01 | Ransomware bloquea las historias clínicas y la atención | 4 | 5 | 20 | Crítico | Dirección Médica | Mitigar |
| R02 | Acceso no autorizado a datos de obras sociales y facturación | 4 | 4 | 16 | Crítico | Responsable de Administración | Mitigar |
| R03 | Alteración accidental de importes y prestaciones en facturación | 3 | 4 | 12 | Alto | Responsable de Administración | Mitigar |
| R04 | Falla del servidor interrumpe el sistema de gestión clínica | 3 | 4 | 12 | Alto | Dirección Médica | Mitigar |
| R05 | Corte de Internet impide gestionar autorizaciones de obras sociales | 3 | 3 | 9 | Medio | Responsable de Administración | Mitigar |
| R06 | Acceso no autorizado a la red interna desde Wi-Fi de invitados | 3 | 4 | 12 | Alto | Responsable de Sistemas | Mitigar |
| R07 | Copias de seguridad no recuperables ante una pérdida de datos | 3 | 4 | 12 | Alto | Responsable de Sistemas | Mitigar |

Distribución: 2 riesgos críticos, 4 altos y 1 medio.

## R01 - Ransomware bloquea las historias clínicas y la atención

- Categoría: Technical Vulnerability Management.
- Activos afectados: A01, A02, A03, A04 y A06.
- Propietario: Dirección Médica.
- Responsable técnico del tratamiento: Responsable de Sistemas.

### Escenario

Un correo malicioso compromete un equipo del personal.
El software malicioso se propaga y cifra información del servidor
y las copias de seguridad accesibles desde la red.

### Debilidades y controles existentes

Se supone antivirus básico, actualizaciones manuales sin
verificación centralizada y copias diarias conectadas a la red.
Estas medidas ofrecen protección limitada frente al escenario.

### Justificación de la valoración

Probabilidad 4: la exposición al correo y la falta de gestión
centralizada de protección y actualizaciones hacen probable
el escenario dentro de los supuestos del ejercicio.

Impacto 5: el bloqueo simultáneo de la aplicación, las historias
y los respaldos puede provocar una interrupción prolongada
de servicios esenciales para la atención.

Puntuación: 4 × 5 = 20, crítico.

### Tratamiento

Mitigar mediante protección centralizada de equipos, actualizaciones,
filtros de correo, capacitación, segmentación y respaldos recuperables.

Plan detallado asociado: PA01.
Se complementa con las medidas de R06 y el plan PA03 de R07.

## R02 - Acceso no autorizado a datos de obras sociales y facturación

- Categoría: Access Management.
- Activos afectados: A07 y A06.
- Propietario: Responsable de Administración.
- Responsable técnico del tratamiento: Responsable de Sistemas.

### Escenario

Un integrante del personal accede a planillas de obras sociales
y facturación que no necesita para sus funciones, y puede
consultarlas o copiarlas sin autorización organizacional.

### Debilidades y controles existentes

Se suponen cuentas con contraseña y permisos básicos sobre
una carpeta compartida. Los permisos son excesivos y no
se revisan periódicamente.

### Justificación de la valoración

Probabilidad 4: los accesos innecesarios permanecen disponibles
durante el trabajo habitual, sin revisiones periódicas.

Impacto 4: la exposición de numerosos registros puede afectar
la privacidad, la confianza y la relación con las obras sociales.

Puntuación: 4 × 4 = 16, crítico.

### Tratamiento

Mitigar mediante permisos por función, aprobación de accesos,
retiro de permisos innecesarios y revisiones periódicas.

Plan detallado asociado: PA02.
Administración valida la matriz de acceso y Sistemas la implementa.

## R03 - Alteración accidental de importes y prestaciones en facturación

- Categoría: Policy and Procedure.
- Activos afectados: A07 y A06.
- Propietario: Responsable de Administración.

### Escenario

Durante la edición de planillas se modifica por error una fórmula,
un importe o la asociación entre paciente y prestación.
El error se incorpora al lote de facturación enviado.

### Debilidades y controles existentes

Se supone revisión informal por quien prepara las planillas,
comprobantes de respaldo y copias diarias.
No existen protección suficiente de fórmulas ni una segunda
validación independiente.

### Justificación de la valoración

Probabilidad 3: el trabajo manual permite errores plausibles,
aunque no se dispone de una frecuencia histórica.

Impacto 4: se supone que el error afecta un lote mensual completo,
provocando rechazos, reprocesos y demoras relevantes en los cobros.

Puntuación: 3 × 4 = 12, alto.

### Tratamiento

Mitigar mediante protección de fórmulas, validaciones de datos,
control de versiones, conciliación y revisión por otra persona.

Plan detallado pendiente de desarrollo.

## R04 - Falla del servidor interrumpe el sistema de gestión clínica

- Categoría: Environmental Resilience.
- Activos afectados: A03, A02 y A01.
- Propietario: Dirección Médica.
- Responsable técnico del tratamiento: Responsable de Sistemas.

### Escenario

Una falla de hardware deja fuera de servicio el único servidor
que aloja el sistema de gestión clínica y su base de datos.

### Debilidades y controles existentes

Se suponen soporte técnico y copias diarias, pero no un servidor
alternativo con conmutación automática ni pruebas de recuperación.
Existe posibilidad de continuar parcialmente mediante registros manuales.

### Justificación de la valoración

Probabilidad 3: la falla de hardware es un evento posible.
No se afirma que el equipo esté deteriorado ni se dispone
de estadísticas de fallas.

Impacto 4: se supone una interrupción de una jornada,
con demoras importantes y continuidad manual parcial.
La falta de redundancia aumenta las consecuencias del evento.

Puntuación: 3 × 4 = 12, alto.

### Tratamiento

Mitigar mediante infraestructura alternativa, monitoreo,
procedimientos de recuperación y pruebas de continuidad.
Definir y validar el tiempo objetivo de recuperación.

Plan detallado pendiente de desarrollo.

## R05 - Corte de Internet impide gestionar autorizaciones de obras sociales

- Categoría: Third-Party Management.
- Activos afectados: A05 y A07.
- Propietario: Responsable de Administración.

### Escenario

Una interrupción del proveedor de Internet impide acceder
a los portales externos de autorizaciones y facturación.

### Debilidades y controles existentes

Se supone un único proveedor, soporte contractual y registro
local de trámites pendientes. No existe un enlace alternativo.

### Justificación de la valoración

Probabilidad 3: una interrupción del proveedor es posible,
sin contar con estadísticas de disponibilidad.

Impacto 3: se supone una caída de varias horas que retrasa
los trámites externos. El sistema clínico local continúa operativo.

Puntuación: 3 × 3 = 9, medio.

### Tratamiento

Mitigar mediante un enlace alternativo independiente,
procedimientos de contingencia y seguimiento del proveedor.
La atención urgente no debe depender de obtener una autorización en línea.

Plan detallado pendiente de desarrollo.

## R06 - Acceso no autorizado a la red interna desde Wi-Fi de invitados

- Categoría: Access Management.
- Activos afectados: A05, A03, A02 y A01.
- Propietario: Responsable de Sistemas.

### Escenario

Una persona conectada al Wi-Fi de invitados alcanza recursos
internos y aprovecha credenciales débiles o una vulnerabilidad
para acceder sin autorización.

### Debilidades y controles existentes

Se supone autenticación en los sistemas internos, pero una
segmentación insuficiente entre invitados y recursos de la clínica.
Poder alcanzar un servicio no implica por sí solo haberlo comprometido.

### Justificación de la valoración

Probabilidad 3: el escenario es posible por la exposición interna,
aunque requiere superar la autenticación o explotar otra debilidad.

Impacto 4: un acceso exitoso puede comprometer la confidencialidad
o integridad de numerosos registros clínicos.

Puntuación: 3 × 4 = 12, alto.

### Tratamiento

Mitigar mediante separación de la red de invitados,
acceso exclusivo a Internet, bloqueo de conexiones internas
y pruebas de aislamiento y registro de eventos.

Plan detallado pendiente de desarrollo.

## R07 - Copias de seguridad no recuperables ante una pérdida de datos

- Categoría: Policy and Procedure.
- Activos afectados: A04, A01 y A07.
- Propietario: Responsable de Sistemas.

### Escenario

Después de una eliminación accidental se intenta restaurar
información y se descubre que los respaldos están incompletos,
corruptos o no incluyen los datos necesarios.

### Debilidades y controles existentes

Se suponen copias diarias, sin pruebas periódicas de restauración
ni validación suficiente de cobertura e integridad.
La falta de pruebas genera incertidumbre; no demuestra
que las copias estén efectivamente dañadas.

### Justificación de la valoración

Probabilidad 3: la combinación de pérdida accidental y problemas
de recuperación se considera posible bajo estos supuestos.

Impacto 4: se supone la pérdida de un conjunto relevante de datos,
con reconstrucción manual parcial, demoras y afectación operativa.

Puntuación: 3 × 4 = 12, alto.

### Tratamiento

Mitigar mediante verificación de cobertura, copias aisladas,
monitoreo y pruebas de restauración en un entorno separado.
Definir objetivos de recuperación y pérdida de datos tolerable.

Plan detallado asociado: PA03.
Este escenario se diferencia del cifrado malicioso de R01,
aunque comparte medidas de recuperación.

## Estado del tratamiento y riesgo residual

Los planes PA01, PA02 y PA03 están registrados como planificados,
pendientes de aprobación y ejecución.

Mitigation Percent permanece en 0: no se ha acreditado reducción
del riesgo por medidas implementadas.

Las puntuaciones actuales se mantienen.
Cualquier valoración residual objetivo será una estimación
condicionada a implementar las medidas y comprobar su eficacia.

Los otros cuatro riesgos tienen una estrategia propuesta,
pero todavía no un plan detallado registrado.
La ausencia de un plan detallado no significa aceptación del riesgo.
