#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERADOR DE FICHA TÉCNICA L3 - CALE.n_2
Genera ficha HTML profesional para CALE.n_2 (Centros Subregionales)
Basado en datos de SECCION_B20_CALE_N2.md (Anexo B)
"""

import os
import sys
from datetime import datetime

# Importar logo UPTC
sys.path.insert(0, 'C:/guezarel/templates')
from logo_uptc_constant import LOGO_UPTC_BASE64

# Configuración
OUTPUT_DIR = 'fichas_l3'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_svg_isometrico_cale_n2():
    """Genera diagrama isométrico simplificado de CALE.n_2"""
    return '''
    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <!-- Fondo -->
        <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#e8f5e9;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#c8e6c9;stop-opacity:1" />
            </linearGradient>
            <filter id="shadow">
                <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.3"/>
            </filter>
        </defs>
        
        <rect width="800" height="600" fill="url(#bgGrad)"/>
        
        <!-- Título -->
        <text x="400" y="30" text-anchor="middle" font-size="24" font-weight="bold" fill="#2e7d32">
            CALE.n_2 - Centro Subregional
        </text>
        <text x="400" y="55" text-anchor="middle" font-size="14" fill="#424242">
            Vista isométrica simplificada - Clase I + II
        </text>
        
        <!-- Edificación (fondo) - Isométrica -->
        <g transform="translate(80, 120)">
            <!-- Base edificio -->
            <path d="M 0,100 L 180,10 L 360,100 L 180,190 Z" 
                  fill="#ff7043" stroke="#d84315" stroke-width="2" filter="url(#shadow)"/>
            <path d="M 180,190 L 180,370 L 0,280 L 0,100 Z" 
                  fill="#ff5722" stroke="#d84315" stroke-width="2"/>
            <path d="M 180,190 L 360,100 L 360,280 L 180,370 Z" 
                  fill="#f4511e" stroke="#d84315" stroke-width="2"/>
            
            <!-- Ventanas múltiples -->
            <rect x="20" y="140" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            <rect x="60" y="160" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            <rect x="100" y="180" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            <rect x="140" y="200" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            
            <!-- Segunda fila ventanas -->
            <rect x="20" y="200" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            <rect x="60" y="220" width="30" height="35" fill="#64b5f6" stroke="#1976d2" stroke-width="1"/>
            
            <!-- Puerta -->
            <rect x="150" y="280" width="50" height="90" fill="#795548" stroke="#4e342e" stroke-width="2"/>
            
            <!-- Letrero CALE -->
            <rect x="60" y="60" width="120" height="30" fill="#2e7d32" rx="3"/>
            <text x="120" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="white">CALE.n_2</text>
        </g>
        
        <!-- Pista Clase II (centro-derecha) -->
        <g transform="translate(450, 150)">
            <!-- Base pista II -->
            <path d="M 0,40 L 80,0 L 240,40 L 160,80 Z" 
                  fill="#7986cb" stroke="#303f9f" stroke-width="2" filter="url(#shadow)"/>
            
            <!-- Maniobras avanzadas -->
            <circle cx="40" cy="28" r="10" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
            <circle cx="90" cy="18" r="10" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
            <circle cx="140" cy="22" r="10" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
            <circle cx="190" cy="32" r="10" fill="#ffb74d" stroke="#f57c00" stroke-width="2"/>
            
            <!-- Etiqueta -->
            <text x="120" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a237e">
                Pista Clase II
            </text>
            <text x="120" y="85" text-anchor="middle" font-size="9" fill="#1a237e">
                (Motocicletas)
            </text>
        </g>
        
        <!-- Pista Clase I Superior -->
        <g transform="translate(480, 250)">
            <!-- Base pista I -->
            <path d="M 0,40 L 70,0 L 210,40 L 140,80 Z" 
                  fill="#81c784" stroke="#388e3c" stroke-width="2" filter="url(#shadow)"/>
            
            <!-- Maniobras básicas -->
            <circle cx="35" cy="28" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="70" cy="18" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="105" cy="20" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="140" cy="28" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="175" cy="36" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            
            <!-- Etiqueta -->
            <text x="105" y="70" text-anchor="middle" font-size="10" font-weight="bold" fill="#1b5e20">
                Pista Clase I (#1)
            </text>
        </g>
        
        <!-- Pista Clase I Inferior -->
        <g transform="translate(480, 370)">
            <!-- Base pista I -->
            <path d="M 0,30 L 70,0 L 210,30 L 140,60 Z" 
                  fill="#81c784" stroke="#388e3c" stroke-width="2" filter="url(#shadow)"/>
            
            <!-- Maniobras básicas -->
            <circle cx="35" cy="20" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="70" y="12" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="105" cy="14" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="140" cy="20" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            <circle cx="175" cy="26" r="8" fill="#fff59d" stroke="#f57f17" stroke-width="1.5"/>
            
            <!-- Etiqueta -->
            <text x="105" y="55" text-anchor="middle" font-size="10" font-weight="bold" fill="#1b5e20">
                Pista Clase I (#2)
            </text>
        </g>
        
        <!-- Área Teórica -->
        <g transform="translate(60, 400)">
            <rect width="130" height="90" fill="#ba68c8" stroke="#6a1b9a" stroke-width="2" 
                  rx="5" filter="url(#shadow)"/>
            <text x="65" y="25" text-anchor="middle" font-size="12" font-weight="bold" fill="#4a148c">
                Área Teórica
            </text>
            <text x="65" y="45" text-anchor="middle" font-size="11" fill="#6a1b9a">
                16 Cubículos
            </text>
            <text x="65" y="62" text-anchor="middle" font-size="10" fill="#6a1b9a">
                8 Evaluadores
            </text>
            <text x="65" y="78" text-anchor="middle" font-size="9" fill="#6a1b9a">
                6 Administrativos
            </text>
        </g>
        
        <!-- Leyenda -->
        <g transform="translate(220, 420)">
            <text x="0" y="0" font-size="13" font-weight="bold" fill="#2e7d32">Componentes L2:</text>
            
            <rect x="0" y="10" width="18" height="13" fill="#7986cb" stroke="#303f9f" stroke-width="1"/>
            <text x="22" y="21" font-size="10" fill="#424242">Pista Clase II (1,800 m²)</text>
            
            <rect x="160" y="10" width="18" height="13" fill="#81c784" stroke="#388e3c" stroke-width="1"/>
            <text x="182" y="21" font-size="10" fill="#424242">Pista Clase I×2 (5,000 m²)</text>
            
            <rect x="340" y="10" width="18" height="13" fill="#ff7043" stroke="#d84315" stroke-width="1"/>
            <text x="362" y="21" font-size="10" fill="#424242">Edificación</text>
            
            <rect x="0" y="30" width="18" height="13" fill="#ba68c8" stroke="#6a1b9a" stroke-width="1"/>
            <text x="22" y="41" font-size="10" fill="#424242">Centro Teórico 16q</text>
            
            <text x="0" y="65" font-size="10" font-weight="bold" fill="#2e7d32">
                Capacidad: 15,000 - 35,000 eval/año | Personal: 18 personas/nodo
            </text>
            <text x="0" y="80" font-size="9" fill="#666">
                20 centros a nivel nacional | Cobertura: Ciudades intermedias y centros subregionales
            </text>
        </g>
    </svg>
    '''

def generar_ficha_l3_cale_n2():
    """Genera ficha HTML para BIM_L3_002 (CALE.n_2)"""
    
    bim_id = "BIM_L3_002"
    nombre = "CALE.n_2 - Centros Subregionales"
    
    # Datos del Anexo B (SECCION_B20)
    datos = {
        'nombre': nombre,
        'descripcion': 'Centro de Enseñanza para Licencias - Categoría Subregional (n_2)',
        'categoria': 'Centros Subregionales',
        'capacidad_evaluaciones': '15,000 - 35,000 eval/año',
        'infraestructura': 'Edificación adecuada (arriendo) + 1 Pista Clase II + 2 Pistas Clase I',
        'personal': '18 personas/nodo (4 evaluadores prácticos, 8 teóricos, 6 administrativos)',
        'instancias_nacionales': 20,
        'cobertura': 'Ciudades intermedias y centros subregionales',
        'normativa': 'Resolución 20253040037125/2025 - Categoría B',
        'capex_parcial': 4012929940,  # Solo CALE_TEORICO_16q valorizado
        'componentes_l2': [
            {
                'nombre': 'Pista Clase II',
                'bim_id': 'BIM_L2_002',
                'descripcion': 'Pista completa Clase II (B2, C2) - Motocicletas',
                'cantidad': 20,
                'url': '../fichas_l2/BIM_L2_002.html'
            },
            {
                'nombre': 'Pista Clase I',
                'bim_id': 'BIM_L2_001',
                'descripcion': 'Pista completa Clase I (A1, A2, B1, C1) - Vehículos livianos (×2)',
                'cantidad': 40,
                'url': '../fichas_l2/BIM_L2_001.html'
            },
            {
                'nombre': 'Edificación',
                'bim_id': 'L2.edificacion',
                'descripcion': 'Edificación adecuada (arriendo)',
                'cantidad': 20,
                'url': '#'
            },
            {
                'nombre': 'Centro Teórico 16q',
                'bim_id': 'L2.cale_teorico_16q',
                'descripcion': 'Centro teórico 16 cubículos + áreas admin',
                'cantidad': 20,
                'valor_unitario': 200646497,
                'url': '#'
            },
            {
                'nombre': 'Tecnología',
                'bim_id': 'L2.tecnologia',
                'descripcion': 'Plataforma tecnológica CALE',
                'cantidad': 20,
                'url': '#'
            },
            {
                'nombre': 'Certificaciones',
                'bim_id': 'L2.certificaciones',
                'descripcion': 'Certificaciones ISO (4)',
                'cantidad': 20,
                'url': '#'
            },
            {
                'nombre': 'Seguros',
                'bim_id': 'L2.seguros',
                'descripcion': 'Seguros y pólizas',
                'cantidad': 20,
                'url': '#'
            }
        ]
    }
    
    svg_diagrama = generar_svg_isometrico_cale_n2()
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nombre} - {bim_id} | SNCALE L3</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2e7d32 0%, #43a047 100%);
            color: white;
            padding: 40px;
            position: relative;
        }}
        
        .logo-uptc {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 80px;
            height: auto;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header .bim-id {{
            font-size: 1.2em;
            opacity: 0.9;
            font-weight: 300;
        }}
        
        .badges {{
            display: flex;
            gap: 10px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #2e7d32;
            border-left: 5px solid #43a047;
            padding-left: 15px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        
        .diagram-container {{
            background: #f1f8e9;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .diagram-container svg {{
            width: 100%;
            height: auto;
            max-height: 600px;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .info-card {{
            background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }}
        
        .info-card:hover {{
            transform: translateY(-5px);
        }}
        
        .info-card h3 {{
            font-size: 1.1em;
            margin-bottom: 10px;
            opacity: 0.9;
        }}
        
        .info-card .value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .info-card .label {{
            font-size: 0.9em;
            opacity: 0.8;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        table th {{
            background: linear-gradient(135deg, #2e7d32 0%, #43a047 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        table tr:hover {{
            background: #f1f8e9;
        }}
        
        .alert {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        
        .alert-info {{
            background: #e8f5e9;
            border-left-color: #2e7d32;
            color: #1b5e20;
        }}
        
        .alert h4 {{
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 30px 40px;
            border-top: 3px solid #43a047;
            text-align: center;
        }}
        
        .footer-logo {{
            width: 60px;
            margin-bottom: 15px;
        }}
        
        .nav-links {{
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }}
        
        .nav-links a {{
            background: #43a047;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s ease;
        }}
        
        .nav-links a:hover {{
            background: #2e7d32;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
            
            table {{
                font-size: 0.9em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="{LOGO_UPTC_BASE64}" alt="Logo UPTC" class="logo-uptc">
            <h1>{nombre}</h1>
            <div class="bim-id">Código BIM: {bim_id}</div>
            <div class="badges">
                <span class="badge">🏢 Nivel L3 - Especialización CALE</span>
                <span class="badge">📍 {datos['instancias_nacionales']} Centros Nacionales</span>
                <span class="badge">🏍️ Clase I + II (sin pesados)</span>
            </div>
        </div>
        
        <div class="content">
            <!-- Diagrama Isométrico -->
            <div class="section">
                <h2>📐 Diagrama Isométrico</h2>
                <div class="diagram-container">
                    {svg_diagrama}
                </div>
            </div>
            
            <!-- Información General -->
            <div class="section">
                <h2>📊 Información General</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <h3>CAPEX Parcial</h3>
                        <div class="value">${datos['capex_parcial']:,.0f}</div>
                        <div class="label">COP (componentes valorizados)</div>
                    </div>
                    <div class="info-card">
                        <h3>Capacidad</h3>
                        <div class="value">{datos['capacidad_evaluaciones']}</div>
                        <div class="label">Evaluaciones/año por centro</div>
                    </div>
                    <div class="info-card">
                        <h3>Categoría</h3>
                        <div class="value">{datos['categoria']}</div>
                        <div class="label">Nivel de servicio</div>
                    </div>
                </div>
                
                <div class="alert alert-info">
                    <h4>📋 Normatividad</h4>
                    <p>{datos['normativa']}</p>
                </div>
            </div>
            
            <!-- Descripción -->
            <div class="section">
                <h2>📝 Descripción</h2>
                <p><strong>{datos['descripcion']}</strong></p>
                <p style="margin-top: 15px;">
                    Los <strong>CALE.n_2</strong> son centros subregionales diseñados para atender la demanda de evaluación 
                    de licencias de conducción <strong>Clase I + II</strong> (vehículos livianos y motocicletas, sin vehículos pesados). 
                    Estos centros están ubicados en <strong>{datos['cobertura'].lower()}</strong>, proporcionando 
                    cobertura intermedia entre los centros metropolitanos (n_1) y locales (n_3).
                </p>
                <p style="margin-top: 15px;">
                    <strong>Infraestructura:</strong> {datos['infraestructura']}<br>
                    <strong>Personal operativo:</strong> {datos['personal']}<br>
                    <strong>Instancias a nivel nacional:</strong> {datos['instancias_nacionales']} centros
                </p>
            </div>
            
            <!-- Componentes L2 -->
            <div class="section">
                <h2>🔧 Componentes L2 que lo forman</h2>
                <p>Este nivel L3 se ensambla a partir de los siguientes componentes de nivel L2:</p>
                
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Componente L2</th>
                            <th>Código BIM</th>
                            <th>Descripción</th>
                            <th>Cantidad</th>
                            <th>Ver Ficha</th>
                        </tr>
                    </thead>
                    <tbody>
'''
    
    # Agregar componentes L2
    for idx, comp in enumerate(datos['componentes_l2'], 1):
        link = f'<a href="{comp["url"]}" target="_blank" style="color: #43a047; text-decoration: none; font-weight: bold;">Ver →</a>' if comp['url'] != '#' else '<span style="color: #999;">Pendiente</span>'
        valor_info = ''
        if 'valor_unitario' in comp:
            valor_info = f'<br><small style="color: #666;">Vr. Unit: ${comp["valor_unitario"]:,.0f} COP</small>'
        
        html += f'''
                        <tr>
                            <td>{idx}</td>
                            <td><strong>{comp['nombre']}</strong></td>
                            <td><code style="background: #f1f8e9; padding: 3px 6px; border-radius: 3px;">{comp['bim_id']}</code></td>
                            <td>{comp['descripcion']}{valor_info}</td>
                            <td style="text-align: center;"><strong>{comp['cantidad']}</strong></td>
                            <td>{link}</td>
                        </tr>
'''
    
    html += f'''
                    </tbody>
                </table>
                
                <div class="alert">
                    <h4>⚠️ Nota sobre valorización</h4>
                    <p>
                        El CAPEX parcial mostrado (<strong>${datos['capex_parcial']:,.0f} COP</strong>) corresponde 
                        únicamente al componente <strong>Centro Teórico 16q</strong> que está valorizado en Anexo B.
                        Los demás componentes (Pista Clase I, Pista Clase II, Edificación, Tecnología, Certificaciones, Seguros) 
                        requieren cálculo detallado desde sus respectivas hojas L2.
                    </p>
                </div>
            </div>
            
            <!-- Cobertura Nacional -->
            <div class="section">
                <h2>🗺️ Cobertura Nacional</h2>
                <p>
                    Los {datos['instancias_nacionales']} centros CALE.n_2 están distribuidos estratégicamente en 
                    <strong>{datos['cobertura'].lower()}</strong>, garantizando acceso intermedio al servicio de evaluación 
                    de licencias con capacidad para vehículos livianos y motocicletas.
                </p>
                <p style="margin-top: 15px;">
                    <strong>Tipo de localización:</strong> Configuración base estándar<br>
                    <strong>Mapa interactivo:</strong> 
                    <a href="https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_v2_sidebar_iebm.html" 
                       target="_blank" style="color: #43a047; text-decoration: none; font-weight: bold;">
                        Ver Topología SNCALE BIM (filtrar: 20 CALE.n_2) →
                    </a>
                </p>
            </div>
            
            <!-- Proyección Nacional -->
            <div class="section">
                <h2>📈 Proyección Nacional</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <h3>Total Centros</h3>
                        <div class="value">{datos['instancias_nacionales']}</div>
                        <div class="label">CALE.n_2 a nivel nacional</div>
                    </div>
                    <div class="info-card">
                        <h3>Capacidad Total</h3>
                        <div class="value">{int(datos['capacidad_evaluaciones'].split('-')[0].replace(',','').strip())*datos['instancias_nacionales']:,}</div>
                        <div class="label">Evaluaciones/año (mínimo estimado)</div>
                    </div>
                    <div class="info-card">
                        <h3>Personal Total</h3>
                        <div class="value">{int(datos['personal'].split()[0]) * datos['instancias_nacionales']}</div>
                        <div class="label">Empleos directos generados</div>
                    </div>
                </div>
            </div>
            
            <!-- Referencias -->
            <div class="section">
                <h2>📚 Referencias</h2>
                <ul style="list-style: none; padding: 0;">
                    <li style="padding: 10px; background: #f1f8e9; margin: 5px 0; border-radius: 5px;">
                        📄 <strong>Anexo B - Sección B20:</strong> CALE.N_2 - Centros Subregionales
                    </li>
                    <li style="padding: 10px; background: #f1f8e9; margin: 5px 0; border-radius: 5px;">
                        📊 <strong>Google Sheets:</strong> 
                        <a href="https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=758032184#gid=758032184" 
                           target="_blank" style="color: #43a047;">
                            L3.CALE.n_2
                        </a>
                    </li>
                    <li style="padding: 10px; background: #f1f8e9; margin: 5px 0; border-radius: 5px;">
                        🏗️ <strong>Modelo BIM:</strong> Jerarquía L5→L4→L3→L2→L1→L0
                    </li>
                    <li style="padding: 10px; background: #f1f8e9; margin: 5px 0; border-radius: 5px;">
                        📅 <strong>Generado:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </li>
                </ul>
            </div>
            
            <!-- Navegación -->
            <div class="section">
                <h2>🔗 Navegación</h2>
                <div class="nav-links">
                    <a href="../index.html">🏠 Inicio</a>
                    <a href="BIM_L3_003.html">📍 CALE.n_3</a>
                    <a href="../fichas_l2/BIM_L2_001.html">📦 Ver Fichas L2</a>
                    <a href="../fichas_l1/BIM_L1_001.html">🔩 Ver Fichas L1</a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <img src="{LOGO_UPTC_BASE64}" alt="Logo UPTC" class="footer-logo">
            <p><strong>Universidad Pedagógica y Tecnológica de Colombia - UPTC</strong></p>
            <p>Sistema Nacional de CALE (SNCALE) - Modelo BIM</p>
            <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                Ficha Técnica L3 - {bim_id} | Generado automáticamente desde Anexo B
            </p>
        </div>
    </div>
</body>
</html>
'''
    
    return html

# MAIN
if __name__ == '__main__':
    print("\n" + "="*60)
    print("  GENERADOR DE FICHA TÉCNICA L3 - CALE.n_2")
    print("="*60)
    
    print("\n📋 Generando ficha BIM_L3_002 (CALE.n_2)...")
    
    html_content = generar_ficha_l3_cale_n2()
    output_path = os.path.join(OUTPUT_DIR, 'BIM_L3_002.html')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Guardado en: {os.path.abspath(output_path)}")
    
    print("\n" + "="*60)
    print("  ✅ GENERACIÓN COMPLETADA")
    print("="*60)
    print(f"\n📂 Archivo generado: {output_path}")
    print(f"📊 Categoría: CALE.n_2 - Centros Subregionales")
    print(f"📍 Instancias nacionales: 20 centros")
    print(f"💰 CAPEX parcial: $4,012,929,940 COP")
    print("\n")
