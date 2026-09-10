# Parte C — Análisis crítico y profundización

## 1. Comparación metodológica

### 1.1 Metodología utilizada en el trabajo

Para el registro de riesgos de la clínica se utilizó SimpleRisk como herramienta de gestión, tomando como referencia una evaluación basada en una matriz de **probabilidad e impacto de 1 a 5**.

Para el análisis académico realizado en este trabajo, el nivel de riesgo se obtiene mediante:

**Riesgo = Probabilidad × Impacto**

La escala utilizada permite clasificar los resultados en cuatro niveles:

| Valor | Nivel   |
| ----: | ------- |
|   1–4 | Bajo    |
|   5–9 | Medio   |
| 10–15 | Alto    |
| 16–25 | Crítico |

Esta representación resulta especialmente útil para comunicar rápidamente la prioridad de un riesgo. Por ejemplo, los riesgos R-01 —ransomware— y R-02 —acceso no autorizado a historias clínicas— obtuvieron un valor de 20/25, por lo que fueron considerados críticos.

Debe distinguirse esta matriz utilizada para el análisis del comportamiento interno del método **Classic** de SimpleRisk. La documentación de SimpleRisk describe Classic como una metodología de scoring propia, cuyo cálculo considera la probabilidad y el impacto y puede normalizar el resultado para su presentación. Por este motivo, el valor visual mostrado por una instalación de SimpleRisk no necesariamente coincide literalmente con el producto `P × I` utilizado en la matriz académica.

### 1.2 Metodología alternativa: NIST SP 800-30 Rev. 1

Como metodología alternativa se seleccionó **NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments**.

NIST SP 800-30 propone un proceso estructurado para realizar evaluaciones de riesgo y contempla tres grandes etapas: preparar la evaluación, realizarla y mantenerla. La metodología busca proporcionar información que permita a los responsables tomar decisiones sobre cómo responder a los riesgos identificados.

Una diferencia importante es que NIST no se limita a asignar un valor numérico a un riesgo. La evaluación considera elementos como fuentes de amenaza, eventos de amenaza, vulnerabilidades o condiciones predisponentes, probabilidad, impacto y nivel de riesgo.

Esto permite construir una explicación más completa de **por qué un riesgo puede ocurrir y qué factores contribuyen a que sus consecuencias sean relevantes**.

### 1.3 Comparación

| Aspecto                  | SimpleRisk / enfoque de matriz                               | NIST SP 800-30 Rev. 1                                                 |
| ------------------------ | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| Objetivo principal       | Registrar, priorizar y gestionar riesgos.                    | Realizar una evaluación de riesgos estructurada.                      |
| Complejidad              | Baja a media.                                                | Media a alta.                                                         |
| Valoración               | Puede representarse mediante probabilidad e impacto.         | Analiza probabilidad, impacto y los elementos que los determinan.     |
| Amenazas                 | Pueden documentarse dentro del riesgo.                       | Forman parte explícita del proceso de evaluación.                     |
| Vulnerabilidades         | Pueden registrarse como parte del análisis.                  | Se analizan como condiciones que pueden facilitar eventos de amenaza. |
| Facilidad de seguimiento | Alta. Permite propietarios, estados y planes de tratamiento. | Requiere mayor trabajo documental para mantener la evaluación.        |
| Comunicación ejecutiva   | Muy buena mediante matrices y niveles.                       | Buena, pero requiere mayor elaboración para resumir el análisis.      |
| Recolección de evidencia | Puede comenzar con supuestos y evolucionar.                  | Favorece un análisis respaldado por evidencia y contexto.             |
| Mejor uso                | Registro operativo y seguimiento continuo.                   | Evaluaciones profundas y decisiones sobre sistemas críticos.          |

### 1.4 Ventajas del enfoque de SimpleRisk

Una de las principales ventajas de SimpleRisk es la **simplicidad operativa**.

