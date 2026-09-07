# D1 — Análisis de Seguridad de la Instalación por Defecto de SimpleRisk

## Vulnerabilidad 1 — Certificado SSL autofirmado por defecto

La imagen de Docker de SimpleRisk trae un certificado autofirmado genérico en lugar de uno emitido por una CA real. Esto entrena a los usuarios a ignorar advertencias de "conexión no segura" del navegador, lo cual es un mal hábito de seguridad si se replicara sin corrección en un entorno de producción.

**Mitigación propuesta:** en un entorno productivo, reemplazar el certificado autofirmado por uno válido emitido por una CA reconocida (por ejemplo, Let's Encrypt), o por un certificado interno de la organización si se usa en red privada.

## Vulnerabilidad 2 — Puertos expuestos sin restricción de interfaz de red

El comando de instalación estándar (`docker run -p 80:80 -p 443:443 simplerisk/simplerisk`) expone la aplicación a **todas** las interfaces de red del host, no solo a `localhost`. Si este mismo comando se ejecutara en un servidor con IP pública sin un firewall configurado, cualquier persona en internet podría acceder al panel de login de SimpleRisk.

**Mitigación propuesta:** restringir el binding a la interfaz local con `-p 127.0.0.1:443:443`, o colocar un firewall / reverse proxy delante del contenedor que controle el acceso.

## Vulnerabilidad 3 — Ausencia de política de bloqueo de intentos de login

Durante la configuración inicial y la creación de usuarios, se observó en el panel Settings → Security la existencia de opciones de política de contraseñas y sesión, pero no hay una política de bloqueo de cuenta tras múltiples intentos fallidos activada por defecto. Esto deja la instalación expuesta a ataques de fuerza bruta contra el panel de administración.

**Mitigación propuesta:** revisar y activar explícitamente, en Settings → Security, las opciones de bloqueo temporal de cuenta tras N intentos fallidos de login.

## Conclusión

Ninguna de estas tres observaciones es exclusiva de SimpleRisk — son patrones comunes en instalaciones "quick start" de aplicaciones web mediante Docker, donde se prioriza la facilidad de prueba sobre el hardening de seguridad. Se recomienda que cualquier instalación destinada a un entorno real (no solo de prueba/aprendizaje) revise y corrija estos tres puntos antes de exponer el sistema fuera de un entorno de laboratorio.
