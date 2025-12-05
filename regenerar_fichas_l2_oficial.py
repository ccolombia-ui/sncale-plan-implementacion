"""
Regenerar Fichas L2 desde Google Doc Oficial
=============================================

Genera fichas HTML para las 5 configuraciones L2:
- BIM_L2_001.html - Pista Clase I ($975M)
- BIM_L2_002.html - Pista Clase II ($680M)
- BIM_L2_003.html - Pista Clase III ($1.85B)
- BIM_L2_004.html - CALE Teórico 24q ($243M) ✨ NUEVA
- BIM_L2_005.html - CALE Teórico 16q ($200M) ✨ NUEVA

Fuente: TABLAS_L2_OFICIALES.json (extraído del Google Doc oficial)
"""

import json
from pathlib import Path

# Configuración
INPUT_FILE = Path('TABLAS_L2_OFICIALES.json')
OUTPUT_DIR = Path('fichas_l2')

# Crear directorio de salida
OUTPUT_DIR.mkdir(exist_ok=True)

# Colores por nivel
COLORES_L2 = {
    'BIM_L2_001': {'primario': '#2a5298', 'secundario': '#667eea'},
    'BIM_L2_002': {'primario': '#764ba2', 'secundario': '#f093fb'},
    'BIM_L2_003': {'primario': '#1e3c72', 'secundario': '#2a5298'},
    'BIM_L2_004': {'primario': '#0f2027', 'secundario': '#2c5364'},
    'BIM_L2_005': {'primario': '#134e5e', 'secundario': '#71b280'}
}

def formatear_valor(valor_str):
    """Formatea valor COP para mejor lectura"""
    if 'N/A' in valor_str:
        return valor_str
    # Extraer número y formatear
    try:
        # Eliminar $ y comas
        num_str = valor_str.replace('$', '').replace(',', '').strip()
        num = int(num_str)
        # Formatear con comas
        return f"${num:,}"
    except:
        return valor_str

