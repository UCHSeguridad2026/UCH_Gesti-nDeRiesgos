\# Informe TP: SimpleRisk â€” Seguridad de Sistemas



\## 1. IntroducciÃ³n



El presente trabajo prÃ¡ctico tiene como objetivo aplicar conceptos de gestiÃ³n de riesgos de seguridad de sistemas mediante la implementaciÃ³n y utilizaciÃ³n de SimpleRisk.



El trabajo se desarrolla sobre el escenario ficticio de una clÃ­nica privada de 120 empleados que atiende aproximadamente 800 pacientes por dÃ­a. La organizaciÃ³n utiliza sistemas informÃ¡ticos para la gestiÃ³n de historias clÃ­nicas digitales, informaciÃ³n mÃ©dica, datos personales, informaciÃ³n de obras sociales, facturaciÃ³n y atenciÃ³n de pacientes.



A partir de este escenario se identificaron, evaluaron y trataron diferentes riesgos relacionados con la confidencialidad, integridad, disponibilidad y seguridad fÃ­sica de los activos tecnolÃ³gicos.



\---



\## 2. Objetivos



Los principales objetivos del trabajo son:



\* Implementar un entorno reproducible de SimpleRisk.

\* Configurar usuarios con diferentes niveles de permisos.

\* Identificar riesgos especÃ­ficos para una clÃ­nica privada.

\* Evaluar los riesgos utilizando el mÃ©todo Probabilidad x Impacto.

\* Definir estrategias de tratamiento.

\* Crear planes de mitigaciÃ³n.

\* Realizar revisiones de gestiÃ³n.

\* Analizar el riesgo residual despuÃ©s de aplicar medidas de mitigaciÃ³n.

\* Comparar la metodologÃ­a utilizada con alternativas de gestiÃ³n de riesgos.

\* Analizar una posible integraciÃ³n de SimpleRisk con herramientas externas.

\* Documentar el proceso de forma reproducible.



\---



\# 3. ImplementaciÃ³n del entorno



\## 3.1 TecnologÃ­a utilizada



Para la implementaciÃ³n se utilizÃ³ Docker y Docker Compose.



La utilizaciÃ³n de contenedores permite disponer de un entorno aislado y reproducible, evitando depender de una instalaciÃ³n manual especÃ­fica del sistema operativo.



La estructura utilizada es:



```text

entorno/

â”œâ”€â”€ docker-compose.yml

â””â”€â”€ setup.sh

```



El archivo `docker-compose.yml` define el servicio de SimpleRisk, sus puertos de acceso, almacenamiento persistente y polÃ­tica de reinicio.



El contenedor utiliza la imagen:



```text

simplerisk/simplerisk:20260828-001

```



Los puertos utilizados son:



\* HTTP: 8080

\* HTTPS: 8443



El acceso a la aplicaciÃ³n se realizÃ³ mediante:



```text

https://localhost:8443

```



\## 3.2 Persistencia



Se configurÃ³ un volumen Docker denominado `simplerisk-data`, montado sobre el directorio de datos de SimpleRisk.



Esto permite mantener la informaciÃ³n de la aplicaciÃ³n aunque el contenedor sea detenido o recreado.



\## 3.3 VerificaciÃ³n del entorno



Se verificÃ³ que el contenedor de SimpleRisk se encuentre en ejecuciÃ³n y en estado saludable mediante Docker Compose.



TambiÃ©n se verificÃ³ el funcionamiento del servicio web desde el navegador.



\---



\# 4. ConfiguraciÃ³n de usuarios



Se configuraron tres usuarios con funciones diferenciadas:



| Usuario          | FunciÃ³n             |

| ---------------- | ------------------- |

| admin            | Administrador       |

| analista.riesgos | Analista de riesgos |

| auditor          | Auditor             |



La cuenta `admin` posee el rol de administrador de SimpleRisk.



