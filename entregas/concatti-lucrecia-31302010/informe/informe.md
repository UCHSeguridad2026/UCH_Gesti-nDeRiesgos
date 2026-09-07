# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## 1. Introducción

El presente trabajo tiene como objetivo aplicar conceptos de identificación, evaluación y tratamiento de riesgos mediante la utilización de SimpleRisk.

El análisis se desarrolla sobre el escenario de una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día. La organización utiliza sistemas informáticos para gestionar historias clínicas digitales, turnos, datos de obras sociales y procesos de facturación.

El trabajo comprende la instalación y configuración de la herramienta, la definición de usuarios con diferentes responsabilidades, la identificación y valoración de riesgos específicos del escenario, la planificación de acciones de mitigación y un análisis crítico de la metodología utilizada.

---

# 2. Parte A - Instalación y configuración básica

## 2.1 Entorno utilizado

SimpleRisk fue instalado en una máquina virtual con Ubuntu 20.04 ejecutada mediante Oracle VirtualBox sobre un equipo con Windows.

La utilización de una máquina virtual permitió disponer de un entorno Linux independiente y reproducible sin modificar el sistema operativo principal.

Dentro de Ubuntu se instaló Docker y Docker Compose. SimpleRisk fue desplegado mediante un archivo `docker-compose.yml` almacenado dentro de la carpeta `entorno` de la entrega.

El servicio se configuró para exponer los siguientes puertos:

- HTTP: puerto 8080.
- HTTPS: puerto 8443.

Una vez iniciado el contenedor, se verificó su correcto funcionamiento mediante el acceso a la interfaz web de SimpleRisk desde el navegador de Ubuntu.

## 2.2 Instalación reproducible

La instalación se realizó mediante Docker Compose con el objetivo de simplificar la reproducción del entorno.

El archivo `docker-compose.yml` contiene la definición necesaria para ejecutar la imagen de SimpleRisk y publicar los puertos utilizados por la aplicación.

El entorno puede iniciarse desde la carpeta `entorno` mediante:

`sudo docker-compose up -d`

El estado del contenedor puede verificarse mediante:

`sudo docker-compose ps`

Esta configuración permite que el entorno pueda ser reproducido nuevamente sin necesidad de realizar una instalación manual completa de SimpleRisk.

## 2.3 Usuarios y responsabilidades

Se configuraron tres perfiles con responsabilidades diferenciadas:

### Administrador de Seguridad

Posee permisos administrativos sobre la plataforma y es responsable de la configuración general y supervisión del proceso de gestión de riesgos.

### Martina López - Analista de Riesgos

Cuenta con permisos para registrar y modificar riesgos, planificar mitigaciones, revisar diferentes niveles de riesgo y realizar comentarios dentro del módulo Risk Management.

No posee privilegios administrativos.

### Nicolás Fernández - Auditor

Dispone principalmente de permisos de revisión y auditoría. Puede consultar riesgos y acceder a funciones relacionadas con Compliance, pero no puede crear o modificar riesgos ni administrar la plataforma.

La configuración detallada de los usuarios y permisos se encuentra documentada en `configuracion/usuarios.md`. No se almacenan contraseñas en el repositorio.

## 2.4 Riesgo de prueba

Como validación inicial de la instalación se registró un riesgo de prueba denominado:

`Riesgo de prueba - indisponibilidad del portal interno`

El registro permitió comprobar el funcionamiento de la creación, valoración y almacenamiento de riesgos dentro de SimpleRisk antes de comenzar con el escenario principal.

---

# 3. Parte B - Análisis de riesgos de la clínica

## 3.1 Criterio de valoración

Se utilizó una matriz de probabilidad e impacto con valores de 1 a 5.

El valor académico del riesgo se calculó mediante:

`Riesgo = Probabilidad × Impacto`

Los niveles utilizados fueron:

- Bajo: 1 a 4.
- Medio: 5 a 9.
- Alto: 10 a 15.
- Crítico: 16 a 25.

