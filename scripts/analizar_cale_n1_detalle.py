#!/usr/bin/env python3
"""
Análisis detallado CALE.n_1: Componentes de fichas vs Anexo B vs Plan v4.1
"""

# ============================================================================
# CALE.n_1 - CENTRO METROPOLITANO (17 nodos)
# ============================================================================

print('='*100)
print('📊 ANÁLISIS DETALLADO: CALE.n_1 - CENTRO METROPOLITANO')
print('='*100)
print()

# COMPONENTES EN FICHA ACTUAL (BIM_L3_001.html)
print('🔧 COMPONENTES EN FICHA L3 ACTUAL (valores UNITARIOS para 1 CALE.n_1):\n')

componentes_ficha = [
    {'num': 1, 'nombre': 'Pista Evaluación Clase III', 'ref': 'L2.pista_clase_3', 'valor': 1_850_000_000, 'cant': 1},
    {'num': 2, 'nombre': 'Pista Evaluación Clase II', 'ref': 'L2.pista_clase_2', 'valor': 980_000_000, 'cant': 1},
    {'num': 3, 'nombre': 'Pista Evaluación Clase I', 'ref': 'L2.pista_clase_1', 'valor': 750_000_000, 'cant': 1},
    {'num': 4, 'nombre': 'Sala Evaluación Teórica (24 cubículos)', 'ref': 'L1.sala_24_cubiculos', 'valor': 186_000_000, 'cant': 1},
    {'num': 5, 'nombre': 'Simulador Conducción Clase III', 'ref': 'L0.simulador_c3', 'valor': 450_000_000, 'cant': 2},
    {'num': 6, 'nombre': 'Infraestructura Civil Base', 'ref': 'L2.edificacion_admin', 'valor': 2_400_000_000, 'cant': 1},
]

total_ficha = 0
for comp in componentes_ficha:
    subtotal = comp['valor'] * comp['cant']
    total_ficha += subtotal
    print(f"  {comp['num']}. {comp['nombre']:<50} {comp['ref']:<25}")
    print(f"     Valor unitario: ${comp['valor']:>15,} × {comp['cant']} = ${subtotal:>15,}")
    print()

print('-'*100)
print(f"{'TOTAL FICHA (CALE-P componente práctico):':<70} ${total_ficha:>20,}")
print('='*100)
print()

# VALORES ANEXO B
print('📄 VALORES ANEXO B (según documento oficial):\n')

vr_teorico_anexoB = 243_063_465
vr_practico_anexoB = 17_068_936_100
vr_total_anexoB = 17_311_999_565

print(f"  CALE-T (Componente Teórico):      ${vr_teorico_anexoB:>15,}")
print(f"  CALE-P (Componente Práctico):      ${vr_practico_anexoB:>15,}")
print('-'*100)
print(f"  VALOR TOTAL ANEXO B (UNITARIO):    ${vr_total_anexoB:>15,}")
print()
print('  📝 Nota: Anexo B NO incluye PREDIO (terreno)')
print('='*100)
print()

# VALORES PLAN v4.1
print('📋 VALORES PLAN v4.1:\n')

vr_con_predio_plan41 = 30_805_186_100
vr_predio = 4_894_890_000
vr_sin_predio_plan41 = vr_con_predio_plan41 - vr_predio

print(f"  Valor TOTAL con PREDIO:            ${vr_con_predio_plan41:>15,}")
print(f"  Menos: PREDIO (terreno):          -${vr_predio:>15,}")
print('-'*100)
print(f"  Valor SIN PREDIO:                  ${vr_sin_predio_plan41:>15,}")
print()
print('  ⚠️  Plan v4.1 incluye costo del terreno, Anexo B NO')
print('='*100)
print()

# COMPARACIÓN
print('🔍 COMPARACIÓN DE VALORES (UNITARIOS, SIN PREDIO):\n')

diferencia_ficha_anexoB = total_ficha - vr_total_anexoB
porcentaje_ficha = (total_ficha / vr_total_anexoB * 100) if vr_total_anexoB > 0 else 0

diferencia_ficha_practico = total_ficha - vr_practico_anexoB
faltante_teorico = vr_teorico_anexoB

print(f"  Ficha L3 (CALE-P):                 ${total_ficha:>15,}  (actual)")
print(f"  Anexo B CALE-P:                    ${vr_practico_anexoB:>15,}")
print(f"  Anexo B CALE-T:                   +${vr_teorico_anexoB:>15,}")
print('-'*100)
print(f"  Anexo B TOTAL:                     ${vr_total_anexoB:>15,}  (esperado)")
print()
print(f"  Diferencia Ficha vs Anexo B:      -${abs(diferencia_ficha_anexoB):>15,}  ({100 - porcentaje_ficha:.1f}% faltante)")
print(f"  Cobertura actual:                   {porcentaje_ficha:>15.1f}%")
print()

