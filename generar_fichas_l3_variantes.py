#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERADOR DE FICHAS TÉCNICAS HTML - CAMBIO 1
===========================================
Genera 4 fichas técnicas HTML para configuraciones L3 con recursividad:
- BIM_L3_001_BASE (CALE.n_1.base)
- BIM_L3_001_PLUS (CALE.n_1.plus)
- BIM_L3_002_BASE (CALE.n_2.base)
- BIM_L3_002_STAR (CALE.n_2.star)

Incluye visualización de herencia L3→L3 y comparación BASE vs VARIANTE.
"""

import json
from pathlib import Path
from funciones_recursividad_l3 import (
    resolver_l3_recursivo, 
    calcular_totales_agregados,
    validar_herencia_l3
)

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

RUTA_JSON = Path(__file__).parent / "TABLAS_L3_VARIANTES_RECURSIVAS.json"
RUTA_OUTPUT = Path(__file__).parent / "output"

# ============================================================================
# PLANTILLA HTML
# ============================================================================

def generar_html_ficha(bim_id, config, tablas_l3):
    """
    Genera HTML para una configuración L3.
    
    Args:
        bim_id: Identificador BIM (ej: "BIM_L3_001_BASE")
        config: Configuración completa
        tablas_l3: Todas las configuraciones (para resolver referencias)
    
    Returns:
        str: HTML completo
    """
    
    # Resolver componentes (con recursividad si aplica)
    componentes = resolver_l3_recursivo(bim_id, tablas_l3)
    totales = calcular_totales_agregados(bim_id, tablas_l3)
    
    # Determinar si es extendida
    es_extendida = config.get('tipo') == 'CONFIGURACION_EXTENDIDA'
    base_id = None
    config_base = None
    componentes_heredados = []
    componentes_adicionales = []
    
    if es_extendida:
        base_id = config['recursividad_l3']['referencia_base']
        config_base = tablas_l3[base_id]
        componentes_heredados = resolver_l3_recursivo(base_id, tablas_l3)
        componentes_adicionales = config['recursividad_l3']['componentes_adicionales']
    
    # Generar HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ficha Técnica - {config['nombre']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        
        .header .codigo {{
            font-size: 1.2rem;
            opacity: 0.9;
            font-family: 'Courier New', monospace;
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
            margin-top: 1rem;
        }}
        
        .badge.base {{
            background: #10b981;
            color: white;
        }}
        
        .badge.extendida {{
            background: #f59e0b;
            color: white;
        }}
        
        .content {{
            padding: 2rem;
        }}
        
        .section {{
            margin-bottom: 2rem;
        }}
        
        .section h2 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        
        .info-card {{
            background: #f3f4f6;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .info-card h3 {{
            color: #667eea;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }}
        
        .info-card .value {{
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
        }}
        
        .info-card .unit {{
            font-size: 0.9rem;
            color: #666;
        }}
        
        .herencia-section {{
            background: #fef3c7;
            padding: 1.5rem;
            border-radius: 8px;
            border: 2px solid #f59e0b;
            margin-bottom: 2rem;
        }}
        
        .herencia-section h3 {{
            color: #d97706;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .herencia-arrow {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 1rem 0;
        }}
        
        .herencia-box {{
            flex: 1;
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border: 2px solid #d97706;
        }}
        
        .herencia-box strong {{
            color: #d97706;
            display: block;
            margin-bottom: 0.5rem;
        }}
        
        .arrow {{
            font-size: 2rem;
            color: #d97706;
            font-weight: bold;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }}
        
        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #e5e7eb;
        }}
        
        th {{
            background: #f3f4f6;
            color: #667eea;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
        }}
        
        tr:hover {{
            background: #f9fafb;
        }}
        
        .component-type {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: bold;
        }}
        
        .component-type.heredado {{
            background: #dbeafe;
            color: #1e40af;
        }}
        
        .component-type.adicional {{
            background: #fef3c7;
            color: #d97706;
        }}
        
        .money {{
            color: #059669;
            font-weight: bold;
        }}
        
        .footer {{
            background: #f3f4f6;
            padding: 1.5rem;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }}
        
        .comparacion {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-top: 1rem;
        }}
        
        .comparacion-card {{
            background: #f3f4f6;
            padding: 1.5rem;
            border-radius: 8px;
        }}
        
        .comparacion-card h4 {{
            color: #667eea;
            margin-bottom: 1rem;
        }}
        
        .delta {{
            color: #059669;
            font-weight: bold;
        }}
        
        .delta.negative {{
            color: #dc2626;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{config['nombre']}</h1>
            <div class="codigo">{config['codigo']}</div>
            <div class="badge {'extendida' if es_extendida else 'base'}">
                {config['tipo'].replace('_', ' ')}
            </div>
        </div>
        
        <div class="content">
            <!-- RESUMEN EJECUTIVO -->
            <div class="section">
                <h2>📊 Resumen Ejecutivo</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <h3>BIM ID</h3>
                        <div class="value">{config['bim_id']}</div>
                    </div>
                    <div class="info-card">
                        <h3>Nodos Aplicables</h3>
                        <div class="value">{config['nodos_aplicables']}</div>
                        <div class="unit">nodos en red</div>
                    </div>
                    <div class="info-card">
                        <h3>CAPEX Total</h3>
                        <div class="value money">${totales['capex_total']:,.0f}</div>
                        <div class="unit">COP</div>
                    </div>
                    <div class="info-card">
                        <h3>Capacidad Mensual</h3>
                        <div class="value">{totales['capacidad_mes']:,}</div>
                        <div class="unit">evaluaciones/mes</div>
                    </div>
                    <div class="info-card">
                        <h3>Personal Requerido</h3>
                        <div class="value">{totales['personal_total']}</div>
                        <div class="unit">personas/nodo</div>
                    </div>
                    <div class="info-card">
                        <h3>Componentes L2</h3>
                        <div class="value">{len(componentes)}</div>
                        <div class="unit">componentes</div>
                    </div>
                </div>
            </div>
"""
    
    # Si es extendida, mostrar herencia
    if es_extendida:
        assert base_id is not None, "base_id debe existir para configuraciones extendidas"
        assert config_base is not None, "config_base debe existir para configuraciones extendidas"
        totales_base = calcular_totales_agregados(base_id, tablas_l3)
        delta_capex = totales['capex_total'] - totales_base['capex_total']
        delta_capacidad = totales['capacidad_mes'] - totales_base['capacidad_mes']
        delta_pct_capex = (delta_capex / totales_base['capex_total']) * 100
        delta_pct_capacidad = (delta_capacidad / totales_base['capacidad_mes']) * 100 if totales_base['capacidad_mes'] > 0 else 0
        
        html += f"""
            <!-- HERENCIA L3→L3 -->
            <div class="section">
                <h2>🔗 Recursividad L3→L3</h2>
                <div class="herencia-section">
                    <h3>
                        ⚡ Herencia de Configuración
                    </h3>
                    <p>Esta configuración <strong>hereda todos los componentes</strong> de la configuración base y agrega componentes adicionales.</p>
                    
                    <div class="herencia-arrow">
                        <div class="herencia-box">
                            <strong>BASE:</strong>
                            {config_base['codigo']}<br>
                            <small>{config_base['nombre']}</small><br>
                            <div class="money" style="margin-top: 0.5rem;">${totales_base['capex_total']:,.0f}</div>
                        </div>
                        <div class="arrow">→</div>
                        <div class="herencia-box">
                            <strong>EXTENDIDA:</strong>
                            {config['codigo']}<br>
                            <small>{config['nombre']}</small><br>
                            <div class="money" style="margin-top: 0.5rem;">${totales['capex_total']:,.0f}</div>
                        </div>
                    </div>
                    
                    <div class="comparacion">
                        <div class="comparacion-card">
                            <h4>💰 Incremento CAPEX</h4>
                            <div class="value delta" style="font-size: 1.5rem;">
                                +${delta_capex:,.0f}
                            </div>
                            <div class="unit">+{delta_pct_capex:.1f}% sobre base</div>
                        </div>
                        <div class="comparacion-card">
                            <h4>📈 Incremento Capacidad</h4>
                            <div class="value delta" style="font-size: 1.5rem;">
                                +{delta_capacidad:,} eval/mes
                            </div>
                            <div class="unit">+{delta_pct_capacidad:.1f}% sobre base</div>
                        </div>
                    </div>
                </div>
            </div>
"""
    
    # Tabla de componentes
    html += f"""
            <!-- COMPONENTES L2 -->
            <div class="section">
                <h2>🧩 Componentes L2</h2>
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Código L2</th>
                            <th>Descripción</th>
                            <th>Valor Unitario (COP)</th>
"""
    
    if es_extendida:
        html += """
                            <th>Tipo</th>
"""
    
    html += """
                        </tr>
                    </thead>
                    <tbody>
"""
    
    # Listar componentes
    for idx, comp in enumerate(componentes, 1):
        tipo_comp = ""
        if es_extendida:
            es_heredado = comp in componentes_heredados
            tipo_comp = f'<td><span class="component-type {"heredado" if es_heredado else "adicional"}">{"HEREDADO" if es_heredado else "ADICIONAL"}</span></td>'
        
        html += f"""
                        <tr>
                            <td>{idx}</td>
                            <td><code>{comp['codigo']}</code></td>
                            <td>{comp['nombre']}</td>
                            <td class="money">${comp['valor_unitario']:,.0f}</td>
                            {tipo_comp}
                        </tr>
"""
    
    html += """
                    </tbody>
                </table>
            </div>
"""
    
    # Características espaciales (si están disponibles)
    if 'recursos' in config and 'area_total_m2' in config['recursos']:
        html += f"""
            <!-- CARACTERÍSTICAS ESPACIALES -->
            <div class="section">
                <h2>📐 Características Espaciales</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <h3>Área Total</h3>
                        <div class="value">{config['recursos']['area_total_m2']:,.0f}</div>
                        <div class="unit">m²</div>
                    </div>
                    <div class="info-card">
                        <h3>Área Teórica</h3>
                        <div class="value">{config['recursos'].get('area_teorica_m2', 0):,.0f}</div>
                        <div class="unit">m²</div>
                    </div>
                    <div class="info-card">
                        <h3>Área Pistas</h3>
                        <div class="value">{config['recursos'].get('area_pistas_m2', 0):,.0f}</div>
                        <div class="unit">m²</div>
                    </div>
                    <div class="info-card">
                        <h3>Área Parqueadero</h3>
                        <div class="value">{config['recursos'].get('area_parqueadero_m2', 0):,.0f}</div>
                        <div class="unit">m²</div>
                    </div>
                </div>
            </div>
"""
    
    html += """
            <!-- METADATOS -->
            <div class="section">
                <h2>ℹ️ Metadatos</h2>
                <table>
                    <tr>
                        <th>Versión</th>
                        <td>{config['metadata']['version']}</td>
                    </tr>
                    <tr>
                        <th>Fecha Creación</th>
                        <td>{config['metadata']['fecha_creacion']}</td>
                    </tr>
                    <tr>
                        <th>Autor</th>
                        <td>{config['metadata']['autor']}</td>
                    </tr>
                    <tr>
                        <th>Patrón</th>
                        <td><code>{config['metadata']['patron']}</code></td>
                    </tr>
                </table>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>CAMBIO 1 - Recursividad L3→L3 para Variantes CALE</strong></p>
            <p>Generado automáticamente por generar_fichas_l3_variantes.py</p>
            <p>BIM 5D Munay - Sistema Nacional CALE</p>
        </div>
    </div>
</body>
</html>
"""
    
    return html


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Genera las 4 fichas técnicas HTML."""
    
    print("=" * 80)
    print("GENERADOR DE FICHAS TÉCNICAS HTML - CAMBIO 1")
    print("=" * 80)
    print()
    
    # Cargar JSON
    print(f"📖 Cargando {RUTA_JSON.name}...")
    with open(RUTA_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tablas_l3 = {k: v for k, v in data.items() if k != 'metadata'}
    print(f"✅ {len(tablas_l3)} configuraciones cargadas\n")
    
    # Crear carpeta output
    RUTA_OUTPUT.mkdir(exist_ok=True)
    
    # Generar fichas
    fichas_generadas = []
    
    for bim_id, config in tablas_l3.items():
        print(f"🔧 Generando ficha para {config['codigo']}...")
        
        html = generar_html_ficha(bim_id, config, tablas_l3)
        
        # Nombre de archivo
        codigo_limpio = config['codigo'].replace('.', '_')
        nombre_archivo = f"{bim_id}_{codigo_limpio}.html"
        ruta_salida = RUTA_OUTPUT / nombre_archivo
        
        # Guardar
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            f.write(html)
        
        fichas_generadas.append({
            'bim_id': bim_id,
            'codigo': config['codigo'],
            'archivo': nombre_archivo,
            'ruta': str(ruta_salida)
        })
        
        print(f"   ✅ Guardada en: {ruta_salida}\n")
    
    # Resumen
    print("=" * 80)
    print("✅ GENERACIÓN COMPLETADA")
    print("=" * 80)
    print(f"\n📁 Total fichas generadas: {len(fichas_generadas)}\n")
    
    for ficha in fichas_generadas:
        tipo = "🟢 BASE" if "BASE" in ficha['bim_id'] else "🟡 EXTENDIDA"
        print(f"{tipo} {ficha['codigo']}")
        print(f"    → {ficha['archivo']}")
        print()
    
    print(f"📂 Ubicación: {RUTA_OUTPUT.absolute()}\n")


if __name__ == "__main__":
    main()
