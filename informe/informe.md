# Informe — Trabajo Práctico: Gestión de Riesgos con SimpleRisk

**Materia:** Seguridad de Sistemas · **Alumno:** Juan Narváez (Juanchi) · **LU:** `31631196` · **Comisión:** `4°G`

---

## 1. Introducción

Este informe documenta el desarrollo del TP de gestión de riesgos utilizando **SimpleRisk**
como herramienta GRC (Governance, Risk & Compliance). Se instaló la herramienta en un entorno
reproducible, se modeló un escenario realista de una clínica privada y se cargó el registro
inicial de riesgos con sus planes de acción, siguiendo criterios profesionales de análisis,
evaluación y tratamiento.

---

## 2. Parte A — Instalación y configuración básica

### 2.1 Instalación reproducible
Se utilizó **Docker** sobre **Ubuntu 24.04 LTS** (VirtualBox), con la imagen oficial
autocontenida `simplerisk/simplerisk`, que incluye servidor web y base de datos. El proceso
está automatizado en `entorno/setup.sh` y definido en `entorno/docker-compose.yml`.

Pasos resumidos:
1. `cd entorno && ./setup.sh` (instala Docker si falta y levanta el contenedor).
2. Acceso por `https://localhost/`, login inicial `admin/admin`.
3. Cambio inmediato de la contraseña por defecto.

> *Capturas:* `informe/capturas/01-instalacion.png`, `02-instalacion.png`, `03-login.png`, `04-login.png`, `05-dashboard.png`.

### 2.2 Usuarios y permisos
Se crearon **3 usuarios con roles diferenciados** aplicando mínimo privilegio
(detalle completo en `configuracion/usuarios.md`):

- `admin` — Administrator (configuración).
- `analista_riesgos` — Risk Manager (alta/valoración de riesgos y planes).
- `auditor` — Auditor (solo lectura).

> *Capturas:* `informe/capturas/06-user.png` a `09-user.png` (alta de cada usuario), `10-usuarios.png` (listado final con los 3 usuarios).

### 2.3 Primer riesgo de prueba
Se creó un riesgo de validación para confirmar el funcionamiento del sistema, verificando
el flujo completo: alta → valoración (P×I) → clasificación de nivel → plan de mitigación.

---

## 3. Parte B — Escenario real (el corazón del TP)

### 3.1 Contexto
**"Centro Médico del Valle"**, clínica privada de 120 empleados que atiende ~800 pacientes/día
y maneja historias clínicas digitales, datos de obras sociales y facturación. Una auditoría
externa reciente detectó debilidades en su gestión de riesgos.

### 3.2 Riesgos identificados
Se definieron **9 riesgos específicos** (no genéricos), documentados en `configuracion/riesgos.md`
con nombre, descripción, categoría, activos, probabilidad e impacto justificados (escala 1–5),
nivel resultante, controles existentes, plan de tratamiento y propietario.

| ID | Riesgo | P×I | Nivel |
|----|--------|-----|-------|
| R01 | Ransomware sobre historias clínicas | 20 | Crítico |
| R03 | Phishing al personal administrativo | 16 | Crítico |
| R02 | Exfiltración de datos de pacientes | 15 | Alto |
| R04 | Ausencia de backups probados | 15 | Alto |
| R05 | Privilegios excesivos / cuentas compartidas | 12 | Alto |
| R06 | Exposición en facturación con obras sociales | 12 | Alto |
| R07 | Incumplimiento Ley 25.326 | 12 | Alto |
| R08 | Dispositivos sin cifrado | 9 | Medio |
| R09 | Falla de infraestructura sin redundancia | 9 | Medio |

**Justificación de valores:** apoyada en la evidencia del *Verizon DBIR* (el sector salud es de
los más atacados, con fuerte peso del elemento humano y del ransomware) y en que la auditoría
externa **ya confirmó** las debilidades, lo que eleva la probabilidad mientras no haya controles.

> *Capturas:* `informe/capturas/11-riesgos-cargados.png` a `14-riesgos-cargados.png`, `15-matriz-calor.png`.

### 3.3 Planes de acción
Se crearon **3 planes de acción** para los riesgos de mayor nivel (detalle en `riesgos.md`):

- **PA-01** — Defensa contra ransomware (R01): EDR, segmentación, parcheo. Venc. 90 días.
- **PA-02** — Protección de datos de pacientes (R02): cifrado, RBAC, logging/DLP. Venc. 120 días.
- **PA-03** — Concientización + MFA (R03): capacitación y MFA. Venc. 60 días. *(En curso.)*

Cada plan incluye título, descripción, fecha de vencimiento, responsable, presupuesto estimado
y estado inicial.

> *Capturas:* `informe/capturas/16-planes-accion.png` a `18-planes-accion.png`.

### 3.4 Reporte ejecutivo
Se generó el reporte para la dirección en `reporte-ejecutivo/reporte.pdf` (máx. 3 páginas):
resumen ejecutivo, top 5 riesgos por nivel, estado de los planes y recomendaciones prioritarias.

