# PLAN DE ACTUALIZACIÓN MAPA CALE

## 🎯 Objetivo
Actualizar `services/github_pages/mapa_cale.html` para usar **ÚNICAMENTE datos oficiales** del archivo `data/nodos_cale_197.json` generado desde `TABLA_197_NODOS_COMPLETA.csv`.

## ✅ Cambios Completados

### 1. Generación de Datos Oficiales
- ✅ Script `actualizador_sistema_cale.py` ejecutado exitosamente
- ✅ Archivo JSON creado: `services/github_pages/data/nodos_cale_197.json` (197 nodos)
- ✅ Configuración creada: `services/github_pages/data/config_sistema.json`
- ✅ Informe Markdown: `INFORME_SISTEMA_CALE_ACTUALIZADO.md`

### 2. Actualizaciones en HTML

#### index.html
- ✅ Estadísticas principales (CAPEX $851B → $12.4B, categorías 5 → 9)
- ✅ Sección mapa destacado (197 nodos)
- ✅ Sección categorías (9 categorías con datos reales)

#### mapa_cale.html
- ✅ Panel estadísticas (demanda, CAPEX, departamentos)
- ✅ Objeto `capexPorCategoria` (9 categorías con valores oficiales)
- ✅ Inicio de carga dinámica desde JSON (`fetch('data/nodos_cale_197.json')`)

## 🔄 Cambios Pendientes en mapa_cale.html

### 3. Eliminar Array Estático de Nodos
**Problema**: Líneas 462-1090 tienen array `nodosCale` hardcodeado con datos inventados  
**Solución**: Ya iniciamos el `fetch()` del JSON, ahora eliminar array viejo completo

### 4. Mover Lógica a Función `inicializarMapa()`
**Ubicación**: Después de línea 1090 (cierre del array)  
**Cambios necesarios**:
```javascript
function inicializarMapa() {
    // Colores de categorías - ACTUALIZAR PARA 9 CATEGORÍAS
    const categoryColors = {
        'Cat.A+': '#FF0000',    // Rojo intenso
        'Cat.A': '#FF4444',      // Rojo
        'Cat.B**': '#FF8800',    // Naranja intenso
        'Cat.B': '#FFAA00',      // Naranja
        'Cat.C1': '#FFDD00',     // Amarillo
        'Cat.C2': '#88DD00',     // Verde claro
        'Cat.C3': '#44DD00',     // Verde
        'Cat.C4': '#00DD44',     // Verde azulado
        'Cat.C5': '#00DD88'      // Turquesa
    };
    
    // [RESTO DE LA LÓGICA DEL MAPA]
}
```

### 5. Actualizar Filtros para 9 Categorías
**Ubicación**: Línea ~1290 función `updateMapDisplay()`  
**Cambios**:
```javascript
// ANTES (5 categorías con comentarios DATO INVENTADO):
if (document.getElementById('cat-a-plus').checked) activeCategories.push('CAT.A+');
if (document.getElementById('cat-a').checked) activeCategories.push('CAT.A');
if (document.getElementById('cat-b-plus').checked) activeCategories.push('CAT.B+');
if (document.getElementById('cat-b').checked) activeCategories.push('CAT.B');
if (document.getElementById('cat-c1').checked) activeCategories.push('CAT.C1');

// DESPUÉS (9 categorías oficiales):
if (document.getElementById('cat-a-plus').checked) activeCategories.push('Cat.A+');
if (document.getElementById('cat-a').checked) activeCategories.push('Cat.A');
if (document.getElementById('cat-b-star').checked) activeCategories.push('Cat.B**');
if (document.getElementById('cat-b').checked) activeCategories.push('Cat.B');
if (document.getElementById('cat-c1').checked) activeCategories.push('Cat.C1');
if (document.getElementById('cat-c2').checked) activeCategories.push('Cat.C2');
if (document.getElementById('cat-c3').checked) activeCategories.push('Cat.C3');
if (document.getElementById('cat-c4').checked) activeCategories.push('Cat.C4');
if (document.getElementById('cat-c5').checked) activeCategories.push('Cat.C5');
```

### 6. Actualizar Cálculo de CAPEX en updateMapDisplay()
**Ubicación**: Línea ~1310  
**Cambio**:
```javascript
// ANTES:
totalCapex += capexPorCategoria[markerObj.categoria] || 0;

// DESPUÉS (usar datos del nodo directamente):
totalCapex += (markerObj.nodo.capex_millones || 0);
```