Durante la utilización de SimpleRisk se observó que el método Classic normaliza el resultado a una escala de 10 mediante:

`(Likelihood × Impact) × (10 / 25)`

Por ejemplo, un riesgo con probabilidad 3 e impacto 5 obtiene un valor académico de 15, clasificado como Alto según la matriz utilizada para el trabajo, mientras que SimpleRisk muestra un valor normalizado de 6.

Para mantener consistencia con la metodología solicitada por la cátedra, el análisis documentado utiliza los valores de la matriz 5x5.

## 3.2 Riesgos identificados

Se identificaron siete riesgos específicos del contexto de la clínica:

| ID | Riesgo | Prob. | Impacto | Valor | Nivel |
|---|---|---:|---:|---:|---|
| R01 | Acceso no autorizado a historias clínicas digitales | 4 | 5 | 20 | Crítico |
| R02 | Ransomware en sistemas clínicos | 4 | 5 | 20 | Crítico |
| R03 | Indisponibilidad del sistema de turnos e historias clínicas | 3 | 5 | 15 | Alto |
| R04 | Alteración indebida de información clínica | 3 | 5 | 15 | Alto |
| R05 | Filtración de datos de pacientes por error del personal | 3 | 4 | 12 | Alto |
| R06 | Falla del almacenamiento sin recuperación adecuada | 2 | 5 | 10 | Alto |
| R07 | Interrupción temporal del sistema de facturación con obras sociales | 3 | 3 | 9 | Medio |

El detalle de las descripciones, activos afectados, justificaciones de probabilidad e impacto, controles existentes, propietarios y tratamientos propuestos se encuentra en `configuracion/riesgos.md`.

## 3.3 Resultados

La distribución obtenida fue:

- 2 riesgos críticos.
- 4 riesgos altos.
- 1 riesgo medio.
- 0 riesgos bajos.

Los riesgos de mayor prioridad son el acceso no autorizado a historias clínicas y el ransomware en sistemas clínicos, ambos con un valor de 20.

Estos escenarios pueden comprometer información médica sensible y afectar directamente la continuidad de los servicios utilizados durante la atención de pacientes.

## 3.4 Planes de acción

Se definieron tres planes prioritarios de mitigación.

### Plan 1 - Implementación de MFA y revisión de accesos

Riesgo asociado: Acceso no autorizado a historias clínicas digitales.

Responsable: Martina López.

Fecha de vencimiento: 15/10/2026.

Presupuesto estimado: USD 3.500.

Estado inicial: No iniciado (0%).

El plan contempla implementar autenticación multifactor para los usuarios que acceden a información clínica, revisar privilegios, aplicar el principio de mínimo privilegio y fortalecer el monitoreo de accesos.

### Plan 2 - Fortalecimiento de protección frente a ransomware

Riesgo asociado: Ransomware en sistemas clínicos.

Responsable: Administrador de Seguridad.

Fecha de vencimiento: 31/10/2026.

Presupuesto estimado: USD 8.000.

Estado inicial: No iniciado (0%).

Se propone implementar protección EDR, segmentación de red, filtrado de correo, copias de seguridad offline o inmutables y capacitación frente a phishing.

### Plan 3 - Plan de continuidad de sistemas clínicos

Riesgo asociado: Indisponibilidad del sistema de turnos e historias clínicas.

Responsable: Martina López.

Fecha de vencimiento: 30/11/2026.

Presupuesto estimado: USD 6.000.

Estado inicial: No iniciado (0%).

El plan contempla redundancia de componentes críticos, monitoreo de disponibilidad, procedimientos de contingencia y pruebas periódicas de recuperación.

---

# 4. Parte C - Análisis crítico y profundización

## 4.1 Comparación metodológica: SimpleRisk y NIST SP 800-30 Rev. 1

Para complementar el enfoque utilizado en SimpleRisk se analizó NIST SP 800-30 Rev. 1, guía orientada a la realización de evaluaciones de riesgos de seguridad de la información.