El usuario `analista.riesgos` posee permisos relacionados con la gestiÃ³n de riesgos, incluyendo creaciÃ³n, modificaciÃ³n, planificaciÃ³n de mitigaciones, revisiÃ³n y comentarios.



El usuario `auditor` posee permisos principalmente orientados a revisiÃ³n y seguimiento de riesgos.



Las contraseÃ±as no se almacenan en el repositorio.



Esta configuraciÃ³n permite aplicar el principio de \*\*segregaciÃ³n de funciones\*\*, evitando concentrar todas las actividades en una Ãºnica cuenta.



La descripciÃ³n detallada de usuarios y permisos se encuentra en:



```text

configuracion/usuarios.md

```



\---



\# 5. Escenario de anÃ¡lisis



El escenario corresponde a una clÃ­nica privada con:



\* 120 empleados.

\* Aproximadamente 800 pacientes diarios.

\* Historias clÃ­nicas digitales.

\* InformaciÃ³n mÃ©dica.

\* Datos personales.

\* Datos de obras sociales.

\* Sistemas de facturaciÃ³n.

\* Sistemas utilizados para la atenciÃ³n de pacientes.



Debido a la naturaleza de la informaciÃ³n procesada, la protecciÃ³n de los sistemas resulta especialmente importante.



Los principales objetivos de seguridad considerados fueron:



\* Confidencialidad de la informaciÃ³n.

\* Integridad de los datos.

\* Disponibilidad de los sistemas.

\* Continuidad operativa.

\* Seguridad fÃ­sica de la infraestructura.



\---



\# 6. MetodologÃ­a de evaluaciÃ³n



Para la evaluaciÃ³n de riesgos se utilizÃ³ una matriz clÃ¡sica de \*\*Probabilidad x Impacto\*\*.



La probabilidad y el impacto se consideran en una escala de 1 a 5.



El cÃ¡lculo utilizado es:



\*\*Riesgo = Probabilidad x Impacto\*\*



La clasificaciÃ³n utilizada es:



| Puntaje | Nivel   |

| ------: | ------- |

|     1â€“4 | Bajo    |

|     5â€“9 | Medio   |

|   10â€“15 | Alto    |

|   16â€“25 | CrÃ­tico |



AdemÃ¡s del riesgo inherente, se considerÃ³ el riesgo residual luego de la aplicaciÃ³n de medidas de tratamiento.



\---



\# 7. IdentificaciÃ³n de riesgos



Se identificaron siete riesgos principales para la clÃ­nica.



\## 7.1 Riesgo 1001 â€” Acceso no autorizado a historias clÃ­nicas



Existe el riesgo de que personas no autorizadas accedan a historias clÃ­nicas y otra informaciÃ³n sensible de pacientes.



El riesgo afecta principalmente la confidencialidad de la informaciÃ³n y puede generar consecuencias legales y reputacionales.



\*\*Activo:\*\* Sistema de Historias ClÃ­nicas.



\*\*CategorÃ­a:\*\* Sensitive Data Management.



\*\*TecnologÃ­a:\*\* Windows.



\*\*Fuente:\*\* People.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 8 â€” Medio.



Como medidas de tratamiento se consideran el acceso basado en roles, credenciales individuales y revisiÃ³n periÃ³dica de permisos.



\---



\## 7.2 Riesgo 1002 â€” PÃ©rdida de informaciÃ³n por fallas en las copias de seguridad



Existe el riesgo de pÃ©rdida de informaciÃ³n ante fallas en los mecanismos de backup o imposibilidad de recuperar los datos.



\*\*Activo:\*\* Sistema de Historias ClÃ­nicas.



\*\*CategorÃ­a:\*\* Sensitive Data Management.



\*\*TecnologÃ­a:\*\* Backups.



\*\*Fuente:\*\* System.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 6,4 â€” Medio.



Se definiÃ³ un plan de mitigaciÃ³n destinado a formalizar la polÃ­tica de backups, proteger las copias y realizar pruebas periÃ³dicas de restauraciÃ³n.



