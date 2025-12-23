#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para actualizar la demanda anual real de satélites C6 desde el CSV oficial
"""

import json
import pandas as pd
import unicodedata
from pathlib import Path

CSV_PATH = r"C:\Users\USER\Downloads\4-CALES-TEORICOS.csv"
SATELITES_JSON = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"

def normalizar_texto(texto):
    """Normaliza texto para comparación: mayúsculas, sin tildes, sin espacios extra"""
    if pd.isna(texto):
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
    
    try:
        # Leer CSV
        df = pd.read_csv(CSV_PATH, encoding='latin-1')
        
        # Encontrar las columnas correctas
        # El CSV tiene columnas sin nombre al inicio, buscar las columnas de datos
        columnas = df.columns.tolist()
        
        # Buscar índices de columnas relevantes
        col_departamento = None
        col_municipio = None
        col_demanda = None
        
        for i, col in enumerate(columnas):
            col_norm = str(col).upper()
            if 'DEPARTAMENTO' in col_norm:
                col_departamento = i
            elif 'MUNICIPIO' in col_norm:
                col_municipio = i
            elif 'DEMANDA EXPEDICION' in col_norm or 'DEMANDA PROYECTADA' in col_norm:
                col_demanda = i
        
        if col_departamento is None or col_municipio is None or col_demanda is None:
            # Si no encuentra por nombre, usar índices fijos del CSV
            col_departamento = 2
            col_municipio = 3
            col_demanda = 5  # DEMANDA EXPEDICION + RECATEGORIZACION
        
        demandas = {}
        
        # Procesar cada fila
        for idx, row in df.iterrows():
            try:
                departamento = row.iloc[col_departamento]
                municipio = row.iloc[col_municipio]
                demanda = row.iloc[col_demanda]
                
                # Saltar filas vacías o de encabezado
                if pd.isna(municipio) or pd.isna(demanda):
                    continue
                
                # Saltar filas que no son datos
                if 'COBERTURA' in str(municipio).upper() or 'DEMANDA' in str(municipio).upper():
                    continue
                
                municipio_norm = normalizar_texto(municipio)
                
                # Convertir demanda a entero (puede tener comas o puntos)
                demanda_str = str(demanda).replace(',', '').replace('.', '')
                try:
                    demanda_int = int(float(demanda_str))
                except:
                    continue
                
                if municipio_norm and demanda_int > 0:
                    demandas[municipio_norm] = demanda_int
                    
            except Exception as e:
                continue
        
        print(f"✅ CSV cargado: {len(demandas)} municipios con demanda")
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
                    
                    print(f"✅ {satelite['centro_id']:<8} {municipio:<25} {demanda_anterior:>6} → {demanda_nueva:>6}")
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
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    actualizar_demandas_c6()
