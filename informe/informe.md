# Informe técnico — Gestión de Riesgos

## Parte A — Instalación y configuración

### A.1 Instalación de SimpleRisk

Se utilizó Docker Compose para implementar un entorno reproducible compuesto por dos contenedores:

* SimpleRisk.
* MySQL 8.0.

La separación entre la aplicación y la base de datos permite mantener una arquitectura simple y reproducible para el entorno de laboratorio.

### A.2 Levantamiento del entorno

Desde la carpeta `entorno/` se ejecutaron:

```bash
docker compose pull
docker compose up -d
docker compose ps
```

### Acceso a SimpleRisk

La aplicación utiliza HTTPS. Para permitir el acceso desde el host se publicaron los siguientes puertos:

* `8080` → HTTP.
* `8443` → HTTPS.

El acceso principal al sistema se realiza mediante:

`https://localhost:8443`

Al tratarse de un entorno local de laboratorio, el certificado HTTPS no corresponde a una autoridad certificadora pública.

### A.3 Usuarios y permisos

Se configuraron tres cuentas ficticias con responsabilidades diferenciadas:

* **Administrador:** responsable de la administración general de la instancia y de la configuración de la plataforma.
* **Analista de riesgos:** responsable de registrar, evaluar y actualizar los riesgos.
* **Auditor:** responsable de consultar la información y evidencias del registro sin modificar los riesgos.

La asignación de permisos busca aplicar el principio de mínimo privilegio, otorgando a cada usuario solamente las capacidades necesarias para desempeñar su función.

El detalle de las cuentas, roles y permisos se encuentra documentado en:

`../configuracion/usuarios.md`

No se incluyen contraseñas en la documentación.

### A.4 Validación funcional

Se creó un riesgo de prueba con el objetivo de verificar el correcto funcionamiento de la plataforma y validar el proceso de alta, evaluación y visualización de riesgos.

El riesgo de prueba corresponde a:

**PRUEBA-001 — Acceso no autorizado a historias clínicas electrónicas.**

La prueba permitió comprobar el funcionamiento del formulario de carga, la asignación de propietario, la selección de categoría, la valoración mediante la metodología Classic y el almacenamiento del riesgo.

La prueba fue realizada satisfactoriamente y posteriormente se verificó que el registro permaneciera almacenado en SimpleRisk.

El detalle del riesgo de prueba se encuentra en:

`../configuracion/riesgos.md`

---

# Parte B — Registro inicial de riesgos de la clínica

## B.1 Contexto del escenario

El análisis se realizó sobre una clínica privada de aproximadamente **120 empleados** que atiende alrededor de **800 pacientes por día**.

La organización utiliza sistemas digitales para gestionar historias clínicas, información médica, datos de obras sociales y procesos de facturación. Debido a esta dependencia tecnológica, la confidencialidad, integridad y disponibilidad de la información resultan fundamentales para garantizar tanto la continuidad operativa como la correcta atención de los pacientes.

La evaluación parte de las debilidades detectadas durante una auditoría externa de seguridad y gestión de riesgos.

## B.2 Metodología de evaluación

Para la valoración se utilizó la metodología **Classic** de SimpleRisk, utilizando una escala de 1 a 5 para probabilidad e impacto.

El nivel de riesgo se obtiene mediante:

**Riesgo = Probabilidad × Impacto**

La clasificación utilizada es:

| Valor | Nivel   |
| ----: | ------- |
|   1–4 | Bajo    |
|   5–9 | Medio   |
| 10–15 | Alto    |
| 16–25 | Crítico |

La probabilidad se determinó considerando la exposición de la organización, cantidad de usuarios, dependencia tecnológica, amenazas existentes y controles asumidos.

El impacto se determinó considerando principalmente las consecuencias sobre la atención médica, la confidencialidad de la información, la integridad de los registros clínicos, la continuidad operativa, la reputación y las posibles consecuencias legales.

