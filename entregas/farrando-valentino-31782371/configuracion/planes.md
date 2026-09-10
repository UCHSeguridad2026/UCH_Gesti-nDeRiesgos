# Planes de tratamiento

## Estado general

Los tres planes están registrados en SimpleRisk como planificados,
pendientes de aprobación presupuestaria y ejecución.

Las medidas propuestas todavía no se consideran implementadas.
Mitigation Percent permanece en 0 en los tres registros.
Este campo representa reducción del riesgo, no avance de tareas.

Los presupuestos son estimaciones académicas simuladas en USD,
no cotizaciones comerciales.

## Resumen

| Plan | Riesgo | Responsable de ejecución | Vencimiento | Presupuesto | Estado |
|---|---|---|---|---|---|
| PA01 | R01 - Ransomware | Responsable de Sistemas | 2026-09-30 | USD 8.000 | Planificado |
| PA02 | R02 - Acceso no autorizado a facturación | Responsable de Sistemas | 2026-09-23 | USD 1.200 | Planificado |
| PA03 | R07 - Respaldos no recuperables | Responsable de Sistemas | 2026-09-30 | USD 3.000 | Planificado |

Presupuesto total estimado: USD 12.200.

## PA01 - Protección de equipos y correo frente a ransomware

- Riesgo asociado: R01.
- Propietario del riesgo: Dirección Médica.
- Responsable de ejecución: Responsable de Sistemas.
- Estrategia: Mitigate.
- Esfuerzo registrado: Significant.
- Vencimiento: 30 de septiembre de 2026.
- Estado: planificado, pendiente de aprobación y ejecución.

### Situación inicial

Se supone antivirus básico y actualizaciones manuales sin
verificación centralizada. Existen copias diarias conectadas
a la red, sin aislamiento ni pruebas periódicas de restauración.

### Acciones

1. Inventariar los equipos y verificar su protección y actualizaciones.
2. Implementar protección centralizada de endpoints con capacidad
   de detección y aislamiento.
3. Centralizar las actualizaciones y documentar las excepciones.
4. Configurar filtros de archivos y enlaces maliciosos en el correo.
5. Capacitar al personal para reconocer y reportar correos sospechosos.

### Criterios de finalización

- Todos los equipos del alcance están inventariados y protegidos.
- Las actualizaciones están verificadas y las excepciones documentadas.
- Se realiza una prueba controlada de alertas y aislamiento,
  sin utilizar malware real.
- Se comprueba el funcionamiento de los filtros de correo.
- La capacitación queda registrada.

### Presupuesto académico

Estimación para el primer año: USD 8.000.

Supuesto de dimensionamiento: 60 puestos de trabajo.
La cantidad de empleados no se equipara automáticamente
con la cantidad de computadoras.

| Concepto | Estimación |
|---|---|
| Licencias | USD 4.500 |
| Configuración | USD 2.000 |
| Capacitación y pruebas | USD 1.500 |
| Total | USD 8.000 |

El alcance y los importes requieren validación antes de aprobarse.

### Dependencias y recomendaciones

Este plan cubre equipos y correo.
Se complementa con la segmentación propuesta para R06
y las copias recuperables de PA03.

Como analogía solicitada en la consigna, los 3 cerditos representan
la importancia de construir defensas resistentes.
En seguridad, las capas de prevención, detección, respuesta
y recuperación se complementan.

La puntuación actual de R01 permanece en 20, crítico,
hasta implementar las medidas y verificar su eficacia.

## PA02 - Control de acceso a datos de obras sociales y facturación

- Riesgo asociado: R02.
- Propietario del riesgo: Responsable de Administración.
- Responsable de ejecución: Responsable de Sistemas.
- Validación funcional: Responsable de Administración.
- Estrategia: Mitigate.
- Esfuerzo registrado: Considerable.
- Vencimiento: 23 de septiembre de 2026.
- Estado: planificado, pendiente de aprobación y ejecución.

### Situación inicial

Se suponen cuentas individuales con contraseña y permisos básicos
en una carpeta compartida. Existen accesos excesivos
y no se realizan revisiones periódicas.

### Acciones

