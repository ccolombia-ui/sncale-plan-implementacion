#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INFORME COMPLETO - ANEXO B OFICIAL
Analiza las 89 tablas del Google Doc oficial y genera reporte detallado
para construcción de fichas L1, L2, L3
"""

import json

# Cargar análisis existente
with open('clasificacion_tablas_anexo_b.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("\n" + "="*80)
print("  INFORME ANEXO B OFICIAL - FUENTE ÚNICA DE VERDAD")
print("="*80)
print(f"\nDocumento: {data['titulo']}")
print(f"ID: {data['documento_id']}")
print(f"Total tablas: {data['total_tablas']}")

# Reclasificar manualmente basado en encabezados y contenido
tablas_l0 = []
tablas_l1 = []
tablas_l2_componentes = []
tablas_l3_valorizacion = []
tablas_l3_metadata = []

print("\n" + "="*80)
print("  ANÁLISIS DETALLADO POR TIPO DE TABLA")
print("="*80)

# Analizar todas las tablas
todas = []
for categoria, lista_tablas in data['tablas'].items():
    todas.extend(lista_tablas)

# Ordenar por número
todas_ordenadas = sorted(todas, key=lambda x: x['numero'])

# Clasificar correctamente
for tabla in todas_ordenadas:
    enc = ' '.join(tabla['encabezados']).lower()
    ejemplo = ' '.join([str(x) for x in tabla.get('ejemplo_fila2', [])]).lower()
    
    # Tablas L0 - Componentes Atómicos
    if 'bim_l0_' in ejemplo or 'bim_id' in enc:
        tablas_l0.append(tabla)
    
    # Tablas L1 - Componentes que forman L2
    elif ('#' in enc and 'componente' in enc and 'categoría' in enc and 
          ('maniobra' in ejemplo or 'l1.' in ejemplo)):
        tablas_l1.append(tabla)
    
    # Tablas L2 - Valorización de configuraciones
    elif 'concepto' in enc and 'valor (cop)' in enc and 'l2.' in ejemplo:
        tablas_l2_componentes.append(tabla)
    
    # Tablas L3 - Valorización CALE
    elif ('componente' in enc and 'vr. unitario' in enc and 'vr. total' in enc and
          ('pista' in ejemplo or 'cale' in ejemplo or 'l2.' in ejemplo)):
        tablas_l3_valorizacion.append(tabla)
    
    # Metadatos L3
    elif 'tipo cale' in enc and 'cantidad' in enc:
        tablas_l3_metadata.append(tabla)

# REPORTE
print("\n📊 TABLAS L0 - COMPONENTES ATÓMICOS")
print("-" * 80)
print(f"Total: {len(tablas_l0)} tablas")
print("\nEjemplos:")
for tabla in tablas_l0[:3]:
    print(f"\n  Tabla #{tabla['numero']}: {tabla['filas']} filas × {tabla['columnas']} cols")
    print(f"  Encabezados: {', '.join(tabla['encabezados'][:5])}...")
    if tabla.get('ejemplo_fila2'):
        print(f"  Ejemplo: {tabla['ejemplo_fila2'][0] if tabla['ejemplo_fila2'] else 'N/A'}")

print("\n\n📊 TABLAS L1 - ENSAMBLAJES (Componentes que forman L2)")
print("-" * 80)
print(f"Total: {len(tablas_l1)} tablas")
print("\nDetalle completo:")
for tabla in tablas_l1:
    print(f"\n  ✅ Tabla #{tabla['numero']}: {tabla['filas']} filas × {tabla['columnas']} cols")
    print(f"     Encabezados: {tabla['encabezados']}")
    if tabla.get('todas_filas') and len(tabla['todas_filas']) > 1:
        print(f"     Primer componente: {tabla['todas_filas'][1][:3] if len(tabla['todas_filas'][1]) >= 3 else tabla['todas_filas'][1]}")

print("\n\n📊 TABLAS L2 - CONFIGURACIONES BASE (Valorizaciones)")
print("-" * 80)
print(f"Total: {len(tablas_l2_componentes)} tablas")
print("\nDetalle completo:")
for tabla in tablas_l2_componentes:
    print(f"\n  ✅ Tabla #{tabla['numero']}: {tabla['filas']} filas × {tabla['columnas']} cols")
    print(f"     Encabezados: {tabla['encabezados']}")
    if tabla.get('todas_filas'):
        for fila in tabla['todas_filas'][1:]:
            print(f"     {fila}")

print("\n\n📊 TABLAS L3 - ESPECIALIZACIÓN CALE (Valorización componentes)")
print("-" * 80)
print(f"Total: {len(tablas_l3_valorizacion)} tablas")
print("\nDetalle completo:")
for tabla in tablas_l3_valorizacion[:5]:  # Primeras 5
    print(f"\n  ✅ Tabla #{tabla['numero']}: {tabla['filas']} filas × {tabla['columnas']} cols")
    print(f"     Encabezados: {tabla['encabezados']}")
    if tabla.get('ejemplo_fila2'):
        print(f"     Ejemplo: {tabla['ejemplo_fila2'][:3]}")

print("\n\n📊 TABLAS L3 - METADATOS (Geolocalización y configuración)")
print("-" * 80)
print(f"Total: {len(tablas_l3_metadata)} tablas")
for tabla in tablas_l3_metadata:
    print(f"\n  Tabla #{tabla['numero']}: {tabla['encabezados']}")

# CONCLUSIONES
print("\n\n" + "="*80)
print("  RESUMEN Y PLAN DE ACCIÓN")
print("="*80)

print(f"""
📌 ESTADO ACTUAL:
   • {len(tablas_l0)} tablas L0 (Componentes Atómicos) ✅ COMPLETO
   • {len(tablas_l1)} tablas L1 (Ensamblajes para L2) ⚠️ REQUIERE ANÁLISIS
   • {len(tablas_l2_componentes)} tablas L2 (Valorizaciones) ✅ IDENTIFICADAS
   • {len(tablas_l3_valorizacion)} tablas L3 (Valorización CALE) ✅ IDENTIFICADAS
   • {len(tablas_l3_metadata)} tablas L3 (Metadatos) ✅ IDENTIFICADAS

