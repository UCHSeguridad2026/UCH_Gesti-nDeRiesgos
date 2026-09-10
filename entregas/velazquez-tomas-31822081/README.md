# Trabajo Práctico — Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- **Nombre completo:** Tomás Velazquez
- **LU:** 31822081
- **Email:** tomiveltorres@gmail.com
- **Comisión:** 4G

## Descripción y objetivo

Este trabajo presenta el análisis y tratamiento inicial de riesgos de seguridad de la información para una clínica privada ficticia de 120 empleados. La clínica atiende aproximadamente 800 pacientes por día y utiliza historias clínicas digitales, información de obras sociales y sistemas de facturación.

El objetivo es identificar riesgos realistas para la operación de la clínica, evaluarlos de manera consistente y proponer acciones de tratamiento fundamentadas.

Se utiliza SimpleRisk para registrar, evaluar y gestionar los riesgos identificados.

## Cómo levantar el entorno

El entorno utiliza Docker para ejecutar SimpleRisk.

### Requisitos previos

- Docker Desktop instalado y en ejecución.
- WSL 2 habilitado.
- Navegador web.

### Ejecución mediante Docker

1. Abrir Docker Desktop y esperar a que se encuentre en ejecución.

2. Verificar que Docker funcione correctamente:

```powershell
docker --version
```

3. Descargar la imagen de SimpleRisk:

```powershell
docker pull simplerisk/simplerisk
```

4. Crear e iniciar el contenedor:

```powershell
docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk
```

5. Verificar que el contenedor esté funcionando:

```powershell
docker ps
```

6. Abrir en el navegador:

```text
https://localhost/
```

El certificado utilizado en este entorno local es autofirmado, por lo que el navegador puede mostrar una advertencia de seguridad.

### Ejecución mediante Docker Compose

También se incluye el archivo:

```text
entorno/docker-compose.yml
```

Desde la carpeta `entorno/`, el servicio puede iniciarse mediante:

```powershell
docker compose up -d
```

Para verificar su estado:

```powershell
docker compose ps
```

Para detenerlo:

```powershell
docker compose down
```

Si ya existe un contenedor llamado `simplerisk` utilizando los puertos 80 y 443, debe detenerse antes de levantar otra instancia mediante Docker Compose.

## Metodología y decisiones de diseño

- Se utilizó SimpleRisk con el método de puntuación **Classic**.
- Para documentar y justificar los riesgos también se utilizó una valoración académica de probabilidad e impacto en escala de 1 a 5.
- La valoración académica se calcula como **Probabilidad × Impacto**.
- La valoración académica se mantiene separada de la puntuación interna mostrada por SimpleRisk, ya que el método Classic puede presentar valores diferentes.
- Se identificaron siete riesgos específicos relacionados con el escenario de la clínica.
- Se consideró al **Sistema de Historias Clínicas Digitales** como uno de los activos principales del análisis.
- Se definieron tratamientos de mitigación para los riesgos prioritarios.
- Se configuraron usuarios con responsabilidades diferenciadas para administración, análisis de riesgos y auditoría.
- Se trabajó exclusivamente en la branch `entrega/velazquez-tomas-31822081`.

### Escala académica utilizada

| Valor | Nivel |
|---|---|
| 1 - 4 | Bajo |
| 5 - 9 | Medio |
| 10 - 16 | Alto |
| 17 - 25 | Crítico |

### Supuestos del escenario

- La clínica depende de los sistemas informáticos para su operación diaria.
- Las historias clínicas digitales constituyen información crítica y sensible.
- Una indisponibilidad prolongada puede afectar la atención de pacientes.
- Existen usuarios con diferentes niveles de acceso a los sistemas.
- La clínica depende de proveedores tecnológicos externos.
- La pérdida, modificación o divulgación de información clínica puede producir consecuencias operativas, legales, económicas y reputacionales.

## Decisiones de seguridad

- Se utilizaron datos de demostración y no se almacenaron contraseñas reales en el repositorio.
- Los secretos, archivos de entorno, claves, respaldos y dumps de bases de datos se excluyen mediante `.gitignore`.
- Las capturas fueron revisadas antes de incorporarlas para evitar exponer contraseñas, tokens, direcciones IP reales o datos personales.
- No se incluyen credenciales de SimpleRisk dentro de la documentación.
-**girasol**.


## Checklist de seguridad y entrega

- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona correctamente.