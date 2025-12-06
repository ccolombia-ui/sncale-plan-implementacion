#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script v2 para actualizar fichas L0 con barra lateral derecha
Incluye tablas de componentes con datos CAPEX/OPEX
Estructura: L3 -> L2 -> L1 -> L0
"""

import os
import re
import json

# Directorio de fichas L0
FICHAS_DIR = "fichas"

# Cargar datos de los archivos JSON
def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

# Datos de componentes por nivel
L3_DATA = load_json("TABLAS_L3_OFICIALES.json")
L3_TEORICO = load_json("TABLAS_L3_CALE_TEORICO.json")
L2_DATA = load_json("TABLAS_L2_OFICIALES.json") if os.path.exists("TABLAS_L2_OFICIALES.json") else {}
L1_DATA = load_json("TABLAS_L1_OFICIALES.json")
L0_DATA = load_json("TABLAS_L0_OFICIALES.json")

def format_cop(value):
    """Formatea valores en COP"""
    if value is None or value == 0:
        return "-"
    if value >= 1000000000:
        return f"${value/1000000000:.1f}B"
    elif value >= 1000000:
        return f"${value/1000000:.0f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value:,.0f}"

# CSS para la nueva barra lateral derecha
NEW_RIGHT_SIDEBAR_CSS = """
        /* SIDEBAR DERECHA v2 - TABLAS COMPONENTES */
        .sidebar-right {
            position: fixed;
            right: 0;
            top: 0;
            width: 380px;
            height: 100vh;
            background: linear-gradient(180deg, #1a5276 0%, #154360 100%);
            color: white;
            overflow-y: auto;
            padding: 12px;
            box-shadow: -4px 0 15px rgba(0,0,0,0.2);
            z-index: 1000;
            font-size: 0.85em;
        }

        .sidebar-right-header {
            text-align: center;
            padding: 10px;
            border-bottom: 2px solid rgba(255,255,255,0.2);
            margin-bottom: 12px;
        }

        .sidebar-right-title {
            font-size: 1.1em;
            font-weight: bold;
        }

        .sidebar-right-subtitle {
            font-size: 0.75em;
            opacity: 0.8;
            margin-top: 3px;
        }

        /* Secciones colapsables */
        .nivel-section {
            margin-bottom: 8px;
            border-radius: 6px;
            overflow: hidden;
            background: rgba(0,0,0,0.1);
        }

        .nivel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 12px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
            font-size: 0.95em;
        }

        .nivel-header:hover {
            filter: brightness(1.1);
        }

        .nivel-header .badge {
            background: rgba(255,255,255,0.25);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 8px;
        }

        .nivel-header .arrow {
            transition: transform 0.3s;
            font-size: 0.7em;
        }

        .nivel-header.active .arrow {
            transform: rotate(90deg);
        }

        .nivel-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
            background: rgba(0,0,0,0.15);
        }

        .nivel-content.show {
            max-height: 600px;
            overflow-y: auto;
        }

        .nivel-content-inner {
            padding: 10px;
        }

        /* Colores por nivel */
        .nivel-l3 .nivel-header { background: linear-gradient(135deg, #c0392b, #e74c3c); }
        .nivel-l2 .nivel-header { background: linear-gradient(135deg, #d35400, #e67e22); }
        .nivel-l1 .nivel-header { background: linear-gradient(135deg, #27ae60, #2ecc71); }
        .nivel-l0 .nivel-header { background: linear-gradient(135deg, #2980b9, #3498db); }

        /* Tabla compacta de componentes */
        .comp-table {
            width: 100%;
            font-size: 0.8em;
            border-collapse: collapse;
            background: rgba(255,255,255,0.05);
            border-radius: 4px;
            overflow: hidden;
        }

        .comp-table th {
            background: rgba(0,0,0,0.3);
            padding: 6px 4px;
            text-align: left;
            font-weight: 600;
            font-size: 0.85em;
            white-space: nowrap;
        }

        .comp-table td {
            padding: 5px 4px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            vertical-align: top;
        }

        .comp-table tr:hover {
            background: rgba(255,255,255,0.1);
        }

        .comp-table .bim-id {
            font-family: monospace;
            font-size: 0.85em;
            color: #f39c12;
            white-space: nowrap;
        }

        .comp-table .concepto {
            max-width: 120px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .comp-table .valor {
            text-align: right;
            font-family: monospace;
            font-size: 0.9em;
            white-space: nowrap;
        }

        .comp-table .capex { color: #2ecc71; }
        .comp-table .opex { color: #3498db; }

        /* Fila componente expandible */
        .comp-row {
            padding: 8px;
            margin-bottom: 6px;
            background: rgba(255,255,255,0.08);
            border-radius: 5px;
            border-left: 3px solid #f39c12;
            cursor: pointer;
            transition: all 0.2s;
        }

        .comp-row:hover {
            background: rgba(255,255,255,0.15);
            transform: translateX(3px);
        }

        .comp-row.current {
            background: rgba(243,156,18,0.3);
            border-left-color: #e74c3c;
        }

        .comp-row-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }

        .comp-row-id {
            font-family: monospace;
            color: #f39c12;
            font-weight: bold;
            font-size: 0.9em;
        }

        .comp-row-name {
            font-size: 0.85em;
            opacity: 0.9;
            margin-bottom: 4px;
        }

        .comp-row-details {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 4px;
            font-size: 0.75em;
            margin-top: 6px;
            padding-top: 6px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        .comp-row-details .detail-item {
            display: flex;
            justify-content: space-between;
        }

        .comp-row-details .label {
            opacity: 0.7;
        }

        .comp-row-details .value {
            font-family: monospace;
            font-weight: bold;
        }

        .comp-row-details .capex { color: #2ecc71; }
        .comp-row-details .opex { color: #3498db; }

        /* Boton ver ficha */
        .btn-ver-ficha {
            display: inline-block;
            padding: 3px 8px;
            background: #f39c12;
            color: white;
            text-decoration: none;
            border-radius: 3px;
            font-size: 0.75em;
            margin-left: 8px;
        }

        .btn-ver-ficha:hover {
            background: #e67e22;
        }

        .btn-indice {
            display: block;
            text-align: center;
            padding: 8px;
            background: linear-gradient(135deg, #f39c12, #d68910);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.85em;
            margin-top: 8px;
        }

        .btn-indice:hover {
            filter: brightness(1.1);
        }

        /* Resumen financiero */
        .resumen-financiero {
            background: rgba(0,0,0,0.2);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }

        .resumen-row {
            display: flex;
            justify-content: space-between;
            padding: 4px 0;
            font-size: 0.85em;
        }

        .resumen-row .label { opacity: 0.8; }
        .resumen-row .value { font-weight: bold; font-family: monospace; }
        .resumen-row .capex-total { color: #2ecc71; }
        .resumen-row .opex-total { color: #3498db; }

        /* Ajuste del contenido principal */
        .main-content {
            margin-right: 380px;
        }

        /* Toggle sidebar (movil) */
        .sidebar-right-toggle {
            display: none;
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1001;
            background: #1a5276;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.85em;
        }

        /* Responsivo */
        @media (max-width: 1400px) {
            .sidebar-right { width: 340px; }
            .main-content { margin-right: 340px; }
        }

        @media (max-width: 1200px) {
            .sidebar-right {
                transform: translateX(100%);
                transition: transform 0.3s;
            }
            .sidebar-right.active {
                transform: translateX(0);
            }
            .main-content { margin-right: 0; }
            .sidebar-right-toggle { display: block; }
        }
"""

def get_l3_components():
    """Obtiene componentes L3 con datos financieros"""
    components = []

    # Datos de L3 Oficiales
    if L3_DATA and "configuraciones" in L3_DATA:
        for config in L3_DATA["configuraciones"][:4]:  # Primeros 4
            capex = config.get("valorizacion", {}).get("total_cop", 0)
            components.append({
                "bim_id": config.get("bim_id", ""),
                "nombre": config.get("titulo", "").replace("CALE.", ""),
                "tipo": config.get("tipo_cale", ""),
                "cantidad": config.get("cantidad_base", 0),
                "capex": capex,
                "opex": int(capex * 0.08),  # Estimacion 8% OPEX
                "ficha": f"../fichas_l3_unitarias/{config.get('bim_id', '')}.html"
            })

    # Datos de L3 Teorico
    if L3_TEORICO and "componentes" in L3_TEORICO:
        for key, comp in list(L3_TEORICO["componentes"].items())[:3]:
            components.append({
                "bim_id": comp.get("bim_id", ""),
                "nombre": comp.get("nombre", ""),
                "tipo": "Teorico",
                "cantidad": 1,
                "capex": comp.get("valor_total_capex", 0),
                "opex": comp.get("valor_total_opex_anual", 0),
                "ficha": f"../fichas_l3_unitarias/{comp.get('bim_id', '')}.html"
            })

    return components[:7]  # Maximo 7

def get_l2_components():
    """Obtiene componentes L2"""
    components = []

    # Datos basicos L2
    l2_items = [
        {"bim_id": "BIM_L2_001", "nombre": "Pista Clase I (Motos+Carros)", "capex": 721440000},
        {"bim_id": "BIM_L2_002", "nombre": "Pista Clase II (Camiones)", "capex": 980000000},
        {"bim_id": "BIM_L2_003", "nombre": "Pista Clase III (Articulados)", "capex": 1850000000},
        {"bim_id": "BIM_L2_004", "nombre": "Sala Evaluacion Teorica", "capex": 186000000},
        {"bim_id": "BIM_L2_005", "nombre": "Edificacion Administrativa", "capex": 2400000000},
    ]

    for item in l2_items:
        components.append({
            "bim_id": item["bim_id"],
            "nombre": item["nombre"],
            "unidad": "glb",
            "cantidad": 1,
            "capex": item["capex"],
            "opex": int(item["capex"] * 0.05),
            "ficha": f"../fichas_l2/{item['bim_id']}.html"
        })

    return components

def get_l1_components():
    """Obtiene componentes L1"""
    components = []

    if L1_DATA and "componentes" in L1_DATA:
        for key, comp in list(L1_DATA["componentes"].items())[:6]:
            components.append({
                "bim_id": comp.get("bim_id", ""),
                "nombre": comp.get("nombre", ""),
                "unidad": comp.get("unidad", "glb"),
                "cantidad": comp.get("cantidad", 1),
                "capex": comp.get("valor_cop", 0),
                "opex": int(comp.get("valor_cop", 0) * 0.03),
                "ficha": f"../fichas_l1/{comp.get('bim_id', '')}.html"
            })

    return components

def get_l0_components(current_id):
    """Obtiene componentes L0 representativos"""
    components = []

    # Componentes representativos
    l0_samples = [
        ("BIM_L0_001", "Pavimento flexible", "m2", 85000),
        ("BIM_L0_015", "Edificacion CALE", "m2", 2500000),
        ("BIM_L0_023", "Cubiculos evaluacion", "und", 4500000),
        ("BIM_L0_035", "Luminaria LED 150W", "und", 850000),
        ("BIM_L0_060", "PC Desktop Core i5", "und", 3200000),
        ("BIM_L0_077", "Motocicleta adaptada", "und", 12000000),
        ("BIM_L0_079", "Automovil B1/C1", "und", 65000000),
    ]

    for bim_id, nombre, unidad, capex in l0_samples:
        is_current = bim_id == current_id
        components.append({
            "bim_id": bim_id,
            "nombre": nombre,
            "unidad": unidad,
            "cantidad": 1,
            "capex": capex,
            "opex": int(capex * 0.02),
            "ficha": f"{bim_id}.html",
            "current": is_current
        })

    # Agregar el actual si no esta en la lista
    if current_id and not any(c["bim_id"] == current_id for c in components):
        components.insert(0, {
            "bim_id": current_id,
            "nombre": "Componente Actual",
            "unidad": "und",
            "cantidad": 1,
            "capex": 0,
            "opex": 0,
            "ficha": f"{current_id}.html",
            "current": True
        })

    return components[:8]

def generate_component_rows(components, level):
    """Genera filas de componentes para la tabla"""
    rows = ""
    for comp in components:
        current_class = " current" if comp.get("current", False) else ""
        ficha_link = f'<a href="{comp["ficha"]}" class="btn-ver-ficha">Ver</a>' if comp.get("ficha") else ""

        rows += f'''
                <div class="comp-row{current_class}">
                    <div class="comp-row-header">
                        <span class="comp-row-id">{comp["bim_id"]}</span>
                        {ficha_link}
                    </div>
                    <div class="comp-row-name">{comp["nombre"]}</div>
                    <div class="comp-row-details">
                        <div class="detail-item">
                            <span class="label">Unidad:</span>
                            <span class="value">{comp.get("unidad", "glb")}</span>
                        </div>
                        <div class="detail-item">
                            <span class="label">Cant:</span>
                            <span class="value">{comp.get("cantidad", 1)}</span>
                        </div>
                        <div class="detail-item">
                            <span class="label">CAPEX:</span>
                            <span class="value capex">{format_cop(comp.get("capex", 0))}</span>
                        </div>
                        <div class="detail-item">
                            <span class="label">OPEX:</span>
                            <span class="value opex">{format_cop(comp.get("opex", 0))}</span>
                        </div>
                    </div>
                </div>'''
    return rows

def generate_right_sidebar_html(current_l0_id):
    """Genera el HTML de la barra lateral derecha con tablas"""

    l3_components = get_l3_components()
    l2_components = get_l2_components()
    l1_components = get_l1_components()
    l0_components = get_l0_components(current_l0_id)

    # Calcular totales
    total_capex = sum(c.get("capex", 0) for c in l3_components)
    total_opex = sum(c.get("opex", 0) for c in l3_components)

    html = f'''
    <!-- BOTON TOGGLE SIDEBAR DERECHA (MOVIL) -->
    <button class="sidebar-right-toggle" onclick="toggleSidebarRight()">Componentes BIM</button>

    <!-- SIDEBAR DERECHA v2 - TABLAS COMPONENTES -->
    <aside class="sidebar-right">
        <div class="sidebar-right-header">
            <div class="sidebar-right-title">Jerarquia BIM SNCALE</div>
            <div class="sidebar-right-subtitle">Componentes con CAPEX / OPEX</div>
        </div>

        <!-- RESUMEN FINANCIERO -->
        <div class="resumen-financiero">
            <div class="resumen-row">
                <span class="label">CAPEX Total L3:</span>
                <span class="value capex-total">{format_cop(total_capex)}</span>
            </div>
            <div class="resumen-row">
                <span class="label">OPEX Anual Est.:</span>
                <span class="value opex-total">{format_cop(total_opex)}</span>
            </div>
        </div>

        <!-- NIVEL L3: CAPACIDAD -->
        <div class="nivel-section nivel-l3">
            <div class="nivel-header active" onclick="toggleNivel(this)">
                <div>
                    <span class="badge">L3</span>
                    Capacidad - Tipos CALE
                </div>
                <span class="arrow">&#9654;</span>
            </div>
            <div class="nivel-content show">
                <div class="nivel-content-inner">
                    {generate_component_rows(l3_components, "L3")}
                    <a href="../fichas_l3_unitarias/BIM_L3_001.html" class="btn-indice">Ver Fichas L3</a>
                </div>
            </div>
        </div>

        <!-- NIVEL L2: DISTRIBUCION -->
        <div class="nivel-section nivel-l2">
            <div class="nivel-header" onclick="toggleNivel(this)">
                <div>
                    <span class="badge">L2</span>
                    Distribucion - Configuraciones
                </div>
                <span class="arrow">&#9654;</span>
            </div>
            <div class="nivel-content">
                <div class="nivel-content-inner">
                    {generate_component_rows(l2_components, "L2")}
                    <a href="../fichas_l2/index_l2.html" class="btn-indice">Ver Indice L2</a>
                </div>
            </div>
        </div>

        <!-- NIVEL L1: UNIDADES FUNCIONALES -->
        <div class="nivel-section nivel-l1">
            <div class="nivel-header" onclick="toggleNivel(this)">
                <div>
                    <span class="badge">L1</span>
                    Unidades Funcionales
                </div>
                <span class="arrow">&#9654;</span>
            </div>
            <div class="nivel-content">
                <div class="nivel-content-inner">
                    {generate_component_rows(l1_components, "L1")}
                    <a href="../fichas_l1/index_l1.html" class="btn-indice">Ver Indice L1</a>
                </div>
            </div>
        </div>

        <!-- NIVEL L0: ELEMENTOS -->
        <div class="nivel-section nivel-l0">
            <div class="nivel-header" onclick="toggleNivel(this)">
                <div>
                    <span class="badge">L0</span>
                    Elementos Atomicos
                </div>
                <span class="arrow">&#9654;</span>
            </div>
            <div class="nivel-content">
                <div class="nivel-content-inner">
                    {generate_component_rows(l0_components, "L0")}
                    <a href="../fichas_l0/index_l0.html" class="btn-indice">Ver 91 Componentes L0</a>
                </div>
            </div>
        </div>

        <!-- Enlaces rapidos -->
        <div style="margin-top: 15px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.2);">
            <a href="../visualizacion/mapa-interactivo.html" style="display: block; padding: 8px; background: rgba(255,255,255,0.1); color: white; text-decoration: none; border-radius: 5px; margin-bottom: 6px; text-align: center; font-size: 0.8em;">
                Mapa Interactivo 197 Nodos
            </a>
            <a href="../index.html" style="display: block; padding: 8px; background: rgba(255,255,255,0.1); color: white; text-decoration: none; border-radius: 5px; text-align: center; font-size: 0.8em;">
                Dashboard Principal
            </a>
        </div>
    </aside>
'''
    return html


NEW_RIGHT_SIDEBAR_JS = """
        // Toggle sidebar derecha
        function toggleSidebarRight() {
            document.querySelector('.sidebar-right').classList.toggle('active');
        }

        // Toggle secciones de nivel
        function toggleNivel(header) {
            header.classList.toggle('active');
            const content = header.nextElementSibling;
            content.classList.toggle('show');
        }

        // Cerrar sidebar derecha al hacer clic fuera (movil)
        document.querySelector('.main-content').addEventListener('click', function() {
            if (window.innerWidth <= 1200) {
                document.querySelector('.sidebar-right').classList.remove('active');
            }
        });
"""


def update_ficha(filepath):
    """Actualiza una ficha L0 reemplazando la barra lateral derecha"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    l0_id = filename.replace('.html', '')

    # Verificar si ya tiene la v1 de sidebar-right
    has_old_sidebar = 'sidebar-right' in content

    if has_old_sidebar:
        # Remover CSS antiguo de sidebar-right
        content = re.sub(
            r'/\* SIDEBAR DERECHA.*?(?=\s*/\* Toggle sidebar derecha|\s*/\* Responsivo|\s*@media)',
            '',
            content,
            flags=re.DOTALL
        )

        # Remover el HTML de sidebar-right antiguo
        content = re.sub(
            r'<!-- BOTON TOGGLE SIDEBAR DERECHA.*?</aside>\s*',
            '',
            content,
            flags=re.DOTALL
        )

        # Remover funciones JS antiguas
        content = re.sub(
            r'// Toggle sidebar derecha\s*function toggleSidebarRight.*?(?=\s*</script>)',
            '',
            content,
            flags=re.DOTALL
        )

    # 1. Agregar nuevo CSS antes del cierre de </style>
    if '</style>' in content and 'SIDEBAR DERECHA v2' not in content:
        content = content.replace('</style>', NEW_RIGHT_SIDEBAR_CSS + '\n    </style>')

    # 2. Agregar nuevo HTML de la barra lateral derecha antes de </body>
    sidebar_html = generate_right_sidebar_html(l0_id)
    if '</body>' in content and 'nivel-section nivel-l3' not in content:
        content = content.replace('</body>', sidebar_html + '\n</body>')

    # 3. Agregar JavaScript
    if '<script>' in content and '</script>' in content and 'toggleNivel' not in content:
        content = content.replace('</script>', NEW_RIGHT_SIDEBAR_JS + '\n    </script>')

    # Guardar archivo actualizado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Actualizado: {filename}")
    return True


def main():
    print("=" * 60)
    print("ACTUALIZANDO FICHAS L0 - SIDEBAR DERECHA v2")
    print("Con tablas de componentes CAPEX/OPEX")
    print("=" * 60)

    # Obtener lista de fichas L0
    fichas = []
    for f in os.listdir(FICHAS_DIR):
        if f.startswith('BIM_L0_') and f.endswith('.html'):
            fichas.append(os.path.join(FICHAS_DIR, f))

    fichas.sort()
    print(f"\nEncontradas {len(fichas)} fichas L0")
    print("-" * 40)

    updated = 0
    for filepath in fichas:
        if update_ficha(filepath):
            updated += 1

    print("-" * 40)
    print(f"Actualizadas: {updated}/{len(fichas)} fichas")
    print("=" * 60)


if __name__ == "__main__":
    main()
