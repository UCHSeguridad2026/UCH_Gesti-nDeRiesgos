| ID | Riesgo / Descripción | Activo Afectado | Prob. | Impacto | Nivel | Mitigación Principal |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **R01** | Filtración o Acceso No Autorizado a Credenciales | Credenciales de autenticación | 3 | 4 | **Medio-Alto** | Excluir del control de versiones y proteger credenciales. |
| **R02** | Interrupción del Servicio de Gestión | Plataforma de atención y BD | 2 | 5 | **Medio** | Respaldos periódicos y volúmenes persistentes. |
| **R03** | Compromiso por Cuentas por Defecto | Base de datos / Consola | 2 | 4 | **Medio** | Establecer contraseñas robustas y únicas. |
| **R04** | Pérdida o Corrupción de Registros Históricos | Bases de datos históricas | 2 | 5 | **Medio** | Respaldos automatizados y fuera de línea. |
| **R05** | Acceso No Autorizado por Segregación Deficiente | Módulos de administración | 3 | 3 | **Medio** | Aplicar principio de mínimo privilegio (RBAC). |
| **R06** | Saturación de Recursos del Servidor | Entorno de ejecución | 3 | 3 | **Medio** | Limitar recursos de hardware y monitoreo activo. |
| **R07** | Ausencia de Trazabilidad / Auditoría | Registros de eventos (*logs*) | 3 | 2 | **Bajo-Medio**| Habilitar y centralizar bitácoras de auditoría. |