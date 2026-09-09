# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

**Seguridad de Sistemas**

---

## Datos del alumno

| Campo | Dato |
|---|---|
| Apellido y nombre | Barbero, Lautaro |
| Libreta universitaria | 44820797 |
| Email institucional | *(completar)* |
| Comisión | *(completar)* |
| Branch de entrega | `entrega/barbero-lautaro-44820797` |

---

## Contenido de la entrega

```
entregas/barbero-lautaro-44820797/
├── README.md                        Este archivo
├── .gitignore                       Exclusiones de versionado
├── entorno/
│   └── docker-compose.yml           Despliegue reproducible de SimpleRisk
├── informe/
│   ├── informe.md                   Desarrollo completo del TP (Partes A, B, C y D)
│   └── capturas/                    Evidencia de la configuración y la carga
├── configuracion/
│   ├── usuarios.md                  Usuarios, roles y permisos (sin contraseñas)
│   └── riesgos.md                   Matriz de riesgos completa
├── scripts/
│   └── notificar_riesgos.py         Integración SimpleRisk → Discord (Parte C.2 / D2)
└── reporte-ejecutivo/
    └── reporte.pdf                  Reporte para el directorio de la clínica
```

**Orden de lectura sugerido:** `informe.md` desarrolla el trabajo y remite a los demás documentos. `riesgos.md` contiene el análisis completo según la plantilla de matriz de riesgos de la cátedra.

---

## Cómo levantar el entorno

### Requisitos

- Docker y el complemento Docker Compose
- Puertos 80 y 443 libres en el equipo anfitrión

Verificación previa:

```bash
docker --version
docker compose version
```

Si Docker no está instalado (ejemplo para distribuciones basadas en Arch):

```bash
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker.service
sudo usermod -aG docker $USER
```

El cambio de grupo requiere cerrar y reabrir la sesión.

### Despliegue

Desde la raíz del repositorio:

```bash
docker compose -f entregas/barbero-lautaro-44820797/entorno/docker-compose.yml up -d
```

La primera ejecución descarga la imagen (varios cientos de MB) y puede demorar. Verificar que el contenedor esté activo:

```bash
docker ps
```

Esperar entre 30 y 60 segundos antes de acceder: MariaDB necesita inicializarse.

### Acceso

Abrir **https://localhost/** en el navegador.

El certificado es autofirmado, por lo que el navegador mostrará una advertencia de seguridad. Es esperable en un despliegue local. En Firefox: *Avanzado → Aceptar el riesgo y continuar*. En Chrome o derivados: *Configuración avanzada → Acceder a localhost*.

Credenciales por defecto de una instancia recién desplegada: usuario `admin`, contraseña `admin`.

### Operación

| Acción | Comando |
|---|---|
| Detener conservando los datos | `docker stop simplerisk` |
| Reanudar | `docker start simplerisk` |
| Ver registros del contenedor | `docker logs simplerisk` |
| Abrir una shell dentro del contenedor | `docker exec -it simplerisk bash` |
| Espacio ocupado por Docker | `docker system df` |

> **Advertencia.** `docker compose down -v` elimina los volúmenes y con ellos toda la información cargada. Para detener el entorno sin pérdida de datos, usar `docker stop`.

---

## Reproducción de la configuración

El `docker-compose.yml` despliega una instancia limpia de SimpleRisk. Los usuarios, activos, riesgos y planes de acción documentados en esta entrega no se cargan automáticamente: la evidencia de su configuración se encuentra en `informe/capturas/`.

Para reproducir la configuración manualmente, el orden es el siguiente:

1. **Ajustar el motor de scoring.** En `Configure → Risk Configuration → Classic Risk Formula`, desactivar *Normalize scoring on a 0-10 scale*. En la pestaña *Scoring*, fijar los umbrales de nivel en 16 (Very High), 10 (High), 5 (Medium) y 1 (Low). Fijar el apetito de riesgo en Medium.
2. **Crear los roles.** En `Configure → Role Management`, crear *Analista de Riesgos* y *Auditor* con los permisos detallados en `configuracion/usuarios.md`.
3. **Crear los usuarios.** En `Configure → User Management`, dar de alta los tres usuarios y asignarles su rol.
4. **Cargar los activos.** En `Asset Management → Manage Assets`, dar de alta los once activos del inventario de `configuracion/riesgos.md`.
5. **Cargar los riesgos.** En `Risk Management → Submit Your Risks`, cargar los ocho riesgos con sus valoraciones.
6. **Cargar los planes de acción.** Desde cada riesgo, mediante la opción de planificación de mitigación.

---

## Uso del script de integración

El script `scripts/notificar_riesgos.py` consulta el registro de riesgos y notifica por Discord aquellos que superan el umbral de nivel Alto.

```bash
# Verificación sin enviar nada
python3 entregas/barbero-lautaro-44820797/scripts/notificar_riesgos.py --dry-run

# Envío efectivo
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
python3 entregas/barbero-lautaro-44820797/scripts/notificar_riesgos.py

# Notificar únicamente riesgos de nivel Crítico
python3 entregas/barbero-lautaro-44820797/scripts/notificar_riesgos.py --umbral 16
```

Requiere el contenedor en ejecución. No tiene dependencias externas: utiliza únicamente la biblioteca estándar de Python 3.

La URL del webhook se lee de una variable de entorno y **no está incluida en el repositorio**, por tratarse de una credencial.

---

## Decisiones de diseño

### Metodología de análisis de riesgos

Se adoptó la **matriz cualitativa de probabilidad × impacto** definida en la plantilla de matriz de riesgos de la cátedra, con escalas de 1 a 5 en ambos ejes y cuatro bandas de nivel (Bajo 1-4, Medio 5-9, Alto 10-15, Crítico 16-25).

La estructura del análisis sigue la secuencia de la plantilla: inventario de activos con identificador único, identificación de amenazas y vulnerabilidades asociadas, evaluación de riesgos, tratamiento y cálculo del riesgo residual.

### Criterio de agrupación de amenazas en riesgos

Las diecisiete amenazas identificadas se consolidaron en ocho riesgos aplicando el criterio de **comunidad de tratamiento**: amenazas que se mitigan con las mismas salvaguardas se agrupan en un mismo riesgo, de modo que cada plan de acción resulte coherente y ejecutable. La alternativa de agrupar por tema habría producido riesgos cuyo tratamiento debería atacar problemas heterogéneos.

### Supuestos del escenario

El enunciado no detalla la infraestructura de la clínica. Los supuestos técnicos fueron definidos como parte del análisis y se documentan en la sección 2 de `configuracion/riesgos.md`.

La definición se orientó deliberadamente a construir un escenario **con debilidades reales**, en coherencia con el planteo del enunciado, que sitúa a la clínica inmediatamente después de una auditoría externa con hallazgos.

### Configuración de la herramienta

SimpleRisk aplica por defecto una normalización de la puntuación a escala 0-10 y establece umbrales de nivel sobre esa escala comprimida. Ambos parámetros se modificaron para alinear la herramienta con la metodología adoptada: se desactivó la normalización, restituyendo el rango 1-25, y se redefinieron los umbrales en 16 / 10 / 5 / 1. El apetito de riesgo se fijó en Medium, frente al valor Insignificant (0) por defecto.

### Persistencia del entorno

El despliegue se definió mediante Docker Compose con seis volúmenes persistentes, en lugar del comando `docker run` sin volúmenes. El fundamento se detalla en la sección 1.1 del informe: sin persistencia, la eliminación del contenedor destruye toda la información cargada.

La imagen se referencia con la etiqueta `:latest`. Se deja constancia de la limitación que ello implica para la reproducibilidad estricta: una ejecución futura podría obtener una versión distinta de la imagen. La alternativa —fijar una etiqueta de versión— habría garantizado reproducibilidad exacta a costa de no recibir correcciones de seguridad.

### Integración externa

Se implementó mediante consulta directa a la base de datos y no a través de la API REST de SimpleRisk. El fundamento es una limitación de la versión Community: la generación de claves de API forma parte del complemento comercial *SimpleRisk API Extra*. El detalle figura en la sección 3.2 del informe.

### Verificación

Palabra clave de verificación de lectura del enunciado: **girasol**

---

## Manejo de información sensible

El repositorio es público, por lo que se aplicaron las siguientes medidas:

- **Credenciales ficticias.** Los usuarios del escenario emplean identificadores de demostración (`admin_demo`, `analista_demo`, `auditor_demo`) y direcciones de correo bajo el dominio `.local`, reservado por convención para redes internas y no resoluble en internet.
- **Sin contraseñas versionadas.** `configuracion/usuarios.md` documenta usuarios, roles y permisos sin incluir contraseña alguna.
- **Credenciales por variable de entorno.** La URL del webhook de Discord se lee de `DISCORD_WEBHOOK_URL`. La contraseña de la base de datos nunca sale del contenedor: se lee desde `/passwords/pass_mysql_root.txt` mediante `docker exec`, sin pasarse como argumento —lo que la expondría en la lista de procesos— ni quedar en el historial de comandos.
- **Capturas revisadas.** Las capturas de pantalla se tomaron sobre `localhost`, sin exponer direcciones IP de red, y no incluyen contraseñas ni datos personales.
- **Datos simulados.** El escenario de la clínica es ficticio. No se utilizó información real de pacientes, personal ni instituciones.

---

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio
- [x] El `.gitignore` está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos `.sql` o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona

---

## Referencias

- Plantilla de Matriz de Riesgos — Cátedra
- ISO/IEC 27005: *Information security risk management*
- NIST SP 800-30 Rev. 1: *Guide for Conducting Risk Assessments*
- FAIR Institute: https://www.fairinstitute.org/what-is-fair
- Documentación de SimpleRisk: https://www.simplerisk.com/documentation
