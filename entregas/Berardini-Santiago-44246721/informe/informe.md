# Informe - TP Gestión de Riesgos con SimpleRisk

**Alumno:** Santiago Berardini
**LU:** 44246721
**Materia:** Seguridad de Sistemas

## 1. Introducción

Este informe documenta el trabajo realizado para el TP de gestión de riesgos usando SimpleRisk. El objetivo fue simular el trabajo de un responsable de seguridad en una clínica privada de 120 empleados y 800 pacientes por día, identificando riesgos reales del negocio y proponiendo cómo tratarlos.

## 2. Decisiones de diseño

- Se instaló SimpleRisk usando Docker, con la imagen oficial `simplerisk/simplerisk`, que incluye la aplicación y su base de datos en un solo contenedor. Esto se documentó en un archivo `docker-compose.yml` dentro de la carpeta `entorno/`, para que el entorno sea fácil de reproducir.
- Se crearon 3 usuarios con roles diferentes (Admin, Analista de Riesgos y Auditor), para reflejar cómo estarían organizados los permisos en una clínica real: no todos deberían poder hacer todo.
- Para los 7 riesgos, se buscó que no todos dieran el mismo nivel de gravedad, para que el análisis sea más realista (en la vida real no todos los riesgos son igual de graves).
- Se usó el método clásico de puntuación de SimpleRisk (Probabilidad x Impacto), que es el que trae el sistema por defecto.

## 3. Usuarios y roles

Se crearon los siguientes roles dentro de SimpleRisk:

**Analista de Riesgos:** puede presentar nuevos riesgos, modificarlos, planificar medidas de mitigación y evaluar el nivel de riesgo. No tiene permisos de administración del sistema.

**Auditor:** solo tiene acceso de lectura a los menús de Gobierno, Gestión de riesgos, Gestión de activos y Evaluaciones. No puede crear, modificar ni eliminar nada. Esto simula el rol de alguien que audita sin intervenir.

Se crearon 3 usuarios en total (Admin, Analista y Auditor), cada uno asociado a su rol correspondiente. El detalle completo está en `configuracion/usuarios.md`.

## 4. Escenario y riesgos identificados

El escenario es una clínica privada que recientemente tuvo una auditoría externa que encontró debilidades en su gestión de riesgos. A partir de eso, se identificaron 7 riesgos concretos:

### Riesgo 1: Acceso no autorizado a historias clínicas digitales
- **Categoría:** Confidencialidad
- **Activos afectados:** Historias clínicas digitales
- **Probabilidad:** 3 (Media) — porque existen controles de acceso, pero son parciales según la auditoría.
- **Impacto:** 5 (Muy alto) — porque son datos de salud, una categoría de información especialmente protegida por ley.
- **Nivel de riesgo:** 6/10 (Medio, según la fórmula clásica de SimpleRisk)
- **Controles existentes:** autenticación individual y roles diferenciados, pero sin registro de quién accede a cada historia clínica.
- **Tratamiento:** Mitigar. Se propone implementar logs de auditoría de acceso, revisión periódica de permisos y capacitación al personal.
- **Propietario:** Responsable de Seguridad de la Información.

### Riesgo 2: Filtración de datos por mal manejo de backups y USB
- **Categoría:** Confidencialidad
- **Activos afectados:** Historias clínicas digitales, Datos de obras sociales y facturación
- **Probabilidad:** 4 (Alta)
- **Impacto:** 5 (Muy alto)
- **Nivel de riesgo:** 8/10 (Alto) — **con plan de acción**
- **Controles existentes:** ninguno; no hay bloqueo de puertos USB ni cifrado de backups.
- **Tratamiento:** Mitigar. Bloqueo de puertos USB, cifrado obligatorio de backups y política formal de manejo de medios extraíbles.
- **Propietario:** Responsable de Seguridad de la Información.
- **Plan de acción:** implementar controles técnicos y política. Costo estimado: USD 100.001 a 200.000. Vencimiento: 60 días.

### Riesgo 3: Modificación accidental o maliciosa de historias clínicas
- **Categoría:** Integridad
- **Activos afectados:** Historias clínicas digitales
- **Probabilidad:** 3 (Media)
- **Impacto:** 5 (Muy alto) — puede afectar directamente la salud del paciente (ej. error de medicación).
- **Nivel de riesgo:** 6/10 (Medio)
- **Controles existentes:** ninguno; no hay control de versiones ni logs de cambios.
- **Tratamiento:** Mitigar. Registro de auditoría de modificaciones y doble verificación para cambios en datos críticos.
- **Propietario:** Responsable de Seguridad de la Información.

### Riesgo 4: Caída del sistema durante horario de atención
- **Categoría:** Disponibilidad
- **Activos afectados:** Servidor de historias clínicas, Infraestructura de red
- **Probabilidad:** 3 (Media)
- **Impacto:** 4 (Alto)
- **Nivel de riesgo:** 4.8/10 (Medio)
- **Controles existentes:** ninguno; no hay redundancia de servidores.
- **Tratamiento:** Mitigar. Servidor de respaldo con replicación automática y plan de continuidad con procedimiento manual de contingencia.
- **Propietario:** Responsable de Seguridad de la Información.

### Riesgo 5: Ransomware que cifra los servidores
- **Categoría:** Disponibilidad
- **Activos afectados:** Servidor de historias clínicas, Infraestructura de red
- **Probabilidad:** 2 (Baja) — no hay antecedentes de ataques previos en la clínica.
- **Impacto:** 5 (Muy alto) — el sector salud es un blanco frecuente de ransomware a nivel mundial.
- **Nivel de riesgo:** 4/10 (Medio-bajo)
- **Controles existentes:** ninguno; no hay backups offline ni segmentación de red.
- **Tratamiento:** Mitigar. Backups offline con verificación de restauración, segmentación de red y capacitación en phishing.
- **Propietario:** Responsable de Seguridad de la Información.

