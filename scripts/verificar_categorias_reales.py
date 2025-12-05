"""
Script para verificar qué categorías CALE existen realmente en Google Sheets
"""

import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuración
SPREADSHEET_ID = "1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU"
CREDENTIALS_PATH = r"c:\raziel\ia_formulacion\.config\credentials_google.json"
SHEET_NAME = "arquitectura_red_cale_nacional"

def main():
    print("[*] Verificando categorias CALE en Google Sheets...\n")

    # Cargar credenciales
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
    )

    # Crear servicio
    service = build('sheets', 'v4', credentials=credentials)

    # Leer datos
    range_name = f"'{SHEET_NAME}'!A2:Z198"
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name
    ).execute()

    values = result.get('values', [])

    if not values:
        print("[ERROR] No se encontraron datos")
        return

    # Obtener headers
    headers_result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{SHEET_NAME}'!A1:Z1"
    ).execute()

    headers = headers_result.get('values', [[]])[0]

    # Encontrar columna de categoría
    cat_index = None
    for i, header in enumerate(headers):
        if 'categoria' in header.lower() and 'cale' in header.lower():
            cat_index = i
            print(f"[OK] Columna de categoria encontrada: '{header}' (columna {i})")
            break

    if cat_index is None:
        print("[ERROR] No se encontro columna de categoria_cale")
        return

    # Extraer todas las categorías únicas
    categorias = set()
    for row in values:
        if len(row) > cat_index:
            cat = row[cat_index].strip()
            if cat:
                categorias.add(cat)

    # Mostrar resultados
    print(f"\n[*] Categorias encontradas: {len(categorias)}\n")

    for cat in sorted(categorias):
        count = sum(1 for row in values if len(row) > cat_index and row[cat_index].strip() == cat)
        print(f"   {cat:<15} -> {count:>3} centros")

    print("\n" + "="*50)
    print("RESULTADO PARA USAR EN EL CÓDIGO:")
    print("="*50)
    print("\nconst CATEGORIAS_CALE = [")

    # Definir colores por categoría
    colores = {
        'CALE.n_1': '#2563eb',   # Azul
        'CALE.n_2': '#16a34a',   # Verde
        'CALE.n_3': '#ea580c',   # Naranja
        'CALE.C2': '#dc2626',    # Rojo
        'CALE.C3': '#dc2626',
        'CALE.C4': '#dc2626',
        'CALE.C5': '#dc2626',
    }

    for cat in sorted(categorias):
        color = colores.get(cat, '#666666')
        print(f"    {{ id: '{cat}', nombre: '{cat}', color: '{color}' }},")

    print("];\n")

if __name__ == '__main__':
    main()
