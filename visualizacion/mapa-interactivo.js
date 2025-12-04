// SNCALE - Mapa Interactivo Nacional
// Sistema de Navegación Jerárquica L3→L4

// ========================================
// CONFIGURACIÓN Y DATOS
// ========================================

const TIPOS_CONFIG = [
    {
        tipo_id: 'L3.CALE.n_1.plus',
        nombre: 'CALE Metropolitano Premium',
        categoria: 'Cat.A+',
        color: '#E63946',
        icono: '🔴',
        cantidad: 3
    },
    {
        tipo_id: 'L3.CALE.n_1.base',
        nombre: 'CALE Metropolitano Base',
        categoria: 'Cat.A',
        color: '#F77F00',
        icono: '🟠',
        cantidad: 17
    },
    {
        tipo_id: 'L3.CALE.n_2.star',
        nombre: 'CALE Regional Plus',
        categoria: 'Cat.B**',
        color: '#FCBF49',
        icono: '🟡',
        cantidad: 16
    },
    {
        tipo_id: 'L3.CALE.n_2.base',
        nombre: 'CALE Regional Base',
        categoria: 'Cat.B',
        color: '#06D6A0',
        icono: '🟢',
        cantidad: 4
    },
    {
        tipo_id: 'L3.CALE.n_3.base',
        nombre: 'CALE Provincial',
        categoria: 'Cat.C1',
        color: '#118AB2',
        icono: '🔵',
        cantidad: 16
    },
    {
        tipo_id: 'L3.SATELITE.c2',
        nombre: 'Satélites C2',
        categoria: 'Cat.C2',
        color: '#8338EC',
        icono: '⬤',
        cantidad: 31
    },
    {
        tipo_id: 'L3.SATELITE.c3',
        nombre: 'Satélites C3',
        categoria: 'Cat.C3',
        color: '#A05EB5',
        icono: '⬤',
        cantidad: 69
    },
    {
        tipo_id: 'L3.SATELITE.c4',
        nombre: 'Satélites C4',
        categoria: 'Cat.C4',
        color: '#C77DFF',
        icono: '⬤',
        cantidad: 27
    },
    {
        tipo_id: 'L3.SATELITE.c5',
        nombre: 'Satélites C5',
        categoria: 'Cat.C5',
        color: '#6C757D',
        icono: '⬤',
        cantidad: 14
    }
];

// Mapeo de categorías a fichas L3 y configuración de capacidad
const FICHAS_L3_CONFIG = {
    'CALE.n_1': {
        ficha: '../fichas_l3_unitarias/BIM_L3_001.html',
        cubiculos: 24,
        pistas: 'Clase I + II + III',
        nombre: 'CALE Metropolitano'
    },
    'CALE.n_2': {
        ficha: '../fichas_l3_unitarias/BIM_L3_002.html',
        cubiculos: 16,
        pistas: 'Clase I + II',
        nombre: 'CALE Regional'
    },
    'CALE.n_3': {
        ficha: '../fichas_l3_unitarias/BIM_L3_003.html',
        cubiculos: 12,
        pistas: 'Clase I',
        nombre: 'CALE Provincial'
    },
    'CALE.C2': {
        ficha: '../fichas_l3_unitarias/BIM_L3_C2.html',
        cubiculos: 8,
        pistas: 'Apoyo',
        nombre: 'Satélite C2'
    },
    'CALE.C3': {
        ficha: '../fichas_l3_unitarias/BIM_L3_C3.html',
        cubiculos: 4,
        pistas: 'Apoyo',
        nombre: 'Satélite C3'
    },
    'CALE.C4': {
        ficha: '../fichas_l3_unitarias/BIM_L3_C4.html',
        cubiculos: 2,
        pistas: 'Mínimo',
        nombre: 'Satélite C4'
    },
    'CALE.C5': {
        ficha: '../fichas_l3_unitarias/BIM_L3_C5.html',
        cubiculos: 1,
        pistas: 'Punto Info',
        nombre: 'Satélite C5'
    }
};

// Función para obtener config de ficha L3
function getFichaL3Config(categoriaRaw) {
    if (!categoriaRaw) return null;
    return FICHAS_L3_CONFIG[categoriaRaw] || null;
}

// Datos de ejemplo (normalmente se cargarían desde tipos_l3_con_instancias_l4.json)
let NODOS_DATA = {};
let RELACIONES_JERARQUICAS = {};
let map = null;
let markers = {};
let layers = {
    principales: L.layerGroup(),
    satelites: L.layerGroup(),
    conexiones: L.layerGroup(),
    heatmap: null
};
let selectedNodo = null;

