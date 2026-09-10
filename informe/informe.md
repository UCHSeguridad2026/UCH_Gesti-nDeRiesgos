# Informe - Gestión de Riesgos con SimpleRisk

## Trabajo Práctico de Seguridad de Sistemas

**Carrera:** Licenciatura en Sistemas de Información
**Asignatura:** Seguridad de Sistemas
**Trabajo:** Gestión de Riesgos con SimpleRisk
**Estudiante:** Camila Olivera
**Fecha:** 04/09/2026

---

# 1. Introducción

El presente informe documenta el desarrollo del Trabajo Práctico de Gestión de Riesgos con SimpleRisk.

El objetivo principal es aplicar conceptos de gestión de riesgos de seguridad de la información mediante la identificación, evaluación y tratamiento de riesgos en un escenario organizacional concreto.

Para el desarrollo del trabajo se utilizó una instalación reproducible de SimpleRisk mediante Docker Compose, configurando usuarios con diferentes responsabilidades y registrando riesgos relacionados con una clínica privada.

El análisis considera principalmente los principios de **confidencialidad, integridad y disponibilidad** de la información, además de aspectos legales, operativos y de continuidad del negocio.

---

# 2. Objetivos

## 2.1 Objetivo general

Familiarizarse con una herramienta de gestión de riesgos como SimpleRisk y aplicar criterios profesionales para identificar, evaluar, priorizar y tratar riesgos de seguridad de la información.

## 2.2 Objetivos específicos

* Implementar un entorno reproducible para utilizar SimpleRisk.
* Configurar usuarios con diferentes roles y responsabilidades.
* Aplicar el principio de mínimo privilegio y separación de funciones.
* Identificar riesgos relevantes para una clínica privada.
* Evaluar los riesgos considerando probabilidad e impacto.
* Registrar los riesgos identificados en SimpleRisk.
* Definir tratamientos y planes de mitigación.
* Analizar diferentes metodologías de evaluación de riesgos.
* Documentar las decisiones tomadas durante el desarrollo.
* Mantener prácticas seguras para evitar la exposición de credenciales y secretos.

---

# 3. Descripción del escenario

El escenario analizado corresponde a una clínica privada que cuenta aproximadamente con **120 empleados** y atiende alrededor de **800 pacientes por día**.

La organización utiliza sistemas digitales para gestionar:

* Historias clínicas.
* Información personal y médica de pacientes.
* Datos de seguros.
* Facturación.
* Información necesaria para la atención y gestión administrativa.

Una auditoría externa identificó debilidades en la gestión de riesgos de la organización.

A partir de esta situación se realizó una identificación de riesgos tecnológicos y operativos, priorizando aquellos que pueden afectar la confidencialidad, integridad y disponibilidad de la información y de los servicios críticos.

---

# 4. Entorno de implementación

## 4.1 Tecnología utilizada

Para implementar SimpleRisk se utilizó un entorno virtualizado con:

* Sistema operativo: Kali Linux.
* Virtualización: VirtualBox.
* Contenedores: Docker.
* Orquestación de contenedores: Docker Compose.
* Base de datos: MySQL 8.0.
* Aplicación: SimpleRisk.

La aplicación se ejecuta mediante dos contenedores principales:

* `simplerisk`: aplicación SimpleRisk.
* `simplerisk-mysql`: base de datos MySQL.

La aplicación fue configurada para ser accesible mediante HTTPS.

---

## 4.2 Estructura del entorno

El proyecto utiliza una estructura organizada para separar la configuración del entorno, la documentación, los scripts y el reporte ejecutivo.

La estructura principal es:

```text
entorno/
├── docker-compose.yml
└── .env

configuracion/
├── usuarios.md
└── riesgos.md

informe/
└── capturas/

scripts/

reporte-ejecutivo/
```

El archivo `.env` se utiliza para información de configuración sensible y no se incluye en el repositorio mediante las reglas definidas en `.gitignore`.

---

## 4.3 Instalación reproducible

La instalación de SimpleRisk se realizó mediante Docker Compose.

El archivo `entorno/docker-compose.yml` define los servicios necesarios para ejecutar la aplicación y su base de datos.

