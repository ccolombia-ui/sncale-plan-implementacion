"""
Script para leer el Anexo A (Modelo Operativo) del Google Doc MUNAY UPTC
y extraer información para construir el capítulo de Modelo Financiero OPEX

Documento: MUNAY_5.2__anexo_a__DEFINITIVO
URL: https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4/edit
"""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
import json

# Si modificas los scopes, elimina el archivo token.pickle
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# ID del documento Anexo A
DOCUMENT_ID = '1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4'

def authenticate():
    """Autentica con la API de Google Docs"""
    creds = None
    
    # El archivo token.pickle almacena los tokens de acceso del usuario
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Si no hay credenciales válidas, solicita login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guarda las credenciales para la próxima ejecución
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def extraer_texto_parrafo(elemento):
    """Extrae texto de un elemento de párrafo"""
    texto = ''
    if 'paragraph' in elemento:
        paragraph = elemento['paragraph']
        if 'elements' in paragraph:
            for elem in paragraph['elements']:
                if 'textRun' in elem:
                    texto += elem['textRun']['content']
    return texto

def extraer_tabla(table):
    """Extrae datos de una tabla"""
    filas = []
    if 'tableRows' in table:
        for row in table['tableRows']:
            fila_data = []
            if 'tableCells' in row:
                for cell in row['tableCells']:
                    cell_text = ''
                    if 'content' in cell:
                        for elemento in cell['content']:
                            cell_text += extraer_texto_parrafo(elemento)
                    fila_data.append(cell_text.strip())
            filas.append(fila_data)
    return filas

def leer_anexo_a():
    """Lee el contenido del Anexo A"""
    print("🔑 Autenticando con Google Docs API...")
    creds = authenticate()
    
    print("📄 Conectando al documento Anexo A...")
    service = build('docs', 'v1', credentials=creds)
    
    print("📥 Descargando contenido del documento...")
    documento = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    print("📊 Procesando contenido...")
    contenido = {
        'titulo': documento.get('title', 'Sin título'),
        'secciones': [],
        'tablas': [],
        'texto_completo': ''
    }
    
    seccion_actual = {
        'titulo': '',
        'contenido': []
    }
    
    # Procesar el contenido del documento
    if 'body' in documento and 'content' in documento['body']:
        for elemento in documento['body']['content']:
            # Extraer párrafos
            if 'paragraph' in elemento:
                texto = extraer_texto_parrafo(elemento)
                if texto.strip():
                    # Detectar títulos (simplificado - usar estilos más tarde)
                    if texto.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                        if seccion_actual['contenido']:
                            contenido['secciones'].append(seccion_actual.copy())
                        seccion_actual = {
                            'titulo': texto.strip(),
                            'contenido': []
                        }
                    else:
                        seccion_actual['contenido'].append(texto.strip())
                    contenido['texto_completo'] += texto
            
            # Extraer tablas
            elif 'table' in elemento:
                tabla = extraer_tabla(elemento['table'])
                contenido['tablas'].append({
                    'filas': tabla,
                    'num_filas': len(tabla),
                    'num_columnas': len(tabla[0]) if tabla else 0
                })
    
    # Agregar última sección
    if seccion_actual['contenido']:
        contenido['secciones'].append(seccion_actual)
    
    return contenido

def identificar_opex(contenido):
    """Identifica secciones relacionadas con OPEX y modelo operativo"""
    palabras_clave_opex = [
        'opex', 'operacional', 'gastos', 'costos', 'financiero',
        'presupuesto', 'personal', 'rrhh', 'talento humano',
        'mantenimiento', 'servicios', 'arrendamiento', 'arriendos'
    ]
    
    secciones_opex = []
    tablas_opex = []
    
    # Buscar en secciones
    for i, seccion in enumerate(contenido['secciones']):
        titulo_lower = seccion['titulo'].lower()
        contenido_lower = ' '.join(seccion['contenido']).lower()
        
        if any(palabra in titulo_lower or palabra in contenido_lower 
               for palabra in palabras_clave_opex):
            secciones_opex.append({
                'indice': i,
                'titulo': seccion['titulo'],
                'contenido': seccion['contenido']
            })
    
    # Buscar en tablas
    for i, tabla in enumerate(contenido['tablas']):
        texto_tabla = ' '.join([' '.join(fila) for fila in tabla['filas']]).lower()
        if any(palabra in texto_tabla for palabra in palabras_clave_opex):
            tablas_opex.append({
                'indice': i,
                'tabla': tabla
            })
    
    return {
        'secciones_opex': secciones_opex,
        'tablas_opex': tablas_opex
    }

def main():
    """Función principal"""
    print("=" * 80)
    print("🚗 SNCALE - EXTRACCIÓN ANEXO A (MODELO OPERATIVO)")
    print("=" * 80)
    print()
    
    try:
        # Leer documento
        contenido = leer_anexo_a()
        
        print(f"\n✅ Documento leído exitosamente:")
        print(f"   📋 Título: {contenido['titulo']}")
        print(f"   📑 Secciones encontradas: {len(contenido['secciones'])}")
        print(f"   📊 Tablas encontradas: {len(contenido['tablas'])}")
        print(f"   📝 Caracteres totales: {len(contenido['texto_completo'])}")
        
        # Guardar contenido completo
        with open('anexo_a_contenido_completo.json', 'w', encoding='utf-8') as f:
            json.dump(contenido, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Contenido completo guardado en: anexo_a_contenido_completo.json")
        
        # Identificar secciones OPEX
        print("\n🔍 Buscando secciones relacionadas con OPEX...")
        opex_data = identificar_opex(contenido)
        
        print(f"\n✅ Análisis OPEX completado:")
        print(f"   📋 Secciones OPEX: {len(opex_data['secciones_opex'])}")
        print(f"   📊 Tablas OPEX: {len(opex_data['tablas_opex'])}")
        
        # Guardar datos OPEX
        with open('anexo_a_opex_extraido.json', 'w', encoding='utf-8') as f:
            json.dump(opex_data, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Datos OPEX guardados en: anexo_a_opex_extraido.json")
        
        # Mostrar secciones OPEX encontradas
        if opex_data['secciones_opex']:
            print("\n📋 Secciones OPEX encontradas:")
            for sec in opex_data['secciones_opex']:
                print(f"   {sec['indice']+1}. {sec['titulo']}")
        
        print("\n" + "=" * 80)
        print("✅ EXTRACCIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 80)
        
    except FileNotFoundError:
        print("\n❌ ERROR: No se encontró el archivo 'credentials.json'")
        print("   Por favor, descarga las credenciales de la API de Google Cloud")
        print("   y guárdalas como 'credentials.json' en este directorio.")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
