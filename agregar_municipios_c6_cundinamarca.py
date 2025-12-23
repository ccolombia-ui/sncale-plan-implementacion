#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para agregar 14 municipios adicionales de Cundinamarca a la categoría C6
"""

import json
from pathlib import Path

# Coordenadas de los 14 municipios de Cundinamarca
NUEVOS_MUNICIPIOS_C6 = {
    "CHIA": {"lat": 4.8607, "lon": -74.0582, "departamento": "CUNDINAMARCA"},
    "FUNZA": {"lat": 4.7161, "lon": -74.2089, "departamento": "CUNDINAMARCA"},
    "FUSAGASUGA": {"lat": 4.3378, "lon": -74.3636, "departamento": "CUNDINAMARCA"},
    "UBATE": {"lat": 5.3119, "lon": -73.8197, "departamento": "CUNDINAMARCA"},
    "CAJICA": {"lat": 4.9186, "lon": -74.0275, "departamento": "CUNDINAMARCA"},
    "FACATATIVA": {"lat": 4.8144, "lon": -74.3547, "departamento": "CUNDINAMARCA"},
    "SOPO": {"lat": 4.9089, "lon": -73.9447, "departamento": "CUNDINAMARCA"},
    "MADRID": {"lat": 4.7314, "lon": -74.2636, "departamento": "CUNDINAMARCA"},
    "LA CALERA": {"lat": 4.7222, "lon": -73.9689, "departamento": "CUNDINAMARCA"},
    "CAQUEZA": {"lat": 4.4078, "lon": -73.9508, "departamento": "CUNDINAMARCA"},
    "PACHO": {"lat": 5.1328, "lon": -74.1589, "departamento": "CUNDINAMARCA"},
    "SIBATE": {"lat": 4.4908, "lon": -74.2597, "departamento": "CUNDINAMARCA"},
    "SILVANIA": {"lat": 4.4019, "lon": -74.3886, "departamento": "CUNDINAMARCA"},
    "CHOCONTA": {"lat": 5.1467, "lon": -73.6858, "departamento": "CUNDINAMARCA"}
}

SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"

def agregar_municipios_c6():
    """Agrega los 14 municipios de Cundinamarca a la categoría C6"""
    print("=" * 70)
    print("📍 AGREGANDO 14 MUNICIPIOS DE CUNDINAMARCA A C6")
    print("=" * 70)
    
    try:
        # Cargar datos existentes
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        satelites_antes = len(data['satelites'])
        print(f"\n📊 Satélites actuales: {satelites_antes}")
        
        # Obtener el último centro_id para continuar la secuencia
        ultimo_centro_id = max([s['centro_id'] for s in data['satelites']], key=lambda x: int(x.split('_')[1]))
        ultimo_numero = int(ultimo_centro_id.split('_')[1])
        print(f"🔢 Último centro_id: {ultimo_centro_id}")
        
        # Agregar los 14 nuevos municipios
        contador = 0
        for municipio, coords in NUEVOS_MUNICIPIOS_C6.items():
            ultimo_numero += 1
            nuevo_satelite = {
                "centro_id": f"SAT_{str(ultimo_numero).zfill(3)}",
                "municipio": municipio.title(),
                "departamento": coords["departamento"],
                "latitud": coords["lat"],
                "longitud": coords["lon"],
                "categoria_cale": "C6",
                "color": "#FF6B6B",
                "demanda_estimada_anual": 1200
            }
            data['satelites'].append(nuevo_satelite)
            contador += 1
            print(f"✅ {contador:2d}. {nuevo_satelite['centro_id']} - {municipio.title():<20} ({coords['lat']}, {coords['lon']})")
        
        # Actualizar metadata
        satelites_despues = len(data['satelites'])
        
        # Actualizar distribución de C6
        distribucion_actual = data['metadata']['distribucion']
        c6_antes = distribucion_actual.get('C6', 0)
        distribucion_actual['C6'] = c6_antes + 14
        
        data['metadata']['total_satelites'] = satelites_despues
        data['metadata']['distribucion'] = distribucion_actual
        
        # Guardar archivo actualizado
        with open(SATELITES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 70)
        print("✅ ACTUALIZACIÓN COMPLETADA")
        print("=" * 70)
        print(f"📊 Satélites totales: {satelites_antes} → {satelites_despues} (+{contador})")
        print(f"📍 Satélites C6: {c6_antes} → {distribucion_actual['C6']} (+14)")
        print(f"\n💾 Archivo actualizado: satelites_completos_141_nodos.json")
        print("\n🎯 Recarga el mapa para ver los 14 nuevos puntos en Cundinamarca")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    agregar_municipios_c6()
