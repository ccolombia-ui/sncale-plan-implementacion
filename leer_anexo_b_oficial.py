#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LECTOR DE ANEXO B OFICIAL - GOOGLE DOC
Extrae estructura completa de tablas L1, L2, L3 desde el Google Doc oficial
Fuente única de verdad: https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Configuración
DOCUMENT_ID = '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE'
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
CREDENTIALS_FILE = r'C:\guezarel\.secret\credentials_google.json'

def extraer_texto_tabla(tabla):
    """Extrae contenido de una tabla como texto estructurado"""
    filas = []
    for row in tabla.get('tableRows', []):
        celdas = []
        for cell in row.get('tableCells', []):
            texto_celda = ''
            for elemento in cell.get('content', []):
                if 'paragraph' in elemento:
                    for elem in elemento['paragraph'].get('elements', []):
                        if 'textRun' in elem:
                            texto_celda += elem['textRun'].get('content', '')
            celdas.append(texto_celda.strip())
        filas.append(celdas)
    return filas

def analizar_documento():
    """Lee y analiza el documento completo"""
    print("\n" + "="*80)
    print("  ANÁLISIS DE ANEXO B OFICIAL - GOOGLE DOC")
    print("="*80)
    print(f"\nDocumento ID: {DOCUMENT_ID}")
    print("URL: https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE")
    
    # Autenticar
    print("\n📋 Autenticando con Google Docs API...")
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    service = build('docs', 'v1', credentials=creds)
    
    # Leer documento
    print("📖 Leyendo documento completo...")
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    print(f"✅ Documento leído: {document.get('title')}")
    
    # Analizar pestañas
    tabs = document.get('tabs', [])
    print(f"\n📑 Total de pestañas: {len(tabs)}")
    
    resultado = {
        'titulo': document.get('title'),
        'document_id': DOCUMENT_ID,
        'total_tabs': len(tabs),
        'tabs': []
    }
    
    # Procesar cada pestaña
    for idx, tab in enumerate(tabs):
        tab_properties = tab.get('tabProperties', {})
        tab_title = tab_properties.get('title', f'Pestaña {idx+1}')
        
        print(f"\n{'='*60}")
        print(f"📂 Pestaña {idx+1}: {tab_title}")
        print("="*60)
        
        tab_data = {
            'index': idx + 1,
            'title': tab_title,
            'tabId': tab_properties.get('tabId', ''),
            'tablas': [],
            'secciones': []
        }
        
        # Procesar contenido de la pestaña
        content = tab.get('documentTab', {}).get('body', {}).get('content', [])
        
        tabla_count = 0
        seccion_actual = None
        
        for element in content:
            # Detectar tablas
            if 'table' in element:
                tabla_count += 1
                tabla_contenido = extraer_texto_tabla(element['table'])
                
                # Intentar identificar el tipo de tabla
                tipo_tabla = 'Desconocida'
                if tabla_contenido and len(tabla_contenido) > 0:
                    primera_fila = ' '.join(tabla_contenido[0]).lower()
                    
                    if 'l0' in primera_fila or 'componente atómico' in primera_fila:
                        tipo_tabla = 'L0 - Componentes Atómicos'
                    elif 'l1' in primera_fila or 'ensamblaje' in primera_fila:
                        tipo_tabla = 'L1 - Ensamblajes'
                    elif 'l2' in primera_fila or 'configuración' in primera_fila:
                        tipo_tabla = 'L2 - Configuraciones Base'
                    elif 'l3' in primera_fila or 'cale.n' in primera_fila:
                        tipo_tabla = 'L3 - Especialización CALE'
                    elif 'componente' in primera_fila and 'valor' in primera_fila:
                        tipo_tabla = 'Valorización'
                
                print(f"  📊 Tabla {tabla_count}: {tipo_tabla} ({len(tabla_contenido)} filas)")
                
                tab_data['tablas'].append({
                    'numero': tabla_count,
                    'tipo': tipo_tabla,
                    'filas': len(tabla_contenido),
                    'columnas': len(tabla_contenido[0]) if tabla_contenido else 0,
                    'contenido': tabla_contenido[:5]  # Primeras 5 filas como muestra
                })
            
            # Detectar encabezados/secciones
            elif 'paragraph' in element:
                para = element['paragraph']
                estilo = para.get('paragraphStyle', {}).get('namedStyleType', '')
                
                if estilo in ['HEADING_1', 'HEADING_2', 'HEADING_3']:
                    texto_seccion = ''
                    for elem in para.get('elements', []):
                        if 'textRun' in elem:
                            texto_seccion += elem['textRun'].get('content', '')
                    
                    seccion_actual = texto_seccion.strip()
                    if seccion_actual:
                        print(f"  📌 Sección: {seccion_actual}")
                        tab_data['secciones'].append(seccion_actual)
        
        resultado['tabs'].append(tab_data)
        print(f"\n  ✅ Total tablas en pestaña: {tabla_count}")
    
    # Guardar resultado
    output_file = 'analisis_anexo_b_oficial.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*80)
    print("  ✅ ANÁLISIS COMPLETADO")
    print("="*80)
    print(f"\n📁 Resultado guardado en: {output_file}")
    
    # Resumen por tipo de tabla
    print("\n📊 RESUMEN POR TIPO DE TABLA:")
    tipos_contador = {}
    for tab in resultado['tabs']:
        for tabla in tab['tablas']:
            tipo = tabla['tipo']
            tipos_contador[tipo] = tipos_contador.get(tipo, 0) + 1
    
    for tipo, count in sorted(tipos_contador.items()):
        print(f"  • {tipo}: {count} tablas")
    
    print(f"\n📑 Total pestañas: {resultado['total_tabs']}")
    print(f"📊 Total tablas: {sum(len(tab['tablas']) for tab in resultado['tabs'])}")
    
    return resultado

if __name__ == '__main__':
    try:
        resultado = analizar_documento()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
