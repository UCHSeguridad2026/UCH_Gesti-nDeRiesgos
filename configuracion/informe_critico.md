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


---

## 3. Parte D: Actividades Optativas (Bonificación +1 Punto)

### Actividad D1: Análisis de Seguridad de la Instalación por Defecto de SimpleRisk

Evaluando la arquitectura de contenedores desplegada localmente mediante Docker Compose, se identificaron tres (3) vulnerabilidades de configuración y malas prácticas críticas en la instalación por defecto, proponiendo sus respectivas mitigaciones de nivel corporativo:

#### 1. Exposición de Credenciales en Texto Plano (Docker Compose Variables)
* **Vulnerabilidad:** Las contraseñas del motor de base de datos (`MYSQL_PASSWORD` y `MYSQL_ROOT_PASSWORD`) están hardcodeadas directamente en texto plano dentro del archivo `docker-compose.yml`. Cualquier usuario con acceso de lectura al repositorio de Git puede comprometer la integridad total de la base de datos de la clínica.
* **Mitigación:** Implementar el uso de archivos de entorno ocultos (`.env`) agregados a la directiva `.gitignore`, o utilizar mecanismos de almacenamiento seguro como **Docker Secrets** para inyectar las credenciales en memoria durante el tiempo de ejecución (runtime).

#### 2. Ausencia de Headers HTTP de Seguridad y Uso de HTTP Nativo
* **Vulnerabilidad:** La configuración predeterminada del servidor Apache dentro de la imagen de SimpleRisk expone la plataforma a ataques de redirección maliciosa o secuestro de clics (Clickjacking) debido a la ausencia de headers HTTP críticos como `X-Frame-Options: DENY`, `Strict-Transport-Security` (HSTS) y `Content-Security-Policy` (CSP).
* **Mitigación:** Configurar un proxy inverso perimetral (como **Nginx** o **Traefik**) por delante del contenedor de SimpleRisk. Este proxy será el responsable exclusivo de forzar conexiones seguras HTTPS mediante certificados válidos y de inyectar las cabeceras de seguridad requeridas en cada petición web.

#### 3. Uso de la Cuenta Administrativa por Defecto ('admin')
* **Vulnerabilidad:** La instalación inicial fuerza al sistema a operar bajo un identificador predecible y estandarizado (`admin`), lo que simplifica de manera drástica la ejecución de ataques automatizados de fuerza bruta o diccionario orientados al panel de inicio de sesión de la clínica.
* **Mitigación:** Aplicar una política estricta de endurecimiento (Hardening) que consista en la creación inmediata de un usuario con privilegios elevados con nomenclatura corporativa compleja (ej: `adm_mendoza_sec`), seguida de la **desactivación o baja absoluta e inmediata de la cuenta nativa `admin`** en la base de datos.
