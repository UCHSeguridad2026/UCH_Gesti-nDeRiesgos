# Usuarios y Roles — SimpleRisk

> **Ninguna contraseña se documenta en este archivo.** Las credenciales se
> comunican por canal aparte si el docente las requiere para la evaluación.

## Roles definidos

| # | Usuario | Rol | Justificación del rol |
|---|---|---|---|
| 1 | `admin_sistemas_clinica` | Administrador | Gestión de la plataforma, alta de usuarios y configuración. Creado durante la instalación inicial (*Default Admin Account Creation*). |
| 2 | `analista_riesgos` | Analista de Riesgos | Identifica, valora y modifica riesgos; propone planes de mitigación. |
| 3 | `auditor_interno` | Auditor | Acceso de sólo lectura sobre riesgos, controles y reportes. Verifica sin capacidad de modificar. |

## Matriz de permisos

Los permisos se transcriben con la denominación exacta que utiliza SimpleRisk en
la sección *User Responsibilities* del alta de usuarios, de modo que esta tabla
sea contrastable contra las capturas de `../informe/capturas/`.

### Governance

| Permiso | Admin | Analista | Auditor |
|---|:---:|:---:|:---:|
| Allow Access to "Governance" Menu | ✅ | ✅ | ✅ |
| Able to Add New Frameworks | ✅ | ❌ | ❌ |
| Able to Modify Existing Frameworks | ✅ | ❌ | ❌ |
| Able to Delete Existing Frameworks | ✅ | ❌ | ❌ |
| Able to Add New Controls | ✅ | ❌ | ❌ |
| Able to Modify Existing Controls | ✅ | ❌ | ❌ |
| Able to Delete Existing Controls | ✅ | ❌ | ❌ |
| Able to Add Documentation | ✅ | ❌ | ❌ |
| Able to Modify Documentation | ✅ | ❌ | ❌ |
| Able to Delete Documentation | ✅ | ❌ | ❌ |
| Able to View Exceptions | ✅ | ✅ | ✅ |
| Able to Create Exceptions | ✅ | ❌ | ❌ |
| Able to Update Exceptions | ✅ | ❌ | ❌ |
| Able to Delete Exceptions | ✅ | ❌ | ❌ |
| Able to Approve Exceptions | ✅ | ❌ | ❌ |

### Risk Management

| Permiso | Admin | Analista | Auditor |
|---|:---:|:---:|:---:|
| Allow Access to "Risk Management" Menu | ✅ | ✅ | ✅ |
| Able to Submit New Risks | ✅ | ✅ | ❌ |
| Able to Modify Risk Details | ✅ | ✅ | ❌ |
| Able to Close Risks | ✅ | ❌ | ❌ |
| Able to Plan Mitigations | ✅ | ✅ | ❌ |
| Able to Accept Mitigations | ✅ | ❌ | ❌ |
| Able to Review Insignificant Risks | ✅ | ✅ | ❌ |
| Able to Review Low Risks | ✅ | ✅ | ❌ |
| Able to Review Medium Risks | ✅ | ✅ | ❌ |
| Able to Review High Risks | ✅ | ❌ | ❌ |
| Able to Review Very High Risks | ✅ | ❌ | ❌ |
| Able to Comment Risk Management | ✅ | ✅ | ❌ |
| Able to Add Projects | ✅ | ❌ | ❌ |
| Able to Delete Projects | ✅ | ❌ | ❌ |
| Able to Manage Projects | ✅ | ❌ | ❌ |
| Able to Add Saved Risk Reports | ✅ | ✅ | ❌ |
| Able to Delete Saved Risk Reports | ✅ | ❌ | ❌ |

### Compliance

| Permiso | Admin | Analista | Auditor |
|---|:---:|:---:|:---:|
| Allow Access to "Compliance" Menu | ✅ | ❌ | ✅ |
| Able to Comment Compliance | ✅ | ❌ | ❌ |
| Able to Define Tests | ✅ | ❌ | ❌ |
| Able to Edit Tests | ✅ | ❌ | ❌ |
| Able to Delete Tests | ✅ | ❌ | ❌ |
| Able to Initiate Audits | ✅ | ❌ | ❌ |
| Able to Modify Audits | ✅ | ❌ | ❌ |
| Able to Reopen Audits | ✅ | ❌ | ❌ |
| Able to Delete Audits | ✅ | ❌ | ❌ |
| Able to Approve Tests | ✅ | ❌ | ❌ |

