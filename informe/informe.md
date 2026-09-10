# Informe de Desarrollo Técnico - Plataforma SimpleRisk

Este documento detalla el proceso de instalación, configuración y resolución de conflictos arquitectónicos implementado para el despliegue reproducible de la plataforma SimpleRisk en el entorno corporativo.

---

## 1. Proceso de Instalación Reproducible (Docker Compose)
Para garantizar la portabilidad y replicabilidad del entorno exigida por la cátedra, se optó por una arquitectura de microservicios contenedorizados mediante **Docker Compose**. El entorno consta de dos servicios principales interconectados de forma segura a través de una red aislada (`simplerisk-net`):

1. **Backend de Datos (simplerisk-mysql):** Un contenedor basado en la imagen oficial de `mysql:8.0`, configurado con almacenamiento persistente mapeado al volumen local `db_data` para evitar la pérdida de información al apagar el entorno.
2. **Frontend Aplicativo (simplerisk-web):** Un contenedor basado en la imagen oficial `simplerisk/simplerisk:latest`, que aloja el servidor Apache y el core del sistema de gobernanza.

---

## 2. Resolución de Conflictos y Configuración de Puertos
Durante la etapa de despliegue inicial en el sistema operativo Windows, se identificaron dos colisiones críticas de red que impedían el acceso local:

* **Conflicto del Puerto 80 (HTTP Nativo):** El puerto estándar de internet se encontraba bloqueado en la máquina anfitriona debido a la presencia previa de servicios de XAMPP (Apache en segundo plano).
* **Conflicto del Puerto 8080 (Proxy/Tomcat):** Se detectaron procesos fantasma reteniendo el puerto 8080 en la memoria caché de los navegadores (Google Chrome / Microsoft Edge Chromium), arrojando errores de protocolo e interfaces bloqueadas de forma persistente.

### Solución Arquitectónica Implementada
Para aislar por completo el laboratorio técnico y evadir los bloqueos ocultos de la máquina local, se modificó el mapeo perimetral en el archivo `docker-compose.yml`. Se configuró el puerto **`9000`** de Windows para redirigir el tráfico de forma directa hacia el puerto **`443` (HTTPS Seguro)** interno del contenedor aplicativo. 

Esta redirección forzó al software a generar sus certificados de seguridad SSL locales de manera nativa, mitigando los fallos de respuesta vacía (`ERR_EMPTY_RESPONSE`) y permitiendo el acceso transparente y limpio mediante la URL segura:
```text
https://localhost:9000
```

---

## 3. Conclusión de la Arquitectura
El entorno ha quedado operativo, validado y con persistencia de datos asentada en disco duro virtual. La segregación de funciones (SoD) se aplicó de forma exitosa mediante tres perfiles diferenciados, y la consistencia técnica entre los registros de la base de datos de Docker y los reportes formales entregados al Directorio de la clínica se encuentra 100% consolidada.
 
