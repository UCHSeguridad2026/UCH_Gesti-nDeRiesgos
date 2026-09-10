# Tabla de Riesgos Definidos - Clínica Privada

Este documento contiene la matriz formal de riesgos identificados en el contexto de la clínica (120 empleados, 800 pacientes diarios, manejo de Historias Clínicas Digitales y facturación de obras sociales).

---

## Matriz Detallada de Riesgos (Escala 1-5)

| ID | Nombre del Riesgo y Descripción | Categoría | Activos Afectados | Probabilidad | Impacto | Nivel | Controles Existentes | Plan de Tratamiento |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **1001** | **Indisponibilidad por falla de energía:** Corte total del suministro eléctrico en el data center local que apaga los servidores de la guardia médica. | Disponibilidad | Servidor de Historias Clínicas | 3 | 4 | **Alto (12)** | UPS básica de 15 minutos en rack. | **Mitigar:** Instalar grupo electrógeno de transferencia automática. |
| **1002** | **Ataque de Ransomware:** Infiltración externa por malware que secuestra y encripta el sistema central de gestión hospitalaria exigiendo rescate. | Confidencialidad e Integridad | Servidor de Aplicaciones y Base de Datos | 4 | 5 | **Crítico (20)** | Antivirus estándar en terminales. | **Mitigar:** Desplegar NGFW perimetral y backups inmutables. |
| **1003** | **Exfiltración de Historias Clínicas:** Acceso no autorizado de un atacante externo a la base de datos central y extracción de datos médicos sensibles. | Confidencialidad | Base de Datos de Pacientes (HCD) | 3 | 5 | **Crítico (15)** | Autenticación simple por usuario y clave. | **Mitigar:** Cifrado AES-256 en reposo e implementación de MFA. |
| **1004** | **Fuga de datos por ingeniería social:** Personal administrativo cae en fraudes o comparte planillas de facturación por canales inseguros (WhatsApp web). | Confidencialidad | Datos de Obras Sociales y Facturación | 4 | 3 | **Alto (12)** | Ninguno (Solo políticas en papel no supervisadas). | **Mitigar:** Capacitación continua en phishing y bloqueo de redes. |
| **1005** | **Pérdida por falta de backups:** Inexistencia de copias de seguridad desconectadas de la red (offline), provocando pérdida irreversible ante fallos lógicos. | Disponibilidad e Integridad | Servidor de Almacenamiento Principal | 3 | 5 | **Crítico (15)** | Backup diario automatizado en la misma red local. | **Mitigar:** Configurar política de respaldos redundantes 3-2-1. |
| **1006** | **Caída del enlace de internet:** Interrupción del proveedor de internet (ISP) principal, impidiendo validar las coberturas de obras sociales en tiempo real. | Operativo / Disponibilidad | Canal de Comunicación (Router WAN) | 4 | 3 | **Alto (12)** | Un solo proveedor de internet contratado actualmente. | **Mitigar:** Contratar un segundo enlace redundante con failover. |
| **1007** | **Acceso físico no autorizado:** Intrusión al rack de comunicaciones debido a que la puerta de sistemas permanece sin llave ni control estricto. | Integridad y Disponibilidad | Infraestructura de Red y Switch Central | 2 | 4 | **Medio (8)** | Llave común en puerta de madera ordinaria. | **Mitigar:** Cerradura electrónica biométrica y cámaras CCTV. |

---

## Justificación de la Escala Utilizada
* **Probabilidad (1-5):** Determinado según el nivel de vulnerabilidad hallado por la auditoría (ej: 4 indica alta exposición por falta de capacitación o parches).
* **Impacto (1-5):** Ponderado bajo la criticidad del negocio (ej: 5 indica paralización absoluta de la atención de los 800 pacientes diarios o multas legales severas).
* **Nivel de Riesgo:** Calculado de forma matemática mediante el producto clásico (`Probabilidad x Impacto`), replicando el algoritmo de SimpleRisk.
 
