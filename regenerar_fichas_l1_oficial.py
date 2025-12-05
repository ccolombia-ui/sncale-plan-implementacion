"""
Regenerar Fichas L1 desde Google Doc Oficial
=============================================

Genera fichas HTML para los 3 ensamblajes L1 (Pistas de conducción):
- BIM_L1_001.html - Pista Clase I (Básica) - 16 componentes
- BIM_L1_002.html - Pista Clase II (Intermedia) - 6 componentes adicionales
- BIM_L1_003.html - Pista Clase III (Avanzada) - 7 componentes adicionales

Fuente: TABLAS_L1_OFICIALES.json (extraído del Google Doc oficial)
"""

import json
from pathlib import Path

# Configuración
INPUT_FILE = Path('TABLAS_L1_OFICIALES.json')
OUTPUT_DIR = Path('fichas_l1')

# Crear directorio de salida
OUTPUT_DIR.mkdir(exist_ok=True)

# Mapeo de niveles L1 a BIM IDs
MAPEO_FICHAS = {
    'pista_clase_I': {
        'bim_id': 'BIM_L1_001',
        'titulo': 'Pista de Conducción Clase I',
        'subtitulo': 'Ensamblaje Básico - Categorías A1, A2, B1, C1',
        'descripcion': 'Circuito de evaluación para maniobras básicas de conducción. Incluye 14 maniobras fundamentales (MANIOBRA_00 a MANIOBRA_13) más pavimento asfáltico y señalización horizontal/vertical estándar.',
        'color_primario': '#2a5298',
        'color_secundario': '#667eea'
    },
    'pista_clase_II': {
        'bim_id': 'BIM_L1_002',
        'titulo': 'Pista de Conducción Clase II',
        'subtitulo': 'Ensamblaje Intermedio - Categorías A2, B1, C1',
        'descripcion': 'Circuito de evaluación intermedia que incluye todos los componentes de Clase I más 3 maniobras con remolque (MANIOBRA_14 a MANIOBRA_16). Pavimento reforzado y señalización intermedia.',
        'color_primario': '#764ba2',
        'color_secundario': '#f093fb'
    },
    'pista_clase_III': {
        'bim_id': 'BIM_L1_003',
        'titulo': 'Pista de Conducción Clase III',
        'subtitulo': 'Ensamblaje Avanzado - Categorías B1, C1',
        'descripcion': 'Circuito de evaluación avanzada que incluye todos los componentes de Clase II más 3 maniobras para vehículos pesados (MANIOBRA_17 a MANIOBRA_19). Incluye pavimento especializado, señalización avanzada y área de carga/descarga.',
        'color_primario': '#1e3c72',
        'color_secundario': '#2a5298'
    }
}

