# Inventario de activos

Escenario académico: clínica privada ficticia con 120 empleados
y 800 pacientes diarios. No se utilizan datos reales de pacientes.

## Activos registrados

| ID | Activo | Tipo | Responsable propuesto | Clasificación | Criticidad |
|---|---|---|---|---|---|
| A01 | Historias clínicas digitales | Información | Dirección Médica | Restringida | Alta |
| A02 | Sistema de gestión clínica | Software | Responsable de Sistemas | Uso interno; procesa información restringida | Alta |
| A03 | Servidor de gestión clínica | Hardware | Responsable de Sistemas | Acceso restringido | Alta |
| A04 | Copias de seguridad | Información y soporte de respaldo | Responsable de Sistemas | Restringida | Alta |
| A05 | Red y conectividad | Infraestructura de comunicaciones | Responsable de Sistemas | Uso interno; configuración restringida | Alta |
| A06 | Equipos de médicos y administrativos | Hardware | Responsable de Sistemas | Uso interno; acceso a información restringida | Alta en conjunto |
| A07 | Datos de obras sociales y facturación | Información | Responsable de Administración | Restringida | Alta |

## Descripción y justificación

### A01 - Historias clínicas digitales

Incluyen antecedentes, diagnósticos, resultados y tratamientos.
Su divulgación expondría información privada; su alteración podría
provocar decisiones clínicas incorrectas y su indisponibilidad
dificultaría la atención.

### A02 - Sistema de gestión clínica

Aplicación utilizada para consultar historias clínicas y gestionar
turnos y admisión. Se supone una solución integrada para el ejercicio.
Su interrupción afecta simultáneamente varias tareas asistenciales
y administrativas.

### A03 - Servidor de gestión clínica

Servidor que aloja la aplicación y su base de datos.
Se supone un único servidor de producción, sin conmutación automática
a otro equipo. Su falla puede interrumpir el sistema de gestión clínica.

### A04 - Copias de seguridad

Respaldos de información clínica y administrativa necesarios
para recuperar el servicio ante pérdida o alteración de datos.
Se suponen copias diarias conectadas a la misma red, sin aislamiento
ni pruebas periódicas de restauración.
La existencia de una copia no demuestra que pueda recuperarse.

### A05 - Red y conectividad

Red interna, acceso Wi-Fi y conexión a Internet.
Se supone un único proveedor de Internet y una separación insuficiente
entre la red de invitados y los recursos internos.
Su disponibilidad permite acceder a servicios externos de obras
sociales y su configuración protege el acceso a los sistemas internos.

### A06 - Equipos de médicos y administrativos

Conjunto de computadoras utilizadas por el personal.
Se supone antivirus básico y actualizaciones manuales sin verificación
centralizada. Su compromiso puede facilitar el acceso indebido
a información o la propagación de software malicioso.
La criticidad alta corresponde al conjunto; la falla de un equipo
aislado puede tener un impacto menor.

### A07 - Datos de obras sociales y facturación

Incluyen afiliaciones, autorizaciones, prestaciones, importes y pagos.
Se supone el uso de planillas en una carpeta compartida con permisos
que no se revisan periódicamente.
Su divulgación afecta la confidencialidad y su alteración puede
generar rechazos de facturación y demoras en los cobros.

## Criterios de carga en SimpleRisk

- Los responsables indicados son responsabilidades organizacionales
  propuestas y documentadas en la descripción del activo.
- No se asignaron direcciones IP ficticias.
- Site/Location y Team quedaron sin seleccionar.
- No se vincularon controles del catálogo durante esta etapa.
- Asset Valuation se dejó en el rango obligatorio "$0 to $100,000"
  como valor provisional de carga.
- Ese rango no constituye una tasación ni se utilizó para calcular
  la puntuación de los riesgos.
- La clasificación y la criticidad se documentaron en Asset Details.
- Los supuestos describen el caso académico, no hallazgos de una
  auditoría sobre una clínica real.