\*\*MitigaciÃ³n:\*\* 80 %.



\*\*Riesgo residual:\*\* 1,28 â€” Bajo.



\---



\## 7.3 Riesgo 1003 â€” InfecciÃ³n por malware o ransomware



Existe el riesgo de infecciÃ³n por malware o ransomware que pueda comprometer informaciÃ³n, afectar los sistemas y provocar interrupciones en la operaciÃ³n.



\*\*Activo:\*\* Sistema de Historias ClÃ­nicas.



\*\*CategorÃ­a:\*\* Technical Vulnerability Management.



\*\*TecnologÃ­a:\*\* Anti-Virus.



\*\*Fuente:\*\* External.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 4,8 â€” Medio.



Se definiÃ³ un plan de mitigaciÃ³n para fortalecer las herramientas de protecciÃ³n, mantener actualizados los sistemas y aplicaciones, controlar archivos y enlaces maliciosos y restringir software no autorizado.



\*\*MitigaciÃ³n:\*\* 80 %.



\---



\## 7.4 Riesgo 1004 â€” Acceso fÃ­sico no autorizado al equipamiento informÃ¡tico



Existe el riesgo de acceso fÃ­sico no autorizado a equipamiento informÃ¡tico crÃ­tico.



Esto podrÃ­a provocar robo, manipulaciÃ³n, daÃ±o o indisponibilidad de los sistemas.



\*\*Activo:\*\* Equipamiento informÃ¡tico.



\*\*CategorÃ­a:\*\* Physical Security.



\*\*TecnologÃ­a:\*\* Datacenter.



\*\*Fuente:\*\* People.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 3,2 â€” Bajo.



Los equipos crÃ­ticos deben permanecer en Ã¡reas restringidas y con controles de acceso fÃ­sico.



Como requisito especÃ­fico del escenario, los centros de datos no deben ubicarse prÃ³ximos a cocinas ni debajo de piletas, lavamanos u otras instalaciones que puedan producir filtraciones de agua.



\---



\## 7.5 Riesgo 1005 â€” InterrupciÃ³n de la red interna de la clÃ­nica



Existe el riesgo de interrupciÃ³n de la red interna, afectando la comunicaciÃ³n entre los sistemas y el acceso de los usuarios a los servicios tecnolÃ³gicos.



\*\*Activo:\*\* Red interna de la clÃ­nica.



\*\*CategorÃ­a:\*\* Environmental Resilience.



\*\*TecnologÃ­a:\*\* Network.



\*\*Fuente:\*\* System.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 4,8 â€” Medio.



El tratamiento contempla monitoreo de la infraestructura de red, medidas de continuidad y procedimientos de recuperaciÃ³n.



\---



\## 7.6 Riesgo 1006 â€” Robo de credenciales mediante phishing



Existe el riesgo de robo de credenciales mediante campaÃ±as de phishing o ingenierÃ­a social.



La obtenciÃ³n de credenciales podrÃ­a permitir el acceso no autorizado a sistemas e informaciÃ³n sensible.



\*\*Activo:\*\* Sistema de Historias ClÃ­nicas.



\*\*CategorÃ­a:\*\* Access Management.



\*\*TecnologÃ­a:\*\* Mail Routing.



\*\*Fuente:\*\* People.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 6,4 â€” Medio.



Se definiÃ³ un plan de mitigaciÃ³n basado en capacitaciÃ³n periÃ³dica, autenticaciÃ³n adicional cuando sea posible, protecciÃ³n del correo electrÃ³nico y revisiÃ³n de accesos.



\*\*MitigaciÃ³n:\*\* 75 %.



\*\*Riesgo residual:\*\* 1,6 â€” Bajo.



\---



\## 7.7 Riesgo 1007 â€” Indisponibilidad de sistemas por corte elÃ©ctrico



Existe el riesgo de indisponibilidad de los sistemas tecnolÃ³gicos debido a cortes o interrupciones del suministro elÃ©ctrico.



