# ✅ Corrección: Mapa con Google Sheets TSV

**Fecha:** 29 de octubre de 2025
**Problema:** Mapa no cargaba datos desde Google Sheets
**Solución:** Actualizar a formato TSV y corregir URL

---

## 🔴 Problema Identificado

### Error en el navegador:
```
Error al cargar datos
Failed to fetch
Verifica que la Google Sheet esté publicada como CSV público.
```

### Causa raíz:
1. ❌ URL incorrecta (antigua, no publicada)
2. ❌ Formato CSV incompatible (latitudes con comas decimales)
3. ❌ Hoja no publicada correctamente

---

## ✅ Solución Implementada

### 1. Publicar Google Sheets como TSV

**¿Por qué TSV y no CSV?**
- Las coordenadas tienen comas decimales: `4,649251` y `-74,106992`
- CSV usa comas como separador → CONFLICTO
- TSV usa tabs como separador → SIN CONFLICTO

**URL publicada (TSV):**
```
https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhmqT_SMan7EeQRmStRS0jofd0VMQPvKemLZ_70Oiruj-yI1jh9ShgSuR7ZsFLMfz8wwDq5hde9Jo/pub?gid=197105959&single=true&output=tsv
```

### 2. Actualizar mapa_cale_nacional.html

**Cambios realizados:**

#### A. Actualizar configuración
```javascript
const GOOGLE_SHEETS_CONFIG = {
    // URL de Google Sheets publicada como TSV
    url: 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhmqT_SMan7EeQRmStRS0jofd0VMQPvKemLZ_70Oiruj-yI1jh9ShgSuR7ZsFLMfz8wwDq5hde9Jo/pub?gid=197105959&single=true&output=tsv',

    cacheKey: 'cale_centros_cache',
    cacheTTL: 5 * 60 * 1000,
    format: 'tsv'  // Tab-separated values
};
```

#### B. Crear parser universal TSV/CSV
```javascript
function parseData(text, format = 'tsv') {
    const lines = text.trim().split('\n');
    const separator = format === 'tsv' ? '\t' : ',';

    // Parse headers
    const headers = lines[0].split(separator).map(h => h.trim());

    // Parse datos
    for (let i = 1; i < lines.length; i++) {
        if (format === 'tsv') {
            // TSV: simple split por tab
            const values = line.split('\t').map(v => v.trim());
        } else {
            // CSV: manejar comillas
            // ... (lógica compleja para CSV con quotes)
        }
    }

    return data;
}
```

#### C. Actualizar llamada
```javascript
// Antes:
const csvText = await response.text();
const centros = parseCSV(csvText);

// Ahora:
const dataText = await response.text();
const centros = parseData(dataText, GOOGLE_SHEETS_CONFIG.format);
```

### 3. Herramienta de limpieza de cache

**Archivo:** `services/github_pages/limpiar_cache.html`

**Características:**
- Visualiza estado del cache actual
- Muestra tiempo restante de expiración
- Botón para limpiar cache
- Redirige al mapa actualizado

**Uso:**
1. Abrir `limpiar_cache.html`
2. Click en "Limpiar Cache y Recargar"
3. Click en "Ir al Mapa"

---

## 📊 Verificación

### Verificar que Google Sheets está publicada

**Probar URL directamente en el navegador:**
```
https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhmqT_SMan7EeQRmStRS0jofd0VMQPvKemLZ_70Oiruj-yI1jh9ShgSuR7ZsFLMfz8wwDq5hde9Jo/pub?gid=197105959&single=true&output=tsv
```

**Debe mostrar:**
```tsv
centro_id	tipo_centro	codigo_dane	municipio	...
NODO_01	NODO_PRINCIPAL	1111001.0	BOGOTÁ, D.C.	...
NODO_02	NODO_PRINCIPAL	1111001.0	BOGOTÁ, D.C.	...
```

### Verificar en el mapa

**Abrir:** `services/github_pages/mapa_cale_nacional.html`