Los servicios utilizados son:

```text
simplerisk
simplerisk-mysql
```

La aplicación se expone mediante los puertos:

```text
8080 → HTTP
443 → HTTPS
```

Durante la configuración inicial se detectó que SimpleRisk redirigía las solicitudes hacia HTTPS, por lo que fue necesario publicar también el puerto 443 del contenedor.

La configuración final permite acceder a SimpleRisk mediante:

```text
https://localhost
```

No se documentan ni almacenan contraseñas o credenciales utilizadas durante la instalación.

---

# 5. Configuración de usuarios

Se configuraron tres usuarios con funciones diferenciadas:

| Usuario         | Nombre           | Función             |
| --------------- | ---------------- | ------------------- |
| `admin_demo`    | Laura Fernández  | Administrador       |
| `analista_demo` | Martín Rodríguez | Analista de Riesgos |
| `auditor_demo`  | Sofía González   | Auditor             |

La configuración busca aplicar el principio de **mínimo privilegio** y evitar la concentración de funciones.

### Administrador

`admin_demo` posee los permisos administrativos necesarios para gestionar la plataforma.

### Analista de Riesgos

`analista_demo` posee permisos relacionados con el registro, modificación, evaluación y tratamiento de riesgos.

### Auditor

`auditor_demo` posee permisos relacionados con auditorías, cumplimiento y revisión de riesgos.

Las contraseñas de los usuarios no se documentan ni se incluyen en el repositorio.

La descripción detallada de los permisos se encuentra en:

`configuracion/usuarios.md`

---

# 6. Metodología de identificación y evaluación

La identificación de riesgos se realizó considerando los activos críticos de la clínica, las amenazas relevantes y las posibles consecuencias sobre la organización.

Para cada riesgo se analizaron:

* Activo afectado.
* Amenaza.
* Categoría.
* Probabilidad.
* Impacto.
* Nivel de riesgo.
* Controles existentes.
* Tratamiento propuesto.
* Responsable.

Para complementar la evaluación realizada en SimpleRisk se utilizó una escala de **1 a 5** para probabilidad e impacto.

El cálculo utilizado fue:

**Riesgo inherente = Probabilidad × Impacto**

La escala utilizada fue:

| Puntaje | Clasificación |
| ------: | ------------- |
|   1 - 4 | Bajo          |
|   5 - 9 | Medio         |
| 10 - 15 | Alto          |
| 16 - 25 | Crítico       |

Esta evaluación representa el análisis metodológico del escenario. SimpleRisk, utilizando el método **Classic**, puede mostrar una puntuación diferente debido a su propia escala y fórmula de cálculo.

---

# 7. Identificación de riesgos

En el escenario se identificaron siete riesgos principales:

1. Acceso no autorizado a historias clínicas digitales.
2. Ransomware sobre el sistema de historias clínicas.
3. Pérdida o corrupción de historias clínicas digitales.
4. Indisponibilidad del sistema de historias clínicas.
5. Filtración de datos personales y médicos de pacientes.
6. Manipulación no autorizada de datos de facturación.
7. Falla de infraestructura eléctrica y de red.

Los siete riesgos fueron registrados en SimpleRisk y documentados detalladamente en:

`configuracion/riesgos.md`

---

# 8. Evidencia de la configuración

Las capturas de pantalla obtenidas durante la configuración de SimpleRisk se almacenarán en:

`informe/capturas/`

Las capturas permiten demostrar la creación y configuración de los riesgos y los planes de mitigación.

Los nombres definitivos de los archivos de evidencia serán revisados al finalizar el trabajo para garantizar que las referencias del informe coincidan con los archivos disponibles.

---

# 9. Seguridad de la información durante el desarrollo

Durante el desarrollo se aplicaron medidas para evitar la exposición accidental de información sensible.

Entre ellas:

* No documentar contraseñas.
* No almacenar tokens.
* No almacenar claves de API.
* No incluir credenciales en el repositorio.
* Mantener el archivo `.env` fuera del control de versiones.
* Excluir archivos de bases de datos y respaldos.
* Evitar incluir archivos de máquinas virtuales.
* Evitar incluir logs innecesarios.

