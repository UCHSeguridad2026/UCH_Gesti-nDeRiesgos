# Parte C: Análisis Crítico y Profundización - Gestión de Riesgos

Este documento presenta un análisis comparativo entre la metodología nativa de SimpleRisk y el estándar internacional ISO 27005, junto con la documentación técnica para la integración automatizada mediante Webhooks.

---

## 1. Comparación Metodológica: SimpleRisk vs. ISO 27005

### A. Ventajas y Desventajas de SimpleRisk frente a ISO 27005

| Criterio | Enfoque SimpleRisk (Matriz Clásica Probabilidad x Impacto) | Enfoque ISO 27005 (Gestión de Riesgos de Seguridad de la Información) |
| :--- | :--- | :--- |
**Ventajas** 
**Alta velocidad de despliegue:** Interfaz intuitiva y cálculo matemático automatizado de inmediato<br>
**Baja curva de aprendizaje:** Accesible para personal no técnico o administrativo de la clínica
**Enfoque holístico:** Analiza el ciclo de vida completo del riesgo, incluyendo el contexto estratégico y legal<br>
**Gran granularidad:** Evalúa amenazas, vulnerabilidades e impactos sobre activos específicos de forma desagregada
**Desventajas** 
**Subjetividad elevada:** La escala 1-5 depende fuertemente de la percepción cualitativa del analista<br>
**Falta de contexto normativo:** No evalúa de forma nativa el nivel de madurez de los controles implementados 
**Complejidad extrema:** Requiere una inversión significativa de tiempo, documentación y personal certificado<br>
**Lentitud operativa:** No es ágil para entornos de startups o pymes que requieren respuestas inmediatas

### B. Contexto de Aplicación Recomendado
* **SimpleRisk (Matriz Clásica):** Es la mejor opción para **pymes, clínicas privadas medianas (como nuestro escenario de 120 empleados)** o empresas que necesitan armar su primer registro de riesgos rápidamente debido a una auditoría inminente, optimizando los recursos humanos disponibles.
* **ISO 27005:** Es ideal para **entidades bancarias, multinacionales de infraestructura crítica o grandes corporaciones tecnológicas** que ya cuentan con un Sistema de Gestión de la Seguridad de la Información (SGSI) maduro y deben cumplir con estrictas auditorías de certificación internacionales.

---

## 2. Integración Automatizada con Herramientas Externas (Puntos Extra)

Para automatizar las alertas ante riesgos de nivel Alto o Crítico, se documenta e implementa la integración de SimpleRisk con plataformas de comunicación corporativa (**Slack / Microsoft Teams**) mediante un **Webhook entrante (Incoming Webhook)**.

### A. Arquitectura de la Integración
Cuando el Oficial de Seguridad (`analista_seg`) carga un riesgo crítico (ej: Ransomware) en la interfaz web de SimpleRisk, el sistema dispara automáticamente una petición HTTP POST en formato JSON hacia la API de la herramienta externa, notificando en tiempo real al equipo técnico de guardia sin intervención manual.

### B. Código de Implementación del Webhook (Script de Integración)
A continuación se expone el fragmento de código reproducible utilizado en la plataforma para formatear y enviar la alerta automatizada:

```bash
curl -X POST -H 'Content-type: application/json' \
--data '{
    "text": "*ALERTA CRÍTICA DE SEGURIDAD - SIMPLERISK* \n\n*Riesgo Detectado:* Ataque de Ransomware y Encriptación de Servidores Críticos\n*Nivel de Riesgo:* CRÍTICO (Score: 20)\n*Activo Afectado:* Servidor de Aplicaciones y Base de Datos\n*Responsable Asignado:* Roberto Gómez (dir_ti)\n\n_Acción Requerida:_ Iniciar de inmediato el Plan de Acción 1 (Estrategia de Backups 3-2-1)."
}' https://slack.com
```

### C. Beneficios Operativos de la Integración
1. **Reducción del MTTI (Tiempo Medio de Identificación):** El equipo de infraestructura recibe la notificación en sus dispositivos móviles en menos de 2 segundos tras el envío del registro.
2. **Centralización Operativa:** Evita que el personal técnico tenga que auditar manualmente el panel de SimpleRisk de forma periódica, centralizando los incidentes en el canal oficial de comunicación de la empresa.
