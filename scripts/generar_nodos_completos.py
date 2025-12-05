"""
Script para completar TODOS los 197 nodos en el mapa interactivo
Extrae datos completos del JSON oficial
"""

import json

# Cargar datos oficiales
with open('TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nodos_completos = []

# Función para procesar cada nodo
def procesar_nodo(nodo, categoria_grupo):
    return {
        'nodo_id': nodo.get('centro_id', f'NODO_DESCONOCIDO_{len(nodos_completos)}'),
        'nombre': nodo.get('municipio', 'DESCONOCIDO'),
        'departamento': nodo.get('departamento', ''),
        'codigo_dane': nodo.get('codigo_dane', ''),
        'coords': {
            'lat': nodo.get('latitud'),
            'lon': nodo.get('longitud')
        },
        'demanda_anual': nodo.get('demanda_estimada_anual', 0),
        'cluster_municipios': nodo.get('total_municipios_cluster', 0),
        'tipo_id': nodo.get('tipo_l3', categoria_grupo),
        'tipo_nombre': obtener_nombre_tipo(nodo.get('tipo_l3', categoria_grupo)),
        'tipo_color': obtener_color_tipo(nodo.get('tipo_l3', categoria_grupo)),
        'tipo_icono': obtener_icono_tipo(nodo.get('tipo_l3', categoria_grupo)),
        'categoria': nodo.get('variante', 'N/A'),
        'infraestructura': {
            'direccion_teorica': nodo.get('direccion_teorica', ''),
            'area_m2': nodo.get('area_m2', 0),
            'inmobiliaria': nodo.get('inmobiliaria', ''),
            'arriendo_mensual': nodo.get('arriendo_mensual', 0),
            'arriendo_anual': nodo.get('arriendo_anual', 0)
        } if nodo.get('direccion_teorica') else None,
        'valores_unitarios': obtener_valores_unitarios(nodo.get('tipo_l3', categoria_grupo))
    }

def obtener_nombre_tipo(tipo_id):
    mapping = {
        'L3.CALE.n_1.plus': 'CALE Metropolitano Premium',
        'L3.CALE.n_1.base': 'CALE Metropolitano Base',
        'L3.CALE.n_2.star': 'CALE Regional Plus',
        'L3.CALE.n_2.base': 'CALE Regional Base',
        'L3.CALE.n_3.base': 'CALE Provincial',
        'L3.SATELITE.c2': 'Satélite C2',
        'L3.SATELITE.c3': 'Satélite C3',
        'L3.SATELITE.c4': 'Satélite C4',
        'L3.SATELITE.c5': 'Satélite C5'
    }
    return mapping.get(tipo_id, tipo_id)

def obtener_color_tipo(tipo_id):
    mapping = {
        'L3.CALE.n_1.plus': '#E63946',
        'L3.CALE.n_1.base': '#F77F00',
        'L3.CALE.n_2.star': '#FCBF49',
        'L3.CALE.n_2.base': '#06D6A0',
        'L3.CALE.n_3.base': '#118AB2',
        'L3.SATELITE.c2': '#8338EC',
        'L3.SATELITE.c3': '#A05EB5',
        'L3.SATELITE.c4': '#C77DFF',
        'L3.SATELITE.c5': '#6C757D'
    }
    return mapping.get(tipo_id, '#8338EC')

def obtener_icono_tipo(tipo_id):
    mapping = {
        'L3.CALE.n_1.plus': '🔴',
        'L3.CALE.n_1.base': '🟠',
        'L3.CALE.n_2.star': '🟡',
        'L3.CALE.n_2.base': '🟢',
        'L3.CALE.n_3.base': '🔵',
        'L3.SATELITE.c2': '⬤',
        'L3.SATELITE.c3': '⬤',
        'L3.SATELITE.c4': '⬤',
        'L3.SATELITE.c5': '⬤'
    }
    return mapping.get(tipo_id, '⬤')

def obtener_valores_unitarios(tipo_id):
    valores = {
        'L3.CALE.n_1.plus': {
            'capex': 3728340000,
            'opex_anual': 2400000000,
            'capacidad_anual': 173040
        },
        'L3.CALE.n_1.base': {
            'capex': 2818340000,
            'opex_anual': 2400000000,
            'capacidad_anual': 127644
        },
        'L3.CALE.n_2.star': {
            'capex': 2196000000,
            'opex_anual': 1600000000,
            'capacidad_anual': 107520
        },
        'L3.CALE.n_2.base': {
            'capex': 1856000000,
            'opex_anual': 1600000000,
            'capacidad_anual': 71676
        },
        'L3.CALE.n_3.base': {
            'capex': 1228000000,
            'opex_anual': 800000000,
            'capacidad_anual': 40960
        },
        'L3.SATELITE.c2': {
            'capex': 800000000,
            'opex_anual': 400000000,
            'capacidad_anual': 10240
        },
        'L3.SATELITE.c3': {
            'capex': 600000000,
            'opex_anual': 300000000,
            'capacidad_anual': 5120
        },
        'L3.SATELITE.c4': {
            'capex': 400000000,
            'opex_anual': 200000000,
            'capacidad_anual': 2560
        },
        'L3.SATELITE.c5': {
            'capex': 400000000,
            'opex_anual': 200000000,
            'capacidad_anual': 2560
        }
    }
    return valores.get(tipo_id, {})

# Procesar todos los nodos principales
print("📦 Procesando nodos principales...")

for categoria, lista_nodos in data['nodos_principales'].items():
    for nodo in lista_nodos:
        nodos_completos.append(procesar_nodo(nodo, categoria))

print(f"✅ Procesados {len(nodos_completos)} nodos principales")

# Procesar satélites (si existen)
if 'satelites' in data:
    print("📦 Procesando satélites...")
    
    satelites_data = data['satelites']
    
    # Estructura de referencia para satélites
    if isinstance(satelites_data, dict) and 'total' in satelites_data:
        # Solo tenemos referencia, no datos completos
        print(f"ℹ️  Satélites: {satelites_data.get('total', 0)} (solo referencia)")
    elif isinstance(satelites_data, list):
        for sat in satelites_data:
            nodos_completos.append(procesar_nodo(sat, 'L3.SATELITE.c2'))
        print(f"✅ Procesados {len(satelites_data)} satélites")

# Generar archivo completo para el mapa
output = {
    'metadata': {
        'fecha': '2025-11-04',
        'version': '1.0_COMPLETA',
        'total_nodos': len(nodos_completos),
        'fuente': 'TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json'
    },
    'nodos': {nodo['nodo_id']: nodo for nodo in nodos_completos}
}

with open('data/nodos_completos_mapa.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print("✅ DATOS COMPLETOS GENERADOS")
print("=" * 80)
print(f"📊 Total nodos: {len(nodos_completos)}")
print(f"📁 Archivo: data/nodos_completos_mapa.json")
print("=" * 80)

# Resumen por tipo
from collections import Counter
tipos_count = Counter([n['tipo_id'] for n in nodos_completos])

print("\n📊 Distribución por tipo:")
for tipo, count in sorted(tipos_count.items()):
    nombre = obtener_nombre_tipo(tipo)
    icono = obtener_icono_tipo(tipo)
    print(f"  {icono} {nombre}: {count} nodos")

print("\n💡 Siguiente paso: Actualizar mapa-interactivo.js para cargar desde nodos_completos_mapa.json")
