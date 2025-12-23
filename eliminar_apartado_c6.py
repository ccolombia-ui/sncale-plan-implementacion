#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para eliminar el municipio APARTADO de la categoría C6
"""

import json
import unicodedata
from pathlib import Path

SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"

def normalizar_texto(texto):
    """Normaliza texto: mayúsculas, sin tildes"""
    if not texto:
        return ""
    texto = str(texto).upper().strip()
    # Remover tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def eliminar_apartado():
    """Elimina el municipio APARTADO de C6"""
    print("=" * 70)
    print("🗑️  ELIMINANDO APARTADO DE C6")
    print("=" * 70)
    
    try:
        # Cargar JSON
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        total_antes = len(data['satelites'])
        c6_antes = sum(1 for s in data['satelites'] if s.get('categoria_cale') == 'C6')
        
        print(f"\n📊 Estado actual:")
        print(f"   Total satélites: {total_antes}")
        print(f"   Satélites C6: {c6_antes}")
        
        print(f"\n🔍 Buscando APARTADO...\n")
        
        # Filtrar satélites, eliminando APARTADO
        satelites_filtrados = []
        eliminado = None
        
        for satelite in data['satelites']:
            municipio_norm = normalizar_texto(satelite.get('municipio', ''))
            
            # Si es C6 y es APARTADO, no agregarlo
            if satelite.get('categoria_cale') == 'C6' and municipio_norm == 'APARTADO':
                eliminado = {
                    'centro_id': satelite['centro_id'],
                    'municipio': satelite['municipio'],
                    'demanda': satelite.get('demanda_estimada_anual', 0)
                }
                print(f"❌ {satelite['centro_id']:<8} {satelite['municipio']:<25} ELIMINADO")
            else:
                satelites_filtrados.append(satelite)
        
        if not eliminado:
            print("⚠️  APARTADO no encontrado en C6")
            return
        
        # Actualizar datos
        data['satelites'] = satelites_filtrados
        
        # Actualizar metadata
        total_despues = len(satelites_filtrados)
        c6_despues = sum(1 for s in satelites_filtrados if s.get('categoria_cale') == 'C6')
        
        data['metadata']['total_satelites'] = total_despues
        data['metadata']['distribucion']['C6'] = c6_despues
        
        # Guardar JSON actualizado
        with open(SATELITES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 70)
        print("✅ ELIMINACIÓN COMPLETADA")
        print("=" * 70)
        print(f"\n📉 Cambios:")
        print(f"   Total satélites: {total_antes} → {total_despues} (-1)")
        print(f"   Satélites C6: {c6_antes} → {c6_despues} (-1)")
        
        print(f"\n🗑️  Municipio eliminado:")
        print(f"   {eliminado['centro_id']}: {eliminado['municipio']} (Demanda: {eliminado['demanda']:,})")
        
        print(f"\n💾 Archivo actualizado: satelites_completos_141_nodos.json")
        print("\n🎯 Recarga el mapa para ver los cambios")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    eliminar_apartado()
