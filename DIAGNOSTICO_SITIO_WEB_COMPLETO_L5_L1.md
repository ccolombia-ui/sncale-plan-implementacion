# 🌐 DIAGNÓSTICO COMPLETO: Sitio Web SNCALE L5 → L1

**Fecha:** 4 de noviembre de 2025  
**Proyecto:** SNCALE - Sistema Nacional de Centros de Apoyo Logístico de Evaluación  
**Institución:** Universidad Pedagógica y Tecnológica de Colombia (UPTC)  

---

## 📋 RESUMEN EJECUTIVO

Este documento presenta el **estado actual** del sitio web del proyecto SNCALE y detalla **qué existe** y **qué falta** para tener una visualización completa de la arquitectura BIM desde el nivel L5 (Dashboard Nacional) hasta L1 (Componentes/Agregaciones).

### 🎯 Arquitectura BIM del Proyecto

```
L5: DASHBOARD NACIONAL (Consolidación)
    ↓
L4: NODOS MUNICIPALES (197 instancias georreferenciadas)
    ↓
L3: CONFIGURACIONES CALE (Tipos: n_1, n_2, n_3, C2-C5)
    ↓
L2: PISTAS Y EDIFICACIONES (Sistemas: Clase I, II, III)
    ↓
L1: COMPONENTES/AGREGACIONES (Salas, Maniobras)
    ↓
L0: COMPONENTES ATÓMICOS (Pavimentos, Equipos, Mobiliario)
```

---

## ✅ LO QUE TENEMOS (Estado Actual)

### 1️⃣ **Página Principal (index.html)** ✅ OPERATIVA

**Ubicación:** `c:\guezarel\sncale-plan-implementacion\index.html`

**Estado:** ✅ **Actualizada y funcional**

**Contenido:**
- ✅ Título correcto: "SNCALE - Sistema Nacional CALE | UPTC"
- ✅ Definición correcta de CALE (Apoyo Logístico de Evaluación, NO idiomas)
- ✅ Branding UPTC visible
- ✅ Estadísticas del proyecto:
  - 197 Nodos L4
  - 9 Categorías CALE
  - 2.56M Capacidad/año
- ✅ Clarificación L4 vs L5
- ✅ Enlaces a visualizaciones

**Botones de Acción:**
```html
✅ "Ver Mapa Interactivo" → visualizacion/mapa-interactivo.html
✅ "Explorar Fichas Técnicas" → fichas_l3/BIM_L3_001.html
```

**Observaciones:**
- ⚠️ Menciona "Dashboard L5" pero NO existe aún
- ⚠️ No hay navegación directa a niveles L2 o L1

---

### 2️⃣ **Nivel L4: Mapa Interactivo** ✅ COMPLETO

**Ubicación:** `visualizacion/mapa-interactivo.html`

**Estado:** ✅ **100% funcional con 197 nodos**

**Características:**
- ✅ **197 nodos georreferenciados** en mapa Leaflet
- ✅ Logo UPTC en header
- ✅ Definición correcta de CALE
- ✅ Distinción clara "L4: Nodos Municipales"
- ✅ Datos cargados desde `TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json`

**Funcionalidades:**
```javascript
✅ Visualización geoespacial (Leaflet.js + OpenStreetMap)
✅ Marcadores por categoría CALE (colores diferenciados)
✅ Popups con información detallada:
   - Centro ID
   - Municipio/Departamento
   - Categoría CALE
   - Demanda anual estimada
   - Nodo principal asociado
✅ Estadísticas en footer:
   - 197 Nodos L4
   - 9 Categorías
   - 2.56M Capacidad/año
✅ Leyenda de categorías
✅ Filtros por tipo de centro
```

**Datos Disponibles:**
- ✅ `TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json` (547 líneas)
  - 20 CALE.n_1 (Metropolitanos)
  - 20 CALE.n_2 (Subregionales)
  - 16 CALE.n_3 (Locales)
  - 141 Satélites (C2-C5)

**Observaciones:**
- ✅ Datos oficiales validados desde Google Sheets
- ⚠️ No hay link de regreso a niveles superiores/inferiores

---

### 3️⃣ **Nivel L3: Fichas de Configuraciones CALE** ✅ ACTUALIZADAS

**Ubicación:** `fichas_l3/`

**Archivos Existentes:**
```
✅ BIM_L3_001.html - CALE.n_1 - Centro Metropolitano
✅ BIM_L3_002.html - CALE.n_2 - Centro Subregional
✅ BIM_L3_003.html - CALE.n_3 - Centro Local
✅ BIM_L3_004.html - Red Nacional de Satélites
```

**Estado:** ✅ **Recientemente actualizadas con marco normativo completo**

