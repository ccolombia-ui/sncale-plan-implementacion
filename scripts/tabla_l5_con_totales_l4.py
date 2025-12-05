#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TABLA L5: RED NACIONAL
Muestra valores TOTALES de todas las instancias L4 (L3 × cantidad municipios)
NO muestra valores unitarios, sino TOTALES NACIONALES por tipo de edificación.
"""

def generar_tabla_l5_totales():
    """Genera tabla L5 con TOTALES NACIONALES (suma de todas las instancias L4)"""
    
    # DATOS BASE: Valores unitarios L3 y cantidad de municipios
    datos_l3 = {
        'CALE.n_1+': {
            'cantidad_municipios': 3,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 22_876_926_598,
            'vr_unitario_anexoB': 22_876_926_598,
        },
        'CALE.n_1': {
            'cantidad_municipios': 17,
            'vr_unitario_l3_actual': 6_166_000_000,
            'vr_unitario_l3_objetivo': 17_311_999_565,
            'vr_unitario_anexoB': 17_311_999_565,
        },
        'CALE.n_2**': {
            'cantidad_municipios': 16,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 22_087_585_297,
            'vr_unitario_anexoB': 22_087_585_297,
        },
        'CALE.n_2': {
            'cantidad_municipios': 4,
            'vr_unitario_l3_actual': 200_646_497,
            'vr_unitario_l3_objetivo': 11_206_265_897,
            'vr_unitario_anexoB': 11_206_265_897,
        },
        'CALE.n_3': {
            'cantidad_municipios': 16,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 5_641_306_197,
            'vr_unitario_anexoB': 5_641_306_197,
        },
        'CALE.n_C2': {
            'cantidad_municipios': 31,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 30_000_000,
            'vr_unitario_anexoB': 30_000_000,
        },
        'CALE.n_C3': {
            'cantidad_municipios': 69,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 20_000_000,
            'vr_unitario_anexoB': 20_000_000,
        },
        'CALE.n_C4': {
            'cantidad_municipios': 27,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 15_000_000,
            'vr_unitario_anexoB': 15_000_000,
        },
        'CALE.n_C5': {
            'cantidad_municipios': 14,
            'vr_unitario_l3_actual': 0,
            'vr_unitario_l3_objetivo': 12_000_000,
            'vr_unitario_anexoB': 12_000_000,
        },
    }
    
    print("=" * 180)
    print("\n📊 TABLA L5: RED NACIONAL - TOTALES DE INSTANCIAS L4")
    print("   (Cada fila = TOTAL NACIONAL de ese tipo de edificación = VR_Unitario_L3 × Cantidad_Municipios)")
    print("=" * 180)
    print()
    
    # Header
    print(f"{'Tipo L3':<15} | {'Cant':>4} | {'VR_Unit_L3_Actual':>20} | {'VR_Total_L4_Actual':>22} | {'VR_Unit_L3_Objetivo':>20} | {'VR_Total_L4_Objetivo':>22} | {'VR_Total_AnexoB':>22} | {'Estado':<7}")
    print(f"{'(edificación)':<15} | {'Mun':>4} | {'(1 unidad)':>20} | {'(Cant × Unit_Actual)':>22} | {'(1 unidad)':>20} | {'(Cant × Unit_Obj)':>22} | {'(referencia)':>22} | {'':<7}")
    print("-" * 180)
    
    # Procesar cada tipo L3
    total_mun = 0
    total_l4_actual = 0
    total_l4_objetivo = 0
    total_anexoB = 0
    
    print("\n🏢 CENTROS CALE:\n")
    for tipo in ['CALE.n_1+', 'CALE.n_1', 'CALE.n_2**', 'CALE.n_2', 'CALE.n_3']:
        data = datos_l3[tipo]
        cant = data['cantidad_municipios']
        unit_actual = data['vr_unitario_l3_actual']
        unit_objetivo = data['vr_unitario_l3_objetivo']
        unit_anexoB = data['vr_unitario_anexoB']
        
        # CÁLCULO L5: Total nacional = Unitario L3 × Cantidad municipios
        total_actual = unit_actual * cant
        total_objetivo = unit_objetivo * cant
        total_anexo = unit_anexoB * cant
        
        total_mun += cant
        total_l4_actual += total_actual
        total_l4_objetivo += total_objetivo
        total_anexoB += total_anexo
        
        estado = '✅' if total_objetivo == total_anexo else '⚠️'
        
        str_unit_actual = f"${unit_actual:,}" if unit_actual > 0 else "🔴 $0"
        str_total_actual = f"${total_actual:,}" if total_actual > 0 else "🔴 $0"
        str_unit_objetivo = f"${unit_objetivo:,}"
        str_total_objetivo = f"${total_objetivo:,}"
        str_total_anexo = f"${total_anexo:,}"
        
        print(f"{tipo:<15} | {cant:>4} | {str_unit_actual:>20} | {str_total_actual:>22} | {str_unit_objetivo:>20} | {str_total_objetivo:>22} | {str_total_anexo:>22} | {estado:<7}")
    
    print("\n🛰️ SATÉLITES:\n")
    for tipo in ['CALE.n_C2', 'CALE.n_C3', 'CALE.n_C4', 'CALE.n_C5']:
        data = datos_l3[tipo]
        cant = data['cantidad_municipios']
        unit_actual = data['vr_unitario_l3_actual']
        unit_objetivo = data['vr_unitario_l3_objetivo']
        unit_anexoB = data['vr_unitario_anexoB']
        
        # CÁLCULO L5: Total nacional = Unitario L3 × Cantidad municipios
        total_actual = unit_actual * cant
        total_objetivo = unit_objetivo * cant
        total_anexo = unit_anexoB * cant
        
        total_mun += cant
        total_l4_actual += total_actual
        total_l4_objetivo += total_objetivo
        total_anexoB += total_anexo
        
        estado = '✅' if total_objetivo == total_anexo else '⚠️'
        
        str_unit_actual = f"${unit_actual:,}" if unit_actual > 0 else "🔴 $0"
        str_total_actual = f"${total_actual:,}" if total_actual > 0 else "🔴 $0"
        str_unit_objetivo = f"${unit_objetivo:,}"
        str_total_objetivo = f"${total_objetivo:,}"
        str_total_anexo = f"${total_anexo:,}"
        
        print(f"{tipo:<15} | {cant:>4} | {str_unit_actual:>20} | {str_total_actual:>22} | {str_unit_objetivo:>20} | {str_total_objetivo:>22} | {str_total_anexo:>22} | {estado:<7}")
    
    # TOTALES
    print("-" * 180)
    print(f"{'TOTAL L5':<15} | {total_mun:>4} | {'(suma ponderada)':>20} | ${total_l4_actual:>21,} | {'(suma ponderada)':>20} | ${total_l4_objetivo:>21,} | ${total_anexoB:>21,} | {'✅':<7}")
    print("=" * 180)
    
    # EXPLICACIÓN DETALLADA POR FILA
    print("\n\n📋 EXPLICACIÓN DETALLADA DE CADA FILA:")
    print("=" * 180)
    
    for idx, tipo in enumerate(['CALE.n_1+', 'CALE.n_1', 'CALE.n_2**', 'CALE.n_2', 'CALE.n_3', 'CALE.n_C2', 'CALE.n_C3', 'CALE.n_C4', 'CALE.n_C5'], 1):
        data = datos_l3[tipo]
        cant = data['cantidad_municipios']
        unit_actual = data['vr_unitario_l3_actual']
        unit_objetivo = data['vr_unitario_l3_objetivo']
        unit_anexoB = data['vr_unitario_anexoB']
        
        total_actual = unit_actual * cant
        total_objetivo = unit_objetivo * cant
        total_anexo = unit_anexoB * cant
        
        print(f"\n{idx}. {tipo}")
        print("-" * 80)
        print(f"   Cantidad de municipios: {cant}")
        print(f"   Valor unitario L3 (1 edificación): ${unit_objetivo:,}")
        print(f"   ")
        print(f"   CÁLCULO L5 (Total Nacional):")
        print(f"   └─ VR_Total_L4 = VR_Unitario_L3 × Cantidad_Municipios")
        print(f"   └─ VR_Total_L4 = ${unit_objetivo:,} × {cant}")
        print(f"   └─ VR_Total_L4 = ${total_objetivo:,}")
        print(f"   ")
        print(f"   Estado actual ficha:")
        print(f"   └─ VR_Unit_L3_Actual: ${unit_actual:,}")
        print(f"   └─ VR_Total_L4_Actual: ${total_actual:,}")
        print(f"   └─ Cobertura: {(total_actual/total_objetivo*100 if total_objetivo > 0 else 0):.1f}%")
        print(f"   ")
        
        if tipo == 'CALE.n_1+':
            print(f"   Componentes:")
            print(f"   └─ Base CALE.n_1 ($17.312M)")
            print(f"   └─ + 1 pista Clase II adicional ($5.565M)")
            print(f"   └─ = ${unit_objetivo:,} por unidad")
        elif tipo == 'CALE.n_1':
            print(f"   Componentes actuales en ficha:")
            print(f"   └─ 3 pistas (Clase III $1.850M + Clase II $980M + Clase I $750M) = $3.580M")
            print(f"   └─ 1 sala 24 cubículos = $186M")
            print(f"   └─ 1 edificación admin = $2.400M")
            print(f"   └─ TOTAL ACTUAL = $6.166M")
            print(f"   ")
            print(f"   Componentes a AGREGAR para llegar a objetivo $17.312M:")
            print(f"   └─ CALE-T ajustado = $159M (era $243M, menos $84M de C2-C5)")
            print(f"   └─ Componentes CALE-P adicionales = ~$11.146M")
            print(f"   └─ (señalización, equipamiento TIC, mobiliario, instalaciones, etc.)")
        elif tipo == 'CALE.n_2**':
            print(f"   Componentes:")
            print(f"   └─ Base CALE.n_2 ($11.206M)")
            print(f"   └─ + 2 pistas Clase I adicionales ($1.500M × 2 = $3.000M)")
            print(f"   └─ = ${unit_objetivo:,} por unidad")
        elif tipo == 'CALE.n_2':
            print(f"   Componentes:")
            print(f"   └─ Configuración intermedia: 1 pista Clase II + sala 12 cubículos + edificación admin")
            print(f"   └─ Ficha actual incorrecta ($200M) → Corregir a $11.206M")
        elif tipo == 'CALE.n_3':
            print(f"   Componentes:")
            print(f"   └─ Configuración básica: 1 pista Clase I + sala 12 cubículos + edificación admin")
            print(f"   └─ Ficha actual vacía ($0) → Generar completa con $5.641M")
        elif tipo == 'CALE.n_C2':
            print(f"   Componentes estimados:")
            print(f"   └─ Adecuación infraestructura básica (L2)")
            print(f"   └─ Estaciones de trabajo (L1)")
            print(f"   └─ Red local y conectividad (L1)")
            print(f"   └─ Estimado: $30M por unidad")
        elif tipo == 'CALE.n_C3':
            print(f"   Componentes estimados:")
            print(f"   └─ Infraestructura más simple que C2")
            print(f"   └─ Equipamiento reducido")
            print(f"   └─ Estimado: $20M por unidad")
        elif tipo == 'CALE.n_C4':
            print(f"   Componentes estimados:")
            print(f"   └─ Punto remoto con menor equipamiento")
            print(f"   └─ Estimado: $15M por unidad")
        elif tipo == 'CALE.n_C5':
            print(f"   Componentes estimados:")
            print(f"   └─ Infraestructura mínima esencial")
            print(f"   └─ Estimado: $12M por unidad")
    
    print("\n" + "=" * 180)
    print("\n✅ RESUMEN:")
    print(f"   - Cada fila muestra el TOTAL NACIONAL de todas las instancias L4 de ese tipo")
    print(f"   - L4 = Una instancia de L3 en un municipio específico")
    print(f"   - L5 = Suma de todos los L4 = Red Nacional completa")
    print(f"   - Total municipios: {total_mun}")
    print(f"   - Total red nacional (Anexo B): ${total_anexoB:,}")
    print(f"   - Total fichas actual: ${total_l4_actual:,} ({(total_l4_actual/total_anexoB*100):.1f}%)")
    print(f"   - Total fichas objetivo: ${total_l4_objetivo:,} ({(total_l4_objetivo/total_anexoB*100):.1f}%)")
    print()

if __name__ == '__main__':
    generar_tabla_l5_totales()
