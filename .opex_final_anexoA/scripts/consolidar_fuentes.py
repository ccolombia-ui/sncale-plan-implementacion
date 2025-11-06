#!/usr/bin/env python3
"""
Consolidador de Fuentes para Reconciliación OPEX
Extrae datos de Google Docs (Anexo A, B, Plan v4.1), USCO local y fichas técnicas
y genera tabla maestra de coherencia.

NO convierte documentos - lee directamente vía API para mantener actualización.
"""
from pathlib import Path
import csv
import json
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Rutas
ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
CREDS_PATH = ROOT.parent / '.secrets' / 'google-service-account.json'
L3_PATH = ROOT / 'TABLAS_L3_CALE_TEORICO.json'
USCO_PATH = Path(r'C:\raziel\aktriel\01__min_transporte\02__uscocalemania\draft_3\uscocalemania__v4.docx')

# IDs de Google Docs (extraídos de las URLs)
DOCS = {
    'anexo_a': '1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4',
    'anexo_b': '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
    'plan_41': '1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg'
}

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def get_docs_service():
    """Inicializar servicio de Google Docs API con credenciales de cuenta de servicio"""
    try:
        creds = service_account.Credentials.from_service_account_file(
            str(CREDS_PATH), scopes=SCOPES
        )
        service = build('docs', 'v1', credentials=creds)
        return service
    except Exception as e:
        print(f'⚠️  Error inicializando Google Docs API: {e}')
        return None

def extract_text_from_doc(service, doc_id):
    """Extraer texto completo de un Google Doc sin convertir"""
    try:
        doc = service.documents().get(documentId=doc_id).execute()
        content = doc.get('body', {}).get('content', [])
        text_parts = []
        
        def extract_paragraph_text(elements):
            for elem in elements:
                if 'paragraph' in elem:
                    for text_run in elem['paragraph'].get('elements', []):
                        if 'textRun' in text_run:
                            text_parts.append(text_run['textRun'].get('content', ''))
                if 'table' in elem:
                    for row in elem['table'].get('tableRows', []):
                        for cell in row.get('tableCells', []):
                            extract_paragraph_text(cell.get('content', []))
        
        extract_paragraph_text(content)
        return ''.join(text_parts)
    except Exception as e:
        print(f'⚠️  Error extrayendo doc {doc_id}: {e}')
        return ''

def parse_anexo_a(text):
    """Extraer valores OPEX mensuales de Anexo A: tthh, munay, aleya por configuración"""
    data = {}
    # Buscar patrones: "24q" o "24 cubículos" seguido de valores monetarios
    # Ejemplo: "CALE 24q: TTHH $16,500,000/mes, Munay $1,500,000/mes, Aleya $2,000,000/mes"
    
    configs = ['24q', '16q', '4q']
    for cfg in configs:
        data[cfg] = {'tthh_mes': 0, 'munay_mes': 0, 'aleya_mes': 0}
        
        # Buscar sección relacionada con la config
        pattern_section = rf'(?i)(cale|configuraci[oó]n).*?{cfg}.*?(?=cale|configuraci[oó]n|$)'
        section_match = re.search(pattern_section, text, re.DOTALL)
        
        if section_match:
            section = section_match.group(0)
            
            # Extraer TTHH/Talento Humano
            tthh_match = re.search(r'(?i)(tthh|talento humano|recursos humanos).*?([\d\.,]+)', section)
            if tthh_match:
                data[cfg]['tthh_mes'] = int(re.sub(r'[\.,]', '', tthh_match.group(2)))
            
            # Extraer Munay
            munay_match = re.search(r'(?i)munay.*?([\d\.,]+)', section)
            if munay_match:
                data[cfg]['munay_mes'] = int(re.sub(r'[\.,]', '', munay_match.group(1)))
            
            # Extraer Aleya
            aleya_match = re.search(r'(?i)aleya.*?([\d\.,]+)', section)
            if aleya_match:
                data[cfg]['aleya_mes'] = int(re.sub(r'[\.,]', '', aleya_match.group(1)))
    
    return data

def parse_anexo_b(text):
    """Extraer valores unitarios de Anexo B por configuración CALE"""
    data = {}
    configs = {
        'CALE.n_1': ['cale.n_1', 'cale n_1', 'cale n1', '24q', '24 cub'],
        'CALE.n_2': ['cale.n_2', 'cale n_2', 'cale n2', '16q', '16 cub'],
        'CALE.n_3': ['cale.n_3', 'cale n_3', 'cale n3', '4q', '4 cub']
    }
    
    for cale_key, keywords in configs.items():
        data[cale_key] = 0
        for kw in keywords:
            pattern = rf'(?i){re.escape(kw)}.*?([\d\.,]+)'
            matches = re.findall(pattern, text)
            if matches:
                # Tomar el valor más grande (probablemente el unitario total)
                values = [int(re.sub(r'[\.,]', '', m)) for m in matches if len(re.sub(r'[\.,]', '', m)) > 6]
                if values:
                    data[cale_key] = max(values)
                    break
    
    return data