\*\*Activo:\*\* Equipamiento informÃ¡tico.



\*\*CategorÃ­a:\*\* Environmental Resilience.



\*\*TecnologÃ­a:\*\* Power.



\*\*Fuente:\*\* External.



\*\*Propietario:\*\* Analista de Riesgos.



\*\*Riesgo inherente:\*\* 4,8 â€” Medio.



El tratamiento contempla medidas de contingencia y continuidad para reducir el impacto sobre los sistemas crÃ­ticos.



\---



\# 8. Planes de mitigaciÃ³n



Se definieron tres planes de mitigaciÃ³n.



\## 8.1 Plan de mitigaciÃ³n del riesgo 1002



\*\*Riesgo:\*\* PÃ©rdida de informaciÃ³n por fallas en las copias de seguridad.



\*\*Estrategia:\*\* Mitigate.



\*\*Esfuerzo:\*\* Considerable.



\*\*Costo:\*\* $100.001 a $200.000.



\*\*Fecha prevista:\*\* 01/10/2026.



\*\*Responsable:\*\* Analista de Riesgos.



\*\*Equipo:\*\* Information Security.



\*\*MitigaciÃ³n:\*\* 80 %.



El plan contempla formalizar la polÃ­tica de backups, utilizar ubicaciones independientes, monitorear las copias y realizar pruebas de restauraciÃ³n.



\---



\## 8.2 Plan de mitigaciÃ³n del riesgo 1003



\*\*Riesgo:\*\* InfecciÃ³n por malware o ransomware.



\*\*Estrategia:\*\* Mitigate.



\*\*Esfuerzo:\*\* Significant.



\*\*Costo:\*\* $200.001 a $300.000.



\*\*Fecha prevista:\*\* 15/10/2026.



\*\*Responsable:\*\* Analista de Riesgos.



\*\*Equipo:\*\* Information Security.



\*\*MitigaciÃ³n:\*\* 80 %.



El plan contempla actualizar las herramientas de protecciÃ³n, fortalecer la detecciÃ³n de software malicioso, filtrar archivos y enlaces peligrosos, restringir software no autorizado y capacitar a los usuarios.



\---



\## 8.3 Plan de mitigaciÃ³n del riesgo 1006



\*\*Riesgo:\*\* Robo de credenciales mediante phishing.



\*\*Estrategia:\*\* Mitigate.



\*\*Esfuerzo:\*\* Considerable.



\*\*Costo:\*\* $0 a $100.000.



\*\*Fecha prevista:\*\* 30/10/2026.



\*\*Responsable:\*\* Analista de Riesgos.



\*\*Equipo:\*\* Information Security.



\*\*MitigaciÃ³n:\*\* 75 %.



El plan contempla capacitaciÃ³n periÃ³dica contra phishing, autenticaciÃ³n multifactor cuando sea posible, filtros antiphishing y revisiÃ³n periÃ³dica de permisos.



\---



\# 9. Revisiones de gestiÃ³n



Los riesgos 1002, 1003 y 1006 fueron sometidos a revisiÃ³n de gestiÃ³n dentro de SimpleRisk.



La revisiÃ³n fue realizada el \*\*09/10/2026\*\* por \*\*Bruno Lopez\*\*.



La acciÃ³n seleccionada fue:



\*\*Approve Risk\*\*



y el siguiente paso:



\*\*Accept Until Next Review\*\*.



SimpleRisk estableciÃ³ como prÃ³xima fecha de revisiÃ³n:



\*\*03/09/2027\*\*.



Para los riesgos 1002 y 1006 se verificaron los siguientes resultados:



| Riesgo | Inherente |    Residual |

| ------ | --------: | ----------: |

| 1002   |       6,4 | 1,28 â€” Bajo |

| 1006   |       6,4 |  1,6 â€” Bajo |



El riesgo 1003 cuenta con un plan de mitigaciÃ³n del 80 %. Su valor residual serÃ¡ documentado a partir de la informaciÃ³n obtenida directamente desde la pantalla de detalle de SimpleRisk.