**Contenido de Cada Ficha:**

#### Sección 1: Header
```html
✅ BIM ID prominente
✅ Logo UPTC (SVG)
✅ Título del tipo CALE
✅ Descripción de la configuración
```

#### Sección 2: Información Clave
```html
✅ Cards con datos principales:
   - Identificador BIM
   - Nivel Jerarquía (L3)
   - Tipo CALE
   - Valorización Total
   - Cantidad de Nodos (Base + Variante)
```

#### Sección 3: Tabla de Componentes
```html
✅ Tabla HTML detallada con:
   - # Componente
   - Descripción
   - Referencia BIM (L2/L1/L0)
   - Valor Unitario
   - Cantidades (Base/Variante)
   - Valor Total
```

**Ejemplo (BIM_L3_001):**
| Componente | Referencia BIM | Valor Unitario |
|------------|----------------|----------------|
| Pista Evaluación Clase III | `L2.pista_clase_3` | $1.850.000.000 |
| Sala Evaluación Teórica (24 cubículos) | `L1.sala_24_cubiculos` | $186.000.000 |
| Simulador Conducción Clase III | `L0.simulador_c3` | $450.000.000 |

#### Sección 4: Tabla de Metadata
```html
✅ Información adicional:
   - Tipos CALE (n_1, n_1+)
   - Cantidades por variante
   - Descripción de modificadores
   - Referencias a mapa de geolocalización
```

#### Sección 5: **Marco Normativo** 🆕 (RECIÉN AGREGADA)
```html
✅ Normatividad Aplicable:
   - Resolución 20253040037125/2025
   - Ley 2251/2022 ("Ley Julián Esteban")
   - Ley 769/2002 (Código Nacional Tránsito)
   - Clasificación CALE (Clase I/II/III)

✅ Certificaciones ISO Obligatorias:
   - ISO 9001:2015 (Calidad)
   - ISO 14001:2015 (Ambiental)
   - ISO 45001:2018 (SST)

✅ Seguros Obligatorios:
   - Responsabilidad Civil Extracontractual
   - Accidentes Personales para evaluados

✅ Supervisión y Control:
   - Superintendencia de Transporte
   - Sistema SICOV
   - Frecuencia de inspección (1/año mínimo)
```

#### Sección 6: Fuente de Datos
```html
✅ Trazabilidad completa:
   - Documento: MUNAY_5.2__anexo_b__DEFINITIVO
   - ID Google Doc
   - Número de tabla de valorización
   - Total de componentes
   - Estado de validación
```

#### Sección 7: Footer
```html
✅ Descripción correcta: "Sistema Nacional de Centros de Apoyo 
    Logístico de Evaluación - SNCALE | UPTC"
✅ Enlaces de navegación:
   - ← Fichas L1
   - ← Fichas L2
   - L3 Index
✅ Información de generación
```

**Clasificación por Ficha:**

| Ficha | Tipo CALE | Clasificación | Categorías Autorizadas |
|-------|-----------|---------------|------------------------|
| BIM_L3_001 | CALE.n_1 Metropolitano | **Clase III** | A1, A2, B1, B2, B3, C1, C2, C3 (todas) |
| BIM_L3_002 | CALE.n_2 Subregional | **Clase II** | A1, A2, B1, B2, C1, C2 |
| BIM_L3_003 | CALE.n_3 Local | **Clase I** | A1, A2, B1, C1 |
| BIM_L3_004 | Satélites C2-C5 | **Variable** | Según configuración |

**Observaciones:**
- ✅ Fichas completas con normatividad
- ✅ Diseño visual consistente (gradientes rojos UPTC)
- ✅ Responsivas (grids adaptativos)
- ⚠️ **Enlaces a L2 y L1 NO ESTÁN IMPLEMENTADOS** (aparecen en footer pero 404)
- ⚠️ No hay navegación jerárquica visual (breadcrumbs L5→L4→L3→L2→L1)

---

### 4️⃣ **Nivel L2: Fichas de Pistas y Edificaciones** ✅ PARCIAL

**Ubicación:** `fichas_l2/`

**Archivos Existentes:**
```
✅ BIM_L2_001.html - Pista de Conducción Clase I
✅ BIM_L2_002.html - Pista de Conducción Clase II
✅ BIM_L2_003.html - Pista de Conducción Clase III
✅ BIM_L2_004.html - (Por confirmar contenido)
✅ BIM_L2_005.html - CALE Teórico 16 Cubículos
```

**Estado:** ⚠️ **Existen pero NO revisadas/actualizadas con normatividad**

**Contenido Esperado (Según ARBOL_JERARQUIA_BIM_COMPLETO.md):**