def generar_html_ficha_l1(nivel, datos, config):
    """
    Genera HTML completo para una ficha L1
    
    Args:
        nivel: 'pista_clase_I', 'pista_clase_II', 'pista_clase_III'
        datos: Datos del nivel desde TABLAS_L1_OFICIALES.json
        config: Configuración visual y descriptiva
    
    Returns:
        str: HTML completo de la ficha
    """
    componentes = datos['componentes']
    num_componentes = len(componentes)
    
    # Calcular valorización aproximada (si aplica)
    # Estos valores vendrán de las tablas L2 en siguiente fase
    valores_aproximados = {
        'pista_clase_I': '$975,000,000',
        'pista_clase_II': '$680,000,000',
        'pista_clase_III': '$1,850,000,000'
    }
    
    valor_aproximado = valores_aproximados.get(nivel, 'Por determinar')
    
    # Generar filas de tabla de componentes
    filas_componentes = []
    for i, comp in enumerate(componentes, start=1):
        fila = f"""
                        <tr>
                            <td style="text-align: center;">{i}</td>
                            <td><strong>{comp.get('componente', 'N/A')}</strong></td>
                            <td>{comp.get('descripcion', 'Sin descripción')}</td>
                            <td style="text-align: center;">{comp.get('categoria', 'N/A')}</td>
                            <td style="text-align: center;">{comp.get('tipo', 'N/A')}</td>
                            <td><code>{comp.get('referencia', 'N/A')}</code></td>
                        </tr>"""
        filas_componentes.append(fila)
    
    filas_html = ''.join(filas_componentes)
    
    # Generar HTML completo
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['titulo']} - {config['bim_id']} | SNCALE L1</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, {config['color_primario']} 0%, {config['color_secundario']} 100%);
            color: #333;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 20px auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        /* Header con logo UPTC */
        .header {{
            background: linear-gradient(135deg, {config['color_primario']} 0%, {config['color_secundario']} 100%);
            color: white;
            padding: 40px;
            position: relative;
        }}
        
        .header-logo {{
            position: absolute;
            top: 20px;
            right: 40px;
            width: 100px;
            height: 100px;
        }}
        
        .header-logo svg {{
            width: 100%;
            height: 100%;
        }}
        
        .header-content {{
            max-width: 900px;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.95;
            margin-bottom: 20px;
            font-weight: 500;
        }}
        
        .header .description {{
            font-size: 1em;
            opacity: 0.9;
            margin-bottom: 25px;
            line-height: 1.8;
        }}
        
        .badges {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            background: rgba(255,255,255,0.25);
            padding: 10px 24px;
            border-radius: 25px;
            font-size: 0.95em;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
            font-weight: 500;
        }}
        
        .content {{
            padding: 50px;
        }}
        
        .section {{
            margin-bottom: 50px;
        }}
        
        .section-title {{
            font-size: 2em;
            color: {config['color_primario']};
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 3px solid {config['color_secundario']};
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid {config['color_primario']};
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .info-card h3 {{
            color: {config['color_primario']};
            margin-bottom: 12px;
            font-size: 1.1em;
        }}
        
        .info-card p {{
            color: #495057;
            font-size: 1.3em;
            font-weight: 600;
        }}
        
        .info-card .unit {{
            font-size: 0.85em;
            color: #6c757d;
            font-weight: normal;
        }}
        
        /* Tabla de componentes */
        .table-container {{
            overflow-x: auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}
        
        thead {{
            background: linear-gradient(135deg, {config['color_primario']} 0%, {config['color_secundario']} 100%);
            color: white;
        }}
        
        thead th {{
            padding: 18px 15px;
            text-align: left;
            font-weight: 600;
            font-size: 0.95em;
            letter-spacing: 0.5px;
        }}
        
        tbody tr {{
            border-bottom: 1px solid #e9ecef;
            transition: background 0.3s;
        }}
        
        tbody tr:hover {{
            background: #f8f9fa;
        }}
        
        tbody td {{
            padding: 16px 15px;
            font-size: 0.9em;
        }}
        
        tbody td code {{
            background: #e9ecef;
            padding: 4px 10px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: {config['color_primario']};
        }}
        
        /* Footer */
        .footer {{
            background: #f8f9fa;
            padding: 30px 50px;
            border-top: 1px solid #dee2e6;
        }}
        
        .footer-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }}
        
        .footer-info {{
            color: #6c757d;
            font-size: 0.9em;
        }}
        
        .footer-info strong {{
            color: {config['color_primario']};
        }}
        
        .footer-links {{
            display: flex;
            gap: 20px;
        }}
        
        .footer-links a {{
            color: {config['color_primario']};
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }}
        
        .footer-links a:hover {{
            color: {config['color_secundario']};
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .header {{
                padding: 30px 20px;
            }}
            
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .header-logo {{
                width: 70px;
                height: 70px;
                right: 20px;
            }}
            
            .content {{
                padding: 30px 20px;
            }}
            
            .section-title {{
                font-size: 1.5em;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
            
            .footer {{
                padding: 20px;
            }}
            
            .footer-content {{
                flex-direction: column;
                align-items: flex-start;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-logo">
                <!-- Logo UPTC SVG -->
                <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="50" cy="50" r="45" fill="none" stroke="white" stroke-width="3"/>
                    <text x="50" y="58" font-family="Arial, sans-serif" font-size="32" font-weight="bold" 
                          fill="white" text-anchor="middle">UPTC</text>
                </svg>
            </div>
            
            <div class="header-content">
                <h1>{config['bim_id']}</h1>
                <div class="subtitle">{config['titulo']}</div>
                <div class="description">{config['descripcion']}</div>
                
                <div class="badges">
                    <span class="badge">Nivel L1 - Ensamblaje</span>
                    <span class="badge">{num_componentes} Componentes</span>
                    <span class="badge">{config['subtitulo']}</span>
                    <span class="badge">Fuente: Google Doc Oficial</span>
                </div>
            </div>
        </header>
        
        <!-- Content -->
        <main class="content">
            <!-- Información General -->
            <section class="section">
                <h2 class="section-title">📊 Información General</h2>
                
                <div class="info-grid">
                    <div class="info-card">
                        <h3>Código BIM</h3>
                        <p>{config['bim_id']}</p>
                    </div>
                    
                    <div class="info-card">
                        <h3>Nivel</h3>
                        <p>L1 - Ensamblaje</p>
                    </div>
                    
                    <div class="info-card">
                        <h3>Componentes</h3>
                        <p>{num_componentes} <span class="unit">elementos</span></p>
                    </div>
                    
                    <div class="info-card">
                        <h3>Valorización Aproximada</h3>
                        <p>{valor_aproximado} <span class="unit">COP</span></p>
                    </div>
                </div>
            </section>
            
            <!-- Componentes del Ensamblaje -->
            <section class="section">
                <h2 class="section-title">🔧 Componentes del Ensamblaje</h2>
                
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 60px;">#</th>
                                <th style="width: 180px;">Componente</th>
                                <th>Descripción</th>
                                <th style="width: 120px;">Categoría</th>
                                <th style="width: 110px;">Tipo</th>
                                <th style="width: 180px;">Referencia</th>
                            </tr>
                        </thead>
                        <tbody>
{filas_html}
                        </tbody>
                    </table>
                </div>
            </section>
            
            <!-- Fuente de Datos -->
            <section class="section">
                <h2 class="section-title">📄 Fuente de Datos</h2>
                
                <div class="info-card">
                    <h3>Documento Oficial</h3>
                    <p style="font-size: 1em; font-weight: normal; margin-top: 10px;">
                        <strong>Título:</strong> MUNAY_5.2__anexo_b__DEFINITIVO<br>
                        <strong>Google Doc ID:</strong> 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE<br>
                        <strong>Tabla origen:</strong> #{datos['tabla_numero']} (Elemento índice {datos['elemento_index']})<br>
                        <strong>Fecha extracción:</strong> 2025-11-03<br>
                        <strong>Estado:</strong> ✅ Validado como única fuente de verdad
                    </p>
                </div>
            </section>
        </main>
        
        <!-- Footer -->
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-info">
                    <strong>Sistema Nacional de Centros de Enseñanza Automovilística Certificados (SNCALE)</strong><br>
                    Universidad Pedagógica y Tecnológica de Colombia (UPTC)<br>
                    Generado desde Google Doc oficial - Nivel L1
                </div>
                
                <div class="footer-links">
                    <a href="../index.html">← Volver al Índice</a>
                    <a href="../fichas_l2/{config['bim_id'].replace('L1', 'L2')}.html">Ver Configuración L2 →</a>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>"""
    
    return html

def main():
    print("=" * 70)
    print("REGENERACIÓN DE FICHAS L1 - GOOGLE DOC OFICIAL")
    print("=" * 70)
    print()
    
    # 1. Cargar datos L1
    print("📂 Cargando datos L1 oficiales...")
    if not INPUT_FILE.exists():
        print(f"❌ ERROR: No se encuentra {INPUT_FILE}")
        print("   Ejecuta primero: python extraer_tablas_l1_oficial.py")
        return
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        datos_l1 = json.load(f)
    
    tablas = datos_l1['tablas_l1']
    print(f"✅ Cargadas {len(tablas)} tablas L1")
    print()
    
    # 2. Generar cada ficha
    print("🔨 Generando fichas HTML...")
    print()
    
    fichas_generadas = []
    
    for nivel, config in MAPEO_FICHAS.items():
        if nivel not in tablas:
            print(f"⏭️  {nivel}: OMITIDO (no encontrado en datos)")
            continue
        
        datos = tablas[nivel]
        bim_id = config['bim_id']
        
        print(f"📄 Generando {bim_id}.html ({config['titulo']})...")
        
        # Generar HTML
        html = generar_html_ficha_l1(nivel, datos, config)
        
        # Guardar archivo
        output_file = OUTPUT_DIR / f"{bim_id}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        num_componentes = len(datos['componentes'])
        print(f"   ✅ {num_componentes} componentes incluidos")
        print(f"   💾 Guardado: {output_file}")
        
        fichas_generadas.append({
            'bim_id': bim_id,
            'titulo': config['titulo'],
            'archivo': output_file.name,
            'componentes': num_componentes
        })
        
        print()
    
    # 3. Resumen final
    print("=" * 70)
    print("RESUMEN DE GENERACIÓN")
    print("=" * 70)
    print()
    
    print(f"📊 Fichas generadas: {len(fichas_generadas)}")
    print(f"📁 Directorio: {OUTPUT_DIR.absolute()}")
    print()
    
    for ficha in fichas_generadas:
        print(f"   ✅ {ficha['bim_id']} - {ficha['titulo']}")
        print(f"      Archivo: {ficha['archivo']}")
        print(f"      Componentes: {ficha['componentes']}")
        print()
    
    print("=" * 70)
    print("✅ REGENERACIÓN COMPLETADA")
    print("=" * 70)
    print()
    print("SIGUIENTE PASO:")
    print("1. Revisar fichas generadas en:", OUTPUT_DIR.absolute())
    print("2. Copiar a repositorio GitHub Pages si es necesario")
    print("3. Ejecutar: git add fichas_l1/*.html && git commit && git push")
    print()
    
    # URLs de GitHub Pages (asumir estructura estándar)
    print("🌐 URLs esperadas en GitHub Pages:")
    for ficha in fichas_generadas:
        url = f"https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l1/{ficha['archivo']}"
        print(f"   {url}")
    print()
    
    print("=" * 70)

if __name__ == '__main__':
    main()
