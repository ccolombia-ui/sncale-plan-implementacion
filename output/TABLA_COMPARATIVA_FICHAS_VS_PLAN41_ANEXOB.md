# 📊 TABLA COMPARATIVA: FICHAS L3 vs PLAN v4.1 vs ANEXO B

## Valores UNITARIOS (por configuración)

| Edificación | VR_Fichas | VR_Plan41 | VR_AnexoB | Notas | Recomendación |
|-------------|-----------|-----------|-----------|-------|---------------|
| **CALE.n_1** | ⚠️ $7.066B<br>(40.8% del esperado) | $17.312B | $17.312B | Ficha **VALIDADA compositivamente**. Diferencia: Plan v4.1 incluye componentes CALE-T ($9.3B) no presentes en ficha actual | ✅ Completar con componentes CALE-T + CALE-P para alcanzar $17.3B |
| **CALE.n_1+** | 🔴 **$0**<br>(no existe) | $22.877B | $22.877B | No existe ficha unitaria separada. Variante de CALE.n_1 con pista Clase II adicional (~$5.56B más) | 📝 Crear **BIM_L3_001b.html** con componente adicional |
| **CALE.n_2** | 🔴 $200M<br>(1.8% del esperado) | $11.206B | $11.206B | Ficha con **datos incompletos** (componentes en $0). Estructura existe pero valores faltantes | 🔧 Corregir **BIM_L3_002.html** desde Anexo B |
| **CALE.n_2**\*\* | 🔴 **$0**<br>(no existe) | $22.088B | $22.088B | No existe ficha unitaria. Variante con 2 pistas Clase I adicionales (~$10.88B más que CALE.n_2) | 📝 Crear **BIM_L3_002b.html** con componentes adicionales |
| **CALE.n_3** | 🔴 **$0**<br>(vacía) | $5.641B | $5.641B | Ficha vacía. Configuración más básica: 1 pista Clase I + sala 4 cubículos + simulador C1 + edificación básica | 🏗️ Generar **BIM_L3_003.html** completa desde estructura base |

---

## Valores NACIONALES (Red completa)

| Edificación | Nodos | VR_Fichas_Nacional | VR_Plan41_Nacional | VR_AnexoB_Nacional | Diferencia |
|-------------|-------|-------------------|-------------------|-------------------|------------|
| CALE.n_1 | 17 | $120.122B | $294.304B | $294.304B | **-$174.182B** (-59.2%) |
| CALE.n_1+ | 3 | $0 | $68.631B | $68.631B | **-$68.631B** (-100%) |
| CALE.n_2 | 4 | $802M | $44.825B | $44.825B | **-$44.023B** (-98.2%) |
| CALE.n_2** | 16 | $0 | $353.401B | $353.401B | **-$353.401B** (-100%) |
| CALE.n_3 | 16 | $0 | $90.261B | $90.261B | **-$90.261B** (-100%) |
| **TOTAL** | **56** | **$120.925B** | **$851.422B** | **$851.422B** | **-$730.498B** (-85.8%) |

---

## 📊 ANÁLISIS DE COBERTURA

### Estado Actual
```
Valor Total Esperado (Plan v4.1):  $851.422.099.891
Valor Total en Fichas:             $120.924.585.988
────────────────────────────────────────────────────
Diferencia:                        $730.497.513.903
Cobertura Actual:                           14.2%
Faltante:                                   85.8%
```

### Desglose por Configuración

| Config | Nodos | Cobertura | Estado | Fichas Unitario | Plan Unitario | Acción |
|--------|-------|-----------|--------|-----------------|---------------|--------|
| CALE.n_1 | 17 | **40.8%** | ⚠️ Parcial | $7.066B | $17.312B | Completar componentes |
| CALE.n_1+ | 3 | **0.0%** | 🔴 No existe | $0 | $22.877B | Crear ficha variante |
| CALE.n_2 | 4 | **1.8%** | 🔴 Incompleta | $200M | $11.206B | Corregir datos |
| CALE.n_2** | 16 | **0.0%** | 🔴 No existe | $0 | $22.088B | Crear ficha variante |
| CALE.n_3 | 16 | **0.0%** | 🔴 Vacía | $0 | $5.641B | Generar completa |

---

## 🎯 RECOMENDACIONES PRIORITARIAS

### 1. ✅ CALE.n_1 (BIM_L3_001) - COMPLETAR
**Estado:** Validada compositivamente pero incompleta  
**Cobertura:** 40.8% ($7.066B de $17.312B esperados)  
**Faltante:** $10.246B