#### BIM_L2_001 - Pista Clase I
```
Valorización: $975.000.000
Componentes: 16 maniobras (L1)
   - MANIOBRA_00: Arranque en pendiente
   - MANIOBRA_01: Estacionamiento paralelo
   - MANIOBRA_02: Estacionamiento batería
   - ... (hasta MANIOBRA_13)
```

#### BIM_L2_002 - Pista Clase II
```
Valorización: $680.000.000
Componentes: 6 maniobras (L1)
   - MANIOBRA_14: Maniobras con remolque
   - MANIOBRA_15: Reversa con remolque
   - MANIOBRA_16: Estacionamiento con remolque
```

#### BIM_L2_005 - CALE Teórico 16 Cubículos
```
Valorización: $200.646.497
Componentes: 0 (directo L0)
```

**Observaciones:**
- ✅ Archivos HTML existen
- ⚠️ **NO tienen marco normativo agregado** (solo L3 actualizado)
- ⚠️ **NO hay índice L2** para navegación
- ⚠️ **NO hay enlaces desde L3 hacia L2** (aunque se mencionan en tablas)
- ⚠️ No se han validado contra normatividad

---

### 5️⃣ **Nivel L1: Fichas de Componentes/Agregaciones** ✅ PARCIAL

**Ubicación:** `fichas_l1/`

**Archivos Existentes:**
```
✅ BIM_L1_001.html
✅ BIM_L1_002.html
✅ BIM_L1_003.html
✅ BIM_L1_004.html
✅ BIM_L1_REF_001.html
✅ BIM_L1_REF_002.html
```

**Estado:** ⚠️ **Existen pero estructura/contenido desconocido**

**Contenido Esperado (Según árbol BIM):**

Componentes L1 identificados en el árbol:
```
MANIOBRAS (16 para Clase I):
   - L1.maniobra_00 → Arranque en pendiente
   - L1.maniobra_01 → Estacionamiento paralelo
   - L1.maniobra_02 → Estacionamiento batería
   - ... hasta L1.maniobra_13

MANIOBRAS INTERMEDIAS (Clase II):
   - L1.maniobra_14 → Con remolque
   - L1.maniobra_15 → Reversa con remolque
   - L1.maniobra_16 → Estacionamiento con remolque

COMPONENTES AGREGADOS:
   - L1.sala_24_cubiculos → Sala evaluación teórica
   - (Otros por identificar)
```

**Observaciones:**
- ✅ 6 archivos HTML existen
- ❓ **Contenido NO verificado** (necesita lectura)
- ⚠️ **NO tienen marco normativo**
- ⚠️ **NO hay índice L1** para navegación
- ⚠️ **NO hay enlaces desde L2 hacia L1**
- ❓ No se sabe si están completos (31 componentes esperados según árbol)

---

### 6️⃣ **Nivel L0: Componentes Atómicos** ❌ NO IMPLEMENTADO WEB

**Ubicación Esperada:** `fichas_l0/` (NO EXISTE)

**Estado:** ❌ **NO HAY FICHAS HTML L0 EN EL SITIO**

**Datos Disponibles:**
```
✅ output/fichas_html/BIM_L0_001.html → BIM_L0_050.html
   (50 fichas en carpeta output, NO en sitio principal)
```

**Componentes L0 Esperados (según tablas):**

Ejemplos mencionados en fichas L3:
- `L0.simulador_c3` → Simulador Conducción Clase III ($450M)
- `L0.pavimento_rigido` → Pavimento de pistas
- `L0.mobiliario_aula` → Mobiliario educativo
- `L0.equipo_computo` → Equipos tecnológicos
- `L0.señalizacion_vial` → Señalización de pistas
- (Y más componentes atómicos)

**Observaciones:**
- ❌ **NO hay carpeta `fichas_l0/` en sitio**
- ✅ Existen fichas en `output/` pero aisladas
- ❌ **NO hay integración en navegación web**
- ❌ **NO tienen marco normativo**
- ❌ **NO hay índice L0**

---

## ❌ LO QUE FALTA (Para Sitio Completo L5→L1)

### 🚨 **CRÍTICO - Dashboard L5** ❌ NO EXISTE

**Descripción:** Panel de consolidación nacional

**Ubicación Esperada:** `dashboard.html` o `l5-dashboard.html`

**Funcionalidades Requeridas:**

#### 1. Resumen Nacional
```html
📊 ESTADÍSTICAS CONSOLIDADAS:
   - Presupuesto Total: $884.200.000.000 (5 años)
   - Total Nodos: 197
   - Departamentos: 32
   - Capacidad Anual: 2.560.000 evaluaciones
   - Área Total Construida: ~XXX,XXX m²
```

