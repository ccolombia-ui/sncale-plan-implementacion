#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar satélites C6 con los 109 municipios faltantes
Incluye coordenadas aproximadas de municipios colombianos
"""

import pandas as pd
import json
from pathlib import Path

# Rutas
CSV_PATH = r"C:\Users\USER\Downloads\4-CALES-TEORICOS.csv"
SATELITES_JSON_PATH = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"
OUTPUT_JSON_PATH = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_c6_nuevos.json"

# Diccionario de coordenadas aproximadas de municipios colombianos (centros aproximados)
COORDENADAS_MUNICIPIOS = {
    # Antioquia
    ('RIONEGRO', 'ANTIOQUIA'): (6.1551, -75.3736),
    ('BARBOSA', 'ANTIOQUIA'): (6.4392, -75.3317),
    ('GUARNE', 'ANTIOQUIA'): (6.2767, -75.4428),
    ('SABANETA', 'ANTIOQUIA'): (6.1513, -75.6169),
    ('ITAGUI', 'ANTIOQUIA'): (6.1848, -75.5994),
    ('APARTADO', 'ANTIOQUIA'): (7.8856, -76.6358),
    ('COPACABANA', 'ANTIOQUIA'): (6.3467, -75.5078),
    ('LA CEJA', 'ANTIOQUIA'): (6.0278, -75.4289),
    ('CHIGORODO', 'ANTIOQUIA'): (7.6667, -76.6833),
    ('GIRARDOTA', 'ANTIOQUIA'): (6.3778, -75.4469),
    ('EL CARMEN DE VIBORAL', 'ANTIOQUIA'): (6.0847, -75.3333),
    ('CAUCASIA', 'ANTIOQUIA'): (7.9833, -75.1917),
    ('MARINILLA', 'ANTIOQUIA'): (6.1733, -75.3367),
    ('ANDES', 'ANTIOQUIA'): (5.6567, -75.8781),
    ('CIUDAD BOLIVAR', 'ANTIOQUIA'): (5.8572, -76.0192),
    ('SANTA ROSA DE OSOS', 'ANTIOQUIA'): (6.6458, -75.4594),
    
    # Arauca
    ('SARAVENA', 'ARAUCA'): (6.9500, -71.8833),
    ('TAME', 'ARAUCA'): (6.4594, -71.7367),
    
    # Atlántico
    ('PUERTO COLOMBIA', 'ATLANTICO'): (11.0056, -74.8369),
    ('GALAPA', 'ATLANTICO'): (10.8983, -74.8819),
    ('SABANAGRANDE', 'ATLANTICO'): (10.7914, -74.7558),
    ('MALAMBO', 'ATLANTICO'): (10.8594, -74.7739),
    ('BARANOA', 'ATLANTICO'): (10.7939, -74.9164),
    ('SABANALARGA', 'ATLANTICO'): (10.6322, -74.9219),
    
    # Bolívar
    ('ARJONA', 'BOLIVAR'): (10.2583, -75.3472),
    ('SANTA ROSA', 'BOLIVAR'): (10.4097, -75.1528),
    ('TURBACO', 'BOLIVAR'): (10.3333, -75.4167),
    ('CLEMENCIA', 'BOLIVAR'): (10.5833, -75.4333),
    ('MAGANGUE', 'BOLIVAR'): (9.2417, -74.7544),
    
    # Boyacá
    ('DUITAMA', 'BOYACA'): (5.8267, -73.0342),
    ('COMBITA', 'BOYACA'): (5.6275, -73.3164),
    ('CHIQUINQUIRA', 'BOYACA'): (5.6181, -73.8189),
    ('SANTA ROSA DE VITERBO', 'BOYACA'): (5.8858, -72.9933),
    ('PAIPA', 'BOYACA'): (5.7814, -73.1167),
    ('PUERTO BOYACA', 'BOYACA'): (5.9833, -74.5833),
    ('VILLA DE LEYVA', 'BOYACA'): (5.6333, -73.5250),
    ('RAMIRIQUI', 'BOYACA'): (5.3950, -73.3231),
    
    # Caldas
    ('VILLAMARIA', 'CALDAS'): (5.0414, -75.5114),
    ('LA DORADA', 'CALDAS'): (5.4522, -74.6667),
    ('ANSERMA', 'CALDAS'): (5.2392, -75.7833),
    ('RIOSUCIO', 'CALDAS'): (5.4211, -75.7022),
    ('MANZANARES', 'CALDAS'): (5.2564, -75.1561),
    ('SUPIA', 'CALDAS'): (5.4472, -75.6442),
    ('CHINCHINA', 'CALDAS'): (4.9828, -75.6036),
    ('AGUADAS', 'CALDAS'): (5.6094, -75.4564),
    
    # Casanare
    ('VILLANUEVA', 'CASANARE'): (4.5667, -72.9500),
    ('AGUAZUL', 'CASANARE'): (5.1667, -72.5500),
    
    # Cauca
    ('SANTANDER DE QUILICHAO', 'CAUCA'): (3.0094, -76.4839),
    ('PIENDAMO', 'CAUCA'): (2.6389, -76.4167),
    ('MIRANDA', 'CAUCA'): (3.2492, -76.2325),
    ('PUERTO TEJADA', 'CAUCA'): (3.2317, -76.4175),
    ('PATIA', 'CAUCA'): (2.0667, -77.1167),
    
    # Cesar
    ('AGUACHICA', 'CESAR'): (8.3119, -73.6178),
    ('SAN DIEGO', 'CESAR'): (10.3422, -73.1681),
    ('EL PASO', 'CESAR'): (9.6578, -73.7561),
    ('BOSCONIA', 'CESAR'): (9.9667, -73.8833),
    ('SAN MARTIN', 'CESAR'): (7.9972, -73.5267),
    
    # Córdoba
    ('CERETE', 'CORDOBA'): (8.8856, -75.7928),
    ('LORICA', 'CORDOBA'): (9.2403, -75.8144),
    ('PLANETA RICA', 'CORDOBA'): (8.4089, -75.5858),
    ('SAHAGUN', 'CORDOBA'): (8.9458, -75.4453),
    ('LA APARTADA', 'CORDOBA'): (8.6667, -76.0500),
    
    # Cundinamarca (cerca de Bogotá)
    ('FACATATIVA', 'CUNDINAMARCA'): (4.8139, -74.3550),
    ('SOPO', 'CUNDINAMARCA'): (4.9086, -73.9422),
    ('MADRID', 'CUNDINAMARCA'): (4.7314, -74.2617),
    ('LA CALERA', 'CUNDINAMARCA'): (4.7217, -73.9678),
    ('CAQUEZA', 'CUNDINAMARCA'): (4.4089, -73.9472),
    ('PACHO', 'CUNDINAMARCA'): (5.1322, -74.1617),
    ('SIBATE', 'CUNDINAMARCA'): (4.4889, -74.2597),
    ('SILVANIA', 'CUNDINAMARCA'): (4.4039, -74.3881),
    ('CHOCONTA', 'CUNDINAMARCA'): (5.1422, -73.6839),
    
    # Huila
    ('RIVERA', 'HUILA'): (2.7767, -75.2561),
    ('PALERMO', 'HUILA'): (2.8872, -75.4536),
    ('GARZON', 'HUILA'): (2.1975, -75.6261),
    
    # La Guajira
    ('ALBANIA', 'LA GUAJIRA'): (11.0089, -72.6011),
    
    # Magdalena
    ('ARACATACA', 'MAGDALENA'): (10.5917, -74.1833),
    ('CIENAGA', 'MAGDALENA'): (11.0097, -74.2458),
    ('SITIONUEVO', 'MAGDALENA'): (10.7742, -74.7194),
    
    # Meta
    ('ACACIAS', 'META'): (3.9883, -73.7606),
    ('RESTREPO', 'META'): (4.2617, -73.5686),
    ('PUERTO LOPEZ', 'META'): (4.0850, -72.9572),
    
    # Nariño
    ('IPIALES', 'NARINO'): (0.8264, -77.6436),
    ('PUPIALES', 'NARINO'): (0.8667, -77.6167),
    ('TUQUERRES', 'NARINO'): (1.0869, -77.6206),
    ('TUMACO', 'NARINO'): (1.8067, -78.7656),
    ('LA UNION', 'NARINO'): (1.6000, -77.1333),
    ('GUACHUCAL', 'NARINO'): (1.0167, -77.7667),
    
    # Norte de Santander
    ('CUCUTA', 'NORTE DE SANTANDER'): (7.8939, -72.5078),
    ('OCAÑA', 'NORTE DE SANTANDER'): (8.2386, -73.3558),
    ('OCAÃA', 'NORTE DE SANTANDER'): (8.2386, -73.3558),
    ('PAMPLONA', 'NORTE DE SANTANDER'): (7.3758, -72.6492),
    
    # Quindío
    ('CIRCASIA', 'QUINDIO'): (4.6197, -75.6378),
    ('CALARCA', 'QUINDIO'): (4.5289, -75.6433),
    ('QUIMBAYA', 'QUINDIO'): (4.6208, -75.7678),
    ('LA TEBAIDA', 'QUINDIO'): (4.4544, -75.7878),
    
    # Risaralda
    ('LA VIRGINIA', 'RISARALDA'): (4.8983, -75.8819),
    ('SANTA ROSA DE CABAL', 'RISARALDA'): (4.8686, -75.6203),
    
    # Santander
    ('FLORIDABLANCA', 'SANTANDER'): (7.0644, -73.0867),
    ('PIEDECUESTA', 'SANTANDER'): (6.9778, -73.0500),
    ('BARBOSA', 'SANTANDER'): (5.9350, -73.6117),
    ('SAN GIL', 'SANTANDER'): (6.5558, -73.1336),
    ('LEBRIJA', 'SANTANDER'): (7.7269, -73.0078),
    ('SOCORRO', 'SANTANDER'): (6.4667, -73.2667),
    ('CHARALA', 'SANTANDER'): (6.2833, -73.1500),
    
    # Sucre
    ('SINCE', 'SUCRE'): (9.2447, -75.1686),
    
    # Tolima
    ('ALVARADO', 'TOLIMA'): (4.5736, -75.2078),
    ('MELGAR', 'TOLIMA'): (4.2044, -74.6428),
    ('MARIQUITA', 'TOLIMA'): (5.1986, -74.8878),
    ('CHAPARRAL', 'TOLIMA'): (3.7236, -75.4856),
    ('PURIFICACION', 'TOLIMA'): (3.8567, -74.9322),
    ('GUAMO', 'TOLIMA'): (4.0317, -74.9678),
    ('FRESNO', 'TOLIMA'): (5.1544, -75.0378),
    
    # Valle del Cauca
    ('GUADALAJARA DE BUGA', 'VALLE DEL CAUCA'): (3.8997, -76.2978),
    ('CARTAGO', 'VALLE DEL CAUCA'): (4.7467, -75.9117),
    ('DAGUA', 'VALLE DEL CAUCA'): (3.6597, -76.6867),
    ('TULUA', 'VALLE DEL CAUCA'): (4.0839, -76.1953),
    ('PRADERA', 'VALLE DEL CAUCA'): (3.4167, -76.2500),
    ('ANDALUCIA', 'VALLE DEL CAUCA'): (4.1350, -76.1819),
    ('YUMBO', 'VALLE DEL CAUCA'): (3.5878, -76.4989),
    ('BUENAVENTURA', 'VALLE DEL CAUCA'): (3.8833, -77.0317),
    ('EL CERRITO', 'VALLE DEL CAUCA'): (3.6833, -76.3167),
    ('ROLDANILLO', 'VALLE DEL CAUCA'): (4.4133, -76.1522),
    ('ZARZAL', 'VALLE DEL CAUCA'): (4.3939, -76.0728),
    ('FLORIDA', 'VALLE DEL CAUCA'): (3.3233, -76.2358),
    ('CAICEDONIA', 'VALLE DEL CAUCA'): (4.3322, -75.8236),
}

def normalizar_texto(texto):
    """Normaliza texto para comparación"""
    if pd.isna(texto):
        return ""
    texto = str(texto).upper().strip()
    reemplazos = {
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'Ñ': 'N', 'Ü': 'U'
    }
    for old, new in reemplazos.items():
        texto = texto.replace(old, new)
    return texto

def cargar_faltantes_csv():
    """Carga los municipios faltantes del CSV"""
    print("📄 Cargando municipios faltantes del CSV...")
    
    df = pd.read_csv(CSV_PATH, encoding='latin-1', skiprows=2)
    df.columns = ['GRUPO', 'N', 'DEPARTAMENTO', 'MUNICIPIO', 'TIPO_CALE', 'DEMANDA_EXPEDICION', 
                  'DEMANDA_PROYECTADA', 'NUM_AULAS', 'MOD_AULA', 'CICLOS_DIA', 'DIAS_OPERACION',
                  'CAPACIDAD_AULA_DIA', 'CAPACIDAD_AULA_ANO', 'OFERTA_REEVALUACION', 
                  'OFERTA_CONTINGENCIA', 'CAPACIDAD_ADICIONAL', 'PORCENTAJE']
    
    df_satelites = df[df['TIPO_CALE'] == 'SATELITE'].copy()
    df_satelites['MUNICIPIO_NORM'] = df_satelites['MUNICIPIO'].apply(normalizar_texto)
    df_satelites['DEPARTAMENTO_NORM'] = df_satelites['DEPARTAMENTO'].apply(normalizar_texto)
    
    # Cargar satélites existentes
    with open(SATELITES_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existentes = {
        (normalizar_texto(s['municipio']), normalizar_texto(s['departamento'])) 
        for s in data['satelites']
    }
    
    # Filtrar faltantes
    faltantes = []
    for idx, row in df_satelites.iterrows():
        clave = (row['MUNICIPIO_NORM'], row['DEPARTAMENTO_NORM'])
        if clave not in existentes:
            faltantes.append(row)
    
    print(f"✅ Encontrados {len(faltantes)} municipios faltantes")
    return faltantes

def generar_satelites_c6(faltantes):
    """Genera los satélites C6 con coordenadas"""
    print("\n🎯 Generando satélites C6...")
    
    satelites_c6 = []
    sin_coordenadas = []
    
    for idx, row in enumerate(faltantes, start=142):  # Continuar desde 142
        municipio_norm = normalizar_texto(row['MUNICIPIO'])
        depto_norm = normalizar_texto(row['DEPARTAMENTO'])
        clave = (municipio_norm, depto_norm)
        
        # Buscar coordenadas
        coords = COORDENADAS_MUNICIPIOS.get(clave)
        
        if coords:
            lat, lon = coords
        else:
            # Coordenada por defecto en centro de Colombia si no se encuentra
            lat, lon = 4.5709, -74.2973
            sin_coordenadas.append(f"{row['MUNICIPIO']} ({row['DEPARTAMENTO']})")
        
        satelite = {
            "centro_id": f"SAT_{idx:03d}",
            "tipo_centro": "SATELITE",
            "codigo_dane": "",
            "municipio": row['MUNICIPIO'],
            "departamento": row['DEPARTAMENTO'],
            "latitud": lat,
            "longitud": lon,
            "categoria_cale": "C6",
            "tipo_l3": "L3.SATELITE.c6",
            "tipo_nombre": "Satélite Categoría 6 (Pendiente de clasificación)",
            "color": "#FF6B6B",
            "demanda_estimada_anual": int(row['DEMANDA_PROYECTADA']) if pd.notna(row['DEMANDA_PROYECTADA']) else 0,
            "nodo_principal": "PENDIENTE",
            "codigo_dane_nodo": "",
            "total_municipios_cluster": 0,
            "distancia_al_nodo_km": 0,
            "distancia_maxima_cluster_km": 0,
            "observaciones": "Satélite C6 - Pendiente de asignación y configuración completa"
        }
        
        satelites_c6.append(satelite)
    
    print(f"✅ Generados {len(satelites_c6)} satélites C6")
    if sin_coordenadas:
        print(f"⚠️  {len(sin_coordenadas)} municipios usan coordenadas por defecto:")
        for m in sin_coordenadas[:5]:
            print(f"   - {m}")
        if len(sin_coordenadas) > 5:
            print(f"   ... y {len(sin_coordenadas) - 5} más")
    
    return satelites_c6

def guardar_json(satelites_c6):
    """Guarda los satélites C6 en JSON"""
    print(f"\n💾 Guardando JSON...")
    
    output = {
        "metadata": {
            "version": "2.0",
            "fecha": "2025-12-22",
            "descripcion": "Satélites C6 - Municipios faltantes del CSV 4-CALES-TEORICOS",
            "total_satelites_c6": len(satelites_c6)
        },
        "satelites_c6": satelites_c6
    }
    
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Archivo guardado: {OUTPUT_JSON_PATH}")
    
    # También actualizar el archivo principal agregando C6
    with open(SATELITES_JSON_PATH, 'r', encoding='utf-8') as f:
        data_principal = json.load(f)
    
    data_principal['satelites'].extend(satelites_c6)
    data_principal['metadata']['total_satelites'] = len(data_principal['satelites'])
    data_principal['metadata']['distribucion']['C6'] = len(satelites_c6)
    
    with open(SATELITES_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_principal, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Actualizado: {SATELITES_JSON_PATH}")

def main():
    print("="*70)
    print("🚀 GENERACIÓN DE SATÉLITES C6")
    print("="*70)
    
    faltantes = cargar_faltantes_csv()
    satelites_c6 = generar_satelites_c6(faltantes)
    guardar_json(satelites_c6)
    
    print("\n" + "="*70)
    print("✅ PROCESO COMPLETADO")
    print("="*70)
    print(f"📊 Total satélites C6 creados: {len(satelites_c6)}")
    print(f"📁 Archivos actualizados:")
    print(f"   - {OUTPUT_JSON_PATH}")
    print(f"   - {SATELITES_JSON_PATH}")
    print("\n🎯 Siguiente paso: Actualizar mapa-interactivo.js")

if __name__ == "__main__":
    main()
