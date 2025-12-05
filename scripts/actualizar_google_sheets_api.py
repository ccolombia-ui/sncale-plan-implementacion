"""
Script para actualizar Google Sheets directamente usando la API de Google Sheets
Actualiza la columna K (nodo_principal) con valores corregidos

REQUISITOS:
pip install gspread oauth2client pandas

CREDENCIALES:
Necesitas un archivo credentials.json de Google Cloud Console
https://console.cloud.google.com/apis/credentials
"""

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
import os

# Configuración
SPREADSHEET_ID = '1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU'
WORKSHEET_NAME = 'arquitectura_red_cale_nacional'
COLUMN_TO_UPDATE = 'K'  # nodo_principal
CSV_FILE = 'arquitectura_red_cale_nacional_MAPEADO.csv'

def conectar_google_sheets(credentials_file='.config/credentials_google.json'):
    """Conectar a Google Sheets usando credenciales"""
    try:
        # Define el scope
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]

        # Autenticar
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)

        print(f"[OK] Autenticado con Google Sheets API")
        return client

    except FileNotFoundError:
        print(f"[ERROR] No se encontro el archivo de credenciales: {credentials_file}")
        print()
        print("INSTRUCCIONES PARA OBTENER CREDENCIALES:")
        print("1. Ir a: https://console.cloud.google.com/apis/credentials")
        print("2. Crear proyecto (si no tienes uno)")
        print("3. Habilitar Google Sheets API")
        print("4. Crear Service Account")
        print("5. Descargar JSON y guardarlo como 'credentials.json'")
        print("6. Compartir la Google Sheet con el email del Service Account")
        sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Error de autenticacion: {e}")
        sys.exit(1)

def actualizar_columna_k(client, csv_file=CSV_FILE):
    """Actualizar columna K en Google Sheets"""
    try:
        # 1. Leer CSV con valores corregidos
        print(f"[*] Leyendo CSV: {csv_file}")
        df = pd.read_csv(csv_file)
        print(f"[OK] CSV leido: {len(df)} filas")

        # 2. Extraer columna nodo_principal
        valores_columna_k = df['nodo_principal'].tolist()
        print(f"[OK] Extraidos {len(valores_columna_k)} valores para columna K")

        # 3. Abrir Google Sheet
        print(f"[*] Abriendo Google Sheet: {SPREADSHEET_ID}")
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        print(f"[OK] Hoja abierta: {WORKSHEET_NAME}")

        # 4. Verificar datos actuales
        current_values = worksheet.col_values(11)  # Columna K = 11
        print(f"[*] Valores actuales en columna K: {len(current_values)}")

        # 5. Preparar rango de actualización (K2:K198)
        start_row = 2  # Primera fila de datos (después del header)
        end_row = start_row + len(valores_columna_k) - 1
        rango = f'K{start_row}:K{end_row}'

        # 6. Formatear valores para batch update
        valores_formateados = [[valor] for valor in valores_columna_k]

        print(f"[*] Actualizando rango: {rango}")
        print(f"[*] Total valores a actualizar: {len(valores_formateados)}")

        # 7. Actualizar en batch (más eficiente)
        worksheet.update(rango, valores_formateados)

        print(f"[OK] Columna K actualizada exitosamente!")
        print()

        # 8. Verificar algunos valores
        print("Verificacion de valores actualizados:")
        print("-" * 60)
        nuevos_valores = worksheet.col_values(11)
        for i in range(min(10, len(nuevos_valores) - 1)):
            fila = i + 2
            valor = nuevos_valores[i + 1]  # +1 porque col_values incluye header
            print(f"  Fila {fila}: {valor}")
        print("-" * 60)
        print(f"[OK] Total filas actualizadas: {len(valores_formateados)}")

        return True

    except Exception as e:
        print(f"[ERROR] Error actualizando Google Sheets: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 80)
    print("ACTUALIZAR GOOGLE SHEETS - COLUMNA K (nodo_principal)")
    print("=" * 80)
    print()

    # Verificar que existe el CSV
    if not os.path.exists(CSV_FILE):
        print(f"[ERROR] No se encuentra el archivo: {CSV_FILE}")
        print(f"[ERROR] Ejecutar primero: python scripts/mapear_nodo_principal.py")
        sys.exit(1)

    # Conectar a Google Sheets
    print("[*] Conectando a Google Sheets API...")
    client = conectar_google_sheets()

    # Actualizar columna K
    exito = actualizar_columna_k(client)

    if exito:
        print()
        print("=" * 80)
        print("[OK] ACTUALIZACION COMPLETADA EXITOSAMENTE")
        print("=" * 80)
        print()
        print("SIGUIENTE PASO:")
        print("1. Verificar Google Sheets manualmente")
        print("2. Publicar hoja como CSV (File → Share → Publish to web)")
        print("3. Probar mapa: services/github_pages/mapa_cale_nacional.html")
        print()
    else:
        print()
        print("=" * 80)
        print("[ERROR] ACTUALIZACION FALLIDA")
        print("=" * 80)
        sys.exit(1)

if __name__ == "__main__":
    main()
