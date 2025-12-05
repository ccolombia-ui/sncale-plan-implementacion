#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Fichas HTML para CALE Teórico (Fase 1)
Crea fichas visuales interactivas para las 3 configuraciones de CALE Teórico

Autor: Modelo BIM 5D SNCALE
Fecha: 2025-11-03
Version: 1.0
"""

import json
import os
from datetime import datetime

def formatear_valor_cop(valor):
    """Formatea valores en pesos colombianos"""
    if valor >= 1000000000:
        return f"${valor/1000000000:.1f}B"
    elif valor >= 1000000:
        return f"${valor/1000000:.0f}M"
    else:
        return f"${valor/1000:.0f}K"

def generar_ficha_html(componente, output_dir="output/fichas_cale_teorico"):
    """Genera ficha HTML individual para un componente CALE Teórico"""
    
    bim_id = componente['bim_id']
    codigo = componente['codigo']
    nombre = componente['nombre']
    
    # Crear directorio de salida
    os.makedirs(output_dir, exist_ok=True)
    
    # Generar HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nombre} - Ficha Técnica</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px;
            position: relative;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"><path fill="rgba(255,255,255,0.1)" d="M0,0 C150,100 350,0 600,50 C850,100 1050,0 1200,50 L1200,120 L0,120 Z"/></svg>');
            background-size: cover;
            opacity: 0.3;
        }}
        
        .badge {{
            display: inline-block;
            background: #ffd700;
            color: #1e3c72;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(255,215,0,0.3);
        }}
        
        .badge.fase1 {{
            background: #ff6b6b;
            color: white;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }}
        
        .header .codigo {{
            font-size: 1.2em;
            opacity: 0.9;
            font-family: 'Courier New', monospace;
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 5px;
            display: inline-block;
            margin-top: 10px;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }}
        
        .section h2 {{
            color: #1e3c72;
            margin-bottom: 20px;
            font-size: 1.8em;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .icon {{
            font-size: 1.2em;
        }}
        
        .capacidad-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .capacidad-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        
        .capacidad-card:hover {{
            transform: translateY(-5px);
        }}
        
        .capacidad-card .numero {{
            font-size: 2.5em;
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}
        
        .capacidad-card .label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        
        .componentes-list {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .componente-item {{
            background: white;
            margin: 10px 0;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }}
        
        .componente-item:hover {{
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transform: translateX(5px);
        }}
        
        .componente-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        
        .componente-nombre {{
            font-weight: bold;
            color: #1e3c72;
            font-size: 1.1em;
        }}
        
        .componente-valor {{
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
        }}
        
        .componente-descripcion {{
            color: #666;
            font-size: 0.95em;
            margin-top: 5px;
        }}
        
        .componente-detalle {{
            display: flex;
            gap: 15px;
            margin-top: 10px;
            font-size: 0.9em;
            color: #888;
        }}
        
        .detalle-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        .financiero-summary {{
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
        }}
        
        .financiero-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .financiero-item {{
            text-align: center;
            background: rgba(255,255,255,0.2);
            padding: 15px;
            border-radius: 10px;
        }}
        
        .financiero-item .valor {{
            font-size: 1.8em;
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}
        
        .financiero-item .label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        
        .upgrade-path {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .upgrade-path h3 {{
            color: #856404;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .upgrade-option {{
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            border-left: 4px solid #ffc107;
        }}
        
        .upgrade-option strong {{
            color: #856404;
            display: block;
            margin-bottom: 5px;
        }}
        
        .actores-section {{
            background: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        
        .actor-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        
        .actor-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #2196f3;
        }}
        
        .actor-card .cargo {{
            font-weight: bold;
            color: #1565c0;
            margin-bottom: 5px;
        }}
        
        .actor-card .costo {{
            color: #4caf50;
            font-weight: bold;
        }}
        
        .caracteristicas-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin: 20px 0;
        }}
        
        .caracteristica {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 8px;
        }}
        
        .caracteristica.yes {{
            border-left: 4px solid #4caf50;
        }}
        
        .caracteristica.no {{
            border-left: 4px solid #f44336;
        }}
        
        .check {{
            color: #4caf50;
            font-weight: bold;
            font-size: 1.2em;
        }}
        
        .cross {{
            color: #f44336;
            font-weight: bold;
            font-size: 1.2em;
        }}
        
        .timing-bar {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        
        .timeline {{
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 40px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 1.2em;
            margin-top: 10px;
        }}
        
        .footer {{
            background: #1e3c72;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .footer p {{
            margin: 5px 0;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .capacidad-grid,
            .financiero-grid,
            .caracteristicas-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <span class="badge fase1">🚀 FASE 1 - Solo Evaluación Teórica</span>
            <h1>{nombre}</h1>
            <div class="codigo">{codigo} | {bim_id}</div>
        </div>
        
        <!-- CONTENT -->
        <div class="content">
            
            <!-- DESCRIPCIÓN -->
            <div class="section">
                <h2><span class="icon">📋</span> Descripción</h2>
                <p style="font-size: 1.1em; color: #555; line-height: 1.8;">
                    {componente['descripcion']}
                </p>
            </div>
            
            <!-- CAPACIDAD -->
            <div class="section">
                <h2><span class="icon">📊</span> Capacidad Operativa</h2>
                <div class="capacidad-grid">
                    <div class="capacidad-card">
                        <span class="numero">{componente['capacidad']['cubiculos_evaluacion']}</span>
                        <span class="label">Cubículos Evaluación</span>
                    </div>
                    <div class="capacidad-card">
                        <span class="numero">{componente['capacidad']['evaluaciones_teoricas_mes']}</span>
                        <span class="label">Evaluaciones/Mes</span>
                    </div>
                    <div class="capacidad-card">
                        <span class="numero">{componente['capacidad']['sala_formacion_pax']}</span>
                        <span class="label">Capacidad Formación</span>
                    </div>
                    <div class="capacidad-card">
                        <span class="numero">{componente['caracteristicas']['personal_total']}</span>
                        <span class="label">Personal Requerido</span>
                    </div>
                </div>
            </div>
            
            <!-- RESUMEN FINANCIERO -->
            <div class="section">
                <h2><span class="icon">💰</span> Resumen Financiero</h2>
                <div class="financiero-summary">
                    <div class="financiero-grid">
                        <div class="financiero-item">
                            <span class="valor">{formatear_valor_cop(componente['resumen_financiero']['capex_inicial'])}</span>
                            <span class="label">CAPEX Inicial</span>
                        </div>
                        <div class="financiero-item">
                            <span class="valor">{formatear_valor_cop(componente['resumen_financiero']['opex_anual_total'])}</span>
                            <span class="label">OPEX Anual</span>
                        </div>
                        <div class="financiero-item">
                            <span class="valor">{componente['resumen_financiero']['ratio_opex_capex']}</span>
                            <span class="label">Ratio OPEX/CAPEX</span>
                        </div>
                        <div class="financiero-item">
                            <span class="valor">{formatear_valor_cop(componente['resumen_financiero']['costo_total_primer_ano'])}</span>
                            <span class="label">Total Primer Año</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- COMPONENTES L2 -->
            <div class="section">
                <h2><span class="icon">🏗️</span> Componentes L2 Incluidos</h2>
                <div class="componentes-list">
"""
    
    # Agregar componentes L2
    for comp_l2 in componente['componentes_l2']:
        html += f"""
                    <div class="componente-item">
                        <div class="componente-header">
                            <div class="componente-nombre">{comp_l2['nombre']}</div>
                            <div class="componente-valor">{formatear_valor_cop(comp_l2['valor_total'])}</div>
                        </div>
                        <div class="componente-descripcion">{comp_l2['descripcion']}</div>
                        <div class="componente-detalle">
                            <div class="detalle-item">
                                <span>📦</span> {comp_l2['codigo']}
                            </div>
                            <div class="detalle-item">
                                <span>📐</span> {comp_l2.get('metros_cuadrados', 'N/A')} m²
                            </div>
                            <div class="detalle-item">
                                <span>🏷️</span> {comp_l2['categoria']}
                            </div>
                        </div>
                    </div>
"""
    
    html += """
                </div>
            </div>
            
            <!-- ACTORES ESPACIALES -->
            <div class="section">
                <h2><span class="icon">👥</span> Actores Espaciales (OPEX)</h2>
                
                <div class="actores-section">
                    <h3 style="color: #1565c0; margin-bottom: 15px;">💻 Software y Sistemas</h3>
                    <div class="actor-grid">
"""
    
    # Agregar actores software
    for actor in componente['actores_espaciales']['software']:
        html += f"""
                        <div class="actor-card">
                            <div class="cargo">{actor['codigo']}</div>
                            <div style="color: #666; font-size: 0.9em; margin: 5px 0;">{actor['funcionalidad']}</div>
                            <div class="costo">{formatear_valor_cop(actor['costo_anual'])}/año</div>
                        </div>
"""
    
    html += """
                    </div>
                </div>
                
                <div class="actores-section" style="background: #f3e5f5; margin-top: 20px;">
                    <h3 style="color: #6a1b9a; margin-bottom: 15px;">👔 Talento Humano</h3>
                    <div class="actor-grid">
"""
    
    # Agregar actores RRHH
    for actor in componente['actores_espaciales']['rrhh']:
        html += f"""
                        <div class="actor-card" style="border-left-color: #9c27b0;">
                            <div class="cargo">{actor['cargo']}</div>
                            <div style="color: #666; font-size: 0.9em; margin: 5px 0;">Cantidad: {actor['cantidad']}</div>
                            <div class="costo">{formatear_valor_cop(actor['costo_anual'])}/año</div>
                        </div>
"""
    
    html += """
                    </div>
                </div>
            </div>
            
            <!-- CARACTERÍSTICAS -->
            <div class="section">
                <h2><span class="icon">✨</span> Características</h2>
                <div class="caracteristicas-grid">
"""
    
    # Características
    caracteristicas = [
        ("✅ Evaluación Teórica", "yes" if componente['caracteristicas']['evaluacion_teorica'] else "no"),
        ("❌ Evaluación Práctica", "no" if not componente['caracteristicas']['evaluacion_practica'] else "yes"),
        ("✅ Todas las Categorías (Teórico)", "yes" if componente['caracteristicas']['categorias_todas_teorico'] else "no"),
        ("❌ Requiere Pistas", "no" if not componente['caracteristicas']['requiere_pistas'] else "yes"),
        (f"📐 Área: {componente['caracteristicas']['area_construida_total_m2']} m²", "yes"),
        (f"👥 Personal: {componente['caracteristicas']['personal_total']} personas", "yes"),
    ]
    
    for caracteristica, clase in caracteristicas:
        simbolo = "✅" if clase == "yes" else "❌"
        html += f"""
                    <div class="caracteristica {clase}">
                        <span class="{'check' if clase == 'yes' else 'cross'}">{simbolo}</span>
                        <span>{caracteristica}</span>
                    </div>
"""
    
    html += """
                </div>
            </div>
            
            <!-- UPGRADE PATH -->
"""
    
    if 'upgrade_path' in componente and componente['upgrade_path']:
        html += """
            <div class="section">
                <h2><span class="icon">⬆️</span> Rutas de Actualización</h2>
                <div class="upgrade-path">
                    <h3>🎯 Opciones para Habilitar Evaluación Práctica</h3>
"""
        
        for key, upgrade in componente['upgrade_path'].items():
            html += f"""
                    <div class="upgrade-option">
                        <strong>→ {upgrade['descripcion']}</strong>
                        <div style="margin-top: 8px; color: #666;">
                            <div>📦 Componente: {upgrade.get('componente_adicional', upgrade.get('bim_resultante', 'N/A'))}</div>
                            <div>💰 Incremento CAPEX: {formatear_valor_cop(upgrade.get('incremento_capex', 0))}</div>
                            {f"<div>💸 Incremento OPEX: {formatear_valor_cop(upgrade.get('incremento_opex_anual', 0))}/año</div>" if 'incremento_opex_anual' in upgrade else ""}
                            {f"<div>🎓 Nuevas Categorías: {', '.join(upgrade.get('nuevas_categorias_practicas', []))}</div>" if 'nuevas_categorias_practicas' in upgrade else ""}
                        </div>
                    </div>
"""
        
        html += """
                </div>
            </div>
"""
    
    # TIMING
    timing_dias = componente.get('timing', {}).get('total_dias', 0)
    timing_meses = componente.get('timing', {}).get('total_meses', 0)
    
    html += f"""
            <!-- TIMING -->
            <div class="section">
                <h2><span class="icon">⏱️</span> Tiempo de Implementación</h2>
                <div class="timing-bar">
                    <p style="color: #666; margin-bottom: 10px;">Tiempo total desde inicio hasta operación completa:</p>
                    <div class="timeline">
                        📅 {timing_dias} días ({timing_meses} meses)
                    </div>
                </div>
            </div>
            
            <!-- NODOS APLICABLES -->
            <div class="section">
                <h2><span class="icon">🗺️</span> Nodos Aplicables</h2>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px;">
                    <p style="color: #555; margin-bottom: 10px;"><strong>Tipo de nodos:</strong> {', '.join(componente['nodos_aplicables']['tipo_nodos'])}</p>
                    <p style="color: #555;"><strong>Cantidad estimada en red nacional:</strong> {componente['nodos_aplicables']['cantidad_estimada']} nodos</p>
                    <p style="color: #888; font-size: 0.9em; margin-top: 10px;">
                        <em>Capacidad total estimada: {componente['nodos_aplicables']['cantidad_estimada'] * componente['capacidad']['evaluaciones_teoricas_mes']:,} evaluaciones teóricas/mes</em>
                    </p>
                </div>
            </div>
            
        </div>
        
        <!-- FOOTER -->
        <div class="footer">
            <p><strong>Modelo BIM 5D SNCALE v2.0</strong></p>
            <p>Ficha generada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Fuente de valores: {componente['validaciones']['fuente_valores']}</p>
            <p>Estado validación: <strong>{componente['validaciones']['estado']}</strong></p>
        </div>
    </div>
</body>
</html>
"""
    
    # Guardar archivo
    filename = f"{bim_id}_{codigo.replace('.', '_')}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filepath

