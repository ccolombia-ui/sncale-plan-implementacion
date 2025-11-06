#!/usr/bin/env python3
"""
Reconciliación sobre la Red Nacional completa
Estructura: CALE-T (Teórico) + CALE-P (Práctico) = Total por categoría
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
L3_PATH = ROOT / 'TABLAS_L3_CALE_TEORICO.json'
DATA_DIR = OPEX_ROOT / 'data'
OUTPUT_DIR = OPEX_ROOT / 'output'

# ============================================================================
# DATOS OFICIALES ANEXO B - Tabla resumen nacional (Sección B10.3)
# ============================================================================
ANEXO_B_RED_NACIONAL = [
    {
        'categoria': 'CALE.n_1+',
        'cantidad': 3,
        'comp_teorico': 'CALE-T-24q + 7 satélites C2-C5',
        'comp_practico': 'CALE-P.C3 (Clase I+II+III) & (Clase II)',
        'vr_unit_teorico': 243_063_465,
        'vr_unit_practico': 22_633_895_800,
        'vr_unit_inversion': 22_876_959_265,
        'vr_total': 68_630_877_795,
        'pct_total': 8.06
    },
    {
        'categoria': 'CALE.n_1',
        'cantidad': 17,
        'comp_teorico': 'CALE-T-24q + 7 satélites C2-C5',
        'comp_practico': 'CALE-P.C3 (Clase I+II+III)',
        'vr_unit_teorico': 243_063_465,
        'vr_unit_practico': 17_068_936_100,
        'vr_unit_inversion': 17_311_999_565,
        'vr_total': 294_303_992_605,
        'pct_total': 34.57
    },
    {
        'categoria': 'CALE.n_2**',
        'cantidad': 16,
        'comp_teorico': 'CALE-T-16q',
        'comp_practico': 'CALE-P.C2 (Clase I+II) & 2x(Clase I)',
        'vr_unit_teorico': 200_646_497,
        'vr_unit_practico': 21_886_938_800,
        'vr_unit_inversion': 22_087_585_297,
        'vr_total': 353_401_364_752,
        'pct_total': 41.51
    },
    {
        'categoria': 'CALE.n_2',
        'cantidad': 4,
        'comp_teorico': 'CALE-T-16q',
        'comp_practico': 'CALE-P.C2 (Clase I+II)',
        'vr_unit_teorico': 200_646_497,
        'vr_unit_practico': 11_005_619_400,
        'vr_unit_inversion': 11_206_265_897,
        'vr_total': 44_825_063_588,
        'pct_total': 5.26
    },
    {
        'categoria': 'CALE.n_3',
        'cantidad': 16,
        'comp_teorico': 'CALE-T-16q',
        'comp_practico': 'CALE-P.C1 (Clase I)',
        'vr_unit_teorico': 200_646_497,
        'vr_unit_practico': 5_440_659_700,
        'vr_unit_inversion': 5_641_306_197,
        'vr_total': 90_260_899_152,
        'pct_total': 10.60
    }
]

TOTAL_INVERSION_ANEXO_B = 851_422_197_892

# ============================================================================
# DATOS PLAN V4.1 - Valores extraídos de sección 7.2
# ============================================================================
PLAN_41_VALORES = {
    'CALE_P_Clase_I_total': 10_335_549_700,   # Incluye predio $4,894,890,000
    'CALE_P_Clase_II_total': 14_406_319_700,  # Incluye predio $8,841,360,000
    'CALE_P_Clase_III_total': 6_063_316_700,  # Sin predio valorizado
    'CALE_T_24q': 243_063_465,
    'CALE_T_16q': 200_646_497,
    'satelites_7_unidades': 84_000_000,  # 7 × $12M
    'predio_clase_I': 4_894_890_000,     # 3,421 m² × $1,430,000/m²
    'predio_clase_II': 8_841_360_000,    # 4,728 m² × $1,870,000/m²
    'predio_clase_III': 0                # Pendiente valorización
}

# ============================================================================
# DATOS FICHAS L3 - Valores CALE-T únicamente
# ============================================================================
def load_fichas_cale_t():
    """Cargar valores CALE-T de fichas técnicas (solo componente teórico)"""
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as f:
            l3 = json.load(f)
        
        fichas = {}
        comps = l3.get('components') or l3.get('componentes') or {}
        
        for comp_key, comp in comps.items():
            codigo = comp.get('codigo', '')
            capex = comp.get('valor_total_capex', 0)
            
            if 'BIM_L3_010' in codigo or '24q' in codigo.lower():
                fichas['CALE-T-24q'] = capex
            elif 'BIM_L3_011' in codigo or '16q' in codigo.lower():
                fichas['CALE-T-16q'] = capex
            elif 'BIM_L3_012' in codigo or '4q' in codigo.lower():
                fichas['CALE-T-4q'] = capex
        
        return fichas
    except Exception as e:
        print(f'⚠️  Error cargando fichas: {e}')
        return {
            'CALE-T-24q': 645_000_000,
            'CALE-T-16q': 460_000_000,
            'CALE-T-4q': 175_000_000
        }

# ============================================================================
# FUNCIÓN PRINCIPAL: GENERAR TABLA DE RECONCILIACIÓN
# ============================================================================
def generar_tabla_reconciliacion():
    """
    Genera tabla comparando:
    - AnexoB: Valores oficiales (CALE-T + CALE-P separados)
    - Plan v4.1: Cálculo alternativo con predio
    - Fichas L3: Solo valores CALE-T
    """
    print('🔄 Generando tabla de reconciliación sobre red nacional...\n')
    
    fichas = load_fichas_cale_t()
    
    rows = []
    
    for item in ANEXO_B_RED_NACIONAL:
        cat = item['categoria']
        
        # Mapear categoría a ficha correspondiente
        if '24q' in item['comp_teorico']:
            ficha_teorico = fichas.get('CALE-T-24q', 0)
        elif '16q' in item['comp_teorico']:
            ficha_teorico = fichas.get('CALE-T-16q', 0)
        elif '4q' in item['comp_teorico']:
            ficha_teorico = fichas.get('CALE-T-4q', 0)
        else:
            ficha_teorico = 0
        
        # Calcular valor Plan v4.1 según configuración
        # CALE.n_1+ y CALE.n_1 usan misma base
        if cat in ['CALE.n_1+', 'CALE.n_1']:
            plan_teorico = PLAN_41_VALORES['CALE_T_24q'] + PLAN_41_VALORES['satelites_7_unidades']
            # CALE-P.C3 = Clase I+II+III (todas las pistas)
            plan_practico = (
                PLAN_41_VALORES['CALE_P_Clase_I_total'] +
                PLAN_41_VALORES['CALE_P_Clase_II_total'] +
                PLAN_41_VALORES['CALE_P_Clase_III_total']
            )
            predio_total = (
                PLAN_41_VALORES['predio_clase_I'] +
                PLAN_41_VALORES['predio_clase_II'] +
                PLAN_41_VALORES['predio_clase_III']
            )
            
            if cat == 'CALE.n_1+':
                # Incluye CALE.n_2 adicional (Clase II extra)
                plan_practico += PLAN_41_VALORES['CALE_P_Clase_II_total']
                predio_total += PLAN_41_VALORES['predio_clase_II']
        
        elif cat in ['CALE.n_2**', 'CALE.n_2']:
            plan_teorico = PLAN_41_VALORES['CALE_T_16q']
            # CALE-P.C2 = Clase I+II
            plan_practico = (
                PLAN_41_VALORES['CALE_P_Clase_I_total'] +
                PLAN_41_VALORES['CALE_P_Clase_II_total']
            )
            predio_total = (
                PLAN_41_VALORES['predio_clase_I'] +
                PLAN_41_VALORES['predio_clase_II']
            )
            
            if cat == 'CALE.n_2**':
                # Incluye 2× Clase I adicional
                plan_practico += 2 * PLAN_41_VALORES['CALE_P_Clase_I_total']
                predio_total += 2 * PLAN_41_VALORES['predio_clase_I']
        
        elif cat == 'CALE.n_3':
            plan_teorico = PLAN_41_VALORES['CALE_T_16q']
            # CALE-P.C1 = Solo Clase I
            plan_practico = PLAN_41_VALORES['CALE_P_Clase_I_total']
            predio_total = PLAN_41_VALORES['predio_clase_I']
        
        plan_unit_total = plan_teorico + plan_practico
        plan_total_nacional = plan_unit_total * item['cantidad']
        
        # Análisis de diferencias
        delta_teorico_abs = item['vr_unit_teorico'] - ficha_teorico
        delta_teorico_pct = (delta_teorico_abs / ficha_teorico * 100) if ficha_teorico else 0
        
        delta_practico_abs = item['vr_unit_practico'] - plan_practico
        delta_practico_pct = (delta_practico_abs / plan_practico * 100) if plan_practico else 0
        
        delta_total_abs = item['vr_total'] - plan_total_nacional
        delta_total_pct = (delta_total_abs / plan_total_nacional * 100) if plan_total_nacional else 0
        
        # Generar comentarios
        comentarios = []
        recomendaciones = []
        
        # Análisis componente teórico
        if abs(delta_teorico_pct) < 5:
            comentarios.append(f'✅ Teórico coherente: Ficha vs AnexoB <5% dif')
        elif abs(delta_teorico_pct) < 100:
            comentarios.append(f'⚠️  Teórico: AnexoB ${item["vr_unit_teorico"]:,} vs Ficha ${ficha_teorico:,} ({delta_teorico_pct:+.1f}%)')
        else:
            comentarios.append(f'🔴 Teórico: Gran diferencia {delta_teorico_pct:+.1f}%')
            recomendaciones.append(f'Validar por qué AnexoB teórico ({item["vr_unit_teorico"]:,}) difiere de Ficha ({ficha_teorico:,})')
        
        # Análisis componente práctico
        if predio_total > 0:
            practico_sin_predio = plan_practico - predio_total
            delta_ajustado = item['vr_unit_practico'] - practico_sin_predio
            pct_ajustado = (delta_ajustado / practico_sin_predio * 100) if practico_sin_predio else 0
            
            comentarios.append(f'🔍 Plan.41 práctico incluye PREDIO: ${predio_total:,}')
            
            if abs(pct_ajustado) < 15:
                comentarios.append(f'✅ Práctico coherente sin predio (<15% dif)')
                recomendaciones.append(f'✅ DIFERENCIA EXPLICADA: Predio ${predio_total:,} explica delta. Sin predio: {pct_ajustado:+.1f}% dif')
            else:
                comentarios.append(f'⚠️  Aún sin predio, persiste {pct_ajustado:+.1f}% diferencia')
                recomendaciones.append(f'⚠️  Revisar: Aún restando predio (${predio_total:,}), queda ${delta_ajustado:,} diferencia')
        else:
            if abs(delta_practico_pct) < 10:
                comentarios.append(f'✅ Práctico coherente: AnexoB vs Plan.41 <10% dif')
            else:
                comentarios.append(f'🔴 Práctico: AnexoB ${item["vr_unit_practico"]:,} vs Plan.41 ${plan_practico:,} ({delta_practico_pct:+.1f}%)')
                recomendaciones.append(f'Analizar componentes: AnexoB práctico difiere ${delta_practico_abs:,} de Plan.41')
        
        # Análisis total nacional
        if abs(delta_total_pct) < 10:
            comentarios.append(f'✅ Total nacional coherente (<10% dif)')
        else:
            comentarios.append(f'📊 Total nacional: AnexoB ${item["vr_total"]:,} vs Plan.41 ${plan_total_nacional:,} ({delta_total_pct:+.1f}%)')
        
        row = {
            'categoria': cat,
            'cantidad': item['cantidad'],
            'comp_teorico': item['comp_teorico'],
            'comp_practico': item['comp_practico'],
            # Valores AnexoB (oficial)
            'anexoB_vr_unit_teorico': item['vr_unit_teorico'],
            'anexoB_vr_unit_practico': item['vr_unit_practico'],
            'anexoB_vr_unit_total': item['vr_unit_inversion'],
            'anexoB_vr_total_nacional': item['vr_total'],
            'anexoB_pct_total': item['pct_total'],
            # Valores Ficha L3 (solo teórico)
            'ficha_vr_teorico': ficha_teorico,
            # Valores Plan v4.1 (con predio)
            'plan41_vr_unit_teorico': plan_teorico,
            'plan41_vr_unit_practico': plan_practico,
            'plan41_predio_incluido': predio_total,
            'plan41_vr_unit_total': plan_unit_total,
            'plan41_vr_total_nacional': plan_total_nacional,
            # Deltas
            'delta_teorico_ficha_anexoB': delta_teorico_abs,
            'delta_practico_plan_anexoB': delta_practico_abs,
            'delta_total_nacional': delta_total_abs,
            # Análisis
            'comentarios': ' | '.join(comentarios),
            'recomendaciones': ' | '.join(recomendaciones) if recomendaciones else '✅ Valores coherentes'
        }
        
        rows.append(row)
    
    # Escribir CSV
    output_path = OUTPUT_DIR / 'reconciliacion_red_nacional.csv'
    fieldnames = [
        'categoria', 'cantidad', 'comp_teorico', 'comp_practico',
        'anexoB_vr_unit_teorico', 'anexoB_vr_unit_practico', 'anexoB_vr_unit_total',
        'anexoB_vr_total_nacional', 'anexoB_pct_total',
        'ficha_vr_teorico',
        'plan41_vr_unit_teorico', 'plan41_vr_unit_practico', 'plan41_predio_incluido',
        'plan41_vr_unit_total', 'plan41_vr_total_nacional',
        'delta_teorico_ficha_anexoB', 'delta_practico_plan_anexoB', 'delta_total_nacional',
        'comentarios', 'recomendaciones'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f'✅ Tabla generada: {output_path}\n')
    
    # Resumen en consola
    print('=' * 120)
    print('📊 RECONCILIACIÓN RED NACIONAL - RESUMEN')
    print('=' * 120)
    
    for row in rows:
        print(f"\n🏢 {row['categoria']} ({row['cantidad']} nodos)")
        print(f"   Componente Teórico:  {row['comp_teorico']}")
        print(f"   Componente Práctico: {row['comp_practico']}")
        print(f"\n   📊 ANEXO B (OFICIAL):")
        print(f"      Teórico:   ${row['anexoB_vr_unit_teorico']:>15,}")
        print(f"      Práctico:  ${row['anexoB_vr_unit_practico']:>15,}")
        print(f"      UNITARIO:  ${row['anexoB_vr_unit_total']:>15,}")
        print(f"      NACIONAL:  ${row['anexoB_vr_total_nacional']:>15,} ({row['anexoB_pct_total']:.2f}%)")
        print(f"\n   📋 FICHA L3:")
        print(f"      Teórico:   ${row['ficha_vr_teorico']:>15,}")
        print(f"\n   📄 PLAN v4.1:")
        print(f"      Teórico:   ${row['plan41_vr_unit_teorico']:>15,}")
        print(f"      Práctico:  ${row['plan41_vr_unit_practico']:>15,}")
        if row['plan41_predio_incluido'] > 0:
            print(f"      🔴 PREDIO:  ${row['plan41_predio_incluido']:>15,}")
        print(f"      UNITARIO:  ${row['plan41_vr_unit_total']:>15,}")
        print(f"      NACIONAL:  ${row['plan41_vr_total_nacional']:>15,}")
        print(f"\n   💬 {row['comentarios']}")
        print(f"   🎯 {row['recomendaciones']}")
        print('-' * 120)
    
    print(f"\n{'=' * 120}")
    print(f"💰 TOTAL INVERSIÓN ANEXO B: ${TOTAL_INVERSION_ANEXO_B:,}")
    total_plan41 = sum(r['plan41_vr_total_nacional'] for r in rows)
    print(f"💰 TOTAL INVERSIÓN PLAN v4.1: ${total_plan41:,}")
    delta_total = TOTAL_INVERSION_ANEXO_B - total_plan41
    pct_total = (delta_total / total_plan41 * 100) if total_plan41 else 0
    print(f"📊 DIFERENCIA: ${delta_total:+,} ({pct_total:+.2f}%)")
    print('=' * 120)

if __name__ == '__main__':
    generar_tabla_reconciliacion()