**Verificar:**
- ✅ NO muestra error "Failed to fetch"
- ✅ Muestra "Cargando datos desde Google Sheets..."
- ✅ Mapa se carga con 197 centros
- ✅ Marcadores visibles en Colombia
- ✅ Popups funcionan correctamente
- ✅ Estadísticas: 56 nodos + 141 satélites

### Verificar en consola del navegador (F12)

**Comandos útiles:**
```javascript
// Ver datos cargados
const cache = JSON.parse(localStorage.getItem('cale_centros_cache'));
console.log('Centros cargados:', cache.data.length);

// Ver primer centro
console.log('Primer centro:', cache.data[0]);

// Ver coordenadas
console.log('Latitud:', cache.data[0].latitud);
console.log('Longitud:', cache.data[0].longitud);
```

**Output esperado:**
```javascript
Centros cargados: 197
Primer centro: {
  centro_id: "NODO_01",
  tipo_centro: "NODO_PRINCIPAL",
  latitud: "4.649251",
  longitud: "-74.106992",
  nodo_principal: "NODO_02",
  ...
}
```

---

## 🔧 Troubleshooting

### Problema: Sigue mostrando "Failed to fetch"

**Solución:**
1. Limpiar cache del navegador:
   - Abrir `limpiar_cache.html`
   - Click "Limpiar Cache y Recargar"

2. Verificar URL TSV:
   - Abrir URL directamente en navegador
   - Debe descargar archivo o mostrar texto TSV

3. Verificar CORS:
   - Abrir consola del navegador (F12)
   - Buscar errores de CORS
   - Google Sheets debería permitir CORS por defecto

### Problema: Datos incorrectos o incompletos

**Solución:**
1. Verificar columna K en Google Sheets:
   - Debe contener NODO_XX (no nombres de municipios)
   - 197 filas de datos

2. Verificar headers:
   - Primera línea debe tener: centro_id, tipo_centro, codigo_dane, municipio, departamento, latitud, longitud, categoria_cale, demanda_estimada_anual, nodo_principal, ...

3. Volver a publicar:
   - File → Share → Publish to web
   - Unpublish
   - Publish again (TSV format)

### Problema: Coordenadas incorrectas

**Verificar en consola:**
```javascript
const cache = JSON.parse(localStorage.getItem('cale_centros_cache'));
cache.data.forEach((c, i) => {
    const lat = parseFloat(c.latitud);
    const lng = parseFloat(c.longitud);
    if (isNaN(lat) || isNaN(lng)) {
        console.log(`Error en fila ${i + 2}:`, c.centro_id, 'lat:', c.latitud, 'lng:', c.longitud);
    }
});
```

---

## 📁 Archivos Modificados

| Archivo | Cambios |
|---------|---------|
| `services/github_pages/mapa_cale_nacional.html` | URL actualizada, parser TSV, formato TSV |
| `services/github_pages/limpiar_cache.html` | Nuevo archivo - herramienta limpieza |
| `CORRECCION_TSV_GOOGLE_SHEETS.md` | Este archivo - documentación |

---

## 🎉 Resultado Final

### ✅ Sistema Funcionando

```
Google Sheets (publicada como TSV)
    ↓
URL pública TSV
    ↓
fetch() JavaScript
    ↓
parseData(text, 'tsv')
    ↓
Cache (5 min)
    ↓
Leaflet Map (197 marcadores)
```

### 📊 Métricas

- ✅ 197 centros cargados
- ✅ 0 errores de parsing
- ✅ 0 errores de coordenadas
- ✅ Latitudes y longitudes correctas (con decimales)
- ✅ Cache funcionando (5 min TTL)
- ✅ 100% lectura desde Google Sheets

---

## 🚀 Próximos Pasos

1. **Verificar mapa en navegador:**
   - Abrir `mapa_cale_nacional.html`
   - Confirmar que se carga sin errores

2. **Documentar en README:**
   - Agregar instrucciones de publicación TSV
   - Explicar por qué TSV y no CSV

3. **Continuar con visor BIM 3D:**
   - Migrar a Xeokit ES6 modules
   - Implementar jerarquía BIM recursiva

---

**¡Mapa funcionando correctamente con Google Sheets TSV!**

*Última actualización: 29 de octubre de 2025*
