# Registro de Riesgos - SimpleRisk

## Escenario: Clinica privada (120 empleados, ~800 pacientes/dia)

| ID | Nombre | Categoria | Activo Afectado | Probabilidad | Impacto | Nivel | Tratamiento | Propietario |
|---|---|---|---|---|---|---|---|---|
| R01 | Acceso no autorizado a historias clinicas digitales | Access Management | Sistema de historias clinicas electronicas | Likely | Major | Alto | Mitigar | Responsable de TI |
| R02 | Ransomware en servidores de facturacion | Technical Vulnerability Management | Servidor de facturacion y obras sociales | Likely | Extreme/Catastrophic | Critico | Mitigar | Responsable de TI |
| R03 | Perdida de datos por falla de backup | Monitoring | Base de datos de pacientes | Unlikely | Major | Medio | Mitigar | Responsable de TI |
| R04 | Phishing dirigido al personal administrativo | Sensitive Data Management | Cuentas de correo institucional | Almost Certain | Moderate | Alto | Mitigar | Responsable de RRHH / TI |
| R05 | Filtracion de datos por dispositivos moviles sin control (BYOD) | Policy and Procedure | Datos de pacientes en dispositivos personales | Likely | Moderate | Alto | Mitigar | Responsable de TI |
| R06 | Interrupcion del servicio electrico en el centro de datos | Environmental Resilience | Infraestructura de servidores locales | Unlikely | Moderate | Medio | Mitigar | Responsable de Infraestructura |
| R07 | Incumplimiento normativo por retencion excesiva de datos | Sensitive Data Management | Bases de datos historicas de pacientes | Possible | Moderate | Medio | Mitigar | Responsable Legal / Compliance |

## Riesgo de prueba (validacion inicial del sistema)

| ID | Nombre | Categoria | Activo Afectado | Probabilidad | Impacto | Nivel | Propietario |
|---|---|---|---|---|---|---|---|
| R00 | Riesgo de prueba - Validacion del sistema | - | Servidor de prueba | Credible | Minor | Bajo/Medio | Gaston Alvarez |

## Justificacion de valores

Las probabilidades e impactos fueron estimados en base a:
- Estadisticas del sector salud como blanco frecuente de ataques de ransomware y phishing a nivel mundial (Verizon DBIR)
- Ausencia de politicas formales documentadas (BYOD, retencion de datos) en el escenario planteado
- Sensibilidad de los datos manejados (historias clinicas, datos de obras sociales) bajo la Ley 25.326 de Proteccion de Datos Personales