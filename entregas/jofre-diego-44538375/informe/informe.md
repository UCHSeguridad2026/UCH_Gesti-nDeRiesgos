# Informe del Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## Parte A - Instalación y configuración básica

### 1. Preparación del entorno

> Las evidencias visuales de esta sección se encuentran en el directorio `informe/capturas/`.
*RECOMENDACIÓN: Abrir una pestaña en paralelo para visualizar las cpturas.*

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

Se crearon usuarios con roles diferenciados para validar la separación de responsabilidades dentro de la herramienta.

El detalle de usuarios, roles y permisos se encuentra documentado en:

`configuracion/usuarios.md`


### 6. Riesgo de prueba

Se creó un riesgo de prueba para validar el funcionamiento del flujo de alta, evaluación y asignación de riesgos en SimpleRisk.

Este riesgo fue utilizado únicamente como prueba funcional de la herramienta, por lo que los valores de probabilidad e impacto seleccionados no representan una valoración real del riesgo para la clínica.

El detalle se encuentra documentado en:

`configuracion/riesgos.md`

### 7. Riesgos del escenario y planes de acción

Se definieron y cargaron en SimpleRisk siete riesgos específicos del escenario de la clínica, contemplando aspectos de confidencialidad, integridad, disponibilidad, continuidad operativa y dependencia de terceros.

Para cada riesgo se documentaron los activos afectados, la probabilidad e impacto, su justificación, el nivel resultante, los controles existentes, el tratamiento propuesto y el propietario correspondiente.

Además, se definieron tres planes de acción asociados a riesgos de nivel alto o muy alto:

- Protección contra ransomware.
- Fortalecimiento de autenticación y prevención de phishing.
- Fortalecimiento de la estrategia de backups.

El detalle completo de los riesgos, sus evaluaciones, tratamientos, planes de acción y evidencias se encuentra en:

`configuracion/riesgos.md`