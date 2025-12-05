# 🎯 ESTRATEGIA FINAL: GOOGLE SHEETS COMO ÚNICA FUENTE DE VERDAD

**Fecha:** 2025-10-29
**Estado:** ✅ ESTRATEGIA DEFINIDA
**Principio:** Zero Intermediate Files - Lectura directa desde Google Sheets

---

## 📊 DATOS EXISTENTES CONFIRMADOS

### ✅ **Archivos locales con datos completos:**

1. **`MUNAY_5.3__ESCENARIO_2_PRESUPUESTO_141__LISTADO_TODOS_CENTROS.csv`**
   - ✅ 141 centros CALE
   - ✅ Columnas: centro_id, tipo_centro, codigo_dane, municipio, departamento
   - ✅ **latitud, longitud** (coordenadas geográficas)
   - ✅ **categoria_cale** (Cat.A+, Cat.A, Cat.B**, etc.)
   - ✅ **nodo_principal** (YA CALCULADO con distancias viales)
   - ✅ **distancia_maxima_km, distancia_promedio_km** (distancias reales por carretera)
   - ✅ total_municipios_cluster

2. **`services/github_pages/data/nodos_cale_197_MUNAY53.json`**
   - ✅ 197 nodos (141 principales + 56 satélites adicionales)
   - ✅ Formato JSON listo para consumo
   - ✅ Incluye referencias a nodo_principal

### ⚠️ **Dato faltante confirmado:**
- Columna `nodo_principal` en CSV muestra **nombre del municipio** en vez de **centro_id**
- Ejemplo: `"nodo_principal": "BOGOTÁ, D.C."` en vez de `"nodo_principal": "NODO_01"`

**Solución:** Script de mapeo municipio → centro_id

---

## 🏗️ ARQUITECTURA DEFINITIVA

```
┌─────────────────────────────────────────────────────────────────┐
│         GOOGLE SHEETS (Fuente Única de Verdad)                  │
│  https://docs.google.com/spreadsheets/d/1ibTlTyA.../            │
│                                                                 │
│  📍 Hoja: arquitectura_red_cale_nacional                        │
│  ════════════════════════════════════════════════════════       │
│                                                                 │
│  Datos a IMPORTAR desde CSV existente:                         │
│  ├─ centro_id (NODO_01, NODO_02, SAT_001, ...)                 │
│  ├─ tipo_centro (NODO_PRINCIPAL, SATÉLITE)                     │
│  ├─ codigo_dane (1111001, 6868001, ...)                        │
│  ├─ municipio (BOGOTÁ, Bucaramanga, ...)                       │
│  ├─ departamento (BOGOTÁ D.C., SANTANDER, ...)                 │
│  ├─ latitud (4.649251, 7.11647, ...)                           │
│  ├─ longitud (-74.106992, -73.132562, ...)                     │
│  ├─ categoria_cale (Cat.A+ → CALE.n_1+) ⬅️ ACTUALIZAR          │
│  ├─ demanda_estimada_anual (80453, 68000, ...)                 │
│  ├─ nodo_principal (NODO_01, NODO_03, ...) ⬅️ MAPEAR           │
│  ├─ codigo_dane_nodo (1111001, 6868001, ...)                   │
│  ├─ total_municipios_cluster (7, 14, ...)                      │
│  ├─ distancia_maxima_km (51.47, 33.24, ...)                    │
│  └─ distancia_promedio_km (29.3, 19.35, ...)                   │
│                                                                 │
│  🔧 ACCIONES REQUERIDAS:                                        │
│  1. Importar datos desde CSV ✅                                 │
│  2. Actualizar categoria_cale (Cat.X → CALE.n_X) ✅ YA HECHO   │
│  3. Mapear nodo_principal (municipio → centro_id) ⬅️ PENDIENTE │
│  4. Publicar como CSV público ⬅️ PENDIENTE                     │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ ⚡ Publicar en la web
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│  URL PÚBLICA (sin autenticación, CORS habilitado)               │
│                                                                 │
│  https://docs.google.com/spreadsheets/d/                        │
│    1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/                │
│    export?format=csv&gid=197105959                             │
│                                                                 │
│  ✅ Actualización en tiempo real                                │
│  ✅ Caché controlable                                           │
│  ✅ Accesible desde JavaScript                                  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ fetch() directo
                     ▼
    ┌────────────────┴──────────────┐
    │                               │
    ▼                               ▼
┌─────────────┐              ┌─────────────┐
│ Mapa HTML   │              │ Visor 3D    │
│             │              │             │
│ Lee Sheets  │              │ Lee Sheets  │
│ Renderiza   │              │ Renderiza   │
└─────────────┘              └─────────────┘
```

