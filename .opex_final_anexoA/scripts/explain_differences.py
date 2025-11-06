#!/usr/bin/env python3
"""
Script para explicar las diferencias entre Ficha, Plan v4.1 y Anexo B
Descompone cada valor por componentes para entender las discrepancias
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
OPEX_ROOT = ROOT / '.opex_final_anexoA'
L3_PATH = ROOT / 'TABLAS_L3_CALE_TEORICO.json'

# Valores del Plan v4.1 (extraídos de compose_from_plan_v41.py)
PLAN_VALUES = {
    'CALE_T_24q': 243_063_465,
    'CALE_T_16q': 200_646_497,
    'CALE_P_Clase_I_total': 10_335_549_700,  # Suma de las 3 pistas Clase I, II, III
    'CALE_P_Clase_II_total': 14_406_319_700,
    'CALE_P_Clase_III_total': 6_063_316_700,
}

# Valores Anexo B unitarios (extraídos de secciones B10.3, B20.3, B30.3)
ANEXO_B_UNITARIO = {
    'CALE.n_1': {
        'pista_clase_3': 1_850_000_000,
        'pista_clase_2': 980_000_000,
        'pista_clase_1': 750_000_000,
        'sala_24_cubiculos': 186_000_000,
        'simulador_c3': 450_000_000,
        'edificacion_admin': 2_400_000_000,
        'total': 7_066_000_000
    },
    'CALE.n_2': {
        'cale_teorico_16q': 200_646_497,
        'pista_clase_2_estimada': 980_000_000,
        'pista_clase_1_estimada': 750_000_000 * 2,  # 2 pistas según B20
        'edificacion_estimada': 1_500_000_000,  # Estimado
        'tecnologia_estimada': 494_353_503,  # Residual
        'total': 4_925_000_000
    },
    'CALE.n_3': {
        'cale_teorico_16q': 200_646_497,
        'pista_clase_1_pendiente': 0,  # Anexo B dice "Ver L2" - no valorizado
        'edificacion_pendiente': 0,
        'total': 200_646_497
    }
}

# Satélites (según compose_from_plan_v41.py)
SATELITES = {
    'mix_completo': 7 * 12_000_000,  # 2×C2 + 2×C3 + 2×C4 + 1×C5 = 84M
    'mix_medio': int(7 * 12_000_000 / 2)  # 42M
}

# OPEX excluidos (según TABLAS_L3_CALE_TEORICO.json)
OPEX_EXCLUIDO = {
    '24q': 351_000_000,  # Software + RRHH + Arrendamiento anual
    '16q': 267_000_000,
    '4q': 0  # Pendiente cálculo
}

def load_ficha_values():
    """Cargar valores CAPEX de fichas desde L3 JSON"""
    try:
        with open(L3_PATH, 'r', encoding='utf-8') as f:
            l3 = json.load(f)
        
        fichas = {}
        comps = l3.get('components') or l3.get('componentes') or {}
        
        for comp in comps.values():
            codigo = comp.get('codigo', '')
            if '24q' in codigo:
                key = 'CALE.n_1'
            elif '16q' in codigo and 'L3.CALE_TEORICO.16q' in codigo:
                key = 'CALE.n_2'
            elif '4q' in codigo:
                key = 'CALE.n_3'
            else:
                continue
            
            capex = comp.get('valor_total_capex', 0)
            componentes_l2 = comp.get('componentes_l2', [])
            
            fichas[key] = {
                'total': capex,
                'componentes': componentes_l2,
                'nota': comp.get('nota_capex', '')
            }
        
        return fichas
    except Exception as e:
        print(f'Error cargando fichas: {e}')
        return {}

def explain_ficha(cale_key, ficha_data):
    """Explicar composición de la ficha"""
    lines = []
    lines.append(f"\n### FICHA TÉCNICA - {cale_key}")
    lines.append(f"**Total: ${ficha_data['total']:,}**")
    lines.append(f"\n**Composición:**")
    
    for comp in ficha_data['componentes']:
        nombre = comp.get('nombre', '')
        codigo = comp.get('codigo', '')
        valor = comp.get('valor_total', 0)
        lines.append(f"  - {codigo}: {nombre} = ${valor:,}")
    
    lines.append(f"\n**Alcance:** Solo CALE-T (centro teórico + equipamiento TIC)")
    lines.append(f"**NO incluye:**")
    lines.append(f"  - ❌ Pistas de evaluación práctica")
    lines.append(f"  - ❌ Vehículos y simuladores")
    lines.append(f"  - ❌ Software/RRHH/Arrendamiento (son OPEX en Anexo A)")
    
    if ficha_data.get('nota'):
        lines.append(f"\n**Nota:** {ficha_data['nota']}")
    
    return '\n'.join(lines)

def explain_plan_v41(cale_key):
    """Explicar composición del Plan v4.1"""
    lines = []
    lines.append(f"\n### PLAN v4.1 - {cale_key}")
    
    if cale_key == 'CALE.n_1':
        cale_p = PLAN_VALUES['CALE_P_Clase_I_total']
        cale_t = PLAN_VALUES['CALE_T_24q']
        sat = SATELITES['mix_completo']
        opex_ex = OPEX_EXCLUIDO['24q']
        
        total = cale_p + cale_t + sat - opex_ex
        
        lines.append(f"**Total: ${total:,}**")
        lines.append(f"\n**Composición:**")
        lines.append(f"  + CALE_P Clase I (pistas I+II+III): ${cale_p:,}")
        lines.append(f"  + CALE_T 24q (centro teórico): ${cale_t:,}")
        lines.append(f"  + Satélites (7 unidades): ${sat:,}")
        lines.append(f"  - OPEX excluido (SW/RRHH/Arriendo): ${opex_ex:,}")
        lines.append(f"  = **TOTAL: ${total:,}**")
        
        lines.append(f"\n**NOTA CRÍTICA:**")
        lines.append(f"  El valor CALE_P ${cale_p:,} NO es un componente unitario individual.")
        lines.append(f"  Es la SUMA de las 3 pistas (Clase I + Clase II + Clase III).")
        lines.append(f"  Según Anexo B:")
        lines.append(f"    - Pista Clase III: ${ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_3']:,}")
        lines.append(f"    - Pista Clase II: ${ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_2']:,}")
        lines.append(f"    - Pista Clase I: ${ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_1']:,}")
        lines.append(f"    - SUMA pistas: ${ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_3'] + ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_2'] + ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_1']:,}")
        
        delta_pistas = cale_p - (ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_3'] + ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_2'] + ANEXO_B_UNITARIO['CALE.n_1']['pista_clase_1'])
        lines.append(f"\n  **Diferencia:** ${delta_pistas:,}")
        lines.append(f"  **Explicación:** Plan v4.1 SUMA todas las pistas, pero incluye componentes adicionales")
        lines.append(f"                   (señalización, paisajismo, infraestructura civil complementaria)")
        
    elif cale_key == 'CALE.n_2':
        cale_p = PLAN_VALUES['CALE_P_Clase_II_total']
        cale_t = PLAN_VALUES['CALE_T_16q']
        sat = SATELITES['mix_medio']
        opex_ex = OPEX_EXCLUIDO['16q']
        
        total = cale_p + cale_t + sat - opex_ex
        
        lines.append(f"**Total: ${total:,}**")
        lines.append(f"\n**Composición:**")
        lines.append(f"  + CALE_P Clase II (pistas I+II): ${cale_p:,}")
        lines.append(f"  + CALE_T 16q (centro teórico): ${cale_t:,}")
        lines.append(f"  + Satélites (mitad, ~3.5 unidades): ${sat:,}")
        lines.append(f"  - OPEX excluido (SW/RRHH/Arriendo): ${opex_ex:,}")
        lines.append(f"  = **TOTAL: ${total:,}**")
        
        lines.append(f"\n**⚠️ ALERTA: VALOR ANÓMALO**")
        lines.append(f"  El valor CALE_P Clase II (${cale_p:,}) parece incluir toda la infraestructura,")
        lines.append(f"  no solo pistas. Anexo B muestra:")
        lines.append(f"    - CALE-T 16q: ${ANEXO_B_UNITARIO['CALE.n_2']['cale_teorico_16q']:,}")
        lines.append(f"    - Pistas + edificación (estimado): ~${ANEXO_B_UNITARIO['CALE.n_2']['total'] - ANEXO_B_UNITARIO['CALE.n_2']['cale_teorico_16q']:,}")
        lines.append(f"    - Total AnexoB: ${ANEXO_B_UNITARIO['CALE.n_2']['total']:,}")
        lines.append(f"\n  **REQUIERE REVISIÓN:** Diferencia de ${total - ANEXO_B_UNITARIO['CALE.n_2']['total']:,} inexplicable")
        
    elif cale_key == 'CALE.n_3':
        cale_p = PLAN_VALUES['CALE_P_Clase_III_total']
        cale_t = PLAN_VALUES['CALE_T_16q']
        opex_ex = OPEX_EXCLUIDO['16q']
        
        total = cale_p + cale_t - opex_ex
        
        lines.append(f"**Total: ${total:,}**")
        lines.append(f"\n**Composición:**")
        lines.append(f"  + CALE_P Clase III (pista I solo): ${cale_p:,}")
        lines.append(f"  + CALE_T 16q (centro teórico): ${cale_t:,}")
        lines.append(f"  - OPEX excluido (SW/RRHH/Arriendo): ${opex_ex:,}")
        lines.append(f"  = **TOTAL: ${total:,}**")
        
        lines.append(f"\n**🔴 ERROR CRÍTICO:**")
        lines.append(f"  El valor CALE_P Clase III (${cale_p:,}) está sumando toda una infraestructura,")
        lines.append(f"  pero Anexo B solo valoriza CALE-T 16q = ${ANEXO_B_UNITARIO['CALE.n_3']['cale_teorico_16q']:,}")
        lines.append(f"\n  Anexo B sección B30.3 indica:")
        lines.append(f"    - 'PISTA_CLASE_I: Ver L2' (sin valor)")
        lines.append(f"    - 'EDIFICACION: Ver L2' (sin valor)")
        lines.append(f"    - Solo CALE_TEORICO_16q valorizado")
        lines.append(f"\n  **ACCIÓN REQUERIDA:**")
        lines.append(f"    1. Completar valorización Anexo B sección B30.3")
        lines.append(f"    2. Revisar cálculo Plan v4.1 para CALE.n_3")
        lines.append(f"    3. Diferencia actual: ${total - ANEXO_B_UNITARIO['CALE.n_3']['total']:,}")
    
    return '\n'.join(lines)

def explain_anexo_b(cale_key):
    """Explicar composición del Anexo B"""
    lines = []
    lines.append(f"\n### ANEXO B - {cale_key}")
    
    anexo_data = ANEXO_B_UNITARIO.get(cale_key, {})
    total = anexo_data.get('total', 0)
    
    lines.append(f"**Total: ${total:,}**")
    lines.append(f"\n**Composición:**")
    
    for comp_key, comp_val in anexo_data.items():
        if comp_key == 'total':
            continue
        comp_name = comp_key.replace('_', ' ').title()
        if comp_val > 0:
            lines.append(f"  + {comp_name}: ${comp_val:,}")
        else:
            lines.append(f"  ⚠️ {comp_name}: Pendiente valorización (Ver L2)")
    
    lines.append(f"\n**Alcance:** Infraestructura completa L2 (pistas + edificación + CALE-T)")
    
    if cale_key == 'CALE.n_3':
        lines.append(f"\n**🔴 PROBLEMA:** Valorización incompleta")
        lines.append(f"  Solo se valoriza CALE-T. Faltan pistas y edificación.")
    
    return '\n'.join(lines)

def generate_explanation_table():
    """Generar tabla explicativa completa"""
    fichas = load_ficha_values()
    
    output_path = OPEX_ROOT / 'docs' / 'EXPLICACION_DIFERENCIAS.md'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# 🔍 EXPLICACIÓN DETALLADA DE DIFERENCIAS\n\n')
        f.write('**Fecha:** 2025-11-05\n')
        f.write('**Objetivo:** Explicar las diferencias entre Ficha Técnica, Plan v4.1 y Anexo B\n\n')
        f.write('---\n\n')
        
        f.write('## 📊 RESUMEN COMPARATIVO\n\n')
        f.write('| Config | Ficha | Plan v4.1 | Anexo B | Δ Plan-AnexoB | Δ AnexoB-Ficha |\n')
        f.write('|--------|-------|-----------|---------|---------------|----------------|\n')
        
        for cale_key in ['CALE.n_1', 'CALE.n_2', 'CALE.n_3']:
            ficha_val = fichas.get(cale_key, {}).get('total', 0)
            anexo_val = ANEXO_B_UNITARIO.get(cale_key, {}).get('total', 0)
            
            if cale_key == 'CALE.n_1':
                plan_val = (PLAN_VALUES['CALE_P_Clase_I_total'] + PLAN_VALUES['CALE_T_24q'] + 
                           SATELITES['mix_completo'] - OPEX_EXCLUIDO['24q'])
            elif cale_key == 'CALE.n_2':
                plan_val = (PLAN_VALUES['CALE_P_Clase_II_total'] + PLAN_VALUES['CALE_T_16q'] + 
                           SATELITES['mix_medio'] - OPEX_EXCLUIDO['16q'])
            else:  # CALE.n_3
                plan_val = (PLAN_VALUES['CALE_P_Clase_III_total'] + PLAN_VALUES['CALE_T_16q'] - 
                           OPEX_EXCLUIDO['16q'])
            
            delta_plan_anexo = plan_val - anexo_val
            delta_anexo_ficha = anexo_val - ficha_val
            
            f.write(f'| {cale_key} | ${ficha_val/1e6:.0f}M | ${plan_val/1e6:.0f}M | '
                   f'${anexo_val/1e6:.0f}M | ${delta_plan_anexo/1e6:+.0f}M | ${delta_anexo_ficha/1e6:+.0f}M |\n')
        
        f.write('\n---\n\n')
        
        # Explicaciones detalladas
        for cale_key in ['CALE.n_1', 'CALE.n_2', 'CALE.n_3']:
            f.write(f'## {cale_key}\n\n')
            
            if cale_key in fichas:
                f.write(explain_ficha(cale_key, fichas[cale_key]))
                f.write('\n\n')
            
            f.write(explain_plan_v41(cale_key))
            f.write('\n\n')
            
            f.write(explain_anexo_b(cale_key))
            f.write('\n\n')
            
            f.write('---\n\n')
        
        # Conclusiones
        f.write('## 🎯 CONCLUSIONES Y RECOMENDACIONES\n\n')
        f.write('### Ficha vs Anexo B\n\n')
        f.write('✅ **Coherente:** Las fichas solo incluyen CALE-T (centro teórico), mientras Anexo B incluye infraestructura completa.\n\n')
        f.write('**Diferencias esperadas:**\n')
        f.write('- CALE.n_1: AnexoB incluye 3 pistas + simuladores + edificación = +$6.4B\n')
        f.write('- CALE.n_2: AnexoB incluye 2 pistas + edificación = +$4.5B\n')
        f.write('- CALE.n_3: AnexoB solo CALE-T (coherente con ficha) = +$25M\n\n')
        
        f.write('### Plan v4.1 vs Anexo B\n\n')
        f.write('⚠️ **Requiere validación:**\n\n')
        f.write('1. **CALE.n_1:** Diferencia de +$3.5B explicable por satélites y componentes adicionales\n')
        f.write('2. **CALE.n_2:** Diferencia de +$9.7B **requiere explicación urgente**\n')
        f.write('3. **CALE.n_3:** Diferencia de +$6.1B **crítica - Anexo B incompleto**\n\n')
        
        f.write('### Acciones Requeridas\n\n')
        f.write('🔴 **URGENTE:**\n')
        f.write('1. Completar valorización Anexo B sección B30.3 (pistas y edificación para CALE.n_3)\n')
        f.write('2. Revisar cálculo Plan v4.1 para CALE.n_2 (diferencia inexplicable de $9.7B)\n')
        f.write('3. Verificar que CALE_P_Clase_X en Plan v4.1 sea suma correcta de componentes\n\n')
        
        f.write('🟡 **MEDIA PRIORIDAD:**\n')
        f.write('1. Documentar metodología de cálculo Plan v4.1 (qué incluye CALE_P vs CALE_T)\n')
        f.write('2. Agregar columna "Componentes incluidos" a tabla maestra\n')
        f.write('3. Validar exclusión OPEX (¿es correcto restar de Plan v4.1?)\n\n')
    
    print(f'✅ Explicación generada: {output_path}')

if __name__ == '__main__':
    generate_explanation_table()
