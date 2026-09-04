# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## 1. Introducción

El trabajo desarrolla una evaluación inicial de riesgos de seguridad sobre el escenario de una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes diariamente.

La organización procesa historias clínicas digitales, información personal, datos de obras sociales, turnos y procesos administrativos mediante sistemas informáticos.

Para administrar el registro se utilizó SimpleRisk dentro de un entorno Linux virtualizado. El trabajo incluyó la configuración de la plataforma, definición de perfiles con responsabilidades diferentes, identificación y evaluación de riesgos y planificación de medidas de tratamiento.

---

# 2. Parte A - Preparación y configuración de SimpleRisk

## 2.1 Entorno

La herramienta fue desplegada sobre Ubuntu ejecutado mediante Oracle VirtualBox.

Dentro de la máquina virtual se utilizó Docker y Docker Compose para ejecutar SimpleRisk. La configuración se almacenó dentro de entorno/docker-compose.yml, permitiendo reproducir el despliegue.

La aplicación quedó disponible localmente mediante los puertos 8080 para HTTP y 8443 para HTTPS.

El funcionamiento se comprobó accediendo a la interfaz web y verificando el estado del contenedor.

## 2.2 Usuarios

Se crearon tres perfiles diferenciados.

### Responsable de Seguridad

Cuenta administrativa utilizada para la configuración y supervisión general de la plataforma.

### Valentina Ríos - Analista de Riesgos

Dispone de permisos operativos para registrar y modificar riesgos, trabajar sobre mitigaciones, realizar revisiones y agregar comentarios.

### Tomás Herrera - Auditor

Cuenta con permisos orientados a la revisión y auditoría. No dispone de privilegios para administrar la plataforma ni modificar el registro de riesgos.

Los permisos detallados se encuentran documentados en configuracion/usuarios.md. Las contraseñas no forman parte del repositorio.

## 2.3 Validación inicial

Antes de comenzar el análisis definitivo se registró un riesgo de prueba relacionado con una interrupción del sistema de turnos.

La prueba permitió validar la creación y almacenamiento de riesgos dentro de SimpleRisk.

---

# 3. Parte B - Evaluación de riesgos

## 3.1 Metodología de valoración

La probabilidad y el impacto fueron valorados de 1 a 5.

El valor académico se calculó mediante:

Valor = Probabilidad × Impacto

Los niveles utilizados fueron:

- Bajo: 1 a 4.
- Medio: 5 a 9.
- Alto: 10 a 15.
- Crítico: 16 a 25.

Durante la utilización de SimpleRisk se observó que el método Classic aplica una normalización a una escala de 10. Por este motivo, el valor mostrado por la herramienta no necesariamente coincide numéricamente con el resultado directo de la matriz 5x5.

Para la documentación académica se conservó la escala establecida por la cátedra.

## 3.2 Riesgos identificados

| ID | Riesgo | Prob. | Impacto | Valor | Nivel |
|---|---|---:|---:|---:|---|
| R01 | Compromiso de credenciales del personal médico | 4 | 5 | 20 | Crítico |
| R02 | Propagación de malware desde equipos administrativos | 4 | 5 | 20 | Crítico |
| R03 | Caída de infraestructura que soporta la atención de pacientes | 3 | 5 | 15 | Alto |
| R04 | Modificación accidental de datos médicos por permisos excesivos | 3 | 5 | 15 | Alto |
| R05 | Envío accidental de información sensible a terceros no autorizados | 3 | 4 | 12 | Alto |
| R06 | Imposibilidad de restaurar información luego de una falla crítica | 2 | 5 | 10 | Alto |
| R07 | Falla de integración con sistemas de obras sociales | 3 | 3 | 9 | Medio |

Se obtuvieron dos riesgos críticos, cuatro altos y uno medio.

El detalle de cada escenario, sus activos, controles, justificaciones y tratamientos se encuentra en configuracion/riesgos.md.

## 3.3 Planes de acción

### Programa de protección de identidades clínicas

Riesgo asociado: Compromiso de credenciales del personal médico.

Responsable: Valentina Ríos.

Vencimiento: 20/10/2026.

Presupuesto estimado: USD 3.200.

Estado: No iniciado (0%).

El plan contempla MFA, revisión de privilegios, fortalecimiento de políticas de autenticación y monitoreo de accesos sospechosos.

### Fortalecimiento de endpoints y segmentación de red

Riesgo asociado: Propagación de malware desde equipos administrativos.

Responsable: Responsable de Seguridad.

Vencimiento: 05/11/2026.

Presupuesto estimado: USD 7.500.

Estado: No iniciado (0%).

Se propone desplegar mecanismos EDR, segmentar la red para reducir movimientos laterales, reforzar el filtrado de correo y restringir privilegios innecesarios.

### Plan de alta disponibilidad para servicios asistenciales

Riesgo asociado: Caída de infraestructura que soporta la atención de pacientes.

Responsable: Valentina Ríos.

Vencimiento: 05/12/2026.

Presupuesto estimado: USD