---

## 🔧 PASO 1: IMPORTAR DATOS A GOOGLE SHEETS

### **Método A: Copiar y Pegar desde CSV**

```bash
# 1. Abrir CSV en Excel/Google Sheets
Archivo CSV: MUNAY_5.3__ESCENARIO_2_PRESUPUESTO_141__LISTADO_TODOS_CENTROS.csv

# 2. Seleccionar TODAS las filas y columnas (Ctrl+A)

# 3. Copiar (Ctrl+C)

# 4. Ir a Google Sheets → arquitectura_red_cale_nacional

# 5. Pegar en celda A1 (Ctrl+V)

# 6. Verificar que las columnas están correctas
```

### **Método B: Importar CSV a Google Sheets**

```
1. Abrir Google Sheets
2. Archivo → Importar
3. Cargar → Seleccionar archivo CSV
4. Opciones:
   - Ubicación de importación: Reemplazar hoja actual
   - Tipo de separador: Detectar automáticamente
   - Convertir texto a números y fechas: ✅
5. Importar datos
```

---

## 🔧 PASO 2: MAPEAR `nodo_principal` (Municipio → centro_id)

**Problema actual:**
```csv
nodo_principal
"BOGOTÁ, D.C."    ❌ Es el nombre del municipio
Bucaramanga       ❌ Es el nombre del municipio
```

**Necesitamos:**
```csv
nodo_principal
NODO_01          ✅ Es el centro_id
NODO_03          ✅ Es el centro_id
```

### **Script de mapeo:**

