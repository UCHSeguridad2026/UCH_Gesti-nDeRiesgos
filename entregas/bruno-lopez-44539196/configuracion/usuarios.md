\# Usuarios y permisos de SimpleRisk



\## 1. Objetivo



Este documento registra los usuarios creados en la instancia de SimpleRisk utilizada para el trabajo práctico de Gestión de Riesgos.



Por razones de seguridad, \*\*no se almacenan contraseñas, credenciales ni secretos en el repositorio\*\*.



\## 2. Usuarios configurados



| Usuario            | Nombre              | Tipo       | Rol                 | Equipo               |

| ------------------ | ------------------- | ---------- | ------------------- | -------------------- |

| `admin`            | Bruno Lopez         | SimpleRisk | Administrador       | —                    |

| `analista.riesgos` | Analista de Riesgos | SimpleRisk | Sin rol predefinido | Information Security |

| `auditor`          | Auditor             | SimpleRisk | Sin rol predefinido | Information Security |



\## 3. Permisos



\### 3.1 Administrador



El usuario `admin` posee el rol predefinido \*\*Administrator\*\*, utilizado para la administración general de la instancia de SimpleRisk.



\### 3.2 Analista de Riesgos



El usuario `analista.riesgos` utiliza permisos específicos de \*\*Risk Management\*\*, sin asignarle el rol predefinido de administrador.



Permisos asignados:



\* Acceso al menú Risk Management.

\* Crear nuevos riesgos.

\* Modificar detalles de riesgos.

\* Planificar mitigaciones.

\* Revisar riesgos insignificantes.

\* Revisar riesgos bajos.

\* Revisar riesgos medios.

\* Revisar riesgos altos.

\* Revisar riesgos muy altos.

\* Agregar comentarios en Risk Management.



\### 3.3 Auditor



El usuario `auditor` utiliza permisos orientados a la revisión y seguimiento de riesgos.



Permisos asignados:



\* Acceso al menú Risk Management.

\* Revisar riesgos insignificantes.

\* Revisar riesgos bajos.

\* Revisar riesgos medios.

\* Revisar riesgos altos.

\* Revisar riesgos muy altos.

\* Agregar comentarios en Risk Management.



No posee permisos para crear, modificar, cerrar ni planificar mitigaciones de riesgos.



\## 4. Criterio de segregación de funciones



Se definieron permisos diferenciados para evitar que todas las actividades de gestión de riesgos dependan de una única cuenta.



La cuenta administradora se utiliza para tareas de administración de la plataforma, mientras que el analista concentra las actividades de gestión y tratamiento de riesgos. El auditor dispone de permisos principalmente orientados a revisión y seguimiento.



Esta separación permite representar, dentro de la herramienta, tres funciones diferentes: \*\*administración, análisis y auditoría\*\*.
