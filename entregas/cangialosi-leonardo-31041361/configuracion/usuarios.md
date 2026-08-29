# Usuarios y Roles en SimpleRisk

> TP SimpleRisk — Seguridad de Sistemas — Cangialosi Leonardo Arturo — LU 31041361 — Comisión G
>
> ⚠️ **Este archivo NO contiene contraseñas.** Las credenciales usadas en la instalación son
> ficticias y de demostración; nunca se versionan. Ejemplos de convención de credenciales
> ficticias: `Passw0rd!Demo` (documentado solo como formato, no como valor real en uso).

## Criterio de diseño

Se aplica el principio de **mínimo privilegio**: cada usuario recibe únicamente los permisos
necesarios para su función. Se definen **4 usuarios con roles diferenciados** (el TP pide al
menos 3), separando quién **carga** riesgos, quién los **trata/planifica**, quién **revisa/aprueba**
y quién solo **audita/consulta**. Esta separación de funciones (SoD) es en sí misma un control
frente a R02 (acceso indebido).

## Usuarios definidos

| Usuario (ficticio) | Nombre de rol | Función en la clínica | Alcance |
|--------------------|---------------|------------------------|---------|
| `admin_demo` | **Administrador** | Responsable de Seguridad / Sistemas | Total |
| `analista_demo` | **Analista de Riesgos** | Analista de seguridad | Gestión de riesgos |
| `revisor_demo` | **Revisor / Gerencia** | Dirección / dueño de riesgo | Revisión y aprobación |
| `auditor_demo` | **Auditor** | Auditoría interna/externa | Solo lectura |

## Permisos por rol

### 1. Administrador — `admin_demo`
Configura la instancia y administra el resto de los usuarios.
- Gestión de usuarios y roles (alta/baja, asignación de permisos).
- Configuración: categorías, ubicaciones, equipos, escalas de riesgo, plantillas.
- Todos los permisos de gestión de riesgos.
- **Justificación:** rol técnico de administración; debe existir uno solo y con MFA.

### 2. Analista de Riesgos — `analista_demo`
Opera el ciclo de vida del riesgo día a día.
- **Submit risks** — cargar nuevos riesgos.
- **Modify risks** — editar riesgos existentes.
- **Plan mitigations** — definir planes de mitigación/tratamiento.
- **Ver** management reports.
- **NO** puede: administrar usuarios ni aprobar/cerrar formalmente riesgos (separación de funciones).

### 3. Revisor / Gerencia — `revisor_demo`
Representa al **propietario del riesgo** y a la dirección.
- **Review risks** — revisar y aprobar la valoración y el tratamiento.
- **Close risks** — cerrar riesgos tratados o aceptados.
- **Ver** reportes ejecutivos.
- **NO** puede: crear ni editar riesgos (evita que quien aprueba sea quien carga).

### 4. Auditor — `auditor_demo`
Verifica el proceso sin poder alterarlo.
- **Solo lectura**: consulta de riesgos, planes, reportes e historial.
- Sin permisos de escritura, mitigación, revisión ni administración.
- **Justificación:** garantiza la independencia de la auditoría (relevante porque el escenario
  parte de una auditoría externa).

## Mapa de separación de funciones (SoD)

| Acción | Admin | Analista | Revisor | Auditor |
|--------|:-----:|:--------:|:-------:|:-------:|
| Administrar usuarios | ✅ | ❌ | ❌ | ❌ |
| Cargar riesgo | ✅ | ✅ | ❌ | ❌ |
| Editar riesgo | ✅ | ✅ | ❌ | ❌ |
| Planificar mitigación | ✅ | ✅ | ❌ | ❌ |
| Revisar / aprobar | ✅ | ❌ | ✅ | ❌ |
| Cerrar riesgo | ✅ | ❌ | ✅ | ❌ |
| Solo lectura / reportes | ✅ | ✅ | ✅ | ✅ |

## Nota sobre el riesgo de prueba (Parte A.3)

Para validar que el sistema funciona correctamente se creó un **riesgo de prueba**
(`R00 — Riesgo de prueba de instalación`) cargado con el usuario `analista_demo`, revisado con
`revisor_demo` y consultado con `auditor_demo`, verificando así el flujo completo y los permisos
de cada rol. Una vez validado, se marca como cerrado / de prueba para no contaminar el registro real.