En el caso de la clínica, fue posible registrar siete riesgos, asignar propietarios, establecer niveles de prioridad y asociar planes de tratamiento sin construir previamente un proceso de evaluación excesivamente complejo.

Esto resulta útil para una organización que necesita pasar rápidamente de una auditoría con hallazgos a un registro de riesgos accionable.

Por ejemplo, el riesgo:

> R-01 — Ransomware sobre sistemas de historias clínicas

puede ser registrado, evaluado, asignado a un responsable y vinculado con una estrategia de mitigación basada en backups resilientes, MFA, segmentación y recuperación.

Otra ventaja es la **centralización del ciclo de gestión**. El riesgo no queda solamente en una planilla: puede mantenerse como un registro vivo y asociarse a tratamientos y responsables.

### 1.5 Limitaciones del enfoque de matriz

La principal limitación de una matriz de probabilidad × impacto es que puede simplificar demasiado situaciones complejas.

Dos riesgos pueden obtener el mismo resultado aunque tengan causas, escenarios y consecuencias completamente diferentes. Por ejemplo, una indisponibilidad por una falla de infraestructura y una indisponibilidad provocada por ransomware podrían terminar con un valor similar, aunque las medidas de tratamiento necesarias sean muy diferentes.

También existe cierto grado de subjetividad.

Asignar un valor de probabilidad de 3 significa que el evaluador considera que el evento es posible, pero ese valor no constituye por sí mismo una medición estadística. Para reducir esta subjetividad es necesario establecer criterios comunes, justificar cada puntuación y revisar periódicamente los valores.

En este trabajo se intentó reducir ese problema justificando individualmente la probabilidad y el impacto de los siete riesgos.

### 1.6 Ventajas de NIST SP 800-30

La principal ventaja de NIST SP 800-30 es que permite profundizar en el **contexto que origina el riesgo**.

En el caso del ransomware, por ejemplo, no sería suficiente indicar que existe una probabilidad alta. Un análisis basado en NIST puede estudiar:

* fuentes de amenaza;
* vectores de ataque;
* vulnerabilidades existentes;
* condiciones que favorecen el incidente;
* activos afectados;
* controles existentes;
* consecuencias sobre la organización;
* incertidumbre de la estimación.

Esto produce una evaluación más defendible frente a una auditoría y resulta especialmente útil para sistemas críticos.

NIST también está pensado para integrarse con procesos más amplios de gestión de riesgos y proporcionar información para la toma de decisiones de los responsables de la organización.

### 1.7 Desventajas de NIST para este escenario

La principal desventaja es el esfuerzo necesario.

Para realizar una evaluación profunda sería necesario recopilar información adicional de la clínica, por ejemplo:

* inventario detallado de sistemas;
* arquitectura de red;
* registros de incidentes;
* resultados de escaneos de vulnerabilidades;
* información sobre proveedores;
* estadísticas de disponibilidad;
* configuración de backups;
* controles de acceso existentes;
* entrevistas con responsables de las áreas.

Para una primera evaluación de una clínica de 120 empleados, utilizar este nivel de profundidad para absolutamente todos los riesgos podría resultar costoso en tiempo y recursos.

### 1.8 ¿Cuándo conviene utilizar cada enfoque?

No se considera que una metodología deba reemplazar completamente a la otra.

**SimpleRisk con una matriz de riesgo** resulta más conveniente para:

* mantener el registro centralizado;
* priorizar riesgos;
* asignar propietarios;
* realizar seguimiento de tratamientos;
* presentar resultados a la dirección;
* revisar periódicamente el estado de los riesgos.

**NIST SP 800-30** resulta más conveniente cuando:

* se evalúa un sistema crítico;
* se introduce una tecnología nueva;
* se cambia un proveedor importante;
* se investiga un incidente grave;
* se requiere justificar técnicamente una decisión;
* se necesita una evaluación más profunda para una auditoría.