**Componentes presentes:**
- ✅ L2.pista_clase_3: $1.850B
- ✅ L2.pista_clase_2: $980M
- ✅ L2.pista_clase_1: $750M
- ✅ L1.sala_24_cubiculos: $186M
- ✅ L0.simulador_c3 (×2): $900M
- ✅ L2.edificacion_admin: $2.400B
- **SUMA:** $7.066B ✅

**Componentes faltantes (según Plan v4.1):**
- ❌ CALE-T (componente teórico): ~$9.300B
- ❌ Otros componentes menores: ~$946M

**Acción:** Agregar componentes faltantes para llegar a $17.312B

---

### 2. 🔴 CALE.n_2 (BIM_L3_002) - CORREGIR
**Estado:** Datos incompletos (componentes en $0)  
**Cobertura:** 1.8% ($200M de $11.206B esperados)  
**Faltante:** $11.006B

**Problema:** Estructura HTML existe pero valores en $0

**Acción:** Reemplazar con datos reales desde Anexo B o fuente confiable

---

### 3. 🔴 CALE.n_3 (BIM_L3_003) - GENERAR
**Estado:** Vacía  
**Cobertura:** 0% ($0 de $5.641B esperados)  
**Faltante:** $5.641B

**Configuración esperada:**
- 1× Pista Evaluación Clase I: ~$750M
- 1× Sala 4 cubículos: ~$62M
- 1× Simulador C1: ~$250M
- 1× Edificación básica: ~$900M
- CALE-T componente: ~$3.679B

**Acción:** Generar ficha completa desde estructura validada de BIM_L3_001

---

### 4. 📝 VARIANTES - CREAR FICHAS SEPARADAS
**Estado:** No existen  
**Cobertura:** 0%

#### CALE.n_1+ (BIM_L3_001b.html)
- Base: CALE.n_1 ($17.312B)
- **+** Pista Clase II adicional: ~$5.565B
- **TOTAL:** $22.877B
- **Nodos:** 3

#### CALE.n_2** (BIM_L3_002b.html)
- Base: CALE.n_2 ($11.206B)
- **+** 2× Pistas Clase I adicionales: ~$10.881B
- **TOTAL:** $22.088B
- **Nodos:** 16

**Acción:** Crear fichas HTML separadas para variantes con componentes adicionales

---

## 📁 ESTRUCTURA PROPUESTA

```
fichas_l3_unitarias/
├── BIM_L3_001.html         ✅ VALIDADA ($7.066B) → Completar a $17.312B
├── BIM_L3_001b.html        📝 CREAR ($22.877B) - CALE.n_1+
├── BIM_L3_002.html         🔴 CORREGIR ($11.206B) - datos en $0
├── BIM_L3_002b.html        📝 CREAR ($22.088B) - CALE.n_2**
├── BIM_L3_003.html         🔴 GENERAR ($5.641B) - vacía
└── BIM_L3_004.html         ⚠️ REVISAR - estructura diferente
```

---

## 🔄 PRINCIPIO BIM CONFIRMADO

```
┌────────────────────────────────────────────────────┐
│ JERARQUÍA BIM (bottom-up)                         │
├────────────────────────────────────────────────────┤
│ L0: Componentes Atómicos (CAMACOL/SECOP) ✅       │
│ L1: Ensamblajes ✅                                 │
│ L2: Áreas Unifuncionales ✅                        │
│ L3: Edificaciones UNITARIAS ⚠️ (14.2% completo)   │
│ L4: Instancias Municipales (por generar)          │
│ L5: Red Nacional = Σ(L4)                          │
└────────────────────────────────────────────────────┘
```

**Fuente de verdad:** Fichas L0-L3 UNITARIAS  
**Validado:** BIM_L3_001 compositivamente coherente  
**Pendiente:** Completar 85.8% faltante en fichas L3

---

## 📌 NOTAS IMPORTANTES

1. **Plan v4.1 y Anexo B tienen valores idénticos** → Son coherentes entre sí
2. **Fichas actuales tienen solo 14.2%** del valor total → Requieren completar
3. **BIM_L3_001 validada** → Puede usarse como plantilla para las demás
4. **Diferencia principal:** Componentes CALE-T (~$9.3B por CALE.n_1) no presentes en fichas actuales
5. **Variantes (n_1+, n_2**)** → Requieren fichas HTML separadas

---

**Generado:** 2025-11-06  
**Fuente:** scripts/comparar_fichas_plan41_anexoB.py  
**CSV completo:** output/comparacion_fichas_vs_plan41_anexoB.csv
