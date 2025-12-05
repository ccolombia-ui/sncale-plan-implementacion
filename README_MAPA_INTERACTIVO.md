# � SNCALE - Sistema Nacional CALE | UPTC

## 📋 ¿Qué es CALE?

**CALE** = **C**entro de **A**plicación para **L**icencias de Conducción **E**scuela

Son instalaciones especializadas donde los aspirantes a licencias de conducción realizan sus exámenes teóricos y prácticos, conforme a la normativa del Ministerio de Transporte de Colombia.

**NO es un centro de idiomas.** Es un proyecto de **infraestructura de evaluación vial** desarrollado en colaboración con la **UPTC (Universidad Pedagógica y Tecnológica de Colombia)**.

---

## 📊 Información General

**Proyecto:** Plan Nacional de Implementación SNCALE  
**Institución:** Universidad Pedagógica y Tecnológica de Colombia (UPTC)  
**Nivel:** L4 - Nodos Municipales CALE  
**Nodos L4:** 197 (56 Principales + 141 Satélites)  
**Cobertura:** 32 Departamentos  
**Capacidad Total:** 2.56M evaluaciones/año

💡 **Nota:** Los datos de presupuesto consolidado ($884B) se encuentran en el **Dashboard L5** (nivel nacional), no en L4 (nodos individuales).

---

## 🚀 Inicio Rápido

### **Visualizar el Mapa Interactivo:**

1. **Iniciar el servidor:**
   ```cmd
   iniciar_servidor.bat
   ```
   
2. **Abrir en navegador:**
   - **Página principal:** http://localhost:8085/index.html
   - **Mapa interactivo:** http://localhost:8085/visualizacion/mapa-interactivo.html
   - **Diagnóstico:** http://localhost:8085/visualizacion/test-carga-datos.html

---

## 📁 Estructura del Proyecto

```
sncale-plan-implementacion/
├── index.html                          ✅ Página principal (NUEVO)
├── iniciar_servidor.bat                ✅ Script para iniciar servidor
│
├── visualizacion/
│   ├── mapa-interactivo.html          ✅ Mapa completo con 197 nodos
│   ├── mapa-interactivo.js            ✅ JavaScript actualizado
│   └── test-carga-datos.html          ✅ Herramienta de diagnóstico
│
├── data/
│   ├── nodos_completos_mapa.json      ✅ 56 nodos principales
│   ├── satelites_completos_141_nodos.json  ✅ 141 satélites
│   ├── relaciones_jerarquicas_completas.json  ✅ Relaciones completas
│   └── tipos_l3_con_instancias_l4.json     📄 Tipos L3 con instancias
│
├── scripts/
│   ├── extraer_satelites_completos.py      ✅ Extracción de satélites
│   ├── generar_relaciones_completas.py     ✅ Generación de jerarquías
│   ├── generar_nodos_completos.py          ✅ Procesamiento de nodos
│   └── construir_relaciones_nodos.py       📄 Relaciones básicas
│
└── docs/
    ├── ACTUALIZACION_MAPA_197_NODOS.md    📄 Resumen de actualización
    ├── ESTADO_PLAN_SNCALE.md              📄 Estado del plan completo
    └── ANALISIS_UX_NAVEGACION_JERARQUICA.md  📄 Análisis UX
```

---

## 🗺️ Características del Mapa Interactivo

### **Visualización:**
- ✅ **197 nodos georreferenciados** (coordenadas lat/lon precisas)
- ✅ **Marcadores diferenciados:** Principales (24px) vs Satélites (16px)
- ✅ **9 categorías de colores:**
  - 🔴 Cat.A+ Premium (3 nodos)
  - 🟠 Cat.A Base (17 nodos)
  - 🟡 Cat.B** Plus (16 nodos)
  - 🟢 Cat.B Base (4 nodos)
  - 🔵 Cat.C1 Provincial (16 nodos)
  - ⬤ C2 Satélites (31 nodos)
  - ⬤ C3 Satélites (69 nodos)
  - ⬤ C4 Satélites (27 nodos)
  - ⬤ C5 Satélites (14 nodos)

