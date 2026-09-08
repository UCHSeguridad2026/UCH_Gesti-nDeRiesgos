# TP Seguridad de Sistemas — SimpleRisk

## Datos del alumno

- **Nombre completo:** Maximiliano Zapata
- **LU:** 31493739
- **Email institucional:** zapatamaximilianp@gmail.com
- **Comisión:** 4G

## Instrucciones para levantar el entorno

Resumen de los pasos (detalle completo en
[`entorno/instrucciones.md`](entorno/instrucciones.md)):

1. Instalar WSL2 en Windows: `wsl --install` (requiere reiniciar).
2. Instalar Docker Desktop (instalación per-user, backend WSL2) y verificar
   que el motor esté corriendo.
3. Descargar y levantar el contenedor de SimpleRisk:
   ```bash
   docker pull simplerisk/simplerisk
   docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk
   ```
4. Acceder a **https://localhost/**, aceptando la advertencia de
   certificado autofirmado (esperable en un entorno local de pruebas).
5. Completar el wizard **"Default Admin Account Creation"** para crear la
   cuenta de administrador inicial.

## Decisiones de diseño

Para este TP se optó por **no usar el escenario de la clínica sugerido por
la cátedra**, y en su lugar se modeló un escenario propio: la fiambrería
**"Punta Pueyrredón"**.

Características del negocio modelado:

- Comercio de barrio con **5 empleados**.
- Sistema de gestión **EPyme** para facturación y administración.
- **Cámaras de seguridad** para el local.
- **Control de stock** de mercadería.
- **Pagos con QR y tarjeta** (posnet / billeteras virtuales).
- Manejo de **datos de clientes, proveedores y empleados**.

Este escenario se usó como base para relevar activos, identificar riesgos y
cargarlos en SimpleRisk (ver [`configuracion/riesgos.md`](configuracion/riesgos.md)
y [`informe/informe.md`](informe/informe.md)).

## Verificación

Palabra clave de verificación: **girasol**

(Esta sección confirma la lectura completa del enunciado del TP, según lo
solicitado por la cátedra.)

## Checklist de auto-revisión

- [ ] No hay credenciales en el repositorio.
- [ ] El archivo `.gitignore` está correctamente configurado.
- [ ] Las capturas de pantalla no muestran datos sensibles.
- [ ] Los archivos `.sql` o dumps no están subidos.
- [ ] El informe está en un formato legible.
- [ ] El reporte ejecutivo está completo.
- [ ] Los mensajes de commit son descriptivos.
- [ ] Mi branch está actualizada y funciona correctamente.
