#!/usr/bin/env python3
"""Script simple para extraer y listar contenido del ZIP"""

import zipfile
import os

zip_path = r"c:\proyectos\sncale-plan-implementacion-main\Plan-Implementacion.zip"
extract_path = r"c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main\temp-nueva-version"

print("Iniciando extracción...")
print(f"ZIP: {zip_path}")
print(f"Destino: {extract_path}")

# Verificar ZIP
if not os.path.exists(zip_path):
    print(f"ERROR: ZIP no encontrado")
    exit(1)

# Extraer
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Listar contenido primero
    print("\nContenido del ZIP:")
    for name in zip_ref.namelist()[:50]:  # Primeros 50
        print(f"  {name}")
    
    # Extraer todo
    zip_ref.extractall(extract_path)

print("\n✓ Extracción completada")
