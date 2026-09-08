# Informe — TP Gestión de Riesgos con SimpleRisk

**Alumno:** Maximiliano Zapata
**LU:** 31493739
**Comisión:** 4G
**Fecha:** Septiembre 2026

---

## 1. Escenario elegido

Se optó por trabajar sobre un caso propio en lugar del escenario de la clínica sugerido por la cátedra: **Punta Pueyrredón**, una fiambrería de 5 empleados que utiliza un sistema de gestión (EPyme), cuenta con cámaras de seguridad, control de stock, y acepta pagos con QR y tarjeta. El negocio maneja datos de clientes, proveedores y empleados.

Se eligió este escenario por tratarse de un caso real conocido por el autor, lo que permitió definir riesgos con mayor precisión y realismo que un caso puramente hipotético.

## 2. Parte A — Instalación y Configuración Básica

### 2.1 Instalación

Se instaló SimpleRisk mediante Docker en un entorno Windows, utilizando WSL2 como backend. El proceso completo está detallado en `entorno/instrucciones.md`. En resumen:

1. Instalación de WSL2 (`wsl --install`)
2. Instalación de Docker Desktop (modalidad per-user, backend WSL2)
3. Descarga de la imagen oficial: `docker pull simplerisk/simplerisk`
4. Ejecución del contenedor: `docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk`
5. Acceso vía `https://localhost/` (aceptando la advertencia de certificado autofirmado, esperable en un entorno local)
6. Configuración de la cuenta de administrador mediante el wizard inicial de SimpleRisk

### 2.2 Usuarios y roles

Se crearon 3 usuarios con roles diferenciados (documentado sin contraseñas en `configuracion/usuarios.md`):

| Usuario | Rol | Permisos principales |
|---|---|---|
| admin | Administrator | Acceso completo al sistema |
| analista_riesgos | Analista (custom) | Crear/modificar riesgos, planificar mitigaciones, comentar. No puede cerrar riesgos ni administrar el sistema |
| auditor_ext | Auditor (custom) | Solo lectura sobre Governance, Risk Management, Compliance, Asset Management y Assessments |

### 2.3 Riesgo de prueba

Se creó un riesgo de prueba ("Riesgo de prueba - validación del sistema") para confirmar el correcto funcionamiento de la instalación antes de proceder con el escenario real.

## 3. Parte B — Escenario Real

### 3.1 Riesgos identificados

Se identificaron 9 riesgos específicos del contexto de Punta Pueyrredón (detalle completo en `configuracion/riesgos.md`), cubriendo las categorías de confidencialidad, integridad, disponibilidad, legal y operativo:

| ID | Riesgo | Nivel | Valor |
|---|---|---|---|
| R01 | Robo de credenciales del sistema de gestión (EPyme) | Alto | 12 |
| R02 | Pérdida de datos por falta de backup del sistema EPyme | Alto | 12 |
| R03 | Acceso físico no autorizado a la caja/POS fuera de horario | Medio | 6 |
| R04 | Grabaciones de cámaras de seguridad accesibles sin protección | Medio | 6 |
| R05 | Error humano al cargar precios o stock en el sistema | Medio | 8 |
| R06 | Fuga de datos de empleados por mal manejo de archivos | Alto | 12 |
| R07 | Interrupción del sistema de gestión por falla del proveedor | Medio | 6 |
| R08 | Uso de dispositivo personal del empleado sin control (BYOD) | Medio | 9 |
| R09 | Exposición de datos de tarjeta por mal manejo del POS/QR de pago | Medio | 8 |

**Nota metodológica:** los valores de Probabilidad e Impacto (escala 1-5) y su producto (Valor, escala 1-25) siguen la matriz clásica de la plantilla académica de la cátedra. Al cargar los mismos riesgos en SimpleRisk, la herramienta calculó valores distintos (por ejemplo, escala 0-5 con decimales) porque utiliza su propia lógica interna de scoring ("Classic Risk Scoring"). Esta discrepancia no representa un error, sino una diferencia metodológica entre ambos sistemas, que se retoma en la Parte C.

### 3.2 Planes de acción

Se definieron 3 planes de mitigación para los riesgos de nivel Alto, cargados directamente en SimpleRisk (pestaña "Mitigation" de cada riesgo):

**Plan 1 — R01 (Robo de credenciales):** Implementar 2FA (si el proveedor del EPyme lo permite), política de contraseñas fuertes, y capacitación al personal sobre phishing. Estrategia: Mitigar. Responsable: admin (representando al dueño/responsable).

