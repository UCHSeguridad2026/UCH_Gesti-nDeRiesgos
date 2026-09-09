# Informe — TP Gestión de Riesgos con SimpleRisk

**Alumno:** Uriel Cabrera — LU 31673361

---

## Parte A — Instalación y configuración básica

### A.1 Instalación reproducible

**Método elegido:** Docker Compose sobre la imagen oficial
`simplerisk/simplerisk`. La justificación de esta elección frente a la variante
`simplerisk-minimal` está detallada en el README, sección 3.1.

**Entorno de ejecución:** Windows 11 con Docker Desktop sobre backend WSL 2.

**Procedimiento:**

1. Verificación de que la virtualización esté habilitada en la UEFI/BIOS y de
   que Docker Desktop opere sobre WSL 2.
2. Descarga de la imagen: `docker compose pull`.
3. Levantamiento del contenedor: `docker compose up -d`.
4. Verificación del estado: `docker ps`.
5. Acceso a `https://localhost:8443` y creación de la cuenta administradora.

El archivo `entorno/setup.sh` automatiza los pasos 2 a 5, incorporando además
la verificación previa de prerrequisitos (presencia de Docker, disponibilidad
del daemon y de los puertos 8080/8443) y una espera activa hasta que la
aplicación responda.

**Verificación del despliegue:**

El contenedor `simplerisk_app` se reporta como `Up (healthy)`, con los puertos
`8080→80` y `8443→443` publicados. El estado *healthy* proviene del
`healthcheck` declarado en `docker-compose.yml`, que consulta la aplicación por
HTTPS aceptando el certificado autofirmado. Es decir, la verificación no
confirma únicamente que el contenedor esté en ejecución, sino que la aplicación
responde efectivamente por el puerto esperado.

> Evidencia: `capturas/a1-contenedor-running.png`

**Observación sobre credenciales iniciales:**

En el primer acceso, la aplicación presenta la pantalla *Default Admin Account
Creation*. SimpleRisk no distribuye una cuenta administradora preconfigurada:
obliga a definir usuario y contraseña durante la instalación. Esto elimina el
riesgo asociado a credenciales por defecto conocidas, que constituye una de las
debilidades más habituales en despliegues de aplicaciones web y una vía de
acceso inicial frecuentemente explotada.

> Evidencia: `capturas/a1-simplerisk-admin-creation.png`,
> `capturas/a1-home-simplerisk.png`

### A.2 Usuarios y permisos

Se definieron tres usuarios con roles diferenciados: administrador, analista de
riesgos y auditor interno. La matriz completa de permisos, con la denominación
exacta que emplea SimpleRisk, está en `../configuracion/usuarios.md`.

**Modelo de asignación.** SimpleRisk permite asignar permisos por dos vías: un
rol predefinido seleccionable desde el formulario de alta, o la asignación
granular mediante la sección *User Responsibilities*. Se optó por la asignación
granular para que cada permiso otorgado responda a una decisión explícita y
documentable, en lugar de heredar un conjunto cuyo contenido no queda registrado
en la entrega.

**Criterios aplicados.** La configuración no se limita a diferenciar niveles de
acceso, sino que materializa tres principios:

1. *Menor privilegio.* El auditor conserva únicamente permisos de acceso a los
   módulos y visualización de excepciones. No posee ninguna capacidad de
   creación, modificación, aprobación ni eliminación.

2. *Separación de funciones.* El analista puede planificar mitigaciones pero no
   aceptarlas. La propuesta de tratamiento y su aprobación quedan en manos
   distintas, de modo que ninguna cuenta controla por sí sola el ciclo completo
   de decisión sobre un riesgo.

3. *Escalamiento por criticidad.* El analista revisa riesgos hasta nivel medio;
   los niveles alto y muy alto quedan reservados al administrador. Esto guarda
   coherencia con la escala adoptada, donde el nivel Crítico implica
   escalamiento a dirección.

**Verificación.** La restricción no se declara únicamente por configuración: se
comprobó iniciando sesión con la cuenta del auditor y constatando que la interfaz
efectivamente no ofrece las acciones restringidas. La diferencia más visible es
la ausencia del ícono de configuración en la barra superior, presente en la
sesión del administrador. El auditor visualiza el riesgo registrado y los paneles
de reporte, pero la interfaz no le expone ninguna acción de creación o
modificación.

