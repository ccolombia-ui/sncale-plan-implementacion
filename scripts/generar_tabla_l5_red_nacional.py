#!/usr/bin/env python3
"""
Tabla L5 Red Nacional: Construida desde instancias L4
(L4 = instancia municipal de un L3)
"""

# ============================================================================
# DEFINICIÓN DE CONFIGURACIONES L3
# ============================================================================

# L3 Principales (Centros completos)
L3_PRINCIPALES = {
    'CALE.n_1+': {
        'nombre': 'Centro Metropolitano Plus',
        'componentes': 'CALE-T + CALE-P.C3 (I+II+III) + Clase II adicional',
        'vr_anexoB': 22_876_926_598,
        'vr_plan41': 22_876_926_598,
        'vr_fichas': 0,  # Por crear
        'cantidad_municipios': 3,
        'notas': 'Variante de CALE.n_1 con pista Clase II adicional. No existe ficha L3 separada.',
        'recomendacion': 'Crear BIM_L3_001b con componente adicional L2.pista_clase_2 ($980M)'
    },
    'CALE.n_1': {
        'nombre': 'Centro Metropolitano',
        'componentes': 'CALE-T + CALE-P.C3 (Clase I+II+III)',
        'vr_anexoB': 17_311_999_565,
        'vr_plan41': 17_311_999_565,  # Sin predio
        'vr_fichas': 6_166_000_000,  # SIN simuladores: $7.066M - $900M = $6.166M
        'cantidad_municipios': 17,
        'notas': 'Ficha validada compositivamente pero incompleta (35.6%). Componentes actuales: pistas I+II+III ($3.580M) + edificación ($2.400M) + sala 24q ($186M). FALTA: CALE-T reducido ($159M, descontando C2-C5) + componentes adicionales CALE-P',
        'recomendacion': 'Agregar CALE-T reducido ($159M = $243M - $84M de C2-C5). Investigar componentes CALE-P adicionales para alcanzar $17.312M'
    },
    'CALE.n_2**': {
        'nombre': 'Centro Subregional Plus',
        'componentes': 'CALE-T + CALE-P.C2 (Clase I+II) + 2×Clase I adicionales',
        'vr_anexoB': 22_087_585_297,
        'vr_plan41': 22_087_585_297,
        'vr_fichas': 0,  # Vacía
        'cantidad_municipios': 16,
        'notas': 'No existe ficha. Variante con 2 pistas Clase I adicionales',
        'recomendacion': 'Crear BIM_L3_002b con 3 pistas Clase I totales'
    },
    'CALE.n_2': {
        'nombre': 'Centro Subregional',
        'componentes': 'CALE-T + CALE-P.C2 (Clase I+II)',
        'vr_anexoB': 11_206_265_897,
        'vr_plan41': 11_206_265_897,
        'vr_fichas': 200_646_497,  # Datos incompletos
        'cantidad_municipios': 4,
        'notas': 'Ficha con componentes en $0 (1.8% cobertura). Estructura existe pero sin valores',
        'recomendacion': 'Corregir BIM_L3_002 con datos completos desde Anexo B'
    },
    'CALE.n_3': {
        'nombre': 'Centro Local',
        'componentes': 'CALE-T + CALE-P.C1 (Clase I)',
        'vr_anexoB': 5_641_306_197,
        'vr_plan41': 5_641_306_197,
        'vr_fichas': 0,  # Vacía
        'cantidad_municipios': 16,
        'notas': 'Ficha vacía. Configuración básica: 1 pista Clase I + sala 4q + edificación básica',
        'recomendacion': 'Generar BIM_L3_003 completa'
    }
}

