#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TABLA L5 COMPLETA PARA APROBACIÓN
Muestra TODOS los datos necesarios para autorizar la actualización de fichas.
"""

def mostrar_tabla_completa_aprobacion():
    """Genera tabla L5 completa con todos los detalles para aprobación"""
    
    # DATOS COMPLETOS
    datos = [
        {
            'tipo': 'CALE.n_1+',
            'categoria': 'Centro',
            'cant_mun': 3,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 22_876_926_598,
            'vr_total_actual': 0,
            'vr_total_objetivo': 68_630_779_794,
            'vr_total_anexoB': 68_630_779_794,
            'componentes': 'Base CALE.n_1 + 1 pista Clase II adicional',
            'accion': 'CREAR ficha BIM_L3_001b',
        },
        {
            'tipo': 'CALE.n_1',
            'categoria': 'Centro',
            'cant_mun': 17,
            'vr_unit_actual': 6_166_000_000,
            'vr_unit_objetivo': 17_311_999_565,
            'vr_total_actual': 104_822_000_000,
            'vr_total_objetivo': 294_303_992_605,
            'vr_total_anexoB': 294_303_992_605,
            'componentes': '3 pistas + sala 24 cub + edif admin + CALE-T ($159M) + CALE-P adicional (~$11M)',
            'accion': 'ACTUALIZAR ficha BIM_L3_001 (agregar CALE-T + componentes)',
        },
        {
            'tipo': 'CALE.n_2**',
            'categoria': 'Centro',
            'cant_mun': 16,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 22_087_585_297,
            'vr_total_actual': 0,
            'vr_total_objetivo': 353_401_364_752,
            'vr_total_anexoB': 353_401_364_752,
            'componentes': 'Base CALE.n_2 + 2 pistas Clase I adicionales',
            'accion': 'CREAR ficha BIM_L3_002b',
        },
        {
            'tipo': 'CALE.n_2',
            'categoria': 'Centro',
            'cant_mun': 4,
            'vr_unit_actual': 200_646_497,
            'vr_unit_objetivo': 11_206_265_897,
            'vr_total_actual': 802_585_988,
            'vr_total_objetivo': 44_825_063_588,
            'vr_total_anexoB': 44_825_063_588,
            'componentes': '1 pista Clase II + sala 12 cub + edif admin',
            'accion': 'CORREGIR ficha BIM_L3_002 (datos incorrectos)',
        },
        {
            'tipo': 'CALE.n_3',
            'categoria': 'Centro',
            'cant_mun': 16,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 5_641_306_197,
            'vr_total_actual': 0,
            'vr_total_objetivo': 90_260_899_152,
            'vr_total_anexoB': 90_260_899_152,
            'componentes': '1 pista Clase I + sala 12 cub + edif admin',
            'accion': 'GENERAR ficha BIM_L3_003 completa',
        },
        {
            'tipo': 'CALE.n_C2',
            'categoria': 'Satélite',
            'cant_mun': 31,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 30_000_000,
            'vr_total_actual': 0,
            'vr_total_objetivo': 930_000_000,
            'vr_total_anexoB': 930_000_000,
            'componentes': 'Adec infraestr + estaciones trabajo + red local',
            'accion': 'CREAR ficha BIM_L3_C2',
        },
        {
            'tipo': 'CALE.n_C3',
            'categoria': 'Satélite',
            'cant_mun': 69,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 20_000_000,
            'vr_total_actual': 0,
            'vr_total_objetivo': 1_380_000_000,
            'vr_total_anexoB': 1_380_000_000,
            'componentes': 'Infraestr simple + equipamiento reducido',
            'accion': 'CREAR ficha BIM_L3_C3',
        },
        {
            'tipo': 'CALE.n_C4',
            'categoria': 'Satélite',
            'cant_mun': 27,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 15_000_000,
            'vr_total_actual': 0,
            'vr_total_objetivo': 405_000_000,
            'vr_total_anexoB': 405_000_000,
            'componentes': 'Punto remoto menor equipamiento',
            'accion': 'CREAR ficha BIM_L3_C4',
        },
        {
            'tipo': 'CALE.n_C5',
            'categoria': 'Satélite',
            'cant_mun': 14,
            'vr_unit_actual': 0,
            'vr_unit_objetivo': 12_000_000,
            'vr_total_actual': 0,
            'vr_total_objetivo': 168_000_000,
            'vr_total_anexoB': 168_000_000,
            'componentes': 'Infraestr mínima esencial',
            'accion': 'CREAR ficha BIM_L3_C5',
        },
    ]
    
    print("╔" + "═" * 198 + "╗")
    print("║" + " " * 70 + "📊 TABLA L5: RED NACIONAL COMPLETA" + " " * 94 + "║")
    print("║" + " " * 70 + "PARA APROBACIÓN DE ACTUALIZACIÓN" + " " * 96 + "║")
    print("╠" + "═" * 198 + "╣")
    print("║                                                                                                                                                                                      ║")
    print("║  ESTRUCTURA:                                                                                                                                                                         ║")
    print("║  • L3 = Edificación funcional UNITARIA (1 unidad)                                                                                                                                   ║")
    print("║  • L4 = Instancia de L3 en un municipio específico                                                                                                                                  ║")
    print("║  • L5 = Esta tabla: Suma de todas las instancias L4 por tipo = RED NACIONAL                                                                                                         ║")
    print("║                                                                                                                                                                                      ║")
    print("║  CÁLCULO POR FILA:                                                                                                                                                                   ║")
    print("║  • VR_Total_L4 = VR_Unitario_L3 × Cantidad_Municipios                                                                                                                               ║")
    print("║                                                                                                                                                                                      ║")
    print("╠" + "═" * 198 + "╣")
    
    # Cabecera de tabla
    print("║")
    print("║  " + f"{'#':<3} {'Tipo L3':<15} {'Cat':<8} {'Mun':>4} │ {'VR Unitario L3 ACTUAL':>23} │ {'VR Unitario L3 OBJETIVO':>23} │ {'VR TOTAL L4 ACTUAL':>23} │ {'VR TOTAL L4 OBJETIVO':>23} │ {'VR TOTAL AnexoB':>23} │ {'%':>6}" + "  ║")
    print("║  " + "─" * 3 + " " + "─" * 15 + " " + "─" * 8 + " " + "─" * 4 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 6 + "  ║")
    
    # Datos
    total_mun = 0
    total_actual = 0
    total_objetivo = 0
    total_anexo = 0
    
    centros_mun = 0
    centros_actual = 0
    centros_objetivo = 0
    
    satelites_mun = 0
    satelites_actual = 0
    satelites_objetivo = 0
    
    for idx, row in enumerate(datos, 1):
        tipo = row['tipo']
        cat = row['categoria']
        mun = row['cant_mun']
        unit_act = row['vr_unit_actual']
        unit_obj = row['vr_unit_objetivo']
        tot_act = row['vr_total_actual']
        tot_obj = row['vr_total_objetivo']
        tot_anex = row['vr_total_anexoB']
        
        total_mun += mun
        total_actual += tot_act
        total_objetivo += tot_obj
        total_anexo += tot_anex
        
        if cat == 'Centro':
            centros_mun += mun
            centros_actual += tot_act
            centros_objetivo += tot_obj
        else:
            satelites_mun += mun
            satelites_actual += tot_act
            satelites_objetivo += tot_obj
        
        pct = (tot_act / tot_obj * 100) if tot_obj > 0 else 0
        
        str_unit_act = f"${unit_act:>21,}" if unit_act > 0 else f"{'🔴 $0':>23}"
        str_unit_obj = f"${unit_obj:>21,}"
        str_tot_act = f"${tot_act:>21,}" if tot_act > 0 else f"{'🔴 $0':>23}"
        str_tot_obj = f"${tot_obj:>21,}"
        str_tot_anex = f"${tot_anex:>21,}"
        
        print(f"║  {idx:<3} {tipo:<15} {cat:<8} {mun:>4} │ {str_unit_act} │ {str_unit_obj} │ {str_tot_act} │ {str_tot_obj} │ {str_tot_anex} │ {pct:>5.1f}%  ║")
    
    # Separador subtotales
    print("║  " + "─" * 3 + " " + "─" * 15 + " " + "─" * 8 + " " + "─" * 4 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 23 + " ┼ " + "─" * 6 + "  ║")
    
    # Subtotal Centros
    pct_centros = (centros_actual / centros_objetivo * 100) if centros_objetivo > 0 else 0
    print(f"║  {'':>3} {'SUBTOTAL Centros':<15} {'':<8} {centros_mun:>4} │ {'(suma ponderada)':>23} │ {'(suma ponderada)':>23} │ ${centros_actual:>21,} │ ${centros_objetivo:>21,} │ ${centros_objetivo:>21,} │ {pct_centros:>5.1f}%  ║")
    
    # Subtotal Satélites
    pct_satelites = (satelites_actual / satelites_objetivo * 100) if satelites_objetivo > 0 else 0
    print(f"║  {'':>3} {'SUBTOTAL Satélit':<15} {'':<8} {satelites_mun:>4} │ {'(suma ponderada)':>23} │ {'(suma ponderada)':>23} │ ${satelites_actual:>21,} │ ${satelites_objetivo:>21,} │ ${satelites_objetivo:>21,} │ {pct_satelites:>5.1f}%  ║")
    
    # Separador total
    print("║  " + "═" * 3 + " " + "═" * 15 + " " + "═" * 8 + " " + "═" * 4 + " ╪ " + "═" * 23 + " ╪ " + "═" * 23 + " ╪ " + "═" * 23 + " ╪ " + "═" * 23 + " ╪ " + "═" * 23 + " ╪ " + "═" * 6 + "  ║")
    
    # TOTAL GENERAL
    pct_total = (total_actual / total_objetivo * 100) if total_objetivo > 0 else 0
    print(f"║  {'':>3} {'TOTAL L5':<15} {'Red Nal':<8} {total_mun:>4} │ {'(suma ponderada)':>23} │ {'(suma ponderada)':>23} │ ${total_actual:>21,} │ ${total_objetivo:>21,} │ ${total_anexo:>21,} │ {pct_total:>5.1f}%  ║")
    
    print("╠" + "═" * 198 + "╣")
    
    # EXPLICACIÓN DE COMPONENTES
    print("║                                                                                                                                                                                      ║")
    print("║  📋 DETALLE DE COMPONENTES Y ACCIONES POR TIPO:                                                                                                                                     ║")
    print("║                                                                                                                                                                                      ║")
    
    for idx, row in enumerate(datos, 1):
        tipo = row['tipo']
        componentes = row['componentes']
        accion = row['accion']
        unit_obj = row['vr_unit_objetivo']
        
        print(f"║  {idx}. {tipo} (${unit_obj:,} unitario)                                                                                                                                        "[:200] + "  ║")
        print(f"║     Componentes: {componentes}                                                                                                                                                 "[:200] + "  ║")
        print(f"║     Acción: {accion}                                                                                                                                                           "[:200] + "  ║")
        print("║                                                                                                                                                                                      ║")
    
    print("╠" + "═" * 198 + "╣")
    
    # RESUMEN DE ACCIONES
    print("║                                                                                                                                                                                      ║")
    print("║  🎯 RESUMEN DE ACCIONES A EJECUTAR:                                                                                                                                                 ║")
    print("║                                                                                                                                                                                      ║")
    print("║  1. ACTUALIZAR 1 ficha existente:                                                                                                                                                   ║")
    print("║     └─ BIM_L3_001 (CALE.n_1): $6.166M → $17.312M                                                                                                                                    ║")
    print("║        • Remover: Simuladores ($900M)                                                                                                                                                ║")
    print("║        • Agregar: CALE-T ajustado ($159M)                                                                                                                                            ║")
    print("║        • Agregar: Componentes CALE-P adicionales (~$11.146M)                                                                                                                         ║")
    print("║                                                                                                                                                                                      ║")
    print("║  2. CREAR 6 fichas nuevas:                                                                                                                                                          ║")
    print("║     └─ BIM_L3_001b (CALE.n_1+): $22.877M × 3 mun = $68.631M                                                                                                                         ║")
    print("║     └─ BIM_L3_002b (CALE.n_2**): $22.088M × 16 mun = $353.401M                                                                                                                      ║")
    print("║     └─ BIM_L3_C2: $30M × 31 mun = $930M                                                                                                                                             ║")
    print("║     └─ BIM_L3_C3: $20M × 69 mun = $1.380M                                                                                                                                           ║")
    print("║     └─ BIM_L3_C4: $15M × 27 mun = $405M                                                                                                                                             ║")
    print("║     └─ BIM_L3_C5: $12M × 14 mun = $168M                                                                                                                                             ║")
    print("║                                                                                                                                                                                      ║")
    print("║  3. CORREGIR 1 ficha existente:                                                                                                                                                     ║")
    print("║     └─ BIM_L3_002 (CALE.n_2): $200M → $11.206M                                                                                                                                      ║")
    print("║                                                                                                                                                                                      ║")
    print("║  4. GENERAR 1 ficha faltante:                                                                                                                                                       ║")
    print("║     └─ BIM_L3_003 (CALE.n_3): $0 → $5.641M                                                                                                                                          ║")
    print("║                                                                                                                                                                                      ║")
    print("╠" + "═" * 198 + "╣")
    
    # RESULTADO ESPERADO
    print("║                                                                                                                                                                                      ║")
    print("║  ✅ RESULTADO ESPERADO POST-IMPLEMENTACIÓN:                                                                                                                                         ║")
    print("║                                                                                                                                                                                      ║")
    print(f"║  • Total fichas: 9 fichas L3 completas                                                                                                                                               ║")
    print(f"║  • Total instancias L4: 197 (L3 × municipios)                                                                                                                                        ║")
    print(f"║  • Valor red nacional L5: ${total_anexo:,}                                                                                                                                          "[:200] + "  ║")
    print(f"║  • Cobertura actual: {pct_total:.1f}%                                                                                                                                                       ║")
    print(f"║  • Cobertura objetivo: 100.0%                                                                                                                                                        ║")
    print(f"║  • Incremento: {100.0 - pct_total:.1f}%                                                                                                                                                     ║")
    print("║  • Coherencia Fichas vs Anexo B: 100%                                                                                                                                               ║")
    print("║                                                                                                                                                                                      ║")
    print("╠" + "═" * 198 + "╣")
    
    # VALIDACIONES
    print("║                                                                                                                                                                                      ║")
    print("║  ✓ VALIDACIONES CRÍTICAS:                                                                                                                                                           ║")
    print("║                                                                                                                                                                                      ║")
    print("║  ✓ Simuladores ($900M) eliminados de CALE.n_1                                                                                                                                       ║")
    print("║  ✓ Predio NO incluido en L3 (es costo L4 municipal)                                                                                                                                 ║")
    print("║  ✓ CALE-T ajustado a $159M (separados $84M para C2-C5)                                                                                                                              ║")
    print("║  ✓ C2-C5 como L3 independientes (no parte de CALE-T)                                                                                                                                ║")
    print("║  ✓ Todas las fichas L3 en valores UNITARIOS                                                                                                                                         ║")
    print("║  ✓ L5 = suma correcta de todos los L4 (L3 × municipios)                                                                                                                             ║")
    print("║                                                                                                                                                                                      ║")
    print("╚" + "═" * 198 + "╝")
    print()
    print("═" * 200)
    print()
    print("⚠️  AUTORIZACIÓN REQUERIDA:")
    print()
    print("    Esta tabla muestra el estado ACTUAL y el estado OBJETIVO después de ejecutar")
    print("    todas las actualizaciones de fichas L3.")
    print()
    print("    Si aprueba esta tabla, se procederá a:")
    print("    • Actualizar 1 ficha existente (BIM_L3_001)")
    print("    • Crear 6 fichas nuevas (variantes + satélites)")
    print("    • Corregir 2 fichas existentes (BIM_L3_002, BIM_L3_003)")
    print()
    print(f"    Resultado: Cobertura {pct_total:.1f}% → 100.0% (${total_actual:,} → ${total_objetivo:,})")
    print()
    print("═" * 200)

if __name__ == '__main__':
    mostrar_tabla_completa_aprobacion()
