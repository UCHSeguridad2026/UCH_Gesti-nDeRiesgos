# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

## Datos del estudiante

| | |
|---|---|
| **Nombre completo** | Enrique Pizarro |
| **LU** | 31130908 |
| **Email institucional** | pizarroenrique@uch.edu.ar |
| **Comisión** | Tarde-G |
| **Materia** | Seguridad Aplicada a Sistemas de Información |
| **Branch** | `entrega/pizarro-enrique-31130908` |

## Contenido de la entrega

    entregas/pizarro-enrique-31130908/
    |-- README.md                        # este archivo
    |-- .gitignore
    |-- entorno/
    |   |-- README.md                    # instalación detallada y decisiones
    |   '-- docker-compose.yml
    |-- informe/
    |   |-- informe.md                   # desarrollo completo del TP
    |   '-- capturas/                    # evidencias
    |-- configuracion/
    |   |-- usuarios.md                  # usuarios, roles y permisos
    |   '-- riesgos.md                   # análisis de riesgos completo
    |-- scripts/
    |   |-- notificar_riesgos_altos.sh   # integración con Discord
    |   '-- .env.example                 # plantilla de configuración
    '-- reporte-ejecutivo/
        '-- reporte.pdf                  # informe para el directorio

## Cómo levantar el entorno

### Requisitos

- Docker Engine
- Docker Compose (plugin v2)

Verificación:

    docker --version
    docker compose version

### Paso 1: levantar el contenedor

Desde la carpeta `entorno/` de esta entrega:

    docker compose up -d

La primera ejecución descarga la imagen `simplerisk/simplerisk` desde Docker Hub y
puede demorar varios minutos.

Verificar que el contenedor está corriendo:

    docker compose ps

### Paso 2: acceder a la aplicación

Ingresar desde el navegador a:

    https://localhost:8443

El navegador mostrará una advertencia de certificado no confiable. Es esperable:
la imagen incluye un certificado autofirmado. Aceptar la excepción para continuar.

### Paso 3: crear la cuenta administrativa

El primer acceso redirige automáticamente a la pantalla *Default Admin Account
Creation*. Allí se define el usuario administrador inicial.

Los usuarios utilizados durante el desarrollo del trabajo están documentados en
`configuracion/usuarios.md`. **Las contraseñas no se incluyen en este
repositorio**, por lo que el entorno se levanta con credenciales nuevas.

### Paso 4: reproducir la configuración

Para replicar el estado del trabajo:

1. Crear las tres cuentas descritas en `configuracion/usuarios.md`, asignando los
   permisos allí detallados mediante la sección *User Responsibilities*.
2. Cargar los riesgos R01 a R10 según las valoraciones de
   `configuracion/riesgos.md`, utilizando el método de scoring *Classic*.
3. Definir los tres planes de mitigación descritos en el punto B.4 del informe.

### Detener y reiniciar el entorno

    docker compose stop     # detiene sin perder datos
    docker compose start    # reinicia

**No utilizar `docker compose down`**: elimina el contenedor y, al no haberse
definido un volumen persistente, se pierden los usuarios y riesgos cargados.

### Opcional: integración con Discord

Para ejecutar el script de notificación descrito en el punto C.2 del informe:

    cd scripts/
    cp .env.example .env
    # completar .env con la URL del webhook y la contraseña de la base
    chmod +x notificar_riesgos_altos.sh
    ./notificar_riesgos_altos.sh

## Decisiones de diseño

**Metodología de riesgos.** Se aplicó la matriz de probabilidad × impacto
propuesta por la Plantilla de Matriz de Riesgos de la cátedra, con escalas de 1 a
5 y rangos de nivel Bajo (1-4), Medio (5-9), Alto (10-15) y Crítico (16-25). Se
optó por realizar el análisis completo antes de cargarlo en SimpleRisk, de modo
que las decisiones respondieran al contexto de la organización y no a las
restricciones del formulario de la herramienta.

**Supuestos del escenario.** El enunciado define una clínica de 120 empleados que
atiende 800 pacientes diarios y que proviene de una auditoría externa con
hallazgos. A partir de ese marco se asumió que la organización no cuenta con área
de seguridad constituida ni con un programa formal de gestión de riesgos, lo que
fundamenta que la mayoría de los riesgos identificados carezca de controles
existentes.

**Cantidad de riesgos.** Se identificaron diez riesgos en lugar de los siete
mínimos requeridos, con el fin de cubrir las cinco categorías sugeridas
—confidencialidad, integridad, disponibilidad, legal y operativo— y los tres
orígenes de exposición detectados: factor humano, amenaza externa deliberada e
incumplimiento normativo.

**Imagen Docker.** Se utilizó la imagen all-in-one `simplerisk/simplerisk` en
lugar de `simplerisk-minimal` con base de datos externa, priorizando la
reproducibilidad del entorno con un único comando. El detalle de esta y otras
decisiones de infraestructura se encuentra en `entorno/README.md`.

**Esquema de permisos.** Las tres cuentas se configuraron con permisos
individuales en lugar del rol *Administrator* predefinido, aplicando segregación
de funciones entre quien analiza, quien aprueba y quien controla. La
justificación completa está en `configuracion/usuarios.md`.

**Doble clasificación de categorías.** Las categorías disponibles en SimpleRisk
responden a dominios de control operativo y no a las propiedades de seguridad de
la información. Se mantuvieron ambas clasificaciones en lugar de modificar la
taxonomía de la herramienta. El fundamento está en el punto B.3 del informe.

## Verificación

girasol

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio
- [x] El `.gitignore` está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos `.sql` o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona
