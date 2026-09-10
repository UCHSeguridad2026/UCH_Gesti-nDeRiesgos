
# TP: Gestión de Riesgos con SimpleRisk

## Datos del alumno

- **Nombre completo:** Tomás Ortiz
- **LU:** 44907961
- **Email institucional:ttomasortiz23@gmail.com
- **Comisión:4G

## Cómo levantar el entorno

1. Descargar el archivo OVA oficial de SimpleRisk desde https://www.simplerisk.com/documentation
   (sección de descargas / VM appliance).
2. Abrir VirtualBox → **Archivo → Importar servicio virtualizado** → seleccionar el archivo `.ova` 
   descargado → seguir el asistente con la configuración por defecto.
3. Iniciar la máquina virtual una vez importada.
4. Acceder a la aplicación desde el navegador en `https://localhost:8443` (o la IP que asigne la VM, 
   según configuración de red de VirtualBox).
5. Completar el asistente inicial de creación de cuenta de administrador con credenciales ficticias.
6. Los 3 usuarios creados (admin, analista, auditor) están documentados en `configuracion/usuarios.md` 
   (sin contraseñas, por seguridad).

## Decisiones de diseño

- **Metodología de riesgos:** se utilizó el método de puntuación clásica de SimpleRisk 
  (Probabilidad × Impacto), con escala 1-5 para ambas variables.
- **Escenario y supuestos:** se definió el contexto de una clínica privada de 120 empleados 
  con ~800 pacientes/día, manejando historias clínicas digitales, datos de obras sociales y 
  facturación, tal como establece la consigna del TP.
- **Selección de riesgos de nivel alto para planes de acción:** se priorizaron los 3 riesgos 
  de mayor score (Robo de dispositivo móvil sin cifrar, Ransomware sobre historias clínicas, 
  y Filtración de historias clínicas), por representar el mayor impacto potencial sobre la 
  confidencialidad y disponibilidad de información crítica de pacientes.
- **Verificación:** girasol

## Estructura del repositorio


entregas/Ortiz-Tomas-44907961/
├── README.md
├── .gitignore
├── informe/
│   └── informe-partec.md
├── configuracion/
│   ├── usuarios.md
│   └── riesgos.md
└── reporte-ejecutivo/
    └── reporte.pdf