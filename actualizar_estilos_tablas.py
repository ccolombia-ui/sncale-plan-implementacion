#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para cambiar el fondo de las tablas en todas las fichas BIM_L0
Cambio: background de th de negro (#333) a azul claro (#e8f4f8)
"""

import os
import re
from pathlib import Path

# Ruta de la carpeta de fichas
FICHAS_DIR = Path(__file__).parent / "fichas"

# Patrón antiguo (color: #000)
OLD_PATTERN_1 = r'''        th {
            background: var\(--primary-color\);
            color: #000;
            font-weight: 600;
        }'''

# Patrón antiguo (color: white)
OLD_PATTERN_2 = r'''        th {
            background: var\(--primary-color\);
            color: white;
            font-weight: 600;
        }'''

# Patrón nuevo
NEW_PATTERN = '''        th {
            background: #e8f4f8;
            color: var(--primary-color);
            font-weight: 600;
        }'''


def actualizar_ficha(filepath):
    """Actualiza el estilo de tabla en una ficha"""
    print(f"Actualizando: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Intentar reemplazar primer patrón
    nuevo_contenido = re.sub(OLD_PATTERN_1, NEW_PATTERN, content)
    
    # Si no cambió, intentar con el segundo patrón
    if nuevo_contenido == content:
        nuevo_contenido = re.sub(OLD_PATTERN_2, NEW_PATTERN, content)
    
    # Verificar si se hizo algún cambio
    if nuevo_contenido == content:
        print(f"  ⚠️  No se encontró el patrón en {filepath.name}")
        return False
    
    # Guardar archivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    
    print(f"  ✓ Completado: {filepath.name}")
    return True


def main():
    """Función principal"""
    print("=" * 70)
    print("ACTUALIZACIÓN DE ESTILOS DE TABLA EN FICHAS BIM")
    print("Cambiando fondo de encabezados de tabla de negro a azul claro")
    print("=" * 70)
    
    # Obtener todos los archivos BIM_L0_*.html
    fichas = sorted(FICHAS_DIR.glob("BIM_L0_*.html"))
    
    print(f"\nSe encontraron {len(fichas)} fichas para actualizar\n")
    
    actualizadas = 0
    no_encontradas = 0
    
    # Actualizar cada ficha
    for i, ficha in enumerate(fichas, 1):
        try:
            print(f"[{i}/{len(fichas)}] ", end="")
            if actualizar_ficha(ficha):
                actualizadas += 1
            else:
                no_encontradas += 1
        except Exception as e:
            print(f"  ✗ ERROR en {ficha.name}: {str(e)}")
    
    print("\n" + "=" * 70)
    print(f"ACTUALIZACIÓN COMPLETADA:")
    print(f"  ✓ Actualizadas: {actualizadas}")
    print(f"  ⚠️  Sin cambios: {no_encontradas}")
    print("=" * 70)


if __name__ == "__main__":
    main()
