import zipfile
import os
import sys

zip_path = r"c:\proyectos\sncale-plan-implementacion-main\Plan-Implementacion.zip"

# Solo listar contenido sin extraer
try:
    print("Analizando ZIP:", zip_path)
    print("="*60)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files = zip_ref.namelist()
        
        print(f"Total de archivos: {len(files)}")
        print("\nPrimeros 100 archivos:")
        print("-"*60)
        
        for i, name in enumerate(files[:100], 1):
            info = zip_ref.getinfo(name)
            size_mb = info.file_size / (1024 * 1024)
            print(f"{i:3}. {name:60} ({size_mb:.2f} MB)")
        
        if len(files) > 100:
            print(f"\n... y {len(files) - 100} archivos más")
        
        # Contar por extensión
        print("\n" + "="*60)
        print("CONTEO POR EXTENSION:")
        print("="*60)
        
        ext_count = {}
        for name in files:
            if name.endswith('/'):
                ext = "CARPETA"
            else:
                ext = os.path.splitext(name)[1] or "(sin ext)"
            ext_count[ext] = ext_count.get(ext, 0) + 1
        
        for ext, count in sorted(ext_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{ext:20} : {count:5} archivos")
        
        # Estructura de carpetas raíz
        print("\n" + "="*60)
        print("ESTRUCTURA RAIZ:")
        print("="*60)
        
        root_items = set()
        for name in files:
            parts = name.split('/')
            if len(parts) > 0:
                root_items.add(parts[0] + ("/" if len(parts) > 1 or name.endswith('/') else ""))
        
        for item in sorted(root_items):
            print(f"  {item}")
        
except FileNotFoundError:
    print(f"ERROR: No se encuentra el archivo: {zip_path}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
