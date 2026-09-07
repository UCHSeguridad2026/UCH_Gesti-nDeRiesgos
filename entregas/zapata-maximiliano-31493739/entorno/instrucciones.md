# Entorno de trabajo

Documentación del entorno real utilizado para levantar SimpleRisk durante la
realización de este TP.

## Sistema operativo

- Windows 10/11 con **WSL2** + **Docker Desktop** (backend WSL2).

## 1. Instalación de WSL2

Desde una terminal de Windows (PowerShell o CMD) con privilegios de
administrador:

```powershell
wsl --install
```

Este comando instala WSL2, descarga una distribución Linux por defecto
(Ubuntu) y habilita los componentes de Windows necesarios (Plataforma de
máquina virtual y Subsistema de Windows para Linux). Requiere reiniciar la
PC al finalizar.

## 2. Instalación de Docker Desktop

- Se instaló Docker Desktop para Windows en modalidad **per-user
  installation**, con el backend configurado en **WSL2** (no Hyper-V).
- Durante la instalación se habilitó la integración de Docker con la
  distribución WSL2 correspondiente.
- Se verificó la instalación abriendo Docker Desktop y confirmando que el
  motor Docker está corriendo sobre WSL2 (ícono de Docker en la bandeja del
  sistema, estado "Engine running").

## 3. Levantar SimpleRisk con Docker

Con Docker Desktop corriendo, desde una terminal:

```bash
docker pull simplerisk/simplerisk
docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk
```

- `docker pull simplerisk/simplerisk`: descarga la imagen oficial de
  SimpleRisk desde Docker Hub.
- `docker run --name simplerisk -d -p 80:80 -p 443:443 simplerisk/simplerisk`:
  levanta un contenedor llamado `simplerisk` en modo *detached* (`-d`),
  mapeando los puertos 80 (HTTP) y 443 (HTTPS) del contenedor a los mismos
  puertos del host.

## 4. Acceso a la aplicación

- Se accede desde el navegador a **https://localhost/**.
- El certificado TLS es autofirmado (generado por el propio contenedor), por
  lo que el navegador muestra una advertencia de seguridad. Se aceptó la
  excepción de certificado ("Avanzado" → "Continuar de todos modos"), algo
  esperable y normal en un entorno de pruebas local, no expuesto a Internet.

## 5. Creación de la cuenta de administrador

- En el primer acceso, SimpleRisk presenta el wizard **"Default Admin
  Account Creation"**.
- Se completó dicho wizard para crear la cuenta de administrador inicial
  (usuario `admin`), que luego se usó para configurar el resto de usuarios y
  la carga de riesgos.

## Comandos útiles adicionales

```bash
# Ver el estado del contenedor
docker ps

# Ver logs del contenedor
docker logs simplerisk

# Detener / iniciar el contenedor
docker stop simplerisk
docker start simplerisk
```
