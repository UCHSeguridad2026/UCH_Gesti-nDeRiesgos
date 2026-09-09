
# Informe: Gestión de riesgos con SimpleRisk

## 1. Objetivo y alcance

El objetivo es construir un registro inicial de riesgos para la **Clínica UCH**, una clínica privada de 120 empleados y aproximadamente 800 pacientes diarios. El alcance incluye historias clínicas electrónicas, admisión, agenda, facturación, obras sociales, correo, infraestructura y copias de seguridad.

## 2. Metodología aplicada

Se empleó una matriz de probabilidad e impacto de 1 a 5. La probabilidad estima la posibilidad de ocurrencia en el contexto planteado y el impacto considera consecuencias sobre la atención, confidencialidad de datos sanitarios, integridad de facturación y cumplimiento. El nivel se obtiene multiplicando ambos valores y se priorizan los riesgos críticos y altos.

La matriz facilita la comunicación con la dirección y permite ordenar acciones con pocos datos. Su limitación es que comprime escenarios distintos en un único número, depende del criterio de quien valora y no expresa por sí sola incertidumbre ni pérdida económica. Por eso las justificaciones deben revisarse con incidentes, auditorías y métricas.

## 3. Registro y tratamiento

Los siete riesgos, sus activos, controles, propietarios, justificaciones y tratamientos se encuentran en `../configuracion/riesgos.md`. Los tres planes se asociarán en SimpleRisk a riesgos altos o críticos y comenzarán en estado **No iniciado**. Las fechas y presupuestos son estimaciones académicas explícitas para este ejercicio y deberán validarse con la clínica.

## 4. Comparación con NIST SP 800-30

NIST SP 800-30 propone preparar la evaluación, identificar fuentes y eventos de amenaza, vulnerabilidades y condiciones predisponentes, determinar probabilidad e impacto y comunicar los resultados. Frente a la matriz de SimpleRisk, aporta un proceso más trazable y una separación explícita entre amenaza, vulnerabilidad y consecuencia. Es preferible para evaluaciones formales, auditorías y decisiones donde se necesita justificar el origen de cada valoración.

SimpleRisk resulta más rápido para mantener un registro operativo, asignar propietarios y seguir tratamientos. NIST requiere más trabajo documental y capacitación, mientras que una implementación simple de SimpleRisk puede perder detalle si solo se carga el puntaje. Una combinación razonable es usar NIST para analizar los riesgos y SimpleRisk para registrarlos, priorizarlos y hacer seguimiento.

## 5. Integración propuesta

La integración prioritaria sería con un sistema de tickets como Jira o GLPI. Cuando se crea o actualiza un riesgo crítico, SimpleRisk debería enviar un webhook HTTPS con el identificador, título, nivel, propietario y fecha objetivo. Un servicio intermedio validaría una firma HMAC, eliminaría datos clínicos, crearía un ticket y devolvería un identificador de trazabilidad.

El webhook no debe incluir historias clínicas, contraseñas ni tokens en texto plano. Debe usar TLS, autenticación por secreto almacenado fuera del repositorio, reintentos idempotentes, registro de errores sin datos sensibles y permisos mínimos. Como evidencia, se documentará el diseño y, si se implementa, una prueba con un riesgo ficticio y una captura del ticket anonimizado.

## 6. Revisión de seguridad de SimpleRisk

Antes de usar el entorno fuera de laboratorio se deben revisar: versión soportada de PHP y base de datos; permisos de archivos y exposición del archivo de configuración; HTTPS, cookies seguras, cabeceras HTTP y protección de sesión; cuentas por rol y MFA; backups cifrados y restaurables; y eliminación de credenciales por defecto. La configuración concreta y la versión observada deben completarse con evidencia de la instalación.

## 7. Evidencias y pendientes

- Capturas de usuarios, riesgos y planes: `capturas/`.
- URL y versión de SimpleRisk: pendiente de registrar después de la carga manual.
- Riesgo de prueba: pendiente de registrar después de la carga manual.
- IDs de riesgos y planes en SimpleRisk: pendientes de registrar después de la carga manual.
- Reporte ejecutivo PDF: `../reporte-ejecutivo/reporte.pdf`.
