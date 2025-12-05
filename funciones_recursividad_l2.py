#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FUNCIONES DE RECURSIVIDAD L2→L2 - PISTAS CALE
============================================
Resuelve herencia L2→L2 para pistas de conducción:
- Pista Clase I (BASE)
- Pista Clase II (hereda de I + adicionales)
- Pista Clase III (hereda de II + adicionales)

Patrón: HERENCIA_MEJORAMIENTO_PROGRESIVO
"""

import json
from pathlib import Path
from typing import Dict, List, Set

# ============================================================================
# EXCEPCIONES
# ============================================================================

class ErrorCicloDetectado(Exception):
    """Excepción cuando se detecta ciclo en herencia L2→L2"""
    pass


# ============================================================================
# FUNCIÓN PRINCIPAL: RESOLVER RECURSIVIDAD L2→L2
# ============================================================================

def resolver_l2_recursivo(
    bim_id: str, 
    tablas_l2: Dict, 
    profundidad_max: int = 5,
    _visitados: Set[str] = None
) -> List[Dict]:
    """
    Resuelve recursivamente componentes L1 de una configuración L2,
    incluyendo componentes heredados de configuraciones base.
    
    Args:
        bim_id: ID de configuración L2 (ej: "BIM_L2_003")
        tablas_l2: Diccionario con todas las configuraciones L2
        profundidad_max: Máxima profundidad de recursión (evita loops infinitos)
        _visitados: Set interno para detectar ciclos
    
    Returns:
        Lista de componentes L1 (heredados + propios)
    
    Raises:
        ErrorCicloDetectado: Si se detecta ciclo (L2_A → L2_B → L2_A)
        KeyError: Si bim_id no existe en tablas_l2
    
    Ejemplo:
        >>> resolver_l2_recursivo("BIM_L2_003", tablas_l2)
        [
            # Heredados de BIM_L2_001 (Clase I):
            {"codigo": "L1.area_maniobras", "valor_total": 450000000},
            {"codigo": "L1.area_estacionamiento", "valor_total": 180000000},
            {"codigo": "L1.circuito_urbano", "valor_total": 91440000},
            # Heredados de BIM_L2_002 (Clase II):
            {"codigo": "L1.area_carga_descarga", "valor_total": 120000000},
            {"codigo": "L1.rampa_pendiente", "valor_total": 45000000},
            # Propios de BIM_L2_003 (Clase III):
            {"codigo": "L1.area_articulados", "valor_total": 200000000},
            {"codigo": "L1.circuito_carretera", "valor_total": 180000000}
        ]
        # Total: 7 componentes (3 de I + 2 de II + 2 de III)
    """
    # Inicializar set de visitados si es primera llamada
    if _visitados is None:
        _visitados = set()
    
    # Validar profundidad máxima
    if profundidad_max <= 0:
        raise ErrorCicloDetectado(
            f"Profundidad máxima alcanzada resolviendo {bim_id}. "
            f"Posible ciclo en cadena de herencia."
        )
    
    # Detectar ciclos
    if bim_id in _visitados:
        cadena = " → ".join(sorted(_visitados)) + f" → {bim_id}"
        raise ErrorCicloDetectado(
            f"Ciclo detectado en herencia L2→L2: {cadena}"
        )
    
    # Validar que existe
    if bim_id not in tablas_l2:
        raise KeyError(f"Configuración {bim_id} no encontrada en tablas_l2")
    
    # Marcar como visitado
    _visitados.add(bim_id)
    
    config = tablas_l2[bim_id]
    componentes = []
    
    # CASO 1: Configuración EXTENDIDA (tiene recursividad_l2)
    if 'recursividad_l2' in config:
        recursividad = config['recursividad_l2']
        base_id = recursividad['referencia_base']
        
        # RECURSIÓN: Resolver componentes de base
        componentes_base = resolver_l2_recursivo(
            base_id, 
            tablas_l2, 
            profundidad_max - 1,
            _visitados.copy()  # Copiar para evitar contaminar otras ramas
        )
        componentes.extend(componentes_base)
        
        # Agregar componentes adicionales
        if 'componentes_adicionales' in recursividad:
            componentes.extend(recursividad['componentes_adicionales'])
    
    # CASO 2: Configuración BASE (solo sus componentes directos)
    else:
        componentes = config.get('componentes_l1', [])
    
    return componentes


# ============================================================================
# VALIDACIÓN DE HERENCIA
# ============================================================================

def validar_herencia_l2(bim_id: str, tablas_l2: Dict) -> Dict:
    """
    Valida que una configuración L2 extendida hereda correctamente de su base
    
    Args:
        bim_id: ID de configuración L2 extendida
        tablas_l2: Diccionario con todas las configuraciones L2
    
    Returns:
        Dict con resultados de validación:
        {
            'valido': bool,
            'base_id': str,
            'componentes_heredados': int,
            'componentes_nuevos': int,
            'componentes_totales': int,
            'errores': List[str]
        }
    """
    if bim_id not in tablas_l2:
        return {
            'valido': False,
            'errores': [f"Configuración {bim_id} no encontrada"]
        }
    
    config = tablas_l2[bim_id]
    errores = []
    
    # Validar que es EXTENDIDA
    if config.get('tipo') != 'CONFIGURACION_EXTENDIDA':
        errores.append(f"{bim_id} no es CONFIGURACION_EXTENDIDA")
        return {'valido': False, 'errores': errores}
    
    # Validar que tiene recursividad_l2
    if 'recursividad_l2' not in config:
        errores.append(f"{bim_id} no tiene campo 'recursividad_l2'")
        return {'valido': False, 'errores': errores}
    
    recursividad = config['recursividad_l2']
    base_id = recursividad.get('referencia_base')
    
    # Validar que referencia_base existe
    if not base_id:
        errores.append("Falta campo 'referencia_base' en recursividad_l2")
        return {'valido': False, 'errores': errores}
    
    if base_id not in tablas_l2:
        errores.append(f"Configuración base {base_id} no encontrada")
        return {'valido': False, 'errores': errores}
    
    # Validar hereda_todos_componentes
    if not recursividad.get('hereda_todos_componentes', False):
        errores.append("Campo 'hereda_todos_componentes' debe ser true")
    
    # Resolver componentes
    try:
        componentes_base = resolver_l2_recursivo(base_id, tablas_l2)
        componentes_nuevos = recursividad.get('componentes_adicionales', [])
        todos_componentes = resolver_l2_recursivo(bim_id, tablas_l2)
        
        # Validar que componentes totales = base + nuevos
        if len(todos_componentes) != len(componentes_base) + len(componentes_nuevos):
            errores.append(
                f"Componentes totales ({len(todos_componentes)}) != "
                f"base ({len(componentes_base)}) + nuevos ({len(componentes_nuevos)})"
            )
        
        return {
            'valido': len(errores) == 0,
            'base_id': base_id,
            'componentes_heredados': len(componentes_base),
            'componentes_nuevos': len(componentes_nuevos),
            'componentes_totales': len(todos_componentes),
            'errores': errores
        }
    except Exception as e:
        errores.append(f"Error resolviendo componentes: {str(e)}")
        return {'valido': False, 'errores': errores}


# ============================================================================
# CALCULAR TOTALES AGREGADOS
# ============================================================================

def calcular_totales_agregados(bim_id: str, tablas_l2: Dict) -> Dict:
    """
    Calcula totales agregados (CAPEX, capacidad, personal) de configuración L2
    incluyendo herencia de componentes base
    
    Args:
        bim_id: ID de configuración L2
        tablas_l2: Diccionario con todas las configuraciones L2
    
    Returns:
        Dict con totales calculados:
        {
            'capex_total': float,
            'capacidad_mes': int,
            'capacidad_anual': int,
            'personal_total': int,
            'area_total_m2': float,
            'componentes_count': int
        }
    """
    if bim_id not in tablas_l2:
        raise KeyError(f"Configuración {bim_id} no encontrada")
    
    config = tablas_l2[bim_id]
    componentes = resolver_l2_recursivo(bim_id, tablas_l2)
    
    # CAPEX: sumar valor_total de todos los componentes L1
    capex_total = sum(c.get('valor_total', 0) for c in componentes)
    
    # Capacidad
    capacidad_mes = config.get('capacidad_mes', 0)
    capacidad_anual = config.get('capacidad_anual', 0)
    
    # Personal
    recursos = config.get('recursos', {})
    personal_total = recursos.get('personal_total', 0)
    area_total_m2 = recursos.get('area_total_m2', 0)
    
    return {
        'capex_total': capex_total,
        'capacidad_mes': capacidad_mes,
        'capacidad_anual': capacidad_anual,
        'personal_total': personal_total,
        'area_total_m2': area_total_m2,
        'componentes_count': len(componentes)
    }


# ============================================================================
# GENERAR ÁRBOL DE COMPONENTES
# ============================================================================

def generar_arbol_componentes(bim_id: str, tablas_l2: Dict, nivel: int = 0) -> str:
    """
    Genera representación en árbol de componentes L2 con recursividad
    
    Args:
        bim_id: ID de configuración L2
        tablas_l2: Diccionario con todas las configuraciones L2
        nivel: Nivel de indentación (para recursión)
    
    Returns:
        String con árbol de componentes
    """
    if bim_id not in tablas_l2:
        return f"{'  ' * nivel}❌ {bim_id} NO ENCONTRADO\n"
    
    config = tablas_l2[bim_id]
    indent = '  ' * nivel
    arbol = f"{indent}🏗️ {config['codigo']} - {config['nombre']}\n"
    arbol += f"{indent}💰 CAPEX: ${config.get('valor_total_capex', 0):,.0f}\n"
    
    # Si es extendida, mostrar herencia
    if 'recursividad_l2' in config:
        recursividad = config['recursividad_l2']
        base_id = recursividad['referencia_base']
        
        arbol += f"{indent}   ↓ HEREDA DE:\n"
        arbol += generar_arbol_componentes(base_id, tablas_l2, nivel + 2)
        
        # Componentes adicionales
        if 'componentes_adicionales' in recursividad:
            arbol += f"{indent}   ➕ COMPONENTES ADICIONALES:\n"
            for comp in recursividad['componentes_adicionales']:
                arbol += f"{indent}      • {comp['codigo']}: ${comp['valor_total']:,.0f}\n"
    else:
        # Base: listar componentes directos
        arbol += f"{indent}   📦 COMPONENTES BASE:\n"
        for comp in config.get('componentes_l1', []):
            arbol += f"{indent}      • {comp['codigo']}: ${comp['valor_total']:,.0f}\n"
    
    return arbol


# ============================================================================
# VALIDAR TODAS LAS CONFIGURACIONES
# ============================================================================

def validar_todas_configuraciones(tablas_l2: Dict) -> Dict:
    """
    Valida todas las configuraciones L2 en el archivo
    
    Returns:
        Dict con resultados de validación
    """
    resultados = {
        'total': len(tablas_l2),
        'bases': 0,
        'extendidas': 0,
        'validas': 0,
        'invalidas': 0,
        'detalles': []
    }
    
    for bim_id, config in tablas_l2.items():
        tipo = config.get('tipo', 'DESCONOCIDO')
        
        if tipo == 'CONFIGURACION_BASE':
            resultados['bases'] += 1
            resultados['validas'] += 1
            resultados['detalles'].append({
                'bim_id': bim_id,
                'tipo': 'BASE',
                'valido': True
            })
        
        elif tipo == 'CONFIGURACION_EXTENDIDA':
            resultados['extendidas'] += 1
            validacion = validar_herencia_l2(bim_id, tablas_l2)
            
            if validacion['valido']:
                resultados['validas'] += 1
            else:
                resultados['invalidas'] += 1
            
            resultados['detalles'].append({
                'bim_id': bim_id,
                'tipo': 'EXTENDIDA',
                'valido': validacion['valido'],
                'base_id': validacion.get('base_id'),
                'componentes_totales': validacion.get('componentes_totales'),
                'errores': validacion.get('errores', [])
            })
    
    return resultados


# ============================================================================
# FUNCIÓN DE PRUEBA
# ============================================================================

def main():
    """Función de prueba para validar recursividad L2→L2"""
    
    print("=" * 80)
    print("FUNCIONES RECURSIVIDAD L2→L2 - PRUEBA")
    print("=" * 80)
    print()
    
    # Cargar JSON
    ruta_json = Path(__file__).parent / "TABLAS_L2_PISTAS_RECURSIVAS.json"
    print(f"📖 Cargando {ruta_json.name}...")
    
    with open(ruta_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Excluir metadata
    tablas_l2 = {k: v for k, v in data.items() if k != 'metadata'}
    print(f"✅ {len(tablas_l2)} configuraciones cargadas\n")
    
    # Validar todas
    print("🔍 VALIDANDO TODAS LAS CONFIGURACIONES...")
    print("-" * 80)
    resultados = validar_todas_configuraciones(tablas_l2)
    
    print(f"Total configuraciones: {resultados['total']}")
    print(f"  • Bases: {resultados['bases']}")
    print(f"  • Extendidas: {resultados['extendidas']}")
    print(f"  • Válidas: {resultados['validas']} ✅")
    print(f"  • Inválidas: {resultados['invalidas']} ❌")
    print()
    
    # Ejemplo 1: Pista Clase II
    print("📊 EJEMPLO 1: Resolver BIM_L2_002 (Pista Clase II)")
    print("-" * 80)
    componentes_ii = resolver_l2_recursivo("BIM_L2_002", tablas_l2)
    print(f"✅ {len(componentes_ii)} componentes resueltos:")
    for idx, comp in enumerate(componentes_ii, 1):
        print(f"   {idx}. {comp['codigo']}: ${comp['valor_total']:,.0f}")
    
    totales_ii = calcular_totales_agregados("BIM_L2_002", tablas_l2)
    print(f"\n💰 CAPEX Total: ${totales_ii['capex_total']:,.0f}")
    print(f"📈 Capacidad/Mes: {totales_ii['capacidad_mes']:,} evaluaciones")
    print(f"📈 Capacidad/Año: {totales_ii['capacidad_anual']:,} evaluaciones")
    print(f"👥 Personal: {totales_ii['personal_total']} personas")
    print()
    
    # Ejemplo 2: Pista Clase III
    print("📊 EJEMPLO 2: Resolver BIM_L2_003 (Pista Clase III)")
    print("-" * 80)
    componentes_iii = resolver_l2_recursivo("BIM_L2_003", tablas_l2)
    print(f"✅ {len(componentes_iii)} componentes resueltos:")
    for idx, comp in enumerate(componentes_iii, 1):
        print(f"   {idx}. {comp['codigo']}: ${comp['valor_total']:,.0f}")
    
    totales_iii = calcular_totales_agregados("BIM_L2_003", tablas_l2)
    print(f"\n💰 CAPEX Total: ${totales_iii['capex_total']:,.0f}")
    print(f"📈 Capacidad/Mes: {totales_iii['capacidad_mes']:,} evaluaciones")
    print(f"📈 Capacidad/Año: {totales_iii['capacidad_anual']:,} evaluaciones")
    print(f"👥 Personal: {totales_iii['personal_total']} personas")
    print()
    
    # Árbol de herencia
    print("🌳 ÁRBOL DE COMPONENTES BIM_L2_003:")
    print("-" * 80)
    arbol = generar_arbol_componentes("BIM_L2_003", tablas_l2)
    print(arbol)
    
    print("=" * 80)
    print("✅ PRUEBA COMPLETADA")
    print("=" * 80)


if __name__ == "__main__":
    main()