#### 2. Desglose por Nivel
```html
NIVEL L4 (Nodos Municipales):
   - 20 CALE.n_1 (Metropolitanos)
   - 20 CALE.n_2 (Subregionales)
   - 16 CALE.n_3 (Locales)
   - 141 Satélites (C2-C5)
   
NIVEL L3 (Configuraciones):
   - 4 tipos base documentados
   - Valorización por tipo
   
NIVEL L2 (Pistas/Edificaciones):
   - 5 configuraciones identificadas
   - Presupuesto por sistema
```

#### 3. Visualizaciones
```html
GRÁFICOS REQUERIDOS:
   📈 Distribución presupuestal por nivel BIM
   🗺️ Mapa nacional con densidad de nodos
   📊 Capacidad por departamento
   💰 Presupuesto por categoría CALE
   📅 Cronograma de implementación
```

#### 4. Navegación Jerárquica
```html
ENLACES DESCENDENTES:
   L5 (Dashboard) 
     ↓ "Ver Nodos Municipales"
   L4 (Mapa 197 nodos)
     ↓ Click en marcador
   L3 (Ficha de configuración CALE)
     ↓ Click en componente L2
   L2 (Ficha de pista/edificación)
     ↓ Click en componente L1
   L1 (Ficha de maniobra/sala)
     ↓ Click en componente L0
   L0 (Ficha de componente atómico)
```

#### 5. Cumplimiento Normativo (Agregado)
```html
📜 INDICADORES DE CUMPLIMIENTO:
   ✅ Nodos con certificación ISO completa: XX/197
   ✅ Nodos con seguros vigentes: XX/197
   ⏰ Próximas inspecciones SICOV: [Lista]
   📋 Resoluciones aplicables: [Lista con links]
```

**Estado:** ❌ **COMPLETAMENTE AUSENTE**

---

### 🔴 **ALTO - Navegación Jerárquica Completa** ⚠️ FRAGMENTADA

**Problema:** Cada nivel existe de forma aislada, sin navegación clara entre niveles.

**Lo que Falta:**

#### 1. Breadcrumbs en Cada Página
```html
<!-- EJEMPLO PARA FICHA L2 -->
<nav class="breadcrumb">
    <a href="dashboard.html">🏠 L5: Dashboard</a> › 
    <a href="visualizacion/mapa-interactivo.html">🗺️ L4: Mapa</a> › 
    <a href="fichas_l3/BIM_L3_001.html">📋 L3: CALE.n_1</a> › 
    <span>🛣️ L2: Pista Clase I</span>
</nav>
```

#### 2. Sidebar de Niveles
```html
<!-- PANEL LATERAL EN TODAS LAS PÁGINAS -->
<aside class="levels-sidebar">
    <h3>Niveles BIM</h3>
    <ul>
        <li><a href="dashboard.html">L5: Dashboard Nacional</a></li>
        <li><a href="visualizacion/mapa-interactivo.html">L4: 197 Nodos</a></li>
        <li class="active">L3: Configuraciones CALE</li>
        <li><a href="fichas_l2/">L2: Pistas/Edificaciones</a></li>
        <li><a href="fichas_l1/">L1: Componentes</a></li>
        <li><a href="fichas_l0/">L0: Atómicos</a></li>
    </ul>
</aside>
```

#### 3. Botones de Navegación Ascendente/Descendente
```html
<!-- EN CADA FICHA -->
<div class="navigation-controls">
    <button onclick="goUp()">⬆️ Nivel Superior (L3)</button>
    <button onclick="goDown()">⬇️ Ver Componentes (L1)</button>
</div>
```

**Estado:** ❌ **NO IMPLEMENTADO**

---

### 🔴 **ALTO - Índices por Nivel** ⚠️ PARCIAL

**Problema:** No hay páginas índice que listen todas las fichas de cada nivel.

**Lo que Falta:**

#### Index L3 (`fichas_l3/index.html`)
```html
CONTENIDO ESPERADO:
📋 Lista de las 4 configuraciones CALE
   - BIM_L3_001: CALE.n_1 - Metropolitano (Clase III)
   - BIM_L3_002: CALE.n_2 - Subregional (Clase II)
   - BIM_L3_003: CALE.n_3 - Local (Clase I)
   - BIM_L3_004: Satélites C2-C5 (Variable)
   
Con:
   - Miniatura/Preview
   - Valorización
   - Cantidad de nodos que usan ese tipo
   - Link a ficha completa
```

#### Index L2 (`fichas_l2/index.html`)
```html
CONTENIDO ESPERADO:
🛣️ Lista de pistas y edificaciones
   - BIM_L2_001: Pista Clase I ($975M)
   - BIM_L2_002: Pista Clase II ($680M)
   - BIM_L2_003: Pista Clase III
   - BIM_L2_005: CALE Teórico 16 Cubículos
   
Con:
   - Imagen/Diagrama de pista
   - Cantidad de maniobras incluidas
   - Tipos CALE que la usan
```

