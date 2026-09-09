# TP Gestión de Riesgos con SimpleRisk

## Datos del alumno

- **Nombre completo:** Juan Narváez *(Juanchi)*
- **Legajo (LU):** `31631196`
- **Email institucional:** `narvaezjuan@uch.edu.ar`
- **Comisión:** `4°G`
- **Branch de entrega:** `entrega/narvaez-juan-31631196`

---

## Cómo levantar el entorno (paso a paso)

El entorno usa **Docker** sobre **Ubuntu** (probado en 22.04/24.04 LTS en VirtualBox).
Todo es reproducible con la imagen oficial autocontenida `simplerisk/simplerisk`.

### Opción A — Script automático
```bash
cd entorno
chmod +x setup.sh
./setup.sh
```

### Opción B — Manual con Docker Compose
```bash
cd entorno
sudo docker compose up -d
sudo docker compose ps      # verificar estado
```

### Acceso
1. Abrir en el navegador: `https://localhost/` (aceptar el certificado autofirmado).
2. Login inicial: **usuario `admin` / contraseña `admin`**.
3. **Cambiar la contraseña** en el primer ingreso (obligatorio por seguridad).
4. Crear los usuarios y roles descriptos en `configuracion/usuarios.md`.

### Detener / reiniciar
```bash
sudo docker compose down    # detiene y conserva los datos (volúmenes)
sudo docker compose up -d   # vuelve a levantar
```

---

## Estructura del repositorio

```
├── README.md                 # este archivo
├── .gitignore                # exclusión de credenciales y binarios
├── entorno/
│   ├── docker-compose.yml    # definición del servicio SimpleRisk
│   └── setup.sh              # instalación reproducible en Ubuntu
├── informe/
│   ├── informe.md            # desarrollo completo del TP (Partes A–D)
│   └── capturas/             # screenshots (sin datos sensibles)
├── configuracion/
│   ├── usuarios.md           # usuarios y roles (SIN contraseñas reales)
│   └── riesgos.md            # registro de los 9 riesgos y planes de acción
├── scripts/                  # (opcional) automatización / seed
└── reporte-ejecutivo/
    └── reporte.pdf           # reporte para la dirección de la clínica
```

---

## Decisiones de diseño

- **Escenario:** clínica privada ficticia *"Centro Médico del Valle"* (120 empleados, ~800
  pacientes/día), en línea con el contexto del enunciado.
- **Metodología:** matriz clásica **Probabilidad × Impacto** (escala 1–5) de SimpleRisk,
  alineada con la plantilla A03 de la cátedra para reutilizar el análisis.
- **Foco:** Confidencialidad de datos sensibles de salud y Disponibilidad asistencial.
- **Entorno:** se eligió Docker (imagen oficial autocontenida) por ser el método más
  **reproducible** para que el docente levante el sistema con un solo comando.
- **Seguridad de la entrega:** credenciales ficticias, `.gitignore` que excluye secretos y
  dumps, y capturas sin datos sensibles.
- **Verificación:** girasol *(palabra clave que confirma la lectura completa del enunciado)*.

---

## Checklist de auto-revisión

- [x] No hay credenciales reales en el repositorio
- [x] El `.gitignore` está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos `.sql` o dumps no están subidos
- [x] El informe está en formato legible (`informe/informe.md`)
- [x] El reporte ejecutivo está completo (`reporte-ejecutivo/reporte.pdf`)
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona
