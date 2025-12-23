"""
Script para actualizar cubículos de municipios de Cundinamarca en el JSON
"""

import json

# Mapeo de cubículos para los municipios de Cundinamarca
CUBICULOS_CUNDINAMARCA = {
    'CHIA': 4,
    'FUNZA': 4,
    'FUSAGASUGA': 4,
    'UBATE': 4,
    'CAJICA': 4,
    'FACATATIVA': 2,
    'SOPO': 2,
    'MADRID': 2,
    'LA CALERA': 2,
    'CAQUEZA': 2,
    'PACHO': 2,
    'SIBATE': 2,
    'SILVANIA': 2,
    'CHOCONTA': 2
}

# Leer JSON
ruta_json = 'data/satelites_completos_141_nodos.json'
with open(ruta_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

actualizados = 0

# Actualizar cada satélite
for satelite in data['satelites']:
    municipio = satelite.get('municipio', '').upper().strip()
    
    if municipio in CUBICULOS_CUNDINAMARCA:
        cubiculos_nuevo = CUBICULOS_CUNDINAMARCA[municipio]
        cubiculos_anterior = satelite.get('cubiculos', 'N/A')
        satelite['cubiculos'] = cubiculos_nuevo
        actualizados += 1
        print(f"✓ {municipio}: {cubiculos_anterior} → {cubiculos_nuevo} cubículos")

# Guardar JSON actualizado
with open(ruta_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ JSON actualizado: {ruta_json}")
print(f"   Total actualizado: {actualizados} municipios de Cundinamarca")
