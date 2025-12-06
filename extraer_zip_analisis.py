import zipfile
import os
import json

# Rutas
zip_path = r"c:\proyectos\sncale-plan-implementacion-main\Plan-Implementacion.zip"
extract_path = r"c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main\temp-nueva-version"

# Verificar que el ZIP existe
if not os.path.exists(zip_path):
    print(f"ERROR: No se encuentra el archivo ZIP en: {zip_path}")
    exit(1)

print(f"✓ ZIP encontrado: {zip_path}")
print(f"✓ Extrayendo a: {extract_path}")

# Extraer el ZIP
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"✓ Extracción completada")
except Exception as e:
    print(f"ERROR al extraer: {e}")
    exit(1)

# Analizar estructura
def analizar_directorio(path, nivel=0, max_nivel=4):
    """Analiza recursivamente la estructura de directorios"""
    estructura = {}
    
    if nivel > max_nivel:
        return {"...": "truncado"}
    
    try:
        items = os.listdir(path)
        for item in sorted(items):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                estructura[item + "/"] = analizar_directorio(item_path, nivel + 1, max_nivel)
            else:
                # Obtener tamaño y extensión
                size = os.path.getsize(item_path)
                ext = os.path.splitext(item)[1]
                estructura[item] = {
                    "size": size,
                    "ext": ext
                }
    except Exception as e:
        estructura["ERROR"] = str(e)
    
    return estructura

print("\n" + "="*60)
print("ANALIZANDO ESTRUCTURA DEL ZIP EXTRAÍDO")
print("="*60)

estructura = analizar_directorio(extract_path)

# Guardar análisis en JSON
output_json = r"c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main\analisis_nueva_version.json"
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(estructura, f, indent=2, ensure_ascii=False)

print(f"\n✓ Análisis guardado en: {output_json}")

# Imprimir estructura resumida
def print_estructura(est, nivel=0, max_items=20):
    """Imprime la estructura de forma legible"""
    count = 0
    for key, value in est.items():
        if count >= max_items:
            print("  " * nivel + "... (más archivos)")
            break
        
        if isinstance(value, dict):
            if "size" in value and "ext" in value:
                # Es un archivo
                size_mb = value["size"] / (1024 * 1024)
                print(f"{'  ' * nivel}📄 {key} ({size_mb:.2f} MB)")
            else:
                # Es un directorio
                print(f"{'  ' * nivel}📁 {key}")
                print_estructura(value, nivel + 1, max_items)
        count += 1

print("\nESTRUCTURA DE ARCHIVOS:")
print_estructura(estructura)

# Contar tipos de archivos
def contar_archivos(est):
    """Cuenta archivos por extensión"""
    conteo = {}
    
    for key, value in est.items():
        if isinstance(value, dict):
            if "ext" in value:
                ext = value["ext"] if value["ext"] else "(sin extensión)"
                conteo[ext] = conteo.get(ext, 0) + 1
            else:
                # Recursión para subdirectorios
                sub_conteo = contar_archivos(value)
                for ext, count in sub_conteo.items():
                    conteo[ext] = conteo.get(ext, 0) + count
    
    return conteo

conteo = contar_archivos(estructura)
print("\n" + "="*60)
print("CONTEO DE ARCHIVOS POR TIPO:")
print("="*60)
for ext, count in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
    print(f"{ext:20} : {count:4} archivos")

print("\n✓ Análisis completado")
