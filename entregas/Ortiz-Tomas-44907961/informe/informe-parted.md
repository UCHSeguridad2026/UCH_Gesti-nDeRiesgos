
# Parte D4 - Propuesta de Mejora a SimpleRisk

## Issue: Dashboard con visualizaciones gráficas mejoradas

**Tipo:** Feature Request / UX Enhancement
**Etiquetas:** `enhancement`, `dashboard`, `ux`

### Descripción del problema

Actualmente, SimpleRisk presenta la información de riesgos principalmente en tablas (listados de 
riesgos, planes de mitigación, revisiones) con indicadores de color simples (rojo/naranja/amarillo) 
para el nivel de riesgo. Si bien esto es funcional, dificulta que una gerencia o directorio sin 
conocimiento técnico profundo capte rápidamente el panorama general de riesgos de la organización 
de un solo vistazo. Durante la realización de este TP, se identificó que armar el reporte ejecutivo 
para el directorio de la clínica requirió procesar manualmente los datos de la tabla de riesgos para 
poder representarlos gráficamente, ya que la herramienta no ofrece esa visualización de forma nativa.

### Propuesta de mejora

Agregar a la pantalla principal (Dashboard) un conjunto de gráficos interactivos, generados 
automáticamente a partir de los riesgos ya cargados:

1. **Gráfico de torta/dona** con la distribución de riesgos por nivel (Insignificante, Bajo, Medio, 
   Alto, Muy Alto).
2. **Gráfico de barras** con la distribución de riesgos por categoría (Confidencialidad, Integridad, 
   Disponibilidad, Legal, Operativo, etc.).
3. **Gráfico de tendencia temporal** mostrando la evolución del riesgo total de la organización 
   (suma o promedio de scores) a lo largo del tiempo, para poder visualizar si las medidas de 
   mitigación implementadas están reduciendo la exposición general.
4. **Indicador de estado de planes de acción** (ej. barra de progreso apilada: planificados / en 
   ejecución / completados / vencidos).

### Beneficio esperado

- Permite generar reportes ejecutivos como el solicitado en este TP de forma más rápida, exportando 
  directamente los gráficos en vez de recrearlos manualmente en una herramienta externa.
- Facilita la comunicación con stakeholders no técnicos (directorio, gerencia), alineado con el 
  objetivo de "hablar el lenguaje del negocio" que promueven metodologías como FAIR.
- Mejora la adopción de la herramienta por parte de organizaciones pequeñas (como la clínica de este 
  TP) que no cuentan con un equipo dedicado a generar reportes de gestión.

### Alcance técnico sugerido (a alto nivel)

- Utilizar una librería de gráficos ya popular en el ecosistema PHP/JS (ej. Chart.js, que es 
  liviana y de código abierto) para no incrementar significativamente la complejidad del stack 
  actual de SimpleRisk.
- Los datos ya existen en la base de datos (tabla de riesgos con score, categoría y fecha), por lo 
  que la mejora sería principalmente de capa de presentación (frontend), sin requerir cambios 
  estructurales grandes en el modelo de datos.

### Prioridad sugerida

Media-Alta: no es una funcionalidad crítica de seguridad, pero tiene alto impacto en la usabilidad 
y en la percepción de valor de la herramienta para la toma de decisiones gerenciales.