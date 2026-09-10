# Informe — TP SimpleRisk, Gestión de Riesgos con SimpleRisk

**Materia:** Seguridad de Sistemas — 4to año, Licenciatura en Ciencias de la Computación
**Alumno/a:** Mateo Agustin Falanti - 31645404 - mateofalantiuch@gmail.com 
**Comisión:** g

---

## 1. Preparación del entorno de trabajo

Antes de empezar con la instalación, se preparó el flujo de trabajo en Git de acuerdo a lo pedido en la consigna:

1. Se clonó el repositorio compartido del TP.
2. Se creó una rama individual siguiendo la convención `entrega/<apellido>-<nombre>-<lu>`, sin realizar ningún commit sobre `main`.
3. Dentro de la rama, se armó la estructura de carpetas exigida (`entorno/`, `informe/`, `configuracion/`, `reporte-ejecutivo/`), y se configuró un `.gitignore` para evitar subir credenciales, dumps de base de datos, binarios pesados de VM y logs con datos sensibles.
4. Se decidió trabajar con Docker Desktop sobre Windows como entorno de virtualización, en lugar de una VM completa (VirtualBox/Vagrant), por ser más liviano y reproducible para este caso.
---

## 2. Parte A — Instalación y configuración básica

### 2.1 Instalación reproducible

Se optó por la imagen oficial *all-in-one* `simplerisk/simplerisk` (Apache + PHP + MySQL en un único contenedor), en lugar de `simplerisk-minimal` junto a un contenedor de MySQL separado. La razón de esta elección fue la simplicidad: un solo servicio a levantar, sin necesidad de coordinar variables de entorno entre múltiples contenedores ni de configurar un servicio SMTP adicional, lo cual reduce los puntos de falla en un entorno de prueba individual.

La instalación se documentó mediante un archivo `entorno/docker-compose.yml`, de forma que el entorno completo pueda levantarse con un único comando (`docker compose up -d`) y sea reproducible por cualquier persona que clone la rama, sin pasos manuales adicionales más allá de aceptar el certificado autofirmado del navegador.

Decisiones tomadas en esa configuración:

- **Puertos:** se mapearon los puertos del contenedor (80/443) a `8080`/`8443` en el host, para evitar conflictos con otros servicios que en Windows suelen ocupar los puertos estándar (IIS, otros contenedores, etc.).
- **Persistencia:** la imagen utilizada no documenta oficialmente un volumen externo para los datos de la aplicación. Se optó por dejar esta limitación explícita en la documentación en lugar de asumir una ruta de volumen no confirmada: mientras el contenedor no se elimine (`docker rm`), los datos persisten entre reinicios (`docker compose stop` / `up`).

El proceso de instalación se validó de la siguiente forma:

1. `docker compose up -d` desde `entorno/`.
2. Verificación de que el contenedor está corriendo con `docker ps`.
3. Acceso a `https://localhost:8443/`, aceptando la advertencia de certificado autofirmado.
4. `index.php` redirige automáticamente al wizard de instalación de 6 pasos (idioma, chequeo de requisitos, configuración de base de datos, creación de la cuenta de administrador, etc.), documentado con capturas de pantalla en `informe/capturas/`.
5. Se validó la reproducibilidad ejecutando `docker compose down` seguido de `docker compose up -d`, confirmando que el entorno vuelve a estar disponible sin intervención manual adicional.

Las instrucciones completas para que el docente pueda reproducir el entorno se encuentran también en el `README.md` de esta entrega.

### 2.2 Usuarios y permisos

SimpleRisk no define roles fijos de fábrica (tipo "Admin/Analista/Auditor"): el control de acceso se maneja mediante un conjunto de permisos individuales por checkbox (acceso a cada menú, capacidad de crear/modificar/cerrar riesgos, revisar riesgos por nivel, gestionar auditorías, etc.), más un permiso especial de "Grant Admin" que otorga acceso total. Por lo tanto, los tres roles pedidos por la consigna se construyeron combinando esos permisos de forma deliberada, aplicando el principio de menor privilegio y, cuando fue posible, separación de funciones.

Se crearon los siguientes 3 usuarios (detalle completo de permisos en `configuracion/usuarios.md`, sin incluir contraseñas en ningún archivo del repositorio):

