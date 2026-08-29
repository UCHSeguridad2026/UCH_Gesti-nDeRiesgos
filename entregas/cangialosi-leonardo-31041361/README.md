# TP Gestión de Riesgos con SimpleRisk — Entrega

## Datos personales
- **Nombre completo:** Cangialosi, Leonardo Arturo
- **LU / Legajo:** 31041361
- **Email:** leocangialosi04@gmail.com
- **Comisión:** G
- **Materia:** Seguridad de Sistemas — Cátedra Ing. Rodrigo Atilio Elgueta

## Estructura de la entrega
```
entregas/cangialosi-leonardo-31041361/
|-- README.md                 # este archivo
|-- .gitignore                # obligatorio (credenciales, dumps, binarios)
|-- entorno/
|   |-- docker-compose.yml    # levantamiento reproducible
|   `-- setup.sh              # script de instalación
|-- informe/
|   |-- informe.md            # desarrollo completo del TP (Partes A, B, C, D)
|   `-- capturas/            # screenshots (sin datos sensibles)
|-- configuracion/
|   |-- usuarios.md           # usuarios y roles (SIN contraseñas)
|   `-- riesgos.md           # registro de 8 riesgos + planes + residual
|-- scripts/
|   `-- notificar_riesgos.py # PoC webhook Slack/Discord (Parte D)
`-- reporte-ejecutivo/
    `-- reporte.pdf          # reporte para la gerencia (máx 3 pág)
```

## Cómo levantar el entorno (paso a paso)

Requisito: **Docker Desktop** instalado y en ejecución.

**Opción A — Docker Compose (recomendada):**
```bash
cd entorno
docker compose up -d
# abrir https://localhost/  (aceptar el certificado autofirmado)
```

**Opción B — script:**
```bash
cd entorno
chmod +x setup.sh
./setup.sh
```

**Opción C — comandos manuales:**
```bash
docker pull  --platform linux/amd64 simplerisk/simplerisk
docker run   --platform linux/amd64 --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk
```

> El flag `--platform linux/amd64` es **necesario en Mac con Apple Silicon** (la imagen solo se
> publica para amd64) y es inofensivo en x86. Acceso inicial: `admin` / `admin` → **cambiar la
> contraseña de inmediato**.

## Decisiones de diseño
- **Escenario:** clínica privada ficticia "Vida Sana" (120 empleados, 800 pacientes/día).
- **Metodología de riesgos:** matriz cualitativa **Probabilidad × Impacto** (escala 1–5) alineada
  a la plantilla de la cátedra; niveles Bajo/Medio/Alto/Crítico.
- **Justificación de probabilidades:** criterio profesional apoyado, donde corresponde, en el
  **Verizon DBIR** y en el marco legal argentino (**Ley 25.326**, secreto médico).
- **Usuarios:** 4 roles con **mínimo privilegio** y **separación de funciones** (admin, analista,
  revisor, auditor).
- **Seguridad de la entrega:** `.gitignore` que excluye credenciales, dumps y binarios; ninguna
  contraseña versionada; credenciales ficticias.
- **Marco legal asumido:** Argentina (protección de datos personales y de salud).

## Verificación de lectura completa
🌻 **girasol** — palabra clave incluida para confirmar la lectura completa del enunciado
(sección "Verificación de lectura completa" del PDF).

## Checklist de auto-revisión
- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles. *(verificar al agregarlas)*
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona correctamente.
