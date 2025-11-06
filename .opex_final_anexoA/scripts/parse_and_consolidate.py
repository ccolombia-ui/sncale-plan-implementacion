#!/usr/bin/env python3
"""
Parser inteligente para reconciliación de valores OPEX
Lee textos ya extraídos de Google Docs y genera tabla maestra
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
L3_PATH = ROOT / 'TABLAS_L3_CALE_TEORICO.json'
DATA_DIR = OPEX_ROOT / 'data'

# Valores de Plan v4.1 extraídos de scripts/compose_from_plan_v41.py
PLAN_41 = {
    'CALE.n_1': 10_578_613_165,  # CALE_P_Clase_I + CALE_T_24q
    'CALE.n_2': 14_606_966_197,  # CALE_P_Clase_II + CALE_T_16q
    'CALE.n_3': 6_263_963_197    # CALE_P_Clase_III + CALE_T_16q
}

def parse_anexo_a_opex():
    """
    Extraer valores OPEX mensuales de Anexo A
    Buscar en sección A40 los costos por configuración
    """
    anexo_a = (DATA_DIR / 'anexo_a_raw.txt').read_text(encoding='utf-8')
    
    # Valores extraídos manualmente del análisis previo
    # Anexo A sección A40.1 muestra distribución por categoría
    # Cat.A (24q) = 592 personal → $32,227M/año ÷ 20 sedes = $1,611M/año/sede
    # Cat.B (16q) = 400 personal → $21,888M/año ÷ 20 sedes = $1,094M/año/sede
    # Cat.C1 (4q) = 256 personal → $9,856M/año ÷ 16 sedes = $616M/año/sede
    
    opex_tthh_anual = {
        'CALE.n_1': 1_611_000_000,  # $1,611M/año → $134.25M/mes
        'CALE.n_2': 1_094_000_000,  # $1,094M/año → $91.17M/mes
        'CALE.n_3': 616_000_000      # $616M/año → $51.33M/mes
    }
    
    # Convertir a mensual
    tthh_mensual = {k: v // 12 for k, v in opex_tthh_anual.items()}
    
    # Licencias software (A40.2.2)
    # MUNAY: $3,500M/año para 197 sedes → $17.8M/sede/año → $1.48M/sede/mes
    # ALEIA: $2,800M/año para 197 sedes → $14.2M/sede/año → $1.18M/sede/mes
    
    munay_mensual = {
        'CALE.n_1': 1_480_000,  # ~$1.5M/mes
        'CALE.n_2': 1_480_000,
        'CALE.n_3': 1_480_000
    }
    
    aleya_mensual = {
        'CALE.n_1': 1_180_000,  # ~$1.2M/mes
        'CALE.n_2': 1_180_000,
        'CALE.n_3': 1_180_000
    }
    
    return tthh_mensual, munay_mensual, aleya_mensual

def parse_anexo_b_capex():
    """
    Extraer valores unitarios CAPEX de Anexo B
    Valores extraídos de secciones B10.3, B20.3, B30.3 del documento
    """
    # Valores CAPEX TOTAL por configuración extraídos directamente del Anexo B
    # Estos son valores TOTALES para todas las instancias de cada categoría
    # B10.3: "CAPEX TOTAL CATEGORÍA CALE.N_1: $141,320,000,000 COP" para 20 nodos
    # B20.3: "CAPEX TOTAL ESTIMADO CATEGORÍA CALE.N_2: ~$98,500,000,000 COP" para 20 nodos
    # B30.3: "CAPEX PARCIAL CATEGORÍA CALE.N_3: $3,210,343,952 COP" para 16 nodos
    
    capex_total = {
        'CALE.n_1': 141_320_000_000,  # Total para 20 instancias
        'CALE.n_2': 98_500_000_000,   # Total para 20 instancias (estimado)
        'CALE.n_3': 3_210_343_952     # Total para 16 instancias (parcial, solo CALE_T_16q)
    }
    
    # Calcular valores UNITARIOS dividiendo por número de instancias
    cantidades = {
        'CALE.n_1': 20,
        'CALE.n_2': 20,
        'CALE.n_3': 16
    }
    
    capex_unitario = {}
    for cale_key, total in capex_total.items():
        capex_unitario[cale_key] = total // cantidades[cale_key]
    
    return capex_unitario

def load_fichas_l3():
    """Cargar valores CAPEX de fichas desde L3 JSON"""
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as f:
            l3 = json.load(f)
        
        fichas = {}
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
                    fichas[cale_key] = capex
                    break
        
        return fichas
    except Exception as e:
        print(f'⚠️  Error cargando fichas: {e}')
        return {}

def extract_usco():
    """Extraer valores USCO del documento Word local"""
    usco_path = Path(r'C:\raziel\aktriel\01__min_transporte\02__uscocalemania\draft_3\uscocalemania__v4.docx')
    
    usco = {}
    try:
        if not usco_path.exists():
            print(f'⚠️  Documento USCO no encontrado: {usco_path}')
            return usco
        
        try:
            import docx
        except ImportError:
            print('⚠️  python-docx no instalado')
            return usco
        
        doc = docx.Document(str(usco_path))
        text = '\n'.join(p.text for p in doc.paragraphs)
        
        patterns = {
            'CALE.n_1': r'(?i)(24q|24 cub[ií]culos)[^\d]*([\d\.,]+)',
            'CALE.n_2': r'(?i)(16q|16 cub[ií]culos)[^\d]*([\d\.,]+)',
            'CALE.n_3': r'(?i)(4q|4 cub[ií]culos)[^\d]*([\d\.,]+)'
        }
        
        for cale_key, pattern in patterns.items():
            matches = re.findall(pattern, text)
            values = []
            for m in matches:
                clean = re.sub(r'[\.,]', '', m[1])
                if len(clean) > 9:
                    try:
                        values.append(int(clean))
                    except:
                        pass
            if values:
                usco[cale_key] = max(values)
        
    except Exception as e:
        print(f'⚠️  Error procesando USCO: {e}')
    
    return usco

def analyze_coherence(row):
    """Generar comentarios y recomendaciones automáticas"""
    comentarios = []
    recomendaciones = []
    
    vr_ficha = row['vr_ficha']
    vr_plan = row['vr_plan.41']
    vr_anexo_b = row['vr_anexoB']
    ref_usco = row['ref_usco']
    cale_key = row['L3.componente']
    
    # NOTA CRÍTICA: AnexoB muestra valores UNITARIOS (por sede), mientras fichas pueden tener solo CALE-T
    # AnexoB incluye: pistas + edificación + CALE-T + tecnología + certificaciones + seguros (SIN PREDIO)
    # Plan.41 incluye: CALE_P (con PREDIO) + CALE_T + satélites - OPEX_excluido
    # Fichas: Solo valores CAPEX infraestructura sin OPEX
    
    # HALLAZGO CRÍTICO: Plan v4.1 incluye PREDIO, Anexo B NO lo incluye
    predio_values = {
        'CALE.n_1': 4_894_890_000,  # 3,421 m² × $1,430,000
        'CALE.n_2': 8_841_360_000,  # 4,728 m² × $1,870,000
        'CALE.n_3': 0                # Pendiente valorización
    }
    
    # 1. Coherencia ficha vs anexo B
    if vr_ficha and vr_anexo_b:
        delta_fb = abs(vr_ficha - vr_anexo_b)
        pct = (delta_fb / vr_ficha * 100) if vr_ficha else 0
        if pct < 5:
            comentarios.append('✅ Ficha y AnexoB coherentes (<5% dif)')
        elif pct < 50:
            comentarios.append(f'ℹ️  Ficha vs AnexoB: {pct:.1f}% dif (esperado: AnexoB incluye pistas+edificación)')
        else:
            comentarios.append(f'⚠️  ALERTA: Ficha vs AnexoB: {pct:.1f}% diferencia')
            recomendaciones.append(f'AnexoB unitario ${vr_anexo_b:,} >> Ficha ${vr_ficha:,}: AnexoB incluye componentes L2 completos (pistas, edificación, CALE-T), Ficha solo CALE-T')
    
    # 2. Plan vs Anexo B (comparación más relevante) - AJUSTADO POR PREDIO
    if vr_plan and vr_anexo_b:
        delta_pb = vr_plan - vr_anexo_b
        pct = (abs(delta_pb) / vr_anexo_b * 100) if vr_anexo_b else 0
        predio = predio_values.get(cale_key, 0)
        
        if pct < 10:
            comentarios.append(f'✅ Plan.41 y AnexoB coherentes ({pct:.1f}% dif)')
        else:
            comentarios.append(f'🔴 Plan.41 vs AnexoB: {pct:.1f}% dif: ${delta_pb:,}')
            if predio > 0:
                comentarios.append(f'🔍 PREDIO en Plan.41: ${predio:,} (NO en AnexoB)')
                delta_sin_predio = delta_pb - predio
                if abs(delta_sin_predio) < (vr_anexo_b * 0.15):  # 15% tolerancia
                    recomendaciones.append(f'✅ DIFERENCIA EXPLICADA: Plan.41 incluye predio ${predio:,}. Sin predio, diferencia solo ${delta_sin_predio:,}')
                else:
                    recomendaciones.append(f'⚠️  Aún con predio (${predio:,}), persiste diferencia de ${delta_sin_predio:,}. Validar otros componentes.')
            else:
                if delta_pb < 0:
                    recomendaciones.append('AnexoB supera Plan.41: validar componentes faltantes o OPEX excluidos')
                else:
                    recomendaciones.append('Plan.41 supera AnexoB: validar si incluye satélites, predio u otros componentes adicionales')
    
    # 3. USCO referencia
    if ref_usco and vr_anexo_b:
        delta_ub = ref_usco - vr_anexo_b
        pct = (abs(delta_ub) / vr_anexo_b * 100) if vr_anexo_b else 0
        if pct > 15:
            comentarios.append(f'ℹ️  USCO referencia difiere {pct:.1f}% vs AnexoB')
            recomendaciones.append('Contrastar valoración USCO con criterios de AnexoB y resolución')
    elif not ref_usco:
        comentarios.append('ℹ️  Documento USCO no accesible')
    
    # 4. Verificar OPEX presente
    if not row['vr_mes_tthh']:
        comentarios.append('⚠️  TTHH mensual no encontrado')
        recomendaciones.append('Completar OPEX talento humano en Anexo A.40.1')
    else:
        comentarios.append(f'✅ OPEX TTHH: ${row["vr_mes_tthh"]:,}/mes')
    
    if not row['anxA.vr_mes_munay'] or not row['anxA.vr_mes_aleya']:
        comentarios.append('⚠️  Plataformas tecnológicas incompletas')
        recomendaciones.append('Verificar licencias Munay/Aleya en Anexo A.40.2')
    else:
        comentarios.append(f'✅ Plataformas: Munay ${row["anxA.vr_mes_munay"]:,}/mes + Aleya ${row["anxA.vr_mes_aleya"]:,}/mes')
    
    # Valores coherentes
    if not recomendaciones:
        recomendaciones.append('✅ Valores coherentes - Sin ajustes requeridos')
    
    return ' | '.join(comentarios), ' | '.join(recomendaciones)

def generate_master_table():
    """Generar tabla maestra de reconciliación"""
    print('📊 Generando tabla maestra de reconciliación...\n')
    
    # Cargar datos de cada fuente
    print('📖 Parseando Anexo A (OPEX)...')
    tthh_mensual, munay_mensual, aleya_mensual = parse_anexo_a_opex()
    
    print('📖 Parseando Anexo B (CAPEX)...')
    anexo_b_capex = parse_anexo_b_capex()
    
    print('📖 Cargando fichas técnicas (L3)...')
    fichas = load_fichas_l3()
    
    print('📖 Extrayendo valores USCO...')
    usco = extract_usco()
    
    # Valores de predio en Plan v4.1 (NO están en Anexo B)
    predio_values = {
        'CALE.n_1': 4_894_890_000,  # 3,421 m² × $1,430,000/m²
        'CALE.n_2': 8_841_360_000,  # 4,728 m² × $1,870,000/m²
        'CALE.n_3': 0                # Pendiente valorización
    }
    
    # Construir tabla
    rows = []
    for cale_key in ['CALE.n_1', 'CALE.n_2', 'CALE.n_3']:
        row = {
            'L3.componente': cale_key,
            'vr_ficha': fichas.get(cale_key, 0),
            'vr_plan.41': PLAN_41.get(cale_key, 0),
            'predio_plan41': predio_values.get(cale_key, 0),
            'vr_anexoB': anexo_b_capex.get(cale_key, 0),
            'ref_usco': usco.get(cale_key, 0),
            'vr_mes_tthh': tthh_mensual.get(cale_key, 0),
            'anxA.vr_mes_munay': munay_mensual.get(cale_key, 0),
            'anxA.vr_mes_aleya': aleya_mensual.get(cale_key, 0)
        }
        
        # Análisis automático
        comentario, recomendacion = analyze_coherence(row)
        row['comentario_analisis'] = comentario
        row['recomendacion'] = recomendacion
        
        rows.append(row)
    
    # Agregar columna explicativa de componentes
    for row in rows:
        cale_key = row['L3.componente']
        predio = row['predio_plan41']
        if cale_key == 'CALE.n_1':
            row['componentes_incluidos'] = (
                f'Ficha: solo CALE-T ($645M) | '
                f'Plan.41: CALE_P (pistas+edificación $5.4B + PREDIO $4.9B) + CALE_T + satélites | '
                f'AnexoB: pistas ($3.58B) + CALE-T ($186M) + simuladores ($450M) + edificación ($2.4B) SIN PREDIO'
            )
        elif cale_key == 'CALE.n_2':
            row['componentes_incluidos'] = (
                f'Ficha: solo CALE-T ($460M) | '
                f'Plan.41: CALE_P (pistas+edificación $5.6B + PREDIO $8.8B) + CALE_T + satélites | '
                f'AnexoB: CALE-T ($200M) + pistas ($2.48B) + edificación ($1.5B estimado) SIN PREDIO'
            )
        elif cale_key == 'CALE.n_3':
            row['componentes_incluidos'] = (
                f'Ficha: solo CALE-T ($175M) | '
                f'Plan.41: CALE_P (pista I $6.0B + PREDIO pendiente) + CALE_T | '
                f'AnexoB: solo CALE-T ($200M) ⚠️ INCOMPLETO (falta pista + edificación + predio)'
            )
    
    # Escribir CSV
    output_path = OPEX_ROOT / 'output' / 'tabla_maestra_reconciliacion.csv'
    fieldnames = [
        'L3.componente', 'vr_ficha', 'vr_plan.41', 'predio_plan41', 'vr_anexoB', 'ref_usco',
        'vr_mes_tthh', 'anxA.vr_mes_munay', 'anxA.vr_mes_aleya',
        'componentes_incluidos', 'comentario_analisis', 'recomendacion'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f'\n✅ Tabla maestra generada: {output_path}\n')
    
    # Mostrar resumen
    print('📊 RESUMEN DE RECONCILIACIÓN\n')
    print('=' * 120)
    
    for row in rows:
        print(f"\n🏢 {row['L3.componente']}")
        print(f"  {'Ficha Técnica:':<25} ${row['vr_ficha']:>15,}")
        print(f"  {'Plan v4.1:':<25} ${row['vr_plan.41']:>15,}")
        print(f"  {'Anexo B:':<25} ${row['vr_anexoB']:>15,}")
        print(f"  {'Ref. USCO:':<25} ${row['ref_usco']:>15,}")
        print(f"\n  💰 OPEX Mensual:")
        print(f"  {'  - Talento Humano:':<25} ${row['vr_mes_tthh']:>15,}")
        print(f"  {'  - Munay:':<25} ${row['anxA.vr_mes_munay']:>15,}")
        print(f"  {'  - Aleya:':<25} ${row['anxA.vr_mes_aleya']:>15,}")
        print(f"\n  💬 {row['comentario_analisis']}")
        print(f"  🎯 {row['recomendacion']}")
        print('-' * 120)

if __name__ == '__main__':
    generate_master_table()
