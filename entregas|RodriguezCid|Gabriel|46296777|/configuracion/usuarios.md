# Definición de Roles y Usuarios - Clínica Médica
Metodología aplicada: Control de Acceso Basado en Roles (RBAC) y Principio de Mínimo Privilegio

## 1. Contexto y Objetivos
Para garantizar la seguridad de la información, la confidencialidad de los historiales médicos y la correcta gestión de los riesgos en la plataforma de la clínica, se definen los siguientes perfiles de usuario dentro del sistema, segmentando sus permisos y accesos.

## 2. Matriz de Usuarios y Permisos

| Rol / Usuario | Nivel de Acceso | Permisos y Capacidades | Restricciones Principales |
| :--- | :--- | :--- | :--- |
| **Administrador (Admin)** | Total / Global | - Gestión integral de la plataforma.<br>- Creación y baja de cuentas de usuario.<br>- Configuración global del sistema y respaldos. | - Prohibido alterar registros clínicos de pacientes directamente sin justificación de auditoría. |
| **Analista de Riesgos** | Moderado / Operativo | - Alta, modificación y seguimiento de riesgos en la matriz.<br>- Evaluación de probabilidades e impactos.<br>- Propuesta de planes de mitigación. | - Sin permisos para modificar configuraciones del servidor o gestionar credenciales de base de datos. |
| **Auditor de Seguridad** | Solo Lectura / Supervisión | - Visualización completa de reportes, riesgos e informes de auditoría.<br>- Revisión de bitácoras y registros de actividad (*logs*). | - Sin permisos para modificar datos, crear riesgos o alterar configuraciones del sistema. |
| **Personal Médico / Operativo** | Restringido | - Consulta de historias clínicas y gestión de turnos asignados.<br>- Registro de atenciones médicas. | - Acceso exclusivamente limitado a su área de atención y pacientes asignados; sin acceso al panel de riesgos. |