```python
# scripts/mapear_nodo_principal.py

import pandas as pd

# ═══════════════════════════════════════════════════════════════
# CARGAR DATOS
# ═══════════════════════════════════════════════════════════════

csv_path = 'MUNAY_5.3__ESCENARIO_2_PRESUPUESTO_141__LISTADO_TODOS_CENTROS.csv'
df = pd.read_csv(csv_path)

print(f"✅ {len(df)} centros cargados")

# ═══════════════════════════════════════════════════════════════
# CREAR DICCIONARIO: municipio → centro_id
# ═══════════════════════════════════════════════════════════════

# Crear mapeo de todos los NODOS PRINCIPALES (HUBs)
nodos_principales = df[df['tipo_centro'] == 'NODO_PRINCIPAL'].copy()

# Diccionario: municipio → centro_id
mapa_municipio_a_centro = {}

for _, row in nodos_principales.iterrows():
    municipio = row['municipio'].strip()
    centro_id = row['centro_id'].strip()

    # Guardar mapeo
    mapa_municipio_a_centro[municipio] = centro_id

    # También agregar variaciones comunes
    # "BOGOTÁ, D.C." → "BOGOTÁ"
    if ',' in municipio:
        municipio_corto = municipio.split(',')[0].strip()
        mapa_municipio_a_centro[municipio_corto] = centro_id

print(f"✅ {len(mapa_municipio_a_centro)} mapeos creados")

# ═══════════════════════════════════════════════════════════════
# APLICAR MAPEO
# ═══════════════════════════════════════════════════════════════

def mapear_nodo(nodo_actual):
    """
    Convierte nombre de municipio a centro_id
    """
    if pd.isna(nodo_actual) or nodo_actual == '':
        return ''

    nodo_str = str(nodo_actual).strip()

    # Si ya es un centro_id (formato NODO_XX o SAT_XXX), dejar igual
    if nodo_str.startswith('NODO_') or nodo_str.startswith('SAT_'):
        return nodo_str

    # Buscar en el diccionario
    if nodo_str in mapa_municipio_a_centro:
        return mapa_municipio_a_centro[nodo_str]

    # Buscar sin el sufijo ", D.C." o similar
    if ',' in nodo_str:
        nodo_corto = nodo_str.split(',')[0].strip()
        if nodo_corto in mapa_municipio_a_centro:
            return mapa_municipio_a_centro[nodo_corto]

    # Si no encuentra, dejar el original
    print(f"⚠️ No se pudo mapear: {nodo_str}")
    return nodo_str

# Aplicar mapeo
df['nodo_principal_mapeado'] = df['nodo_principal'].apply(mapear_nodo)

# ═══════════════════════════════════════════════════════════════
# VERIFICAR RESULTADOS
# ═══════════════════════════════════════════════════════════════

print("\n📊 ANTES vs DESPUÉS:")
print(df[['centro_id', 'municipio', 'nodo_principal', 'nodo_principal_mapeado']].head(20))

# Contar cuántos se mapearon correctamente
mapeados_correctos = df['nodo_principal_mapeado'].str.startswith('NODO_').sum()
print(f"\n✅ {mapeados_correctos}/{len(df)} nodos mapeados correctamente")

# ═══════════════════════════════════════════════════════════════
# REEMPLAZAR COLUMNA
# ═══════════════════════════════════════════════════════════════

df['nodo_principal'] = df['nodo_principal_mapeado']
df.drop(columns=['nodo_principal_mapeado'], inplace=True)

# ═══════════════════════════════════════════════════════════════
# EXPORTAR
# ═══════════════════════════════════════════════════════════════

output_file = 'arquitectura_red_cale_nacional_MAPEADO.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n✅ Archivo guardado: {output_file}")
print("\n📋 PRÓXIMOS PASOS:")
print("1. Abre el archivo CSV generado")
print("2. Importa a Google Sheets (arquitectura_red_cale_nacional)")
print("3. Verifica que la columna 'nodo_principal' tiene centro_id (NODO_XX)")
```

---

## 🔧 PASO 3: ACTUALIZAR NOMENCLATURA (Ya hecho ✅)

**Confirmado:** Ya actualizaste `categoria_cale` de Cat.X → CALE.n_X

Si falta actualizar en el CSV local:

```python
# scripts/actualizar_nomenclatura.py

import pandas as pd

MAPPING = {
    'Cat.A+': 'CALE.n_1+',
    'Cat.A': 'CALE.n_1',
    'Cat.B**': 'CALE.n_2**',
    'Cat.B': 'CALE.n_2',
    'Cat.C1': 'CALE.n_3',
    'Cat.C2': 'CALE.C2',
    'Cat.C3': 'CALE.C3',
    'Cat.C4': 'CALE.C4',
    'Cat.C5': 'CALE.C5'
}

df = pd.read_csv('arquitectura_red_cale_nacional_MAPEADO.csv')

df['categoria_cale'] = df['categoria_cale'].replace(MAPPING)

df.to_csv('arquitectura_red_cale_nacional_FINAL.csv', index=False, encoding='utf-8-sig')

print("✅ Nomenclatura actualizada")
```

---

## 🔧 PASO 4: PUBLICAR GOOGLE SHEETS COMO CSV PÚBLICO

### **Instrucciones paso a paso:**

```
1. Abrir Google Sheets
   https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit

2. Seleccionar la hoja "arquitectura_red_cale_nacional"

3. Archivo → Compartir → Publicar en la web

4. Opciones:
   - Enlace: Hoja específica (arquitectura_red_cale_nacional)
   - Formato: Valores separados por comas (.csv)
   - ✅ Publicar automáticamente al hacer cambios
   - ✅ Publicar ahora

5. Copiar URL generada:
   https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/export?format=csv&gid=197105959
```

