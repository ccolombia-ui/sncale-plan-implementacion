#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funciones Recursividad L3→L3 - CALE Variantes
=============================================

Implementa resolución recursiva de configuraciones L3 CALE
que heredan componentes de configuraciones base.

Autor: Modelo BIM 5D SNCALE
Fecha: 2025-11-03
Versión: 1.0
"""

import json
from typing import Dict, List, Set, Tuple


class ErrorCicloDetectado(Exception):
    """Error cuando se detecta ciclo en recursividad L3→L3"""
    pass


def resolver_l3_recursivo(
    bim_id: str,
    tablas_l3: Dict,
    profundidad_max: int = 3,
    _visitados: Set[str] = None
) -> List[Dict]:
    """
    Resuelve recursivamente configuración L3→L3
    Retorna lista de TODOS los componentes L2/L3 (heredados + nuevos)
    
    Args:
        bim_id: ID de configuración L3 a resolver
        tablas_l3: Diccionario con todas las configuraciones L3
        profundidad_max: Máxima profundidad recursión (previene ciclos infinitos)
        _visitados: Set de IDs ya visitados (para detectar ciclos)
    
    Returns:
        Lista de componentes L2/L3 resueltos
    
    Raises:
        ErrorCicloDetectado: Si hay ciclo L3_A → L3_B → L3_A
    
    Example:
        >>> resolver_l3_recursivo('BIM_L3_001_PLUS', tablas_l3)
        [
            # Componentes heredados de BIM_L3_001_BASE
            {'bim_id': 'BIM_L2_003', 'codigo': 'L2.pista_clase_III', ...},
            {'bim_id': 'BIM_L3_010', 'codigo': 'L3.CALE_TEORICO.24q', ...},
            {'bim_id': 'BIM_L2_007', 'codigo': 'L2.parqueadero', ...},
            # Componentes adicionales de BIM_L3_001_PLUS
            {'bim_id': 'BIM_L2_009', 'codigo': 'L2.edificacion_adecuada', ...},
            {'bim_id': 'BIM_L2_008', 'codigo': 'L2.datacenter', ...},
            {'bim_id': 'BIM_L3_011', 'codigo': 'L3.CALE_TEORICO.16q', ...}
        ]
    """
    if profundidad_max == 0:
        raise ErrorCicloDetectado(f"Profundidad máxima alcanzada resolviendo {bim_id}")
    
    if _visitados is None:
        _visitados = set()
    
    if bim_id in _visitados:
        raise ErrorCicloDetectado(f"Ciclo L3 detectado: {bim_id} ya fue visitado")
    
    _visitados.add(bim_id)
    
    if bim_id not in tablas_l3:
        raise KeyError(f"Configuración L3 no encontrada: {bim_id}")
    
    config = tablas_l3[bim_id]
    componentes = []
    
    # Si tiene recursividad, resolver base primero
    if 'recursividad_l3' in config:
        base_id = config['recursividad_l3']['referencia_base']
        
        # RECURSIÓN: Obtener componentes de la configuración base
        componentes_base = resolver_l3_recursivo(
            base_id,
            tablas_l3,
            profundidad_max - 1,
            _visitados.copy()  # Nueva copia para cada rama
        )
        componentes.extend(componentes_base)
        
        # Agregar componentes adicionales de la variante
        if 'componentes_adicionales' in config['recursividad_l3']:
            componentes.extend(config['recursividad_l3']['componentes_adicionales'])
    else:
        # Configuración base: solo sus componentes directos
        componentes = config.get('componentes_l2', [])
    
    return componentes


def validar_herencia_l3(bim_id: str, tablas_l3: Dict) -> Dict:
    """
    Valida que una configuración extendida hereda correctamente de su base
    
    Args:
        bim_id: ID de configuración extendida a validar
        tablas_l3: Diccionario con todas las configuraciones L3
    
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
    if bim_id not in tablas_l3:
        return {
            'valido': False,
            'errores': [f"Configuración {bim_id} no encontrada"]
        }
    
    config = tablas_l3[bim_id]
    errores = []
    
    # Validar que es configuración extendida
    if config['tipo'] != 'CONFIGURACION_EXTENDIDA':
        return {
            'valido': True,
            'nota': 'Configuración base - no requiere validación de herencia'
        }
    
    # Validar campo recursividad_l3
    if 'recursividad_l3' not in config:
        errores.append("Falta campo 'recursividad_l3'")
        return {'valido': False, 'errores': errores}
    
    rec = config['recursividad_l3']
    base_id = rec.get('referencia_base')
    
    if not base_id:
        errores.append("Falta 'referencia_base' en recursividad_l3")
    
    if base_id not in tablas_l3:
        errores.append(f"Configuración base no encontrada: {base_id}")
    
    # Validar que hereda todos los componentes
    if not rec.get('hereda_todos_componentes'):
        errores.append("Campo 'hereda_todos_componentes' debe ser true")
    
    # Contar componentes
    try:
        todos_componentes = resolver_l3_recursivo(bim_id, tablas_l3)
        config_base = tablas_l3[base_id]
        componentes_base = config_base.get('componentes_l2', [])
        componentes_nuevos = rec.get('componentes_adicionales', [])
        
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


