"""
Extracción de Tablas L1 del Google Doc Oficial - Anexo B
=========================================================

Extrae las tablas #10, #12, #14 que contienen las definiciones
de ensamblajes L1 (Pista Clase I, II, III) desde el documento oficial:

Google Doc ID: 16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
Título: MUNAY_5.2__anexo_b__DEFINITIVO

Tablas objetivo:
- Tabla #10: Pista Clase I (17 filas - MANIOBRA_00 a MANIOBRA_13)
- Tabla #12: Pista Clase II (7 filas - MANIOBRA_14 a MANIOBRA_16)
- Tabla #14: Pista Clase III (8 filas - MANIOBRA_17 a MANIOBRA_19)

Salida: TABLAS_L1_OFICIALES.json
"""

import json
from pathlib import Path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Configuración
CREDENTIALS_FILE = r'C:\guezarel\.secret\credentials_google.json'
DOC_ID = '16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE'
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# Archivos de entrada/salida
CLASIFICACION_FILE = Path('INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json')
OUTPUT_FILE = Path('TABLAS_L1_OFICIALES.json')

def extraer_texto_celda(cell):
    """Extrae texto completo de una celda de tabla Google Docs"""
    texto = ''
    for content_elem in cell.get('content', []):
        if 'paragraph' in content_elem:
            for para_elem in content_elem['paragraph'].get('elements', []):
                if 'textRun' in para_elem:
                    texto += para_elem['textRun'].get('content', '')
    return texto.strip()

def procesar_tabla_l1(tabla_data, numero_tabla, nombre_nivel):
    """
    Procesa una tabla L1 y extrae componentes estructurados
    
    Args:
        tabla_data: Datos de la tabla desde INFORME_ANEXO_B_OFICIAL_RECLASIFICADO.json
        numero_tabla: Número de tabla (#10, #12, #14)
        nombre_nivel: 'pista_clase_I', 'pista_clase_II', 'pista_clase_III'
    
    Returns:
        dict con estructura L1 completa
    """
    encabezados = tabla_data.get('encabezados', [])
    todas_filas = tabla_data.get('todas_filas', [])
    
    # Estructura de salida
    resultado = {
        'nivel': nombre_nivel,
        'tabla_numero': numero_tabla,
        'elemento_index': tabla_data.get('elemento_index'),
        'dimensiones': {
            'filas': len(todas_filas),
            'columnas': len(encabezados)
        },
        'encabezados': encabezados,
        'componentes': []
    }
    
    # Procesar cada fila (excepto encabezado)
    for i, fila in enumerate(todas_filas[1:], start=1):  # Saltamos primera fila (encabezados)
        # Verificar que la fila tenga datos
        if not fila or len(fila) < 2:
            continue
        
        # Extraer datos de componente
        componente = {}
        
        for j, valor in enumerate(fila):
            if j < len(encabezados):
                header = encabezados[j].lower().strip()
                
                # Mapear encabezados a claves limpias
                if header == '#' or header == 'no.' or header == 'número':
                    componente['numero'] = valor.strip()
                elif 'componente' in header:
                    componente['componente'] = valor.strip()
                elif 'descripción' in header or 'descripcion' in header:
                    componente['descripcion'] = valor.strip()
                elif 'categoría' in header or 'categoria' in header:
                    componente['categoria'] = valor.strip()
                elif 'tipo' in header:
                    componente['tipo'] = valor.strip()
                elif 'referencia' in header:
                    componente['referencia'] = valor.strip()
                else:
                    # Guardar otros campos no reconocidos
                    componente[header] = valor.strip()
        
        # Solo agregar si tiene al menos componente o descripción
        if componente.get('componente') or componente.get('descripcion'):
            resultado['componentes'].append(componente)
    
    return resultado

