# 🚀 PLAN CORREGIDO: SISTEMA COMPLETO MUNAY-SNCALE

**Proyecto:** Sistema Nacional de Centros de Enseñanza Automovilística (SNCALE)
**Versión:** 4.0 - ARQUITECTURA REAL CORREGIDA
**Fecha:** 2025-10-29
**Estado:** 🟡 EN PLANIFICACIÓN
**Prioridad:** 🔴 ALTA

---

## 🎯 ACLARACIÓN CRÍTICA: ARQUITECTURA REAL

### **HOJAS DE GOOGLE SHEETS (Fuente Única de Verdad)**

**URL Base:** https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit

#### **📍 HOJA 1: `arquitectura_red_cale_nacional`**
**Propósito:** MAPA INTERACTIVO (ubicaciones de 141+ centros CALE)

**Datos que contiene:**
- centro_id, tipo_centro (NODO_PRINCIPAL/SATELITE)
- municipio, departamento
- **⚠️ FALTA:** latitud, longitud, codigo_dane
- categoria_cale (Cat.A+ → CALE.n_1+)
- demanda_estimada_anual
- nodo_principal (referencia al nodo padre)
- total_municipios_cluster
- distancia_maxima_km, distancia_promedio_km

**ACCIÓN REQUERIDA:**
- ✅ Completar columnas faltantes: latitud, longitud, codigo_dane
- ✅ Actualizar datos NODO_PRINCIPAL
- ✅ Actualizar nomenclatura Cat.X → CALE.n_X

**Destino:** Mapa Interactivo Leaflet.js

---

#### **📊 HOJA 2: `presupuesto_general`**
**Propósito:** PRESUPUESTO TOTAL DEL PROYECTO COMPLETO

**Datos que contiene:**
- Presupuesto consolidado de toda la red nacional
- Inversión total (CAPEX)
- Gastos operativos (OPEX)
- Costos por categoría de centro
- Distribución por región/departamento

**Destino:** Dashboards, reportes ejecutivos, visualizaciones de presupuesto

---

#### **🔬 HOJA 3: `presupuesto_nivel_-1` (ATÓMICOS)**
**Propósito:** **FICHAS TÉCNICAS** + CATÁLOGO BASE BIM

**Datos que contiene:**
- **125 productos atómicos** (componentes base sin subcomponentes)
- Códigos ERP: MAT-XXX, ELE-XXX, MOB-XXX, SEÑ-XXX, etc.
- Nombre Comercial
- Categoría BIM, Clase IFC
- Unidad de Medida
- CAPEX Unitario, OPEX Anual, TCO 5 Años
- Código DANE, Código CAMACOL
- Proveedor Principal, Garantía, Normativas
- **Columna O: "Ficha Técnica"** → URL de la página web de la ficha
  - Ejemplo: `https://sncale.mintransporte.gov.co/fichas/mat-001.html`
  - **Esta URL se genera automáticamente** desde los datos de esta fila

**USO CRÍTICO:**
- Los datos de cada fila son lo que se muestra en la ficha técnica HTML
- La ficha técnica es 100% dinámica (lee datos desde esta hoja)
- **NO HAY DATOS HARDCODEADOS EN HTML**

**Destino:**
- Fichas técnicas HTML (generadas dinámicamente)
- Visor 3D (componentes atómicos)
- Catálogo de productos

---

#### **🏗️ HOJAS 4-6: JERARQUÍA BIM RECURSIVA**

**`nivel_0.ESP_xxxx`** - Espacios/Planos 3D Base
- Ensamblajes de componentes atómicos (presupuesto_nivel_-1)
- Ejemplos:
  - `MOB-001_cubiculo.json` (1.2×0.8×1.6m)
    - Componentes: Mesa + Silla + 3×Divisiones + LED + Canaleta
    - Precio: $1,100,000 (suma automática de atómicos)
  - `SALA-FORM_espacio.json`
  - `DATACENTER_espacio.json`

**`nivel_1.ESP_xxxx`** - Plantas/Zonas Completas
- Se construyen con `nivel_0`
- Ejemplos:
  - `CALE-T.24q` (Sala Teórica 24 puestos)
    - Componentes: 24× MOB-001_cubiculo
    - Precio: $26,400,000 (24 × $1.1M)
  - `CALE-P.Clase1` (Pista Práctica Clase 1)
    - Componentes: Asfalto + Señalización + Iluminación
  - `AREA-ADM` (Área Administrativa)
  - `SERVICIOS` (Baños, cafetería, etc.)

**`nivel_2+.ESP_xxxx`** - Centros CALE Completos
- Se construyen con `nivel_1`
- Ejemplos:
  - `CALE.n_1+` (Centro Principal Enhanced)
    - Componentes: CALE-T.24q + CALE-P.C3 + CALE-P.C2 + 4×CALE-P.C1
    - Precio: $750,000,000+
  - `CALE.n_1` (Centro Principal)
  - `CALE.n_2**` (Centro Intermedio Enhanced)
  - `CALE.n_3` (Centro Básico)

