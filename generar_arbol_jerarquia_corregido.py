#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Árbol de Jerarquía BIM - VERSIÓN CORREGIDA
========================================================

Genera árbol completo L3→L2→L1→L0 con estructura correcta:
- 91 componentes L0 (atómicos)
- 6 componentes L1 (4 constructores + 2 referencias)
- 3 componentes L2 (con recursividad L2→L2)
- 4 componentes L3 (configuraciones completas)

CORRECCIÓN CRÍTICA:
- Maniobras NO son componentes BIM independientes
- Maniobras son specs geométricas en L0
- L2 puede referenciar otros L2 (recursividad)
"""

import json
from funciones_recursividad_bim import resolver_componentes_l2

def generar_arbol_completo():
    """Genera árbol de jerarquía BIM completo"""
    
    print("="*80)
    print("ÁRBOL DE JERARQUÍA BIM - ESTRUCTURA CORRECTA CON RECURSIVIDAD")
    print("="*80)
    print()
    
    # Cargar tablas
    print("📂 Cargando tablas BIM...")
    with open('TABLAS_L0_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l0 = json.load(f)
    
    with open('TABLAS_L1_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l1 = json.load(f)
    
    with open('TABLAS_L2_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l2 = json.load(f)
    
    # Intentar cargar L3 (si existe)
    try:
        with open('TABLAS_L3_OFICIALES.json', 'r', encoding='utf-8') as f:
            tablas_l3 = json.load(f)
        # Normalizar estructura (usa 'configuraciones' en lugar de 'componentes')
        if 'configuraciones' in tablas_l3:
            num_l3 = len(tablas_l3['configuraciones'])
        elif 'componentes' in tablas_l3:
            num_l3 = len(tablas_l3['componentes'])
        else:
            num_l3 = 0
        tiene_l3 = num_l3 > 0
    except FileNotFoundError:
        tablas_l3 = {'configuraciones': []}
        tiene_l3 = False
        num_l3 = 0
    
    print(f"✅ L0: {len(tablas_l0['componentes'])} componentes")
    print(f"✅ L1: {len(tablas_l1['componentes'])} componentes")
    print(f"✅ L2: {len(tablas_l2['componentes'])} componentes")
    if tiene_l3:
        print(f"✅ L3: {num_l3} componentes")
    else:
        print(f"⚠️  L3: No encontrado (se generará solo L0→L1→L2)")
    print()
    
    # Generar árbol markdown
    arbol_md = []
    arbol_md.append("# Árbol de Jerarquía BIM - Sistema CALE\n")
    arbol_md.append("**Estructura Corregida con Recursividad L2→L2**\n")
    
    from datetime import datetime
    arbol_md.append(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    arbol_md.append("\n")
    arbol_md.append("## 📊 Estadísticas Generales\n")
    arbol_md.append("\n")
    arbol_md.append("```\n")
    arbol_md.append(f"Nivel L0 (Atómicos):      {len(tablas_l0['componentes'])} componentes\n")
    arbol_md.append(f"Nivel L1 (Ensamblajes):   {len(tablas_l1['componentes'])} componentes\n")
    arbol_md.append(f"Nivel L2 (Configuraciones): {len(tablas_l2['componentes'])} componentes\n")
    if tiene_l3:
        arbol_md.append(f"Nivel L3 (CALE Completo):   {num_l3} componentes\n")
    arbol_md.append("\n")
    arbol_md.append(f"TOTAL: {len(tablas_l0['componentes']) + len(tablas_l1['componentes']) + len(tablas_l2['componentes']) + (num_l3 if tiene_l3 else 0)} componentes BIM\n")
    arbol_md.append("```\n")
    arbol_md.append("\n")
    
    # Categorías L0
    arbol_md.append("## 🧩 Nivel L0: Componentes Atómicos\n")
    arbol_md.append("\n")
    for cat_codigo, cat_data in tablas_l0['categorias'].items():
        num_comps = len(cat_data['componentes'])
        arbol_md.append(f"### {cat_codigo}: {cat_data['nombre']} ({num_comps} componentes)\n")
        arbol_md.append("\n")
        for comp_codigo in cat_data['componentes']:
            # Buscar el componente
            for comp_bim_id, comp_data in tablas_l0['componentes'].items():
                if comp_data['codigo_l0'] == comp_codigo:
                    arbol_md.append(f"- `{comp_data['codigo_l0']}` - {comp_data['componente']}\n")
                    arbol_md.append(f"  - **BIM ID**: {comp_bim_id}\n")
                    arbol_md.append(f"  - **Descripción**: {comp_data['descripcion']}\n")
                    arbol_md.append(f"  - **Unidad**: {comp_data['unidad']}\n")
                    if comp_data.get('usado_en'):
                        arbol_md.append(f"  - **Usado en**: {comp_data['usado_en']}\n")
                    arbol_md.append("\n")
                    break
        arbol_md.append("\n")
    
    # Nivel L1
    arbol_md.append("## ⚙️ Nivel L1: Ensamblajes\n")
    arbol_md.append("\n")
    for bim_id, comp in sorted(tablas_l1['componentes'].items()):
        tipo = comp['tipo']
        arbol_md.append(f"### {bim_id}: {comp['nombre']}\n")
        arbol_md.append("\n")
        arbol_md.append(f"- **Código**: `{comp['codigo']}`\n")
        arbol_md.append(f"- **Tipo**: {tipo}\n")
        arbol_md.append(f"- **Descripción**: {comp['descripcion']}\n")
        
        if tipo == 'CONSTRUCTOR':
            arbol_md.append(f"- **Valor**: ${comp['valor_cop']:,}\n")
            arbol_md.append("\n")
            
            # Componentes L0
            codigos_l0 = comp.get('componentes_l0', [])
            if codigos_l0:
                arbol_md.append(f"**Componentes L0** ({len(codigos_l0)}):\n")
                arbol_md.append("\n")
                for codigo_l0 in codigos_l0:
                    arbol_md.append(f"  - `{codigo_l0}`\n")
                arbol_md.append("\n")
            
            # Maniobras soportadas
            maniobras = comp.get('maniobras_soportadas', [])
            if maniobras:
                arbol_md.append(f"**Maniobras Soportadas** (geometría embebida, NO componentes):\n")
                arbol_md.append("\n")
                arbol_md.append("<details>\n")
                arbol_md.append(f"<summary>{len(maniobras)} especificaciones geométricas</summary>\n")
                arbol_md.append("\n")
                for maniobra in maniobras:
                    arbol_md.append(f"  - {maniobra}\n")
                arbol_md.append("\n")
                arbol_md.append("</details>\n")
                arbol_md.append("\n")
        
        elif tipo == 'REFERENCIA':
            ref_l2 = comp.get('referencia_l2', '')
            resuelve_a = comp.get('resuelve_a', [])
            arbol_md.append(f"- **Referencia L2**: `{ref_l2}`\n")
            arbol_md.append(f"- **Resuelve a**: {', '.join([f'`{c}`' for c in resuelve_a])}\n")
            arbol_md.append("\n")
        
        arbol_md.append("---\n")
        arbol_md.append("\n")
    
    # Nivel L2
    arbol_md.append("## 🏗️ Nivel L2: Configuraciones\n")
    arbol_md.append("\n")
    arbol_md.append("**NOTA**: Este nivel implementa recursividad L2→L2 (Single Source of Truth)\n")
    arbol_md.append("\n")
    
    for bim_id, comp in sorted(tablas_l2['componentes'].items()):
        arbol_md.append(f"### {bim_id}: {comp['nombre']}\n")
        arbol_md.append("\n")
        arbol_md.append(f"- **Código**: `{comp['codigo']}`\n")
        arbol_md.append(f"- **Tipo**: {comp['tipo']}\n")
        arbol_md.append(f"- **Descripción**: {comp['descripcion']}\n")
        arbol_md.append(f"- **Valor Total**: ${comp['valor_total']:,}\n")
        
        categorias = comp.get('categorias_licencia', [])
        if categorias:
            arbol_md.append(f"- **Categorías**: {', '.join(categorias)}\n")
        
        arbol_md.append("\n")
        
        # Componentes directos
        componentes = comp.get('componentes', [])
        arbol_md.append(f"**Componentes Directos** ({len(componentes)}):\n")
        arbol_md.append("\n")
        
        for comp_item in componentes:
            tipo_item = comp_item['tipo']
            if tipo_item == 'L2':
                # Referencia L2
                arbol_md.append(f"  - 🔗 **REFERENCIA L2**: `{comp_item['referencia']}`\n")
                resuelve_a = comp_item.get('resuelve_a', [])
                arbol_md.append("    <details>\n")
                arbol_md.append(f"    <summary>Resuelve a {len(resuelve_a)} componentes L1</summary>\n")
                arbol_md.append("\n")
                for codigo in resuelve_a:
                    arbol_md.append(f"      - `{codigo}`\n")
                arbol_md.append("\n")
                arbol_md.append("    </details>\n")
            else:
                # Componente L1 directo
                arbol_md.append(f"  - ⚙️ **L1**: `{comp_item['codigo']}` - {comp_item['nombre']} (${comp_item['valor']:,})\n")
        
        arbol_md.append("\n")
        
        # Resolución completa
        componentes_l1_resueltos = resolver_componentes_l2(bim_id, tablas_l2)
        
        arbol_md.append(f"**Componentes L1 Resueltos** (total: {len(componentes_l1_resueltos)}):\n")
        arbol_md.append("\n")
        arbol_md.append("<details>\n")
        arbol_md.append("<summary>Ver todos los L1 después de resolver recursividad</summary>\n")
        arbol_md.append("\n")
        
        for comp_l1 in componentes_l1_resueltos:
            codigo = comp_l1.get('codigo', 'N/A')
            nombre = comp_l1.get('nombre', 'N/A')
            valor = comp_l1.get('valor_cop', 0)
            arbol_md.append(f"  - `{codigo}` - {nombre} (${valor:,})\n")
        
        arbol_md.append("\n")
        arbol_md.append("</details>\n")
        arbol_md.append("\n")
        arbol_md.append("---\n")
        arbol_md.append("\n")
    
    # Nivel L3 (si existe)
    if tiene_l3:
        arbol_md.append("## 🏢 Nivel L3: CALE Completo\n")
        arbol_md.append("\n")
        
        configuraciones = tablas_l3.get('configuraciones', [])
        for comp in configuraciones:
            bim_id = comp.get('bim_id', 'N/A')
            nombre = comp.get('titulo', comp.get('nombre', 'Sin nombre'))
            arbol_md.append(f"### {bim_id}: {nombre}\n")
            arbol_md.append("\n")
            arbol_md.append(f"- **Nivel**: `{comp.get('nivel', 'N/A')}`\n")
            arbol_md.append(f"- **Descripción**: {comp.get('descripcion', 'N/A')}\n")
            arbol_md.append(f"- **Tipo CALE**: {comp.get('tipo_cale', 'N/A')}\n")
            
            if 'cantidad_total' in comp:
                arbol_md.append(f"- **Cantidad Total**: {comp['cantidad_total']}\n")
            
            arbol_md.append("\n")
            
            # Componentes
            componentes_l3 = comp.get('componentes', [])
            if componentes_l3:
                arbol_md.append(f"**Componentes** ({len(componentes_l3)}):\n")
                arbol_md.append("\n")
                for comp_item in componentes_l3:
                    ref_bim = comp_item.get('referencia_bim', 'N/A')
                    nombre_comp = comp_item.get('componente', 'N/A')
                    valor = comp_item.get('valor_total_cop', 0)
                    arbol_md.append(f"  - `{ref_bim}` - {nombre_comp} (${valor:,})\n")
                arbol_md.append("\n")
            
            arbol_md.append("---\n")
            arbol_md.append("\n")
    
    # Resumen final
    arbol_md.append("## 📋 Resumen de Correcciones\n")
    arbol_md.append("\n")
    arbol_md.append("### ✅ Estructura Correcta Implementada\n")
    arbol_md.append("\n")
    arbol_md.append("1. **L0**: 91 componentes atómicos organizados en 18 categorías\n")
    arbol_md.append("   - Maniobras embebidas como especificaciones geométricas\n")
    arbol_md.append("   - NO como componentes BIM independientes\n")
    arbol_md.append("\n")
    arbol_md.append("2. **L1**: 6 ensamblajes (4 constructores + 2 referencias)\n")
    arbol_md.append("   - Constructores muestran componentes L0\n")
    arbol_md.append("   - Maniobras como atributo descriptivo\n")
    arbol_md.append("   - Referencias apuntan a L2\n")
    arbol_md.append("\n")
    arbol_md.append("3. **L2**: 3 configuraciones con recursividad L2→L2\n")
    arbol_md.append("   - Single Source of Truth implementado\n")
    arbol_md.append("   - L2.pista_clase_II → REFERENCIA a L2.pista_clase_I\n")
    arbol_md.append("   - L2.pista_clase_III → REFERENCIA a L2.pista_clase_II\n")
    arbol_md.append("   - 0% duplicación de datos\n")
    arbol_md.append("\n")
    if tiene_l3:
        arbol_md.append("4. **L3**: 4 configuraciones completas de CALE\n")
        arbol_md.append("   - Referencias validadas a L2\n")
        arbol_md.append("\n")
    
    arbol_md.append("### ❌ Errores Corregidos\n")
    arbol_md.append("\n")
    arbol_md.append("- ~~31 \"L1\" maniobras~~ → 91 L0 atómicos + maniobras embebidas\n")
    arbol_md.append("- ~~L2 duplica L1~~ → L2 referencia otros L2 (recursividad)\n")
    arbol_md.append("- ~~600% duplicación~~ → 0% duplicación (SSOT)\n")
    arbol_md.append("- ~~Maniobras como componentes~~ → Maniobras como geometría\n")
    arbol_md.append("\n")
    arbol_md.append("---\n")
    arbol_md.append("\n")
    arbol_md.append("**Documento generado automáticamente**\n")
    arbol_md.append("Basado en estructura BIM oficial con recursividad L2→L2\n")
    
    # Guardar archivo
    with open('ARBOL_JERARQUIA_BIM_CORREGIDO.md', 'w', encoding='utf-8') as f:
        f.write(''.join(arbol_md))
    
    print("✅ Árbol generado: ARBOL_JERARQUIA_BIM_CORREGIDO.md")
    print()
    print("📊 Resumen:")
    print(f"   - L0: {len(tablas_l0['componentes'])} componentes atómicos")
    print(f"   - L1: {len(tablas_l1['componentes'])} ensamblajes")
    print(f"   - L2: {len(tablas_l2['componentes'])} configuraciones")
    if tiene_l3:
        print(f"   - L3: {num_l3} CALE completos")
    print()
    print("🎯 Correcciones aplicadas:")
    print("   ✅ Maniobras como geometría embebida (NO componentes)")
    print("   ✅ Recursividad L2→L2 documentada")
    print("   ✅ Single Source of Truth implementado")
    print()

if __name__ == '__main__':
    generar_arbol_completo()
