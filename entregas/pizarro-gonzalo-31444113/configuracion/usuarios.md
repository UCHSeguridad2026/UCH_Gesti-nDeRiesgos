
# Usuarios y permisos de SimpleRisk

Las cuentas deben crearse con credenciales ficticias y únicas para el entorno local. Este archivo no contiene contraseñas.

| Usuario | Rol | Permisos y responsabilidad |
|---------|-----|----------------------------|
| `administrador` | Administrador | Configuración de SimpleRisk, usuarios, categorías, matriz, respaldos y administración general. No debe usarse para la carga diaria de riesgos. |
| `analista_riesgos` | Analista de riesgos | Crear y actualizar riesgos, valorar probabilidad e impacto, registrar controles, proponer tratamientos y mantener planes de acción. |
| `auditor` | Auditor / consulta | Lectura de riesgos, controles, planes y reportes; acceso a evidencias. Sin permisos para modificar el registro. |

## Evidencia de configuración

- Captura de usuarios y roles: `../informe/capturas/`