### Riesgo 6: Incumplimiento de la Ley 25.326 de Protección de Datos Personales
- **Categoría:** Legal
- **Activos afectados:** Historias clínicas digitales, Datos de obras sociales y facturación
- **Probabilidad:** 4 (Alta) — dado el antecedente de la auditoría externa negativa.
- **Impacto:** 5 (Muy alto) — puede implicar sanciones económicas y daño reputacional grave.
- **Nivel de riesgo:** 8/10 (Alto) — **con plan de acción**
- **Controles existentes:** ninguno; no hay políticas formales de tratamiento de datos personales.
- **Tratamiento:** Mitigar. Auditoría de cumplimiento normativo y designación de un responsable de protección de datos.
- **Propietario:** Responsable de Seguridad de la Información.
- **Plan de acción:** auditoría y documentación de políticas. Costo estimado: USD 0 a 100.000. Vencimiento: 60 días.

### Riesgo 7: Dependencia de un único administrador de sistemas
- **Categoría:** Operativo
- **Activos afectados:** Servidor de historias clínicas, Infraestructura de red
- **Probabilidad:** 5 (Muy alta) — depende de una sola persona, sin respaldo.
- **Impacto:** 4 (Alto) — genera parálisis operativa, aunque no compromete directamente los datos.
- **Nivel de riesgo:** 8/10 (Alto) — **con plan de acción**
- **Controles existentes:** ninguno; no hay documentación de procedimientos técnicos.
- **Tratamiento:** Mitigar. Documentación de procedimientos (runbooks), capacitación de un segundo perfil de respaldo, y evaluar soporte externo.
- **Propietario:** Responsable de Seguridad de la Información.
- **Plan de acción:** documentación y capacitación de respaldo. Costo estimado: USD 0 a 100.000. Vencimiento: 90 días.

La tabla resumen de estos 7 riesgos también está disponible en `configuracion/riesgos.md`.

## 5. Reporte ejecutivo

Se generó un reporte ejecutivo en PDF dirigido al Directorio de la clínica, disponible en `reporte-ejecutivo/`, con el resumen de los hallazgos principales, el top 5 de riesgos por nivel, el estado de los planes de acción y las recomendaciones prioritarias.

## 6. Comparación con otra metodología: FAIR

SimpleRisk usa una matriz clásica de Probabilidad x Impacto (escala 1 a 5), que es simple y rápida de usar, pero tiene una limitación que se notó en este mismo trabajo: el Riesgo 1 (acceso no autorizado a historias clínicas) dio un nivel "Medio" (6/10), a pesar de tratarse de datos de salud —una categoría especialmente protegida por ley— y de que la clínica ya tenía un antecedente de auditoría negativa. La matriz clásica no logra reflejar del todo esos matices porque solo usa dos números para calcular el resultado.

FAIR (Factor Analysis of Information Risk) es una metodología distinta, creada por Jack Jones en 2005 y reconocida como estándar internacional por The Open Group. En vez de usar etiquetas como "Alto" o "Medio", FAIR descompone el riesgo en factores más detallados (frecuencia de eventos y magnitud de la pérdida) y expresa el resultado en términos de dinero (por ejemplo, "pérdida esperada de USD 2 millones al año"). Esto permite justificar decisiones de inversión en seguridad con números concretos frente a una dirección o un directorio, en vez de una etiqueta relativa que puede interpretarse de formas distintas según quién la lea.

**Ventaja de SimpleRisk:** es rápido de implementar y fácil de usar, ideal para una primera evaluación de riesgos o para equipos sin especialistas en análisis cuantitativo.

**Ventaja de FAIR:** da resultados más precisos y defendibles ante una dirección, útil para justificar presupuestos de seguridad con cifras concretas.

**Cuándo conviene cada una:** para la clínica, SimpleRisk es adecuado como punto de partida (como se hizo en este TP). A medida que la organización mejore su gestión de riesgos, FAIR sería más apropiado para decisiones de inversión más grandes, como implementar infraestructura redundante (Riesgo 4) o contratar un seguro contra ciberataques.

## 7. Integración con herramienta externa

Se investigó cómo integrar SimpleRisk con Discord o Slack para notificar automáticamente cuando se registre un riesgo de nivel Alto, agilizando la respuesta del equipo de seguridad sin depender de que alguien revise el sistema manualmente.

La forma más simple de implementar esto es mediante un "Incoming Webhook": una URL especial que Discord o Slack generan, a la que se le puede enviar un mensaje mediante una solicitud HTTP desde cualquier sistema externo. SimpleRisk cuenta con una función llamada "API Extra" que permitiría automatizar esta conexión, pero se trata de un complemento pago que no está disponible en la versión gratuita instalada para este TP. Por eso, la integración automática completa no se pudo implementar, aunque el mecanismo (webhook) es simple y funcional si se contara con esa licencia.

El mensaje notificado incluiría: nombre del riesgo, nivel, propietario asignado y fecha de vencimiento del plan de mitigación.

## 8. Conclusiones

Este trabajo permitió aplicar en la práctica los conceptos de gestión de riesgos vistos en la materia, usando una herramienta real (SimpleRisk) sobre un escenario simulado pero realista. Se identificaron 7 riesgos con distinto nivel de gravedad, se definieron controles y planes de tratamiento para los 3 riesgos de nivel Alto, y se analizó críticamente tanto la herramienta usada como una alternativa (FAIR), entendiendo en qué casos conviene cada una.