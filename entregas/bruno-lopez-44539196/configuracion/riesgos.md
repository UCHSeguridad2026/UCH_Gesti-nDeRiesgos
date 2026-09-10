# Riesgos de la ClÃƒÂ­nica



## 1. Objetivo



Este documento registra los riesgos identificados y gestionados en la instancia de SimpleRisk correspondiente al escenario de una clÃƒÂ­nica privada.



Se definieron siete riesgos relacionados con la confidencialidad, integridad, disponibilidad y seguridad fÃƒÂ­sica de los activos tecnolÃƒÂ³gicos.



La valoraciÃƒÂ³n utiliza el mÃƒÂ©todo **Probabilidad x Impacto**, con una escala de 1 a 5.



### ClasificaciÃƒÂ³n del riesgo



| Puntaje | Nivel   |

| ------: | ------- |

|     1Ã¢â‚¬â€œ4 | Bajo    |

|     5Ã¢â‚¬â€œ9 | Medio   |

|   10Ã¢â‚¬â€œ15 | Alto    |

|   16Ã¢â‚¬â€œ25 | CrÃƒÂ­tico |



## 2. Matriz de riesgos



| ID   | Riesgo                                                       | Probabilidad | Impacto              | Riesgo inherente | Tratamiento |        Riesgo residual |

| ---- | ------------------------------------------------------------ | ------------ | -------------------- | ---------------: | ----------- | ---------------------: |

| 1001 | Acceso no autorizado a historias clÃƒÂ­nicas                    | Likely       | Extreme/Catastrophic |                8 | Mitigar     |              Pendiente |

| 1002 | PÃƒÂ©rdida de informaciÃƒÂ³n por fallas en las copias de seguridad | Likely       | Major                |              6,4 | Mitigar     |            1,28 Ã¢â‚¬â€ Bajo |

| 1003 | InfecciÃƒÂ³n por malware o ransomware                           | Credible     | Major                |              4,8 | Mitigar     | Pendiente de verificar |

| 1004 | Acceso fÃƒÂ­sico no autorizado al equipamiento informÃƒÂ¡tico      | Unlikely     | Major                |              3,2 | Mitigar     |              Pendiente |

| 1005 | InterrupciÃƒÂ³n de la red interna de la clÃƒÂ­nica                 | Credible     | Major                |              4,8 | Mitigar     |              Pendiente |

| 1006 | Robo de credenciales mediante phishing                       | Likely       | Major                |              6,4 | Mitigar     |             1,6 Ã¢â‚¬â€ Bajo |

| 1007 | Indisponibilidad de sistemas por corte elÃƒÂ©ctrico             | Credible     | Major                |              4,8 | Mitigar     |              Pendiente |



> Los valores de riesgo residual se registran ÃƒÂºnicamente cuando fueron obtenidos de la evaluaciÃƒÂ³n posterior a la mitigaciÃƒÂ³n en SimpleRisk. No se estiman valores que no hayan sido verificados en la herramienta.



## 3. Detalle de los riesgos



### 1001 Ã¢â‚¬â€ Acceso no autorizado a historias clÃƒÂ­nicas



**CategorÃƒÂ­a:** Sensitive Data Management

**Activo afectado:** Sistema de Historias ClÃƒÂ­nicas

**TecnologÃƒÂ­a:** Windows

**Equipo:** Information Security

**Fuente:** People

**Propietario:** Analista de Riesgos



Existe el riesgo de que personas no autorizadas accedan a historias clÃƒÂ­nicas y otra informaciÃƒÂ³n sensible de pacientes. Esto podrÃƒÂ­a afectar la confidencialidad de los datos, generar incumplimientos y producir un impacto reputacional para la clÃƒÂ­nica.



Como medidas de tratamiento se consideran el acceso basado en roles, el uso de credenciales individuales y la revisiÃƒÂ³n periÃƒÂ³dica de permisos.



### 1002 Ã¢â‚¬â€ PÃƒÂ©rdida de informaciÃƒÂ³n por fallas en las copias de seguridad



**CategorÃƒÂ­a:** Sensitive Data Management

**Activo afectado:** Sistema de Historias ClÃƒÂ­nicas

**TecnologÃƒÂ­a:** Backups

**Equipo:** Information Security

**Fuente:** System

**Propietario:** Analista de Riesgos



Existe el riesgo de pÃƒÂ©rdida de informaciÃƒÂ³n ante fallas en los mecanismos de copia de seguridad o imposibilidad de recuperar los datos.



Se definiÃƒÂ³ un plan de mitigaciÃƒÂ³n para formalizar la polÃƒÂ­tica y frecuencia de backups, mantener copias protegidas y realizar pruebas periÃƒÂ³dicas de restauraciÃƒÂ³n.



**Riesgo inherente:** 6,4 Ã¢â‚¬â€ Medio

**Riesgo residual:** 1,28 Ã¢â‚¬â€ Bajo

**MitigaciÃƒÂ³n:** 80 %



### 1003 Ã¢â‚¬â€ InfecciÃƒÂ³n por malware o ransomware



**CategorÃƒÂ­a:** Technical Vulnerability Management

**Activo afectado:** Sistema de Historias ClÃƒÂ­nicas

**TecnologÃƒÂ­a:** Anti-Virus

**Equipo:** Information Security

**Fuente:** External

**Propietario:** Analista de Riesgos



Existe el riesgo de infecciÃƒÂ³n por malware o ransomware que pueda comprometer la informaciÃƒÂ³n, afectar los sistemas y provocar interrupciones en las operaciones de la clÃƒÂ­nica.



Se definiÃƒÂ³ un plan de mitigaciÃƒÂ³n para fortalecer las herramientas de protecciÃƒÂ³n, mantener actualizados los sistemas y aplicaciones, controlar archivos y enlaces maliciosos y limitar la instalaciÃƒÂ³n de software no autorizado.



**MitigaciÃƒÂ³n:** 80 %



### 1004 Ã¢â‚¬â€ Acceso fÃƒÂ­sico no autorizado al equipamiento informÃƒÂ¡tico



**CategorÃƒÂ­a:** Physical Security

**Activo afectado:** Equipamiento informÃƒÂ¡tico

**TecnologÃƒÂ­a:** Datacenter

**Equipo:** Information Security

**Fuente:** People

**Propietario:** Analista de Riesgos



Existe el riesgo de acceso fÃƒÂ­sico no autorizado a equipamiento informÃƒÂ¡tico crÃƒÂ­tico, pudiendo producir robo, manipulaciÃƒÂ³n, daÃƒÂ±o o indisponibilidad de los sistemas.



Los equipos crÃƒÂ­ticos deben permanecer en ÃƒÂ¡reas restringidas y con controles de acceso fÃƒÂ­sico.



Como requisito especÃƒÂ­fico del escenario, los centros de datos **no deben ubicarse prÃƒÂ³ximos a cocinas ni debajo de piletas, lavamanos u otras instalaciones que puedan generar filtraciones de agua**.



### 1005 Ã¢â‚¬â€ InterrupciÃƒÂ³n de la red interna de la clÃƒÂ­nica



**CategorÃƒÂ­a:** Environmental Resilience

**Activo afectado:** Red interna de la clÃƒÂ­nica

**TecnologÃƒÂ­a:** Network

**Equipo:** Network

**Fuente:** System

**Propietario:** Analista de Riesgos



Existe el riesgo de interrupciÃƒÂ³n de la red interna, afectando la comunicaciÃƒÂ³n entre los sistemas y el acceso de los usuarios a los servicios tecnolÃƒÂ³gicos necesarios para la operaciÃƒÂ³n de la clÃƒÂ­nica.



El tratamiento contempla medidas de continuidad, monitoreo de la infraestructura de red y procedimientos para la recuperaciÃƒÂ³n del servicio.



### 1006 Ã¢â‚¬â€ Robo de credenciales mediante phishing



**CategorÃƒÂ­a:** Access Management

**Activo afectado:** Sistema de Historias ClÃƒÂ­nicas

**TecnologÃƒÂ­a:** Mail Routing

**Equipo:** Information Security

**Fuente:** People

**Propietario:** Analista de Riesgos



Existe el riesgo de robo de credenciales mediante campaÃƒÂ±as de phishing o ingenierÃƒÂ­a social. La obtenciÃƒÂ³n de credenciales podrÃƒÂ­a permitir el acceso no autorizado a sistemas e informaciÃƒÂ³n sensible.



Se definiÃƒÂ³ un plan de mitigaciÃƒÂ³n basado en capacitaciÃƒÂ³n periÃƒÂ³dica, autenticaciÃƒÂ³n adicional cuando sea posible, protecciÃƒÂ³n del correo electrÃƒÂ³nico y revisiÃƒÂ³n periÃƒÂ³dica de accesos.



**Riesgo inherente:** 6,4 Ã¢â‚¬â€ Medio

**Riesgo residual:** 1,6 Ã¢â‚¬â€ Bajo

**MitigaciÃƒÂ³n:** 75 %



### 1007 Ã¢â‚¬â€ Indisponibilidad de sistemas por corte elÃƒÂ©ctrico



**CategorÃƒÂ­a:** Environmental Resilience

**Activo afectado:** Equipamiento informÃƒÂ¡tico