def main():
    """Función principal"""
    print("=" * 80)
    print("GENERADOR DE FICHAS HTML - CALE TEÓRICO (FASE 1)")
    print("=" * 80)
    print()
    
    # Cargar datos
    json_file = "TABLAS_L3_CALE_TEORICO.json"
    
    if not os.path.exists(json_file):
        print(f"❌ ERROR: No se encuentra el archivo {json_file}")
        return
    
    print(f"📖 Cargando datos desde {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    componentes = data['componentes']
    total = len(componentes)
    
    print(f"✅ {total} configuraciones encontradas")
    print()
    
    # Generar fichas
    fichas_generadas = []
    
    for i, (bim_id, componente) in enumerate(componentes.items(), 1):
        print(f"[{i}/{total}] Generando ficha para {componente['nombre']}...")
        filepath = generar_ficha_html(componente)
        fichas_generadas.append(filepath)
        print(f"    ✅ {filepath}")
    
    print()
    print("=" * 80)
    print("✅ PROCESO COMPLETADO")
    print("=" * 80)
    print()
    print(f"📁 {len(fichas_generadas)} fichas HTML generadas en: output/fichas_cale_teorico/")
    print()
    print("Archivos generados:")
    for ficha in fichas_generadas:
        print(f"  - {os.path.basename(ficha)}")
    print()
    print("💡 Abre las fichas en tu navegador para visualizarlas")
    print()

if __name__ == "__main__":
    main()