// ========================================
// INICIALIZACIÓN
// ========================================

document.addEventListener('DOMContentLoaded', async () => {
    console.log('� Iniciando SNCALE - Mapa L4 (Nodos Municipales)...');
    console.log('═══════════════════════════════════════════════════════════');
    console.log('🏛️  UPTC - Universidad Pedagógica y Tecnológica de Colombia');
    console.log('📊 Sistema Nacional de Centros de Aplicación para Licencias de Conducción');
    console.log('🗺️  Nivel L4: 197 Nodos Georreferenciados (56 Principales + 141 Satélites)');
    console.log('📍 Cobertura: 32 Departamentos | 9 Categorías CALE');
    console.log('═══════════════════════════════════════════════════════════');
    console.log('');
    console.log('ℹ️  CALE = Centro de Aplicación para Licencias de Conducción Escuela');
    console.log('ℹ️  Este es el nivel L4 (nodos individuales), NO L5 (dashboard nacional)');
    console.log('');
    
    try {
        await cargarDatos();
        await cargarRelacionesJerarquicas();
        inicializarMapa();
        renderizarSidebar();
        configurarBusqueda();
        ocultarLoading();
        
        console.log('✅ Sistema inicializado correctamente');
        console.log(`📌 Total nodos cargados: ${Object.keys(NODOS_DATA).length}`);
        console.log(`🔗 Relaciones jerárquicas: ${Object.keys(RELACIONES_JERARQUICAS).length} nodos principales`);
        
    } catch (error) {
        console.error('❌ Error en inicialización:', error);
        mostrarError('Error al cargar los datos. Por favor recarga la página.');
    }
});

// ========================================
// CARGA DE DATOS
// ========================================

async function cargarDatos() {
    console.log('📥 Cargando datos desde JSON...');
    
    try {
        // Intentar cargar archivo completo primero
        let response = await fetch('../data/nodos_completos_mapa.json');
        if (response.ok) {
            const data = await response.json();
            NODOS_DATA = data.nodos || {};
            console.log(`✅ Cargados ${Object.keys(NODOS_DATA).length} nodos desde nodos_completos_mapa.json`);
            return NODOS_DATA;
        }
        
        // Fallback a tipos_l3_con_instancias_l4.json
        response = await fetch('../data/tipos_l3_con_instancias_l4.json');
        const data = await response.json();
        
        NODOS_DATA = procesarDatos(data);
        console.log(`✅ Cargados ${Object.keys(NODOS_DATA).length} nodos desde tipos_l3_con_instancias_l4.json`);
        
        return NODOS_DATA;
    } catch (error) {
        console.warn('⚠️ No se pudo cargar JSON, usando datos de ejemplo');
        NODOS_DATA = generarDatosEjemplo();
        return NODOS_DATA;
    }
}

async function cargarRelacionesJerarquicas() {
    console.log('🔗 Cargando relaciones jerárquicas...');
    
    try {
        // Cargar relaciones COMPLETAS (56 nodos → 141 satélites)
        const response = await fetch('../data/relaciones_jerarquicas_completas.json');
        const data = await response.json();
        
        RELACIONES_JERARQUICAS = data.relaciones || {};
        
        // Extraer satélites de las relaciones y agregarlos a NODOS_DATA
        Object.keys(RELACIONES_JERARQUICAS).forEach(nodoId => {
            const relacion = RELACIONES_JERARQUICAS[nodoId];
            
            // Actualizar info del nodo principal
            if (NODOS_DATA[nodoId]) {
                NODOS_DATA[nodoId].subnodos_ids = relacion.subnodos.map(s => s.id);
                NODOS_DATA[nodoId].num_subnodos = relacion.subnodos.length;
            }
            
            // Agregar satélites a NODOS_DATA
            relacion.subnodos.forEach(satelite => {
                NODOS_DATA[satelite.id] = {
                    nodo_id: satelite.id,
                    nombre: satelite.nombre,
                    departamento: satelite.departamento || 'N/A',
                    coords: {
                        lat: satelite.latitud,
                        lon: satelite.longitud
                    },
                    categoria: satelite.categoria,
                    tipo_id: `L3.SATELITE.${satelite.categoria.toLowerCase()}`,
                    tipo_color: satelite.color,
                    tipo_icono: '⬤',
                    demanda_anual: satelite.demanda,
                    nodo_principal: nodoId,
                    distancia_al_nodo_km: satelite.distancia_km,
                    es_satelite: true
                };
            });
        });
        
        console.log(`✅ Cargadas ${Object.keys(RELACIONES_JERARQUICAS).length} relaciones jerárquicas`);
        console.log(`✅ Total nodos en sistema: ${Object.keys(NODOS_DATA).length} (56 principales + satélites)`);
        
        return RELACIONES_JERARQUICAS;
    } catch (error) {
        console.warn('⚠️ No se pudieron cargar relaciones jerárquicas:', error);
        
        // Fallback al archivo anterior (solo 6 nodos con relaciones)
        try {
            const fallbackResponse = await fetch('../data/relaciones_jerarquicas_nodos.json');
            const fallbackData = await fallbackResponse.json();
            RELACIONES_JERARQUICAS = fallbackData.relaciones || {};
            console.log('✅ Usando relaciones parciales (fallback)');
        } catch (e) {
            console.error('❌ No se pudo cargar ningún archivo de relaciones');
            RELACIONES_JERARQUICAS = {};
        }
        
        return {};
    }
}

