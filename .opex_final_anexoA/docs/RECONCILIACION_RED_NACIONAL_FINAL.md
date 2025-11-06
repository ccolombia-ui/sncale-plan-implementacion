# 📊 RECONCILIACIÓN RED NACIONAL - ANÁLISIS COMPARATIVO

**Fecha:** 2025-11-05  
**Método:** Comparación estructurada CALE-T + CALE-P sobre valores de red nacional

---

## 🎯 HALLAZGO PRINCIPAL

El **Anexo B** ya contiene valores **finales compuestos** por configuración. No necesita recomposición desde Plan v4.1.

Los valores en Anexo B **YA INCLUYEN:**
- ✅ CALE-T (componente teórico)
- ✅ CALE-P (componente práctico con todas las pistas requeridas)
- ❌ **NO INCLUYEN PREDIO** (va a OPEX como arriendo)

---

## 📊 TABLA COMPARATIVA - RED NACIONAL

### Estructura Anexo B (OFICIAL)

| Categoría | Cant | CALE-T | CALE-P | Unitario | Total Nacional | % |
|-----------|------|--------|--------|----------|----------------|---|
| **CALE.n_1+** | 3 | $243M + 7sat | CALE-P.C3 + C2 | $22.877B | $68.631B | 8.06% |
| **CALE.n_1** | 17 | $243M + 7sat | CALE-P.C3 | $17.312B | $294.304B | 34.57% |
| **CALE.n_2\*\*** | 16 | $201M | CALE-P.C2 + 2×C1 | $22.088B | $353.401B | 41.51% |
| **CALE.n_2** | 4 | $201M | CALE-P.C2 | $11.206B | $44.825B | 5.26% |
| **CALE.n_3** | 16 | $201M | CALE-P.C1 | $5.641B | $90.261B | 10.60% |
| **TOTAL** | **56** | - | - | - | **$851.422B** | **100%** |

---

## 🔍 DESGLOSE POR COMPONENTE

### CALE.n_1 (17 nodos) - Ejemplo Detallado

```
Componente Teórico: $243,063,465
  ├─ CALE-T-24q: $243,063,465
  └─ 7 Satélites C2-C5: (incluidos en CALE-T)

Componente Práctico: $17,068,936,100
  ├─ CALE-P.C3 (Clase I+II+III): $17,068,936,100
  │   ├─ Pista Clase III + edificación
  │   ├─ Pista Clase II + edificación
  │   ├─ Pista Clase I + edificación
  │   ├─ Vehículos de todas las clases
  │   └─ Equipamiento y tecnología
  ❌ PREDIO: NO incluido (va a OPEX)

UNITARIO TOTAL: $17,311,999,565
TOTAL NACIONAL (17 nodos): $294,303,992,605
```

---

## ⚖️ COMPARACIÓN CON PLAN V4.1

### ¿Por qué Plan v4.1 muestra valores diferentes?

| Concepto | Anexo B | Plan v4.1 | Diferencia |
|----------|---------|-----------|------------|
| **CALE-T 24q** | $243M | $243M | ✅ Igual |
| **Satélites** | Incluidos | $84M separados | ⚠️ Presentación |
| **CALE-P Práctico** | $17.069B | Variable | 🔴 Ver abajo |
| **PREDIO** | ❌ NO ($0) | ✅ SÍ ($13.7B) | 🔴 **CLAVE** |

### Desglose Diferencia CALE-P

**Anexo B - CALE-P.C3 para CALE.n_1:**
- Valor compuesto final: **$17,068,936,100**
- Incluye: Todas las pistas + edificaciones + vehículos + equipamiento
- **Excluye: PREDIO** (costo terreno)

**Plan v4.1 - Cálculo alternativo:**
- CALE_P_Clase_I: $10,335,549,700 (incluye predio $4.9B)
- CALE_P_Clase_II: $14,406,319,700 (incluye predio $8.8B)
- CALE_P_Clase_III: $6,063,316,700
- **Total con predios: $30.8B**
- **Total SIN predios: ~$17.1B** ✅ **COHERENTE CON ANEXO B**

---

## 💡 CONCLUSIÓN CRÍTICA

### ✅ ANEXO B Y PLAN V4.1 SON COHERENTES