### **Interactividad:**
- 🔍 **Búsqueda:** Encuentra cualquier municipio o nodo
- 🗂️ **Sidebar jerárquico:** Navega por categorías expandibles
- 🔗 **Relaciones visuales:** Líneas de conexión entre nodos principales y satélites
- 📊 **Panel flotante:** 4 tabs con información detallada
- 🔲 **Toggles de capas:** Muestra/oculta principales, satélites, conexiones
- 🎯 **Click navigation:** Haz clic en nodos para ver detalles y conexiones

### **Datos Mostrados:**
- 📍 Ubicación (departamento, municipio, coordenadas)
- 📊 Demanda estimada anual (evaluaciones/año)
- 🏢 Infraestructura (dirección, área, arriendo)
- 💰 Presupuesto (CAPEX, OPEX, totales)
- 🔗 Cluster (satélites vinculados, distancias)

---

## 📊 Distribución de Nodos

### **Por Categoría:**
| Categoría | Tipo | Cantidad | Demanda Promedio |
|-----------|------|----------|------------------|
| Cat.A+ | CALE Metropolitano Premium | 3 | 73,283 eval/año |
| Cat.A | CALE Metropolitano Base | 17 | 25,000 eval/año |
| Cat.B** | CALE Regional Plus | 16 | 8,500 eval/año |
| Cat.B | CALE Regional Base | 4 | 5,200 eval/año |
| Cat.C1 | CALE Provincial | 16 | 2,800 eval/año |
| C2 | Satélite Alta Demanda | 31 | 3,500 eval/año |
| C3 | Satélite Media Demanda | 69 | 2,000 eval/año |
| C4 | Satélite Baja Demanda | 27 | 1,250 eval/año |
| C5 | Satélite Muy Baja Demanda | 14 | 750 eval/año |
| **TOTAL** | | **197** | |

### **Por Región:**
- 🗺️ Andina: 98 nodos (49.7%)
- 🌴 Caribe: 42 nodos (21.3%)
- 🏔️ Pacífico: 28 nodos (14.2%)
- 🌾 Orinoquía: 18 nodos (9.1%)
- 🌳 Amazonía: 11 nodos (5.6%)

---

## 💾 Datos Disponibles

### **Archivos JSON:**

1. **nodos_completos_mapa.json** (56 nodos principales)
   - Estructura: `{metadata, nodos: {NODO_01: {...}, ...}}`
   - Campos: coords, demanda, infraestructura, presupuesto
   - Tamaño: ~85KB

2. **satelites_completos_141_nodos.json** (141 satélites)
   - Estructura: `{metadata, satelites: [{...}, ...]}`
   - Campos: coords, categoria, nodo_principal, distancia
   - Tamaño: ~68KB

3. **relaciones_jerarquicas_completas.json** (56 → 141)
   - Estructura: `{metadata, relaciones: {NODO_01: {info, subnodos}, ...}}`
   - Relaciones: 51 nodos con satélites, 5 sin satélites
   - Tamaño: ~72KB

---

## 🔧 Scripts de Generación

### **1. Extraer Satélites:**
```bash
python scripts\extraer_satelites_completos.py
```
- **Entrada:** `arquitectura_red_cale_nacional_MAPEADO.csv`
- **Salida:** `data/satelites_completos_141_nodos.json`
- **Función:** Extrae todos los satélites con coordenadas y datos de clustering

### **2. Generar Relaciones:**
```bash
python scripts\generar_relaciones_completas.py
```
- **Entrada:** `nodos_completos_mapa.json` + `satelites_completos_141_nodos.json`
- **Salida:** `data/relaciones_jerarquicas_completas.json`
- **Función:** Asigna satélites a nodos principales, calcula distancias

### **3. Procesar Nodos:**
```bash
python scripts\generar_nodos_completos.py
```
- **Entrada:** `TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json`
- **Salida:** `data/nodos_completos_mapa.json`
- **Función:** Enriquece nodos con tipos L3, colores, categorías

---

## 🎯 Casos de Uso

### **1. Consultar Nodo Específico:**
1. Abrir mapa interactivo
2. Buscar en barra superior (ej: "Tunja")
3. Click en resultado
4. Ver panel con 4 tabs de información

### **2. Ver Cluster de un Nodo:**
1. Click en nodo principal en mapa
2. Ver líneas amarillas a satélites vinculados
3. Tab "Cluster" muestra lista de satélites
4. Click en satélite para navegar

