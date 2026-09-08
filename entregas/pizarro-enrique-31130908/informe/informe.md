# Informe — Trabajo Práctico de Gestión de Riesgos con SimpleRisk

Seguridad Aplicada a Sistemas de Información
Licenciatura en Sistemas de Información — Universidad Champagnat

---

## Parte A — Instalación y configuración básica

### A.1 Instalación reproducible

El entorno se desplegó mediante Docker Compose utilizando la imagen oficial
`simplerisk/simplerisk`, que incluye el stack completo (Apache, PHP, MySQL y
utilidades de correo) en un único contenedor.

Las instrucciones completas de despliegue, los requisitos previos y las
decisiones de diseño adoptadas se encuentran documentadas en
[`entorno/README.md`](../entorno/README.md). El archivo de configuración es
[`entorno/docker-compose.yml`](../entorno/docker-compose.yml).

La aplicación queda disponible en `https://localhost:8443`. La captura
`capturas/01-dashboard-inicial.png` corresponde al primer acceso una vez
completada la instalación.

**Observación de seguridad detectada durante la instalación.** El primer acceso a
la aplicación redirige a la pantalla *Default Admin Account Creation*, que permite
crear la cuenta administrativa **sin ninguna autenticación previa**. En una
instancia expuesta a una red no confiable, el primer usuario que alcance el
servicio obtendría el control administrativo completo de la plataforma. Este
hallazgo se desarrolla en la Parte D.

### A.2 Usuarios y permisos

Se crearon tres cuentas con permisos diferenciados, además de la cuenta
administrativa generada por el instalador. El detalle de cada cuenta, los
permisos asignados y los criterios aplicados —segregación de funciones y mínimo
privilegio— se encuentran en
[`configuracion/usuarios.md`](../configuracion/usuarios.md).

Evidencia: `capturas/02-usuarios-creados.png`.

### A.3 Riesgo de prueba

Se registró un riesgo de prueba con el fin de validar el funcionamiento del
módulo de gestión de riesgos antes de proceder a la carga del registro
definitivo.

---

## Parte B — Escenario real

### B.1 Metodología de trabajo

El análisis se desarrolló en dos etapas deliberadamente separadas:

1. **Definición del registro de riesgos** siguiendo la Plantilla de Matriz de
   Riesgos de la cátedra: inventario de activos, identificación de amenazas y
   vulnerabilidades, valoración de probabilidad e impacto, y definición de
   tratamiento con cálculo de riesgo residual.
2. **Carga en SimpleRisk** de los riesgos previamente definidos.

Este orden respondió a un criterio práctico: la herramienta condiciona la forma
del registro mediante sus campos y escalas, por lo que realizar el análisis de
manera independiente permitió que las decisiones respondieran al contexto de la
organización y no a las restricciones del formulario. Las diferencias encontradas
al trasladar el análisis a la herramienta se documentan en el punto B.3.

El análisis completo se encuentra en
[`configuracion/riesgos.md`](../configuracion/riesgos.md).

### B.2 Registro de riesgos

Se identificaron diez riesgos sobre los activos de información de la clínica,
superando el mínimo de siete requerido. La distribución por nivel resultó en
cuatro riesgos Críticos, cinco Altos y uno Medio.

Los diez riesgos fueron cargados en SimpleRisk conservando la nomenclatura R01 a
R10 en el campo *Subject*, de modo de mantener la trazabilidad entre el documento
de análisis y el registro en la herramienta.

Evidencia: `capturas/03-riesgos-cargados.png`.

### B.3 Diferencias entre el análisis y la herramienta

El traslado del análisis a SimpleRisk hizo evidentes tres discrepancias entre el
modelo de la plantilla y la implementación de la herramienta.

**Escalas de valoración.** Las escalas de probabilidad e impacto coinciden en
cantidad de niveles y en semántica, por lo que la conversión fue directa:

| Valor | Plantilla (Probabilidad) | SimpleRisk (Likelihood) |
|---|---|---|
| 1 | Raro | Remote |
| 2 | Improbable | Unlikely |
| 3 | Posible | Credible |
| 4 | Probable | Likely |
| 5 | Casi seguro | Almost Certain |

| Valor | Plantilla (Impacto) | SimpleRisk (Impact) |
|---|---|---|
| 1 | Insignificante | Insignificant |
| 2 | Menor | Minor |
| 3 | Moderado | Moderate |
| 4 | Mayor | Major |
| 5 | Catastrófico | Catastrophic |