def parse_plan_41(text):
    """Extraer valores del Plan v4.1 por configuración CALE"""
    data = {}
    # Similar a anexo_b pero buscando en contexto de Plan v4.1
    configs = {
        'CALE.n_1': ['cale.n_1', 'cale n_1', 'clase i', '24q'],
        'CALE.n_2': ['cale.n_2', 'cale n_2', 'clase ii', '16q'],
        'CALE.n_3': ['cale.n_3', 'cale n_3', 'clase iii', '4q']
    }
    
    for cale_key, keywords in configs.items():
        data[cale_key] = 0
        for kw in keywords:
            pattern = rf'(?i){re.escape(kw)}.*?([\d\.,]+)'
            matches = re.findall(pattern, text)
            if matches:
                values = [int(re.sub(r'[\.,]', '', m)) for m in matches if len(re.sub(r'[\.,]', '', m)) > 9]
                if values:
                    data[cale_key] = max(values)
                    break
    
    return data

def extract_usco_values():
    """Extraer valores USCO del documento Word local"""
    data = {'24q': 0, '16q': 0, '4q': 0}
    try:
        if not USCO_PATH.exists():
            print(f'⚠️  Documento USCO no encontrado: {USCO_PATH}')
            return data
        
        try:
            import docx
        except ImportError:
            print('⚠️  python-docx no instalado. Ejecutar: pip install python-docx')
            return data
        
        doc = docx.Document(str(USCO_PATH))
        text = '\n'.join(p.text for p in doc.paragraphs)
        
        patterns = {
            '24q': r'(?i)(24q|24 cub[ií]culos)[^\d]*([\d\.,]+)',
            '16q': r'(?i)(16q|16 cub[ií]culos)[^\d]*([\d\.,]+)',
            '4q': r'(?i)(4q|4 cub[ií]culos)[^\d]*([\d\.,]+)'
        }
        
        for cfg, pattern in patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                values = [int(re.sub(r'[\.,]', '', m[1])) for m in matches if len(re.sub(r'[\.,]', '', m[1])) > 9]
                if values:
                    data[cfg] = max(values)
        
    except Exception as e:
        print(f'⚠️  Error procesando USCO: {e}')
    
    return data

def load_fichas_from_l3():
    """Cargar valores de fichas desde TABLAS_L3_CALE_TEORICO.json"""
    data = {}
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as f:
            l3 = json.load(f)
        
        comps = l3.get('components') or l3.get('componentes') or {}
        
        mapping = {
            'L3.CALE_TEORICO.24q': 'CALE.n_1',
            'L3.CALE_TEORICO.16q': 'CALE.n_2',
            'L3.CALE_TEORICO.4q': 'CALE.n_3'
        }
        
        for comp in comps.values():
            codigo = comp.get('codigo', '')
            for l3_code, cale_key in mapping.items():
                if l3_code in codigo:
                    capex = comp.get('valor_total_capex', 0)
                    data[cale_key] = capex
                    break
        
    except Exception as e:
        print(f'⚠️  Error cargando fichas L3: {e}')
    
    return data

