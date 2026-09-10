# Informe del trabajo práctico

## 1. Resumen del escenario

La organización analizada es una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día. Sus procesos dependen de historias clínicas digitales, sistemas de turnos, integraciones con obras sociales y facturación.

## 2. Alcance

El análisis cubre identidad y acceso, historia clínica electrónica, correo, red, servidores, backups, integraciones con terceros, documentación física y continuidad operativa. No se evalúan en detalle dispositivos médicos especializados ni la seguridad física completa de todas las sedes.

## 3. Método

Se utiliza una matriz de probabilidad por impacto de 1 a 5. La matriz facilita priorizar rápidamente y comunicar resultados a la dirección. Para evitar una valoración arbitraria, cada puntuación se acompaña de una justificación contextual.

## 4. Resultados

El registro completo se encuentra en `configuracion/riesgos.md`. Los riesgos prioritarios son ransomware, acceso indebido a historias clínicas, phishing y fallas de recuperación. Los planes PA-01, PA-02 y PA-03 atienden los riesgos críticos y altos con mayor impacto sobre continuidad, confidencialidad e integridad.

## 5. Comparación con NIST SP 800-30

La matriz de SimpleRisk es simple, rápida y útil para establecer un registro inicial. Su principal limitación es que puede ocultar incertidumbre: dos riesgos con el mismo producto P×I pueden tener causas, controles y consecuencias muy diferentes.

NIST SP 800-30 propone preparar la evaluación, identificar fuentes de amenaza, eventos, vulnerabilidades, predisposiciones, probabilidad, impacto y riesgo, y comunicar los resultados para mantenerlos actualizados. Ofrece más trazabilidad y contexto, pero requiere más tiempo, evidencias y participación de distintas áreas.

Para una clínica que necesita iniciar rápidamente un registro, SimpleRisk resulta adecuado como sistema operativo de seguimiento. Para decisiones de inversión, cambios importantes o riesgos regulatorios, conviene enriquecer cada registro con el razonamiento estructurado de NIST.

## 6. Integración propuesta

Se propone integrar SimpleRisk con un sistema de tickets mediante un webhook o tarea programada:

1. Detectar riesgos nuevos o modificados con nivel alto/crítico.
2. Crear un ticket con ID, descripción, propietario, vencimiento y tratamiento.
3. Guardar en SimpleRisk el identificador del ticket y su estado.
4. Notificar cambios de estado al responsable y al comité de seguridad.
5. No enviar secretos ni datos clínicos; solo metadatos mínimos del riesgo.

La integración debe autenticar el webhook, validar certificados, limitar permisos, registrar errores y evitar duplicados mediante el ID del riesgo.

## 7. Actividad optativa elegida: D1

Se recomienda revisar tres áreas de la instalación: versiones soportadas de PHP/base de datos, permisos de archivos y configuración de sesión/headers HTTP. Las mitigaciones son mantener componentes soportados, restringir permisos, usar HTTPS local cuando corresponda, activar cookies seguras y revisar cabeceras como HSTS, CSP y protección contra framing según compatibilidad.

## 8. Evidencias

Las capturas de instalación, usuarios, riesgos y planes deben ubicarse en `informe/capturas/` sin credenciales ni datos reales.

## 9. Referencias

- NIST, *Guide for Conducting Risk Assessments*, SP 800-30 Rev. 1: https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final
- SimpleRisk, documentación oficial: https://www.simplerisk.com/documentation
- ISO, ISO/IEC 27005: https://www.iso.org/standard/75281.html
- Verizon, Data Breach Investigations Report: https://www.verizon.com/business/resources/reports/dbir/