**Cálculo del valor de riesgo.** Pese a que ambos enfoques se basan en la
combinación de probabilidad e impacto, los valores resultantes difieren. La
plantilla calcula el producto directo sobre un rango de 1 a 25; SimpleRisk aplica
su propia fórmula sobre un rango de 1 a 10:

| Riesgo | Valor plantilla (P×I) | Nivel plantilla | Valor SimpleRisk |
|---|---|---|---|
| R07 | 20 | Crítico | 8 |
| R08 | 20 | Crítico | 8 |
| R02 | 16 | Crítico | 6.4 |
| R10 | 16 | Crítico | 6.4 |
| R09 | 15 | Alto | 6 |
| R01 | 12 | Alto | 4.8 |
| R04 | 12 | Alto | 4.8 |
| R05 | 12 | Alto | 4.8 |
| R06 | 12 | Alto | 4.8 |
| R03 | 5 | Medio | 2 |

Lo relevante es que **el ordenamiento relativo se conserva pero la magnitud
absoluta no**. Ambos métodos priorizan los mismos riesgos en el mismo orden, de
modo que la decisión sobre qué tratar primero no se ve afectada. Sin embargo, los
umbrales de clasificación no son transferibles entre instrumentos: un riesgo
clasificado como Crítico según los rangos de la plantilla (16 a 25) corresponde a
un valor de 8 en SimpleRisk, donde ese rango no existe. La consecuencia práctica
es que el nivel de riesgo solo tiene sentido dentro del instrumento que lo
produce, y comparar valores entre herramientas distintas carece de significado.

**Taxonomía de categorías.** Las categorías disponibles en SimpleRisk responden a
dominios de control operativo (*Access Management*, *Physical Security*,
*Monitoring*, *Sensitive Data Management*, entre otras) y no a las propiedades de
seguridad de la información —confidencialidad, integridad y disponibilidad— que
propone la consigna. Ante esta diferencia se optó por mantener ambas
clasificaciones: la categorización por propiedad afectada en el documento de
análisis, y la categorización por dominio de control en la herramienta.

La divergencia no es un defecto sino una consecuencia del propósito de cada
instrumento: SimpleRisk está orientado a la gestión operativa de controles, por
lo que su taxonomía facilita agrupar riesgos según el área responsable de
tratarlos, mientras que la clasificación por propiedades resulta más adecuada
para el análisis conceptual.

### B.4 Planes de acción

Se definieron tres planes de acción sobre riesgos de nivel Crítico y Alto,
seleccionados según su relación entre efecto esperado y esfuerzo de
implementación:

| Riesgo | Plan | Vencimiento | Responsable | Esfuerzo | Presupuesto estimado |
|---|---|---|---|---|---|
| R02 (Crítico) | Formalización del procedimiento de baja de accesos | 07/11/2026 | Responsable de Tratamiento | Minor | $600.000 ARS |
| R09 (Alto) | Pruebas documentadas de restauración de copias de respaldo | 07/12/2026 | Responsable de Tratamiento | Considerable | $2.000.000 ARS |
| R07 (Crítico) | Implementación de MFA y programa de concientización | 06/01/2027 | Analista de Riesgos | Significant | $4.500.000 ARS |

Los montos se expresan en pesos argentinos a valores de septiembre de 2026.

El criterio de selección buscó cubrir tres tipos distintos de control: uno
procedimental (R02), uno de verificación (R09) y uno tecnológico combinado con
capacitación (R07). Los tres planes se corresponden con las recomendaciones
prioritarias formuladas en las conclusiones del análisis de riesgos.

El plan sobre R07 presenta un efecto que excede al riesgo tratado: la
implementación de autenticación multifactor reduce también la exposición de R02 y
R08, dado que neutraliza el valor de una credencial comprometida con independencia
del vector por el cual se obtuvo.

Evidencia: `capturas/04-planes-de-accion.png`.

**Limitación de la herramienta en el registro de presupuesto.** El campo
*Mitigation Cost* de SimpleRisk no admite el ingreso de un monto, sino la
selección de un rango predefinido expresado en dólares estadounidenses, con
tramos de 100.000 dólares. Para una organización del tamaño de la analizada, los
tres planes se ubican en el primer tramo disponible, con lo que el campo pierde
toda capacidad de discriminación. Por este motivo, el monto estimado en pesos se
consignó en el campo descriptivo de cada plan. La limitación evidencia que la
herramienta fue diseñada bajo supuestos de escala presupuestaria que no se
corresponden con el contexto de aplicación.

