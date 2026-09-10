# Control de Usuarios y Permisos - Gestión de Riesgos Clínica

Este documento detalla la configuración de accesos implementada en la plataforma de gestión de riesgos, garantizando el principio de mínimo privilegio y la segregación de funciones (SoD).

## Política de Seguridad de Credenciales
Siguiendo las buenas prácticas de seguridad informática, las contraseñas de acceso son estrictamente confidenciales. **Nunca se deben incluir contraseñas en este repositorio o documentación técnica.**

---

## Matriz de Roles y Permisos Asignados en SimpleRisk

### 1. Director de TI (Administrador General)
* **Usuario:** `dir_ti`
* **Nombre Real:** Roberto Gómez
* **Rol en la plataforma:** Administrator
* **Permisos:** Control total sobre el entorno. Modifica configuraciones globales, administra bases de datos y gestiona altas/bajas de personal

### 2. Oficial de Seguridad (Analista de Riesgos)
* **Usuario:** `analista_seg`
* **Nombre Real:** Laura Palacios
* **Equipo asignado:** Information Security Team
* **Rol en la plataforma:** Submitter / Reviewer (Usuario Operativo)
* **Permisos:** Identifica nuevos riesgos en el contexto clínico, evalúa niveles de probabilidad e impacto, y planifica las mitigaciones

### 3. Inspector de Auditoría (Auditor Externo)
* **Usuario:** `auditor_salud`
* **Nombre Real:** Carlos Mendoza
* **Rol en la plataforma:** Auditor / Reader (Solo Lectura)
* **Permisos:** Permisos exclusivos de solo lectura (Read-Only) para inspeccionar el mapa de riesgos y verificar los planes de acción
 
