// SNCALE - Mapa Interactivo Nacional
// Sistema de Navegación Jerárquica L3→L4

// ========================================
// CONFIGURACIÓN Y DATOS
// ========================================

// Vista inicial del mapa (Colombia)
const MAPA_VISTA_INICIAL = {
    lat: 4.5709,
    lng: -74.2973,
    zoom: 6
};

// TIPOS_CONFIG actualizado para coincidir con datos reales del JSON
// VISUALIZACIÓN 2: Filtrado para excluir C2, C3, C4, C5
const TIPOS_CONFIG = [
    {
        tipo_id: 'L3.CALE.n_1',
        nombre: 'CALE Metropolitano',
        categoria: 'Cat.A+',
        color: '#E63946',
        icono: '🔴',
        cantidad: 17
    },
    {
        tipo_id: 'L3.SATELITE.n_2',
        nombre: 'CALE Regional',
        categoria: 'Cat.B',
        color: '#f3af10ff',
        icono: '🟡',
        cantidad: 4
    },
    {
        tipo_id: 'L3.SATELITE.n_3',
        nombre: 'CALE Provincial',
        categoria: 'Cat.C1',
        color: '#06D6A0',
        icono: '🟢',
        cantidad: 16
    },
    {
        tipo_id: 'L3.SATELITE.c6',
        nombre: 'Satelites',
        categoria: 'Cat.C6',
        color: '#FF6B6B',
        icono: '🟠',
        cantidad: 109
    }
];

// Mapeo de categorías a fichas L3 y configuración de capacidad
const FICHAS_L3_CONFIG = {
    'CALE.n_1': {
        ficha: '../cales/BIM_L3_001.html',
        cubiculos: 24,
        pistas: 'Clase I + II + III',
        nombre: 'CALE Metropolitano'
    },
    'CALE.n_2': {
        ficha: '../cales/BIM_L3_002.html',
        cubiculos: 16,
        pistas: 'Clase I + II',
        nombre: 'CALE Regional'
    },
    'CALE.n_3': {
        ficha: '../cales/BIM_L3_003.html',
        cubiculos: 12,
        pistas: 'Clase I',
        nombre: 'CALE Provincial'
    },
    'CALE.C2': {
        ficha: '../cales/BIM_L3_C2.html',
        cubiculos: 8,
        pistas: 'Apoyo',
        nombre: 'Satélite C2'
    },
    'CALE.C3': {
        ficha: '../cales/BIM_L3_C3.html',
        cubiculos: 4,
        pistas: 'Apoyo',
        nombre: 'Satélite C3'
    },
    'CALE.C4': {
        ficha: '../cales/BIM_L3_C4.html',
        cubiculos: 2,
        pistas: 'Mínimo',
        nombre: 'Satélite C4'
    },
    'CALE.C5': {
        ficha: '../cales/BIM_L3_C5.html',
        cubiculos: 1,
        pistas: 'Punto Info',
        nombre: 'Satélite C5'
    },
    'CALE.C6': {
        ficha: '../cales/BIM_L3_C6.html',
        cubiculos: 4, // Valor por defecto, se sobrescribe con CUBICULOS_SATELITES_POR_MUNICIPIO
        pistas: 'Apoyo',
        nombre: 'Satelites'
    }
};

// Mapeo de cubículos por municipio para TODOS los satélites (MOD POR AULA del info.md)
// Formato: 'MUNICIPIO|DEPARTAMENTO': cubiculos (para evitar duplicados)
const CUBICULOS_SATELITES_POR_MUNICIPIO = {
    // ANTIOQUIA
    'RIONEGRO': 4, 'BARBOSA|ANTIOQUIA': 4, 'GUARNE': 4, 'SABANETA': 4, 'ITAGUI': 2, 'APARTADO': 2,
    'COPACABANA': 2, 'LA CEJA': 2, 'CHIGORODO': 2, 'GIRARDOTA': 2, 'EL CARMEN DE VIBORAL': 2,
    'CAUCASIA': 2, 'MARINILLA': 2, 'ANDES': 2, 'CIUDAD BOLIVAR': 2, 'SANTA ROSA DE OSOS': 2,
    // ATLANTICO
    'PUERTO COLOMBIA': 4, 'GALAPA': 2, 'SABANAGRANDE': 2, 'MALAMBO': 2, 'BARANOA': 2, 'SABANALARGA': 2,
    // BOLIVAR
    'ARJONA': 2, 'SANTA ROSA': 2, 'TURBACO': 2, 'CLEMENCIA': 2, 'MAGANGUE': 2,
    // BOYACA
    'DUITAMA': 4, 'COMBITA': 4, 'CHIQUINQUIRA': 2, 'SANTA ROSA DE VITERBO': 2, 'PAIPA': 2,
    'PUERTO BOYACA': 2, 'VILLA DE LEYVA': 2, 'RAMIRIQUI': 2,
    // CESAR
    'SAN DIEGO': 2, 'AGUACHICA': 2, 'EL PASO': 2, 'BOSCONIA': 2, 'SAN MARTIN': 2,
    // CORDOBA
    'LORICA': 2, 'CERETE': 2, 'PLANETA RICA': 2, 'SAHAGUN': 2, 'LA APARTADA': 2,
    // NORTE DE SANTANDER
    'OCAÑA': 2, 'PAMPLONA': 2, 'CUCUTA': 2,
    // SANTANDER
    'FLORIDABLANCA': 4, 'PIEDECUESTA': 4, 'BARBOSA|SANTANDER': 4, 'SAN GIL': 2, 'LEBRIJA': 2,
    'SOCORRO': 2, 'CHARALA': 2,
    // SUCRE
    'SINCE': 4,
    // LA GUAJIRA
    'ALBANIA': 2,
    // MAGDALENA
    'ARACATACA': 2, 'CIENAGA': 2, 'SITIONUEVO': 2,
    // TOLIMA
    'ALVARADO': 2, 'MELGAR': 2, 'MARIQUITA': 2, 'CHAPARRAL': 2, 'PURIFICACION': 2,
    'GUAMO': 2, 'FRESNO': 2,
    // HUILA
    'RIVERA': 4, 'PALERMO': 2, 'GARZON': 2,
    // META
    'ACACIAS': 2, 'RESTREPO': 2, 'PUERTO LOPEZ': 2,
    // ARAUCA
    'SARAVENA': 1, 'TAME': 1,
    // CASANARE
    'VILLANUEVA': 2, 'AGUAZUL': 2,
    // CAUCA
    'SANTANDER DE QUILICHAO': 2, 'PIENDAMO': 2, 'MIRANDA': 2, 'PUERTO TEJADA': 2, 'PATIA': 2,
    // NARINO
    'IPIALES': 2, 'PUPIALES': 2, 'TUQUERRES': 2, 'TUMACO': 2, 'LA UNION': 2, 'GUACHUCAL': 2,
    // QUINDIO
    'CIRCASIA': 4, 'CALARCA': 2, 'QUIMBAYA': 2, 'LA TEBAIDA': 2,
    // CALDAS
    'VILLAMARIA': 4, 'LA DORADA': 2, 'ANSERMA': 2, 'RIOSUCIO': 2, 'MANZANARES': 2,
    'SUPIA': 2, 'CHINCHINA': 2, 'AGUADAS': 2,
    // RISARALDA
    'LA VIRGINIA': 4, 'SANTA ROSA DE CABAL': 2,
    // VALLE DEL CAUCA
    'GUADALAJARA DE BUGA': 4, 'CARTAGO': 4, 'DAGUA': 4, 'TULUA': 4, 'PRADERA': 4,
    'ANDALUCIA': 4, 'YUMBO': 2, 'BUENAVENTURA': 2, 'EL CERRITO': 2, 'ROLDANILLO': 2,
    'ZARZAL': 2, 'FLORIDA': 2, 'CAICEDONIA': 2,
    // PUTUMAYO
    'PUERTO ASIS': 2,
    // CUNDINAMARCA
    'CHIA': 4, 'FUNZA': 4, 'FUSAGASUGA': 4, 'UBATE': 4, 'CAJICA': 4,
    'FACATATIVA': 2, 'SOPO': 2, 'MADRID': 2, 'LA CALERA': 2, 'CAQUEZA': 2,
    'PACHO': 2, 'SIBATE': 2, 'SILVANIA': 2, 'CHOCONTA': 2,
    // ARCHIPIELAGO
    'SAN ANDRES': 2,
    // AMAZONAS
    'LETICIA': 1
};

