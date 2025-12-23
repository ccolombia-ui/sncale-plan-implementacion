#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para convertir a MAYÚSCULAS los nombres de los 14 municipios de Cundinamarca
"""

import json
from pathlib import Path

SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"

def convertir_a_mayusculas():
    """Convierte los nombres de los 14 nuevos municipios a MAYÚSCULAS"""
    print("=" * 70)
    print("🔠 CONVIRTIENDO MUNICIPIOS DE CUNDINAMARCA A MAYÚSCULAS")
    print("=" * 70)
    
    try:
        # Cargar datos
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # IDs de los 14 nuevos municipios
        ids_nuevos = [f"SAT_{i:03d}" for i in range(251, 265)]
        
        print(f"\n📝 Convirtiendo nombres de municipios...\n")
        
        contador = 0
        for satelite in data['satelites']:
            if satelite['centro_id'] in ids_nuevos:
                nombre_antes = satelite['municipio']
                nombre_despues = satelite['municipio'].upper()
                satelite['municipio'] = nombre_despues
                contador += 1
                print(f"✅ {satelite['centro_id']}: {nombre_antes:<20} → {nombre_despues}")
        
        # Guardar cambios
        with open(SATELITES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 70)
        print("✅ CONVERSIÓN COMPLETADA")
        print("=" * 70)
        print(f"📊 Municipios actualizados: {contador}")
        print(f"💾 Archivo guardado: satelites_completos_141_nodos.json")
        print("\n🎯 Recarga el mapa para ver los nombres en MAYÚSCULAS")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    convertir_a_mayusculas()
