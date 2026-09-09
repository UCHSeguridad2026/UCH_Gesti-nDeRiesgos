# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

> **Materia:** Seguridad de Sistemas — Licenciatura en Ciencias de la Computación (4to Año)  
> **Institución:** Universidad de Congreso (UCH)  
> **Estudiante:** Martín Vera  
> **Libreta Universitaria (LU):** 31341047  
> **Email institucional:** `revisar`  
> **Comisión:** Única  

---

## 1. Estructura de la Entrega

La entrega cumple estrictamente con el árbol de directorios estandarizado para la materia:

```text
entregas/Vera-Martin-31341047/
|-- README.md                    # Datos personales, guía de despliegue, decisiones y verificación
|-- .gitignore                   # Exclusiones estrictas de seguridad (credenciales, dumps, binarios)
|-- entorno/
|   |-- docker-compose.yml       # Definición de servicios SimpleRisk y MySQL 5.7 en puerto HTTPS 8443
|   `-- setup.sh                 # Script automatizado de levantamiento del entorno
|-- informe/
|   |-- informe-ejecutivo.md     # Reporte técnico y ejecutivo formal para el Directorio
|   |-- informe.md               # Desarrollo metodológico completo del TP
|   `-- capturas/                # Evidencias visuales de la plataforma SimpleRisk
|       |-- contenedor docker.png
|       |-- usuarios cargados.png
|       |-- riesgos.png
|       |-- plan de mitigacion Secuestro de datos (Ransomware) en servidores principales.png
|       |-- plan de mitigacion Robo de credenciales administrativas por correos de suplantación.png
|       `-- plan de mitigacion Interrupción del centro de datos por fallo eléctrico y climático.png
|-- configuracion/
|   |-- usuarios.md              # Definición de los 3 usuarios con roles diferenciados (sin contraseñas)
|   `-- riesgos.md               # Tabla y detalle de los 7 riesgos específicos evaluados
|-- scripts/                     # Directorio reservado para automatizaciones
`-- reporte-ejecutivo/           # Directorio para compilaciones documentales ejecutivas
```

---

## 2. Instrucciones de Despliegue Reproducible (Paso a Paso)

El entorno fue diseñado para ser 100% reproducible en cualquier equipo con **Docker** y **Docker Compose** instalado.

### Paso 1: Clonar / Posicionarse en el directorio del entorno
Abrir una terminal y ubicarse en la carpeta `entorno/` de esta entrega:
```bash
cd entregas/Vera-Martin-31341047/entorno
```

### Paso 2: Iniciar los contenedores
Ejecutar el script de inicio o el comando directo de Docker Compose:
```bash
# Opción A: Mediante script automatizado
chmod +x setup.sh
./setup.sh

# Opción B: Mediante Docker Compose directo
docker-compose up -d
```

### Paso 3: Acceso a la plataforma SimpleRisk
Una vez que ambos contenedores (`simplerisk` y `simplerisk-db`) se encuentren en estado *healthy/running*:
1. Abrir el navegador web e ingresar al puerto seguro HTTPS:  
   👉 **`https://localhost:8443`** *(o alternativamente http://localhost:8888)*
2. Al tratarse de un certificado autofirmado para desarrollo local, el navegador presentará una advertencia de seguridad. Hacer clic en **"Configuración avanzada"** y seleccionar **"Continuar a localhost (no seguro)"**.
3. Iniciar sesión con las credenciales demo iniciales:
   * **Usuario:** `admin`
   * **Contraseña inicial:** `admin` *(el sistema solicitará actualizarla en el primer ingreso; utilizar credencial ficticia de prueba como `Passw0rd!Demo`)*.

---

## 3. Decisiones de Diseño y Supuestos del Escenario

1. **Contexto Organizacional Realista:**
   * La organización modelada es una clínica médica privada de mediana complejidad con **120 empleados** y un flujo sostenido de **~800 pacientes diarios**.
   * Los procesos más sensibles involucran la confidencialidad e integridad de las Historias Clínicas Electrónicas (HCE), el diagnóstico por imágenes (PACS), la liquidación de prestaciones con obras sociales y la continuidad del suministro de medicamentos.
2. **Parametrización de Riesgos (Escala 1 a 5):**
   * Se calibró la matriz clásica de SimpleRisk asignando la máxima severidad de impacto (5) al secuestro masivo de datos por Ransomware, dado que compromete de manera directa la vida y salud de los pacientes internados al impedir la consulta de diagnósticos y alergias medicamentosas.
   * La probabilidad se fundamentó con base en estadísticas sectoriales (Verizon DBIR, Sophos), donde el sector de la salud representa uno de los objetivos más atacados mediante campañas de phishing a usuarios administrativos y sanitarios.
3. **Segregación Funcional de Usuarios:**
   * En `configuracion/usuarios.md` se estructuraron tres roles rigurosos: **Administrador de IT** (control total de infraestructura), **Analista de Riesgos** (carga, actualización y propuesta de mitigaciones) y **Auditor Externo** (acceso de solo lectura y revisión de cumplimiento normativo), garantizando el principio de menor privilegio.

---

## 4. Verificación de Lectura Completa de la Consigna

En estricto cumplimiento con la verificación requerida al final de la consigna oficial del trabajo práctico, se declara la siguiente palabra clave:

> **Palabra clave secreta de verificación:** **`girasol`**

---

## 5. Checklist de Auto-Revisión

Antes de consolidar la entrega, se verificaron todos los puntos de control del proyecto:

- [x] **Sin credenciales reales:** No existen contraseñas, secretos, tokens ni llaves privadas en el repositorio. Se utilizan exclusivamente identificadores ficticios de demo (`Passw0rd!Demo`).
- [x] **Archivo `.gitignore` exhaustivo:** Configurado con exclusión estricta de `.env`, bases de datos (`.sql`, `.dump`, `.bak`), binarios pesados (`.ova`, `.vmdk`, `.iso`, `.zip`), logs y temporales de IDEs.
- [x] **Capturas auditadas:** Todas las capturas en `informe/capturas/` corresponden a `localhost:8443` y Docker Desktop local, sin exposición de IPs públicas, datos personales reales ni información sensible.
- [x] **Sin archivos `.sql` o volcados:** No se incluye ningún dump de base de datos en el repositorio.
- [x] **Informes legibles y completos:** Disponibles en formato Markdown normalizado en `informe/informe-ejecutivo.md` e `informe/informe.md`.
- [x] **Reporte ejecutivo sobrio y formal:** Orientado al Directorio, libre de analogías no solicitadas ni recursos narrativos infantiles.
- [x] **Registro de 7 riesgos:** Documentados detalladamente en `configuracion/riesgos.md` y validados con su captura de SimpleRisk.
- [x] **3 Planes de mitigación:** Detallados con presupuesto, fechas, responsables y estado coincidente con el sistema.
- [x] **Mensajes de commit descriptivos:** Historial con mensajes claros y precisos sobre cada módulo.
- [x] **Rama y entorno operativos:** Verificado sobre la rama asignada `entrega/Martin-Vera-31341047`.

---

## 6. Política de Control de Versiones (Git)

* **Rama de trabajo asignada:** `entrega/Martin-Vera-31341047` (derivada de la nomenclatura `entrega/<apellido>-<nombre>-<lu>`).
* **Protección de `main`:** Queda terminantemente prohibido realizar commits directos o push sobre la rama `main`.
* **Prohibición de operaciones destructivas:** No se debe ejecutar `git push --force` ni reescribir el historial en ramas compartidas.