function procesarDatos(data) {
    const nodos = {};
    
    // Procesar cada tipo L3
    data.tipos_l3.forEach(tipo => {
        if (tipo.instancias_l4 && Array.isArray(tipo.instancias_l4)) {
            tipo.instancias_l4.forEach(nodo => {
                nodos[nodo.nodo_id] = {
                    ...nodo,
                    tipo_id: tipo.tipo_id,
                    tipo_nombre: tipo.nombre,
                    tipo_color: tipo.color,
                    tipo_icono: tipo.icono,
                    categoria: tipo.categoria,
                    valores_unitarios: tipo.valores_unitarios
                };
            });
        }
    });
    
    return nodos;
}

function generarDatosEjemplo() {
    // Datos de ejemplo basados en la tabla real
    return {
        'NODO_01': {
            nodo_id: 'NODO_01',
            nombre: 'BOGOTÁ SUR',
            departamento: 'BOGOTA, D.C.',
            codigo_dane: '11001',
            coords: { lat: 4.649251, lon: -74.106992 },
            demanda_anual: 80453,
            cluster_municipios: 7,
            tipo_id: 'L3.CALE.n_1.plus',
            tipo_nombre: 'CALE Metropolitano Premium',
            tipo_color: '#E63946',
            tipo_icono: '🔴',
            categoria: 'Cat.A+',
            satelites_vinculados: ['SAT_016'],
            destacado: true,
            infraestructura: {
                direccion_teorica: 'Cra. 71D #6-94 Sur, CC Plaza de las Américas, Kennedy',
                area_m2: 3800,
                inmobiliaria: 'CBRE Colombia',
                arriendo_mensual: 77000000,
                arriendo_anual: 924000000
            },
            valores_unitarios: {
                capex: 3728340000,
                opex_anual: 2400000000,
                capacidad_anual: 173040
            }
        },
        'NODO_02': {
            nodo_id: 'NODO_02',
            nombre: 'BOGOTÁ NORTE',
            departamento: 'BOGOTA, D.C.',
            codigo_dane: '11001',
            coords: { lat: 4.649251, lon: -74.106992 },
            demanda_anual: 70396,
            cluster_municipios: 7,
            tipo_id: 'L3.CALE.n_1.plus',
            tipo_nombre: 'CALE Metropolitano Premium',
            tipo_color: '#E63946',
            tipo_icono: '🔴',
            categoria: 'Cat.A+',
            valores_unitarios: {
                capex: 3728340000,
                opex_anual: 2400000000,
                capacidad_anual: 173040
            }
        },
        'NODO_03': {
            nodo_id: 'NODO_03',
            nombre: 'BUCARAMANGA',
            departamento: 'SANTANDER',
            codigo_dane: '68001',
            coords: { lat: 7.11647, lon: -73.132562 },
            demanda_anual: 68000,
            cluster_municipios: 14,
            tipo_id: 'L3.CALE.n_1.plus',
            tipo_nombre: 'CALE Metropolitano Premium',
            tipo_color: '#E63946',
            tipo_icono: '🔴',
            categoria: 'Cat.A+',
            satelites_vinculados: ['SAT_018', 'SAT_019'],
            infraestructura: {
                direccion_teorica: 'Cra. 27 #42-27, CC Cacique',
                area_m2: 3500,
                inmobiliaria: 'Lonja de Santander',
                arriendo_mensual: 66500000,
                arriendo_anual: 798000000
            },
            valores_unitarios: {
                capex: 3728340000,
                opex_anual: 2400000000,
                capacidad_anual: 173040
            }
        },
        'NODO_04': {
            nodo_id: 'NODO_04',
            nombre: 'CALI',
            departamento: 'VALLE DEL CAUCA',
            codigo_dane: '76001',
            coords: { lat: 3.413686, lon: -76.52133 },
            demanda_anual: 57318,
            cluster_municipios: 10,
            tipo_id: 'L3.CALE.n_1.base',
            tipo_nombre: 'CALE Metropolitano Base',
            tipo_color: '#F77F00',
            tipo_icono: '🟠',
            categoria: 'Cat.A',
            destacado: true,
            valores_unitarios: {
                capex: 2818340000,
                opex_anual: 2400000000,
                capacidad_anual: 127644
            }
        },
        'NODO_05': {
            nodo_id: 'NODO_05',
            nombre: 'IBAGUÉ',
            departamento: 'TOLIMA',
            codigo_dane: '73001',
            coords: { lat: 4.432248, lon: -75.19425 },
            demanda_anual: 55000,
            cluster_municipios: 8,
            tipo_id: 'L3.CALE.n_1.base',
            tipo_nombre: 'CALE Metropolitano Base',
            tipo_color: '#F77F00',
            tipo_icono: '🟠',
            categoria: 'Cat.A',
            valores_unitarios: {
                capex: 2818340000,
                opex_anual: 2400000000,
                capacidad_anual: 127644
            }
        }
    };
}

