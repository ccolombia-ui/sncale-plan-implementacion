# Instrucciones: Actualizar Google Sheets - Columna K (nodo_principal)

**Fecha:** 29 de octubre de 2025
**Objetivo:** Actualizar columna K con valores corregidos (municipio → centro_id)

---

## Archivo Generado

✅ **columna_k_nodo_principal.txt** - 197 valores listos para copiar

---

## Método 1: Copiar desde archivo TXT (RECOMENDADO)

### Paso 1: Abrir archivo
```
Abrir: columna_k_nodo_principal.txt
```

### Paso 2: Seleccionar todo
```
Ctrl + A (seleccionar todo)
Ctrl + C (copiar)
```

### Paso 3: Ir a Google Sheets
```
URL: https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=197105959#gid=197105959
```

### Paso 4: Seleccionar celda K2
```
Click en celda K2 (primera celda de DATOS, NO el header "nodo_principal")
```

### Paso 5: Pegar valores
```
Ctrl + V
```

✅ **Los 197 valores se pegarán automáticamente en la columna K (K2:K198)**

---

## Método 2: Importar CSV completo

### Opción A: Reemplazar hoja completa

1. Ir a Google Sheets
2. File → Import
3. Upload → Seleccionar `arquitectura_red_cale_nacional_MAPEADO.csv`
4. Import location: **Replace current sheet**
5. Separator type: Comma
6. Click "Import data"

⚠️ **ADVERTENCIA:** Esto reemplazará TODA la hoja actual

### Opción B: Crear nueva hoja

1. Ir a Google Sheets
2. Crear nueva hoja (botón + abajo)
3. Nombrar: `arquitectura_red_cale_nacional_V2`
4. File → Import
5. Upload → Seleccionar `arquitectura_red_cale_nacional_MAPEADO.csv`
6. Import location: **Replace current sheet**
7. Click "Import data"

✅ **RECOMENDADO:** Mantiene la hoja original como respaldo

---

## Verificación de Datos

### ✅ Valores Correctos (centro_id)
```
NODO_02
NODO_03
NODO_40
SAT_001
```

### ❌ Valores Incorrectos (nombres de municipios)
```
"BOGOTÁ, D.C."
Bucaramanga
Aguachica
```

### Verificar Algunos Casos Clave

| centro_id | municipio | nodo_principal (DEBE SER) |
|-----------|-----------|---------------------------|
| NODO_01 | BOGOTÁ, D.C. | NODO_02 |
| NODO_05 | Ibagué | NODO_27 |
| SAT_001 | ARENAL | NODO_40 |
| SAT_005 | PUEBLORRICO | NODO_36 |
| SAT_010 | CARACOLÍ | NODO_21 |

---

## Después de Actualizar

### Paso 1: Verificar datos en Google Sheets

```
1. Scroll hasta abajo (fila 198)
2. Verificar que haya 197 filas de datos
3. Verificar columna K tiene formato NODO_XX o SAT_XX
4. NO debe tener nombres de municipios
```

### Paso 2: Publicar hoja como CSV

```
1. File → Share → Publish to web
2. Link: arquitectura_red_cale_nacional (o la nueva hoja V2)
3. Format: CSV
4. Click "Publish"
5. Copiar URL generada
```

**URL esperada:**
```
https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/export?format=csv&gid=197105959
```

⚠️ **IMPORTANTE:** Si creaste una hoja nueva (V2), el `gid` será diferente

### Paso 3: Actualizar HTML (si cambió el gid)

Si creaste una hoja nueva, actualizar en `mapa_cale_nacional.html`:

```javascript
const GOOGLE_SHEETS_CONFIG = {
    // Actualizar el gid si es una hoja nueva
    url: 'https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/export?format=csv&gid=NUEVO_GID_AQUI',
    cacheKey: 'cale_centros_cache',
    cacheTTL: 5 * 60 * 1000
};
```

### Paso 4: Limpiar cache del navegador

```javascript
// En consola del navegador (F12):
localStorage.removeItem('cale_centros_cache');
location.reload();
```

### Paso 5: Probar mapa

```
Abrir: services/github_pages/mapa_cale_nacional.html

Verificar:
✅ Se cargan 197 centros
✅ Marcadores visibles en Colombia
✅ Popups muestran "Nodo Principal: NODO_XX" (NO nombres de municipios)
✅ Estadísticas muestran: 56 nodos + 141 satélites
```

---

## Troubleshooting

### Problema: "No se encontraron datos"

**Solución:**
1. Verificar que la hoja esté publicada (File → Share → Publish to web)
2. Verificar que el formato sea CSV (no HTML)
3. Probar abrir la URL directamente en el navegador
4. Verificar CORS (debe cargar sin errores)

### Problema: "Nodo Principal muestra nombres de municipios"

**Solución:**
1. Verificar que copiaste la columna K CORRECTA
2. El archivo debe ser `columna_k_nodo_principal.txt`
3. Los valores deben ser NODO_XX, NO nombres de ciudades
4. Limpiar cache: `localStorage.clear()`

### Problema: "Faltan centros en el mapa"

**Solución:**
1. Verificar que se pegaron los 197 valores (K2:K198)
2. Verificar que NO hay filas vacías
3. Verificar columnas latitud/longitud tienen valores
4. Ver consola del navegador (F12) para errores

---

## Resumen de Archivos

| Archivo | Descripción |
|---------|-------------|
| `arquitectura_red_cale_nacional_MAPEADO.csv` | CSV completo con 197 centros corregidos |
| `columna_k_nodo_principal.txt` | Solo columna K (197 valores) |
| `scripts/extraer_columna_k.py` | Script para regenerar la columna |
| `scripts/mapear_nodo_principal.py` | Script original de mapeo |

---

## Valores Estadísticos

```
Total centros: 197
├─ Nodos principales: 56
└─ Satélites: 141

Valores únicos en nodo_principal:
├─ NODO_02: 3 centros
├─ NODO_03: 3 centros
├─ NODO_31: 17 centros
├─ NODO_40: 4 centros
└─ ... (53 nodos únicos en total)
```

---

## ¡Listo!

Una vez actualizada la Google Sheet y publicada como CSV:

✅ El mapa cargará datos en tiempo real desde Google Sheets
✅ Cualquier cambio en la Sheet se reflejará en < 5 minutos
✅ Zero archivos intermedios
✅ Sistema completamente funcional

**Siguiente paso:** Probar mapa en navegador