SimpleRisk permite utilizar un enfoque de valoración basado en probabilidad e impacto que facilita el registro, clasificación y priorización de riesgos. Su principal ventaja es la sencillez, ya que permite obtener rápidamente una visión comparable de diferentes escenarios y comunicar los resultados a responsables técnicos y no técnicos.

Como limitación, una valoración centrada principalmente en probabilidad e impacto puede simplificar situaciones complejas y depender significativamente del criterio utilizado para asignar cada valor.

NIST SP 800-30 propone un proceso de evaluación más estructurado. El análisis contempla fuentes de amenaza, eventos de amenaza, vulnerabilidades, condiciones predisponentes, probabilidad de ocurrencia, impacto e incertidumbre antes de determinar el nivel de riesgo.

Este enfoque permite una mayor trazabilidad del razonamiento utilizado para llegar a una valoración y facilita el análisis detallado de escenarios complejos. Como contrapartida, requiere mayor cantidad de información, tiempo y conocimiento técnico.

Para una organización que necesita construir rápidamente un registro inicial y realizar seguimiento de los riesgos, el enfoque aplicado mediante SimpleRisk resulta práctico. En cambio, NIST SP 800-30 resulta conveniente para profundizar el análisis de sistemas críticos o escenarios de amenaza que requieran una fundamentación técnica más detallada.

La experiencia práctica también permitió observar una diferencia en la presentación de los resultados. La matriz académica utilizada en el trabajo opera directamente sobre el resultado de Probabilidad × Impacto, mientras que SimpleRisk normaliza el resultado del método Classic a una escala de 10. Esta diferencia debe considerarse al interpretar y comunicar los niveles de riesgo.

## 4.2 Integración propuesta con Microsoft Teams

Se propone una integración entre SimpleRisk y Microsoft Teams con el objetivo de comunicar rápidamente la aparición de riesgos que requieran atención prioritaria.

SimpleRisk dispone de una API que permite consultar programáticamente información almacenada en la plataforma. La integración podría utilizar una cuenta específica con los privilegios mínimos necesarios para consultar los riesgos.

Un proceso de integración consultaría periódicamente la información disponible y evaluaría los riesgos registrados. Cuando se detectara un riesgo crítico o que superara un umbral previamente establecido, se generaría una notificación.

La notificación podría enviarse mediante una solicitud HTTP POST a un Workflow de Microsoft Teams configurado para recibir peticiones mediante webhook.

El mensaje publicado en el canal de Seguridad podría incluir:

- ID del riesgo.
- Nombre.
- Nivel.
- Responsable.
- Fecha de detección.
- Enlace o referencia al registro correspondiente.

El flujo propuesto sería:

`SimpleRisk -> API -> proceso de integración -> HTTP POST -> Teams Workflow -> canal de Seguridad`

Desde el punto de vista de seguridad, las API keys y las URL utilizadas por los webhooks deben tratarse como secretos. No deberían almacenarse directamente en el código fuente ni incorporarse al repositorio Git.

Se recomienda utilizar variables de entorno o mecanismos específicos de gestión de secretos y aplicar el principio de mínimo privilegio a la cuenta utilizada para la integración.

La integración permitiría reducir el tiempo entre la identificación de un riesgo relevante y su comunicación al equipo responsable.

---

# 5. Consideraciones de seguridad de la entrega

Durante la realización del trabajo se aplicaron medidas destinadas a evitar la exposición de información sensible.

Entre ellas:

- No se almacenaron contraseñas de SimpleRisk en la documentación.
- Se configuró un archivo `.gitignore`.
- Se excluyeron archivos de credenciales, claves, dumps y bases de datos.
- Las capturas utilizadas como evidencia fueron revisadas para evitar la exposición de contraseñas o tokens.
- Se utilizaron datos ficticios para representar usuarios y responsables.
- El trabajo se realizó sobre una branch individual del repositorio.

---
# 6. Parte D - Análisis de seguridad de la instalación

## 5.1 Evaluación de la instalación propia de SimpleRisk