// Función para reclasificar C6 según cubículos y demanda (VISUALIZACIÓN 2)
function reclasificarC6(nodo) {
    // Obtener cubículos para este nodo C6
    const cubiculos = getCubiculosParaNodo(nodo, FICHAS_L3_CONFIG['CALE.C6']);
    const demanda = nodo.demanda_anual || 0;
    
    // REGLA 1: Clasificar por cubículos primero
    if (cubiculos === 4) {
        return 'CALE.C2';
    } else if (cubiculos === 3) {
        return 'CALE.C3';
    } else if (cubiculos === 2 || cubiculos === 1) {
        // REGLA 2: Si tiene 2 o 1 cubículos, clasificar por demanda
        if (demanda >= 2000) {
            return 'CALE.C2';
        } else if (demanda >= 1000) {
            return 'CALE.C3';
        } else if (demanda >= 500) {
            return 'CALE.C4';
        } else {
            return 'CALE.C5';
        }
    }
    
    // Por defecto, si no hay cubículos definidos, usar solo demanda
    if (demanda >= 2000) {
        return 'CALE.C2';
    } else if (demanda >= 1000) {
        return 'CALE.C3';
    } else if (demanda >= 500) {
        return 'CALE.C4';
    } else {
        return 'CALE.C5';
    }
}

// Función para obtener config de ficha L3
function getFichaL3Config(categoriaRaw, nodo = null) {
    if (!categoriaRaw) return null;
    
    // VISUALIZACIÓN 2: Si es C6, reclasificar dinámicamente
    if (categoriaRaw === 'CALE.C6' && nodo) {
        const categoriaReclasificada = reclasificarC6(nodo);
        return FICHAS_L3_CONFIG[categoriaReclasificada] || null;
    }
    
    return FICHAS_L3_CONFIG[categoriaRaw] || null;
}

