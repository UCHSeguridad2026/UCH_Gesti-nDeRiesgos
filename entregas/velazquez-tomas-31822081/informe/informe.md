# Informe técnico — Gestión de Riesgos con SimpleRisk

## 1. Introducción

El presente trabajo tiene como objetivo aplicar un proceso de identificación, análisis, evaluación y tratamiento de riesgos de seguridad utilizando la plataforma SimpleRisk.

El escenario planteado corresponde a una clínica privada con aproximadamente 120 empleados y una atención de 800 pacientes por día. La organización utiliza sistemas informáticos para gestionar historias clínicas digitales, información de obras sociales y datos relacionados con facturación.

Debido a la sensibilidad de esta información y a la dependencia de los sistemas informáticos para la operación diaria, resulta necesario identificar los principales escenarios de riesgo y establecer medidas de tratamiento adecuadas.

---

## 2. Alcance

El análisis se concentra principalmente en los siguientes activos y procesos:

- Sistema de historias clínicas digitales.
- Información médica de pacientes.
- Base de datos clínica.
- Infraestructura de red.
- Credenciales y cuentas de usuarios.
- Servicios proporcionados por terceros.
- Procesos relacionados con el tratamiento de información sensible.

Se consideran riesgos que puedan afectar la confidencialidad, integridad y disponibilidad de la información, además de consecuencias legales y operativas.

---

## 3. Entorno utilizado

Para ejecutar SimpleRisk se utilizó un entorno local compuesto por:

| Componente | Utilización |
|---|---|
| Sistema operativo | Windows |
| Contenedores | Docker Desktop |
| Subsistema | WSL 2 |
| Plataforma | SimpleRisk |
| Navegador | Navegador web mediante HTTPS |
| Control de versiones | Git / GitHub |
| Editor | Visual Studio Code |

SimpleRisk fue desplegado mediante Docker y se accedió localmente utilizando HTTPS.

La configuración reproducible del entorno se encuentra documentada en:

`entorno/docker-compose.yml`

---

## 4. Configuración inicial de SimpleRisk

Como parte de la configuración inicial se definieron usuarios con diferentes responsabilidades.

| Perfil | Responsabilidad |
|---|---|
| Administrador | Administración y configuración general de SimpleRisk |
| Analista de riesgos | Registro, evaluación y tratamiento de riesgos |
| Auditor | Consulta, revisión y seguimiento |

La separación de funciones busca evitar la asignación innecesaria de privilegios y aplicar el principio de mínimo privilegio.

Las contraseñas y demás credenciales utilizadas no se incluyen en el repositorio.

La configuración completa se encuentra documentada en:

`configuracion/usuarios.md`

---

## 5. Riesgo inicial de prueba

Antes de realizar el análisis definitivo se creó un riesgo de prueba con el objetivo de validar el funcionamiento del registro de riesgos y la configuración inicial de SimpleRisk.

Esta prueba permitió verificar:

- Creación de riesgos.
- Selección de categorías.
- Asociación de activos.
- Asignación de propietarios.
- Configuración de probabilidad e impacto.
- Funcionamiento del método Classic.

Una vez validado el entorno se procedió a registrar los riesgos correspondientes al escenario de la clínica.

---

## 6. Metodología de evaluación

Para registrar y evaluar los riesgos se utilizó el método **Classic** disponible en SimpleRisk.

Para la documentación académica se utilizó además una escala de probabilidad e impacto de 1 a 5.

### Probabilidad

| Valor | Interpretación |
|---:|---|
| 1 | Muy improbable |
| 2 | Improbable |
| 3 | Posible / Credible |
| 4 | Probable / Likely |
| 5 | Casi seguro |

### Impacto

| Valor | Interpretación |
|---:|---|
| 1 | Insignificante |
| 2 | Menor |
| 3 | Moderado |
| 4 | Mayor |
| 5 | Catastrófico |

La valoración académica se obtiene mediante:

**Riesgo = Probabilidad × Impacto**

Esta valoración se utiliza para justificar y comparar los riesgos del trabajo. La puntuación interna presentada por SimpleRisk mediante el método Classic se documenta separadamente cuando su escala no coincide directamente con el valor académico P × I.

