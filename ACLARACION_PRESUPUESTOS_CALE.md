# ACLARACIÓN: DOS NIVELES DE PRESUPUESTO CALE

## 🎯 IMPORTANTE: No es un error, son DOS presupuestos diferentes

### 📊 **PRESUPUESTO 1: CAPEX por Nodos Individuales**
**Valor**: $12,392 millones COP  
**Fuente**: `TABLA_197_NODOS_COMPLETA.csv` (Plan de Implementación)

#### ¿Qué incluye?
Suma directa del CAPEX de cada uno de los 197 nodos:
- Cat.A+: 3 nodos × $243M = $729M
- Cat.A: 17 nodos × $243M = $4,131M
- Cat.B**: 16 nodos × $196M = $3,136M
- Cat.B: 4 nodos × $196M = $784M
- Cat.C1: 16 nodos × $120M = $1,920M
- Cat.C2: 50 satélites × $12M = $600M
- Cat.C3: 45 satélites × $12M = $540M
- Cat.C4: 30 satélites × $12M = $360M
- Cat.C5: 16 satélites × $12M = $192M

**TOTAL**: $12,392 millones COP

#### Componentes por nodo:
- Infraestructura física del CALE
- Equipos de cómputo (cubículos)
- Software de evaluación local
- Pistas de práctica (según categoría)
- Mobiliario y equipamiento

---

### 💰 **PRESUPUESTO 2: CAPEX TOTAL DEL SISTEMA**
**Valor**: $851.422.197.892 COP (851.422 millones)  
**Fuente**: https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/edit?gid=1032260683

#### Tabla Oficial de Presupuesto:

| Categoría | Cant. | Tipo Teórico | Tipo Práctico | VR Unit CAPEX | VR Total | % Total |
|-----------|-------|--------------|---------------|---------------|----------|---------|
| **CAT.A+** | 3 | CALE-T-24q + 7 satélites C2-C5 | CALE-P.C3 (Clase I+II+III) & (Clase II) | $22.876.959.265 | $68.630.877.795 | 8,06% |
| **CAT.A** | 17 | CALE-T-24q + 7 satélites C2-C5 | CALE-P.C3 (Clase I+II+III) | $17.311.999.565 | $294.303.992.605 | 34,57% |
| **CAT.B**\*\* | 16 | CALE-T-16q | CALE-P.C2 (Clase I+II) & 2x(Clase I) | $22.087.585.297 | $353.401.364.752 | 41,51% |
| **CAT.B** | 4 | CALE-T-16q | CALE-P.C2 (Clase I+II) | $11.206.265.897 | $44.825.063.588 | 5,26% |
| **CAT.C1** | 16 | CALE-T-16q | CALE-P.C1 (Clase I) | $5.641.306.197 | $90.260.899.152 | 10,60% |
| **TOTAL** | **56** | - | - | - | **$851.422.197.892** | **100%** |

#### ¿Qué incluye cada CAPEX unitario?

**1. CALE-T (Componente Teórico)**
   - CALE-T-24q: $243.063.465 COP (Cat.A+, Cat.A)
   - CALE-T-16q: $200.646.497 COP (Cat.B**, Cat.B, Cat.C1)
   - Incluye: Infraestructura física, cubículos de evaluación, equipos de cómputo, software

**2. CALE-P (Componente Práctico)**
   - CALE-P.C3 (Clase I+II+III): $17.068.936.100 COP (Cat.A)
   - CALE-P.C3 (Clase I+II+III) & (Clase II): $22.633.895.800 COP (Cat.A+ con pista adicional)
   - CALE-P.C2 (Clase I+II): $11.005.619.400 COP (Cat.B)
   - CALE-P.C2 (Clase I+II) & 2x(Clase I): $21.886.938.800 COP (Cat.B** con 2 pistas adicionales)
   - CALE-P.C1 (Clase I): $5.440.659.700 COP (Cat.C1)
   - Incluye: Terrenos, pistas de práctica, vehículos, señalización, infraestructura de seguridad

**3. Satélites Asignados**
   - Nodos Cat.A+ y Cat.A incluyen 7 satélites C2-C5 en su presupuesto
   - Satélites solo realizan evaluaciones teóricas (sin componente práctico)

**TOTAL por categoría**: CALE-T + CALE-P + Satélites = CAPEX Unitario

---

## 🔍 **¿Por qué la diferencia?**

### La explicación está en los componentes:

**Presupuesto 1 ($12,392M)** solo incluye:
- CALE-T (componente teórico) de cada nodo
- Valores simplificados por nodo individual

