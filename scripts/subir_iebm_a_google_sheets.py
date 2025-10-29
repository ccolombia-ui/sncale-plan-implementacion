"""
Script para subir tabla de IEBM a Google Sheets
Crea una nueva pestaña llamada 'iebm_educacion_media'
"""

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración
SPREADSHEET_ID = '1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU'
WORKSHEET_NAME = 'iebm_educacion_media'
CSV_FILE = 'iebm_con_cale_asignado.csv'

def main():
    print("=" * 80)
    print("SUBIR IEBM A GOOGLE SHEETS")
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

    # 2. Abrir spreadsheet
    print(f"[*] Abriendo Spreadsheet: {SPREADSHEET_ID}")
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    print(f"[OK] Spreadsheet abierto: {spreadsheet.title}")
    print()

    # 3. Verificar si la hoja existe
    try:
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        print(f"[*] Hoja '{WORKSHEET_NAME}' ya existe. Eliminando...")
        spreadsheet.del_worksheet(worksheet)
        print("[OK] Hoja eliminada")
    except:
        print(f"[*] Hoja '{WORKSHEET_NAME}' no existe (se creara nueva)")

    # 4. Crear nueva hoja
    print(f"[*] Creando hoja '{WORKSHEET_NAME}'...")
    worksheet = spreadsheet.add_worksheet(title=WORKSHEET_NAME, rows=20000, cols=20)
    print("[OK] Hoja creada")
    print()

    # 5. Leer CSV
    print(f"[*] Leyendo CSV: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE)
    print(f"[OK] CSV leido: {len(df)} filas, {len(df.columns)} columnas")
    print()

    # 6. Preparar datos
    print("[*] Preparando datos...")
    # Reemplazar NaN con cadenas vacías
    df = df.fillna('')

    # Headers
    data = [df.columns.tolist()]
    # Rows
    for index, row in df.iterrows():
        data.append(row.tolist())

    print(f"[OK] Datos preparados: {len(data)} filas (incluyendo header)")
    print()

    # 7. Subir datos
    print("[*] Subiendo datos a Google Sheets...")
    worksheet.update(values=data, range_name='A1', value_input_option='RAW')
    print("[OK] Datos subidos exitosamente!")
    print()

    # 8. Formatear
    print("[*] Formateando hoja...")

    # Header en negrita
    worksheet.format('A1:P1', {
        "textFormat": {"bold": True},
        "backgroundColor": {"red": 0.4, "green": 0.5, "blue": 0.9}
    })

    # Congelar primera fila
    worksheet.freeze(rows=1)

    # Formatear columnas de coordenadas
    lat_col_idx = df.columns.tolist().index('latitud')
    lon_col_idx = df.columns.tolist().index('longitud')
    lat_col_letter = chr(65 + lat_col_idx)
    lon_col_letter = chr(65 + lon_col_idx)

    worksheet.format(f'{lat_col_letter}2:{lat_col_letter}', {"numberFormat": {"type": "NUMBER", "pattern": "0.000000"}})
    worksheet.format(f'{lon_col_letter}2:{lon_col_letter}', {"numberFormat": {"type": "NUMBER", "pattern": "0.000000"}})

    print("[OK] Formato aplicado")
    print()

    # 9. Estadísticas
    print("=" * 80)
    print("SUBIDA COMPLETADA EXITOSAMENTE")
    print("=" * 80)
    print()
    print(f"Spreadsheet: {spreadsheet.title}")
    print(f"URL: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")
    print(f"Hoja: {WORKSHEET_NAME}")
    print(f"Total filas: {len(df):,}")
    print()
    print("Top 10 CALE por cantidad de IEBM:")
    top_cales = df['nodo_cale_mas_cercano'].value_counts().head(10)
    for cale, count in top_cales.items():
        print(f"  {cale}: {count:,} IEBM")

if __name__ == '__main__':
    main()
