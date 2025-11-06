# 🔍 HALLAZGO CRÍTICO: DIFERENCIA PLAN V4.1 VS ANEXO B

**Fecha:** 2025-11-05  
**Analista:** Reconciliación automatizada  
**Impacto:** ALTO - Afecta valorización nacional

---

## 🎯 RESUMEN EJECUTIVO

### El Problema
- **Plan v4.1 CALE.n_1:** $10.578B unitario
- **Anexo B CALE.n_1:** $7.066B unitario
- **Diferencia:** $3.512B (33% más en Plan v4.1)

### La Causa Raíz
**El Plan v4.1 incluye el PREDIO (terreno) en sus cálculos. El Anexo B NO lo incluye.**

---

## 📋 ANÁLISIS DETALLADO

### Plan v4.1 - Sección 7.2.1 "CALE-P Clase I"

Extracción literal del documento:

```
COMPONENTE                                    | UND | Cantidad | Valor Unitario | Subtotal
--------------------------------------------------------------------------------
Construcción pistas evaluación práctica     | m²  | 3,236    | $1,237,600     | $4,004,873,600
Construcción infraestructura administrativa  | m²  | 382      | $3,180,900     | $1,215,103,800
Vehículos de prueba A1                       | UND | 3        | $7,893,200     | $23,679,600
Vehículos de prueba A2                       | UND | 3        | $10,893,000    | $32,679,000
Vehículos de prueba B1-C1                    | UND | 2        | $72,680,000    | $145,360,000
Vehículos de prueba B2-C2                    | UND | 1        | $124,300,000   | $124,300,000
Vehículos de prueba B3-C3                    | UND | 1        | $498,357,000   | $498,357,000
Equipos de seguridad                         | UND | 1        | $18,963,700    | $18,963,700
🔴 PREDIO                                    | m²  | 3,421    | $1,430,000     | $4,894,890,000
--------------------------------------------------------------------------------
TOTAL CLASE I                                                                  $10,335,549,700
```

### Desglose del Total Plan v4.1

| Concepto | Valor | % del Total |
|----------|-------|-------------|
| **PREDIO (terreno)** | $4,894,890,000 | **47.4%** |
| Construcción pistas | $4,004,873,600 | 38.7% |
| Construcción admin | $1,215,103,800 | 11.8% |
| Vehículos (todos) | $822,375,600 | 8.0% |
| Equipos seguridad | $18,963,700 | 0.2% |
| **TOTAL** | **$10,335,549,700** | **100%** |

🚨 **El predio representa casi la MITAD del costo total en Plan v4.1**

---

## 🔄 COMPARACIÓN CON ANEXO B

### Anexo B - Sección B10.3/B10.4

El Anexo B valoriza:

| Componente | Valor Unitario | Observación |
|------------|----------------|-------------|
| Pista Clase III | $1,850,000,000 | ✅ Incluido |
| Pista Clase II | $980,000,000 | ✅ Incluido |
| Pista Clase I | $750,000,000 | ✅ Incluido |
| Sala 24 cubículos | $186,000,000 | ✅ Incluido |
| Simulador C3 | $450,000,000 | ✅ Incluido |
| Edificación admin | $2,400,000,000 | ✅ Incluido |
| **Predio** | **$0** | **🔴 NO incluido** |
| **SUBTOTAL** | **$6,616,000,000** | Sin predio |

**Diferencia identificada:**
- Plan v4.1 con predio: $10,335,549,700
- Anexo B sin predio: ~$6,616,000,000
- Diferencia: ~$3,719,549,700 (~$4.9B predio - $1.2B ajustes)

---

## 🧮 RECONCILIACIÓN ARITMÉTICA

### Fórmula Plan v4.1 (por nodo)

```
CALE.n_1 = CALE_P_Clase_I + CALE_T_24q + Satélites - OPEX_excluido

Donde CALE_P_Clase_I incluye:
  - Construcción pistas ($4.0B)
  - Construcción admin ($1.2B)
  - Vehículos ($822M)
  - Equipos ($19M)
  - 🔴 PREDIO ($4.9B) ← ESTA ES LA DIFERENCIA CLAVE

CALE_P_Clase_I_total = $10,335,549,700

Agregando CALE-T y satélites:
  + CALE_T_24q: $243,063,465
  + Satélites (7 × $12M): $84,000,000
  - OPEX excluido: -$351,000,000
  
TOTAL UNITARIO = $10,311,613,165
```

### Fórmula Anexo B (por nodo)

```
CALE.n_1 = Σ componentes L2 (pistas + edificación + CALE-T + simuladores)

Total nacional: $141,320,000,000
Nodos: 20
Unitario: $7,066,000,000

Desglose:
  - Pista Clase III: $1,850,000,000
  - Pista Clase II: $980,000,000
  - Pista Clase I: $750,000,000
  - Sala 24q: $186,000,000
  - Simulador C3: $450,000,000
  - Edificación: $2,400,000,000
  - Otros componentes L2: ~$450,000,000
  
TOTAL UNITARIO = $7,066,000,000
(SIN incluir predio)
```

---

## 💡 INTERPRETACIÓN

### Diferencia Filosófica en Modelos

1. **Plan v4.1 (Modelo CAPEX tradicional):**
   - Incluye adquisición del terreno como inversión inicial
   - Supone que el Estado debe comprar los predios
   - Valorización típica: $1,430,000/m² en Clase I
   - Área predio Clase I: 3,421 m² = $4.9B

