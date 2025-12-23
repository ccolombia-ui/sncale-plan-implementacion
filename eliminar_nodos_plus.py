#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para eliminar nodos PLUS (Metropolitano Plus y Subregional Plus)
de los archivos JSON del proyecto
"""

import json
from pathlib import Path

# Rutas de archivos
SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"
RELACIONES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\relaciones_jerarquicas_completas.json"
NODOS_COMPLETOS_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\nodos_completos_mapa.json"

def limpiar_satelites_json():
    """Elimina satélites PLUS del archivo satelites_completos_141_nodos.json"""
    print("\n🧹 Limpiando satelites_completos_141_nodos.json...")
    
    try:
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        satelites_originales = len(data['satelites'])
        
        # Filtrar satélites que NO sean PLUS
        # Buscamos por tipo_l3 o por nombres que contengan "PLUS"
        data['satelites'] = [
            s for s in data['satelites']
            if 'n_1_plus' not in s.get('tipo_l3', '').lower() and
               'n_2_plus' not in s.get('tipo_l3', '').lower() and
               'plus' not in s.get('municipio', '').upper()
        ]
        
        satelites_limpiados = len(data['satelites'])
        eliminados = satelites_originales - satelites_limpiados
        
        # Actualizar metadata
        if 'metadata' in data:
            data['metadata']['total_satelites'] = satelites_limpiados
        
        # Guardar
        with open(SATELITES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Eliminados {eliminados} satélites PLUS")
        print(f"   Original: {satelites_originales} → Final: {satelites_limpiados}")
        
        return eliminados
    except FileNotFoundError:
        print("⚠️  Archivo no encontrado")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 0

def limpiar_relaciones_json():
    """Elimina relaciones de nodos PLUS del archivo relaciones_jerarquicas_completas.json"""
    print("\n🧹 Limpiando relaciones_jerarquicas_completas.json...")
    
    try:
        with open(RELACIONES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        nodos_originales = len(data['relaciones'])
        eliminados = 0
        
        # Lista de nodos a eliminar
        nodos_a_eliminar = []
        
        # Buscar nodos PLUS
        for nodo_id, relacion in data['relaciones'].items():
            info = relacion.get('info', {})
            nombre = info.get('nombre', '')
            
            # Si el nombre contiene "PLUS", marcarlo para eliminar
            if 'PLUS' in nombre.upper():
                nodos_a_eliminar.append(nodo_id)
        
        # Eliminar nodos marcados
        for nodo_id in nodos_a_eliminar:
            del data['relaciones'][nodo_id]
            eliminados += 1
            print(f"   ❌ Eliminado: {nodo_id}")
        
        # Actualizar metadata
        if 'metadata' in data:
            data['metadata']['total_nodos_principales'] = len(data['relaciones'])
            data['metadata']['nodos_con_satelites'] = sum(
                1 for r in data['relaciones'].values() if len(r.get('subnodos', [])) > 0
            )
            data['metadata']['nodos_sin_satelites'] = len(data['relaciones']) - data['metadata']['nodos_con_satelites']
        
        # Guardar
        with open(RELACIONES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Eliminados {eliminados} nodos PLUS de relaciones")
        print(f"   Original: {nodos_originales} → Final: {len(data['relaciones'])}")
        
        return eliminados
    except FileNotFoundError:
        print("⚠️  Archivo no encontrado")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 0

def limpiar_nodos_completos_json():
    """Elimina nodos PLUS del archivo nodos_completos_mapa.json"""
    print("\n🧹 Limpiando nodos_completos_mapa.json...")
    
    try:
        with open(NODOS_COMPLETOS_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'nodos' not in data:
            print("⚠️  No se encontró la clave 'nodos'")
            return 0
        
        nodos_originales = len(data['nodos'])
        eliminados = 0
        
        # Lista de nodos a eliminar
        nodos_a_eliminar = []
        
        # Buscar nodos PLUS
        for nodo_id, nodo in data['nodos'].items():
            tipo_id = nodo.get('tipo_id', '')
            nombre = nodo.get('nombre', '')
            
            # Si el tipo_id contiene "plus" o el nombre contiene "PLUS"
            if 'plus' in tipo_id.lower() or 'PLUS' in nombre.upper():
                nodos_a_eliminar.append(nodo_id)
        
        # Eliminar nodos marcados
        for nodo_id in nodos_a_eliminar:
            del data['nodos'][nodo_id]
            eliminados += 1
            print(f"   ❌ Eliminado: {nodo_id}")
        
        # Guardar
        with open(NODOS_COMPLETOS_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Eliminados {eliminados} nodos PLUS")
        print(f"   Original: {nodos_originales} → Final: {len(data['nodos'])}")
        
        return eliminados
    except FileNotFoundError:
        print("⚠️  Archivo no encontrado")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 0

def main():
    print("=" * 70)
    print("🗑️  ELIMINACIÓN DE NODOS PLUS")
    print("=" * 70)
    print("\nEliminando nodos CALE Metropolitano Plus y CALE Subregional Plus...")
    
    total_eliminados = 0
    
    # Limpiar cada archivo
    total_eliminados += limpiar_satelites_json()
    total_eliminados += limpiar_relaciones_json()
    total_eliminados += limpiar_nodos_completos_json()
    
    print("\n" + "=" * 70)
    print("✅ PROCESO COMPLETADO")
    print("=" * 70)
    print(f"📊 Total nodos/satélites eliminados: {total_eliminados}")
    print("\n🎯 Ahora recarga el mapa para ver los cambios")
    print("   Los puntos azules y naranjas deberían haber desaparecido")

if __name__ == "__main__":
    main()
