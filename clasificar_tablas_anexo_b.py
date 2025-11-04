#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLASIFICAR TABLAS DEL ANEXO B OFICIAL POR NIVEL BIM
Identifica y clasifica las 89 tablas en L0, L1, L2, L3
Fuente única de verdad: https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
CREDENTIALS_FILE = r'C:\guezarel\.secret\credentials_google.json'
DOC_ID = '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE'

def extraer_texto_celda(cell):
    """Extrae texto de una celda de tabla"""
    texto = ''
    for content_elem in cell.get('content', []):
        if 'paragraph' in content_elem:
            for para_elem in content_elem['paragraph'].get('elements', []):
                if 'textRun' in para_elem:
                    texto += para_elem['textRun'].get('content', '')
    return texto.strip()

def clasificar_tabla(tabla_info):
    """Clasifica una tabla según su contenido"""
    encabezados = ' '.join(tabla_info.get('encabezados', [])).lower()
    ejemplo = ' '.join(tabla_info.get('ejemplo_fila2', [])).lower()
    
    # Detección de nivel BIM
    if 'l2.pista' in ejemplo or 'l2.cale' in ejemplo or 'l2.' in ejemplo:
        return 'L3 - Especialización CALE'
    elif 'l1.' in ejemplo or 'ensamblaje' in encabezados:
        return 'L2 - Configuración Base'
    elif 'bim_l0_' in ejemplo or 'componente atómico' in encabezados:
        return 'L1 - Ensamblaje'
    elif 'cale.n_' in ejemplo:
        if 'componente' in encabezados and 'vr' in encabezados:
            return 'L3 - Especialización CALE'
        else:
            return 'L3 - Metadatos'
    else:
        return 'Otra/Administrativa'

def main():
    print("\n" + "="*80)
    print("  CLASIFICACIÓN DE TABLAS - ANEXO B OFICIAL")
    print("="*80)
    print(f"\nDocumento ID: {DOC_ID}")
    
    # Autenticar
    print("\n📋 Conectando a Google Docs API...")
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    docs_service = build('docs', 'v1', credentials=creds)
    
    # Leer documento
    print("📖 Leyendo documento completo...")
    document = docs_service.documents().get(documentId=DOC_ID).execute()
    
    print(f"✅ Documento: {document.get('title')}")
    
    # Extraer tablas
    content = document.get('body', {}).get('content', [])
    print(f"\n📊 Analizando {len(content)} elementos...")
    
    tablas_clasificadas = {
        'L0 - Componentes Atómicos': [],
        'L1 - Ensamblaje': [],
        'L2 - Configuración Base': [],
        'L3 - Especialización CALE': [],
        'L3 - Metadatos': [],
        'Otra/Administrativa': []
    }
    
    tabla_count = 0
    
    for i, element in enumerate(content):
        if 'table' in element:
            tabla_count += 1
            rows = element['table'].get('tableRows', [])
            
            tabla_info = {
                'numero': tabla_count,
                'elemento_index': i,
                'filas': len(rows),
                'columnas': 0,
                'encabezados': [],
                'ejemplo_fila2': [],
                'todas_filas': []
            }
            
            # Extraer todas las filas
            for row_idx, row in enumerate(rows):
                cells = row.get('tableCells', [])
                fila_textos = [extraer_texto_celda(cell) for cell in cells]
                tabla_info['todas_filas'].append(fila_textos)
                
                if row_idx == 0:
                    tabla_info['columnas'] = len(fila_textos)
                    tabla_info['encabezados'] = fila_textos
                elif row_idx == 1:
                    tabla_info['ejemplo_fila2'] = [t[:100] for t in fila_textos]
            
            # Clasificar
            categoria = clasificar_tabla(tabla_info)
            tablas_clasificadas[categoria].append(tabla_info)
    
    print(f"\n✅ Total tablas procesadas: {tabla_count}")
    
    # Mostrar resumen
    print("\n" + "="*80)
    print("  RESUMEN POR CATEGORÍA")
    print("="*80)
    
    for categoria, tablas in sorted(tablas_clasificadas.items()):
        if tablas:
            print(f"\n📊 {categoria}: {len(tablas)} tablas")
            for tabla in tablas[:3]:  # Primeras 3
                print(f"   • Tabla #{tabla['numero']}: {tabla['filas']} filas × {tabla['columnas']} cols")
                print(f"     Encabezados: {', '.join(tabla['encabezados'][:4])}...")
    
    # Guardar resultado detallado
    output_file = 'clasificacion_tablas_anexo_b.json'
    resultado = {
        'documento_id': DOC_ID,
        'titulo': document.get('title'),
        'total_tablas': tabla_count,
        'clasificacion': {k: len(v) for k, v in tablas_clasificadas.items()},
        'tablas': tablas_clasificadas
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Análisis completo guardado: {output_file}")
    
    # Análisis específico de tablas L1, L2, L3
    print("\n" + "="*80)
    print("  ANÁLISIS DETALLADO - TABLAS L1, L2, L3")
    print("="*80)
    
    for nivel in ['L1 - Ensamblaje', 'L2 - Configuración Base', 'L3 - Especialización CALE']:
        tablas_nivel = tablas_clasificadas.get(nivel, [])
        if tablas_nivel:
            print(f"\n🔍 {nivel} ({len(tablas_nivel)} tablas)")
            print("-" * 80)
            for tabla in tablas_nivel:
                print(f"\n📋 Tabla #{tabla['numero']} - Elemento {tabla['elemento_index']}")
                print(f"   Dimensiones: {tabla['filas']} filas × {tabla['columnas']} columnas")
                print(f"   Encabezados: {tabla['encabezados']}")
                if tabla['ejemplo_fila2']:
                    print(f"   Ejemplo fila 2: {tabla['ejemplo_fila2'][:2]}")
    
    print("\n" + "="*80)
    print("  ✅ CLASIFICACIÓN COMPLETADA")
    print("="*80)
    
    return resultado

if __name__ == '__main__':
    try:
        resultado = main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
