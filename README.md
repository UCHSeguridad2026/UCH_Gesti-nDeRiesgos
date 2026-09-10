# UCH - Seguridad - Gestión de Riesgos
> `#UCH_GestiónDeRiesgos`

Este repositorio público está destinado únicamente para las entregas de los estudiantes.

---

## 📌 Checklist de Auto-Revisión
*Por favor, marca las casillas correspondientes antes de realizar tu entrega:*

- [ ] No hay credenciales en el repositorio.
- [ ] El archivo `.gitignore` está correctamente configurado.
- [ ] Las capturas de pantalla no muestran datos sensibles.
- [ ] Los archivos `.sql` o dumps no están subidos.
- [ ] El informe está en un formato legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] Mi branch está actualizada y funciona correctamente.

---

## ⚠️ Política de Branches y Resolución de Conflictos

- **Responsabilidad:** Cada estudiante es responsable exclusivo de su propia branch.
- **Errores de Commit:** Si por error haces un commit sobre `main` o sobre la branch de otro compañero, avisa inmediatamente al docente.
- **Restricciones:** No se permite hacer `git push --force` sobre ninguna branch compartida.
- **Soporte:** Ante dudas sobre Git, consulta al docente antes de realizar operaciones destructivas (`reset`, `rebase`, `push -f`).


---

## 👤 Datos de la estudiante

**Nombre:** Camila Olivera  
**LU:** 31711902  
**Correo institucional:** oliveracamila@uch.edu.ar  
**Comisión:** Turno tarde-noche  
**materia:**  Seguridad

---

## 🛠️ Entorno de implementación

El Trabajo Práctico fue desarrollado utilizando el siguiente entorno:

* Sistema operativo: Kali Linux.
* Virtualización: VirtualBox.
* Contenedores: Docker.
* Orquestación: Docker Compose.
* Base de datos: MySQL 8.0.
* Aplicación de gestión de riesgos: SimpleRisk.

SimpleRisk se ejecuta mediante Docker Compose utilizando dos contenedores principales:

* `simplerisk`: aplicación SimpleRisk.
* `simplerisk-mysql`: base de datos MySQL.

---

## ▶️ Reproducción del entorno
 
Para levantar el entorno se debe disponer de Docker y Docker Compose.

Desde la raíz del proyecto ejecutar:

```bash
./entorno/setup.sh```

El script verifica la disponibilidad de Docker y Docker Compose, comprueba la existencia del archivo de configuración necesario y levanta los servicios definidos en Docker Compose.
Una vez iniciado el entorno, SimpleRisk se encuentra disponible mediante:

```text
https://localhost```

---

## 📁 Estructura del proyecto
entorno/
├── docker-compose.yml
├── setup.sh
└── .env
configuracion/
├── usuarios.md
└── riesgos.md

informe/
├── informe.md
└── capturas/

scripts/
└── generar_reporte.py

reporte-ejecutivo/
└── reporte.pdf

Los archivos de configuración sensible se encuentran excluidos mediante .gitignore.

---

## 🔐 Decisiones de diseño y seguridad

Durante el desarrollo se adoptaron las siguientes decisiones:

Utilizar Docker Compose para disponer de un entorno reproducible.
Separar la aplicación y la base de datos en contenedores independientes.
Utilizar HTTPS para el acceso a SimpleRisk.
Configurar usuarios con diferentes responsabilidades.
Aplicar el principio de mínimo privilegio.
Mantener separación entre las funciones administrativas, de análisis de riesgos y de auditoría.
No almacenar contraseñas, tokens ni claves de API en el repositorio.
Excluir archivos sensibles mediante .gitignore.
Mantener el archivo .env fuera del control de versiones.
Evitar incluir bases de datos, dumps, máquinas virtuales y logs en el repositorio.

---

## 🧪 Verificación de la entrega

La implementación fue verificada mediante:

Levantamiento correcto de los contenedores de SimpleRisk y MySQL.
Acceso funcional a SimpleRisk mediante HTTPS.
Configuración de tres usuarios con responsabilidades diferenciadas.
Registro de un riesgo de prueba.
Registro de siete riesgos correspondientes al escenario de la clínica.
Creación de tres planes de mitigación.
Generación del reporte ejecutivo.
Verificación de que el archivo entorno/.env se encuentra correctamente ignorado por Git.

Como mecanismo de verificación de la lectura de las consignas se incorpora la palabra girasol.

---

## 📚 Documentación de la entrega

La documentación se encuentra organizada de la siguiente manera:

informe/informe.md: informe principal del Trabajo Práctico.
configuracion/usuarios.md: usuarios, responsabilidades y permisos configurados.
configuracion/riesgos.md: identificación, evaluación y tratamiento de los riesgos.
informe/capturas/: evidencias gráficas de la configuración.
reporte-ejecutivo/reporte.pdf: reporte ejecutivo destinado al directorio.
entorno/docker-compose.yml: definición del entorno reproducible.
entorno/setup.sh: script para levantar el entorno.
