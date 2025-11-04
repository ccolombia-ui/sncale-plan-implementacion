"""
Extracción de Tablas L2 del Google Doc Oficial - Anexo B
=========================================================

Extrae las tablas #11, #13, #15, #16, #17 que contienen las valorizaciones
de configuraciones L2 desde el documento oficial.

Tablas objetivo:
- Tabla #11: L2.pista_clase_I = $975,000,000 COP
- Tabla #13: L2.pista_clase_II = $680,000,000 COP
- Tabla #15: L2.pista_clase_III = $1,850,000,000 COP
- Tabla #16: L2.cale_teorico_24q = $243,063,465 COP
- Tabla #17: L2.cale_teorico_16q = $200,646,497 COP

Salida: TABLAS_L2_OFICIALES.json
"""

import json
from pathlib import Path

# Configuración
INPUT_FILE = Path('INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json')
L1_FILE = Path('TABLAS_L1_OFICIALES.json')
OUTPUT_FILE = Path('TABLAS_L2_OFICIALES.json')

# Mapeo de tablas L2
MAPEO_L2 = {
    11: {
        'nivel': 'pista_clase_I',
        'bim_id': 'BIM_L2_001',
        'titulo': 'Pista de Conducción Clase I',
        'descripcion': 'Configuración básica con 14 maniobras fundamentales (MANIOBRA_00 a MANIOBRA_13), pavimento asfáltico estándar y señalización horizontal/vertical. Apta para categorías A1, A2, B1, C1.',
        'l1_referencia': 'pista_clase_I',
        'categoria_licencias': 'A1, A2, B1, C1'
    },
    13: {
        'nivel': 'pista_clase_II',
        'bim_id': 'BIM_L2_002',
        'titulo': 'Pista de Conducción Clase II',
        'descripcion': 'Configuración intermedia que incluye toda la Clase I más 3 maniobras con remolque (MANIOBRA_14 a MANIOBRA_16). Pavimento reforzado y señalización intermedia. Apta para categorías A2, B1, C1.',
        'l1_referencia': 'pista_clase_II',
        'categoria_licencias': 'A2, B1, C1'
    },
    15: {
        'nivel': 'pista_clase_III',
        'bim_id': 'BIM_L2_003',
        'titulo': 'Pista de Conducción Clase III',
        'descripcion': 'Configuración avanzada que incluye toda la Clase II más 3 maniobras para vehículos pesados (MANIOBRA_17 a MANIOBRA_19). Pavimento especializado, señalización avanzada y área de carga/descarga. Apta para categorías B1, C1.',
        'l1_referencia': 'pista_clase_III',
        'categoria_licencias': 'B1, C1'
    },
    16: {
        'nivel': 'cale_teorico_24q',
        'bim_id': 'BIM_L2_004',
        'titulo': 'CALE Teórico 24 Cubículos',
        'descripcion': 'Configuración de centro teórico con capacidad para 24 cubículos simultáneos. Incluye edificación principal, aulas teóricas, batería de sanitarios, sistema de ventilación y aire acondicionado, mobiliario completo y tecnología educativa.',
        'l1_referencia': None,  # No tiene L1 (es edificación)
        'categoria_licencias': 'Todas'
    },
    17: {
        'nivel': 'cale_teorico_16q',
        'bim_id': 'BIM_L2_005',
        'titulo': 'CALE Teórico 16 Cubículos',
        'descripcion': 'Configuración de centro teórico con capacidad para 16 cubículos simultáneos. Incluye edificación principal, aulas teóricas, batería de sanitarios, sistema de ventilación, mobiliario y tecnología educativa básica.',
        'l1_referencia': None,  # No tiene L1 (es edificación)
        'categoria_licencias': 'Todas'
    }
}