// ========================================
// INICIALIZACIÓN DEL MAPA
// ========================================

function inicializarMapa() {
    console.log('🗺️ Inicializando mapa Leaflet...');
    
    // Crear mapa centrado en Colombia
    map = L.map('map').setView([4.5709, -74.2973], 6);
    
    // Tile layer (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 18
    }).addTo(map);
    
    // Agregar capas de grupos (según checkboxes)
    layers.principales.addTo(map);
    layers.satelites.addTo(map); // Checked por defecto en HTML
    
    // Agregar marcadores
    agregarMarcadores();
    
    console.log('✅ Mapa inicializado');
}

function agregarMarcadores() {
    Object.values(NODOS_DATA).forEach(nodo => {
        const marker = crearMarcador(nodo);
        markers[nodo.nodo_id] = marker;
        
        // Agregar a capa correspondiente
        if (nodo.es_satelite || nodo.nodo_id.startsWith('SAT_')) {
            marker.addTo(layers.satelites);
        } else {
            marker.addTo(layers.principales);
        }
    });
    
    console.log(`✅ Agregados ${Object.keys(markers).length} marcadores`);
    
    // Contar por capa
    const numPrincipales = Object.values(NODOS_DATA).filter(n => !n.es_satelite && !n.nodo_id.startsWith('SAT_')).length;
    const numSatelites = Object.values(NODOS_DATA).filter(n => n.es_satelite || n.nodo_id.startsWith('SAT_')).length;
    console.log(`  → Principales: ${numPrincipales}, Satélites: ${numSatelites}`);
}

function crearMarcador(nodo) {
    // Tamaño diferenciado para principales vs satélites
    const esSatelite = nodo.es_satelite || nodo.nodo_id.startsWith('SAT_');
    const size = esSatelite ? 16 : 24;
    const borderWidth = esSatelite ? 2 : 3;
    
    const icon = L.divIcon({
        className: 'custom-marker',
        html: `<div style="
            background: ${nodo.tipo_color};
            width: ${size}px;
            height: ${size}px;
            border-radius: 50%;
            border: ${borderWidth}px solid white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: ${esSatelite ? '10px' : '12px'};
            cursor: pointer;
        ">${nodo.tipo_icono}</div>`,
        iconSize: [size, size],
        iconAnchor: [size/2, size/2]
    });
    
    const marker = L.marker([nodo.coords.lat, nodo.coords.lon], { icon });
    
    // Popup
    const popupContent = crearPopupContent(nodo);
    marker.bindPopup(popupContent);
    
    // Click event
    marker.on('click', () => {
        seleccionarNodo(nodo.nodo_id);
        mostrarPanel(nodo);
    });
    
    return marker;
}

