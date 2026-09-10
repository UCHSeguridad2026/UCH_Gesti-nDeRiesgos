Mateo Agustin Falanti - 31645404 - mateofalantiuch@gmail.com 

comision: G

# Instalación de SimpleRisk (Parte A)

## Requisitos previos

- Docker Desktop instalado y corriendo (Windows, con el motor de Linux containers habilitado).
- Puertos `8080` y `8443` libres en el host.

## Pasos para levantar el entorno

1. Ubicate en la carpeta del proyecto que contiene `entorno/docker-compose.yml`.

   ```
   cd entrega/<apellido>-<nombre>-<lu>/entorno
   ```

2. Levantá el contenedor:

   ```
   docker compose up -d
   ```

3. Verificá que esté corriendo:

   ```
   docker ps
   ```

   Deberías ver el contenedor `simplerisk` con estado `Up` y los puertos `8080->80` y `8443->443`.

4. Esperá 1-2 minutos a que Apache y MySQL terminen de inicializar dentro del contenedor.

5. Abrí el navegador en:

   ```
   https://localhost:8443/
   ```

   El navegador va a advertir que el certificado es autofirmado y no confiable. Es esperable en este entorno de prueba: aceptá la excepción para continuar.

6. `index.php` detecta que no hay instalación previa y te redirige automáticamente al wizard de configuración inicial (selección de idioma, chequeo de requisitos, configuración de base de datos, creación de la cuenta de administrador, etc.). Completá los 6 pasos.

7. Al finalizar el wizard, vas a llegar a la pantalla de login de SimpleRisk con la cuenta de administrador que acabás de crear.

## Decisiones de diseño

GIRASOL :D

- **Imagen utilizada:** `simplerisk/simplerisk` (imagen oficial *all-in-one*, incluye Apache + PHP + MySQL en un solo contenedor), en lugar de `simplerisk-minimal` + MySQL separado. Se eligió por simplicidad: un solo servicio, sin necesidad de coordinar variables de entorno entre contenedores ni de un servicio SMTP adicional.
- **Puertos:** se mapearon `8080` y `8443` en el host (en vez de `80`/`443`) para evitar conflictos con otros servicios que suelen ocupar esos puertos en Windows (IIS, otros contenedores, etc.).
- **Persistencia:** esta imagen no documenta oficialmente un volumen externo para los datos; mientras no se elimine el contenedor (`docker rm`) los datos persisten entre `docker compose stop` / `up`. Se documenta esta limitación en vez de asumir una ruta de volumen no confirmada.

## Verificación de reproducibilidad

Para confirmar que la instalación es reproducible sin intervención manual adicional:

```
docker compose down
docker compose up -d
```

El entorno debe volver a estar disponible en `https://localhost:8443/` sin pasos extra más allá de esperar a que el contenedor inicialice.

## Problemas conocidos

- Si el puerto `8080` u `8443` ya está en uso en tu máquina, cambiá el mapeo en `docker-compose.yml` (por ejemplo `"8081:80"`) y volvé a levantar el entorno.
- Si la página no carga al primer intento, esperá unos segundos más: MySQL puede tardar en inicializar dentro del contenedor la primera vez.



# Decisiones de diseño

## Contexto del escenario

La organización simulada es una clínica privada de 120 empleados que atiende 800 pacientes por día, y maneja tres tipos de información sensible:

- **Historias clínicas digitales:** dato de salud, considerado dato sensible bajo la Ley 25.326 de Protección de Datos Personales, y regulado también por la Ley 26.529 de Derechos del Paciente / Historia Clínica.
- **Datos de obras sociales:** implican vinculación con terceros (aseguradoras/obras sociales) para validación de afiliados y prestaciones.
- **Facturación:** datos financieros, con superficie de fraude propia.

La clínica acaba de sufrir una auditoría externa que identificó debilidades en su gestión de riesgos, lo que justifica que se esté armando recién ahora un registro formal de riesgos, y permite asumir que no existía previamente un proceso de gestión de riesgos consolidado.

## Supuestos del escenario

Dado que la consigna no especifica la infraestructura de la clínica, se asumió lo siguiente para poder definir riesgos realistas:

- La clínica opera un sistema de Historia Clínica Electrónica (HCE) accedido por personal médico y administrativo desde estaciones de trabajo y/o tablets.
- Existe una red interna con Wi-Fi para personal, separada de la red de pacientes/visitas.
- La facturación y la integración con obras sociales se realiza mediante un sistema conectado a internet (envío de prestaciones, validación de afiliados).
- Hay guardias con turnos rotativos que operan fuera del horario administrativo habitual, lo que implica accesos al sistema fuera de horario o en forma remota.
- No existía previamente un área formal de seguridad de la información; el responsable de seguridad (rol asumido en este TP) es una función nueva en la organización.
- Marco legal aplicable: Ley 25.326 (Protección de Datos Personales) y Ley 26.529 (Historia Clínica).

## Metodología de evaluación de riesgos

SimpleRisk trabaja de forma nativa con una matriz de Probabilidad × Impacto en escala 1-5. Antes de cargar los riesgos se definieron los criterios de cada escala, para que los valores asignados a cada riesgo sean consistentes y justificables.

### Escala de Probabilidad

| Valor | Nivel | Criterio |
|---|---|---|
| 1 | Muy baja | Nunca ocurrió en el sector o en la organización; requeriría múltiples fallas simultáneas |
| 2 | Baja | Posible pero poco frecuente (una vez cada varios años) |
| 3 | Media | Ocurre ocasionalmente en organizaciones similares (cada 1-2 años) |
| 4 | Alta | Ocurre con cierta frecuencia en el sector salud (según reportes como Verizon DBIR) |
| 5 | Muy alta | Ya ocurrió en la organización o es prácticamente inevitable sin controles |

### Escala de Impacto

Adaptada al contexto específico de una clínica, incorporando el efecto sobre la atención al paciente como criterio (no solo el efecto técnico u operativo):

| Valor | Nivel | Criterio |
|---|---|---|
| 1 | Insignificante | Sin efecto en pacientes ni operación; molestia menor |
| 2 | Menor | Afecta a un área puntual, sin exposición de datos ni interrupción de atención |
| 3 | Moderado | Interrupción parcial de atención, o exposición de datos de un grupo acotado de pacientes |
| 4 | Mayor | Exposición masiva de historias clínicas/datos financieros, sanción regulatoria probable, o interrupción significativa de atención médica |
| 5 | Catastrófico | Riesgo para la seguridad/vida de pacientes, o incidente que compromete la continuidad de la clínica |

### Categorías de riesgo

Se utilizan las categorías propuestas por la consigna: Confidencialidad, Integridad, Disponibilidad, Legal, Operativo.

### Propietarios de riesgo

Para mantener consistencia entre los riesgos definidos, se establecieron de antemano los owners naturales según el tipo de riesgo:

- **Jefe de IT / Sistemas:** riesgos técnicos (infraestructura, backups, accesos).
- **Responsable de Seguridad de la Información:** riesgos transversales de confidencialidad y legales.
- **Dirección Médica:** riesgos que afectan directamente la atención al paciente.
- **Administración/Facturación:** riesgos vinculados a obras sociales y facturación.


## 📌 Checklist de Auto-Revisión
*Por favor, marca las casillas correspondientes antes de realizar tu entrega:*

- [x] No hay credenciales en el repositorio.
- [x] El archivo `.gitignore` está correctamente configurado.
- [x] Las capturas de pantalla no muestran datos sensibles.
- [x] Los archivos `.sql` o dumps no están subidos.
- [x] El informe está en un formato legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] Mi branch está actualizada y funciona correctamente.