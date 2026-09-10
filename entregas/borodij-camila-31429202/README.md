**Materia:** Seguridad de Sistemas  
**Carrera:** Licenciatura en Sistemas de Información  
**Estudiante:** Camila Aylen Borodij (LU: 31429202)  

---

## 1. Guía de Instalación y Despliegue del Entorno

Para levantar el entorno local de SimpleRisk con Docker Compose, ejecute los siguientes comandos desde la carpeta entorno:

  cd entorno/
  docker-compose up -d

Una vez iniciados los contenedores, la aplicación estará disponible en el navegador web a través de la dirección: http://localhost:8080

---

## 2. Decisiones de Diseño

* **Metodología de Riesgos:** Se adoptó una matriz semicuantitativa clásica de 5x5 (Probabilidad x Impacto) por su alineación con la interfaz nativa de SimpleRisk y su agilidad para la toma de decisiones iniciales en el ámbito de la salud[cite: 1].
* **Supuestos del Escenario:** La entidad corresponde a una clínica privada con 120 empleados, una afluencia media de 800 pacientes diarios y administración digitalizada de historias clínicas y facturación con obras sociales[cite: 1].

### Verificación
girasol

---

## 3. Checklist de Auto-Revisión

- [x] No hay credenciales en el repositorio[cite: 1]
- [x] El .gitignore está correctamente configurado[cite: 1]
- [x] Las capturas no muestran datos sensibles[cite: 1]
- [x] Los archivos .sql o dumps no están subidos[cite: 1]
- [x] El informe está en formato legible[cite: 1]
- [x] El reporte ejecutivo está completo[cite: 1]
- [x] Los mensajes de commit son descriptivos[cite: 1]
- [x] Mi branch está actualizada y funciona[cite: 1]
