# Gestión de Usuarios y Permisos — SimpleRisk

En cumplimiento del principio de **menor privilegio** y separación de funciones, se han configurado tres cuentas de usuario en la plataforma SimpleRisk para la gestión de riesgos de la clínica.

> **Nota de Seguridad:** En cumplimiento con las políticas del trabajo práctico, no se almacenan ni documentan contraseñas reales ni hash de autenticación en este repositorio.

## Tabla de Usuarios Configurados

| Nombre de Usuario | Nombre Completo | Rol Asignado | Ámbito de Permisos / Funciones |
| :--- | :--- | :--- | :--- |
| `admin_sys` | Tomás Serrani | Administrator | Gestión global del sistema, administración de usuarios, mantenimiento de parámetros y copias de seguridad. |
| `analyst_sec` | Mario Gómez | Risk Analyst | Creación, evaluación y actualización de riesgos, definición de probabilidades, impactos y planes de tratamiento. |
| `auditor_ext` | Estefania Ortiz | Auditor | Acceso exclusivo de lectura (*Read-Only*) para revisión de controles, trazabilidad y generación de reportes ejecutivos. |

## Matriz de Control de Acceso (RBAC)

* **Administrador (`admin_sys`):** Acceso total a los módulos de Configuración, Usuarios, Roles y Columna Vertebral del Sistema.
* **Analista de Riesgos (`analyst_sec`):** Acceso de lectura/escritura en los módulos *Risk Management*, *Define Mitigations* y *Perform Reviews*.
* **Auditor (`auditor_ext`):** Acceso restringido de lectura en *Risk Management* y *Reporting*. Sin permisos de modificación o borrado.