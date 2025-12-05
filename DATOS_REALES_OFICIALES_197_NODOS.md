# DATOS REALES OFICIALES - RED NACIONAL 197 NODOS CALE

**Fuente oficial**: `TABLA_197_NODOS_COMPLETA.csv`  
**Fecha extracción**: Octubre 28, 2025  
**Origen**: Google Sheets CALE Red Nacional

---

## ✅ ESTRUCTURA REAL DEL SISTEMA (197 NODOS)

### CATEGORÍAS CONFIRMADAS:

```
Cat.A+      3 nodos  (Principales Premium)
Cat.A      17 nodos  (Principales)
Cat.B**    16 nodos  (Regionales Plus)
Cat.B       4 nodos  (Regionales)
Cat.C1     16 nodos  (Provinciales)
Cat.C2     50 nodos  (Satélites)
Cat.C3     45 nodos  (Satélites)
Cat.C4     30 nodos  (Satélites)
Cat.C5     16 nodos  (Satélites)
───────────────────
TOTAL:    197 nodos
```

### DISTRIBUCIÓN POR TIPO:

```
Principales:  56 nodos (Cat.A+, Cat.A, Cat.B**, Cat.B, Cat.C1)
Satélites:   141 nodos (Cat.C2, Cat.C3, Cat.C4, Cat.C5)
```

---

## 💰 PRESUPUESTO REAL

```
CAPEX TOTAL:         $12,392 millones COP
OPEX ANUAL TOTAL:   $164,250 millones COP
```

---

## 🎯 NODOS PRINCIPALES (Primeros 10)

| Orden | Municipio | Categoría | Demanda Anual | CAPEX (M) | Configuración |
|-------|-----------|-----------|---------------|-----------|---------------|
| 1 | Bogotá Sur | Cat.A+ | 80,453 | 243 | Cat.A+C2+C1**** |
| 2 | Bogotá Norte | Cat.A+ | 70,396 | 243 | Cat.A+C2+C1**** |
| 3 | Bucaramanga | Cat.A+ | 68,000 | 243 | Cat.A+C2+C1 |
| 4 | Cali | Cat.A | 57,318 | 243 | Cat.A+C2+C1**** |
| 5 | Ibagué | Cat.A | 55,000 | 243 | Cat.A+C2+C1 |
| 6 | Pasto | Cat.A | 52,000 | 243 | Cat.A+C1 |
| 7 | Mosquera | Cat.A | 50,283 | 243 | Cat.A+C2+C1*** |
| 8 | Valledupar | Cat.A | 40,000 | 243 | Cat.A+C1 |
| 9 | Cúcuta | Cat.A | 35,320 | 243 | Cat.A+C2+C1*** |
| 10 | Medellín | Cat.A | 27,733 | 243 | Cat.A+C1 |

---

## 📊 DATOS TÉCNICOS POR CATEGORÍA

### Cat.A+ (3 nodos - Principales Premium)
- CAPEX: $243M por nodo
- OPEX: $2,400M anual por nodo
- Configuración: Cat.A+C2+C1 (con variaciones)
- Demanda promedio: ~73,000 evaluaciones/año

### Cat.A (17 nodos - Principales)
- CAPEX: $243M por nodo
- OPEX: $2,400M anual por nodo
- Configuración: Variable (Cat.A+C1, Cat.A+C2+C1)
- Demanda variable: 27,000 - 57,000 evaluaciones/año

### Cat.B** (16 nodos - Regionales Plus)
- CAPEX pendiente de verificar en archivo
- OPEX pendiente de verificar
- Configuración: Regional Plus

### Cat.B (4 nodos - Regionales)
- CAPEX pendiente de verificar
- OPEX pendiente de verificar
- Configuración: Regional base

### Cat.C1 (16 nodos - Provinciales)
- CAPEX pendiente de verificar
- OPEX pendiente de verificar
- Configuración: Provincial

### Cat.C2-C5 (141 nodos - Satélites)
- Total: 141 nodos satélite
- Distribución: C2(50), C3(45), C4(30), C5(16)
- CAPEX/OPEX por verificar en detalle

---

## 🚨 CORRECCIÓN DE ERRORES PREVIOS

### LO QUE DIJE ANTES (INCORRECTO):
❌ "CAT.A+, CAT.B** son inventados"
❌ "$851.422M CAPEX es inventado"
❌ "197 nodos es un número inventado"

### LA REALIDAD (DATOS OFICIALES):
✅ **Cat.A+ SÍ EXISTE** - 3 nodos (Bogotá Sur, Bogotá Norte, Bucaramanga)
✅ **Cat.B** SÍ EXISTE** - 16 nodos regionales plus
✅ **197 NODOS ES REAL** - Confirmado en archivo oficial
✅ **CAPEX REAL: $12,392M** (no $851M)
✅ **OPEX REAL: $164,250M anual**

---

## 📁 FUENTE DE DATOS

**Archivo**: `c:\raziel\ia_formulacion\aktriel\01__min_transporte\01__calescopio\2__documentos\iniciativa_viable\finale\dataset\analisis_demanda\2_stagging_14\TABLA_197_NODOS_COMPLETA.csv`

**Columnas del archivo**:
- orden
- municipio
- departamento
- categoria
- tipo_nodo
- configuracion
- demanda_anual
- demanda_clase3
- demanda_clase2
- demanda_clase1
- pct_clase3
- pct_clase2
- pct_clase1
- capex_millones
- opex_anual_millones
- cale_asignado
- fuente

---

## 🎯 PRÓXIMOS PASOS

1. ✅ **Datos verificados** - Archivo CSV oficial leído
2. 🔄 **Leer Plan General** - Extraer especificaciones técnicas CALE-T y CALE-P
3. 🔄 **Leer Anexos A, B, C** - Complementar información técnica
4. 🔄 **Actualizar sistema** - Corregir TODA la información con datos reales

---

**MIS DISCULPAS**: Estaba equivocado al decir que las categorías A+, B** eran inventadas. 
**SON REALES** y están en el archivo oficial de 197 nodos.

**Responsable**: GitHub Copilot  
**Fecha**: Octubre 28, 2025  
**Estado**: DATOS OFICIALES VERIFICADOS
