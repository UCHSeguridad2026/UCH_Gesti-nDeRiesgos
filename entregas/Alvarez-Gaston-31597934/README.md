# TP Individual - Gestion de Riesgos con SimpleRisk

## Datos del alumno

* **Nombre completo:** Gaston Alvarez
* **Legajo (LU):** 31597934
* **Email:** [gastonalvarez.gma@gmail.com](mailto:gastonalvarez.gma@gmail.com)
* **Comision:** G

## Descripcion del trabajo

Este trabajo practico consiste en instalar y configurar SimpleRisk para gestionar riesgos de seguridad.

Para realizarlo se utilizo como ejemplo una clinica privada de 120 empleados. La clinica trabaja con historias clinicas digitales, datos de obras sociales y sistemas de facturacion.

La idea fue usar este escenario para cargar y analizar distintos riesgos relacionados con la informacion y los sistemas de la clinica.

## Como levantar el entorno

Para levantar el entorno es necesario tener **Docker Desktop** instalado y ejecutandose.

### 1. Clonar el repositorio

Primero hay que clonar el repositorio y entrar en la carpeta del entorno:

```bash
cd entregas/Alvarez-Gaston-31597934/entorno
```

### 2. Levantar los contenedores

Ejecutar:

```bash
docker-compose up -d
```

### 3. Verificar que los contenedores esten funcionando

Se puede comprobar con:

```bash
docker ps
```

Deberian aparecer los contenedores:

* `simplerisk_app`
* `simplerisk_db`

Ambos deberian figurar como **Up** o **healthy**.

### 4. Acceder a SimpleRisk

Abrir en el navegador:

https://localhost:8443

Es posible que el navegador muestre una advertencia porque se utiliza un certificado autofirmado. En ese caso hay que aceptar la advertencia y continuar.

### 5. Instalar SimpleRisk

Al ingresar se muestra el instalador de SimpleRisk.

Se deben completar los datos de conexion a la base de datos utilizando los valores definidos en el archivo `docker-compose.yml`.

Una vez terminada la instalacion, se puede ingresar utilizando el usuario administrador creado durante el proceso.

## Decisiones de diseno

Para realizar el entorno se eligio **Docker Compose**, utilizando un contenedor para SimpleRisk y otro para MySQL 8.0. De esta forma se puede levantar todo el entorno sin tener que instalar cada componente por separado.

Tambien se configuraron los puertos **80 y 443**. El puerto 443 fue necesario porque SimpleRisk redirige el acceso a HTTPS. Sin ese puerto mapeado, la aplicacion no podia abrirse correctamente desde el navegador.

Para probar la herramienta se eligio como escenario una clinica privada de 120 empleados. Este caso permite trabajar con informacion que requiere cierto nivel de proteccion, como historias clinicas, datos de obras sociales y datos de facturacion.

## Checklist de auto-revision

* [x] Entorno Docker funcional y documentado
* [x] SimpleRisk instalado y configurado
* [x] Escenario aplicado y documentado en el informe
* [x] Actividad optativa D1 (analisis de seguridad de la instalacion) incluida
* [x] Commits realizados y pusheados a la rama de entrega
* [x] README completo con datos del alumno e instrucciones de uso