def calcular_totales_agregados(bim_id: str, tablas_l3: Dict) -> Dict:
    """
    Calcula totales agregados (CAPEX, capacidad, personal) de configuración L3
    incluyendo herencia de componentes base
    
    Args:
        bim_id: ID de configuración L3
        tablas_l3: Diccionario con todas las configuraciones L3
    
    Returns:
        Dict con totales calculados:
        {
            'capex_total': float,
            'capacidad_mes': int,
            'personal_total': int,
            'componentes_count': int
        }
    """
    if bim_id not in tablas_l3:
        raise KeyError(f"Configuración {bim_id} no encontrada")
    
    config = tablas_l3[bim_id]
    componentes = resolver_l3_recursivo(bim_id, tablas_l3)
    
    capex_total = sum(c.get('valor_total', 0) for c in componentes)
    
    # Capacidad: sumar capacidades teóricas (algunos componentes no tienen)
    capacidad_mes = config.get('capacidad', {}).get('total_evaluaciones_mes', 0)
    
    # Personal
    personal_total = config.get('recursos', {}).get('personal_total', 0)
    
    return {
        'capex_total': capex_total,
        'capacidad_mes': capacidad_mes,
        'personal_total': personal_total,
        'componentes_count': len(componentes)
    }


def generar_arbol_componentes(bim_id: str, tablas_l3: Dict, nivel: int = 0) -> str:
    """
    Genera representación en árbol de componentes L3 con recursividad
    
    Args:
        bim_id: ID de configuración L3
        tablas_l3: Diccionario con todas las configuraciones L3
        nivel: Nivel de indentación (para recursión)
    
    Returns:
        String con árbol de componentes
    """
    if bim_id not in tablas_l3:
        return f"{'  ' * nivel}❌ {bim_id} NO ENCONTRADO\n"
    
    config = tablas_l3[bim_id]
    indent = '  ' * nivel
    arbol = f"{indent}🏢 {config['codigo']} - {config['nombre']}\n"
    arbol += f"{indent}   💰 CAPEX: ${config.get('valor_total_capex', 0):,}\n"
    
    # Si tiene recursividad, mostrar herencia
    if 'recursividad_l3' in config:
        rec = config['recursividad_l3']
        base_id = rec['referencia_base']
        arbol += f"{indent}   ↓ HEREDA DE:\n"
        arbol += generar_arbol_componentes(base_id, tablas_l3, nivel + 2)
        
        arbol += f"{indent}   ➕ COMPONENTES ADICIONALES:\n"
        for comp in rec.get('componentes_adicionales', []):
            arbol += f"{indent}      • {comp['codigo']}: ${comp.get('valor_total', 0):,}\n"
    else:
        arbol += f"{indent}   📦 COMPONENTES BASE:\n"
        for comp in config.get('componentes_l2', []):
            arbol += f"{indent}      • {comp['codigo']}: ${comp.get('valor_total', 0):,}\n"
    
    return arbol


