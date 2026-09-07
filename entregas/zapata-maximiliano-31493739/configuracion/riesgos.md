# Riesgos Identificados — Fiambrería Punta Pueyrredón

| ID | Riesgo | Categoría | Activos Afectados | Probabilidad | Impacto | Valor | Nivel | Controles Existentes | Tratamiento | Propietario |
|----|--------|-----------|--------------------|--------------:|--------:|------:|-------|----------------------|-------------|--------------|
| R01 | Robo de credenciales del sistema de gestión (EPyme) | Confidencialidad | Sistema de gestión, BD clientes/proveedores | 4 | 3 | 12 | Alto | Ninguno / usuario y contraseña básica | Mitigar (contraseñas fuertes + 2FA, capacitación) | Dueño/responsable |
| R02 | Pérdida de datos por falta de backup del sistema EPyme | Disponibilidad | BD ventas, stock, clientes | 3 | 4 | 12 | Alto | Ninguno | Mitigar (backup automático diario, copia en la nube) | Dueño/responsable técnico |
| R03 | Acceso físico no autorizado a la caja/POS fuera de horario | Disponibilidad/Integridad | Caja, efectivo, sistema POS | 2 | 3 | 6 | Medio | Cámaras de seguridad instaladas | Mitigar (alarma + cerradura reforzada) | Dueño |
| R04 | Grabaciones de cámaras accesibles sin protección | Confidencialidad | Sistema de videovigilancia | 3 | 2 | 6 | Medio | Cámaras instaladas (config. sin detallar) | Mitigar (cambiar contraseñas por defecto, restringir acceso remoto) | Encargado sistemas/dueño |
| R05 | Error humano al cargar precios o stock | Integridad/Operativo | Sistema de gestión, stock | 4 | 2 | 8 | Medio | Ninguno formal | Mitigar (doble verificación, capacitación) | Encargado de stock |
| R06 | Fuga de datos de empleados (legajos, sueldos) | Legal/Confidencialidad | Datos de RRHH | 3 | 4 | 12 | Alto | Ninguno formal | Mitigar (acceso restringido, archivos con contraseña) | Dueño/responsable administrativo |
| R07 | Interrupción del sistema de gestión por falla del proveedor | Disponibilidad | Sistema de gestión (SaaS) | 2 | 3 | 6 | Medio | Ninguno | Aceptar / Mitigar (procedimiento manual de respaldo) | Dueño |
| R08 | Uso de dispositivo personal sin control (BYOD) | Confidencialidad/Integridad | Sistema de gestión, datos clientes | 3 | 3 | 9 | Medio | Ninguno | Mitigar (política de acceso solo desde equipos del negocio) | Dueño |
| R09 | Exposición de datos de tarjeta por mal manejo POS/QR | Confidencialidad/Legal | Terminal POS, sistema QR, transacciones | 2 | 4 | 8 | Medio | Procesador de pago PCI-compliant (Mercado Pago/Getnet) | Mitigar (verificar sticker/QR físico, no almacenar datos de tarjeta) | Dueño/cajero responsable |

**Nota sobre escala**: Probabilidad e Impacto en escala 1-5 (según plantilla de la cátedra). Valor = Probabilidad × Impacto. Niveles: Bajo (1-4), Medio (5-9), Alto (10-15), Crítico (16-25).
