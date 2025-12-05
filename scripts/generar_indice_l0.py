#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera índice HTML para nivel L0
"""

import json

def main():
    with open('TABLAS_L0_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    colores = {
        "IC": "#34495e",
        "DR": "#3498db",
        "SV": "#e67e22",
        "SEG": "#c0392b",
        "EDIF": "#95a5a6",
        "MAT": "#16a085",
        "ADEC": "#27ae60",
        "ELE": "#f39c12",
        "ILU": "#8e44ad",
        "HVAC": "#2980b9",
        "HID": "#3498db",
        "MOB": "#d35400",
        "TEC": "#16a085",
        "AV": "#9b59b6",
        "ACC": "#7f8c8d",
        "VEH": "#1abc9c",
        "CERT": "#2ecc71",
        "OTROS": "#95a5a6"
    }
    
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice L0 - Elementos Atómicos CALE</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            padding: 20px;
        }
        .container {
            max-width: 1600px;
            margin: 0 auto;
        }
        .header {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 {
            color: #2c3e50;
            font-size: 3em;
            margin-bottom: 10px;
        }
        .header p {
            color: #7f8c8d;
            font-size: 1.2em;
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .stat-box {
            background: #ecf0f1;
            padding: 20px 30px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }
        .stat-box h3 {
            color: #3498db;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .stat-box p {
            font-size: 2em;
            font-weight: bold;
            color: #2c3e50;
        }
        .btn-back {
            background: white;
            color: #2c3e50;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            margin-bottom: 30px;
            display: inline-block;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: all 0.3s;
        }
        .btn-back:hover {
            transform: translateX(-5px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }
        .categoria-section {
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .categoria-section h2 {
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid;
        }
        .elementos-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
        }
        .elemento-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            border-left: 4px solid;
            transition: all 0.3s;
        }
        .elemento-card:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }
        .elemento-card h3 {
            font-size: 1.2em;
            margin-bottom: 8px;
        }
        .elemento-card .codigo {
            color: #7f8c8d;
            font-size: 0.85em;
            margin-bottom: 12px;
        }
        .elemento-card p {
            color: #555;
            font-size: 0.9em;
            margin-bottom: 10px;
        }
        .elemento-card .unidad {
            display: inline-block;
            background: #ecf0f1;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.8em;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .elemento-card a {
            display: inline-block;
            margin-top: 10px;
            padding: 8px 16px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            transition: all 0.3s;
        }
        .elemento-card a:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="btn-back">← Volver al Inicio</a>
        
        <div class="header">
            <h1>🔬 Nivel L0 - Elementos Atómicos</h1>
            <p>Base del Modelo BIM - Componentes Individuales</p>
            
            <div class="stats">
                <div class="stat-box">
                    <h3>Total Elementos</h3>
                    <p>91</p>
                </div>
                <div class="stat-box">
                    <h3>Categorías</h3>
                    <p>18</p>
                </div>
                <div class="stat-box">
                    <h3>Completitud</h3>
                    <p>100%</p>
                </div>
                <div class="stat-box">
                    <h3>Con Normatividad</h3>
                    <p>✅ Sí</p>
                </div>
            </div>
        </div>
"""
    
    # Generar secciones por categoría
    for cat_code, cat_info in datos['categorias'].items():
        color = colores.get(cat_code, "#95a5a6")
        
        html += f"""
        <div class="categoria-section">
            <h2 style="color: {color}; border-color: {color};">
                {cat_info['nombre']} ({cat_code}) - {cat_info['cantidad']} elementos
            </h2>
            <div class="elementos-grid">
"""
        
        for comp in cat_info['componentes']:
            codigo_limpio = comp['codigo_l0'].replace('L0.', '').replace('_', '-')
            
            html += f"""
                <div class="elemento-card" style="border-color: {color};">
                    <h3 style="color: {color};">{comp['componente']}</h3>
                    <div class="codigo">{comp['bim_id']} · {comp['codigo_l0']}</div>
                    <p>{comp['descripcion']}</p>
                    <span class="unidad">📦 {comp['unidad']}</span>
                    <a href="{codigo_limpio}.html">Ver Detalles →</a>
                </div>
"""
        
        html += """
            </div>
        </div>
"""
    
    html += """
    </div>
</body>
</html>"""
    
    with open('fichas_l0/index_l0.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ Índice L0 generado: fichas_l0/index_l0.html")

if __name__ == "__main__":
    main()