### B.5 Consideración sobre la ejecución del laboratorio

La carga de los riesgos y de los planes de acción se realizó utilizando la cuenta
administrativa. Si bien el esquema de permisos documentado en
`configuracion/usuarios.md` está configurado y es funcional —cada cuenta posee
únicamente los permisos correspondientes a su función—, la operación efectiva no
se distribuyó entre las tres cuentas por razones de practicidad del entorno de
laboratorio. En un despliegue productivo, el registro de riesgos correspondería a
la cuenta de analista y la aprobación de mitigaciones a la de responsable de
tratamiento.


---

## Parte C — Análisis crítico y profundización

### C.1 Comparación metodológica: matriz probabilidad × impacto frente a FAIR

#### El enfoque de SimpleRisk

SimpleRisk implementa, en su método de scoring *Classic*, el enfoque tradicional
de matriz de probabilidad por impacto. El analista selecciona un nivel de
probabilidad y uno de impacto sobre escalas ordinales de cinco valores etiquetados
(*Remote* a *Almost Certain*, *Insignificant* a *Catastrophic*) y la herramienta
deriva un valor de riesgo que permite ordenar el registro.

Es el mismo modelo conceptual que propone la plantilla de la cátedra, y el que se
aplicó en el análisis desarrollado en la Parte B.

#### El enfoque de FAIR

FAIR (Factor Analysis of Information Risk) es un marco cuantitativo que, a
diferencia de los modelos cualitativos basados en clasificaciones alta, media o
baja, utiliza modelos probabilísticos para estimar la frecuencia y la magnitud de
las pérdidas posibles, expresadas en términos financieros.

Su diferencia estructural no es solamente el uso de números en lugar de
etiquetas, sino la **descomposición del riesgo en factores**. Donde la matriz
clásica pide dos juicios globales —qué tan probable es y qué tan grave sería—,
FAIR descompone el riesgo en dos componentes principales, la frecuencia del
evento de pérdida y la magnitud de la pérdida, y a su vez descompone la primera
en frecuencia del evento de amenaza y vulnerabilidad, entendida como la
probabilidad de que la acción del atacante efectivamente derive en una pérdida.

Una segunda diferencia relevante es que FAIR expresa sus resultados como
distribuciones de probabilidad y no como estimaciones puntuales, incorporando la
incertidumbre como parte constitutiva del análisis en lugar de ocultarla detrás de
un número único.

#### Ventajas del enfoque de SimpleRisk

**Costo de aplicación bajo.** El análisis desarrollado en este trabajo, con diez
riesgos valorados y tratados, requirió únicamente el conocimiento del contexto de
la organización. No demandó datos históricos de incidentes, estimaciones de costos
por hora de indisponibilidad ni herramientas de simulación.

**Accesibilidad para participantes no especializados.** Las escalas etiquetadas
permiten que personas ajenas al área de seguridad —responsables de RRHH,
mantenimiento o administración— participen de la valoración. En una clínica de
120 empleados sin área de seguridad constituida, esta característica es
determinante para que el análisis pueda realizarse.

**Suficiencia para la función de priorizar.** Cuando el objetivo es decidir qué
tratar primero, el ordenamiento relativo alcanza. El análisis realizado permitió
identificar sin ambigüedad los cuatro riesgos críticos y fundamentar tres planes
de acción.

#### Desventajas del enfoque de SimpleRisk

**Los valores no son magnitudes.** Esta limitación se verificó empíricamente
durante el desarrollo del trabajo. Como se documentó en el punto B.3, el mismo
riesgo R08 obtuvo un valor de 20 sobre 25 según la plantilla y de 8 sobre 10 según
SimpleRisk. Ambos instrumentos implementan el mismo modelo conceptual y arrojan el
mismo ordenamiento, pero magnitudes distintas. Esto evidencia que el número
producido no mide una cantidad de riesgo existente en el mundo, sino que expresa
una posición dentro de una escala convencional. En consecuencia, no admite
operaciones aritméticas: no tiene sentido afirmar que un riesgo de valor 20 es el
doble de grave que uno de valor 10, ni sumar los diez valores para obtener la
exposición total de la organización.

**No permite evaluar la conveniencia económica del tratamiento.** El plan sobre
R07 tiene un costo estimado de $4.500.000. La matriz permite afirmar que reduce el
riesgo de nivel Crítico a Medio, pero no permite responder si esa reducción
justifica la inversión, porque no existe una unidad común entre el costo del
control y el beneficio esperado. FAIR, al expresar ambos en términos monetarios,
convierte esa comparación en una operación directa.

