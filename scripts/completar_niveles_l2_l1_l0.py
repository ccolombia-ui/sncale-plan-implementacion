#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script maestro para completar niveles L2, L1 y L0
Genera fichas HTML completas con normatividad
"""

import json
import os
from datetime import datetime

# ========================= CONSTANTES =========================

NORMATIVIDAD_L2 = """
        <div class="section">
            <h2>📋 Marco Normativo</h2>
            
            <div class="normatividad-box">
                <h3>⚖️ Resolución 20253040037125 de 2025</h3>
                <p><strong>Emisor:</strong> Ministerio de Transporte</p>
                <p><strong>Aplicación:</strong> Pistas de evaluación práctica</p>
                
                <div class="norma-requisito">
                    <strong>Art. 3.7.1.1 - Dimensiones y Especificaciones:</strong>
                    <ul>
                        <li>Área mínima según clase: I (3,500 m²), II (5,200 m²), III (8,500 m²)</li>
                        <li>Superficie en asfalto o concreto con rugosidad controlada</li>
                        <li>Pendientes máximas: longitudinal 12%, transversal 2%</li>
                        <li>Radio mínimo de giro según categoría vehículo</li>
                        <li>Zonas de seguridad perimetrales ≥2.0 m</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Art. 3.7.1.2 - Señalización y Demarcación:</strong>
                    <ul>
                        <li>Señalización horizontal con pintura termoplástica reflectiva</li>
                        <li>Señales verticales según Manual de Señalización Vial (Res 1885/2015)</li>
                        <li>Demarcación circuitos según NT TS 004:2021</li>
                        <li>Conos, balizas y elementos móviles certificados</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Art. 3.7.1.3 - Seguridad y Protección:</strong>
                    <ul>
                        <li>Barreras de contención en zonas de riesgo</li>
                        <li>Zonas de escape en curvas y pendientes</li>
                        <li>Sistema de drenaje certificado ISO 14001</li>
                        <li>Seguro RC con cobertura ≥500 SMLMV</li>
                    </ul>
                </div>
            </div>
            
            <div class="normatividad-box">
                <h3>🌍 ISO 39001:2012 - Sistemas de Gestión de Seguridad Vial</h3>
                <p><strong>Aplicación:</strong> Diseño y operación de infraestructura vial de evaluación</p>
                
                <div class="norma-requisito">
                    <strong>Cláusula 4.3.1 - Identificación de Peligros:</strong>
                    <ul>
                        <li>Análisis de riesgos en cada maniobra de evaluación</li>
                        <li>Matriz de peligros actualizada semestralmente</li>
                        <li>Protocolos de emergencia para cada circuito</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Cláusula 5.2 - Infraestructura Segura:</strong>
                    <ul>
                        <li>Diseño "auto-explicativo" de circuitos</li>
                        <li>Visibilidad mínima 100 m en rectas</li>
                        <li>Iluminación ≥150 lux en zonas de maniobras</li>
                        <li>Superficies antideslizantes (coef. fricción ≥0.45)</li>
                    </ul>
                </div>
            </div>
            
            <div class="normatividad-box">
                <h3>🛣️ Resolución 160 de 2018 - INVIAS</h3>
                <p><strong>Aplicación:</strong> Especificaciones técnicas de construcción</p>
                
                <div class="norma-requisito">
                    <strong>Artículo 450 - Pavimentos Asfálticos:</strong>
                    <ul>
                        <li>MDC-3 (Mezcla Densa en Caliente tipo III) espesor ≥75mm</li>
                        <li>Base granular estabilizada CBR ≥80%</li>
                        <li>Subbase granular compactada 95% Proctor</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Artículo 500 - Concreto Hidráulico:</strong>
                    <ul>
                        <li>Resistencia f'c ≥280 kg/cm² (opcional en zonas específicas)</li>
                        <li>Juntas de dilatación cada 4.5 m</li>
                        <li>Acabado superficial con textura estriada</li>
                    </ul>
                </div>
            </div>
        </div>
