"""
Script para mapear nodo_principal de nombre de municipio a centro_id
Convierte valores como "BOGOTÁ, D.C." a "NODO_01"

Autor: Generado para Proyecto MUNAY
Fecha: 2025-10-29
"""

import pandas as pd
import os

# Rutas de archivos
CSV_ENTRADA = r'c:\raziel\ia_formulacion\MUNAY_5.3__ESCENARIO_2_PRESUPUESTO_141__LISTADO_TODOS_CENTROS.csv'
CSV_SALIDA = r'c:\raziel\ia_formulacion\arquitectura_red_cale_nacional_MAPEADO.csv'

def limpiar_texto(texto):
    """Limpia espacios y normaliza texto"""
    if pd.isna(texto):
        return ""
    return str(texto).strip().upper()

def main():
    print("=" * 80)
    print("SCRIPT: Mapeo de nodo_principal (municipio -> centro_id)")
    print("=" * 80)
    print()

    # 1. Leer CSV de entrada
    print(f"[*] Leyendo CSV: {CSV_ENTRADA}")
    df = pd.read_csv(CSV_ENTRADA)
    print(f"[OK] Leido: {len(df)} filas, {len(df.columns)} columnas")
    print()

    # 2. Identificar nodos principales (tipo_centro == 'NODO_PRINCIPAL')
    print("[*] Identificando nodos principales...")
    nodos_principales = df[df['tipo_centro'] == 'NODO_PRINCIPAL'].copy()
    print(f"[OK] Encontrados: {len(nodos_principales)} nodos principales")
    print()

    # 3. Crear diccionario: municipio -> centro_id
    print("[*] Creando diccionario de mapeo:")
    mapa_municipio_a_centro = {}

    for _, row in nodos_principales.iterrows():
        municipio = limpiar_texto(row['municipio'])
        centro_id = limpiar_texto(row['centro_id'])

        if municipio and centro_id:
            mapa_municipio_a_centro[municipio] = centro_id
            print(f"   {municipio:30s} -> {centro_id}")

    print()
    print(f"[OK] Diccionario creado: {len(mapa_municipio_a_centro)} municipios mapeados")
    print()

    # 4. Función para mapear nodo_principal
    def mapear_nodo(nodo_actual):
        """Convierte nombre de municipio a centro_id"""
        if pd.isna(nodo_actual):
            return nodo_actual

        nodo_limpio = limpiar_texto(nodo_actual)

        # Si ya es un centro_id (formato NODO_XX o SAT_XX), no cambiar
        if nodo_limpio.startswith('NODO_') or nodo_limpio.startswith('SAT_'):
            return nodo_actual

        # Buscar en el diccionario
        if nodo_limpio in mapa_municipio_a_centro:
            return mapa_municipio_a_centro[nodo_limpio]

        # Si no se encuentra, buscar parcialmente (ej: "BOGOTÁ, D.C." vs "BOGOTÁ")
        for municipio, centro_id in mapa_municipio_a_centro.items():
            if municipio in nodo_limpio or nodo_limpio in municipio:
                return centro_id

        # Si no se encuentra, mantener original pero avisar
        print(f"[WARNING] No se encontro mapeo para '{nodo_actual}'")
        return nodo_actual

    # 5. Aplicar mapeo
    print("[*] Aplicando mapeo a columna 'nodo_principal'...")
    df_mapeado = df.copy()
    df_mapeado['nodo_principal'] = df['nodo_principal'].apply(mapear_nodo)
    print("[OK] Mapeo completado")
    print()

    # 6. Verificar cambios
    print("[*] Verificacion de cambios:")
    cambios = df[df['nodo_principal'] != df_mapeado['nodo_principal']]
    print(f"   Total de filas modificadas: {len(cambios)}")

    if len(cambios) > 0:
        print("\n   Ejemplos de cambios realizados:")
        for i, (idx, row) in enumerate(cambios.head(5).iterrows()):
            original = df.loc[idx, 'nodo_principal']
            nuevo = df_mapeado.loc[idx, 'nodo_principal']
            print(f"      {row['centro_id']:15s} | {original:30s} -> {nuevo}")

    print()

    # 7. Guardar CSV corregido
    print(f"[*] Guardando CSV corregido: {CSV_SALIDA}")
    df_mapeado.to_csv(CSV_SALIDA, index=False, encoding='utf-8-sig')
    print("[OK] Archivo guardado exitosamente")
    print()

    # 8. Resumen final
    print("=" * 80)
    print("RESUMEN FINAL")
    print("=" * 80)
    print(f"[*] Archivo entrada:  {CSV_ENTRADA}")
    print(f"[*] Archivo salida:   {CSV_SALIDA}")
    print(f"[*] Total filas:      {len(df_mapeado)}")
    print(f"[*] Filas modificadas: {len(cambios)}")
    print(f"[*] Nodos mapeados:   {len(mapa_municipio_a_centro)}")
    print()
    print("[OK] PROCESO COMPLETADO")
    print()
    print("SIGUIENTE PASO:")
    print("  1. Revisar el archivo: arquitectura_red_cale_nacional_MAPEADO.csv")
    print("  2. Importar a Google Sheets (arquitectura_red_cale_nacional)")
    print("  3. Publicar como CSV público")
    print("  4. Actualizar HTML con URL pública")
    print("=" * 80)

if __name__ == "__main__":
    main()