> Evidencia: `capturas/a2-usuarios-creados.png`,
> `capturas/a2-analista-riesgos-creacion.png`,
> `capturas/a2-auditor-interno-creacion.png`,
> `capturas/a2-permisos-analista-1.png` a `-3.png`,
> `capturas/a2-permisos-auditor.png`, `capturas/a2-verificacion-auditor.png`

### A.3 Primer riesgo de prueba

Se registró un riesgo de validación con el asunto *PRUEBA - Validación de alta de
riesgos*, identificado explícitamente como tal para no confundirlo con el registro
de riesgos del escenario, que se desarrolla en la Parte B.

| Campo | Valor |
|---|---|
| ID | 1001 |
| Categoría | Policy and Procedure |
| Origen del riesgo | Process |
| Método de scoring | Classic |
| Probabilidad actual | Credible (3) |
| Impacto actual | Moderate (3) |
| Tecnología | Backups |
| Equipo | Information Security |
| Propietario | Analista De Riesgos |
| Manager del propietario | Administrador de Sistemas |
| Estado | New |

**Resultado obtenido.** Con la configuración que trae la instalación por defecto,
SimpleRisk calculó un riesgo inherente y residual de **3.6**, clasificado como
*Low*. El riesgo residual coincide con el inherente porque aún no se registraron
controles ni mitigaciones sobre él.

**Inconsistencia detectada.** Ese resultado no se correspondía con la valoración
esperada. Según la escala de la plantilla A03, una probabilidad *Posible* (3)
combinada con un impacto *Moderado* (3) arroja un valor de 9, que cae dentro del
rango 5–9 y por lo tanto corresponde al nivel **Medio**. La aplicación mostraba
en cambio 3.6 y lo clasificaba como *Low*.

La discrepancia no era menor: un riesgo de nivel medio presentado como bajo puede
quedar fuera de un plan de tratamiento. Esto motivó revisar la configuración de
scoring de la herramienta antes de continuar con el registro de riesgos del
escenario, ya que de haberse mantenido, los siete riesgos de la Parte B habrían
quedado sistemáticamente subvaluados respecto del instrumento de la cátedra.

El análisis de esa revisión y la configuración finalmente adoptada se desarrollan
en la Parte C, sección C.1. La configuración resultante está documentada en el
README, sección 3.4.

**Validación funcional del entorno.** Independientemente del ajuste posterior, el
alta del riesgo confirma que la cadena completa opera correctamente: la
aplicación acepta el formulario, persiste el registro en la base de datos,
calcula el score conforme a la fórmula configurada y lo refleja en el panel de
reportes.

> Evidencia: `capturas/a3-riesgo-prueba-formulario.png`,
> `capturas/a3-riesgo-prueba-detalle.png`

---

## Parte B — Escenario real

### Contexto y supuestos

El enunciado aporta cinco datos sobre la organización: 120 empleados, 800
pacientes diarios, historias clínicas digitales, datos de obras sociales y
facturación, y una auditoría externa reciente que identificó debilidades en la
gestión de riesgos. Todo análisis de riesgos requiere además conocer la
infraestructura, la dotación técnica y el marco normativo aplicable, de modo que
se asumen los siguientes supuestos, explicitados porque cada uno sostiene al
menos una de las valoraciones del registro:

| # | Supuesto | Valoraciones que sostiene |
|---|---|---|
| S1 | Área de sistemas de dos a tres personas, sin rol dedicado a seguridad de la información | Probabilidad de R01, R03 |
| S2 | Historia clínica electrónica de proveedor externo, alojada en servidores propios de la clínica, con soporte remoto del proveedor | Impacto de R01; alcance de R07 |
| S3 | Sala de servidores propia dentro del edificio, sin redundancia de centro de datos | Probabilidad e impacto de R06 |
| S4 | Personal asistencial con alta rotación y usuarios compartidos por turno en algunos sectores | Probabilidad de R02 |
| S5 | Red interna sin segmentación entre el segmento clínico y el administrativo | Probabilidad de R01 |
| S6 | Backups diarios automatizados a disco local, sin copia fuera de línea ni prueba de restauración documentada | Probabilidad e impacto de R05 |
| S7 | Marco normativo aplicable: Ley 25.326 de Protección de los Datos Personales. Los datos de salud revisten carácter de datos sensibles y están sujetos a un régimen agravado | Impacto de R02, R04; existencia de R07 |
| S8 | Intercambio mensual de planillas de facturación con obras sociales por correo electrónico, sin procedimiento formalizado | Probabilidad de R04 |

Estos supuestos describen una organización verosímil para el tamaño y el rubro
indicados: una clínica de porte medio con sistemas digitalizados pero sin una
función de seguridad de la información constituida, que es precisamente la
situación que la auditoría externa vino a señalar.

### Registro de riesgos

Se identificaron siete riesgos específicos del contexto de la clínica. El
registro completo —con descripción, activos afectados, justificación individual
de cada valor de probabilidad e impacto, controles existentes y plan de
tratamiento— está en `../configuracion/riesgos.md`.

**Criterio de selección.** El conjunto cubre deliberadamente las tres dimensiones
clásicas de la seguridad de la información y agrega la dimensión legal, que en
una institución de salud no es accesoria:

| Dimensión | Riesgos |
|---|---|
| Confidencialidad | R02, R03, R04 |
| Integridad | R01, R03 |
| Disponibilidad | R01, R05, R06 |
| Legal | R04, R07 |

Ninguno de los siete es un riesgo genérico aplicable a cualquier organización:
todos se apoyan en una característica propia del escenario —el volumen de
atención diaria, la naturaleza sensible de la historia clínica, el vínculo
operativo con obras sociales o la infraestructura descrita en los supuestos.

**Carga en la herramienta.** Los siete riesgos fueron registrados en SimpleRisk
con la cuenta `analista_riesgos`, que es el rol al que corresponde la
identificación y valoración según la matriz de permisos de la Parte A.2. El campo
*Submitted By* de cada riesgo deja constancia de ello, lo que verifica en la
práctica que el permiso *Able to Submit New Risks* opera como fue configurado.

Cada riesgo lleva su código del registro en el campo *External Reference ID*, y
la justificación de probabilidad e impacto se transcribió en *Additional Notes*,
de modo que el razonamiento resulte consultable desde la propia herramienta y no
únicamente desde este repositorio.

| Ref | ID SimpleRisk | Valor | Nivel |
|---|:-:|:-:|---|
| R01 | 1002 | 20 | Very High |
| R02 | 1003 | 16 | Very High |
| R03 | 1004 | 16 | Very High |
| R04 | 1005 | 16 | Very High |
| R05 | 1006 | 15 | High |
| R07 | 1008 | 12 | High |
| R06 | 1007 | 9 | Medium |

Los valores y niveles calculados por SimpleRisk coinciden exactamente con los de
la plantilla A03 consignados en `../configuracion/riesgos.md`, lo que confirma
que la configuración de scoring descrita en el README, sección 3.4, produce el
resultado buscado.

> Evidencia: `capturas/b1-riesgos-cargados.png`,
> `capturas/b1-riesgo-r01-detalle.png` a `b1-riesgo-r07-detalle.png`

**Distribución resultante.** Cuatro riesgos de nivel Crítico, dos de nivel Alto y
uno Medio. La concentración en los niveles superiores es coherente con el punto
de partida planteado en el enunciado: una organización que acaba de recibir una
auditoría con hallazgos y que aún no implementó controles sistemáticos.

**Incidencia de la evidencia sectorial sobre las valoraciones.** Las
probabilidades se contrastaron contra el *2026 Data Breach Investigations Report*
de Verizon, en su edición correspondiente al sector Healthcare. El contraste no
fue meramente confirmatorio: modificó el registro en dos puntos.

R04 —fuga de datos por envío inseguro de planillas— había sido valorado
inicialmente con probabilidad 3. El informe identifica *Misdelivery* como el error
más frecuente del sector y consigna que el patrón de errores diversos figura entre
los tres principales de forma sostenida desde 2014. Esa evidencia justificó
elevarlo a 4, con lo que el riesgo pasó de nivel Alto a Crítico. El resultado es
contraintuitivo y por eso relevante: un error administrativo cotidiano alcanza el
mismo nivel que un ataque de ransomware.

En sentido inverso, R02 —acceso indebido a historias clínicas— encontró un dato
en contra: el patrón *Privilege Misuse* representa apenas el 3 % de las brechas
del sector, en descenso sostenido. Se mantuvo la valoración en 4 por las
condiciones específicas de la organización, dejando constancia expresa de la
tensión en la ficha del riesgo. Un registro que sólo incorpora la evidencia
favorable a sus conclusiones no resiste una revisión externa.

### Planes de acción

