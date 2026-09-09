# Usuarios y Permisos — SimpleRisk

> **IMPORTANTE:** Todas las credenciales son **ficticias** y de demostración.
> Nunca se suben contraseñas reales al repositorio (ver `.gitignore` y checklist del README).
> Las contraseñas mostradas aquí son solo de ejemplo para el entorno local del docente.

## Roles definidos

Se crearon **3 usuarios con roles diferenciados**, aplicando el principio de **mínimo privilegio**.

| Usuario (login) | Nombre visible | Rol | Permisos principales | Contraseña (ficticia) |
|-----------------|----------------|-----|----------------------|------------------------|
| `admin`         | Administrador  | Administrator | Configuración total del sistema, gestión de usuarios, ajustes de la matriz de riesgo | `Passw0rd!Demo` |
| `analista_riesgos` | Ana Lista   | Risk Manager / Analista | Alta y edición de riesgos, valoración, creación de planes de acción (mitigaciones) | `Analista!2026` |
| `auditor`       | Aud Itor       | Auditor (solo lectura) | Consulta de riesgos, reportes y planes; **sin** permisos de edición | `Auditor!2026` |

## Detalle de permisos por rol

**Administrator (`admin`)**
- Gestión de usuarios y roles (`User Management`).
- Configuración de la matriz de riesgo, categorías y parámetros.
- Acceso a todos los módulos. Se usa solo para configuración inicial, no para operación diaria.

**Risk Manager (`analista_riesgos`)**
- Permisos: *Risk Management*, *Assessments*, *Mitigations*, *Reviews*.
- Es el rol operativo: define y valora los riesgos R01–R09 y crea los planes PA-01 a PA-03.
- No puede administrar usuarios ni cambiar la configuración global.

**Auditor (`auditor`)**
- Permisos de **solo lectura**: *Reporting* y consulta de riesgos y planes.
- Representa al auditor externo que revisó la gestión de riesgos.
- No puede crear ni modificar riesgos, garantizando separación de funciones.

## Notas de seguridad aplicadas
- Se cambió la contraseña por defecto de `admin/admin` inmediatamente tras la instalación.
- Se habilitó (o se recomienda habilitar) **MFA** para el rol administrador (ver PA-03).
- No se comparten cuentas entre personas: cada rol tiene un usuario propio para garantizar
  la trazabilidad (mitigación directa del riesgo **R05**).