**Oculta el razonamiento detrás de un juicio global.** Al asignar probabilidad 4 a
R07 se condensa en un único valor la frecuencia con que llegan correos maliciosos,
la proporción de empleados susceptibles de hacer clic y la efectividad de los
controles existentes. La descomposición en factores que propone FAIR obliga a
explicitar cada uno de esos supuestos, lo que los vuelve discutibles y revisables
de manera independiente.

**Favorece el sesgo de concentración en los niveles altos.** El análisis
desarrollado ilustra el fenómeno: la valoración inicial no arrojó ningún riesgo de
nivel Bajo y solo uno Medio. Sin un anclaje externo que discipline la asignación
de valores, la tendencia es a sobrevalorar, lo que degrada la capacidad de la
matriz para discriminar entre riesgos.

#### Ventajas y desventajas de FAIR

FAIR resuelve las limitaciones anteriores: produce magnitudes comparables entre
sí, permite el análisis de costo-beneficio de los controles y explicita los
supuestos. Sin embargo, su aplicación requiere datos de los que la clínica no
dispone —frecuencia histórica de incidentes, costo por hora de indisponibilidad
del sistema de historias clínicas, valor de la información comprometida—, así como
formación específica en el modelo y capacidad de análisis probabilístico.

Aplicado sin esos insumos, FAIR produce estimaciones cuantitativas construidas
sobre supuestos igualmente subjetivos que los de la matriz, pero presentadas con
una apariencia de precisión que no poseen. Este es su principal riesgo de uso: la
falsa precisión resulta más peligrosa que la imprecisión declarada, porque induce
confianza injustificada en el resultado.

#### En qué contexto conviene cada uno

**La matriz de probabilidad × impacto resulta apropiada** para organizaciones que
inician su gestión de riesgos, cuando no existen datos históricos, cuando la
valoración debe involucrar a personas sin formación técnica, y cuando el objetivo
es priorizar antes que cuantificar. Es el caso de la clínica analizada: no cuenta
con área de seguridad constituida, no dispone de registro histórico de incidentes
y necesita definir por dónde empezar.

**FAIR resulta apropiado** para organizaciones con un programa de gestión de
riesgos ya establecido, que disponen de datos históricos, que deben justificar
inversiones de seguridad ante un directorio en términos financieros, o que operan
en sectores regulados donde se exige demostrar la razonabilidad económica de las
decisiones de tratamiento.

#### Conclusión

Los dos enfoques no compiten por el mismo lugar sino que corresponden a etapas
distintas de madurez. La matriz cualitativa responde a la pregunta *qué tratamos
primero*; FAIR responde a *cuánto conviene invertir en tratarlo*. La segunda
pregunta solo tiene sentido una vez respondida la primera, y requiere una base de
datos históricos que únicamente se construye después de haber operado un programa
de gestión de riesgos durante cierto tiempo.

Para el escenario analizado, el enfoque de SimpleRisk es el adecuado. Una
progresión razonable consistiría en mantener la matriz para el registro general y
aplicar un análisis cuantitativo únicamente sobre los riesgos críticos, cuando la
organización acumule datos suficientes y deba decidir sobre inversiones de
magnitud significativa.

### C.2 Integración con una herramienta externa

Se documentó e **implementó** una integración entre SimpleRisk y Discord, que
notifica automáticamente los riesgos cuyo score supera un umbral configurable.

#### Justificación de la herramienta elegida

Se evaluaron tres alternativas de integración:

| Alternativa | Ventaja | Limitación |
|---|---|---|
| SIEM | Correlación con eventos de seguridad reales | Requiere infraestructura de la que la clínica no dispone |
| Jira / sistema de tickets | Convierte cada riesgo en una tarea con seguimiento | SimpleRisk ofrece integración nativa, pero como Extra de pago |
| Mensajería (Discord / Slack / Teams) | Notificación inmediata, sin infraestructura adicional | No genera seguimiento; solo informa |

Se optó por la mensajería instantánea por ser la única implementable de forma
completa en el entorno del trabajo práctico. En un despliegue real de la clínica,
la integración con un sistema de tickets resultaría más adecuada, dado que la
notificación por sí sola no garantiza que el riesgo sea efectivamente tratado.

#### Restricción encontrada: la API es un Extra de pago