📋 PLAN DE ACCIÓN:

1. NIVEL L1 - ENSAMBLAJES:
   Analizar {len(tablas_l1)} tablas que definen componentes L1
   Tablas clave: #{', #'.join([str(t['numero']) for t in tablas_l1])}
   Acción: Extraer definiciones de cada ensamblaje L1

2. NIVEL L2 - CONFIGURACIONES BASE:
   Usar {len(tablas_l2_componentes)} tablas de valorización
   Tablas clave: #{', #'.join([str(t['numero']) for t in tablas_l2_componentes])}
   Acción: Crear fichas L2 con valores oficiales

3. NIVEL L3 - ESPECIALIZACIÓN CALE:
   Usar {len(tablas_l3_valorizacion)} tablas de componentes + {len(tablas_l3_metadata)} de metadatos
   Acción: Generar fichas L3 para CALE.n_1, n_2, n_3

🎯 SIGUIENTE PASO INMEDIATO:
   Extraer y analizar tablas L1 (#{', #'.join([str(t['numero']) for t in tablas_l1][:5])})
   para identificar qué ensamblajes existen y sus componentes L0
""")

# Guardar reclasificación
resultado_final = {
    'documento': data['titulo'],
    'fecha_analisis': '2025-11-03',
    'fuente_verdad': 'https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
    'clasificacion': {
        'L0': len(tablas_l0),
        'L1': len(tablas_l1),
        'L2': len(tablas_l2_componentes),
        'L3_valorizacion': len(tablas_l3_valorizacion),
        'L3_metadata': len(tablas_l3_metadata)
    },
    'tablas_l1': tablas_l1,
    'tablas_l2': tablas_l2_componentes,
    'tablas_l3_valorizacion': tablas_l3_valorizacion,
    'tablas_l3_metadata': tablas_l3_metadata
}

with open('INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json', 'w', encoding='utf-8') as f:
    json.dump(resultado_final, f, indent=2, ensure_ascii=False)

print(f"\n💾 Informe guardado: INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json")
print("\n" + "="*80)
