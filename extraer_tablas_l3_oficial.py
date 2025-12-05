#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracción de tablas L3 desde Google Doc oficial
Procesa tablas #2-#9 (configuraciones CALE + metadatos)

FUENTE ÚNICA: Google Doc ID 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import json
import re

# Mapeo de tablas L3 a BIM IDs
MAPEO_L3_VALORIZACION = {
    3: {
        'nivel': 'cale_n1_metropolitano',
        'bim_id': 'BIM_L3_001',
        'titulo': 'CALE.n_1 - Centro Metropolitano',
        'descripcion': 'Configuración completa para centros de enseñanza en ciudades metropolitanas (20 nodos base + 3 variante+)',
        'tipo_cale': 'Metropolitano',
        'cantidad_base': 20,
        'cantidad_variante': 3
    },
    5: {
        'nivel': 'cale_n2_subregional',
        'bim_id': 'BIM_L3_002',
        'titulo': 'CALE.n_2 - Centro Subregional',
        'descripcion': 'Configuración para centros en capitales subregionales (20 nodos base + 16 variante**)',
        'tipo_cale': 'Subregional',
        'cantidad_base': 20,
        'cantidad_variante': 16
    },
    7: {
        'nivel': 'cale_n3_local',
        'bim_id': 'BIM_L3_003',
        'titulo': 'CALE.n_3 - Centro Local',
        'descripcion': 'Configuración básica para centros locales (16 nodos)',
        'tipo_cale': 'Local',
        'cantidad_base': 16,
        'cantidad_variante': 0
    },
    9: {
        'nivel': 'red_satelites',
        'bim_id': 'BIM_L3_004',
        'titulo': 'Red Nacional de Satélites',
        'descripcion': 'Distribución de 140 satélites en categorías C2-C5 para cobertura nacional',
        'tipo_cale': 'Red Satélites',
        'cantidad_total': 140,
        'distribucion': 'C2: 40 | C3: 40 | C4: 40 | C5: 20'
    }
}

MAPEO_L3_METADATA = {
    2: 'cale_n1_metropolitano',
    4: 'cale_n2_subregional', 
    6: 'cale_n3_local',
    8: 'red_satelites'
}

def limpiar_valor_cop(valor_str):
    """Extrae el valor numérico de una cadena COP"""
    if not valor_str or valor_str == '-':
        return 0
    # Eliminar $ y comas
    valor_limpio = valor_str.replace('$', '').replace(',', '').strip()
    try:
        return int(valor_limpio)
    except ValueError:
        return 0

def procesar_tabla_l3_valorizacion(tabla, mapeo_config):
    """Procesa una tabla de valorización L3"""
    
    componentes = []
    total_valorizacion = 0
    
    # Saltar la primera fila (encabezados)
    for i, fila in enumerate(tabla['todas_filas'][1:], start=1):
        if len(fila) < 7:
            continue
            
        componente = fila[0].strip()
        descripcion = fila[1].strip()
        ref_bim = fila[2].strip()
        vr_unitario_str = fila[3].strip()
        cant_variante_str = fila[4].strip()
        cant_base_str = fila[5].strip()
        vr_total_str = fila[6].strip()
        
        # Limpiar valores
        vr_unitario = limpiar_valor_cop(vr_unitario_str)
        cant_variante = int(cant_variante_str) if cant_variante_str.isdigit() else 0
        cant_base = int(cant_base_str) if cant_base_str.isdigit() else 0
        vr_total = limpiar_valor_cop(vr_total_str)
        
        componentes.append({
            'numero': i,
            'componente': componente,
            'descripcion': descripcion,
            'referencia_bim': ref_bim,
            'valor_unitario_cop': vr_unitario,
            'cantidad_variante': cant_variante,
            'cantidad_base': cant_base,
            'valor_total_cop': vr_total,
            'fuente': f"Tabla #{tabla['numero']}, Fila {i+1}"
        })
        
        total_valorizacion += vr_total
    
    return {
        'bim_id': mapeo_config['bim_id'],
        'nivel': mapeo_config['nivel'],
        'titulo': mapeo_config['titulo'],
        'descripcion': mapeo_config['descripcion'],
        'tipo_cale': mapeo_config['tipo_cale'],
        'cantidad_base': mapeo_config.get('cantidad_base', 0),
        'cantidad_variante': mapeo_config.get('cantidad_variante', 0),
        'cantidad_total': mapeo_config.get('cantidad_total', 0),
        'distribucion': mapeo_config.get('distribucion', ''),
        'componentes': componentes,
        'valorizacion': {
            'total_cop': total_valorizacion,
            'total_cop_formateado': f"${total_valorizacion:,}".replace(',', '.')
        },
        'metadatos': {
            'fuente_tabla': tabla['numero'],
            'total_filas': len(componentes),
            'elemento_index': tabla['elemento_index']
        }
    }