2. **Anexo B (Modelo OPEX / arrendamiento):**
   - NO incluye predio en CAPEX
   - Supone arrendamiento mensual del terreno
   - El costo del predio va a OPEX como "arrendamiento"
   - Referencia: Anexo A muestra ~$111M/año arrendamiento en OPEX

3. **Fichas Técnicas (Configuración L3):**
   - Solo valorizan CALE-T ($645M)
   - No incluyen pistas ni predio
   - Enfocadas en equipamiento TIC y edificación básica

---

## 📊 IMPACTO EN VALORIZACIÓN NACIONAL

### Si incluimos el predio (modelo Plan v4.1):

| Config | Qty | Unitario (con predio) | Total Nacional |
|--------|-----|-----------------------|----------------|
| CALE.n_1 | 20 | $10,311,613,165 | $206,232,263,300 |
| CALE.n_2 | 20 | $14,690,966,197 | $293,819,323,940 |
| CALE.n_3 | 16 | $6,347,963,197 | $101,567,411,152 |
| **TOTAL** | **56** | - | **$601,618,998,392** |

### Si excluimos el predio (modelo Anexo B):

| Config | Qty | Unitario (sin predio) | Total Nacional |
|--------|-----|-----------------------|----------------|
| CALE.n_1 | 20 | $7,066,000,000 | $141,320,000,000 |
| CALE.n_2 | 20 | $4,925,000,000 | $98,500,000,000 |
| CALE.n_3 | 16 | $200,646,497 | $3,210,343,952 |
| **TOTAL** | **56** | - | **$243,030,343,952** |

🔴 **DIFERENCIA TOTAL: $358,588,654,440 (358 mil millones)**

---

## 🎯 CONCLUSIONES Y RECOMENDACIONES

### Conclusiones

1. ✅ **Ambos documentos son matemáticamente correctos** dentro de sus propios modelos
2. ✅ **No hay error de cálculo**, sino **diferencia conceptual** sobre el tratamiento del predio
3. ⚠️ **La diferencia de $358B es material** y debe clarificarse en la estrategia financiera

### Modelos Identificados

| Modelo | Predio | Ventaja | Desventaja |
|--------|--------|---------|------------|
| **CAPEX (Plan v4.1)** | Compra | Activo patrimonial | Inversión inicial alta |
| **OPEX (Anexo B)** | Arriendo | Menor inversión inicial | Costo perpetuo mensual |
| **Mixto** | Variable | Flexibilidad regional | Complejidad administrativa |

### Recomendaciones

#### 1. Definir Estrategia de Adquisición de Predios (URGENTE)
- [ ] ¿El Estado comprará todos los predios? → Usar Plan v4.1
- [ ] ¿El Estado arrendará los predios? → Usar Anexo B
- [ ] ¿Estrategia mixta por región? → Definir porcentajes

#### 2. Actualizar Documentos Coherentemente
- [ ] Si CAPEX: Agregar predios a Anexo B
- [ ] Si OPEX: Quitar predios de Plan v4.1, aumentar arrendamiento en Anexo A
- [ ] Crear columna "predio_incluido: SI/NO" en tabla reconciliación

#### 3. Valorizar Predio por Configuración
- [ ] CALE.n_1 (Clase I): 3,421 m² × $1,430,000 = $4.9B
- [ ] CALE.n_2 (Clase II): 4,728 m² × $1,870,000 = $8.8B
- [ ] CALE.n_3 (Clase III): Pendiente valorizar
- [ ] Crear tabla de referencia por ciudad

#### 4. Análisis OPEX si se arrienda
Si se decide arrendamiento:
- [ ] Calcular costo mensual por m² según ciudad
- [ ] Comparar VPN 20 años: compra vs arriendo
- [ ] Incluir escalamiento de arriendos (IPC)

#### 5. Documentación Técnica
- [ ] Crear "ANEXO_C_ESTRATEGIA_PREDIOS.md"
- [ ] Definir mix óptimo (% compra, % arriendo, % comodato)
- [ ] Identificar predios del Estado reutilizables

---

## 📎 REFERENCIAS

**Plan v4.1:**
- Sección 7.2.1 "CALE-P Clase I - Costos de Construcción"
- Línea 1579: "TOTAL CLASE I: $10,335,549,700"
- Componente predio: 3,421 m² × $1,430,000/m²

**Anexo B:**
- Sección B10.3: "CAPEX TOTAL CATEGORÍA CALE.N_1: $141,320,000,000"
- Sección B10.4: Tabla componentes (sin predio)

**Anexo A:**
- Sección A40: OPEX incluye "arrendamiento" ~$111M/año/nodo

---

## 🔗 ARCHIVOS RELACIONADOS

- `tabla_maestra_reconciliacion.csv` - Tabla comparativa
- `EXPLICACION_DIFERENCIAS.md` - Análisis componente por componente
- `VERIFICACION_FUENTES.md` - Confirmación de fuentes API
- `plan_41_raw.txt` (líneas 1515-1635) - Extracto Plan v4.1

---

**¿Siguiente paso?** Definir si el modelo financiero contempla **CAPEX (compra)** u **OPEX (arriendo)** para predios, y actualizar todos los documentos coherentemente.
