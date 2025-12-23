#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar qué satélites del CSV 4-CALES-TEORICOS.csv
ya existen en el proyecto y cuáles faltan.
"""

import pandas as pd
import json
from pathlib import Path
from collections import defaultdict

# Rutas de archivos
CSV_PATH = r"C:\Users\USER\Downloads\4-CALES-TEORICOS.csv"
SATELITES_JSON_PATH = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\data\satelites_completos_141_nodos.json"
OUTPUT_PATH = r"C:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\REPORTE_SATELITES_FALTANTES.md"

def normalizar_texto(texto):
    """Normaliza texto para comparación (mayúsculas, sin tildes, sin espacios extra)"""
    if pd.isna(texto):
        return ""
    texto = str(texto).upper().strip()
    # Remover tildes
    reemplazos = {
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'Ñ': 'N', 'Ü': 'U'
    }
    for old, new in reemplazos.items():
        texto = texto.replace(old, new)
    return texto

def cargar_satelites_csv():
    """Carga los satélites del CSV"""
    print("📄 Cargando CSV...")
    
    # Leer CSV con encoding adecuado, skip las primeras 2 filas de headers
    df = pd.read_csv(CSV_PATH, encoding='latin-1', skiprows=2)
    
    # Renombrar columnas según estructura
    df.columns = ['GRUPO', 'N', 'DEPARTAMENTO', 'MUNICIPIO', 'TIPO_CALE', 'DEMANDA_EXPEDICION', 
                  'DEMANDA_PROYECTADA', 'NUM_AULAS', 'MOD_AULA', 'CICLOS_DIA', 'DIAS_OPERACION',
                  'CAPACIDAD_AULA_DIA', 'CAPACIDAD_AULA_ANO', 'OFERTA_REEVALUACION', 
                  'OFERTA_CONTINGENCIA', 'CAPACIDAD_ADICIONAL', 'PORCENTAJE']
    
    # Filtrar solo satélites
    df_satelites = df[df['TIPO_CALE'] == 'SATELITE'].copy()
    
    # Normalizar nombres
    df_satelites['MUNICIPIO_NORM'] = df_satelites['MUNICIPIO'].apply(normalizar_texto)
    df_satelites['DEPARTAMENTO_NORM'] = df_satelites['DEPARTAMENTO'].apply(normalizar_texto)
    
    print(f"✅ Encontrados {len(df_satelites)} satélites en CSV")
    
    return df_satelites

def cargar_satelites_proyecto():
    """Carga los satélites que ya existen en el proyecto"""
    print("\n📦 Cargando satélites del proyecto...")
    
    with open(SATELITES_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    satelites = []
    for sat in data['satelites']:
        satelites.append({
            'id': sat['centro_id'],
            'municipio': sat['municipio'],
            'departamento': sat['departamento'],
            'categoria': sat['categoria_cale'],
            'municipio_norm': normalizar_texto(sat['municipio']),
            'departamento_norm': normalizar_texto(sat['departamento'])
        })
    
    print(f"✅ Encontrados {len(satelites)} satélites en proyecto")
    print(f"   - C2: {len([s for s in satelites if s['categoria'] == 'C2'])}")
    print(f"   - C3: {len([s for s in satelites if s['categoria'] == 'C3'])}")
    print(f"   - C4: {len([s for s in satelites if s['categoria'] == 'C4'])}")
    print(f"   - C5: {len([s for s in satelites if s['categoria'] == 'C5'])}")
    
    return satelites

def comparar_satelites(df_csv, satelites_proyecto):
    """Compara los satélites del CSV con los del proyecto"""
    print("\n🔍 Comparando satélites...\n")
    
    # Crear set de tuplas (municipio, departamento) del proyecto
    existentes = {
        (s['municipio_norm'], s['departamento_norm']): s 
        for s in satelites_proyecto
    }
    
    encontrados = []
    faltantes = []
    
    for idx, row in df_csv.iterrows():
        municipio = row['MUNICIPIO_NORM']
        departamento = row['DEPARTAMENTO_NORM']
        clave = (municipio, departamento)
        
        if clave in existentes:
            encontrados.append({
                'municipio': row['MUNICIPIO'],
                'departamento': row['DEPARTAMENTO'],
                'categoria_proyecto': existentes[clave]['categoria'],
                'id_proyecto': existentes[clave]['id'],
                'demanda_csv': row.get('DEMANDA_PROYECTADA', 'N/A')
            })
        else:
            faltantes.append({
                'municipio': row['MUNICIPIO'],
                'departamento': row['DEPARTAMENTO'],
                'demanda_csv': row.get('DEMANDA_PROYECTADA', 'N/A'),
                'aulas_csv': row.get('NUM_AULAS', 'N/A')
            })
    
    return encontrados, faltantes

def generar_reporte(encontrados, faltantes, df_csv, satelites_proyecto):
    """Genera un reporte en Markdown"""
    print("\n📝 Generando reporte...\n")
    
    reporte = []
    reporte.append("# 📊 REPORTE DE VERIFICACIÓN DE SATÉLITES")
    reporte.append("## Sistema Nacional CALE - Escenario 2\n")
    reporte.append(f"**Fecha:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    reporte.append("---\n")
    
    # Resumen
    reporte.append("## 📈 RESUMEN EJECUTIVO\n")
    reporte.append(f"- **Total satélites en CSV:** {len(df_csv)}")
    reporte.append(f"- **Total satélites en proyecto:** {len(satelites_proyecto)}")
    reporte.append(f"- **Satélites encontrados (coinciden):** {len(encontrados)} ✅")
    reporte.append(f"- **Satélites faltantes:** {len(faltantes)} ❌\n")
    
    if len(encontrados) > 0:
        porcentaje = (len(encontrados) / len(df_csv)) * 100
        reporte.append(f"**Cobertura actual:** {porcentaje:.1f}%\n")
    
    reporte.append("---\n")
    
    # Distribución por categoría en proyecto
    reporte.append("## 🏷️ DISTRIBUCIÓN POR CATEGORÍA (PROYECTO ACTUAL)\n")
    categorias = defaultdict(int)
    for s in satelites_proyecto:
        categorias[s['categoria']] += 1
    
    for cat in sorted(categorias.keys()):
        reporte.append(f"- **{cat}:** {categorias[cat]} satélites")
    reporte.append("\n---\n")
    
    # Satélites encontrados
    reporte.append("## ✅ SATÉLITES ENCONTRADOS (YA EN PROYECTO)\n")
    reporte.append(f"Total: {len(encontrados)} municipios\n")
    
    if encontrados:
        # Agrupar por departamento
        por_depto = defaultdict(list)
        for item in encontrados:
            por_depto[item['departamento']].append(item)
        
        for depto in sorted(por_depto.keys()):
            reporte.append(f"\n### {depto} ({len(por_depto[depto])})\n")
            reporte.append("| Municipio | Categoría | ID Proyecto | Demanda Anual |")
            reporte.append("|-----------|-----------|-------------|---------------|")
            for item in sorted(por_depto[depto], key=lambda x: x['municipio']):
                reporte.append(f"| {item['municipio']} | {item['categoria_proyecto']} | {item['id_proyecto']} | {item['demanda_csv']} |")
    else:
        reporte.append("*No se encontraron coincidencias*\n")
    
    reporte.append("\n---\n")
    
    # Satélites faltantes
    reporte.append("## ❌ SATÉLITES FALTANTES (NO IMPLEMENTADOS)\n")
    reporte.append(f"Total: {len(faltantes)} municipios\n")
    
    if faltantes:
        # Agrupar por departamento
        por_depto = defaultdict(list)
        for item in faltantes:
            por_depto[item['departamento']].append(item)
        
        for depto in sorted(por_depto.keys()):
            reporte.append(f"\n### {depto} ({len(por_depto[depto])})\n")
            reporte.append("| Municipio | Demanda Anual | Aulas CSV |")
            reporte.append("|-----------|---------------|-----------|")
            for item in sorted(por_depto[depto], key=lambda x: x['municipio']):
                reporte.append(f"| {item['municipio']} | {item['demanda_csv']} | {item['aulas_csv']} |")
    else:
        reporte.append("*¡Todos los satélites del CSV están implementados!* 🎉\n")
    
    reporte.append("\n---\n")
    
    # Próximos pasos
    reporte.append("## 📋 PRÓXIMOS PASOS\n")
    if faltantes:
        reporte.append("1. Revisar los satélites faltantes listados arriba")
        reporte.append("2. Decidir cuáles son prioritarios según demanda")
        reporte.append("3. Asignar categorías (C2/C3/C4/C5) a cada uno")
        reporte.append("4. Obtener coordenadas geográficas (lat/lon)")
        reporte.append("5. Asignar a un nodo principal existente")
        reporte.append("6. Agregar al archivo `satelites_completos_141_nodos.json`")
        reporte.append("7. Actualizar `relaciones_jerarquicas_completas.json`\n")
    else:
        reporte.append("✅ El proyecto está completo según el CSV de referencia.\n")
    
    reporte.append("---\n")
    reporte.append("\n*Reporte generado automáticamente por `verificar_satelites.py`*\n")
    
    # Guardar reporte
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(reporte))
    
    print(f"✅ Reporte guardado en: {OUTPUT_PATH}")
    
    return '\n'.join(reporte)

def main():
    print("=" * 70)
    print("🔍 VERIFICACIÓN DE SATÉLITES - SNCALE")
    print("=" * 70)
    
    # Cargar datos
    df_csv = cargar_satelites_csv()
    satelites_proyecto = cargar_satelites_proyecto()
    
    # Comparar
    encontrados, faltantes = comparar_satelites(df_csv, satelites_proyecto)
    
    # Generar reporte
    reporte = generar_reporte(encontrados, faltantes, df_csv, satelites_proyecto)
    
    # Mostrar resumen en consola
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    print(f"✅ Encontrados: {len(encontrados)}")
    print(f"❌ Faltantes:   {len(faltantes)}")
    print(f"📁 Total CSV:   {len(df_csv)}")
    print(f"🗂️  Total Proyecto: {len(satelites_proyecto)}")
    print("=" * 70)
    
    if faltantes:
        print(f"\n⚠️  Hay {len(faltantes)} satélites que NO están en el proyecto.")
        print(f"📄 Ver detalles en: {OUTPUT_PATH}")
    else:
        print("\n🎉 ¡Todos los satélites del CSV están implementados!")

if __name__ == "__main__":
    main()