### 1.9 Propuesta para la clínica

Para la clínica se propone utilizar ambos enfoques de forma complementaria.

SimpleRisk actuaría como **repositorio central del registro y de los tratamientos**, mientras que NIST SP 800-30 se utilizaría para profundizar los riesgos de mayor criticidad.

Por ejemplo, R-01 —ransomware— podría mantenerse en SimpleRisk con su propietario, nivel, tratamiento y estado. Paralelamente, podría realizarse una evaluación NIST específica para determinar con mayor precisión los vectores de ataque, vulnerabilidades, controles existentes y escenarios de impacto.

De esta forma se obtiene un equilibrio entre **facilidad de gestión y profundidad del análisis**.

---

# 2. Integración con una herramienta externa

## 2.1 Herramienta seleccionada: Jira

Para la integración se seleccionó **Jira** como sistema externo de gestión de tareas.

La elección se debe a que los riesgos registrados en SimpleRisk pueden generar acciones de tratamiento que posteriormente deben ser ejecutadas por equipos técnicos.

El objetivo de la integración es evitar que una mitigación quede registrada únicamente como una intención dentro del sistema de riesgos.

Por ejemplo:

**R-01 — Ransomware**

↓

**PA-01 — Implementación de backups resilientes**

↓

**Tareas técnicas en Jira**

↓

**Evidencia de implementación**

↓

**Revisión del riesgo residual**

SimpleRisk dispone actualmente de una API REST v2 para integraciones programáticas y también contempla mecanismos específicos de integración dentro de su ecosistema. La API permite consultar y modificar información de riesgos mediante solicitudes HTTP autenticadas.

Jira, por su parte, dispone de una API REST que permite crear y modificar incidencias mediante solicitudes HTTP.

## 2.2 Arquitectura propuesta

Se propone implementar un pequeño servicio intermedio:

```text
                    ┌──────────────────┐
                    │    SimpleRisk    │
                    │ Registro de      │
                    │ riesgos          │
                    └────────┬─────────┘
                             │
                       REST API / HTTPS
                             │
                             ▼
                    ┌──────────────────┐
                    │ Integrador       │
                    │ / Script         │
                    └────────┬─────────┘
                             │
                       REST API / HTTPS
                             │
                             ▼
                    ┌──────────────────┐
                    │      Jira        │
                    │ Tareas técnicas  │
                    └──────────────────┘
```

El componente intermedio tendría la responsabilidad de consultar los riesgos de SimpleRisk y generar o actualizar las tareas correspondientes en Jira.

## 2.3 Flujo de funcionamiento

El flujo propuesto sería:

1. El analista registra y evalúa un riesgo en SimpleRisk.
2. El riesgo recibe un nivel de prioridad y un propietario.
3. Cuando el riesgo requiere tratamiento, se crea un plan de acción.
4. El integrador identifica el plan que debe ejecutarse.
5. Se crea una tarea en Jira para el equipo responsable.
6. Jira mantiene el seguimiento de la tarea, responsable, vencimiento y evidencias.
7. Cuando la tarea finaliza, el resultado queda disponible para la revisión del responsable del riesgo.
8. El responsable actualiza el estado del tratamiento y vuelve a evaluar el riesgo.
9. Se calcula o determina el riesgo residual.
10. La aceptación del riesgo residual permanece como una decisión del responsable y no como una acción automática.

Este último punto es importante: **automatizar la creación o actualización de tareas no debería implicar automatizar la aceptación del riesgo**.

---

## 2.4 Datos que se transferirían

La integración no debería copiar toda la información disponible en SimpleRisk.

Se propone transferir únicamente los datos necesarios para ejecutar el tratamiento:

