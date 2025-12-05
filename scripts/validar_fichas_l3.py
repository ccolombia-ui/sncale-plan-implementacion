#!/usr/bin/env python3
"""
Validador y corrector de fichas L3
Valida que las fichas L3 sean UNITARIAS y coherentes con composición desde L0/L1/L2
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FICHAS_L3 = ROOT / 'fichas_l3'

# ============================================================================
# CONFIGURACIONES L3 UNITARIAS (1 unidad de cada configuración)
# ============================================================================

L3_CONFIGS = {
    'CALE.n_1': {
        'nombre': 'Centro Metropolitano',
        'descripcion': 'Configuración completa para centros en ciudades metropolitanas',
        'componentes': [
            {'ref': 'L2.pista_clase_3', 'nombre': 'Pista Evaluación Clase III', 'valor_unit': 1_850_000_000, 'cant': 1},
            {'ref': 'L2.pista_clase_2', 'nombre': 'Pista Evaluación Clase II', 'valor_unit': 980_000_000, 'cant': 1},
            {'ref': 'L2.pista_clase_1', 'nombre': 'Pista Evaluación Clase I', 'valor_unit': 750_000_000, 'cant': 1},
            {'ref': 'L1.sala_24_cubiculos', 'nombre': 'Sala Evaluación Teórica (24 cubículos)', 'valor_unit': 186_000_000, 'cant': 1},
            {'ref': 'L0.simulador_c3', 'nombre': 'Simulador Conducción Clase III', 'valor_unit': 450_000_000, 'cant': 2},
            {'ref': 'L2.edificacion_admin', 'nombre': 'Infraestructura Civil Base', 'valor_unit': 2_400_000_000, 'cant': 1},
        ],
        'cantidad_nacional': {'base': 17, 'variante': 0},
        'variantes': ['CALE.n_1+']
    },
    'CALE.n_1+': {
        'nombre': 'Centro Metropolitano Plus',
        'descripcion': 'Configuración metropolitana con pista Clase II adicional',
        'componentes': [
            # Incluye todo de CALE.n_1
            {'ref': 'L2.pista_clase_3', 'nombre': 'Pista Evaluación Clase III', 'valor_unit': 1_850_000_000, 'cant': 1},
            {'ref': 'L2.pista_clase_2', 'nombre': 'Pista Evaluación Clase II', 'valor_unit': 980_000_000, 'cant': 2},  # ← 2 unidades
            {'ref': 'L2.pista_clase_1', 'nombre': 'Pista Evaluación Clase I', 'valor_unit': 750_000_000, 'cant': 1},
            {'ref': 'L1.sala_24_cubiculos', 'nombre': 'Sala Evaluación Teórica (24 cubículos)', 'valor_unit': 186_000_000, 'cant': 1},
            {'ref': 'L0.simulador_c3', 'nombre': 'Simulador Conducción Clase III', 'valor_unit': 450_000_000, 'cant': 2},
            {'ref': 'L2.edificacion_admin', 'nombre': 'Infraestructura Civil Base', 'valor_unit': 2_400_000_000, 'cant': 1},
            # Componente adicional de CALE.n_2
            {'ref': 'L1.sala_16_cubiculos', 'nombre': 'Sala Evaluación Teórica (16 cubículos)', 'valor_unit': 124_000_000, 'cant': 1},
        ],
        'cantidad_nacional': {'base': 3, 'variante': 0}
    },
    'CALE.n_2': {
        'nombre': 'Centro Subregional',
        'descripcion': 'Configuración para centros en capitales subregionales',
        'componentes': [
            {'ref': 'L2.pista_clase_2', 'nombre': 'Pista Evaluación Clase II', 'valor_unit': 980_000_000, 'cant': 1},
            {'ref': 'L2.pista_clase_1', 'nombre': 'Pista Evaluación Clase I', 'valor_unit': 750_000_000, 'cant': 1},
            {'ref': 'L1.sala_16_cubiculos', 'nombre': 'Sala Evaluación Teórica (16 cubículos)', 'valor_unit': 124_000_000, 'cant': 1},
            {'ref': 'L0.simulador_c2', 'nombre': 'Simulador Conducción Clase II', 'valor_unit': 350_000_000, 'cant': 1},
            {'ref': 'L2.edificacion_media', 'nombre': 'Infraestructura Civil Media', 'valor_unit': 1_800_000_000, 'cant': 1},
        ],
        'cantidad_nacional': {'base': 4, 'variante': 0},
        'variantes': ['CALE.n_2**']
    },
    'CALE.n_2**': {
        'nombre': 'Centro Subregional Plus',
        'descripcion': 'Configuración subregional con pistas Clase I adicionales',
        'componentes': [
            {'ref': 'L2.pista_clase_2', 'nombre': 'Pista Evaluación Clase II', 'valor_unit': 980_000_000, 'cant': 1},
            {'ref': 'L2.pista_clase_1', 'nombre': 'Pista Evaluación Clase I', 'valor_unit': 750_000_000, 'cant': 3},  # ← 3 unidades
            {'ref': 'L1.sala_16_cubiculos', 'nombre': 'Sala Evaluación Teórica (16 cubículos)', 'valor_unit': 124_000_000, 'cant': 1},
            {'ref': 'L0.simulador_c2', 'nombre': 'Simulador Conducción Clase II', 'valor_unit': 350_000_000, 'cant': 1},
            {'ref': 'L2.edificacion_media', 'nombre': 'Infraestructura Civil Media', 'valor_unit': 1_800_000_000, 'cant': 1},
        ],
        'cantidad_nacional': {'base': 16, 'variante': 0}
    },
    'CALE.n_3': {
        'nombre': 'Centro Local',
        'descripcion': 'Configuración para centros en municipios intermedios',
        'componentes': [
            {'ref': 'L2.pista_clase_1', 'nombre': 'Pista Evaluación Clase I', 'valor_unit': 750_000_000, 'cant': 1},
            {'ref': 'L1.sala_4_cubiculos', 'nombre': 'Sala Evaluación Teórica (4 cubículos)', 'valor_unit': 62_000_000, 'cant': 1},
            {'ref': 'L0.simulador_c1', 'nombre': 'Simulador Conducción Clase I', 'valor_unit': 250_000_000, 'cant': 1},
            {'ref': 'L2.edificacion_basica', 'nombre': 'Infraestructura Civil Básica', 'valor_unit': 900_000_000, 'cant': 1},
        ],
        'cantidad_nacional': {'base': 16, 'variante': 0}
    }
}

def calcular_valor_unitario(config):
    """Calcula el valor unitario total de una configuración L3"""
    total = 0
    for comp in config['componentes']:
        subtotal = comp['valor_unit'] * comp['cant']
        total += subtotal
    return total

def validar_ficha_actual(archivo_html, config_name):
    """Valida si una ficha actual tiene valores correctos"""
    try:
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Extraer valorización total actual
        match_valor = re.search(r'<h3>💰 Valorización Total</h3>\s*<p>\$([0-9.]+)', contenido)
        if not match_valor:
            return None, "No se encontró valorización total"
        
        valor_actual = int(match_valor.group(1).replace('.', ''))
        
        # Calcular valor esperado UNITARIO
        config = L3_CONFIGS[config_name]
        valor_esperado = calcular_valor_unitario(config)
        
        # Verificar si es unitario o nacional
        cant_nacional = config['cantidad_nacional']['base']
        valor_nacional = valor_esperado * cant_nacional
        
        if abs(valor_actual - valor_nacional) < 1000:
            return 'NACIONAL', f"Muestra valor nacional (${valor_nacional:,}) en vez de unitario (${valor_esperado:,})"
        elif abs(valor_actual - valor_esperado) < 1000:
            return 'UNITARIO', "✅ Correcto - valor unitario"
        else:
            return 'DESCONOCIDO', f"Valor ${valor_actual:,} no coincide con unitario (${valor_esperado:,}) ni nacional (${valor_nacional:,})"
            
    except Exception as e:
        return None, f"Error: {e}"

def generar_reporte_validacion():
    """Genera reporte de validación de fichas L3"""
    print('🔍 VALIDANDO FICHAS L3 ACTUALES\n')
    print('=' * 100)
    print(f"{'Configuración':<15} | {'Archivo':<20} | {'Estado':<15} | {'Análisis'}")
    print('-' * 100)
    
    fichas_a_validar = {
        'CALE.n_1': 'BIM_L3_001.html',
        'CALE.n_2': 'BIM_L3_002.html',
        'CALE.n_3': 'BIM_L3_003.html',
    }
    
    resultados = []
    
    for config_name, archivo in fichas_a_validar.items():
        archivo_path = FICHAS_L3 / archivo
        
        if not archivo_path.exists():
            print(f"{config_name:<15} | {archivo:<20} | {'❌ NO EXISTE':<15} | Archivo no encontrado")
            resultados.append({'config': config_name, 'estado': 'NO_EXISTE'})
            continue
        
        estado, analisis = validar_ficha_actual(archivo_path, config_name)
        
        if estado == 'UNITARIO':
            emoji = '✅'
        elif estado == 'NACIONAL':
            emoji = '🔴'
        else:
            emoji = '⚠️'
        
        print(f"{config_name:<15} | {archivo:<20} | {emoji} {estado:<13} | {analisis}")
        resultados.append({'config': config_name, 'estado': estado, 'analisis': analisis})
    
    print('=' * 100)
    
    # Resumen
    print('\n📊 RESUMEN DE VALIDACIÓN\n')
    
    for config_name, config in L3_CONFIGS.items():
        valor_unit = calcular_valor_unitario(config)
        cant_nacional = config['cantidad_nacional']['base']
        valor_nacional = valor_unit * cant_nacional
        
        print(f"📦 {config_name}")
        print(f"   Componentes: {len(config['componentes'])}")
        print(f"   Valor UNITARIO (1 unidad): ${valor_unit:,}")
        print(f"   Cantidad nacional: {cant_nacional} nodos")
        print(f"   Valor NACIONAL total: ${valor_nacional:,}")
        print()
    
    # Recomendaciones
    print('🎯 ACCIONES REQUERIDAS\n')
    
    hay_problemas = False
    for resultado in resultados:
        if resultado['estado'] == 'NACIONAL':
            hay_problemas = True
            print(f"🔴 {resultado['config']}: Convertir de valor nacional a unitario")
            print(f"   - Dividir 'Valorización Total' entre cantidad de nodos")
            print(f"   - Cambiar 'Cant. Base' de 20/16 a 1")
            print(f"   - Actualizar 'Valor Total' de componentes\n")
    
    if not hay_problemas:
        print('✅ Todas las fichas están correctas como unitarias')
    else:
        print('\n⚠️  CRÍTICO: Las fichas actuales muestran valores NACIONALES, no UNITARIOS')
        print('   Esto hace que el modelo BIM sea inconsistente L0→L1→L2→L3→L4→L5')

if __name__ == '__main__':
    generar_reporte_validacion()
