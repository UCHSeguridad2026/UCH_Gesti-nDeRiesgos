# D4 — Propuesta de mejora para SimpleRisk

## Issue propuesto — Autenticación multifactor para cuentas privilegiadas

**Tipo:** Feature / Security Enhancement
**Prioridad:** Alta
**Área:** Seguridad / Autenticación
**Título:** `feat(security): incorporar MFA obligatorio para cuentas administrativas`

---

## 1. Resumen

Incorporar autenticación multifactor (MFA) como mecanismo adicional de protección para las cuentas privilegiadas de SimpleRisk.

La funcionalidad permitiría que los usuarios con permisos administrativos deban proporcionar, además de su contraseña, un segundo factor de autenticación basado en una aplicación TOTP compatible con estándares habituales de autenticación multifactor.

El objetivo principal es reducir el riesgo de acceso no autorizado cuando las credenciales de un usuario administrativo sean obtenidas mediante phishing, reutilización de contraseñas o filtraciones.

---

## 2. Problema

Actualmente, la seguridad de una cuenta de SimpleRisk depende en gran medida de la protección de sus credenciales.

Si un atacante obtiene las credenciales de un usuario con privilegios elevados, podría acceder a información relacionada con la gestión de riesgos y realizar modificaciones sin necesidad de comprometer físicamente el servidor.

Este problema resulta especialmente relevante para instalaciones donde existen usuarios con capacidad para:

* administrar usuarios;
* modificar riesgos;
* gestionar configuraciones;
* consultar información sensible;
* administrar planes de tratamiento.

En el escenario de la clínica analizado durante este trabajo, el compromiso de una cuenta privilegiada podría permitir modificar información relacionada con los riesgos de seguridad y afectar la trazabilidad de las decisiones tomadas por la organización.

---

## 3. Propuesta

Agregar soporte nativo para **TOTP (Time-based One-Time Password)**.

El flujo propuesto sería:

1. El administrador habilita MFA desde su perfil.
2. SimpleRisk genera una clave secreta única.
3. La aplicación muestra un código QR para registrar la cuenta en una aplicación autenticadora.
4. El usuario introduce un código TOTP para confirmar la configuración.
5. A partir de ese momento, el inicio de sesión requiere:

   * usuario;
   * contraseña;
   * código MFA.
6. El sistema ofrece códigos de recuperación de un solo uso.
7. El administrador puede revocar el segundo factor desde un procedimiento controlado.

---

## 4. Alcance inicial

La primera versión debería concentrarse en las cuentas privilegiadas.

### Fase 1

MFA obligatorio para:

* administradores;
* cuentas con permisos equivalentes a administración.

### Fase 2

MFA opcional para:

* analistas;
* auditores;
* usuarios estándar.

### Fase 3

MFA obligatorio para todos los usuarios, configurable por política de seguridad.

Esto permitiría introducir la funcionalidad progresivamente sin interrumpir inmediatamente instalaciones existentes.

---

## 5. Requisitos funcionales

### RF-01 — Activación

El administrador debe poder habilitar MFA para una cuenta.

### RF-02 — Registro del segundo factor

La aplicación debe generar una clave secreta y permitir configurar el segundo factor mediante código QR.

### RF-03 — Validación

Antes de activar MFA, el usuario debe demostrar que posee el segundo factor introduciendo un código válido.

### RF-04 — Login

Cuando MFA esté activo, el inicio de sesión deberá solicitar el código TOTP además de las credenciales tradicionales.

### RF-05 — Códigos de recuperación

El sistema deberá generar códigos de recuperación de un solo uso para permitir recuperar el acceso si el usuario pierde su dispositivo autenticador.

Los códigos deberán mostrarse una única vez y almacenarse de forma segura.

### RF-06 — Revocación

Debe existir un mecanismo para revocar el segundo factor cuando sea necesario.

### RF-07 — Auditoría

Las siguientes acciones deberían registrarse en el log de auditoría:

* activación de MFA;
* desactivación de MFA;
* intento exitoso de autenticación;
* intento fallido de autenticación MFA;
* utilización de un código de recuperación.

---

## 6. Requisitos de seguridad

La implementación debería respetar las siguientes condiciones:

* Las claves TOTP no deben almacenarse en texto plano.
* Las claves y códigos de recuperación deben almacenarse de forma protegida.
* Los códigos TOTP deben tener una ventana temporal limitada.
* Los códigos utilizados no deben poder reutilizarse.
* Debe existir protección contra intentos repetidos de autenticación.
* Los códigos de recuperación deben invalidarse después de su utilización.
* La recuperación de una cuenta no debe permitir simplemente desactivar MFA mediante una contraseña.
* Las operaciones administrativas relacionadas con MFA deben quedar registradas.
* Nunca deben almacenarse códigos TOTP en logs.
* Nunca deben incluirse secretos MFA en mensajes de error.

---

## 7. Consideraciones de UX

La incorporación de MFA debe evitar generar una experiencia innecesariamente compleja.

El proceso de configuración debería mostrar un asistente similar a:

**Paso 1 — Activar MFA**

> Proteja su cuenta utilizando autenticación multifactor.

**Paso 2 — Registrar dispositivo**

> Escanee el código QR con su aplicación autenticadora.

**Paso 3 — Verificar**

> Introduzca el código de seis dígitos generado por su aplicación.

**Paso 4 — Guardar recuperación**

> Guarde los códigos de recuperación en un lugar seguro.

Una vez completado el proceso, la interfaz debería indicar claramente:

**MFA habilitado correctamente.**

---

## 8. Criterios de aceptación

La funcionalidad se considerará implementada cuando:

