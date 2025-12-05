# 📊 TABLA RESUMEN: CALE.n_1 - Análisis Detallado

## Edificación: CALE.n_1 - Centro Metropolitano

---

### 🔧 Componentes en Ficha L3 Actual (valores en millones de pesos)

| # | Componente | Referencia BIM | Valor Unitario | Cant | Valor Total |
|---|------------|----------------|----------------|------|-------------|
| 1 | Pista Evaluación Clase III | `L2.pista_clase_3` | $1.850 M | 1 | $1.850 M |
| 2 | Pista Evaluación Clase II | `L2.pista_clase_2` | $980 M | 1 | $980 M |
| 3 | Pista Evaluación Clase I | `L2.pista_clase_1` | $750 M | 1 | $750 M |
| 4 | Sala Evaluación Teórica (24 cubículos) | `L1.sala_24_cubiculos` | $186 M | 1 | $186 M |
| 5 | Simulador Conducción Clase III | `L0.simulador_c3` | $450 M | 2 | $900 M |
| 6 | Infraestructura Civil Base | `L2.edificacion_admin` | $2.400 M | 1 | $2.400 M |
| **TOTAL FICHA** | | | | | **$7.066 M** |

---

### 💰 Comparación de Valores (valores unitarios, en millones)

| Fuente | VR_Fichas | VR_Plan41 | VR_AnexoB | Diferencia | Cobertura |
|--------|-----------|-----------|-----------|------------|-----------|
| **CALE.n_1** | **$7.066 M** | ~~$30.805 M~~ → $17.312 M | **$17.312 M** | -$10.246 M | **40.8%** |

**Notas:**
- ✅ Anexo B: $17.312 M (SIN predio)
- ⚠️ Plan v4.1 original: $30.805 M (INCLUÍA predio $4.895 M - **descartado**)
- ✅ Plan v4.1 corregido: $17.312 M (sin predio, coincide con Anexo B)

---

### 📊 Desglose de Valores Anexo B

**Componente Teórico (CALE-T):**
- Valor: $243 M
- Incluye: Infraestructura tecnológica, sistemas de gestión, certificaciones ISO, seguros

**Componente Práctico (CALE-P):**
- Anexo B: $17.069 M
- Ficha actual: $7.066 M
- Diferencia: -$10.003 M (58.6% faltante en componente práctico)

**TOTAL Anexo B:**
- CALE-T + CALE-P = $243 M + $17.069 M = **$17.312 M**

---

### 📝 Notas

1. **Ficha actual ($7.066 M):**
   - ✅ Compositivamente COHERENTE: Σ(L2) + Σ(L1) + Σ(L0) = $7.066 M
   - ✅ Validada matemáticamente (suma de componentes = total declarado)
   - ❌ INCOMPLETA: Solo cubre 40.8% del valor esperado

2. **Componentes PRESENTES en ficha:**
   - Pistas evaluación (I, II, III): $3.580 M (50.7% de la ficha)
   - Edificación administrativa: $2.400 M (34.0%)
   - Simuladores C3 (2 unidades): $900 M (12.7%)
   - Sala teórica 24q: $186 M (2.6%)

3. **Componentes FALTANTES:**
   - ❌ CALE-T (componente teórico completo): $243 M
   - ❌ Diferencia en CALE-P: $10.003 M
     * Posibles componentes adicionales L2 no detallados en ficha
     * Equipamiento complementario, señalización, tecnología adicional

4. **Predio (terreno):**
   - ⚠️ Plan v4.1 incluía: $4.895 M por nodo
   - ✅ Anexo B NO incluye predio (correcto)
   - 📌 Decisión: **NO incluir en ficha L3** (el predio es costo L4 municipal, no L3 unitario)

5. **Coherencia Plan v4.1 vs Anexo B:**
   - Con predio: $30.805 M (Plan v4.1) vs $17.312 M (Anexo B) → **56.2% diferencia**
   - Sin predio: $25.910 M (Plan v4.1) vs $17.312 M (Anexo B) → **49.7% diferencia AÚN PERSISTE**
   - ⚠️ Existe diferencia adicional de $8.598 M por investigar

---

### 🎯 Recomendación

**ACCIÓN INMEDIATA:**

1. **Agregar componente CALE-T ($243 M):**
   - Crear nueva fila en tabla de componentes de BIM_L3_001.html
   - Referencia BIM: `L2.cale_teorico_24q`
   - Descripción: "Infraestructura tecnológica, gestión, certificaciones ISO, seguros"

2. **Investigar diferencia en CALE-P ($10.003 M):**
   - Revisar Anexo B completo para identificar componentes L2/L1/L0 adicionales
   - Posibles faltantes:
     * Señalización vertical/horizontal completa
     * Equipamiento tecnológico adicional (cámaras, sistemas control)
     * Mobiliario administrativo
     * Instalaciones eléctricas/hidráulicas detalladas
     * Áreas verdes, parqueaderos, cerramiento perimetral

3. **Objetivo L3 unitario:**
   - Valor actual ficha: $7.066 M
   - Valor objetivo Anexo B: $17.312 M
   - Por agregar: $10.246 M (59.2% faltante)

4. **NO incluir:**
   - ❌ Predio (terreno): Es costo L4 (instancia municipal), no L3 (edificación unitaria)
   - ✅ Ficha L3 = solo componentes constructivos y equipamiento, SIN terreno

---

### 📌 Conclusión

| Concepto | Valor | Estado |
|----------|-------|--------|
| **Ficha L3 actual** | $7.066 M | ✅ Validada compositivamente, ❌ Incompleta (40.8%) |
| **Anexo B esperado** | $17.312 M | ✅ Valor objetivo (sin predio) |
| **Faltante** | $10.246 M | 🔴 Por agregar (59.2%) |
| **Predio Plan v4.1** | $4.895 M | ❌ NO incluir en L3 (es L4) |

**Estado:** ⚠️ FICHA PARCIALMENTE COMPLETA - Requiere agregar $10.246 M en componentes faltantes

**Próximo paso:** Revisar Anexo B sección B20, B30, B40, B50, B60, B70 para identificar todos los componentes L2/L1/L0 que conforman CALE-P completo