SimpleRisk expone una API REST, pero está disponible únicamente mediante el *API
Extra*, uno de los complementos comerciales listados en el panel de
configuración. La instalación base no permite consultar los riesgos por vía
programática.

Esta restricción condicionó el diseño de la integración: ante la imposibilidad de
utilizar la interfaz prevista por el fabricante, la consulta se realiza
directamente sobre la base de datos MySQL del contenedor.

La decisión tiene una contrapartida que corresponde señalar: **acceder
directamente a la base de datos de una aplicación es una práctica frágil**. El
esquema de la base no es una interfaz pública, por lo que puede cambiar entre
versiones sin previo aviso y romper la integración. En un entorno productivo, la
alternativa correcta sería adquirir el Extra correspondiente o utilizar
notificaciones nativas.

#### Arquitectura de la solución

El flujo consta de tres pasos:

1. Un script en Bash consulta la base de datos de SimpleRisk mediante `docker
   exec`, uniendo las tablas `risks` y `risk_scoring` por su identificador.
2. Filtra los riesgos cuyo campo `calculated_risk` supera el umbral configurado y
   que no se encuentran cerrados.
3. Construye un mensaje con formato *embed* y lo envía por HTTP POST a la URL del
   webhook de Discord.

La consulta utilizada es la siguiente:

    SELECT r.id, r.subject, s.calculated_risk,
           s.CLASSIC_likelihood, s.CLASSIC_impact
    FROM risks r
    JOIN risk_scoring s ON r.id = s.id
    WHERE s.calculated_risk >= <umbral>
      AND r.close_id IS NULL
    ORDER BY s.calculated_risk DESC;

La tabla `risk_scoring` almacena los valores de las escalas cargadas por el
analista (`CLASSIC_likelihood` y `CLASSIC_impact`) junto con el score derivado
(`calculated_risk`). La condición sobre `close_id` evita notificar riesgos ya
cerrados.

#### Tratamiento de las credenciales

La integración requiere dos credenciales: la contraseña de la base de datos y la
URL del webhook de Discord, que constituye en sí misma un secreto —quien la posea
puede publicar mensajes en el canal.

Ninguna de las dos está escrita en el script. Ambas se leen desde un archivo
`.env` ubicado en el mismo directorio, que **no se versiona**. El repositorio
incluye en su lugar un archivo `.env.example` con la estructura de variables
requeridas y valores de reemplazo, de modo que la configuración necesaria quede
documentada sin exponer los valores reales.

Para que esto funcione, el `.gitignore` de la entrega incorpora una excepción
explícita:

    .env.*
    !.env.example

La primera línea bloquea cualquier archivo con ese patrón; la segunda lo
reincorpora únicamente para la plantilla. El orden es significativo: la excepción
debe declararse después de la regla que la bloquea.

#### Resultado

La ejecución del script sobre el registro de riesgos cargado detectó cinco
riesgos con score igual o superior a 6 —R08, R07, R10, R02 y R09— y los notificó
correctamente en el canal de Discord configurado, indicando para cada uno su
identificador, denominación, score y los valores de probabilidad e impacto
asignados.

Evidencia: `capturas/05-webhook-discord.png`.

Archivos: `scripts/notificar_riesgos_altos.sh` y `scripts/.env.example`.

#### Posibles extensiones

La implementación actual requiere ejecución manual. Las mejoras inmediatas serían:

- **Programación periódica** mediante `cron`, para una verificación diaria o
  semanal automática.
- **Registro de notificaciones ya enviadas**, de modo que solo se informen riesgos
  nuevos o cuyo score haya aumentado, evitando repetir el mismo listado en cada
  ejecución.
- **Diferenciación por nivel**, enviando los riesgos críticos a un canal distinto
  del de los altos, o mencionando al responsable correspondiente.

#### Referencias 
#### (la búsqueda bibliográfica de esta sección se realizó con asistencia de IA; las fuentes fueron verificadas por el autor)

- The Open Group. *Risk Analysis (O-RA)*. Estándar del modelo FAIR.
- FAIR Institute. *What is FAIR*. https://www.fairinstitute.org/what-is-fair
- Jones, J. A. (2005). *An Introduction to Factor Analysis of Information Risk (FAIR)*. Risk Management Insight LLC.
- NIST (2012). *Guide for Conducting Risk Assessments* (SP 800-30 Rev. 1).
- ISO/IEC (2018). *ISO/IEC 27005: Information security risk management*.