def main():
    print("=" * 70)
    print("EXTRACCIÓN DE TABLAS L2 - GOOGLE DOC OFICIAL")
    print("=" * 70)
    print()
    
    # 1. Cargar informe reclasificado
    print("📂 Cargando informe reclasificado...")
    if not INPUT_FILE.exists():
        print(f"❌ ERROR: No se encuentra {INPUT_FILE}")
        return
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        informe = json.load(f)
    
    tablas_l2 = informe.get('tablas_l2', [])
    print(f"✅ Encontradas {len(tablas_l2)} tablas L2 en informe")
    print()
    
    # 2. Cargar componentes L1 (para referencias)
    print("📂 Cargando componentes L1...")
    componentes_l1 = {}
    if L1_FILE.exists():
        with open(L1_FILE, 'r', encoding='utf-8') as f:
            datos_l1 = json.load(f)
            componentes_l1 = datos_l1.get('tablas_l1', {})
        print(f"✅ Cargados {len(componentes_l1)} niveles L1")
    else:
        print("⚠️  No se encontró archivo L1 (opcional)")
    print()
    
    # 3. Procesar tablas L2
    print("⚙️  Procesando tablas L2...")
    print()
    
    resultado_final = {
        'fuente': {
            'documento': 'MUNAY_5.2__anexo_b__DEFINITIVO',
            'google_doc_id': '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
            'url': 'https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE/edit',
            'fecha_extraccion': '2025-11-03'
        },
        'tablas_l2': {}
    }
    
    for tabla in tablas_l2:
        num_tabla = tabla.get('numero')
        
        if num_tabla not in MAPEO_L2:
            continue
        
        config = MAPEO_L2[num_tabla]
        nivel = config['nivel']
        
        # Extraer valor de la tabla
        todas_filas = tabla.get('todas_filas', [])
        valor_cop = 'N/A'
        
        if len(todas_filas) >= 2:
            fila_datos = todas_filas[1]
            if len(fila_datos) >= 2:
                valor_cop = fila_datos[1]
        
        print(f"📊 Tabla #{num_tabla}: {config['titulo']}")
        print(f"   💰 Valor: {valor_cop}")
        print(f"   🔗 BIM ID: {config['bim_id']}")
        
        # Obtener componentes L1 si aplica
        componentes_l1_asociados = []
        if config['l1_referencia'] and config['l1_referencia'] in componentes_l1:
            componentes_l1_asociados = componentes_l1[config['l1_referencia']].get('componentes', [])
            print(f"   🔧 Componentes L1: {len(componentes_l1_asociados)}")
        else:
            print(f"   🔧 Componentes L1: No aplica (edificación)")
        
        # Estructura de datos L2
        datos_l2 = {
            'nivel': nivel,
            'bim_id': config['bim_id'],
            'titulo': config['titulo'],
            'descripcion': config['descripcion'],
            'tabla_numero': num_tabla,
            'elemento_index': tabla.get('elemento_index'),
            'valorización': {
                'valor_cop': valor_cop,
                'valor_numerico': valor_cop.replace('$', '').replace(',', '').replace(' ', '')
            },
            'categoria_licencias': config['categoria_licencias'],
            'componentes_l1': componentes_l1_asociados,
            'num_componentes_l1': len(componentes_l1_asociados)
        }
        
        resultado_final['tablas_l2'][nivel] = datos_l2
        print()
    
    # 4. Guardar resultado
    print("💾 Guardando resultado...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(resultado_final, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Archivo generado: {OUTPUT_FILE}")
    print()
    
    # 5. Resumen final
    print("=" * 70)
    print("RESUMEN DE EXTRACCIÓN L2")
    print("=" * 70)
    print()
    
    total_valorizado = 0
    for nivel, datos in resultado_final['tablas_l2'].items():
        valor_str = datos['valorización']['valor_numerico']
        try:
            valor_num = int(valor_str) if valor_str != 'N/A' else 0
            total_valorizado += valor_num
        except:
            pass
    
    print(f"📊 Configuraciones L2 procesadas: {len(resultado_final['tablas_l2'])}")
    print(f"💰 Valorización total: ${total_valorizado:,} COP")
    print()
    
    for nivel, datos in resultado_final['tablas_l2'].items():
        print(f"   • {datos['bim_id']} - {datos['titulo']}")
        print(f"     Valor: {datos['valorización']['valor_cop']}")
        print(f"     Componentes L1: {datos['num_componentes_l1']}")
        print(f"     Tabla: #{datos['tabla_numero']}")
        print()
    
    print("=" * 70)
    print("✅ EXTRACCIÓN L2 COMPLETADA")
    print("=" * 70)
    print()
    print("SIGUIENTE PASO:")
    print("Ejecutar: python regenerar_fichas_l2_oficial.py")
    print("=" * 70)

if __name__ == '__main__':
    main()