"""

NORMATIVIDAD_L1 = """
        <div class="section">
            <h2>📋 Marco Normativo</h2>
            
            <div class="normatividad-box">
                <h3>⚖️ Resolución 20253040037125 de 2025</h3>
                <p><strong>Emisor:</strong> Ministerio de Transporte</p>
                <p><strong>Aplicación:</strong> Componentes de infraestructura de evaluación</p>
                
                <div class="norma-requisito">
                    <strong>Art. 3.7.1.4 - Componentes Obligatorios:</strong>
                    <ul>
                        <li>Circuitos de maniobras certificados (14 básicas + 3 avanzadas)</li>
                        <li>Sistemas de iluminación artificial (emergencias nocturnas)</li>
                        <li>Drenaje pluvial dimensionado para Tr=10 años</li>
                        <li>Señalización vertical y horizontal durable (≥5 años)</li>
                        <li>Vehículos de evaluación con mantenimiento certificado</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Art. 3.7.1.5 - Mantenimiento:</strong>
                    <ul>
                        <li>Inspección mensual de pavimentos (IRI, baches, fisuras)</li>
                        <li>Repintado señalización cada 6 meses o antes si retro-reflectividad <50 mcd/lx/m²</li>
                        <li>Limpieza drenajes trimestralmente</li>
                        <li>Certificación anual de iluminación (lux metros)</li>
                    </ul>
                </div>
            </div>
            
            <div class="normatividad-box">
                <h3>🔧 NTC-ISO 9001:2015 - Gestión de Calidad</h3>
                <p><strong>Aplicación:</strong> Procesos de mantenimiento y control</p>
                
                <div class="norma-requisito">
                    <strong>Cláusula 7.1.3 - Infraestructura:</strong>
                    <ul>
                        <li>Documentación técnica de cada componente (fichas, planos, manuales)</li>
                        <li>Plan de mantenimiento preventivo basado en fabricante</li>
                        <li>Registros de intervenciones y reparaciones</li>
                        <li>Proveedores calificados con certificación ISO 9001</li>
                    </ul>
                </div>
                
                <div class="norma-requisito">
                    <strong>Cláusula 8.5.1 - Control de Producción:</strong>
                    <ul>
                        <li>Inspecciones pre-operacionales diarias</li>
                        <li>Verificación calibración sensores ALEYA (semanal)</li>
                        <li>Control dimensional señalización (mensual)</li>
                    </ul>
                </div>
            </div>
        </div>
"""

NORMATIVIDAD_L0 = """
        <div class="section">
            <h2>📋 Marco Normativo</h2>
            
            <div class="normatividad-box">
                <h3>⚖️ Resolución 20253040037125 de 2025</h3>
                <p><strong>Artículo 3.7.1.6 - Elementos Atómicos:</strong>
                <ul>
                    <li>Especificaciones técnicas según fabricante certificado</li>
                    <li>Trazabilidad de suministro (proveedor, lote, fecha)</li>
                    <li>Certificados de calidad y conformidad</li>
                    <li>Vida útil mínima garantizada</li>
                </ul>
            </div>
            
            <div class="normatividad-box">
                <h3>🛠️ NTC 4595 - Señalización Vial</h3>
                <p><strong>Especificaciones:</strong></p>
                <ul>
                    <li>Señales verticales: lámina reflectiva Tipo IV (alta intensidad)</li>
                    <li>Postes soporte: acero galvanizado o aluminio anodizado</li>
                    <li>Resistencia viento: 120 km/h (zona urbana), 150 km/h (rural)</li>
                </ul>
            </div>
            
            <div class="normatividad-box">
                <h3>⚡ RETIE - Reglamento Técnico de Instalaciones Eléctricas</h3>
                <p><strong>Sistemas de iluminación:</strong></p>
                <ul>
                    <li>Luminarias LED certificadas para tránsito vehicular</li>
                    <li>IP65 mínimo (protección polvo y agua)</li>
                    <li>IK08 mínimo (resistencia impactos)</li>
                    <li>Sistema puesta a tierra <25 Ω</li>
                </ul>
            </div>
        </div>
