# Registro de Riesgos - Clínica Privada

## Tabla de Riesgos Definidos

| ID | Nombre / Descripción | Categoría | Activos Afectados | Prob. (1-5) | Imp. (1-5) | Nivel | Controles Existentes | Plan Tratamiento | Propietario |
|---|---|---|---|:---:|:---:|:---:|---|---|---|
| **R01** | Infección por Ransomware en Servidor de Historia Clínica Digital (HCD). | Disponibilidad / Integridad | Servidor HCD, Base de Datos | 4 | 5 | **Crítico (20)** | Antivirus básico comercial | Mitigar | Gerente de TI |
| **R02** | Filtración de datos médicos e historias clínicas por ataque de Phishing al personal. | Confidencialidad / Legal | Datos Personales de Pacientes, Email | 4 | 4 | **Alto (16)** | Filtro SPAM básico | Mitigar | CISO / Seguridad |
| **R03** | Interrupción del servicio de facturación con Obras Sociales por corte eléctrico o fallo de UPS. | Disponibilidad / Operativo | Servidor de Facturación, UPS | 3 | 4 | **Alto (12)** | UPS en servidor principal | Mitigar | Jefe de Infraestructura |
| **R04** | Fuga de información sensible por dispositivos USB no autorizados en recepción. | Confidencialidad | Terminales de Atención | 3 | 3 | **Medio (9)** | Política verbal de uso | Mitigar | Sup. de Operaciones |
| **R05** | Acceso no autorizado a legajos por credenciales compartidas o contraseñas débiles. | Confidencialidad | Sistema de RRHH y Gestión | 4 | 3 | **Alto (12)** | Ninguno | Mitigar | Gerente de RRHH |
| **R06** | Incumplimiento normativo de protección de datos personales (Ley 25.326). | Legal / Reputacional | Base de Datos de Pacientes | 2 | 5 | **Alto (10)** | Contratos estándar | Transferir | Asesor Legal |
| **R07** | Indisponibilidad del Sistema de Turnos Médicos Web por ataque DDoS. | Disponibilidad | Portal Web de Pacientes | 3 | 3 | **Medio (9)** | Firewall perimetral | Aceptar | Gerente de TI |

## Justificación de Valoración

* **R01 (Probabilidad 4, Impacto 5):** Alta frecuencia del ransomware en salud global (DBIR). Un cifrado total paraliza la atención médica y cirugías.
* **R02 (Probabilidad 4, Impacto 4):** 120 empleados sin capacitación continua en phishing. La fuga de datos genera sanciones legales graves.
* **R03 (Probabilidad 3, Impacto 4):** Red eléctrica inestable. La caída del sistema de cobro frena el flujo de caja diario.
