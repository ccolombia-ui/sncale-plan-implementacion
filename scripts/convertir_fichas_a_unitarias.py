#!/usr/bin/env python3
"""
Convertir fichas L3 de valor NACIONAL a valor UNITARIO
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FICHAS_L3 = ROOT / 'fichas_l3'
OUTPUT = ROOT / 'fichas_l3_unitarias'

def extraer_valor(texto_valor):
    """Extrae el valor numérico de un string como '$1.850.000.000'"""
    return int(texto_valor.replace('$', '').replace('.', '').replace(',', ''))

def formatear_valor(valor):
    """Formatea un valor numérico como '$1.850.000.000'"""
    valor_str = f"{valor:,}".replace(',', '.')
    return f"${valor_str}"

def corregir_ficha_a_unitaria(archivo_html):
    """Convierte una ficha de valores nacionales a valores unitarios"""
    
    with open(archivo_html, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Extraer valorización total actual
    match_valor = re.search(r'<h3>💰 Valorización Total</h3>\s*<p>\$([\d.]+)\s+COP</p>', contenido)
    if not match_valor:
        print(f"⚠️ No se encontró valorización total en {archivo_html.name}")
        return None
    
    valor_nacional = extraer_valor(match_valor.group(1))
    
    # Extraer cantidad de nodos base
    match_nodos = re.search(r'<p><strong>Nodos Base:</strong>\s*(\d+)</p>', contenido)
    if not match_nodos:
        print(f"⚠️ No se encontró cantidad de nodos en {archivo_html.name}")
        return None
    
    cant_nodos = int(match_nodos.group(1))
    
    # Calcular valor unitario
    valor_unitario = valor_nacional // cant_nodos
    
    print(f"\n📦 {archivo_html.name}")
    print(f"   Valor NACIONAL: {formatear_valor(valor_nacional)}")
    print(f"   Cantidad nodos: {cant_nodos}")
    print(f"   Valor UNITARIO: {formatear_valor(valor_unitario)}")
    
    # 1. Cambiar valorización total
    contenido_nuevo = re.sub(
        r'(<h3>💰 Valorización Total</h3>\s*<p>)\$[\d.]+\s+COP',
        r'\1' + formatear_valor(valor_unitario) + ' COP',
        contenido
    )
    
    # 2. Cambiar descripción a indicar que es UNITARIA
    contenido_nuevo = re.sub(
        r'(para centros en [^<]+)',
        r'\1 (VALORES UNITARIOS - 1 unidad)',
        contenido_nuevo
    )
    
    # 3. Actualizar cada fila de componente
    # Buscar todas las filas de la tabla de componentes
    def actualizar_fila(match):
        fila = match.group(0)
        
        # Extraer valor unitario
        match_valor_unit = re.search(r'<td class="text-right">\$([\d.]+)</td>', fila)
        if not match_valor_unit:
            return fila
        
        valor_unit_comp = extraer_valor(match_valor_unit.group(1))
        
        # Extraer cantidad base (puede ser 20, 40, etc.)
        match_cant = re.search(r'<td class="text-center">(\d+)</td>', fila)
        if not match_cant:
            return fila
        
        cant_nacional = int(match_cant.group(1))
        
        # Calcular cantidad unitaria
        # Si cant_nacional es múltiplo de cant_nodos, es la cantidad por nodo
        if cant_nacional % cant_nodos == 0:
            cant_unitaria = cant_nacional // cant_nodos
        else:
            cant_unitaria = 1
        
        # Calcular valor total unitario
        valor_total_unitario = valor_unit_comp * cant_unitaria
        
        # Reemplazar cantidad base
        fila_nueva = re.sub(
            r'(<td class="text-center">)\d+(</td>\s*<td class="text-center">)',
            r'\g<1>' + str(cant_unitaria) + r'\g<2>',
            fila,
            count=1
        )
        
        # Reemplazar valor total
        fila_nueva = re.sub(
            r'(<td class="text-right"><strong>)\$[\d.]+(</strong></td>)',
            r'\1' + formatear_valor(valor_total_unitario) + r'\2',
            fila_nueva
        )
        
        return fila_nueva
    
    # Aplicar a todas las filas <tr> del tbody
    contenido_nuevo = re.sub(
        r'<tr>\s*<td>\d+</td>.*?</tr>',
        actualizar_fila,
        contenido_nuevo,
        flags=re.DOTALL
    )
    
    # 4. Actualizar descripción "Cantidad de Nodos" a indicar que es por 1 unidad
    contenido_nuevo = re.sub(
        r'(<h3>📍 Cantidad de Nodos</h3>\s*<p><strong>Nodos Base:</strong> )\d+',
        r'\g<1>1 (UNITARIA)',
        contenido_nuevo
    )
    
    return contenido_nuevo

def main():
    OUTPUT.mkdir(exist_ok=True)
    
    print('🔄 CONVIRTIENDO FICHAS L3 A VALORES UNITARIOS\n')
    print('=' * 80)
    
    fichas = sorted(FICHAS_L3.glob('BIM_L3_*.html'))
    
    for ficha in fichas:
        contenido_corregido = corregir_ficha_a_unitaria(ficha)
        
        if contenido_corregido:
            archivo_salida = OUTPUT / ficha.name
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write(contenido_corregido)
            print(f"   ✅ Generado: {archivo_salida.relative_to(ROOT)}")
    
    print('\n' + '=' * 80)
    print(f"\n✅ Fichas unitarias generadas en: {OUTPUT.relative_to(ROOT)}/\n")
    print("🔍 VERIFICAR:")
    print("   1. Valorización Total dividida por cantidad de nodos")
    print("   2. Cant. Base actualizada (ej: 40→2 para simuladores, 20→1 para pistas)")
    print("   3. Valor Total de cada componente recalculado")
    print("   4. Título actualizado con '(VALORES UNITARIOS - 1 unidad)'")

if __name__ == '__main__':
    main()
