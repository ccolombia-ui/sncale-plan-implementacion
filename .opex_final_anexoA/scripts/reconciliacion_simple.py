#!/usr/bin/env python3
"""
Tabla de reconciliación SIMPLIFICADA
Compara valores Anexo B (oficial) con Fichas actuales
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
OUTPUT_DIR = OPEX_ROOT / 'output'

# Valores ANEXO B (OFICIAL - Fuente única de verdad)
ANEXO_B_OFICIAL = [
    {
        'categoria': 'CALE.n_1+',
        'cantidad': 3,
        'anexoB_teorico': 243_063_465,
        'anexoB_practico': 22_633_895_800,
        'anexoB_unitario': 22_876_959_265,
        'anexoB_total_nacional': 68_630_877_795,
        'ficha_actual_teorico': 645_000_000,  # De fichas L3 publicadas
        'ficha_actual_practico': 0,  # NO incluido en fichas
    },
    {
        'categoria': 'CALE.n_1',
        'cantidad': 17,
        'anexoB_teorico': 243_063_465,
        'anexoB_practico': 17_068_936_100,
        'anexoB_unitario': 17_311_999_565,
        'anexoB_total_nacional': 294_303_992_605,
        'ficha_actual_teorico': 645_000_000,
        'ficha_actual_practico': 0,
    },
    {
        'categoria': 'CALE.n_2**',
        'cantidad': 16,
        'anexoB_teorico': 200_646_497,
        'anexoB_practico': 21_886_938_800,
        'anexoB_unitario': 22_087_585_297,
        'anexoB_total_nacional': 353_401_364_752,
        'ficha_actual_teorico': 460_000_000,
        'ficha_actual_practico': 0,
    },
    {
        'categoria': 'CALE.n_2',
        'cantidad': 4,
        'anexoB_teorico': 200_646_497,
        'anexoB_practico': 11_005_619_400,
        'anexoB_unitario': 11_206_265_897,
        'anexoB_total_nacional': 44_825_063_588,
        'ficha_actual_teorico': 460_000_000,
        'ficha_actual_practico': 0,
    },
    {
        'categoria': 'CALE.n_3',
        'cantidad': 16,
        'anexoB_teorico': 200_646_497,
        'anexoB_practico': 5_440_659_700,
        'anexoB_unitario': 5_641_306_197,
        'anexoB_total_nacional': 90_260_899_152,
        'ficha_actual_teorico': 175_000_000,
        'ficha_actual_practico': 0,
    }
]

def generar_tabla_simple():
    """Genera tabla comparativa simple entre Anexo B y Fichas"""
    
    print('📊 Generando tabla de reconciliación simplificada...\n')
    
    rows = []
    total_anexoB = 0
    total_fichas = 0
    
    for item in ANEXO_B_OFICIAL:
        # Calcular total ficha actual
        ficha_unitario = item['ficha_actual_teorico'] + item['ficha_actual_practico']
        ficha_total_nacional = ficha_unitario * item['cantidad']
        
        # Deltas
        delta_teorico = item['anexoB_teorico'] - item['ficha_actual_teorico']
        delta_practico = item['anexoB_practico'] - item['ficha_actual_practico']
        delta_unitario = item['anexoB_unitario'] - ficha_unitario
        delta_nacional = item['anexoB_total_nacional'] - ficha_total_nacional
        
        # Análisis
        estado_teorico = '✅' if abs(delta_teorico / item['anexoB_teorico']) < 0.05 else '⚠️'
        estado_practico = '🔴 FALTA' if item['ficha_actual_practico'] == 0 else '✅'
        
        if item['ficha_actual_practico'] == 0:
            accion = f'AGREGAR componente práctico CALE-P: ${item["anexoB_practico"]:,}'
        elif abs(delta_unitario / item['anexoB_unitario']) < 0.10:
            accion = '✅ Coherente - Sin ajustes'
        else:
            accion = f'⚠️ Ajustar valores: delta ${delta_unitario:,}'
        
        row = {
            'categoria': item['categoria'],
            'cantidad_nodos': item['cantidad'],
            # ANEXO B (Oficial)
            'anexoB_teorico_CALE_T': item['anexoB_teorico'],
            'anexoB_practico_CALE_P': item['anexoB_practico'],
            'anexoB_unitario_total': item['anexoB_unitario'],
            'anexoB_total_nacional': item['anexoB_total_nacional'],
            # FICHA ACTUAL (Publicada)
            'ficha_teorico_CALE_T': item['ficha_actual_teorico'],
            'ficha_practico_CALE_P': item['ficha_actual_practico'],
            'ficha_unitario_total': ficha_unitario,
            'ficha_total_nacional': ficha_total_nacional,
            # DELTAS
            'delta_teorico': delta_teorico,
            'delta_practico': delta_practico,
            'delta_unitario': delta_unitario,
            'delta_nacional': delta_nacional,
            # ANÁLISIS
            'estado_teorico': estado_teorico,
            'estado_practico': estado_practico,
            'accion_requerida': accion
        }
        
        rows.append(row)
        total_anexoB += item['anexoB_total_nacional']
        total_fichas += ficha_total_nacional
    
    # Escribir CSV
    output_path = OUTPUT_DIR / 'reconciliacion_simple_anexoB_vs_fichas.csv'
    fieldnames = [
        'categoria', 'cantidad_nodos',
        'anexoB_teorico_CALE_T', 'anexoB_practico_CALE_P', 'anexoB_unitario_total', 'anexoB_total_nacional',
        'ficha_teorico_CALE_T', 'ficha_practico_CALE_P', 'ficha_unitario_total', 'ficha_total_nacional',
        'delta_teorico', 'delta_practico', 'delta_unitario', 'delta_nacional',
        'estado_teorico', 'estado_practico', 'accion_requerida'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f'✅ Tabla generada: {output_path}\n')
    
    # Resumen en consola
    print('=' * 140)
    print('📊 RECONCILIACIÓN: ANEXO B (OFICIAL) vs FICHAS L3 (PUBLICADAS)')
    print('=' * 140)
    print(f"{'Categoría':<12} | {'Nodos':<5} | {'AnexoB Teórico':>15} | {'AnexoB Práctico':>17} | {'AnexoB TOTAL':>17} | {'Ficha Actual':>17} | {'Estado':>10} | Acción")
    print('-' * 140)
    
    for row in rows:
        print(f"{row['categoria']:<12} | "
              f"{row['cantidad_nodos']:<5} | "
              f"${row['anexoB_teorico_CALE_T']:>14,} | "
              f"${row['anexoB_practico_CALE_P']:>16,} | "
              f"${row['anexoB_total_nacional']:>16,} | "
              f"${row['ficha_total_nacional']:>16,} | "
              f"{row['estado_practico']:>10} | "
              f"{row['accion_requerida']}")
    
    print('-' * 140)
    print(f"{'TOTAL':<12} | {'56':>5} | {'':>15} | {'':>17} | ${total_anexoB:>16,} | ${total_fichas:>16,} | {''} |")
    print('=' * 140)
    
    delta_total = total_anexoB - total_fichas
    pct_faltante = (delta_total / total_anexoB * 100) if total_anexoB else 0
    
    print(f'\n💰 TOTAL INVERSIÓN ANEXO B (Oficial): ${total_anexoB:,}')
    print(f'💰 TOTAL FICHAS ACTUALES (Publicadas): ${total_fichas:,}')
    print(f'📊 FALTANTE EN FICHAS: ${delta_total:,} ({pct_faltante:.1f}%)')
    print(f'\n🔴 CRÍTICO: Las fichas actuales solo contienen CALE-T (componente teórico)')
    print(f'✅ ACCIÓN: Agregar CALE-P (componente práctico) con valores del Anexo B oficial')

if __name__ == '__main__':
    generar_tabla_simple()
