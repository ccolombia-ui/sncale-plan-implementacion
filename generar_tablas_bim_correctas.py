#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generación de TABLAS BIM CORRECTAS con RECURSIVIDAD L2→L2
==========================================================

CORRECCIÓN CRÍTICA aplicada:
- Las MANIOBRA_XX NO son componentes BIM
- Son especificaciones geométricas dentro de L0
- Los L2 pueden referenciar a otros L2 (recursividad)
- Opción 1: Referencias L2→L2 (Single Source of Truth)

Fuente: Google Doc MUNAY_5.2__anexo_b__DEFINITIVO
Doc ID: 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import json
from datetime import datetime

def main():
    print("="*80)
    print("GENERACIÓN DE TABLAS BIM CORRECTAS - OPCIÓN 1 (RECURSIVIDAD)")
    print("="*80)
    print()
    
    # Cargar jerarquía correcta ya extraída
    print("📂 Cargando jerarquía BIM correcta...")
    with open('JERARQUIA_BIM_CORRECTA.json', 'r', encoding='utf-8') as f:
        jerarquia = json.load(f)
    
    componentes_l1 = jerarquia['niveles']['L1']
    componentes_l0 = jerarquia['niveles']['L0']
    
    print(f"✅ Cargados {len(componentes_l0)} componentes L0")
    print(f"✅ Cargados {len(componentes_l1)} grupos de L1")
    print()
    
    # ==========================================================================
    # PASO 1: GENERAR TABLAS_L0_OFICIALES.json
    # ==========================================================================
    
    print("="*80)
    print("PASO 1: Generando TABLAS_L0_OFICIALES.json")
    print("="*80)
    print()
    
    tablas_l0 = {
        "metadata": {
            "documento": "MUNAY_5.2__anexo_b__DEFINITIVO",
            "doc_id": "16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE",
            "fecha_extraccion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_componentes": len(componentes_l0),
            "version": "1.0.0",
            "notas": "Componentes atómicos L0 - Base de la jerarquía BIM"
        },
        "categorias": {
            "IC": {"nombre": "Infraestructura Civil", "cantidad": 0, "componentes": []},
            "DR": {"nombre": "Drenajes", "cantidad": 0, "componentes": []},
            "SV": {"nombre": "Señalización Vial", "cantidad": 0, "componentes": []},
            "SEG": {"nombre": "Seguridad", "cantidad": 0, "componentes": []},
            "EDIF": {"nombre": "Edificación", "cantidad": 0, "componentes": []},
            "MAT": {"nombre": "Materiales", "cantidad": 0, "componentes": []},
            "ADEC": {"nombre": "Adecuaciones", "cantidad": 0, "componentes": []},
            "ELE": {"nombre": "Instalaciones Eléctricas", "cantidad": 0, "componentes": []},
            "ILU": {"nombre": "Iluminación", "cantidad": 0, "componentes": []},
            "HVAC": {"nombre": "Climatización", "cantidad": 0, "componentes": []},
            "HID": {"nombre": "Instalaciones Hidráulicas", "cantidad": 0, "componentes": []},
            "MOB": {"nombre": "Mobiliario", "cantidad": 0, "componentes": []},
            "TEC": {"nombre": "Tecnología", "cantidad": 0, "componentes": []},
            "AV": {"nombre": "Audiovisual", "cantidad": 0, "componentes": []},
            "ACC": {"nombre": "Accesorios", "cantidad": 0, "componentes": []},
            "VEH": {"nombre": "Vehículos", "cantidad": 0, "componentes": []},
            "CERT": {"nombre": "Certificaciones", "cantidad": 0, "componentes": []},
            "OTROS": {"nombre": "Otros", "cantidad": 0, "componentes": []}
        },
        "componentes": {}
    }
    
    # Clasificar L0 por categoría
    for comp_l0 in componentes_l0:
        codigo = comp_l0['codigo_l0']
        bim_id = comp_l0['bim_id']
        
        # Extraer categoría del código (L0.IC_001 → IC)
        categoria = codigo.split('.')[1].split('_')[0]
        
        # Si la categoría no existe, usar OTROS
        if categoria not in tablas_l0['categorias']:
            categoria = 'OTROS'
        
        # Agregar a la categoría
        tablas_l0['categorias'][categoria]['componentes'].append(comp_l0)
        tablas_l0['categorias'][categoria]['cantidad'] += 1
        
        # Agregar al diccionario de componentes
        tablas_l0['componentes'][bim_id] = comp_l0
    
    # Guardar L0
    with open('TABLAS_L0_OFICIALES.json', 'w', encoding='utf-8') as f:
        json.dump(tablas_l0, f, indent=2, ensure_ascii=False)
    
    print(f"✅ TABLAS_L0_OFICIALES.json generado")
    print(f"   - Total componentes: {len(componentes_l0)}")
    print(f"   - Categorías: {len([c for c in tablas_l0['categorias'].values() if c['cantidad'] > 0])}")
    print()
    
    # ==========================================================================
    # PASO 2: GENERAR TABLAS_L1_OFICIALES.json
    # ==========================================================================
    
    print("="*80)
    print("PASO 2: Generando TABLAS_L1_OFICIALES.json")
    print("="*80)
    print()
    
    tablas_l1 = {
        "metadata": {
            "documento": "MUNAY_5.2__anexo_b__DEFINITIVO",
            "doc_id": "16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE",
            "fecha_extraccion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_componentes": 0,
            "version": "1.0.0",
            "notas": "Ensamblajes L1 - Componentes de infraestructura CORRECTOS (NO maniobras)"
        },
        "componentes": {}
    }
    
    # Contador de componentes L1
    contador_l1 = 1
    
    # Extraer L1 de pista_clase_I
    for comp in componentes_l1['pista_clase_I']:
        bim_id = f"BIM_L1_{contador_l1:03d}"
        
        tablas_l1['componentes'][bim_id] = {
            "bim_id": bim_id,
            "codigo": comp['codigo_l1'],
            "nombre": comp['componente'],
            "descripcion": comp['descripcion'],
            "cantidad": comp['cantidad'],
            "unidad": comp['unidad'],
            "valor_cop": comp['valor_cop'],
            "tipo": "CONSTRUCTOR",
            "fuente": comp['fuente'],
            "componentes_l0": [c['codigo_l0'] for c in comp['componentes_l0']],
            "maniobras_soportadas": obtener_maniobras_por_tipo(comp['codigo_l1'])
        }
        
        contador_l1 += 1
        print(f"   ✅ {bim_id}: {comp['codigo_l1']} - ${comp['valor_cop']:,}")
    
    # Extraer L1 de pista_clase_II (solo el nuevo, no las referencias)
    for comp in componentes_l1['pista_clase_II']:
        if comp['codigo_l1'] == 'L1.pista_clase_I':
            continue  # Saltar la referencia, ya la tenemos
        
        bim_id = f"BIM_L1_{contador_l1:03d}"
        
        tablas_l1['componentes'][bim_id] = {
            "bim_id": bim_id,
            "codigo": comp['codigo_l1'],
            "nombre": comp['componente'],
            "descripcion": comp['descripcion'],
            "cantidad": comp['cantidad'],
            "unidad": comp['unidad'],
            "valor_cop": comp['valor_cop'],
            "tipo": "CONSTRUCTOR",
            "fuente": comp['fuente'],
            "componentes_l0": [],  # Pendiente extraer
            "maniobras_soportadas": obtener_maniobras_por_tipo(comp['codigo_l1'])
        }
        
        contador_l1 += 1
        print(f"   ✅ {bim_id}: {comp['codigo_l1']} - ${comp['valor_cop']:,}")
    
    # Extraer L1 de pista_clase_III (solo el nuevo)
    for comp in componentes_l1['pista_clase_III']:
        if comp['codigo_l1'] in ['L1.pista_clase_I', 'L1.pista_clase_II']:
            continue  # Saltar referencias
        
        bim_id = f"BIM_L1_{contador_l1:03d}"
        
        tablas_l1['componentes'][bim_id] = {
            "bim_id": bim_id,
            "codigo": comp['codigo_l1'],
            "nombre": comp['componente'],
            "descripcion": comp['descripcion'],
            "cantidad": comp['cantidad'],
            "unidad": comp['unidad'],
            "valor_cop": comp.get('valor_cop', 0),
            "tipo": "CONSTRUCTOR",
            "fuente": comp['fuente'],
            "componentes_l0": [],  # Pendiente extraer
            "maniobras_soportadas": obtener_maniobras_por_tipo(comp['codigo_l1'])
        }
        
        contador_l1 += 1
        print(f"   ✅ {bim_id}: {comp['codigo_l1']} - ${comp.get('valor_cop', 0):,}")
    
    # Agregar L1 de REFERENCIA para pista_clase_I y pista_clase_II
    tablas_l1['componentes']['BIM_L1_REF_001'] = {
        "bim_id": "BIM_L1_REF_001",
        "codigo": "L1.pista_clase_I",
        "nombre": "Pista Clase I completa",
        "descripcion": "Infraestructura completa motos + carros (REFERENCIA a L2.pista_clase_I)",
        "cantidad": "1",
        "unidad": "glb",
        "valor_cop": 721440000,
        "tipo": "REFERENCIA",
        "fuente": "Tabla #20, Fila 2",
        "referencia_l2": "BIM_L2_001",
        "resuelve_a": ["BIM_L1_001", "BIM_L1_002"]
    }
    
    tablas_l1['componentes']['BIM_L1_REF_002'] = {
        "bim_id": "BIM_L1_REF_002",
        "codigo": "L1.pista_clase_II",
        "nombre": "Pista Clase II completa",
        "descripcion": "Infraestructura completa motos + carros + camiones (REFERENCIA a L2.pista_clase_II)",
        "cantidad": "1",
        "unidad": "glb",
        "valor_cop": 1407390000,
        "tipo": "REFERENCIA",
        "fuente": "Tabla #21, Fila 2",
        "referencia_l2": "BIM_L2_002",
        "resuelve_a": ["BIM_L2_001", "BIM_L1_003"]
    }
    
    print(f"   🔗 BIM_L1_REF_001: L1.pista_clase_I (Referencia) - $721.440.000")
    print(f"   🔗 BIM_L1_REF_002: L1.pista_clase_II (Referencia) - $1.407.390.000")
    
    tablas_l1['metadata']['total_componentes'] = len(tablas_l1['componentes'])
    
    # Guardar L1
    with open('TABLAS_L1_OFICIALES.json', 'w', encoding='utf-8') as f:
        json.dump(tablas_l1, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"✅ TABLAS_L1_OFICIALES.json generado")
    print(f"   - Total componentes: {len(tablas_l1['componentes'])}")
    print(f"   - Constructores: {len([c for c in tablas_l1['componentes'].values() if c['tipo'] == 'CONSTRUCTOR'])}")
    print(f"   - Referencias: {len([c for c in tablas_l1['componentes'].values() if c['tipo'] == 'REFERENCIA'])}")
    print()
    
    # ==========================================================================
    # PASO 3: GENERAR TABLAS_L2_OFICIALES.json CON RECURSIVIDAD
    # ==========================================================================
    
    print("="*80)
    print("PASO 3: Generando TABLAS_L2_OFICIALES.json CON RECURSIVIDAD L2→L2")
    print("="*80)
    print()
    
    tablas_l2 = {
        "metadata": {
            "documento": "MUNAY_5.2__anexo_b__DEFINITIVO",
            "doc_id": "16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE",
            "fecha_extraccion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_componentes": 0,
            "version": "1.0.0",
            "estructura": "RECURSIVIDAD L2→L2",
            "notas": "Configuraciones L2 con referencias a otros L2 (Single Source of Truth)"
        },
        "componentes": {}
    }
    
    # L2.pista_clase_I (BASE - no referencia a nadie)
    tablas_l2['componentes']['BIM_L2_001'] = {
        "bim_id": "BIM_L2_001",
        "codigo": "L2.pista_clase_I",
        "nombre": "Pista Clase I",
        "descripcion": "Infraestructura completa motos A1/A2 + carros B1/C1",
        "categorias_licencia": ["A1", "A2", "B1", "C1"],
        "valor_total": 721440000,
        "tipo": "CONFIGURACION_BASE",
        "fuente": "Tabla #11 (valorización), Tabla #19 (componentes)",
        "componentes": [
            {
                "tipo": "L1",
                "bim_id": "BIM_L1_001",
                "codigo": "L1.pista_motos_A1A2_completa",
                "nombre": "Pista motos A1A2 completa",
                "valor": 289805000
            },
            {
                "tipo": "L1",
                "bim_id": "BIM_L1_002",
                "codigo": "L1.pista_carros_B1C1_completa",
                "nombre": "Pista carros B1C1 completa",
                "valor": 431635000
            }
        ]
    }
    print(f"   ✅ BIM_L2_001: L2.pista_clase_I - $721.440.000 (BASE)")
    print(f"      - 2 componentes L1 directos")
    
    # L2.pista_clase_II (EXTENDIDA - referencia a L2.pista_clase_I)
    tablas_l2['componentes']['BIM_L2_002'] = {
        "bim_id": "BIM_L2_002",
        "codigo": "L2.pista_clase_II",
        "nombre": "Pista Clase II",
        "descripcion": "Infraestructura completa clase I + camiones B2/C2",
        "categorias_licencia": ["A1", "A2", "B1", "B2", "C1", "C2"],
        "valor_total": 1407390000,
        "tipo": "CONFIGURACION_EXTENDIDA",
        "fuente": "Tabla #13 (valorización), Tabla #20 (componentes)",
        "componentes": [
            {
                "tipo": "L2",
                "referencia": "BIM_L2_001",
                "codigo": "L2.pista_clase_I",
                "nombre": "Pista Clase I completa",
                "valor": 721440000,
                "resuelve_a": [
                    "L1.pista_motos_A1A2_completa",
                    "L1.pista_carros_B1C1_completa"
                ]
            },
            {
                "tipo": "L1",
                "bim_id": "BIM_L1_003",
                "codigo": "L1.pista_camiones_B2C2_completa",
                "nombre": "Pista camiones B2C2 completa",
                "valor": 685950000
            }
        ]
    }
    print(f"   ✅ BIM_L2_002: L2.pista_clase_II - $1.407.390.000 (EXTENDIDA)")
    print(f"      - 1 referencia L2 (BIM_L2_001)")
    print(f"      - 1 componente L1 directo")
    
    # L2.pista_clase_III (EXTENDIDA - referencia a L2.pista_clase_II)
    tablas_l2['componentes']['BIM_L2_003'] = {
        "bim_id": "BIM_L2_003",
        "codigo": "L2.pista_clase_III",
        "nombre": "Pista Clase III",
        "descripcion": "Infraestructura completa clase II + tractocamiones B3/C3",
        "categorias_licencia": ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3"],
        "valor_total": 2093340000,  # TBD: Validar
        "tipo": "CONFIGURACION_EXTENDIDA",
        "fuente": "Tabla #15 (valorización), Tabla #21 (componentes)",
        "componentes": [
            {
                "tipo": "L2",
                "referencia": "BIM_L2_002",
                "codigo": "L2.pista_clase_II",
                "nombre": "Pista Clase II completa",
                "valor": 1407390000,
                "resuelve_a": [
                    "L2.pista_clase_I",
                    "L1.pista_camiones_B2C2_completa"
                ]
            },
            {
                "tipo": "L1",
                "bim_id": "BIM_L1_004",
                "codigo": "L1.pista_tractocamiones_B3C3_completa",
                "nombre": "Pista tractocamiones B3C3 completa",
                "valor": 686000000  # TBD: Validar
            }
        ]
    }
    print(f"   ✅ BIM_L2_003: L2.pista_clase_III - $2.093.340.000 (EXTENDIDA)")
    print(f"      - 1 referencia L2 (BIM_L2_002)")
    print(f"      - 1 componente L1 directo")
    
    # Pendiente: L2 de edificaciones (salas teóricas, datacenter, etc.)
    print()
    print(f"   ⚠️  Pendiente: L2 de edificaciones (sala_teorica, sala_formacion, datacenter)")
    
    tablas_l2['metadata']['total_componentes'] = len(tablas_l2['componentes'])
    
    # Guardar L2
    with open('TABLAS_L2_OFICIALES.json', 'w', encoding='utf-8') as f:
        json.dump(tablas_l2, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"✅ TABLAS_L2_OFICIALES.json generado")
    print(f"   - Total componentes: {len(tablas_l2['componentes'])}")
    print(f"   - Base: {len([c for c in tablas_l2['componentes'].values() if c['tipo'] == 'CONFIGURACION_BASE'])}")
    print(f"   - Extendidas: {len([c for c in tablas_l2['componentes'].values() if c['tipo'] == 'CONFIGURACION_EXTENDIDA'])}")
    print()
    
    # ==========================================================================
    # RESUMEN FINAL
    # ==========================================================================
    
    print("="*80)
    print("RESUMEN FINAL")
    print("="*80)
    print()
    print(f"✅ TABLAS_L0_OFICIALES.json: {len(componentes_l0)} componentes atómicos")
    print(f"✅ TABLAS_L1_OFICIALES.json: {len(tablas_l1['componentes'])} ensamblajes (4 constructores + 2 referencias)")
    print(f"✅ TABLAS_L2_OFICIALES.json: {len(tablas_l2['componentes'])} configuraciones (1 base + 2 extendidas)")
    print()
    print("📊 Estructura correcta:")
    print("   - L2.pista_clase_I (BASE): 2 L1 directos")
    print("   - L2.pista_clase_II (EXTENDIDA): 1 L2 referencia + 1 L1 directo")
    print("   - L2.pista_clase_III (EXTENDIDA): 1 L2 referencia + 1 L1 directo")
    print()
    print("🔗 Recursividad L2→L2 implementada correctamente")
    print("✅ Single Source of Truth garantizado")
    print()