- **`admin_demo` — Administrador de seguridad:** permiso "Grant Admin", con acceso total a la configuración del sistema y a todos los módulos.
- **`analista_demo` — Analista de riesgos:** puede cargar, modificar y planificar el tratamiento de riesgos, y revisar riesgos de cualquier nivel para tener visibilidad completa del registro. No tiene permiso para cerrar riesgos ni aceptar mitigaciones, decisiones que se reservan para el administrador/dueño del riesgo.
- **`auditor_demo` — Auditor:** acceso de solo revisión sobre los riesgos (puede ver y comentar, pero no crear ni modificar) y puede iniciar y aprobar auditorías de compliance, sin permiso de edición sobre riesgos ni tests, para preservar la independencia de la auditoría.

Esta combinación de permisos busca reflejar una separación de funciones real: quien carga y analiza riesgos no es necesariamente quien los aprueba/cierra, y quien audita no puede modificar lo que está auditando.

### 2.3 Riesgo de prueba

Para validar el funcionamiento end-to-end de la instalación, se creó un riesgo de prueba genérico ("Riesgo de prueba — validación de instalación", categoría Operativo), no vinculado al escenario real de la clínica. Se confirmó que el riesgo quedó correctamente registrado y visible en el listado de riesgos del sistema, documentado con una captura en `informe/capturas/`. El desarrollo del registro de riesgos real de la clínica se aborda en la Parte B de este informe.

---

## 3. Parte B — Escenario real: registro de riesgos de la clínica

### 3.1 Contexto del escenario

El escenario planteado es una clínica privada de 120 empleados que atiende 800 pacientes por día, y que maneja tres tipos de información especialmente sensible: historias clínicas digitales, datos de obras sociales y datos de facturación. La clínica acaba de sufrir una auditoría externa que identificó debilidades en su gestión de riesgos, lo cual constituye el disparador de este trabajo y permite asumir que, hasta el momento, no existía un proceso formal de gestión de riesgos en la organización.

### 3.2 Supuestos del escenario

Dado que la consigna no detalla la infraestructura de la clínica, se definieron explícitamente los siguientes supuestos para poder plantear riesgos realistas y no genéricos:

- La clínica opera un sistema de Historia Clínica Electrónica (HCE) accedido por personal médico y administrativo desde estaciones de trabajo y/o tablets.
- Existe una red interna con Wi-Fi para personal, separada de la red de pacientes/visitas.
- La facturación y la integración con obras sociales se realizan mediante un sistema conectado a internet (envío de prestaciones, validación de afiliados).
- Hay guardias con turnos rotativos que operan fuera del horario administrativo habitual, con acceso al sistema fuera de horario.
- No existía previamente un área formal de seguridad de la información; el rol de responsable de seguridad asumido en este TP es una función nueva en la organización.
- Marco legal aplicable: Ley 25.326 (Protección de Datos Personales) y Ley 26.529 (Historia Clínica).

### 3.3 Metodología de evaluación de riesgos

SimpleRisk trabaja de forma nativa con una matriz de Probabilidad × Impacto en escala 1-5. Antes de definir los riesgos concretos, se establecieron los criterios de cada escala para asegurar consistencia y trazabilidad en las justificaciones (detalle completo en el README, sección "Decisiones de diseño"):

- La escala de **Probabilidad** va de "Muy baja" (1, nunca ocurrió en el sector) a "Muy alta" (5, ya ocurrió en la organización o es prácticamente inevitable sin controles).
- La escala de **Impacto** se adaptó específicamente al contexto de una clínica, incorporando el efecto sobre la seguridad y atención del paciente como criterio central, y no solo el efecto técnico u operativo — desde "Insignificante" (1) hasta "Catastrófico" (5, riesgo para la seguridad/vida de pacientes o continuidad de la clínica).
- Se utilizaron las categorías propuestas por la consigna: Confidencialidad, Integridad, Disponibilidad, Legal, Operativo.
- Se definieron de antemano los propietarios naturales de riesgo según su tipo: Jefe de IT/Sistemas, Responsable de Seguridad de la Información, Dirección Médica y Administración/Facturación.

### 3.4 Registro de riesgos

Se definieron 7 riesgos específicos del contexto de la clínica, cubriendo las 5 categorías propuestas y un espectro de niveles (1 bajo, 1 medio, 5 altos). La tabla resumen se encuentra en `configuracion/riesgos.md`; el detalle completo de cada uno es el siguiente:

