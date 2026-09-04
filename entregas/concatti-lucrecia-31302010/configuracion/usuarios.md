# Configuración de usuarios

Se configuraron tres usuarios con responsabilidades diferenciadas dentro de SimpleRisk, aplicando el principio de mínimo privilegio de acuerdo con las funciones asignadas.

## 1. Administrador de Seguridad

 - Usuario: admin_demo
 - Rol: Administrador
 - Función: administración general de la plataforma.
 - Permisos: acceso administrativo completo para configuración, gestión de usuarios y supervisión del proceso de gestión de riesgos.

## 2. Martina López 

 -Usuario: analista_demo
 -Rol: Analista de Riesgos
 -Responsable superior: Administrador de Seguridad.
 -Permisos asignados:
  - Acceso al módulo Risk Management.
  - Registro de nuevos riesgos.
  - Modificación de riesgos existentes.
  - Planificación y aceptación de mitigaciones.
  - Revisión de riesgos bajos, medios y altos.
  - Comentarios dentro del módulo de gestión de riesgos.
 -Restricciones: no posee privilegios administrativos ni permisos para eliminar o cerrar riesgos.

## 3. Nicolás Fernández

  -Usuario: auditor_demo
  -Rol: Auditor
  -Responsable superior: Administrador de Seguridad.
  -Permisos asignados:
   - Acceso al módulo Risk Management.
   - Revisión de riesgos en sus diferentes niveles.
   - Comentarios sobre riesgos.
   - Acceso al módulo Compliance.
   - Inicio de auditorías.
   - Comentarios relacionados con cumplimiento.
 -Restricciones: no puede crear, modificar, cerrar ni aceptar mitigaciones sobre riesgos y no posee privilegios administrativos.

## Consideraciones de seguridad

Las contraseñas utilizadas para las cuentas no se documentan ni almacenan en el repositorio. La separación de responsabilidades busca limitar los privilegios de cada usuario a las funciones necesarios para su actividad.
