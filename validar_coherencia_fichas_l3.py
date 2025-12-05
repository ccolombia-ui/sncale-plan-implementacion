#!/usr/bin/env python3
"""
Script de validación compositiva para fichas L3
Verifica que la suma de componentes = valor total unitario
y otras validaciones de coherencia estructural
"""

import re
from pathlib import Path
from html.parser import HTMLParser

class FichaL3Parser(HTMLParser):
    """Parser HTML para extraer datos de fichas L3"""
    
    def __init__(self):
        super().__init__()
        self.in_h3 = False
        self.last_h3_text = ""
        self.in_valor_total_section = False
        self.in_component_row = False
        self.in_valor_cell = False
        self.valor_total = None
        self.componentes = []
        self.current_component = {}
        self.cell_count = 0
        
    def handle_starttag(self, tag, attrs):
        # Detectar inicio de h3
        if tag == "h3":
            self.in_h3 = True
            self.last_h3_text = ""
            
        # Detectar fila de componente
        if tag == "tr":
            self.in_component_row = True
            self.current_component = {}
            self.cell_count = 0
            
        # Detectar celda de valor
        if tag == "td" and self.in_component_row:
            self.cell_count += 1
            if self.cell_count == 8:  # Columna "Valor Total"
                self.in_valor_cell = True
    
    def handle_data(self, data):
        data = data.strip()
        
        # Capturar texto de h3
        if self.in_h3:
            self.last_h3_text += data
        
        # Si el h3 anterior era "Valorización Total", el siguiente dato con $ es el valor
        if self.in_valor_total_section and data.startswith("$") and not self.valor_total:
            self.valor_total = self._parse_cop(data)
            self.in_valor_total_section = False
        
        # Capturar valor de componente
        if self.in_valor_cell and data.startswith("$"):
            valor = self._parse_cop(data)
            if valor > 0:
                self.componentes.append(valor)
            self.in_valor_cell = False
    
    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_h3 = False
            # Si acabamos de cerrar un h3 que dice "Valorización Total"
            if "Valorización Total" in self.last_h3_text or "💰" in self.last_h3_text:
                self.in_valor_total_section = True
        
        if tag == "tr":
            self.in_component_row = False
            self.cell_count = 0
    
    def _parse_cop(self, valor_str):
        """Convierte string $X.XXX.XXX a número"""
        # Remover $, espacios, puntos, comas
        cleaned = valor_str.replace("$", "").replace(" ", "").replace(".", "").replace(",", "").replace("COP", "").strip()
        try:
            return int(cleaned)
        except ValueError:
            return 0

def validar_ficha(ruta_ficha):
    """Valida coherencia compositiva de una ficha L3"""
    
    nombre_ficha = ruta_ficha.name
    
    try:
        with open(ruta_ficha, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = FichaL3Parser()
        parser.feed(html_content)
        
        valor_total = parser.valor_total
        componentes = parser.componentes
        suma_componentes = sum(componentes)
        
        if not valor_total:
            return {
                "ficha": nombre_ficha,
                "estado": "⚠️ ADVERTENCIA",
                "mensaje": "No se pudo leer valor total",
                "detalles": None
            }
        
        if not componentes:
            return {
                "ficha": nombre_ficha,
                "estado": "⚠️ ADVERTENCIA", 
                "mensaje": "No se encontraron componentes",
                "detalles": {
                    "valor_total": valor_total,
                    "componentes": 0,
                    "suma": 0
                }
            }
        
        # Calcular diferencia
        diferencia = abs(valor_total - suma_componentes)
        porcentaje_error = (diferencia / valor_total) * 100 if valor_total > 0 else 0
        
        # Tolerancia: 0.1% (errores de redondeo)
        if porcentaje_error < 0.1:
            estado = "✅ VÁLIDA"
        elif porcentaje_error < 1.0:
            estado = "⚠️ REVISAR"
        else:
            estado = "❌ ERROR"
        
        return {
            "ficha": nombre_ficha,
            "estado": estado,
            "mensaje": f"Diferencia: ${diferencia:,} ({porcentaje_error:.2f}%)",
            "detalles": {
                "valor_total": valor_total,
                "cantidad_componentes": len(componentes),
                "suma_componentes": suma_componentes,
                "diferencia": diferencia,
                "porcentaje_error": porcentaje_error
            }
        }
        
    except Exception as e:
        return {
            "ficha": nombre_ficha,
            "estado": "❌ ERROR",
            "mensaje": f"Error al procesar: {str(e)}",
            "detalles": None
        }

def main():
    """Ejecuta validación en todas las fichas L3"""
    
    print("=" * 100)
    print("VALIDACIÓN COMPOSITIVA - FICHAS L3")
    print("=" * 100)
    print()
    
    # Buscar todas las fichas L3
    fichas_dir = Path("fichas_l3_unitarias")
    
    if not fichas_dir.exists():
        print(f"❌ ERROR: No se encontró el directorio {fichas_dir}")
        return
    
    fichas = sorted(fichas_dir.glob("BIM_L3_*.html"))
    
    if not fichas:
        print(f"❌ ERROR: No se encontraron fichas en {fichas_dir}")
        return
    
    print(f"📁 Encontradas {len(fichas)} fichas\n")
    
    # Validar cada ficha
    resultados = []
    for ficha in fichas:
        resultado = validar_ficha(ficha)
        resultados.append(resultado)
    
    # Mostrar resultados
    print(f"{'Ficha':<20} | {'Estado':<15} | {'Mensaje':<50}")
    print("-" * 100)
    
    validas = 0
    advertencias = 0
    errores = 0
    
    for r in resultados:
        print(f"{r['ficha']:<20} | {r['estado']:<15} | {r['mensaje']:<50}")
        
        if r['detalles'] and 'cantidad_componentes' in r['detalles']:
            d = r['detalles']
            print(f"{'':>20}   → Valor total: ${d['valor_total']:,}")
            print(f"{'':>20}   → Componentes: {d['cantidad_componentes']}")
            print(f"{'':>20}   → Suma: ${d['suma_componentes']:,}")
            print()
        elif r['detalles']:
            d = r['detalles']
            print(f"{'':>20}   → Valor total: ${d['valor_total']:,}")
            print(f"{'':>20}   → Componentes: {d.get('componentes', 'N/A')}")
            print()
        
        if r['estado'].startswith("✅"):
            validas += 1
        elif r['estado'].startswith("⚠️"):
            advertencias += 1
        else:
            errores += 1
    
    print("-" * 100)
    print(f"\n📊 RESUMEN:")
    print(f"  ✅ Válidas: {validas}/{len(resultados)}")
    print(f"  ⚠️ Advertencias: {advertencias}/{len(resultados)}")
    print(f"  ❌ Errores: {errores}/{len(resultados)}")
    print()
    
    if errores == 0 and advertencias == 0:
        print("🎉 TODAS LAS FICHAS SON COHERENTES")
    elif errores == 0:
        print("✅ NO HAY ERRORES CRÍTICOS (solo advertencias menores)")
    else:
        print("⚠️ SE ENCONTRARON ERRORES QUE REQUIEREN CORRECCIÓN")
    
    print("=" * 100)

if __name__ == "__main__":
    main()
