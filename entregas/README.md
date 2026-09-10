# Trabajo Práctico: Gestión de Riesgos con SimpleRisk
**Asignatura:** Seguridad de Sistemas — 4to Año  
**Carrera:** Licenciatura en Ciencias de la Computación  
**Institución:** Facultad de Ciencias Exactas y Naturales  
**Fecha:** 27 de agosto de 2026  

---

## 1. Datos Personales
* **Nombre Completo:** Luciano Jofre
* **Legajo / LU:** 33155555
* **Email Institucional:** jofreluciano@uch.edu.ar

---

## 2. Instrucciones para Levantar el Entorno

El despliegue de la infraestructura está totalmente automatizado a través de Docker y scripts de inicialización. Para replicar la instancia de SimpleRisk de forma local, sigue estos pasos:

### Prerrequisitos
* Tienes que tener instalados **Git**, **Docker** y **Docker Compose** en tu sistema.

### Pasos de Despliegue
1. Clonar el repositorio y posicionarse en la rama/directorio correspondiente:
   ```bash
   git checkout entrega/luciano-jofre-33155555
   cd entregas
Dar permisos de ejecución al script de inicialización e iniciarlo:

Bash
chmod +x entorno/setup.sh
./entorno/setup.sh
(El script setup.sh se encarga de verificar dependencias, levantar los contenedores mediante docker-compose.yml e inicializar la base de datos con las tablas requeridas).

Acceder a la aplicación desde el navegador web en:
http://localhost:8080 (o el puerto configurado en tu entorno).

3. Decisiones de Diseño y Supuestos del Escenario
Contexto Operativo: Se simuló una clínica privada con 120 empleados y 800 atenciones diarias con un nivel de exposición alto sobre activos como las Historias Clínicas Electrónicas (HCE) y la infraestructura de cobros/obras sociales.

Metodología de Riesgos: Se adoptó la matriz semicuantitativa de SimpleRisk (5×5), calculando el nivel de riesgo mediante Probabilidad (1-5)×Impacto (1-5) para categorizar los hallazgos en Bajo, Medio, Alto y Crítico.

Separación de Funciones: Se configuraron tres perfiles clave (sec_admin, analyst_med, auditor_ext) aplicando el principio de menor privilegio.

4. Verificación
Palabra clave de verificación de lectura: girasol

5. Checklist de Auto-Revisión Obligatorio
[x] No hay credenciales en el repositorio

[x] El .gitignore está correctamente configurado

[x] Las capturas no muestran datos sensibles

[x] Los archivos .sql o dumps no están subidos

[x] El informe está en formato legible

[x] El reporte ejecutivo está completo

[x] Los mensajes de commit son descriptivos

[x] Mi branch está actualizada y funciona