Los valores corresponden a una **evaluación inicial del escenario académico** y no representan estadísticas reales de incidentes de la clínica.

El detalle completo de los riesgos se encuentra en:

`../configuracion/riesgos.md`

---

## B.3 Riesgos identificados

Se identificaron siete riesgos principales:

| ID   | Riesgo                                               |  P |  I | Valor | Nivel       |
| ---- | ---------------------------------------------------- | -: | -: | ----: | ----------- |
| R-01 | Ransomware sobre sistemas de historias clínicas      |  4 |  5 |    20 | **Crítico** |
| R-02 | Acceso no autorizado a historias clínicas            |  4 |  5 |    20 | **Crítico** |
| R-03 | Indisponibilidad del sistema de historias clínicas   |  3 |  5 |    15 | **Alto**    |
| R-04 | Phishing y robo de credenciales de empleados         |  4 |  4 |    16 | **Crítico** |
| R-05 | Fuga de información de pacientes y obras sociales    |  3 |  5 |    15 | **Alto**    |
| R-06 | Alteración no autorizada de información clínica      |  3 |  5 |    15 | **Alto**    |
| R-07 | Incendio o inundación de infraestructura tecnológica |  2 |  5 |    10 | **Alto**    |

### Principales riesgos

Los riesgos con mayor valoración son **R-01 y R-02**, ambos con un valor de 20/25.

El ransomware podría impedir el acceso a las historias clínicas y afectar directamente la continuidad de la atención médica. Por otro lado, un acceso no autorizado podría comprometer información médica y personal altamente sensible.

El tercer riesgo crítico corresponde a **R-04 — Phishing y robo de credenciales**, con un valor de 16/25. El compromiso de una cuenta podría facilitar accesos indebidos y constituir un punto de entrada para ataques posteriores.

Los riesgos R-03, R-05, R-06 y R-07 se encuentran en nivel alto.

---

## B.4 Tratamiento de los riesgos

Para los siete riesgos se seleccionó la estrategia de **mitigación**, debido a que es posible reducir la probabilidad o las consecuencias mediante controles técnicos, administrativos y físicos.

Entre las principales salvaguardas propuestas se encuentran:

* Copias de seguridad offline o inmutables.
* Autenticación multifactor.
* Principio de mínimo privilegio.
* Revisión periódica de permisos.
* Segmentación de red.
* Protección de endpoints.
* Capacitación contra phishing.
* Monitoreo de accesos.
* Registros de auditoría.
* Redundancia de infraestructura.
* Procedimientos de contingencia.
* Pruebas de recuperación.
* Clasificación y cifrado de información.
* Protección física de servidores y equipamiento.

El detalle de cada tratamiento se encuentra documentado en:

`../configuracion/riesgos.md`

---

## B.5 Planes de acción

Se definieron tres planes de acción asociados a riesgos prioritarios.

| ID    | Riesgo asociado             | Plan de acción                        | Vencimiento | Presupuesto | Estado      |
| ----- | --------------------------- | ------------------------------------- | ----------- | ----------: | ----------- |
| PA-01 | R-01 — Ransomware           | Backups resilientes contra ransomware | 30/11/2026  |   USD 8.000 | Not Started |
| PA-02 | R-02 — Acceso no autorizado | Implementación de MFA                 | 31/10/2026  |   USD 4.000 | Not Started |
| PA-03 | R-04 — Phishing             | Capacitación y simulación de phishing | 15/10/2026  |   USD 2.000 | Not Started |

El presupuesto total estimado para los tres planes es de **USD 14.000**.

### PA-01 — Backups resilientes contra ransomware

El objetivo es implementar una estrategia de copias de seguridad que incluya almacenamiento separado de la infraestructura productiva y al menos una copia offline o inmutable.

También se realizarán pruebas periódicas de restauración para verificar que los respaldos puedan utilizarse ante un incidente.

**Vencimiento:** 30/11/2026.
**Responsable:** Director de Sistemas / Responsable de Infraestructura.
**Presupuesto:** USD 8.000.
**Estado inicial:** Not Started.

