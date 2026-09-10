# Parte D — Actividades optativas

# D1 — Análisis de seguridad de la instalación de SimpleRisk

## 1. Objetivo

El objetivo de esta actividad es analizar la seguridad de la propia instalación de SimpleRisk utilizada durante el trabajo práctico.

El análisis no busca demostrar la existencia de vulnerabilidades explotables en la aplicación, sino identificar **malas prácticas o superficies de riesgo potenciales** que deberían revisarse antes de utilizar una instalación de SimpleRisk en un entorno productivo.

La instalación utilizada para el trabajo se ejecuta mediante Docker Compose y está compuesta por:

* SimpleRisk.
* MySQL 8.0.
* Comunicación mediante HTTP/HTTPS.
* Persistencia mediante volúmenes Docker.

El entorno fue diseñado para laboratorio, por lo que algunas configuraciones son aceptables para una práctica pero deberían modificarse para un escenario real.

---

# 2. Hallazgos

Se identificaron tres aspectos principales que requieren atención:

| ID    | Hallazgo                                               | Tipo                        | Riesgo                                                                                   | Prioridad |
| ----- | ------------------------------------------------------ | --------------------------- | ---------------------------------------------------------------------------------------- | --------- |
| D1-01 | Ausencia de headers HTTP de seguridad                  | Configuración web           | XSS, clickjacking y otras técnicas de ataque pueden contar con menos capas de protección | Media     |
| D1-02 | HTTP disponible sin redirección obligatoria a HTTPS    | Configuración de transporte | Posible envío de credenciales o sesiones mediante canal no cifrado                       | Alta      |
| D1-03 | Permisos de archivos y configuración deben endurecerse | Sistema de archivos         | Exposición o modificación de configuración y archivos sensibles                          | Alta      |

Como observación adicional, el entorno de laboratorio utiliza un certificado HTTPS autofirmado. Esto no constituye por sí mismo una vulnerabilidad de SimpleRisk, pero no sería apropiado para una instalación productiva.

---

# 3. D1-01 — Ausencia de headers HTTP de seguridad

## Descripción

SimpleRisk no incorpora por defecto determinados headers HTTP de seguridad y delega esta configuración en el servidor web o reverse proxy.

La documentación oficial de SimpleRisk indica específicamente que la aplicación no agrega automáticamente headers como:

* `Strict-Transport-Security`;
* `Content-Security-Policy`;
* `X-Frame-Options`;
* otros headers de seguridad.

Por lo tanto, si el servidor web no los configura, las respuestas HTTP pueden carecer de estas capas adicionales de protección.

## Riesgo

La ausencia de estos headers no significa que exista automáticamente una vulnerabilidad explotable, pero elimina mecanismos de defensa que pueden reducir el impacto de determinados ataques.

Por ejemplo:

* `X-Frame-Options` ayuda a reducir riesgos de clickjacking.
* `Content-Security-Policy` permite limitar los recursos que el navegador puede ejecutar o cargar.
* `Strict-Transport-Security` ayuda a indicar al navegador que debe utilizar HTTPS.
* `X-Content-Type-Options: nosniff` reduce determinados problemas relacionados con interpretación incorrecta de tipos MIME.

En una aplicación que administra información sobre riesgos, usuarios, propietarios y planes de tratamiento, agregar estas capas resulta conveniente.

## Mitigación propuesta

Los headers deberían configurarse en Apache, Nginx o en el reverse proxy ubicado delante de SimpleRisk.

Una configuración de referencia podría incluir:

```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
```

También debería evaluarse una política `Content-Security-Policy` compatible con la aplicación antes de activarla de forma restrictiva, ya que una política incorrecta podría afectar funcionalidades legítimas.

## Verificación

Después de implementar la mitigación se debería comprobar la respuesta HTTP mediante:

```bash
curl -k -I https://localhost:8443
```

y verificar que los headers configurados aparezcan en la respuesta.

## Prioridad

**Media.**

La ausencia de headers no implica por sí sola un compromiso de la aplicación, pero representa una oportunidad de hardening sencilla y de bajo costo.

---

# 4. D1-02 — Disponibilidad de HTTP sin redirección obligatoria a HTTPS

## Descripción

Durante la instalación del laboratorio se publicaron dos puertos:

* `8080` → HTTP.
* `8443` → HTTPS.

El acceso principal se realiza mediante HTTPS:

`https://localhost:8443`

Sin embargo, SimpleRisk no implementa internamente una redirección automática de HTTP hacia HTTPS. La documentación oficial establece que la aplicación delega esta función al servidor web o reverse proxy.

Por lo tanto, publicar simultáneamente HTTP y HTTPS sin una política de redirección o bloqueo puede dejar disponible un canal de comunicación no cifrado.

## Riesgo

Si un usuario accediera a SimpleRisk mediante HTTP desde una red donde exista posibilidad de interceptación del tráfico, podría existir exposición de información de sesión o de datos enviados por el navegador.

