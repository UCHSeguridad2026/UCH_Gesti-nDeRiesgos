# Trabajo Práctico: Gestión de Riesgos con SimpleRisk

**Estudiante:** Emilia Ortiz  
**LU:** 31030898  
**Email Institucional:** ortizemilia@uch.edu.ar 
**Comisión:** G 

---

## Instrucciones para levantar el entorno

Para auditar este trabajo práctico y levantar la instancia de SimpleRisk, siga estos pasos:

1. Clonar el repositorio y posicionarse en la rama correspondiente a esta entrega.
2. Navegar hacia el directorio del entorno:
   `cd entregas/Ortiz-Emilia-31030898/entorno`
3. Ejecutar el siguiente comando para levantar los contenedores en segundo plano:
   `docker compose up -d`
4. Ingresar desde el navegador a la interfaz web mediante conexión segura:
   `https://localhost` *(Aceptar la advertencia de certificado autofirmado local)*.
5. Los usuarios de prueba y sus roles están documentados en `configuracion/usuarios.md`.

---

## Decisiones de diseño tomadas

El escenario simulado corresponde a una clínica privada (120 empleados, 800 pacientes diarios) fuertemente dependiente de Historias Clínicas Digitales (HCD) y conectividad con obras sociales. 
Se optó por una evaluación cualitativa de riesgos (Probabilidad x Impacto) enfocada en las amenazas estadísticas más frecuentes del sector salud (Ransomware y fuga de datos internos), justificadas en reportes de la industria.

### Verificación
girasol

---

## Checklist de Auto-Revisión

- [x] No hay credenciales en el repositorio
- [x] El .gitignore está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos .sql o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona

*Nota: Se realizó la actividad optativa D4. La propuesta de mejora documentada como issue de GitHub se encuentra en informe/optativa_D4_issue.md*