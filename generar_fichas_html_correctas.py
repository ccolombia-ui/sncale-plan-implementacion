#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Fichas HTML BIM con RECURSIVIDAD L2→L2
====================================================

CORRECCIÓN CRÍTICA aplicada:
- Fichas L1 muestran componentes L0 (NO maniobras)
- Maniobras como sección descriptiva (NO tabla)
- Fichas L2 muestran componentes L1 + referencias L2 colapsables
- Uso de <details> para referencias recursivas

Genera:
- Fichas L1 (4 constructores + 2 referencias)
- Fichas L2 (3 configuraciones con recursividad)
- Fichas L3 (validar/actualizar referencias)
"""

import json
import os
from datetime import datetime
from funciones_recursividad_bim import (
    resolver_componentes_l2,
    expandir_para_ficha,
    validar_integridad_completa
)

def generar_ficha_l1(componente_l1, tablas_l0, output_dir='fichas_l1'):
    """Genera ficha HTML para un componente L1"""
    
    bim_id = componente_l1['bim_id']
    codigo = componente_l1['codigo']
    nombre = componente_l1['nombre']
    descripcion = componente_l1['descripcion']
    valor = componente_l1['valor_cop']
    tipo = componente_l1['tipo']
    
    # Obtener componentes L0
    if tipo == 'CONSTRUCTOR':
        codigos_l0 = componente_l1.get('componentes_l0', [])
        componentes_l0_data = []
        
        for codigo_l0 in codigos_l0:
            # Buscar en tablas_l0
            for comp in tablas_l0['componentes'].values():
                if comp['codigo_l0'] == codigo_l0:
                    componentes_l0_data.append(comp)
                    break
        
        maniobras = componente_l1.get('maniobras_soportadas', [])
    else:
        # Es una referencia
        componentes_l0_data = []
        maniobras = []
    
    # Generar HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bim_id} - {nombre}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .badge {{
            display: inline-block;
            padding: 5px 15px;
            background: rgba(255,255,255,0.2);
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 10px;
        }}
        
        .badge.constructor {{
            background: #27ae60;
        }}
        
        .badge.referencia {{
            background: #3498db;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }}
        
        .info-card .label {{
            font-weight: bold;
            color: #7f8c8d;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }}
        
        .info-card .value {{
            font-size: 1.3em;
            color: #2c3e50;
        }}
        
        .info-card.valor .value {{
            color: #27ae60;
            font-weight: bold;
            font-size: 1.5em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        thead {{
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
        }}
        
        th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tbody tr:hover {{
            background: #f8f9fa;
        }}
        
        .maniobras-list {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 20px;
            border-radius: 8px;
        }}
        
        .maniobras-list h3 {{
            color: #856404;
            margin-bottom: 15px;
        }}
        
        .maniobras-list ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .maniobras-list li {{
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
        }}
        
        .maniobras-list li:before {{
            content: "▸";
            position: absolute;
            left: 5px;
            color: #ffc107;
            font-weight: bold;
        }}
        
        .footer {{
            background: #ecf0f1;
            padding: 20px 40px;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        
        .referencia-info {{
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }}
        
        .referencia-info h3 {{
            color: #0c5460;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{bim_id}</h1>
            <p class="subtitle">{nombre}</p>
            <span class="badge {'constructor' if tipo == 'CONSTRUCTOR' else 'referencia'}">{tipo}</span>
        </div>
        
        <div class="content">
            <!-- Información General -->
            <div class="section">
                <h2>📋 Información General</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">Código BIM</div>
                        <div class="value">{codigo}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Descripción</div>
                        <div class="value">{descripcion}</div>
                    </div>
                    <div class="info-card valor">
                        <div class="label">Valor Total</div>
                        <div class="value">${valor:,}</div>
                    </div>
                </div>
            </div>
"""

    if tipo == 'CONSTRUCTOR':
        # Sección de componentes L0
        html += """
            <!-- Componentes L0 -->
            <div class="section">
                <h2>⚙️ Componentes Atómicos (L0)</h2>
                <table>
                    <thead>
                        <tr>
                            <th>BIM ID</th>
                            <th>Código</th>
                            <th>Componente</th>
                            <th>Descripción</th>
                            <th>Unidad</th>
                        </tr>
                    </thead>
                    <tbody>
"""
        
        for comp_l0 in componentes_l0_data:
            html += f"""
                        <tr>
                            <td>{comp_l0['bim_id']}</td>
                            <td><strong>{comp_l0['codigo_l0']}</strong></td>
                            <td>{comp_l0['componente']}</td>
                            <td>{comp_l0['descripcion']}</td>
                            <td>{comp_l0['unidad']}</td>
                        </tr>
"""
        
        html += """
                    </tbody>
                </table>
            </div>
"""
        
        # Sección de maniobras (solo descriptiva)
        if maniobras:
            html += """
            <!-- Maniobras Soportadas -->
            <div class="section">
                <div class="maniobras-list">
                    <h3>🛣️ Maniobras Soportadas (Especificaciones Geométricas)</h3>
                    <p style="margin-bottom: 15px; color: #856404;">
                        <em>Nota: Las maniobras NO son componentes BIM independientes. Son especificaciones 
                        geométricas embebidas en los componentes L0 (pavimentos, señalización, etc.)</em>
                    </p>
                    <ul>
"""
            for maniobra in maniobras:
                html += f"""
                        <li>{maniobra}</li>
"""
            html += """
                    </ul>
                </div>
            </div>
"""
    
    else:
        # Es una referencia
        ref_l2 = componente_l1.get('referencia_l2', '')
        resuelve_a = componente_l1.get('resuelve_a', [])
        
        html += f"""
            <!-- Información de Referencia -->
            <div class="section">
                <div class="referencia-info">
                    <h3>🔗 Componente de Referencia</h3>
                    <p>Este es un componente de <strong>REFERENCIA</strong> que apunta a una configuración L2.</p>
                    <p style="margin-top: 10px;">
                        <strong>Referencia L2:</strong> {ref_l2}<br>
                        <strong>Resuelve a:</strong> {', '.join(resuelve_a)}
                    </p>
                    <p style="margin-top: 15px; font-size: 0.9em; color: #0c5460;">
                        Para ver los componentes L0 específicos, consulte la ficha del componente L2 correspondiente.
                    </p>
                </div>
            </div>
"""
    
    # Footer
    html += f"""
        </div>
        
        <div class="footer">
            <p>Ficha generada el {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p>Sistema Nacional de Centros de Enseñanza Automovilística (SNCALE)</p>
            <p>Ministerio de Transporte - Colombia</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Guardar archivo
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{bim_id}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filepath


def generar_ficha_l2(componente_l2, tablas_l2, tablas_l1, output_dir='fichas_l2'):
    """Genera ficha HTML para un componente L2 con recursividad"""
    
    bim_id = componente_l2['bim_id']
    codigo = componente_l2['codigo']
    nombre = componente_l2['nombre']
    descripcion = componente_l2['descripcion']
    valor = componente_l2['valor_total']
    tipo = componente_l2['tipo']
    categorias = componente_l2.get('categorias_licencia', [])
    
    # Expandir componentes para la ficha
    datos_expandidos = expandir_para_ficha(bim_id, tablas_l2, tablas_l1)
    
    componentes_directos = datos_expandidos['componentes_directos']
    componentes_expandidos = datos_expandidos['componentes_expandidos']
    stats = datos_expandidos['estadisticas']
    
    # Generar HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bim_id} - {nombre}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
            padding: 40px;
        }}
        
        .header h1 {{
            font-size: 2.8em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.3em;
            opacity: 0.9;
        }}
        
        .badges {{
            margin-top: 15px;
        }}
        
        .badge {{
            display: inline-block;
            padding: 5px 12px;
            background: rgba(255,255,255,0.2);
            border-radius: 15px;
            font-size: 0.85em;
            margin-right: 8px;
            margin-top: 5px;
        }}
        
        .badge.base {{
            background: #27ae60;
        }}
        
        .badge.extendida {{
            background: #f39c12;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            border-left: 4px solid #e74c3c;
        }}
        
        .info-card .label {{
            font-weight: bold;
            color: #7f8c8d;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}
        
        .info-card .value {{
            font-size: 1.4em;
            color: #2c3e50;
        }}
        
        .info-card.valor .value {{
            color: #27ae60;
            font-weight: bold;
            font-size: 1.8em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        thead {{
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
        }}
        
        th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tbody tr:hover {{
            background: #f8f9fa;
        }}
        
        details {{
            background: #e8f4f8;
            border: 1px solid #bee5eb;
            border-radius: 8px;
            padding: 15px;
            margin-top: 10px;
        }}
        
        summary {{
            cursor: pointer;
            font-weight: bold;
            color: #0c5460;
            padding: 10px;
            background: #d1ecf1;
            border-radius: 5px;
            user-select: none;
        }}
        
        summary:hover {{
            background: #bee5eb;
        }}
        
        details table {{
            margin-top: 15px;
            font-size: 0.95em;
        }}
        
        .ref-l2 {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
        }}
        
        .comp-l1 {{
            background: #d4edda;
            border-left: 4px solid #28a745;
        }}
        
        .stats {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        
        .stats h3 {{
            color: #2c3e50;
            margin-bottom: 15px;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        
        .stat-item {{
            text-align: center;
            padding: 15px;
            background: white;
            border-radius: 8px;
            border: 2px solid #ecf0f1;
        }}
        
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #e74c3c;
        }}
        
        .stat-label {{
            font-size: 0.9em;
            color: #7f8c8d;
            margin-top: 5px;
        }}
        
        .footer {{
            background: #ecf0f1;
            padding: 20px 40px;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{bim_id}</h1>
            <p class="subtitle">{nombre}</p>
            <div class="badges">
                <span class="badge {'base' if tipo == 'CONFIGURACION_BASE' else 'extendida'}">{tipo}</span>
"""
    
    for cat in categorias:
        html += f"""
                <span class="badge">{cat}</span>
"""
    
    html += """
            </div>
        </div>
        
        <div class="content">
            <!-- Información General -->
            <div class="section">
                <h2>📋 Información General</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">Código BIM</div>
                        <div class="value">{}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Descripción</div>
                        <div class="value">{}</div>
                    </div>
                    <div class="info-card valor">
                        <div class="label">Valor Total</div>
                        <div class="value">${:,}</div>
                    </div>
                </div>
            </div>
            
            <!-- Estadísticas -->
            <div class="stats">
                <h3>📊 Estadísticas de Componentes</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-number">{}</div>
                        <div class="stat-label">Componentes L1 Totales</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">{}</div>
                        <div class="stat-label">Referencias L2</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">{}</div>
                        <div class="stat-label">L1 Directos</div>
                    </div>
                </div>
            </div>
""".format(codigo, descripcion, valor, stats['total_l1'], stats['total_l2_referenciados'], stats['total_l1_directos'])
    
    # Tabla de componentes directos
    html += """
            <!-- Componentes Directos -->
            <div class="section">
                <h2>🔧 Componentes de Nivel 1 (L1)</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Tipo</th>
                            <th>Código</th>
                            <th>Nombre</th>
                            <th>Valor</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    for comp in componentes_directos:
        if comp['tipo'] == 'L2':
            # Referencia L2 con expansión colapsable
            resuelve_a = comp.get('resuelve_a', [])
            html += f"""
                        <tr class="ref-l2">
                            <td><strong>🔗 REFERENCIA L2</strong></td>
                            <td>{comp['codigo']}</td>
                            <td>
                                <details>
                                    <summary>{comp['nombre']} (Click para expandir)</summary>
                                    <p style="margin-top: 10px; padding: 10px; background: white; border-radius: 5px;">
                                        <strong>Resuelve a:</strong><br>