* [ ] Un administrador pueda activar MFA.
* [ ] Se pueda registrar un dispositivo mediante TOTP.
* [ ] El sistema rechace un código MFA incorrecto.
* [ ] Un código válido permita completar el inicio de sesión.
* [ ] Un código TOTP utilizado no pueda reutilizarse.
* [ ] Existan códigos de recuperación de un solo uso.
* [ ] Sea posible revocar el segundo factor mediante un procedimiento autorizado.
* [ ] Las operaciones relacionadas con MFA queden registradas en auditoría.
* [ ] Los secretos no aparezcan en logs.
* [ ] Existan pruebas automatizadas para los casos de éxito y error.
* [ ] La documentación de administración y usuario sea actualizada.

---

## 9. Casos de prueba

| Caso                                                                 | Resultado esperado                      |
| -------------------------------------------------------------------- | --------------------------------------- |
| Usuario con MFA deshabilitado inicia sesión                          | Acceso normal                           |
| Usuario con MFA habilitado ingresa contraseña correcta y TOTP válido | Acceso permitido                        |
| Usuario ingresa contraseña correcta y TOTP incorrecto                | Acceso rechazado                        |
| Usuario reutiliza un código ya utilizado                             | Acceso rechazado                        |
| Usuario utiliza código de recuperación válido                        | Acceso permitido y código invalidado    |
| Usuario utiliza código de recuperación nuevamente                    | Acceso rechazado                        |
| Se realizan múltiples intentos incorrectos                           | Se aplica protección contra abuso       |
| Administrador deshabilita MFA                                        | La acción queda registrada en auditoría |
| Se consulta el log                                                   | No aparecen secretos ni códigos TOTP    |

---

## 10. Impacto esperado

La incorporación de MFA reduciría significativamente el impacto de un escenario en el que las credenciales de un usuario privilegiado sean comprometidas.

En particular, ayudaría a mitigar riesgos identificados durante el análisis de la clínica:

* **R2 — Acceso no autorizado a historias clínicas.**
* **R4 — Phishing y robo de credenciales.**
* **R1 — Ransomware**, al dificultar el uso de credenciales comprometidas como mecanismo de acceso inicial o movimiento posterior.

MFA no elimina estos riesgos por completo, por lo que debería complementarse con mínimo privilegio, monitoreo, capacitación contra phishing, gestión de vulnerabilidades y controles de endpoint.

---

## 11. Compatibilidad y migración

La funcionalidad debería ser compatible con instalaciones existentes.

Se propone:

1. Mantener MFA deshabilitado inicialmente después de actualizar.
2. Permitir que los administradores configuren su segundo factor.
3. Proporcionar un período de transición.
4. Permitir establecer una política que obligue MFA para cuentas privilegiadas.
5. Documentar un procedimiento seguro de recuperación.

La actualización no debería modificar ni eliminar las contraseñas existentes.

---

## 12. Implementación técnica propuesta

La implementación podría dividirse en los siguientes componentes:

### Backend

* Generación de secretos TOTP.
* Validación de códigos.
* Gestión del estado MFA por usuario.
* Generación y validación de códigos de recuperación.
* Registro de eventos de auditoría.

### Base de datos

Agregar información asociada al estado MFA de cada usuario, evitando almacenar secretos de forma directa cuando sea posible.

### Interfaz

Incorporar:

* configuración de MFA en el perfil;
* asistente de registro;
* pantalla de validación;
* administración de dispositivos;
* códigos de recuperación.

### Autenticación

Modificar el flujo de login para introducir un segundo paso cuando el usuario tenga MFA habilitado.

---

## 13. Riesgos de implementación

La propia incorporación de MFA introduce algunos riesgos que deberían considerarse:

* pérdida del dispositivo autenticador;
* bloqueo accidental de cuentas administrativas;
* errores durante una migración;
* problemas de sincronización horaria;
* recuperación insegura de cuentas.

Por este motivo, el mecanismo de recuperación debe diseñarse con el mismo nivel de seguridad que el mecanismo principal de autenticación.

---

## 14. Prioridad propuesta

**Alta.**

La autenticación multifactor debería priorizarse especialmente para cuentas administrativas debido a las consecuencias que puede tener el compromiso de una cuenta privilegiada.

Para el escenario de la clínica utilizado en este trabajo, la medida se considera una de las acciones prioritarias dentro del tratamiento de los riesgos de acceso no autorizado y phishing.

---

## 15. Resultado esperado

Una vez implementada la funcionalidad, una cuenta administrativa comprometida por robo de contraseña no debería poder utilizarse directamente para iniciar sesión sin disponer también del segundo factor.

De esta forma, SimpleRisk incorporaría una capa adicional de defensa frente al compromiso de credenciales y mejoraría su adecuación para organizaciones que necesitan proteger información de gestión de riesgos sensible.

---

## 16. Relación con el Trabajo Práctico

La propuesta se encuentra directamente relacionada con los riesgos identificados en la Parte B.

En particular:

| Riesgo                    | Relación con la mejora                                                             |
| ------------------------- | ---------------------------------------------------------------------------------- |
| R1 — Ransomware           | Reduce la posibilidad de utilizar credenciales comprometidas como vector de acceso |
| R2 — Acceso no autorizado | Agrega un factor adicional para autenticar usuarios                                |
| R4 — Phishing             | Reduce el impacto del robo de contraseñas                                          |
| R5 — Fuga de información  | Dificulta el acceso mediante cuentas comprometidas                                 |

La propuesta transforma una necesidad detectada durante el análisis de riesgos en una mejora concreta del producto, siguiendo un formato de requerimiento que podría utilizarse como base para una futura implementación y revisión técnica.
