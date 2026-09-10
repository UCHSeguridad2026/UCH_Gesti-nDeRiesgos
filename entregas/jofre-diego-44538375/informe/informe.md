# Informe del Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## Parte A - Instalación y configuración básica

### 1. Preparación del entorno

> Las evidencias visuales de esta sección se encuentran en el directorio `informe/capturas/`.

*RECOMENDACIÓN: Abrir una pestaña en paralelo para visualizar las capturas.*

Se creó una máquina virtual en VirtualBox con Ubuntu Server 24.04 LTS como sistema operativo invitado.

La máquina virtual fue configurada con recursos suficientes para ejecutar SimpleRisk y Docker, manteniendo el entorno aislado del sistema operativo anfitrión.

Evidencias:

- `1-VB`
- `2-Asignacion de recursos para la VM`
- `3-Resumen VM`
- `4-VM creada`

### 2. Instalación del sistema operativo

Se instaló Ubuntu Server 24.04 LTS dentro de la máquina virtual y se realizaron las actualizaciones iniciales del sistema.

Durante la instalación se utilizó configuración de red mediante NAT y DHCP. No se configuró un proxy y no se instaló inicialmente OpenSSH Server, evitando habilitar servicios que no eran necesarios para el desarrollo del trabajo.

Evidencia:

- `14-Ubuntu ok`

### 3. Instalación de Docker

Se instaló Docker Engine y Docker Compose dentro de Ubuntu Server.

Posteriormente se verificó que Docker se encontrara operativo antes de continuar con la instalación de SimpleRisk.

Evidencia:

- `15-Docker OK`

### 4. Instalación de SimpleRisk

Se descargó y ejecutó la imagen de SimpleRisk mediante Docker.

Se verificó que el contenedor estuviera en ejecución y que la aplicación pudiera ser accedida desde el navegador del sistema anfitrión mediante redirección de puertos de VirtualBox.

Evidencias:

- `16-simplerisk OK`
- `17-Admin default creation form`

### 5. Usuarios y roles

Se crearon cuatro usuarios con roles diferenciados para validar la separación de responsabilidades dentro de la herramienta y aplicar un criterio de mínimo privilegio.

Los roles configurados corresponden a Administrador, Analista de Riesgos, Auditor y Responsable de TI.

El detalle de usuarios, roles, permisos asignados y evidencias correspondientes se encuentra documentado en:

`configuracion/usuarios.md`

### 6. Riesgo de prueba

Se creó un riesgo de prueba para validar el funcionamiento del flujo de alta, evaluación y asignación de riesgos en SimpleRisk.

Este riesgo fue utilizado únicamente como prueba funcional de la herramienta, por lo que los valores de probabilidad e impacto seleccionados no representan una valoración real del riesgo para la clínica.

El detalle se encuentra documentado en:

`configuracion/riesgos.md`

---

## Parte B - Análisis de riesgos del escenario

### 7. Riesgos del escenario y planes de acción

Se definieron y cargaron en SimpleRisk siete riesgos específicos del escenario de la clínica, contemplando aspectos de confidencialidad, integridad, disponibilidad, continuidad operativa y dependencia de terceros.

Para cada riesgo se documentaron los activos afectados, la probabilidad e impacto, su justificación, el nivel resultante, los controles existentes, el tratamiento propuesto y el propietario correspondiente.

Además, se definieron tres planes de acción asociados a los riesgos priorizados por su puntuación, impacto y relevancia para la continuidad y seguridad de la clínica:

- Protección contra ransomware.
- Fortalecimiento de autenticación y prevención de phishing.
- Fortalecimiento de la estrategia de backups.

La instancia de SimpleRisk utilizada normaliza el resultado del método Classic, por lo que riesgos con combinaciones elevadas de probabilidad e impacto pueden quedar clasificados dentro del nivel `Medium`. Por este motivo, la priorización de los planes de acción no se realizó únicamente por la etiqueta asignada por la herramienta, sino también considerando la puntuación obtenida, el impacto potencial y los activos afectados.

El detalle completo de los riesgos, sus evaluaciones, tratamientos, planes de acción y evidencias se encuentra en:

`configuracion/riesgos.md`


---

## Parte C - Análisis crítico y comparación metodológica

### 8. Comparación entre el método Classic de SimpleRisk y NIST SP 800-30

Para la evaluación de los riesgos del escenario se utilizó el método `Classic` disponible en SimpleRisk.

Este método permite valorar cada riesgo mediante la combinación de dos variables principales:

- Probabilidad de ocurrencia.
- Impacto asociado.

La utilización de una escala de 1 a 5 permite obtener una valoración sencilla y comparable entre los distintos riesgos registrados.