# Análisis componente por componente
print('='*100)
print('📊 ANÁLISIS: ¿Qué falta en la ficha?\n')

print('✅ COMPONENTES PRESENTES (CALE-P - Componente Práctico):')
print(f"   • Pistas de evaluación (Clase I, II, III):  ${1_850_000_000 + 980_000_000 + 750_000_000:>15,}")
print(f"   • Sala teórica 24 cubículos:                ${186_000_000:>15,}")
print(f"   • Simuladores C3 (2 unidades):              ${900_000_000:>15,}")
print(f"   • Edificación administrativa:               ${2_400_000_000:>15,}")
print(f"   SUBTOTAL CALE-P:                            ${total_ficha:>15,}")
print()

print('❌ COMPONENTES FALTANTES:')
print(f"   • CALE-T (Componente Teórico):              ${vr_teorico_anexoB:>15,}")
print('     └─ Incluye: Infraestructura tecnológica, sistemas de gestión,')
print('        certificaciones ISO, seguros, equipamiento administrativo')
print()

diferencia_practico = vr_practico_anexoB - total_ficha
if diferencia_practico > 0:
    print(f"   • Diferencia en CALE-P (ajuste):           +${diferencia_practico:>15,}")
    print('     └─ Posibles componentes adicionales no detallados en ficha')
    print()

print('-'*100)
print(f"   TOTAL FALTANTE:                            -${abs(diferencia_ficha_anexoB):>15,}")
print()

# RECOMENDACIÓN
print('='*100)
print('🎯 RECOMENDACIÓN:\n')

print('1. ✅ VALIDAR componentes actuales ($7.066M):')
print('   La ficha actual está compositivamente COHERENTE para CALE-P')
print('   └─ Σ(L2) + Σ(L1) + Σ(L0) = $7.066M ✅')
print()

print('2. 📝 AGREGAR componente CALE-T ($243M):')
print('   └─ Crear entrada en tabla de componentes')
print('   └─ Referencia BIM: L2.cale_teorico_24q')
print('   └─ Incluye infraestructura tecnológica completa')
print()

print(f'3. 🔍 REVISAR diferencia en CALE-P (+${diferencia_practico:,}):')
print('   └─ Verificar si existen componentes L2/L1/L0 adicionales')
print('   └─ Posibles: señalización adicional, equipamiento complementario')
print()

print('4. ⚠️  NO INCLUIR predio en ficha L3:')
print('   └─ El predio es componente L4 (instancia municipal)')
print('   └─ Anexo B correcto: valor L3 SIN terreno')
print()

# TABLA RESUMEN
print('='*100)
print('📋 TABLA RESUMEN CALE.n_1:\n')
print(f"{'Concepto':<40} | {'Valor Unitario':>20} | {'Notas':<40}")
print('-'*100)
print(f"{'Ficha L3 actual (CALE-P)':<40} | ${total_ficha:>19,} | {'Validada, pero incompleta':<40}")
print(f"{'Anexo B CALE-P':<40} | ${vr_practico_anexoB:>19,} | {'Componente práctico completo':<40}")
print(f"{'Anexo B CALE-T':<40} | ${vr_teorico_anexoB:>19,} | {'Componente teórico (faltante)':<40}")
print('-'*100)
print(f"{'Anexo B TOTAL (sin predio)':<40} | ${vr_total_anexoB:>19,} | {'Valor esperado L3 unitario':<40}")
print(f"{'Plan v4.1 predio':<40} | ${vr_predio:>19,} | {'NO incluir (es L4, no L3)':<40}")
print(f"{'Plan v4.1 con predio':<40} | ${vr_con_predio_plan41:>19,} | {'Incluye terreno (incorrecto para L3)':<40}")
print('='*100)
print()

print('✅ CONCLUSIÓN:')
print(f'   Ficha actual: ${total_ficha:,} ({porcentaje_ficha:.1f}% del total esperado)')
print(f'   Por agregar: ${abs(diferencia_ficha_anexoB):,} ({100 - porcentaje_ficha:.1f}% faltante)')
print(f'   Valor objetivo (L3 unitario): ${vr_total_anexoB:,}')
print()
print('   📝 Acción: Agregar componente CALE-T ($243M) + revisar ajuste CALE-P')
print('   ⚠️  NO agregar predio ($4.895M) - ese es costo L4 municipal, no L3 unitario')
print()