1. Inventariar las carpetas, los archivos y los usuarios con acceso.
2. Definir una matriz de permisos según las funciones del personal.
3. Obtener la validación de Administración sobre los accesos necesarios.
4. Aplicar permisos mediante grupos y retirar los accesos innecesarios.
5. Probar accesos permitidos y denegados con cuentas de prueba.
6. Establecer revisiones trimestrales y revisiones ante bajas
   o cambios de función.

### Criterios de finalización

- Existe un inventario de recursos y accesos.
- Administración aprueba la matriz de permisos.
- Los permisos aplicados coinciden con la matriz aprobada.
- Las pruebas de acceso permitido y denegado quedan documentadas.
- Se establece un responsable y una frecuencia de revisión.

### Presupuesto académico

Estimación: USD 1.200.

Se suponen 30 horas de trabajo a USD 40 por hora.
No se prevé adquisición de nuevas licencias en esta estimación.
La disponibilidad de herramientas y las horas requieren validación.

### Recomendaciones

Aplicar mínimo privilegio y conservar evidencia de las aprobaciones
y revisiones. Sistemas ejecuta los cambios y Administración
determina quién necesita acceder a la información.

La puntuación actual de R02 permanece en 16, crítico,
hasta implementar las medidas y verificar su eficacia.

## PA03 - Copias de seguridad recuperables y pruebas de restauración

- Riesgo asociado: R07.
- Propietario del riesgo: Responsable de Sistemas.
- Responsable de ejecución: Responsable de Sistemas.
- Estrategia: Mitigate.
- Esfuerzo registrado: Significant.
- Vencimiento: 30 de septiembre de 2026.
- Estado: planificado, pendiente de aprobación y ejecución.

### Situación inicial

Se suponen copias diarias conectadas a la red, sin pruebas periódicas
de restauración ni validación suficiente de cobertura e integridad.
Su existencia no demuestra que puedan recuperarse los datos necesarios.

### Acciones

1. Inventariar los datos, las aplicaciones y las configuraciones
   que deben recuperarse.
2. Acordar con las áreas usuarias el tiempo objetivo de recuperación
   y la pérdida de datos tolerable.
3. Diseñar un esquema de tres copias, en dos tipos de medios,
   con una copia fuera del sitio.
4. Incorporar una copia desconectada o inmutable y credenciales
   separadas para administrar los respaldos.
5. Configurar monitoreo y alertas diarias sobre las tareas de respaldo.
6. Realizar una restauración de prueba en un entorno separado.
7. Validar con las áreas usuarias la integridad y utilidad
   de la información recuperada.
8. Programar pruebas trimestrales y documentar los resultados.

### Criterios de finalización

- El inventario define el alcance de los respaldos.
- Se documentan y acuerdan los objetivos de recuperación.
- El esquema de copias y su aislamiento quedan comprobados.
- Las alertas de fallas se prueban.
- Se completa una restauración del alcance acordado
  y se registra el tiempo empleado.
- Las áreas usuarias validan los datos recuperados.
- Existe un procedimiento y un calendario de pruebas.

### Presupuesto académico

Estimación para el primer año: USD 3.000.

| Concepto | Estimación |
|---|---|
| Almacenamiento y copia externa | USD 1.500 |
| Configuración, pruebas y documentación | USD 1.500 |
| Total | USD 3.000 |

El importe depende del volumen de datos, la retención
y los objetivos de recuperación, pendientes de validación.

### Recomendaciones

Realizar las pruebas en un entorno separado para evitar
sobrescribir información operativa.

Este plan también contribuye a la recuperación frente a R01,
pero no reemplaza las medidas de prevención de ransomware.

La puntuación actual de R07 permanece en 12, alto,
hasta implementar las medidas y verificar su eficacia.

## Registro económico en SimpleRisk

En Mitigation Cost se seleccionó el rango disponible
"$0 to $100,000" para los tres planes.

Los presupuestos concretos se documentaron en el texto del plan.
El rango de la aplicación no representa el presupuesto aprobado.

## Seguimiento

En cada revisión se deberá registrar:

- Estado de aprobación y ejecución.
- Acciones completadas y pendientes.
- Evidencias de las pruebas.
- Costos y fechas actualizados.
- Desvíos y decisiones del responsable.

La reducción del riesgo se evaluará después de comprobar
la eficacia de las medidas. Registrar un plan no demuestra
que el riesgo haya disminuido.