Este enfoque presenta como principal ventaja su facilidad de aplicación y comprensión, ya que permite identificar rápidamente cuáles son los riesgos que requieren mayor atención.

Sin embargo, al reducir el análisis principalmente a probabilidad e impacto, puede simplificar situaciones en las que intervienen múltiples amenazas, vulnerabilidades, controles o escenarios de ataque.

Como metodología alternativa se analizó NIST SP 800-30 Rev. 1, guía desarrollada por el National Institute of Standards and Technology para la realización de evaluaciones de riesgos de seguridad de la información.

NIST propone un proceso más estructurado que contempla la preparación de la evaluación, la identificación y análisis de amenazas y vulnerabilidades, la determinación de la probabilidad e impacto, la comunicación de los resultados y el mantenimiento de la evaluación a lo largo del tiempo.

### Comparación

| Aspecto | SimpleRisk Classic | NIST SP 800-30 |
|---|---|---|
| Enfoque | Probabilidad × impacto | Análisis estructurado de amenazas, vulnerabilidades, probabilidad e impacto |
| Complejidad | Baja | Media/Alta |
| Facilidad de aplicación | Alta | Requiere mayor análisis y documentación |
| Velocidad de evaluación | Alta | Menor debido al nivel de detalle |
| Nivel de detalle | General | Más profundo y contextual |
| Seguimiento | Depende de la gestión realizada en la herramienta | Considera explícitamente el mantenimiento de la evaluación |
| Uso recomendado | Evaluaciones rápidas y priorización de riesgos | Evaluaciones más formales y detalladas |

### Ventajas y desventajas

El método Classic resulta adecuado cuando se necesita realizar una evaluación rápida, comprensible y fácil de comunicar a responsables no técnicos.

NIST SP 800-30 permite desarrollar un análisis más profundo de las causas y condiciones que generan un riesgo, aunque requiere mayor esfuerzo, información y tiempo para su aplicación.

Para el escenario de la clínica, el método Classic resulta suficiente para realizar una primera identificación y priorización de riesgos.

Sin embargo, en una organización real que administra historias clínicas digitales, información personal y procesos críticos, sería conveniente complementar esta valoración inicial con una metodología más estructurada como NIST SP 800-30, especialmente para los riesgos de mayor impacto.

### 9. Integración propuesta con Slack

Como integración externa se propone vincular SimpleRisk con Slack, utilizando esta plataforma como canal de comunicación y notificación para el seguimiento de riesgos y planes de mitigación.

El objetivo de la integración sería mejorar la comunicación entre los responsables involucrados en la gestión de riesgos, permitiendo informar rápidamente sobre nuevos riesgos, cambios en su nivel de criticidad, vencimientos de acciones de mitigación o situaciones que requieran revisión.

SimpleRisk continuaría siendo la herramienta principal para registrar, evaluar y gestionar los riesgos, mientras que Slack funcionaría como medio de comunicación y alerta para los responsables correspondientes.

#### Flujo de integración propuesto

```text
SimpleRisk
    |
    v
Cambio o evento relevante sobre un riesgo
    |
    v
Integración / API / Webhook
    |
    v
Slack
    |
    v
Canal de gestión de riesgos
    |
    v
Responsable de TI / Analista / Administrador
```

Por ejemplo, cuando un riesgo alcance un nivel elevado o se aproxime la fecha límite de un plan de mitigación, podría generarse una notificación en un canal específico de Slack.

La notificación podría incluir información como:

- Nombre del riesgo.
- Nivel de criticidad.
- Responsable asignado.
- Estado del plan de mitigación.
- Fecha límite de la acción.
- Enlace o referencia al riesgo registrado en SimpleRisk.

#### Aplicación al escenario de la clínica

En el escenario de la clínica, esta integración permitiría mejorar la coordinación entre el Analista de Riesgos, el Responsable de TI y otros responsables involucrados.

Por ejemplo, ante el riesgo de ransomware sobre el sistema de gestión clínica, Slack podría utilizarse para notificar al Responsable de TI sobre una acción de mitigación pendiente o próxima a vencer.

De manera similar, podría utilizarse para informar sobre riesgos relacionados con phishing, pérdida de backups, indisponibilidad de la red interna o accesos no autorizados.

#### Consideraciones de seguridad

Las notificaciones enviadas a Slack deberían contener únicamente la información necesaria para identificar y gestionar el riesgo.

No deberían enviarse mediante este canal contraseñas, credenciales, historias clínicas, datos personales de pacientes ni otra información sensible.

También sería recomendable utilizar canales con acceso restringido únicamente al personal que participe en el proceso de gestión de riesgos.

Para este trabajo se documenta únicamente la propuesta conceptual de integración con Slack, sin realizar su implementación técnica.s