| SimpleRisk             | Jira                             |
| ---------------------- | -------------------------------- |
| ID del riesgo          | Campo de referencia              |
| Nombre del riesgo      | Summary                          |
| Descripción resumida   | Description                      |
| Nivel                  | Priority / etiqueta              |
| Propietario            | Assignee                         |
| Plan de tratamiento    | Task / Issue                     |
| Fecha de vencimiento   | Due date                         |
| Estado del tratamiento | Status                           |
| Identificador de Jira  | Referencia cruzada en SimpleRisk |

Por ejemplo, para PA-01 podría generarse una tarea similar a:

```text
SEG-101 — Implementar backups resilientes contra ransomware

Riesgo: R-01
Prioridad: Crítico
Responsable: Infraestructura
Vencimiento: 30/11/2026

Objetivo:
Implementar una copia de seguridad offline o inmutable,
separada de la infraestructura productiva, y realizar
una prueba documentada de restauración.
```

El uso de un identificador común permite mantener la trazabilidad entre el riesgo y la tarea técnica.

---

## 2.5 Seguridad de la integración

La integración debe diseñarse considerando que el registro de riesgos puede contener información sensible sobre la seguridad de la organización.

Se proponen las siguientes medidas:

### Cuenta técnica independiente

La integración debe utilizar una cuenta técnica exclusiva y no una cuenta personal del administrador.

Esto permite revocar el acceso o rotar las credenciales sin afectar las cuentas de los usuarios.

### Mínimo privilegio

La cuenta utilizada por el integrador debería tener únicamente los permisos necesarios para consultar riesgos y crear o actualizar las tareas correspondientes.

### Protección de API keys

SimpleRisk permite utilizar autenticación mediante API key para automatizaciones. Las claves no deben almacenarse dentro del código fuente ni incluirse en el repositorio Git.

Se propone almacenarlas mediante:

* variables de entorno;
* secretos de Docker;
* un gestor de secretos;
* o un mecanismo equivalente.

### Comunicación cifrada

Las comunicaciones entre SimpleRisk, el integrador y Jira deben realizarse mediante HTTPS.

### Minimización de información

No se deberían enviar a Jira:

* historias clínicas;
* nombres de pacientes;
* números de documento;
* diagnósticos;
* credenciales;
* API keys;
* información clínica.

Jira debería recibir únicamente la información necesaria para ejecutar y controlar la mitigación.

### Registro de errores

El integrador debería registrar errores de comunicación y eventos de sincronización, pero evitando almacenar innecesariamente el contenido completo de las solicitudes y respuestas.

Esto es especialmente importante porque las descripciones de los riesgos podrían contener información sensible. La propia documentación de integración de SimpleRisk recomienda evitar registrar cuerpos completos de solicitudes y respuestas cuando puedan contener información sensible.

---

## 2.6 Ejemplo conceptual de automatización

Una implementación mínima podría ejecutarse periódicamente:

```text
Cada 15 minutos
       │
       ▼
Consultar SimpleRisk
       │
       ▼
¿Existen riesgos con tratamiento pendiente?
       │
       ├── No ──► Finalizar
       │
       └── Sí
             │
             ▼
       Verificar si ya existe
       una tarea asociada
             │
             ├── Sí ──► Actualizar
             │
             └── No ──► Crear tarea Jira
```

El proceso podría implementarse mediante un pequeño script en Python, un contenedor Docker o una herramienta de automatización.

SimpleRisk expone una API REST como superficie de integración y Jira proporciona endpoints REST para crear incidencias, por lo que no sería necesario acceder directamente a las bases de datos de ninguna de las dos aplicaciones.

---

## 2.7 Integración mediante webhook

Como alternativa, se podría utilizar un mecanismo basado en eventos.

El flujo sería:

```text
SimpleRisk
    │
    │ evento de riesgo / tratamiento
    ▼
Webhook
    │
    ▼
Servicio integrador
    │
    ▼
Jira
```

El servicio recibiría el evento, validaría su autenticidad, comprobaría el identificador del riesgo y posteriormente crearía o actualizaría la tarea correspondiente.

