# PROPUESTA DE REORGANIZACIÓN - ANEXO C
## Sistema Nacional de Centros de Enseñanza Automovilística (SNCALE)

**Fecha**: 2025-11-03  
**Objetivo**: Reorganizar el Anexo C con navegación lateral intuitiva y estructura modular  
**URL Principal**: https://ccolombia-ui.github.io/sncale-plan-implementacion/

---

## 📋 TABLA DE CONTENIDOS

1. [Estructura Conceptual](#estructura-conceptual)
2. [Arquitectura de Navegación](#arquitectura-de-navegación)
3. [Blueprint 1: Infraestructura y Dotación](#blueprint-1-infraestructura-y-dotación)
4. [Blueprint 2: Plataformas Tecnológicas](#blueprint-2-plataformas-tecnológicas)
5. [Blueprint 3: Talento Humano](#blueprint-3-talento-humano)
6. [Blueprint 4: Modelo Financiero](#blueprint-4-modelo-financiero)
7. [Diseño Visual](#diseño-visual)
8. [Plan de Implementación](#plan-de-implementación)

---

## 1. ESTRUCTURA CONCEPTUAL

### 1.1 Organización por Blueprints

El Anexo C se reorganiza en **4 blueprints principales**, cada uno con su sección dedicada en la barra lateral:

```
ANEXO C - MODELO BIM SNCALE
│
├─── 📘 BLUEPRINT 1: INFRAESTRUCTURA Y DOTACIÓN (BIM)
│    ├─ L4: Red Nacional CALE (Mapa Interactivo)
│    ├─ L3: CALE Completos
│    ├─ L2: Configuraciones
│    ├─ L1: Ensamblajes
│    └─ L0: Componentes Atómicos
│
├─── 💻 BLUEPRINT 2: PLATAFORMAS TECNOLÓGICAS
│    ├─ DEMO Aleya
│    └─ DEMO Munay
│
├─── 👥 BLUEPRINT 3: TALENTO HUMANO
│    ├─ HUB Nacional
│    ├─ CALE.n_1 (Metropolitano)
│    ├─ CALE.n_2 (Intermedio)
│    └─ CALE.n_3 (Básico)
│
└─── 💰 BLUEPRINT 4: MODELO FINANCIERO OPERATIVO
     ├─ Escenarios de Inversión
     ├─ OPEX Proyectado
     └─ Modelo de Sostenibilidad
```

### 1.2 Jerarquía de Navegación

```
Nivel 0: Página Principal (index.html)
   │
   ├─ Nivel 1: Sección de Blueprint
   │     │
   │     ├─ Nivel 2: Subsección (ej: L3, L2, L1, L0)
   │     │     │
   │     │     └─ Nivel 3: Fichas Técnicas Individuales
   │     │
   │     └─ Nivel 2: DEMO / Visualizador
   │
   └─ Nivel 1: Documentación / Ayuda
```

---

## 2. ARQUITECTURA DE NAVEGACIÓN

### 2.1 Barra Lateral (Sidebar) - Componente Principal

**Ubicación**: Izquierda, fija (sticky)  
**Ancho**: 280px  
**Comportamiento**: Colapsable en móvil (hamburger menu)

#### Estructura HTML:

```html
<aside class="sidebar" id="mainSidebar">
  <!-- HEADER SIDEBAR -->
  <div class="sidebar-header">
    <img src="logo-uptc.png" alt="UPTC" class="sidebar-logo">
    <h3>ANEXO C</h3>
    <p>MODELO BIM SNCALE</p>
  </div>

  <!-- BUSCADOR -->
  <div class="sidebar-search">
    <input type="text" id="searchBox" placeholder="🔍 Buscar ficha...">
  </div>

  <!-- NAVEGACIÓN -->
  <nav class="sidebar-nav">
    
    <!-- BLUEPRINT 1: INFRAESTRUCTURA -->
    <div class="nav-section">
      <button class="nav-section-header" data-toggle="blueprint1">
        <span class="icon">📘</span>
        <span class="title">Infraestructura BIM</span>
        <span class="arrow">▼</span>
      </button>
      
      <div class="nav-section-content" id="blueprint1">
        
        <!-- L4: Red Nacional -->
        <div class="nav-subsection">
          <button class="nav-subsection-header" data-toggle="l4">
            <span class="icon">🗺️</span>
            <span class="title">L4 - Red Nacional CALE</span>
            <span class="badge">197 nodos</span>
            <span class="arrow">▼</span>
          </button>
          <div class="nav-subsection-content" id="l4">
            <a href="mapa-interactivo.html" class="nav-link">
              <span class="icon">🌍</span>
              Mapa Interactivo
            </a>
            <a href="lista-municipios.html" class="nav-link">
              <span class="icon">📍</span>
              Lista de Municipios
            </a>
            <a href="red-por-departamento.html" class="nav-link">
              <span class="icon">🏛️</span>
              Por Departamento
            </a>
          </div>
        </div>

        <!-- L3: CALE Completos -->
        <div class="nav-subsection">
          <button class="nav-subsection-header" data-toggle="l3">
            <span class="icon">🏢</span>
            <span class="title">L3 - CALE Completos</span>
            <span class="badge">4</span>
            <span class="arrow">▼</span>
          </button>
          <div class="nav-subsection-content" id="l3">
            <a href="fichas_l3/BIM_L3_001.html" class="nav-link">
              <span class="icon">🏙️</span>
              CALE.n_1 Metropolitano
            </a>
            <a href="fichas_l3/BIM_L3_002.html" class="nav-link">
              <span class="icon">🏘️</span>
              CALE.n_2 Intermedio
            </a>
            <a href="fichas_l3/BIM_L3_003.html" class="nav-link">
              <span class="icon">🏡</span>
              CALE.n_3 Básico
            </a>
            <a href="fichas_l3/BIM_L3_004.html" class="nav-link">
              <span class="icon">🌐</span>
              HUB Nacional
            </a>
          </div>
        </div>

        <!-- L2: Configuraciones -->
        <div class="nav-subsection">
          <button class="nav-subsection-header" data-toggle="l2">
            <span class="icon">⚙️</span>
            <span class="title">L2 - Configuraciones</span>
            <span class="badge">3+</span>
            <span class="arrow">▼</span>
          </button>
          <div class="nav-subsection-content" id="l2">
            <a href="fichas_l2/BIM_L2_001.html" class="nav-link">
              <span class="icon">🛣️</span>
              Pista Clase I
            </a>
            <a href="fichas_l2/BIM_L2_002.html" class="nav-link">
              <span class="icon">🛣️</span>
              Pista Clase II
            </a>
            <a href="fichas_l2/BIM_L2_003.html" class="nav-link">
              <span class="icon">🛣️</span>
              Pista Clase III
            </a>
            <div class="nav-divider"></div>
            <a href="fichas_l2/edificaciones.html" class="nav-link">
              <span class="icon">🏗️</span>
              Edificaciones
            </a>
          </div>
        </div>

        <!-- L1: Ensamblajes -->
        <div class="nav-subsection">
          <button class="nav-subsection-header" data-toggle="l1">
            <span class="icon">🔧</span>
            <span class="title">L1 - Ensamblajes</span>
            <span class="badge">6</span>
            <span class="arrow">▼</span>
          </button>
          <div class="nav-subsection-content" id="l1">
            <a href="fichas_l1/BIM_L1_001.html" class="nav-link">
              <span class="icon">🏍️</span>
              Pista Motos A1A2
            </a>
            <a href="fichas_l1/BIM_L1_002.html" class="nav-link">
              <span class="icon">🚗</span>
              Pista Carros B1C1
            </a>
            <a href="fichas_l1/BIM_L1_003.html" class="nav-link">
              <span class="icon">🚚</span>
              Pista Camiones B2C2
            </a>
            <a href="fichas_l1/BIM_L1_004.html" class="nav-link">
              <span class="icon">🚛</span>
              Pista Tractocamiones B3C3
            </a>
          </div>
        </div>

        <!-- L0: Componentes Atómicos -->
        <div class="nav-subsection">
          <button class="nav-subsection-header" data-toggle="l0">
            <span class="icon">⚛️</span>
            <span class="title">L0 - Componentes</span>
            <span class="badge">82</span>
            <span class="arrow">▼</span>
          </button>
          <div class="nav-subsection-content" id="l0">
            <a href="catalogo-l0.html" class="nav-link">
              <span class="icon">📋</span>
              Catálogo Completo
            </a>
            <div class="nav-divider"></div>
            <a href="l0-por-categoria.html" class="nav-link">
              <span class="icon">🗂️</span>
              Por Categoría
            </a>
            <a href="l0-pavimentos.html" class="nav-link">
              <span class="icon">🛤️</span>
              Pavimentos
            </a>
            <a href="l0-vehiculos.html" class="nav-link">
              <span class="icon">🚗</span>
              Vehículos
            </a>
            <a href="l0-mobiliario.html" class="nav-link">
              <span class="icon">🪑</span>
              Mobiliario
            </a>
          </div>
        </div>

      </div>
    </div>

    <!-- BLUEPRINT 2: PLATAFORMAS TECNOLÓGICAS -->
    <div class="nav-section">
      <button class="nav-section-header" data-toggle="blueprint2">
        <span class="icon">💻</span>
        <span class="title">Plataformas Tech</span>
        <span class="arrow">▼</span>
      </button>
      
      <div class="nav-section-content" id="blueprint2">
        <a href="demo-aleya.html" class="nav-link featured">
          <span class="icon">🎯</span>
          <span class="text">
            <strong>DEMO Aleya</strong>
            <small>Sistema de Evaluación</small>
          </span>
        </a>
        <a href="demo-munay.html" class="nav-link featured">
          <span class="icon">📊</span>
          <span class="text">
            <strong>DEMO Munay</strong>
            <small>Gestión Administrativa</small>
          </span>
        </a>
      </div>
    </div>

    <!-- BLUEPRINT 3: TALENTO HUMANO -->
    <div class="nav-section">
      <button class="nav-section-header" data-toggle="blueprint3">
        <span class="icon">👥</span>
        <span class="title">Talento Humano</span>
        <span class="arrow">▼</span>
      </button>
      
      <div class="nav-section-content" id="blueprint3">
        <a href="talento-hub.html" class="nav-link">
          <span class="icon">🌐</span>
          <span class="text">
            <strong>HUB Nacional</strong>
            <small>Centro de Coordinación</small>
          </span>
        </a>
        <div class="nav-divider"></div>
        <a href="talento-cale-n1.html" class="nav-link">
          <span class="icon">🏙️</span>
          CALE.n_1 - Personal
        </a>
        <a href="talento-cale-n2.html" class="nav-link">
          <span class="icon">🏘️</span>
          CALE.n_2 - Personal
        </a>
        <a href="talento-cale-n3.html" class="nav-link">
          <span class="icon">🏡</span>
          CALE.n_3 - Personal
        </a>
      </div>
    </div>

    <!-- BLUEPRINT 4: MODELO FINANCIERO -->
    <div class="nav-section">
      <button class="nav-section-header" data-toggle="blueprint4">
        <span class="icon">💰</span>
        <span class="title">Modelo Financiero</span>
        <span class="arrow">▼</span>
      </button>
      
      <div class="nav-section-content" id="blueprint4">
        <a href="financiero-escenarios.html" class="nav-link">
          <span class="icon">📈</span>
          Escenarios de Inversión
        </a>
        <a href="financiero-opex.html" class="nav-link">
          <span class="icon">💵</span>
          OPEX Proyectado
        </a>
        <a href="financiero-sostenibilidad.html" class="nav-link">
          <span class="icon">♻️</span>
          Sostenibilidad
        </a>
      </div>
    </div>

    <!-- SEPARADOR -->
    <div class="nav-separator"></div>

    <!-- ENLACES RÁPIDOS -->
    <div class="nav-section">
      <h4 class="nav-section-title">DOCUMENTACIÓN</h4>
      <a href="arbol-jerarquia.html" class="nav-link">
        <span class="icon">🌳</span>
        Árbol de Jerarquía BIM
      </a>
      <a href="resumen-ejecutivo.html" class="nav-link">
        <span class="icon">📄</span>
        Resumen Ejecutivo
      </a>
      <a href="guia-uso.html" class="nav-link">
        <span class="icon">❓</span>
        Guía de Uso
      </a>
    </div>

  </nav>

  <!-- FOOTER SIDEBAR -->
  <div class="sidebar-footer">
    <p><small>SNCALE - UPTC</small></p>
    <p><small>© 2025 Ministerio de Transporte</small></p>
  </div>
</aside>
```

### 2.2 Área de Contenido Principal

**Layout**: Grid responsive  
**Ancho**: calc(100% - 280px) en desktop  
**Ancho**: 100% en móvil

```html
<main class="main-content">
  <!-- BREADCRUMBS -->
  <nav class="breadcrumbs">
    <a href="index.html">Inicio</a>
    <span>/</span>
    <a href="#blueprint1">Infraestructura BIM</a>
    <span>/</span>
    <span class="current">L3 - CALE Completos</span>
  </nav>

  <!-- CONTENIDO DINÁMICO -->
  <div class="content-area">
    <!-- Aquí se carga el contenido específico -->
  </div>
</main>
```

---

## 3. BLUEPRINT 1: INFRAESTRUCTURA Y DOTACIÓN

### 3.1 Nivel L4: Red Nacional CALE

#### Página: `mapa-interactivo.html`

**Componentes**:
1. **Mapa interactivo** (Leaflet.js)
   - 197 marcadores (municipios)
   - Filtros por departamento
   - Filtros por tipo de CALE (n_1, n_2, n_3)
   - Click en marcador → popup con info básica
   - Botón "Ver Ficha Técnica" → enlace a ficha L3

2. **Panel lateral de estadísticas**:
   ```
   📊 ESTADÍSTICAS RED NACIONAL
   
   Total Nodos: 197
   ├─ CALE.n_1: 23 (Metropolitanos)
   ├─ CALE.n_2: 50 (Intermedios)
   └─ CALE.n_3: 124 (Básicos)
   
   Por Región:
   ├─ Andina: 89
   ├─ Caribe: 32
   ├─ Pacífica: 28
   ├─ Orinoquía: 25
   └─ Amazonía: 23
   ```

3. **Tabla de municipios** (DataTables.js):
   - Columnas: Municipio, Departamento, Tipo CALE, Población, Inversión
   - Ordenable, filtrable, paginada
   - Link a ficha técnica en cada fila

#### Página: `lista-municipios.html`

Lista completa con cards:
```html
<div class="municipios-grid">
  <div class="municipio-card">
    <div class="card-header">
      <h3>Bogotá D.C.</h3>
      <span class="badge badge-n1">CALE.n_1</span>
    </div>
    <div class="card-body">
      <p><strong>Departamento:</strong> Cundinamarca</p>
      <p><strong>Población:</strong> 7.901.653</p>
      <p><strong>Inversión:</strong> $145.332.930.021</p>
    </div>
    <div class="card-footer">
      <a href="fichas_l3/BIM_L3_001_bogota.html" class="btn-primary">
        Ver Ficha Técnica
      </a>
    </div>
  </div>
  <!-- Repetir para cada municipio -->
</div>
```

### 3.2 Nivel L3: CALE Completos

**Fichas existentes** (ya generadas):
- `fichas_l3/BIM_L3_001.html` - CALE.n_1 Metropolitano
- `fichas_l3/BIM_L3_002.html` - CALE.n_2 Intermedio
- `fichas_l3/BIM_L3_003.html` - CALE.n_3 Básico
- `fichas_l3/BIM_L3_004.html` - HUB Nacional

**Mejoras a implementar**:
1. Agregar sección "Ubicaciones de este tipo"
2. Galería de renders 3D (si disponibles)
3. Visor IFC embebido (xeokit-sdk)
4. Planos arquitectónicos (imágenes/PDFs)

### 3.3 Nivel L2: Configuraciones

**Fichas actuales** (con recursividad L2→L2):
- `fichas_l2/BIM_L2_001.html` - Pista Clase I ✅
- `fichas_l2/BIM_L2_002.html` - Pista Clase II ✅
- `fichas_l2/BIM_L2_003.html` - Pista Clase III ✅

**Nuevas fichas a crear**:
- `fichas_l2/BIM_L2_004.html` - Sala Teórica 24 Cubículos
- `fichas_l2/BIM_L2_005.html` - Sala Formación 50 PAX
- `fichas_l2/BIM_L2_006.html` - Datacenter 12m²
- `fichas_l2/BIM_L2_007.html` - Parqueadero Administrativo

**Características**:
- ✅ Referencias L2→L2 expandibles con `<details>`
- ✅ Tabla de componentes L1 resueltos
- ✅ Estadísticas de recursividad
- 🆕 Imágenes de referencia (renders)
- 🆕 Especificaciones técnicas detalladas

### 3.4 Nivel L1: Ensamblajes

**Fichas actuales**:
- `fichas_l1/BIM_L1_001.html` - Pista Motos A1A2 ✅
- `fichas_l1/BIM_L1_002.html` - Pista Carros B1C1 ✅
- `fichas_l1/BIM_L1_003.html` - Pista Camiones B2C2 ✅
- `fichas_l1/BIM_L1_004.html` - Pista Tractocamiones B3C3 ✅
- `fichas_l1/BIM_L1_REF_001.html` - Pista Clase I (Referencia) ✅
- `fichas_l1/BIM_L1_REF_002.html` - Pista Clase II (Referencia) ✅

**Características actuales**:
- ✅ Tabla de componentes L0 (NO maniobras)
- ✅ Maniobras como sección descriptiva
- ✅ Diseño responsive

**Mejoras**:
- 🆕 Diagramas de ensamblaje (SVG)
- 🆕 Vista 3D de pista (Three.js)

### 3.5 Nivel L0: Componentes Atómicos

**Datos actuales**: 82 componentes en 18 categorías

**Páginas a crear**:

#### `catalogo-l0.html`
Tabla completa con filtros:
```html
<div class="l0-catalog">
  <div class="filters">
    <select id="filterCategoria">
      <option value="">Todas las categorías</option>
      <option value="IC">Pavimentos</option>
      <option value="VEH">Vehículos</option>
      <option value="MOB">Mobiliario</option>
      <!-- ... más categorías -->
    </select>
  </div>
  
  <table id="tableL0">
    <thead>
      <tr>
        <th>BIM ID</th>
        <th>Código</th>
        <th>Componente</th>
        <th>Categoría</th>
        <th>Unidad</th>
        <th>Usado en</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <!-- Datos de TABLAS_L0_OFICIALES.json -->
    </tbody>
  </table>
</div>
```

#### `l0-por-categoria.html`
Cards agrupadas por categoría:
```html
<div class="categorias-l0">
  <div class="categoria-section">
    <h2>🛤️ Pavimentos (4 componentes)</h2>
    <div class="componentes-grid">
      <div class="componente-card">
        <h3>L0.IC_001</h3>
        <p>Pavimento flexible asfalto e=12cm</p>
        <span class="badge">m²</span>
      </div>
      <!-- ... más componentes -->
    </div>
  </div>
  <!-- Repetir para cada categoría -->
</div>
```

---

## 4. BLUEPRINT 2: PLATAFORMAS TECNOLÓGICAS

### 4.1 DEMO Aleya

**Página**: `demo-aleya.html`

**Contenido**:
```html
<div class="demo-container">
  <div class="demo-header">
    <h1>🎯 ALEYA - Sistema de Evaluación de Conductores</h1>
    <p class="subtitle">Plataforma interactiva para evaluación práctica y teórica</p>
  </div>

  <div class="demo-content">
    <!-- VIDEO DEMO -->
    <div class="video-section">
      <h2>Demo en Vivo</h2>
      <div class="video-wrapper">
        <iframe src="demo-aleya-video.html" frameborder="0"></iframe>
      </div>
    </div>

    <!-- CARACTERÍSTICAS -->
    <div class="features-grid">
      <div class="feature-card">
        <span class="icon">📱</span>
        <h3>Interfaz Intuitiva</h3>
        <p>Diseño centrado en el usuario para evaluadores y aspirantes</p>
      </div>
      <div class="feature-card">
        <span class="icon">⏱️</span>
        <h3>Tiempo Real</h3>
        <p>Retroalimentación instantánea durante evaluación</p>
      </div>
      <div class="feature-card">
        <span class="icon">📊</span>
        <h3>Analytics</h3>
        <p>Dashboard de métricas y estadísticas</p>
      </div>
      <div class="feature-card">
        <span class="icon">☁️</span>
        <h3>Cloud Native</h3>
        <p>Arquitectura escalable en la nube</p>
      </div>
    </div>

    <!-- ARQUITECTURA -->
    <div class="architecture-section">
      <h2>Arquitectura Técnica</h2>
      <img src="diagrama-aleya.svg" alt="Arquitectura Aleya">
      
      <div class="tech-stack">
        <h3>Stack Tecnológico</h3>
        <div class="tech-badges">
          <span class="tech-badge">React</span>
          <span class="tech-badge">Node.js</span>
          <span class="tech-badge">PostgreSQL</span>
          <span class="tech-badge">AWS</span>
        </div>
      </div>
    </div>

    <!-- CAPTURAS DE PANTALLA -->
    <div class="screenshots-gallery">
      <h2>Capturas de Pantalla</h2>
      <div class="gallery-grid">
        <img src="aleya-screenshot-1.png" alt="Dashboard">
        <img src="aleya-screenshot-2.png" alt="Evaluación">
        <img src="aleya-screenshot-3.png" alt="Reportes">
      </div>
    </div>

    <!-- ENLACE A DEMO INTERACTIVA -->
    <div class="cta-section">
      <a href="https://demo-aleya.sncale.gov.co" class="btn-large" target="_blank">
        🚀 Acceder a Demo Interactiva
      </a>
    </div>
  </div>
</div>
```

### 4.2 DEMO Munay

**Página**: `demo-munay.html`

Similar a Aleya pero enfocado en gestión administrativa:

```html
<div class="demo-container">
  <div class="demo-header">
    <h1>📊 MUNAY - Sistema de Gestión Administrativa</h1>
    <p class="subtitle">Plataforma integral para operación de CALEs</p>
  </div>

  <div class="demo-content">
    <!-- Módulos -->
    <div class="modules-grid">
      <div class="module-card">
        <h3>📅 Agenda y Citas</h3>
        <p>Programación de evaluaciones y gestión de disponibilidad</p>
      </div>
      <div class="module-card">
        <h3>💰 Facturación</h3>
        <p>Gestión financiera y facturación electrónica</p>
      </div>
      <div class="module-card">
        <h3>👥 RRHH</h3>
        <p>Gestión de personal evaluador y administrativo</p>
      </div>
      <div class="module-card">
        <h3>📈 Reportes</h3>
        <p>Analítica avanzada y reportes regulatorios</p>
      </div>
    </div>

    <!-- Dashboard Preview -->
    <div class="dashboard-preview">
      <h2>Dashboard Principal</h2>
      <iframe src="munay-dashboard-embed.html" frameborder="0"></iframe>
    </div>
  </div>
</div>
```

---

## 5. BLUEPRINT 3: TALENTO HUMANO

### 5.1 Estructura de Páginas

#### `talento-hub.html` - HUB Nacional

```html
<div class="talento-hub">
  <h1>🌐 HUB Nacional - Centro de Coordinación</h1>
  
  <div class="org-chart">
    <h2>Organigrama</h2>
    <!-- Diagrama interactivo con vis.js o D3.js -->
  </div>

  <div class="positions-grid">
    <div class="position-card">
      <h3>Director Nacional SNCALE</h3>
      <p><strong>Cantidad:</strong> 1</p>
      <p><strong>Perfil:</strong> Profesional ingeniería/administración + MBA</p>
      <p><strong>Salario:</strong> $XX.XXX.XXX</p>
      <button class="btn-details">Ver Perfil Completo</button>
    </div>
    <!-- Repetir para cada cargo -->
  </div>
</div>
```

#### `talento-cale-n1.html` - CALE.n_1 Personal

```html
<div class="talento-cale">
  <h1>🏙️ CALE.n_1 - Personal Metropolitano</h1>
  
  <div class="stats-section">
    <div class="stat-card">
      <h3>Total Personal</h3>
      <p class="stat-number">45</p>
    </div>
    <div class="stat-card">
      <h3>Evaluadores</h3>
      <p class="stat-number">20</p>
    </div>
    <div class="stat-card">
      <h3>Administrativos</h3>
      <p class="stat-number">15</p>
    </div>
    <div class="stat-card">
      <h3>Técnicos</h3>
      <p class="stat-number">10</p>
    </div>
  </div>

  <div class="positions-detail">
    <h2>Cargos Requeridos</h2>
    <table class="positions-table">
      <thead>
        <tr>
          <th>Cargo</th>
          <th>Cantidad</th>
          <th>Perfil</th>
          <th>Salario Mensual</th>
          <th>Costo Anual</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Evaluador Clase III</td>
          <td>5</td>
          <td>Licencia categoría 3 + capacitación</td>
          <td>$4.500.000</td>
          <td>$270.000.000</td>
        </tr>
        <!-- Más cargos -->
      </tbody>
    </table>
  </div>

  <div class="training-section">
    <h2>Plan de Capacitación</h2>
    <!-- Cronograma de capacitación -->
  </div>
</div>
```

Similar para `talento-cale-n2.html` y `talento-cale-n3.html` con datos ajustados.

---

## 6. BLUEPRINT 4: MODELO FINANCIERO

### 6.1 `financiero-escenarios.html`

```html
<div class="financial-scenarios">
  <h1>💰 Escenarios de Inversión SNCALE</h1>

  <div class="scenario-selector">
    <button class="scenario-btn active" data-scenario="escenario1">
      Escenario 1: Red Completa (197 nodos)
    </button>
    <button class="scenario-btn" data-scenario="escenario2">
      Escenario 2: Red Intermedia (141 nodos)
    </button>
    <button class="scenario-btn" data-scenario="escenario3">
      Escenario 3: Red Básica (90 nodos)
    </button>
  </div>

  <div class="scenario-content" id="escenario1">
    <div class="investment-summary">
      <h2>Inversión Total</h2>
      <p class="investment-amount">$XX.XXX.XXX.XXX.XXX</p>
      
      <div class="breakdown-chart">
        <!-- Gráfico de torta con Chart.js -->
        <canvas id="breakdownChart"></canvas>
      </div>

      <div class="breakdown-table">
        <table>
          <tr>
            <td>Infraestructura (CAPEX)</td>
            <td>$XX.XXX.XXX.XXX</td>
            <td>65%</td>
          </tr>
          <tr>
            <td>Tecnología</td>
            <td>$XX.XXX.XXX.XXX</td>
            <td>15%</td>
          </tr>
          <tr>
            <td>Talento Humano (Año 1)</td>
            <td>$XX.XXX.XXX.XXX</td>
            <td>20%</td>
          </tr>
        </table>
      </div>
    </div>

    <div class="timeline-section">
      <h2>Cronograma de Inversión</h2>
      <!-- Gantt chart con vis-timeline -->
    </div>
  </div>
</div>
```

### 6.2 `financiero-opex.html`

```html
<div class="opex-projection">
  <h1>💵 OPEX Proyectado - Gastos Operacionales</h1>

  <div class="year-selector">
    <button class="year-btn active" data-year="1">Año 1</button>
    <button class="year-btn" data-year="2">Año 2</button>
    <button class="year-btn" data-year="3">Año 3</button>
    <button class="year-btn" data-year="5">Año 5</button>
    <button class="year-btn" data-year="10">Año 10</button>
  </div>

  <div class="opex-content">
    <div class="opex-chart">
      <canvas id="opexChart"></canvas>
    </div>

    <div class="opex-breakdown">
      <h2>Desglose OPEX Anual</h2>
      <table>
        <tr>
          <td>Nómina</td>
          <td>$XX.XXX.XXX.XXX</td>
          <td>45%</td>
        </tr>
        <tr>
          <td>Mantenimiento Infraestructura</td>
          <td>$XX.XXX.XXX.XXX</td>
          <td>25%</td>
        </tr>
        <tr>
          <td>Licencias Software</td>
          <td>$XX.XXX.XXX</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Servicios Públicos</td>
          <td>$XX.XXX.XXX</td>
          <td>8%</td>
        </tr>
        <tr>
          <td>Otros</td>
          <td>$XX.XXX.XXX</td>
          <td>12%</td>
        </tr>
      </table>
    </div>
  </div>
</div>
```

### 6.3 `financiero-sostenibilidad.html`

```html
<div class="sustainability-model">
  <h1>♻️ Modelo de Sostenibilidad SNCALE</h1>

  <div class="revenue-model">
    <h2>Modelo de Ingresos</h2>
    
    <div class="revenue-sources">
      <div class="source-card">
        <h3>Tarifas de Evaluación</h3>
        <p class="amount">$XXX por evaluación</p>
        <p>Proyección anual: $XX.XXX.XXX.XXX</p>
      </div>
      
      <div class="source-card">
        <h3>Convenios Interinstitucionales</h3>
        <p class="amount">Variable</p>
        <p>Proyección anual: $XX.XXX.XXX</p>
      </div>
      
      <div class="source-card">
        <h3>Certificaciones Especiales</h3>
        <p class="amount">$XXX por certificación</p>
        <p>Proyección anual: $XX.XXX.XXX</p>
      </div>
    </div>
  </div>

  <div class="break-even-analysis">
    <h2>Punto de Equilibrio</h2>
    <canvas id="breakEvenChart"></canvas>
    
    <div class="break-even-summary">
      <p><strong>Evaluaciones mensuales requeridas:</strong> X.XXX</p>
      <p><strong>Mes de equilibrio proyectado:</strong> Mes XX (Año 2)</p>
    </div>
  </div>

  <div class="roi-section">
    <h2>Retorno de Inversión (ROI)</h2>
    <canvas id="roiChart"></canvas>
  </div>
</div>
```

---

## 7. DISEÑO VISUAL

### 7.1 Paleta de Colores

```css
:root {
  /* UPTC Institucional */
  --uptc-amarillo: #FFD700;
  --uptc-negro: #000000;
  --uptc-blanco: #FFFFFF;
  
  /* BIM por Nivel */
  --color-l4: #8B4513;  /* Marrón (Red) */
  --color-l3: #DC143C;  /* Crimson (CALE) */
  --color-l2: #FF8C00;  /* Naranja (Config) */
  --color-l1: #3B82F6;  /* Azul (Ensamblaje) */
  --color-l0: #10B981;  /* Verde (Atómico) */
  
  /* Blueprints */
  --blueprint-infraestructura: #1e3c72;
  --blueprint-tecnologia: #6366f1;
  --blueprint-talento: #ec4899;
  --blueprint-financiero: #10b981;
  
  /* Estados */
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-error: #dc3545;
  --color-info: #17a2b8;
}
```

### 7.2 Tipografía

```css
:root {
  --font-heading: 'Arial Black', Arial, sans-serif;
  --font-body: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  --font-mono: 'Courier New', monospace;
}

h1 { font-size: 2.5rem; font-weight: 700; }
h2 { font-size: 2rem; font-weight: 600; }
h3 { font-size: 1.5rem; font-weight: 600; }
h4 { font-size: 1.25rem; font-weight: 600; }
body { font-size: 1rem; line-height: 1.6; }
```

### 7.3 Componentes Reutilizables

#### Sidebar
```css
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  width: 280px;
  height: 100vh;
  background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
  color: white;
  overflow-y: auto;
  z-index: 1000;
  box-shadow: 2px 0 10px rgba(0,0,0,0.1);
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  text-align: center;
}

.sidebar-nav {
  padding: 10px 0;
}

.nav-section {
  margin-bottom: 5px;
}

.nav-section-header {
  width: 100%;
  background: rgba(255,255,255,0.05);
  border: none;
  color: white;
  padding: 15px 20px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: background 0.3s;
}

.nav-section-header:hover {
  background: rgba(255,255,255,0.1);
}

.nav-section-header .icon {
  font-size: 1.2em;
}

.nav-section-header .title {
  flex: 1;
  font-weight: 600;
}

.nav-section-header .arrow {
  transition: transform 0.3s;
}

.nav-section-header.active .arrow {
  transform: rotate(180deg);
}

.nav-section-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}

.nav-section-content.active {
  max-height: 1000px;
}

.nav-subsection {
  margin-left: 10px;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  transition: all 0.3s;
}

.nav-link:hover {
  background: rgba(255,255,255,0.1);
  color: white;
  padding-left: 25px;
}

.nav-link .icon {
  font-size: 1.1em;
}

.nav-link .badge {
  margin-left: auto;
  background: var(--uptc-amarillo);
  color: var(--uptc-negro);
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.75em;
  font-weight: bold;
}

.nav-divider {
  height: 1px;
  background: rgba(255,255,255,0.1);
  margin: 10px 20px;
}

.nav-separator {
  height: 2px;
  background: rgba(255,255,255,0.2);
  margin: 20px 0;
}

@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
    transition: transform 0.3s;
  }
  
  .sidebar.active {
    transform: translateX(0);
  }
}
```

#### Cards
```css
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  padding: 20px;
  margin-bottom: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.card-header {
  border-bottom: 2px solid var(--uptc-amarillo);
  padding-bottom: 10px;
  margin-bottom: 15px;
}

.card-body {
  padding: 15px 0;
}

.card-footer {
  border-top: 1px solid #eee;
  padding-top: 15px;
  margin-top: 15px;
  text-align: right;
}
```

#### Badges de Nivel BIM
```css
.badge-l4 { background: var(--color-l4); color: white; }
.badge-l3 { background: var(--color-l3); color: white; }
.badge-l2 { background: var(--color-l2); color: white; }
.badge-l1 { background: var(--color-l1); color: white; }
.badge-l0 { background: var(--color-l0); color: white; }

.badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.85em;
  font-weight: 600;
}
```

---

## 8. PLAN DE IMPLEMENTACIÓN

### 8.1 Fase 1: Estructura Base (Semana 1)

**Archivos a crear**:
1. `index-v3-sidebar.html` - Nueva página principal con sidebar
2. `assets/css/sidebar.css` - Estilos del sidebar
3. `assets/js/sidebar.js` - JavaScript para interactividad
4. `assets/css/variables.css` - Variables CSS globales

**Tareas**:
- [ ] Diseñar HTML base con sidebar + área de contenido
- [ ] Implementar lógica de colapso/expansión de secciones
- [ ] Hacer responsive (hamburger menu en móvil)
- [ ] Agregar buscador en sidebar

### 8.2 Fase 2: Blueprint 1 - Infraestructura (Semana 2-3)

**Archivos a crear**:
1. `mapa-interactivo.html` - Mapa con Leaflet.js
2. `lista-municipios.html` - Cards de municipios
3. `catalogo-l0.html` - Tabla de componentes L0
4. `l0-por-categoria.html` - Vista categorizada

**Tareas**:
- [ ] Integrar Leaflet.js para mapa
- [ ] Cargar 197 marcadores desde JSON
- [ ] Implementar filtros de mapa
- [ ] Crear tabla L0 con DataTables
- [ ] Generar cards categorizadas
- [ ] Agregar imágenes/renders a fichas L2/L3

### 8.3 Fase 3: Blueprint 2 - Plataformas (Semana 4)

**Archivos a crear**:
1. `demo-aleya.html` - Página demo Aleya
2. `demo-munay.html` - Página demo Munay

**Tareas**:
- [ ] Diseñar maquetas de demos
- [ ] Agregar videos/screenshots
- [ ] Documentar arquitectura técnica
- [ ] Crear diagramas con diagrams.net

### 8.4 Fase 4: Blueprint 3 - Talento (Semana 5)

**Archivos a crear**:
1. `talento-hub.html`
2. `talento-cale-n1.html`
3. `talento-cale-n2.html`
4. `talento-cale-n3.html`

**Tareas**:
- [ ] Extraer datos de talento humano de Google Sheets
- [ ] Crear organigramas interactivos (vis.js)
- [ ] Diseñar tablas de cargos y perfiles
- [ ] Calcular costos anuales de nómina

### 8.5 Fase 5: Blueprint 4 - Financiero (Semana 6)

**Archivos a crear**:
1. `financiero-escenarios.html`
2. `financiero-opex.html`
3. `financiero-sostenibilidad.html`

**Tareas**:
- [ ] Integrar Chart.js para gráficos
- [ ] Extraer datos financieros de MUNAY_5.3
- [ ] Crear modelos interactivos de escenarios
- [ ] Implementar calculadoras de ROI
- [ ] Generar gráficos de proyección

### 8.6 Fase 6: Pulido y Testing (Semana 7)

**Tareas**:
- [ ] Testing cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] Testing responsive (móvil, tablet, desktop)
- [ ] Optimización de performance (lazy loading)
- [ ] Agregar analytics (Google Analytics)
- [ ] Crear guía de uso (`guia-uso.html`)
- [ ] Documentar código

### 8.7 Fase 7: Deployment (Semana 8)

**Tareas**:
- [ ] Commit a GitHub
- [ ] Push a GitHub Pages
- [ ] Verificar todos los enlaces
- [ ] Crear README actualizado
- [ ] Anunciar nueva versión

---

## 9. ARCHIVOS DE SOPORTE

### 9.1 `assets/js/sidebar.js`

```javascript
// Inicialización del sidebar
document.addEventListener('DOMContentLoaded', function() {
  
  // Toggle de secciones principales
  const sectionHeaders = document.querySelectorAll('.nav-section-header');
  sectionHeaders.forEach(header => {
    header.addEventListener('click', function() {
      const targetId = this.dataset.toggle;
      const content = document.getElementById(targetId);
      
      // Toggle active class
      this.classList.toggle('active');
      content.classList.toggle('active');
      
      // Cerrar otras secciones (acordeón)
      sectionHeaders.forEach(other => {
        if (other !== this && other.classList.contains('active')) {
          other.classList.remove('active');
          const otherId = other.dataset.toggle;
          document.getElementById(otherId).classList.remove('active');
        }
      });
    });
  });
  
  // Toggle de subsecciones
  const subsectionHeaders = document.querySelectorAll('.nav-subsection-header');
  subsectionHeaders.forEach(header => {
    header.addEventListener('click', function() {
      const targetId = this.dataset.toggle;
      const content = document.getElementById(targetId);
      
      this.classList.toggle('active');
      content.classList.toggle('active');
    });
  });
  
  // Buscador
  const searchBox = document.getElementById('searchBox');
  if (searchBox) {
    searchBox.addEventListener('input', function() {
      const query = this.value.toLowerCase();
      const links = document.querySelectorAll('.nav-link');
      
      links.forEach(link => {
        const text = link.textContent.toLowerCase();
        if (text.includes(query)) {
          link.style.display = 'flex';
          // Expandir sección padre
          const parent = link.closest('.nav-section-content');
          if (parent) parent.classList.add('active');
        } else {
          link.style.display = 'none';
        }
      });
      
      // Si búsqueda vacía, restaurar
      if (query === '') {
        links.forEach(link => link.style.display = 'flex');
      }
    });
  }
  
  // Mobile hamburger menu
  const hamburger = document.getElementById('hamburger');
  const sidebar = document.getElementById('mainSidebar');
  
  if (hamburger && sidebar) {
    hamburger.addEventListener('click', function() {
      sidebar.classList.toggle('active');
    });
  }
  
  // Highlight del link activo
  const currentPage = window.location.pathname.split('/').pop();
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPage) {
      link.classList.add('active');
      // Expandir sección padre
      const parent = link.closest('.nav-section-content');
      if (parent) {
        parent.classList.add('active');
        const header = document.querySelector(`[data-toggle="${parent.id}"]`);
        if (header) header.classList.add('active');
      }
    }
  });
});
```

### 9.2 `assets/data/municipios.json`

```json
{
  "metadata": {
    "total_nodos": 197,
    "fecha_actualizacion": "2025-11-03"
  },
  "municipios": [
    {
      "id": 1,
      "nombre": "Bogotá D.C.",
      "departamento": "Cundinamarca",
      "tipo_cale": "n_1",
      "poblacion": 7901653,
      "latitud": 4.7110,
      "longitud": -74.0721,
      "inversion_total": 145332930021,
      "ficha_l3": "fichas_l3/BIM_L3_001_bogota.html"
    },
    {
      "id": 2,
      "nombre": "Tunja",
      "departamento": "Boyacá",
      "tipo_cale": "n_2",
      "poblacion": 203251,
      "latitud": 5.5353,
      "longitud": -73.3678,
      "inversion_total": 98500000000,
      "ficha_l3": "fichas_l3/BIM_L3_002_tunja.html"
    }
    // ... 195 municipios más
  ]
}
```

---

## 10. VENTAJAS DE LA NUEVA ESTRUCTURA

### ✅ **Usabilidad**
- Navegación intuitiva con jerarquía clara
- Acceso rápido a cualquier sección
- Buscador integrado
- Breadcrumbs para orientación

### ✅ **Escalabilidad**
- Fácil agregar nuevas fichas L0/L1/L2/L3
- Modular: cada blueprint es independiente
- JSON centralizado para datos

### ✅ **Mantenibilidad**
- CSS modular con variables
- JavaScript separado por funcionalidad
- Estructura de carpetas clara

### ✅ **Responsive**
- Sidebar colapsable en móvil
- Grid adaptativo
- Imágenes responsive

### ✅ **Profesionalismo**
- Identidad UPTC consistente
- Diseño moderno
- Animaciones suaves
- Performance optimizado

---

## 11. ESTRUCTURA DE CARPETAS PROPUESTA

```
sncale-plan-implementacion/
│
├── index.html (Redirige a index-v3-sidebar.html)
├── index-v3-sidebar.html (NUEVA VERSIÓN)
│
├── assets/
│   ├── css/
│   │   ├── variables.css
│   │   ├── sidebar.css
│   │   ├── cards.css
│   │   ├── tables.css
│   │   └── responsive.css
│   │
│   ├── js/
│   │   ├── sidebar.js
│   │   ├── maps.js
│   │   ├── charts.js
│   │   └── utils.js
│   │
│   ├── data/
│   │   ├── municipios.json
│   │   ├── talento-humano.json
│   │   └── financiero.json
│   │
│   └── images/
│       ├── logo-uptc.png
│       ├── renders/
│       └── screenshots/
│
├── blueprint1-infraestructura/
│   ├── mapa-interactivo.html
│   ├── lista-municipios.html
│   ├── catalogo-l0.html
│   └── l0-por-categoria.html
│
├── blueprint2-tecnologia/
│   ├── demo-aleya.html
│   └── demo-munay.html
│
├── blueprint3-talento/
│   ├── talento-hub.html
│   ├── talento-cale-n1.html
│   ├── talento-cale-n2.html
│   └── talento-cale-n3.html
│
├── blueprint4-financiero/
│   ├── financiero-escenarios.html
│   ├── financiero-opex.html
│   └── financiero-sostenibilidad.html
│
├── fichas_l0/ (a crear)
├── fichas_l1/ (existente - ya generadas)
├── fichas_l2/ (existente - ya generadas)
├── fichas_l3/ (existente - ya generadas)
│
└── docs/
    ├── arbol-jerarquia.html
    ├── resumen-ejecutivo.html
    └── guia-uso.html
```

---

## 12. RESUMEN EJECUTIVO

### 🎯 Objetivo
Reorganizar el Anexo C con una **barra lateral de navegación** que organice todo el contenido en **4 blueprints principales**, facilitando el acceso a las **fichas técnicas BIM**, **demos de plataformas**, **datos de talento humano** y **modelo financiero**.

### 📊 Estructura
- **Blueprint 1**: Infraestructura BIM (L4→L3→L2→L1→L0)
- **Blueprint 2**: Plataformas Tecnológicas (Aleya + Munay)
- **Blueprint 3**: Talento Humano (HUB + CALE.n_1/2/3)
- **Blueprint 4**: Modelo Financiero (Escenarios + OPEX + ROI)

### 🚀 Implementación
8 semanas de desarrollo incremental con entregables por fase.

### ✅ Beneficios
- Navegación intuitiva
- Escalable y mantenible
- Responsive
- Profesional

---

**¿Apruebas esta propuesta para proceder con la implementación?**