El archivo `.gitignore` contiene reglas específicas para excluir estos elementos.

La configuración fue verificada mediante Git, comprobando que `entorno/.env` se encuentra correctamente ignorado.

---

# 10. Decisiones de diseño

Las principales decisiones adoptadas durante el trabajo fueron:

* Utilizar Docker Compose para disponer de un entorno reproducible.
* Separar la aplicación y la base de datos en contenedores independientes.
* Publicar HTTPS para permitir el acceso seguro a SimpleRisk.
* Diferenciar las funciones de administrador, analista y auditor.
* Aplicar el principio de mínimo privilegio.
* Utilizar una evaluación complementaria de probabilidad e impacto de 1 a 5.
* Priorizar el tratamiento mediante mitigación para los riesgos identificados.
* Evitar almacenar información sensible dentro del repositorio.

Como mecanismo de verificación de la lectura y aplicación de las consignas del trabajo se incorpora la palabra **girasol**.

---

# 11. Resultados iniciales

La implementación permitió disponer de una plataforma funcional para registrar y administrar riesgos de seguridad.

Se configuraron los usuarios requeridos y se registró un riesgo de prueba para verificar el funcionamiento inicial de la herramienta.

Posteriormente se registraron siete riesgos correspondientes al escenario de la clínica y se definieron tres planes de mitigación para riesgos prioritarios.

Las siguientes secciones presentan el análisis detallado de los riesgos, los tratamientos seleccionados y la evaluación metodológica.

---

# 12. Comparación metodológica

## 12.1 Metodología utilizada en el trabajo

Para la evaluación de los riesgos se utilizó una matriz de Probabilidad × Impacto.

La probabilidad y el impacto se valoraron mediante una escala de 1 a 5. El nivel de riesgo inherente se obtuvo mediante la siguiente fórmula:

**Riesgo inherente = Probabilidad × Impacto**

La clasificación utilizada fue:

| Puntaje | Clasificación |
| ------: | ------------- |
| 1 - 4   | Bajo          |
| 5 - 9   | Medio         |
| 10 - 15 | Alto          |
| 16 - 25 | Crítico       |

Este método permite priorizar los riesgos de manera sencilla y facilita la comunicación de los resultados.

Por ejemplo, el riesgo **R01 - Acceso no autorizado a historias clínicas digitales** fue evaluado con una probabilidad de 4 y un impacto de 5:

**4 × 5 = 20 → Crítico**

La matriz permite identificar rápidamente los riesgos que requieren mayor atención y facilita la toma de decisiones sobre su tratamiento.

---

## 12.2 Comparación con NIST SP 800-30 Rev. 1

Como metodología alternativa se seleccionó **NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments**.

NIST propone un proceso estructurado para realizar evaluaciones de riesgos. Además de considerar probabilidad e impacto, contempla la identificación de fuentes y eventos de amenaza, vulnerabilidades y condiciones predisponentes, así como las posibles consecuencias para la organización.

La siguiente tabla resume las principales diferencias:

| Aspecto | Matriz Probabilidad × Impacto | NIST SP 800-30 Rev. 1 |
|---|---|---|
| Enfoque | Simple y semicuantitativo | Evaluación de riesgos estructurada |
| Probabilidad | Escala de 1 a 5 | Evaluación de la probabilidad de ocurrencia de eventos de amenaza |
| Impacto | Escala de 1 a 5 | Análisis de las consecuencias adversas |
| Amenazas | Se identifican como parte del análisis | Considera explícitamente fuentes y eventos de amenaza |
| Vulnerabilidades | Se consideran dentro del análisis | Considera vulnerabilidades y condiciones predisponentes |
| Complejidad | Baja | Media/alta |
| Facilidad de comunicación | Alta | Requiere mayor análisis y documentación |
| Uso principal | Priorización rápida de riesgos | Evaluaciones de riesgo más completas y estructuradas |

---

## 12.3 Ventajas y desventajas

### Matriz Probabilidad × Impacto

**Ventajas:**

