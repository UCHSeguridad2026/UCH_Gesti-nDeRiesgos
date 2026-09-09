DATOS DEL ALUMNO
Nombre del alumno: Juan Maure - 31017414 - juanmaure123@outlook.com
Comision: G

Instrucciones para levantar el entorno

A continuación, se detallan los pasos exactos para levantar la infraestructura de SimpleRisk y su base de datos MySQL asociada de manera local, utilizando Docker Compose.

1. Requisitos Previos
* Tener instalado **Docker Desktop** (con WSL 2 habilitado en caso de usar Windows) y asegurarse de que el motor se encuentre en ejecución.
* Abrir una terminal y posicionarse dentro del directorio del proyecto (carpeta `entorno`), donde deben coexistir los archivos `docker-compose.yml` y `.env`.

2. Configuración Inicial
El proyecto incluye un archivo `.env` preconfigurado con las variables de entorno necesarias para la conexión de la base de datos y la aplicación. No es necesario realizar modificaciones adicionales en este archivo para evaluar el entorno.

3. Ejecución y Despliegue
Para crear la red, descargar las imágenes e iniciar los contenedores en segundo plano, ejecute el siguiente comando en la terminal:

```bash
cd entorno/
docker compose up -d
```
4. Tiempo de Inicialización
Una vez enviado el comando, es necesario esperar entre 30 y 45 segundos. Durante este lapso, el contenedor de la base de datos realizará su configuración inicial y creará las tablas internas.
Para comprobar que los contenedores están corriendo correctamente, ejecute:

```bash
docker compose ps 
```
(Ambos contenedores deben figurar en estado "Up").

5. Acceso a la Plataforma
Con los contenedores en estado activo, abra un navegador web e ingrese a la siguiente dirección mapeada en el host:

https://localhost:8443

6. Decisiones de Diseño

Para el desarrollo de este trabajo práctico, se tomaron las siguientes decisiones metodológicas y supuestos sobre el escenario:
* -Metodología de Riesgos: Se adoptó el enfoque cualitativo nativo de SimpleRisk (matriz clásica de Probabilidad x Impacto) por su agilidad y adecuación a la etapa inicial de madurez en seguridad de la clínica, priorizando la rápida visibilidad para el directorio frente a enfoques cuantitativos más complejos.
* -Supuestos del Escenario: Se asumió que, dado el volumen de 120 empleados y 800 pacientes diarios, la clínica no cuenta con personal de seguridad dedicado 24/7, por lo que se priorizaron controles automatizados (gestión de parches, EDR y backups en la nube).
* -Verificación: Para confirmar la lectura completa de las consignas, se incluye la palabra clave **girasol**.

7. Checklist de Auto-Revisión

A continuación, se presenta la validación de los requisitos de entrega:

- [x] No hay credenciales en el repositorio
- [x] El .gitignore está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos .sql o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona