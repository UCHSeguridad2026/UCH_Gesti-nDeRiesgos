# Trabajo Práctico — Gestión de Riesgos con SimpleRisk

> Entrega individual · `entrega/cabrera-uriel-31673361`

---

## 1. Datos del alumno

| Campo | Dato |
|---|---|
| Nombre completo | Uriel Cabrera |
| Legajo (LU) | 31673361 |
| Email institucional | `cabrerauriel@uch.edu.ar` |
| Comisión | `G` |
| Materia | Seguridad Aplicada a Sistemas de Información |
| Branch | `entrega/cabrera-uriel-31673361` |

---

## 2. Cómo levantar el entorno

### Prerrequisitos

- Docker Desktop con backend WSL 2 (Windows 10/11) o Docker Engine (Linux).
- Virtualización habilitada en la UEFI/BIOS.
- ~3 GB libres de disco para la imagen.

### Levantamiento en un comando

Desde la raíz de esta carpeta:

```bash
cd entorno
chmod +x setup.sh
./setup.sh
```

En Windows, ejecutar el script desde WSL o Git Bash con Docker Desktop iniciado.

### Levantamiento manual (equivalente)

```bash
cd entorno
docker compose pull
docker compose up -d
docker compose ps
```

### Acceso

Abrir **https://localhost:8443**

El certificado es autofirmado, por lo que el navegador muestra una advertencia.
Es el comportamiento esperado de la imagen: se acepta la excepción y se continúa.

En el primer acceso, SimpleRisk presenta la pantalla *Default Admin Account
Creation*: la aplicación **no incluye una cuenta administradora preconfigurada**,
sino que exige crearla en ese momento definiendo usuario y contraseña propios.
Esto elimina de raíz el riesgo de credenciales por defecto conocidas, una de las
malas prácticas más frecuentes en despliegues de aplicaciones web.

Por política de la cátedra, ninguna contraseña —ni real ni de demostración— se
documenta en este repositorio.

### Comandos útiles

```bash
docker compose logs -f          # ver logs en vivo
docker compose stop             # detener sin borrar datos
docker compose down             # detener y eliminar el contenedor
docker compose down -v          # ¡CUIDADO! borra también la base de datos
```

---

## 3. Decisiones de diseño

### 3.1 Elección de la imagen: `simplerisk/simplerisk`

SimpleRisk publica dos imágenes oficiales:

| Imagen | Contenido | Elegida |
|---|---|---|
| `simplerisk/simplerisk` | LAMP completo + utilidades de correo en un contenedor | ✅ |
| `simplerisk-minimal` | Sólo la aplicación; requiere base de datos externa | ❌ |

Se eligió la imagen todo en uno porque es la ruta de instalación que el
proveedor documenta oficialmente para Docker y la única que puede levantarse
sin configuración adicional de conexión. La consigna A.1 pide que la
instalación sea **replicable**, y cada componente extra (variables de conexión,
orden de arranque entre contenedores, espera de disponibilidad de la base)
agrega un punto de falla en la máquina del evaluador sin aportar al análisis de
riesgos, que es el objeto del trabajo.

Limitación conocida: al residir la base de datos dentro del mismo contenedor,
la persistencia depende exclusivamente del volumen declarado en la sección 3.3.

### 3.2 Puertos 8080 / 8443 en lugar de 80 / 443

En Windows los puertos privilegiados suelen estar ocupados por otros servicios.
Usar puertos altos evita un conflicto que rompería la reproducibilidad en la
máquina del evaluador.

### 3.3 Persistencia sólo de la base de datos

Se persiste `/var/lib/mysql` mediante un volumen nombrado. Los archivos de la
aplicación no se persisten: se regeneran desde la imagen, lo que mantiene el
entorno reproducible y evita que un volumen desactualizado enmascare la versión
real de la aplicación.

### 3.4 Metodología de valoración de riesgos

Se utiliza la matriz clásica **Probabilidad × Impacto** en escala 1–5, alineada
con la plantilla de la Actividad A03. En SimpleRisk se selecciona el método de
scoring **Classic**, y no CVSS, DREAD ni OWASP, porque es el único que responde a
esa misma lógica; los demás métodos responden a modelos de puntuación distintos y
no serían comparables con la plantilla de la cátedra.

**Equivalencia de escalas.** Las denominaciones de SimpleRisk se corresponden una
a una con las de la plantilla A03:

| Valor | Probabilidad (SimpleRisk) | Probabilidad (A03) | Impacto (SimpleRisk) | Impacto (A03) |
|:-:|---|---|---|---|
| 1 | Remote | Raro | Insignificant | Insignificante |
| 2 | Unlikely | Improbable | Minor | Menor |
| 3 | Credible | Posible | Moderate | Moderado |
| 4 | Likely | Probable | Major | Mayor |
| 5 | Almost Certain | Casi seguro | Extreme/Catastrophic | Catastrófico |

**Diferencia en la escala de resultado.** Ambos enfoques calculan el mismo
producto, pero lo expresan de forma distinta. La plantilla A03 conserva el
producto en su rango natural de 1 a 25; SimpleRisk lo normaliza a una escala de
0 a 10 mediante la expresión (P × I) / 25 × 10.

El riesgo de validación cargado durante la Parte A ilustra el efecto: valorado
como Credible (3) y Moderate (3), la plantilla A03 arroja un valor de 9 y
SimpleRisk muestra 3.6. Son la misma valoración expresada en dos escalas.

**Criterio adoptado.** Los niveles de riesgo se clasifican según la tabla de la
plantilla A03 —Bajo (1–4), Medio (5–9), Alto (10–15), Crítico (16–25)—, por ser
el instrumento formal de la cátedra. En `configuracion/riesgos.md` se consignan
ambos valores para cada riesgo, de modo que la documentación resulte contrastable
contra las capturas de SimpleRisk sin ambigüedad.

### 3.5 Supuestos del escenario

Documentados en detalle en `informe/informe.md`, sección "Contexto y supuestos".

### 3.6 Normalización de fines de línea (`.gitattributes`)

Windows y Linux marcan el fin de línea de manera distinta: Windows usa CRLF
(retorno de carro + salto de línea) y Linux usa únicamente LF. El desarrollo de
esta entrega se realizó en Windows, pero el entorno se ejecuta sobre
contenedores Linux.

La consecuencia práctica es que un script convertido a CRLF **no se ejecuta**:
`bash` interpreta el carácter `\r` sobrante como parte del comando y falla con
un error poco descriptivo (`$'\r': command not found`).

El archivo `.gitattributes` fija el criterio en el propio repositorio:

```
* text=auto
*.sh  text eol=lf
*.yml text eol=lf
```

Con esto, `setup.sh` y `docker-compose.yml` conservan finales de línea LF en
cualquier clon del repositorio, sea cual sea el sistema operativo de quien lo
descargue. Sin este archivo, la reproducibilidad que exige la consigna A.1
quedaría sujeta a la configuración local `core.autocrlf` de cada máquina, es
decir, a un factor externo al repositorio y fuera del control del autor.

---

## 4. Verificación

Palabra clave de verificación de lectura: **girasol**

---

## 5. Estructura de la entrega

```
entregas/cabrera-uriel-31673361/
├── README.md                    # este archivo
├── .gitignore
├── .gitattributes               # normalización de fines de línea (ver 3.6)
├── entorno/
│   ├── docker-compose.yml
│   └── setup.sh
├── informe/
│   ├── informe.md
│   └── capturas/
├── configuracion/
│   ├── usuarios.md              # usuarios y roles (SIN contraseñas)
│   └── riesgos.md               # tabla de riesgos definidos
├── scripts/
└── reporte-ejecutivo/
    └── reporte.pdf
```

---

## 6. Checklist de auto-revisión

- [X] No hay credenciales en el repositorio
- [X] El `.gitignore` está correctamente configurado
- [X] Las capturas no muestran datos sensibles
- [X] Los archivos `.sql` o dumps no están subidos
- [ ] El informe está en formato legible
- [ ] El reporte ejecutivo está completo
- [X] Los mensajes de commit son descriptivos
- [X] Mi branch está actualizada y funciona
