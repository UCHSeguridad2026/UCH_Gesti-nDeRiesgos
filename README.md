# UCH - Seguridad - Gestión de Riesgos
> `#UCH_GestiónDeRiesgos`

Este repositorio público está destinado únicamente para las entregas de los estudiantes.

---

##  Datos del Alumno
* **Nombre del alumno:** Martín Carrera
* **DNI:** 45715448
* **Email:** tinchocarrera45@gmail.com 
* **Comisión:** G

---

##  Instrucciones para levantar el entorno
A continuación, se detallan los pasos exactos para levantar la infraestructura de SimpleRisk y su base de datos MySQL asociada de manera local, utilizando Docker Compose en un entorno Windows.

**Requisitos Previos:**
1. Tener instalado Docker Desktop (con WSL 2 habilitado) y asegurarse de que el motor de Docker esté en ejecución.
2. Abrir una terminal y posicionarse dentro del directorio del proyecto (carpeta `entorno/`), donde se encuentra el archivo `docker-compose.yml`.

**Ejecución y Despliegue:**
1. El archivo `docker-compose.yml` incluye credenciales de demostración predefinidas (usuario y base de datos de MySQL). No es necesario modificarlas para levantar el entorno.
2. Ejecute los siguientes comandos para crear la red e iniciar los contenedores en segundo plano:
    `cd entorno/`
    `docker compose up -d`
3. Espere entre 30 y 45 segundos para que la base de datos configure las tablas internas. Puede verificar que ambos contenedores estén en estado "Up" con el comando:
    `docker compose ps`
4. Acceda a la plataforma abriendo un navegador web en: `https://localhost` (el contenedor expone los puertos 80 y 443 directamente sobre el host).

---

##  Decisiones de Diseño
Para el desarrollo de este trabajo práctico sobre la clínica (120 empleados y 800 pacientes diarios), se tomaron las siguientes decisiones:

* **Arquitectura de Accesos:** Se implementó un modelo centralizado tipo **girasol**, donde la base de datos se ubica en el núcleo y los distintos perfiles (Administrador, Analista, Auditor) interactúan alrededor mediante permisos de acceso estrictamente diferenciados.
* **Metodología de Riesgos:** Se adoptó el enfoque cualitativo nativo de SimpleRisk (matriz de Probabilidad x Impacto) para categorizar los 7 riesgos operativos y de seguridad, priorizando la visibilidad rápida y la facilidad de gestión.
* **Supuestos del Escenario:** Se asumió que la clínica no cuenta con personal de ciberseguridad dedicado 24/7. Por ende, los planes de mitigación de nivel alto/crítico se enfocaron en soluciones de alto impacto y bajo mantenimiento manual (copias inmutables, software EDR, enlaces de backup automatizados y capacitación obligatoria con 2FA).

---

##  Checklist de Auto-Revisión

- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona correctamente.

---

##  Política de Branches y Resolución de Conflictos

- **Responsabilidad:** Cada estudiante es responsable exclusivo de su propia branch.
- **Errores de Commit:** Si por error haces un commit sobre `main` o sobre la branch de otro compañero, avisa inmediatamente al docente.
- **Restricciones:** No se permite hacer `git push --force` sobre ninguna branch compartida.
- **Soporte:** Ante dudas sobre Git, consulta al docente antes de realizar operaciones destructivas (`reset`, `rebase`, `push -f`).