### 7. Actualizar HTML de Filtros (Panel Lateral)
**Buscar**: `<div class="filter-group">`  
**Actualizar checkboxes**:
```html
<div class="filter-group">
    <h3>📊 Categorías CALE</h3>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-a-plus" checked>
        <span class="filter-dot" style="background: #FF0000;"></span>
        Cat.A+ (3 nodos) - Bogotá Sur, Bogotá Norte, Bucaramanga
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-a" checked>
        <span class="filter-dot" style="background: #FF4444;"></span>
        Cat.A (17 nodos) - Principales
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-b-star" checked>
        <span class="filter-dot" style="background: #FF8800;"></span>
        Cat.B** (16 nodos) - Regionales+
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-b" checked>
        <span class="filter-dot" style="background: #FFAA00;"></span>
        Cat.B (4 nodos) - Regionales
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-c1" checked>
        <span class="filter-dot" style="background: #FFDD00;"></span>
        Cat.C1 (16 nodos) - Especiales
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-c2" checked>
        <span class="filter-dot" style="background: #88DD00;"></span>
        Cat.C2 (50 satélites)
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-c3" checked>
        <span class="filter-dot" style="background: #44DD00;"></span>
        Cat.C3 (45 satélites)
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-c4" checked>
        <span class="filter-dot" style="background: #00DD44;"></span>
        Cat.C4 (30 satélites)
    </label>
    <label class="filter-label">
        <input type="checkbox" class="filter-checkbox" id="cat-c5" checked>
        <span class="filter-dot" style="background: #00DD88;"></span>
        Cat.C5 (16 satélites)
    </label>
</div>
```

### 8. Actualizar Popups de Nodos
**Problema**: Los popups muestran información inventada  
**Solución**: Usar datos del JSON directamente:
```javascript
// Crear popup con datos oficiales del CSV
const popupContent = `
    <div class="popup-content">
        <h3>${nodo.nombre}</h3>
        <p><strong>Categoría:</strong> ${nodo.categoria}</p>
        <p><strong>Departamento:</strong> ${nodo.departamento}</p>
        <p><strong>Tipo:</strong> ${nodo.tipo}</p>
        <p><strong>Configuración:</strong> ${nodo.configuracion}</p>
        <p><strong>Demanda Anual:</strong> ${nodo.demanda_anual.toLocaleString()} eval/año</p>
        <p><strong>CAPEX:</strong> $${nodo.capex_millones.toLocaleString()}M COP</p>
        <p><strong>OPEX Anual:</strong> $${nodo.opex_anual_millones.toLocaleString()}M COP</p>
    </div>
`;
```

### 9. Eliminar/Comentar Array `asignaciones`
**Problema**: Líneas 1092-1200 tienen asignaciones coordinador-satélite inventadas  
**Decisión**: 
- **Opción A**: Comentar todo el array y conexiones (más limpio)
- **Opción B**: Actualizar cuando tengamos coordenadas reales en el CSV

### 10. Agregar Manejo de Coordenadas Faltantes
**Problema**: El JSON tiene `lat: 0, lon: 0` para todos los nodos  
**Solución temporal**:
```javascript
// Si el nodo no tiene coordenadas, no crear marcador todavía
if (nodo.lat === 0 || nodo.lon === 0) {
    console.warn(`Nodo ${nodo.nombre} sin coordenadas geográficas`);
    return;
}
```

## 📋 Orden de Ejecución Recomendado

1. ✅ **COMPLETADO**: Iniciar carga desde JSON con `fetch()`
2. **SIGUIENTE**: Buscar y eliminar líneas 462-1090 (array hardcodeado)
3. Envolver lógica del mapa en `function inicializarMapa() {}`
4. Actualizar `categoryColors` a 9 categorías
5. Actualizar HTML de filtros (9 checkboxes)
6. Actualizar función `updateMapDisplay()` con 9 categorías
7. Actualizar popups con datos oficiales
8. Comentar array `asignaciones` y lógica de conexiones
9. Agregar validación de coordenadas
10. Llamar `inicializarMapa()` después del `fetch()`

## 🚀 Siguiente Acción Inmediata

Ejecutar búsqueda para eliminar todo el array viejo de nodos:

```bash
# Líneas a eliminar: 462-1090 (aprox. 628 líneas de datos inventados)
# Reemplazar con: código ya insertado del fetch() + inicializarMapa()
```

## 📍 Nota Crítica

**COORDENADAS GEOGRÁFICAS**: El CSV actual NO tiene coordenadas reales. Todos los nodos tienen `lat: 0, lon: 0`. 

**Opciones**:
1. Extraer coordenadas del array viejo antes de borrarlo (si son correctas)
2. Usar API de geocodificación para obtener coordenadas de municipios
3. Agregar coordenadas manualmente al CSV desde fuente oficial

**Decisión**: Guardar coordenadas del array viejo en un archivo separado para validación antes de borrar.