\---



\# 10. Trazabilidad de activos, amenazas y riesgos



Para facilitar la trazabilidad del anÃ¡lisis se definiÃ³ una identificaciÃ³n Ãºnica para activos, amenazas y riesgos.



Los activos se identifican mediante cÃ³digos como:



```text

A01

A02

A03

```



Las amenazas mediante:



```text

T01

T02

T03

```



Y los riesgos mediante:



```text

R01

R02

R03

```



En SimpleRisk los riesgos fueron registrados con sus identificadores correspondientes, permitiendo realizar seguimiento individual de cada situaciÃ³n.



\---



\# 11. Principios de seguridad considerados



El anÃ¡lisis contempla los principales principios de seguridad de la informaciÃ³n.



\## Confidencialidad



Se busca evitar el acceso no autorizado a historias clÃ­nicas, credenciales y otros datos sensibles.



\## Integridad



Se busca prevenir modificaciones, pÃ©rdidas o alteraciones no autorizadas de la informaciÃ³n.



\## Disponibilidad



Se consideran riesgos relacionados con red, energÃ­a, malware y recuperaciÃ³n de informaciÃ³n.



\## Seguridad fÃ­sica



Se considera la protecciÃ³n fÃ­sica del equipamiento y la ubicaciÃ³n adecuada de la infraestructura crÃ­tica.



\## Continuidad operativa



Los planes de backup, recuperaciÃ³n y contingencia buscan mantener la capacidad operativa ante incidentes.



\---



\# 12. Parte C â€” ComparaciÃ³n metodolÃ³gica



La metodologÃ­a Probabilidad x Impacto presenta como principal ventaja su simplicidad.



Permite clasificar rÃ¡pidamente los riesgos utilizando una escala comprensible y facilita la comunicaciÃ³n de los resultados a personas tÃ©cnicas y no tÃ©cnicas.



Sin embargo, presenta un componente subjetivo importante, debido a que la asignaciÃ³n de valores de probabilidad e impacto depende del criterio utilizado por los evaluadores.



Como alternativa se considera \*\*NIST SP 800-30\*\*, una metodologÃ­a orientada a la evaluaciÃ³n de riesgos de seguridad de la informaciÃ³n.



NIST SP 800-30 propone analizar las fuentes de amenaza, eventos de amenaza, vulnerabilidades, probabilidad, impacto y riesgo resultante.



\### ComparaciÃ³n



| Criterio                    | Probabilidad x Impacto | NIST SP 800-30  |

| --------------------------- | ---------------------- | --------------- |

| Complejidad                 | Baja                   | Media           |

| Facilidad de implementaciÃ³n | Alta                   | Media           |

| Subjetividad                | Alta                   | Media           |

| Datos cuantitativos         | No obligatorios        | No obligatorios |

| Trazabilidad                | Media                  | Alta            |

| Reproducibilidad            | Media                  | Alta            |

| AplicaciÃ³n en una clÃ­nica   | Alta                   | Alta            |



Para este trabajo, Probabilidad x Impacto resulta apropiada debido a la necesidad de implementar una metodologÃ­a sencilla y comprensible dentro de SimpleRisk.



NIST SP 800-30 puede utilizarse como complemento para profundizar la identificaciÃ³n de amenazas, vulnerabilidades y escenarios.



\---



\# 13. IntegraciÃ³n con una herramienta externa



Una posible mejora consiste en integrar SimpleRisk con un sistema externo de gestiÃ³n de tickets.



Por ejemplo, ante la creaciÃ³n de un riesgo de nivel alto o crÃ­tico, SimpleRisk podrÃ­a generar automÃ¡ticamente un ticket en una plataforma como Jira.



El flujo podrÃ­a ser:



