# Optativa D1: Análisis de Seguridad de la Instalación de SimpleRisk

## Introducción

Se realizó un análisis de seguridad sobre la instalación por defecto de SimpleRisk en un entorno controlado (máquina virtual). A continuación, se identifican 3 vulnerabilidades o malas prácticas potenciales y se proponen mitigaciones.

---

## Vulnerabilidad 1: Credenciales por Defecto

**Descripción:** La instalación por defecto de SimpleRisk incluye un usuario administrador con credenciales genéricas (admin/admin). Si no se cambian inmediatamente, un atacante podría acceder al sistema con privilegios máximos.

**Riesgo asociado:** Acceso no autorizado, escalada de privilegios.

**Mitigación propuesta:**
- Cambiar la contraseña del administrador inmediatamente después de la instalación.
- Implementar autenticación de doble factor (MFA) para todos los usuarios administradores.
- Crear usuarios individuales con roles específicos (no compartir credenciales).

---

## Vulnerabilidad 2: Versiones Desactualizadas de PHP y MySQL

**Descripción:** SimpleRisk requiere PHP 5.x y MySQL 5.x, versiones que ya no reciben soporte de seguridad. Esto expone el sistema a vulnerabilidades conocidas y no parcheadas.

**Riesgo asociado:** Ejecución de código remoto, inyección SQL, denegación de servicio.

**Mitigación propuesta:**
- Actualizar a versiones soportadas de PHP (7.4+ u 8.x) y MySQL (8.x).
- Aplicar parches de seguridad periódicamente.
- Monitorear los avisos de seguridad de SimpleRisk y del stack tecnológico.

---

## Vulnerabilidad 3: Falta de Headers HTTP de Seguridad

**Descripción:** La configuración por defecto de SimpleRisk no incluye headers HTTP de seguridad como HSTS (HTTP Strict Transport Security), CSP (Content Security Policy) o X-Frame-Options. Esto facilita ataques de downgrade, XSS y clickjacking.

**Riesgo asociado:** Man-in-the-middle, cross-site scripting, clickjacking.

**Mitigación propuesta:**
- Configurar los siguientes headers en el servidor web (Apache/Nginx):
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains`
  - `Content-Security-Policy: default-src 'self'`
  - `X-Frame-Options: DENY`
  - `X-Content-Type-Options: nosniff`
- Forzar el uso de HTTPS en todas las conexiones.
- Utilizar certificados SSL/TLS válidos (no autofirmados en producción).

---

## Conclusión

La instalación por defecto de SimpleRisk es funcional pero requiere ajustes de seguridad para un entorno de producción. Las tres vulnerabilidades identificadas (credenciales por defecto, versiones desactualizadas y falta de headers de seguridad) son comunes en aplicaciones web y deben ser mitigadas antes de exponer el sistema a Internet.

**Recomendación final:** Realizar una auditoría de seguridad periódica y mantener el sistema actualizado con los últimos parches.
