# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

## Datos de la estudiante

* **Nombre completo:** Camila Aylen Borodij
* **LU:** 31429202
* **Email institucional:** camilaborodijferrari@gmail.com
* **Comisión:** 4° Año 

---

## Descripción

El trabajo consiste en instalar y configurar SimpleRisk mediante Docker Compose para gestionar integralmente el ciclo de vida de los riesgos de ciberseguridad en una clínica privada ficticia de 120 empleados. La institución atiende aproximadamente 800 pacientes al día y administra digitalmente Historias Clínicas Electrónicas (HCE), portal web de médicos y facturación con obras sociales.

Se definieron roles aplicando el principio de menor privilegio, se registraron y categorizaron 7 riesgos específicos del entorno sanitario bajo una matriz semicuantitativa de 5x5, se configuraron planes de mitigación presupuestados por un total de USD 28.500 para los riesgos de mayor impacto y se elaboró un Reporte Ejecutivo para la gerencia general.

---

## Requisitos previos

* Git
* Docker Desktop / Docker Engine
* Docker Compose
* Navegador web
* Puerto `8080` disponible

---

## Instrucciones para levantar el entorno

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/arelgueta/UCH_Gesti-nDeRiesgos.git

2. **Ingresar al repositorio:** cd UCH_Gesti-nDeRiesgos

3. **Cambiar a la branch de la entrega:** git switch entrega/borodij-camila-31429202

4. **Ingresar al directorio del entorno:** cd entorno

5. **Levantar los servicios con Docker Compose:** docker-compose up -d

6. **Comprobar el estado de los servicios:** docker-compose ps
Los contenedores de SimpleRisk y MySQL deben figurar en ejecución y en estado saludable (healthy).

7. **Acceder a la plataforma:** Abrir el navegador web e ingresar a: http://localhost:8080

8. **Iniciar sesión:** Utilizar las credenciales asignadas para cada rol (admin_sys, analista_sec, auditor_ext). Las claves temporales se suministran por canal institucional privado.

Ejecuciones posteriores: Para volver a levantar el entorno en sesiones posteriores, simplemente ejecute: 
docker-compose up -d

Luego puede verificarse su estado mediante: docker-compose ps

**Detención del entorno**: Para detener los contenedores manteniendo intactos la base de datos y los registros configurados, ejecutar: docker-compose down
> Atención: No utilizar docker-compose down -v ya que la opción -v destruye los volúmenes persistentes donde reside la base de datos de SimpleRisk.

+ Decisiones de diseño:

Despliegue Aislado: Se utilizó Docker Compose para obtener una instalación portátil, aislada y reproducible del stack SimpleRisk y MySQL.

Persistencia de Datos: Los datos se conservan mediante volúmenes persistentes de Docker para garantizar la integridad de la base de datos ante reinicios o apagados del entorno.

Seguridad de Archivos (.gitignore): Se configuró el archivo .gitignore para excluir credenciales locales, copias de seguridad .sql, datos temporales e imágenes locales.

Segregación de Roles (RBAC): Se aplicó el principio de mínimo privilegio configurando perfiles diferenciados:

**admin_sys:** Gestión general del sistema, parámetros globales y administración de usuarios.

**analista_sec:** Carga de riesgos, evaluación de probabilidad/impacto y definición de planes de acción.

**auditor_ext:** Perfil de solo lectura para auditoría interna, revisión del registro de riesgos y consulta de reportes.

Metodología de Valoración: Se adoptó la matriz semicuantitativa clásica de 5x5 ($Probabilidad \times Impacto$) nativa en SimpleRisk. Permite priorizar eficientemente las amenazas considerando la continuidad asistencial y la confidencialidad de los datos médicos.

Escenario y Presupuesto: Se diseñó un plan de acción formal asociado a los riesgos de nivel alto (Ransomware, Phishing y Acceso sin MFA) con una asignación presupuestaria total de USD 28.500 y fechas de vencimiento acotadas al cuarto trimestre de 2026.

**Verificación:** girasol.

Checklist de auto-revisión
[x] No hay credenciales ni contraseñas reales expuestas en el repositorio.[x] El .gitignore está correctamente configurado.
[x] Las capturas y evidencias adjuntas no muestran datos sensibles ni reales.
[x] Los archivos .sql o dumps de base de datos no están subidos al repositorio.
[x] El informe y la documentación están completos y en formato legible (README.md y HTML).
[x] El reporte ejecutivo está completo e incluye presupuestos, planes de acción y recomendaciones.
[x] Los mensajes de commit son descriptivos y reflejan el avance del proyecto.
[x] La branch de entrega está actualizada, sincronizada y el entorno funciona correctamente.