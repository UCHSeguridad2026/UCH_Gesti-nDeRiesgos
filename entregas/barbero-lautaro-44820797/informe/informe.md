# Informe — Trabajo Práctico: Gestión de Riesgos con SimpleRisk

**Alumno:** Barbero, Lautaro — LU 44820797
**Materia:** Seguridad de Sistemas

---

## Índice

1. [Parte A — Instalación y configuración básica](#1-parte-a--instalación-y-configuración-básica)
2. [Parte B — Escenario real](#2-parte-b--escenario-real)
3. [Parte C — Análisis crítico y profundización](#3-parte-c--análisis-crítico-y-profundización)
4. [Parte D — Actividad optativa](#4-parte-d--actividad-optativa)
5. [Observaciones sobre la herramienta](#5-observaciones-sobre-la-herramienta)
6. [Conclusiones](#6-conclusiones)

---

## 1. Parte A — Instalación y configuración básica

### 1.1. Instalación reproducible

Se desplegó SimpleRisk mediante **Docker Compose** sobre CachyOS. La instalación inicial se realizó a partir de la imagen `simplerisk/simplerisk` publicada en DockerHub, y posteriormente se migró a una definición declarativa en `entorno/docker-compose.yml`.

**Motivo de la migración.** El comando de despliegue propuesto en la consigna original —`docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk`— crea un contenedor sin volúmenes persistentes. La base de datos reside en la capa escribible del contenedor, de modo que su eliminación destruye toda la información cargada. Para un trabajo cuyo contenido principal se carga en la herramienta, esta configuración representa un riesgo operativo inaceptable.

**Volúmenes definidos.** La inspección del `Dockerfile` oficial del proyecto reveló que la imagen declara seis volúmenes, no únicamente el de la base de datos:

| Ruta interna | Contenido |
|---|---|
| `/var/lib/mysql` | Base de datos MariaDB |
| `/passwords` | Contraseñas generadas en el arranque |
| `/configurations` | Configuración de la aplicación |
| `/var/www/simplerisk` | Código y archivos subidos |
| `/etc/apache2/ssl` | Certificados SSL autofirmados |
| `/var/log` | Registros del sistema |

El directorio `/passwords` merece atención particular: el script de arranque genera allí contraseñas aleatorias para MySQL y para el usuario `simplerisk` de la base. Persistir la base sin persistir ese directorio provoca que, al recrear el contenedor, se generen credenciales nuevas que no coinciden con las de la base existente, dejando la aplicación sin conexión a sus datos.

**Verificación de la persistencia.** Se comprobó destruyendo y recreando el contenedor. La presencia de dos archivos `.pid` con identificadores distintos dentro de `/var/lib/mysql` confirma que dos contenedores diferentes escribieron sobre el mismo volumen, es decir, que este sobrevivió a la eliminación del primero.

**Reproducción del entorno.** Las instrucciones detalladas figuran en el `README.md` de la entrega.

### 1.2. Usuarios y permisos

Se crearon tres usuarios con roles diferenciados, documentados en `configuracion/usuarios.md`. Los cargos coinciden deliberadamente con los propietarios de riesgo definidos en el análisis, de modo que la configuración de la herramienta refleje la estructura de responsabilidades del escenario.

| Usuario | Cargo | Rol |
|---|---|---|
| `admin_demo` | Jefe de Sistemas | Administrator |
| `analista_demo` | Responsable de Seguridad de la Información | Analista de Riesgos |
| `auditor_demo` | Responsable de Cumplimiento y Protección de Datos | Auditor |

SimpleRisk incorpora únicamente el rol Administrator en su instalación por defecto. Los roles **Analista de Riesgos** y **Auditor** fueron creados para este trabajo, definiendo sus permisos uno a uno sobre el catálogo de 46 responsabilidades que ofrece la herramienta.

El criterio rector fue la **segregación de funciones**: quien administra la infraestructura no es quien audita los accesos. El rol Auditor se configuró como solo lectura y comentario, dado que un auditor con capacidad de modificar aquello que audita pierde independencia.

La configuración se verificó de dos maneras: mediante el reporte comparativo de permisos por usuario, y mediante el inicio de sesión efectivo con el rol Auditor, donde se constató la ausencia del menú de configuración y la reducción de las acciones disponibles.

### 1.3. Riesgo de prueba

Se creó el riesgo `PRUEBA - Validación de funcionamiento del sistema` con probabilidad 3 e impacto 3. El sistema calculó un valor de 9 y lo clasificó como nivel Medio, resultado coincidente con la matriz configurada. La prueba validó el alta de riesgos, el motor de cálculo y la clasificación por nivel antes de cargar el registro real.

### 1.4. Configuración del motor de scoring

La instalación por defecto de SimpleRisk aplica una **normalización de la puntuación a una escala 0-10**, dividiendo el producto de probabilidad por impacto entre 2,5. Los umbrales de nivel venían fijados en 10,1 / 7,0 / 4,0 / 0,0 sobre esa escala comprimida.

Dado que el análisis se desarrolló sobre la escala 1-25 de la plantilla de matriz de riesgos de la cátedra, mantener la configuración por defecto habría producido una discrepancia entre los valores del documento y los mostrados por la herramienta. Se realizaron dos ajustes:

- Se desactivó la normalización, restituyendo el rango 1-25
- Se redefinieron los umbrales de nivel en 16 / 10 / 5 / 1

La fórmula subyacente (`Likelihood × Impact`, con escalas de 1 a 5 en ambos ejes) ya coincidía con la metodología adoptada.

**Equivalencia de nomenclatura.** SimpleRisk emplea denominaciones propias que no coinciden literalmente con las de la plantilla, aunque las bandas son idénticas:

| Plantilla | SimpleRisk | Rango |
|---|---|---|
| Crítico | Very High | 16 – 25 |
| Alto | High | 10 – 15 |
| Medio | Medium | 5 – 9 |
| Bajo | Low | 1 – 4 |

Asimismo, la herramienta denomina *Likelihood* a lo que la plantilla llama *Probabilidad*, con etiquetas Remote / Unlikely / Credible / Likely / Almost Certain frente a Raro / Improbable / Posible / Probable / Casi seguro. Los valores numéricos son equivalentes.

**Apetito de riesgo.** Se fijó en nivel Medium. La configuración por defecto lo establecía en Insignificant (0), lo que equivale a declarar que la organización no tolera riesgo alguno: una postura carente de utilidad práctica, dado que implicaría tratamiento inmediato incluso para riesgos de valor 1. El valor adoptado es coherente con los criterios de acción de la escala, donde el nivel Bajo admite aceptación y el Medio un plan a mediano plazo.

---

## 2. Parte B — Escenario real

El desarrollo completo del análisis figura en `configuracion/riesgos.md`, elaborado según la estructura de la plantilla de matriz de riesgos de la cátedra. Esta sección resume las decisiones metodológicas.

### 2.1. Alcance y supuestos

El enunciado describe una clínica privada de 120 empleados que atiende 800 pacientes diarios y que acaba de atravesar una auditoría externa con hallazgos, pero no detalla su infraestructura. Los supuestos técnicos fueron definidos como parte del análisis y documentados explícitamente.

La definición de esos supuestos se orientó deliberadamente a construir un escenario **con debilidades reales**. Un escenario sin vulnerabilidades no produce riesgos que analizar, y el propio enunciado establece que la clínica presenta problemas de gestión detectados por una auditoría.

### 2.2. Estructura del análisis

El análisis siguió la secuencia activos → amenazas → riesgos → tratamiento → riesgo residual:

| Etapa | Resultado |
|---|---|
| Inventario de activos | 11 activos (A01–A11), 8 de criticidad Alta y 3 Media |
| Identificación de amenazas | 17 amenazas (T01–T17): 9 accidentales, 6 intencionales, 2 naturales |
| Evaluación de riesgos | 8 riesgos (R01–R08) |
| Tratamiento | 8 estrategias de mitigación con salvaguardas técnicas, físicas y administrativas |
| Planes de acción | 3 planes (PA-01 a PA-03) sobre los riesgos de mayor valor |

### 2.3. Criterio de agrupación

Las diecisiete amenazas se consolidaron en ocho riesgos aplicando el criterio de **comunidad de tratamiento**: amenazas que se mitigan con las mismas salvaguardas se agrupan en un mismo riesgo. La alternativa —agrupar por tema o por activo afectado— habría producido riesgos cuyo plan de acción debería atacar problemas heterogéneos, dificultando su ejecución y seguimiento.

Este criterio motivó separar amenazas temáticamente cercanas. Por ejemplo, la saturación del servidor por volumen de datos y la falta de normalización de la base son ambos problemas de la infraestructura de datos, pero se tratan de forma distinta: uno con capacidad de cómputo y el otro con rediseño del esquema. Se asignaron, en consecuencia, a riesgos diferentes.

### 2.4. Decisiones metodológicas explicitadas

Tres decisiones se dejaron documentadas en el propio registro para evidenciar que las valoraciones responden a un análisis y no a una asignación uniforme.

**Distinción entre exposición y aprovechamiento.** En R02 y R08, la exposición es prácticamente permanente —el wifi abierto está disponible todo el día, los equipos sin restricciones se usan durante turnos completos— pero su materialización en un incidente requiere intención y capacidad técnica. Se valoró el aprovechamiento efectivo, no la exposición, y así se hizo constar.

**Valoración por causa dominante.** R05 agrupa tres causas independientes con frecuencias muy dispares: saturación por capacidad, corte de energía e incendio o inundación. Se optó por valorar la probabilidad según la causa dominante en lugar de promediar o tomar el máximo, dejando constancia del criterio.

**Encadenamiento de riesgos.** El análisis identificó que los riesgos no son independientes entre sí. R03 habilita R04, al impedir la detección del acceso indebido. R06 multiplica el impacto de R05 y R08, al convertir incidentes recuperables en pérdidas definitivas. R02 constituye precondición de R07. Estas relaciones se documentaron en las fichas correspondientes porque determinan el orden de prioridad del plan de tratamiento: tratar R03 y R06 mejora simultáneamente varios frentes.

### 2.5. Resultado

| Nivel | Riesgo inherente | Riesgo residual |
|---|---|---|
| Crítico | 4 | 0 |
| Alto | 3 | 3 |
| Medio | 1 | 4 |
| Bajo | 0 | 1 |

El plan de tratamiento elimina la totalidad de los riesgos de nivel Crítico sin que ninguno supere el nivel Alto en su valoración residual. Los tres que permanecen en Alto conservan un componente irreductible: la conducta del personal con acceso legítimo en R03 y R04, y la consecuencia inherente a la pérdida de información no reconstruible en R06.

---

## 3. Parte C — Análisis crítico y profundización

### 3.1. Comparación metodológica: matriz cualitativa frente a FAIR

#### El enfoque de SimpleRisk

SimpleRisk implementa por defecto una **matriz cualitativa de probabilidad × impacto**, donde ambos factores se valoran en una escala ordinal de cinco posiciones y su producto determina el nivel de riesgo. Es la metodología empleada en este trabajo, alineada con la plantilla de la cátedra y con el enfoque general de ISO 27005 y NIST SP 800-30.

#### El enfoque de FAIR

**Factor Analysis of Information Risk** es un modelo cuantitativo que expresa el riesgo como **pérdida monetaria esperada en un período**, típicamente anual. En lugar de asignar un número ordinal, descompone el riesgo en dos factores que se multiplican:

- **Frecuencia de eventos de pérdida (LEF):** cuántas veces por año se espera que el evento se materialice, estimada a partir de la frecuencia de intentos y la proporción de estos que superan las defensas existentes
- **Magnitud de la pérdida (LM):** cuánto cuesta cada ocurrencia, sumando pérdidas primarias (respuesta al incidente, reemplazo, productividad perdida) y secundarias (multas regulatorias, litigios, daño reputacional)

Cada factor se estima como un **rango** con valores mínimo, máximo y más probable, en lugar de un valor puntual. Una simulación de Monte Carlo combina esas distribuciones y produce como resultado una curva de exposición: no un número único, sino un rango de pérdida anual con su probabilidad asociada.

Aplicado a un riesgo de este trabajo, FAIR no diría *"R04 vale 20 y es Crítico"*, sino algo como *"la exposición anual asociada al acceso indebido a datos de pacientes se sitúa entre X e Y, con valor más probable Z"*.

#### Ventajas del enfoque de SimpleRisk

**Costo de aplicación bajo.** Los ocho riesgos de este trabajo se valoraron sin necesidad de datos históricos de incidentes, estadísticas sectoriales de frecuencia ni estimaciones de costo por evento. Para una organización que no dispone de ninguno de esos insumos —como la clínica del escenario, que carece incluso de registros de auditoría de accesos— es la única metodología aplicable de forma inmediata.

**Cobertura amplia en poco tiempo.** Permite construir un registro inicial completo, que es exactamente lo que el escenario requiere tras una auditoría con hallazgos. El objetivo en esa etapa es no dejar riesgos sin identificar, no cuantificar con precisión los ya conocidos.

**Comunicabilidad.** Un semáforo de cuatro niveles es interpretable sin formación previa. La dirección de una clínica entiende "cuatro riesgos críticos" sin necesidad de explicar qué es una distribución de probabilidad.

**Trazabilidad del razonamiento.** Al obligar a justificar cada valor en prosa, el análisis deja explícito el fundamento de cada decisión, que puede discutirse y corregirse.

#### Limitaciones del enfoque de SimpleRisk

Las siguientes limitaciones no son teóricas: se manifestaron durante la elaboración de este trabajo.

**Los valores son ordinales, no aritméticos.** Un riesgo de valor 20 no es "dos veces peor" que uno de valor 10, ni la suma de dos riesgos de valor 8 equivale a uno de 16. La escala solo permite ordenar, no operar. Esto impide agregar el riesgo total de la organización en una cifra única, que es precisamente lo que la dirección necesita para decidir cuánto invertir en seguridad.

**Los empates carecen de criterio de desempate.** En este trabajo, **R04 y R06 obtuvieron ambos valor 20**. La matriz los declara equivalentes y no ofrece ningún elemento para priorizar entre ellos. La decisión de atender primero R06 debió tomarse con argumentos externos a la metodología: menor costo de implementación y efecto de reducción sobre otros riesgos del registro. FAIR habría resuelto el empate de forma directa, indicando cuál de los dos representa mayor pérdida anual esperada.

**La escala fuerza a colapsar rangos amplios en un punto.** La valoración del impacto de R01 ilustra el problema: un error de carga puede ser trivial —un domicilio mal escrito— o grave —una alergia mal registrada—. La metodología obliga a elegir un valor único para un fenómeno cuyo rango real de consecuencias abarca varios órdenes de magnitud. FAIR modela ese rango explícitamente mediante distribuciones, en lugar de exigir que se lo reduzca a un número.

**No permite análisis de costo-beneficio.** El plan de tratamiento propuesto asciende a USD 23.300. La matriz no ofrece ningún elemento para determinar si esa inversión es proporcionada, insuficiente o excesiva: indica que los riesgos bajan de Crítico a Alto, pero no cuánta pérdida esperada se evita. FAIR permite comparar el costo de la salvaguarda contra la reducción de exposición que produce, y decidir sobre esa base.

**La subjetividad no queda acotada.** Dos analistas pueden asignar valores distintos al mismo riesgo sin que la metodología ofrezca un procedimiento para resolver la diferencia. Durante este trabajo, varias valoraciones fueron revisadas tras discutir el fundamento, lo que es saludable, pero evidencia que el resultado depende del criterio de quien lo elabora.

#### Limitaciones de FAIR

**Requiere datos que la mayoría de las organizaciones no tiene.** Estimar la frecuencia de eventos de pérdida exige registros históricos de incidentes o estadísticas sectoriales confiables. La clínica del escenario no tiene registro de auditoría de accesos: literalmente no puede saber cuántas consultas indebidas a historias clínicas ocurrieron el año pasado. Aplicar FAIR en ese contexto produciría cifras con apariencia de precisión pero fundamento inventado, lo que es peor que una escala ordinal honesta.

**Costo y tiempo.** Cada riesgo requiere descomposición en múltiples factores, estimación calibrada de rangos y simulación. Analizar ocho riesgos con FAIR demanda un esfuerzo considerablemente mayor que con una matriz.

**Requiere formación específica.** El modelo exige comprensión de estimación calibrada y de simulación estocástica, competencias que no son habituales fuera de equipos de riesgo maduros.

**Riesgo de falsa precisión.** Un resultado expresado en dólares transmite una autoridad que las estimaciones subyacentes pueden no respaldar. Un valor "20 sobre 25" comunica su propia imprecisión; "USD 187.400 anuales" no.

#### En qué contexto conviene cada una

| Situación | Metodología adecuada |
|---|---|
| Registro inicial de riesgos, sin análisis previo | Matriz cualitativa |
| Organización sin datos históricos de incidentes | Matriz cualitativa |
| Necesidad de cobertura amplia en poco tiempo | Matriz cualitativa |
| Comunicación a dirección no técnica | Matriz cualitativa |
| Justificar presupuesto de seguridad ante la dirección | FAIR |
| Priorizar entre riesgos de magnitud similar | FAIR |
| Evaluar si una salvaguarda concreta se paga a sí misma | FAIR |
| Comparar riesgo de seguridad con otros riesgos del negocio | FAIR |

**Aplicación al escenario.** Para la clínica en su estado actual, la matriz cualitativa es la elección correcta. La organización viene de una auditoría con hallazgos, no dispone de registro de incidentes ni de trazabilidad de accesos, y lo que necesita es un inventario de riesgos que le permita empezar a actuar. Intentar FAIR en esta etapa sería un ejercicio de precisión ficticia.

FAIR sería apropiado en una segunda instancia, una vez implementados los planes PA-01 a PA-03. En particular, tras la implementación de PA-03 —que instaura el registro de auditoría de accesos— la clínica dispondría por primera vez de datos reales sobre frecuencia de consultas indebidas, insumo indispensable para una estimación cuantitativa fundada. Ese es también el momento en que la dirección probablemente pregunte si el gasto en seguridad se justifica, pregunta que la matriz no puede responder.

#### Nota sobre las metodologías no elegidas

**NIST SP 800-30** e **ISO 27005** comparten con SimpleRisk el enfoque cualitativo, por lo que la comparación resultaría menos ilustrativa. Aportan, sí, un proceso más estructurado: NIST SP 800-30 formaliza la distinción entre fuentes de amenaza, eventos, vulnerabilidades y condiciones predisponentes, con mayor rigor que la separación amenaza/vulnerabilidad empleada aquí.

**OCTAVE** se distingue por ser un método autodirigido, ejecutado por el propio personal de la organización en lugar de por consultores externos, y por partir de los activos críticos identificados por las áreas de negocio. Habría sido apropiado para el momento de definición de los supuestos del escenario, donde precisamente se requiere conocimiento operativo interno.

**Observación sobre la herramienta.** SimpleRisk no está limitado al enfoque cualitativo: el formulario de alta de activos incluye un campo obligatorio de **Asset Valuation** expresado en rangos monetarios, y el selector de método de scoring ofrece alternativas a la fórmula Classic. La herramienta contempla ambos paradigmas; la elección del enfoque cualitativo en este trabajo responde a la metodología adoptada, no a una restricción del software.

### 3.2. Integración con una herramienta externa

Se implementó una integración funcional entre SimpleRisk y **Discord**, mediante un script que notifica automáticamente los riesgos que superan el umbral de nivel Alto.

#### Arquitectura

```
SimpleRisk (contenedor Docker)
        │
        │  consulta SQL sobre MariaDB
        ▼
notificar_riesgos.py  (host)
        │
        │  HTTP POST (JSON)
        ▼
Webhook de Discord → canal de alertas
```

El script `scripts/notificar_riesgos.py` consulta la base de datos de SimpleRisk, filtra los riesgos abiertos con valor calculado igual o superior al umbral configurado, y publica un mensaje estructurado en un canal de Discord mediante webhook. Cada riesgo se presenta con su nivel, valor, probabilidad e impacto, con código de color correspondiente a su banda.

#### Decisión sobre el método de acceso a los datos

SimpleRisk expone una API REST bajo `/api/v2/`, disponible sin configuración adicional. Sin embargo, la generación y rotación de claves de API —necesarias para autenticar peticiones automatizadas— forma parte del complemento comercial **SimpleRisk API Extra**, no incluido en la versión Community empleada en este trabajo. La API acepta autenticación por cookie de sesión, mecanismo pensado para pruebas manuales desde un navegador y no apto para un proceso desatendido.

Se optó, en consecuencia, por consultar directamente la base de datos. La decisión es una limitación de la versión disponible y no una preferencia arquitectónica: en un despliegue con el complemento habilitado, la integración por API sería preferible, ya que respeta la capa de abstracción de la aplicación y no depende del esquema interno de la base.

#### Decisiones de seguridad de la integración

**La URL del webhook no se versiona.** Se lee de la variable de entorno `DISCORD_WEBHOOK_URL`. Una URL de webhook es una credencial: cualquiera que la posea puede publicar en el canal. Incluirla en el código la expondría en el repositorio, que es público.

**La contraseña de la base de datos nunca sale del contenedor.** La consulta se ejecuta mediante `docker exec`, leyendo la contraseña desde `/passwords/pass_mysql_root.txt` dentro del propio contenedor. El valor no se transmite al sistema anfitrión, no se pasa como argumento —lo que lo expondría en la lista de procesos— ni queda registrado en el historial de comandos.

**El script incluye un modo `--dry-run`** que lista los riesgos por consola sin realizar ninguna petición externa, permitiendo verificar la consulta sin generar notificaciones.

#### Incidencias durante la implementación

Dos problemas surgidos durante la puesta en marcha resultan ilustrativos.

**Codificación de caracteres.** La conexión de MySQL devolvía la salida en Latin-1, mientras Python la interpretaba como UTF-8, provocando el fallo de decodificación en los nombres de riesgo con acentos. Se resolvió forzando `utf8mb4` en la conexión e implementando un respaldo de decodificación en el script.

**Bloqueo por User-Agent.** Las peticiones al webhook eran rechazadas con HTTP 403. La causa es que Discord opera detrás de Cloudflare, cuyo filtrado anti-bots rechaza el User-Agent por defecto de la biblioteca `urllib`. Se resolvió identificando explícitamente la integración mediante una cabecera `User-Agent` propia, conforme a la práctica que la propia documentación de Discord recomienda.

#### Resultado y limitaciones

La ejecución notifica correctamente los siete riesgos con valor igual o superior a 10, respondiendo Discord con HTTP 204.

La integración opera por **consulta periódica** y no por eventos: no detecta el alta de un riesgo en el momento en que ocurre, sino que informa el estado del registro cuando se la ejecuta. Para operación continua correspondería programarla mediante `cron` o un temporizador de `systemd`, con una frecuencia acorde a la criticidad del entorno. Una integración basada en eventos requeriría que SimpleRisk emitiera notificaciones salientes, capacidad que la versión Community no ofrece de forma nativa.

#### Otras integraciones posibles

La misma arquitectura admite destinos alternativos con modificaciones menores en la función de envío:

- **Sistema de tickets (Jira, Redmine):** crear automáticamente una incidencia por cada riesgo de nivel Crítico, asignada a su propietario, vinculando el seguimiento del tratamiento al flujo de trabajo habitual del equipo
- **SIEM:** enviar los riesgos como eventos correlacionables con la actividad detectada en la infraestructura, permitiendo priorizar alertas según los activos involucrados
- **Correo electrónico:** SimpleRisk incorpora configuración SMTP nativa en `Configure → Mail`, alternativa que no requiere desarrollo pero ofrece menor capacidad de formato y filtrado

---

## 4. Parte D — Actividad optativa

### D2 — Implementación de una integración real

La actividad optativa seleccionada corresponde a **D2: implementación de una integración real mediante webhook que notifique riesgos de nivel alto**.

La implementación, sus decisiones de diseño y sus limitaciones se documentan en la sección 3.2 de este informe. El código fuente se encuentra en `scripts/notificar_riesgos.py`.

**Alcance de lo implementado:**

- Consulta funcional sobre el registro de riesgos de SimpleRisk
- Filtrado configurable por umbral de valor, con nivel Alto (≥ 10) por defecto
- Notificación estructurada con formato y código de color por nivel de riesgo
- Modo de verificación sin envío (`--dry-run`)
- Gestión de credenciales por variable de entorno, sin exposición en el repositorio
- Manejo de errores diferenciado para fallos de consulta, ausencia de configuración y rechazo del destino

---

## 5. Observaciones sobre la herramienta

Durante la configuración se identificaron funcionalidades de SimpleRisk que implementan controles equivalentes a los propuestos en el plan de tratamiento de la clínica. La coincidencia es relevante: la herramienta con la que se documenta el análisis aplica sobre sí misma varias de las salvaguardas recomendadas.

**Autenticación multifactor.** El formulario de alta de usuarios ofrece la opción de MFA, correspondiente a la salvaguarda propuesta en R07 y en el plan PA-02. Se mantiene desactivada en este entorno para permitir la reproducción del trabajo sin requerir la configuración de un dispositivo autenticador.

**Granularidad de permisos.** El catálogo de 46 responsabilidades individuales permite implementar el principio de mínimo privilegio con precisión, que es el control central de PA-03. La herramienta no obliga a elegir entre perfiles predefinidos.

**Registro de auditoría.** El módulo `Configure → Audit Trail` registra y permite exportar las acciones de los usuarios, implementación directa del registro de auditoría de accesos que PA-03 propone para el sistema de gestión clínica.

**Deshabilitación frente a eliminación.** La función *Enable and Disable Users* permite desactivar el acceso de un usuario conservando el rastro de auditoría de su actividad previa. Esta distinción refina la recomendación formulada en PA-03 sobre la baja de cuentas al egreso: la revocación debe implementarse como **deshabilitación y no como eliminación**, dado que borrar la cuenta destruiría la trazabilidad histórica de las acciones realizadas por esa persona, que es precisamente la evidencia que el control busca preservar.

**Umbrales de servicio.** La sección *SLA Thresholds* define el plazo máximo de resolución por nivel de riesgo, con 30 días para Very High en su configuración por defecto. Los planes de acción propuestos en este trabajo establecen vencimientos de entre 98 y 204 días, superiores a ese umbral. Se mantuvieron los plazos propios por reflejar la complejidad técnica real de cada implementación —PA-03 requiere desarrollo sobre el sistema de gestión clínica, no configuración— asumiendo que la herramienta señalará los riesgos como excedidos. Esa señalización constituye información útil para la dirección y no un error de configuración.

**Activos preexistentes.** El inventario incluye tres activos genéricos (Application, Network, System) provenientes de la instalación por defecto, que no forman parte del escenario analizado y se conservan sin modificación.

---

## 6. Conclusiones

**Sobre el escenario analizado.** La clínica presenta una concentración inicial de riesgo elevada, con cuatro riesgos de nivel Crítico sobre ocho identificados. La distribución es consistente con una organización que carece de controles implementados: R01 y R08 no cuentan con ningún control existente, y los presentes en el resto son parciales. El caso de la restricción del portal a la red interna resulta ilustrativo de un patrón más general: se trata de un control correctamente concebido cuya eficacia queda anulada por la ausencia de segmentación, dado que el wifi abierto de sala de espera coloca a cualquier persona dentro del perímetro que ese control presupone confiable.

**Sobre la interdependencia de los riesgos.** El hallazgo de mayor valor práctico del análisis es que las debilidades identificadas se encadenan y se amplifican mutuamente. Esto tiene una consecuencia directa sobre la asignación de recursos: tratar un número reducido de riesgos produce mejoras simultáneas en varios frentes, lo que permite un plan de acción más eficiente que el que resultaría de atender los ocho de forma independiente.

**Sobre la metodología.** La matriz de probabilidad por impacto demostró ser adecuada para construir el registro inicial que el escenario requiere, y sus limitaciones se manifestaron con claridad en el empate entre R04 y R06, que la metodología no permite resolver. La elección de una metodología de análisis de riesgos no es neutral respecto de las preguntas que la organización podrá responder: una matriz cualitativa responde "qué debemos atender primero"; solo un enfoque cuantitativo responde "cuánto debemos invertir".

**Sobre la herramienta.** SimpleRisk cumple adecuadamente su función de registro y seguimiento, aunque su configuración por defecto requiere ajustes para alinearse con una metodología específica. La normalización de la puntuación a escala 0-10, activa por defecto, habría producido una discrepancia silenciosa entre el análisis documentado y los valores mostrados. La observación general es que una herramienta de gestión de riesgos no sustituye la definición metodológica previa: la configura y la registra, pero el criterio debe existir antes.