"""
            for codigo_resuelto in resuelve_a:
                html += f"""
                                        • {codigo_resuelto}<br>
"""
            html += f"""
                                    </p>
                                </details>
                            </td>
                            <td><strong>${comp['valor']:,}</strong></td>
                        </tr>
"""
        else:
            # Componente L1 directo
            html += f"""
                        <tr class="comp-l1">
                            <td><strong>⚙️ COMPONENTE L1</strong></td>
                            <td>{comp['codigo']}</td>
                            <td>{comp['nombre']}</td>
                            <td><strong>${comp['valor']:,}</strong></td>
                        </tr>
"""
    
    html += """
                    </tbody>
                </table>
            </div>
"""
    
    # Tabla de componentes L1 expandidos
    html += """
            <!-- Componentes L1 Expandidos -->
            <div class="section">
                <h2>📦 Todos los Componentes L1 (Expandidos)</h2>
                <p style="margin-bottom: 20px; color: #7f8c8d;">
                    Esta tabla muestra todos los componentes L1 después de resolver las referencias L2→L2.
                </p>
                <table>
                    <thead>
                        <tr>
                            <th>BIM ID</th>
                            <th>Código</th>
                            <th>Nombre</th>
                            <th>Tipo</th>
                            <th>Valor</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    for comp_l1 in componentes_expandidos:
        tipo_comp = comp_l1.get('tipo', 'CONSTRUCTOR')
        html += f"""
                        <tr>
                            <td>{comp_l1.get('bim_id', 'N/A')}</td>
                            <td><strong>{comp_l1.get('codigo', 'N/A')}</strong></td>
                            <td>{comp_l1.get('nombre', 'N/A')}</td>
                            <td><span class="badge {'constructor' if tipo_comp == 'CONSTRUCTOR' else 'referencia'}">{tipo_comp}</span></td>
                            <td><strong>${comp_l1.get('valor_cop', 0):,}</strong></td>
                        </tr>
"""
    
    html += f"""
                    </tbody>
                </table>
            </div>
        </div>
        
        <div class="footer">
            <p>Ficha generada el {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p>Sistema Nacional de Centros de Enseñanza Automovilística (SNCALE)</p>
            <p>Ministerio de Transporte - Colombia</p>
            <p style="margin-top: 10px; font-size: 0.85em;">
                <em>Estructura con recursividad L2→L2 - Single Source of Truth</em>
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    # Guardar archivo
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{bim_id}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filepath


def main():
    print("="*80)
    print("GENERACIÓN DE FICHAS HTML BIM - ESTRUCTURA CORRECTA CON RECURSIVIDAD")
    print("="*80)
    print()
    
    # Cargar tablas
    print("📂 Cargando tablas BIM...")
    with open('TABLAS_L0_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l0 = json.load(f)
    
    with open('TABLAS_L1_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l1 = json.load(f)
    
    with open('TABLAS_L2_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l2 = json.load(f)
    
    print(f"✅ Cargados {len(tablas_l0['componentes'])} componentes L0")
    print(f"✅ Cargados {len(tablas_l1['componentes'])} componentes L1")
    print(f"✅ Cargados {len(tablas_l2['componentes'])} componentes L2")
    print()
    
    # Validar integridad antes de generar
    print("🔍 Validando integridad BIM...")
    print()
    reporte = validar_integridad_completa(tablas_l2, tablas_l1)
    print()
    
    if reporte['estado'] == 'ERRORES':
        print("❌ HAY ERRORES CRÍTICOS. Corrígelos antes de generar fichas.")
        return
    
    # Generar fichas L1
    print("="*80)
    print("GENERANDO FICHAS L1")
    print("="*80)
    print()
    
    fichas_l1_generadas = []
    for bim_id, comp in tablas_l1['componentes'].items():
        print(f"Generando {bim_id}: {comp['nombre']}...")
        filepath = generar_ficha_l1(comp, tablas_l0)
        fichas_l1_generadas.append(filepath)
        print(f"   ✅ {filepath}")
    
    print()
    print(f"✅ {len(fichas_l1_generadas)} fichas L1 generadas")
    print()
    
    # Generar fichas L2
    print("="*80)
    print("GENERANDO FICHAS L2")
    print("="*80)
    print()
    
    fichas_l2_generadas = []
    for bim_id, comp in tablas_l2['componentes'].items():
        print(f"Generando {bim_id}: {comp['nombre']}...")
        filepath = generar_ficha_l2(comp, tablas_l2, tablas_l1)
        fichas_l2_generadas.append(filepath)
        print(f"   ✅ {filepath}")
    
    print()
    print(f"✅ {len(fichas_l2_generadas)} fichas L2 generadas")
    print()
    
    # Resumen final
    print("="*80)
    print("RESUMEN FINAL")
    print("="*80)
    print()
    print(f"📄 Fichas L1 generadas: {len(fichas_l1_generadas)}")
    print(f"   - Directorio: fichas_l1/")
    print()
    print(f"📄 Fichas L2 generadas: {len(fichas_l2_generadas)}")
    print(f"   - Directorio: fichas_l2/")
    print()
    print("✅ Todas las fichas incluyen:")
    print("   - Componentes L0 en fichas L1 (NO maniobras)")
    print("   - Maniobras como sección descriptiva (NO tabla)")
    print("   - Referencias L2→L2 con <details> colapsables")
    print("   - Resolución automática de componentes L1")
    print("   - Diseño responsive y profesional")
    print()
    print("🎯 Estructura correcta implementada:")
    print("   - L1 muestra L0 + maniobras descriptivas")
    print("   - L2 muestra L1 + referencias L2 expandibles")
    print("   - Single Source of Truth garantizado")
    print()

if __name__ == '__main__':
    main()