El riesgo es especialmente relevante para una aplicación que maneja:

* cuentas de usuarios;
* autenticación;
* información de riesgos;
* propietarios;
* planes de tratamiento;
* información potencialmente sensible sobre la infraestructura de seguridad de la organización.

Aunque el entorno utilizado es local, esta configuración no debería trasladarse directamente a producción.

## Mitigación propuesta

La alternativa recomendada es que HTTPS sea el único protocolo disponible para los usuarios.

Una configuración de producción debería:

1. Mantener HTTPS habilitado.
2. Redireccionar todas las solicitudes HTTP hacia HTTPS, o directamente bloquear HTTP si no es necesario.
3. Utilizar un certificado válido emitido por una autoridad certificadora confiable.
4. Habilitar HSTS una vez verificado que todo el servicio funciona correctamente mediante HTTPS.

Por ejemplo, en Apache se puede implementar una redirección:

```apache
Redirect permanent / https://simplerisk.example.com/
```

La documentación oficial de SimpleRisk recomienda realizar esta redirección en la configuración del servidor web y no en la propia aplicación.

## Situación en el laboratorio

En este trabajo se mantiene el puerto HTTP únicamente para facilitar la demostración y el acceso local.

El acceso operativo utilizado durante las pruebas fue:

`https://localhost:8443`

Para una implementación productiva se eliminaría la exposición innecesaria del puerto HTTP o se configuraría una redirección permanente hacia HTTPS.

## Prioridad

**Alta.**

El transporte cifrado debe considerarse un requisito básico cuando SimpleRisk se utiliza fuera de un entorno de laboratorio.

---

# 5. D1-03 — Permisos de archivos y configuración

## Descripción

SimpleRisk necesita determinados permisos de escritura durante la instalación y para algunas operaciones posteriores.

La documentación oficial indica que el usuario del servidor web necesita acceso de lectura y escritura sobre determinados componentes del directorio de SimpleRisk, incluyendo:

* `includes/config.php`;
* logs;
* directorios de cargas;
* determinados componentes utilizados durante la ejecución.

Esto genera una superficie que debe controlarse cuidadosamente.

El problema no consiste en que SimpleRisk necesite permisos de escritura, sino en otorgar permisos más amplios de los estrictamente necesarios.

## Riesgo

Si toda la aplicación queda con permisos de escritura excesivamente permisivos, una cuenta o proceso comprometido podría modificar archivos que posteriormente sean ejecutados por el servidor web.

También existe riesgo de exposición de información sensible contenida en archivos de configuración.

Por ejemplo, `config.php` contiene información necesaria para que SimpleRisk pueda conectarse a la base de datos. La documentación de actualización de SimpleRisk recomienda proteger este archivo y evitar mantener copias en ubicaciones accesibles desde el servidor web.

## Mitigación propuesta

Se debería aplicar el principio de mínimo privilegio al sistema de archivos.

Como referencia para una instalación Linux, SimpleRisk documenta un esquema en el cual el propietario es el usuario del servidor web y se utilizan permisos restrictivos para directorios y archivos.

Una configuración de referencia podría ser:

```bash
chown -R www-data:www-data /var/www/simplerisk

find /var/www/simplerisk -type d -exec chmod 750 {} \;
find /var/www/simplerisk -type f -exec chmod 640 {} \;
```

Los directorios que realmente necesiten escritura deben habilitarse de manera específica.

En un entorno Docker, el mismo principio debe aplicarse dentro de la imagen o volumen utilizado por SimpleRisk.

Además:

* `config.php` debe protegerse especialmente.
* No deben utilizarse permisos `777`.
* Las copias de configuración deben mantenerse fuera del document root.
* Los secretos no deben almacenarse dentro del repositorio Git.
* Los volúmenes de Docker deben tener permisos controlados.
* El acceso al host Docker debe considerarse altamente privilegiado.

## Situación en el laboratorio

La instalación utilizada para el TP funciona correctamente con los permisos necesarios para que SimpleRisk pueda ejecutarse.

Sin embargo, al tratarse de un entorno académico, no se realizó una auditoría exhaustiva de permisos de cada archivo del contenedor.

Por este motivo, el hallazgo se considera una **recomendación de hardening** y no una vulnerabilidad demostrada.

## Prioridad

**Alta.**

Una mala configuración de permisos puede transformar un compromiso de bajo nivel en una modificación persistente de la aplicación o una exposición de credenciales.

---

# 6. Observación adicional — Certificado HTTPS autofirmado

## Situación

El entorno del trabajo utiliza HTTPS mediante:

`https://localhost:8443`

El certificado utilizado es autofirmado porque la instalación está destinada exclusivamente al laboratorio.

Esto genera una advertencia en el navegador, ya que el certificado no fue emitido por una autoridad certificadora reconocida.