**Destino:** Visores 3D y 2D (composición jerárquica)

---

## 🏗️ JERARQUÍA BIM RECURSIVA EXPLICADA

```
┌─────────────────────────────────────────────────────────────┐
│  NIVEL -1: ATÓMICOS (presupuesto_nivel_-1)                  │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  • 125 productos base SIN subcomponentes                    │
│  • Fuente única de verdad para specs técnicas              │
│  • Ejemplos:                                                │
│    - SILLA-ERG-001: $450,000                               │
│    - MESA-CUB-001: $350,000                                │
│    - DIV-MEL-1600: $80,000 (panel divisor)                 │
│    - LED-STRIP-12W: $45,000                                │
│    - CANAL-PVC-80: $15,000 (canaleta cables)               │
│    - PINTURA-INT: $525,000                                 │
│    - CABLEADO-CAT6A: $1,500,000                            │
│                                                             │
│  📄 FICHA TÉCNICA = DATOS DE ESTA FILA                      │
│     - Código, Nombre, Precio, Proveedor, Garantía          │
│     - Normativas, Especificaciones técnicas                │
│     - URL ficha: https://sncale.../fichas/{codigo}.html    │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │ $ref (referencias JSON)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  NIVEL 0: ESPACIOS BASE (nivel_0.ESP_xxxx)                  │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  • Ensamblajes de ATÓMICOS                                  │
│  • Espacios/módulos 3D reutilizables                       │
│  • Precio calculado automáticamente                        │
│                                                             │
│  Ejemplo: MOB-001_cubiculo                                  │
│  {                                                          │
│    "codigo": "MOB-001",                                     │
│    "nombre": "Cubículo Evaluación Estándar Plus",          │
│    "dimensiones": {"x": 1.2, "y": 0.8, "z": 1.6},         │
│    "composicion": {                                         │
│      "es_recursivo": true,                                 │
│      "subcomponentes": [                                    │
│        {"$ref": "atomicos/MESA-CUB-001.json", "cant": 1},  │
│        {"$ref": "atomicos/SILLA-ERG-001.json", "cant": 1}, │
│        {"$ref": "atomicos/DIV-MEL-1600.json", "cant": 3},  │
│        {"$ref": "atomicos/LED-STRIP-12W.json", "cant": 1}, │
│        {"$ref": "atomicos/CANAL-PVC-80.json", "cant": 1}   │
│      ]                                                      │
│    },                                                       │
│    "precio_calculado": 1100000  // AUTO: suma de $refs     │
│  }                                                          │
│                                                             │
│  ⚙️ CÁLCULO AUTOMÁTICO:                                     │
│     $350K (mesa) + $450K (silla) + $240K (3×div)           │
│     + $45K (LED) + $15K (canaleta) = $1,100,000            │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │ $ref (referencias JSON)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  NIVEL 1: PLANTAS/ZONAS (nivel_1.ESP_xxxx)                  │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  • Ensamblajes de NIVEL 0                                   │
│  • Salas completas, pistas, áreas funcionales              │
│                                                             │
│  Ejemplo: CALE-T.24q (Sala Teórica 24 puestos)             │
│  {                                                          │
│    "codigo": "SALA-T-24q",                                  │
│    "nombre": "Sala Evaluación Teórica 24 Puestos",         │
│    "dimensiones": {"x": 10, "y": 8, "z": 3},              │
│    "composicion": {                                         │
│      "es_recursivo": true,                                 │
│      "subcomponentes": [                                    │
│        {"$ref": "nivel_0/MOB-001.json", "cant": 24},       │
│        {"$ref": "atomicos/PINTURA-INT.json", "cant": 1},   │
│        {"$ref": "atomicos/ILUM-LED-40W.json", "cant": 18}, │
│        {"$ref": "nivel_0/AREA-CIRCULACION.json", "cant":1} │
│      ]                                                      │
│    },                                                       │
│    "precio_calculado": 4400000  // AUTO: 24×$1.1M + otros  │
│  }                                                          │
│                                                             │
│  Otros ejemplos:                                            │
│  - CALE-T.16q: Sala 16 puestos ($2,937,000)               │
│  - CALE-T.8q: Sala 8 puestos ($1,468,500)                 │
│  - CALE-P.C1: Pista Clase 1 livianos                       │
│  - CALE-P.C2: Pista Clase 2 medianos                       │
│  - CALE-P.C3: Pista Clase 3 pesados                        │
│  - AREA-ADMIN: Oficinas administrativas                    │
│  - DATACENTER: Cuarto de servidores                        │
│  - SERVICIOS: Baños, cafetería                             │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │ $ref (referencias JSON)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  NIVEL 2+: CENTROS CALE COMPLETOS                           │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  • Ensamblajes de NIVEL 1                                   │
│  • Configuraciones completas por categoría                 │
│                                                             │
│  CALE.n_1+ (Cat.A+ - Centro Principal Enhanced)            │
│  {                                                          │
│    "categoria": "CALE.n_1+",                                │
│    "nombre": "Centro Principal Enhanced Bogotá Norte",     │
│    "composicion": {                                         │
│      "subcomponentes": [                                    │
│        {"$ref": "nivel_1/SALA-T-24q.json", "cant": 1},     │
│        {"$ref": "nivel_1/PISTA-P-C3.json", "cant": 1},     │
│        {"$ref": "nivel_1/PISTA-P-C2.json", "cant": 1},     │
│        {"$ref": "nivel_1/PISTA-P-C1.json", "cant": 4},     │
│        {"$ref": "nivel_1/DATACENTER.json", "cant": 1},     │
│        {"$ref": "nivel_1/AREA-ADMIN.json", "cant": 1},     │
│        {"$ref": "nivel_1/SERVICIOS.json", "cant": 1}       │
│      ]                                                      │
│    },                                                       │
│    "precio_calculado": 750000000  // AUTO calculado        │
│  }                                                          │
│                                                             │
│  Otras categorías:                                          │
│  - CALE.n_1 (Cat.A): T-24q + P-C3 + 2×P-C1                │
│  - CALE.n_2** (Cat.B**): T-16q + P-C2 + 2×P-C1            │
│  - CALE.n_2 (Cat.B): T-16q (solo teórico)                 │
│  - CALE.n_3 (Cat.C1): T-8q + P-C1                         │
│  - CALE.C2: T-4q (satélite)                                │
│  - CALE.C3: T-2q (satélite)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 FLUJO DE ACTUALIZACIÓN AUTOMÁTICA

### **Escenario: Cambio de Precio en un Atómico**

**Ejemplo:** La silla ergonómica sube de precio

```
1️⃣ CAMBIO EN GOOGLE SHEETS (presupuesto_nivel_-1)
   ════════════════════════════════════════════════
   Fila SILLA-ERG-001:
   CAPEX: $450,000 → $500,000 ✏️