---

## 4. Parte C — Análisis crítico y profundización

### 4.1 Comparación metodológica: SimpleRisk vs FAIR

SimpleRisk implementa por defecto una matriz **cualitativa Probabilidad × Impacto** (escala 1–5),
enfoque clásico y simple. Como metodología alternativa se analiza **FAIR** (*Factor Analysis of
Information Risk*), un modelo **cuantitativo** que expresa el riesgo en términos económicos
(pérdida anual esperada) descomponiendo la frecuencia de eventos de pérdida y la magnitud de
pérdida en factores medibles.

**Ventajas de SimpleRisk (matriz P×I):**
- Simple, rápida de aplicar y de comunicar; ideal para un registro inicial como el de esta clínica.
- Bajo costo de datos: no requiere estimaciones económicas detalladas.
- Buena para priorizar cuando la organización tiene madurez baja en seguridad.

**Desventajas:**
- Subjetividad: dos analistas pueden asignar valores distintos.
- La escala ordinal no permite sumar ni comparar magnitudes reales (un "20" no es el doble de un "10").
- No traduce el riesgo a dinero, lo que dificulta justificar inversiones ante la dirección.

**Ventajas de FAIR:**
- Cuantifica el riesgo en pérdida económica esperada → decisiones de inversión basadas en ROI.
- Reduce la subjetividad mediante distribuciones y rangos.
- Facilita comparar el costo de un control contra la reducción de pérdida esperada.

**Desventajas de FAIR:**
- Requiere datos y experiencia (frecuencias, costos) muchas veces no disponibles.
- Mayor esfuerzo y curva de aprendizaje; puede ser excesivo para un primer registro.

**¿En qué contexto es mejor cada una?**
La matriz P×I de SimpleRisk es preferible en organizaciones de **madurez inicial** o para un
**relevamiento rápido** (como el de esta clínica que recién sale de una auditoría). FAIR es
superior cuando se necesita **justificar económicamente** inversiones de seguridad o priorizar
entre controles costosos, en organizaciones con más datos y madurez. Un camino habitual es
**empezar con P×I y migrar a FAIR** los riesgos top para el caso de negocio.

> *Nota:* OCTAVE (enfoque organizacional dirigido por activos) y NIST SP 800-30 (guía de
> conducción de evaluaciones de riesgo) son otras alternativas válidas; NIST 800-30 de hecho
> también usa una matriz cualitativa likelihood × impact, más formalizada que la de SimpleRisk.

### 4.2 Integración con una herramienta externa

Se propone integrar SimpleRisk con **Slack/Microsoft Teams** mediante un **webhook** que notifique
automáticamente cuando se crea o actualiza un riesgo de nivel **Alto o Crítico**, para que el
Responsable de Seguridad y la Gerencia de TI reciban alertas en tiempo real.

**Diseño de la integración (webhook simple):**
- SimpleRisk dispara (vía su API/eventos o un job que consulta la base) un `POST` a un
  *Incoming Webhook* de Slack con el detalle del riesgo.
- Ejemplo de payload:

```bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"⚠️ Riesgo CRÍTICO cargado en SimpleRisk: R01 - Ransomware (P×I=20). Propietario: Gerencia de TI"}' \
  https://hooks.slack.com/services/XXXX/YYYY/ZZZZ
```

Otras integraciones útiles: **SIEM** (enviar riesgos y su estado como eventos para correlación),
**sistema de tickets/Jira** (convertir cada plan de acción en un ticket con responsable y
vencimiento) y correo para reportes periódicos.

---

## 5. Parte D — Actividad optativa (D2: integración real)

Se implementó la propuesta **D2**: un webhook de notificación a Slack para riesgos de nivel alto,
descripto en la sección 4.2. El script de ejemplo se incluye en `scripts/notify_slack.sh`
(usa credenciales/URL ficticias que **no** se versionan; se cargan por variable de entorno).

> *Justificación de la elección:* D2 refuerza el valor operativo de SimpleRisk conectándolo con
> las herramientas de comunicación que la clínica ya usa, cerrando el ciclo detección → alerta →
> acción.

---

## 6. Conclusiones

SimpleRisk resultó una herramienta adecuada para construir un **registro inicial de riesgos**
en un contexto realista: su matriz P×I permite priorizar rápido y comunicar a la dirección.
El escenario de la clínica evidenció que los mayores riesgos combinan **amenaza técnica**
(ransomware, exfiltración) con **factor humano** (phishing) y **debilidades organizativas**
(backups, privilegios, cumplimiento). El tratamiento propuesto se concentra en los planes
PA-01 a PA-03, con foco en reducir la probabilidad de los vectores más frecuentes. Para madurar,
la clínica debería complementar el enfoque cualitativo con un análisis cuantitativo (FAIR) en
sus riesgos críticos y automatizar la notificación y el seguimiento de los planes.
