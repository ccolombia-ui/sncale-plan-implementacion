#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para convertir todas las fichas BIM_L0 al nuevo formato con CARDS
Basado en el formato de BIM_L0_001.html
"""

import os
import re
from pathlib import Path

# Ruta de la carpeta de fichas
FICHAS_DIR = Path(__file__).parent / "fichas"

# CSS completo del nuevo formato con cards
NEW_CSS = """        :root {
            --primary-color: #333;
            --secondary-color: #666;
            --accent-color: #999;
            --success-color: #27ae60;
            --warning-color: #f39c12;
            --bg-light: #f5f7fa;
            --sidebar-width: 280px;
            --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
            --card-shadow-hover: 0 8px 16px rgba(0,0,0,0.15);
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--primary-color);
            background: var(--bg-light);
            display: flex;
        }
        
        /* SIDEBAR - JERARQUÍA BIM */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: var(--sidebar-width);
            height: 100vh;
            background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
            color: #000;
            overflow-y: auto;
            padding: 20px;
            box-shadow: 4px 0 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        
        .sidebar-header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #ddd;
            margin-bottom: 20px;
        }
        
        .sidebar-logo {
            font-size: 2em;
            margin-bottom: 5px;
        }
        
        .sidebar-title {
            font-size: 0.9em;
            opacity: 0.8;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Árbol jerárquico BIM */
        .bim-tree {
            margin-top: 20px;
        }
        
        .tree-level {
            margin: 15px 0;
            position: relative;
        }
        
        .tree-level::before {
            content: '';
            position: absolute;
            left: 10px;
            top: 30px;
            bottom: -15px;
            width: 2px;
            background: rgba(255,255,255,0.2);
        }
        
        .tree-level:last-child::before {
            display: none;
        }
        
        .level-header {
            display: flex;
            align-items: center;
            padding: 10px;
            background: rgba(255,255,255,0.1);
            border-radius: 5px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .level-header:hover {
            background: rgba(255,255,255,0.2);
            transform: translateX(5px);
        }
        
        .level-header.active {
            background: var(--secondary-color);
            box-shadow: 0 2px 8px rgba(52,152,219,0.3);
        }
        
        .level-checkbox {
            margin-right: 10px;
            font-size: 1.2em;
        }
        
        .level-badge {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.75em;
            font-weight: bold;
            margin-right: 8px;
            min-width: 35px;
            text-align: center;
        }
        
        .level-name {
            font-weight: 600;
            font-size: 0.95em;
        }
        
        .level-items {
            margin-left: 35px;
            padding-left: 15px;
            border-left: 2px solid rgba(255,255,255,0.15);
        }
        
        .item-node {
            padding: 8px 10px;
            margin: 5px 0;
            background: rgba(255,255,255,0.05);
            border-radius: 4px;
            font-size: 0.85em;
            position: relative;
            transition: all 0.2s;
        }
        
        .item-node::before {
            content: '├─';
            position: absolute;
            left: -15px;
            color: rgba(255,255,255,0.3);
        }
        
        .item-node:last-child::before {
            content: '└─';
        }
        
        .item-node:hover {
            background: rgba(255,255,255,0.15);
            transform: translateX(3px);
        }
        
        .item-node.current {
            background: var(--accent-color);
            font-weight: bold;
            box-shadow: 0 2px 6px rgba(231,76,60,0.3);
        }
        
        .item-code {
            color: rgba(255,255,255,0.6);
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        
        /* MAIN CONTENT */
        .main-content {
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 20px;
            max-width: calc(100% - var(--sidebar-width));
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        /* Toggle sidebar button (móvil) */
        .sidebar-toggle {
            display: none;
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1001;
            background: var(--primary-color);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        
        /* Header BIM */
        .bim-header {
            background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
            color: #000;
            padding: 40px;
            border-radius: 12px;
            margin-bottom: 40px;
            box-shadow: var(--card-shadow);
        }
        
        .bim-id {
            font-size: 2.8em;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--secondary-color);
        }
        
        .bim-nivel {
            display: inline-block;
            background: rgba(0,0,0,0.1);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        
        .bim-header h1 {
            margin-top: 20px;
            font-size: 2em;
            color: var(--primary-color);
        }
        
        .bim-header p {
            opacity: 0.8;
            margin-top: 10px;
            font-size: 1.05em;
        }

        /* Grid de Cards */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        /* Card Styling */
        .card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--secondary-color), var(--accent-color));
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: var(--card-shadow-hover);
        }

        .card-icon {
            font-size: 3em;
            margin-bottom: 15px;
            display: block;
        }

        .card-title {
            font-size: 1.4em;
            font-weight: bold;
            color: var(--secondary-color);
            margin-bottom: 20px;
            border-bottom: 2px solid var(--bg-light);
            padding-bottom: 10px;
        }

        /* Card Content */
        .card-item {
            margin-bottom: 15px;
            padding: 12px;
            background: var(--bg-light);
            border-radius: 6px;
            border-left: 3px solid var(--secondary-color);
        }

        .card-label {
            font-size: 0.85em;
            font-weight: 600;
            color: var(--secondary-color);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
        }

        .card-value {
            font-size: 1.1em;
            color: var(--primary-color);
            font-weight: 500;
        }

        .card-value.highlight {
            font-size: 1.8em;
            color: var(--secondary-color);
            font-weight: bold;
        }

        /* Tabla dentro de Card */
        .card-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        .card-table tr {
            border-bottom: 1px solid var(--bg-light);
        }

        .card-table tr:last-child {
            border-bottom: none;
        }

        .card-table td {
            padding: 10px 8px;
            font-size: 0.9em;
        }

        .card-table td:first-child {
            font-weight: 600;
            color: var(--secondary-color);
            width: 45%;
        }

        .card-table td:last-child {
            color: var(--primary-color);
        }

        /* Secciones adicionales */
        .seccion {
            background: white;
            padding: 30px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: var(--card-shadow);
        }
        
        .seccion h2 {
            color: var(--secondary-color);
            border-bottom: 3px solid var(--secondary-color);
            padding-bottom: 12px;
            margin-bottom: 25px;
            font-size: 1.6em;
        }

        .seccion h3 {
            color: var(--accent-color);
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 1.2em;
        }
        
        .normativa-item {
            padding: 12px 15px;
            margin: 12px 0;
            border-left: 3px solid var(--accent-color);
            background: #fff5f5;
            border-radius: 4px;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 30px;
            color: #7f8c8d;
            font-size: 0.9em;
            margin-top: 50px;
            background: white;
            border-radius: 12px;
            box-shadow: var(--card-shadow);
        }

        .footer p {
            margin: 8px 0;
        }

        /* Navegación */
        .nav-buttons {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .nav-btn {
            padding: 12px 24px;
            background: var(--secondary-color);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-block;
        }

        .nav-btn:hover {
            background: var(--primary-color);
            transform: translateY(-2px);
            box-shadow: var(--card-shadow);
        }
        
        /* Responsivo */
        @media (max-width: 768px) {
            .sidebar {
                transform: translateX(-100%);
                transition: transform 0.3s;
            }
            
            .sidebar.active {
                transform: translateX(0);
            }
            
            .main-content {
                margin-left: 0;
                max-width: 100%;
            }
            
            .sidebar-toggle {
                display: block;
            }
            
            .cards-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }

            .bim-header {
                padding: 25px;
            }

            .bim-id {
                font-size: 2em;
            }

            .bim-header h1 {
                font-size: 1.5em;
            }

            .card {
                padding: 20px;
            }

            .card-title {
                font-size: 1.2em;
            }
        }"""


def extract_data_from_old_format(html_content):
    """Extrae los datos específicos del formato antiguo"""
    data = {}
    
    # Extraer BIM_ID
    match = re.search(r'<div class="bim-id">([^<]+)</div>', html_content)
    if match:
        data['bim_id'] = match.group(1).strip()
    
    # Extraer título
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
    if match:
        data['titulo'] = match.group(1).strip()
    
    # Extraer descripción
    match = re.search(r'<p style="opacity: 0\.9[^"]*">([^<]+)</p>', html_content)
    if match:
        data['descripcion'] = match.group(1).strip()
    else:
        data['descripcion'] = ""
    
    # Extraer nivel, sistema, categoría
    niveles = re.findall(r'<span class="bim-nivel">([^<]+)</span>', html_content)
    data['badges'] = niveles if niveles else []
    
    return data


def convert_to_card_format(filepath):
    """Convierte una ficha al formato con cards"""
    print(f"Convirtiendo: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer datos
    data = extract_data_from_old_format(content)
    
    # Reemplazar TODO el CSS (desde <style> hasta </style>)
    content = re.sub(
        r'<style>.*?</style>',
        f'<style>\n{NEW_CSS}\n    </style>',
        content,
        flags=re.DOTALL
    )
    
    # Extraer todo el contenido HTML dentro de main-content y reemplazarlo completamente
    # Buscar el bloque completo desde <div class="main-content"> hasta antes del script
    main_content_match = re.search(
        r'(<div class="main-content">.*?)(    <script>)',
        content,
        flags=re.DOTALL
    )
    
    if main_content_match:
        # Extraer datos específicos de la ficha del contenido antiguo
        old_main = main_content_match.group(1)
        
        # Extraer datos usando regex más robusto
        bim_id = re.search(r'<div class="bim-id">([^<]+)</div>', old_main)
        bim_id = bim_id.group(1).strip() if bim_id else "BIM_L0_XXX"
        
        titulo = re.search(r'<h1[^>]*>([^<]+)</h1>', old_main)
        titulo = titulo.group(1).strip() if titulo else "Título no encontrado"
        
        descripcion = re.search(r'<p style="opacity: 0\.[89][^"]*">([^<]+)</p>', old_main)
        descripcion = descripcion.group(1).strip() if descripcion else ""
        
        # Extraer badges (nivel, sistema, categoría)
        badges = re.findall(r'<span class="bim-nivel">([^<]+)</span>', old_main)
        badges_html = '\n                '.join([f'<span class="bim-nivel">{b}</span>' for b in badges])
        
        # Extraer datos de identificación
        identificacion_items = extract_section_items(old_main, "IDENTIFICACIÓN BIM")
        
        # Extraer datos presupuestales
        presupuestal_items = extract_section_items(old_main, "INFORMACIÓN PRESUPUESTAL")
        
        # Extraer tabla de especificaciones
        tabla_match = re.search(
            r'<table>.*?<tbody>(.*?)</tbody>.*?</table>',
            old_main,
            flags=re.DOTALL
        )
        tabla_rows = []
        if tabla_match:
            rows = re.findall(
                r'<tr>\s*<td>([^<]+)</td>\s*<td>([^<]+)</td>\s*<td>([^<]+)</td>\s*</tr>',
                tabla_match.group(1)
            )
            for col1, col2, col3 in rows:
                tabla_rows.append(f'''        <tr>
            <td>{col1.strip()}</td>
            <td>{col2.strip()}</td>
            <td>{col3.strip()}</td>
        </tr>''')
        
        tabla_html = '\n        \n'.join(tabla_rows) if tabla_rows else ""
        
        # Extraer sección de normatividad completa
        normatividad_match = re.search(
            r'<!-- SECCIÓN 4: NORMATIVIDAD.*?</div>\s*</div>',
            old_main,
            flags=re.DOTALL
        )
        normatividad_html = normatividad_match.group(0) if normatividad_match else ""
        
        # Construir cards de identificación
        identificacion_cards = []
        for label, value in identificacion_items:
            identificacion_cards.append(f'''                <div class="card-item">
                    <div class="card-label">{label}</div>
                    <div class="card-value">{value}</div>
                </div>''')
        
        # Construir cards presupuestales
        presupuestal_cards = []
        for label, value in presupuestal_items:
            # Detectar si es un valor monetario para usar highlight
            if '$' in value or 'COP' in value or re.search(r'\d{1,3}(?:[.,]\d{3})*', value):
                presupuestal_cards.append(f'''                <div class="card-item">
                    <div class="card-label">{label}</div>
                    <div class="card-value highlight">{value}</div>
                </div>''')
            else:
                presupuestal_cards.append(f'''                <div class="card-item">
                    <div class="card-label">{label}</div>
                    <div class="card-value">{value}</div>
                </div>''')
        
        # Construir el nuevo main-content completo
        new_main_content = f'''    <div class="main-content">
    <div class="container">

        <!-- HEADER BIM -->
        <div class="bim-header">
            <div class="bim-id">{bim_id}</div>
            <div>
                {badges_html}
            </div>
            <h1>{titulo}</h1>
            <p>{descripcion}</p>
        </div>

        <!-- CARDS GRID -->
        <div class="cards-grid">
            <!-- CARD 1: Identificación BIM -->
            <div class="card">
                <span class="card-icon">🎯</span>
                <h2 class="card-title">Identificación BIM</h2>
                
{chr(10).join(identificacion_cards)}
            </div>

            <!-- CARD 2: Información Presupuestal -->
            <div class="card">
                <span class="card-icon">💰</span>
                <h2 class="card-title">Información Presupuestal</h2>
                
{chr(10).join(presupuestal_cards)}
            </div>

            <!-- CARD 3: Especificaciones Técnicas -->
            <div class="card">
                <span class="card-icon">⚙️</span>
                <h2 class="card-title">Especificaciones Técnicas</h2>
                
                <table class="card-table">
                    <thead>
                        <tr>
                            <th>Parámetro</th>
                            <th>Valor/Característica</th>
                            <th>Norma Aplicable</th>
                        </tr>
                    </thead>
                    <tbody>
                        
{tabla_html}
        
                    </tbody>
                </table>
            </div>
        </div>

        <!-- SECCIÓN: NORMATIVIDAD Y CUMPLIMIENTO -->
        {normatividad_html}

        <!-- FOOTER -->
        <div class="footer">
            <p><strong>Sistema MUNAY/SNCALE</strong> - Metodología BIM para Proyectos Públicos</p>
            <p>Generado automáticamente | Última actualización: 2025-10-31 15:12:27</p>
            <p>Conforme a: ISO 19650 | COBie | Guía BIM Colombia | Resolución 20253040037125</p>
        </div>
    </div>
    </div>

'''
        
        # Reemplazar el contenido completo
        content = re.sub(
            r'<div class="main-content">.*?(?=    <script>)',
            new_main_content,
            content,
            flags=re.DOTALL
        )
    
    # Guardar archivo modificado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Completado: {filepath.name}")


def extract_section_items(html_content, section_name):
    """Extrae items de una sección (info-item o card-item)"""
    # Buscar la sección específica
    section_pattern = rf'<!-- SECCIÓN \d+: {section_name} -->.*?</div>\s*</div>'
    section_match = re.search(section_pattern, html_content, flags=re.DOTALL)
    
    if not section_match:
        return []
    
    section_html = section_match.group(0)
    
    # Extraer items
    items = re.findall(
        r'<div class="(?:info-label|card-label)">([^<]+)</div>\s*<div class="(?:info-value|card-value)[^"]*">([^<]+)</div>',
        section_html
    )
    
    return [(label.strip(), value.strip()) for label, value in items]


def convert_identificacion_to_card(section_html):
    """Convierte la sección de identificación al formato card"""
    # Extraer los valores de info-item
    items = re.findall(
        r'<div class="info-label">([^<]+)</div>\s*<div class="info-value">([^<]+)</div>',
        section_html
    )
    
    card_items = []
    for label, value in items:
        card_items.append(f'''                <div class="card-item">
                    <div class="card-label">{label.strip()}</div>
                    <div class="card-value">{value.strip()}</div>
                </div>''')
    
    return f'''            <div class="card">
                <span class="card-icon">🎯</span>
                <h2 class="card-title">Identificación BIM</h2>
                
{chr(10).join(card_items)}
            </div>'''


def convert_presupuestal_to_card(section_html):
    """Convierte la sección presupuestal al formato card"""
    items = re.findall(
        r'<div class="info-label">([^<]+)</div>\s*<div class="info-value">([^<]+)</div>',
        section_html
    )
    
    card_items = []
    for label, value in items:
        # Si el valor contiene $ y números grandes, usar highlight
        if '$' in value or 'COP' in value:
            card_items.append(f'''                <div class="card-item">
                    <div class="card-label">{label.strip()}</div>
                    <div class="card-value highlight">{value.strip()}</div>
                </div>''')
        else:
            card_items.append(f'''                <div class="card-item">
                    <div class="card-label">{label.strip()}</div>
                    <div class="card-value">{value.strip()}</div>
                </div>''')
    
    return f'''            <div class="card">
                <span class="card-icon">💰</span>
                <h2 class="card-title">Información Presupuestal</h2>
                
{chr(10).join(card_items)}
            </div>'''


def convert_especificaciones_to_card(section_html):
    """Convierte la sección de especificaciones técnicas al formato card con tabla"""
    # Extraer filas de la tabla
    rows = re.findall(r'<tr>\s*<td>([^<]+)</td>\s*<td>([^<]+)</td>\s*<td>([^<]+)</td>\s*</tr>', section_html)
    
    table_rows = []
    for col1, col2, col3 in rows:
        table_rows.append(f'''        <tr>
            <td>{col1.strip()}</td>
            <td>{col2.strip()}</td>
            <td>{col3.strip()}</td>
        </tr>''')
    
    return f'''            <div class="card">
                <span class="card-icon">⚙️</span>
                <h2 class="card-title">Especificaciones Técnicas</h2>
                
                <table class="card-table">
                    <thead>
                        <tr>
                            <th>Parámetro</th>
                            <th>Valor/Característica</th>
                            <th>Norma Aplicable</th>
                        </tr>
                    </thead>
                    <tbody>
                        
{chr(10).join(table_rows)}
        
                    </tbody>
                </table>
            </div>'''


def main():
    """Función principal"""
    print("=" * 60)
    print("CONVERSIÓN MASIVA DE FICHAS BIM AL FORMATO CARDS")
    print("=" * 60)
    
    # Obtener todos los archivos BIM_L0_*.html excepto el 001
    fichas = sorted([f for f in FICHAS_DIR.glob("BIM_L0_*.html") if f.name != "BIM_L0_001.html"])
    
    print(f"\nSe encontraron {len(fichas)} fichas para convertir\n")
    
    # Convertir cada ficha
    for i, ficha in enumerate(fichas, 1):
        try:
            print(f"[{i}/{len(fichas)}] ", end="")
            convert_to_card_format(ficha)
        except Exception as e:
            print(f"✗ ERROR en {ficha.name}: {str(e)}")
    
    print("\n" + "=" * 60)
    print(f"CONVERSIÓN COMPLETADA: {len(fichas)} fichas procesadas")
    print("=" * 60)


if __name__ == "__main__":
    main()