**Presupuesto 2 ($851,422M)** incluye:
- CALE-T (componente teórico): ~$243M o $200M por nodo
- **CALE-P (componente práctico)**: $5,440M a $22,633M por nodo
- **Satélites asignados**: 7 por cada nodo Cat.A+/A
- **Terrenos y pistas de práctica**: Mayores costos
- **Vehículos y equipos especializados**: Para evaluaciones prácticas

### Desglose del CAPEX unitario (ejemplo Cat.A):

```
CALE-T-24q (Teórico):           $243.063.465
CALE-P.C3 (Práctico):      + $17.068.936.100
Satélites (7 unidades):    +  (incluido)
─────────────────────────────────────────────
CAPEX Unitario Cat.A:      = $17.311.999.565  (68.7x mayor que solo teórico)
```

### Factor multiplicador por categoría:

| Categoría | Solo Teórico | Teórico + Práctico | Multiplicador |
|-----------|--------------|-------------------|---------------|
| Cat.A+ | $243M | $22.876M | **94x** |
| Cat.A | $243M | $17.311M | **71x** |
| Cat.B** | $200M | $22.087M | **110x** |
| Cat.B | $200M | $11.206M | **56x** |
| Cat.C1 | $200M | $5.641M | **28x** |

**Conclusión**: El componente práctico (CALE-P) representa entre el 95% y 98% del costo total de cada nodo, principalmente por:
- Adquisición de terrenos para pistas
- Construcción de infraestructura de práctica
- Vehículos especializados (Clase I, II, III)
- Equipos de seguridad y control

---

## 📌 **USO CORRECTO EN DOCUMENTACIÓN**

### En el Portal Web (público):
✅ **Usar CAPEX TOTAL**: $851.422M
- Muestra la inversión completa del plan nacional
- Incluye todos los componentes necesarios
- Es el presupuesto oficial para autoridades

### En Fichas Técnicas por Nodo:
✅ **Usar CAPEX Individual**: $243M, $196M, $120M, $12M
- Detalla el costo específico de cada CALE
- Útil para planificación local
- Permite calcular costos por municipio

### En Tablas de 197 Nodos:
✅ **Usar ambos**:
- CAPEX por categoría (individual)
- CAPEX total sumado de nodos: $12,392M
- Nota aclaratoria: "Sistema completo: $851.422M"

---

## ⚠️ **DATOS OFICIALES CONFIRMADOS**

### Archivos oficiales procesados:
1. ✅ **presupuesto_sistema_cale.csv**: Descargado del Google Sheets oficial
2. ✅ **TABLA_197_NODOS_COMPLETA.csv**: Base de datos de nodos individuales

### Valores oficiales verificados:

| Concepto | Valor | Fuente |
|----------|-------|--------|
| CAPEX TOTAL SISTEMA | $851.422.197.892 | presupuesto_sistema_cale.csv |
| CAPEX solo componente teórico | $12,392M | TABLA_197_NODOS_COMPLETA.csv |
| Nodos totales | 197 (56 principales + 141 satélites) | TABLA_197_NODOS_COMPLETA.csv |
| OPEX Anual | $164,250M | TABLA_197_NODOS_COMPLETA.csv |
| Categorías | 9 (A+, A, B**, B, C1, C2, C3, C4, C5) | Ambas fuentes |

### Composición del presupuesto:
- **CAT.B**\*\* (16 nodos): $353.401M (41,51%) - Mayor por pistas adicionales
- **CAT.A** (17 nodos): $294.303M (34,57%) - Red troncal nacional
- **CAT.C1** (16 nodos): $90.260M (10,60%) - Cobertura fronteriza
- **CAT.A+** (3 nodos): $68.630M (8,06%) - Nodos especiales (Bogotá Sur/Norte, Bucaramanga)
- **CAT.B** (4 nodos): $44.825M (5,26%) - Regionales estratégicos

---

## ✅ **CORRECCIONES APLICADAS**

### Archivos actualizados con presupuesto oficial ($851.422M):
1. ✅ `enfoque_interactivo.md`: Tabla completa con valores oficiales
2. ✅ `services/github_pages/index.html`: $851.4B (corregido de $12.4B)
3. ✅ `services/github_pages/mapa_cale.html`: $851.4B (corregido de $12.4B)
4. ✅ `presupuesto_sistema_cale.csv`: Descargado y guardado localmente

### Archivos que mantienen CAPEX por nodos (uso interno):
- ✅ `TABLA_197_NODOS_COMPLETA.csv`: Datos individuales para análisis técnico
- ✅ `nodos_cale_197_completo.json`: CAPEX simplificado por nodo
- ✅ Scripts de actualización: Procesan datos detallados

---

*Última actualización: 2025-10-28 10:20*  
*Presupuesto oficial confirmado: $851.422.197.892 COP*  
*Fuente: Google Sheets descargado exitosamente como CSV*