# L3 Satelitales (Infraestructura ligera + equipamiento TIC)
L3_SATELITALES = {
    'C2': {
        'nombre': 'Satélite C2 - Sede Principal',
        'componentes': 'Adecuación infraestructura + equipamiento TIC básico',
        'vr_anexoB': 30_000_000,  # Estimado: más completo (sede principal)
        'vr_plan41': 30_000_000,
        'vr_fichas': 0,
        'cantidad_municipios': 31,
        'notas': 'Satélite tipo C2 (sede principal municipal). Antes dentro de CALE-T ($84M para C2-C5). Ahora independiente L3 con componentes: adecuación local, equipamiento TIC, conectividad',
        'recomendacion': 'Crear BIM_L3_C2 con componentes L2/L1: adecuación civil básica, estaciones trabajo, red local'
    },
    'C3': {
        'nombre': 'Satélite C3 - Sede Secundaria',
        'componentes': 'Adecuación infraestructura + equipamiento TIC medio',
        'vr_anexoB': 20_000_000,  # Estimado: intermedio
        'vr_plan41': 20_000_000,
        'vr_fichas': 0,
        'cantidad_municipios': 69,
        'notas': 'Satélite tipo C3 (sede secundaria). Infraestructura más simple que C2',
        'recomendacion': 'Crear BIM_L3_C3 con componentes ligeros'
    },
    'C4': {
        'nombre': 'Satélite C4 - Punto Remoto',
        'componentes': 'Adecuación mínima + equipamiento TIC reducido',
        'vr_anexoB': 15_000_000,  # Estimado: menor
        'vr_plan41': 15_000_000,
        'vr_fichas': 0,
        'cantidad_municipios': 27,
        'notas': 'Satélite tipo C4 (punto remoto). Menor equipamiento',
        'recomendacion': 'Crear BIM_L3_C4 con componentes mínimos'
    },
    'C5': {
        'nombre': 'Satélite C5 - Punto Básico',
        'componentes': 'Adecuación básica + equipamiento TIC esencial',
        'vr_anexoB': 12_000_000,  # Estimado: mínimo
        'vr_plan41': 12_000_000,
        'vr_fichas': 0,
        'cantidad_municipios': 14,
        'notas': 'Satélite tipo C5 (punto básico). Infraestructura mínima',
        'recomendacion': 'Crear BIM_L3_C5 con componentes esenciales'
    }
}

# ============================================================================
# GENERACIÓN TABLA L5 (RED NACIONAL)
# ============================================================================