### PA-02 — Implementación de MFA

El objetivo es implementar autenticación multifactor en los sistemas críticos, priorizando cuentas administrativas y usuarios con acceso a información clínica.

**Vencimiento:** 31/10/2026.
**Responsable:** Responsable de Seguridad de la Información.
**Presupuesto:** USD 4.000.
**Estado inicial:** Not Started.

### PA-03 — Capacitación y simulación de phishing

El objetivo es capacitar a los aproximadamente 120 empleados en reconocimiento de correos fraudulentos, ingeniería social, manejo seguro de credenciales y mecanismos de reporte.

También se realizarán campañas de simulación para evaluar la efectividad de la capacitación.

**Vencimiento:** 15/10/2026.
**Responsable:** Responsable de Seguridad de la Información / Recursos Humanos.
**Presupuesto:** USD 2.000.
**Estado inicial:** Not Started.

El detalle de los planes se encuentra en:

`../configuracion/riesgos.md`

---

## B.6 Estado de los tratamientos

Los tres planes de acción se encuentran inicialmente en estado **Not Started**, ya que las salvaguardas propuestas todavía no fueron implementadas.

Por este motivo, los valores de riesgo utilizados como referencia corresponden al **riesgo actual/inherente** y no deben interpretarse como una reducción ya obtenida.

Los planes representan acciones de tratamiento futuras destinadas a disminuir la exposición de la clínica.

---

## B.7 Distribución de riesgos

La distribución de los siete riesgos según la matriz utilizada es:

| Nivel     | Cantidad | Porcentaje |
| --------- | -------: | ---------: |
| Crítico   |        3 |    42,86 % |
| Alto      |        4 |    57,14 % |
| Medio     |        0 |        0 % |
| Bajo      |        0 |        0 % |
| **Total** |    **7** |  **100 %** |

El **100 % de los riesgos identificados requiere algún nivel de tratamiento**, mientras que el 42,86 % corresponde a riesgos críticos que requieren acción inmediata y seguimiento prioritario.

---

# Parte C — Reporte ejecutivo

## C.1 Resumen ejecutivo

La evaluación inicial identificó siete riesgos de seguridad de la información que afectan sistemas y datos críticos de una clínica privada de 120 empleados y aproximadamente 800 pacientes diarios.

Los principales riesgos corresponden a ransomware, acceso no autorizado a historias clínicas y phishing. Estos riesgos pueden afectar la continuidad de la atención médica y comprometer información altamente sensible.

Se definieron tres planes de acción prioritarios con un presupuesto total estimado de **USD 14.000**.

## C.2 Top 5 de riesgos

| Prioridad | Riesgo                                             | Valor | Nivel   |
| --------: | -------------------------------------------------- | ----: | ------- |
|         1 | Ransomware sobre sistemas de historias clínicas    |    20 | Crítico |
|         2 | Acceso no autorizado a historias clínicas          |    20 | Crítico |
|         3 | Phishing y robo de credenciales                    |    16 | Crítico |
|         4 | Indisponibilidad del sistema de historias clínicas |    15 | Alto    |
|         5 | Fuga de información de pacientes y obras sociales  |    15 | Alto    |

## C.3 Recomendaciones prioritarias

Se recomienda:

1. Implementar backups offline o inmutables y probar periódicamente su restauración.
2. Implementar MFA para sistemas críticos y cuentas con acceso a información clínica.
3. Establecer un programa permanente de capacitación y simulación de phishing.
4. Aplicar mínimo privilegio y revisar periódicamente los permisos.
5. Fortalecer los mecanismos de auditoría y monitoreo de accesos y modificaciones de historias clínicas.
6. Formalizar procedimientos de continuidad, contingencia y recuperación.

El reporte ejecutivo completo se encuentra documentado en el informe correspondiente.

---

# Parte D — Análisis crítico e integración

