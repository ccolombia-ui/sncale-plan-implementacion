#!/usr/bin/env python3
"""
Tabla comparativa: Fichas L3 vs Plan v4.1 vs Anexo B
"""
from pathlib import Path
import re
import csv

ROOT = Path(__file__).resolve().parents[1]
FICHAS_UNIT = ROOT / 'fichas_l3_unitarias'
OUTPUT = ROOT / 'output'

def extraer_valor_ficha(archivo_html):
    """Extrae valorización total de una ficha unitaria"""
    try:
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        match_valor = re.search(r'<h3>💰 Valorización Total</h3>\s*<p>\$([\d.]+)\s+COP</p>', contenido)
        if match_valor:
            return int(match_valor.group(1).replace('.', ''))
        return 0
    except:
        return 0

# Datos consolidados de Plan v4.1 y Anexo B (fuente: trabajos anteriores)
DATOS = {
    'CALE.n_1': {
        'nombre': 'Centro Metropolitano (base)',
        'fichas_unitario': 7_066_000_000,  # BIM_L3_001 validado
        'fichas_nodos': 17,
        'plan41_unitario': 17_311_999_565,  # Incluye CALE-T + CALE-P
        'anexoB_unitario': 17_311_999_565,
        'anexoB_nodos': 17,
        'notas': 'Ficha validada. Diferencia: Plan v4.1 incluye componentes adicionales no presentes en ficha actual',
        'recomendacion': 'Completar ficha con componentes CALE-T ($9.3B) + ajustes'
    },
    'CALE.n_1+': {
        'nombre': 'Centro Metropolitano Plus',
        'fichas_unitario': 0,  # No existe ficha separada aún
        'fichas_nodos': 3,
        'plan41_unitario': 22_876_926_598,  # CALE.n_1 + componente adicional
        'anexoB_unitario': 22_876_926_598,
        'anexoB_nodos': 3,
        'notas': 'No existe ficha unitaria separada. Variante de CALE.n_1 con pista Clase II adicional',
        'recomendacion': 'Crear BIM_L3_001b.html con componente adicional ($5.56B)'
    },
    'CALE.n_2': {
        'nombre': 'Centro Subregional (base)',
        'fichas_unitario': 200_646_497,  # BIM_L3_002 - datos incompletos
        'fichas_nodos': 4,
        'plan41_unitario': 11_206_265_897,
        'anexoB_unitario': 11_206_265_897,
        'anexoB_nodos': 4,
        'notas': 'Ficha con datos incompletos (componentes en $0). Valor esperado: $11.2B unitario',
        'recomendacion': 'Corregir BIM_L3_002.html desde fuente confiable'
    },
    'CALE.n_2**': {
        'nombre': 'Centro Subregional Plus',
        'fichas_unitario': 0,  # No existe ficha separada
        'fichas_nodos': 16,
        'plan41_unitario': 22_087_585_297,  # CALE.n_2 + pistas adicionales
        'anexoB_unitario': 22_087_585_297,
        'anexoB_nodos': 16,
        'notas': 'No existe ficha unitaria. Variante con 2 pistas Clase I adicionales',
        'recomendacion': 'Crear BIM_L3_002b.html con componentes adicionales'
    },
    'CALE.n_3': {
        'nombre': 'Centro Local',
        'fichas_unitario': 0,  # BIM_L3_003 vacía
        'fichas_nodos': 16,
        'plan41_unitario': 5_641_306_197,
        'anexoB_unitario': 5_641_306_197,
        'anexoB_nodos': 16,
        'notas': 'Ficha vacía. Configuración más básica (1 pista Clase I + sala 4q + simulador C1)',
        'recomendacion': 'Generar BIM_L3_003.html completa desde estructura base'
    }
}