function crearPopupContent(nodo) {
    const fichaConfig = getFichaL3Config(nodo.categoria_raw);
    const fichaBtn = fichaConfig ?
        `<a href="${fichaConfig.ficha}" target="_blank" class="popup-btn" style="display:block; text-align:center; margin-top:8px; background:#27ae60;">
            📋 Ver Ficha ${fichaConfig.nombre}
        </a>` : '';

    const capacidadInfo = fichaConfig ?
        `<div class="popup-stat">
            <div class="popup-stat-value">${fichaConfig.cubiculos}</div>
            <div class="popup-stat-label">Cubículos</div>
        </div>
        <div class="popup-stat">
            <div class="popup-stat-value" style="font-size:0.9em">${fichaConfig.pistas}</div>
            <div class="popup-stat-label">Pistas</div>
        </div>` : '';

    return `
        <div class="popup-title">${nodo.tipo_icono} ${nodo.nombre}</div>
        <div class="popup-stats">
            <div class="popup-stat">
                <div class="popup-stat-value">${formatNumber(nodo.demanda_anual)}</div>
                <div class="popup-stat-label">Demanda/año</div>
            </div>
            <div class="popup-stat">
                <div class="popup-stat-value">${nodo.cluster_municipios || 0}</div>
                <div class="popup-stat-label">Municipios</div>
            </div>
            ${capacidadInfo}
        </div>
        <button class="popup-btn" onclick="abrirDetalleNodo('${nodo.nodo_id}')">
            Ver Detalle Completo
        </button>
        ${fichaBtn}
    `;
}

// ========================================
// RENDERIZADO DEL SIDEBAR
// ========================================

function renderizarSidebar() {
    const container = document.getElementById('tiposContainer');
    
    TIPOS_CONFIG.forEach(tipo => {
        const tipoElement = crearTipoElement(tipo);
        container.appendChild(tipoElement);
    });
    
    console.log('✅ Sidebar renderizado');
}

function crearTipoElement(tipo) {
    const div = document.createElement('div');
    div.className = 'tipo-item';
    div.dataset.tipoId = tipo.tipo_id;
    
    // Obtener nodos de este tipo
    const nodosTipo = Object.values(NODOS_DATA).filter(n => n.tipo_id === tipo.tipo_id);
    
    div.innerHTML = `
        <div class="tipo-header" onclick="toggleTipo('${tipo.tipo_id}')">
            <div class="tipo-info">
                <span class="tipo-icon">${tipo.icono}</span>
                <span class="tipo-name">${tipo.nombre}</span>
                <span class="tipo-badge">${nodosTipo.length}</span>
            </div>
            <span class="tipo-toggle" id="toggle-${tipo.tipo_id}">▶</span>
        </div>
        <div class="nodos-list" id="nodos-${tipo.tipo_id}">
            ${nodosTipo.map(nodo => crearNodoElement(nodo)).join('')}
        </div>
    `;
    
    return div;
}

function crearNodoElement(nodo) {
    const vinculados = nodo.subnodos_ids?.length || nodo.satelites_vinculados?.length || 0;
    const fichaConfig = getFichaL3Config(nodo.categoria_raw);

    // Info de capacidad
    const capacidadHtml = fichaConfig ?
        `<div class="nodo-capacidad" style="font-size:0.75em; color:#4299e1; margin-top:3px;">
            🏢 ${fichaConfig.cubiculos} cubículos • 🛣️ ${fichaConfig.pistas}
        </div>` : '';

    // Link a ficha L3
    const fichaLink = fichaConfig ?
        `<a href="${fichaConfig.ficha}" target="_blank"
            onclick="event.stopPropagation();"
            style="display:inline-block; font-size:0.7em; color:#27ae60; margin-top:4px; text-decoration:none;"
            title="Ver ficha ${fichaConfig.nombre}">
            📋 Ficha L3
        </a>` : '';

    return `
        <div class="nodo-item" data-nodo-id="${nodo.nodo_id}" onclick="seleccionarNodo('${nodo.nodo_id}')">
            <div class="nodo-main-info">
                <div class="nodo-name">${nodo.nombre}</div>
                ${capacidadHtml}
                <div class="nodo-stats" style="margin-top:4px;">
                    <span>📊 ${formatNumber(nodo.demanda_anual)}</span>
                    ${fichaLink}
                </div>
            </div>
            ${vinculados > 0 ? `<div class="nodo-links">🔗 ${vinculados}</div>` : ''}
        </div>
    `;
}

// ========================================
// INTERACCIONES
// ========================================

function toggleTipo(tipoId) {
    const nodosList = document.getElementById(`nodos-${tipoId}`);
    const toggle = document.getElementById(`toggle-${tipoId}`);
    
    if (nodosList.classList.contains('expanded')) {
        nodosList.classList.remove('expanded');
        toggle.classList.remove('expanded');
        
        // Dejar de resaltar en mapa
        deshighlightCategoria(tipoId);
    } else {
        nodosList.classList.add('expanded');
        toggle.classList.add('expanded');
        
        // Resaltar en mapa
        highlightCategoria(tipoId);
    }
}