**Plan 2 — R02 (Falta de backup):** Configurar backup automático diario con copia en la nube o disco externo. Estrategia: Mitigar. Responsable: admin (responsable técnico).

**Plan 3 — R06 (Fuga de datos de empleados):** Restringir acceso a legajos/sueldos solo al responsable de RRHH; eliminar el intercambio de archivos sin protección por WhatsApp/email. Estrategia: Mitigar. Responsable: admin (responsable administrativo).

### 3.3 Reporte ejecutivo

Ver `reporte-ejecutivo/reporte.pdf` — resumen ejecutivo dirigido al directorio de Punta Pueyrredón, con el Top 5 de riesgos, estado de los planes de acción, y recomendaciones prioritarias.

## 4. Parte C — Análisis Crítico y Profundización

### 4.1 Comparación metodológica: SimpleRisk vs. NIST SP 800-30

**Enfoque de SimpleRisk:** matriz clásica de Probabilidad × Impacto (Classic Risk Scoring), con categorías predefinidas de likelihood (Remote a Almost Certain) e impact (escala equivalente), resultando en un valor numérico simple que ubica al riesgo en una matriz de calor.

**Enfoque de NIST SP 800-30:** proceso más granular, que separa fuentes de amenaza (adversarial, accidental, estructural, ambiental), eventos de amenaza específicos vinculados a vulnerabilidades concretas, y evalúa probabilidad de ocurrencia y probabilidad de impacto como variables separadas, con una escala de impacto multidimensional y documentación explícita de supuestos.

**Ventajas y desventajas:**

- SimpleRisk es más simple, rápido e intuitivo (ideal para un negocio pequeño como Punta Pueyrredón), pero pierde granularidad y no fuerza a documentar los supuestos detrás de cada estimación.
- NIST SP 800-30 es más riguroso y trazable (mejor para auditorías o sectores regulados), pero requiere considerablemente más tiempo y expertise, resultando sobredimensionado para una pyme de 5 empleados.

**Conclusión:** para el contexto de Punta Pueyrredón, la matriz clásica de SimpleRisk es la opción adecuada como primer paso de madurez en gestión de riesgos; NIST SP 800-30 sería más apropiado si el negocio creciera significativamente o necesitara cumplir con normativas específicas que exigan trazabilidad detallada.

### 4.2 Integración con herramienta externa: Slack

Se documentó y **se implementó realmente** una integración entre SimpleRisk y Slack, para notificar automáticamente cuando existen riesgos de nivel Alto o Crítico.

**Limitación encontrada:** la API REST oficial de SimpleRisk ("API Extra") es una funcionalidad de pago, no incluida en la versión Community/Docker utilizada en este TP. Por lo tanto, la integración implementada simula la consulta de riesgos leyendo un archivo JSON local (`scripts/riesgos_actuales.json`) que representa el estado actual de los riesgos cargados manualmente en SimpleRisk, en lugar de consultar la API real.

**Lo que sí es 100% real y funcional:** la notificación a Slack mediante un Incoming Webhook real, implementada en `scripts/notify_slack_risks.py`. Al ejecutar el script, se detectaron correctamente los 3 riesgos de nivel Alto (R01, R02, R06) y se envió una notificación real al canal `#seguridad-riesgos`, confirmando el funcionamiento de punta a punta de la integración (ver captura en `informe/capturas/`).

Si en el futuro se adquiriera la API Extra de SimpleRisk, bastaría con modificar la función `obtener_riesgos()` del script para que consulte `{SIMPLERISK_URL}/api/risks` en lugar del JSON local — el resto de la lógica (filtrado y notificación) funcionaría sin cambios.

## 5. Parte D — Actividad Optativa

**D2 — Integración real implementada:** tal como se detalla en la sección 4.2, se implementó una integración funcional entre SimpleRisk y Slack mediante un Incoming Webhook y un script en Python, superando la limitación de la API paga mediante una arquitectura híbrida (datos locales + notificación real).

## 6. Conclusiones y Recomendaciones

El uso de SimpleRisk permitió estructurar de forma ordenada el proceso de identificación, evaluación y tratamiento de riesgos de un negocio real, evidenciando que incluso una pyme pequeña como Punta Pueyrredón enfrenta riesgos de seguridad de la información no triviales (especialmente en torno a credenciales, backups y datos de RRHH).

Se recomienda como próximos pasos: implementar los 3 planes de mitigación definidos para los riesgos de nivel Alto, revisar periódicamente los riesgos de nivel Medio, y evaluar en el futuro la adquisición de la API Extra de SimpleRisk si el negocio requiere automatizar más profundamente su gestión de riesgos.

## 7. Verificación

girasol
