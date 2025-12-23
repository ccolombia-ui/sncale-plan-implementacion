#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para actualizar cubículos de satélites C6 desde MOD POR AULA del CSV
"""

import json
import csv
import unicodedata
from pathlib import Path

CSV_PATH = r"C:\Users\USER\Downloads\4-CALES-TEORICOS.csv"
SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"

def normalizar_texto(texto):
    """Normaliza texto para comparación: mayúsculas, sin tildes, sin espacios extra"""
    if not texto or texto.strip() == '':
        return ""
    texto = str(texto).upper().strip()
    # Remover tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def cargar_cubiculos_csv():
    """Carga MOD POR AULA del CSV oficial"""
    print("📂 Cargando cubículos (MOD POR AULA) del CSV...")
    
    cubiculos = {}
    
    try:
        with open(CSV_PATH, 'r', encoding='latin-1') as f:
            reader = csv.reader(f)
            
            for row in reader:
                try:
                    # Saltar filas vacías
                    if len(row) < 8:
                        continue
                    
                    # Las columnas son:
                    # 0: Número, 1: N, 2: DEPARTAMENTO, 3: MUNICIPIO, 4: TIPO, 
                    # 5: DEMANDA, 6: DEMANDA PROYECTADA, 7: NO. AULAS, 8: MOD POR AULA
                    municipio = row[3] if len(row) > 3 else ""
                    mod_aula_str = row[7] if len(row) > 7 else ""
                    
                    # Saltar encabezados
                    if 'DEPARTAMENTO' in municipio.upper() or 'COBERTURA' in municipio.upper():
                        continue
                    
                    # Saltar filas sin datos
                    if not municipio or not mod_aula_str:
                        continue
                    
                    municipio_norm = normalizar_texto(municipio)
                    
                    # Convertir MOD POR AULA a entero
                    mod_clean = mod_aula_str.replace(',', '').replace('.', '').strip()
                    
                    if not mod_clean or not mod_clean.isdigit():
                        continue
                    
                    mod_int = int(mod_clean)
                    
                    if municipio_norm and mod_int > 0:
                        cubiculos[municipio_norm] = mod_int
                        
                except Exception as e:
                    continue
        
        print(f"✅ CSV cargado: {len(cubiculos)} municipios con MOD POR AULA")
        
        # Mostrar algunos ejemplos
        print("\n📋 Ejemplos de MOD POR AULA cargados:")
        contador = 0
        for mun, cub in list(cubiculos.items())[:15]:
            print(f"   {mun:<30} → {cub:>3} cubículos")
            contador += 1
        
        return cubiculos
        
    except Exception as e:
        print(f"❌ Error al cargar CSV: {e}")
        import traceback
        traceback.print_exc()
        return {}

def actualizar_cubiculos_c6():
    """Actualiza los cubículos de los satélites C6 con valores reales del CSV"""
    print("=" * 70)
    print("🏗️  ACTUALIZANDO CUBÍCULOS DE SATÉLITES C6")
    print("=" * 70)
    
    # Cargar cubículos del CSV
    cubiculos_csv = cargar_cubiculos_csv()
    
    if not cubiculos_csv:
        print("❌ No se pudieron cargar cubículos del CSV")
        return
    
    print("\n📂 Cargando satélites del JSON...")
    
    try:
        # Cargar JSON
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filtrar satélites C6
        satelites_c6 = [s for s in data['satelites'] if s.get('categoria_cale') == 'C6']
        print(f"🔍 Encontrados {len(satelites_c6)} satélites C6")
        
        print("\n🔄 Actualizando cubículos...\n")
        
        actualizados = 0
        no_encontrados = []
        
        for satelite in data['satelites']:
            if satelite.get('categoria_cale') == 'C6':
                municipio = satelite['municipio']
                municipio_norm = normalizar_texto(municipio)
                
                # Buscar cubículos en CSV
                if municipio_norm in cubiculos_csv:
                    cubiculos_anterior = satelite.get('cubiculos', 0)
                    cubiculos_nuevo = cubiculos_csv[municipio_norm]
                    satelite['cubiculos'] = cubiculos_nuevo
                    actualizados += 1
                    
                    print(f"✅ {satelite['centro_id']:<8} {municipio:<25} {cubiculos_anterior:>3} → {cubiculos_nuevo:>3} cubículos")
                else:
                    no_encontrados.append(municipio)
                    print(f"⚠️  {satelite['centro_id']:<8} {municipio:<25} NO ENCONTRADO en CSV")
        
        # Guardar JSON actualizado
        with open(SATELITES_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 70)
        print("✅ ACTUALIZACIÓN COMPLETADA")
        print("=" * 70)
        print(f"📊 Satélites C6 actualizados: {actualizados}/{len(satelites_c6)}")
        
        if no_encontrados:
            print(f"\n⚠️  Municipios no encontrados en CSV ({len(no_encontrados)}):")
            for mun in no_encontrados:
                print(f"   - {mun}")
        
        print(f"\n💾 Archivo guardado: satelites_completos_141_nodos.json")
        print("\n🎯 Recarga el mapa para ver los cubículos reales")
        
        # Mostrar algunas estadísticas
        cubiculos_actualizados = [s['cubiculos'] for s in data['satelites'] if s.get('categoria_cale') == 'C6' and 'cubiculos' in s]
        if cubiculos_actualizados:
            print(f"\n📈 Estadísticas de cubículos C6:")
            print(f"   Mínimo: {min(cubiculos_actualizados)}")
            print(f"   Máximo: {max(cubiculos_actualizados)}")
            
            # Contar distribución
            from collections import Counter
            distribucion = Counter(cubiculos_actualizados)
            print(f"\n📊 Distribución de cubículos:")
            for cub, count in sorted(distribucion.items()):
                print(f"   {cub} cubículos: {count} municipios")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    actualizar_cubiculos_c6()