function highlightCategoria(tipoId) {
    const nodosTipo = Object.values(NODOS_DATA).filter(n => n.tipo_id === tipoId);
    
    // Fade otros nodos
    Object.keys(markers).forEach(nodoId => {
        const nodo = NODOS_DATA[nodoId];
        if (nodo.tipo_id !== tipoId) {
            markers[nodoId].setOpacity(0.3);
        } else {
            markers[nodoId].setOpacity(1);
        }
    });
}

function deshighlightCategoria() {
    // Restaurar opacidad
    Object.keys(markers).forEach(nodoId => {
        markers[nodoId].setOpacity(1);
    });
}

function seleccionarNodo(nodoId) {
    // Deseleccionar anterior
    if (selectedNodo) {
        const prevElement = document.querySelector(`[data-nodo-id="${selectedNodo}"]`);
        if (prevElement) prevElement.classList.remove('selected');
    }
    
    // Seleccionar nuevo
    selectedNodo = nodoId;
    const element = document.querySelector(`[data-nodo-id="${nodoId}"]`);
    if (element) {
        element.classList.add('selected');
        element.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    
    // Zoom en mapa
    const nodo = NODOS_DATA[nodoId];
    if (nodo && map) {
        map.flyTo([nodo.coords.lat, nodo.coords.lon], 10, {
            duration: 1
        });
    }
    
    // Mostrar panel
    mostrarPanel(nodo);
    
    // Dibujar conexiones si tiene subnodos
    const tieneSubnodos = (RELACIONES_JERARQUICAS[nodoId] && RELACIONES_JERARQUICAS[nodoId].subnodos?.length > 0) ||
                          (nodo.satelites_vinculados && nodo.satelites_vinculados.length > 0);
    
    if (tieneSubnodos) {
        dibujarConexiones(nodo);
        
        // Auto-activar capa de conexiones si está desactivada
        const checkboxConexiones = document.getElementById('layerConexiones');
        if (checkboxConexiones && !checkboxConexiones.checked) {
            checkboxConexiones.checked = true;
            layers.conexiones.addTo(map);
        }
    }
}

function mostrarPanel(nodo) {
    const panel = document.getElementById('panelFlotante');
    const fichaConfig = getFichaL3Config(nodo.categoria_raw);

    // Actualizar contenido
    document.getElementById('panelNodoNombre').textContent = nodo.nombre;

    // Agregar link a ficha L3 en el subtítulo
    const categoriaHtml = fichaConfig ?
        `${nodo.tipo_icono} ${nodo.categoria} • ${nodo.departamento}
         <a href="${fichaConfig.ficha}" target="_blank"
            style="display:inline-block; margin-left:10px; padding:3px 8px; background:#27ae60; color:white; text-decoration:none; border-radius:4px; font-size:0.8em;">
            📋 Ver Ficha L3
         </a>` :
        `${nodo.tipo_icono} ${nodo.categoria} • ${nodo.departamento}`;

    document.getElementById('panelNodoCategoria').innerHTML = categoriaHtml;

    // Tab General - Agregar info de capacidad
    document.getElementById('panelDemanda').textContent = formatNumber(nodo.demanda_anual);

    // Mostrar cubículos y pistas en lugar de capacidad anual si hay config
    if (fichaConfig) {
        document.getElementById('panelCapacidad').innerHTML =
            `${fichaConfig.cubiculos} cubículos<br><small style="color:#4299e1">${fichaConfig.pistas}</small>`;
    } else {
        document.getElementById('panelCapacidad').textContent = formatNumber(nodo.valores_unitarios?.capacidad_anual || 0);
    }

    document.getElementById('panelDepartamento').textContent = nodo.departamento;
    document.getElementById('panelDane').textContent = nodo.codigo_dane || '-';
    
    // Tab Infraestructura
    if (nodo.infraestructura) {
        document.getElementById('panelDireccion').textContent = nodo.infraestructura.direccion_teorica || '-';
        document.getElementById('panelArea').textContent = formatNumber(nodo.infraestructura.area_m2 || 0);
        document.getElementById('panelInmobiliaria').textContent = nodo.infraestructura.inmobiliaria || '-';
    }
    
    // Tab Presupuesto
    if (nodo.valores_unitarios) {
        document.getElementById('panelCapex').textContent = formatCurrency(nodo.valores_unitarios.capex);
        document.getElementById('panelOpex').textContent = formatCurrency(nodo.valores_unitarios.opex_anual);
    }
    if (nodo.infraestructura) {
        document.getElementById('panelArriendo').textContent = formatCurrency(nodo.infraestructura.arriendo_mensual || 0);
        document.getElementById('panelArriendoAnual').textContent = formatCurrency(nodo.infraestructura.arriendo_anual || 0);
    }
    
    // Tab Cluster
    actualizarClusterTab(nodo);
    
    // Mostrar panel
    panel.classList.add('visible');
}

function actualizarClusterTab(nodo) {
    const clusterList = document.getElementById('clusterList');
    const clusterTitulo = document.getElementById('clusterTitulo');
    
    // Buscar subnodos desde las relaciones jerárquicas
    let subnodos = [];
    
    if (RELACIONES_JERARQUICAS[nodo.nodo_id]) {
        subnodos = RELACIONES_JERARQUICAS[nodo.nodo_id].subnodos || [];
    } else if (nodo.satelites_vinculados) {
        // Fallback a satelites_vinculados si existe
        subnodos = nodo.satelites_vinculados.map(id => ({ id, municipio: id }));
    }
    
    clusterTitulo.textContent = `Nodos Vinculados (${subnodos.length})`;
    
    if (subnodos.length === 0) {
        clusterList.innerHTML = '<li style="text-align: center; color: var(--text-secondary); padding: 2rem;">No hay nodos vinculados</li>';
        return;
    }
    
    clusterList.innerHTML = subnodos.map(subnodo => {
        const subnodoId = subnodo.id;
        const municipio = subnodo.municipio || 'DESCONOCIDO';
        const tipo = subnodo.tipo || '-';
        const dane = subnodo.dane || '-';
        
        // Determinar color del icono según tipo
        let icono = '⬤';
        let color = '#8338EC';
        
        if (tipo.includes('Cat.A')) {
            icono = '🟠';
            color = '#F77F00';
        } else if (tipo.includes('Cat.B')) {
            icono = '🟡';
            color = '#FCBF49';
        } else if (tipo.includes('Cat.C1')) {
            icono = '🔵';
            color = '#118AB2';
        } else if (tipo.includes('C2')) {
            color = '#8338EC';
        } else if (tipo.includes('C3')) {
            color = '#A05EB5';
        } else if (tipo.includes('C4')) {
            color = '#C77DFF';
        } else if (tipo.includes('C5')) {
            color = '#6C757D';
        }
        
        return `
            <li class="cluster-item" onclick="event.stopPropagation(); seleccionarSubnodo('${subnodoId}', '${municipio}')" style="cursor: pointer;">
                <span class="cluster-icon" style="color: ${color};">${icono}</span>
                <div class="cluster-info">
                    <div class="cluster-name">${municipio}</div>
                    <div class="cluster-meta">${tipo}${dane !== '-' ? ` • DANE: ${dane}` : ''}</div>
                </div>
            </li>
        `;
    }).join('');
}

function seleccionarSubnodo(subnodoId, municipio) {
    console.log(`🔗 Seleccionando subnodo: ${subnodoId} (${municipio})`);
    
    // Si el subnodo existe en NODOS_DATA, seleccionarlo
    if (NODOS_DATA[subnodoId]) {
        seleccionarNodo(subnodoId);
    } else {
        // Si no existe, mostrar info básica
        alert(`Subnodo: ${municipio}\nID: ${subnodoId}\n\nDatos completos no disponibles aún.`);
    }
}

function cerrarPanel() {
    document.getElementById('panelFlotante').classList.remove('visible');
}

function cambiarTab(tabName) {
    // Ocultar todos los tabs
    ['tabGeneral', 'tabInfraestructura', 'tabCluster', 'tabPresupuesto'].forEach(id => {
        document.getElementById(id).style.display = 'none';
    });
    
    // Remover active de todos los botones
    document.querySelectorAll('.panel-tab').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Mostrar tab seleccionado
    const tabId = 'tab' + tabName.charAt(0).toUpperCase() + tabName.slice(1);
    document.getElementById(tabId).style.display = 'block';
    
    // Activar botón
    event.target.classList.add('active');
}

function dibujarConexiones(nodo) {
    // Limpiar conexiones anteriores
    layers.conexiones.clearLayers();
    
    // Buscar subnodos desde relaciones jerárquicas
    let subnodos = [];
    
    if (RELACIONES_JERARQUICAS[nodo.nodo_id]) {
        subnodos = RELACIONES_JERARQUICAS[nodo.nodo_id].subnodos || [];
    } else if (nodo.satelites_vinculados) {
        subnodos = nodo.satelites_vinculados.map(id => ({ id }));
    }
    
    if (subnodos.length === 0) return;
    
    subnodos.forEach(subnodo => {
        const subnodoId = subnodo.id;
        const subnodoData = NODOS_DATA[subnodoId];
        
        // Si tenemos coordenadas del subnodo, dibujar línea
        if (subnodoData && subnodoData.coords) {
            const line = L.polyline([
                [nodo.coords.lat, nodo.coords.lon],
                [subnodoData.coords.lat, subnodoData.coords.lon]
            ], {
                color: '#FCBF49',
                weight: 2,
                opacity: 0.6,
                dashArray: '5, 10'
            });
            
            line.bindTooltip(`${nodo.nombre} → ${subnodoData.nombre || subnodo.municipio}`);
            line.addTo(layers.conexiones);
        } else {
            // Si no tenemos coordenadas exactas, al menos registrar en consola
            console.log(`⚠️ Subnodo ${subnodoId} (${subnodo.municipio}) no tiene coordenadas`);
        }
    });
    
    console.log(`✅ Dibujadas ${subnodos.length} conexiones para ${nodo.nombre}`);
}

// ========================================
// BÚSQUEDA
// ========================================

function configurarBusqueda() {
    const searchInput = document.getElementById('searchInput');
    
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        
        if (query.length < 2) {
            limpiarBusqueda();
            return;
        }
        
        buscarNodos(query);
    });
}