Como actividad adicional se realizó una revisión básica de seguridad sobre la instalación de SimpleRisk utilizada durante el trabajo. El análisis permitió identificar tres configuraciones que podrían fortalecerse en un entorno real.

### Hallazgo 1 - Exposición del servicio en todas las interfaces

Mediante la revisión de los puertos publicados por Docker se comprobó que SimpleRisk escucha en los puertos 8080 y 8443 sobre las direcciones `0.0.0.0` e `[::]`. Esto implica que el servicio se encuentra publicado sobre todas las interfaces de red disponibles en la máquina virtual.

Para un entorno de laboratorio esta configuración facilita el acceso, pero representa una superficie de exposición mayor a la necesaria cuando la aplicación solamente debe utilizarse localmente.

Como mitigación se propone limitar la publicación de los puertos a la interfaz loopback, por ejemplo:

`127.0.0.1:8080:80`

`127.0.0.1:8443:443`

Cuando sea necesario permitir acceso remoto, se recomienda restringir los orígenes autorizados mediante controles de red y firewall.

### Hallazgo 2 - Utilización de una imagen Docker sin versión fija

La instalación utiliza la imagen `simplerisk/simplerisk:latest`.

El uso de la etiqueta `latest` implica que una nueva ejecución o descarga de la imagen podría obtener una versión diferente de la utilizada originalmente. Esto reduce la reproducibilidad del entorno y puede incorporar cambios de funcionamiento o seguridad que no hayan sido previamente evaluados.

Como mitigación se recomienda fijar una versión específica de SimpleRisk o utilizar el digest de una imagen previamente validada. Las actualizaciones deberían realizarse de forma controlada después de verificar su funcionamiento y revisar los cambios de seguridad correspondientes.

### Hallazgo 3 - Firewall del sistema operativo inactivo

La comprobación realizada mediante `ufw status verbose` indicó que el firewall UFW se encuentra inactivo.

Aunque la máquina virtual utilizada para el laboratorio se encuentra en un entorno controlado, la ausencia de una política de firewall del host limita la capacidad de restringir conexiones entrantes si la configuración de red cambia o se publican nuevos servicios.

Como mitigación se propone habilitar UFW y establecer una política restrictiva que permita únicamente las conexiones y puertos estrictamente necesarios para la operación del entorno.

## 5.2 Resultado del análisis

Los hallazgos identificados no impidieron el desarrollo del laboratorio, pero muestran diferencias importantes entre una configuración orientada a pruebas y una instalación destinada a producción.

En un entorno real se recomienda reducir la superficie de exposición de red, utilizar versiones de software controladas y aplicar mecanismos de filtrado de tráfico. Estas medidas contribuyen a mejorar la reproducibilidad, reducir configuraciones innecesariamente permisivas y aplicar el principio de defensa en profundidad.

# 7. Conclusiones

La utilización de SimpleRisk permitió construir un registro inicial de riesgos para el escenario planteado y aplicar de manera práctica las etapas de identificación, valoración y tratamiento.

Los resultados muestran que los principales riesgos de la clínica se encuentran asociados con la protección de las historias clínicas, los accesos a información sensible, la amenaza de ransomware y la continuidad de los sistemas utilizados durante la atención.

La definición de responsables y planes de mitigación permite transformar el análisis en acciones concretas y priorizadas.

La experiencia también permitió observar que las herramientas de gestión de riesgos deben complementarse con criterios metodológicos claros. La puntuación obtenida mediante una herramienta facilita la priorización, pero debe estar acompañada por una justificación del contexto, las amenazas, los activos afectados y las consecuencias potenciales.

Como resultado, se considera prioritario fortalecer la gestión de identidades y accesos, la protección frente a malware, las estrategias de backup y recuperación y la disponibilidad de los servicios clínicos críticos.

---

# 8. Referencias

- NIST. Guide for Conducting Risk Assessments. Special Publication 800-30 Revision 1.
- SimpleRisk. Documentación oficial.
- Plantilla de Matriz de Riesgos provista por la cátedra.
