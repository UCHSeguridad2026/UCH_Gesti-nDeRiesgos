# Informe — TP Gestión de Riesgos con SimpleRisk

> Seguridad de Sistemas — Cangialosi Leonardo Arturo — LU 31041361 — Comisión G
> Cátedra: Ing. Rodrigo Atilio Elgueta

## Índice
1. Parte A — Instalación y configuración básica
2. Parte B — Escenario real (clínica privada)
3. Parte C — Análisis crítico y profundización
4. Parte D — Actividad optativa
5. Capturas de pantalla

---

## 1. Parte A — Instalación y configuración básica

### 1.1. Instalación reproducible

SimpleRisk se instaló en un entorno local con **Docker** sobre **macOS (Apple Silicon)** usando la
imagen oficial de DockerHub. El proceso completo y reproducible está en `entorno/`
(`docker-compose.yml` y `setup.sh`).

**Pasos:**
1. Instalar y abrir **Docker Desktop**.
2. Descargar la imagen forzando la plataforma amd64 (necesario en chips Apple Silicon):
   `docker pull --platform linux/amd64 simplerisk/simplerisk`
3. Levantar el contenedor:
   `docker run --platform linux/amd64 --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk`
   (equivalente a `docker compose up -d` con el archivo provisto).
4. Verificar con `docker ps` (estado `Up (healthy)`) y abrir `https://localhost/`.

> **Hallazgo técnico documentado:** la imagen `simplerisk/simplerisk` se publica **solo para
> amd64**. En un Mac ARM el `pull` inicial falla con
> `no matching manifest for linux/arm64/v8`. La solución fue forzar `--platform linux/amd64`
> para ejecutarla bajo emulación (Rosetta/QEMU). Este detalle está contemplado en los scripts de
> `entorno/` para que el docente pueda reproducir el entorno sin tropezar con el mismo error.

### 1.2. Usuarios y permisos

Se crearon **4 usuarios con roles diferenciados** aplicando mínimo privilegio y separación de
funciones. El detalle completo (roles, permisos y mapa SoD) está en
[`configuracion/usuarios.md`](../configuracion/usuarios.md). Resumen: `admin_demo` (Administrador),
`analista_demo` (Analista de Riesgos), `revisor_demo` (Revisor/Gerencia) y `auditor_demo`
(Auditor, solo lectura). **No se versionan contraseñas.**

### 1.3. Riesgo de prueba

Se cargó `R00 — Riesgo de prueba de instalación` para validar el flujo completo (carga →
mitigación → revisión → cierre) y verificar que cada rol tiene los permisos esperados.

---

## 2. Parte B — Escenario real (el corazón del TP)

El registro completo de **8 riesgos** de la clínica, con categoría, activos, probabilidad e
impacto justificados (escala 1–5), nivel, controles, tratamiento y propietario, está en
[`configuracion/riesgos.md`](../configuracion/riesgos.md). Allí también están la **matriz de
calor**, el **resumen por nivel**, los **3 planes de acción** y la estimación de **riesgo
residual**.

**Síntesis:** 3 riesgos Críticos (R01 ransomware, R02 acceso indebido, R03 phishing), 4 Altos
(R04 backups, R05 infraestructura, R06 cumplimiento, R07 malware en red) y 1 Medio (R08
robo/pérdida de equipos). Los 3 planes de acción (PA-01 blindaje anti-ransomware, PA-02
MFA+concientización, PA-03 control de acceso) reducen todo el registro a nivel Medio/Bajo.

El **reporte ejecutivo** para el directorio está en `reporte-ejecutivo/reporte.pdf`.

---

## 3. Parte C — Análisis crítico y profundización

### 3.1. Comparación metodológica: SimpleRisk (P × I) vs. FAIR

SimpleRisk implementa por defecto una **matriz cualitativa de Probabilidad × Impacto** (CVSS y
otras fórmulas también están disponibles, pero el enfoque base es la matriz clásica). Se la
compara con **FAIR (Factor Analysis of Information Risk)**, una metodología **cuantitativa**.

| Dimensión | SimpleRisk (matriz P×I) | FAIR |
|-----------|-------------------------|------|
| Naturaleza | Cualitativa / semicuantitativa | Cuantitativa (probabilística) |
| Salida | Nivel (Bajo→Crítico) | Pérdida esperada en $ (distribución, ALE) |
| Datos requeridos | Bajos; juicio experto | Altos; frecuencia y magnitud de pérdida |
| Curva de aprendizaje | Baja | Alta |
| Comunicación a dirección | Simple (colores) | Muy potente (habla en dinero) |
| Riesgo de subjetividad | Alto (escalas 1–5 opinables) | Menor, pero sensible a los supuestos |