#### Riesgo 1 — Uso de WhatsApp/mensajería personal para compartir información clínica entre profesionales
- **Categoría:** Confidencialidad
- **Descripción:** El personal médico utiliza WhatsApp en sus celulares personales para compartir fotos de estudios, resultados de laboratorio o comentarios sobre pacientes entre colegas, fuera de cualquier sistema institucional auditable.
- **Activos afectados:** Historias clínicas digitales, datos de salud de pacientes.
- **Probabilidad:** 4 (Alta) — práctica extendida e informal en el sector salud, no requiere ninguna falla técnica.
- **Impacto:** 3 (Moderado) — expone datos de un grupo acotado de pacientes por vez, viola la Ley 25.326 y queda fuera de toda trazabilidad de auditoría.
- **Nivel de riesgo:** Alto
- **Controles existentes:** Ninguno específico; existe una política general de uso aceptable de TI que no contempla mensajería instantánea.
- **Plan de tratamiento:** Mitigar — canal de mensajería institucional cifrado y auditable, y política específica de prohibición de apps personales para datos de pacientes, con capacitación.
- **Propietario:** Dirección Médica.

#### Riesgo 2 — Backups del sistema de HCE sin prueba de restauración
- **Categoría:** Disponibilidad
- **Descripción:** Se realizan backups automáticos diarios de la base de datos del sistema de HCE, pero nunca se probó un proceso de restauración completo.
- **Activos afectados:** Servidor de base de datos de HCE, historias clínicas digitales, continuidad de la atención médica.
- **Probabilidad:** 3 (Media) — la ausencia de pruebas de restauración es una debilidad común en organizaciones sin un área de IT madura.
- **Impacto:** 5 (Catastrófico) — una falla del backup al momento de necesitarse podría implicar pérdida irrecuperable de historias clínicas, comprometiendo la atención segura de pacientes.
- **Nivel de riesgo:** Alto
- **Controles existentes:** Backup automático diario; sin política de retención ni pruebas de restauración documentadas.
- **Plan de tratamiento:** Mitigar — cronograma trimestral de pruebas de restauración en entorno aislado, definición de RTO/RPO y política de retención.
- **Propietario:** Jefe de IT / Sistemas.

#### Riesgo 3 — Doble carga manual de prestaciones entre HCE y facturación a obras sociales
- **Categoría:** Integridad
- **Descripción:** Las prestaciones se registran primero en el sistema de HCE y luego se cargan manualmente de nuevo en el sistema de facturación, por falta de integración entre ambos sistemas.
- **Activos afectados:** Sistema de facturación, datos de obras sociales, ingresos de la clínica.
- **Probabilidad:** 4 (Alta) — proceso manual y repetitivo, con error humano estadísticamente frecuente en el uso normal.
- **Impacto:** 3 (Moderado) — pérdidas económicas por prestaciones no facturadas o rechazos, y observaciones en auditorías de obras sociales, sin comprometer la atención al paciente.
- **Nivel de riesgo:** Alto
- **Controles existentes:** Revisión manual mensual de discrepancias, de forma reactiva.
- **Plan de tratamiento:** Mitigar — evaluar integración automatizada entre HCE y facturación, e implementar conciliación diaria en el corto plazo.
- **Propietario:** Administración/Facturación.

#### Riesgo 4 — Exhibición del nombre completo de pacientes en pantalla de sala de espera
- **Categoría:** Confidencialidad
- **Descripción:** Una pantalla en sala de espera muestra el nombre completo del paciente al llamar su turno, visible para el resto de las personas presentes.
- **Activos afectados:** Dato personal (nombre) del paciente.
- **Probabilidad:** 5 (Muy alta) — ocurre todos los días con cada paciente atendido.
- **Impacto:** 1 (Insignificante) — solo revela la presencia de la persona en la clínica ese día, sin vincularlo a diagnóstico ni especialidad.
- **Nivel de riesgo:** Bajo
- **Controles existentes:** Ninguno específico; práctica estándar del sistema de gestión de turnos.
- **Plan de tratamiento:** Aceptar — el beneficio operativo supera la exposición mínima; se revisará solo si en el futuro se comparte sala de espera con especialidades sensibles (salud mental, infectología).
- **Propietario:** Dirección Médica.

#### Riesgo 5 — Credenciales compartidas en guardias nocturnas del sistema de HCE
- **Categoría:** Integridad / Confidencialidad
- **Descripción:** Durante las guardias nocturnas, el personal comparte un usuario genérico ("guardia_noche") para acceder al sistema de HCE, en lugar de usar cuentas individuales, por agilidad operativa.
- **Activos afectados:** Sistema de HCE, trazabilidad de accesos y modificaciones a historias clínicas.
- **Probabilidad:** 4 (Alta) — práctica ya instalada, sostenida por la presión operativa de las urgencias nocturnas.
- **Impacto:** 3 (Moderado) — rompe la trazabilidad de quién interviene en cada historia clínica, lo cual es tanto un problema operativo como legal (Ley 26.529).
- **Nivel de riesgo:** Alto
- **Controles existentes:** Ninguno; el sistema soporta cuentas individuales pero no se exige su uso en la práctica.
- **Plan de tratamiento:** Mitigar — eliminar el usuario genérico, dar de alta cuentas individuales, y resolver la demora de login con una solución técnica (tarjeta/PIN corto) que no sacrifique trazabilidad por velocidad.
- **Propietario:** Jefe de IT / Sistemas, en conjunto con Dirección Médica.

#### Riesgo 6 — Falta de NDA y cláusulas de protección de datos con proveedores externos de TI
- **Categoría:** Legal
- **Descripción:** Los técnicos externos de mantenimiento de servidores, redes y soporte del sistema de HCE tienen acceso potencial a datos sensibles sin un contrato ni NDA firmado que regule ese tratamiento.
- **Activos afectados:** Historias clínicas digitales, datos de facturación, reputación institucional, cumplimiento normativo.
- **Probabilidad:** 3 (Media) — debilidad estructural presente mientras dure el vínculo, típica de tercerización sin control documental.
- **Impacto:** 4 (Mayor) — ante un incidente originado por el proveedor, la clínica no podría exigir responsabilidad contractual ni demostrar debida diligencia ante el organismo regulador.
- **Nivel de riesgo:** Alto
- **Controles existentes:** Ninguno formal; relación con proveedores manejada de forma informal.
- **Plan de tratamiento:** Mitigar — formalizar con todos los proveedores un contrato con NDA y cláusulas de encargado de tratamiento conforme a la Ley 25.326.
- **Propietario:** Responsable de Seguridad de la Información, en conjunto con Administración.

#### Riesgo 7 — Falta de actualización periódica del stock de insumos críticos
- **Categoría:** Operativo
- **Descripción:** El sistema de gestión de stock de insumos médicos depende de una actualización manual de salidas de depósito, que se retrasa varios días respecto al uso real.
- **Activos afectados:** Sistema de gestión de depósito/insumos, continuidad operativa de áreas asistenciales.
- **Probabilidad:** 3 (Media) — el retraso ya ocurre de forma recurrente, aunque el margen de stock físico a veces absorbe el desfasaje.
- **Impacto:** 2 (Menor) — en el peor caso genera una demora puntual o un pedido innecesario, sin comprometer la atención médica en curso.
- **Nivel de riesgo:** Medio
- **Controles existentes:** Conteo físico de depósito una vez al mes para reconciliar contra el sistema.
- **Plan de tratamiento:** Mitigar — registrar la salida del insumo al momento del uso (ej. escaneo de código de barras) en lugar de carga diferida.
- **Propietario:** Administración/Facturación.

---
3.5 Planes de acción para riesgos de nivel alto

Se definieron 3 planes de acción asociados a riesgos de nivel Alto del registro, seleccionados de forma de cubrir distintos tipos de tratamiento (técnico, de procesos/personas, y legal/contractual):

Plan de acción 1 — asociado al Riesgo 2 (Backups del sistema de HCE sin prueba de restauración)
Título: Implementación de pruebas trimestrales de restauración de backups.
Descripción: Diseñar y ejecutar un cronograma de pruebas de restauración del backup de la base de datos de HCE en un entorno aislado, documentando resultados, tiempos de restauración obtenidos (RTO real) y definiendo una política formal de retención.
Fecha de vencimiento: 60 días desde la aprobación del plan.
Responsable: Jefe de IT / Sistemas.
Presupuesto estimado: USD 500–1000 (horas de trabajo del equipo de IT y, si aplica, un entorno de pruebas separado).
Estado inicial: No iniciado / Pendiente.
Plan de acción 2 — asociado al Riesgo 5 (Credenciales compartidas en guardias nocturnas)
Título: Eliminación de usuario genérico y alta de accesos individuales para el personal de guardia.
Descripción: Dar de baja el usuario compartido "guardia_noche", crear cuentas individuales para todo el personal que realiza guardias, y evaluar una solución de acceso rápido (tarjeta/PIN corto) que no sacrifique trazabilidad por velocidad de login.
Fecha de vencimiento: 45 días.
Responsable: Jefe de IT / Sistemas, en coordinación con Dirección Médica para la capacitación del personal.
Presupuesto estimado: USD 300–600 (principalmente horas de configuración; más si se implementa hardware de acceso rápido).
Estado inicial: No iniciado / Pendiente.
Plan de acción 3 — asociado al Riesgo 6 (Falta de NDA con proveedores externos de TI)
Título: Formalización contractual con proveedores externos de TI.
Descripción: Redactar y firmar con cada proveedor externo con acceso a sistemas o datos un contrato que incluya acuerdo de confidencialidad (NDA) y cláusulas de encargado de tratamiento de datos personales conforme a la Ley 25.326.
Fecha de vencimiento: 90 días (incluye tiempo de negociación legal).
Responsable: Responsable de Seguridad de la Información, en conjunto con Administración.
Presupuesto estimado: USD 800–1500 (asesoría legal externa para la redacción de los contratos).
Estado inicial: No iniciado / Pendiente.


