# Informe del TP — Gestión de Riesgos con SimpleRisk

## 1. Introducción
Se analiza una clínica privada de 120 empleados que atiende aproximadamente 800 pacientes por día y gestiona historias clínicas digitales, datos de obras sociales y facturación.

El objetivo es construir un registro inicial de riesgos, priorizar los escenarios de mayor impacto y proponer tratamientos y planes de acción.

## 2. Metodología
Se utiliza una matriz cualitativa de Probabilidad × Impacto, con valores de 1 a 5. El nivel se obtiene multiplicando ambos valores.

La valoración se fundamenta en razonamiento explícito sobre exposición, dependencia operativa, sensibilidad de la información y consecuencias.

## 3. Riesgos
Se definieron siete riesgos específicos. El registro completo se encuentra en "configuracion/riesgos.md".

Los riesgos de mayor prioridad son:
1. Ransomware sobre servidores de historias clínicas — 20.
2. Phishing contra personal administrativo — 16.
3. Acceso indebido a historias clínicas — 15.
4. Caída del sistema de historias clínicas — 15.
5. Fuga de datos de obras sociales — 15.

## 4. Planes de acción
Se proponen tres planes prioritarios:
- Backups offline/inmutables y recuperación ante ransomware.
- Implementación de MFA y programa anti-phishing.
- Revisión de privilegios y auditoría de accesos a historias clínicas.

## 5. Análisis crítico
SimpleRisk permite operacionalizar una matriz sencilla y mantener un registro de riesgos, propietarios, tratamientos y acciones. Su principal ventaja es la facilidad de uso y priorización rápida.

Como alternativa se analiza FAIR. FAIR busca modelar y cuantificar el riesgo, especialmente en términos financieros, y puede ser más apropiado cuando la dirección necesita comparar inversiones de seguridad mediante exposición económica.

La matriz de SimpleRisk es adecuada para un registro inicial y priorización operativa. FAIR requiere más datos, conocimiento y esfuerzo analítico, pero permite una cuantificación más profunda.

## 6. Integración propuesta
Se propone integrar SimpleRisk con un sistema de tickets mediante webhook. Cuando un riesgo alcance nivel alto, SimpleRisk puede generar una notificación que cree o actualice un ticket con:
- ID del riesgo.
- Nombre.
- Nivel.
- Propietario.
- Tratamiento.
- Fecha objetivo.

El ticket permitiría seguimiento, responsables, evidencias y cierre.

## 7. Actividad optativa D1
Como análisis complementario se identifican controles a verificar en una instalación de SimpleRisk:
1. Uso de HTTPS/TLS y encabezados de seguridad.
2. Gestión segura de sesiones y cookies.
3. Versiones soportadas de PHP/MySQL y permisos mínimos de archivos.

Estas comprobaciones son recomendaciones de revisión y no deben presentarse como hallazgos observados hasta ser verificadas en la instalación concreta.

## 8. Evidencias
Agregar las capturas reales en "informe/capturas/":
- Instalación funcionando.
- Usuarios.
- Riesgo de prueba.
- Riesgos del escenario.
- Planes de acción.
- Reportes de SimpleRisk.

## 9. Conclusión
La prioridad de la clínica debe ser reducir el riesgo asociado a indisponibilidad y exposición de información sensible. El tratamiento debe combinar controles preventivos, detectivos y de recuperación. La gestión debe mantenerse como un proceso continuo y no como una actividad única.
