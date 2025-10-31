"""
Script para crear la hoja 'Asignación Municipal 1122' en Google Sheets
usando la cuenta de servicio
"""

import json
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuración
SPREADSHEET_ID = "1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU"
CREDENTIALS_PATH = r"c:\raziel\ia_formulacion\.config\credentials_google.json"
CSV_PATH = r"C:\raziel\ia_formulacion\data\ASIGNACION_1122_MUNICIPIOS_A_197_NODOS_CALE.csv"
SHEET_NAME = "Asignación Municipal 1122"

def main():
    print(f"[*] Cargando credenciales desde: {CREDENTIALS_PATH}")

    # Cargar credenciales
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    # Crear servicio
    service = build('sheets', 'v4', credentials=credentials)

    print(f"\n[*] Creando hoja '{SHEET_NAME}'...")

    # Crear nueva hoja
    try:
        request_body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': SHEET_NAME,
                        'gridProperties': {
                            'rowCount': 1150,  # 1122 municipios + encabezado + margen
                            'columnCount': 10
                        }
                    }
                }
            }]
        }

        response = service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body=request_body
        ).execute()

        print(f"[OK] Hoja '{SHEET_NAME}' creada exitosamente")

    except Exception as e:
        if "already exists" in str(e).lower():
            print(f"[!] La hoja '{SHEET_NAME}' ya existe, continuando...")
        else:
            print(f"[ERROR] Error al crear hoja: {e}")
            return

    # Leer CSV
    print(f"\n[*] Leyendo datos desde: {CSV_PATH}")

    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(f"[OK] Leidas {len(data)} filas (incluyendo encabezado)")

    # Subir datos
    print(f"\n[*] Subiendo datos a Google Sheets...")

    range_name = f"'{SHEET_NAME}'!A1"

    body = {
        'values': data
    }

    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

    updated_cells = result.get('updatedCells', 0)
    print(f"[OK] {updated_cells} celdas actualizadas")

    # Formatear encabezado
    print(f"\n[*] Formateando encabezado...")

    try:
        # Obtener sheet ID
        sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        sheet_id = None
        for sheet in sheet_metadata.get('sheets', []):
            if sheet.get('properties', {}).get('title') == SHEET_NAME:
                sheet_id = sheet.get('properties', {}).get('sheetId')
                break

        if sheet_id is not None:
            format_request = {
                'requests': [
                    {
                        'repeatCell': {
                            'range': {
                                'sheetId': sheet_id,
                                'startRowIndex': 0,
                                'endRowIndex': 1
                            },
                            'cell': {
                                'userEnteredFormat': {
                                    'backgroundColor': {
                                        'red': 0.26,
                                        'green': 0.52,
                                        'blue': 0.96
                                    },
                                    'textFormat': {
                                        'foregroundColor': {
                                            'red': 1.0,
                                            'green': 1.0,
                                            'blue': 1.0
                                        },
                                        'fontSize': 10,
                                        'bold': True
                                    }
                                }
                            },
                            'fields': 'userEnteredFormat(backgroundColor,textFormat)'
                        }
                    },
                    {
                        'updateSheetProperties': {
                            'properties': {
                                'sheetId': sheet_id,
                                'gridProperties': {
                                    'frozenRowCount': 1
                                }
                            },
                            'fields': 'gridProperties.frozenRowCount'
                        }
                    }
                ]
            }

            service.spreadsheets().batchUpdate(
                spreadsheetId=SPREADSHEET_ID,
                body=format_request
            ).execute()

            print(f"[OK] Encabezado formateado (azul, texto blanco, negrita, congelado)")

    except Exception as e:
        print(f"[!] No se pudo formatear el encabezado: {e}")

    print(f"\n=== COMPLETADO ===")
    print(f"\nResumen:")
    print(f"   - Hoja: '{SHEET_NAME}'")
    print(f"   - Municipios: {len(data) - 1}")
    print(f"   - Columnas: {len(data[0])}")
    print(f"\nVer en: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit#gid={sheet_id if sheet_id else 0}")

if __name__ == '__main__':
    main()
