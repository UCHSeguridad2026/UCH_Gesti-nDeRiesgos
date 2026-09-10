# Informe - Trabajo Practico Gestion de Riesgos con SimpleRisk

## Escenario

Clinica privada de 120 empleados que atiende aproximadamente 800 pacientes por dia. Maneja historias clinicas digitales, datos de obras sociales y facturacion. La clinica sufrio recientemente una auditoria externa que identifico debilidades en su gestion de riesgos.

## Riesgos identificados

Se identificaron 7 riesgos especificos del contexto de la clinica. El detalle completo (probabilidad, impacto, nivel, tratamiento y propietario) se encuentra documentado en `configuracion/riesgos.md`.

## Planes de accion

Se definieron 3 planes de mitigacion para los riesgos de mayor nivel:

### Plan 1 - Ransomware en servidores de facturacion (R02, Critico)
- Fecha planificada: 15/11/2026
- Esfuerzo: Significant
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: backups offline inmutables, segmentacion de red, solucion EDR

### Plan 2 - Acceso no autorizado a historias clinicas digitales (R01, Alto)
- Fecha planificada: 30/10/2026
- Esfuerzo: Considerable
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: control de acceso basado en roles (RBAC), logs de auditoria, revision periodica de permisos

### Plan 3 - Phishing dirigido al personal administrativo (R04, Alto)
- Fecha planificada: 15/10/2026
- Esfuerzo: Minor
- Presupuesto: $0 a $100.000
- Responsable: Gaston Alvarez
- Requisitos de seguridad: autenticacion multifactor (MFA), filtrado anti-phishing, capacitacion periodica al personal
## Analisis critico: SimpleRisk vs NIST SP 800-30

### Enfoque de SimpleRisk

SimpleRisk utiliza una matriz clasica de probabilidad x impacto (metodologia cualitativa/semi-cuantitativa de 5x5), donde cada riesgo recibe un puntaje numerico simple resultante de multiplicar ambos valores. Es rapida de aplicar, visual y facil de entender para audiencias no tecnicas, pero depende fuertemente del criterio subjetivo de quien evalua cada riesgo.

### Enfoque de NIST SP 800-30

La guia NIST SP 800-30 (Guide for Conducting Risk Assessments) propone un proceso mas estructurado y documentado, que incluye:
- Identificacion explicita de fuentes de amenaza (adversarial, accidental, estructural, ambiental) y su capacidad, intencion y probabilidad de exito.
- Analisis de vulnerabilidades asociadas a cada activo, con severidad asignada por separado.
- Calculo de probabilidad como una combinacion de probabilidad de inicio de la amenaza y probabilidad de exito dado el inicio.
- Documentacion extensa de supuestos e incertidumbre en cada estimacion.

### Ventajas y desventajas

**SimpleRisk (matriz clasica):**
- Ventaja: rapidez de implementacion, curva de aprendizaje baja, ideal para organizaciones pequenas o medianas sin equipo dedicado de riesgos (como el caso de la clinica de este TP).
- Desventaja: simplifica demasiado el analisis, puede subestimar riesgos compuestos (por ejemplo, cuando una amenaza depende de multiples vulnerabilidades encadenadas) y la escala 1-5 puede generar falsa precision.

**NIST SP 800-30:**
- Ventaja: mayor rigor metodologico, mejor trazabilidad de las decisiones y supuestos, mas adecuado para auditorias externas o sectores altamente regulados (como salud o finanzas).
- Desventaja: requiere mas tiempo, mas capacitacion del equipo y mas documentacion, lo que puede ser excesivo para una organizacion chica con recursos limitados.

### En que contexto conviene cada una

Para una clinica de 120 empleados como la del escenario de este TP, el enfoque de SimpleRisk resulta razonable como punto de partida, dado el tamano de la organizacion y la necesidad de resultados rapidos y comunicables al directorio. Sin embargo, dado que la clinica maneja datos de salud (altamente sensibles y regulados), a mediano plazo seria recomendable migrar hacia un proceso mas alineado con NIST SP 800-30, especialmente para los riesgos clasificados como criticos o altos (R01, R02, R04), donde una mejor trazabilidad de los supuestos podria ser exigida en una auditoria de cumplimiento normativo.

## Integracion con herramienta externa

Se investigo la integracion de SimpleRisk con **Slack**, mediante el envio de notificaciones automaticas mediante webhooks cuando se crea un riesgo de nivel alto o critico.

SimpleRisk permite configurar notificaciones por correo electronico de forma nativa, y estas pueden redirigirse a un canal de Slack mediante la funcionalidad de "Email to Slack" (cada canal de Slack puede generar una direccion de correo unica a la que reenviar notificaciones). De esta forma, cuando SimpleRisk envia un correo de alerta por un riesgo critico, ese mismo correo llega automaticamente al canal de seguridad del equipo de TI, sin necesidad de desarrollar una integracion a medida.

Una alternativa mas robusta, no implementada en este TP por falta de tiempo, seria un script que consulte la API de SimpleRisk periodicamente y publique en Slack mediante un webhook nativo los riesgos que superen un umbral de puntaje definido.

## Actividad optativa D1: Analisis de seguridad de la instalacion por defecto

Se realizaron tres verificaciones sobre la instalacion por defecto de SimpleRisk (imagen oficial `simplerisk/simplerisk:latest` sobre Docker):

### Hallazgo 1: Content-Security-Policy permisiva

El header CSP devuelto por el servidor es `default-src * 'unsafe-inline' 'unsafe-eval' data:`. Esta configuracion permite cargar recursos desde cualquier origen y ejecutar scripts inline y `eval()`, anulando practicamente el proposito de la CSP como mitigacion contra ataques XSS. Se detecto ademas una inconsistencia: el header `Referrer-Policy` aparece duplicado con dos valores distintos (`no-referrer-when-downgrade` y `origin`), lo que sugiere una configuracion de servidor descuidada o superpuesta entre distintas capas (aplicacion + servidor web).

**Mitigacion propuesta:** restringir la CSP a los origenes especificos que realmente necesita la aplicacion (scripts propios, CDN si corresponde) y eliminar `unsafe-inline` y `unsafe-eval`. Unificar la configuracion de `Referrer-Policy` en un unico valor explicito, por ejemplo `strict-origin-when-cross-origin`.

### Hallazgo 2: Version de PHP

Se verifico la version de PHP en ejecucion dentro del contenedor: PHP 8.3.6. Es una version reciente y sin vulnerabilidades criticas conocidas al momento de este analisis, por lo que no representa un riesgo inmediato, aunque se recomienda mantener un proceso de actualizacion periodica de la imagen base.

### Hallazgo 3: Proceso ejecutado como root

Se verifico el usuario bajo el cual corre el proceso principal del contenedor (`docker exec simplerisk_app whoami`), resultando en `root`. Ejecutar la aplicacion web como usuario con privilegios administrativos dentro del contenedor viola el principio de minimo privilegio: ante una vulnerabilidad de ejecucion remota de codigo en la aplicacion, un atacante obtendria control total del contenedor en lugar de estar limitado a los permisos de un usuario sin privilegios.

**Mitigacion propuesta:** modificar el Dockerfile o `docker-compose.yml` para ejecutar el proceso de Apache/PHP con un usuario dedicado sin privilegios (por ejemplo `www-data`), y aplicar `USER` en el Dockerfile antes del `ENTRYPOINT`.