# Informe — TP SimpleRisk, Gestión de Riesgos con SimpleRisk

**Materia:** Seguridad de Sistemas — Licenciatura en Ciencias de la Computación
**Alumno:** Martín Carrera - 45715448 - tinchocarrera45@gmail.com
**Comisión:** G

---

### 1. Preparación del entorno de trabajo
Antes de comenzar con la instalación, se estructuró el flujo de trabajo en Git:
* Se clonó el repositorio compartido del TP y se creó una rama individual siguiendo la convención `entrega/carrera-martin-45715448`.
* Se armó la estructura de carpetas exigida (`entorno/`, `documentacion/`, `configuracion/`).
* Se decidió trabajar con Docker Desktop sobre Windows como entorno de virtualización por ser más liviano y reproducible.

### 2. Parte A — Instalación y configuración básica
**2.1 Instalación reproducible**
Se utilizó la imagen oficial `simplerisk/simplerisk` configurada mediante un archivo `docker-compose.yml`. El entorno se levanta con el comando `docker compose up -d`. Se mapearon los puertos al 8443 en el host. La reproducibilidad se validó deteniendo y levantando los contenedores, verificando la persistencia de datos y el acceso al sistema.

**2.2 Usuarios y permisos**
Se aplicó el principio de menor privilegio creando 3 roles específicos:
* **Administrador:** Permiso "Grant Admin", acceso total y aprobación de mitigaciones.
* **Analista de Riesgos:** Carga, modificación y planificación de mitigaciones, sin permisos de cierre.
* **Auditor:** Solo revisión para preservar la independencia de la auditoría.

**2.3 Riesgo de prueba**
Se creó un riesgo de prueba inicial genérico para validar la correcta persistencia en la base de datos antes de proceder con el escenario real.

### 3. Parte B — Escenario real: registro de riesgos de la clínica
**3.1 Contexto y Supuestos**
El escenario es una clínica privada de 120 empleados que atiende 800 pacientes diarios[cite: 1]. Se asume que no existe personal de ciberseguridad dedicado 24/7 y que se manejan datos sensibles regulados por la Ley de Protección de Datos Personales.

**3.2 Registro de riesgos (Matriz Cualitativa)**
Se definieron 7 riesgos utilizando la matriz cualitativa nativa:
1. **Ransomware en Historias Clínicas (Crítico):** Paralización total de la atención médica y pérdida de acceso a datos sensibles[cite: 1].
2. **Caída del validador de Obras Sociales (Crítico):** Freno inmediato en la facturación y validación de turnos en recepción[cite: 1].
3. **Sanciones legales por fuga de datos (Alto):** Daño reputacional y severas multas por incumplimiento de la Ley de Protección de Datos Personales[cite: 1].
4. **Falla de hardware en servidor principal (Alto):** Interrupción de la operación por desgaste del equipamiento físico[cite: 1].
5. **Phishing a empleados de la clínica (Alto):** Brecha de seguridad inicial a través de ataques de ingeniería social al personal[cite: 1].
6. **Alteración de datos de facturación (Medio):** Posible fraude interno por abuso de privilegios.
7. **Corte de suministro eléctrico (Medio):** Cortes zonales imprevistos.

**3.3 Planes de acción**
Se definieron 3 planes de acción para los riesgos de mayor nivel:
* **Plan 1 (Ransomware):** Implementación de Backups EDR. Vencimiento: Diciembre 2026. Presupuesto: $100,001 a $200,000[cite: 1].
* **Plan 2 (Validador):** Enlace Backup y Pre-facturación Offline. Vencimiento: Noviembre 2026. Presupuesto: $0 a $100,000[cite: 1].
* **Plan 3 (Phishing):** Capacitación y 2FA. Vencimiento: Octubre 2026. Presupuesto: $0 a $100,000[cite: 1].

### 4. Parte C — Análisis crítico
**4.1 SimpleRisk vs. NIST SP 800-30**
La matriz de SimpleRisk es ágil y de baja curva de aprendizaje, ideal para la clínica que recién inicia su gestión de riesgos. Por el contrario, NIST SP 800-30 ofrece un desglose formal de vulnerabilidades y amenazas, siendo más rigurosa pero requiriendo mayor tiempo y madurez organizacional.

**4.2 Integración externa (Slack)**
Se documenta la posibilidad de integrar SimpleRisk con Slack mediante su API RESTful. Un proceso programado podría detectar riesgos "Altos" y enviar alertas mediante un Webhook a un canal de Slack, brindando visibilidad inmediata a la Dirección sin requerir acceso manual al sistema.

*Cierre:* Con esto queda documentado el desarrollo de las partes obligatorias. No se desarrollaron actividades optativas de la Parte D.