# TP: SimpleRisk — Seguridad de Sistemas

## Datos del estudiante

* **Nombre completo:** Bruno Lopez
* **LU / DNI:** 44539196
* **Email institucional:** [lopeznoguerabruno@gmail.com](mailto:lopeznoguerabruno@gmail.com)
* **Comisión:** G

## Descripción del trabajo

Este trabajo práctico tiene como objetivo familiarizarse con SimpleRisk como herramienta de gestión de riesgos y aplicar criterios de análisis, evaluación y tratamiento de riesgos sobre un escenario organizacional.

El escenario seleccionado corresponde a una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día y gestiona historias clínicas digitales, datos de obras sociales, información médica, datos personales y sistemas relacionados con la facturación y la atención.

El análisis busca construir un registro de riesgos, evaluar su nivel, proponer tratamientos y documentar las decisiones tomadas.

## Estructura de la entrega

```text
entregas/bruno-lopez-44539196/
├── README.md
├── .gitignore
├── entorno/
│   ├── docker-compose.yml
│   └── setup.sh
├── configuracion/
│   ├── usuarios.md
│   └── riesgos.md
├── informe/
│   ├── informe.md
│   └── capturas/
├── scripts/
└── reporte-ejecutivo/
    └── reporte.pdf
```

### Directorios