def generar_html_ficha_l2(nivel, datos):
    """
    Genera HTML completo para una ficha L2
    """
    bim_id = datos['bim_id']
    titulo = datos['titulo']
    descripcion = datos['descripcion']
    valor_cop = datos['valorización']['valor_cop']
    valor_formateado = formatear_valor(valor_cop)
    categorias = datos['categoria_licencias']
    componentes_l1 = datos['componentes_l1']
    num_componentes = len(componentes_l1)
    
    # Colores
    colores = COLORES_L2.get(bim_id, {'primario': '#2a5298', 'secundario': '#667eea'})
    
    # Generar filas de componentes L1
    filas_componentes = []
    if num_componentes > 0:
        for i, comp in enumerate(componentes_l1, start=1):
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
    else:
        # Para CALE teóricos sin componentes L1
        filas_html = """
                        <tr>
                            <td colspan="6" style="text-align: center; padding: 40px; color: #6c757d;">
                                <strong>Esta configuración L2 no incluye componentes L1 de pistas.</strong><br>
                                <span style="font-size: 0.9em;">Corresponde a edificación teórica con componentes L0 directos.</span>
                            </td>
                        </tr>"""
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} - {bim_id} | SNCALE L2</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, {colores['primario']} 0%, {colores['secundario']} 100%);
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
            background: linear-gradient(135deg, {colores['primario']} 0%, {colores['secundario']} 100%);
            color: white;
            padding: 50px;
            position: relative;
        }}
        
        .header-logo {{
            position: absolute;
            top: 25px;
            right: 50px;
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
            font-size: 2.8em;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header .subtitle {{
            font-size: 1.3em;
            opacity: 0.95;
            margin-bottom: 20px;
            font-weight: 500;
        }}
        
        .header .description {{
            font-size: 1.05em;
            opacity: 0.9;
            margin-bottom: 30px;
            line-height: 1.8;
        }}
        
        .badges {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            background: rgba(255,255,255,0.25);
            padding: 12px 28px;
            border-radius: 25px;
            font-size: 1em;
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
            font-size: 2.2em;
            color: {colores['primario']};
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 3px solid {colores['secundario']};
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px;
            border-radius: 12px;
            border-left: 5px solid {colores['primario']};
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .info-card h3 {{
            color: {colores['primario']};
            margin-bottom: 15px;
            font-size: 1.15em;
        }}
        
        .info-card p {{
            color: #495057;
            font-size: 1.4em;
            font-weight: 600;
        }}
        
        .info-card .unit {{
            font-size: 0.85em;
            color: #6c757d;
            font-weight: normal;
        }}
        
        .info-card.destacada {{
            background: linear-gradient(135deg, {colores['primario']} 0%, {colores['secundario']} 100%);
            color: white;
            border-left: 5px solid white;
        }}
        
        .info-card.destacada h3 {{
            color: white;
        }}
        
        .info-card.destacada p {{
            color: white;
        }}
        
        .info-card.destacada .unit {{
            color: rgba(255,255,255,0.9);
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
            background: linear-gradient(135deg, {colores['primario']} 0%, {colores['secundario']} 100%);
            color: white;
        }}
        
        thead th {{
            padding: 20px 15px;
            text-align: left;
            font-weight: 600;
            font-size: 1em;
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
            padding: 18px 15px;
            font-size: 0.95em;
        }}
        
        tbody td code {{
            background: #e9ecef;
            padding: 5px 12px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: {colores['primario']};
        }}
        
        /* Footer */
        .footer {{
            background: #f8f9fa;
            padding: 35px 50px;
            border-top: 1px solid #dee2e6;
        }}
        
        .footer-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 25px;
        }}
        
        .footer-info {{
            color: #6c757d;
            font-size: 0.95em;
        }}
        
        .footer-info strong {{
            color: {colores['primario']};
        }}
        
        .footer-links {{
            display: flex;
            gap: 25px;
        }}
        
        .footer-links a {{
            color: {colores['primario']};
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }}
        
        .footer-links a:hover {{
            color: {colores['secundario']};
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .header {{
                padding: 30px 20px;
            }}
            
            .header h1 {{
                font-size: 2em;
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
                font-size: 1.6em;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
            
            .footer {{
                padding: 25px 20px;
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
                <h1>{bim_id}</h1>
                <div class="subtitle">{titulo}</div>
                <div class="description">{descripcion}</div>
                
                <div class="badges">
                    <span class="badge">Nivel L2 - Configuración Base</span>
                    <span class="badge">{num_componentes} Componentes L1</span>
                    <span class="badge">{categorias}</span>
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
                        <p>{bim_id}</p>
                    </div>
                    
                    <div class="info-card">
                        <h3>Nivel</h3>
                        <p>L2 - Configuración Base</p>
                    </div>
                    
                    <div class="info-card">
                        <h3>Componentes L1</h3>
                        <p>{num_componentes} <span class="unit">ensamblajes</span></p>
                    </div>
                    
                    <div class="info-card destacada">
                        <h3>💰 Valorización Oficial</h3>
                        <p>{valor_formateado} <span class="unit">COP</span></p>
                    </div>
                </div>
            </section>
            
            <!-- Componentes L1 del Ensamblaje -->
            <section class="section">
                <h2 class="section-title">🔧 Componentes L1 Incluidos</h2>
                
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 60px;">#</th>
                                <th style="width: 200px;">Componente</th>
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
                        <strong>Tabla valorización:</strong> #{datos['tabla_numero']} (Elemento índice {datos['elemento_index']})<br>
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
                    Generado desde Google Doc oficial - Nivel L2
                </div>
                
                <div class="footer-links">
                    <a href="../index.html">← Volver al Índice</a>
                    <a href="../fichas_l1/{bim_id.replace('L2', 'L1')}.html">Ver Ensamblaje L1</a>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>"""
    
    return html

def main():
    print("=" * 70)
    print("REGENERACIÓN DE FICHAS L2 - GOOGLE DOC OFICIAL")
    print("=" * 70)
    print()
    
    # 1. Cargar datos L2
    print("📂 Cargando datos L2 oficiales...")
    if not INPUT_FILE.exists():
        print(f"❌ ERROR: No se encuentra {INPUT_FILE}")
        print("   Ejecuta primero: python extraer_tablas_l2_oficial.py")
        return
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        datos_l2 = json.load(f)
    
    tablas = datos_l2['tablas_l2']
    print(f"✅ Cargadas {len(tablas)} configuraciones L2")
    print()
    
    # 2. Generar cada ficha
    print("🔨 Generando fichas HTML...")
    print()
    
    fichas_generadas = []
    
    for nivel, datos in tablas.items():
        bim_id = datos['bim_id']
        titulo = datos['titulo']
        valor = datos['valorización']['valor_cop']
        
        print(f"📄 Generando {bim_id}.html ({titulo})...")
        
        # Generar HTML
        html = generar_html_ficha_l2(nivel, datos)
        
        # Guardar archivo
        output_file = OUTPUT_DIR / f"{bim_id}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        num_componentes = len(datos['componentes_l1'])
        print(f"   💰 Valor: {valor}")
        print(f"   🔧 Componentes L1: {num_componentes}")
        print(f"   💾 Guardado: {output_file}")
        
        fichas_generadas.append({
            'bim_id': bim_id,
            'titulo': titulo,
            'archivo': output_file.name,
            'valor': valor,
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
        print(f"      Valor: {ficha['valor']}")
        print(f"      Componentes L1: {ficha['componentes']}")
        print()
    
    print("=" * 70)
    print("✅ REGENERACIÓN COMPLETADA")
    print("=" * 70)
    print()
    print("SIGUIENTE PASO:")
    print("1. Revisar fichas generadas en:", OUTPUT_DIR.absolute())
    print("2. Proceder con PASO 4: Regenerar fichas L3")
    print()
    
    # URLs de GitHub Pages
    print("🌐 URLs esperadas en GitHub Pages:")
    for ficha in fichas_generadas:
        url = f"https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l2/{ficha['archivo']}"
        print(f"   {url}")
    print()
    
    print("=" * 70)

if __name__ == '__main__':
    main()
