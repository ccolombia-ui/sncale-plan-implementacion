#!/usr/bin/env python3
"""
Version simplificada - Extractor de Google Docs
Lee directamente sin convertir
"""
from pathlib import Path
import json

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    HAS_GOOGLE_API = True
except ImportError:
    HAS_GOOGLE_API = False
    print('⚠️  Google API no disponible. Instalar: pip install google-api-python-client google-auth')

ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
CREDS_PATH = ROOT.parent / '.secrets' / 'google-service-account.json'

DOCS = {
    'anexo_a': '1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4',
    'anexo_b': '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
    'plan_41': '1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg'
}

def extract_doc(doc_id, doc_name):
    """Extraer texto de un Google Doc"""
    if not HAS_GOOGLE_API:
        return None
    
    try:
        print(f'📖 Conectando a {doc_name}...')
        creds = service_account.Credentials.from_service_account_file(
            str(CREDS_PATH),
            scopes=['https://www.googleapis.com/auth/documents.readonly']
        )
        service = build('docs', 'v1', credentials=creds)
        
        print(f'📥 Descargando {doc_name}...')
        doc = service.documents().get(documentId=doc_id).execute()
        
        print(f'📄 Extrayendo texto de {doc_name}...')
        content = doc.get('body', {}).get('content', [])
        text_parts = []
        
        def extract_text(elements):
            for elem in elements:
                if 'paragraph' in elem:
                    for tr in elem['paragraph'].get('elements', []):
                        if 'textRun' in tr:
                            text_parts.append(tr['textRun'].get('content', ''))
                if 'table' in elem:
                    for row in elem['table'].get('tableRows', []):
                        for cell in row.get('tableCells', []):
                            extract_text(cell.get('content', []))
        
        extract_text(content)
        full_text = ''.join(text_parts)
        
        # Guardar
        output_file = OPEX_ROOT / 'data' / f'{doc_name}_raw.txt'
        output_file.write_text(full_text, encoding='utf-8')
        print(f'✅ {doc_name} guardado: {output_file} ({len(full_text)} caracteres)')
        
        return full_text
        
    except Exception as e:
        print(f'❌ Error en {doc_name}: {e}')
        import traceback
        traceback.print_exc()
        return None

def main():
    print('🚀 Iniciando extracción de Google Docs\n')
    
    for key, doc_id in DOCS.items():
        text = extract_doc(doc_id, key)
        if text:
            print(f'   Primeras 200 chars: {text[:200]}\n')
    
    print('✅ Extracción completada')

if __name__ == '__main__':
    main()
