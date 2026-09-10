# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## 1. Introducción

El presente trabajo práctico tiene como objetivo aplicar conceptos de gestión de riesgos de seguridad de sistemas mediante la utilización de SimpleRisk.

Para el desarrollo del trabajo se configuró un escenario correspondiente a una clínica privada que utiliza sistemas informáticos para gestionar información de pacientes, historias clínicas digitales, datos de obras sociales y facturación.

A partir del escenario planteado se identificaron diferentes riesgos relacionados con la seguridad, disponibilidad e integridad de la información. Estos riesgos fueron registrados en SimpleRisk para realizar su evaluación, seguimiento y tratamiento.

## 2. Usuarios y roles

Se configuraron diferentes usuarios dentro de SimpleRisk, asignando a cada uno un rol de acuerdo con sus funciones.

Los usuarios configurados fueron:

- Administrador Clinica Demo - Administrador.
- Administrador Demo - Administrador.
- Analista de Riesgos Demo - Analista de Riesgos.
- Auditor Demo - Auditor.

La configuración de usuarios permite diferenciar las funciones y responsabilidades dentro del sistema de gestión de riesgos y aplicar distintos niveles de acceso según el rol de cada usuario.

## 3. Identificación y registro de riesgos

Se registraron ocho riesgos relacionados con el funcionamiento y la seguridad de la clínica.

Los riesgos registrados fueron:

1. Prueba de funcionamiento - acceso no autorizado.
2. Uso indebido de cuentas con acceso a historias clínicas.
3. Modificación incorrecta de una historia clínica.
4. Exposición de información de pacientes mediante exportaciones.
5. Interrupción del sistema de historias clínicas durante la atención.
6. Error en la facturación de prestaciones a obras sociales.
7. Acceso de personal que ya no debería tener permisos.
8. Indisponibilidad de información por fallas en las copias de respaldo.

Cada riesgo fue registrado en SimpleRisk con información relacionada con su categoría, activo afectado, probabilidad, impacto, nivel de riesgo, propietario y tratamiento propuesto.

## 4. Evaluación de riesgos

La evaluación de los riesgos se realizó utilizando la metodología de puntuación clásica de SimpleRisk, basada en la combinación de probabilidad e impacto.

Los riesgos presentan diferentes niveles de acuerdo con la valoración obtenida, permitiendo establecer prioridades para su tratamiento.

Entre los riesgos identificados se encuentran situaciones relacionadas con el acceso no autorizado, modificación incorrecta de información, exposición de datos de pacientes, interrupción de servicios, errores de facturación y problemas con las copias de respaldo.

Uno de los riesgos con mayor valoración fue:

**ID 1008 - Indisponibilidad de información por fallas en las copias de respaldo**

- Riesgo inherente: 8 (High).
- Riesgo residual: 4 (Medium).
- Probabilidad actual: Likely.
- Impacto actual: Extreme/Catastrophic.

Este riesgo se considera importante debido a que una falla en las copias de respaldo podría impedir la recuperación de información clínica necesaria para el funcionamiento de la organización.

También se analizó el riesgo:

**ID 1003 - Modificación incorrecta de una historia clínica**

- Riesgo inherente: 6 (Medium).
- Riesgo residual: 3 (Low).
- Probabilidad actual: Credible.
- Impacto actual: Extreme/Catastrophic.

Una modificación incorrecta o no autorizada de una historia clínica puede afectar la integridad de la información utilizada durante la atención de los pacientes y generar consecuencias para el funcionamiento de la clínica.

## 5. Tratamiento y mitigación

Para los riesgos que requieren tratamiento se utilizaron las funciones de mitigación disponibles en SimpleRisk.

En el caso del riesgo **ID 1008 - Indisponibilidad de información por fallas en las copias de respaldo**, se estableció:

- Estrategia de planificación: Mitigate.
- Esfuerzo de mitigación: Significant.
- Porcentaje de mitigación: 50%.
- Costo estimado: $0 a $100.000.
- Responsable de la mitigación: Analista de Riesgos Demo.

La solución propuesta consiste en realizar copias de respaldo de las historias clínicas y de la información importante. También se recomienda realizar pruebas periódicas de recuperación para comprobar que las copias puedan utilizarse correctamente cuando sea necesario.

Luego de establecer la mitigación, el riesgo pasó de un valor inherente de **8 (High)** a un riesgo residual de **4 (Medium)**.

También se trabajó sobre el riesgo **ID 1003 - Modificación incorrecta de una historia clínica**, que pasó de un riesgo inherente de **6 (Medium)** a un riesgo residual de **3 (Low)**.

Para este riesgo se propuso fortalecer los controles de acceso, realizar revisiones periódicas de permisos y establecer mecanismos de control sobre las modificaciones realizadas en las historias clínicas.

## 6. Revisión de riesgos

Se utilizó la sección de revisión periódica de SimpleRisk para realizar el seguimiento del estado de los riesgos registrados.

La herramienta permite identificar riesgos pendientes de revisión y consultar las fechas previstas para futuras revisiones.

El riesgo **ID 1008 - Indisponibilidad de información por fallas en las copias de respaldo** figura con estado **Mitigation Planned**, debido a que cuenta con un plan de mitigación establecido.

El riesgo **ID 1003 - Modificación incorrecta de una historia clínica** figura con estado **Mgmt Reviewed**, indicando que fue revisado por la gestión.