def generar_tabla_l5():
    """Genera tabla L5 desde instancias L4 (L3 × municipios)"""
    
    print('\n' + '='*160)
    print('📊 TABLA L5: RED NACIONAL - Construida desde instancias L4 (L3 × cantidad municipios)')
    print('='*160)
    print()
    
    # Encabezado tabla
    print(f"{'Instancia Tipo (L3)':<20} | {'Cant':<5} | {'VR_Un_Ficha_L3':<18} | {'VR_Un_Plan41':<18} | {'VR_Un_AnexoB':<18} | {'Notas':<60} | {'Recomendación':<50}")
    print('-'*160)
    
    # L3 Principales
    total_fichas_nacional = 0
    total_plan41_nacional = 0
    total_anexoB_nacional = 0
    total_municipios = 0
    
    print('🏢 CENTROS CALE (L3 Principales):')
    print()
    
    for tipo, datos in L3_PRINCIPALES.items():
        cant = datos['cantidad_municipios']
        vr_fichas = datos['vr_fichas']
        vr_plan41 = datos['vr_plan41']
        vr_anexoB = datos['vr_anexoB']
        
        # Calcular valores nacionales (L5)
        total_fichas_nacional += vr_fichas * cant
        total_plan41_nacional += vr_plan41 * cant
        total_anexoB_nacional += vr_anexoB * cant
        total_municipios += cant
        
        # Estado visual
        if vr_fichas == 0:
            estado_fichas = '🔴 $0'
        elif vr_fichas < vr_anexoB * 0.5:
            estado_fichas = f'⚠️ ${vr_fichas:,}'
        else:
            estado_fichas = f'📊 ${vr_fichas:,}'
        
        # Notas y recomendación cortas
        notas_short = datos['notas'][:58] + '..' if len(datos['notas']) > 60 else datos['notas']
        recom_short = datos['recomendacion'][:48] + '..' if len(datos['recomendacion']) > 50 else datos['recomendacion']
        
        print(f"{tipo:<20} | {cant:<5} | {estado_fichas:<18} | ${vr_plan41:<17,} | ${vr_anexoB:<17,} | {notas_short:<60} | {recom_short:<50}")
    
    print()
    print('🛰️ SATÉLITES (L3 Satelitales independientes):')
    print()
    
    for tipo, datos in L3_SATELITALES.items():
        cant = datos['cantidad_municipios']
        vr_fichas = datos['vr_fichas']
        vr_plan41 = datos['vr_plan41']
        vr_anexoB = datos['vr_anexoB']
        
        total_fichas_nacional += vr_fichas * cant
        total_plan41_nacional += vr_plan41 * cant
        total_anexoB_nacional += vr_anexoB * cant
        total_municipios += cant
        
        notas_short = datos['notas'][:58] + '..' if len(datos['notas']) > 60 else datos['notas']
        recom_short = datos['recomendacion'][:48] + '..' if len(datos['recomendacion']) > 50 else datos['recomendacion']
        
        print(f"CALE.n_{tipo:<14} | {cant:<5} | {'🔴 $0':<18} | ${vr_plan41:<17,} | ${vr_anexoB:<17,} | {notas_short:<60} | {recom_short:<50}")
    
    print('-'*160)
    print(f"{'TOTAL RED NACIONAL':<20} | {total_municipios:<5} | ${total_fichas_nacional:<17,} | ${total_plan41_nacional:<17,} | ${total_anexoB_nacional:<17,} | {'56 nodos totales (5 centros + 4 tipos satélites)':<60} | {'Completar todas las fichas L3 faltantes':<50}")
    print('='*160)
    
    # Análisis
    print('\n📊 ANÁLISIS RED NACIONAL (L5):\n')
    
    diferencia = total_anexoB_nacional - total_fichas_nacional
    cobertura = (total_fichas_nacional / total_anexoB_nacional * 100) if total_anexoB_nacional > 0 else 0
    
    print(f'Valor Total Anexo B (esperado):  ${total_anexoB_nacional:>20,}')
    print(f'Valor Total Fichas (actual):     ${total_fichas_nacional:>20,}')
    print(f'Diferencia (faltante):           ${diferencia:>20,}')
    print(f'Cobertura actual:                {cobertura:>21.1f}%')
    print()
    
    # Desglose
    print('📋 DESGLOSE POR CATEGORÍA:\n')
    
    total_centros_fichas = sum(d['vr_fichas'] * d['cantidad_municipios'] for d in L3_PRINCIPALES.values())
    total_centros_anexoB = sum(d['vr_anexoB'] * d['cantidad_municipios'] for d in L3_PRINCIPALES.values())
    total_satelites_fichas = sum(d['vr_fichas'] * d['cantidad_municipios'] for d in L3_SATELITALES.values())
    total_satelites_anexoB = sum(d['vr_anexoB'] * d['cantidad_municipios'] for d in L3_SATELITALES.values())
    
    total_municipios_centros = sum(d['cantidad_municipios'] for d in L3_PRINCIPALES.values())
    total_municipios_satelites = sum(d['cantidad_municipios'] for d in L3_SATELITALES.values())
    
    print(f'🏢 Centros CALE (n_1, n_2, n_3):')
    print(f'   Municipios: {total_municipios_centros}')
    print(f'   Fichas:     ${total_centros_fichas:>15,}')
    print(f'   Anexo B:    ${total_centros_anexoB:>15,}')
    print(f'   Cobertura:  {(total_centros_fichas/total_centros_anexoB*100):>14.1f}%')
    print()
    
    print(f'🛰️ Satélites (C2-C5):')
    print(f'   Municipios: {total_municipios_satelites}')
    print(f'   Fichas:     ${total_satelites_fichas:>15,}')
    print(f'   Anexo B:    ${total_satelites_anexoB:>15,}')
    print(f'   Cobertura:  {(total_satelites_fichas/total_satelites_anexoB*100) if total_satelites_anexoB > 0 else 0:>14.1f}%')
    print()
    
    # CALE-T ajustado
    print('='*160)
    print('\n💡 AJUSTE CALE-T (Componente Teórico):\n')
    
    cale_t_original = 243_063_465
    cale_t_satelites = 84_000_000  # Estimado C2-C5 dentro de original
    cale_t_centros = cale_t_original - cale_t_satelites
    
    print(f'CALE-T Original (Anexo B):                ${cale_t_original:>15,}')
    print(f'  - Satélites C2-C5 (ahora independientes): ${cale_t_satelites:>15,}')
    print('-'*80)
    print(f'CALE-T para Centros (ajustado):           ${cale_t_centros:>15,}')
    print()
    print('📌 Decisión: Satélites C2-C5 son ahora L3 independientes (no parte de CALE-T)')
    print()
    
    # Recomendaciones
    print('='*160)
    print('\n🎯 RECOMENDACIONES PRIORITARIAS:\n')
    
    print('1. ✅ CALE.n_1: AJUSTAR valor ficha')
    print('   └─ Actual: $6.166M (sin simuladores)')
    print('   └─ Objetivo: $17.312M')
    print('   └─ Agregar: CALE-T ajustado ($159M) + componentes CALE-P adicionales')
    print()
    
    print('2. 🔴 Crear fichas L3 SATELITALES (C2-C5):')
    print('   └─ BIM_L3_C2: $30M × 31 municipios')
    print('   └─ BIM_L3_C3: $20M × 69 municipios')
    print('   └─ BIM_L3_C4: $15M × 27 municipios')
    print('   └─ BIM_L3_C5: $12M × 14 municipios')
    print('   └─ Total satélites: $2.637M nacional')
    print()
    
    print('3. 📝 Crear fichas VARIANTES:')
    print('   └─ BIM_L3_001b (CALE.n_1+): $22.877M')
    print('   └─ BIM_L3_002b (CALE.n_2**): $22.088M')
    print()
    
    print('4. 🔧 Corregir fichas existentes:')
    print('   └─ BIM_L3_002 (CALE.n_2): Reemplazar valores $0')
    print('   └─ BIM_L3_003 (CALE.n_3): Generar completa')
    print()
    
    print('='*160)

if __name__ == '__main__':
    generar_tabla_l5()
