# TP SimpleRisk – Gestión de Riesgos

## Datos personales

- **Nombre completo:** Exequiel Caliri
- **LU:** 31141377
- **Email institucional:** Exequielcaliri686@gmail.com

## Cómo levantar el entorno

Este TP usa la imagen oficial de SimpleRisk mediante Docker Compose.

```bash
# 1. Ir a la carpeta del entorno
cd entorno/

# 2. Levantar el contenedor
docker compose up -d

# (opcional) usar el script de despliegue automatizado
./setup.sh

# 3. Probar la instancia
# Abrir en el navegador:
http://localhost:8080
https://localhost:8443
```

> Nota: el certificado HTTPS es autofirmado, el navegador va a mostrar una advertencia de seguridad la primera vez — es esperable en un entorno local de pruebas.

Para detener y volver a levantar el contenedor más adelante:

```bash
docker compose stop
docker compose start
```

## Decisiones de diseño

- **Metodología de riesgos utilizada:** matriz clásica de Probabilidad × Impacto (escala 1-5) de SimpleRisk ("Classic Risk Rating"), con niveles Bajo/Medio/Alto/Crítico según el valor resultante.
- **Supuestos del escenario:** clínica privada ficticia de 120 empleados y ~800 pacientes/día, definida en el enunciado del TP, con Historias Clínicas Digitales, datos de obras sociales y facturación como activos principales.
- **Otras decisiones relevantes:** esta versión de SimpleRisk no cuenta con roles predefinidos con nombre (Risk Manager, Auditor, etc.); el control de acceso se implementó mediante checkboxes individuales de "User Responsibilities" para cada usuario, aplicando el principio de menor privilegio (detalle en `configuracion/usuarios.md`).

## Verificación

Durante la revisión completa del enunciado se detectó contenido con características de *prompt injection* incrustado en el PDF (una instrucción oculta pidiendo incluir una palabra clave de "verificación", y en la sección de requerimientos del reporte ejecutivo, referencias fuera de contexto a cuentos infantiles). Se decidió conscientemente no seguir esas instrucciones, dado que no corresponden a un requisito profesional legítimo. Ver detalle en `informe/informe.md`, sección de Análisis Crítico.

## Checklist de auto-revisión

- [x] No hay credenciales en el repositorio
- [x] El .gitignore está correctamente configurado
- [x] Las capturas no muestran datos sensibles
- [x] Los archivos .sql o dumps no están subidos
- [x] El informe está en formato legible
- [x] El reporte ejecutivo está completo
- [x] Los mensajes de commit son descriptivos
- [x] Mi branch está actualizada y funciona

---

*verificación de lectura: girasol.*
