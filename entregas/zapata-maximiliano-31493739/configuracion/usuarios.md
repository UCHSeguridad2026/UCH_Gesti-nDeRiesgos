# Usuarios y roles en SimpleRisk

Documentación de los usuarios creados en la instancia de SimpleRisk para
este TP. **No se documentan contraseñas** en este archivo ni en ningún otro
del repositorio (ver `.gitignore`, que excluye archivos con credenciales).

## 1. `admin`

- **Rol:** Administrator (rol nativo de SimpleRisk).
- **Alcance:** Acceso completo al sistema — administración de usuarios,
  configuración global, Governance, Risk Management, Compliance, Asset
  Management, Assessments y Reportes.
- **Uso:** Cuenta creada durante el wizard inicial "Default Admin Account
  Creation", utilizada para la configuración general de la instancia y la
  creación del resto de los usuarios y roles.

## 2. `analista_riesgos`

- **Rol:** Custom **"Analista"**.
- **Permisos otorgados:**
  - Acceso al módulo **Risk Management**.
  - Puede **crear** y **modificar** riesgos.
  - Puede **planificar mitigaciones**.
  - Puede **comentar** sobre riesgos existentes.
- **Restricciones:**
  - **No puede cerrar riesgos.**
  - **No tiene permisos de administración del sistema** (no accede a
    configuración global ni gestión de usuarios).
- **Uso:** Simula el rol de un analista interno encargado de identificar,
  cargar y dar seguimiento a los riesgos de la fiambrería "Punta
  Pueyrredón".

## 3. `auditor_ext`

- **Rol:** Custom **"Auditor"**.
- **Permisos otorgados:**
  - Acceso de **solo lectura** a los módulos:
    - Governance
    - Risk Management
    - Compliance
    - Asset Management
    - Assessments
- **Restricciones:**
  - **No puede crear ni modificar** ningún elemento en ninguno de esos
    módulos.
- **Uso:** Simula el rol de un auditor externo que necesita visibilidad
  completa sobre el estado de riesgos y controles, sin capacidad de alterar
  la información.
