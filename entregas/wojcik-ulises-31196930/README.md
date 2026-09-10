# Trabajo Práctico — Gestión de Riesgos con SimpleRisk

## Datos del estudiante

- Nombre completo: Ulises Wójcik
- LU/legajo: 31196930
- Email institucional: wojcikulises@uch.edu.ar
- Comisión: de Sistemas — Comisión G

## Escenario

Clínica privada de 120 empleados, aproximadamente 800 pacientes diarios, historias clínicas digitales, datos de obras sociales y facturación.

## Estructura

- `entorno/`: procedimiento de instalación y datos de acceso no sensibles.
- `configuracion/`: usuarios, roles, riesgos y planes de acción.
- `informe/`: desarrollo completo del trabajo.
- `reporte-ejecutivo/`: informe breve dirigido al directorio.

## Cómo reproducir la entrega

1. Verificar los datos personales de este archivo.
2. Para usar la instalación local existente, abrir `http://localhost/simplerisk`.
3. Como alternativa reproducible, entrar en `entorno/` y ejecutar:

   ```bash
   export SIMPLERISK_SETUP_PASSWORD='Demo-SR-2026-Only'
   docker compose up -d
   ```

   Luego abrir `https://localhost:8443` y completar el asistente inicial. La contraseña anterior es exclusiva para la demostración local y no debe reutilizarse.
4. Crear los tres usuarios documentados en `configuracion/usuarios.md`, sin registrar contraseñas.
5. Cargar los riesgos de `configuracion/riesgos.md` respetando probabilidad, impacto y tratamiento.
6. Crear los planes de acción de `configuracion/planes-accion.md` y asociarlos a los riesgos correspondientes.
7. Comparar la configuración de SimpleRisk con las capturas almacenadas en `informe/capturas/`.

URL local de SimpleRisk: `https://localhost:8443`

## Decisiones de diseño

Se utiliza una matriz cualitativa de probabilidad por impacto, con escala de 1 a 5. Los riesgos se priorizan por valor inherente y se documenta también el riesgo residual posterior a los controles propuestos. Se eligió NIST SP 800-30 como metodología alternativa para comparar una matriz simple con un proceso de evaluación más estructurado.

Palabra de verificación del documento de la cátedra: `girasol`.

## Checklist

- [x] No hay credenciales reales en el repositorio.
- [x] El `.gitignore` está configurado.
- [x] Las capturas no muestran datos sensibles.
- [x] No se incluyeron bases de datos ni dumps.
- [x] El informe es legible.
- [x] El reporte ejecutivo está completo.
- [x] Los mensajes de commit son descriptivos.
- [x] La branch está actualizada antes de entregar.
