#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para actualizar la demanda anual real de satélites C6 desde el CSV oficial
Versión sin pandas - solo usa módulos estándar de Python
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

def cargar_demandas_csv():
    """Carga las demandas del CSV oficial"""
    print("📂 Cargando CSV oficial...")
    
    demandas = {}
    
    try:
        with open(CSV_PATH, 'r', encoding='latin-1') as f:
            reader = csv.reader(f)
            
            for row in reader:
                try:
                    # Saltar filas vacías
                    if len(row) < 6:
                        continue
                    
                    # Las columnas son:
                    # 0: Número, 1: N, 2: DEPARTAMENTO, 3: MUNICIPIO, 4: TIPO, 5: DEMANDA
                    departamento = row[2] if len(row) > 2 else ""
                    municipio = row[3] if len(row) > 3 else ""
                    demanda_str = row[5] if len(row) > 5 else ""
                    
                    # Saltar encabezados
                    if 'DEPARTAMENTO' in municipio.upper() or 'COBERTURA' in municipio.upper():
                        continue
                    
                    # Saltar filas sin datos
                    if not municipio or not demanda_str:
                        continue
                    
                    municipio_norm = normalizar_texto(municipio)
                    
                    # Convertir demanda a entero (limpiar comas y puntos decimales)
                    demanda_clean = demanda_str.replace(',', '').replace('.', '').strip()
                    
                    if not demanda_clean or not demanda_clean.isdigit():
                        continue
                    
                    demanda_int = int(demanda_clean)
                    
                    if municipio_norm and demanda_int > 0:
                        demandas[municipio_norm] = demanda_int
                        
                except Exception as e:
                    continue
        
        print(f"✅ CSV cargado: {len(demandas)} municipios con demanda")
        
        # Mostrar algunos ejemplos
        print("\n📋 Ejemplos de demandas cargadas:")
        contador = 0
        for mun, dem in list(demandas.items())[:10]:
            print(f"   {mun:<30} → {dem:>8,}")
            contador += 1
        
        return demandas
        
    except Exception as e:
        print(f"❌ Error al cargar CSV: {e}")
        import traceback
        traceback.print_exc()
        return {}

def actualizar_demandas_c6():
    """Actualiza las demandas de los satélites C6 con valores reales del CSV"""
    print("=" * 70)
    print("📊 ACTUALIZANDO DEMANDAS REALES DE SATÉLITES C6")
    print("=" * 70)
    
    # Cargar demandas del CSV
    demandas_csv = cargar_demandas_csv()
    
    if not demandas_csv:
        print("❌ No se pudieron cargar demandas del CSV")
        return
    
    print("\n📂 Cargando satélites del JSON...")
    
    try:
        # Cargar JSON
        with open(SATELITES_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filtrar satélites C6
        satelites_c6 = [s for s in data['satelites'] if s.get('categoria_cale') == 'C6']
        print(f"🔍 Encontrados {len(satelites_c6)} satélites C6")
        
        print("\n🔄 Actualizando demandas...\n")
        
        actualizados = 0
        no_encontrados = []
        
        for satelite in data['satelites']:
            if satelite.get('categoria_cale') == 'C6':
                municipio = satelite['municipio']
                municipio_norm = normalizar_texto(municipio)
                
                # Buscar demanda en CSV
                if municipio_norm in demandas_csv:
                    demanda_anterior = satelite.get('demanda_estimada_anual', 0)
                    demanda_nueva = demandas_csv[municipio_norm]
                    satelite['demanda_estimada_anual'] = demanda_nueva
                    actualizados += 1
                    
                    print(f"✅ {satelite['centro_id']:<8} {municipio:<25} {demanda_anterior:>6,} → {demanda_nueva:>6,}")
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
        print("\n🎯 Recarga el mapa para ver las demandas reales")
        
        # Mostrar algunas estadísticas
        demandas_actualizadas = [s['demanda_estimada_anual'] for s in data['satelites'] if s.get('categoria_cale') == 'C6']
        if demandas_actualizadas:
            print(f"\n📈 Estadísticas de demanda C6:")
            print(f"   Mínima: {min(demandas_actualizadas):,}")
            print(f"   Máxima: {max(demandas_actualizadas):,}")
            print(f"   Promedio: {sum(demandas_actualizadas)//len(demandas_actualizadas):,}")
            print(f"   Total: {sum(demandas_actualizadas):,}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    actualizar_demandas_c6()
