# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- **Nombre completo:** Diego Daniel Jofré Winterstetter
- **DNI:** 44538375
- **Email institucional:** djofre@uch.edu.com


> Las evidencias visuales de esta sección se encuentran en el directorio `informe/capturas/`.
*RECOMENDACIÓN: Abrir una pestaña en paralelo para visualizar las capturas.*

> Por seguridad, las credenciales utilizadas durante el trabajo no se almacenan en este repositorio.

---

## Objetivo

El presente trabajo implementa un entorno de SimpleRisk para realizar el análisis y gestión de riesgos de una clínica privada ficticia.

La solución incluye la instalación de SimpleRisk, configuración de usuarios y roles, identificación y evaluación de riesgos, definición de planes de mitigación y documentación del proceso realizado.

---

## Estructura de la entrega

```text
entorno/
    docker-compose.yml

informe/
    informe.md
    capturas/

configuracion/
    usuarios.md
    riesgos.md

scripts/

reporte-ejecutivo/
    reporte.pdf
```

---

## Entorno utilizado

La instalación fue realizada utilizando:

- VirtualBox
- Ubuntu Server 24.04 LTS
- 2 vCPU
- 4 GB de memoria RAM
- Disco virtual de 30 GB
- Docker Engine
- Docker Compose
- SimpleRisk

La máquina virtual utiliza red NAT para mantener el entorno separado del sistema anfitrión.

---

## Instalación y ejecución

### 1. Preparar la máquina virtual

Crear una máquina virtual con Ubuntu Server 24.04 LTS utilizando recursos equivalentes a los indicados anteriormente.

### 2. Instalar Docker

Actualizar los paquetes del sistema e instalar Docker Engine y Docker Compose.

Verificar la instalación mediante:

```bash
docker --version
docker compose version
```

### 3. Levantar SimpleRisk

El archivo reproducible del entorno se encuentra en:

```text
entorno/docker-compose.yml
```

Desde un sistema con Docker instalado, ubicarse en el directorio `entorno/` y ejecutar:

```bash
docker compose up -d
```

El archivo utiliza la imagen:

```text
simplerisk/simplerisk:latest
```

y publica los puertos:

```text
80:80
443:443
```

### 4. Acceso desde el sistema anfitrión

En el entorno utilizado para este trabajo, VirtualBox fue configurado con redirección de puertos debido al uso de NAT:

```text
Host 8081 -> Guest 80
Host 8444 -> Guest 443
```

Por lo tanto, SimpleRisk puede accederse desde el sistema anfitrión mediante:

http://localhost:8081

o mediante HTTPS utilizando el puerto configurado para tal fin.

---

## Decisiones de diseño

### Verificación

girasol

### Virtualización

Se utilizó una máquina virtual para mantener el entorno de laboratorio aislado del sistema operativo anfitrión.

### Contenedores

SimpleRisk se ejecuta mediante Docker, permitiendo disponer de un entorno reproducible y evitando realizar una instalación directa de la aplicación sobre el sistema operativo.

### Gestión de riesgos

Se utiliza el método de evaluación `Classic` disponible en SimpleRisk, basado en la combinación de probabilidad e impacto.

Para el escenario de la clínica se utilizó una escala equivalente de 1 a 5 para ambos valores.

### Supuestos del escenario

La consigna no especifica completamente la infraestructura tecnológica ni los controles existentes de la clínica.

Por este motivo, cuando fue necesario asumir la existencia de algún activo, servicio o control, dicho supuesto se documentó explícitamente y no se presentó como información proporcionada por el escenario.

### Separación de funciones

Se configuraron usuarios con responsabilidades diferenciadas aplicando los principios de mínimo privilegio y separación de funciones.

El detalle se encuentra disponible en:

```text
configuracion/usuarios.md
```

### Seguridad de la información

No se almacenan en el repositorio:

- Contraseñas.
- Tokens.
- API Keys.
- Claves privadas.
- Dumps de bases de datos.
- Archivos de máquinas virtuales.
- Logs que puedan contener información sensible.

El archivo `.gitignore` fue configurado según los requerimientos indicados en la consigna.

---

## Documentación

El desarrollo general del trabajo se encuentra en:

```text
informe/informe.md
```

La configuración de usuarios y roles se encuentra en:

```text
configuracion/usuarios.md
```

El registro detallado de riesgos y planes de mitigación se encuentra en:

```text
configuracion/riesgos.md
```

Las evidencias visuales se encuentran en:

```text
informe/capturas/
```

---

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio.
- [x] El `.gitignore` está correctamente configurado.
- [x] Las capturas no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona.