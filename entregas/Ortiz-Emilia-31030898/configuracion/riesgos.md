# Registro de Riesgos - Clínica Privada

Matriz de riesgos definida para el contexto de la clínica (120 empleados, 800 pacientes/día, uso de Historias Clínicas Digitales).

| ID | Riesgo | Categoría | Activo Afectado | Probabilidad | Impacto | Nivel (PxI) | Tratamiento |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **RSK-01** | **Infección por Ransomware en HCD**<br>Cifrado de BD tras phishing. | Disponibilidad | Servidores HCD | 4 | 5 | **20 (Crítico)** | Mitigar |
| **RSK-02** | **Fuga de datos por WhatsApp**<br>Médicos comparten estudios por chat. | Confidencialidad | Datos de Pacientes | 5 | 4 | **20 (Crítico)** | Mitigar |
| **RSK-03** | **Caída de validación de Obras Sociales**<br>Corte de fibra óptica único. | Disponibilidad | Enlace WAN | 4 | 4 | **16 (Alto)** | Mitigar |
| **RSK-04** | **Exfiltración por terminales desatendidas**<br>Sesiones de HCD abiertas en guardias. | Confidencialidad | Terminales HCD | 4 | 4 | **16 (Alto)** | Mitigar |
| **RSK-05** | **Falla catastrófica de hardware SAN**<br>Rotura de discos con imágenes (PACS). | Disponibilidad | Almacenamiento SAN | 2 | 5 | **10 (Medio)** | Transferir |
| **RSK-06** | **Alteración no autorizada de registros**<br>Privilegios excesivos en administrativos. | Integridad | Sistema HIS | 3 | 4 | **12 (Medio)** | Mitigar |
| **RSK-07** | **Incumplimiento normativo (Ley 25.326)**<br>Falta de consentimiento digital. | Legal | Reputación institucional | 3 | 4 | **12 (Medio)** | Mitigar |

*Justificaciones basadas en reportes de la industria (ej. Verizon DBIR) para el sector salud, donde el error humano y el ransomware son las amenazas principales.*