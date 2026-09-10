### Desarrollo del Trabajo Práctico

*A. Despliegue del Entorno y Resolución Técnica*
El trabajo práctico comenzó con el despliegue local de la plataforma SimpleRisk utilizando contenedores Docker. Durante la configuración inicial y las primeras pruebas, se presentó un error de servidor (HTTP 500) al intentar enviar el formulario de registro de riesgos. Mediante la inspección de las peticiones de red y la consola, se diagnosticó que el fallo derivaba de la configuración del modo estricto de MySQL (ONLY_FULL_GROUP_BY).

Para solucionarlo, fue necesario acceder interactivamente al contenedor de la base de datos (simplerisk-db) mediante la terminal y ejecutar una sentencia SQL para reconfigurar la variable global sql_mode. Tras reiniciar los contenedores, la aplicación funcionó correctamente.

*B. Carga de Riesgos y Planes de Mitigación*
Una vez estabilizado el entorno, se procedió a modelar el escenario de la clínica privada (120 empleados y 800 pacientes diarios). Se identificaron y registraron 7 riesgos específicos, abarcando vulnerabilidades críticas como accesos genéricos a historias clínicas, falta de alta disponibilidad en servidores y escasa concientización del personal ante ataques de ingeniería social.

Posteriormente, utilizando el módulo Plan Mitigation, se diseñaron 3 planes de acción formales para tratar los riesgos de nivel Alto y Crítico. A cada plan se le asignó una estrategia de mitigación, un propietario responsable, un presupuesto estimado y una fecha de vencimiento (RBAC, Alta Disponibilidad/Backups, y Gestión de Parches con EDR).

*Parte C - Análisis Crítico y Profundización*
C.1. Comparación metodológica: SimpleRisk vs. FAIR
¿Qué es SimpleRisk?
SimpleRisk es una plataforma de software orientada a la gestión de riesgos que utiliza un enfoque eminentemente cualitativo. Se basa en una matriz clásica de Probabilidad × Impacto (escala 1-5). No es un estándar normativo en sí mismo, sino una herramienta operativa que facilita el registro, la asignación de puntajes subjetivos y el seguimiento visual mediante una interfaz gráfica.

¿Qué es FAIR (Factor Analysis of Information Risk)?
FAIR es una metodología analítica y un marco de referencia puramente cuantitativo. A diferencia de las escalas de colores, FAIR modela el riesgo basándose en el impacto financiero real y las probabilidades matemáticas. Responde preguntas exactas, como: "¿Cuál es la probabilidad de perder más de $50,000 USD este año debido a una interrupción del servidor?".

*Ventajas y Desventajas*

Ventaja de SimpleRisk: Agilidad y despliegue rápido. Permite evaluar decenas de riesgos en días usando el juicio experto, siendo muy visual para la alta gerencia.

Desventaja de SimpleRisk: Alta subjetividad. Un nivel 4 para IT puede ser un 3 para el área médica. No permite calcular con exactitud el Retorno de Inversión (ROI).

Ventaja de FAIR: Precisión financiera. Expresa el riesgo en términos monetarios exactos, facilitando la justificación de presupuestos.

Desventaja de FAIR: Alta complejidad. Requiere madurez, datos estadísticos históricos y personal altamente capacitado.

¿En qué contexto conviene cada una?
SimpleRisk es ideal para organizaciones que recién comienzan a formalizar su seguridad, como esta clínica de 120 empleados motivada por una auditoría. Permite ordenar la casa con bajo costo. FAIR es necesario en organizaciones con alta madurez (bancos, multinacionales) que deben justificar inversiones millonarias.

C.2. Integración con herramienta externa
Herramienta elegida: Slack (vía Webhooks)
Se seleccionó Slack por ser el estándar actual en comunicación de operaciones de IT (ChatOps). Integrar alertas en la plataforma de trabajo diario asegura visibilidad inmediata, superando a los correos electrónicos que suelen perderse en bandejas saturadas.

*Objetivo y Arquitectura propuesta*
La integración busca automatizar la detección: cuando se registre un riesgo Alto o Crítico, el sistema empuja (push) una alerta en tiempo real al equipo técnico.

Se configura una aplicación interna en Slack habilitando Incoming Webhooks hacia un canal específico (ej. #alertas-seguridad).

Un script en Python consulta periódicamente la API REST de SimpleRisk (GET /api/risks).

Si detecta un nuevo riesgo crítico (nivel 4 o 5), construye un JSON y lo envía mediante HTTP POST al Webhook de Slack.

Consideraciones de Seguridad y Valor aportado
La URL del Webhook debe tratarse como una credencial crítica para evitar inyección de mensajes falsos. Esta integración transforma la gestión de riesgos de reactiva a dinámica, reduciendo el Tiempo Medio de Respuesta (MTTR) del equipo frente a nuevos hallazgos.