4. Parte C — Análisis crítico y profundización
4.1 Comparación metodológica: SimpleRisk vs. NIST SP 800-30

SimpleRisk trabaja de forma nativa con una matriz clásica de Probabilidad × Impacto en escala 1-5 (método "Classic"), que fue la utilizada para el registro de riesgos de este TP. Como metodología alternativa para comparar se eligió NIST SP 800-30 ("Guide for Conducting Risk Assessments").

Ventajas y desventajas de cada enfoque:

La matriz clásica de SimpleRisk es simple, visual y de baja curva de aprendizaje: cualquier persona sin formación previa en gestión de riesgos puede completarla, y permite obtener rápidamente una priorización útil (como la Tabla de riesgos de este TP). Su principal debilidad es que los valores de probabilidad e impacto se asignan de forma bastante subjetiva, sin un desglose formal de fuentes de amenaza, capacidad del atacante o vulnerabilidad específica, lo cual puede generar inconsistencias si distintas personas cargan riesgos con criterios distintos.

NIST SP 800-30, en cambio, propone un proceso mucho más estructurado: identifica fuentes de amenaza (adversarias y no adversarias), vulnerabilidades y condiciones predisponentes, y determina la probabilidad considerando explícitamente la capacidad e intención del atacante, además de definir el impacto en función de los tiers de la organización (organizacional, de misión/proceso de negocio, y de sistema de información). Esto la hace mucho más rigurosa y defendible ante un auditor o regulador, pero a costa de requerir considerablemente más tiempo, expertise específico y documentación por cada riesgo evaluado.

Contexto en el que conviene cada una: la matriz clásica de SimpleRisk resulta más adecuada para organizaciones que, como la clínica de este escenario, recién están iniciando un programa formal de gestión de riesgos y necesitan una primera fotografía rápida y accionable. NIST SP 800-30 es preferible cuando existe una exigencia regulatoria fuerte, se necesita auditar en profundidad un sistema crítico específico, o la organización ya cuenta con un programa de riesgos maduro que puede sostener el esfuerzo adicional que exige esta metodología.

4.2 Integración con herramienta externa

Se documenta (sin implementar) una integración entre SimpleRisk y Slack, elegida por ser una herramienta de mensajería de equipo ampliamente utilizada y por encajar con el caso de uso de notificar automáticamente la aparición de riesgos de nivel alto.

SimpleRisk no incluye un conector nativo a Slack, pero expone una API RESTful bajo /api (con autenticación por cookie, o mediante API keys si se cuenta con el módulo "API Extra") pensada específicamente para integrarlo con sistemas externos. La integración propuesta funcionaría de la siguiente manera:

Un proceso programado (cron job) consulta periódicamente la API de SimpleRisk en busca de riesgos nuevos o modificados con nivel "Alto" o "Muy Alto".
Al detectar uno, arma un mensaje con los datos clave del riesgo (nombre, categoría, nivel, propietario) y lo envía a un canal de Slack mediante un Incoming Webhook (una URL provista por Slack para publicar mensajes en un canal específico, sin necesidad de desarrollar una app de Slack completa).
Esto brinda visibilidad inmediata al equipo de seguridad y a la Dirección ante la aparición de riesgos críticos, sin depender de que alguien ingrese manualmente a revisar el sistema.

Esta integración no fue implementada en el marco de este TP, ya que la consigna la establece como parte obligatoria solo en su etapa de investigación y documentación (una implementación real, aunque sea con un webhook simple, corresponde a puntos extra dentro de la Parte D, optativa).

5. Cierre

Con esto queda completo el desarrollo de las partes obligatorias del TP (A, B y C). No se desarrollaron actividades de la Parte D (optativas) porque no organice bien mis tiempos para hacerlo disculpe.