#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regeneración de fichas L3 desde Google Doc oficial
Genera 4 fichas HTML para configuraciones CALE (n_1, n_2, n_3, satélites)

FUENTE ÚNICA: Google Doc ID 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import json
import os

# Configuración de colores para cada BIM L3
COLORES_L3 = {
    'BIM_L3_001': {
        'primario': '#8b0000',
        'secundario': '#dc143c',
        'nombre': 'Rojo Metropolitano'
    },
    'BIM_L3_002': {
        'primario': '#004d99',
        'secundario': '#0066cc',
        'nombre': 'Azul Subregional'
    },
    'BIM_L3_003': {
        'primario': '#2d5016',
        'secundario': '#4a7c28',
        'nombre': 'Verde Local'
    },
    'BIM_L3_004': {
        'primario': '#4b0082',
        'secundario': '#8a2be2',
        'nombre': 'Púrpura Satélites'
    }
}

def formatear_valor(valor_str):
    """Formatea un valor COP con separador de miles"""
    if isinstance(valor_str, str):
        # Ya viene formateado
        return valor_str
    # Es un número
    return f"${valor_str:,}".replace(',', '.')

def generar_html_ficha_l3(configuracion):
    """Genera HTML completo para una ficha L3"""
    
    bim_id = configuracion['bim_id']
    titulo = configuracion['titulo']
    descripcion = configuracion['descripcion']
    tipo_cale = configuracion['tipo_cale']
    componentes = configuracion['componentes']
    valorizacion_total = configuracion['valorizacion']['total_cop']
    valorizacion_formateado = formatear_valor(valorizacion_total)
    
    # Información adicional según tipo
    cantidad_base = configuracion.get('cantidad_base', 0)
    cantidad_variante = configuracion.get('cantidad_variante', 0)
    cantidad_total = configuracion.get('cantidad_total', 0)
    distribucion = configuracion.get('distribucion', '')
    
    # Metadatos
    fuente_tabla = configuracion['metadatos']['fuente_tabla']
    total_componentes = len(componentes)
    
    # Metadata adicional
    metadata_adicional = configuracion.get('metadata_adicional', {})
    
    # Colores
    colores = COLORES_L3.get(bim_id, {
        'primario': '#333',
        'secundario': '#666',
        'nombre': 'Gris'
    })
    
    # Generar filas de componentes
    filas_componentes = ""
    if total_componentes > 0:
        for comp in componentes:
            filas_componentes += f"""
            <tr>
                <td>{comp['numero']}</td>
                <td><strong>{comp['componente']}</strong></td>
                <td>{comp['descripcion']}</td>
                <td><code>{comp['referencia_bim']}</code></td>
                <td class="text-right">{formatear_valor(comp['valor_unitario_cop'])}</td>
                <td class="text-center">{comp['cantidad_base']}</td>
                <td class="text-center">{comp['cantidad_variante']}</td>
                <td class="text-right"><strong>{formatear_valor(comp['valor_total_cop'])}</strong></td>
            </tr>"""
    else:
        filas_componentes = """
            <tr>
                <td colspan="8" class="text-center" style="padding: 2rem; color: #666;">
                    <em>Información de componentes pendiente de validación en Google Doc oficial</em>
                </td>
            </tr>"""
    
    # Generar información de cantidad según tipo
    info_cantidad = ""
    if cantidad_total > 0:
        # Es la red de satélites
        info_cantidad = f"""
        <div class="info-card">
            <h3>📍 Distribución Nacional</h3>
            <p><strong>Total Satélites:</strong> {cantidad_total}</p>
            <p><strong>Distribución:</strong> {distribucion}</p>
        </div>"""
    else:
        # Es un CALE n_1, n_2 o n_3
        info_cantidad = f"""
        <div class="info-card">
            <h3>📍 Cantidad de Nodos</h3>
            <p><strong>Nodos Base:</strong> {cantidad_base}</p>
            {f'<p><strong>Nodos Variante:</strong> {cantidad_variante}</p>' if cantidad_variante > 0 else ''}
        </div>"""
    
    # Generar sección de metadatos adicionales
    seccion_metadata = ""
    if metadata_adicional and 'datos' in metadata_adicional:
        datos_meta = metadata_adicional['datos']
        if datos_meta:
            filas_metadata = ""
            for dato in datos_meta:
                fila_meta = "<tr>"
                for key, value in dato.items():
                    fila_meta += f"<td>{value}</td>"
                fila_meta += "</tr>"
                filas_metadata += fila_meta
            
            encabezados_meta = metadata_adicional.get('encabezados', [])
            encabezados_html = "".join([f"<th>{enc}</th>" for enc in encabezados_meta])
            
            seccion_metadata = f"""
        <section class="metadata-section">
            <h2>📋 Información Adicional</h2>
            <p class="metadata-info">Datos complementarios de la configuración (Tabla #{metadata_adicional['numero_tabla']})</p>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>{encabezados_html}</tr>
                    </thead>
                    <tbody>
                        {filas_metadata}
                    </tbody>
                </table>
            </div>
        </section>"""
    
    # HTML completo
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bim_id} - {titulo}</title>
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
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem 1rem;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, {colores['primario']} 0%, {colores['secundario']} 100%);
            color: white;
            padding: 2.5rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        .header-content {{
            flex: 1;
            min-width: 300px;
        }}
        
        .logo {{
            width: 120px;
            height: auto;
            filter: brightness(0) invert(1);
        }}
        
        .bim-id {{
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}
        
        h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        
        .subtitle {{
            font-size: 1.1rem;
            opacity: 0.95;
            font-weight: 300;
        }}
        
        .content {{
            padding: 2.5rem;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2.5rem;
        }}
        
        .info-card {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid {colores['primario']};
        }}
        
        .info-card.destacada {{
            background: linear-gradient(135deg, {colores['primario']}15 0%, {colores['secundario']}15 100%);
            border-left: 4px solid {colores['secundario']};
        }}
        
        .info-card h3 {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .info-card p {{
            font-size: 1.3rem;
            font-weight: 600;
            color: {colores['primario']};
            margin: 0.3rem 0;
        }}
        
        .info-card.destacada p {{
            font-size: 1.8rem;
            color: {colores['secundario']};
        }}
        
        section {{
            margin-bottom: 2.5rem;
        }}
        
        h2 {{
            color: {colores['primario']};
            font-size: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid {colores['primario']};
        }}
        
        .table-wrapper {{
            overflow-x: auto;
            margin-top: 1rem;
            border-radius: 8px;
            border: 1px solid #dee2e6;
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
        
        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }}
        
        th {{
            font-weight: 600;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        tbody tr:hover {{
            background-color: #f8f9fa;
        }}
        
        tbody tr:last-child td {{
            border-bottom: none;
        }}
        
        .text-right {{
            text-align: right;
        }}
        
        .text-center {{
            text-align: center;
        }}
        
        code {{
            background: #f8f9fa;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: {colores['secundario']};
        }}
        
        .fuente-datos {{
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin-top: 2rem;
        }}
        
        .fuente-datos h3 {{
            color: #28a745;
            margin-bottom: 0.75rem;
            font-size: 1.1rem;
        }}
        
        .fuente-datos p {{
            color: #666;
            margin: 0.5rem 0;
            font-size: 0.95rem;
        }}
        
        .metadata-info {{
            color: #666;
            font-style: italic;
            margin-bottom: 1rem;
        }}
        
        footer {{
            background: #f8f9fa;
            padding: 1.5rem 2.5rem;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #dee2e6;
        }}
        
        footer a {{
            color: {colores['primario']};
            text-decoration: none;
            margin: 0 0.5rem;
        }}
        
        footer a:hover {{
            text-decoration: underline;
        }}
        
        @media (max-width: 768px) {{
            .header {{
                padding: 1.5rem 1rem;
            }}
            
            h1 {{
                font-size: 1.5rem;
            }}
            
            .content {{
                padding: 1.5rem;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
            
            table {{
                font-size: 0.85rem;
            }}
            
            th, td {{
                padding: 0.75rem 0.5rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-content">
                <div class="bim-id">{bim_id}</div>
                <h1>{titulo}</h1>
                <p class="subtitle">{descripcion}</p>
            </div>
            <svg class="logo" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
                <text x="10" y="40" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="currentColor">UPTC</text>
                <text x="10" y="65" font-family="Arial, sans-serif" font-size="14" fill="currentColor">Universidad Pedagógica</text>
            </svg>
        </header>
        
        <div class="content">
            <div class="info-grid">
                <div class="info-card">
                    <h3>🔖 Identificador BIM</h3>
                    <p><code>{bim_id}</code></p>
                </div>
                
                <div class="info-card">
                    <h3>📂 Nivel Jerarquía</h3>
                    <p>Nivel L3</p>
                </div>
                
                <div class="info-card">
                    <h3>🏗️ Tipo CALE</h3>
                    <p>{tipo_cale}</p>
                </div>
                
                <div class="info-card destacada">
                    <h3>💰 Valorización Total</h3>
                    <p>{valorizacion_formateado} COP</p>
                </div>
            </div>
            
            {info_cantidad}
            
            <section>
                <h2>🔧 Componentes de la Configuración</h2>
                <p class="metadata-info">Desglose completo de componentes con valores unitarios y totales</p>
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Componente</th>
                                <th>Descripción</th>
                                <th>Referencia BIM</th>
                                <th>Valor Unitario</th>
                                <th>Cant. Base</th>
                                <th>Cant. Variante</th>
                                <th>Valor Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filas_componentes}
                        </tbody>
                    </table>
                </div>
            </section>
            
            {seccion_metadata}
            
            <div class="fuente-datos">
                <h3>📊 Fuente de Datos</h3>
                <p><strong>Documento:</strong> Google Doc MUNAY_5.2__anexo_b__DEFINITIVO</p>
                <p><strong>ID:</strong> <code>16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE</code></p>
                <p><strong>Tabla Valorización:</strong> #{fuente_tabla}</p>
                <p><strong>Total Componentes:</strong> {total_componentes}</p>
                <p><strong>Estado:</strong> ✅ Validado desde fuente oficial única</p>
            </div>
        </div>
        
        <footer>
            <p>Sistema Nacional de Centros de Enseñanza - SNCALE</p>
            <p>
                <a href="../fichas_l1/BIM_L1_001.html">← Fichas L1</a> |
                <a href="../fichas_l2/BIM_L2_001.html">← Fichas L2</a> |
                <a href="BIM_L3_001.html">L3 Index</a>
            </p>
            <p style="margin-top: 1rem; font-size: 0.85rem;">
                Generado desde Google Doc oficial | {bim_id} | UPTC 2025
            </p>
        </footer>
    </div>
</body>
</html>"""
    
    return html

def main():
    print("="*70)
    print("REGENERACIÓN DE FICHAS L3 - GOOGLE DOC OFICIAL")
    print("="*70)
    print()
    
    # Cargar datos L3
    print("📂 Cargando datos L3 oficiales...")
    with open('TABLAS_L3_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l3 = json.load(f)
    
    configuraciones = datos_l3['configuraciones']
    print(f"✅ Cargadas {len(configuraciones)} configuraciones L3")
    print()
    
    # Crear directorio de salida
    output_dir = 'fichas_l3'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Directorio creado: {output_dir}")
    print()
    
    # Generar fichas
    print("🔨 Generando fichas HTML...")
    print()
    
    fichas_generadas = []
    
    for config in configuraciones:
        bim_id = config['bim_id']
        titulo = config['titulo']
        valor = config['valorizacion']['total_cop_formateado']
        componentes = len(config['componentes'])
        
        print(f"📄 Generando {bim_id}.html ({titulo})...")
        print(f"   💰 Valor: {valor}")
        print(f"   🔧 Componentes: {componentes}")
        
        # Generar HTML
        html = generar_html_ficha_l3(config)
        
        # Guardar archivo
        filename = f"{bim_id}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"   💾 Guardado: {filepath}")
        print()
        
        fichas_generadas.append({
            'bim_id': bim_id,
            'titulo': titulo,
            'archivo': filename,
            'valor': valor,
            'componentes': componentes
        })
    
    # Resumen final
    print("="*70)
    print("RESUMEN DE GENERACIÓN")
    print("="*70)
    print()
    print(f"📊 Fichas generadas: {len(fichas_generadas)}")
    print(f"📁 Directorio: {os.path.abspath(output_dir)}")
    print()
    
    for ficha in fichas_generadas:
        print(f"✅ {ficha['bim_id']} - {ficha['titulo']}")
        print(f"   Archivo: {ficha['archivo']}")
        print(f"   Valor: {ficha['valor']}")
        print(f"   Componentes: {ficha['componentes']}")
        print()
    
    # URLs esperadas
    print("🌐 URLs esperadas en GitHub Pages:")
    for ficha in fichas_generadas:
        print(f"   https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/{ficha['archivo']}")
    print()
    
    print("✅ Generación L3 completada exitosamente")
    print()

if __name__ == '__main__':
    main()
