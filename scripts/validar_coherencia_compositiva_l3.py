#!/usr/bin/env python3
"""
Validación compositiva de fichas L3
Verifica que L3 = Σ(L2) + Σ(L1) + Σ(L0)
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FICHAS_L3_UNIT = ROOT / 'fichas_l3_unitarias'

def extraer_componentes_ficha(archivo_html):
    """Extrae componentes y valores de una ficha HTML"""
    with open(archivo_html, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Extraer valorización total
    match_total = re.search(r'<h3>💰 Valorización Total</h3>\s*<p>\$([\d.]+)\s+COP</p>', contenido)
    if not match_total:
        return None, []
    
    valor_total = int(match_total.group(1).replace('.', ''))
    
    # Extraer componentes de la tabla
    componentes = []
    patron_fila = r'<tr>\s*<td>(\d+)</td>\s*<td><strong>([^<]+)</strong></td>.*?<code>([^<]+)</code>.*?<td class="text-right">\$([\d.]+)</td>\s*<td class="text-center">(\d+)</td>.*?<td class="text-right"><strong>\$([\d.]+)</strong></td>'
    
    for match in re.finditer(patron_fila, contenido, re.DOTALL):
        num = int(match.group(1))
        nombre = match.group(2)
        ref_bim = match.group(3)
        valor_unit = int(match.group(4).replace('.', ''))
        cantidad = int(match.group(5))
        valor_total_comp = int(match.group(6).replace('.', ''))
        
        componentes.append({
            'num': num,
            'nombre': nombre,
            'ref_bim': ref_bim,
            'valor_unitario': valor_unit,
            'cantidad': cantidad,
            'valor_total': valor_total_comp,
            'nivel': ref_bim.split('.')[0]  # L0, L1, L2
        })
    
    return valor_total, componentes

def validar_coherencia_compositiva(archivo_html):
    """Valida que la suma de componentes = valorización total"""
    
    nombre_archivo = archivo_html.name
    print(f'\n{"="*80}')
    print(f'📦 VALIDANDO: {nombre_archivo}')
    print(f'{"="*80}\n')
    
    valor_total_declarado, componentes = extraer_componentes_ficha(archivo_html)
    
    if valor_total_declarado is None:
        print('❌ No se pudo extraer valorización total')
        return False
    
    if not componentes:
        print('❌ No se encontraron componentes')
        return False
    
    # Agrupar por nivel
    por_nivel = {'L0': [], 'L1': [], 'L2': [], 'L3': []}
    suma_total = 0
    
    print('🔧 COMPONENTES DECLARADOS:\n')
    print(f"{'#':<3} | {'Nombre':<45} | {'Ref BIM':<25} | {'V.Unit':<15} | {'Cant':<5} | {'V.Total':<15}")
    print('-' * 115)
    
    for comp in componentes:
        suma_total += comp['valor_total']
        por_nivel[comp['nivel']].append(comp)
        
        print(f"{comp['num']:<3} | {comp['nombre']:<45} | {comp['ref_bim']:<25} | "
              f"${comp['valor_unitario']:>13,} | {comp['cantidad']:<5} | ${comp['valor_total']:>13,}")
    
    print('-' * 115)
    print(f"{'SUMA COMPONENTES':<77} | ${suma_total:>13,}")
    print()
    
    # Validar suma
    diferencia = suma_total - valor_total_declarado
    porcentaje = (diferencia / valor_total_declarado * 100) if valor_total_declarado > 0 else 0
    
    print(f'💰 VALORIZACIÓN TOTAL DECLARADA: ${valor_total_declarado:>13,}')
    print(f'🧮 SUMA DE COMPONENTES:           ${suma_total:>13,}')
    print(f'📊 DIFERENCIA:                    ${diferencia:>13,} ({porcentaje:+.2f}%)')
    
    if abs(diferencia) < 1000:  # Tolerancia de $1000 por redondeos
        print('\n✅ COHERENCIA VALIDADA - La suma de componentes coincide con el total declarado')
        coherente = True
    else:
        print(f'\n❌ INCOHERENCIA DETECTADA - Diferencia de ${abs(diferencia):,}')
        coherente = False
    
    # Desglose por nivel
    print(f'\n{"─"*80}')
    print('📊 DESGLOSE POR NIVEL BIM:\n')
    
    for nivel in ['L2', 'L1', 'L0']:
        if por_nivel[nivel]:
            suma_nivel = sum(c['valor_total'] for c in por_nivel[nivel])
            print(f'{nivel} ({len(por_nivel[nivel])} componentes): ${suma_nivel:>15,}')
            for c in por_nivel[nivel]:
                print(f'    └─ {c["ref_bim"]:<30} ${c["valor_total"]:>13,}')
    
    # Validar multiplicaciones
    print(f'\n{"─"*80}')
    print('🔍 VALIDACIÓN DE MULTIPLICACIONES:\n')
    
    errores_mult = []
    for comp in componentes:
        calculado = comp['valor_unitario'] * comp['cantidad']
        if calculado != comp['valor_total']:
            errores_mult.append(comp)
            print(f'❌ {comp["ref_bim"]}: ${comp["valor_unitario"]:,} × {comp["cantidad"]} = '
                  f'${calculado:,} (declarado: ${comp["valor_total"]:,})')
        else:
            print(f'✅ {comp["ref_bim"]}: ${comp["valor_unitario"]:,} × {comp["cantidad"]} = ${comp["valor_total"]:,}')
    
    if errores_mult:
        print(f'\n⚠️ ADVERTENCIA: {len(errores_mult)} error(es) de multiplicación detectados')
        coherente = False
    else:
        print('\n✅ Todas las multiplicaciones son correctas')
    
    return coherente

def main():
    print('🎯 VALIDACIÓN COMPOSITIVA DE FICHAS L3 UNITARIAS')
    print('=' * 80)
    print('Verificando que: L3_total = Σ(L2_componentes) + Σ(L1_componentes) + Σ(L0_componentes)\n')
    
    fichas = sorted(FICHAS_L3_UNIT.glob('BIM_L3_*.html'))
    
    if not fichas:
        print(f'❌ No se encontraron fichas en: {FICHAS_L3_UNIT}')
        return
    
    resultados = []
    
    for ficha in fichas:
        coherente = validar_coherencia_compositiva(ficha)
        resultados.append({'ficha': ficha.name, 'coherente': coherente})
    
    # Resumen final
    print(f'\n{"="*80}')
    print('📊 RESUMEN DE VALIDACIÓN')
    print('=' * 80)
    
    coherentes = sum(1 for r in resultados if r['coherente'])
    incoherentes = len(resultados) - coherentes
    
    print(f'\n✅ Fichas coherentes:   {coherentes}/{len(resultados)}')
    print(f'❌ Fichas incoherentes: {incoherentes}/{len(resultados)}\n')
    
    for r in resultados:
        estado = '✅' if r['coherente'] else '❌'
        print(f"{estado} {r['ficha']}")
    
    print('\n' + '=' * 80)

if __name__ == '__main__':
    main()
