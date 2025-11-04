"""
Script para generar relaciones jerárquicas COMPLETAS:
- 56 nodos principales (Cat.A+ hasta Cat.C1)
- 141 satélites (C2-C5) asignados a sus nodos principales

Entrada: 
  - arquitectura_red_cale_nacional_MAPEADO.csv (tiene las relaciones)
  - data/nodos_completos_mapa.json (nodos principales)
  - data/satelites_completos_141_nodos.json (satélites)

Salida: 
  - data/relaciones_jerarquicas_completas.json (56 nodos → 141 satélites)
"""

import csv
import json
from pathlib import Path
from collections import defaultdict

# Colores por categoría
TIPO_COLORS = {
    'L3.CALE.n_1.plus': '#E63946',   # Cat.A+ - Rojo
    'L3.CALE.n_1.base': '#F77F00',   # Cat.A - Naranja
    'L3.CALE.n_2.star': '#FCBF49',   # Cat.B** - Amarillo
    'L3.CALE.n_2.base': '#06D6A0',   # Cat.B - Verde
    'L3.CALE.n_3': '#118AB2',        # Cat.C1 - Azul
    'L3.SATELITE.c2': '#8338EC',     # C2 - Morado intenso
    'L3.SATELITE.c3': '#A05EB5',     # C3 - Morado medio
    'L3.SATELITE.c4': '#C77DFF',     # C4 - Morado claro
    'L3.SATELITE.c5': '#6C757D'      # C5 - Gris
}

def generar_relaciones_completas():
    """Genera las relaciones jerárquicas completas"""
    
    # Rutas
    csv_path = Path('arquitectura_red_cale_nacional_MAPEADO.csv')
    nodos_path = Path('data/nodos_completos_mapa.json')
    satelites_path = Path('data/satelites_completos_141_nodos.json')
    output_path = Path('data/relaciones_jerarquicas_completas.json')
    
    print("📥 Cargando datos...")
    
    # Cargar nodos principales
    with open(nodos_path, 'r', encoding='utf-8') as f:
        nodos_data = json.load(f)
        # El formato es: {"nodos": {"NODO_01": {...}, "NODO_02": {...}}}
        nodos_principales = nodos_data.get('nodos', nodos_data)
    
    # Cargar satélites
    with open(satelites_path, 'r', encoding='utf-8') as f:
        satelites_data = json.load(f)
        satelites = satelites_data['satelites']
    
    print(f"✅ Cargados {len(nodos_principales)} nodos principales")
    print(f"✅ Cargados {len(satelites)} satélites")
    
    # Agrupar satélites por nodo principal
    satelites_por_nodo = defaultdict(list)
    
    for satelite in satelites:
        nodo_padre = satelite['nodo_principal']
        
        # Crear objeto simplificado para subnodo
        subnodo = {
            'id': satelite['centro_id'],
            'nombre': satelite['municipio'],
            'departamento': satelite['departamento'],
            'tipo': 'SATELITE',
            'categoria': satelite['categoria_cale'],
            'color': satelite['color'],
            'demanda': satelite['demanda_estimada_anual'],
            'latitud': satelite['latitud'],
            'longitud': satelite['longitud'],
            'distancia_km': satelite['distancia_al_nodo_km']
        }
        
        satelites_por_nodo[nodo_padre].append(subnodo)
    
    # Construir relaciones
    relaciones = {}
    
    for nodo_id, nodo_info in nodos_principales.items():
        # Info del nodo padre
        relaciones[nodo_id] = {
            'info': {
                'nombre': nodo_info.get('municipio', nodo_info.get('nombre', 'N/A')),
                'categoria': nodo_info.get('variante', nodo_info.get('categoria_cale', 'N/A')),
                'tipo_l3': nodo_info.get('tipo_l3', 'N/A'),
                'color': nodo_info.get('color', '#999'),
                'demanda': nodo_info.get('demanda_estimada_anual', nodo_info.get('demanda_anual', 0)),
                'latitud': nodo_info.get('latitud', nodo_info.get('coords', {}).get('lat', 0)),
                'longitud': nodo_info.get('longitud', nodo_info.get('coords', {}).get('lon', 0))
            },
            'subnodos': satelites_por_nodo.get(nodo_id, [])
        }
    
    # Ordenar subnodos por distancia
    for nodo_id in relaciones:
        relaciones[nodo_id]['subnodos'].sort(key=lambda x: x['distancia_km'])
    
    # Estadísticas
    total_subnodos = sum(len(r['subnodos']) for r in relaciones.values())
    nodos_con_satelites = sum(1 for r in relaciones.values() if len(r['subnodos']) > 0)
    nodos_sin_satelites = len(relaciones) - nodos_con_satelites
    
    # Crear output
    output = {
        'metadata': {
            'version': '2.0',
            'fecha': '2025-11-04',
            'descripcion': 'Relaciones jerárquicas completas: 56 nodos principales → 141 satélites',
            'total_nodos_principales': len(relaciones),
            'total_satelites': total_subnodos,
            'nodos_con_satelites': nodos_con_satelites,
            'nodos_sin_satelites': nodos_sin_satelites
        },
        'relaciones': relaciones
    }
    
    # Guardar
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    # Resumen
    print(f"\n✅ Relaciones generadas!")
    print(f"📊 Estadísticas:")
    print(f"  - Total nodos principales: {len(relaciones)}")
    print(f"  - Total satélites asignados: {total_subnodos}")
    print(f"  - Nodos CON satélites: {nodos_con_satelites}")
    print(f"  - Nodos SIN satélites: {nodos_sin_satelites}")
    
    # Top 5 nodos con más satélites
    print(f"\n🏆 Top 5 nodos con más satélites:")
    top_nodos = sorted(relaciones.items(), key=lambda x: len(x[1]['subnodos']), reverse=True)[:5]
    for nodo_id, data in top_nodos:
        count = len(data['subnodos'])
        nombre = data['info']['nombre']
        print(f"  {nodo_id}: {nombre} → {count} satélites")
    
    print(f"\n💾 Archivo generado: {output_path}")
    
    return relaciones

if __name__ == '__main__':
    relaciones = generar_relaciones_completas()