```text

SimpleRisk

&#x20;    |

&#x20;    v

Nuevo riesgo

&#x20;    |

&#x20;    v

EvaluaciÃ³n del nivel

&#x20;    |

&#x20;    v

Riesgo Alto/CrÃ­tico

&#x20;    |

&#x20;    v

Sistema de tickets

&#x20;    |

&#x20;    v

AsignaciÃ³n de responsable

&#x20;    |

&#x20;    v

Seguimiento de mitigaciÃ³n

&#x20;    |

&#x20;    v

Cierre del ticket

```



Esta integraciÃ³n permitirÃ­a mejorar la trazabilidad de los planes de acciÃ³n y centralizar el seguimiento de las tareas.



Otra alternativa serÃ­a integrar eventos de seguridad con un SIEM para correlacionar incidentes tÃ©cnicos con los riesgos registrados.



En el contexto de la clÃ­nica, esta integraciÃ³n permitirÃ­a relacionar los riesgos de seguridad con las actividades concretas necesarias para reducirlos.



\---



\# 14. Consideraciones de seguridad



Durante la realizaciÃ³n del trabajo se evitÃ³ almacenar informaciÃ³n sensible en el repositorio.



No se deben incluir:



\* ContraseÃ±as.

\* Tokens.

\* API keys.

\* Credenciales reales.

\* Dumps de bases de datos.

\* Backups sensibles.

\* InformaciÃ³n real de pacientes.



Las capturas utilizadas como evidencia deben revisarse antes de incorporarse al repositorio para evitar exponer informaciÃ³n innecesaria.



TambiÃ©n se utiliza `.gitignore` para reducir el riesgo de incorporar accidentalmente archivos sensibles.



\---



\# 15. Conclusiones



La implementaciÃ³n de SimpleRisk permitiÃ³ aplicar un proceso bÃ¡sico de identificaciÃ³n, evaluaciÃ³n y tratamiento de riesgos de seguridad sobre un escenario organizacional.



Se configuraron tres perfiles diferenciados, se registraron siete riesgos especÃ­ficos y se definieron tres planes de mitigaciÃ³n.



La utilizaciÃ³n de la matriz Probabilidad x Impacto permitiÃ³ establecer una clasificaciÃ³n inicial de los riesgos y posteriormente analizar la reducciÃ³n del riesgo mediante las medidas de tratamiento.



Los resultados verificados muestran una reducciÃ³n del riesgo residual en los riesgos 1002 y 1006.



El trabajo tambiÃ©n permitiÃ³ analizar las limitaciones de una metodologÃ­a cualitativa y compararla con un enfoque mÃ¡s estructurado como NIST SP 800-30.



Finalmente, la posibilidad de integrar SimpleRisk con sistemas de tickets o herramientas de monitoreo permitirÃ­a mejorar la trazabilidad, seguimiento y gestiÃ³n de las acciones de tratamiento.



\---



\# 16. Evidencias



Las capturas de pantalla utilizadas como evidencia serÃ¡n almacenadas en:



```text

informe/capturas/

```



Las evidencias deberÃ¡n demostrar, como mÃ­nimo:



\* Funcionamiento de SimpleRisk.

\* Usuarios configurados.

\* Riesgos registrados.

\* Planes de mitigaciÃ³n.

\* Revisiones de gestiÃ³n.

\* Riesgo residual.

\* Elementos relevantes de la configuraciÃ³n.



Las capturas deberÃ¡n evitar mostrar contraseÃ±as, tokens u otra informaciÃ³n sensible.



\---



\# 17. Referencias al escenario



Como parte de las condiciones particulares del trabajo prÃ¡ctico se incorporan las referencias solicitadas al escenario:



\* Lobo feroz.

\* Caperucita Roja.

\* Los tres cerditos.



Estas referencias se consideran elementos narrativos del escenario y no representan amenazas reales adicionales.



En relaciÃ³n con la infraestructura fÃ­sica, se establece que los centros de datos deben mantenerse alejados de cocinas y no deben ubicarse debajo de piletas, lavamanos u otras instalaciones que puedan provocar filtraciones de agua.