def validar_todas_configuraciones(tablas_l3: Dict) -> Dict:
    """
    Valida todas las configuraciones L3 en el diccionario
    
    Returns:
        Dict con resultados:
        {
            'total': int,
            'bases': int,
            'extendidas': int,
            'validas': int,
            'invalidas': int,
            'detalles': List[Dict]
        }
    """
    total = len(tablas_l3)
    bases = 0
    extendidas = 0
    validas = 0
    invalidas = 0
    detalles = []
    
    for bim_id, config in tablas_l3.items():
        if bim_id == 'metadata':
            continue
        
        tipo = config.get('tipo')
        
        if tipo == 'CONFIGURACION_BASE':
            bases += 1
            validas += 1
            detalles.append({
                'bim_id': bim_id,
                'tipo': 'BASE',
                'valido': True
            })
        elif tipo == 'CONFIGURACION_EXTENDIDA':
            extendidas += 1
            validacion = validar_herencia_l3(bim_id, tablas_l3)
            
            if validacion['valido']:
                validas += 1
            else:
                invalidas += 1
            
            detalles.append({
                'bim_id': bim_id,
                'tipo': 'EXTENDIDA',
                'valido': validacion['valido'],
                'validacion': validacion
            })
    
    return {
        'total': total - 1,  # Excluir metadata
        'bases': bases,
        'extendidas': extendidas,
        'validas': validas,
        'invalidas': invalidas,
        'detalles': detalles
    }


def main():
    """Función principal de prueba"""
    print("=" * 80)
    print("  FUNCIONES RECURSIVIDAD L3→L3 - PRUEBA")
    print("=" * 80)
    print()
    
    # Cargar datos
    print("📖 Cargando TABLAS_L3_VARIANTES_RECURSIVAS.json...")
    with open('TABLAS_L3_VARIANTES_RECURSIVAS.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    tablas_l3 = {k: v for k, v in datos.items() if k != 'metadata'}
    print(f"✅ {len(tablas_l3)} configuraciones cargadas")
    print()
    
    # Validar todas
    print("🔍 VALIDANDO TODAS LAS CONFIGURACIONES...")
    print("-" * 80)
    resultado = validar_todas_configuraciones(datos)
    print(f"Total configuraciones: {resultado['total']}")
    print(f"  • Bases: {resultado['bases']}")
    print(f"  • Extendidas: {resultado['extendidas']}")
    print(f"  • Válidas: {resultado['validas']} ✅")
    print(f"  • Inválidas: {resultado['invalidas']} ❌")
    print()
    
    # Resolver CALE.n_1+
    print("📊 EJEMPLO 1: Resolver BIM_L3_001_PLUS (CALE.n_1+)")
    print("-" * 80)
    try:
        componentes = resolver_l3_recursivo('BIM_L3_001_PLUS', tablas_l3)
        print(f"✅ {len(componentes)} componentes resueltos:")
        for i, comp in enumerate(componentes, 1):
            print(f"   {i}. {comp['codigo']}: ${comp.get('valor_total', 0):,}")
        print()
        
        totales = calcular_totales_agregados('BIM_L3_001_PLUS', tablas_l3)
        print(f"💰 CAPEX Total: ${totales['capex_total']:,}")
        print(f"📈 Capacidad/Mes: {totales['capacidad_mes']:,} evaluaciones")
        print(f"👥 Personal: {totales['personal_total']} personas")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()
    
    # Resolver CALE.n_2**
    print("📊 EJEMPLO 2: Resolver BIM_L3_002_STAR (CALE.n_2**)")
    print("-" * 80)
    try:
        componentes = resolver_l3_recursivo('BIM_L3_002_STAR', tablas_l3)
        print(f"✅ {len(componentes)} componentes resueltos:")
        for i, comp in enumerate(componentes, 1):
            print(f"   {i}. {comp['codigo']}: ${comp.get('valor_total', 0):,}")
        print()
        
        totales = calcular_totales_agregados('BIM_L3_002_STAR', tablas_l3)
        print(f"💰 CAPEX Total: ${totales['capex_total']:,}")
        print(f"📈 Capacidad/Mes: {totales['capacidad_mes']:,} evaluaciones")
        print(f"👥 Personal: {totales['personal_total']} personas")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()
    
    # Árbol de componentes
    print("🌳 ÁRBOL DE COMPONENTES BIM_L3_001_PLUS:")
    print("-" * 80)
    arbol = generar_arbol_componentes('BIM_L3_001_PLUS', tablas_l3)
    print(arbol)
    
    print("=" * 80)
    print("  ✅ PRUEBA COMPLETADA")
    print("=" * 80)


if __name__ == "__main__":
    main()
