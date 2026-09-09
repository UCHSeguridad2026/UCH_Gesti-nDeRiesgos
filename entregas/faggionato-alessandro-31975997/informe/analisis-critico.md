# Análisis crítico y profundización

## 1. Comparación metodológica: SimpleRisk Classic y NIST SP 800-30 Rev. 1

La evaluación cargada en SimpleRisk utiliza el método **Classic**, una matriz cualitativa donde el nivel inicial de riesgo se obtiene multiplicando probabilidad por impacto. Para la clínica se empleó una escala de 1 a 5, con cuatro niveles: bajo, medio, alto y crítico.

Como metodología alternativa se seleccionó **NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments**. NIST organiza la evaluación en tres momentos: preparar la evaluación, conducirla y mantener sus resultados. Al conducirla, propone identificar fuentes y eventos de amenaza, vulnerabilidades o condiciones predisponentes, probabilidad, impacto y nivel de riesgo.

| Aspecto | SimpleRisk Classic | NIST SP 800-30 Rev. 1 |
|---|---|---|
| Enfoque | Matriz cualitativa de probabilidad × impacto. | Proceso estructurado de preparación, evaluación y mantenimiento. |
| Facilidad de uso | Alta: permite registrar y priorizar riesgos rápidamente. | Media: exige más análisis, evidencia y definición de supuestos. |
| Amenazas y vulnerabilidades | Pueden documentarse en la descripción del riesgo. | Son elementos explícitos del análisis. |
| Repetibilidad | Depende de que cada evaluador justifique consistentemente la escala. | Favorece una evaluación más trazable mediante tareas y criterios definidos. |
| Mejor contexto de uso | Registro inicial, priorización operativa y seguimiento cotidiano. | Evaluaciones profundas de sistemas críticos, auditorías y cambios relevantes. |

### Ventajas y limitaciones

La principal ventaja de SimpleRisk para esta clínica es la rapidez: permite centralizar los ocho registros, asignar propietarios, planificar mitigaciones y mostrar prioridades al directorio sin requerir una estimación cuantitativa compleja. También facilita mantener evidencia del ciclo de vida de cada riesgo.

Su limitación es que dos evaluadores pueden interpretar de forma diferente expresiones como “probable” o “mayor”. Por ello, una matriz por sí sola no prueba por qué un valor es correcto. En este trabajo se compensó esa limitación incluyendo una justificación explícita, activos afectados, controles asumidos y tratamiento propuesto para cada riesgo.

NIST SP 800-30 aporta más profundidad al exigir que se analicen las fuentes de amenaza, vulnerabilidades, impacto y condiciones del contexto. Su desventaja es el mayor esfuerzo: requiere entrevistas, evidencia técnica, inventario de activos y revisiones periódicas, recursos que una clínica de 120 empleados podría no tener disponibles para todos sus riesgos.

### Aplicación propuesta

La clínica debería usar SimpleRisk Classic para el registro inicial y las revisiones mensuales de los riesgos operativos. Para riesgos críticos —por ejemplo ransomware, fuga de historias clínicas o cambios de proveedor de salud digital— debería complementar el registro con una evaluación NIST SP 800-30. De ese modo combina velocidad de gestión con un análisis más defendible cuando el impacto sobre pacientes, disponibilidad o datos sensibles es mayor.

## 2. Integración propuesta: SimpleRisk con Jira

Se propone integrar SimpleRisk con Jira para convertir los planes de mitigación en tareas técnicas trazables. El objetivo es evitar que una mitigación registrada en la herramienta de riesgos quede sin ejecución operativa.

### Flujo propuesto

1. Se registra o actualiza en SimpleRisk un riesgo alto o crítico.
2. La integración crea una incidencia de Jira en el proyecto `SEGURIDAD`.
3. La incidencia incluye el ID del riesgo, asunto, puntaje, propietario, fecha objetivo y enlace al registro de SimpleRisk.
4. El equipo de TI actualiza el avance de la tarea en Jira.
5. Cuando la tarea se completa, un webhook o sincronización actualiza el estado de la mitigación en SimpleRisk para revisión del responsable.
6. La aceptación del riesgo residual permanece como una decisión humana; no debe automatizarse.

### Mapeo mínimo de datos

| SimpleRisk | Jira |
|---|---|
| ID y asunto del riesgo | Summary y clave de referencia |
| Descripción y evaluación | Description |
| Nivel de riesgo | Priority / etiqueta `riesgo-alto` o `riesgo-critico` |
| Propietario | Assignee |
| Plan de mitigación | Issue type: Task o Security Remediation |
| Fecha objetivo | Due date |
| Estado de mitigación | Estado del issue y comentario de sincronización |

### Seguridad de la integración

- Crear una cuenta técnica exclusiva para la integración, sin reutilizar una cuenta administradora personal.
- Otorgar el mínimo privilegio necesario tanto en Jira como en SimpleRisk.
- Conservar API keys, tokens y secretos en un gestor de secretos o variables de entorno fuera del repositorio.
- Usar HTTPS y validar el token de autenticación del webhook.
- No enviar contraseñas, historias clínicas ni datos personales de pacientes a Jira; solo identificadores del riesgo y datos de tratamiento.
- Registrar errores y eventos de sincronización sin guardar el contenido sensible completo de los riesgos.

### Factibilidad

SimpleRisk dispone de un Jira Extra que sincroniza riesgos con Jira mediante API REST y webhooks. La integración no se implementó en el entorno de práctica porque requiere una instancia de Jira, una cuenta de servicio y tokens externos; se documenta el diseño y los controles necesarios para una implementación futura.

## Referencias

- National Institute of Standards and Technology. [NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- SimpleRisk. [The Jira Extra](https://support.simplerisk.com/kb/07-01-the-jira-extra).
- SimpleRisk. [Using the API for Integrations](https://support.simplerisk.com/kb/07-04-using-the-api-for-integrations).