function buscarNodos(query) {
    const resultados = Object.values(NODOS_DATA).filter(nodo => 
        nodo.nombre.toLowerCase().includes(query) ||
        nodo.departamento.toLowerCase().includes(query) ||
        nodo.nodo_id.toLowerCase().includes(query)
    );
    
    if (resultados.length > 0) {
        // Auto-expandir tipo del primer resultado
        const primerResultado = resultados[0];
        const tipoId = primerResultado.tipo_id;
        
        // Expandir tipo
        const nodosList = document.getElementById(`nodos-${tipoId}`);
        const toggle = document.getElementById(`toggle-${tipoId}`);
        if (nodosList && !nodosList.classList.contains('expanded')) {
            nodosList.classList.add('expanded');
            toggle.classList.add('expanded');
        }
        
        // Seleccionar primer resultado
        seleccionarNodo(primerResultado.nodo_id);
    }
}

function limpiarBusqueda() {
    deshighlightCategoria();
}

// ========================================
// CONTROL DE CAPAS
// ========================================

function toggleLayer(layerName) {
    const checkbox = document.getElementById(`layer${layerName.charAt(0).toUpperCase() + layerName.slice(1)}`);
    
    switch(layerName) {
        case 'principales':
            if (checkbox.checked) {
                layers.principales.addTo(map);
            } else {
                map.removeLayer(layers.principales);
            }
            break;
        case 'satelites':
            if (checkbox.checked) {
                layers.satelites.addTo(map);
            } else {
                map.removeLayer(layers.satelites);
            }
            break;
        case 'conexiones':
            if (checkbox.checked) {
                layers.conexiones.addTo(map);
            } else {
                map.removeLayer(layers.conexiones);
            }
            break;
        case 'heatmap':
            console.log('Heatmap toggle (por implementar)');
            break;
    }
}