def procesar_tabla_l3_metadata(tabla):
    """Procesa una tabla de metadatos L3"""
    
    # Las tablas de metadatos tienen estructura variable
    # Tabla #2: Tipo CALE, Cantidad, Descripción modificador, Mapa
    # Extraer información clave
    
    metadata = {
        'numero_tabla': tabla['numero'],
        'elemento_index': tabla['elemento_index'],
        'filas': tabla['filas'],
        'columnas': tabla['columnas']
    }
    
    # Intentar extraer datos estructurados
    if 'todas_filas' in tabla and len(tabla['todas_filas']) > 1:
        # Primera fila = encabezados
        encabezados = tabla['todas_filas'][0]
        
        # Procesar filas de datos
        datos = []
        for fila in tabla['todas_filas'][1:]:
            if len(fila) >= len(encabezados):
                fila_dict = {}
                for i, encabezado in enumerate(encabezados):
                    if i < len(fila):
                        fila_dict[encabezado.strip()] = fila[i].strip()
                datos.append(fila_dict)
        
        metadata['encabezados'] = encabezados
        metadata['datos'] = datos
    
    return metadata

def main():
    print("="*70)
    print("EXTRACCIÓN TABLAS L3 - GOOGLE DOC OFICIAL")
    print("="*70)
    print()
    
    # Cargar informe reclasificado
    print("📂 Cargando informe reclasificado...")
    with open('INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json', 'r', encoding='utf-8') as f:
        informe = json.load(f)
    
    # Extraer tablas L3 de valorización
    tablas_l3_valorizacion = informe.get('tablas_l3_valorizacion', [])
    print(f"✅ Encontradas {len(tablas_l3_valorizacion)} tablas L3 de valorización en informe")
    
    # Extraer tablas L3 de metadatos
    tablas_l3_metadata = informe.get('tablas_l3_metadata', [])
    print(f"✅ Encontradas {len(tablas_l3_metadata)} tablas L3 de metadatos en informe")
    print()
    
    # Procesar tablas de valorización
    configuraciones_l3 = []
    total_general = 0
    
    print("🔨 Procesando tablas de valorización L3...")
    print()
    
    for tabla in tablas_l3_valorizacion:
        num_tabla = tabla['numero']
        
        if num_tabla in MAPEO_L3_VALORIZACION:
            mapeo_config = MAPEO_L3_VALORIZACION[num_tabla]
            
            config_procesada = procesar_tabla_l3_valorizacion(tabla, mapeo_config)
            configuraciones_l3.append(config_procesada)
            
            total_general += config_procesada['valorizacion']['total_cop']
            
            print(f"📊 Tabla #{num_tabla}: {mapeo_config['titulo']}")
            print(f"   💰 Valor total: {config_procesada['valorizacion']['total_cop_formateado']} COP")
            print(f"   🔗 BIM ID: {mapeo_config['bim_id']}")
            print(f"   🔧 Componentes: {len(config_procesada['componentes'])}")
            if 'cantidad_base' in mapeo_config:
                print(f"   📍 Nodos base: {mapeo_config['cantidad_base']}")
            if 'cantidad_variante' in mapeo_config and mapeo_config['cantidad_variante'] > 0:
                print(f"   ➕ Variante: {mapeo_config['cantidad_variante']}")
            if 'cantidad_total' in mapeo_config:
                print(f"   📍 Total satélites: {mapeo_config['cantidad_total']}")
            print()
    
    # Procesar tablas de metadatos
    metadatos_l3 = []
    
    print("🔨 Procesando tablas de metadatos L3...")
    print()
    
    for tabla in tablas_l3_metadata:
        num_tabla = tabla['numero']
        
        if num_tabla in MAPEO_L3_METADATA:
            nivel = MAPEO_L3_METADATA[num_tabla]
            metadata_procesada = procesar_tabla_l3_metadata(tabla)
            metadata_procesada['nivel'] = nivel
            metadatos_l3.append(metadata_procesada)
            
            print(f"📊 Tabla #{num_tabla}: Metadatos {nivel}")
            print(f"   📋 Filas: {metadata_procesada['filas']}")
            print(f"   📋 Columnas: {metadata_procesada['columnas']}")
            print()
    
    # Asociar metadatos con configuraciones
    for config in configuraciones_l3:
        nivel = config['nivel']
        metadata_nivel = [m for m in metadatos_l3 if m['nivel'] == nivel]
        if metadata_nivel:
            config['metadata_adicional'] = metadata_nivel[0]
    
    # Resumen
    print("="*70)
    print("RESUMEN DE EXTRACCIÓN")
    print("="*70)
    print()
    print(f"📊 Configuraciones L3 procesadas: {len(configuraciones_l3)}")
    print(f"💰 Valorización total: ${total_general:,}".replace(',', '.') + " COP")
    print()
    
    # Guardar resultado
    resultado = {
        'fuente': {
            'documento': 'Google Doc MUNAY_5.2__anexo_b__DEFINITIVO',
            'doc_id': '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
            'tablas_valorizacion': list(MAPEO_L3_VALORIZACION.keys()),
            'tablas_metadata': list(MAPEO_L3_METADATA.keys())
        },
        'resumen': {
            'total_configuraciones': len(configuraciones_l3),
            'valorizacion_total_cop': total_general,
            'valorizacion_total_formateado': f"${total_general:,}".replace(',', '.') + " COP"
        },
        'configuraciones': configuraciones_l3,
        'metadatos': metadatos_l3
    }
    
    output_file = 'TABLAS_L3_OFICIALES.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Archivo generado: {output_file}")
    print()
    print("✅ Extracción L3 completada exitosamente")
    print()

if __name__ == '__main__':
    main()
