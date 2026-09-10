# Registro de Usuarios - SimpleRisk

A continuación se detallan los perfiles creados en la plataforma SimpleRisk para la gestión de riesgos de la clínica privada, con sus respectivos roles y niveles de acceso. 

> **Nota de Seguridad:** En cumplimiento con las políticas de manejo seguro de la información, las credenciales de acceso (contraseñas) han sido omitidas de este documento.

## 1. Administrador de IT (Acceso Total)
* **Nombre Completo:** Laura Gómez (IT Clínica)
* **Username:** `admin_it`
* **Email:** `lgomez@clinicademo.com`
* **Equipos (Teams):** Information Security, IT Systems Management
* **Rol en el sistema:** Administrator
* **Responsabilidades / Permisos:** Acceso total al sistema (Check All). Posee control absoluto sobre los módulos de Governance, Risk Management, Compliance y Asset Management para la configuración general de la clínica.

## 2. Analista de Riesgos (Gestión Operativa)
* **Nombre Completo:** Dr. Roberto Sánchez
* **Username:** `analista_riesgos`
* **Email:** `rsanchez@clinicademo.com`
* **Equipos (Teams):** Branch Management
* **Rol en el sistema:** Custom (Sin privilegios de superadministrador)
* **Responsabilidades / Permisos:** Permisos específicos de creación y gestión operativa. 
  * **Risk Management:** Acceso al menú, carga de nuevos riesgos, modificación de detalles, planificación y aceptación de mitigaciones, y capacidad de comentar.
  * **Asset Management:** Acceso de visualización al menú de activos.

## 3. Auditor Externo (Solo Lectura)
* **Nombre Completo:** Patricia López (Auditoría)
* **Username:** `auditor_clinica`
* **Email:** `plopez@clinicademo.com`
* **Equipos (Teams):** Ninguno
* **Rol en el sistema:** Custom (Sin privilegios de superadministrador)
* **Responsabilidades / Permisos:** Permisos estrictamente de solo lectura para la auditoría externa. No tiene capacidad de modificación.
  * **Risk Management:** Acceso al menú, revisión de riesgos en todos sus niveles (Insignificant a Very High) y capacidad de añadir reportes guardados.
  * **Compliance:** Acceso al menú de cumplimiento.