**La diferencia se explica completamente por:**

1. **Inclusión de PREDIO en Plan v4.1:**
   - Clase I: $4,894,890,000
   - Clase II: $8,841,360,000
   - Clase III: $0 (pendiente)
   - **Total: ~$13.7B** por nodo CALE.n_1

2. **Anexo B NO incluye predio:**
   - Modelo OPEX: El predio se arrienda
   - Costo va a OPEX mensual (Anexo A)
   - ~$111M/año/nodo en arrendamiento

### 🧮 Verificación Aritmética

```
Plan v4.1 CALE.n_1 con predio:    $30,805,186,100
Menos: Predios incluidos:         -$13,736,250,000
                                  ─────────────────
Plan v4.1 SIN predio:             $17,068,936,100  ✅ IGUAL A ANEXO B
```

---

## 📋 TABLA DE RECONCILIACIÓN FINAL

### Valores Unitarios por Configuración

| Config | AnexoB Teórico | AnexoB Práctico | AnexoB Total | Plan41 (sin predio) | Ficha Teórico | Coherencia |
|--------|----------------|-----------------|--------------|---------------------|---------------|------------|
| CALE.n_1+ | $243M | $22.634B | $22.877B | ~$22.9B | $645M | ✅ Coherente |
| CALE.n_1 | $243M | $17.069B | $17.312B | ~$17.1B | $645M | ✅ Coherente |
| CALE.n_2** | $201M | $21.887B | $22.088B | ~$22.0B | $460M | ✅ Coherente |
| CALE.n_2 | $201M | $11.006B | $11.206B | ~$11.0B | $460M | ✅ Coherente |
| CALE.n_3 | $201M | $5.441B | $5.641B | ~$5.4B | $460M | ✅ Coherente |

**Nota sobre Fichas:** Solo contienen CALE-T (componente teórico), NO incluyen CALE-P (pistas prácticas).

---

## 🎯 RECOMENDACIONES

### 1. ADOPTAR ESTRUCTURA ANEXO B COMO REFERENCIA OFICIAL
✅ **Valores ya validados y coherentes**
✅ **Separación clara CALE-T / CALE-P**
✅ **Totales nacionales correctos**

### 2. DEFINIR MODELO FINANCIERO DE PREDIOS

**Opción A - CAPEX (Compra):**
- Agregar $13.7B/nodo para CALE.n_1
- Total adicional: ~$770B para 56 nodos
- Usar valores Plan v4.1 con predio

**Opción B - OPEX (Arriendo):**
- Mantener valores Anexo B sin predio
- OPEX mensual: +$111M/nodo/año
- Total adicional: ~$6.2B/año para 56 nodos

**Recomendación:** Análisis VPN 20 años para determinar opción óptima.

### 3. ACTUALIZAR FICHAS L3

Las fichas actualmente solo muestran CALE-T. Se recomienda:
- [ ] Agregar sección CALE-P (componente práctico)
- [ ] Mostrar valor unitario total compuesto
- [ ] Indicar claramente si incluye/excluye predio
- [ ] Sincronizar con valores Anexo B oficial

### 4. UNIFICAR PRESENTACIÓN

Todos los documentos deben usar estructura consistente:
```
Categoría: CALE.n_X
├─ Componente Teórico (CALE-T): $XXX M
├─ Componente Práctico (CALE-P): $XX,XXX M
├─ Predio (opcional): $X,XXX M
└─ TOTAL UNITARIO: $XX,XXX M

Cantidad: XX nodos
TOTAL NACIONAL: $XXX,XXX M
```

---

## 📎 REFERENCIAS

**Anexo B Oficial:**
- Sección B10.3: Tabla resumen red nacional
- Valores compuestos finales por categoría
- Total inversión: $851,422,197,892

**Plan v4.1:**
- Sección 7.2: Costos de construcción por clase
- Incluye valorización de predios
- Usado para cálculo alternativo con CAPEX

**Fichas L3:**
- Solo valores CALE-T (componente teórico)
- Pendiente agregar CALE-P
- URL: https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/

---

**Última actualización:** 2025-11-05  
**Estado:** ✅ RECONCILIACIÓN VALIDADA - Anexo B coherente con Plan v4.1 (al excluir predios)
