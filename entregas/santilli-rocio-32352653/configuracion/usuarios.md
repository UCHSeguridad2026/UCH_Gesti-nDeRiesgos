# Configuración de usuarios

Se confuguraron tres cuentas con distintos niveles de 
responsabilidad dentro de SimpleRisk. La asignación de permisos 
se realizó de acuerdo con las tareas previstas para cada perfil, 
evitando otorgar privilegios que no fueran necesarios.

## 1. Responsable de Seguridad 

- Usuario: admin_clinica
- Rol: Administrador
- Función: administración y suspervisión general de SimpleRisk.
- Permisos: acceso administrativo completo para configurar la 
plataforma, gestionar usuarios y supervisar las actividades 
relacionadas con la gestión de riesgos. 

## 2. Valentina Ríos

- Usuario: analista_riesgos
- Rol: Analista de Riesgos
- Responsable superior: Responsable de Seguridad.
- Permisos asignados: 
  - Acceso al módulo Risk Management.
  - Registro de nuevos riesgos. 
  - Modificación de la información de riesgos existentes.
  - Planificación y aceptación de mitigaciones.
  - Revisión de riesgos bajos, medios y altos.
  - Incorporación de comentarios en la gestión de riesgos.
- Restricciones: no posee permisos administrativos ni autorización 
para eliminar o cerrar riesgos.

## 3. Tomás Herrera

- Usuario: auditor_clinica
- Rol: Auditor
- Responsable superior: Responsable de Seguridad.
- Permisos asignados: 
  - Acceso al módulo Risk Management.
  - Revisión de riesgos de diferentes niveles.
  - Incorporación de comentarios sobre los riesgos evaluados.
  - Acceso al módulo Compliance.
  - Inicio de auditorías.
  - Incorporación de comentarios relacionados con cumplimiento.
- Restricciones: no posee autorización para crear o modificar 
riesgos, cerrar riesgos ni aceptar mitigaciones. Tampoco dispone 
de privilegios administrativo.

## Consideraciones de seguridad 

Las credenciales utilizadas para acceder a las cuentas no se 
incluyen en la documentación ni se almacenan en el repositorio. La 
diferenciación de permisos permite mantener una separación entre 
las funciones de administración, análisis y auditoría, reduciendo 
la asignación innecesaria de privilegios.