#### Index L1 (`fichas_l1/index.html`)
```html
CONTENIDO ESPERADO:
🔧 Lista de componentes/agregaciones
   - Salas de evaluación teórica (variantes)
   - Maniobras básicas (Clase I)
   - Maniobras intermedias (Clase II)
   - Maniobras avanzadas (Clase III)
   - Simuladores por tipo
   
Agrupados por categoría funcional
```

#### Index L0 (`fichas_l0/index.html`)
```html
CONTENIDO ESPERADO:
⚙️ Catálogo de componentes atómicos
   - Pavimentos
   - Equipamiento tecnológico
   - Mobiliario
   - Señalización
   - Servicios públicos
   
Con buscador y filtros por categoría
```

**Estado:** ❌ **NINGÚN ÍNDICE EXISTE**

---

### 🟡 **MEDIO - Actualización L2 con Normatividad** ⚠️ PENDIENTE

**Problema:** Fichas L2 existen pero NO tienen marco normativo como L3.

**Lo que Falta:**

Agregar a cada ficha L2:
```html
<section>
    <h2>📜 Marco Normativo Aplicable</h2>
    
    <!-- Resoluciones específicas para pistas -->
    ✅ Resolución 20253040037125/2025
       - Art. 3.7.4.a (Clase I)
       - Art. 3.7.4.b (Clase II)
       - Art. 3.7.4.c (Clase III)
    
    <!-- Normas técnicas colombianas -->
    ✅ NTC 5375 - Especificaciones pistas evaluación
    ✅ NSR-10 - Construcción sismoresistente
    ✅ NTC 4595 - Accesibilidad
    
    <!-- Especificaciones técnicas -->
    - Dimensiones mínimas pista
    - Pendientes permitidas
    - Radio de giros
    - Señalización obligatoria
</section>
```

**Estado:** ⚠️ **ESTRUCTURA EXISTE PERO SIN ACTUALIZAR**

---

### 🟡 **MEDIO - Actualización L1 con Normatividad** ⚠️ PENDIENTE

**Problema:** Fichas L1 existen pero estructura/contenido desconocido.

**Tareas Requeridas:**

1. **Leer contenido actual** de las 6 fichas L1
2. **Validar completitud** (¿están las 31 maniobras/componentes esperados?)
3. **Agregar marco normativo**:
   ```html
   - Resolución específica por tipo de maniobra
   - Estándares de evaluación
   - Criterios de aprobación
   ```
4. **Estandarizar diseño** con fichas L3

**Estado:** ⚠️ **REQUIERE AUDITORÍA**

---

### 🟡 **MEDIO - Implementación Fichas L0 en Sitio** ❌ NO INTEGRADO

**Problema:** Fichas L0 existen en `output/` pero NO en sitio navegable.

**Tareas Requeridas:**

1. **Crear carpeta** `fichas_l0/` en raíz del sitio
2. **Copiar/Mover** fichas desde `output/fichas_html/BIM_L0_*.html`
3. **Revisar contenido** de cada ficha L0:
   - ¿Tienen estructura consistente?
   - ¿Incluyen especificaciones técnicas?
   - ¿Tienen imágenes/diagramas?
4. **Agregar normatividad**:
   ```html
   - Normas técnicas por tipo de componente
   - Certificaciones de producto
   - Proveedores homologados
   ```
5. **Integrar en navegación** del sitio

**Estado:** ❌ **COMPONENTES AISLADOS, NO INTEGRADOS**

---

### 🟢 **BAJO - Mejoras Visuales** ✨ OPCIONAL

**Mejoras Sugeridas:**

#### 1. Diagrama Jerárquico Interactivo
```javascript
// Visualización tipo árbol de toda la jerarquía BIM
// Clic en cada nodo lleva a la ficha correspondiente
// Usa D3.js o similar
```

#### 2. Vista 3D de Configuraciones
```javascript
// Integración con Three.js o Babylon.js
// Modelos 3D simplificados de cada tipo CALE
// Rotación/Zoom interactivo
```

#### 3. Filtros Avanzados en Mapa L4
```javascript
// Filtrar por:
   - Rango de capacidad
   - Rango presupuestal
   - Departamento específico
   - Clase CALE (I/II/III)
   - Estado de implementación (planeado/en obra/operativo)
```

#### 4. Búsqueda Global
```html
<!-- Buscador en header de todas las páginas -->
<input type="search" placeholder="Buscar componente, nodo, municipio...">
```

