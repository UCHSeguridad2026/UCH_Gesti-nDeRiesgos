# Trabajo Práctico - Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- Nombre completo: Lucrecia Concatti
- LU: 31302010
- Email institucional: concattilucrecia@uch.edu.ar
- Comisión: 1
- Materia: Seguridad de Sistemas

## Descripción

El presente trabajo implementa un entorno de gestión de riesgos utilizando SimpleRisk sobre Linux.

El escenario analizado corresponde a una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día y administra historias clínicas digitales, información de obras sociales y procesos de facturación.

SimpleRisk se ejecuta mediante Docker dentro de una máquina virtual Ubuntu 20.04 alojada en Oracle VirtualBox.

## Estructura de la entrega

- `entorno/`: configuración necesaria para ejecutar SimpleRisk.
- `configuracion/`: documentación de usuarios y riesgos.
- `informe/`: desarrollo del trabajo y capturas de evidencia.
- `scripts/`: reservado para posibles automatizaciones.
- `reporte-ejecutivo/`: reporte ejecutivo dirigido a la gerencia.

## Requisitos para reproducir el entorno

Se requiere:

- Sistema Linux.
- Docker.
- Docker Compose.
- Conexión a Internet para descargar la imagen de SimpleRisk.

El entorno utilizado durante el desarrollo fue Ubuntu 20.04 ejecutado mediante Oracle VirtualBox.

## Instrucciones para levantar el entorno

1. Clonar el repositorio.

2. Cambiar a la branch correspondiente a la entrega:

   `git switch entrega/concatti-lucrecia-31302010`

3. Ingresar al directorio del entorno:

   `cd entregas/concatti-lucrecia-31302010/entorno`

4. Levantar SimpleRisk:

   `sudo docker-compose up -d`

5. Verificar el estado del contenedor:

   `sudo docker-compose ps`

6. Acceder desde el navegador a:

   `http://localhost:8080`

   o

   `https://localhost:8443`

7. Para detener el entorno:

   `sudo docker-compose down`

## Decisiones de diseño

### Virtualización

Se utilizó Ubuntu dentro de VirtualBox para disponer de un entorno Linux independiente del sistema operativo Windows utilizado como host.

### Contenedores

Se utilizó Docker Compose para simplificar el despliegue y permitir que el entorno pueda reproducirse utilizando el archivo de configuración incluido en el repositorio.

### Metodología de riesgos

Los riesgos fueron valorados mediante una matriz de probabilidad e impacto de 1 a 5.

La clasificación académica utilizada fue:

- Bajo: 1 a 4.
- Medio: 5 a 9.
- Alto: 10 a 15.
- Crítico: 16 a 25.

SimpleRisk utiliza una normalización propia para mostrar el resultado del método Classic. Por este motivo, los valores visualizados en la aplicación pueden diferir del valor directo obtenido mediante Probabilidad × Impacto.

### Escenario

Se consideró una clínica privada de 120 empleados y aproximadamente 800 pacientes diarios, con dependencia de sistemas digitales para historias clínicas, turnos, facturación y gestión de información de obras sociales.

### Seguridad

No se almacenan contraseñas, tokens ni credenciales reales dentro del repositorio.

Los usuarios y datos utilizados en SimpleRisk son ficticios y fueron creados exclusivamente para el desarrollo académico.

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
