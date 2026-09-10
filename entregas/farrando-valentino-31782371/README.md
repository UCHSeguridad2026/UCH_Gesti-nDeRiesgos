# Gestión de riesgos con SimpleRisk

## Datos del estudiante

- Nombre: Farrando Valentino.
- Legajo: 31782371.
- Correo de contacto: valenfarra@gmail.com.
- Email institucional: pendiente de confirmar.
- Comisión: pendiente de completar.
- Rama: entrega/farrando-valentino-31782371.

## Objetivo

Analizar los riesgos de una clínica ficticia de 120 empleados
que atiende a 800 pacientes por día y gestiona historias clínicas,
datos de obras sociales y facturación.

## Entorno utilizado

- Ubuntu 24.04 LTS en VirtualBox.
- Memoria asignada: 5000 MB.
- Procesadores virtuales: 2.
- Docker y Docker Compose instalados desde los repositorios de Ubuntu.
- SimpleRisk ejecutado mediante Docker Compose.
- Acceso local por HTTPS.
- Imagen fijada mediante su identificador SHA-256.
- Volúmenes persistentes para conservar los datos del entorno.

## Instalación inicial

En una máquina con Ubuntu 24.04 LTS:

1. Actualizar el catálogo de paquetes:
   `sudo apt update`
2. Instalar Docker y Compose:
   `sudo apt install docker.io docker-compose-v2`
3. Desde esta carpeta de entrega, entrar en `entorno`:
   `cd entorno`
4. Iniciar SimpleRisk:
   `sudo docker compose up -d`
5. Consultar el estado:
   `sudo docker compose ps`
6. Abrir `https://localhost` en el navegador de Ubuntu.
7. Crear una cuenta administradora con una contraseña propia.

La instalación utiliza un certificado autofirmado.
La excepción del navegador corresponde únicamente a esta
instancia local de práctica.

El archivo Compose inicia la aplicación, pero no carga por sí solo
los usuarios, activos, riesgos y planes del ejercicio.
Las instrucciones para reproducir esa configuración se incorporarán
en los próximos avances.

## Avance del trabajo

En la instancia local se completaron:

- Creación de seis usuarios con responsabilidades diferenciadas.
- Prueba de consulta con el auditor y rechazo de modificación del puntaje.
- Configuración de la matriz de probabilidad por impacto.
- Registro de siete activos.
- Registro de siete riesgos y un riesgo separado de prueba.
- Asignación de propietarios.
- Registro de tres planes de mitigación pendientes de ejecución.

Pendiente de incorporar al repositorio:

- Documentación detallada y capturas.
- Comparación metodológica.
- Propuesta de integración.
- Reporte ejecutivo de hasta tres páginas.
- Revisión final de reproducibilidad.

## Decisiones de diseño

Se utiliza probabilidad e impacto de 1 a 5.
La normalización a escala 0–10 está desactivada.

Clasificación:
- Bajo: 1–4.
- Medio: 5–9.
- Alto: 10–15.
- Crítico: 16–25.

Los supuestos del escenario son ficticios y se documentan
en los registros. Las valoraciones económicas de activos son
provisionales y no se utilizan para calcular el riesgo.

Los planes están propuestos, no implementados; por tanto,
no se declara una reducción del riesgo por su sola creación.

## Verificación

Palabra clave de lectura de la consigna: girasol.

## Checklist de auto-revisión

Se completará a medida que se verifique cada punto.

- [ ] No hay credenciales en el repositorio.
- [ ] El .gitignore está correctamente configurado.
- [ ] Las capturas no muestran datos sensibles.
- [ ] Los archivos .sql o dumps no están subidos.
- [ ] El informe está en formato legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] Mi branch está actualizada y funciona.
