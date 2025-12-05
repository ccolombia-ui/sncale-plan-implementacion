#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Árbol de Jerarquía BIM Completo
L3 → L2 → L1 → L0

Fuente: Google Doc MUNAY_5.2__anexo_b__DEFINITIVO
Doc ID: 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import json
from collections import defaultdict

def extraer_referencias_l0(componentes):
    """Extrae referencias únicas L0 de una lista de componentes"""
    referencias_l0 = set()
    for comp in componentes:
        ref = comp.get('referencia', '')
        if ref.startswith('L0.'):
            referencias_l0.add(ref)
    return sorted(referencias_l0)

def extraer_referencias_l1(componentes):
    """Extrae referencias únicas L1 de una lista de componentes"""
    referencias_l1 = set()
    for comp in componentes:
        ref = comp.get('referencia', '') or comp.get('referencia_bim', '')
        if ref.startswith('L1.'):
            referencias_l1.add(ref)
    return sorted(referencias_l1)

def extraer_referencias_l2(componentes):
    """Extrae referencias únicas L2 de una lista de componentes"""
    referencias_l2 = set()
    for comp in componentes:
        ref = comp.get('referencia', '') or comp.get('referencia_bim', '')
        if ref.startswith('L2.'):
            referencias_l2.add(ref)
    return sorted(referencias_l2)

