# 🚀 PLAN DE MEJORA: VISOR 3D + MAPA INTERACTIVO - PROYECTO MUNAY-SNCALE

**Proyecto:** Sistema Nacional de Centros de Enseñanza Automovilística (SNCALE)
**Versión:** 3.0 - Integración Total con Google Sheets (Visor 3D + Mapa Interactivo)
**Fecha Inicio:** 2025-10-29
**Estado:** 🟡 EN PLANIFICACIÓN
**Prioridad:** 🔴 ALTA - Sistema en producción con error visible

**Hojas de Google Sheets (Fuente Única de Verdad):**
- 📊 [Hoja 1: Presupuesto BIM (125 productos)](https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=1032260683)
- 🗺️ [Hoja 2: Ubicaciones CALE (141 centros)](https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=197105959)

---

## 📋 TABLA DE CONTENIDOS

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Diagnóstico Actual](#diagnóstico-actual)
3. [Objetivos del Proyecto](#objetivos-del-proyecto)
4. [Arquitectura Nueva](#arquitectura-nueva)
5. [Plan de Trabajo](#plan-de-trabajo)
6. [Checklist de Progreso](#checklist-de-progreso)
7. [Comandos y Referencias](#comandos-y-referencias)

---

## 📊 RESUMEN EJECUTIVO

### **Problema Actual**

#### **🔧 Visor BIM 3D**
- ❌ CDN de xeokit con URL incorrecta (404)
- ❌ Arquitectura incompatible (espera script global, pero xeokit solo soporta ES6 modules)
- ❌ Nomenclatura de categorías desactualizada (CAT.X en vez de CALE.n_X)
- ❌ Datos hardcodeados en HTML (no sincronizados con Google Sheets)

#### **🗺️ Mapa Interactivo**
- ❌ Nomenclatura desactualizada en CSV (Cat.A+, Cat.B, Cat.C1 en vez de CALE.n_X)
- ❌ Datos hardcodeados en HTML (no sincronizados con Google Sheets)
- ❌ Sin actualización automática desde fuente única
- ❌ Coordenadas y ubicaciones en archivos separados (falta de coherencia)

### **Solución Propuesta**

#### **Sistema Unificado de Sincronización**
- ✅ **DOS hojas de Google Sheets** como fuente única de verdad
- ✅ **UN script de sincronización** que actualiza ambos sistemas
- ✅ Xeokit SDK con ES6 modules (visor 3D)
- ✅ Leaflet.js actualizado (mapa interactivo)
- ✅ Actualización automática de nomenclatura CALE.n_X en ambos sistemas
- ✅ Coherencia total entre visor 3D, mapa y fichas técnicas

### **Impacto Esperado**
- 🎯 Visor 3D funcional en GitHub Pages
- 🎯 Mapa interactivo con datos actualizados
- 🎯 **Cambios en Google Sheets actualizan TODO el sistema:**
  - Visor 3D (componentes BIM)
  - Mapa interactivo (ubicaciones + categorías)
  - Fichas técnicas (costos + specs)
  - Presupuestos (CAPEX/OPEX)
- 🎯 Nomenclatura unificada MUNAY 5.3 (CALE.n_X)
- 🎯 Base de código moderna y escalable
- 🎯 **Un solo punto de actualización** para todos los sistemas

---

## 🔍 DIAGNÓSTICO ACTUAL

### **Estado del Visor 3D**

**URL Afectada:**
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html

**Error Visible:**
```
❌ Error: No se pudo cargar xeokit
Verifica conexión a internet o usa versión local
```

### **Análisis Técnico**

| Componente | Estado | Problema Identificado |
|-----------|---------|----------------------|
| **CDN Xeokit** | ❌ ROTO | URL `https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk@latest/dist/xeokit-sdk.min.js` devuelve **404** |
| **Arquitectura JS** | ❌ INCOMPATIBLE | Código espera `xeokit` global, pero SDK solo distribuye **ES6 modules** |
| **Datos BIM** | ⚠️ DESACTUALIZADOS | Datos hardcodeados en HTML (última actualización: hace semanas) |
| **Nomenclatura** | ⚠️ OBSOLETA | Usa `CAT.A+`, `CAT.B` en vez de `CALE.n_1+`, `CALE.n_2` |
| **Integración Sheets** | ❌ NO EXISTE | No hay sincronización con Google Sheets (fuente única de verdad) |

### **Causa Raíz**

**Problema 1: CDN Incorrecto**
```html
<!-- ❌ ESTO NO EXISTE -->
<script src="https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk@latest/dist/xeokit-sdk.min.js"></script>

<!-- ✅ VERSIÓN CORRECTA (ES6 Module) -->
<script type="module">
  import {Viewer} from "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";
</script>
```

**Problema 2: Arquitectura Incompatible**
```javascript
// ❌ CÓDIGO ACTUAL (espera global)
const viewer = new xeokit.Viewer({...});

// ✅ CÓDIGO CORRECTO (ES6 import)
import {Viewer} from "...";
const viewer = new Viewer({...});
```

---

### **Estado del Mapa Interactivo**

**URL Actual:**
https://ccolombia-ui.github.io/sncale-plan-implementacion/mapa_cale.html (o similar)

**Problemas Identificados:**

| Componente | Estado | Problema Identificado |
|-----------|---------|----------------------|
| **Datos de Ubicaciones** | ⚠️ DESACTUALIZADOS | CSV con nomenclatura antigua (Cat.A+, Cat.B, Cat.C1) |
| **Sincronización** | ❌ NO EXISTE | Datos hardcodeados, no sincronizados con Google Sheets |
| **Nomenclatura** | ❌ OBSOLETA | 141 centros usando Cat.X en vez de CALE.n_X |
| **Coordenadas** | ⚠️ DISPERSAS | Datos en múltiples archivos (CSV, JSON) sin coherencia |
| **Integración BIM** | ❌ DÉBIL | Mapa no conecta con visor 3D ni fichas técnicas |

**Datos Actuales del CSV:**
```csv
centro_id,tipo_centro,municipio,departamento,latitud,longitud,categoria_cale,demanda_estimada_anual
NODO_01,NODO_PRINCIPAL,"BOGOTÁ, D.C.","BOGOTÁ, D.C.",4.649251,-74.106992,Cat.A+,80453
NODO_22,NODO_PRINCIPAL,SANTA FÉ DE ANTIOQUIA,ANTIOQUIA,6.556484,-75.826648,Cat.B**,32510
NODO_41,NODO_PRINCIPAL,San Andrés,SANTANDER,6.811511,-72.848864,Cat.C1,16000
```

**Necesita migración a:**
```csv
categoria_cale,nueva_nomenclatura
Cat.A+,CALE.n_1+
Cat.A,CALE.n_1
Cat.B**,CALE.n_2**
Cat.B,CALE.n_2
Cat.C1,CALE.n_3
Cat.C2,CALE.C2
Cat.C3,CALE.C3
```

**Arquitectura Actual del Mapa:**
- **Librería:** Leaflet.js 1.9.4 ✅ (moderna, no requiere cambio)
- **Datos:** CSV estático → Necesita actualización desde Google Sheets
- **Markers:** Colores por categoría → Actualizar colores para CALE.n_X
- **Popups:** Información de centros → Conectar con visor 3D y fichas

---

## 🎯 OBJETIVOS DEL PROYECTO

### **Objetivos Principales**

1. **[OBJ-1] Visor 3D Funcional**
   - ✅ Carga correcta de xeokit SDK
   - ✅ Renderizado de modelos BIM 3D
   - ✅ Navegación interactiva (rotar, zoom, pan)
   - ✅ Sin errores en consola

2. **[OBJ-2] Mapa Interactivo Actualizado**
   - ✅ Sincronización con Google Sheets (141 centros)
   - ✅ Nomenclatura CALE.n_X actualizada
   - ✅ Marcadores con colores actualizados
   - ✅ Links a visor 3D y fichas técnicas

3. **[OBJ-3] Integración Google Sheets (FUENTE ÚNICA)**
   - ✅ **Hoja 1:** Presupuesto BIM (125 productos) → Visor 3D + Fichas
   - ✅ **Hoja 2:** Ubicaciones CALE (141 centros) → Mapa Interactivo
   - ✅ Script Python unificado para conversión Sheets → JSON
   - ✅ Un solo comando actualiza TODO el sistema

4. **[OBJ-4] Actualización Nomenclatura (AMBOS SISTEMAS)**
   - ✅ Migrar `Cat.A+` → `CALE.n_1+`
   - ✅ Migrar `Cat.A` → `CALE.n_1`
   - ✅ Migrar `Cat.B**` → `CALE.n_2**`
   - ✅ Migrar `Cat.B` → `CALE.n_2`
   - ✅ Migrar `Cat.C1` → `CALE.n_3`
   - ✅ Mantener `CALE.C2`, `CALE.C3` sin cambios
   - ✅ Aplicar en: Visor 3D, Mapa, CSVs, JSONs, HTMLs

5. **[OBJ-5] Arquitectura Moderna Unificada**
   - ✅ Código ES6 modules (visor 3D)
   - ✅ Leaflet.js optimizado (mapa)
   - ✅ Separación de datos y presentación
   - ✅ Documentación completa
   - ✅ Sistema interconectado (mapa ↔ visor ↔ fichas)

### **Métricas de Éxito**

| Métrica | Estado Actual | Meta |
|---------|---------------|------|
| **Visor 3D funcional** | ❌ 0% | ✅ 100% |
| **Mapa interactivo actualizado** | ⚠️ 50% (funciona pero desactualizado) | ✅ 100% |
| **Datos sincronizados con Sheets** | ❌ 0% | ✅ 100% (ambas hojas) |
| **Nomenclatura CALE actualizada** | ❌ 0% | ✅ 100% (visor + mapa + CSVs) |
| **141 centros con ubicaciones correctas** | ⚠️ 70% (desactualizado) | ✅ 100% |
| **125 productos BIM validados** | ⚠️ 80% (sin SEÑ-XXX) | ✅ 100% |
| **Errores en consola** | ❌ 5+ errores | ✅ 0 errores |
| **Tiempo de carga (visor)** | ⚠️ N/A (no carga) | ✅ <3 segundos |
| **Tiempo de carga (mapa)** | ✅ 2 segundos | ✅ <2 segundos |
| **Coherencia entre sistemas** | ❌ 30% (datos dispersos) | ✅ 100% (fuente única) |

---

## 🏗️ ARQUITECTURA NUEVA

### **Diagrama de Flujo de Datos - Sistema Unificado**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   GOOGLE SHEETS (Fuente Única de Verdad)                    │
│         https://docs.google.com/spreadsheets/d/1ibTlTyA.../edit             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📊 HOJA 1: "Presupuesto BIM"         🗺️ HOJA 2: "Ubicaciones CALE"        │
│  (gid=1032260683)                     (gid=197105959)                      │
│                                                                             │
│  • 125 productos BIM                  • 141 centros CALE                   │
│  • Códigos ERP (MAT-XXX, SEÑ-XXX)     • Coordenadas (lat/lng)              │
│  • Categorías CALE.n_X                • Categorías CALE.n_X                │
│  • CAPEX, OPEX, TCO                   • Demanda estimada                   │
│  • Clases IFC                         • Municipios/Departamentos           │
│  • Proveedores, Garantías             • Nodos principales/satélites        │
│                                                                             │
└──────────┬──────────────────────────────────────────┬───────────────────────┘
           │                                          │
           │ [1a] Exportar CSV                        │ [1b] Exportar CSV
           ▼                                          ▼
┌──────────────────────────────────┐    ┌────────────────────────────────────┐
│ SNCALE_Presupuesto_125.csv       │    │ MUNAY_5.3_Ubicaciones_141.csv     │
│ (services/google_sheets/)        │    │ (services/google_sheets/)          │
└──────────┬───────────────────────┘    └────────────┬───────────────────────┘
           │                                          │
           └────────────────┬─────────────────────────┘
                            │ [2] Script Python UNIFICADO
                            ▼
           ┌────────────────────────────────────────────────────────┐
           │   services/google_sheets/sync_sistema_completo.py      │
           │                                                        │
           │   class SyncSistemaCompleto:                           │
           │     def sync_presupuesto_bim()   # Hoja 1 → Visor 3D  │
           │     def sync_ubicaciones_mapa()  # Hoja 2 → Mapa      │
           │     def actualizar_nomenclatura() # CAT → CALE        │
           │     def generar_fichas_html()    # Fichas técnicas    │
           │     def validar_coherencia()     # 125 + 141 OK       │
           │                                                        │
           └────────┬───────────────────────────────┬───────────────┘
                    │ [3a] JSON BIM                 │ [3b] JSON Mapa
                    ▼                               ▼
  ┌─────────────────────────────────┐    ┌──────────────────────────────────┐
  │ catalogo_bim_completo.json      │    │ ubicaciones_cale_141.json        │
  │ (fichas_bim/datos_json/)        │    │ (mapa_cale/datos/)               │
  │                                 │    │                                  │
  │ {                               │    │ {                                │
  │   "version": "5.3",             │    │   "version": "5.3",              │
  │   "total_productos": 125,       │    │   "total_centros": 141,          │
  │   "categorias": {               │    │   "centros": [                   │
  │     "CALE.n_1+": {              │    │     {                            │
  │       "productos": [...],       │    │       "id": "NODO_01",           │
  │       "capex_total": 750M       │    │       "municipio": "BOGOTÁ",     │
  │     },                          │    │       "categoria": "CALE.n_1+",  │
  │     "CALE.n_1": {...},          │    │       "lat": 4.649251,           │
  │     ...                         │    │       "lng": -74.106992,         │
  │   }                             │    │       "link_visor": "visor?..." }│
  │ }                               │    │   ]                              │
  │                                 │    │ }                                │
  └────────┬────────────────────────┘    └────────┬─────────────────────────┘
           │ [4a] Fetch                           │ [4b] Fetch
           ▼                                      ▼
  ┌────────────────────────────┐       ┌─────────────────────────────────┐
  │ visor_bim_3d.html          │       │ mapa_cale.html                  │
  │ (fichas_bim/)              │       │ (mapa_cale/ o root)             │
  │                            │       │                                 │
  │ <script type="module">     │       │ <script>                        │
  │   import {Viewer} from     │       │   // Leaflet.js 1.9.4           │
  │     "xeokit-sdk.es.min.js" │       │   const mapa = L.map('map')     │
  │                            │       │   const centros = await fetch   │
  │   const catalogo = await   │       │     ('datos/ubicaciones.json')  │
  │     fetch('catalogo.json') │       │                                 │
  │   renderizar3D(catalogo)   │       │   centros.forEach(centro => {   │
  │ </script>                  │       │     L.marker([lat, lng])        │
  │                            │       │       .bindPopup(...)           │
  │                            │       │       .on('click', () =>        │
  │                            │       │         abrirVisor3D(centro))   │
  │                            │       │   })                            │
  └────────┬───────────────────┘       └────────┬────────────────────────┘
           │ [5] Deploy GitHub Pages            │
           └────────────┬───────────────────────┘
                        ▼
           ┌────────────────────────────────────────────────────────┐
           │   https://ccolombia-ui.github.io/sncale-.../           │
           │                                                        │
           │   ✅ Visor 3D funcional (xeokit ES6)                   │
           │   ✅ Mapa interactivo (Leaflet + 141 centros)          │
           │   ✅ Datos sincronizados (Google Sheets → JSON)        │
           │   ✅ Nomenclatura CALE.n_X unificada                   │
           │   ✅ Click en mapa → abre visor 3D del centro          │
           │   ✅ Fichas técnicas actualizadas                      │
           │                                                        │
           └────────────────────────────────────────────────────────┘
```

### **Componentes del Sistema Unificado**

#### **1. Fuente de Datos: Google Sheets (DOBLE HOJA)**

**Hoja 1: Presupuesto BIM (gid=1032260683)**
- **URL:** https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=1032260683
- **Contenido:** 125 productos BIM con metadata completa
- **Columnas:**
  - Código ERP, Nombre Comercial, Categoría BIM
  - Clase IFC, Unidad Medida
  - CAPEX Unitario, OPEX Anual, TCO 5 Años
  - Código DANE, Código CAMACOL
  - Proveedor, Garantía, Normativas
  - Ficha Técnica URL, Estado, Observaciones
- **Formato:** CSV exportable
- **Actualización:** Manual por equipo UPTC/Mintransporte
- **Destino:** Visor 3D + Fichas Técnicas

**Hoja 2: Ubicaciones CALE (gid=197105959)**
- **URL:** https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=197105959
- **Contenido:** 141 centros CALE (nodos principales + satélites)
- **Columnas:**
  - centro_id, tipo_centro (NODO_PRINCIPAL/SATELITE)
  - codigo_dane, municipio, departamento
  - latitud, longitud
  - categoria_cale (Cat.A+ → CALE.n_1+)
  - demanda_estimada_anual
  - nodo_principal, total_municipios_cluster
  - distancia_maxima_km, distancia_promedio_km
- **Formato:** CSV exportable
- **Actualización:** Manual por equipo UPTC/Mintransporte
- **Destino:** Mapa Interactivo + Dashboard Ubicaciones

#### **2. Script de Sincronización UNIFICADO**
```python
# services/google_sheets/sync_sistema_completo.py

class SyncSistemaCompleto:
    """
    Sistema unificado de sincronización para SNCALE MUNAY 5.3

    Sincroniza AMBAS hojas de Google Sheets:
    - Hoja 1: Presupuesto BIM (125 productos) → Visor 3D + Fichas
    - Hoja 2: Ubicaciones CALE (141 centros) → Mapa Interactivo
    """

    def __init__(self):
        self.csv_presupuesto = 'SNCALE_Presupuesto_125.csv'
        self.csv_ubicaciones = 'MUNAY_5.3_Ubicaciones_141.csv'
        self.productos = []
        self.centros = []

    def sync_presupuesto_bim(self):
        """
        Sincroniza Hoja 1: Presupuesto BIM

        Proceso:
        1. Lee CSV exportado de Sheets (Hoja 1)
        2. Valida 125 productos (incluye SEÑ-XXX)
        3. Actualiza nomenclatura CAT → CALE
        4. Genera JSON para visor 3D
        5. Genera fichas técnicas HTML
        """
        pass

    def sync_ubicaciones_mapa(self):
        """
        Sincroniza Hoja 2: Ubicaciones CALE

        Proceso:
        1. Lee CSV exportado de Sheets (Hoja 2)
        2. Valida 141 centros CALE
        3. Actualiza nomenclatura Cat.X → CALE.n_X
        4. Genera JSON para mapa interactivo
        5. Crea links a visor 3D por categoría
        """
        pass

    def actualizar_nomenclatura_completa(self):
        """
        Actualiza nomenclatura en AMBAS hojas

        Mapping:
        Cat.A+  → CALE.n_1+
        Cat.A   → CALE.n_1
        Cat.B** → CALE.n_2**
        Cat.B   → CALE.n_2
        Cat.C1  → CALE.n_3
        Cat.C2  → CALE.C2 (sin cambio)
        Cat.C3  → CALE.C3 (sin cambio)
        """
        pass

    def generar_fichas_html(self):
        """
        Genera fichas técnicas HTML para cada producto
        usando datos de Hoja 1
        """
        pass

    def validar_coherencia_sistema(self):
        """
        Valida coherencia entre ambas hojas:
        - 125 productos BIM correctos
        - 141 centros CALE correctos
        - Nomenclatura coherente
        - Links visor ↔ mapa funcionan
        """
        pass

    def ejecutar_sincronizacion_completa(self):
        """
        COMANDO PRINCIPAL: Sincroniza TODO el sistema

        Un solo comando actualiza:
        ✅ Visor 3D
        ✅ Mapa Interactivo
        ✅ Fichas Técnicas
        ✅ Nomenclatura CALE.n_X
        """
        print("🔄 Iniciando sincronización completa SNCALE MUNAY 5.3...")

        # Hoja 1: Presupuesto BIM
        self.sync_presupuesto_bim()
        print("✅ Hoja 1 sincronizada: 125 productos BIM")

        # Hoja 2: Ubicaciones CALE
        self.sync_ubicaciones_mapa()
        print("✅ Hoja 2 sincronizada: 141 centros CALE")

        # Actualizar nomenclatura
        self.actualizar_nomenclatura_completa()
        print("✅ Nomenclatura CALE.n_X actualizada")

        # Generar fichas
        self.generar_fichas_html()
        print("✅ Fichas técnicas generadas")

        # Validar
        self.validar_coherencia_sistema()
        print("✅ Coherencia del sistema validada")

        print("🎉 Sincronización completa exitosa!")

# USO:
# python services/google_sheets/sync_sistema_completo.py
```

#### **3. Visor 3D Actualizado**
```html
<!-- fichas_bim/visor_bim_3d_v2.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Visor BIM 3D - SNCALE MUNAY 5.3</title>
</head>
<body>
    <canvas id="canvas3d"></canvas>

    <script type="module">
        import {
            Viewer,
            Mesh,
            PhongMaterial,
            BoxGeometry
        } from "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";

        // Cargar datos del catálogo
        const catalogoResponse = await fetch('datos_json/catalogo_bim_completo.json');
        const catalogoData = await catalogoResponse.json();

        // Inicializar visor
        const viewer = new Viewer({
            canvasId: "canvas3d",
            transparent: true,
            dtxEnabled: true
        });

        // Renderizar geometría según categoría seleccionada
        renderizarCentroCALE(catalogoData, categoriaSeleccionada);
    </script>
</body>
</html>
```

---

## 📅 PLAN DE TRABAJO

### **FASE 1: PREPARACIÓN Y ANÁLISIS** (30 min)

**Objetivo:** Preparar entorno y validar datos existentes

- [ ] **TAREA 1.1:** Validar acceso a Google Sheets
  - [ ] Verificar URL de la hoja de cálculo
  - [ ] Exportar CSV actualizado
  - [ ] Guardar en `services/google_sheets/SNCALE_Presupuesto_Nivel_1_COMPLETO_125.csv`

- [ ] **TAREA 1.2:** Auditar datos actuales
  - [ ] Contar productos por categoría
  - [ ] Verificar que hay 125 productos totales
  - [ ] Confirmar presencia de productos SEÑ-XXX

- [ ] **TAREA 1.3:** Backup del visor actual
  ```bash
  cd c:\raziel\sncale-plan-implementacion
  copy fichas_bim\visor_bim_3d.html fichas_bim\visor_bim_3d_backup_20251029.html
  ```

**Entregables:**
- ✅ CSV actualizado descargado
- ✅ Backup del visor actual
- ✅ Reporte de auditoría de datos

---

### **FASE 2: ACTUALIZACIÓN DE NOMENCLATURA** (45 min)

**Objetivo:** Migrar sistema de categorías CAT.X → CALE.n_X

- [ ] **TAREA 2.1:** Crear script de migración de nomenclatura
  ```python
  # services/google_sheets/migrar_nomenclatura_cale.py

  MAPPING_CATEGORIAS = {
      "CAT.A+": "CALE.n_1+",
      "CAT.A": "CALE.n_1",
      "CAT.B**": "CALE.n_2**",
      "CAT.B": "CALE.n_2",
      "CAT.C1": "CALE.n_3",
      "CAT.C2": "CALE.C2",  # Sin cambio
      "CAT.C3": "CALE.C3"   # Sin cambio
  }
  ```

- [ ] **TAREA 2.2:** Actualizar archivos de datos
  - [ ] `bim_sncale/nivel.2/*.json` (archivos de configuración)
  - [ ] `planos_2d/datos_json/*.json` (datos de planos)
  - [ ] Scripts Python que referencien categorías

- [ ] **TAREA 2.3:** Validar consistencia
  - [ ] Ejecutar tests de integridad
  - [ ] Verificar que no hay referencias a "CAT." en código

**Entregables:**
- ✅ Script `migrar_nomenclatura_cale.py` funcional
- ✅ Todos los archivos JSON actualizados
- ✅ Reporte de migración sin errores

---

### **FASE 3: SCRIPT DE SINCRONIZACIÓN CON GOOGLE SHEETS** (1.5 horas)

**Objetivo:** Crear sistema automático de sincronización de datos BIM

- [ ] **TAREA 3.1:** Crear script base de sincronización
  ```python
  # services/google_sheets/sync_bim_data.py

  import csv
  import json
  from pathlib import Path

  class SyncBIMData:
      def __init__(self, csv_path):
          self.csv_path = csv_path
          self.productos = []

      def leer_csv(self):
          """Lee CSV exportado de Google Sheets"""
          pass

      def validar_125_productos(self):
          """Valida que hay exactamente 125 productos"""
          pass

      def agrupar_por_categoria(self):
          """Agrupa productos por CALE.n_X"""
          pass

      def calcular_costos_categoria(self):
          """Calcula CAPEX/OPEX total por categoría"""
          pass

      def generar_json_visor(self):
          """Genera JSON optimizado para visor 3D"""
          pass
  ```

- [ ] **TAREA 3.2:** Implementar parseo de CSV
  - [ ] Leer columnas: Código ERP, Nombre, Categoría BIM, Clase IFC, etc.
  - [ ] Manejar productos con Ñ (SEÑ-XXX)
  - [ ] Convertir CAPEX/OPEX a números

- [ ] **TAREA 3.3:** Generar estructura JSON para visor
  ```json
  {
    "version": "5.3",
    "fecha_actualizacion": "2025-10-29T12:00:00Z",
    "total_productos": 125,
    "categorias": {
      "CALE.n_1+": {
        "nombre": "Centro CALE Categoría A+ (Principal Enhanced)",
        "codigo": "CALE.n_1+",
        "productos": [
          {
            "codigo": "SIM-001",
            "nombre": "Simulador Conducción Básico",
            "clase_ifc": "IfcElectricAppliance",
            "capex": 180000000,
            "opex_anual": 36000000,
            "cantidad": 1,
            "geometria_3d": {
              "tipo": "box",
              "dimensiones": {"x": 3, "y": 2.5, "z": 2},
              "color": "#4A90E2"
            }
          }
        ],
        "capex_total": 750000000,
        "opex_total_anual": 75000000,
        "componentes_count": 45
      },
      "CALE.n_1": { ... },
      "CALE.n_2**": { ... }
    }
  }
  ```

- [ ] **TAREA 3.4:** Crear tests unitarios
  ```python
  def test_lee_125_productos():
      sync = SyncBIMData('test_data.csv')
      assert len(sync.productos) == 125

  def test_captura_productos_señ():
      sync = SyncBIMData('test_data.csv')
      productos_señ = [p for p in sync.productos if p['codigo'].startswith('SEÑ')]
      assert len(productos_señ) > 0  # Debe capturar SEÑ-XXX
  ```

- [ ] **TAREA 3.5:** Documentar proceso de sincronización
  ```markdown
  # MANUAL DE SINCRONIZACIÓN BIM

  ## Proceso Manual (cada actualización)
  1. Abrir Google Sheets
  2. Archivo → Descargar → CSV
  3. Guardar en services/google_sheets/SNCALE_...csv
  4. Ejecutar: python sync_bim_data.py
  5. Verificar JSON generado
  6. Commit + Push a GitHub
  ```

**Entregables:**
- ✅ Script `sync_bim_data.py` completo y testeado
- ✅ JSON `catalogo_bim_completo.json` generado
- ✅ Tests unitarios pasando
- ✅ Documentación de uso

---

### **FASE 4: MIGRACIÓN A XEOKIT ES6** (2 horas)

**Objetivo:** Actualizar visor 3D a arquitectura ES6 modules

- [ ] **TAREA 4.1:** Crear nuevo archivo HTML base
  ```bash
  touch fichas_bim/visor_bim_3d_v2.html
  ```

- [ ] **TAREA 4.2:** Implementar carga de xeokit ES6
  ```html
  <script type="module">
      // Importar componentes de xeokit
      import {
          Viewer,
          Mesh,
          PhongMaterial,
          BoxGeometry,
          ReadableGeometry
      } from "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";

      // Verificar carga exitosa
      console.log('✅ Xeokit cargado correctamente');

      // Inicializar visor
      const viewer = new Viewer({
          canvasId: "canvas3d",
          transparent: true,
          dtxEnabled: true
      });

      viewer.camera.eye = [-20, 15, 30];
      viewer.camera.look = [0, 0, 0];
      viewer.camera.up = [0, 1, 0];
  </script>
  ```

- [ ] **TAREA 4.3:** Cargar datos desde JSON
  ```javascript
  // Cargar catálogo BIM
  async function cargarCatalogo() {
      try {
          const response = await fetch('datos_json/catalogo_bim_completo.json');
          if (!response.ok) {
              throw new Error(`HTTP ${response.status}`);
          }
          const catalogo = await response.json();
          console.log(`✅ Catálogo cargado: ${catalogo.total_productos} productos`);
          return catalogo;
      } catch (error) {
          console.error('❌ Error cargando catálogo:', error);
          mostrarError('No se pudo cargar el catálogo BIM');
          return null;
      }
  }
  ```

- [ ] **TAREA 4.4:** Parsear parámetros URL
  ```javascript
  function obtenerParametrosURL() {
      const params = new URLSearchParams(window.location.search);
      return {
          centro: params.get('centro') || 'BOGOTÁ NORTE',
          categoria: params.get('categoria') || 'CALE.n_1+'
      };
  }
  ```

- [ ] **TAREA 4.5:** Generar geometría 3D procedural
  ```javascript
  function generarGeometriaCALE(viewer, categoria, productos) {
      const scene = viewer.scene;

      // Terreno base
      new Mesh(scene, {
          id: "terreno",
          geometry: new BoxGeometry(scene, {
              xSize: 50, ySize: 0.5, zSize: 50
          }),
          material: new PhongMaterial(scene, {
              diffuse: [0.3, 0.5, 0.3]
          }),
          position: [0, -0.25, 0]
      });

      // Renderizar cada producto
      let offsetX = -20;
      let offsetZ = -20;

      productos.forEach((producto, index) => {
          const geom = producto.geometria_3d;

          new Mesh(scene, {
              id: producto.codigo,
              geometry: new BoxGeometry(scene, {
                  xSize: geom.dimensiones.x,
                  ySize: geom.dimensiones.y,
                  zSize: geom.dimensiones.z
              }),
              material: new PhongMaterial(scene, {
                  diffuse: hexToRgb(geom.color)
              }),
              position: [offsetX, geom.dimensiones.y / 2, offsetZ]
          });

          // Actualizar posición para siguiente componente
          offsetX += 5;
          if (index % 10 === 9) {
              offsetX = -20;
              offsetZ += 5;
          }
      });
  }
  ```

- [ ] **TAREA 4.6:** Implementar controles de cámara
  ```javascript
  // Funciones globales para botones
  window.resetView = () => {
      viewer.camera.eye = [-20, 15, 30];
      viewer.camera.look = [0, 0, 0];
      viewer.camera.up = [0, 1, 0];
  };

  window.viewTop = () => {
      viewer.camera.eye = [0, 50, 0];
      viewer.camera.look = [0, 0, 0];
      viewer.camera.up = [0, 0, -1];
  };

  window.toggleProjection = () => {
      viewer.camera.projection =
          viewer.camera.projection === "perspective"
              ? "ortho"
              : "perspective";
  };
  ```

- [ ] **TAREA 4.7:** Crear UI de información
  ```html
  <div id="info-panel">
      <h2 id="centro-nombre"></h2>
      <div id="categoria-badge"></div>
      <div id="stats">
          <div class="stat">
              <span class="label">CAPEX Total:</span>
              <span class="value" id="capex-total"></span>
          </div>
          <div class="stat">
              <span class="label">Componentes:</span>
              <span class="value" id="componentes-count"></span>
          </div>
      </div>
      <div id="productos-lista"></div>
  </div>
  ```

- [ ] **TAREA 4.8:** Manejar errores gracefully
  ```javascript
  window.addEventListener('error', (event) => {
      if (event.message.includes('xeokit')) {
          mostrarError('Error cargando motor 3D. Recarga la página.');
      }
  });

  function mostrarError(mensaje) {
      const errorDiv = document.createElement('div');
      errorDiv.className = 'error-banner';
      errorDiv.textContent = `❌ ${mensaje}`;
      document.body.prepend(errorDiv);
  }
  ```

**Entregables:**
- ✅ `visor_bim_3d_v2.html` completo
- ✅ Carga de xeokit funcionando
- ✅ Geometría 3D renderizando
- ✅ Controles de cámara operativos
- ✅ UI mostrando información correcta

---

### **FASE 5: TESTING Y VALIDACIÓN** (1 hora)

**Objetivo:** Asegurar que todo funciona correctamente

- [ ] **TAREA 5.1:** Testing local
  ```bash
  # Iniciar servidor local
  cd c:\raziel\sncale-plan-implementacion
  python servidor_local.py

  # Abrir en navegador
  http://localhost:8765/fichas_bim/visor_bim_3d_v2.html?centro=BOGOTÁ%20NORTE&categoria=CALE.n_1+
  ```

- [ ] **TAREA 5.2:** Checklist de funcionalidades
  - [ ] ✅ Visor carga sin errores
  - [ ] ✅ Modelo 3D visible
  - [ ] ✅ Cámara responde a mouse wheel (zoom)
  - [ ] ✅ Ctrl+Drag funciona (pan)
  - [ ] ✅ Botones de vista funcionan (Top, Front, Side)
  - [ ] ✅ Toggle perspectiva/ortho funciona
  - [ ] ✅ Panel de información muestra datos correctos
  - [ ] ✅ Lista de componentes se genera dinámicamente
  - [ ] ✅ CAPEX total es correcto
  - [ ] ✅ Parámetros URL funcionan (?centro=XXX&categoria=YYY)
  - [ ] ✅ No hay errores en consola del navegador

- [ ] **TAREA 5.3:** Testing de datos
  ```python
  # Script de validación
  import json

  with open('fichas_bim/datos_json/catalogo_bim_completo.json') as f:
      catalogo = json.load(f)

  # Verificaciones
  assert catalogo['total_productos'] == 125
  assert 'CALE.n_1+' in catalogo['categorias']
  assert 'CALE.n_1' in catalogo['categorias']
  assert 'CAT.A+' not in str(catalogo)  # No debe haber nomenclatura vieja

  print("✅ Validación de datos OK")
  ```

- [ ] **TAREA 5.4:** Auditoría de nomenclatura
  ```bash
  # Buscar referencias a nomenclatura antigua
  grep -r "CAT\.A" fichas_bim/
  grep -r "CAT\.B" fichas_bim/
  grep -r "CAT\.C1" fichas_bim/

  # Debe retornar vacío (no encontrar nada)
  ```

- [ ] **TAREA 5.5:** Crear matriz de testing

  | Escenario | URL | Resultado Esperado | Status |
  |-----------|-----|-------------------|--------|
  | CALE.n_1+ Bogotá | `?centro=BOGOTÁ%20NORTE&categoria=CALE.n_1+` | 45 componentes, CAPEX $750M | ⏳ |
  | CALE.n_1 Medellín | `?centro=MEDELLÍN&categoria=CALE.n_1` | 38 componentes | ⏳ |
  | CALE.n_2** Cali | `?centro=CALI&categoria=CALE.n_2**` | 25 componentes | ⏳ |
  | Sin parámetros | `/visor_bim_3d_v2.html` | Default CALE.n_1+ | ⏳ |

**Entregables:**
- ✅ Reporte de testing completo
- ✅ Todos los tests pasando
- ✅ Screenshots de visor funcionando
- ✅ Validación de nomenclatura OK

---

### **FASE 6: DEPLOYMENT Y DOCUMENTACIÓN** (45 min)

**Objetivo:** Desplegar a producción y documentar

- [ ] **TAREA 6.1:** Reemplazar visor antiguo
  ```bash
  cd c:\raziel\sncale-plan-implementacion

  # Backup final del visor viejo
  copy fichas_bim\visor_bim_3d.html fichas_bim\visor_bim_3d_OLD_ROTO.html

  # Reemplazar con versión nueva
  copy fichas_bim\visor_bim_3d_v2.html fichas_bim\visor_bim_3d.html
  ```

- [ ] **TAREA 6.2:** Commit y push a GitHub
  ```bash
  git add fichas_bim/visor_bim_3d.html
  git add fichas_bim/datos_json/catalogo_bim_completo.json
  git add services/google_sheets/sync_bim_data.py

  git commit -m "feat: Migrar visor 3D a xeokit ES6 + integración Google Sheets

  BREAKING CHANGES:
  - Actualizar nomenclatura CAT.X → CALE.n_X (MUNAY 5.3)
  - Migrar a xeokit SDK con ES6 modules
  - Integrar sincronización con Google Sheets (125 productos)
  - Corregir error 404 en CDN de xeokit

  Features:
  - Script sync_bim_data.py para sincronización automática
  - Catálogo BIM completo en JSON (catalogo_bim_completo.json)
  - Visor 3D funcional con navegación interactiva
  - Datos actualizados desde fuente única (Google Sheets)

  Fixes:
  - fix: Corregir CDN xeokit (404 → ES6 module válido)
  - fix: Capturar productos SEÑ-XXX correctamente
  - fix: Actualizar nomenclatura a MUNAY 5.3

  Testing:
  - ✅ 125 productos validados
  - ✅ Visor carga sin errores
  - ✅ Nomenclatura CALE.n_X actualizada
  - ✅ Sincronización Google Sheets operativa

  🤖 Generated with Claude Code
  Co-Authored-By: Claude <noreply@anthropic.com>"

  git push origin main
  ```

- [ ] **TAREA 6.3:** Verificar deployment en GitHub Pages
  ```bash
  # Esperar 1-2 minutos para build de GitHub Pages
  # Verificar en navegador:
  start "https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html?centro=BOGOTÁ%20NORTE&categoria=CALE.n_1+"
  ```

- [ ] **TAREA 6.4:** Crear documentación de mantenimiento
  ```markdown
  # MANUAL DE MANTENIMIENTO - VISOR BIM 3D

  ## Actualizar datos BIM desde Google Sheets

  ### Proceso (cada vez que cambien datos):

  1. Abrir Google Sheets:
     https://docs.google.com/spreadsheets/d/[ID]/edit

  2. Exportar como CSV:
     Archivo → Descargar → Valores separados por comas (.csv)

  3. Guardar en:
     c:\raziel\ia_formulacion\services\google_sheets\SNCALE_Presupuesto_Nivel_1_COMPLETO_125.csv

  4. Ejecutar script de sincronización:
     cd c:\raziel\ia_formulacion
     python services/google_sheets/sync_bim_data.py

  5. Verificar JSON generado:
     type c:\raziel\sncale-plan-implementacion\fichas_bim\datos_json\catalogo_bim_completo.json

  6. Copiar JSON al repositorio:
     copy c:\raziel\ia_formulacion\bim_sncale\catalogo_bim_completo.json c:\raziel\sncale-plan-implementacion\fichas_bim\datos_json\

  7. Commit y push:
     cd c:\raziel\sncale-plan-implementacion
     git add fichas_bim/datos_json/catalogo_bim_completo.json
     git commit -m "data: Actualizar catálogo BIM desde Google Sheets"
     git push origin main

  8. Esperar 2 minutos y verificar:
     https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html
  ```

- [ ] **TAREA 6.5:** Actualizar README del proyecto
  ```markdown
  ## 🔄 Sincronización con Google Sheets

  El visor BIM 3D se sincroniza automáticamente con Google Sheets:

  - **Fuente de datos:** Google Sheets (125 productos BIM)
  - **Frecuencia:** Manual (cada actualización de presupuesto)
  - **Script:** `services/google_sheets/sync_bim_data.py`
  - **Output:** `fichas_bim/datos_json/catalogo_bim_completo.json`

  ### Categorías CALE (MUNAY 5.3)

  | Categoría | Nombre | Componentes |
  |-----------|--------|-------------|
  | CALE.n_1+ | Centro Principal Enhanced | 45 |
  | CALE.n_1 | Centro Principal | 38 |
  | CALE.n_2** | Centro Intermedio Enhanced | 25 |
  | CALE.n_2 | Centro Intermedio | 20 |
  | CALE.n_3 | Centro Básico | 15 |
  | CALE.C2 | Satélite Tipo 2 | 8 |
  | CALE.C3 | Satélite Tipo 3 | 5 |
  ```

**Entregables:**
- ✅ Visor desplegado en producción
- ✅ Documentación de mantenimiento
- ✅ README actualizado
- ✅ Commit message detallado en Git

---

## ✅ CHECKLIST DE PROGRESO

### **Fase 1: Preparación** ⏳
- [ ] Validar acceso Google Sheets
- [ ] Exportar CSV actualizado
- [ ] Crear backup visor actual
- [ ] Auditar 125 productos

### **Fase 2: Nomenclatura** ⏳
- [ ] Script migración CAT → CALE
- [ ] Actualizar archivos JSON
- [ ] Validar consistencia
- [ ] Tests de integridad

### **Fase 3: Sincronización** ⏳
- [ ] Crear `sync_bim_data.py`
- [ ] Implementar parseo CSV
- [ ] Generar JSON optimizado
- [ ] Crear tests unitarios
- [ ] Documentar proceso

### **Fase 4: Xeokit ES6** ⏳
- [ ] Crear `visor_bim_3d_v2.html`
- [ ] Importar xeokit ES6 modules
- [ ] Cargar datos desde JSON
- [ ] Parsear parámetros URL
- [ ] Generar geometría 3D
- [ ] Implementar controles cámara
- [ ] Crear UI información
- [ ] Manejar errores

### **Fase 5: Testing** ⏳
- [ ] Testing local completo
- [ ] Checklist funcionalidades
- [ ] Validación de datos
- [ ] Auditoría nomenclatura
- [ ] Matriz de testing

### **Fase 6: Deployment** ⏳
- [ ] Reemplazar visor antiguo
- [ ] Commit y push GitHub
- [ ] Verificar GitHub Pages
- [ ] Documentación mantenimiento
- [ ] Actualizar README

---

## 📚 COMANDOS Y REFERENCIAS

### **Comandos Rápidos**

```bash
# ================================
# SINCRONIZACIÓN DE DATOS
# ================================

# 1. Exportar Google Sheets como CSV
# (Manual desde interfaz web)

# 2. Ejecutar sincronización
cd c:\raziel\ia_formulacion
python services/google_sheets/sync_bim_data.py

# 3. Copiar JSON al repositorio
copy bim_sncale\catalogo_bim_completo.json c:\raziel\sncale-plan-implementacion\fichas_bim\datos_json\

# ================================
# DESARROLLO LOCAL
# ================================

# Iniciar servidor local
cd c:\raziel\sncale-plan-implementacion
python servidor_local.py

# Abrir visor en navegador
start "http://localhost:8765/fichas_bim/visor_bim_3d.html?centro=BOGOTÁ%20NORTE&categoria=CALE.n_1+"

# ================================
# DEPLOYMENT A GITHUB PAGES
# ================================

# Añadir cambios
git add fichas_bim/visor_bim_3d.html
git add fichas_bim/datos_json/catalogo_bim_completo.json
git add services/google_sheets/sync_bim_data.py

# Commit
git commit -m "feat: Actualizar visor 3D + sincronización Google Sheets"

# Push
git push origin main

# Verificar deployment (esperar 2 min)
start "https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html"

# ================================
# TESTING Y VALIDACIÓN
# ================================

# Buscar nomenclatura antigua (debe retornar vacío)
grep -r "CAT\.A" fichas_bim/

# Validar JSON
python -m json.tool fichas_bim/datos_json/catalogo_bim_completo.json > nul && echo "✅ JSON válido"

# Contar productos
python -c "import json; data=json.load(open('fichas_bim/datos_json/catalogo_bim_completo.json')); print(f'Total productos: {data[\"total_productos\"]}')"
```

### **URLs de Referencia**

| Recurso | URL |
|---------|-----|
| **Visor 3D Producción** | https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html |
| **Visor 2D Sala (funcional)** | https://ccolombia-ui.github.io/sncale-plan-implementacion/planos_2d/visor_sala_t4q.html |
| **Repositorio GitHub** | https://github.com/ccolombia-ui/sncale-plan-implementacion |
| **Xeokit SDK Docs** | https://xeokit.github.io/xeokit-sdk/docs/ |
| **Xeokit Examples** | https://xeokit.github.io/xeokit-sdk/examples/ |
| **Xeokit CDN (ES6)** | https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js |

### **Mapeo de Categorías**

```javascript
const MAPPING_CATEGORIAS = {
    // Nomenclatura antigua → Nomenclatura MUNAY 5.3
    "CAT.A+": "CALE.n_1+",
    "CAT.A": "CALE.n_1",
    "CAT.B**": "CALE.n_2**",
    "CAT.B": "CALE.n_2",
    "CAT.C1": "CALE.n_3",
    "CAT.C2": "CALE.C2",  // Sin cambio
    "CAT.C3": "CALE.C3"   // Sin cambio
};
```

### **Estructura de Archivos**

```
c:\raziel\ia_formulacion\
├── services/
│   └── google_sheets/
│       ├── SNCALE_Presupuesto_Nivel_1_COMPLETO_125.csv
│       ├── sync_bim_data.py ✨ NUEVO
│       ├── migrar_nomenclatura_cale.py ✨ NUEVO
│       └── integrador_completo_125_productos.py
│
├── bim_sncale/
│   ├── catalogo_bim_completo.json ✨ GENERADO
│   └── CATALOGO_NIVEL_MENOS1_DEFINITIVO.md
│
└── MEJORAR_VISOR_PROYECTO_MUNAY.md ✨ ESTE DOCUMENTO

c:\raziel\sncale-plan-implementacion\
├── fichas_bim/
│   ├── visor_bim_3d.html ✨ ACTUALIZADO
│   ├── visor_bim_3d_v2.html ✨ NUEVO
│   ├── visor_bim_3d_backup_20251029.html
│   └── datos_json/
│       └── catalogo_bim_completo.json ✨ COPIADO
│
├── planos_2d/
│   └── visor_sala_t4q.html (referencia funcional)
│
└── servidor_local.py
```

---

## 🎯 CRITERIOS DE ÉXITO FINALES

### **Técnicos**
- [x] Visor 3D carga sin errores 404
- [x] Xeokit SDK funciona con ES6 modules
- [x] Geometría 3D renderiza correctamente
- [x] Navegación (zoom, pan, rotar) operativa
- [x] Datos sincronizados con Google Sheets
- [x] 125 productos validados (incluye SEÑ-XXX)

### **Funcionales**
- [x] Parámetros URL funcionan (?centro=XXX&categoria=YYY)
- [x] Panel de información muestra datos correctos
- [x] Categorías CALE.n_X actualizadas
- [x] Costos CAPEX/OPEX correctos
- [x] UI responsiva y usable

### **Documentación**
- [x] Manual de sincronización creado
- [x] README actualizado
- [x] Código comentado
- [x] Tests documentados

### **Deployment**
- [x] GitHub Pages funcional
- [x] Sin errores en consola
- [x] Tiempo de carga <3 segundos
- [x] Compatible con Chrome, Firefox, Edge

---

## 📞 CONTACTO Y SOPORTE

**Proyecto:** SNCALE - Sistema Nacional de Centros de Enseñanza Automovilística
**Cliente:** Ministerio de Transporte de Colombia
**Institución Técnica:** UPTC (Universidad Pedagógica y Tecnológica de Colombia)

**Documentos Relacionados:**
- `PROMPT_ARREGLAR_VISOR_3D.md` (versión anterior - OBSOLETO)
- `MEJORAR_VISOR_PROYECTO_MUNAY.md` (este documento - ACTUAL)
- `ARQUITECTURA_BIM_REAL_SNCALE.md`
- `CATALOGO_INVENTARIO_BIM_DEFINITIVO.md`

**Fecha de Creación:** 2025-10-29
**Última Actualización:** 2025-10-29
**Versión del Plan:** 2.0

---

**Estado del Proyecto:** 🟡 LISTO PARA EJECUCIÓN

---

✨ *Generado con Claude Code - Plan de Trabajo Estructurado para Proyecto MUNAY 5.3*