// ========================================
// FUNCIONES AUXILIARES
// ========================================

function formatNumber(num) {
    if (!num) return '0';
    return new Intl.NumberFormat('es-CO').format(num);
}

function formatCurrency(num) {
    if (!num) return '$0';
    const billions = num / 1000000000;
    if (billions >= 1) {
        return `$${billions.toFixed(1)}B`;
    }
    const millions = num / 1000000;
    return `$${millions.toFixed(0)}M`;
}

function ocultarLoading() {
    document.getElementById('loading').style.display = 'none';
}

function mostrarError(mensaje) {
    alert(mensaje);
}

function abrirDetalleNodo(nodoId) {
    seleccionarNodo(nodoId);
}

function exportarDatos() {
    alert('Función de exportación por implementar');
}

function mostrarAyuda() {
    alert(`
SNCALE - Mapa Interactivo

NAVEGACIÓN:
• Click en tipo (🔴 🟠 🟡): Expandir/colapsar lista de nodos
• Click en nodo: Ver detalle completo + ubicación en mapa
• Buscar: Escribe nombre de municipio o código

CAPAS DEL MAPA:
• Nodos Principales (56): CALE n_1, n_2, n_3
• Satélites (141): Cat.C2-C5
• Conexiones: Líneas entre nodo principal y satélites
• Heatmap: Visualización de demanda (próximamente)

ATAJOS:
• ESC: Cerrar panel lateral
• F: Buscar (focus en input)
    `);
}

// Atajo de teclado ESC para cerrar panel
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        cerrarPanel();
    }
});

console.log('✅ Script mapa-interactivo.js cargado');