**URL resultante:**
```
https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/export?format=csv&gid=197105959
```

**Características:**
- ✅ Pública (sin autenticación)
- ✅ CORS habilitado automáticamente
- ✅ Actualización automática al editar Sheet
- ✅ Cache de ~5 minutos en Google

---

## 🗺️ PASO 5: MAPA INTERACTIVO (Lectura directa desde Sheets)

```html
<!-- mapa_cale.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mapa CALE - SNCALE MUNAY 5.3</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        body { margin: 0; padding: 0; font-family: Arial, sans-serif; }
        #map { width: 100%; height: 100vh; }
        .leyenda {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        .leyenda h4 {
            margin: 0 0 10px 0;
            font-size: 14px;
            color: #333;
        }
        .leyenda-item {
            display: flex;
            align-items: center;
            margin: 5px 0;
            font-size: 12px;
        }
        .leyenda-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 8px;
            border: 2px solid #fff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div id="map"></div>

    <script type="module">
        // ═══════════════════════════════════════════════════════════════
        // CONFIGURACIÓN
        // ═══════════════════════════════════════════════════════════════
        const GOOGLE_SHEETS_URL = 'https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/export?format=csv&gid=197105959';

        const COLORES_CATEGORIAS = {
            'CALE.n_1+': '#DC143C',  // Rojo carmesí
            'CALE.n_1': '#FF6347',   // Tomate
            'CALE.n_2**': '#FFD700', // Dorado
            'CALE.n_2': '#FFA500',   // Naranja
            'CALE.n_3': '#4169E1',   // Azul real
            'CALE.C2': '#8A2BE2',    // Violeta azulado
            'CALE.C3': '#9370DB',    // Púrpura medio
            'CALE.C4': '#BA55D3',    // Orquídea medio
            'CALE.C5': '#808080'     // Gris
        };

        // ═══════════════════════════════════════════════════════════════
        // PARSER CSV
        // ═══════════════════════════════════════════════════════════════
        function parseCSV(csvText) {
            const lines = csvText.trim().split('\n');
            const headers = lines[0].split(',').map(h => h.replace(/["\ufeff]/g, '').trim());

            return lines.slice(1).map(line => {
                // Parser mejorado para manejar campos con comas dentro de comillas
                const values = [];
                let currentValue = '';
                let insideQuotes = false;

                for (let char of line) {
                    if (char === '"') {
                        insideQuotes = !insideQuotes;
                    } else if (char === ',' && !insideQuotes) {
                        values.push(currentValue.trim());
                        currentValue = '';
                    } else {
                        currentValue += char;
                    }
                }
                values.push(currentValue.trim());

                const obj = {};
                headers.forEach((header, i) => {
                    obj[header] = values[i] || '';
                });
                return obj;
            });
        }

        // ═══════════════════════════════════════════════════════════════
        // CARGAR DATOS DESDE GOOGLE SHEETS
        // ═══════════════════════════════════════════════════════════════
        async function cargarCentrosCALE() {
            try {
                console.log('🔄 Cargando centros desde Google Sheets...');

                const response = await fetch(GOOGLE_SHEETS_URL);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }

                const csvText = await response.text();
                const centros = parseCSV(csvText);

                console.log(`✅ ${centros.length} centros cargados`);
                return centros;

            } catch (error) {
                console.error('❌ Error cargando datos:', error);
                alert(`Error cargando mapa: ${error.message}\n\nVerifica la conexión o URL de Google Sheets.`);
                return [];
            }
        }

        // ═══════════════════════════════════════════════════════════════
        // INICIALIZAR MAPA
        // ═══════════════════════════════════════════════════════════════
        const mapa = L.map('map').setView([4.6, -74.1], 6);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap | SNCALE MUNAY 5.3',
            maxZoom: 18
        }).addTo(mapa);

        // ═══════════════════════════════════════════════════════════════
        // RENDERIZAR CENTROS
        // ═══════════════════════════════════════════════════════════════
        const centros = await cargarCentrosCALE();

        centros.forEach(centro => {
            const lat = parseFloat(centro.latitud);
            const lng = parseFloat(centro.longitud);

            // Validar coordenadas
            if (isNaN(lat) || isNaN(lng)) {
                console.warn(`⚠️ Centro ${centro.centro_id} sin coordenadas válidas`);
                return;
            }

            const color = COLORES_CATEGORIAS[centro.categoria_cale] || '#999999';

            // Determinar radio según tipo
            const radius = centro.tipo_centro === 'NODO_PRINCIPAL' ? 10 : 6;

            // Crear marcador
            const marker = L.circleMarker([lat, lng], {
                radius: radius,
                fillColor: color,
                color: '#fff',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.85
            });

            // Popup con información completa
            const demanda = parseInt(centro.demanda_estimada_anual || 0);
            const distMax = parseFloat(centro.distancia_maxima_km || 0);
            const distProm = parseFloat(centro.distancia_promedio_km || 0);

            const popupHTML = `
                <div style="min-width: 280px; font-family: Arial, sans-serif;">
                    <h3 style="margin: 0 0 10px 0; color: #333; font-size: 16px;">
                        ${centro.municipio}
                    </h3>
                    <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Centro:</strong></td>
                            <td style="padding: 5px 0;">${centro.centro_id}</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Departamento:</strong></td>
                            <td style="padding: 5px 0;">${centro.departamento}</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Categoría:</strong></td>
                            <td style="padding: 5px 0;">
                                <span style="background: ${color}; color: white; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">
                                    ${centro.categoria_cale}
                                </span>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Tipo:</strong></td>
                            <td style="padding: 5px 0;">${centro.tipo_centro}</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Demanda anual:</strong></td>
                            <td style="padding: 5px 0;"><strong>${demanda.toLocaleString()}</strong></td>
                        </tr>
                        ${centro.nodo_principal ? `
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Nodo HUB:</strong></td>
                            <td style="padding: 5px 0;">${centro.nodo_principal}</td>
                        </tr>` : ''}
                        ${distMax > 0 ? `
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Dist. máx:</strong></td>
                            <td style="padding: 5px 0;">${distMax.toFixed(1)} km</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Dist. prom:</strong></td>
                            <td style="padding: 5px 0;">${distProm.toFixed(1)} km</td>
                        </tr>` : ''}
                        <tr>
                            <td style="padding: 5px 10px 5px 0; color: #666;"><strong>Municipios:</strong></td>
                            <td style="padding: 5px 0;">${centro.total_municipios_cluster || '1'}</td>
                        </tr>
                    </table>
                    <hr style="margin: 10px 0; border: none; border-top: 1px solid #eee;">
                    <div style="text-align: center;">
                        <a href="visor_bim_3d.html?centro=${centro.centro_id}&cat=${centro.categoria_cale}"
                           target="_blank"
                           style="display: inline-block; background: #0066CC; color: white; padding: 8px 16px; text-decoration: none; border-radius: 6px; font-size: 13px; margin: 5px;">
                            🔍 Ver Visor 3D
                        </a>
                        <a href="fichas/centro.html?codigo=${centro.centro_id}"
                           target="_blank"
                           style="display: inline-block; background: #00AA00; color: white; padding: 8px 16px; text-decoration: none; border-radius: 6px; font-size: 13px; margin: 5px;">
                            📄 Ficha Centro
                        </a>
                    </div>
                </div>
            `;

            marker.bindPopup(popupHTML, {
                maxWidth: 320,
                className: 'popup-cale'
            });

            marker.addTo(mapa);
        });

        console.log(`✅ ${centros.length} marcadores agregados al mapa`);

        // ═══════════════════════════════════════════════════════════════
        // LEYENDA
        // ═══════════════════════════════════════════════════════════════
        const leyenda = L.control({ position: 'bottomright' });

        leyenda.onAdd = function() {
            const div = L.DomUtil.create('div', 'leyenda');
            div.innerHTML = '<h4>Categorías CALE (MUNAY 5.3)</h4>';

            Object.entries(COLORES_CATEGORIAS).forEach(([cat, color]) => {
                div.innerHTML += `
                    <div class="leyenda-item">
                        <div class="leyenda-color" style="background: ${color};"></div>
                        <span>${cat}</span>
                    </div>
                `;
            });

            return div;
        };

        leyenda.addTo(mapa);

        // ═══════════════════════════════════════════════════════════════
        // CONTROLES ADICIONALES
        // ═══════════════════════════════════════════════════════════════

        // Botón para recargar datos
        const btnRefresh = L.control({ position: 'topright' });

        btnRefresh.onAdd = function() {
            const div = L.DomUtil.create('div');
            div.innerHTML = `
                <button onclick="location.reload()"
                        style="background: #0066CC; color: white; border: none; padding: 10px 15px; border-radius: 6px; cursor: pointer; font-size: 13px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
                    🔄 Actualizar datos
                </button>
            `;
            return div;
        };

        btnRefresh.addTo(mapa);

        // Mostrar total de centros
        const info = L.control({ position: 'topleft' });

        info.onAdd = function() {
            const div = L.DomUtil.create('div', 'info');
            div.style.cssText = 'background: white; padding: 10px 15px; border-radius: 6px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);';
            div.innerHTML = `
                <h4 style="margin: 0; font-size: 14px;">SNCALE MUNAY 5.3</h4>
                <p style="margin: 5px 0 0 0; font-size: 13px; color: #666;">
                    <strong>${centros.length}</strong> centros CALE
                </p>
            `;
            return div;
        };

        info.addTo(mapa);
    </script>
</body>
</html>
```