def generar_arbol_jerarquia():
    """Genera árbol completo de jerarquía BIM"""
    
    print("="*80)
    print("ÁRBOL DE JERARQUÍA BIM - SNCALE")
    print("="*80)
    print("Fuente: Google Doc MUNAY_5.2__anexo_b__DEFINITIVO")
    print("Doc ID: 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE")
    print("="*80)
    print()
    
    # Cargar datos
    with open('TABLAS_L1_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l1 = json.load(f)
    
    with open('TABLAS_L2_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l2 = json.load(f)
    
    with open('TABLAS_L3_OFICIALES.json', 'r', encoding='utf-8') as f:
        datos_l3 = json.load(f)
    
    # Construir árbol completo
    arbol = []
    
    # Nivel L3
    for config_l3 in datos_l3['configuraciones']:
        bim_id_l3 = config_l3['bim_id']
        titulo_l3 = config_l3['titulo']
        valor_l3 = config_l3['valorizacion']['total_cop_formateado']
        componentes_l3 = config_l3['componentes']
        
        # Extraer referencias L2 de componentes L3
        refs_l2 = extraer_referencias_l2(componentes_l3)
        
        nodo_l3 = {
            'bim_id': bim_id_l3,
            'titulo': titulo_l3,
            'valor': valor_l3,
            'nivel': 'L3',
            'componentes_directos': len(componentes_l3),
            'hijos_l2': []
        }
        
        # Para cada referencia L2, buscar en datos L2
        for ref_l2 in refs_l2:
            # Buscar configuración L2 correspondiente
            for nivel_l2, config_l2 in datos_l2['tablas_l2'].items():
                bim_id_l2 = config_l2['bim_id']
                
                # Match por referencia
                if ref_l2.endswith(nivel_l2) or nivel_l2 in ref_l2:
                    titulo_l2 = config_l2['titulo']
                    valor_l2 = config_l2['valorización']['valor_cop']
                    componentes_l2 = config_l2.get('componentes_l1', [])
                    
                    # Extraer referencias L1 de componentes L2
                    refs_l1 = extraer_referencias_l1(componentes_l2)
                    
                    nodo_l2 = {
                        'bim_id': bim_id_l2,
                        'titulo': titulo_l2,
                        'valor': valor_l2,
                        'nivel': 'L2',
                        'componentes_directos': len(componentes_l2),
                        'hijos_l1': []
                    }
                    
                    # Para cada referencia L1, buscar en datos L1
                    for ref_l1 in refs_l1:
                        # Buscar en todas las tablas L1
                        for nivel_l1, tabla_l1 in datos_l1['tablas_l1'].items():
                            componentes_l1 = tabla_l1['componentes']
                            
                            for comp_l1 in componentes_l1:
                                if comp_l1['referencia'] == ref_l1:
                                    # Extraer referencias L0
                                    refs_l0 = []
                                    if comp_l1['referencia'].startswith('L0.'):
                                        refs_l0 = [comp_l1['referencia']]
                                    
                                    nodo_l1 = {
                                        'componente': comp_l1['componente'],
                                        'descripcion': comp_l1['descripcion'],
                                        'referencia': comp_l1['referencia'],
                                        'nivel': 'L1',
                                        'tipo': comp_l1.get('tipo', 'N/A'),
                                        'hijos_l0': []
                                    }
                                    
                                    # Agregar nodos L0 si existen
                                    for ref_l0 in refs_l0:
                                        nodo_l0 = {
                                            'referencia': ref_l0,
                                            'nivel': 'L0',
                                            'tipo': 'Componente Base'
                                        }
                                        nodo_l1['hijos_l0'].append(nodo_l0)
                                    
                                    nodo_l2['hijos_l1'].append(nodo_l1)
                                    break
                    
                    nodo_l3['hijos_l2'].append(nodo_l2)
        
        arbol.append(nodo_l3)
    
    return arbol

def imprimir_arbol_consola(arbol):
    """Imprime el árbol en formato legible en consola"""
    
    for nodo_l3 in arbol:
        # L3
        print(f"\n📦 L3: {nodo_l3['bim_id']} - {nodo_l3['titulo']}")
        print(f"   💰 Valor: {nodo_l3['valor']}")
        print(f"   🔧 Componentes directos: {nodo_l3['componentes_directos']}")
        
        if not nodo_l3['hijos_l2']:
            print("   └─ (Sin componentes L2 mapeados)")
            continue
        
        for i, nodo_l2 in enumerate(nodo_l3['hijos_l2']):
            es_ultimo_l2 = i == len(nodo_l3['hijos_l2']) - 1
            prefijo_l2 = "└─" if es_ultimo_l2 else "├─"
            
            # L2
            print(f"   {prefijo_l2} 📦 L2: {nodo_l2['bim_id']} - {nodo_l2['titulo']}")
            print(f"   {'   ' if es_ultimo_l2 else '│  '}    💰 Valor: {nodo_l2['valor']}")
            print(f"   {'   ' if es_ultimo_l2 else '│  '}    🔧 Componentes: {nodo_l2['componentes_directos']}")
            
            if not nodo_l2['hijos_l1']:
                print(f"   {'   ' if es_ultimo_l2 else '│  '}    └─ (Sin componentes L1 mapeados)")
                continue
            
            for j, nodo_l1 in enumerate(nodo_l2['hijos_l1'][:5]):  # Mostrar máximo 5
                es_ultimo_l1 = j == len(nodo_l2['hijos_l1'][:5]) - 1
                prefijo_l1 = "└─" if es_ultimo_l1 else "├─"
                
                # L1
                ref_corta = nodo_l1['referencia'].split('.')[-1]
                print(f"   {'   ' if es_ultimo_l2 else '│  '}    {prefijo_l1} 🔧 L1: {ref_corta} - {nodo_l1['componente']}")
                
                # L0
                if nodo_l1['hijos_l0']:
                    for nodo_l0 in nodo_l1['hijos_l0']:
                        ref_l0_corta = nodo_l0['referencia'].split('.')[-1]
                        print(f"   {'   ' if es_ultimo_l2 else '│  '}    {'   ' if es_ultimo_l1 else '│  '}    └─ ⚙️ L0: {ref_l0_corta}")
            
            if len(nodo_l2['hijos_l1']) > 5:
                print(f"   {'   ' if es_ultimo_l2 else '│  '}    └─ ... (+{len(nodo_l2['hijos_l1']) - 5} componentes más)")

def generar_arbol_markdown(arbol):
    """Genera archivo markdown con el árbol completo"""
    
    md = "# 🌳 Árbol de Jerarquía BIM - SNCALE\n\n"
    md += "**Fuente:** Google Doc MUNAY_5.2__anexo_b__DEFINITIVO  \n"
    md += "**Doc ID:** `16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE`  \n"
    md += "**Fecha:** 3 de noviembre de 2025\n\n"
    md += "---\n\n"
    
    md += "## Estructura de Jerarquía\n\n"
    md += "```\n"
    md += "L3 (Configuraciones CALE)\n"
    md += "  ├─ L2 (Pistas y Edificaciones)\n"
    md += "  │   ├─ L1 (Maniobras y Componentes)\n"
    md += "  │   │   └─ L0 (Componentes Base)\n"
    md += "```\n\n"
    md += "---\n\n"
    
    # Estadísticas
    total_l3 = len(arbol)
    total_l2 = sum(len(n['hijos_l2']) for n in arbol)
    total_l1 = sum(len(l2['hijos_l1']) for n in arbol for l2 in n['hijos_l2'])
    total_l0 = sum(len(l1['hijos_l0']) for n in arbol for l2 in n['hijos_l2'] for l1 in l2['hijos_l1'])
    
    md += "## 📊 Estadísticas Generales\n\n"
    md += f"- **Nivel L3:** {total_l3} configuraciones CALE\n"
    md += f"- **Nivel L2:** {total_l2} configuraciones de pistas/edificaciones\n"
    md += f"- **Nivel L1:** {total_l1} componentes/maniobras\n"
    md += f"- **Nivel L0:** {total_l0} componentes base\n\n"
    md += "---\n\n"
    
    # Árbol detallado
    for idx_l3, nodo_l3 in enumerate(arbol, 1):
        md += f"## {idx_l3}. L3: {nodo_l3['bim_id']} - {nodo_l3['titulo']}\n\n"
        md += f"**Valorización:** {nodo_l3['valor']}  \n"
        md += f"**Componentes directos:** {nodo_l3['componentes_directos']}  \n"
        md += f"**Ficha:** [Ver ficha HTML](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/{nodo_l3['bim_id']}.html)\n\n"
        
        if not nodo_l3['hijos_l2']:
            md += "*(Sin componentes L2 mapeados)*\n\n"
            continue
        
        for idx_l2, nodo_l2 in enumerate(nodo_l3['hijos_l2'], 1):
            md += f"### {idx_l3}.{idx_l2} L2: {nodo_l2['bim_id']} - {nodo_l2['titulo']}\n\n"
            md += f"**Valorización:** {nodo_l2['valor']}  \n"
            md += f"**Componentes:** {nodo_l2['componentes_directos']}  \n"
            md += f"**Ficha:** [Ver ficha HTML](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l2/{nodo_l2['bim_id']}.html)\n\n"
            
            if not nodo_l2['hijos_l1']:
                md += "*(Sin componentes L1 mapeados)*\n\n"
                continue
            
            md += "#### Componentes L1\n\n"
            md += "| # | Componente | Descripción | Referencia | Tipo | L0 |\n"
            md += "|---|------------|-------------|------------|------|----|\n"
            
            for idx_l1, nodo_l1 in enumerate(nodo_l2['hijos_l1'], 1):
                comp = nodo_l1['componente']
                desc = nodo_l1['descripcion'][:50] + "..." if len(nodo_l1['descripcion']) > 50 else nodo_l1['descripcion']
                ref = f"`{nodo_l1['referencia']}`"
                tipo = nodo_l1['tipo']
                l0_count = len(nodo_l1['hijos_l0'])
                l0_info = f"{l0_count} comp." if l0_count > 0 else "-"
                
                md += f"| {idx_l1} | {comp} | {desc} | {ref} | {tipo} | {l0_info} |\n"
            
            md += "\n"
        
        md += "---\n\n"
    
    return md

def main():
    print("Generando árbol de jerarquía BIM...\n")
    
    # Generar árbol
    arbol = generar_arbol_jerarquia()
    
    # Imprimir en consola
    print("\n" + "="*80)
    print("VISTA RESUMIDA DEL ÁRBOL")
    print("="*80)
    imprimir_arbol_consola(arbol)
    
    # Generar markdown
    print("\n" + "="*80)
    print("Generando archivo markdown...")
    md_content = generar_arbol_markdown(arbol)
    
    with open('ARBOL_JERARQUIA_BIM_COMPLETO.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print("✅ Archivo generado: ARBOL_JERARQUIA_BIM_COMPLETO.md")
    
    # Generar JSON
    print("Generando archivo JSON...")
    with open('ARBOL_JERARQUIA_BIM_COMPLETO.json', 'w', encoding='utf-8') as f:
        json.dump(arbol, f, indent=2, ensure_ascii=False)
    
    print("✅ Archivo generado: ARBOL_JERARQUIA_BIM_COMPLETO.json")
    
    print("\n" + "="*80)
    print("✅ Generación completada")
    print("="*80)

if __name__ == '__main__':
    main()