Jira también dispone de mecanismos de webhook para recibir notificaciones cuando se producen determinados eventos sobre incidencias.

Para el trabajo práctico, sin embargo, se considera más sencilla la primera alternativa basada en API y ejecución periódica.

---

## 2.8 Aplicación al escenario de la clínica

La integración tendría especial utilidad para los tres planes de acción definidos:

| Plan  | Riesgo                      | Posible tarea Jira                                          |
| ----- | --------------------------- | ----------------------------------------------------------- |
| PA-01 | R-01 — Ransomware           | Implementar backup offline/inmutable y probar restauración. |
| PA-02 | R-02 — Acceso no autorizado | Implementar MFA en sistemas críticos.                       |
| PA-03 | R-04 — Phishing             | Ejecutar capacitación y campaña de simulación.              |

De esta manera, la información quedaría distribuida según su propósito:

* **SimpleRisk:** gestión y evaluación del riesgo.
* **Jira:** ejecución y seguimiento de las tareas.
* **Equipo responsable:** implementación de controles.
* **Responsable del riesgo:** evaluación del resultado y riesgo residual.

---

## 2.9 Estado de implementación en este trabajo

La integración con Jira **no fue implementada en el entorno práctico**, ya que el laboratorio utilizado para el trabajo está compuesto por SimpleRisk y MySQL y no cuenta con una instancia de Jira conectada.

Se documentó la arquitectura propuesta y el flujo de integración como diseño técnico para una implementación futura.

La alternativa sería completamente viable mediante la API REST de SimpleRisk y la API REST de Jira.

Una implementación futura podría agregarse como un tercer servicio Docker dentro del entorno:

```text
simple-risk
mysql
risk-integrator
```

El contenedor `risk-integrator` tendría acceso a SimpleRisk mediante HTTPS y utilizaría las credenciales almacenadas como secretos para comunicarse con Jira.

---

# 3. Conclusión

La comparación realizada muestra que una matriz de probabilidad × impacto es una herramienta eficiente para comenzar a ordenar y priorizar los riesgos, pero no debería considerarse suficiente para analizar en profundidad todos los escenarios de una organización.

En el caso de la clínica, SimpleRisk resulta adecuado como plataforma central de registro y seguimiento, mientras que NIST SP 800-30 puede aportar mayor profundidad para los riesgos críticos y para situaciones que requieran una justificación técnica más detallada.

La integración con Jira permitiría completar el ciclo de gestión: SimpleRisk identifica y prioriza el riesgo, mientras que Jira facilita la ejecución y seguimiento de las acciones necesarias para reducirlo.

La combinación propuesta permite pasar de un modelo basado solamente en registrar riesgos a un proceso continuo:

**Identificar → Evaluar → Priorizar → Tratar → Ejecutar → Verificar → Reevaluar**

Esto resulta especialmente importante para la clínica, donde la seguridad de la información está directamente relacionada con la continuidad de la atención médica y la protección de datos sensibles.

## Referencias

* National Institute of Standards and Technology. **NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments.** [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final?utm_source=chatgpt.com)
* SimpleRisk. **The Risk Formula.** [SimpleRisk — The Risk Formula](https://support.simplerisk.com/kb/06-02-the-risk-formula?utm_source=chatgpt.com)
* SimpleRisk. **Using the API for Integrations.** [SimpleRisk — API for Integrations](https://support.simplerisk.com/kb/07-04-using-the-api-for-integrations?utm_source=chatgpt.com)
* SimpleRisk. **API Extra.** [SimpleRisk — API Extra](https://www.simplerisk.com/extras/api?utm_source=chatgpt.com)
* Atlassian. **Jira REST API — Issues.** [Jira REST API — Create Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/?utm_source=chatgpt.com)
* Atlassian. **Jira REST API — Webhooks.** [Jira Webhooks API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-webhooks/?utm_source=chatgpt.com)
