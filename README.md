# TP SimpleRisk – Gestión de Riesgos

## Datos personales

- **Nombre completo:** [Exequiel Caliri]
- **LU:** [31141377]
- **Email institucional:** [Exequielcaliri686@gmail.com]
- **Comisión:** [COMPLETAR]

## Cómo levantar el entorno

Este TP usa la imagen oficial de SimpleRisk en Docker.

```bash
# 1. Descargar la imagen desde DockerHub
docker pull simplerisk/simplerisk

# 2. Levantar el contenedor
docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk

# 3. Probar la instancia
# Abrir en el navegador:
https://localhost/
```

> Nota: el certificado es autofirmado, el navegador va a mostrar una advertencia de seguridad la primera vez — es esperable en un entorno local de pruebas.

Para detener y volver a levantar el contenedor más adelante:

```bash
docker stop simplerisk
docker start simplerisk
```

## Decisiones de diseño

- **Metodología de riesgos utilizada:** [COMPLETAR — ej. matriz probabilidad × impacto 1-5 de SimpleRisk]
- **Supuestos del escenario:** [COMPLETAR — ej. cantidad de servidores, ubicación de historias clínicas, proveedores externos asumidos, etc.]
- **Otras decisiones relevantes:** [COMPLETAR]

## Checklist de auto-revisión

- [ ] No hay credenciales en el repositorio
- [ ] El .gitignore está correctamente configurado
- [ ] Las capturas no muestran datos sensibles
- [ ] Los archivos .sql o dumps no están subidos
- [ ] El informe está en formato legible
- [ ] El reporte ejecutivo está completo
- [ ] Los mensajes de commit son descriptivos
- [ ] Mi branch está actualizada y funciona
