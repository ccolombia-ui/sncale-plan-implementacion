import pandas as pd

# Leer CSV
df = pd.read_csv('arquitectura_red_cale_nacional_MAPEADO.csv')

print(f"Total filas: {len(df)}")
print()
print("COLUMNA K - nodo_principal (para copiar a Google Sheets)")
print("=" * 60)
print()

# Imprimir cada valor en una línea (listo para copiar)
for val in df['nodo_principal']:
    print(val)

print()
print("=" * 60)
print(f"Total valores: {len(df)}")
print()
print("INSTRUCCIONES:")
print("1. Selecciona TODO el output desde 'NODO_02' hasta el ultimo valor")
print("2. Copia (Ctrl+C)")
print("3. Ve a Google Sheets")
print("4. Click en celda K2 (primera celda de datos, NO el header)")
print("5. Pega (Ctrl+V)")
print("6. Los 197 valores se pegaran automaticamente")