### Otros módulos

| Permiso | Admin | Analista | Auditor |
|---|:---:|:---:|:---:|
| Allow Access to "Asset Management" Menu | ✅ | ✅ | ✅ |
| Allow Access to "Assessments" Menu | ✅ | ✅ | ✅ |
| Allow Access to "Artificial Intelligence" Menu | ✅ | ❌ | ❌ |

## Configuración adicional de las cuentas

| Opción | Analista | Auditor | Motivo |
|---|:---:|:---:|---|
| Require password change on login | ✅ | ✅ | El administrador carga una credencial inicial que el usuario debe reemplazar en su primer ingreso, de modo que no conserve conocimiento de las credenciales definitivas de terceros. |
| Multi-Factor Authentication | ❌ | ❌ | Requiere configuración de infraestructura adicional, fuera del alcance del trabajo. |
| Team(s) | Information Security | Information Security | En SimpleRisk la pertenencia a equipos condiciona la visibilidad de los riesgos. Sin asignación, los usuarios podrían no visualizar riesgos aun teniendo permiso de acceso al módulo. |

## Principios aplicados

**Menor privilegio.** Cada cuenta recibe únicamente los permisos necesarios para
su función. El caso más claro es el del auditor: sus permisos se limitan al
acceso de lectura de los módulos, sin una sola capacidad de creación,
modificación, aprobación o eliminación. El auditor no puede modificar aquello
que audita, lo que preserva la independencia del control.

**Separación de funciones.** El analista puede planificar mitigaciones
(*Able to Plan Mitigations*) pero no aceptarlas (*Able to Accept Mitigations*).
Quien propone una medida de tratamiento no es quien la aprueba, evitando que una
sola persona controle el ciclo completo de decisión sobre un riesgo.

**Escalamiento por criticidad.** El analista puede revisar riesgos hasta nivel
medio, pero no altos ni muy altos. Los riesgos de mayor criticidad requieren
intervención de un nivel jerárquico superior, alineado con el criterio de la
matriz de riesgos: nivel Alto implica tratamiento prioritario y nivel Crítico
implica escalamiento a dirección.

## Evidencia

Capturas en `../informe/capturas/`:

**Parte A.1 — Instalación**
- `a1-contenedor-running.png` — contenedor `simplerisk_app` en estado *Up (healthy)*
- `a1-simplerisk-admin-creation.png` — creación de la cuenta administradora inicial
- `a1-simplerisk-login.png` — pantalla de acceso en `localhost:8443`
- `a1-home-simplerisk.png` — aplicación operativa tras el primer ingreso

**Parte A.2 — Usuarios y permisos**
- `a2-usuarios-creados.png` — los tres usuarios dados de alta
- `a2-analista-riesgos-creacion.png` — datos de identidad del analista
- `a2-auditor-interno-creacion.png` — datos de identidad del auditor
- `a2-permisos-analista-1.png` a `-3.png` — los 13 permisos del analista
- `a2-permisos-auditor.png` — los 6 permisos del auditor
- `a2-verificacion-auditor.png` — sesión del auditor: sin acceso a configuración

**Parte A.3 — Riesgo de validación**
- `a3-riesgo-prueba-formulario.png` — formulario de alta completado
- `a3-riesgo-prueba-detalle.png` — riesgo 1001 con la configuración por defecto

**Parte B.1 — Registro de riesgos**
- `b1-riesgos-cargados.png` — los siete riesgos con sus niveles en SimpleRisk
- `b1-riesgo-r01-detalle.png` a `b1-riesgo-r07-detalle.png` — ficha completa de
  cada riesgo, con valoración, justificación y *External Reference ID*

**Parte B.3 — Planes de acción**
- `b3-mitigacion-r01-1.png` — mitigación de R01: estado *Mitigation Planned*,
  estrategia, esfuerzo, costo y solución actual
- `b3-mitigacion-r01-2.png` — requisitos y recomendaciones de seguridad del plan

**Parte C.1 — Análisis metodológico**
- `c1-matriz-normalizada-0-10.png` — matriz con normalización activada
- `c1-matriz-sin-normalizar-1-25.png` — matriz con normalización desactivada
- `c1-score-normalizado-3-6.png` — el riesgo 1001 mostrando 3.6 / Low
- `c1-score-sin-normalizar-9.png` — el riesgo 1001 mostrando 9 / High
- `c1-umbrales-configurados.png` — umbrales finales alineados a la plantilla A03
