# Configuración de usuarios

## Objetivo

Para el desarrollo del trabajo práctico se configuraron usuarios con diferentes responsabilidades dentro de SimpleRisk, buscando aplicar una separación básica de funciones para la gestión de riesgos.

No se documentan contraseñas ni credenciales de acceso utilizadas durante la configuración.

## Usuarios configurados

### 1. Administrador

**Usuario:** tomtom  
**Función:** Administrador del sistema.

Responsabilidades:

- Administración general de SimpleRisk.
- Configuración del sistema.
- Gestión de usuarios y permisos.
- Supervisión del proceso de gestión de riesgos.
- Acceso a las funciones administrativas.

### 2. Analista de riesgos

**Usuario/Rol:** Analista de riesgos  
**Función:** Identificación, análisis y tratamiento de riesgos.

Responsabilidades:

- Registrar nuevos riesgos.
- Evaluar probabilidad e impacto.
- Identificar activos afectados.
- Proponer medidas de mitigación.
- Realizar seguimiento de los riesgos registrados.

Este usuario fue asignado como propietario de los riesgos analizados durante el trabajo práctico.

### 3. Auditor

**Usuario/Rol:** Auditor  
**Función:** Revisión y seguimiento.

Responsabilidades:

- Consultar los riesgos registrados.
- Revisar las evaluaciones realizadas.
- Verificar los controles y tratamientos definidos.
- Realizar tareas de seguimiento y auditoría.

El perfil de auditor debe contar principalmente con permisos de consulta y revisión, evitando privilegios administrativos innecesarios.

## Separación de funciones

La utilización de perfiles diferenciados permite aplicar el principio de mínimo privilegio y separar las responsabilidades de administración, análisis y auditoría.

El administrador mantiene el control de la plataforma, el analista trabaja sobre la identificación y tratamiento de riesgos y el auditor realiza tareas de revisión y seguimiento.

## Seguridad

Por razones de seguridad, este documento no contiene contraseñas, tokens, claves privadas ni otras credenciales.

Todas las cuentas utilizadas en el entorno corresponden exclusivamente al escenario académico del trabajo práctico.