"""

# ========================= PLANTILLAS HTML =========================

def generar_html_l2(datos_l2):
    """Genera HTML completo para ficha L2"""
    
    componentes_html = ""
    for comp in datos_l2.get('componentes', []):
        if comp['tipo'] == 'L2':
            comp_id = comp.get('referencia', comp.get('bim_id', 'N/A'))
            componentes_html += f"""
                <tr>
                    <td><span class="badge-l2">{comp_id}</span></td>
                    <td><strong>{comp['nombre']}</strong></td>
                    <td><span class="badge tipo-ref">REFERENCIA L2</span></td>
                    <td class="text-right">${comp['valor']:,}</td>
                </tr>
            """
        else:  # L1
            comp_id = comp.get('bim_id', 'N/A')
            componentes_html += f"""
                <tr>
                    <td><span class="badge-l1">{comp_id}</span></td>
                    <td>{comp['nombre']}</td>
                    <td><span class="badge tipo-comp">COMPONENTE L1</span></td>
                    <td class="text-right">${comp['valor']:,}</td>
                </tr>
            """
    
    categorias_badges = ''.join([f'<span class="badge cat-{cat}">{cat}</span>' for cat in datos_l2.get('categorias_licencia', [])])
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{datos_l2['bim_id']} - {datos_l2['nombre']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
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
        .header h1 {{ font-size: 2.8em; margin-bottom: 10px; }}
        .header .subtitle {{ font-size: 1.3em; opacity: 0.9; }}
        .badges {{ margin-top: 15px; }}
        .badge {{
            display: inline-block;
            padding: 5px 12px;
            background: rgba(255,255,255,0.2);
            border-radius: 15px;
            font-size: 0.85em;
            margin-right: 8px;
            margin-top: 5px;
        }}
        .content {{ padding: 40px; }}
        .section {{ margin-bottom: 40px; }}
        .section h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #e74c3c;
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
        .info-box {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #e74c3c;
        }}
        .info-box h3 {{
            color: #e74c3c;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        .info-box p {{
            font-size: 1.5em;
            font-weight: bold;
            color: #2c3e50;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }}
        th {{
            background: #2c3e50;
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9em;
        }}
        tr:hover {{ background: #f5f5f5; }}
        .text-right {{ text-align: right; }}
        .badge-l1, .badge-l2 {{
            background: #3498db;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        .badge-l2 {{ background: #e74c3c; }}
        .tipo-ref {{ background: #f39c12; color: white; }}
        .tipo-comp {{ background: #27ae60; color: white; }}
        .cat-A1, .cat-A2 {{ background: #9b59b6; color: white; }}
        .cat-B1, .cat-B2, .cat-B3 {{ background: #3498db; color: white; }}
        .cat-C1, .cat-C2, .cat-C3 {{ background: #e67e22; color: white; }}
        .normatividad-box {{
            background: #ecf0f1;
            padding: 25px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 5px solid #e74c3c;
        }}
        .normatividad-box h3 {{
            color: #c0392b;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        .norma-requisito {{
            background: white;
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
        }}
        .norma-requisito strong {{
            color: #2c3e50;
            display: block;
            margin-bottom: 10px;
        }}
        .norma-requisito ul {{
            margin-left: 20px;
        }}
        .norma-requisito li {{
            margin: 8px 0;
            color: #555;
        }}
        .btn-back {{
            display: inline-block;
            padding: 12px 24px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s;
        }}
        .btn-back:hover {{
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏁 {datos_l2['nombre']}</h1>
            <div class="subtitle">{datos_l2['bim_id']} · {datos_l2['codigo']}</div>
            <div class="badges">
                <span class="badge">Nivel BIM: L2 - Configuración</span>
                <span class="badge">Tipo: {datos_l2['tipo']}</span>
                {categorias_badges}
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📊 Información General</h2>
                <div class="info-grid">
                    <div class="info-box">
                        <h3>💰 Valor Total</h3>
                        <p>${datos_l2['valor_total']:,} COP</p>
                    </div>
                    <div class="info-box">
                        <h3>🔧 Componentes</h3>
                        <p>{len(datos_l2['componentes'])} elementos</p>
                    </div>
                    <div class="info-box">
                        <h3>🚗 Categorías Licencia</h3>
                        <p>{len(datos_l2['categorias_licencia'])} tipos</p>
                    </div>
                </div>
                <p><strong>Descripción:</strong> {datos_l2['descripcion']}</p>
                <p><strong>Fuente:</strong> {datos_l2['fuente']}</p>
            </div>
            
            <div class="section">
                <h2>🧩 Componentes</h2>
                <table>
                    <thead>
                        <tr>
                            <th>BIM ID</th>
                            <th>Nombre</th>
                            <th>Tipo</th>
                            <th>Valor (COP)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {componentes_html}
                    </tbody>
                </table>
            </div>
            
{NORMATIVIDAD_L2}
            
            <div class="section">
                <a href="../index.html" class="btn-back">← Volver al Inicio</a>
                <a href="index_l2.html" class="btn-back">📋 Índice L2</a>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    return html


def generar_html_l1(datos_l1):
    """Genera HTML completo para ficha L1"""
    
    # Componentes L0
    componentes_html = ""
    if datos_l1.get('componentes_l0'):
        for comp_l0 in datos_l1['componentes_l0']:
            componentes_html += f"""
                <tr>
                    <td><span class="badge-l0">{comp_l0}</span></td>
                    <td>Elemento atómico</td>
                    <td><a href="../fichas_l0/{comp_l0}.html">Ver detalles</a></td>
                </tr>
            """
    else:
        componentes_html = "<tr><td colspan='3' style='text-align:center;color:#999;'>Sin componentes L0 definidos</td></tr>"
    
    # Maniobras
    maniobras_html = ""
    for maniobra in datos_l1.get('maniobras_soportadas', []):
        maniobras_html += f"<li>{maniobra}</li>"
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{datos_l1['bim_id']} - {datos_l1['nombre']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
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
            background: linear-gradient(135deg, #27ae60 0%, #229954 100%);
            color: white;
            padding: 40px;
        }}
        .header h1 {{ font-size: 2.8em; margin-bottom: 10px; }}
        .header .subtitle {{ font-size: 1.3em; opacity: 0.9; }}
        .badges {{ margin-top: 15px; }}
        .badge {{
            display: inline-block;
            padding: 5px 12px;
            background: rgba(255,255,255,0.2);
            border-radius: 15px;
            font-size: 0.85em;
            margin-right: 8px;
        }}
        .content {{ padding: 40px; }}
        .section {{ margin-bottom: 40px; }}
        .section h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #27ae60;
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
        .info-box {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #27ae60;
        }}
        .info-box h3 {{
            color: #27ae60;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        .info-box p {{
            font-size: 1.5em;
            font-weight: bold;
            color: #2c3e50;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }}
        th {{
            background: #2c3e50;
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9em;
        }}
        tr:hover {{ background: #f5f5f5; }}
        .badge-l0 {{
            background: #16a085;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        .maniobras-list {{
            background: #ecf0f1;
            padding: 20px 20px 20px 40px;
            border-radius: 8px;
            border-left: 5px solid #27ae60;
        }}
        .maniobras-list li {{
            margin: 8px 0;
            color: #2c3e50;
        }}
        .normatividad-box {{
            background: #ecf0f1;
            padding: 25px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 5px solid #27ae60;
        }}
        .normatividad-box h3 {{
            color: #229954;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        .norma-requisito {{
            background: white;
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
        }}
        .norma-requisito strong {{
            color: #2c3e50;
            display: block;
            margin-bottom: 10px;
        }}
        .norma-requisito ul {{
            margin-left: 20px;
        }}
        .norma-requisito li {{
            margin: 8px 0;
            color: #555;
        }}
        .btn-back {{
            display: inline-block;
            padding: 12px 24px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s;
            margin-right: 10px;
        }}
        .btn-back:hover {{
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔧 {datos_l1['nombre']}</h1>
            <div class="subtitle">{datos_l1['bim_id']} · {datos_l1['codigo']}</div>
            <div class="badges">
                <span class="badge">Nivel BIM: L1 - Ensamblaje</span>
                <span class="badge">Tipo: {datos_l1['tipo']}</span>
                <span class="badge">Valor: ${datos_l1['valor_cop']:,} COP</span>
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📊 Información General</h2>
                <div class="info-grid">
                    <div class="info-box">
                        <h3>💰 Valor</h3>
                        <p>${datos_l1['valor_cop']:,} COP</p>
                    </div>
                    <div class="info-box">
                        <h3>📦 Cantidad</h3>
                        <p>{datos_l1['cantidad']} {datos_l1['unidad']}</p>
                    </div>
                    <div class="info-box">
                        <h3>🔧 Tipo</h3>
                        <p>{datos_l1['tipo']}</p>
                    </div>
                </div>
                <p><strong>Descripción:</strong> {datos_l1['descripcion']}</p>
                <p><strong>Fuente:</strong> {datos_l1['fuente']}</p>
            </div>
            
            <div class="section">
                <h2>🧩 Componentes L0</h2>
                <table>
                    <thead>
                        <tr>
                            <th>BIM ID</th>
                            <th>Tipo</th>
                            <th>Enlace</th>
                        </tr>
                    </thead>
                    <tbody>
                        {componentes_html}
                    </tbody>
                </table>
            </div>
            
            <div class="section">
                <h2>🏁 Maniobras Soportadas</h2>
                <ul class="maniobras-list">
                    {maniobras_html}
                </ul>
            </div>
            
{NORMATIVIDAD_L1}
            
            <div class="section">
                <a href="../index.html" class="btn-back">← Volver al Inicio</a>
                <a href="index_l1.html" class="btn-back">📋 Índice L1</a>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    return html


# ========================= FUNCIÓN PRINCIPAL =========================

def main():
    print("🚀 Completando niveles L2, L1 y L0...\n")
    
    # Cargar datos
    with open('TABLAS_L2_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l2 = json.load(f)
    
    with open('TABLAS_L1_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l1 = json.load(f)
    
    # Generar fichas L2
    print("📋 Generando fichas L2...")
    os.makedirs('fichas_l2', exist_ok=True)
    
    for bim_id, componente in datos_l2['componentes'].items():
        html = generar_html_l2(componente)
        filename = f"fichas_l2/{bim_id}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {filename}")
    
    # Generar fichas L1
    print("\n🔧 Generando fichas L1...")
    os.makedirs('fichas_l1', exist_ok=True)
    
    for bim_id, componente in datos_l1['componentes'].items():
        if componente['tipo'] == 'CONSTRUCTOR':  # Solo las constructoras
            html = generar_html_l1(componente)
            filename = f"fichas_l1/{bim_id}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  ✅ {filename}")
    
    print("\n✨ Completado!")

if __name__ == "__main__":
    main()
