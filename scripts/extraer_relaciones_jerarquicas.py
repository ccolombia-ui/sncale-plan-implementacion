"""
Script para extraer relaciones jerárquicas de nodos
Analiza el campo 'nodo_principal' para determinar qué nodos tienen subnodos asociados
"""

import json
from collections import defaultdict

# Cargar datos
with open('TABLAS_L4_INSTANCIAS_197_NODOS_OFICIAL.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Estructura para almacenar relaciones
relaciones = defaultdict(list)
nodos_info = {}

# Función para procesar nodos
def procesar_nodos(nodos_list, categoria):
    for nodo in nodos_list:
        centro_id = nodo.get('centro_id')
        nodo_principal = nodo.get('nodo_principal', centro_id)
        
        # Guardar info del nodo
        nodos_info[centro_id] = {
            'centro_id': centro_id,
            'municipio': nodo.get('municipio', ''),
            'departamento': nodo.get('departamento', ''),
            'tipo_l3': nodo.get('tipo_l3', ''),
            'variante': nodo.get('variante', ''),
            'categoria_cale': nodo.get('categoria_cale', ''),
            'nodo_principal': nodo_principal,
            'demanda_estimada_anual': nodo.get('demanda_estimada_anual', 0),
            'latitud': nodo.get('latitud'),
            'longitud': nodo.get('longitud'),
            'es_principal': centro_id == nodo_principal
        }
        
        # Si tiene nodo_principal diferente, es un subnodo
        if centro_id != nodo_principal:
            relaciones[nodo_principal].append(centro_id)

# Procesar todas las categorías
print("🔍 Analizando relaciones jerárquicas...\n")

for categoria, nodos in data['nodos_principales'].items():
    procesar_nodos(nodos, categoria)

# Procesar satélites si existen
if 'satelites' in data:
    satelites_data = data.get('satelites', {})
    
    # Buscar en diferentes estructuras posibles
    for key in ['C2', 'C3', 'C4', 'C5', 'lista']:
        if key in satelites_data and isinstance(satelites_data[key], list):
            procesar_nodos(satelites_data[key], f'SATELITE_{key}')

# Imprimir resultados
print("=" * 80)
print("📊 RELACIONES JERÁRQUICAS ENCONTRADAS")
print("=" * 80)

nodos_con_subnodos = {k: v for k, v in relaciones.items() if v}

if nodos_con_subnodos:
    print(f"\n✅ Se encontraron {len(nodos_con_subnodos)} nodos principales con subnodos asociados:\n")
    
    for nodo_principal, subnodos in sorted(nodos_con_subnodos.items()):
        info_principal = nodos_info.get(nodo_principal, {})
        municipio = info_principal.get('municipio', 'DESCONOCIDO')
        categoria = info_principal.get('variante', info_principal.get('categoria_cale', ''))
        
        print(f"🔴 {nodo_principal}: {municipio} ({categoria})")
        print(f"   └─ {len(subnodos)} subnodos asociados:")
        
        for subnodo_id in subnodos[:10]:  # Mostrar máximo 10
            info_sub = nodos_info.get(subnodo_id, {})
            sub_municipio = info_sub.get('municipio', 'DESCONOCIDO')
            sub_categoria = info_sub.get('variante', info_sub.get('categoria_cale', ''))
            demanda = info_sub.get('demanda_estimada_anual', 0)
            
            print(f"      • {subnodo_id}: {sub_municipio} ({sub_categoria}) - {demanda:,} eval/año")
        
        if len(subnodos) > 10:
            print(f"      ... y {len(subnodos) - 10} más")
        print()
else:
    print("\n⚠️  No se encontraron relaciones jerárquicas en el campo 'nodo_principal'")
    print("\n💡 Buscando relaciones alternativas...")
    
    # Buscar por proximidad geográfica o departamento
    nodos_por_depto = defaultdict(list)
    for nodo_id, info in nodos_info.items():
        if info.get('es_principal'):
            depto = info.get('departamento', '')
            if depto:
                nodos_por_depto[depto].append(nodo_id)
    
    print(f"\n📍 Nodos agrupados por departamento:")
    for depto, nodos in sorted(nodos_por_depto.items())[:5]:
        print(f"   {depto}: {len(nodos)} nodos - {', '.join(nodos[:3])}")

# Generar archivo de salida con relaciones
output_data = {
    'metadata': {
        'fecha_analisis': '2025-11-04',
        'total_nodos': len(nodos_info),
        'nodos_con_subnodos': len(nodos_con_subnodos),
        'total_relaciones': sum(len(v) for v in relaciones.values())
    },
    'relaciones_jerarquicas': {
        nodo_id: {
            'info': nodos_info.get(nodo_id, {}),
            'subnodos': [
                {
                    'centro_id': sub_id,
                    **nodos_info.get(sub_id, {})
                }
                for sub_id in subnodos
            ]
        }
        for nodo_id, subnodos in nodos_con_subnodos.items()
    },
    'nodos_principales': [
        nodo_id for nodo_id, info in nodos_info.items() if info.get('es_principal')
    ]
}

with open('data/relaciones_jerarquicas_nodos.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print(f"✅ Archivo generado: data/relaciones_jerarquicas_nodos.json")
print(f"📊 Total nodos analizados: {len(nodos_info)}")
print(f"🔗 Total relaciones jerárquicas: {sum(len(v) for v in relaciones.values())}")
print("=" * 80)
