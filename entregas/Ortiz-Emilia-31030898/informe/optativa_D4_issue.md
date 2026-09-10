# Actividad Optativa D4: Propuesta de Mejora (Issue de GitHub)

**Title:** [UX/Feature] Rediseño del flujo de acceso a "User Management" para administradores
**Labels:** `enhancement`, `UX`, `admin-panel`
**Assignees:** Unassigned

### 📝 Description / Descripción del problema
Actualmente, el flujo para que un Administrador cree un nuevo usuario en el sistema es poco intuitivo y requiere demasiados clics. 
El panel de "User Management" no se encuentra en el menú lateral principal de navegación, sino que el administrador debe:
1. Hacer clic en el ícono del engranaje (Settings) en la esquina superior derecha.
2. Utilizar la barra de búsqueda para tipear "User".
3. Localizar la tarjeta correspondiente entre los resultados para recién acceder al panel de gestión.

En sistemas de gestión de riesgos orientados a empresas, la administración de roles y usuarios es una tarea de acceso frecuente (Core Feature) que debería estar al alcance inmediato.

### 💡 Proposed Solution / Solución Propuesta
Se propone agregar un acceso directo a "User Management" en el menú oscuro lateral izquierdo (Sidebar). 
**Ubicación sugerida:** 
* Opción A: Crear una nueva categoría principal llamada `Admin` o `System` al final del menú lateral.
* Opción B: Incluirlo como un sub-ítem dentro del menú desplegable existente de `Governance`.

### 🖼️ Context / Contexto visual (Mockup conceptual)
*Menú actual:* Sidebar > [Falta opción de usuarios]
*Menú propuesto:* Sidebar > Governance > **User Management**

### ✅ Acceptance Criteria / Criterios de Aceptación
- [ ] El enlace "User Management" debe estar visible en el menú lateral izquierdo para los usuarios con rol de `Administrator`.
- [ ] Usuarios con roles inferiores (ej. Risk Analyst, Reviewer) no deben ver esta opción en el menú, manteniendo el control de acceso (RBAC) actual.