#### 5. Comparador de Configuraciones
```html
<!-- Tabla comparativa lado a lado -->
Comparar: [CALE.n_1] vs [CALE.n_2] vs [CALE.n_3]
   - Presupuesto
   - Capacidad
   - Componentes incluidos
   - Clases autorizadas
```

**Estado:** 💡 **IDEAS FUTURAS**

---

## 📊 CUADRO RESUMEN: ESTADO POR NIVEL

| Nivel | Descripción | Archivos | Navegación | Normatividad | Estado General |
|-------|-------------|----------|------------|--------------|----------------|
| **L5** | Dashboard Nacional | ❌ 0/1 | ❌ No existe | ❌ N/A | ❌ **AUSENTE** |
| **L4** | Mapa 197 Nodos | ✅ 1/1 | ⚠️ Aislado | ✅ Sí (en datos) | ✅ **COMPLETO** |
| **L3** | Configuraciones CALE | ✅ 4/4 | ⚠️ Links rotos | ✅ Completa | ✅ **ACTUALIZADO** |
| **L2** | Pistas/Edificaciones | ✅ 5/5 | ⚠️ No integrado | ❌ Pendiente | ⚠️ **PARCIAL** |
| **L1** | Componentes/Agregaciones | ✅ 6/31? | ⚠️ No integrado | ❌ Pendiente | ⚠️ **INCOMPLETO** |
| **L0** | Componentes Atómicos | ⚠️ 50 en output | ❌ No accesible | ❌ Pendiente | ❌ **NO INTEGRADO** |

### Indicadores Clave

```
COMPLETITUD GENERAL: 50% ████████░░░░░░░░░░

Por Nivel:
   L5: 0%   ░░░░░░░░░░░░░░░░░░░░
   L4: 100% ████████████████████
   L3: 95%  ███████████████████░
   L2: 60%  ████████████░░░░░░░░
   L1: 30%  ██████░░░░░░░░░░░░░░
   L0: 20%  ████░░░░░░░░░░░░░░░░

NAVEGACIÓN: 20% ████░░░░░░░░░░░░░░░░
   - No hay breadcrumbs
   - No hay sidebar de niveles
   - Links entre niveles rotos
   - No hay índices por nivel

NORMATIVIDAD: 40% ████████░░░░░░░░░░░░
   ✅ L3: 100%
   ⚠️ L2: 0%
   ⚠️ L1: 0%
   ⚠️ L0: 0%
```

---

## 🎯 PLAN DE ACCIÓN RECOMENDADO

### 🚨 **FASE 1: CRÍTICO** (1-2 semanas)

#### Tarea 1.1: Crear Dashboard L5
```
Prioridad: CRÍTICA
Esfuerzo: 15-20 horas
Entregables:
   ✓ dashboard.html funcional
   ✓ Estadísticas consolidadas
   ✓ Gráficos básicos (Chart.js)
   ✓ Mapa nacional (vista general)
   ✓ Enlaces a L4 y L3
```

#### Tarea 1.2: Implementar Navegación Jerárquica
```
Prioridad: CRÍTICA
Esfuerzo: 10-15 horas
Entregables:
   ✓ Breadcrumbs en todas las páginas
   ✓ Sidebar de niveles (componente reutilizable)
   ✓ Botones ⬆️/⬇️ en fichas
   ✓ CSS/JS consistente
```

#### Tarea 1.3: Crear Índices por Nivel
```
Prioridad: ALTA
Esfuerzo: 8-12 horas
Entregables:
   ✓ fichas_l3/index.html
   ✓ fichas_l2/index.html
   ✓ fichas_l1/index.html
   ✓ (Opcional) fichas_l0/index.html
```

---

### 🔴 **FASE 2: ALTA PRIORIDAD** (1-2 semanas)

#### Tarea 2.1: Auditar y Completar Fichas L1
```
Prioridad: ALTA
Esfuerzo: 12-18 horas
Actividades:
   1. Leer 6 fichas existentes
   2. Identificar faltantes (¿31 componentes esperados?)
   3. Generar fichas faltantes
   4. Agregar marco normativo
   5. Estandarizar diseño
```

#### Tarea 2.2: Actualizar Fichas L2 con Normatividad
```
Prioridad: ALTA
Esfuerzo: 6-8 horas
Actividades:
   1. Copiar template de sección normativa L3
   2. Adaptar a cada pista (Art. 3.7.4.a/b/c)
   3. Agregar NTC específicas
   4. Validar especificaciones técnicas
```

