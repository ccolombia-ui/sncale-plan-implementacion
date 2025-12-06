#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para actualizar fichas L0 con barra lateral derecha jerarquica
Incluye navegacion colapsable: L3 -> L2 -> L1 -> L0
"""

import os
import re

# Directorio de fichas L0
FICHAS_DIR = "fichas"

# Datos de la jerarquia BIM
HIERARCHY_L3 = [
    {"id": "BIM_L3_001", "nombre": "CALE Metropolitano (n_1)", "file": "../fichas_l3_unitarias/BIM_L3_001.html",
     "capacidad": "24 cubiculos", "pistas": "Clase I + II + III"},
    {"id": "BIM_L3_002", "nombre": "CALE Regional (n_2)", "file": "../fichas_l3_unitarias/BIM_L3_002.html",
     "capacidad": "18 cubiculos", "pistas": "Clase I + II"},
    {"id": "BIM_L3_003", "nombre": "CALE Provincial (n_3)", "file": "../fichas_l3_unitarias/BIM_L3_003.html",
     "capacidad": "12 cubiculos", "pistas": "Clase I"},
    {"id": "BIM_L3_C2", "nombre": "Satelite C2", "file": "../fichas_l3_unitarias/BIM_L3_C2.html",
     "capacidad": "6 cubiculos", "pistas": "Solo teorico"},
    {"id": "BIM_L3_C3", "nombre": "Satelite C3", "file": "../fichas_l3_unitarias/BIM_L3_C3.html",
     "capacidad": "6 cubiculos", "pistas": "Solo teorico"},
    {"id": "BIM_L3_C4", "nombre": "Satelite C4", "file": "../fichas_l3_unitarias/BIM_L3_C4.html",
     "capacidad": "6 cubiculos", "pistas": "Solo teorico"},
    {"id": "BIM_L3_C5", "nombre": "Satelite C5", "file": "../fichas_l3_unitarias/BIM_L3_C5.html",
     "capacidad": "6 cubiculos", "pistas": "Solo teorico"},
]

HIERARCHY_L2 = [
    {"id": "BIM_L2_001", "nombre": "Pista Clase I (Motos+Carros)", "file": "../fichas_l2/BIM_L2_001.html"},
    {"id": "BIM_L2_002", "nombre": "Pista Clase II (Camiones)", "file": "../fichas_l2/BIM_L2_002.html"},
    {"id": "BIM_L2_003", "nombre": "Pista Clase III (Articulados)", "file": "../fichas_l2/BIM_L2_003.html"},
    {"id": "BIM_L2_004", "nombre": "Edificacion Administrativa", "file": "../fichas_l2/BIM_L2_004.html"},
    {"id": "BIM_L2_005", "nombre": "Instalaciones Especiales", "file": "../fichas_l2/BIM_L2_005.html"},
]

HIERARCHY_L1 = [
    {"id": "BIM_L1_001", "nombre": "Pista Motos A1/A2", "file": "../fichas_l1/BIM_L1_001.html"},
    {"id": "BIM_L1_002", "nombre": "Pista Carros B1/C1", "file": "../fichas_l1/BIM_L1_002.html"},
    {"id": "BIM_L1_003", "nombre": "Sala Evaluacion Teorica", "file": "../fichas_l1/BIM_L1_003.html"},
    {"id": "BIM_L1_004", "nombre": "Sistema Tecnologico", "file": "../fichas_l1/BIM_L1_004.html"},
]

# CSS adicional para la barra lateral derecha
RIGHT_SIDEBAR_CSS = """
        /* SIDEBAR DERECHA - JERARQUIA BIM COLAPSABLE */
        .sidebar-right {
            position: fixed;
            right: 0;
            top: 0;
            width: 320px;
            height: 100vh;
            background: linear-gradient(180deg, #1a5276 0%, #154360 100%);
            color: white;
            overflow-y: auto;
            padding: 15px;
            box-shadow: -4px 0 10px rgba(0,0,0,0.15);
            z-index: 1000;
            font-size: 0.9em;
        }

        .sidebar-right-header {
            text-align: center;
            padding-bottom: 15px;
            border-bottom: 2px solid rgba(255,255,255,0.2);
            margin-bottom: 15px;
        }

        .sidebar-right-title {
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .sidebar-right-subtitle {
            font-size: 0.8em;
            opacity: 0.8;
        }

        /* Secciones colapsables */
        .collapse-section {
            margin-bottom: 10px;
            border-radius: 6px;
            overflow: hidden;
        }

        .collapse-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 15px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
        }

        .collapse-header:hover {
            filter: brightness(1.1);
        }

        .collapse-header .level-badge {
            background: rgba(255,255,255,0.2);
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            margin-right: 8px;
        }

        .collapse-header .arrow {
            transition: transform 0.3s;
            font-size: 0.8em;
        }

        .collapse-header.active .arrow {
            transform: rotate(90deg);
        }

        .collapse-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
            background: rgba(0,0,0,0.15);
        }

        .collapse-content.show {
            max-height: 500px;
        }

        .collapse-content-inner {
            padding: 10px 15px;
        }

        /* Colores por nivel */
        .section-l3 .collapse-header { background: linear-gradient(135deg, #8b0000, #dc143c); }
        .section-l2 .collapse-header { background: linear-gradient(135deg, #e74c3c, #c0392b); }
        .section-l1 .collapse-header { background: linear-gradient(135deg, #27ae60, #229954); }
        .section-l0 .collapse-header { background: linear-gradient(135deg, #3498db, #2980b9); }

        /* Items dentro de secciones */
        .hierarchy-item {
            display: block;
            padding: 8px 10px;
            margin: 4px 0;
            background: rgba(255,255,255,0.08);
            border-radius: 4px;
            color: white;
            text-decoration: none;
            font-size: 0.85em;
            transition: all 0.2s;
            border-left: 3px solid transparent;
        }

        .hierarchy-item:hover {
            background: rgba(255,255,255,0.18);
            transform: translateX(3px);
            border-left-color: white;
        }

        .hierarchy-item.current {
            background: rgba(255,255,255,0.25);
            border-left-color: #f39c12;
            font-weight: bold;
        }

        .hierarchy-item-id {
            font-family: monospace;
            font-size: 0.9em;
            opacity: 0.7;
        }

        .hierarchy-item-name {
            display: block;
            margin-top: 2px;
        }

        /* Info de capacidad */
        .capacity-info {
            background: rgba(255,255,255,0.1);
            padding: 10px;
            border-radius: 5px;
            margin: 8px 0;
            border-left: 3px solid #f39c12;
        }

        .capacity-info-row {
            display: flex;
            justify-content: space-between;
            padding: 4px 0;
            font-size: 0.9em;
        }

        .capacity-label {
            opacity: 0.8;
        }

        .capacity-value {
            font-weight: bold;
            color: #f39c12;
        }

        /* Boton ver ficha */
        .btn-ficha {
            display: block;
            text-align: center;
            padding: 10px;
            background: linear-gradient(135deg, #f39c12, #d68910);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.9em;
            margin-top: 8px;
            transition: all 0.3s;
        }

        .btn-ficha:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(243, 156, 18, 0.4);
        }

        /* Ajuste del contenido principal para sidebar derecha */
        .main-content {
            margin-right: 320px;
        }

        /* Toggle sidebar derecha (movil) */
        .sidebar-right-toggle {
            display: none;
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1001;
            background: #1a5276;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Responsivo */
        @media (max-width: 1400px) {
            .sidebar-right {
                width: 280px;
            }
            .main-content {
                margin-right: 280px;
            }
        }

        @media (max-width: 1200px) {
            .sidebar-right {
                transform: translateX(100%);
                transition: transform 0.3s;
            }

            .sidebar-right.active {
                transform: translateX(0);
            }

            .main-content {
                margin-right: 0;
            }

            .sidebar-right-toggle {
                display: block;
            }
        }
"""

def generate_right_sidebar_html(current_l0_id):
    """Genera el HTML de la barra lateral derecha"""

    # Generar items L3
    l3_items = ""
    for item in HIERARCHY_L3:
        l3_items += f'''
                            <a href="{item['file']}" class="hierarchy-item">
                                <span class="hierarchy-item-id">{item['id']}</span>
                                <span class="hierarchy-item-name">{item['nombre']}</span>
                            </a>
                            <div class="capacity-info">
                                <div class="capacity-info-row">
                                    <span class="capacity-label">Cubiculos:</span>
                                    <span class="capacity-value">{item['capacidad']}</span>
                                </div>
                                <div class="capacity-info-row">
                                    <span class="capacity-label">Pistas:</span>
                                    <span class="capacity-value">{item['pistas']}</span>
                                </div>
                            </div>'''

    # Generar items L2
    l2_items = ""
    for item in HIERARCHY_L2:
        l2_items += f'''
                            <a href="{item['file']}" class="hierarchy-item">
                                <span class="hierarchy-item-id">{item['id']}</span>
                                <span class="hierarchy-item-name">{item['nombre']}</span>
                            </a>'''

    # Generar items L1
    l1_items = ""
    for item in HIERARCHY_L1:
        l1_items += f'''
                            <a href="{item['file']}" class="hierarchy-item">
                                <span class="hierarchy-item-id">{item['id']}</span>
                                <span class="hierarchy-item-name">{item['nombre']}</span>
                            </a>'''

    # Generar items L0 (solo algunos representativos, el actual marcado)
    l0_items = ""
    l0_samples = [
        ("BIM_L0_001", "Pavimento flexible asfalto"),
        ("BIM_L0_015", "Edificacion principal CALE"),
        ("BIM_L0_023", "Cubiculos evaluacion"),
        ("BIM_L0_035", "Luminaria LED 150W"),
        ("BIM_L0_060", "PC Desktop Core i5"),
        ("BIM_L0_077", "Motocicleta adaptada"),
        ("BIM_L0_079", "Automovil B1/C1 adaptado"),
    ]

    for l0_id, l0_name in l0_samples:
        current_class = " current" if l0_id == current_l0_id else ""
        l0_items += f'''
                            <a href="{l0_id}.html" class="hierarchy-item{current_class}">
                                <span class="hierarchy-item-id">{l0_id}</span>
                                <span class="hierarchy-item-name">{l0_name}</span>
                            </a>'''

    # Si el L0 actual no esta en los ejemplos, agregarlo
    if current_l0_id and not any(current_l0_id == l0[0] for l0 in l0_samples):
        l0_items = f'''
                            <a href="{current_l0_id}.html" class="hierarchy-item current">
                                <span class="hierarchy-item-id">{current_l0_id}</span>
                                <span class="hierarchy-item-name">Componente Actual</span>
                            </a>''' + l0_items

    html = f'''
    <!-- BOTON TOGGLE SIDEBAR DERECHA (MOVIL) -->
    <button class="sidebar-right-toggle" onclick="toggleSidebarRight()">Jerarquia BIM</button>

    <!-- SIDEBAR DERECHA - JERARQUIA BIM -->
    <aside class="sidebar-right">
        <div class="sidebar-right-header">
            <div class="sidebar-right-title">Jerarquia BIM SNCALE</div>
            <div class="sidebar-right-subtitle">Navegacion por niveles</div>
        </div>

        <div class="hierarchy-tree">
            <!-- NIVEL L3: CAPACIDAD -->
            <div class="collapse-section section-l3">
                <div class="collapse-header active" onclick="toggleCollapse(this)">
                    <div>
                        <span class="level-badge">L3</span>
                        Capacidad - Tipos CALE
                    </div>
                    <span class="arrow">&#9654;</span>
                </div>
                <div class="collapse-content show">
                    <div class="collapse-content-inner">{l3_items}
                        <a href="../fichas_l3_unitarias/BIM_L3_001.html" class="btn-ficha">Ver Todas las Fichas L3</a>
                    </div>
                </div>
            </div>

            <!-- NIVEL L2: DISTRIBUCION -->
            <div class="collapse-section section-l2">
                <div class="collapse-header" onclick="toggleCollapse(this)">
                    <div>
                        <span class="level-badge">L2</span>
                        Distribucion - Configuraciones
                    </div>
                    <span class="arrow">&#9654;</span>
                </div>
                <div class="collapse-content">
                    <div class="collapse-content-inner">{l2_items}
                        <a href="../fichas_l2/index_l2.html" class="btn-ficha">Ver Indice L2 Completo</a>
                    </div>
                </div>
            </div>

            <!-- NIVEL L1: UNIDADES FUNCIONALES -->
            <div class="collapse-section section-l1">
                <div class="collapse-header" onclick="toggleCollapse(this)">
                    <div>
                        <span class="level-badge">L1</span>
                        Unidades Funcionales
                    </div>
                    <span class="arrow">&#9654;</span>
                </div>
                <div class="collapse-content">
                    <div class="collapse-content-inner">{l1_items}
                        <a href="../fichas_l1/index_l1.html" class="btn-ficha">Ver Indice L1 Completo</a>
                    </div>
                </div>
            </div>

            <!-- NIVEL L0: ELEMENTOS -->
            <div class="collapse-section section-l0">
                <div class="collapse-header" onclick="toggleCollapse(this)">
                    <div>
                        <span class="level-badge">L0</span>
                        Elementos Atomicos
                    </div>
                    <span class="arrow">&#9654;</span>
                </div>
                <div class="collapse-content">
                    <div class="collapse-content-inner">{l0_items}
                        <a href="../fichas_l0/index_l0.html" class="btn-ficha">Ver 91 Componentes L0</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Enlaces rapidos -->
        <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.2);">
            <a href="../visualizacion/mapa-interactivo.html" style="display: block; padding: 10px; background: rgba(255,255,255,0.1); color: white; text-decoration: none; border-radius: 5px; margin-bottom: 8px; text-align: center; font-size: 0.85em;">
                Mapa Interactivo 197 Nodos
            </a>
            <a href="../index.html" style="display: block; padding: 10px; background: rgba(255,255,255,0.1); color: white; text-decoration: none; border-radius: 5px; text-align: center; font-size: 0.85em;">
                Dashboard Principal
            </a>
        </div>
    </aside>
'''
    return html


RIGHT_SIDEBAR_JS = """
        // Toggle sidebar derecha
        function toggleSidebarRight() {
            document.querySelector('.sidebar-right').classList.toggle('active');
        }

        // Toggle secciones colapsables
        function toggleCollapse(header) {
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
    """Actualiza una ficha L0 con la barra lateral derecha"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer el ID L0 del archivo
    filename = os.path.basename(filepath)
    l0_id = filename.replace('.html', '')

    # Si ya tiene sidebar-right, saltar
    if 'sidebar-right' in content:
        print(f"  Ya actualizado: {filename}")
        return False

    # 1. Agregar CSS antes del cierre de </style>
    if '</style>' in content:
        content = content.replace('</style>', RIGHT_SIDEBAR_CSS + '\n    </style>')

    # 2. Agregar HTML de la barra lateral derecha antes de </body>
    sidebar_html = generate_right_sidebar_html(l0_id)

    # Buscar el cierre de body y agregar antes del script existente
    if '</body>' in content:
        # Agregar sidebar HTML justo antes de </body>
        content = content.replace('</body>', sidebar_html + '\n</body>')

    # 3. Agregar JavaScript para toggle
    # Buscar el script existente y agregar funciones
    if '<script>' in content and '</script>' in content:
        # Agregar las nuevas funciones al script existente
        content = content.replace('</script>', RIGHT_SIDEBAR_JS + '\n    </script>')

    # Guardar archivo actualizado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Actualizado: {filename}")
    return True


def main():
    print("=" * 60)
    print("ACTUALIZANDO FICHAS L0 CON SIDEBAR DERECHA JERARQUICA")
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