// Función para obtener cubículos específicos para TODOS los satélites
function getCubiculosParaNodo(nodo, fichaConfig) {
    // Si el nodo ya tiene cubículos definidos, usar ese valor
    if (nodo.cubiculos !== undefined) {
        return nodo.cubiculos;
    }
    
    // Si es un satélite (C2, C3, C4, C5, C6), buscar en el mapeo por municipio
    const esSatelite = nodo.categoria_raw && (nodo.categoria_raw.includes('SATELITE') || nodo.categoria_raw.startsWith('CALE.C'));
    if (esSatelite && nodo.municipio) {
        const municipioUpper = nodo.municipio.toUpperCase();
        const deptoUpper = nodo.departamento ? nodo.departamento.toUpperCase() : '';
        
        // Intentar primero con municipio|departamento (para casos duplicados)
        const claveCompuesta = `${municipioUpper}|${deptoUpper}`;
        if (CUBICULOS_SATELITES_POR_MUNICIPIO[claveCompuesta] !== undefined) {
            return CUBICULOS_SATELITES_POR_MUNICIPIO[claveCompuesta];
        }
        
        // Si no, intentar solo con municipio
        if (CUBICULOS_SATELITES_POR_MUNICIPIO[municipioUpper] !== undefined) {
            return CUBICULOS_SATELITES_POR_MUNICIPIO[municipioUpper];
        }
    }
    
    // Si no, usar el valor de la configuración de ficha
    return fichaConfig ? fichaConfig.cubiculos : 0;
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
        await cargarSatelitesC6();
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
            
            // Agregar satélites a NODOS_DATA (VISUALIZACIÓN 2: Filtrar C2-C5)
            relacion.subnodos.forEach(satelite => {
                // Excluir satélites C2, C3, C4, C5 en visualización 2
                const categoria = satelite.categoria.toLowerCase();
                if (categoria === 'c2' || categoria === 'c3' || categoria === 'c4' || categoria === 'c5') {
                    return; // Saltar este satélite
                }
                
                NODOS_DATA[satelite.id] = {
                    nodo_id: satelite.id,
                    nombre: satelite.nombre,
                    departamento: satelite.departamento || 'N/A',
                    coords: {
                        lat: satelite.latitud,
                        lon: satelite.longitud
                    },
                    categoria: satelite.categoria,
                    categoria_raw: `CALE.${satelite.categoria}`,
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

async function cargarSatelitesC6() {
    console.log('🆕 Cargando satélites C6 adicionales...');
    
    try {
        const response = await fetch('../data/satelites_completos_141_nodos.json');
        const data = await response.json();
        
        // Filtrar solo satélites C6
        const satelitesC6 = data.satelites.filter(s => s.categoria_cale === 'C6');
        
        // Agregar cada satélite C6 a NODOS_DATA
        satelitesC6.forEach(satelite => {
            NODOS_DATA[satelite.centro_id] = {
                nodo_id: satelite.centro_id,
                nombre: satelite.municipio,
                departamento: satelite.departamento,
                coords: {
                    lat: satelite.latitud,
                    lon: satelite.longitud
                },
                categoria: satelite.categoria_cale,
                categoria_raw: `CALE.${satelite.categoria_cale}`,
                tipo_id: `L3.SATELITE.${satelite.categoria_cale.toLowerCase()}`,
                tipo_color: satelite.color,
                tipo_icono: '🔶',
                demanda_anual: satelite.demanda_estimada_anual,
                nodo_principal: satelite.nodo_principal,
                distancia_al_nodo_km: satelite.distancia_al_nodo_km,
                es_satelite: true,
                observaciones: satelite.observaciones,
                cubiculos: satelite.cubiculos,  // ⭐ Campo cubiculos individual del JSON
                municipio: satelite.municipio   // ⭐ Asegurar que municipio esté disponible
            };
        });
        
        console.log(`✅ Cargados ${satelitesC6.length} satélites C6`);
        console.log(`✅ Total nodos en sistema: ${Object.keys(NODOS_DATA).length}`);
        
        return satelitesC6.length;
    } catch (error) {
        console.warn('⚠️ No se pudieron cargar satélites C6:', error);
        return 0;
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
            tipo_id: 'L3.CALE.n_1',
            tipo_nombre: 'CALE Metropolitano',
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
            tipo_id: 'L3.CALE.n_1',
            tipo_nombre: 'CALE Metropolitano',
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
            tipo_id: 'L3.CALE.n_1',
            tipo_nombre: 'CALE Metropolitano',
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
            tipo_id: 'L3.CALE.n_1',
            tipo_nombre: 'CALE Metropolitano',
            tipo_color: '#1E90FF',
            tipo_icono: '🔴',
            categoria: 'Cat.A+',
            destacado: true,
            valores_unitarios: {
                capex: 3728340000,
                opex_anual: 2400000000,
                capacidad_anual: 173040
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
            tipo_id: 'L3.CALE.n_1',
            tipo_nombre: 'CALE Metropolitano',
            tipo_color: '#E63946',
            tipo_icono: '🔴',
            categoria: 'Cat.A+',
            valores_unitarios: {
                capex: 3728340000,
                opex_anual: 2400000000,
                capacidad_anual: 173040
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
    map = L.map('map').setView([MAPA_VISTA_INICIAL.lat, MAPA_VISTA_INICIAL.lng], MAPA_VISTA_INICIAL.zoom);
    
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
    // VISUALIZACIÓN 2: Filtrar satélites C2, C3, C4, C5
    const tiposExcluidos = ['L3.SATELITE.c2', 'L3.SATELITE.c3', 'L3.SATELITE.c4', 'L3.SATELITE.c5'];
    
    Object.values(NODOS_DATA).forEach(nodo => {
        // Excluir tipos C2, C3, C4, C5 en visualización 2
        if (tiposExcluidos.includes(nodo.tipo_id)) {
            return;
        }
        
        const marker = crearMarcador(nodo);
        markers[nodo.nodo_id] = marker;
        
        // Agregar a capa correspondiente
        if (nodo.es_satelite || nodo.nodo_id.startsWith('SAT_')) {
            marker.addTo(layers.satelites);
        } else {
            marker.addTo(layers.principales);
        }
    });
    
    console.log(`✅ Agregados ${Object.keys(markers).length} marcadores (Visualización 2: sin C2, C3, C4, C5)`);
    
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
    // Determinar categoría para mapear a la ficha correcta (incluye satélites C2-C5)
    const categoriaRaw = nodo.categoria_raw || determinarCategoriaRaw(nodo);
    const fichaConfig = getFichaL3Config(categoriaRaw, nodo);

    // Usar la función para obtener cubículos específicos
    const cubiculos = getCubiculosParaNodo(nodo, fichaConfig);

    const capacidadInfo = fichaConfig ?
        `<div class="popup-stat">
            <div class="popup-stat-value">${cubiculos}</div>
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
        ${fichaConfig ? `
        <button class="popup-btn" onclick="mostrarFicha('${fichaConfig.ficha}', '${fichaConfig.nombre}')">
            Ver Detalle Completo
        </button>` : ''}
    `;
}

// ========================================
// RENDERIZADO DEL SIDEBAR
// ========================================

function renderizarSidebar() {
    const container = document.getElementById('tiposContainer');
    
    // VISUALIZACIÓN 2: Ya filtrado en TIPOS_CONFIG, pero por seguridad verificamos aquí también
    const tiposExcluidos = ['L3.SATELITE.c2', 'L3.SATELITE.c3', 'L3.SATELITE.c4', 'L3.SATELITE.c5'];
    
    TIPOS_CONFIG.forEach(tipo => {
        // Saltar tipos excluidos
        if (tiposExcluidos.includes(tipo.tipo_id)) {
            return;
        }
        
        const tipoElement = crearTipoElement(tipo);
        container.appendChild(tipoElement);
    });
    
    console.log('✅ Sidebar renderizado (Visualización 2: sin C2, C3, C4, C5)');
}

function crearTipoElement(tipo) {
    const div = document.createElement('div');
    div.className = 'tipo-item';
    div.dataset.tipoId = tipo.tipo_id;
    
    // Obtener nodos de este tipo (VISUALIZACIÓN 2: ya filtrados en NODOS_DATA)
    const tiposExcluidos = ['L3.SATELITE.c2', 'L3.SATELITE.c3', 'L3.SATELITE.c4', 'L3.SATELITE.c5'];
    const nodosTipo = Object.values(NODOS_DATA).filter(n => 
        n.tipo_id === tipo.tipo_id && !tiposExcluidos.includes(n.tipo_id)
    );
    
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
    const fichaConfig = getFichaL3Config(nodo.categoria_raw, nodo);

    // Obtener cubículos usando la función que considera el mapeo C6
    const cubiculos = getCubiculosParaNodo(nodo, fichaConfig);

    // Info de capacidad
    const capacidadHtml = fichaConfig ?
        `<div class="nodo-capacidad" style="font-size:0.75em; color:#4299e1; margin-top:3px;">
            🏢 ${cubiculos} cubículos • 🛣️ ${fichaConfig.pistas}
        </div>` : '';

    return `
        <div class="nodo-item" data-nodo-id="${nodo.nodo_id}" onclick="seleccionarNodo('${nodo.nodo_id}')">
            <div class="nodo-main-info">
                <div class="nodo-name">${nodo.nombre}</div>
                ${capacidadHtml}
                <div class="nodo-stats" style="margin-top:4px;">
                    <span>📊 ${formatNumber(nodo.demanda_anual)}</span>
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
    // Fade otros nodos
    Object.keys(markers).forEach(nodoId => {
        const nodo = NODOS_DATA[nodoId];
        if (nodo.tipo_id === tipoId) {
            markers[nodoId].setOpacity(1.0);
        } else {
            markers[nodoId].setOpacity(0.3);
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
    
    const nodo = NODOS_DATA[nodoId];
    if (!nodo) return;
    
    // Verificar si hay una ficha abierta
    const fichaContainer = document.getElementById('fichaContainer');
    const fichaAbierta = fichaContainer?.classList.contains('active');
    
    if (fichaAbierta) {
        // Si hay ficha abierta, actualizar la ficha con el nuevo nodo
        const fichaConfig = getFichaL3Config(nodo.categoria_raw, nodo);
        if (fichaConfig) {
            mostrarFicha(fichaConfig.ficha, fichaConfig.nombre);
        }
    } else {
        // Comportamiento normal: zoom en mapa y mostrar panel
        if (map) {
            map.flyTo([nodo.coords.lat, nodo.coords.lon], 10, {
                duration: 1
            });
        }
        
        // Mostrar panel flotante (existente)
        mostrarPanel(nodo);

        // Actualizar sidebar derecha con drill-down
        mostrarNodoEnSidebarDerecha(nodo);

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
}

function mostrarPanel(nodo) {
    const panel = document.getElementById('panelFlotante');
    const fichaConfig = getFichaL3Config(nodo.categoria_raw, nodo);

    // Actualizar contenido
    document.getElementById('panelNodoNombre').textContent = nodo.nombre;

    // Subtítulo sin el botón de ficha
    const categoriaHtml = `${nodo.tipo_icono} ${nodo.categoria} • ${nodo.departamento}`;

    document.getElementById('panelNodoCategoria').innerHTML = categoriaHtml;

    // Tab General - Agregar info de capacidad
    document.getElementById('panelDemanda').textContent = formatNumber(nodo.demanda_anual);

    // Obtener cubículos usando la función que considera el mapeo C6
    const cubiculos = getCubiculosParaNodo(nodo, fichaConfig);

    // Mostrar cubículos y pistas en lugar de capacidad anual si hay config
    if (fichaConfig) {
        document.getElementById('panelCapacidad').innerHTML =
            `${cubiculos} cubículos<br><small style="color:#4299e1">${fichaConfig.pistas}</small>`;
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

    // Tab Jerarquía BIM
    poblarJerarquiaBIM(nodo);

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
    
    // VISUALIZACIÓN 2: Filtrar subnodos C2, C3, C4, C5
    subnodos = subnodos.filter(subnodo => {
        const categoria = subnodo.categoria ? subnodo.categoria.toLowerCase() : '';
        return categoria !== 'c2' && categoria !== 'c3' && categoria !== 'c4' && categoria !== 'c5';
    });
    
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
            icono = '🔵';
            color = '#1E90FF';
        } else if (tipo.includes('Cat.B')) {
            icono = '🟡';
            color = '#FCBF49';
        } else if (tipo.includes('Cat.C1')) {
            icono = '🔵';
            color = '#118AB2';
        } else if (tipo.includes('C2')) {
            color = '#711ed7ff';
        } else if (tipo.includes('C3')) {
            color = '#711ed7ff';
        } else if (tipo.includes('C4')) {
            color = '#711ed7ff';
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
    ['tabGeneral', 'tabJerarquia', 'tabInfraestructura', 'tabCluster', 'tabPresupuesto'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });

    // Remover active de todos los botones
    document.querySelectorAll('.panel-tab').forEach(btn => {
        btn.classList.remove('active');
    });

    // Mostrar tab seleccionado
    const tabId = 'tab' + tabName.charAt(0).toUpperCase() + tabName.slice(1);
    const tabEl = document.getElementById(tabId);
    if (tabEl) tabEl.style.display = 'block';

    // Activar botón
    if (event && event.target) event.target.classList.add('active');
}

// ========================================
// JERARQUÍA BIM - FUNCIONES
// ========================================

// Datos de componentes por nivel (basados en TABLAS_L*_OFICIALES.json)
const COMPONENTES_BIM = {
    L3: {
        'CALE.n_1': {
            nombre: 'CALE Metropolitano',
            cubiculos: 24,
            pistas: 'Clase I + II + III',
            capex: 141320000000,
            opex: 11305600000,
            ficha: '../cales/BIM_L3_001.html',
            componentes: [
                { id: 'Pista Clase III', capex: 1850000000, opex: 148000000 },
                { id: 'Pista Clase II', capex: 980000000, opex: 78400000 },
                { id: 'Pista Clase I', capex: 750000000, opex: 60000000 },
                { id: 'Sala 24 Cubículos', capex: 186000000, opex: 14880000 },
                { id: 'Edificación Admin', capex: 2400000000, opex: 192000000 }
            ]
        },
        'CALE.n_2': {
            nombre: 'CALE Regional',
            cubiculos: 16,
            pistas: 'Clase I + II',
            capex: 4012930000,
            opex: 321034400,
            ficha: '../cales/BIM_L3_002.html',
            componentes: [
                { id: 'Pista Clase II', capex: 980000000, opex: 78400000 },
                { id: 'Pista Clase I', capex: 750000000, opex: 60000000 },
                { id: 'Sala 16 Cubículos', capex: 124000000, opex: 9920000 },
                { id: 'Edificación Admin', capex: 1800000000, opex: 144000000 }
            ]
        },
        'CALE.n_3': {
            nombre: 'CALE Provincial',
            cubiculos: 12,
            pistas: 'Clase I',
            capex: 645000000,
            opex: 405188640,
            ficha: '../cales/BIM_L3_003.html',
            componentes: [
                { id: 'Pista Clase I', capex: 750000000, opex: 60000000 },
                { id: 'Sala 12 Cubículos', capex: 93000000, opex: 7440000 },
                { id: 'Zona Administrativa', capex: 120000000, opex: 9600000 }
            ]
        },
        'CALE.C2': {
            nombre: 'Satélite C2',
            cubiculos: 8,
            pistas: 'Apoyo',
            capex: 440000000,
            opex: 285000000,
            ficha: '../cales/BIM_L3_C2.html',
            componentes: [
                { id: 'Sala 8 Cubículos', capex: 62000000, opex: 4960000 },
                { id: 'Zona Administrativa', capex: 80000000, opex: 6400000 }
            ]
        },
        'CALE.C3': {
            nombre: 'Satélite C3',
            cubiculos: 4,
            pistas: 'Apoyo',
            capex: 175000000,
            opex: 125000000,
            ficha: '../cales/BIM_L3_C3.html',
            componentes: [
                { id: 'Sala 4 Cubículos', capex: 31000000, opex: 2480000 },
                { id: 'Recepción', capex: 40000000, opex: 3200000 }
            ]
        },
        'CALE.C4': {
            nombre: 'Satélite C4',
            cubiculos: 2,
            pistas: 'Mínimo',
            capex: 85000000,
            opex: 65000000,
            ficha: '../cales/BIM_L3_C4.html',
            componentes: [
                { id: 'Módulo 2 Cubículos', capex: 15500000, opex: 1240000 }
            ]
        },
        'CALE.C5': {
            nombre: 'Satélite C5',
            cubiculos: 1,
            pistas: 'Punto Info',
            capex: 45000000,
            opex: 35000000,
            ficha: '../cales/BIM_L3_C5.html',
            componentes: [
                { id: 'Punto Información', capex: 7750000, opex: 620000 }
            ]
        }
    },
    L2: [
        { id: 'BIM_L2_001', nombre: 'Pista Clase I (Motos+Carros)', capex: 721440000, opex: 57715200, ficha: '../fichas_l2/BIM_L2_001.html' },
        { id: 'BIM_L2_002', nombre: 'Pista Clase II (Camiones)', capex: 980000000, opex: 78400000, ficha: '../fichas_l2/BIM_L2_002.html' },
        { id: 'BIM_L2_003', nombre: 'Pista Clase III (Articulados)', capex: 1850000000, opex: 148000000, ficha: '../fichas_l2/BIM_L2_003.html' },
        { id: 'BIM_L2_004', nombre: 'Sala Evaluación Teórica', capex: 186000000, opex: 14880000, ficha: '../fichas_l2/BIM_L2_004.html' },
        { id: 'BIM_L2_005', nombre: 'Edificación Administrativa', capex: 2400000000, opex: 192000000, ficha: '../fichas_l2/BIM_L2_005.html' }
    ],
    L1: [
        { id: 'BIM_L1_001', nombre: 'Pista Motos A1/A2', capex: 289805000, opex: 8694150, ficha: '../fichas_l1/BIM_L1_001.html' },
        { id: 'BIM_L1_002', nombre: 'Pista Carros B1/C1', capex: 431635000, opex: 12948050, ficha: '../fichas_l1/BIM_L1_002.html' },
        { id: 'BIM_L1_003', nombre: 'Pista Camiones B2/C2', capex: 685950000, opex: 20578500, ficha: '../fichas_l1/BIM_L1_003.html' },
        { id: 'BIM_L1_004', nombre: 'Pista Tractocamiones B3/C3', capex: 1164050000, opex: 34921500, ficha: '../fichas_l1/BIM_L1_004.html' }
    ],
    L0: [
        { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 85000, opex: 1700, unidad: 'm²', ficha: '../fichas/BIM_L0_001.html' },
        { id: 'BIM_L0_015', nombre: 'Edificación principal CALE', capex: 2500000, opex: 50000, unidad: 'm²', ficha: '../fichas/BIM_L0_015.html' },
        { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 4500000, opex: 90000, unidad: 'und', ficha: '../fichas/BIM_L0_023.html' },
        { id: 'BIM_L0_060', nombre: 'PC Desktop Core i5', capex: 3200000, opex: 64000, unidad: 'und', ficha: '../fichas/BIM_L0_060.html' },
        { id: 'BIM_L0_077', nombre: 'Motocicleta adaptada', capex: 12000000, opex: 360000, unidad: 'und', ficha: '../fichas/BIM_L0_077.html' },
        { id: 'BIM_L0_079', nombre: 'Automóvil B1/C1 adaptado', capex: 65000000, opex: 1950000, unidad: 'und', ficha: '../fichas/BIM_L0_079.html' }
    ]
};

// Función para formatear valores en COP compacto
function formatCOP(value) {
    if (!value || value === 0) return '-';
    if (value >= 1000000000) return '$' + (value/1000000000).toFixed(1) + 'B';
    if (value >= 1000000) return '$' + (value/1000000).toFixed(0) + 'M';
    if (value >= 1000) return '$' + (value/1000).toFixed(0) + 'K';
    return '$' + value.toLocaleString('es-CO');
}

// Toggle de secciones de nivel en el panel
function toggleNivelPanel(nivel) {
    const body = document.getElementById('body' + nivel.toUpperCase());
    const arrow = document.getElementById('arrow' + nivel.toUpperCase());

    if (body && arrow) {
        body.classList.toggle('collapsed');
        arrow.classList.toggle('rotated');
    }
}

// Función para poblar la jerarquía BIM en el panel
function poblarJerarquiaBIM(nodo) {
    const categoriaRaw = nodo.categoria_raw || '';
    const configL3 = COMPONENTES_BIM.L3[categoriaRaw] || COMPONENTES_BIM.L3['CALE.n_1'];

    // Actualizar resumen financiero
    document.getElementById('jerarquiaCapex').textContent = formatCOP(configL3.capex);
    document.getElementById('jerarquiaOpex').textContent = formatCOP(configL3.opex);

    // Actualizar link a ficha L3
    const linkL3 = document.getElementById('linkFichaL3');
    if (linkL3) {
        linkL3.href = configL3.ficha;
        linkL3.textContent = `Ver Ficha ${configL3.nombre}`;
    }

    // Poblar componentes L3
    const compL3Container = document.getElementById('componentesL3');
    if (compL3Container && configL3.componentes) {
        compL3Container.innerHTML = configL3.componentes.map(comp => `
            <div class="comp-item-panel">
                <div class="comp-item-header">
                    <span class="comp-item-id">${comp.id}</span>
                </div>
                <div class="comp-item-valores">
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">CAPEX:</span>
                        <span class="comp-valor-value capex">${formatCOP(comp.capex)}</span>
                    </div>
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">OPEX:</span>
                        <span class="comp-valor-value opex">${formatCOP(comp.opex)}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Poblar componentes L2
    const compL2Container = document.getElementById('componentesL2');
    if (compL2Container) {
        compL2Container.innerHTML = COMPONENTES_BIM.L2.map(comp => `
            <div class="comp-item-panel">
                <div class="comp-item-header">
                    <span class="comp-item-id">${comp.id}</span>
                    <a href="${comp.ficha}" class="comp-item-link" target="_blank">Ver</a>
                </div>
                <div class="comp-item-name">${comp.nombre}</div>
                <div class="comp-item-valores">
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">CAPEX:</span>
                        <span class="comp-valor-value capex">${formatCOP(comp.capex)}</span>
                    </div>
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">OPEX:</span>
                        <span class="comp-valor-value opex">${formatCOP(comp.opex)}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Poblar componentes L1
    const compL1Container = document.getElementById('componentesL1');
    if (compL1Container) {
        compL1Container.innerHTML = COMPONENTES_BIM.L1.map(comp => `
            <div class="comp-item-panel">
                <div class="comp-item-header">
                    <span class="comp-item-id">${comp.id}</span>
                    <a href="${comp.ficha}" class="comp-item-link" target="_blank">Ver</a>
                </div>
                <div class="comp-item-name">${comp.nombre}</div>
                <div class="comp-item-valores">
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">CAPEX:</span>
                        <span class="comp-valor-value capex">${formatCOP(comp.capex)}</span>
                    </div>
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">OPEX:</span>
                        <span class="comp-valor-value opex">${formatCOP(comp.opex)}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Poblar componentes L0
    const compL0Container = document.getElementById('componentesL0');
    if (compL0Container) {
        compL0Container.innerHTML = COMPONENTES_BIM.L0.map(comp => `
            <div class="comp-item-panel">
                <div class="comp-item-header">
                    <span class="comp-item-id">${comp.id}</span>
                    <a href="${comp.ficha}" class="comp-item-link" target="_blank">Ver</a>
                </div>
                <div class="comp-item-name">${comp.nombre}</div>
                <div class="comp-item-valores">
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">Unidad:</span>
                        <span class="comp-valor-value">${comp.unidad}</span>
                    </div>
                    <div class="comp-valor-item">
                        <span class="comp-valor-label">CAPEX:</span>
                        <span class="comp-valor-value capex">${formatCOP(comp.capex)}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }
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
    
    // VISUALIZACIÓN 2: Filtrar subnodos C2, C3, C4, C5
    subnodos = subnodos.filter(subnodo => {
        const categoria = subnodo.categoria ? subnodo.categoria.toLowerCase() : '';
        return categoria !== 'c2' && categoria !== 'c3' && categoria !== 'c4' && categoria !== 'c5';
    });
    
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
    // VISUALIZACIÓN 2: Filtrar C2, C3, C4, C5 de los resultados de búsqueda
    const tiposExcluidos = ['L3.SATELITE.c2', 'L3.SATELITE.c3', 'L3.SATELITE.c4', 'L3.SATELITE.c5'];
    
    const resultados = Object.values(NODOS_DATA).filter(nodo => 
        !tiposExcluidos.includes(nodo.tipo_id) && (
            nodo.nombre.toLowerCase().includes(query) ||
            nodo.departamento.toLowerCase().includes(query) ||
            nodo.nodo_id.toLowerCase().includes(query)
        )
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

// ========================================
// SIDEBAR DERECHA - NAVEGACIÓN DRILL-DOWN
// ========================================

// Datos completos de jerarquía BIM por tipo CALE
const JERARQUIA_BIM_COMPLETA = {
    'CALE.n_1': {
        nombre: 'CALE Metropolitano (n_1)',
        capex: 3728340000,
        opex: 2400000000,
        l2: [
            {
                id: 'L2_PISTAS',
                nombre: 'Sistema de Pistas',
                capex: 3580000000,
                opex: 286400000,
                l1: [
                    {
                        id: 'L1_PISTA_III',
                        nombre: 'Pista Clase III (Articulados)',
                        capex: 1850000000,
                        opex: 148000000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 425000000, opex: 8500000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 180000000, opex: 36000000 },
                            { id: 'BIM_L0_045', nombre: 'Iluminación LED pista', capex: 245000000, opex: 4900000 }
                        ]
                    },
                    {
                        id: 'L1_PISTA_II',
                        nombre: 'Pista Clase II (Camiones)',
                        capex: 980000000,
                        opex: 78400000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 340000000, opex: 6800000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 140000000, opex: 28000000 }
                        ]
                    },
                    {
                        id: 'L1_PISTA_I',
                        nombre: 'Pista Clase I (Motos+Carros)',
                        capex: 750000000,
                        opex: 60000000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 255000000, opex: 5100000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 95000000, opex: 19000000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_SALA_EVAL',
                nombre: 'Sala Evaluación Teórica (24 cubículos)',
                capex: 186000000,
                opex: 14880000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos de Evaluación',
                        capex: 108000000,
                        opex: 2160000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 108000000, opex: 2160000 }
                        ]
                    },
                    {
                        id: 'L1_EQUIPOS',
                        nombre: 'Equipos de Cómputo',
                        capex: 78000000,
                        opex: 1560000,
                        l0: [
                            { id: 'BIM_L0_060', nombre: 'PC Desktop Core i5', capex: 76800000, opex: 1536000 },
                            { id: 'BIM_L0_062', nombre: 'Monitor 24"', capex: 1200000, opex: 24000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_EDIFICACION',
                nombre: 'Edificación Administrativa',
                capex: 2400000000,
                opex: 192000000,
                l1: [
                    {
                        id: 'L1_CONSTRUCCION',
                        nombre: 'Construcción Principal',
                        capex: 1900000000,
                        opex: 152000000,
                        l0: [
                            { id: 'BIM_L0_015', nombre: 'Edificación principal CALE', capex: 1900000000, opex: 38000000 }
                        ]
                    },
                    {
                        id: 'L1_MEP',
                        nombre: 'Instalaciones MEP',
                        capex: 500000000,
                        opex: 40000000,
                        l0: [
                            { id: 'BIM_L0_040', nombre: 'Sistema eléctrico', capex: 200000000, opex: 16000000 },
                            { id: 'BIM_L0_041', nombre: 'Sistema hidráulico', capex: 150000000, opex: 12000000 },
                            { id: 'BIM_L0_042', nombre: 'HVAC', capex: 150000000, opex: 12000000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.n_2': {
        nombre: 'CALE Regional (n_2)',
        capex: 2654000000,
        opex: 212320000,
        l2: [
            {
                id: 'L2_PISTAS',
                nombre: 'Sistema de Pistas (Clase I + II)',
                capex: 1730000000,
                opex: 138400000,
                l1: [
                    {
                        id: 'L1_PISTA_II',
                        nombre: 'Pista Clase II (Camiones)',
                        capex: 980000000,
                        opex: 78400000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 340000000, opex: 6800000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 140000000, opex: 28000000 }
                        ]
                    },
                    {
                        id: 'L1_PISTA_I',
                        nombre: 'Pista Clase I (Motos+Carros)',
                        capex: 750000000,
                        opex: 60000000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 255000000, opex: 5100000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 95000000, opex: 19000000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_SALA_EVAL',
                nombre: 'Sala Evaluación Teórica (16 cubículos)',
                capex: 124000000,
                opex: 9920000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos de Evaluación',
                        capex: 72000000,
                        opex: 1440000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 72000000, opex: 1440000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_EDIFICACION',
                nombre: 'Edificación Administrativa',
                capex: 800000000,
                opex: 64000000,
                l1: [
                    {
                        id: 'L1_CONSTRUCCION',
                        nombre: 'Construcción Principal',
                        capex: 800000000,
                        opex: 64000000,
                        l0: [
                            { id: 'BIM_L0_015', nombre: 'Edificación principal CALE', capex: 800000000, opex: 16000000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.n_3': {
        nombre: 'CALE Provincial (n_3)',
        capex: 963000000,
        opex: 77040000,
        l2: [
            {
                id: 'L2_PISTAS',
                nombre: 'Sistema de Pistas (Clase I)',
                capex: 750000000,
                opex: 60000000,
                l1: [
                    {
                        id: 'L1_PISTA_I',
                        nombre: 'Pista Clase I (Motos+Carros)',
                        capex: 750000000,
                        opex: 60000000,
                        l0: [
                            { id: 'BIM_L0_001', nombre: 'Pavimento flexible asfalto', capex: 255000000, opex: 5100000 },
                            { id: 'BIM_L0_003', nombre: 'Señalización horizontal', capex: 95000000, opex: 19000000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_SALA_EVAL',
                nombre: 'Sala Evaluación Teórica (12 cubículos)',
                capex: 93000000,
                opex: 7440000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos de Evaluación',
                        capex: 54000000,
                        opex: 1080000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 54000000, opex: 1080000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_ZONA_ADMIN',
                nombre: 'Zona Administrativa',
                capex: 120000000,
                opex: 9600000,
                l1: [
                    {
                        id: 'L1_OFICINAS',
                        nombre: 'Oficinas',
                        capex: 120000000,
                        opex: 9600000,
                        l0: [
                            { id: 'BIM_L0_016', nombre: 'Mobiliario oficina', capex: 40000000, opex: 800000 },
                            { id: 'BIM_L0_060', nombre: 'PC Desktop Core i5', capex: 16000000, opex: 320000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.C2': {
        nombre: 'Satélite C2',
        capex: 142000000,
        opex: 11360000,
        l2: [
            {
                id: 'L2_SALA_EVAL',
                nombre: 'Sala Evaluación Teórica (8 cubículos)',
                capex: 62000000,
                opex: 4960000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos de Evaluación',
                        capex: 36000000,
                        opex: 720000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 36000000, opex: 720000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_ZONA_ADMIN',
                nombre: 'Zona Administrativa',
                capex: 80000000,
                opex: 6400000,
                l1: [
                    {
                        id: 'L1_RECEPCION',
                        nombre: 'Recepción y Atención',
                        capex: 80000000,
                        opex: 6400000,
                        l0: [
                            { id: 'BIM_L0_016', nombre: 'Mobiliario oficina', capex: 30000000, opex: 600000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.C3': {
        nombre: 'Satélite C3',
        capex: 71000000,
        opex: 5680000,
        l2: [
            {
                id: 'L2_SALA_EVAL',
                nombre: 'Sala Evaluación Teórica (4 cubículos)',
                capex: 31000000,
                opex: 2480000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos de Evaluación',
                        capex: 18000000,
                        opex: 360000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 18000000, opex: 360000 }
                        ]
                    }
                ]
            },
            {
                id: 'L2_RECEPCION',
                nombre: 'Recepción',
                capex: 40000000,
                opex: 3200000,
                l1: [
                    {
                        id: 'L1_ATENCION',
                        nombre: 'Área de Atención',
                        capex: 40000000,
                        opex: 3200000,
                        l0: [
                            { id: 'BIM_L0_016', nombre: 'Mobiliario oficina', capex: 20000000, opex: 400000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.C4': {
        nombre: 'Satélite C4',
        capex: 15500000,
        opex: 1240000,
        l2: [
            {
                id: 'L2_MODULO',
                nombre: 'Módulo 2 Cubículos',
                capex: 15500000,
                opex: 1240000,
                l1: [
                    {
                        id: 'L1_CUBICULOS',
                        nombre: 'Cubículos Compactos',
                        capex: 15500000,
                        opex: 1240000,
                        l0: [
                            { id: 'BIM_L0_023', nombre: 'Cubículos evaluación', capex: 9000000, opex: 180000 },
                            { id: 'BIM_L0_060', nombre: 'PC Desktop Core i5', capex: 6500000, opex: 130000 }
                        ]
                    }
                ]
            }
        ]
    },
    'CALE.C5': {
        nombre: 'Satélite C5 (Punto Info)',
        capex: 7750000,
        opex: 620000,
        l2: [
            {
                id: 'L2_PUNTO',
                nombre: 'Punto de Información',
                capex: 7750000,
                opex: 620000,
                l1: [
                    {
                        id: 'L1_KIOSKO',
                        nombre: 'Kiosko Digital',
                        capex: 7750000,
                        opex: 620000,
                        l0: [
                            { id: 'BIM_L0_065', nombre: 'Terminal kiosko', capex: 5000000, opex: 100000 },
                            { id: 'BIM_L0_063', nombre: 'Impresora térmica', capex: 2750000, opex: 55000 }
                        ]
                    }
                ]
            }
        ]
    }
};

// Función principal: Mostrar nodo L3 en sidebar derecha
function mostrarNodoEnSidebarDerecha(nodo) {
    const emptyState = document.getElementById('emptyState');
    const nodoSeleccionado = document.getElementById('nodoSeleccionado');
    const drillL2Container = document.getElementById('drillL2Container');

    if (!emptyState || !nodoSeleccionado || !drillL2Container) {
        console.warn('⚠️ Elementos del sidebar derecha no encontrados');
        return;
    }

    // Ocultar estado vacío, mostrar contenido
    emptyState.style.display = 'none';
    nodoSeleccionado.style.display = 'block';

    // Determinar categoría para buscar jerarquía
    const categoriaRaw = nodo.categoria_raw || determinarCategoriaRaw(nodo);
    const jerarquia = JERARQUIA_BIM_COMPLETA[categoriaRaw] || JERARQUIA_BIM_COMPLETA['CALE.n_1'];

    // Actualizar nombre del nodo
    document.getElementById('nombreNodoL3').textContent = `${nodo.nombre} (${nodo.departamento})`;

    // Actualizar resumen financiero
    document.getElementById('resumenCapex').textContent = formatCOP(jerarquia.capex);
    document.getElementById('resumenOpex').textContent = formatCOP(jerarquia.opex);

    // Generar HTML de componentes L2
    drillL2Container.innerHTML = jerarquia.l2.map((comp, idx) => `
        <div class="drill-item drill-l2" id="drillL2_${idx}">
            <div class="drill-header" onclick="toggleDrillL2(${idx})">
                <span class="drill-badge">L2</span>
                <span class="drill-title">${comp.nombre}</span>
                <span class="drill-arrow" id="arrowL2_${idx}">▶</span>
            </div>
            <div class="drill-body" id="bodyL2_${idx}">
                <div class="drill-body-content">
                    <div class="drill-subitem-values" style="margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(0,0,0,0.2); border-radius: 4px;">
                        <span class="capex">CAPEX: ${formatCOP(comp.capex)}</span>
                        <span class="opex">OPEX: ${formatCOP(comp.opex)}</span>
                    </div>
                    ${generarHTMLComponentesL1(comp.l1, idx)}
                </div>
            </div>
        </div>
    `).join('');

    console.log(`✅ Sidebar derecha actualizada para: ${nodo.nombre} (${categoriaRaw})`);
}

// Generar HTML para componentes L1 dentro de un L2
function generarHTMLComponentesL1(componentesL1, idxL2) {
    if (!componentesL1 || componentesL1.length === 0) return '<p style="color: var(--text-secondary); font-size: 0.8rem;">Sin componentes L1</p>';

    return componentesL1.map((comp, idxL1) => `
        <div class="drill-item drill-l1" id="drillL1_${idxL2}_${idxL1}" style="margin-left: 0.5rem;">
            <div class="drill-header" onclick="toggleDrillL1(${idxL2}, ${idxL1})">
                <span class="drill-badge">L1</span>
                <span class="drill-title">${comp.nombre}</span>
                <span class="drill-arrow" id="arrowL1_${idxL2}_${idxL1}">▶</span>
            </div>
            <div class="drill-body" id="bodyL1_${idxL2}_${idxL1}">
                <div class="drill-body-content">
                    <div class="drill-subitem-values" style="margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(0,0,0,0.2); border-radius: 4px;">
                        <span class="capex">CAPEX: ${formatCOP(comp.capex)}</span>
                        <span class="opex">OPEX: ${formatCOP(comp.opex)}</span>
                    </div>
                    ${generarHTMLElementosL0(comp.l0)}
                </div>
            </div>
        </div>
    `).join('');
}

// Generar HTML para elementos L0 (con botón Ver Ficha)
function generarHTMLElementosL0(elementosL0) {
    if (!elementosL0 || elementosL0.length === 0) return '<p style="color: var(--text-secondary); font-size: 0.8rem;">Sin elementos L0</p>';

    return elementosL0.map(elem => `
        <div class="drill-l0-item">
            <div class="drill-l0-info">
                <div class="drill-l0-id">${elem.id}</div>
                <div class="drill-l0-name">${elem.nombre}</div>
            </div>
            <a href="javascript:void(0);" onclick="mostrarFicha('../fichas/${elem.id}.html', '${elem.id} - ${elem.nombre}'); return false;" class="btn-ver-ficha">
                Ver Ficha
            </a>
        </div>
    `).join('');
}

// Toggle L2 accordion
function toggleDrillL2(idx) {
    const body = document.getElementById(`bodyL2_${idx}`);
    const arrow = document.getElementById(`arrowL2_${idx}`);

    if (body && arrow) {
        body.classList.toggle('expanded');
        arrow.classList.toggle('expanded');
    }
}

// Toggle L1 accordion
function toggleDrillL1(idxL2, idxL1) {
    const body = document.getElementById(`bodyL1_${idxL2}_${idxL1}`);
    const arrow = document.getElementById(`arrowL1_${idxL2}_${idxL1}`);

    if (body && arrow) {
        body.classList.toggle('expanded');
        arrow.classList.toggle('expanded');
    }
}

// Determinar categoría raw desde datos del nodo
function determinarCategoriaRaw(nodo) {
    const tipo = nodo.tipo_id || '';
    const cat = nodo.categoria || '';

    if (tipo.includes('n_1_plus')) return 'CALE.n_1+';
    if (tipo.includes('n_1') || cat.includes('A+') || cat.includes('Cat.A+')) return 'CALE.n_1';
    if (tipo.includes('n_2_plus')) return 'CALE.n_2**';
    if (tipo.includes('n_2') || cat.includes('Cat.A') || cat.includes('Cat.B')) return 'CALE.n_2';
    if (tipo.includes('n_3') || cat.includes('C1')) return 'CALE.n_3';
    if (tipo.includes('c2') || cat.includes('C2')) return 'CALE.C2';
    if (tipo.includes('c3') || cat.includes('C3')) return 'CALE.C3';
    if (tipo.includes('c4') || cat.includes('C4')) return 'CALE.C4';
    if (tipo.includes('c5') || cat.includes('C5')) return 'CALE.C5';

    return 'CALE.n_1'; // Default
}

// Limpiar sidebar derecha (volver a estado vacío)
function limpiarSidebarDerecha() {
    const emptyState = document.getElementById('emptyState');
    const nodoSeleccionado = document.getElementById('nodoSeleccionado');

    if (emptyState) emptyState.style.display = 'block';
    if (nodoSeleccionado) nodoSeleccionado.style.display = 'none';
}

// Mapeo de categorías a ficheros L3
const FICHAS_L3_MAPPING = {
    'CALE.n_1': '../cales/BIM_L3_001.html',
    'CALE.n_1+': '../cales/BIM_L3_001.html',
    'CALE.n_2': '../cales/BIM_L3_002.html',
    'CALE.n_2**': '../cales/BIM_L3_002.html',
    'CALE.n_3': '../cales/BIM_L3_003.html',
    'CALE.C2': '../cales/BIM_L3_C2.html',
    'CALE.C3': '../cales/BIM_L3_C3.html',
    'CALE.C4': '../cales/BIM_L3_C4.html',
    'CALE.C5': '../cales/BIM_L3_C5.html'
};

// Función para manejar el click del botón "Ver Ficha"
function verFichaL3() {
    if (!selectedNodo) {
        alert('Por favor selecciona un nodo primero');
        return;
    }

    const nodo = NODOS_DATA[selectedNodo];
    if (!nodo) {
        alert('No se encontraron datos del nodo');
        return;
    }

    const categoriaRaw = nodo.categoria_raw || determinarCategoriaRaw(nodo);
    const fichaUrl = FICHAS_L3_MAPPING[categoriaRaw];

    if (!fichaUrl) {
        console.warn(`⚠️ No se encontró URL para la categoría: ${categoriaRaw}`);
        alert(`No hay ficha disponible para esta categoría: ${categoriaRaw}`);
        return;
    }

    window.open(fichaUrl, '_blank');
}

// Funciones para toggle de sidebars
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('sidebarToggle');
    sidebar.classList.toggle('collapsed');
    toggle.textContent = sidebar.classList.contains('collapsed') ? '▶' : '◀';
}

function toggleSidebarRight() {
    const sidebarRight = document.getElementById('sidebarRight');
    const toggle = document.getElementById('sidebarRightToggle');
    sidebarRight.classList.toggle('collapsed');
    toggle.textContent = sidebarRight.classList.contains('collapsed') ? '◀' : '▶';
}

// Función para limpiar filtros
function limpiarFiltros() {
    const filters = document.querySelectorAll('.category-filter');
    filters.forEach(filter => {
        filter.checked = true;
    });
    
    renderizarSidebar();
    console.log('✅ Filtros limpiados');
}

// Agregar event listeners a los filtros
function inicializarFiltros() {
    const filters = document.querySelectorAll('.category-filter');
    filters.forEach(filter => {
        filter.addEventListener('change', () => {
            renderizarSidebar();
        });
    });
}

// Función para obtener filtros activos
function obtenerFiltrosActivos() {
    const filtros = [];
    const filters = document.querySelectorAll('.category-filter:checked');
    filters.forEach(filter => {
        filtros.push(filter.value);
    });
    return filtros;
}

// ========================================
// FUNCIONES PARA TOGGLE FICHA/MAPA
// ========================================

// Mostrar ficha dentro del contenedor del mapa
function mostrarFicha(urlFicha, titulo) {
    const fichaContainer = document.getElementById('fichaContainer');
    const fichaContent = document.getElementById('fichaContent');
    const fichaTitle = document.getElementById('fichaTitle');
    const mapDiv = document.getElementById('map');
    const btnVolverMapaHeader = document.getElementById('btnVolverMapaHeader');
    
    if (!fichaContainer || !fichaContent) return;
    
    // Actualizar título
    fichaTitle.textContent = titulo;
    
    // Crear iframe con la ficha
    // Inyectar CSS para posicionar sidebar a la derecha
    const fichaHTML = `
        <iframe src="${urlFicha}" style="
            width: 100%; 
            height: 100%; 
            border: none;"
            onload="this.contentDocument.body.style.display='flex'; this.contentDocument.body.style.flexDirection='row-reverse';"
        ></iframe>
    `;
    fichaContent.innerHTML = fichaHTML;
    
    // Ocultar mapa
    mapDiv.style.display = 'none';
    
    // MANTENER header visible (NO OCULTAR)
    // if (headerTop) headerTop.style.display = 'none'; // ← COMENTADO para mantener barra superior
    
    // Mostrar botón Volver al Mapa en el header
    if (btnVolverMapaHeader) btnVolverMapaHeader.classList.add('active');
    
    // Mostrar contenedor de ficha
    fichaContainer.classList.add('active');
}

// Centrar mapa en vista inicial
function centrarMapa() {
    if (map) {
        map.setView([MAPA_VISTA_INICIAL.lat, MAPA_VISTA_INICIAL.lng], MAPA_VISTA_INICIAL.zoom, {
            animate: true,
            duration: 0.5
        });
    }
}

// Volver a mostrar el mapa
function volverAlMapa() {
    const fichaContainer = document.getElementById('fichaContainer');
    const fichaContent = document.getElementById('fichaContent');
    const mapDiv = document.getElementById('map');
    const btnVolverMapaHeader = document.getElementById('btnVolverMapaHeader');
    
    if (!fichaContainer || !fichaContent) return;
    
    // Limpiar ficha
    fichaContent.innerHTML = '';
    
    // Ocultar contenedor de ficha
    fichaContainer.classList.remove('active');
    
    // Mostrar mapa
    mapDiv.style.display = 'block';
    
    // Ocultar botón Volver al Mapa del header
    if (btnVolverMapaHeader) btnVolverMapaHeader.classList.remove('active');
    
    // El header ya está visible (no necesita mostrarse de nuevo)
    // if (headerTop) headerTop.style.display = 'flex'; // ← Ya no es necesario
}

// Agregar event listener al botón cuando el DOM está listo
document.addEventListener('DOMContentLoaded', () => {
    const btnVerFicha = document.getElementById('btnVerFicha');
    if (btnVerFicha) {
        btnVerFicha.addEventListener('click', verFichaL3);
    }
    
    inicializarFiltros();
    inicializarFiltrosCategoria();
});

// Inicializar filtros de categoría (checkboxes superiores)
function inicializarFiltrosCategoria() {
    const checkboxes = document.querySelectorAll('#topCategories input[type="checkbox"]');
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', aplicarFiltrosCategoria);
    });
    
    console.log('✅ Filtros de categoría inicializados');
}

// Aplicar filtros de categoría al mapa
function aplicarFiltrosCategoria() {
    const checkboxes = document.querySelectorAll('#topCategories input[type="checkbox"]:checked');
    const categoriasActivas = Array.from(checkboxes).map(cb => cb.dataset.cat);
    
    // Si no hay ninguno seleccionado, mostrar todos
    const mostrarTodos = categoriasActivas.length === 0;
    
    // VISUALIZACIÓN 2: Lista de tipos excluidos
    const tiposExcluidos = ['L3.SATELITE.c2', 'L3.SATELITE.c3', 'L3.SATELITE.c4', 'L3.SATELITE.c5'];
    
    Object.values(NODOS_DATA).forEach(nodo => {
        const marker = markers[nodo.nodo_id];
        if (!marker) return;
        
        // VISUALIZACIÓN 2: Nunca mostrar C2-C5
        if (tiposExcluidos.includes(nodo.tipo_id)) {
            marker.remove();
            return;
        }
        
        // Determinar categoría del nodo
        const categoriaRaw = nodo.categoria_raw || determinarCategoriaRaw(nodo);
        
        // Verificar si debe mostrarse
        const debeMotrarse = mostrarTodos || categoriasActivas.includes(categoriaRaw);
        
        if (debeMotrarse) {
            // Agregar a capa correspondiente
            if (nodo.es_satelite || nodo.nodo_id.startsWith('SAT_')) {
                marker.addTo(layers.satelites);
            } else {
                marker.addTo(layers.principales);
            }
        } else {
            // Remover del mapa
            marker.remove();
        }
    });
    
    console.log(`🔍 Filtros aplicados: ${categoriasActivas.length > 0 ? categoriasActivas.join(', ') : 'Todos'}`);
}

console.log('✅ Script mapa-interactivo.js cargado');

// ========================================
// FUNCIÓN PARA CAMBIAR ENTRE ESCENARIOS
// ========================================

function cambiarEscenario() {
    console.log('🔄 Cambiando a Escenario 1...');
    // Navegar a la carpeta visualizacion
    window.location.href = '../visualizacion/mapa-interactivo.html';
}

