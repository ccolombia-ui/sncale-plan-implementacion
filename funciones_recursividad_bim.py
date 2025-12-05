#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funciones de Validación y Resolución Recursiva para BIM
========================================================

Implementa:
1. Resolución recursiva de referencias L2→L2
2. Validación de ciclos (evitar referencias circulares)
3. Validación de integridad referencial
4. Validación de totales (sumas correctas)
5. Expansión de componentes para fichas HTML

Uso:
    from funciones_recursividad_bim import *
    
    # Resolver componentes de pista_clase_III
    componentes_l1 = resolver_componentes_l2('BIM_L2_003', tablas_l2)
    
    # Validar integridad completa
    validar_integridad_completa(tablas_l2)
"""

import json
from typing import Dict, List, Set, Tuple

class ErrorCicloDetectado(Exception):
    """Se detectó un ciclo en las referencias L2→L2"""
    pass

class ErrorReferenciaInvalida(Exception):
    """Referencia a componente que no existe"""
    pass

class ErrorTotalIncorrecto(Exception):
    """El total declarado no coincide con la suma de componentes"""
    pass

# =============================================================================
# 1. RESOLUCIÓN RECURSIVA L2→L2
# =============================================================================

def resolver_componentes_l2(
    bim_id: str,
    tablas_l2: Dict,
    profundidad_max: int = 5,
    _visitados: Set[str] = None
) -> List[Dict]:
    """
    Resuelve recursivamente las referencias L2→L2 hasta llegar a L1
    
    Args:
        bim_id: ID del componente L2 a resolver (ej: 'BIM_L2_003')
        tablas_l2: Diccionario con todos los componentes L2
        profundidad_max: Límite para evitar recursión infinita
        _visitados: (Interno) Set de IDs ya visitados para detectar ciclos
    
    Returns:
        Lista de componentes L1 (sin duplicados, mantiene orden)
    
    Raises:
        ErrorCicloDetectado: Si se detecta una referencia circular
        ErrorReferenciaInvalida: Si se referencia un componente inexistente
        RecursionError: Si se alcanza profundidad máxima
    
    Example:
        >>> resolver_componentes_l2('BIM_L2_003', tablas_l2)
        [
            {'tipo': 'L1', 'codigo': 'L1.pista_motos_A1A2_completa', ...},
            {'tipo': 'L1', 'codigo': 'L1.pista_carros_B1C1_completa', ...},
            {'tipo': 'L1', 'codigo': 'L1.pista_camiones_B2C2_completa', ...},
            {'tipo': 'L1', 'codigo': 'L1.pista_tractocamiones_B3C3_completa', ...}
        ]
    """
    if profundidad_max == 0:
        raise RecursionError(f"Profundidad máxima alcanzada resolviendo {bim_id}")
    
    if _visitados is None:
        _visitados = set()
    
    # Detectar ciclos
    if bim_id in _visitados:
        raise ErrorCicloDetectado(f"Ciclo detectado: {bim_id} ya fue visitado en esta rama")
    
    # Validar que el componente existe
    if bim_id not in tablas_l2['componentes']:
        raise ErrorReferenciaInvalida(f"Componente {bim_id} no existe en tablas_l2")
    
    componente = tablas_l2['componentes'][bim_id]
    componentes_l1 = []
    codigos_vistos = set()  # Para evitar duplicados
    
    # Marcar como visitado
    _visitados.add(bim_id)
    
    for comp in componente['componentes']:
        if comp['tipo'] == 'L1':
            # Es un componente L1 directo
            codigo = comp['codigo']
            if codigo not in codigos_vistos:
                componentes_l1.append(comp)
                codigos_vistos.add(codigo)
        
        elif comp['tipo'] == 'L2':
            # Es una referencia a otro L2 - RECURSIÓN
            ref_id = comp['referencia']
            
            # Resolver recursivamente
            sub_componentes = resolver_componentes_l2(
                ref_id,
                tablas_l2,
                profundidad_max - 1,
                _visitados.copy()  # Copiar para mantener detección de ciclos por rama
            )
            
            # Agregar solo si no están duplicados
            for sub_comp in sub_componentes:
                codigo = sub_comp['codigo']
                if codigo not in codigos_vistos:
                    componentes_l1.append(sub_comp)
                    codigos_vistos.add(codigo)
    
    # Desmarcar para permitir reutilización en otras ramas
    _visitados.discard(bim_id)
    
    return componentes_l1


def resolver_componentes_l2_con_jerarquia(
    bim_id: str,
    tablas_l2: Dict,
    profundidad_max: int = 5
) -> Dict:
    """
    Resuelve componentes L2 manteniendo la jerarquía (útil para visualización)
    
    Returns:
        {
            'bim_id': 'BIM_L2_003',
            'codigo': 'L2.pista_clase_III',
            'componentes': [
                {
                    'tipo': 'L2',
                    'referencia': 'BIM_L2_002',
                    'expandido': [
                        {
                            'tipo': 'L2',
                            'referencia': 'BIM_L2_001',
                            'expandido': [...]
                        },
                        {'tipo': 'L1', ...}
                    ]
                },
                {'tipo': 'L1', ...}
            ]
        }
    """
    if bim_id not in tablas_l2['componentes']:
        raise ErrorReferenciaInvalida(f"Componente {bim_id} no existe")
    
    componente = tablas_l2['componentes'][bim_id].copy()
    componentes_expandidos = []
    
    for comp in componente['componentes']:
        if comp['tipo'] == 'L2':
            # Expandir recursivamente
            comp_expandido = comp.copy()
            comp_expandido['expandido'] = resolver_componentes_l2_con_jerarquia(
                comp['referencia'],
                tablas_l2,
                profundidad_max - 1
            )['componentes']
            componentes_expandidos.append(comp_expandido)
        else:
            componentes_expandidos.append(comp)
    
    componente['componentes'] = componentes_expandidos
    return componente


# =============================================================================
# 2. VALIDACIÓN DE CICLOS
# =============================================================================

def validar_sin_ciclos(tablas_l2: Dict) -> bool:
    """
    Valida que no existan referencias circulares en L2
    
    Usa algoritmo DFS (Depth-First Search) para detectar ciclos.
    
    Args:
        tablas_l2: Diccionario con componentes L2
    
    Returns:
        True si no hay ciclos
    
    Raises:
        ErrorCicloDetectado: Si se encuentra un ciclo
    
    Example:
        >>> validar_sin_ciclos(tablas_l2)
        True
    """
    visitados = set()
    en_progreso = set()
    
    def dfs(bim_id: str, camino: List[str]) -> None:
        if bim_id in en_progreso:
            ciclo = ' → '.join(camino + [bim_id])
            raise ErrorCicloDetectado(f"Ciclo detectado: {ciclo}")
        
        if bim_id in visitados:
            return
        
        en_progreso.add(bim_id)
        camino.append(bim_id)
        
        if bim_id in tablas_l2['componentes']:
            componente = tablas_l2['componentes'][bim_id]
            
            for comp in componente['componentes']:
                if comp['tipo'] == 'L2':
                    dfs(comp['referencia'], camino.copy())
        
        en_progreso.remove(bim_id)
        visitados.add(bim_id)
    
    # Verificar desde cada componente L2
    for bim_id in tablas_l2['componentes'].keys():
        dfs(bim_id, [])
    
    return True


# =============================================================================
# 3. VALIDACIÓN DE INTEGRIDAD REFERENCIAL
# =============================================================================

def validar_integridad_referencial(tablas_l2: Dict, tablas_l1: Dict) -> List[str]:
    """
    Valida que todas las referencias sean válidas
    
    Verifica:
    - Referencias L2→L2 apuntan a componentes existentes
    - Referencias L2→L1 apuntan a componentes existentes
    
    Returns:
        Lista de errores encontrados (vacía si todo OK)
    """
    errores = []
    
    for bim_id, componente in tablas_l2['componentes'].items():
        for comp in componente['componentes']:
            if comp['tipo'] == 'L2':
                # Validar referencia L2
                ref_id = comp['referencia']
                if ref_id not in tablas_l2['componentes']:
                    errores.append(
                        f"{bim_id}: Referencia inválida a L2 {ref_id} (no existe)"
                    )
            
            elif comp['tipo'] == 'L1':
                # Validar referencia L1
                bim_id_l1 = comp.get('bim_id')
                if bim_id_l1 and bim_id_l1 not in tablas_l1['componentes']:
                    errores.append(
                        f"{bim_id}: Referencia inválida a L1 {bim_id_l1} (no existe)"
                    )
    
    return errores


# =============================================================================
# 4. VALIDACIÓN DE TOTALES
# =============================================================================

def validar_totales(tablas_l2: Dict) -> List[Tuple[str, int, int, int]]:
    """
    Valida que los totales declarados coincidan con las sumas calculadas
    
    Returns:
        Lista de tuplas (bim_id, calculado, declarado, diferencia)
        Vacía si todos los totales son correctos
    """
    errores = []
    
    for bim_id, componente in tablas_l2['componentes'].items():
        # Resolver componentes L1
        try:
            componentes_l1 = resolver_componentes_l2(bim_id, tablas_l2)
            suma_calculada = sum(c['valor'] for c in componentes_l1)
            suma_declarada = componente['valor_total']
            
            if suma_calculada != suma_declarada:
                diferencia = suma_declarada - suma_calculada
                errores.append((bim_id, suma_calculada, suma_declarada, diferencia))
        
        except Exception as e:
            print(f"⚠️  Error validando totales de {bim_id}: {e}")
    
    return errores


# =============================================================================
# 5. EXPANSIÓN PARA FICHAS HTML
# =============================================================================

def expandir_para_ficha(bim_id: str, tablas_l2: Dict, tablas_l1: Dict) -> Dict:
    """
    Expande un componente L2 con toda la información necesaria para ficha HTML
    
    Returns:
        {
            'metadata': {...},
            'componentes_directos': [...],
            'componentes_expandidos': [...],
            'estadisticas': {...}
        }
    """
    componente = tablas_l2['componentes'][bim_id]
    
    # Resolver componentes L1
    componentes_l1_resueltos = resolver_componentes_l2(bim_id, tablas_l2)
    
    # Enriquecer con datos completos de L1
    componentes_l1_completos = []
    for comp_l1 in componentes_l1_resueltos:
        # Buscar en tablas_l1
        bim_id_l1 = comp_l1.get('bim_id')
        if bim_id_l1 and bim_id_l1 in tablas_l1['componentes']:
            comp_completo = tablas_l1['componentes'][bim_id_l1].copy()
            componentes_l1_completos.append(comp_completo)
        else:
            componentes_l1_completos.append(comp_l1)
    
    return {
        'metadata': {
            'bim_id': componente['bim_id'],
            'codigo': componente['codigo'],
            'nombre': componente['nombre'],
            'descripcion': componente['descripcion'],
            'tipo': componente['tipo'],
            'valor_total': componente['valor_total']
        },
        'componentes_directos': componente['componentes'],
        'componentes_expandidos': componentes_l1_completos,
        'estadisticas': {
            'total_l1': len(componentes_l1_completos),
            'total_l2_referenciados': len([c for c in componente['componentes'] if c['tipo'] == 'L2']),
            'total_l1_directos': len([c for c in componente['componentes'] if c['tipo'] == 'L1'])
        }
    }


# =============================================================================
# 6. VALIDACIÓN COMPLETA
# =============================================================================

def validar_integridad_completa(tablas_l2: Dict, tablas_l1: Dict = None) -> Dict:
    """
    Ejecuta todas las validaciones y retorna reporte completo
    
    Returns:
        {
            'ciclos': bool,
            'integridad': List[str],
            'totales': List[Tuple],
            'estado': 'OK' | 'ERRORES' | 'ADVERTENCIAS'
        }
    """
    print("="*80)
    print("VALIDACIÓN DE INTEGRIDAD BIM")
    print("="*80)
    print()
    
    reporte = {
        'ciclos': True,
        'integridad': [],
        'totales': [],
        'estado': 'OK'
    }
    
    # 1. Validar ciclos
    print("1️⃣  Validando ciclos...")
    try:
        validar_sin_ciclos(tablas_l2)
        print("   ✅ No se detectaron ciclos")
    except ErrorCicloDetectado as e:
        print(f"   ❌ CICLO DETECTADO: {e}")
        reporte['ciclos'] = False
        reporte['estado'] = 'ERRORES'
    print()
    
    # 2. Validar integridad referencial
    if tablas_l1:
        print("2️⃣  Validando integridad referencial...")
        errores_integridad = validar_integridad_referencial(tablas_l2, tablas_l1)
        if errores_integridad:
            print(f"   ❌ {len(errores_integridad)} errores encontrados:")
            for error in errores_integridad:
                print(f"      - {error}")
            reporte['integridad'] = errores_integridad
            reporte['estado'] = 'ERRORES'
        else:
            print("   ✅ Todas las referencias son válidas")
        print()
    
    # 3. Validar totales
    print("3️⃣  Validando totales...")
    errores_totales = validar_totales(tablas_l2)
    if errores_totales:
        print(f"   ⚠️  {len(errores_totales)} diferencias encontradas:")
        for bim_id, calculado, declarado, diff in errores_totales:
            print(f"      - {bim_id}:")
            print(f"        Calculado:  ${calculado:>15,}")
            print(f"        Declarado:  ${declarado:>15,}")
            print(f"        Diferencia: ${diff:>15,}")
        reporte['totales'] = errores_totales
        if reporte['estado'] == 'OK':
            reporte['estado'] = 'ADVERTENCIAS'
    else:
        print("   ✅ Todos los totales coinciden")
    print()
    
    print("="*80)
    if reporte['estado'] == 'OK':
        print("✅ VALIDACIÓN COMPLETA: TODOS LOS CHECKS PASARON")
    elif reporte['estado'] == 'ADVERTENCIAS':
        print("⚠️  VALIDACIÓN COMPLETA: HAY ADVERTENCIAS")
    else:
        print("❌ VALIDACIÓN COMPLETA: HAY ERRORES CRÍTICOS")
    print("="*80)
    print()
    
    return reporte


# =============================================================================
# EJEMPLO DE USO
# =============================================================================

if __name__ == '__main__':
    print("Cargando tablas...")
    
    with open('TABLAS_L2_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l2 = json.load(f)
    
    with open('TABLAS_L1_OFICIALES.json', 'r', encoding='utf-8') as f:
        tablas_l1 = json.load(f)
    
    print()
    
    # Ejemplo 1: Resolver componentes de pista_clase_III
    print("📊 EJEMPLO 1: Resolver BIM_L2_003 (pista_clase_III)")
    print("-" * 80)
    componentes = resolver_componentes_l2('BIM_L2_003', tablas_l2)
    print(f"Componentes L1 resueltos ({len(componentes)}):")
    for i, comp in enumerate(componentes, 1):
        print(f"   {i}. {comp['codigo']}: ${comp['valor']:,}")
    print()
    
    # Ejemplo 2: Validación completa
    reporte = validar_integridad_completa(tablas_l2, tablas_l1)
    
    # Ejemplo 3: Expandir para ficha
    print("📄 EJEMPLO 3: Expandir para ficha HTML (BIM_L2_002)")
    print("-" * 80)
    ficha = expandir_para_ficha('BIM_L2_002', tablas_l2, tablas_l1)
    print(f"Componentes directos: {ficha['estadisticas']['total_l1_directos']} L1 + {ficha['estadisticas']['total_l2_referenciados']} L2")
    print(f"Componentes expandidos: {ficha['estadisticas']['total_l1']} L1 totales")
    print()