* **entorno/**: archivos necesarios para levantar y reproducir el entorno de SimpleRisk.
* **configuracion/**: documentación de usuarios, permisos, riesgos y configuraciones relevantes.
* **informe/**: desarrollo y análisis del trabajo práctico.
* **informe/capturas/**: evidencias gráficas del trabajo realizado, evitando exponer información sensible.
* **scripts/**: scripts utilizados para automatizar tareas, si corresponde.
* **reporte-ejecutivo/**: reporte destinado al directorio de la clínica.

## Entorno de ejecución

El entorno será implementado utilizando **Docker y Docker Compose**, debido a que permiten disponer de una instalación reproducible y aislada de SimpleRisk.

Las instrucciones definitivas de instalación, levantamiento y acceso serán documentadas una vez implementado y probado el entorno.

Las instrucciones incluidas en este documento serán verificadas antes de la entrega para permitir que el docente pueda reproducir el entorno.

## Parte A — Implementación de SimpleRisk

La implementación deberá permitir:

1. Levantar SimpleRisk mediante un entorno reproducible.
2. Acceder a la aplicación.
3. Configurar al menos tres usuarios con roles diferenciados:

   * Administrador.
   * Analista de riesgos.
   * Auditor.
4. Documentar los usuarios, roles y permisos sin incluir contraseñas.
5. Crear un primer riesgo de prueba.

Las credenciales utilizadas durante la implementación serán ficticias y no se incluirán en el repositorio.

## Parte B — Análisis de riesgos de la clínica

Se utilizará como escenario una clínica privada de:

* 120 empleados.
* Aproximadamente 800 pacientes diarios.
* Historias clínicas digitales.
* Información médica.
* Datos personales.
* Datos de obras sociales.
* Sistemas de facturación.
* Sistemas utilizados para la atención de pacientes.

El análisis deberá identificar como mínimo siete riesgos específicos relacionados con el contexto de la organización.

Cada riesgo deberá documentar:

* Identificador.
* Nombre.
* Descripción.
* Categoría.
* Activos afectados.
* Amenaza relacionada.
* Vulnerabilidad asociada.
* Probabilidad.
* Impacto.
* Justificación de la valoración.
* Nivel de riesgo.
* Controles existentes.
* Estrategia de tratamiento.
* Salvaguardas propuestas.
* Riesgo residual.
* Responsable del riesgo.

También se deberán crear al menos tres planes de acción asociados a riesgos de nivel alto o superior.

## Decisiones de diseño

### Metodología de riesgos

Se utilizará una matriz clásica de **Probabilidad × Impacto**, siguiendo las escalas establecidas por la cátedra.

La probabilidad se valorará de 1 a 5:

| Valor | Nivel       |
| ----- | ----------- |
| 1     | Raro        |
| 2     | Improbable  |
| 3     | Posible     |
| 4     | Probable    |
| 5     | Casi seguro |

El impacto se valorará de 1 a 5:

| Valor | Nivel          |
| ----- | -------------- |
| 1     | Insignificante |
| 2     | Menor          |
| 3     | Moderado       |
| 4     | Mayor          |
| 5     | Catastrófico   |

El valor del riesgo se calculará mediante:

**Riesgo = Probabilidad × Impacto**

La clasificación será:

| Valor | Nivel   |
| ----- | ------- |
| 1–4   | Bajo    |
| 5–9   | Medio   |
| 10–15 | Alto    |
| 16–25 | Crítico |

Además del riesgo inicial, se analizará el **riesgo residual** luego de aplicar las salvaguardas propuestas.

### Identificación y trazabilidad

Para mantener la trazabilidad se utilizarán identificadores únicos:

* Activos: `A01`, `A02`, etc.
* Amenazas: `T01`, `T02`, etc.
* Riesgos: `R01`, `R02`, etc.

Las amenazas estarán relacionadas con activos y vulnerabilidades, y los riesgos estarán relacionados con las amenazas correspondientes.

### Tratamiento

Los riesgos podrán recibir alguna de las siguientes estrategias:

* **Mitigar:** implementar controles para reducir la probabilidad o el impacto.
* **Transferir:** trasladar parte del riesgo a un tercero mediante seguros, contratos o servicios especializados.
* **Aceptar:** asumir el riesgo de manera consciente cuando resulte razonable hacerlo.
* **Evitar:** discontinuar la actividad que genera el riesgo.

Las salvaguardas serán clasificadas como:

* Técnicas.
* Físicas.
* Administrativas.

## Supuestos del escenario

Para realizar el análisis se consideran los siguientes supuestos:

1. La clínica depende de sistemas informáticos para procesos críticos de atención y administración.
2. Las historias clínicas digitales contienen información sensible y requieren protección de confidencialidad e integridad.
3. La indisponibilidad de determinados sistemas puede afectar la continuidad de la atención.
4. El personal utiliza sistemas informáticos y servicios de red para desarrollar sus actividades.
5. La clínica debe considerar riesgos tecnológicos, físicos, operativos y legales.
6. Los controles existentes serán documentados únicamente cuando hayan sido definidos por el escenario o establecidos explícitamente como supuesto de trabajo.
7. Las valoraciones de probabilidad e impacto serán justificadas mediante razonamiento explícito y, cuando corresponda, fuentes externas.
8. La información utilizada para el análisis será ficticia y no contendrá datos reales de pacientes.

## Parte C — Comparación metodológica e integración

Se comparará la metodología clásica de **Probabilidad × Impacto** utilizada en SimpleRisk con al menos una metodología alternativa de gestión o análisis de riesgos.

Entre las alternativas posibles se consideran:

* FAIR.
* OCTAVE.
* NIST SP 800-30.
* ISO/IEC 27005.

La comparación contemplará ventajas, desventajas, subjetividad, facilidad de implementación, necesidad de datos cuantitativos, reproducibilidad y aplicabilidad al escenario de la clínica.

También se analizará una posible integración de SimpleRisk con una herramienta externa, como un sistema SIEM, sistema de tickets, Jira, Slack o Microsoft Teams.

## Reproducibilidad

El objetivo de la entrega es que el entorno y el análisis puedan ser reproducidos por el docente.

La documentación final incluirá:

* Requisitos necesarios.
* Levantamiento del entorno Docker.
* Acceso a SimpleRisk.
* Configuración de usuarios y roles.
* Riesgo inicial de prueba.
* Registro de riesgos de la clínica.
* Planes de acción.
* Evidencias y capturas.
* Reporte ejecutivo.

No se documentarán contraseñas reales ni información sensible.

## Seguridad de la información

Debido a que el trabajo corresponde a la materia Seguridad de Sistemas, se tendrá especial cuidado con la información almacenada en el repositorio.

No se incluirán:

* Contraseñas.
* Tokens.
* API keys.
* Credenciales reales.
* Dumps de bases de datos.
* Backups sensibles.
* Información real de pacientes.
* Otros datos sensibles innecesarios para la demostración.

Las capturas de pantalla serán revisadas antes de incorporarse a la entrega.

El repositorio cuenta con un archivo `.gitignore` destinado a evitar la incorporación accidental de credenciales, bases de datos, archivos sensibles, binarios pesados y logs.

## Documentación complementaria

La entrega incluirá:

* `configuracion/usuarios.md`: usuarios, roles y permisos.
* `configuracion/riesgos.md`: matriz y registro de riesgos.
* `informe/informe.md`: desarrollo completo del trabajo práctico.
* `informe/capturas/`: evidencias de la implementación.
* `reporte-ejecutivo/reporte.pdf`: reporte dirigido al directorio de la clínica.

## Checklist de Auto-Revisión

* [ ] No hay credenciales en el repositorio.
* [ ] El archivo `.gitignore` está correctamente configurado.
* [ ] Las capturas de pantalla no muestran datos sensibles.
* [ ] Los archivos `.sql` o dumps no están subidos.
* [ ] El informe está en un formato legible.
* [ ] El reporte ejecutivo está completo.
* [ ] Los mensajes de commit son descriptivos.
* [ ] Mi branch está actualizada y funciona correctamente.

## Palabra de control

**girasol**

## Estado de la entrega

README inicial preparado. Las instrucciones específicas de instalación y reproducción serán completadas y verificadas durante la implementación del entorno SimpleRisk.



