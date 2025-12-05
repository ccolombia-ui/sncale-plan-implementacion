#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracción CORRECTA de jerarquía BIM L3 → L2 → L1 → L0
Basado en la estructura real del Google Doc

CORRECCIÓN CRÍTICA:
- Las MANIOBRA_XX NO son componentes BIM L1
- Son especificaciones geométricas/funcionales dentro de componentes L0
- Los verdaderos L1 son: pista_motos_A1A2_completa, pista_carros_B1C1_completa, etc.
- Los L0 son: pavimentos, drenajes, señalización, etc.

Fuente: Google Doc MUNAY_5.2__anexo_b__DEFINITIVO
Doc ID: 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
"""

import json
import re

def limpiar_valor_cop(valor_str):
    """Extrae valor numérico de string COP"""
    if not valor_str or valor_str == '-' or valor_str == '':
        return 0
    # Eliminar $, puntos y comas
    valor_limpio = valor_str.replace('$', '').replace('.', '').replace(',', '').strip()
    try:
        return int(valor_limpio)
    except ValueError:
        return 0

def main():
    print("="*80)
    print("EXTRACCIÓN CORRECTA DE JERARQUÍA BIM")
    print("="*80)
    print()
    
    # Cargar clasificación de tablas
    print("📂 Cargando clasificación de tablas...")
    with open('clasificacion_tablas_anexo_b.json', 'r', encoding='utf-8') as f:
        clasificacion = json.load(f)
    
    tablas_l2 = clasificacion['tablas']['L2 - Configuración Base']
    tablas_l0 = clasificacion['tablas'].get('L0 - Componentes Atómicos', [])
    
    print(f"✅ Encontradas {len(tablas_l2)} tablas L2")
    print()
    
    # Estructura de datos correcta
    jerarquia = {
        'fuente': {
            'documento': 'MUNAY_5.2__anexo_b__DEFINITIVO',
            'doc_id': '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE',
            'fecha_extraccion': '2025-11-03'
        },
        'estructura_correcta': {
            'L3': 'Configuraciones CALE (n_1, n_2, n_3, satélites)',
            'L2': 'Pistas completas (Clase I, II, III) y edificaciones',
            'L1': 'Componentes de infraestructura (pista_motos, pista_carros, pista_camiones, etc.)',
            'L0': 'Componentes atómicos (pavimentos, drenajes, señalización, mobiliario, etc.)'
        },
        'niveles': {
            'L0': [],
            'L1': [],
            'L2': [],
            'L3': []
        }
    }
    
    # Buscar tablas específicas con componentes L1
    print("🔍 Buscando tablas con componentes L1 reales...")
    print()
    
    componentes_l1_por_pista = {
        'pista_clase_I': [],
        'pista_clase_II': [],
        'pista_clase_III': []
    }
    
    # Buscar tabla 19 (componentes L1 de pista_clase_I)
    for tabla in tablas_l2:
        num_tabla = tabla['numero']
        
        # Tabla 19: COMPONENTES L1 DE PISTA CLASE I
        if num_tabla == 19:
            print(f"📊 Tabla #{num_tabla}: Componentes L1 de Pista Clase I")
            filas = tabla['todas_filas']
            
            for i, fila in enumerate(filas[1:], start=1):  # Saltar encabezado
                if len(fila) >= 5:
                    componente = fila[0].strip()
                    descripcion = fila[1].strip()
                    cantidad = fila[2].strip()
                    unidad = fila[3].strip()
                    codigo_l1 = fila[4].strip()
                    subtotal = fila[5].strip() if len(fila) > 5 else '$0'
                    
                    # Ignorar filas de subtotal
                    if 'SUBTOTAL' in codigo_l1:
                        continue
                    
                    if codigo_l1 and codigo_l1.startswith('L1.'):
                        valor = limpiar_valor_cop(subtotal)
                        
                        comp_l1 = {
                            'numero': i,
                            'componente': componente,
                            'descripcion': descripcion,
                            'cantidad': cantidad,
                            'unidad': unidad,
                            'codigo_l1': codigo_l1,
                            'valor_cop': valor,
                            'fuente': f'Tabla #{num_tabla}, Fila {i+1}',
                            'componentes_l0': []  # Se llenará después
                        }
                        
                        componentes_l1_por_pista['pista_clase_I'].append(comp_l1)
                        
                        print(f"   ✅ {codigo_l1}: {componente} - ${subtotal}")
            print()
        
        # Tabla 20: COMPONENTES L1 DE PISTA CLASE II
        elif num_tabla == 20:
            print(f"📊 Tabla #{num_tabla}: Componentes L1 de Pista Clase II")
            filas = tabla['todas_filas']
            
            for i, fila in enumerate(filas[1:], start=1):
                if len(fila) >= 5:
                    componente = fila[0].strip()
                    codigo_l1 = fila[4].strip()
                    
                    if 'SUBTOTAL' in codigo_l1:
                        continue
                    
                    if codigo_l1 and codigo_l1.startswith('L1.'):
                        valor = limpiar_valor_cop(fila[5] if len(fila) > 5 else '$0')
                        
                        comp_l1 = {
                            'numero': i,
                            'componente': componente,
                            'descripcion': fila[1].strip(),
                            'cantidad': fila[2].strip(),
                            'unidad': fila[3].strip(),
                            'codigo_l1': codigo_l1,
                            'valor_cop': valor,
                            'fuente': f'Tabla #{num_tabla}, Fila {i+1}',
                            'componentes_l0': []
                        }
                        
                        componentes_l1_por_pista['pista_clase_II'].append(comp_l1)
                        print(f"   ✅ {codigo_l1}: {componente}")
            print()
        
        # Tabla 21: COMPONENTES L1 DE PISTA CLASE III
        elif num_tabla == 21:
            print(f"📊 Tabla #{num_tabla}: Componentes L1 de Pista Clase III")
            filas = tabla['todas_filas']
            
            for i, fila in enumerate(filas[1:], start=1):
                if len(fila) >= 5:
                    componente = fila[0].strip()
                    codigo_l1 = fila[4].strip()
                    
                    if 'SUBTOTAL' in codigo_l1:
                        continue
                    
                    if codigo_l1 and codigo_l1.startswith('L1.'):
                        valor = limpiar_valor_cop(fila[5] if len(fila) > 5 else '$0')
                        
                        comp_l1 = {
                            'numero': i,
                            'componente': componente,
                            'descripcion': fila[1].strip(),
                            'cantidad': fila[2].strip(),
                            'unidad': fila[3].strip(),
                            'codigo_l1': codigo_l1,
                            'valor_cop': valor,
                            'fuente': f'Tabla #{num_tabla}, Fila {i+1}',
                            'componentes_l0': []
                        }
                        
                        componentes_l1_por_pista['pista_clase_III'].append(comp_l1)
                        print(f"   ✅ {codigo_l1}: {componente}")
            print()
    
    # Buscar componentes L0
    print("🔍 Buscando componentes L0...")
    print()
    
    componentes_l0 = []
    
    # Buscar en tablas con encabezado "Componente L0" o "Código L0"
    for tabla in tablas_l2:
        encabezados = tabla.get('encabezados', [])
        
        # Buscar tablas con estructura L0
        if 'Código' in encabezados and 'Componente' in encabezados:
            num_tabla = tabla['numero']
            filas = tabla.get('todas_filas', [])
            
            for i, fila in enumerate(filas[1:], start=1):
                if len(fila) >= 3:
                    # Buscar columna con códigos L0.
                    for j, celda in enumerate(fila):
                        if isinstance(celda, str) and celda.startswith('L0.'):
                            codigo_l0 = celda.strip()
                            
                            # Extraer información
                            bim_id = fila[0] if len(fila) > 0 else ''
                            componente = fila[2] if len(fila) > 2 else ''
                            descripcion = fila[3] if len(fila) > 3 else ''
                            unidad = fila[4] if len(fila) > 4 else ''
                            usado_en = fila[-1] if len(fila) > 9 else ''
                            
                            comp_l0 = {
                                'bim_id': bim_id.strip(),
                                'codigo_l0': codigo_l0,
                                'componente': componente.strip(),
                                'descripcion': descripcion.strip(),
                                'unidad': unidad.strip(),
                                'usado_en': usado_en.strip(),
                                'fuente': f'Tabla #{num_tabla}, Fila {i+1}'
                            }
                            
                            componentes_l0.append(comp_l0)
                            print(f"   ⚙️ {codigo_l0}: {componente}")
                            break
    
    print()
    print(f"✅ Total componentes L0 encontrados: {len(componentes_l0)}")
    print()
    
    # Asociar L0 con L1
    print("🔗 Asociando componentes L0 con L1...")
    print()
    
    for pista, componentes_l1 in componentes_l1_por_pista.items():
        for comp_l1 in componentes_l1:
            codigo_l1 = comp_l1['codigo_l1']
            
            # Buscar L0 que mencionan este L1
            for comp_l0 in componentes_l0:
                usado_en = comp_l0['usado_en']
                if codigo_l1 in usado_en or pista in usado_en:
                    comp_l1['componentes_l0'].append(comp_l0)
    
    # Resumen
    print("="*80)
    print("RESUMEN DE EXTRACCIÓN")
    print("="*80)
    print()
    print(f"📊 Componentes L1 por pista:")
    print(f"   - Pista Clase I: {len(componentes_l1_por_pista['pista_clase_I'])} componentes")
    print(f"   - Pista Clase II: {len(componentes_l1_por_pista['pista_clase_II'])} componentes")
    print(f"   - Pista Clase III: {len(componentes_l1_por_pista['pista_clase_III'])} componentes")
    print()
    print(f"⚙️ Total componentes L0: {len(componentes_l0)}")
    print()
    
    # Guardar resultado
    jerarquia['niveles']['L1'] = componentes_l1_por_pista
    jerarquia['niveles']['L0'] = componentes_l0
    
    output_file = 'JERARQUIA_BIM_CORRECTA.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(jerarquia, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Archivo generado: {output_file}")
    print()
    print("✅ Extracción completada")
    print()

if __name__ == '__main__':
    main()
