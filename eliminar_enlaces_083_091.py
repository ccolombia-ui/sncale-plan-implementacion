# -*- coding: utf-8 -*-
"""
Script para eliminar enlaces BIM_L0_083 a BIM_L0_091 de archivos BIM_L0_001 a BIM_L0_081
"""
import os
import re

base_path = r"c:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\sncale-plan-implementacion\fichas"

# Patrón que captura desde BIM_L0_083 hasta BIM_L0_091
# Usamos un patrón que capture todo el bloque incluyendo los 9 enlaces
patron = r'\s*<a href="BIM_L0_083\.html".*?083: Paquete certificaciones ISO\s*</a>\s*<a href="BIM_L0_084\.html".*?084: Pasillos interiores edificación\s*</a>\s*<a href="BIM_L0_085\.html".*?085: Circulaciones exteriores\s*</a>\s*<a href="BIM_L0_086\.html".*?086: Rampa acceso universal\s*</a>\s*<a href="BIM_L0_087\.html".*?087: Escalera principal\s*</a>\s*<a href="BIM_L0_088\.html".*?088: Escalera emergencia\s*</a>\s*<a href="BIM_L0_089\.html".*?089: Pasamanos rampa/escalera\s*</a>\s*<a href="BIM_L0_090\.html".*?090: Piso podotáctil direccional\s*</a>\s*<a href="BIM_L0_091\.html".*?091: Señalización inclusiva braille\s*</a>\s*'

archivos_modificados = 0
archivos_error = 0
archivos_sin_cambio = 0

# Procesar archivos del 001 al 081
for i in range(1, 82):
    numero = f"{i:03d}"
    archivo = os.path.join(base_path, f"BIM_L0_{numero}.html")
    
    if os.path.exists(archivo):
        try:
            print(f"Procesando: BIM_L0_{numero}.html", end=" ... ")
            
            # Leer contenido
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Buscar y reemplazar
            nuevo_contenido = re.sub(patron, '', contenido, flags=re.DOTALL)
            
            # Verificar si hubo cambios
            if contenido != nuevo_contenido:
                # Guardar archivo
                with open(archivo, 'w', encoding='utf-8', newline='') as f:
                    f.write(nuevo_contenido)
                
                print("[OK] Modificado")
                archivos_modificados += 1
            else:
                print("[--] Sin cambios")
                archivos_sin_cambio += 1
                
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            archivos_error += 1
    else:
        print(f"  [!] Archivo no encontrado: BIM_L0_{numero}.html")

print("\n" + "="*50)
print("RESUMEN:")
print("="*50)
print(f"Archivos modificados: {archivos_modificados}")
print(f"Archivos sin cambios: {archivos_sin_cambio}")
print(f"Archivos con error: {archivos_error}")
print("="*50)
