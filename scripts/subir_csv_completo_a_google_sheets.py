"""
Script para subir el CSV completo a Google Sheets
Reemplaza TODO el contenido del worksheet con el CSV
"""

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración
SPREADSHEET_ID = '1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU'
WORKSHEET_NAME = 'arquitectura_red_cale_nacional'
CSV_FILE = 'arquitectura_red_cale_nacional_MAPEADO.csv'

def main():
    print("=" * 80)
    print("SUBIR CSV COMPLETO A GOOGLE SHEETS")
    print("=" * 80)
    print()

    # 1. Conectar a Google Sheets
    print("[*] Conectando a Google Sheets API...")
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('.config/credentials_google.json', scope)
    client = gspread.authorize(creds)
    print("[OK] Autenticado con Google Sheets API")
    print()

    # 2. Leer CSV
    print(f"[*] Leyendo CSV: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE)
    print(f"[OK] CSV leido: {len(df)} filas, {len(df.columns)} columnas")
    print(f"    Columnas: {list(df.columns)}")
    print()

    # 3. Abrir worksheet
    print(f"[*] Abriendo Google Sheet: {SPREADSHEET_ID}")
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
    print(f"[OK] Hoja abierta: {WORKSHEET_NAME}")
    print()

    # 4. Convertir DataFrame a lista de listas
    print("[*] Preparando datos...")
    # Headers
    data = [df.columns.tolist()]
    # Rows
    for index, row in df.iterrows():
        data.append(row.tolist())

    print(f"[OK] Datos preparados: {len(data)} filas (incluyendo header)")
    print()

    # 5. Limpiar worksheet y subir datos
    print("[*] Limpiando worksheet actual...")
    worksheet.clear()
    print("[OK] Worksheet limpiado")
    print()

    print("[*] Subiendo datos completos...")
    worksheet.update(values=data, range_name='A1', value_input_option='RAW')
    print("[OK] Datos subidos exitosamente!")
    print()

    # 6. Formatear columnas de coordenadas con más decimales
    print("[*] Formateando columnas latitud/longitud con 6 decimales...")
    try:
        # Encontrar índice de columnas lat/lon
        headers = df.columns.tolist()
        lat_col_idx = headers.index('latitud') if 'latitud' in headers else None
        lon_col_idx = headers.index('longitud') if 'longitud' in headers else None

        if lat_col_idx is not None and lon_col_idx is not None:
            # Convertir a letra de columna (A=0, B=1, etc.)
            lat_col_letter = chr(65 + lat_col_idx)
            lon_col_letter = chr(65 + lon_col_idx)

            # Formatear rango completo de cada columna
            worksheet.format(f'{lat_col_letter}2:{lat_col_letter}', {"numberFormat": {"type": "NUMBER", "pattern": "0.000000"}})
            worksheet.format(f'{lon_col_letter}2:{lon_col_letter}', {"numberFormat": {"type": "NUMBER", "pattern": "0.000000"}})
            print(f"[OK] Formateadas columnas {lat_col_letter} (latitud) y {lon_col_letter} (longitud)")
        else:
            print("[WARN] No se encontraron columnas latitud/longitud")
    except Exception as e:
        print(f"[WARN] No se pudo formatear coordenadas: {e}")
    print()

    # 7. Verificar
    print("Verificacion:")
    print("-" * 60)
    print(f"  Total filas en Google Sheets: {worksheet.row_count}")
    print(f"  Total columnas en Google Sheets: {worksheet.col_count}")
    print(f"  Header: {worksheet.row_values(1)[:5]}...")
    print(f"  Primera fila de datos: {worksheet.row_values(2)[:5]}...")
    print("-" * 60)
    print()

    print("=" * 80)
    print("[OK] SUBIDA COMPLETADA EXITOSAMENTE")
    print("=" * 80)
    print()
    print("SIGUIENTE PASO:")
    print(f"1. Verificar Google Sheets: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")
    print("2. Publicar hoja como TSV (File -> Share -> Publish to web)")
    print(f"   - Hoja: {WORKSHEET_NAME}")
    print("   - Formato: TSV")
    print("3. Copiar URL TSV y actualizar mapa_cale_nacional.html")

if __name__ == '__main__':
    main()
