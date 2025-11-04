"""
Script para extraer todos los satélites (141 nodos C2-C5) del CSV mapeado
y generar JSON completo con coordenadas y datos de clustering.

Entrada: arquitectura_red_cale_nacional_MAPEADO.csv
Salida: data/satelites_completos_141_nodos.json
"""

import csv
import json
from pathlib import Path

# Configuración de colores por categoría de satélite
SATELITE_COLORS = {
    'C2': '#8338EC',  # Morado intenso
    'C3': '#A05EB5',  # Morado medio
    'C4': '#C77DFF',  # Morado claro
    'C5': '#6C757D'   # Gris
}

# Categoría de demanda por tipo de satélite
SATELITE_TIPOS = {
    'C2': 'Satélite Categoría 2 (3000-4000 eval/año)',
    'C3': 'Satélite Categoría 3 (1500-2500 eval/año)',
    'C4': 'Satélite Categoría 4 (1000-1500 eval/año)',
    'C5': 'Satélite Categoría 5 (500-1000 eval/año)'
}

def extraer_satelites():
    """Extrae todos los satélites del CSV"""
    
    # Rutas
    csv_path = Path('arquitectura_red_cale_nacional_MAPEADO.csv')
    output_path = Path('data/satelites_completos_141_nodos.json')
    
    satelites = []
    distribucion = {'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0}
    
    print("📥 Leyendo CSV mapeado...")
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Filtrar solo satélites
            if row['tipo_centro'] != 'SATÉLITE':
                continue
            
            categoria = row['categoria_cale']
            distribucion[categoria] += 1
            
            # Construir objeto satélite
            satelite = {
                'centro_id': row['centro_id'],
                'tipo_centro': 'SATELITE',
                'codigo_dane': row['codigo_dane'],
                'municipio': row['municipio'].upper(),
                'departamento': row['departamento'].upper(),
                'latitud': float(row['latitud']),
                'longitud': float(row['longitud']),
                'categoria_cale': categoria,
                'tipo_l3': f'L3.SATELITE.{categoria.lower()}',
                'tipo_nombre': SATELITE_TIPOS[categoria],
                'color': SATELITE_COLORS[categoria],
                'demanda_estimada_anual': int(row['demanda_estimada_anual']),
                
                # Datos de clustering
                'nodo_principal': row['nodo_principal'],
                'codigo_dane_nodo': row['codigo_dane_nodo'],
                'total_municipios_cluster': int(row['total_municipios_cluster']),
                'distancia_al_nodo_km': float(row['distancia_promedio_km']),
                'distancia_maxima_cluster_km': float(row['distancia_maxima_km'])
            }
            
            satelites.append(satelite)
    
    # Ordenar por categoría y nombre
    satelites.sort(key=lambda x: (x['categoria_cale'], x['municipio']))
    
    # Crear output
    output = {
        'metadata': {
            'version': '1.0',
            'fecha': '2025-11-04',
            'descripcion': 'Satélites completos (C2-C5) extraídos de arquitectura_red_cale_nacional_MAPEADO.csv',
            'total_satelites': len(satelites),
            'distribucion': distribucion
        },
        'satelites': satelites
    }
    
    # Guardar
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    # Resumen
    print(f"\n✅ Extracción completada!")
    print(f"📊 Total de satélites: {len(satelites)}")
    print(f"\n📈 Distribución por categoría:")
    for cat, count in sorted(distribucion.items()):
        print(f"  {cat}: {count} nodos ({SATELITE_TIPOS[cat]})")
    
    print(f"\n💾 Archivo generado: {output_path}")
    
    # Validación de coordenadas
    sin_coords = [s for s in satelites if s['latitud'] == 0 or s['longitud'] == 0]
    if sin_coords:
        print(f"\n⚠️  Advertencia: {len(sin_coords)} satélites sin coordenadas:")
        for s in sin_coords[:5]:  # Mostrar solo primeros 5
            print(f"  - {s['centro_id']}: {s['municipio']}")
    else:
        print("\n✅ Todas las coordenadas están completas")
    
    return satelites, distribucion

if __name__ == '__main__':
    satelites, dist = extraer_satelites()