def main():
    print("=" * 70)
    print("EXTRACCIÓN DE TABLAS L1 - GOOGLE DOC OFICIAL")
    print("=" * 70)
    print()
    
    # 1. Cargar clasificación previa
    print("📂 Cargando clasificación de tablas...")
    if not CLASIFICACION_FILE.exists():
        print(f"❌ ERROR: No se encuentra {CLASIFICACION_FILE}")
        print("   Ejecuta primero: python generar_informe_anexo_b.py")
        return
    
    with open(CLASIFICACION_FILE, 'r', encoding='utf-8') as f:
        informe = json.load(f)
    
    # Obtener lista de tablas L1
    tablas_l1_lista = informe.get('tablas_l1', [])
    
    print(f"✅ Cargadas {len(tablas_l1_lista)} tablas L1 del informe reclasificado")
    print()
    
    # 2. Identificar tablas L1 (#10, #12, #14)
    tablas_l1_objetivo = {
        10: 'pista_clase_I',
        12: 'pista_clase_II',
        14: 'pista_clase_III'
    }
    
    tablas_l1_encontradas = {}
    
    # Mapear las tablas L1 por número
    for tabla in tablas_l1_lista:
        num_tabla = tabla.get('numero')
        if num_tabla in tablas_l1_objetivo:
            tablas_l1_encontradas[num_tabla] = tabla
    
    print("🔍 Tablas L1 identificadas:")
    for num in sorted(tablas_l1_objetivo.keys()):
        nombre = tablas_l1_objetivo[num]
        if num in tablas_l1_encontradas:
            tabla = tablas_l1_encontradas[num]
            filas = tabla.get('filas', 0)
            cols = tabla.get('columnas', 0)
            print(f"   ✅ Tabla #{num}: {nombre} ({filas} filas × {cols} columnas)")
        else:
            print(f"   ❌ Tabla #{num}: {nombre} - NO ENCONTRADA")
    print()
    
    # 3. Procesar cada tabla L1
    print("⚙️  Procesando tablas L1...")
    print()
    
    resultado_final = {
        'fuente': {
            'documento': 'MUNAY_5.2__anexo_b__DEFINITIVO',
            'google_doc_id': DOC_ID,
            'url': f'https://docs.google.com/document/d/{DOC_ID}/edit',
            'fecha_extraccion': '2025-11-03'
        },
        'tablas_l1': {}
    }
    
    for num_tabla in sorted(tablas_l1_objetivo.keys()):
        if num_tabla not in tablas_l1_encontradas:
            print(f"⏭️  Tabla #{num_tabla}: OMITIDA (no encontrada)")
            continue
        
        nombre_nivel = tablas_l1_objetivo[num_tabla]
        tabla_data = tablas_l1_encontradas[num_tabla]
        
        print(f"📊 Procesando Tabla #{num_tabla}: {nombre_nivel}...")
        
        # Procesar tabla
        tabla_procesada = procesar_tabla_l1(tabla_data, num_tabla, nombre_nivel)
        
        # Guardar en resultado
        resultado_final['tablas_l1'][nombre_nivel] = tabla_procesada
        
        # Mostrar resumen
        num_componentes = len(tabla_procesada['componentes'])
        print(f"   ✅ Extraídos {num_componentes} componentes")
        
        # Mostrar primeros 3 componentes
        for i, comp in enumerate(tabla_procesada['componentes'][:3], start=1):
            comp_id = comp.get('componente', 'N/A')
            comp_desc = comp.get('descripcion', 'Sin descripción')
            print(f"      {i}. {comp_id}: {comp_desc[:60]}...")
        
        if num_componentes > 3:
            print(f"      ... y {num_componentes - 3} más")
        
        print()
    
    # 4. Guardar resultado
    print("💾 Guardando resultado...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(resultado_final, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Archivo generado: {OUTPUT_FILE}")
    print()
    
    # 5. Resumen final
    print("=" * 70)
    print("RESUMEN DE EXTRACCIÓN")
    print("=" * 70)
    print()
    
    total_componentes = sum(
        len(t['componentes']) 
        for t in resultado_final['tablas_l1'].values()
    )
    
    print(f"📊 Total tablas L1 procesadas: {len(resultado_final['tablas_l1'])}")
    print(f"📦 Total componentes extraídos: {total_componentes}")
    print()
    
    # Detalle por tabla
    for nombre_nivel, datos in resultado_final['tablas_l1'].items():
        num_componentes = len(datos['componentes'])
        num_tabla = datos['tabla_numero']
        print(f"   • {nombre_nivel} (Tabla #{num_tabla}): {num_componentes} componentes")
    
    print()
    print("=" * 70)
    print("✅ EXTRACCIÓN COMPLETADA")
    print("=" * 70)
    print()
    print(f"Archivo de salida: {OUTPUT_FILE.absolute()}")
    print()
    
    # 6. Validaciones
    print("🔍 VALIDACIONES:")
    print()
    
    # Verificar que todas las tablas tengan componentes
    tablas_vacias = [
        nombre for nombre, datos in resultado_final['tablas_l1'].items()
        if len(datos['componentes']) == 0
    ]
    
    if tablas_vacias:
        print(f"⚠️  ADVERTENCIA: {len(tablas_vacias)} tabla(s) sin componentes:")
        for nombre in tablas_vacias:
            print(f"   - {nombre}")
    else:
        print("✅ Todas las tablas contienen componentes")
    print()
    
    # Verificar estructura de componentes
    print("🔍 Verificando estructura de componentes...")
    campos_requeridos = ['componente', 'descripcion']
    componentes_incompletos = 0
    
    for nombre_nivel, datos in resultado_final['tablas_l1'].items():
        for comp in datos['componentes']:
            faltantes = [campo for campo in campos_requeridos if not comp.get(campo)]
            if faltantes:
                componentes_incompletos += 1
    
    if componentes_incompletos > 0:
        print(f"⚠️  {componentes_incompletos} componente(s) con campos faltantes")
    else:
        print("✅ Todos los componentes tienen campos requeridos")
    print()
    
    print("=" * 70)
    print("SIGUIENTE PASO:")
    print("Ejecutar: python validar_fichas_l1.py")
    print("   (Validará fichas L1 existentes contra estos datos oficiales)")
    print("=" * 70)

if __name__ == '__main__':
    main()