**Ventajas del enfoque de SimpleRisk:** es rápido de implementar, no exige datos históricos ni
formación estadística, y comunica visualmente. Ideal para una organización con **baja madurez**
—como la clínica del escenario, que recién sale de una auditoría— que necesita un **registro
inicial** operativo en poco tiempo.

**Desventajas frente a FAIR:** las escalas 1–5 son subjetivas y difíciles de comparar entre
analistas; no cuantifican la pérdida económica, lo que dificulta priorizar inversiones (¿conviene
gastar USD 8.000 en PA-01?). FAIR responde esa pregunta expresando el riesgo en dinero
(*Annualized Loss Expectancy*), lo que permite análisis costo-beneficio de cada control.

**¿En qué contexto es mejor cada una?**
- **SimpleRisk / matriz P×I:** organizaciones de baja/media madurez, primer inventario de
  riesgos, necesidad de rapidez y comunicación simple. (El caso de la clínica.)
- **FAIR:** organizaciones maduras que ya tienen datos, deben justificar presupuestos de seguridad
  ante el directorio o cuantificar el ROI de los controles.

> También se consideraron **NIST SP 800-30** (marco de proceso de evaluación, complementario) e
> **ISO 27005** (gestión de riesgos dentro de un SGSI ISO 27001). Ambas son más *marcos de
> proceso* que fórmulas de cálculo, y podrían envolver tanto a SimpleRisk como a FAIR.

### 3.2. Integración con una herramienta externa

Se propone integrar SimpleRisk con **Slack/Discord** mediante un **webhook** para **notificar
automáticamente los riesgos de nivel Alto/Crítico** al canal del equipo de seguridad, de modo que
no dependan de que alguien entre a la herramienta.

**Diseño de la integración:**
- SimpleRisk expone una **API REST** (`/api/...`) con autenticación por API key.
- Un pequeño script (ver `scripts/notificar_riesgos.py`) consulta periódicamente los riesgos con
  `risk_level >= Alto` y publica un mensaje en el **Incoming Webhook** de Slack/Discord.
- La API key **nunca** se sube al repo (queda en una variable de entorno `.env`, ya excluida por
  `.gitignore`).

El script de ejemplo está documentado en `scripts/` como prueba de concepto (Parte D2/D3).

---

## 4. Parte D — Actividad optativa (bonifica)

### D1 — Análisis de seguridad de la propia instalación de SimpleRisk

Tres malas prácticas / debilidades potenciales de la instalación por defecto y su mitigación:

1. **Certificado TLS autofirmado.** La instancia usa un certificado autofirmado que genera
   advertencias y no da garantías de identidad; habilita ataques MITM si se acepta a ciegas.
   *Mitigación:* reemplazar por un certificado válido (Let's Encrypt / CA interna) y forzar HTTPS
   con HSTS.
2. **Credenciales por defecto `admin/admin`.** La cuenta inicial trae usuario y contraseña
   conocidos y públicos. *Mitigación:* cambiar la contraseña en el primer acceso, habilitar MFA y
   renombrar/limitar la cuenta administrativa.
3. **Servicios expuestos y headers HTTP inseguros.** El contenedor publica puertos 80/443 en
   todas las interfaces y puede omitir headers de seguridad (CSP, X-Frame-Options,
   X-Content-Type-Options). *Mitigación:* exponer solo por reverse proxy/VPN, limitar el binding a
   la interfaz necesaria, agregar los headers de seguridad y mantener PHP/MySQL parcheados.

*(Otras observables: versión de PHP/MySQL del contenedor, permisos de archivos y cookies de
sesión sin flags `Secure`/`HttpOnly`/`SameSite`.)*

### D2/D3 — Integración real (webhook) y automatización

Prueba de concepto en `scripts/notificar_riesgos.py`: consulta la API de SimpleRisk y notifica a
Slack/Discord los riesgos Alto/Crítico. Junto con `entorno/docker-compose.yml` automatiza el
levantamiento del entorno.

---

## 5. Capturas de pantalla

Colocar en `informe/capturas/` (difuminando cualquier dato sensible):

- `01_docker_ps.png` — contenedor `simplerisk` en estado `Up (healthy)`.
- `02_login.png` — pantalla de login de SimpleRisk.
- `03_usuarios_roles.png` — listado de usuarios y roles creados (sin contraseñas).
- `04_riesgo_R01.png` — detalle del riesgo R01 (ransomware) cargado.
- `05_matriz_calor.png` — matriz de riesgos / dashboard.
- `06_plan_accion.png` — un plan de acción (PA-01) cargado.
- `07_reporte.png` — vista de un reporte de gestión.

> Recordatorio de seguridad: en las capturas, **ocultar/difuminar** contraseñas, tokens, IPs
> reales y datos personales.