def generate_master_table():
    """Generar tabla maestra de reconciliación consolidando todas las fuentes"""
    print('📊 Iniciando consolidación de fuentes...\n')
    
    # Inicializar servicio Google Docs
    service = get_docs_service()
    if not service:
        print('❌ No se pudo inicializar Google Docs API. Verifica credenciales.')
        return
    
    # Extraer datos de cada fuente
    print('📖 Extrayendo Anexo A...')
    anexo_a_text = extract_text_from_doc(service, DOCS['anexo_a'])
    anexo_a_data = parse_anexo_a(anexo_a_text)
    
    print('📖 Extrayendo Anexo B...')
    anexo_b_text = extract_text_from_doc(service, DOCS['anexo_b'])
    anexo_b_data = parse_anexo_b(anexo_b_text)
    
    print('📖 Extrayendo Plan v4.1...')
    plan_text = extract_text_from_doc(service, DOCS['plan_41'])
    plan_data = parse_plan_41(plan_text)
    
    print('📖 Extrayendo valores USCO...')
    usco_data = extract_usco_values()
    
    print('📖 Cargando fichas técnicas...')
    fichas_data = load_fichas_from_l3()
    
    # Consolidar en tabla
    rows = []
    configs = [
        ('CALE.n_1', '24q'),
        ('CALE.n_2', '16q'),
        ('CALE.n_3', '4q')
    ]
    
    for cale_key, cfg in configs:
        vr_ficha = fichas_data.get(cale_key, 0)
        vr_plan = plan_data.get(cale_key, 0)
        vr_anexo_b = anexo_b_data.get(cale_key, 0)
        ref_usco = usco_data.get(cfg, 0)
        
        anexo_a_cfg = anexo_a_data.get(cfg, {})
        vr_mes_tthh = anexo_a_cfg.get('tthh_mes', 0)
        vr_mes_munay = anexo_a_cfg.get('munay_mes', 0)
        vr_mes_aleya = anexo_a_cfg.get('aleya_mes', 0)
        
        # Análisis automático
        comentario = []
        recomendacion = []
        
        # Coherencia ficha vs anexo B
        if vr_ficha and vr_anexo_b:
            delta_fb = abs(vr_ficha - vr_anexo_b)
            if delta_fb < vr_ficha * 0.05:  # <5% diferencia
                comentario.append('✅ Ficha y AnexoB coherentes')
            else:
                comentario.append(f'⚠️  Delta Ficha-AnexoB: ${delta_fb:,}')
                recomendacion.append('Revisar diferencia ficha vs anexo B')
        
        # Plan vs ficha
        if vr_plan and vr_ficha:
            delta_pf = vr_plan - vr_ficha
            if abs(delta_pf) > vr_ficha * 0.1:  # >10% diferencia
                comentario.append(f'ℹ️  Plan.41 difiere de ficha: ${delta_pf:,}')
                recomendacion.append('Validar componentes adicionales en Plan.41')
        
        # USCO vs otros
        if ref_usco and vr_ficha:
            delta_uf = ref_usco - vr_ficha
            if abs(delta_uf) > vr_ficha * 0.15:
                comentario.append(f'ℹ️  USCO difiere: ${delta_uf:,}')
                recomendacion.append('Revisar contra resolución de pertinencia')
        
        # Verificar OPEX presente
        if not vr_mes_tthh:
            comentario.append('⚠️  TTHH mensual no encontrado')
            recomendacion.append('Completar OPEX TTHH en Anexo A')
        
        if not vr_mes_munay or not vr_mes_aleya:
            comentario.append('⚠️  Plataformas mensuales incompletas')
            recomendacion.append('Completar valores Munay/Aleya en Anexo A')
        
        rows.append({
            'L3.componente': cale_key,
            'vr_ficha': vr_ficha,
            'vr_plan.41': vr_plan,
            'vr_anexoB': vr_anexo_b,
            'ref_usco': ref_usco,
            'vr_mes_tthh': vr_mes_tthh,
            'anxA.vr_mes_munay': vr_mes_munay,
            'anxA.vr_mes_aleya': vr_mes_aleya,
            'comentario_analisis': ' | '.join(comentario) if comentario else 'Sin observaciones',
            'recomendacion': ' | '.join(recomendacion) if recomendacion else 'Valores coherentes'
        })
    
    # Escribir CSV
    output_path = OPEX_ROOT / 'output' / 'tabla_maestra_reconciliacion.csv'
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'L3.componente', 'vr_ficha', 'vr_plan.41', 'vr_anexoB', 'ref_usco',
            'vr_mes_tthh', 'anxA.vr_mes_munay', 'anxA.vr_mes_aleya',
            'comentario_analisis', 'recomendacion'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f'\n✅ Tabla maestra generada: {output_path}')
    
    # Guardar textos extraídos para referencia
    data_path = OPEX_ROOT / 'data'
    (data_path / 'anexo_a_extracted.txt').write_text(anexo_a_text[:5000], encoding='utf-8')
    (data_path / 'anexo_b_extracted.txt').write_text(anexo_b_text[:5000], encoding='utf-8')
    (data_path / 'plan_41_extracted.txt').write_text(plan_text[:5000], encoding='utf-8')
    
    print(f'📁 Textos extraídos guardados en: {data_path}')
    
    # Mostrar resumen
    print('\n📊 Resumen de Reconciliación:')
    for row in rows:
        print(f"\n{row['L3.componente']}:")
        print(f"  Ficha: ${row['vr_ficha']:,}")
        print(f"  Plan.41: ${row['vr_plan.41']:,}")
        print(f"  AnexoB: ${row['vr_anexoB']:,}")
        print(f"  USCO: ${row['ref_usco']:,}")
        print(f"  TTHH/mes: ${row['vr_mes_tthh']:,}")
        print(f"  Munay/mes: ${row['anxA.vr_mes_munay']:,}")
        print(f"  Aleya/mes: ${row['anxA.vr_mes_aleya']:,}")
        print(f"  💬 {row['comentario_analisis']}")
        print(f"  🎯 {row['recomendacion']}")

if __name__ == '__main__':
    generate_master_table()
