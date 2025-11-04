# 🎯 ANÁLISIS: FICHAS L4 vs MAPA INTERACTIVO CON NAVEGACIÓN JERÁRQUICA

**Fecha**: Noviembre 3, 2025  
**Contexto**: Definir estrategia de visualización para 197 nodos CALE

---

## 📊 COMPARATIVA DE ENFOQUES

### OPCIÓN A: Fichas HTML Individuales (197 archivos)

#### Ventajas ✅
- **SEO optimizado**: Cada nodo tiene URL única (`/fichas/nodo-01-bogota-sur.html`)
- **Compartible**: Enlaces directos a nodos específicos
- **Offline-friendly**: Archivos estáticos sin dependencias de JS
- **Imprimible**: Versión física de cada ficha
- **Carga rápida**: No requiere cargar todo el dataset
- **Indexable**: Buscadores pueden indexar cada nodo

#### Desventajas ❌
- **Mantenimiento complejo**: 197 archivos HTML a actualizar
- **Inconsistencias**: Riesgo de versiones desactualizadas
- **Duplicación de código**: Template repetido 197 veces
- **Navegación fragmentada**: Usuario pierde contexto geográfico
- **Sin comparación**: Difícil comparar nodos entre sí
- **Espacio en disco**: ~40-50 MB de archivos HTML

#### Estructura de Archivos
```
fichas/
├── nodo-01-bogota-sur.html
├── nodo-02-bogota-norte.html
├── nodo-03-bucaramanga.html
├── ...
├── nodo-56-riosucio.html
├── sat-001-arenal.html
├── sat-002-curumani.html
├── ...
└── sat-141-necochea.html

Total: 197 archivos × ~250 KB = ~49 MB
```

---

### OPCIÓN B: Mapa Interactivo con Navegación Jerárquica (Recomendado)

#### Ventajas ✅
- **Contexto geográfico**: Usuario ve ubicación + relaciones espaciales
- **Navegación intuitiva**: Árbol jerárquico L3 → L4
- **Comparación visual**: Ver múltiples nodos simultáneamente
- **Filtros dinámicos**: Por categoría, demanda, departamento, presupuesto
- **Datos en tiempo real**: Una fuente de verdad (JSON)
- **Mantenimiento simple**: Actualizar 1 JSON vs 197 HTML
- **Búsqueda integrada**: Buscar por municipio/código/demanda
- **Métricas agregadas**: Ver totales por tipo CALE en tiempo real
- **Exportable**: Generar PDF/Excel de selección
- **Responsive**: Adaptable a móvil/tablet/desktop

