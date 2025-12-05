# 📋 ESTADO DEL PLAN SNCALE - RESUMEN EJECUTIVO
**Fecha:** 2025-11-04  
**Proyecto:** Sistema Nacional de Centros de Aplicación de Lenguas Extranjeras (SNCALE)

---

## ✅ COMPLETADO

### **1. Arquitectura de Datos L0-L5** ✅
- [x] **L0**: Catálogo de componentes base (91 componentes)
- [x] **L1**: Configuraciones básicas (estación de trabajo)
- [x] **L2**: Configuraciones compuestas (sala 24 cubículos, sala formación)
- [x] **L3**: Tipos de CALE definidos (n_1, n_2, n_3, satélites C2-C5)
- [x] **L4**: Instancias en 197 nodos (56 principales + 141 satélites)
- [x] **L5**: Consolidación nacional (totales agregados)

**Archivos Clave:**
- ✅ `TABLAS_L3_VARIANTES_RECURSIVAS.json` (con corrección: 17+3=20 CALE.n_1)
- ✅ `TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json` (datos oficiales Google Sheets)
- ✅ `tipos_l3_con_instancias_l4.json` (estructura jerárquica para mapa)

---

### **2. Visualización Interactiva** ✅
- [x] **Mapa Interactivo Leaflet** (http://localhost:8080/visualizacion/mapa-interactivo.html)
  - ✅ Sidebar jerárquico L3 → L4 (Opción C - 2 niveles + mapa)
  - ✅ 56 nodos principales con marcadores coloreados
  - ✅ Panel flotante con 4 tabs (General, Infraestructura, Cluster, Presupuesto)
  - ✅ Búsqueda autocomplete
  - ✅ Relaciones jerárquicas (6 nodos principales → 32 subnodos)
  - ✅ Líneas de conexión en mapa
  - ✅ Control de capas (principales, satélites, conexiones)

**Archivos:**
- ✅ `visualizacion/mapa-interactivo.html` (~500 líneas)
- ✅ `visualizacion/mapa-interactivo.js` (~650 líneas)
- ✅ `data/relaciones_jerarquicas_nodos.json` (6 nodos con subnodos)
- ✅ `data/nodos_completos_mapa.json` (56 nodos procesados)

**Análisis UX:**
- ✅ `docs/ANALISIS_UX_NAVEGACION_JERARQUICA.md` (comparación 3 opciones)
- ✅ Recomendación: Opción C (85% más eficiente que alternativas)

---

### **3. Documentación Técnica** ✅
- [x] Análisis de arquitectura L3/L4/L5
- [x] Corrección de errores (20 vs 17 nodos CALE.n_1.base)
- [x] Guía de mapa interactivo
- [x] Análisis comparativo de visualización

**Archivos:**
- ✅ `ANALISIS_MEJOR_ESTRUCTURA_ANEXO_B.md`
- ✅ `RESUMEN_FINAL_ANEXO_B.md`
- ✅ `GUIA_MAPA_INTERACTIVO_197_NODOS.md`
- ✅ `ANALISIS_FICHAS_vs_MAPA_JERARQUICO.md`
- ✅ `ANALISIS_UX_NAVEGACION_JERARQUICA.md`

---

## ⚠️ PENDIENTE

### **1. Datos de Satélites (141 nodos)** ⚠️
**Estado:** Solo tenemos referencia, no datos completos

**Faltante:**
- [ ] Coordenadas geográficas (lat/lon) de 141 satélites
- [ ] Códigos DANE de municipios satélite
- [ ] Demanda estimada anual por satélite
- [ ] Asignación de satélites a nodos principales (clustering)
- [ ] Clasificación C2/C3/C4/C5 por demanda

**Acción Requerida:**
```
📊 Fuente de datos: Google Sheets (pestañas satélites)
🔗 URL: https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/
📌 Pestañas pendientes: "Satélites C2", "Satélites C3", "Satélites C4", "Satélites C5"
```

**Archivo a crear:**
- `data/satelites_completos_141_nodos.json`

---

### **2. Relaciones Jerárquicas Completas** ⚠️
**Estado:** Solo 6 nodos con relaciones (32 subnodos mapeados)

**Faltante:**
- [ ] Relaciones para los otros 50 nodos principales
- [ ] Asignación precisa de satélites a nodos (clustering por proximidad)
- [ ] Matriz de distancias (nodo principal ↔ satélites)
- [ ] Criterios de asignación (distancia max, demanda min)

**Acción Requerida:**
```python
# Script pendiente: scripts/generar_clustering_satelites.py
# Entrada: 
#   - nodos_principales.json (56 nodos con coords)
#   - satelites.json (141 satélites con coords)
# Salida:
#   - relaciones_jerarquicas_completas.json (56 nodos → 141 satélites)
# Algoritmo: Nearest neighbor + capacidad máxima por cluster
```

---

### **3. Exportación de Datos** ⏳
**Estado:** Botón "Exportar" en mapa pero sin implementación

**Faltante:**
- [ ] Exportar selección a PDF (ficha técnica individual)
- [ ] Exportar cluster a Excel (nodo + todos sus subnodos)
- [ ] Exportar vista completa a GeoJSON (para GIS)
- [ ] Exportar resumen nacional a CSV (métricas L5)

**Acción Requerida:**
- Implementar función `exportarDatos()` en `mapa-interactivo.js`
- Librerías: jsPDF, xlsx.js, o generar en backend Python

---

### **4. Filtros Avanzados** ⏳
**Estado:** Búsqueda básica implementada

**Faltante:**
- [ ] Filtro por rango de demanda (slider 0-80k eval/año)
- [ ] Filtro por departamento (dropdown)
- [ ] Filtro por presupuesto CAPEX (min/max)
- [ ] Filtro combinado (departamento + demanda)
- [ ] Vista comparativa (seleccionar múltiples nodos lado a lado)

---

### **5. Heatmap de Demanda** ⏳
**Estado:** Checkbox existe pero sin implementación

**Faltante:**
- [ ] Layer de heatmap con Leaflet.heat
- [ ] Gradiente de color por demanda (rojo=alta, azul=baja)
- [ ] Toggle on/off independiente

**Acción Requerida:**
```javascript
// Agregar a mapa-interactivo.js
layers.heatmap = L.heatLayer(
    nodos.map(n => [n.coords.lat, n.coords.lon, n.demanda_anual]),
    {radius: 25, blur: 15, maxZoom: 17}
);
```

---

### **6. Integración con Google Sheets (Sincronización)** ⏳
**Estado:** Datos copiados manualmente

**Faltante:**
- [ ] Script de sincronización automática (Google Sheets API)
- [ ] Actualización incremental (solo cambios)
- [ ] Notificación de cambios (email/webhook)
- [ ] Versionado de datos (histórico de cambios)

**Acción Requerida:**
```python
# scripts/sincronizar_google_sheets.py
# Requiere: google-auth, gspread
# Función: Descargar automáticamente todas las pestañas
# Salida: Actualizar archivos JSON en data/
```

---

### **7. Documentación de Usuario** ⏳
**Faltante:**
- [ ] Manual de usuario del mapa (con screenshots)
- [ ] Tutorial interactivo (onboarding)
- [ ] Glosario de términos (CALE, satélite, cluster, etc.)
- [ ] FAQ (preguntas frecuentes)

---

### **8. Anexo B Formal (Documento Final)** ⏳
**Estado:** Secciones B10-B70 generadas, pero pendiente consolidación

**Faltante:**
- [ ] Anexo B completo en formato Word/PDF
- [ ] Tablas de presupuesto (B60 actualizado con valores correctos)
- [ ] Catálogo L0 con fichas técnicas (B70 con imágenes)
- [ ] Diagrama de arquitectura L0-L5 (visual)
- [ ] Cronograma de implementación (5 años)

**Archivos a generar:**
- `ANEXO_B_COMPLETO_FINAL.docx` (documento Word oficial)
- `ANEXO_B_COMPLETO_FINAL.pdf` (versión PDF)

---

## 📊 MÉTRICAS ACTUALES

### **Datos Cargados:**
| Nivel | Descripción | Cantidad | Estado |
|-------|-------------|----------|--------|
| L0 | Componentes base | 91 | ✅ Completo |
| L1 | Estación trabajo | 1 | ✅ Completo |
| L2 | Salas (cubículos + formación) | 2 | ✅ Completo |
| L3 | Tipos CALE | 8 | ✅ Completo |
| L4 (Principales) | Nodos CALE n_1/n_2/n_3 | 56 | ✅ Completo |
| L4 (Satélites) | Nodos C2-C5 | 141 | ⚠️ Solo referencia |
| L5 | Totales nacionales | 1 | ✅ Completo |
| **TOTAL** | **Nodos mapeados** | **56/197** | **28% completo** |

### **Relaciones Jerárquicas:**
| Nodo Principal | Subnodos Mapeados | Estado |
|----------------|-------------------|--------|
| NODO_01 (Bogotá Sur) | 7 | ✅ |
| NODO_03 (Bucaramanga) | 6 | ✅ |
| NODO_04 (Cali) | 6 | ✅ |
| NODO_07 (Mosquera) | 5 | ✅ |
| NODO_10 (Medellín) | 8 | ✅ |
| NODO_02 (Bogotá Norte) | 0 | ⚠️ |
| **Otros 50 nodos** | 0 | ⚠️ Pendiente |
| **TOTAL** | **32/141** | **23% completo** |

### **Presupuesto Nacional (L5):**
| Concepto | Valor | Estado |
|----------|-------|--------|
| CAPEX Total | $206.7B | ✅ Calculado |
| OPEX Anual | $135.5B | ✅ Calculado |
| Presupuesto 5 años | $884.2B | ✅ Calculado |
| Capacidad Total | 2.56M eval/año | ✅ Calculado |
| Demanda Total | 1.40M eval/año | ⚠️ Parcial (solo 56 nodos) |
| Tasa de Cobertura | 183% | ⚠️ Parcial |

---

## 🎯 PRIORIDADES INMEDIATAS

### **Prioridad 1: Completar Datos de Satélites** 🔥
**Impacto:** Crítico (sin esto, solo tenemos 28% del sistema completo)

**Tareas:**
1. ✅ Identificar pestañas de satélites en Google Sheets
2. ⏳ Extraer coordenadas de 141 municipios satélite
3. ⏳ Extraer demanda estimada (o calcular con criterio)
4. ⏳ Generar `satelites_completos_141_nodos.json`
5. ⏳ Actualizar mapa interactivo con 197 marcadores

**Tiempo Estimado:** 2-3 horas  
**Bloqueador:** Acceso a Google Sheets o CSV con datos completos

---

### **Prioridad 2: Clustering Automático** 🔥
**Impacto:** Alto (necesario para mostrar relaciones completas)

**Tareas:**
1. ⏳ Script de clustering por proximidad geográfica
2. ⏳ Asignar cada satélite a nodo principal más cercano
3. ⏳ Validar distancia máxima (ej: <150km)
4. ⏳ Actualizar `relaciones_jerarquicas_nodos.json` con 56 nodos
5. ⏳ Probar visualización de 197 conexiones en mapa

**Tiempo Estimado:** 1-2 horas  
**Dependencia:** Prioridad 1 (necesita coords de satélites)

---

### **Prioridad 3: Exportación Básica** 🟡
**Impacto:** Medio (funcionalidad útil pero no bloqueante)

**Tareas:**
1. ⏳ Implementar exportar nodo a PDF (usando jsPDF)
2. ⏳ Implementar exportar cluster a Excel (usando xlsx.js)
3. ⏳ Botón "Descargar datos" en panel flotante

**Tiempo Estimado:** 1-2 horas

---

### **Prioridad 4: Heatmap de Demanda** 🟡
**Impacto:** Medio (visualización adicional)

**Tareas:**
1. ⏳ Agregar librería Leaflet.heat
2. ⏳ Implementar capa de heatmap
3. ⏳ Toggle funcional en controles

**Tiempo Estimado:** 30 min - 1 hora

---

### **Prioridad 5: Anexo B Final** 🟢
**Impacto:** Bajo-Medio (deliverable final pero datos ya existen)

**Tareas:**
1. ⏳ Consolidar secciones B10-B70
2. ⏳ Generar tablas de presupuesto actualizadas
3. ⏳ Exportar a Word/PDF con formato oficial

**Tiempo Estimado:** 2-3 horas

---

## 🚀 PRÓXIMOS PASOS RECOMENDADOS

### **Opción A: Completar Mapa (Recomendado)** ✅
1. 🔥 **Ahora:** Extraer datos de satélites desde Google Sheets
2. 🔥 **Después:** Generar clustering automático (56 → 141)
3. 🟡 **Opcional:** Agregar heatmap y exportación

**Resultado:** Mapa 100% funcional con 197 nodos visibles

---

### **Opción B: Generar Anexo B Final** 📄
1. Consolidar documentación existente
2. Generar documento Word formal
3. Exportar a PDF

**Resultado:** Entregable para cliente/stakeholders

---

### **Opción C: Automatizar Sincronización** 🔄
1. Configurar Google Sheets API
2. Script de actualización automática
3. Notificaciones de cambios

**Resultado:** Sistema autónomo y actualizable

---

## ❓ DECISIÓN REQUERIDA

**¿Qué quieres hacer primero?**

1. **Completar el mapa con los 141 satélites** (necesito acceso a Google Sheets o CSV)
2. **Generar el Anexo B completo en Word/PDF** (documentación formal)
3. **Revisar algo específico** (¿qué aspecto del plan quieres profundizar?)

---

## 📁 ESTRUCTURA DE ARCHIVOS ACTUAL

```
sncale-plan-implementacion/
├── data/
│   ├── tipos_l3_con_instancias_l4.json ✅
│   ├── nodos_completos_mapa.json ✅ (56 nodos)
│   ├── relaciones_jerarquicas_nodos.json ✅ (6 nodos → 32 subnodos)
│   └── satelites_completos_141_nodos.json ⚠️ PENDIENTE
├── visualizacion/
│   ├── mapa-interactivo.html ✅
│   └── mapa-interactivo.js ✅
├── scripts/
│   ├── construir_relaciones_nodos.py ✅
│   ├── generar_nodos_completos.py ✅
│   ├── extraer_relaciones_jerarquicas.py ✅
│   └── sincronizar_google_sheets.py ⚠️ PENDIENTE
├── docs/
│   ├── ANALISIS_UX_NAVEGACION_JERARQUICA.md ✅
│   ├── GUIA_MAPA_INTERACTIVO_197_NODOS.md ✅
│   └── ANALISIS_FICHAS_vs_MAPA_JERARQUICO.md ✅
└── TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json ✅
```

---

**🎯 Estamos en: 28% del sistema completo (56/197 nodos con datos geoespaciales)**  
**🚀 Siguiente hito: 100% del sistema (197/197 nodos visualizables en mapa)**