### **3. Filtrar por Categoría:**
1. Sidebar → Click en categoría (ej: "Cat.A+")
2. Lista se expande mostrando nodos
3. Mapa resalta nodos de esa categoría
4. Click en nodo para detalles

### **4. Exportar Datos:**
1. Seleccionar nodo o cluster
2. Click en botón "Exportar"
3. Elegir formato (PDF, Excel, GeoJSON)
4. Descargar archivo generado

---

## 📈 Métricas del Sistema

### **Presupuesto Total (5 años):**
- 💰 **CAPEX:** $206.7B (23.4%)
- 💵 **OPEX:** $677.5B (76.6%)
  - Arrendamientos: $385B
  - Servicios públicos: $96.3B
  - Personal: $135.5B
  - Mantenimiento: $60.7B
- **TOTAL:** $884.2B

### **Capacidad y Demanda:**
- 📊 **Capacidad Total:** 2,562,400 evaluaciones/año
- 📈 **Demanda Estimada:** 1,404,280 evaluaciones/año
- ✅ **Tasa de Cobertura:** 183%
- 🎯 **Margen de Seguridad:** 83% de sobredimensionamiento

---

## 🔄 Actualizaciones Recientes

### **Versión 2.0 - 2025-11-04** ✅ COMPLETADO

**Cambios:**
- ✅ Integrados **141 satélites** (C2-C5) con coordenadas completas
- ✅ Generadas **relaciones jerárquicas completas** (56 → 141)
- ✅ Actualizado mapa interactivo para visualizar 197 nodos
- ✅ Marcadores diferenciados (principales 24px, satélites 16px)
- ✅ 9 categorías en sidebar (desglose C2/C3/C4/C5)
- ✅ Estadísticas actualizadas en footer
- ✅ Página de inicio con resumen ejecutivo
- ✅ Scripts de generación automatizados

**Archivos Modificados:**
- `visualizacion/mapa-interactivo.html`
- `visualizacion/mapa-interactivo.js`
- `data/relaciones_jerarquicas_completas.json`
- `scripts/generar_relaciones_completas.py`
- `scripts/extraer_satelites_completos.py`

**Archivos Nuevos:**
- `index.html` (página principal)
- `iniciar_servidor.bat` (script de inicio)
- `data/satelites_completos_141_nodos.json`
- `docs/ACTUALIZACION_MAPA_197_NODOS.md`

---

## 🐛 Solución de Problemas

### **Error 404 - File not found:**
**Causa:** Servidor iniciado desde directorio incorrecto  
**Solución:** Usar `iniciar_servidor.bat` o asegurar que estás en `C:\guezarel\sncale-plan-implementacion`

### **Mapa no carga nodos:**
**Causa:** Archivos JSON no generados o ruta incorrecta  
**Solución:** Ejecutar scripts de generación, verificar consola del navegador

### **Satélites muestran "undefined" en departamento:**
**Causa:** Campo `departamento` faltante en JSON  
**Solución:** ✅ Corregido en versión 2.0 (regenerar `relaciones_jerarquicas_completas.json`)

### **Servidor no inicia:**
**Causa:** Puerto ocupado o directorio incorrecto  
**Solución:** Cambiar puerto en `iniciar_servidor.bat` (ej: 8086)

---

## 📞 Soporte

**Desarrollador:** Agente IA - GitHub Copilot  
**Fecha:** 2025-11-04  
**Versión:** 2.0 (Mapa Completo)

**Documentación adicional:**
- `docs/ESTADO_PLAN_SNCALE.md` - Estado completo del plan
- `docs/ACTUALIZACION_MAPA_197_NODOS.md` - Resumen de actualización
- `docs/ANALISIS_UX_NAVEGACION_JERARQUICA.md` - Análisis de diseño UX

---

## 🎉 ¡Listo para Usar!

El sistema SNCALE está **100% funcional** con todos los 197 nodos mapeados y visualizables.

**Inicia el servidor y explora:** 
```cmd
iniciar_servidor.bat
```

Luego abre: http://localhost:8085/index.html

¡Disfruta del mapa interactivo! 🗺️✨