#### Desventajas ❌
- **Requiere JavaScript**: No funciona sin JS habilitado
- **SEO limitado**: URLs dinámicas (#/nodo/01)
- **Carga inicial**: Debe cargar GeoJSON completo (~2-3 MB)
- **Complejidad técnica**: Requiere framework (Leaflet/React)

#### Estructura Propuesta
```
app/
├── index.html (SPA)
├── data/
│   ├── nodos.geojson (197 nodos con geometrías)
│   ├── tipos-l3.json (9 tipos CALE)
│   └── satelites.geojson (141 satélites)
├── js/
│   ├── mapa.js (Leaflet/Mapbox)
│   ├── sidebar.js (Navegación jerárquica)
│   ├── filtros.js (Filtros dinámicos)
│   └── popup.js (Detalles de nodo)
└── css/
    ├── mapa.css
    └── sidebar.css

Total: ~8 archivos + 3 JSON = ~5 MB
```

---

## 🏗️ ARQUITECTURA RECOMENDADA: HÍBRIDO

### Concepto: "Mapa Interactivo + Fichas Generadas Dinámicamente"

```
┌─────────────────────────────────────────────────────────────┐
│                    MAPA INTERACTIVO                         │
│  ┌──────────────────┐  ┌───────────────────────────────┐   │
│  │   SIDEBAR        │  │      MAPA GEOGRÁFICO          │   │
│  │  (Jerárquico)    │  │                               │   │
│  │                  │  │  🔴 NODO_01 (Bogotá Sur)      │   │
│  │ 📂 L3 TIPOS      │  │  🔴 NODO_02 (Bogotá Norte)    │   │
│  │  ├─ 🔴 CALE.n_1.plus (3)                            │   │
│  │  │  ├─ NODO_01  │  │  🟠 NODO_04 (Cali)            │   │
│  │  │  ├─ NODO_02  │  │  🟠 NODO_05 (Ibagué)          │   │
│  │  │  └─ NODO_03  │  │                               │   │
│  │  ├─ 🟠 CALE.n_1.base (17)                           │   │
│  │  │  ├─ NODO_04  │  │  [Filtros: Categoría ▼]      │   │
│  │  │  ├─ NODO_05  │  │  [Buscar: Bogotá...    🔍]    │   │
│  │  │  └─ ...      │  │                               │   │
│  │  ├─ 🟡 CALE.n_2.star (16)                           │   │
│  │  ├─ 🟢 CALE.n_2.base (4)                            │   │
│  │  ├─ 🔵 CALE.n_3 (16) │                              │   │
│  │  ├─ ⬤ CALE.C2 (50)   │                              │   │
│  │  ├─ ⬤ CALE.C3 (45)   │                              │   │
│  │  ├─ ⬤ CALE.C4 (30)   │                              │   │
│  │  └─ ⬤ CALE.C5 (16)   │                              │   │
│  │                  │  │                               │   │
│  │ 📊 MÉTRICAS L5   │  │                               │   │
│  │  CAPEX: $206B   │  │                               │   │
│  │  Nodos: 197     │  │                               │   │
│  │  Capacidad: 2.5M│  │                               │   │
│  └──────────────────┘  └───────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (Click en NODO_01)
┌─────────────────────────────────────────────────────────────┐
│              POPUP / PANEL LATERAL DETALLADO                │
├─────────────────────────────────────────────────────────────┤
│ 🏛️ NODO_01: BOGOTÁ SUR                                     │
│ Categoría: Cat.A+ (CALE.n_1.plus)                          │
│                                                             │
│ 📊 DEMANDA Y CAPACIDAD                                      │
│ • Demanda anual: 80,453 evaluaciones/año                    │
│ • Capacidad instalada: 173,040 eval/año (215% cobertura)   │
│ • Cluster: 7 municipios vinculados                          │
│                                                             │
│ 📍 UBICACIÓN                                                │
│ • Municipio: Bogotá D.C.                                    │
│ • DANE: 11001                                               │
│ • Coordenadas: 4.649°N, 74.107°W                           │
│ • Dirección: Cra. 71D #6-94 Sur, CC Plaza de las Américas  │
│                                                             │
│ 🏢 INFRAESTRUCTURA                                          │
│ • Área total: 3,800 m²                                      │
│ • Cubículos: 24 (CALE-T-24q)                               │
│ • Inmobiliaria: CBRE Colombia                               │
│ • Arriendo mensual: $77,000,000                             │
│ • Arriendo anual: $924,000,000                              │
│                                                             │
│ 💰 PRESUPUESTO (VALORES L3 UNITARIOS)                       │
│ • CAPEX: $3,728,340,000                                     │
│ • OPEX anual: $2,400,000,000                                │
│ • OPEX mensual: $200,000,000                                │
│                                                             │
│ 👥 PERSONAL REQUERIDO                                       │
│ • Coordinador: 1                                            │
│ • Psicólogos: 3                                             │
│ • Técnicos: 6                                               │
│ • Administrativos: 2                                        │
│ • Total: 12 funcionarios                                    │
│                                                             │
│ 🛰️ SATÉLITES VINCULADOS                                    │
│ • SAT_016: Fosca (Cundinamarca) - 500 eval/año             │
│ • [Mostrar 6 más...]                                        │
│                                                             │
│ 📋 ACCIONES                                                 │
│ [Ver Ficha L3: CALE.n_1.plus] [Generar PDF] [Exportar]    │
│ [Ver en Google Maps] [Comparar con otros nodos]            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 PROPUESTA FINAL: NAVEGACIÓN JERÁRQUICA MEJORADA

### Sidebar: Árbol Expandible por Tipo L3

```javascript
const sidebar = {
  "L3_TIPOS": [
    {
      "tipo": "L3.CALE.n_1.plus",
      "nombre": "CALE Metropolitano Premium",
      "categoria": "Cat.A+",
      "color": "#E63946",
      "icono": "🔴",
      "cantidad_instancias": 3,
      "expanded": false, // Colapsado por defecto
      "nodos": [
        {
          "id": "NODO_01",
          "nombre": "BOGOTÁ SUR",
          "departamento": "Bogotá D.C.",
          "demanda": 80453,
          "coords": [4.649251, -74.106992],
          "highlighted": false
        },
        {
          "id": "NODO_02",
          "nombre": "BOGOTÁ NORTE",
          "demanda": 70396,
          "coords": [4.649251, -74.106992]
        },
        {
          "id": "NODO_03",
          "nombre": "BUCARAMANGA",
          "demanda": 68000,
          "coords": [7.11647, -73.132562]
        }
      ],
      "metricas_agregadas": {
        "capex_total": 11185020000,
        "demanda_total": 218849,
        "capacidad_total": 519120
      }
    },
    {
      "tipo": "L3.CALE.n_1.base",
      "nombre": "CALE Metropolitano Base",
      "categoria": "Cat.A",
      "color": "#F77F00",
      "icono": "🟠",
      "cantidad_instancias": 17,
      "expanded": false,
      "nodos": [
        {
          "id": "NODO_04",
          "nombre": "CALI",
          "departamento": "Valle del Cauca",
          "demanda": 57318,
          "coords": [3.413686, -76.52133]
        },
        // ... 16 nodos más
      ],
      "metricas_agregadas": {
        "capex_total": 47911780000,
        "demanda_total": 387065,
        "capacidad_total": 2169948
      }
    },
    {
      "tipo": "L3.CALE.n_2.star",
      "nombre": "CALE Regional Plus",
      "categoria": "Cat.B**",
      "color": "#FCBF49",
      "icono": "🟡",
      "cantidad_instancias": 16,
      "expanded": false,
      "nodos": [/* 16 nodos */]
    },
    {
      "tipo": "L3.CALE.n_2.base",
      "categoria": "Cat.B",
      "cantidad_instancias": 4,
      "nodos": [/* 4 nodos */]
    },
    {
      "tipo": "L3.CALE.n_3.base",
      "categoria": "Cat.C1",
      "cantidad_instancias": 16,
      "nodos": [/* 16 nodos */]
    },
    {
      "tipo": "L3.SATELITE.c2",
      "categoria": "Cat.C2",
      "cantidad_instancias": 50,
      "nodos": [/* 50 satélites */]
    },
    {
      "tipo": "L3.SATELITE.c3",
      "categoria": "Cat.C3",
      "cantidad_instancias": 45,
      "nodos": [/* 45 satélites */]
    },
    {
      "tipo": "L3.SATELITE.c4_c5",
      "categoria": "Cat.C4 + C5",
      "cantidad_instancias": 46,
      "nodos": [/* 46 satélites */]
    }
  ]
}
```

### HTML del Sidebar

```html
<div id="sidebar" class="sidebar">
  <div class="sidebar-header">
    <h2>Red Nacional CALE</h2>
    <span class="badge">197 nodos</span>
  </div>
  
  <div class="search-box">
    <input type="text" placeholder="Buscar municipio..." id="search">
    <button class="btn-search">🔍</button>
  </div>
  
  <div class="filters">
    <select id="filter-categoria">
      <option value="">Todas las categorías</option>
      <option value="Cat.A+">Cat.A+ (3)</option>
      <option value="Cat.A">Cat.A (17)</option>
      <option value="Cat.B**">Cat.B** (16)</option>
      <option value="Cat.B">Cat.B (4)</option>
      <option value="Cat.C1">Cat.C1 (16)</option>
      <option value="Cat.C2">Cat.C2 (50)</option>
      <option value="Cat.C3">Cat.C3 (45)</option>
      <option value="Cat.C4-5">Cat.C4-5 (46)</option>
    </select>
    
    <select id="filter-departamento">
      <option value="">Todos los departamentos</option>
      <option value="BOGOTA">Bogotá D.C. (2)</option>
      <option value="SANTANDER">Santander (3)</option>
      <!-- ... -->
    </select>
  </div>
  
  <div class="tipo-list">
    <!-- Cat.A+ (CALE.n_1.plus) -->
    <div class="tipo-item" data-tipo="L3.CALE.n_1.plus">
      <div class="tipo-header" onclick="toggleTipo(this)">
        <span class="icon">🔴</span>
        <span class="nombre">CALE.n_1.plus</span>
        <span class="badge">3</span>
        <span class="toggle">▼</span>
      </div>
      <div class="tipo-metricas collapsed">
        <small>
          CAPEX: $11.2B | Demanda: 218k | Capacidad: 519k
        </small>
      </div>
      <ul class="nodos-list collapsed">
        <li class="nodo-item" data-nodo="NODO_01" onclick="zoomToNodo('NODO_01')">
          <span class="nodo-nombre">BOGOTÁ SUR</span>
          <span class="nodo-demanda">80.5k</span>
          <button class="btn-info" onclick="showPopup('NODO_01')">ℹ️</button>
        </li>
        <li class="nodo-item" data-nodo="NODO_02">
          <span class="nodo-nombre">BOGOTÁ NORTE</span>
          <span class="nodo-demanda">70.4k</span>
          <button class="btn-info" onclick="showPopup('NODO_02')">ℹ️</button>
        </li>
        <li class="nodo-item" data-nodo="NODO_03">
          <span class="nodo-nombre">BUCARAMANGA</span>
          <span class="nodo-demanda">68.0k</span>
          <button class="btn-info" onclick="showPopup('NODO_03')">ℹ️</button>
        </li>
      </ul>
    </div>
    
    <!-- Cat.A (CALE.n_1.base) -->
    <div class="tipo-item" data-tipo="L3.CALE.n_1.base">
      <div class="tipo-header" onclick="toggleTipo(this)">
        <span class="icon">🟠</span>
        <span class="nombre">CALE.n_1.base</span>
        <span class="badge">17</span>
        <span class="toggle">▼</span>
      </div>
      <div class="tipo-metricas collapsed">
        <small>
          CAPEX: $47.9B | Demanda: 387k | Capacidad: 2.17M
        </small>
      </div>
      <ul class="nodos-list collapsed">
        <li class="nodo-item" data-nodo="NODO_04">
          <span class="nodo-nombre">CALI</span>
          <span class="nodo-demanda">57.3k</span>
          <button class="btn-info">ℹ️</button>
        </li>
        <!-- ... 16 nodos más -->
      </ul>
    </div>
    
    <!-- Repetir para Cat.B**, Cat.B, Cat.C1, C2, C3, C4-5 -->
  </div>
  
  <div class="sidebar-footer">
    <h3>Métricas Nacionales (L5)</h3>
    <div class="metricas-grid">
      <div class="metrica">
        <label>CAPEX Total</label>
        <value>$206.7 B</value>
      </div>
      <div class="metrica">
        <label>OPEX Anual</label>
        <value>$135.5 B</value>
      </div>
      <div class="metrica">
        <label>Capacidad Total</label>
        <value>2.56 M eval/año</value>
      </div>
      <div class="metrica">
        <label>Nodos Activos</label>
        <value>197</value>
      </div>
    </div>
    
    <div class="export-buttons">
      <button class="btn-export" onclick="exportToExcel()">
        📊 Exportar Excel
      </button>
      <button class="btn-export" onclick="generatePDF()">
        📄 Generar PDF
      </button>
    </div>
  </div>
</div>
```

---

## 🎯 INTERACCIONES CLAVE

### 1. Click en Tipo L3 (Expandir/Colapsar)

```javascript
function toggleTipo(header) {
  const tipoItem = header.parentElement;
  const nodosList = tipoItem.querySelector('.nodos-list');
  const metricas = tipoItem.querySelector('.tipo-metricas');
  const toggle = header.querySelector('.toggle');
  
  nodosList.classList.toggle('collapsed');
  metricas.classList.toggle('collapsed');
  toggle.textContent = nodosList.classList.contains('collapsed') ? '▼' : '▲';
  
  // Highlight todos los nodos de este tipo en el mapa
  const tipo = tipoItem.dataset.tipo;
  highlightTipoEnMapa(tipo);
}
```

### 2. Click en Nodo Individual

```javascript
function zoomToNodo(nodoId) {
  // 1. Centrar mapa en el nodo
  const nodo = getNodoData(nodoId);
  map.flyTo([nodo.coords[0], nodo.coords[1]], 12, {
    duration: 1.5
  });
  
  // 2. Abrir popup con detalles
  setTimeout(() => {
    showPopup(nodoId);
  }, 1600);
  
  // 3. Highlight en sidebar
  document.querySelectorAll('.nodo-item').forEach(item => {
    item.classList.remove('active');
  });
  document.querySelector(`[data-nodo="${nodoId}"]`).classList.add('active');
}
```

### 3. Hover sobre Tipo L3

```javascript
function highlightTipoEnMapa(tipo) {
  // Resaltar todos los marcadores de este tipo
  map.eachLayer(layer => {
    if (layer.options && layer.options.tipo === tipo) {
      layer.setStyle({
        fillOpacity: 0.9,
        radius: 12,
        weight: 3
      });
    } else {
      layer.setStyle({
        fillOpacity: 0.6,
        radius: 8,
        weight: 1
      });
    }
  });
}
```

### 4. Búsqueda Dinámica

```javascript
document.getElementById('search').addEventListener('input', (e) => {
  const query = e.target.value.toLowerCase();
  
  document.querySelectorAll('.nodo-item').forEach(item => {
    const nombre = item.querySelector('.nodo-nombre').textContent.toLowerCase();
    
    if (nombre.includes(query)) {
      item.style.display = 'flex';
      // Auto-expandir el tipo padre
      item.closest('.tipo-item').querySelector('.nodos-list').classList.remove('collapsed');
    } else {
      item.style.display = 'none';
    }
  });
});
```

---

## 📈 VENTAJAS DEL ENFOQUE JERÁRQUICO

### ✅ UX/UI Benefits

1. **Contexto Preservado**: Usuario siempre ve la jerarquía L3 → L4
2. **Navegación Predecible**: Estructura mental clara (tipos → instancias)
3. **Comparación Facilitada**: Ver todos los nodos de un tipo simultáneamente
4. **Filtrado Intuitivo**: Expandir solo categorías de interés
5. **Métricas Agregadas**: Ver totales por tipo antes de explorar detalles

### ✅ Technical Benefits

1. **Single Source of Truth**: Un JSON vs 197 HTML
2. **Actualización Centralizada**: Cambiar datos en un lugar
3. **Performance**: Lazy loading de detalles (solo cargar popup al hacer click)
4. **Búsqueda Rápida**: Índice en memoria vs búsqueda en 197 archivos
5. **Exportación Dinámica**: Generar PDF solo de nodos seleccionados

### ✅ Business Benefits

1. **Mantenibilidad**: Reducción 95% en archivos a mantener
2. **Escalabilidad**: Fácil agregar nuevos nodos (solo actualizar JSON)
3. **Analytics**: Tracking de interacciones (qué tipos/nodos se consultan más)
4. **Mobile-Friendly**: Sidebar colapsable en dispositivos móviles

---

## 🚀 RECOMENDACIÓN FINAL

### ✨ MEJOR PRÁCTICA: **Mapa Interactivo con Sidebar Jerárquico**

**Justificación**:

1. ✅ **Alineado con arquitectura BIM**: L3 (tipos) → L4 (instancias) → L5 (métricas)
2. ✅ **UX superior**: Navegación intuitiva con contexto geográfico
3. ✅ **Mantenimiento eficiente**: 1 fuente de datos vs 197 archivos
4. ✅ **Escalable**: Fácil agregar filtros, búsquedas, comparaciones
5. ✅ **Analytics-ready**: Métricas agregadas en tiempo real

**NO generar fichas HTML individuales SALVO**:
- Requerimiento legal de archivos estáticos auditables
- Necesidad de versión imprimible offline
- SEO crítico para búsquedas específicas por municipio

En esos casos, generar PDF dinámicamente on-demand, no HTML estático.

---

## 📋 PRÓXIMOS PASOS SUGERIDOS

1. ✅ **Crear estructura JSON jerárquica** (tipos_l3_con_instancias.json)
2. ✅ **Implementar sidebar con árbol expandible**
3. ✅ **Integrar mapa Leaflet/Mapbox**
4. ✅ **Añadir búsqueda y filtros**
5. ✅ **Implementar popups detallados**
6. ✅ **Agregar exportación PDF/Excel on-demand**
7. ⏳ **Testing con usuarios reales**

---

**Conclusión**: La navegación jerárquica en mapa interactivo es superior en todos los aspectos excepto SEO, que se puede resolver con server-side rendering (Next.js/Nuxt) si es crítico.

¿Procedo a implementar la estructura JSON jerárquica y el código del mapa interactivo con sidebar?