* Es sencilla de aplicar.
* Permite comparar rápidamente diferentes riesgos.
* Facilita la priorización.
* Es fácil de interpretar por personas técnicas y no técnicas.
* Requiere una cantidad relativamente reducida de información.

**Desventajas:**

* Puede simplificar escenarios complejos.
* Dos riesgos diferentes pueden obtener el mismo puntaje aunque tengan características distintas.
* No representa por sí sola todos los factores del contexto organizacional.
* La multiplicación de probabilidad e impacto puede ocultar diferencias importantes entre riesgos.

### NIST SP 800-30 Rev. 1

**Ventajas:**

* Proporciona un proceso de evaluación más estructurado.
* Considera fuentes y eventos de amenaza.
* Considera vulnerabilidades y condiciones predisponentes.
* Permite analizar con mayor profundidad la probabilidad y el impacto.
* Puede adaptarse al contexto de la organización.

**Desventajas:**

* Requiere mayor cantidad de información.
* Demanda más tiempo para realizar la evaluación.
* Requiere mayor conocimiento metodológico.
* Puede resultar más complejo para evaluaciones iniciales o de rápida priorización.

---

## 12.4 Contexto de aplicación

La matriz Probabilidad × Impacto resulta adecuada para evaluaciones iniciales y para la priorización de riesgos cuando se necesita un método sencillo, reproducible y fácil de comunicar.

NIST SP 800-30 Rev. 1 resulta apropiado cuando la organización necesita realizar una evaluación de riesgos más detallada y estructurada, especialmente cuando se requiere analizar con mayor profundidad las amenazas, vulnerabilidades y condiciones que pueden afectar la probabilidad o las consecuencias de un evento.

En el escenario de la clínica privada, la matriz permite presentar los resultados de manera clara ante responsables de la organización y priorizar los riesgos que requieren tratamiento.

---

## 12.5 Justificación de la metodología seleccionada

Para este Trabajo Práctico se seleccionó la matriz de Probabilidad × Impacto debido a que permite realizar una evaluación clara, reproducible y comprensible de los riesgos identificados.

La metodología facilita la priorización de los siete riesgos analizados y permite determinar cuáles requieren una atención inmediata.

Sin embargo, se reconoce que la matriz constituye una simplificación del análisis de riesgos. En un contexto real, podría complementarse con un enfoque más estructurado como NIST SP 800-30 Rev. 1, incorporando un análisis detallado de las fuentes de amenaza, eventos, vulnerabilidades, condiciones predisponentes y consecuencias.

De esta manera, ambas metodologías pueden considerarse complementarias: NIST puede utilizarse para profundizar la evaluación, mientras que la matriz Probabilidad × Impacto puede utilizarse para facilitar la comunicación y priorización de los resultados.

---

# 13. Integración con herramienta externa

## 13.1 Propuesta de integración

Como propuesta de integración con una herramienta externa se plantea conectar SimpleRisk con un sistema de gestión de tickets.

El objetivo es vincular la gestión de riesgos con el seguimiento operativo de las acciones de tratamiento. De esta manera, los planes de mitigación definidos en SimpleRisk podrían convertirse en tareas asignadas a responsables concretos dentro de un sistema externo.

SimpleRisk dispone de una API REST v2 que permite realizar integraciones programáticas con sistemas externos.

La integración propuesta sería:

```text
SimpleRisk
    |
    | API REST v2
    v
Servicio de integración
    |
    | Creación / actualización de tickets
    v
Sistema de gestión de tickets
```
---

## 13.2 Funcionamiento de la integración

El flujo propuesto sería el siguiente:

1. Se registra un riesgo en SimpleRisk.
2. El riesgo es evaluado y obtiene un nivel de prioridad.
3. Se define el tratamiento y el correspondiente plan de mitigación.
4. Un servicio externo consulta la API de SimpleRisk.
5. El servicio identifica los riesgos o acciones que requieren seguimiento.
6. Se crea o actualiza un ticket en el sistema externo.
7. El ticket se asigna al responsable correspondiente.
8. El equipo realiza y registra el seguimiento de la acción.
9. El estado de la acción puede utilizarse posteriormente para verificar el tratamiento del riesgo en SimpleRisk.