**TecnologÃƒÂ­a:** Power

**Equipo:** IT Systems Management

**Fuente:** External

**Propietario:** Analista de Riesgos



Existe el riesgo de indisponibilidad de los sistemas tecnolÃƒÂ³gicos debido a cortes o interrupciones del suministro elÃƒÂ©ctrico.



El tratamiento contempla medidas de contingencia y continuidad para reducir el impacto sobre los sistemas crÃƒÂ­ticos de la clÃƒÂ­nica.



## 4. Planes de mitigaciÃƒÂ³n



Se definieron tres planes de mitigaciÃƒÂ³n en SimpleRisk.



### Plan asociado al riesgo 1002



**Riesgo:** PÃƒÂ©rdida de informaciÃƒÂ³n por fallas en las copias de seguridad

**Estrategia:** Mitigate

**Esfuerzo:** Considerable

**Costo:** $100.001 a $200.000

**Fecha prevista:** 01/10/2026

**Responsable:** Analista de Riesgos

**Equipo:** Information Security

**Porcentaje de mitigaciÃƒÂ³n:** 80 %



El plan contempla formalizar la polÃƒÂ­tica de backups, utilizar ubicaciones independientes, monitorear las copias y realizar pruebas de restauraciÃƒÂ³n.



### Plan asociado al riesgo 1003



**Riesgo:** InfecciÃƒÂ³n por malware o ransomware

**Estrategia:** Mitigate

**Esfuerzo:** Significant

**Costo:** $200.001 a $300.000

**Fecha prevista:** 15/10/2026

**Responsable:** Analista de Riesgos

**Equipo:** Information Security

**Porcentaje de mitigaciÃƒÂ³n:** 80 %



El plan contempla mantener actualizadas las herramientas de protecciÃƒÂ³n, fortalecer la detecciÃƒÂ³n de software malicioso, filtrar archivos y enlaces peligrosos, restringir software no autorizado y capacitar a los usuarios.



### Plan asociado al riesgo 1006



**Riesgo:** Robo de credenciales mediante phishing

**Estrategia:** Mitigate

**Esfuerzo:** Considerable

**Costo:** $0 a $100.000

**Fecha prevista:** 30/10/2026

**Responsable:** Analista de Riesgos

**Equipo:** Information Security

**Porcentaje de mitigaciÃƒÂ³n:** 75 %



El plan contempla capacitaciÃƒÂ³n periÃƒÂ³dica contra phishing, autenticaciÃƒÂ³n multifactor cuando sea posible, filtros antiphishing y revisiÃƒÂ³n periÃƒÂ³dica de los permisos de acceso.



## 5. Revisiones de gestiÃƒÂ³n



Los riesgos 1002, 1003 y 1006 fueron sometidos a revisiÃƒÂ³n de gestiÃƒÂ³n en SimpleRisk.



La revisiÃƒÂ³n registrada corresponde al **09/10/2026**, realizada por **Bruno Lopez**, con la opciÃƒÂ³n **Approve Risk** y el siguiente paso **Accept Until Next Review**.



La prÃƒÂ³xima revisiÃƒÂ³n indicada por SimpleRisk es el **03/09/2027**.



Para los riesgos 1002 y 1006 se verificaron los siguientes valores posteriores a la mitigaciÃƒÂ³n:



* **1002:** 6,4 Ã¢â€ â€™ 1,28.

* **1006:** 6,4 Ã¢â€ â€™ 1,6.



El riesgo 1003 posee un plan de mitigaciÃƒÂ³n del 80 %, pero su valor residual debe tomarse directamente de la pantalla de detalle de SimpleRisk para evitar registrar un valor no verificado.



## 6. Criterios de seguridad aplicados



Los riesgos fueron definidos considerando los principios de:



* **Confidencialidad:** protecciÃƒÂ³n de historias clÃƒÂ­nicas y credenciales.

* **Integridad:** prevenciÃƒÂ³n de modificaciones o pÃƒÂ©rdidas no autorizadas.

* **Disponibilidad:** continuidad de sistemas, red, energÃƒÂ­a y recuperaciÃƒÂ³n de informaciÃƒÂ³n.

* **Seguridad fÃƒÂ­sica:** protecciÃƒÂ³n del equipamiento y ubicaciÃƒÂ³n adecuada de infraestructura crÃƒÂ­tica.

* **Continuidad operativa:** backups, recuperaciÃƒÂ³n y medidas de contingencia.

* **SegregaciÃƒÂ³n de funciones:** diferenciaciÃƒÂ³n entre administraciÃƒÂ³n, anÃƒÂ¡lisis y auditorÃƒÂ­a.