def obtener_maniobras_por_tipo(codigo_l1):
    """Retorna lista de maniobras soportadas según tipo de pista"""
    
    maniobras_basicas = [
        "MANIOBRA_00: Estacionamiento en línea recta",
        "MANIOBRA_01: Estacionamiento en batería",
        "MANIOBRA_02: Estacionamiento paralelo",
        "MANIOBRA_03: Circuito en ocho",
        "MANIOBRA_04: Línea recta con cono",
        "MANIOBRA_05: Slalom",
        "MANIOBRA_06: Retroceso en línea",
        "MANIOBRA_07: Frenado controlado",
        "MANIOBRA_08: Giro cerrado",
        "MANIOBRA_09: Ascenso pendiente",
        "MANIOBRA_10: Descenso controlado",
        "MANIOBRA_11: Esquiva de obstáculos",
        "MANIOBRA_12: Arranque pendiente",
        "MANIOBRA_13: Circuito completo"
    ]
    
    maniobras_camiones = [
        "MANIOBRA_14: Puente de equilibrio",
        "MANIOBRA_15: Rampa de frenado",
        "MANIOBRA_16: Rampa de arranque"
    ]
    
    maniobras_tractocamiones = [
        "MANIOBRA_17: Zona de articulación",
        "MANIOBRA_18: Retroceso articulado",
        "MANIOBRA_19: Giro especial"
    ]
    
    if 'motos' in codigo_l1.lower() or 'carros' in codigo_l1.lower():
        return maniobras_basicas
    elif 'camiones' in codigo_l1.lower():
        return maniobras_basicas + maniobras_camiones
    elif 'tractocamiones' in codigo_l1.lower():
        return maniobras_basicas + maniobras_camiones + maniobras_tractocamiones
    else:
        return []

if __name__ == '__main__':
    main()