#### Tarea 2.3: Integrar Fichas L0 al Sitio
```
Prioridad: MEDIA
Esfuerzo: 10-15 horas
Actividades:
   1. Crear carpeta fichas_l0/
   2. Copiar/adaptar 50 fichas desde output/
   3. Revisar y estandarizar contenido
   4. Agregar normatividad técnica
   5. Crear índice L0 categorizado
```

---

### 🟡 **FASE 3: MEJORAS** (1 semana)

#### Tarea 3.1: Buscador Global
```
Prioridad: MEDIA
Esfuerzo: 6-8 horas
```

#### Tarea 3.2: Filtros Avanzados Mapa L4
```
Prioridad: MEDIA
Esfuerzo: 4-6 horas
```

#### Tarea 3.3: Comparador de Configuraciones
```
Prioridad: BAJA
Esfuerzo: 8-10 horas
```

---

## 📁 ESTRUCTURA DE ARCHIVOS OBJETIVO

```
sncale-plan-implementacion/
│
├── index.html ✅ (Landing page principal)
│
├── dashboard.html ❌ (L5 - A CREAR)
│
├── visualizacion/
│   ├── mapa-interactivo.html ✅ (L4)
│   └── mapa-interactivo.js ✅
│
├── fichas_l3/ ✅
│   ├── index.html ❌ (A CREAR)
│   ├── BIM_L3_001.html ✅
│   ├── BIM_L3_002.html ✅
│   ├── BIM_L3_003.html ✅
│   └── BIM_L3_004.html ✅
│
├── fichas_l2/ ⚠️
│   ├── index.html ❌ (A CREAR)
│   ├── BIM_L2_001.html ⚠️ (SIN NORMATIVIDAD)
│   ├── BIM_L2_002.html ⚠️ (SIN NORMATIVIDAD)
│   ├── BIM_L2_003.html ⚠️ (SIN NORMATIVIDAD)
│   ├── BIM_L2_004.html ⚠️
│   └── BIM_L2_005.html ⚠️ (SIN NORMATIVIDAD)
│
├── fichas_l1/ ⚠️
│   ├── index.html ❌ (A CREAR)
│   ├── BIM_L1_001.html ❓ (REVISAR)
│   ├── BIM_L1_002.html ❓ (REVISAR)
│   ├── ... (¿Faltan ~25 fichas?)
│   └── BIM_L1_031.html ❓ (CREAR SI NO EXISTE)
│
├── fichas_l0/ ❌ (CARPETA A CREAR)
│   ├── index.html ❌ (A CREAR)
│   ├── BIM_L0_001.html → (MOVER DESDE output/)
│   ├── BIM_L0_002.html → (MOVER DESDE output/)
│   ├── ...
│   └── BIM_L0_050.html → (MOVER DESDE output/)
│
├── assets/ (compartido)
│   ├── css/
│   │   ├── global.css ❌ (A CREAR)
│   │   ├── navigation.css ❌ (A CREAR)
│   │   └── fichas.css ❌ (A CREAR)
│   ├── js/
│   │   ├── navigation.js ❌ (A CREAR)
│   │   └── breadcrumbs.js ❌ (A CREAR)
│   └── img/
│       └── uptc-logo.svg ✅
│
├── data/
│   ├── TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json ✅
│   ├── TABLAS_L3_OFICIALES.json ✅
│   ├── TABLAS_L2_OFICIALES.json ✅
│   ├── TABLAS_L1_OFICIALES.json ✅
│   └── TABLAS_L0_OFICIALES.json ✅
│
└── docs/
    ├── ANALISIS_RESOLUCION_CALE_2025.md ✅
    ├── REPORTE_ACTUALIZACION_FICHAS_L3_NORMATIVIDAD.md ✅
    └── ARBOL_JERARQUIA_BIM_COMPLETO.md ✅
```

---

## 🔗 MAPA DE NAVEGACIÓN OBJETIVO