2️⃣ EXPORTAR CSV
   ════════════════════════════════════════════════
   Archivo → Descargar → CSV
   Guardar: presupuesto_nivel_-1.csv

3️⃣ EJECUTAR SCRIPT DE SINCRONIZACIÓN
   ════════════════════════════════════════════════
   $ python services/google_sheets/sync_sistema_completo.py

   Proceso:
   a) Lee presupuesto_nivel_-1.csv
   b) Actualiza atomicos/SILLA-ERG-001.json
      {"precio": 500000}  // ✅ Nuevo precio

   c) Recalcula CASCADA (referencias $ref):

      nivel_0/MOB-001_cubiculo.json
      ├─ $ref MESA-CUB-001: $350,000
      ├─ $ref SILLA-ERG-001: $500,000 ← ACTUALIZADO
      ├─ $ref DIV-MEL-1600 ×3: $240,000
      ├─ $ref LED-STRIP-12W: $45,000
      └─ $ref CANAL-PVC-80: $15,000
      ═══════════════════════════════════
      PRECIO NUEVO: $1,150,000 ✅ (+$50K)

      nivel_1/SALA-T-24q.json
      ├─ $ref MOB-001 ×24: $1,150,000 ← ACTUALIZADO
      ├─ $ref PINTURA-INT: $525,000
      └─ $ref ILUM-LED ×18: $1,530,000
      ═══════════════════════════════════
      PRECIO NUEVO: $27,600,000 ✅ (+$1.2M)

      nivel_2/CALE.n_1+.json
      ├─ $ref SALA-T-24q: $27,600,000 ← ACTUALIZADO
      ├─ $ref PISTA-P-C3: ...
      ├─ $ref PISTA-P-C2: ...
      └─ $ref PISTA-P-C1 ×4: ...
      ═══════════════════════════════════
      PRECIO NUEVO: $751,200,000 ✅ (+$1.2M)

   d) Genera JSONs para visores 3D/2D:
      - catalogo_bim_completo.json
      - nivel_0/*.json
      - nivel_1/*.json
      - configuraciones_cale.json

   e) Regenera TODAS las fichas técnicas HTML:
      - fichas/silla-erg-001.html ← Precio actualizado
      - (125 fichas actualizadas dinámicamente)

4️⃣ RESULTADO: TODO EL SISTEMA ACTUALIZADO
   ════════════════════════════════════════════════
   ✅ Precio atómico actualizado
   ✅ Cubículo recalculado (+$50K)
   ✅ Sala T-24q recalculada (+$1.2M)
   ✅ Centro CALE.n_1+ recalculado (+$1.2M)
   ✅ Todas las 141 configuraciones actualizadas
   ✅ Fichas técnicas HTML regeneradas
   ✅ Visor 3D con datos nuevos
   ✅ Visor 2D con datos nuevos
   ✅ Presupuesto general actualizado

5️⃣ DEPLOY A GITHUB PAGES
   ════════════════════════════════════════════════
   $ git add .
   $ git commit -m "data: Actualizar precio SILLA-ERG-001"
   $ git push

   → GitHub Pages reconstruye en 2 minutos
   → Usuario abre ficha técnica en navegador
   → HTML lee JSON dinámicamente
   → Muestra precio actualizado: $500,000 ✅
```

---

## 📄 FICHAS TÉCNICAS DINÁMICAS

### **Concepto Crítico: NO HAY DATOS HARDCODEADOS**

```html
<!-- fichas/silla-erg-001.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Ficha Técnica - SILLA-ERG-001</title>
</head>
<body>
    <div id="ficha-container">
        <h1 id="nombre-producto"></h1>
        <p><strong>Código:</strong> <span id="codigo"></span></p>
        <p><strong>Precio:</strong> <span id="precio"></span></p>
        <p><strong>Proveedor:</strong> <span id="proveedor"></span></p>
        <!-- ... más campos ... -->
    </div>

    <script type="module">
        // ❌ NO HARDCODEADO:
        // const precio = 450000;  // ← NUNCA HACER ESTO

        // ✅ DINÁMICO: Lee desde JSON
        const codigoProducto = 'SILLA-ERG-001';  // Del parámetro URL

        // Cargar datos desde catálogo BIM
        const catalogoResponse = await fetch('../datos_json/catalogo_atomicos.json');
        const catalogo = await catalogoResponse.json();

        // Buscar producto
        const producto = catalogo.productos.find(p => p.codigo === codigoProducto);

        if (producto) {
            // Llenar ficha DINÁMICAMENTE
            document.getElementById('nombre-producto').textContent = producto.nombre;
            document.getElementById('codigo').textContent = producto.codigo;
            document.getElementById('precio').textContent =
                `$${producto.capex_unitario.toLocaleString()}`;
            document.getElementById('proveedor').textContent = producto.proveedor;

            // ... todos los campos desde el JSON
        }
    </script>
</body>
</html>
```

**Ventajas:**
- ✅ Una sola ficha HTML sirve para 125 productos (con parámetro `?codigo=XXX`)
- ✅ Actualización en Google Sheets → Actualiza ficha automáticamente
- ✅ Sin mantenimiento manual de 125 HTMLs
- ✅ Coherencia garantizada (fuente única)

---

## 🗺️ MAPA INTERACTIVO

### **Hoja: `arquitectura_red_cale_nacional`**

**Datos actuales (INCOMPLETOS):**
```csv
centro_id,tipo_centro,municipio,departamento,categoria_cale,demanda_estimada
NODO_01,NODO_PRINCIPAL,BOGOTÁ,BOGOTÁ,Cat.A+,80453
```

**Datos REQUERIDOS (completar):**
```csv
centro_id,tipo_centro,municipio,departamento,latitud,longitud,codigo_dane,categoria_cale,demanda_estimada,nodo_principal
NODO_01,NODO_PRINCIPAL,BOGOTÁ,BOGOTÁ,4.649251,-74.106992,11001,CALE.n_1+,80453,NODO_01
```

**Campos a agregar:**
- `latitud`: Coordenada geográfica (decimal)
- `longitud`: Coordenada geográfica (decimal)
- `codigo_dane`: Código DANE del municipio
- Actualizar `categoria_cale`: Cat.A+ → CALE.n_1+

**Script de sincronización:**
```python
def sync_mapa_interactivo():
    """
    Lee: arquitectura_red_cale_nacional.csv
    Genera: ubicaciones_cale_141.json

    {
      "version": "5.3",
      "total_centros": 141,
      "centros": [
        {
          "id": "NODO_01",
          "tipo": "NODO_PRINCIPAL",
          "municipio": "BOGOTÁ",
          "departamento": "BOGOTÁ",
          "lat": 4.649251,
          "lng": -74.106992,
          "codigo_dane": "11001",
          "categoria": "CALE.n_1+",
          "demanda_anual": 80453,
          "nodo_padre": "NODO_01",
          "url_visor_3d": "visor_bim_3d.html?centro=NODO_01&cat=CALE.n_1+",
          "url_ficha": "fichas/centro_NODO_01.html",
          "color_marker": "#FF0000",  // Rojo para CALE.n_1+
          "popup_html": "..."
        },
        // ... 140 centros más
      ]
    }
    """
```

**Mapa Interactivo HTML:**
```html
<!-- mapa_cale.html -->
<script>
  // Cargar ubicaciones desde JSON
  const ubicacionesResponse = await fetch('datos/ubicaciones_cale_141.json');
  const ubicaciones = await ubicacionesResponse.json();

  // Crear mapa Leaflet
  const mapa = L.map('map').setView([4.6, -74.1], 6);

  // Colores por categoría CALE
  const colores = {
    'CALE.n_1+': '#FF0000',  // Rojo
    'CALE.n_1': '#FF6600',   // Naranja
    'CALE.n_2**': '#FFCC00', // Amarillo
    'CALE.n_2': '#00CC00',   // Verde
    'CALE.n_3': '#0066CC',   // Azul
    'CALE.C2': '#6600CC',    // Morado
    'CALE.C3': '#CC00CC'     // Magenta
  };

  // Crear marcadores
  ubicaciones.centros.forEach(centro => {
    const marker = L.circleMarker([centro.lat, centro.lng], {
      radius: 8,
      fillColor: colores[centro.categoria],
      color: '#fff',
      weight: 2,
      opacity: 1,
      fillOpacity: 0.8
    });

    // Popup con info + link a visor 3D
    marker.bindPopup(`
      <h3>${centro.municipio}</h3>
      <p><strong>Categoría:</strong> ${centro.categoria}</p>
      <p><strong>Demanda:</strong> ${centro.demanda_anual.toLocaleString()}</p>
      <a href="${centro.url_visor_3d}" target="_blank">Ver en Visor 3D →</a>
    `);

    marker.addTo(mapa);
  });
</script>
```

---

## 🎯 OBJETIVOS CORREGIDOS

### **OBJ-1: Visor 3D Funcional**
- ✅ Migrar a xeokit ES6 modules (CDN correcto)
- ✅ Cargar datos desde JSONs jerárquicos (nivel_0, nivel_1, nivel_2)
- ✅ Renderizar componentes BIM con referencias recursivas
- ✅ Navegación 3D (rotar, zoom, pan)

### **OBJ-2: Visor 2D Funcional**
- ✅ Fabric.js cargando planos desde JSONs
- ✅ Mostrar salas (SALA-T-24q, SALA-T-16q, etc.)
- ✅ Interactividad (click en elementos)

### **OBJ-3: Fichas Técnicas Dinámicas**
- ✅ Generar 125 fichas HTML desde `presupuesto_nivel_-1`
- ✅ **Columna O** populate con URL de ficha
- ✅ Fichas leen datos desde JSON (NO hardcodeado)
- ✅ Actualización automática al cambiar Google Sheets

### **OBJ-4: Mapa Interactivo Actualizado**
- ✅ Completar `arquitectura_red_cale_nacional` con lat/lng/DANE
- ✅ Actualizar nomenclatura Cat.X → CALE.n_X
- ✅ Generar JSON con 141 ubicaciones
- ✅ Marcadores con colores por categoría
- ✅ Links a visor 3D desde cada marcador

### **OBJ-5: Sistema Recursivo BIM**
- ✅ Referencias `$ref` funcionando
- ✅ Cálculo automático de precios en cascada
- ✅ Un cambio en atómico actualiza TODO el sistema
- ✅ Validación de integridad (125 atómicos → N configuraciones)

### **OBJ-6: Sincronización Google Sheets**
- ✅ Script unificado `sync_sistema_completo.py`
- ✅ Sincroniza 3 hojas:
  - `presupuesto_nivel_-1` → Fichas + Atómicos
  - `presupuesto_general` → Dashboards
  - `arquitectura_red_cale_nacional` → Mapa
- ✅ Genera todos los JSONs necesarios
- ✅ Actualiza nomenclatura CAT → CALE

---

## 📅 PLAN DE ACCIÓN

### **FASE 0: COMPLETAR GOOGLE SHEETS** ⭐ CRÍTICO

**Tarea 0.1: Completar `arquitectura_red_cale_nacional`**
- [ ] Agregar columna `latitud` (decimal, ej: 4.649251)
- [ ] Agregar columna `longitud` (decimal, ej: -74.106992)
- [ ] Agregar columna `codigo_dane` (5-6 dígitos, ej: 11001)
- [ ] Verificar/actualizar `nodo_principal` (referencia correcta)
- [ ] Actualizar `categoria_cale`:
  ```
  Cat.A+ → CALE.n_1+
  Cat.A → CALE.n_1
  Cat.B** → CALE.n_2**
  Cat.B → CALE.n_2
  Cat.C1 → CALE.n_3
  Cat.C2 → CALE.C2
  Cat.C3 → CALE.C3
  ```
- [ ] Exportar como CSV: `arquitectura_red_cale_nacional.csv`

**Tarea 0.2: Verificar `presupuesto_nivel_-1`**
- [ ] Confirmar 125 productos atómicos completos
- [ ] Verificar columna O "Ficha Técnica" existe
- [ ] Exportar como CSV: `presupuesto_nivel_-1.csv`

**Tarea 0.3: Verificar `presupuesto_general`**
- [ ] Confirmar presupuesto total consolidado
- [ ] Exportar como CSV: `presupuesto_general.csv`

---

### **FASE 1: SCRIPT DE SINCRONIZACIÓN** (3-4 horas)

**Tarea 1.1: Crear `sync_sistema_completo.py`**

```python
class SyncSistemaCompleto:
    def __init__(self):
        self.path_sheets = 'services/google_sheets/'
        self.path_output = 'bim_sncale/'

    def sync_atomicos_fichas(self):
        """Lee presupuesto_nivel_-1.csv → Genera:
        - atomicos/*.json (125 archivos)
        - fichas/*.html (125 fichas técnicas)
        - catalogo_atomicos.json (consolidado)
        """
        csv_path = f'{self.path_sheets}/presupuesto_nivel_-1.csv'
        productos = self.leer_csv(csv_path)

        for producto in productos:
            # Generar JSON atómico
            json_path = f'{self.path_output}/atomicos/{producto.codigo}.json'
            self.escribir_json(json_path, {
                'codigo': producto.codigo,
                'nombre': producto.nombre,
                'categoria_bim': producto.categoria,
                'clase_ifc': producto.clase_ifc,
                'capex_unitario': producto.capex,
                'opex_anual': producto.opex,
                'proveedor': producto.proveedor,
                'garantia': producto.garantia,
                'normativas': producto.normativas,
                'ficha_url': f'fichas/{producto.codigo.lower()}.html'
            })

            # Generar ficha HTML dinámica
            self.generar_ficha_html(producto)

            # Actualizar Columna O en Google Sheets
            producto.ficha_tecnica_url = f'https://sncale.../fichas/{producto.codigo.lower()}.html'

        print(f"✅ {len(productos)} atómicos sincronizados")

    def sync_mapa_interactivo(self):
        """Lee arquitectura_red_cale_nacional.csv → Genera:
        - ubicaciones_cale_141.json
        - mapa_markers.js
        """
        csv_path = f'{self.path_sheets}/arquitectura_red_cale_nacional.csv'
        centros = self.leer_csv(csv_path)

        # Actualizar nomenclatura
        for centro in centros:
            centro.categoria = self.actualizar_nomenclatura(centro.categoria)

        # Generar JSON para mapa
        json_mapa = {
            'version': '5.3',
            'fecha': datetime.now().isoformat(),
            'total_centros': len(centros),
            'centros': [self.centro_to_dict(c) for c in centros]
        }

        self.escribir_json('mapa_cale/datos/ubicaciones_cale_141.json', json_mapa)
        print(f"✅ {len(centros)} centros sincronizados para mapa")

    def calcular_jerarquia_recursiva(self):
        """Calcula precios en cascada:
        atomicos → nivel_0 → nivel_1 → nivel_2
        """
        # Cargar todos los atómicos
        atomicos = self.cargar_atomicos()

        # Calcular nivel_0 (cubículo, etc.)
        nivel_0 = self.calcular_nivel_0(atomicos)

        # Calcular nivel_1 (salas, pistas)
        nivel_1 = self.calcular_nivel_1(nivel_0, atomicos)

        # Calcular nivel_2+ (centros CALE completos)
        configuraciones = self.calcular_configuraciones_cale(nivel_1)

        print("✅ Jerarquía BIM recalculada")
        return configuraciones

    def ejecutar_sincronizacion_completa(self):
        print("🔄 Iniciando sincronización SNCALE MUNAY 5.3...")

        # 1. Atómicos y fichas
        self.sync_atomicos_fichas()

        # 2. Mapa interactivo
        self.sync_mapa_interactivo()

        # 3. Presupuesto general
        self.sync_presupuesto_general()

        # 4. Calcular jerarquía recursiva
        self.calcular_jerarquia_recursiva()

        # 5. Generar JSONs para visores
        self.generar_jsons_visores()

        # 6. Validar coherencia
        self.validar_sistema()

        print("🎉 Sincronización completa exitosa!")

# USO:
sync = SyncSistemaCompleto()
sync.ejecutar_sincronizacion_completa()
```

---

### **FASE 2: VISOR 3D XEOKIT** (2 horas)

**Tarea 2.1: Migrar a xeokit ES6**

```html
<!-- visor_bim_3d.html -->
<script type="module">
  import {Viewer, Mesh, PhongMaterial, BoxGeometry} from
    "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";

  // Cargar configuración del centro
  const params = new URLSearchParams(window.location.search);
  const centroId = params.get('centro') || 'NODO_01';
  const categoria = params.get('cat') || 'CALE.n_1+';

  // Cargar JSON de configuración
  const configResponse = await fetch(`datos/configuraciones/${categoria}.json`);
  const config = await configResponse.json();

  // Crear visor
  const viewer = new Viewer({
    canvasId: "canvas3d",
    transparent: true
  });

  // Renderizar componentes recursivamente
  function renderizarComponente(componente, posicion) {
    if (componente.$ref) {
      // Cargar componente referenciado
      const refPath = componente.$ref.replace('../', 'datos/');
      fetch(refPath).then(r => r.json()).then(subcomp => {
        renderizarComponente(subcomp, posicion);
      });
    } else {
      // Renderizar geometría directa
      new Mesh(viewer.scene, {
        id: componente.codigo,
        geometry: new BoxGeometry(viewer.scene, {
          xSize: componente.dimensiones.x,
          ySize: componente.dimensiones.y,
          zSize: componente.dimensiones.z
        }),
        material: new PhongMaterial(viewer.scene, {
          diffuse: hexToRgb(componente.color || '#CCCCCC')
        }),
        position: posicion
      });
    }
  }

  // Renderizar configuración completa
  config.composicion.subcomponentes.forEach((comp, i) => {
    renderizarComponente(comp, [i * 5, 0, 0]);
  });
</script>
```

---

### **FASE 3: FICHAS TÉCNICAS DINÁMICAS** (1.5 horas)

**Tarea 3.1: Template de ficha técnica**

```html
<!-- fichas/template.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title id="page-title">Ficha Técnica</title>
    <link rel="stylesheet" href="../assets/css/ficha-tecnica.css">
</head>
<body>
    <div class="ficha-container">
        <header class="ficha-header">
            <img src="../assets/img/logo-sncale.png" alt="SNCALE">
            <h1 id="producto-nombre"></h1>
            <p class="producto-codigo" id="producto-codigo"></p>
        </header>

        <section class="ficha-specs">
            <h2>Especificaciones Técnicas</h2>
            <table>
                <tr>
                    <th>Categoría BIM:</th>
                    <td id="spec-categoria"></td>
                </tr>
                <tr>
                    <th>Clase IFC:</th>
                    <td id="spec-ifc"></td>
                </tr>
                <tr>
                    <th>Unidad de Medida:</th>
                    <td id="spec-unidad"></td>
                </tr>
            </table>
        </section>

        <section class="ficha-costos">
            <h2>Costos</h2>
            <div class="costo-grid">
                <div class="costo-item">
                    <span class="costo-label">CAPEX Unitario</span>
                    <span class="costo-value" id="costo-capex"></span>
                </div>
                <div class="costo-item">
                    <span class="costo-label">OPEX Anual</span>
                    <span class="costo-value" id="costo-opex"></span>
                </div>
                <div class="costo-item">
                    <span class="costo-label">TCO 5 Años</span>
                    <span class="costo-value" id="costo-tco"></span>
                </div>
            </div>
        </section>

        <section class="ficha-proveedor">
            <h2>Información del Proveedor</h2>
            <p><strong>Proveedor Principal:</strong> <span id="proveedor"></span></p>
            <p><strong>Garantía:</strong> <span id="garantia"></span></p>
            <p><strong>Normativas:</strong> <span id="normativas"></span></p>
        </section>
    </div>

    <script type="module">
        // Obtener código del producto desde URL
        const params = new URLSearchParams(window.location.search);
        const codigoProducto = params.get('codigo');

        if (!codigoProducto) {
            alert('Código de producto no especificado');
        } else {
            // Cargar datos desde JSON
            const response = await fetch('../datos_json/catalogo_atomicos.json');
            const catalogo = await response.json();

            const producto = catalogo.productos.find(p =>
                p.codigo.toLowerCase() === codigoProducto.toLowerCase()
            );

            if (producto) {
                // Llenar ficha DINÁMICAMENTE
                document.title = `Ficha Técnica - ${producto.codigo}`;
                document.getElementById('page-title').textContent =
                    `Ficha Técnica - ${producto.codigo}`;
                document.getElementById('producto-nombre').textContent =
                    producto.nombre;
                document.getElementById('producto-codigo').textContent =
                    producto.codigo;
                document.getElementById('spec-categoria').textContent =
                    producto.categoria_bim;
                document.getElementById('spec-ifc').textContent =
                    producto.clase_ifc;
                document.getElementById('spec-unidad').textContent =
                    producto.unidad_medida;
                document.getElementById('costo-capex').textContent =
                    `$${producto.capex_unitario.toLocaleString()}`;
                document.getElementById('costo-opex').textContent =
                    `$${producto.opex_anual.toLocaleString()}`;
                document.getElementById('costo-tco').textContent =
                    `$${producto.tco_5_anos.toLocaleString()}`;
                document.getElementById('proveedor').textContent =
                    producto.proveedor_principal;
                document.getElementById('garantia').textContent =
                    producto.garantia;
                document.getElementById('normativas').textContent =
                    producto.normativas;
            } else {
                alert(`Producto ${codigoProducto} no encontrado`);
            }
        }
    </script>
</body>
</html>
```

**USO:**
```
https://sncale.../fichas/template.html?codigo=SILLA-ERG-001
https://sncale.../fichas/template.html?codigo=MESA-CUB-001
https://sncale.../fichas/template.html?codigo=LED-STRIP-12W
```

---

### **FASE 4: MAPA INTERACTIVO** (1.5 horas)

**Tarea 4.1: Actualizar mapa_cale.html**

```html
<!-- mapa_cale.html -->
<script>
  // Cargar ubicaciones desde JSON
  const ubicacionesResponse = await fetch('datos/ubicaciones_cale_141.json');
  const ubicaciones = await ubicacionesResponse.json();

  console.log(`✅ ${ubicaciones.total_centros} centros cargados`);

  // Crear mapa
  const mapa = L.map('map').setView([4.6, -74.1], 6);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(mapa);

  // Colores por categoría CALE.n_X
  const coloresCategorias = {
    'CALE.n_1+': '#FF0000',
    'CALE.n_1': '#FF6600',
    'CALE.n_2**': '#FFCC00',
    'CALE.n_2': '#00CC00',
    'CALE.n_3': '#0066CC',
    'CALE.C2': '#6600CC',
    'CALE.C3': '#CC00CC'
  };

  // Crear marcadores
  ubicaciones.centros.forEach(centro => {
    const marker = L.circleMarker([centro.lat, centro.lng], {
      radius: 8,
      fillColor: coloresCategorias[centro.categoria],
      color: '#fff',
      weight: 2,
      opacity: 1,
      fillOpacity: 0.8
    });

    // Popup dinámico
    const popupHTML = `
      <div class="popup-centro">
        <h3>${centro.municipio}</h3>
        <p><strong>Departamento:</strong> ${centro.departamento}</p>
        <p><strong>Categoría:</strong> ${centro.categoria}</p>
        <p><strong>Tipo:</strong> ${centro.tipo}</p>
        <p><strong>Demanda anual:</strong> ${centro.demanda_anual.toLocaleString()}</p>
        <p><strong>Código DANE:</strong> ${centro.codigo_dane}</p>
        <hr>
        <a href="${centro.url_visor_3d}" target="_blank" class="btn-visor">
          Ver en Visor 3D →
        </a>
        <a href="${centro.url_ficha}" target="_blank" class="btn-ficha">
          Ficha del Centro →
        </a>
      </div>
    `;

    marker.bindPopup(popupHTML);
    marker.addTo(mapa);
  });

  // Leyenda
  const leyenda = L.control({ position: 'bottomright' });
  leyenda.onAdd = function() {
    const div = L.DomUtil.create('div', 'leyenda');
    div.innerHTML = '<h4>Categorías CALE</h4>';

    Object.entries(coloresCategorias).forEach(([cat, color]) => {
      div.innerHTML += `
        <div class="leyenda-item">
          <span class="leyenda-color" style="background: ${color}"></span>
          <span>${cat}</span>
        </div>
      `;
    });

    return div;
  };
  leyenda.addTo(mapa);
</script>
```

---

## ✅ CHECKLIST FINAL

### **Preparación Google Sheets**
- [ ] Completar `arquitectura_red_cale_nacional` (lat/lng/DANE)
- [ ] Actualizar nomenclatura Cat.X → CALE.n_X
- [ ] Verificar `presupuesto_nivel_-1` (125 productos)
- [ ] Exportar 3 CSVs

### **Script de Sincronización**
- [ ] Crear `sync_sistema_completo.py`
- [ ] Implementar `sync_atomicos_fichas()`
- [ ] Implementar `sync_mapa_interactivo()`
- [ ] Implementar `calcular_jerarquia_recursiva()`
- [ ] Tests unitarios

### **Visor 3D**
- [ ] Migrar a xeokit ES6 modules
- [ ] Cargar JSONs jerárquicos
- [ ] Renderizar componentes recursivamente
- [ ] Controles de cámara

### **Fichas Técnicas**
- [ ] Template HTML dinámico
- [ ] Cargar datos desde JSON
- [ ] Generar 125 fichas con parámetro `?codigo=XXX`
- [ ] Actualizar Columna O en Google Sheets

### **Mapa Interactivo**
- [ ] Cargar `ubicaciones_cale_141.json`
- [ ] Marcadores con colores por categoría
- [ ] Popups con links a visor 3D
- [ ] Leyenda de categorías

### **Deployment**
- [ ] Commit a GitHub
- [ ] Push a GitHub Pages
- [ ] Verificar todo funciona

---

## 🚀 COMANDO ÚNICO PARA ACTUALIZAR TODO

```bash
# 1. Exportar Google Sheets como CSV (manual)

# 2. Ejecutar sincronización completa
python services/google_sheets/sync_sistema_completo.py

# Salida esperada:
# 🔄 Iniciando sincronización SNCALE MUNAY 5.3...
# ✅ 125 atómicos sincronizados
# ✅ 125 fichas técnicas generadas
# ✅ 141 centros sincronizados para mapa
# ✅ Presupuesto general consolidado
# ✅ Jerarquía BIM recalculada
#    - nivel_0: 15 componentes
#    - nivel_1: 25 espacios
#    - nivel_2+: 7 configuraciones CALE
# ✅ JSONs para visores generados
# ✅ Coherencia del sistema validada
# 🎉 Sincronización completa exitosa!

# 3. Deploy
git add .
git commit -m "data: Sincronización completa desde Google Sheets"
git push origin main
```

---

**FIN DEL DOCUMENTO**

**Versión:** 4.0 CORREGIDA
**Fecha:** 2025-10-29
**Estado:** ✅ ARQUITECTURA REAL DOCUMENTADA