---

## ✅ RESUMEN DE LA ESTRATEGIA

### **PASOS A SEGUIR:**

1. **✅ Ejecutar scripts de preparación**
   ```bash
   # Mapear nodo_principal (municipio → centro_id)
   python scripts/mapear_nodo_principal.py

   # Actualizar nomenclatura (Cat.X → CALE.n_X) - YA HECHO
   python scripts/actualizar_nomenclatura.py
   ```

2. **✅ Importar a Google Sheets**
   - Abrir `arquitectura_red_cale_nacional_FINAL.csv`
   - Importar a Google Sheets (Archivo → Importar)
   - Verificar datos correctos

3. **✅ Publicar como CSV público**
   - Archivo → Compartir → Publicar en la web
   - Seleccionar hoja específica
   - Formato: CSV
   - Copiar URL pública

4. **✅ Actualizar HTML con URL de Sheets**
   - Reemplazar `GOOGLE_SHEETS_URL` en `mapa_cale.html`
   - Deploy a GitHub Pages

5. **✅ Verificar funcionamiento**
   - Abrir mapa en navegador
   - Verificar que carga los 141 centros
   - Probar clicks en marcadores
   - Verificar popups con datos correctos

---

### **VENTAJAS DE ESTA ESTRATEGIA:**

✅ **Cero archivos intermedios**
- No más CSVs locales desactualizados
- No más sincronización manual

✅ **Google Sheets = Fuente única**
- Cambio en Sheet → Recarga página → Ve cambio inmediato
- Un solo punto de edición

✅ **Datos viales reales**
- `distancia_maxima_km`, `distancia_promedio_km` calculados con red vial
- No solo distancia lineal (coordenadas)

✅ **Mantenimiento mínimo**
- Sin scripts de sincronización periódicos
- Sin commits de datos a Git

✅ **Performance optimizada**
- Caché de 5 min en Google
- Parsing rápido de CSV en cliente

---

**Fecha:** 2025-10-29
**Estado:** ✅ ESTRATEGIA LISTA PARA IMPLEMENTAR
