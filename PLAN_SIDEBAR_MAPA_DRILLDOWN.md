# Plan de Implementación: Sidebar Derecha Mapa Interactivo

## Objetivo
Modificar la barra lateral derecha del mapa interactivo para implementar navegación drill-down jerárquica L3→L2→L1→L0.

## Regla Invariante
**SOLO L0 tiene ficha técnica visible.** Los niveles L3, L2, L1 son solo para navegación.

## Estructura de Navegación

```
SIDEBAR DERECHA (Panel existente modificado)
│
├── L3: NODO SELECCIONADO
│   │   [Nombre, Categoría, CAPEX, OPEX]
│   │
│   └── Componentes L2 (expandibles)
│       │
│       ├── L2: Componente A
│       │   └── Componentes L1 (expandibles)
│       │       ├── L1: Subcomponente A1
│       │       │   └── Elementos L0 (con link a ficha)
│       │       │       ├── L0: Elemento → [Ver Ficha]
│       │       │       └── L0: Elemento → [Ver Ficha]
│       │       └── L1: Subcomponente A2
│       │
│       └── L2: Componente B
```

---

## Sprint Único de Implementación

### Tarea 1: Modificar HTML del panel existente
- [ ] Quitar estructura de tabs actual
- [ ] Crear estructura drill-down con contenedores anidados
- **Tiempo estimado:** 30 min
- **Archivo:** `visualizacion/mapa-interactivo.html`

### Tarea 2: CSS para acordeones anidados
- [ ] Estilos para cada nivel (L3, L2, L1, L0)
- [ ] Indentación visual progresiva
- [ ] Colores por nivel
- [ ] Animación de expansión/colapso
- **Tiempo estimado:** 20 min
- **Archivo:** `visualizacion/mapa-interactivo.html` (sección style)

### Tarea 3: JS función mostrarNodoL3(nodo)
- [ ] Recibe nodo seleccionado del mapa
- [ ] Muestra info básica (nombre, categoría, CAPEX, OPEX)
- [ ] Lista componentes L2 del nodo según su tipo
- **Tiempo estimado:** 30 min
- **Archivo:** `visualizacion/mapa-interactivo.js`

### Tarea 4: JS función expandirL2(componente)
- [ ] Expande/colapsa sección L2
- [ ] Muestra lista de componentes L1
- [ ] Colapsa otros L2 abiertos
- **Tiempo estimado:** 20 min
- **Archivo:** `visualizacion/mapa-interactivo.js`

### Tarea 5: JS función expandirL1(componente)
- [ ] Expande/colapsa sección L1
- [ ] Muestra lista de elementos L0
- [ ] Colapsa otros L1 abiertos
- **Tiempo estimado:** 20 min
- **Archivo:** `visualizacion/mapa-interactivo.js`

### Tarea 6: JS función verFichaL0(id)
- [ ] Abre ficha técnica en nueva pestaña
- [ ] URL: `../fichas/BIM_L0_XXX.html`
- **Tiempo estimado:** 10 min
- **Archivo:** `visualizacion/mapa-interactivo.js`

### Tarea 7: Datos de jerarquía por tipo CALE
- [ ] Mapear L2→L1→L0 para cada tipo (n_1, n_2, n_3, C2, C3, C4, C5)
- [ ] Incluir CAPEX/OPEX por componente
- **Tiempo estimado:** 30 min
- **Archivo:** `visualizacion/mapa-interactivo.js`

---

## Archivos a Modificar

| Archivo | Modificación |
|---------|--------------|
| `visualizacion/mapa-interactivo.html` | HTML del panel + CSS |
| `visualizacion/mapa-interactivo.js` | Funciones JS + Datos jerarquía |

## Criterios de Aceptación

1. Al seleccionar nodo en mapa, sidebar muestra L3 con sus componentes L2
2. Click en L2 expande lista L1
3. Click en L1 expande lista L0
4. Click en L0 abre ficha técnica en nueva pestaña
5. Solo L0 tiene botón "Ver Ficha"
6. Navegación fluida con animaciones suaves

---

## Estado de Ejecución

| Tarea | Estado | Fecha |
|-------|--------|-------|
| Tarea 1 | ✅ Completado | 2025-12-03 |
| Tarea 2 | ✅ Completado | 2025-12-03 |
| Tarea 3 | ✅ Completado | 2025-12-03 |
| Tarea 4 | ✅ Completado | 2025-12-03 |
| Tarea 5 | ✅ Completado | 2025-12-03 |
| Tarea 6 | ✅ Completado | 2025-12-03 |
| Tarea 7 | ✅ Completado | 2025-12-03 |

## Resumen de Implementación

### Archivos Modificados:
1. **visualizacion/mapa-interactivo.html**
   - Agregado CSS para `.sidebar-right` y componentes drill-down
   - Agregado HTML para sidebar derecha permanente

2. **visualizacion/mapa-interactivo.js**
   - Agregado objeto `JERARQUIA_BIM_COMPLETA` con datos de 7 tipos CALE
   - Función `mostrarNodoEnSidebarDerecha(nodo)` - Muestra L3 y genera L2
   - Función `generarHTMLComponentesL1()` - Genera L1 dentro de L2
   - Función `generarHTMLElementosL0()` - Genera L0 con botón "Ver Ficha"
   - Función `toggleDrillL2()` - Expandir/colapsar acordeón L2
   - Función `toggleDrillL1()` - Expandir/colapsar acordeón L1
   - Función `determinarCategoriaRaw()` - Mapeo tipo→categoría
   - Integración con `seleccionarNodo()` existente

### Regla Invariante Implementada:
✅ **SOLO L0 tiene botón "Ver Ficha"** - Los niveles L3, L2, L1 son solo para navegación