## D.1 Análisis de la metodología

La metodología Classic utilizada por SimpleRisk permite obtener una valoración sencilla y comprensible mediante la combinación de probabilidad e impacto.

Su principal ventaja para este trabajo es que permite establecer una línea base y priorizar rápidamente los riesgos que requieren tratamiento.

Sin embargo, la valoración depende de la calidad de los criterios utilizados para asignar probabilidad e impacto. En un entorno real sería necesario complementar la evaluación con información histórica, indicadores, resultados de auditorías, inventario actualizado y evidencia de controles.

## D.2 Integración con buenas prácticas

La metodología utilizada puede complementarse con marcos como **NIST SP 800-30 Rev. 1**, incorporando un análisis más estructurado de amenazas, vulnerabilidades, probabilidad, impacto y riesgo residual.

También sería conveniente relacionar las salvaguardas propuestas con controles específicos y establecer indicadores para medir la reducción efectiva del riesgo.

## D.3 Integración futura con gestión de tareas

Como evolución del proceso, las mitigaciones registradas en SimpleRisk podrían integrarse con una herramienta de gestión de tareas como Jira.

De esta forma, cada plan de tratamiento podría dividirse en tareas técnicas, responsables, fechas límite y evidencias de cumplimiento.

Esto permitiría establecer una trazabilidad entre:

**Riesgo → Tratamiento → Tarea → Responsable → Evidencia → Estado**

El desarrollo completo del análisis crítico y la propuesta de integración se encuentra en:

`../configuracion/analisis-critico.md`

---

# Parte E — Conclusiones

La implementación de SimpleRisk permitió construir un registro inicial de riesgos para el escenario de la clínica y validar el funcionamiento de una herramienta de gestión de riesgos en un entorno reproducible.

El análisis identificó siete riesgos específicos relacionados con la confidencialidad, integridad y disponibilidad de los sistemas y de la información clínica.

Los resultados muestran que los riesgos de mayor prioridad están relacionados con ransomware, acceso no autorizado y phishing. Estos riesgos requieren tratamiento prioritario debido a su capacidad para afectar tanto la información sensible como la continuidad de la atención médica.

Se definieron tres planes de acción iniciales por un presupuesto estimado total de **USD 14.000**, orientados a fortalecer los backups, implementar MFA y reducir la exposición al phishing.

Como siguiente etapa, se recomienda implementar las salvaguardas propuestas, medir su efectividad y actualizar periódicamente la evaluación de riesgos. De esta manera, SimpleRisk puede utilizarse no solamente como un registro estático, sino como una herramienta de seguimiento continuo de la gestión de riesgos de la organización.

---

# Evidencias generales

| Evidencia                                         | Descripción                         |
| ------------------------------------------------- | ----------------------------------- |
| `capturas/01-contenedores-up.png`                 | Contenedores en ejecución.          |
| `capturas/02-simpleRisk-funcionando.png`          | SimpleRisk funcionando.             |
| `capturas/03-user-admin.png`                      | Usuario administrador.              |
| `capturas/04-user-analista.png`                   | Usuario analista de riesgos.        |
| `capturas/05-user-auditor.png`                    | Usuario auditor.                    |
| `capturas/06-riesgo-prueba.png`                   | Riesgo de prueba.                   |
| `capturas/07-riesgo-r01.png`                      | Registro de riesgos de la clínica.  |
| `capturas/08-riesgo-r02.png`                      | Registro de riesgos de la clínica.  |
| `capturas/09-tabla-riesgos.png`                   | Tabla de riesgos.                   |
| `capturas/10-mitigacion-ramsonware.png`           | Plan de acción asociado a R-01.     |
| `capturas/11-mitigacion-acceso.png`               | Plan de acción asociado a R-02.     |
| `capturas/12-mitigacion-phising.png`              | Plan de acción asociado a R-04.     |
| `capturas/13-tabla-mitigaciones.png`              | Tabla de mitigaciones.              |