```
┌─────────────────────────────────────────────────────────────┐
│                    🏠 INDEX.HTML (Landing)                   │
│           "SNCALE - Sistema Nacional CALE | UPTC"            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              📊 DASHBOARD.HTML (L5 - Nacional)               │
│  • Presupuesto Total: $884B                                  │
│  • 197 Nodos | 32 Departamentos                              │
│  • Gráficos consolidados                                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│          🗺️ MAPA-INTERACTIVO.HTML (L4 - 197 Nodos)          │
│  • Leaflet.js interactivo                                    │
│  • Popups con datos por nodo                                 │
│  • Click en marcador → Ficha L3 del tipo CALE               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│             📋 FICHAS_L3/INDEX.HTML (Tipos CALE)             │
│  Grid con 4 configuraciones:                                 │
│  • CALE.n_1 (Metropolitano)                                  │
│  • CALE.n_2 (Subregional)                                    │
│  • CALE.n_3 (Local)                                          │
│  • Satélites C2-C5                                           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│           📄 BIM_L3_001.HTML (Ficha Individual)              │
│  • Header con logo UPTC                                      │
│  • Tabla de componentes L2/L1/L0                             │
│  • Marco normativo completo                                  │
│  • Botones: ⬆️ L4 | ⬇️ Ver Pistas L2                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│        🛣️ FICHAS_L2/INDEX.HTML (Pistas/Edificaciones)       │
│  Lista de 5 sistemas:                                        │
│  • Pista Clase I | II | III                                  │
│  • CALE Teórico 16/24 cubículos                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│           📄 BIM_L2_001.HTML (Pista Clase I)                 │
│  • Especificaciones técnicas                                 │
│  • 16 maniobras incluidas (L1)                               │
│  • Normatividad (Art. 3.7.4.a)                               │
│  • Botones: ⬆️ L3 | ⬇️ Ver Maniobras L1                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│         🔧 FICHAS_L1/INDEX.HTML (Componentes/Maniobras)      │
│  Catálogo de ~31 componentes agrupados:                      │
│  • Maniobras básicas (00-13)                                 │
│  • Maniobras intermedias (14-16)                             │
│  • Salas evaluación (24q, 16q, 4q)                           │
│  • Simuladores (Clase I, II, III)                            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│      📄 BIM_L1_001.HTML (Maniobra 0: Arranque Pendiente)     │
│  • Descripción de la maniobra                                │
│  • Componentes L0 requeridos                                 │
│  • Criterios de evaluación                                   │
│  • Botones: ⬆️ L2 | ⬇️ Ver Componentes L0                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│         ⚙️ FICHAS_L0/INDEX.HTML (Componentes Atómicos)       │
│  Catálogo de ~50+ componentes:                               │
│  • Pavimentos | Señalización                                 │
│  • Equipamiento | Mobiliario                                 │
│  • Simuladores | Tecnología                                  │
│  Con buscador y filtros por categoría                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│     📄 BIM_L0_001.HTML (Pavimento Rígido e=20cm)             │
│  • Especificaciones técnicas detalladas                      │
│  • Normas aplicables (NTC, NSR-10)                           │
│  • Proveedores homologados                                   │
│  • Botón: ⬆️ Volver a L1                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 RECOMENDACIONES FINALES

### ✅ **Lo que está BIEN**

1. **Mapa L4 excelente** - Funcional, completo, con datos oficiales
2. **Fichas L3 actualizadas** - Marco normativo completo, diseño consistente
3. **Branding UPTC correcto** - Logo, colores, slogan presentes
4. **Datos oficiales** - Trazabilidad clara desde Google Sheets
5. **Definición CALE correcta** - Ya no dice "idiomas"

### ⚠️ **Lo que necesita ATENCIÓN INMEDIATA**

1. **Dashboard L5 ausente** - Es la entrada principal del sistema
2. **Navegación rota** - No se puede ir de L3 → L2 → L1 → L0
3. **Índices faltantes** - Dificulta exploración por nivel
4. **L2 sin normatividad** - Inconsistencia con L3
5. **L0 no integrado** - 50 fichas existen pero no accesibles

### 🎯 **Priorización Sugerida**

```
SEMANA 1:
   ✓ Crear dashboard.html (L5)
   ✓ Implementar breadcrumbs globales
   ✓ Crear índices L3, L2, L1

SEMANA 2:
   ✓ Auditar y completar fichas L1
   ✓ Actualizar L2 con normatividad
   ✓ Integrar fichas L0 al sitio

SEMANA 3:
   ✓ Agregar buscador global
   ✓ Mejorar filtros mapa L4
   ✓ Crear comparador de configuraciones

SEMANA 4:
   ✓ Pruebas de navegación completa
   ✓ Optimización de rendimiento
   ✓ Documentación de usuario final
```

---

## 📞 CONTACTO Y RECURSOS

**Proyecto:** SNCALE - UPTC  
**Repositorio:** github.com/ccolombia-ui/sncale-plan-implementacion  
**Documentos Clave:**
- [Análisis Resolución CALE 2025](ANALISIS_RESOLUCION_CALE_2025.md)
- [Reporte Actualización L3](REPORTE_ACTUALIZACION_FICHAS_L3_NORMATIVIDAD.md)
- [Árbol Jerarquía BIM](ARBOL_JERARQUIA_BIM_COMPLETO.md)

**Servidor Local:** `http://localhost:8085`  
**Comando:** `iniciar_servidor.bat`

---

**FIN DEL DIAGNÓSTICO**  
Generado: 4 de noviembre de 2025  
Documento: DIAGNOSTICO_SITIO_WEB_COMPLETO_L5_L1.md
