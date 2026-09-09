# Informe de Desarrollo y Gestión de Riesgos - SimpleRisk

> **Nota:** El presente documento contiene el informe técnico y ejecutivo completo del Trabajo Práctico de Gestión de Riesgos con SimpleRisk, aplicable al escenario de la clínica privada (120 empleados, 800 pacientes diarios). Para facilitar la lectura y evaluación, el contenido se encuentra sincronizado entre [`informe.md`](file:///c:/Users/Tincho/OneDrive/Documentos/GitHub/UCH_Gesti-nDeRiesgos/entregas/Vera-Martin-31341047/informe/informe.md) e [`informe-ejecutivo.md`](file:///c:/Users/Tincho/OneDrive/Documentos/GitHub/UCH_Gesti-nDeRiesgos/entregas/Vera-Martin-31341047/informe/informe-ejecutivo.md).

---

## 1. Resumen Ejecutivo

A raíz de la auditoría externa recientemente efectuada sobre los sistemas de información de la institución, la cual determinó debilidades significativas en la gobernanza y control de riesgos tecnológicos, se implementó el registro y análisis inicial de riesgos en la plataforma **SimpleRisk**.

La clínica cuenta con una dotación activa de **120 colaboradores** (entre personal asistencial, técnico y administrativo) y atiende un promedio diario de **~800 pacientes**. Su continuidad operativa depende de la disponibilidad e integridad de sistemas críticos: Historias Clínicas Electrónicas (HCE), diagnóstico por imágenes (PACS), plataformas de validación online de obras sociales y facturación médica.

### Principales Conclusiones del Diagnóstico:
1. **Nivel de Exposición Crítico:** Se identificaron **7 riesgos estratégicos**. Dos de ellos revisten prioridad urgente (Ransomware y Phishing administrativo), con potencial de causar parálisis asistencial completa, daño irreparable a la salud de los pacientes y sanciones severas por incumplimiento de la Ley 25.326 de Protección de Datos Personales.
2. **Planes de Acción Aprobados:** Se formalizaron e incorporaron al sistema **3 planes de mitigación integrales** para los riesgos de mayor impacto, asignando responsables, cronograma y partidas presupuestarias estimadas.
3. **Gobierno y Trazabilidad:** Se configuró un esquema de perfiles diferenciados (Administración IT, Analista de Riesgos y Auditoría Externa) para garantizar el principio de menor privilegio y la separación de funciones.

---

## 2. Contexto Institucional y Alcance

* **Infraestructura Tecnológica:** Datacenter propio (on-premise) con servidores de bases de datos relacionales, servidores de aplicaciones de gestión clínica, almacenamiento centralizado, enlace troncal con proveedor de internet (ISP) y parque informático distribuido en consultorios, internación, laboratorio, guardia y administración.
* **Flujo de Pacientes:** 800 consultas y prácticas diarias. Cada atención requiere consulta y modificación inmediata de la HCE, verificación de cobertura médica en tiempo real y emisión de prescripciones electrónicas.
* **Activos de Información Esenciales:**
  * Base de datos de Historias Clínicas Electrónicas y antecedentes médicos.
  * Archivos de imágenes diagnósticas (DICOM/PACS).
  * Datos bancarios, fiscales y convenios de facturación con prepagas.
  * Cuentas de identidad y credenciales de acceso a la red interna y Active Directory.

---

## 3. Metodología de Evaluación de Riesgos

La parametrización se llevó a cabo aplicando la **Matriz Clásica de Riesgo de SimpleRisk**, sustentada en una escala semicuantitativa de dos variables independientes de 1 a 5:

$$\text{Riesgo Inmanente} = f(\text{Probabilidad}, \text{Impacto})$$

### Criterios de Calificación:
* **Probabilidad (Likelihood):**
  * **1 (Rara):** Incidente extraordinario sin precedentes en la institución.
  * **2 (Baja):** Baja frecuencia esperable; existen salvaguardas parciales.
  * **3 (Media):** Suceso periódico o esperable en el horizonte anual.
  * **4 (Alta):** Frecuencia elevada; blanco prioritario en el sector salud.
  * **5 (Muy Alta / Casi Segura):** Vulnerabilidad expuesta y explotada activamente en el entorno.
* **Impacto (Impact):**
  * **1 (Insignificante):** Afectación operativa nula o desestimable; sin pérdidas económicas.
  * **2 (Menor):** Demoras administrativas locales subsanables en menos de 2 horas.
  * **3 (Moderado):** Retraso generalizado en la atención ambulatoria; costo de remediación acotado.
  * **4 (Crítico):** Suspensión transitoria de servicios clave; riesgo legal y asistencial grave.
  * **5 (Catastrófico):** Parálisis total de la clínica, afectación directa a la vida de pacientes internados, exfiltración masiva de datos sensibles y multas regulatorias punitivas.

---

## 4. Top 5 Riesgos Prioritarios

A continuación se detallan los cinco riesgos con mayor puntuación inmanente registrados en SimpleRisk:

```
[Alto 8.0]        ID 1001: Ransomware en servidores principales (HCE / PACS)
[Medio-Alto 6.4]  ID 1005: Phishing y robo de credenciales de administradores
[Medio 6.0]       ID 1003: Uso de cuentas compartidas en consultorios externos
[Medio 4.8]       ID 1002: Falla eléctrica y climática en el Centro de Datos
[Medio-Bajo 3.6]  ID 1006: Caída del enlace de telecomunicaciones con el ISP
```

### Tabla Resumen del Top 5 de Riesgos

| Ranking | ID | Nombre del Riesgo | Cat. | Prob. | Imp. | Score | Justificación Técnica del Impacto en la Clínica |
|:---:|:---:|---|:---:|:---:|:---:|:---:|---|
| **1°** | **1001** | Secuestro de datos (Ransomware) | Disp/Int/Conf | 4 | 5 | **8.0** | Cifrado de bases de datos clínicas; imposibilidad de dispensar medicamentos ni consultar antecedentes en urgencias. |
| **2°** | **1005** | Robo de credenciales por phishing | Conf/Int | 4 | 4 | **6.4** | Acceso a Active Directory; movimiento lateral hacia servidores de facturación y exfiltración de historiales de pacientes. |
| **3°** | **1003** | Cuentas compartidas en consultorios | Int/Legal | 4 | 3 | **6.0** | Ruptura del no repudio médico-legal ante mala praxis o adulteración dolosa de indicaciones farmacológicas. |
| **4°** | **1002** | Falla eléctrica y térmica en Datacenter | Disp/Oper | 3 | 4 | **4.8** | Apagón intempestivo de racks; daño en cabezales de discos y caída simultánea de toda la red interna de la clínica. |
| **5°** | **1006** | Corte de conectividad con ISP | Disp | 3 | 3 | **3.6** | Imposibilidad de validar coberturas médicas online y generar autorizaciones para los 800 pacientes diarios. |

---

## 5. Planes de Tratamiento y Mitigación Aprobados

En estricta correspondencia con las capturas auditadas del sistema, se han consolidado y aprobado formalmente tres proyectos de remediación:

### Plan 1: Contención y Resiliencia ante Ransomware (Riesgo ID 1001)
* **Estrategia:** Mitigar.
* **Responsable:** Laura Gómez (IT Clínica / Information Security).
* **Presupuesto Estimado:** Rango de USD $100.001 a USD $200.000.
* **Fecha Objetivo:** 09/08/2026.
* **Estado:** Planificado y Aprobado por Administración (`Mitigation Planned`).
* **Acciones Concretas:**
  1. Adquisición y configuración de una solución de almacenamiento de respaldos inmutables (*WORM / Object Lock*) con aislamiento de red (*air-gap* lógico/físico fuera de línea).
  2. Microsegmentación de redes VLAN para aislar los servidores de bases de datos médicas respecto de los segmentos de puestos de trabajo.
  3. Despliegue de un agente Endpoint Detection & Response (EDR) corporativo en las 120 terminales con capacidad de aislamiento automático ante actividad criptográfica anómala.

### Plan 2: Programa de Protección de Identidad y Antiphishing (Riesgo ID 1005)
* **Estrategia:** Mitigar.
* **Responsable:** Dr. Roberto Sánchez / Laura Gómez (Information Security).
* **Presupuesto Estimado:** Rango de USD $100.001 a USD $200.000.
* **Fecha Objetivo:** 09/08/2026.
* **Estado:** Planificado y Aprobado por Administración (`Mitigation Planned`).
* **Acciones Concretas:**
  1. Implementación forzosa de Autenticación Multifactor (MFA/2FA) para el acceso al correo corporativo, accesos remotos y servicios de liquidación médica.
  2. Campaña continua de capacitación y simulaciones de ataques de phishing para la totalidad de los 120 empleados de la clínica.
  3. Fortalecimiento de la seguridad perimetral de correo electrónico mediante la activación de políticas DMARC (*Reject*), SPF y DKIM, junto con análisis heurístico de adjuntos médicos externos.

### Plan 3: Aseguramiento Energético y Climático del Datacenter (Riesgo ID 1002)
* **Estrategia:** Mitigar.
* **Responsable:** Laura Gómez (Data Center & Storage).
* **Presupuesto Estimado:** Rango de USD $0 a USD $100.000.
* **Fecha Objetivo:** 09/08/2026.
* **Estado:** Planificado y Aprobado por Administración (`Mitigation Planned`).
* **Acciones Concretas:**
  1. Contratación, instalación y plan de mantenimiento preventivo mensual de un grupo electrógeno diésel dedicado para el centro de datos con llave de transferencia automática (ATS).
  2. Reemplazo del banco de baterías de la UPS central, dimensionándolo para otorgar 30 minutos de autonomía plena ante transitorios de arranque del generador.
  3. Implementación de software de monitoreo de temperatura y humedad ambiental con disparador de script de apagado ordenado (*graceful shutdown*) de servidores no críticos.

---

## 6. Análisis Comparativo Metodológico (Parte C.1)

El sistema SimpleRisk adopta el enfoque clásico de matriz de doble entrada (Probabilidad × Impacto). A efectos de evaluar la madurez de nuestra gestión, se contrastó este modelo frente a la metodología **FAIR** (*Factor Analysis of Information Risk*) y el estándar **ISO 27005 / NIST SP 800-30**.

### 6.1. Comparativa: SimpleRisk (Matriz Cualitativa) vs. FAIR (Cuantitativa)

| Eje de Análisis | Enfoque Matricial SimpleRisk | Metodología FAIR |
|---|---|---|
| **Naturaleza del Cálculo** | Semicuantitativo / Ordinal (1 al 5). Escalas discretas subjetivas. | Cuantitativo / Probabilístico continuo mediante simulaciones Monte Carlo. |
| **Expresión del Resultado** | Valor numérico adimensional o etiqueta de color (ej: "8.0 - Alto"). | Pérdida Financiera Esperada expresada en moneda (*Annualized Loss Expectancy - ALE* en USD). |
| **Velocidad de Despliegue** | Muy alta. Permite cargar el inventario de riesgos de la clínica en pocas horas. | Moderada a lenta. Requiere recopilar datos de frecuencia de eventos y calibrar rangos de pérdida. |
| **Comprensión por la Alta Dirección** | Fácil comprensión conceptual rápida, pero genera discusiones subjetivas sobre qué significa "impacto 4". | Óptima para el Directorio Financiero: traduce ciberseguridad a retorno de inversión (ROI) y exposición económica neta. |
| **Sesgos y Ambigüedad** | Propenso a sesgos de estimación y "compresión de rangos" (riesgos muy disímiles obtienen igual puntaje). | Reduce el sesgo mediante modelado de distribuciones de probabilidad y calibración de expertos. |

### 6.2. Recomendación de Adopción para la Clínica
Para el estadio actual de la clínica (post-auditoría inicial), el modelo provisto por **SimpleRisk es idóneo para establecer el registro inicial, visibilizar los 7 riesgos y gestionar operativamente los planes de mitigación**. No obstante, para la justificación de inversiones de capital elevadas (ej: los proyectos de USD $100k-$200k en EDR y respaldos inmutables), se recomienda a la Dirección Médica y de IT complementar las presentaciones financieras aplicando el modelo **FAIR**, expresando la reducción del riesgo en términos de contingencia económica evitada por hora de quirófano o consultorio paralizado.

---

## 7. Integración Externa y Automatización (Parte C.2)

Para potenciar la capacidad de respuesta y evitar que el registro de riesgos sea un repositorio estático, se definió la arquitectura de integración de SimpleRisk con el ecosistema corporativo:

```
[ Sensores de Red / EDR ]
           │
           ▼
     [ SIEM Wazuh ] ──────(Webhooks / REST API)──────► [ SimpleRisk ]
                                                            │
                                                     (Webhooks de Eventos)
                                                            ▼
                                                   [ Ticketing: Jira / GLPI ]
```

1. **Integración con SIEM (Wazuh / Splunk):**
   * **Mecanismo:** La API REST de SimpleRisk expone endpoints para la ingesta programática de riesgos (`/api/risks`).
   * **Caso de Uso:** Cuando el SIEM correlaciona más de 5 intentos fallidos de intrusión administrativa o detecta una estación infectada por malware de exfiltración de credenciales, dispara una llamada API que incrementa automáticamente el valor de probabilidad del riesgo ID 1005 y notifica al analista de seguridad.
2. **Integración con Plataforma de Ticketing (Jira Service Management / GLPI):**
   * **Mecanismo:** Configuración de Webhooks en SimpleRisk vinculados al evento `Mitigation Planned`.
   * **Caso de Uso:** Al aprobarse un plan de mitigación en SimpleRisk, el webhook genera automáticamente las órdenes de trabajo técnicas en el tablero Jira del equipo de infraestructura de IT, sincronizando el avance porcentual del proyecto con el estado de mitigación en SimpleRisk.

---

## 8. Hardening y Seguridad de la Plataforma SimpleRisk (Actividad Optativa D.1)

En el marco de la auditoría técnica, se evaluó la postura de seguridad de la propia instalación de SimpleRisk en Docker, detectando tres vectores de mejora implementados de inmediato:

1. **Inyección de Encabezados HTTP de Seguridad:**
   * *Diagnóstico:* La configuración por defecto no emitía encabezados de protección del navegador.
   * *Mitigación:* Se configuró el servidor web Apache embebido para inyectar `X-Frame-Options: SAMEORIGIN` (mitigación contra Clickjacking), `X-Content-Type-Options: nosniff`, `Strict-Transport-Security: max-age=31536000; includeSubDomains` y una política estricta de `Content-Security-Policy (CSP)`.
2. **Protección de Sesión y Cookies PHP:**
   * *Diagnóstico:* Las cookies de sesión podían quedar expuestas a scripts locales ante ataques XSS.
   * *Mitigación:* Se forzaron las directivas `session.cookie_httponly = 1`, `session.cookie_secure = 1` y `session.cookie_samesite = Strict` en la configuración de `php.ini`, garantizando que el token de autenticación solo viaje cifrado bajo HTTPS y sea inaccesible para código JavaScript del lado del cliente.
3. **Aislamiento y Principio de Menor Privilegio en Base de Datos MySQL:**
   * *Diagnóstico:* El contenedor MySQL exponía el puerto 3306 hacia el exterior y empleaba credenciales predecibles.
   * *Mitigación:* Se eliminó el mapeo externo del puerto 3306 en `docker-compose.yml`, dejándolo confinado exclusivamente a la red interna de Docker (`simplerisk-db`), se restringieron los privilegios del usuario de la aplicación limitándolos a la base `simplerisk` (revocando `GRANT OPTION` y permisos administrativos de sistema) y se establecieron contraseñas de entorno robustas y diferenciadas.

---

## 9. Recomendaciones Finales para el Directorio

1. **Aprobación de Fondos para los 3 Planes Prioritarios:** Se solicita al Directorio la asignación presupuestaria requerida para la ejecución de los planes de mitigación de Ransomware, Phishing y Continuidad Eléctrica antes del vencimiento fijado al 09/08/2026.
2. **Supresión Inmediata de Cuentas Genéricas:** Emitir resolución directiva ordenando a las jefaturas médicas la eliminación de usuarios compartidos en consultorios externos, habilitando la autenticación individual mediante tarjeta de proximidad para cumplir con las exigencias legales de trazabilidad.
3. **Revisión Trimestral del Registro de Riesgos:** Establecer en el calendario de la Dirección Médica y de IT una reunión trimestral de revisión de riesgos en SimpleRisk, midiendo la efectividad de los controles implementados y reclasificando riesgos residuales.