---

## 7. Riesgos identificados

Se identificaron siete riesgos específicos para el escenario de la clínica.

| ID | Riesgo | P | I | Valor |
|---|---|---:|---:|---:|
| R01 | Ataque de ransomware al sistema de historias clínicas | 4 | 5 | 20 |
| R02 | Acceso no autorizado mediante credenciales comprometidas | 4 | 5 | 20 |
| R03 | Pérdida o corrupción de datos clínicos | 3 | 5 | 15 |
| R04 | Caída de la infraestructura de red | 3 | 4 | 12 |
| R05 | Acceso no autorizado a la base de datos clínica | 3 | 5 | 15 |
| R06 | Divulgación accidental de información clínica | 3 | 4 | 12 |
| R07 | Interrupción de servicios de un proveedor tecnológico | 3 | 4 | 12 |

La descripción detallada, justificación, controles existentes y tratamientos correspondientes se encuentran en:

`configuracion/riesgos.md`

---

## 8. Riesgos prioritarios

### R01 — Ataque de ransomware

El ransomware representa uno de los escenarios de mayor impacto debido a la posibilidad de provocar la indisponibilidad de las historias clínicas.

Se asignó una probabilidad de **4/5** y un impacto de **5/5**.

Los controles prioritarios propuestos incluyen:

- EDR.
- MFA.
- Segmentación de red.
- Gestión de parches.
- Backups aislados e inmutables.
- Pruebas de restauración.
- Capacitación frente a phishing.

### R02 — Credenciales comprometidas

El robo de credenciales podría permitir que un atacante acceda a información clínica utilizando una cuenta legítima.

Se asignó una probabilidad de **4/5** y un impacto de **5/5**.

Los principales controles propuestos son:

- MFA.
- Principio de mínimo privilegio.
- Políticas de contraseñas.
- Bloqueo ante intentos fallidos.
- Revisión periódica de permisos.
- Monitoreo de accesos.

### R03 — Pérdida o corrupción de datos

La corrupción o eliminación de información clínica puede producirse por errores de software, almacenamiento, base de datos o acciones humanas accidentales.

Se asignó una probabilidad de **3/5** y un impacto de **5/5**.

Los controles propuestos incluyen:

- Backups automatizados.
- Backups aislados.
- Pruebas de restauración.
- Validación de integridad.
- Redundancia.
- Auditoría de modificaciones.

---

## 9. Planes de acción

Se definieron planes de mitigación asociados a riesgos prioritarios.

| Riesgo | Plan | Responsable | Fecha prevista | Presupuesto | Estado inicial |
|---|---|---|---|---|---|
| R01 | Fortalecimiento contra ransomware | Analista de riesgos | 09/10/2026 | $0–$100.000 | Planificado |
| R02 | Fortalecimiento de autenticación y accesos | Analista de riesgos | 09/10/2026 | $0–$100.000 | Planificado |
| R03 | Protección y recuperación de datos clínicos | Analista de riesgos | 09/10/2026 | $0–$100.000 | Planificado |

### Plan R01 — Fortalecimiento contra ransomware

El plan contempla la incorporación de EDR, MFA, segmentación de red, gestión de parches, backups inmutables y capacitación del personal.

El objetivo es disminuir la probabilidad de infección y mejorar la capacidad de recuperación ante un ataque.

### Plan R02 — Fortalecimiento de autenticación y accesos

El plan contempla MFA, mínimo privilegio, políticas de contraseñas, bloqueo de cuentas, revisión periódica de permisos y monitoreo de accesos.

El objetivo es reducir la posibilidad de que credenciales comprometidas permitan el acceso a información clínica.

### Plan R03 — Protección y recuperación de datos clínicos

El plan contempla backups automatizados y aislados, pruebas de restauración, controles de integridad, redundancia y procedimientos documentados de recuperación.

El objetivo es reducir el impacto de la pérdida o corrupción de información.

---

## 10. Comparación de metodologías

### SimpleRisk Classic

El método Classic utilizado en SimpleRisk permite evaluar y priorizar riesgos mediante valores asociados a probabilidad e impacto.

#### Ventajas

