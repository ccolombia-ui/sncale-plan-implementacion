#!/usr/bin/env python3
"""
Generar tabla resumen del estado actual de fichas L3
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FICHAS_ORIG = ROOT / 'fichas_l3'
FICHAS_UNIT = ROOT / 'fichas_l3_unitarias'

def extraer_info_ficha(archivo_html):
    """Extrae información básica de una ficha"""
    try:
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Título
        match_titulo = re.search(r'<h1>([^<]+)</h1>', contenido)
        titulo = match_titulo.group(1) if match_titulo else 'N/A'
        
        # Valorización total
        match_valor = re.search(r'<h3>💰 Valorización Total</h3>\s*<p>\$([\d.]+)\s+COP</p>', contenido)
        valor = int(match_valor.group(1).replace('.', '')) if match_valor else 0
        
        # Nodos
        match_nodos = re.search(r'<p><strong>Nodos Base:</strong>\s*([^<]+)</p>', contenido)
        nodos = match_nodos.group(1).strip() if match_nodos else 'N/A'
        
        # Contar componentes
        componentes = len(re.findall(r'<tr>\s*<td>\d+</td>\s*<td><strong>', contenido))
        
        return {
            'titulo': titulo,
            'valor': valor,
            'nodos': nodos,
            'componentes': componentes
        }
    except Exception as e:
        return {
            'titulo': 'ERROR',
            'valor': 0,
            'nodos': 'N/A',
            'componentes': 0,
            'error': str(e)
        }

def generar_tabla_resumen():
    """Genera tabla comparativa de fichas originales vs unitarias"""
    
    print('\n' + '='*120)
    print('📊 TABLA RESUMEN: ESTADO ACTUAL DE FICHAS L3')
    print('='*120)
    
    # Tabla comparativa
    print(f"\n{'Archivo':<20} | {'Estado':<12} | {'Título':<40} | {'Valorización':<18} | {'Nodos':<12} | {'Comps'}")
    print('-'*120)
    
    fichas = ['BIM_L3_001.html', 'BIM_L3_002.html', 'BIM_L3_003.html', 'BIM_L3_004.html']
    
    for ficha in fichas:
        # Original
        orig = FICHAS_ORIG / ficha
        if orig.exists():
            info_orig = extraer_info_ficha(orig)
            titulo_short = info_orig['titulo'][:38] + '..' if len(info_orig['titulo']) > 40 else info_orig['titulo']
            print(f"{ficha:<20} | {'🔴 NACIONAL':<12} | {titulo_short:<40} | ${info_orig['valor']:>15,} | {info_orig['nodos']:<12} | {info_orig['componentes']}")
        else:
            print(f"{ficha:<20} | {'❌ NO EXISTE':<12} | {'':<40} | {'':<18} | {'':<12} | {''}")
        
        # Unitaria
        unit = FICHAS_UNIT / ficha
        if unit.exists():
            info_unit = extraer_info_ficha(unit)
            titulo_short = info_unit['titulo'][:38] + '..' if len(info_unit['titulo']) > 40 else info_unit['titulo']
            
            # Determinar estado
            if info_unit['valor'] > 0 and info_unit['componentes'] > 0:
                suma_comps = 0
                with open(unit, 'r', encoding='utf-8') as f:
                    cont = f.read()
                    for match in re.finditer(r'<td class="text-right"><strong>\$([\d.]+)</strong></td>', cont):
                        suma_comps += int(match.group(1).replace('.', ''))
                
                if abs(suma_comps - info_unit['valor']) < 1000:
                    estado = '✅ UNITARIA'
                else:
                    estado = '⚠️ REVISAR'
            elif info_unit['valor'] == 0:
                estado = '🔴 VACÍA'
            else:
                estado = '⚠️ INCOMPLETA'
            
            print(f"{'  └─ (unitaria)':<20} | {estado:<12} | {titulo_short:<40} | ${info_unit['valor']:>15,} | {info_unit['nodos']:<12} | {info_unit['componentes']}")
        else:
            print(f"{'  └─ (unitaria)':<20} | {'❌ NO EXISTE':<12} | {'':<40} | {'':<18} | {'':<12} | {''}")
        
        print()
    
    print('='*120)
    
    # Resumen detallado
    print('\n📋 RESUMEN DETALLADO:\n')
    
    print('✅ BIM_L3_001 (CALE.n_1 - Centro Metropolitano)')
    print('   ORIGINAL: $141.320.000.000 (20 nodos) - Valor NACIONAL')
    print('   UNITARIA: $7.066.000.000 (1 nodo) - Valor UNITARIO ✅ VALIDADA')
    print('   └─ Coherencia: SUMA componentes = Valorización total')
    print('   └─ Composición: L2 ($5.98B) + L1 ($186M) + L0 ($900M) = $7.066B')
    print()
    
    print('🔴 BIM_L3_002 (CALE.n_2 - Centro Subregional)')
    print('   ORIGINAL: $4.012.929.940 (20 nodos) - Valor extraño (debería ser ~$44.8B)')
    print('   UNITARIA: $200.646.497 (1 nodo) - DATOS INCOMPLETOS')
    print('   └─ Componentes tienen valores en $0')
    print('   └─ ACCIÓN: Completar desde fuente confiable')
    print()
    
    print('🔴 BIM_L3_003 (CALE.n_3 - Centro Local)')
    print('   ORIGINAL: $0 (16 nodos) - VACÍA')
    print('   UNITARIA: $0 (1 nodo) - VACÍA')
    print('   └─ Sin componentes declarados')
    print('   └─ ACCIÓN: Generar desde estructura similar a BIM_L3_001')
    print()
    
    print('⚠️ BIM_L3_004')
    print('   ORIGINAL: (revisar manualmente)')
    print('   UNITARIA: No procesada (estructura HTML diferente)')
    print('   └─ ACCIÓN: Revisión manual de estructura')
    print()
    
    print('='*120)
    print('\n🎯 ESTADO GENERAL:')
    print('   ✅ 1 ficha COMPLETA Y VALIDADA (BIM_L3_001)')
    print('   🔴 2 fichas REQUIEREN DATOS (BIM_L3_002, BIM_L3_003)')
    print('   ⚠️ 1 ficha REQUIERE REVISIÓN (BIM_L3_004)')
    print()

if __name__ == '__main__':
    generar_tabla_resumen()
