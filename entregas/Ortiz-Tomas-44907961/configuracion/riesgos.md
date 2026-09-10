
# Registro de Riesgos - Clínica Privada (SimpleRisk)

Contexto: Clínica privada de 120 empleados, ~800 pacientes/día, maneja historias clínicas digitales, datos de obras sociales y facturación.

## Resumen de riesgos

| ID | Riesgo | Categoría | Activos afectados | Probabilidad | Impacto | Score | Nivel | Tratamiento | Propietario |
|----|--------|-----------|--------------------|:---:|:---:|:---:|-------|-------------|-------------|
| 1007 | Robo de dispositivo móvil sin cifrar | Confidencialidad | Notebooks/tablets corporativas con acceso a historias clínicas | 4 (Probable) | 5 (Extremo/Catastrófico) | 8.0 | Alto | Mitigar | analista_clinica |
| 1004 | Ransomware sobre el sistema de historias clínicas | Disponibilidad | Servidor de historias clínicas digitales | 3 (Creíble) | 5 (Extremo/Catastrófico) | 6.0 | Alto | Mitigar | admin_clinica |
| 1002 | Filtración de historias clínicas | Confidencialidad | Base de datos de historias clínicas | 3 (Creíble) | 4 (Importante) | 4.8 | Alto | Mitigar | admin_clinica |
| 1006 | Error humano por personal no capacitado | Operativo | Estaciones de trabajo, sistema de gestión | 4 (Probable) | 3 (Moderado) | 4.8 | Alto | Mitigar | admin_clinica |
| 1008 | Falta de verificación del plan de continuidad | Operativo/Disponibilidad | Infraestructura general de TI | 3 (Creíble) | 4 (Importante) | 4.8 | Alto | Mitigar | auditor_clinica |
| 1005 | Incumplimiento de la Ley de Protección de Datos Personales | Legal | Datos personales de pacientes | 2 (Improbable) | 4 (Importante) | 3.2 | Medio | Transferir | analista_clinica |
| 1003 | Alteración de datos en la facturación | Integridad | Sistema de facturación, datos de obras sociales | 2 (Improbable) | 3 (Moderado) | 2.4 | Medio | Aceptar | analista_clinica |

## Detalle por riesgo

### 1007 - Robo de dispositivo móvil sin cifrar
- **Descripción:** Pérdida o robo de un dispositivo móvil corporativo (notebook/tablet) sin cifrado, exponiendo datos de pacientes almacenados o accesibles desde el equipo.
- **Controles existentes:** Ninguno (sin cifrado de disco).
- **Plan de acción:** Implementar cifrado de disco (BitLocker/FileVault) y solución MDM para bloqueo/borrado remoto.

### 1004 - Ransomware sobre el sistema de historias clínicas
- **Descripción:** Ataque de ransomware que cifra o bloquea el acceso al sistema de historias clínicas, afectando la atención de pacientes.
- **Controles existentes:** Antivirus básico en estaciones de trabajo.
- **Plan de acción:** Backups automáticos diarios offline, solución EDR, segmentación de red, capacitación anti-phishing.

### 1002 - Filtración de historias clínicas
- **Descripción:** Acceso o divulgación no autorizada de historias clínicas digitales por falta de controles de acceso granulares.
- **Controles existentes:** Autenticación básica de usuario, sin control de acceso basado en roles.
- **Plan de acción:** Implementar RBAC, logs de auditoría de accesos, cifrado de datos en reposo y tránsito.

### 1006 - Error humano por personal no capacitado
- **Descripción:** Errores operativos (carga incorrecta de datos, exposición accidental de información) por falta de capacitación del personal en seguridad de la información.
- **Controles existentes:** Ninguno formal.
- **Plan de acción:** Programa de capacitación periódica en seguridad y manejo de datos sensibles.

### 1008 - Falta de verificación del plan de continuidad
- **Descripción:** El plan de continuidad del negocio (BCP/DRP) no se prueba ni verifica periódicamente, generando incertidumbre sobre su efectividad ante un incidente real.
- **Controles existentes:** Plan documentado pero no probado.
- **Plan de acción:** Realizar simulacros periódicos de recuperación ante desastres.

### 1005 - Incumplimiento de la Ley de Protección de Datos Personales
- **Descripción:** La clínica podría no cumplir plenamente con los requisitos legales de tratamiento de datos personales de pacientes, exponiendo a sanciones regulatorias.
- **Controles existentes:** Cumplimiento parcial, sin auditoría legal formal.
- **Tratamiento:** Transferir mediante asesoría legal externa especializada en protección de datos.

### 1003 - Alteración de datos en la facturación
- **Descripción:** Modificación no autorizada de registros de facturación u obras sociales.
- **Controles existentes:** Control de acceso básico al sistema de facturación.
- **Tratamiento:** Aceptado dado el bajo score de riesgo (2.4) y los controles mínimos ya existentes.