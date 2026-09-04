# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- Nombre completo: Rocío SAntilli
- LU: 32352653
- Email institucional: santillirocio@uch.edu.ar
- Comisión: 1
- Materia: Seguridad de Sistemas

## Descripción

El trabajo desarrolla la implementación y utilización de SimpleRisk para realizar una evaluación inicial de riesgos de seguridad sobre el escenario de una clínica privada.

La organización analizada cuenta con 120 empleados, atiende aproximadamente 800 pacientes por día y utiliza sistemas informáticos para gestionar historias clínicas, turnos, información de obras sociales y procesos administrativos.

La herramienta se ejecutó sobre Ubuntu 20.04 mediante Docker, utilizando Oracle VirtualBox para disponer del entorno Linux solicitado.

## Estructura de la entrega

- `entorno/`: archivos necesarios para ejecutar SimpleRisk.
- `configuracion/`: documentación de usuarios y riesgos.
- `informe/`: desarrollo del trabajo y evidencias.
- `scripts/`: espacio destinado a posibles automatizaciones.
- `reporte-ejecutivo/`: reporte ejecutivo del análisis.

## Requisitos para reproducir el entorno

Se requiere:

- Sistema operativo Linux.
- Docker.
- Docker Compose.
- Conexión a Internet para obtener la imagen de SimpleRisk.

El entorno utilizado para el desarrollo fue Ubuntu 20.04 ejecutado mediante Oracle VirtualBox.

## Instrucciones para levantar el entorno

1. Clonar el repositorio.

2. Cambiar a la branch correspondiente:

   `git switch entrega/[APELLIDO]-[NOMBRE]-[LU]`

3. Ingresar a la carpeta del entorno:

   `cd entregas/[CARPETA-DE-LA-ENTREGA]/entorno`

4. Levantar SimpleRisk:

   `sudo docker-compose up -d`

5. Verificar el estado:

   `sudo docker-compose ps`

6. Acceder desde el navegador mediante:

   `http://localhost:8080`

   o

   `https://localhost:8443`

7. Para detener el entorno:

   `sudo docker-compose down`

## Decisiones de diseño

### Entorno virtualizado

Se utilizó Ubuntu mediante VirtualBox para trabajar en un entorno Linux independiente del sistema operativo Windows del equipo principal.

### Despliegue

SimpleRisk fue desplegado mediante Docker Compose. Esta alternativa permite simplificar la instalación y facilita la reproducción del entorno a partir del archivo `docker-compose.yml`.

### Evaluación de riesgos

La valoración se realizó mediante una matriz de probabilidad e impacto de 1 a 5.

Los niveles utilizados fueron:

- Bajo: 1 a 4.
- Medio: 5 a 9.
- Alto: 10 a 15.
- Crítico: 16 a 25.

Durante las pruebas se observó que SimpleRisk normaliza los resultados del método Classic a una escala diferente. Por este motivo, para la documentación académica se conservaron los valores obtenidos mediante la matriz 5x5 establecida para el trabajo.

### Escenario

El análisis se concentró en riesgos vinculados con el compromiso de credenciales, propagación de malware, disponibilidad de infraestructura, integridad de información clínica y exposición accidental de datos sensibles.

### Seguridad

Las cuentas utilizadas durante las pruebas contienen información ficticia.

No se incorporan contraseñas, tokens, claves privadas ni otras credenciales al repositorio.

## Verificación

Palabra clave de verificación de lectura de la consigna: girasol.

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] Mi branch está actualizada y funciona correctamente.
