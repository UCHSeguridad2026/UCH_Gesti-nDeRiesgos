# Gestión de Usuarios y Permisos - SimpleRisk

> **Nota de Seguridad:** En cumplimiento con las directivas del trabajo práctico, las contraseñas no se almacenan en este documento. Las credenciales temporales iniciales se gestionan de forma local.

## 1. Mapeo de Usuarios y Roles

| Usuario | Nombre Completo | Rol en SimpleRisk | Permisos Asignados | Justificación Organizacional |
| :--- | :--- | :--- | :--- | :--- |
| `sec_admin` | Administrador de Seguridad | **Admin** | Full Admin (Configuración del sistema, gestión de usuarios, parámetros globales y permisos) | Responsable de la administración técnica de la plataforma SimpleRisk en la clínica. |
| `analyst_med` | Analista de Riesgos | **User / Risk Management** | Submit Risk, Assess Risk, Modify Risk, Define Mitigation | Responsable de evaluar los riesgos operativos/médicos y definir planes de acción. |
| `auditor_ext` | Auditor Externo | **Read-Only / Submitter** | Read Only (Consulta de inventario de riesgos, matrices y reportes) | Auditor encargado de verificar el cumplimiento normativo sin alterar datos. |

## 2. Evidencia de Configuración
La creación de estos usuarios se realiza a través del módulo `Configure` > `User Management` > `Add & Edit Users` dentro de la interfaz de SimpleRisk.