- Fácil de comprender.
- Rápido de aplicar.
- Facilita la priorización.
- Adecuado para una evaluación inicial.
- Permite mantener un registro centralizado de riesgos.

#### Desventajas

- Puede simplificar escenarios complejos.
- La asignación de valores depende del criterio del analista.
- Proporciona menor profundidad sobre amenazas y vulnerabilidades específicas.

### NIST SP 800-30

Como alternativa se analizó **NIST SP 800-30**, una guía orientada a la realización de evaluaciones de riesgos sobre sistemas y organizaciones.

El enfoque contempla elementos como:

- Fuentes de amenaza.
- Eventos de amenaza.
- Vulnerabilidades y condiciones predisponentes.
- Probabilidad.
- Impacto.
- Determinación del riesgo.

#### Ventajas

- Mayor profundidad de análisis.
- Permite estudiar cómo puede materializarse una amenaza.
- Resulta adecuado para sistemas y activos críticos.
- Proporciona una estructura formal para la evaluación.

#### Desventajas

- Requiere mayor cantidad de información.
- Su aplicación demanda más tiempo.
- Puede requerir participación de diferentes áreas de la organización.

### Comparación

Para una evaluación inicial de la clínica, SimpleRisk Classic permite identificar y priorizar rápidamente los riesgos.

NIST SP 800-30 sería más apropiado para profundizar posteriormente sobre escenarios críticos, por ejemplo ransomware, compromiso de credenciales o pérdida de información clínica.

Por lo tanto, ambos enfoques pueden utilizarse de manera complementaria: SimpleRisk para el registro, seguimiento y priorización general, y NIST SP 800-30 para evaluaciones detalladas de determinados escenarios.

---

## 11. Integración con herramienta externa

Como posible integración externa se analizó el uso de **Jira** para gestionar las tareas derivadas de los planes de mitigación.

El objetivo sería permitir que un tratamiento definido en SimpleRisk pueda convertirse en una tarea gestionable dentro del flujo de trabajo del equipo técnico.

### Flujo propuesto

1. Se identifica y evalúa un riesgo en SimpleRisk.
2. Se define el tratamiento correspondiente.
3. Se genera una tarea en Jira.
4. La tarea contiene el identificador del riesgo, descripción, responsable y fecha prevista.
5. El equipo técnico ejecuta las acciones necesarias.
6. El estado del tratamiento puede ser actualizado a partir del seguimiento de la tarea.

Por ejemplo, para **R01 — Ransomware**, podrían generarse tareas relacionadas con:

- Implementación de EDR.
- Configuración de MFA.
- Segmentación de red.
- Implementación de backups inmutables.
- Ejecución de pruebas de restauración.

La integración podría realizarse mediante una API o webhook, evitando la necesidad de duplicar manualmente la información entre las herramientas.

En este trabajo se documenta la propuesta de integración; no se almacenan tokens ni credenciales de Jira en el repositorio.

---

## 12. Evidencias

Las capturas de pantalla utilizadas para demostrar la configuración y utilización de SimpleRisk se almacenan en:

`informe/capturas/`

Las evidencias deben mostrar, como mínimo:

- SimpleRisk funcionando.
- Usuarios configurados.
- Riesgo inicial de prueba.
- Registro de riesgos.
- Evaluaciones de riesgos.
- Activos asociados.
- Planes de mitigación.

Antes de incorporar una captura al repositorio se verifica que no muestre contraseñas, tokens, credenciales reales u otra información sensible.

---

## 13. Conclusión

La utilización de SimpleRisk permitió estructurar el proceso de identificación, evaluación y tratamiento de riesgos para el escenario de la clínica.

Los resultados muestran que los riesgos relacionados con ransomware, acceso mediante credenciales comprometidas, pérdida de datos y acceso no autorizado a información clínica requieren especial atención debido al posible impacto sobre la atención de pacientes y sobre la confidencialidad, integridad y disponibilidad de la información.

La gestión de riesgos no debe limitarse a la identificación inicial. Los tratamientos definidos deben ser implementados, supervisados y revisados periódicamente para comprobar que continúan siendo efectivos frente a cambios en las amenazas, los sistemas y la operación de la organización.