def generar_tabla_comparativa():
    """Genera tabla CSV y display en consola"""
    
    OUTPUT.mkdir(exist_ok=True)
    
    # Crear CSV
    csv_file = OUTPUT / 'comparacion_fichas_vs_plan41_anexoB.csv'
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Edificación',
            'Nombre',
            'VR_Fichas_Unitario',
            'VR_Plan41_Unitario',
            'VR_AnexoB_Unitario',
            'Diferencia_Fichas_vs_Plan41',
            'Diferencia_%',
            'Nodos_Red',
            'VR_Fichas_Nacional',
            'VR_Plan41_Nacional',
            'VR_AnexoB_Nacional',
            'Notas',
            'Recomendación'
        ])
        
        total_fichas_nacional = 0
        total_plan41_nacional = 0
        total_anexoB_nacional = 0
        
        for config_id, datos in DATOS.items():
            fichas_unit = datos['fichas_unitario']
            plan41_unit = datos['plan41_unitario']
            anexoB_unit = datos['anexoB_unitario']
            nodos = datos['fichas_nodos']
            
            fichas_nacional = fichas_unit * nodos
            plan41_nacional = plan41_unit * nodos
            anexoB_nacional = anexoB_unit * nodos
            
            diferencia = fichas_unit - plan41_unit
            diferencia_pct = (diferencia / plan41_unit * 100) if plan41_unit > 0 else -100
            
            total_fichas_nacional += fichas_nacional
            total_plan41_nacional += plan41_nacional
            total_anexoB_nacional += anexoB_nacional
            
            writer.writerow([
                config_id,
                datos['nombre'],
                fichas_unit,
                plan41_unit,
                anexoB_unit,
                diferencia,
                f"{diferencia_pct:.1f}%",
                nodos,
                fichas_nacional,
                plan41_nacional,
                anexoB_nacional,
                datos['notas'],
                datos['recomendacion']
            ])
        
        # Totales
        writer.writerow([
            'TOTAL',
            'Red Nacional Completa',
            '',
            '',
            '',
            '',
            '',
            '56 nodos',
            total_fichas_nacional,
            total_plan41_nacional,
            total_anexoB_nacional,
            f'Diferencia total: ${(total_plan41_nacional - total_fichas_nacional):,}',
            'Completar fichas faltantes para alcanzar valor total'
        ])
    
    print(f'\n✅ CSV generado: {csv_file.relative_to(ROOT)}\n')
    
    # Display en consola
    print('='*160)
    print('📊 TABLA COMPARATIVA: FICHAS L3 vs PLAN v4.1 vs ANEXO B')
    print('='*160)
    print()
    
    # Formato tabla visual
    print(f"{'Edificación':<15} | {'VR_Fichas':<18} | {'VR_Plan41':<18} | {'VR_AnexoB':<18} | {'Notas':<60} | {'Recomendación':<50}")
    print('-'*160)
    
    for config_id, datos in DATOS.items():
        fichas = datos['fichas_unitario']
        plan41 = datos['plan41_unitario']
        anexoB = datos['anexoB_unitario']
        
        # Estado visual
        if fichas == 0:
            estado = '🔴 $0'
        elif fichas < plan41 * 0.5:
            estado = f'⚠️ ${fichas:,}'
        elif abs(fichas - plan41) < 1_000_000:
            estado = f'✅ ${fichas:,}'
        else:
            estado = f'📊 ${fichas:,}'
        
        notas_short = datos['notas'][:58] + '..' if len(datos['notas']) > 60 else datos['notas']
        recom_short = datos['recomendacion'][:48] + '..' if len(datos['recomendacion']) > 50 else datos['recomendacion']
        
        print(f"{config_id:<15} | {estado:<18} | ${plan41:<17,} | ${anexoB:<17,} | {notas_short:<60} | {recom_short:<50}")
    
    print('-'*160)
    
    # Totales
    total_fichas = sum(d['fichas_unitario'] * d['fichas_nodos'] for d in DATOS.values())
    total_plan41 = sum(d['plan41_unitario'] * d['fichas_nodos'] for d in DATOS.values())
    total_anexoB = sum(d['anexoB_unitario'] * d['anexoB_nodos'] for d in DATOS.values())
    
    print(f"{'TOTAL NACIONAL':<15} | ${total_fichas:<17,} | ${total_plan41:<17,} | ${total_anexoB:<17,} | {'56 nodos en red nacional':<60} | {'Completar fichas para coherencia total':<50}")
    print('='*160)
    
    # Análisis de diferencias
    print('\n📊 ANÁLISIS DE DIFERENCIAS:\n')
    
    diferencia_total = total_plan41 - total_fichas
    porcentaje_cobertura = (total_fichas / total_plan41 * 100) if total_plan41 > 0 else 0
    
    print(f'Valor Total Plan v4.1:      ${total_plan41:>20,}')
    print(f'Valor Total Fichas:         ${total_fichas:>20,}')
    print(f'Diferencia:                 ${diferencia_total:>20,} ({100-porcentaje_cobertura:.1f}% faltante)')
    print(f'Cobertura actual:           {porcentaje_cobertura:>21.1f}%')
    print()
    
    # Desglose por configuración
    print('📋 DESGLOSE POR CONFIGURACIÓN:\n')
    
    for config_id, datos in DATOS.items():
        fichas_unit = datos['fichas_unitario']
        plan41_unit = datos['plan41_unitario']
        nodos = datos['fichas_nodos']
        
        if fichas_unit > 0:
            cobertura = (fichas_unit / plan41_unit * 100)
            simbolo = '✅' if cobertura > 90 else '⚠️' if cobertura > 40 else '🔴'
        else:
            cobertura = 0
            simbolo = '🔴'
        
        print(f'{simbolo} {config_id:<12} ({nodos:>2} nodos): Cobertura {cobertura:>5.1f}% | Fichas: ${fichas_unit:>13,} | Plan: ${plan41_unit:>13,}')
    
    print('\n' + '='*160)
    
    # Recomendaciones prioritarias
    print('\n🎯 RECOMENDACIONES PRIORITARIAS:\n')
    
    print('1. ✅ CALE.n_1 (BIM_L3_001): VALIDADA - pero falta completar con componentes CALE-T')
    print('   └─ Acción: Agregar componentes faltantes ($9.3B aprox) para llegar a $17.3B\n')
    
    print('2. 🔴 CALE.n_2 (BIM_L3_002): CORREGIR DATOS')
    print('   └─ Acción: Reemplazar valores $0 con datos reales desde Anexo B o fuente confiable\n')
    
    print('3. 🔴 CALE.n_3 (BIM_L3_003): GENERAR COMPLETA')
    print('   └─ Acción: Crear ficha desde cero con estructura validada de BIM_L3_001\n')
    
    print('4. 📝 VARIANTES (CALE.n_1+, CALE.n_2**): CREAR FICHAS SEPARADAS')
    print('   └─ Acción: Generar BIM_L3_001b.html y BIM_L3_002b.html con componentes adicionales\n')
    
    print('='*160)

if __name__ == '__main__':
    generar_tabla_comparativa()