La información que podría trasladarse al sistema de tickets incluye:

* Identificador del riesgo.
* Nombre del riesgo.
* Descripción.
* Nivel de riesgo.
* Tratamiento seleccionado.
* Acción de mitigación.
* Responsable.
* Fecha límite.
* Estado de la acción.

---

## 13.3 Ejemplo aplicado al escenario de la clínica

La integración podría utilizarse, por ejemplo, para el riesgo:

**R02 - Ransomware sobre el sistema de historias clínicas**

Este riesgo tiene asociado un plan de mitigación relacionado con la estrategia de respaldos y recuperación.

En una implementación real, la integración podría generar un ticket con información como:

| Campo | Valor de ejemplo |
|---|---|
| Riesgo | R02 - Ransomware sobre el sistema de historias clínicas |
| Prioridad | Crítica |
| Tratamiento | Mitigar |
| Acción | Fortalecer estrategia de backups y recuperación |
| Responsable | Equipo de Seguridad de la Información |
| Fecha límite | 31/10/2026 |
| Estado inicial | Pendiente |

De esta manera, SimpleRisk mantiene la información relacionada con el riesgo y el sistema de tickets permite gestionar operativamente la tarea asociada.

---

## 13.4 API y autenticación

La integración propuesta utiliza la API REST v2 de SimpleRisk.

La API permite que sistemas externos interactúen programáticamente con la información disponible en SimpleRisk.

Para la autenticación se utilizan claves de API asociadas a usuarios. Las solicitudes pueden utilizar el encabezado:

```text
X-API-KEY
```

13.5 Protección de credenciales

Las credenciales utilizadas para acceder a la API deben almacenarse de forma segura.

No deben:

incluirse directamente en el código fuente;
escribirse en el README;
incluirse en el informe;
aparecer en capturas de pantalla;
almacenarse dentro del repositorio Git.

Una alternativa sería utilizar variables de entorno o un sistema específico de gestión de secretos.

En el presente trabajo no se almacenan claves de API reales, ya que la integración se presenta como una propuesta de diseño y documentación.

Además, el archivo .env utilizado para la configuración del entorno se encuentra excluido del repositorio mediante .gitignore.

13.6 Ventajas de la integración

La integración propuesta permitiría:

Centralizar el seguimiento de las acciones de mitigación.
Asignar tareas a responsables concretos.
Establecer fechas límite.
Facilitar el seguimiento del estado de las acciones.
Mejorar la trazabilidad.
Reducir tareas manuales.
Relacionar cada acción operativa con el riesgo que la origina.

En el escenario de la clínica, esto permitiría vincular los riesgos identificados en SimpleRisk con las actividades necesarias para reducir su impacto o probabilidad.

13.7 Limitaciones y consideraciones

La integración también presenta algunas consideraciones:

Requiere desarrollar o configurar un servicio de integración.
Es necesario proteger adecuadamente las credenciales.
Deben controlarse los permisos del usuario técnico.
Se debe controlar la frecuencia de las consultas a la API.
La integración debe mantenerse ante posibles cambios de versión de SimpleRisk o del sistema externo.
Deben definirse mecanismos para evitar la creación de tickets duplicados.

Por estas razones, antes de implementar la integración en un entorno productivo debería realizarse una prueba controlada y establecerse procedimientos de monitoreo y mantenimiento.


## 13.8 Estado de implementación

La integración con una herramienta externa no fue implementada de forma efectiva durante este Trabajo Práctico. Se presenta como una propuesta de diseño basada en las capacidades de integración de SimpleRisk.

La propuesta permite demostrar cómo podría vincularse la gestión de riesgos con el seguimiento operativo de las acciones de mitigación, sin utilizar credenciales, claves de API ni información sensible real.

Una posible implementación futura podría utilizar un proceso periódico que consulte la API de SimpleRisk y genere o actualice tickets cuando se detecten riesgos o acciones que requieran seguimiento.

Esta alternativa permitiría mantener la separación entre la herramienta de gestión de riesgos y el sistema utilizado para administrar las tareas operativas, mejorando la trazabilidad y el seguimiento de los tratamientos definidos.