El seguimiento periódico permite comprobar la evolución de los riesgos y verificar si las medidas implementadas producen una reducción adecuada del riesgo residual.

## 7. Planes de acción

Para el riesgo ID 1008, relacionado con la indisponibilidad de información por fallas en las copias de respaldo, se definieron tres planes de acción para reducir el riesgo y mejorar la capacidad de recuperación de la información.

### Plan 1 - Verificar las copias de respaldo

- Descripción: revisar que las copias de respaldo de la información clínica se estén realizando correctamente y que los archivos generados puedan ser identificados y utilizados.
- Fecha de vencimiento: 30/09/2026.
- Responsable: Analista de Riesgos Demo.
- Presupuesto estimado: USD 300.
- Estado inicial: No iniciado.

### Plan 2 - Realizar una prueba de recuperación

- Descripción: realizar una prueba de restauración a partir de una copia de respaldo para comprobar que la información pueda recuperarse correctamente en caso de una falla.
- Fecha de vencimiento: 15/10/2026.
- Responsable: Analista de Riesgos Demo.
- Presupuesto estimado: USD 500.
- Estado inicial: No iniciado.

### Plan 3 - Mejorar el esquema de respaldo

- Descripción: revisar el esquema actual de copias de respaldo y proponer mejoras para aumentar la disponibilidad y facilitar la recuperación de la información.
- Fecha de vencimiento: 31/10/2026.
- Responsable: Analista de Riesgos Demo.
- Presupuesto estimado: USD 700.
- Estado inicial: No iniciado.

Las fechas y presupuestos son estimaciones realizadas para este trabajo práctico. Los planes se presentan como acciones propuestas para el tratamiento del riesgo y no como tareas ejecutadas.

## 8. Análisis crítico y profundización

### 8.1 Comparación metodológica

SimpleRisk utiliza un enfoque clásico de evaluación de riesgos basado principalmente en la combinación de probabilidad e impacto para obtener un nivel de riesgo.

Este enfoque permite realizar una evaluación sencilla y comprensible, facilitando la identificación y priorización de los riesgos dentro de una organización.

Como metodología alternativa se considera NIST SP 800-30, una guía orientada a la realización de evaluaciones de riesgo de seguridad de la información.

Una de las principales ventajas del enfoque utilizado por SimpleRisk es su simplicidad. La utilización de una escala de probabilidad e impacto permite registrar y comparar riesgos de manera rápida y facilita la comprensión de los resultados.

Otra ventaja es que permite centralizar los riesgos, sus tratamientos y revisiones dentro de una misma herramienta.

Como desventaja, el enfoque basado en probabilidad e impacto puede resultar limitado cuando se necesita realizar un análisis más detallado de las amenazas, vulnerabilidades, escenarios y diferentes factores que pueden influir en un riesgo.

NIST SP 800-30 propone un proceso más estructurado para identificar y analizar factores relacionados con las amenazas, vulnerabilidades, probabilidad e impacto.

Por lo tanto, SimpleRisk resulta adecuado para organizaciones que necesitan una herramienta práctica para registrar, evaluar y realizar el seguimiento de sus riesgos. Por otro lado, NIST SP 800-30 puede ser más conveniente cuando se necesita realizar una evaluación de riesgos más detallada y estructurada.

### 8.2 Integración con una herramienta externa

Una posible integración de SimpleRisk sería conectarlo con un sistema externo de gestión de tickets, como Jira.

Ante la identificación de un riesgo que requiere tratamiento, se podría generar un ticket con la información principal del riesgo, incluyendo su descripción, nivel de riesgo, responsable, acción de mitigación y fecha de vencimiento.

De esta manera, SimpleRisk se utilizaría para registrar y gestionar los riesgos, mientras que el sistema de tickets permitiría realizar el seguimiento de las tareas necesarias para implementar las medidas de tratamiento.

La integración permitiría mejorar el seguimiento de las acciones de mitigación y facilitar la comunicación entre los responsables de seguridad y los equipos técnicos.

## 9. Conclusión

La utilización de SimpleRisk permitió aplicar un proceso de gestión de riesgos de seguridad de sistemas dentro del escenario de una clínica privada.

Se identificaron y registraron ocho riesgos relacionados con diferentes aspectos de la seguridad de la información, incluyendo el acceso a historias clínicas, la integridad de los datos, la disponibilidad de los sistemas, la exposición de información y la recuperación mediante copias de respaldo.

A través de la evaluación de probabilidad e impacto fue posible establecer diferentes niveles de riesgo y determinar cuáles requerían una mayor prioridad de tratamiento.

Las funciones de mitigación de SimpleRisk permitieron establecer medidas para reducir los riesgos. Como resultado, algunos riesgos presentaron una disminución de su nivel residual, como ocurrió con el riesgo ID 1008, que pasó de 8 (High) a 4 (Medium), y con el riesgo ID 1003, que pasó de 6 (Medium) a 3 (Low).

Además, la utilización de revisiones periódicas y planes de acción permite realizar un seguimiento de los riesgos y de las medidas propuestas.

Finalmente, la comparación metodológica permitió observar que SimpleRisk ofrece un enfoque práctico y sencillo para la gestión de riesgos, mientras que metodologías como NIST SP 800-30 permiten realizar evaluaciones más estructuradas y detalladas.