## Riesgo

Un certificado autofirmado no es necesariamente inseguro en un entorno controlado. El problema aparece cuando los usuarios aceptan advertencias de certificado sin verificar su autenticidad.

En producción, esta práctica podría facilitar ataques de intermediario si los usuarios están acostumbrados a ignorar advertencias TLS.

## Mitigación

Para producción se debería utilizar:

* un certificado emitido por una CA confiable;
* renovación automática;
* configuración TLS moderna;
* redirección HTTP → HTTPS;
* HSTS.

La documentación oficial de SimpleRisk recomienda utilizar un certificado real para instalaciones que superen el escenario de demostración o laboratorio.

## Prioridad

**Media para el laboratorio / Alta para producción.**

---

# 7. Revisión de versiones de PHP y MySQL

La versión de los componentes de infraestructura también debe formar parte del hardening.

SimpleRisk documenta actualmente como requisito **PHP 8.3.0 o superior** y recomienda mantener PHP dentro de versiones que continúen recibiendo actualizaciones de seguridad.

En cuanto a MySQL, la versión utilizada en este TP es:

**MySQL 8.0**

El riesgo no debe evaluarse solamente por el número de versión, sino por si la versión concreta continúa recibiendo actualizaciones de seguridad y por si la imagen Docker utilizada está actualizada.

Por este motivo, se recomienda evitar utilizar etiquetas genéricas o imágenes antiguas sin verificar su fecha de actualización.

En un entorno productivo debería establecerse un procedimiento de actualización periódica que contemple:

1. verificar versiones actuales;
2. revisar vulnerabilidades conocidas;
3. realizar backup;
4. probar la actualización;
5. actualizar la imagen;
6. verificar SimpleRisk;
7. conservar un mecanismo de rollback.

La propia documentación de SimpleRisk señala que el operador es responsable de mantener actualizado el stack de infraestructura.

---

# 8. Priorización de las medidas

Las medidas identificadas pueden priorizarse de la siguiente manera:

| Prioridad  | Hallazgo                                 | Mitigación                                                        |
| ---------- | ---------------------------------------- | ----------------------------------------------------------------- |
| Alta       | HTTP disponible sin enforcement de HTTPS | Redireccionar/bloquear HTTP y utilizar certificado válido         |
| Alta       | Permisos de archivos demasiado amplios   | Aplicar mínimo privilegio y proteger `config.php`                 |
| Media      | Ausencia de headers de seguridad         | Configurar HSTS, CSP, X-Frame-Options y otros headers             |
| Media/Alta | Certificado autofirmado                  | Utilizar CA confiable en producción                               |
| Media      | Componentes desactualizados              | Establecer proceso de actualización y gestión de vulnerabilidades |

---

# 9. Checklist de hardening propuesto

Antes de utilizar SimpleRisk en producción se recomienda verificar:

* [ ] PHP en una versión soportada y actualizada.
* [ ] MySQL actualizado y con soporte de seguridad.
* [ ] HTTP redireccionado o bloqueado.
* [ ] HTTPS configurado con certificado válido.
* [ ] HSTS habilitado después de validar HTTPS.
* [ ] Headers HTTP de seguridad configurados.
* [ ] `config.php` protegido.
* [ ] Sin permisos `777`.
* [ ] Directorios de escritura limitados.
* [ ] Secretos fuera del código fuente.
* [ ] Credenciales de base de datos con mínimo privilegio.
* [ ] Backups de la base de datos.
* [ ] Backups almacenados fuera del host.
* [ ] Logs protegidos y con rotación.
* [ ] Actualizaciones de SimpleRisk y del sistema operativo planificadas.
* [ ] Revisión periódica de vulnerabilidades.
* [ ] Acceso administrativo protegido con MFA cuando esté disponible.
* [ ] Exposición de puertos limitada mediante firewall.

---

# 10. Conclusión

El análisis demuestra que instalar correctamente una aplicación no implica necesariamente que la instalación esté completamente endurecida desde el punto de vista de seguridad.

En el caso de SimpleRisk, la propia documentación deja parte de la seguridad en manos del administrador del servidor web y del sistema operativo. Entre las medidas más importantes se encuentran el enforcement de HTTPS, la configuración de headers de seguridad y el control estricto de los permisos de archivos.

Para el entorno académico, algunas decisiones —como utilizar un certificado autofirmado y mantener el puerto HTTP publicado— son aceptables debido a que la aplicación se ejecuta localmente.

Para una implementación real, estas configuraciones deberían modificarse antes de exponer SimpleRisk a usuarios externos o a una red corporativa.

La conclusión principal es que la seguridad de SimpleRisk debe analizarse como la seguridad de un **stack completo**:

**Sistema operativo + Docker + servidor web + PHP + SimpleRisk + MySQL + TLS + permisos + secretos + backups**

y no únicamente como la seguridad de la aplicación web.