Se definieron cuatro planes, uno por cada riesgo de nivel Crítico, detallados en
`../configuracion/riesgos.md`. El primero (PA01) atiende simultáneamente R01 y
R05, dado que la copia de respaldo fuera de línea con restauración verificada es
el control determinante en ambos: es lo que convierte un incidente de ransomware
de pérdida definitiva en interrupción recuperable.

El orden de prioridad no responde únicamente al valor de riesgo. PA04 atiende un
riesgo Crítico con el menor presupuesto y el menor plazo de todo el plan, por lo
que ofrece la mayor reducción de riesgo por unidad de inversión; se trata de un
control de proceso, no de una inversión tecnológica. PA03, en cambio, requiere el
plazo más extenso porque su componente de concientización sólo produce efecto
medible sostenido en el tiempo.

### Reporte ejecutivo
Ver `../reporte-ejecutivo/reporte.pdf`.

---

## Parte C — Análisis crítico

### C.1 Comparación metodológica

*(Pendiente: comparación con la metodología alternativa elegida —
FAIR, OCTAVE, NIST SP 800-30 o ISO 27005—, ventajas, desventajas y contexto de
aplicación de cada una.)*

**Hallazgo: la escala de presentación no es neutral.**

Este hallazgo no fue buscado. Surgió al advertir que el resultado del riesgo de
validación (Parte A.3) no coincidía con el que arrojaba la plantilla A03 para la
misma valoración, y de rastrear a qué se debía esa diferencia.

**Primera observación: la normalización.** La pantalla *Configure → Risk Formula*
reveló que SimpleRisk aplica por defecto la opción *Normalize scoring on a 0-10
scale*. La fórmula sigue siendo Probabilidad × Impacto, pero el producto se
reescala mediante (P × I) / 25 × 10. Por eso un valor de 9 se presentaba como
3.6. Ambos números expresan la misma valoración en escalas distintas.

**Segunda observación: los umbrales quedan desalineados.** Al desactivar la
normalización, el valor pasó correctamente a 9, pero la clasificación se volvió
*High* en lugar de *Medium*. La causa es que los umbrales que trae la instalación
(10.1 / 7.0 / 4.0 / 0.0) están dimensionados para la escala 0–10. Aplicados sobre
valores de 1 a 25 desplazan toda la clasificación hacia arriba: cualquier riesgo
con producto igual o mayor a 10.1 queda como *Very High*, lo que abarca más de la
mitad de la matriz.

Es decir que la configuración por defecto subvaluaba, y desactivar la
normalización sin ajustar los umbrales sobrevaluaba. Un mismo análisis comunicaba
tres severidades distintas:

| Configuración de SimpleRisk | Valor mostrado | Nivel comunicado | Nivel según A03 |
|---|:-:|---|---|
| Normalización activada, umbrales por defecto | 3.6 | Low | Medio |
| Normalización desactivada, umbrales por defecto | 9 | High | Medio |
| Normalización desactivada, umbrales alineados | 9 | Medium | Medio |

**Configuración adoptada.** Se desactivó la normalización y se redefinieron los
cuatro umbrales según los cortes de la plantilla A03 (Very High ≥ 16, High ≥ 10,
Medium ≥ 5, Low ≥ 0). Recién con ambos ajustes la herramienta y el instrumento
formal de la cátedra comunican el mismo nivel para una misma valoración.

**Implicancia para la comparación metodológica.** El episodio ilustra una
limitación del enfoque de matriz probabilidad × impacto que suele pasarse por
alto: la aparente objetividad del número depende de decisiones de configuración
—escala de presentación y cortes de clasificación— que rara vez se documentan y
que quien lee el reporte no puede inferir del resultado.

En un registro de riesgos elevado a dirección, la etiqueta de nivel es lo que
determina la asignación de presupuesto y la urgencia del tratamiento. Una
instalación no revisada puede llevar a omitir riesgos que merecían plan de acción
o, en el escenario inverso, a saturar el plan de falsos críticos. La metodología
alternativa que se analiza a continuación aborda este problema de otro modo.

> Evidencia: `capturas/c1-matriz-normalizada-0-10.png`,
> `capturas/c1-matriz-sin-normalizar-1-25.png`,
> `capturas/c1-score-normalizado-3-6.png`,
> `capturas/c1-score-sin-normalizar-9.png`,
> `capturas/c1-umbrales-configurados.png`

### C.2 Integración con herramienta externa
*(Pendiente.)*

---

## Referencias

*(Pendiente.)*
