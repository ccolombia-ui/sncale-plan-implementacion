"""
Script para procesar IEBM desde GeoJSON y asignar CALE más cercano
Genera tabla para Google Sheets con:
- municipio
- codigo_dane_iebm
- sede_iebm
- grado_9 (placeholder)
- grado_10 (placeholder)
- grado_11 (placeholder)
- ingreso_ES (placeholder)
- pendiente (placeholder)
- nodo_cale_mas_cercano (n2/n3/C2-C5, excluyendo n1)

IMPORTANTE: Excluye CALEs n1, solo considera n2, n3, C2, C3, C4, C5
"""

import json
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

GEOJSON_PATH = 'aktriel/01__min_transporte/01__calescopio/2__documentos/iniciativa_viable/finale/dataset/analisis_demanda/1_raw/geo_data__dane/gjs_sedesSISE/gjsSEDES.geojson'
CSV_CALES = 'arquitectura_red_cale_nacional_MAPEADO.csv'
OUTPUT_CSV = 'iebm_con_cale_asignado.csv'

# ============================================================================
# FUNCIÓN: Calcular distancia haversine entre dos puntos
# ============================================================================

def haversine(lon1, lat1, lon2, lat2):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos
    usando la fórmula de Haversine
    """
    # Convertir grados decimales a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Fórmula de haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # Radio de la Tierra en kilómetros
    r = 6371

    return c * r

# ============================================================================
# FUNCIÓN: Encontrar CALE más cercano (excluyendo n1)
# ============================================================================

def encontrar_cale_mas_cercano(iebm_lat, iebm_lon, df_cales):
    """
    Encuentra el CALE más cercano a una IEBM
    Excluye CALEs de categoría Cat.A+ y Cat.A (n1)
    """
    distancia_minima = float('inf')
    cale_mas_cercano = None
    distancia_km = None

    for idx, cale in df_cales.iterrows():
        # Calcular distancia
        dist = haversine(iebm_lon, iebm_lat, cale['longitud'], cale['latitud'])

        if dist < distancia_minima:
            distancia_minima = dist
            cale_mas_cercano = cale['centro_id']
            distancia_km = dist

    return cale_mas_cercano, round(distancia_km, 2)

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 80)
    print("PROCESAMIENTO DE IEBM CON ASIGNACIÓN DE CALE MÁS CERCANO")
    print("=" * 80)
    print()

    # 1. Cargar GeoJSON de IEBM
    print("[1/5] Cargando GeoJSON de instituciones educativas...")
    with open(GEOJSON_PATH, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    total_features = len(geojson_data['features'])
    print(f"      Total instituciones en GeoJSON: {total_features:,}")

    # Filtrar solo las que tienen EDUCACIÓN MEDIA
    iebm_media = [
        f for f in geojson_data['features']
        if f['properties'].get('NIVEL') and 'MEDIA' in f['properties']['NIVEL'].upper()
        and f['properties'].get('ESTADO') == 'ACTIVA'
    ]
    print(f"      Instituciones con Educación Media (activas): {len(iebm_media):,}")
    print()

    # 2. Cargar CALEs y filtrar (solo n2, n3, C2-C5)
    print("[2/5] Cargando centros CALE...")
    df_cales = pd.read_csv(CSV_CALES)
    print(f"      Total centros CALE: {len(df_cales)}")

    # Filtrar: excluir Cat.A+ y Cat.A (n1)
    df_cales_filtrado = df_cales[
        ~df_cales['categoria_cale'].isin(['Cat.A+', 'Cat.A'])
    ].copy()
    print(f"      CALEs después de excluir n1: {len(df_cales_filtrado)}")
    print(f"      Categorías incluidas: {df_cales_filtrado['categoria_cale'].unique()}")
    print()

    # 3. Procesar cada IEBM
    print("[3/5] Procesando IEBM y calculando CALE más cercano...")
    print("      (Esto puede tardar varios minutos...)")

    resultados = []
    total = len(iebm_media)

    for idx, feature in enumerate(iebm_media, 1):
        props = feature['properties']
        geom = feature['geometry']

        # Validar coordenadas
        if not geom or geom['type'] != 'Point':
            continue

        lon, lat = geom['coordinates']

        if pd.isna(lon) or pd.isna(lat):
            continue

        # Encontrar CALE más cercano
        cale_cercano, distancia = encontrar_cale_mas_cercano(lat, lon, df_cales_filtrado)

        # Estructura de datos
        resultado = {
            'municipio': props.get('MUNICIPIO', ''),
            'departamento': props.get('DEPARTAMEN', ''),
            'codigo_dane_iebm': props.get('COD_DANE', ''),
            'sede_iebm': props.get('NOMBRE_INS', ''),
            'direccion': props.get('DIRECCION', ''),
            'zona': props.get('ZONA', ''),
            'sector': props.get('SECTOR', ''),
            'latitud': lat,
            'longitud': lon,
            'grado_9': 0,  # Placeholder - requiere datos adicionales
            'grado_10': 0,  # Placeholder
            'grado_11': 0,  # Placeholder
            'ingreso_ES': 0,  # Placeholder
            'pendiente': 'SIN_DATOS_MATRICULA',  # Placeholder
            'nodo_cale_mas_cercano': cale_cercano,
            'distancia_km': distancia
        }

        resultados.append(resultado)

        # Progreso
        if idx % 1000 == 0:
            print(f"      Procesadas: {idx:,} / {total:,} ({idx/total*100:.1f}%)")

    print(f"      [OK] Procesamiento completado: {len(resultados):,} IEBM")
    print()

    # 4. Crear DataFrame
    print("[4/5] Creando DataFrame...")
    df_iebm = pd.DataFrame(resultados)

    # Estadísticas
    print("      Estadísticas:")
    print(f"      - Total IEBM procesadas: {len(df_iebm):,}")
    print(f"      - IEBM por departamento (top 10):")
    top_deptos = df_iebm['departamento'].value_counts().head(10)
    for depto, count in top_deptos.items():
        print(f"        {depto}: {count:,}")
    print()
    print(f"      - IEBM por CALE asignado (top 10):")
    top_cales = df_iebm['nodo_cale_mas_cercano'].value_counts().head(10)
    for cale, count in top_cales.items():
        print(f"        {cale}: {count:,}")
    print()

    # 5. Guardar CSV
    print("[5/5] Guardando CSV...")
    df_iebm.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print(f"      [OK] CSV guardado: {OUTPUT_CSV}")
    print()

    print("=" * 80)
    print("PROCESAMIENTO COMPLETADO EXITOSAMENTE")
    print("=" * 80)
    print()
    print("SIGUIENTE PASO:")
    print("1. Revisar CSV generado")
    print("2. Ejecutar script para subir a Google Sheets")
    print("3. Completar datos de matrícula (grados 9, 10, 11) si están disponibles")

if __name__ == '__main__':
    main()
