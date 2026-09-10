# Inventario y Registro Inicial de Riesgos

El siguiente registro fue diseñado específicamente para la clínica (120 empleados, 800 pacientes/día, HCE, obras sociales y facturación). 

La valoración utiliza la matriz de $5 \times 5$ ($Riesgo = Probabilidad \times Impacto$):
* **Bajo:** 1 - 4
* **Medio:** 5 - 9
* **Alto:** 10 - 15
* **Crítico:** 16 - 25

## Tabla General de Riesgos

| ID | Nombre del Riesgo | Activo Afectado | Categoría | Prob (1-5) | Imp (1-5) | Valor | Nivel | Estrategia | Propietario |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **R01** | Infección por Ransomware en Servidor HCE | Servidor de Historias Clínicas Electrónicas (HCE) | Disponibilidad / Operativo | 4 | 5 | **20** | **Crítico** | Mitigar | Jefe de Infraestructura TI |
| **R02** | Exfiltración de Historias Clínicas por Phishing | Base de Datos de Pacientes | Confidencialidad / Legal | 4 | 5 | **20** | **Crítico** | Mitigar | Oficial de Seguridad (CISO) |
| **R03** | Fuga de Datos de Obras Sociales por Ex-empleados | Sistema de Facturación y Obras Sociales | Confidencialidad / Operativo | 3 | 3 | **9** | **Medio** | Mitigar | Dir. de Recursos Humanos |
| **R04** | Caída del Enlace de Internet Principal | Portal Web de Turnos y Facturación | Disponibilidad | 3 | 3 | **9** | **Medio** | Transferir | Jefe de Operaciones |
| **R05** | Modificación no Autorizada de Recetas | Sistema de Farmacia e Insumos | Integridad | 2 | 4 | **8** | **Medio** | Mitigar | Farmacéutico Director |
| **R06** | Pérdida de Backups por Falla de Hardware | Storage NAS de Respaldo | Disponibilidad / Integridad | 2 | 5 | **10** | **Alto** | Mitigar | Administrador SysAdmin |
| **R07** | Interrupción Eléctrica en Centro de Cómputos | Servidores Locales | Disponibilidad | 3 | 4 | **12** | **Alto** | Mitigar | Director de Mantenimiento |

---

## Justificación Detallada de Valoración

### R01: Infección por Ransomware en Servidor HCE
* **Probabilidad (4 - Probable):** El sector salud es uno de los objetivos más atacados globalmente por ransomware (fuente: Verizon DBIR).
* **Impacto (5 - Catastrófico):** Parálisis completa de la atención de los 800 pacientes diarios y bloqueo de acceso a antecedentes médicos.

### R02: Exfiltración de Historias Clínicas por Phishing
* **Probabilidad (4 - Probable):** 120 empleados expuestos a correo electrónico sin autenticación de doble factor (MFA).
* **Impacto (5 - Catastrófico):** Violación grave de confidencialidad médica, sanciones legales/regulatorias y severo daño reputacional.

### R03: Fuga de Datos de Obras Sociales por Ex-empleados
* **Probabilidad (3 - Posible):** Rotación de personal administrativo y falta de desaprovisionamiento inmediato de cuentas.
* **Impacto (3 - Moderado):** Pérdida de datos sensibles de facturación y reprocesamiento de trámites.

### R04: Caída del Enlace de Internet Principal
* **Probabilidad (3 - Posible):** Inestabilidad o cortes ocasionales del proveedor ISP local.
* **Impacto (3 - Moderado):** Imposibilidad de validar obras sociales e ingresar turnos en tiempo real.

### R05: Modificación no Autorizada de Recetas
* **Probabilidad (2 - Improbable):** Requiere credenciales de acceso al módulo de farmacia.
* **Impacto (4 - Mayor):** Posible suministro erróneo de medicamentos a pacientes internados.

### R06: Pérdida de Backups por Falla de Hardware
* **Probabilidad (2 - Improbable):** El almacenamiento cuenta con tolerancia a fallos RAID básica.
* **Impacto (5 - Catastrófico):** Imposibilidad de restaurar la operación ante un incidente informático grave.

### R07: Interrupción Eléctrica en Centro de Cómputos
* **Probabilidad (3 - Posible):** Inestabilidad en el suministro de la red eléctrica urbana.
* **Impacto (4 - Mayor):** Apagado abrupto de servidores, posible corrupción de base de datos y caída de la HCE.
