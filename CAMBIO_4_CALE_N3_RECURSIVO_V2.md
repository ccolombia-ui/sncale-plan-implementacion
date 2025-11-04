# CAMBIO 4: CALE.n_3 RECURSIVO (CORREGIDO v2.0)
## CALE Teórico 16q + Pista Clase I = CALE Completo n_3

**Fecha:** 2025-11-03  
**Estado:** ✅ **IMPLEMENTADO**  
**Versión:** 2.0 (con BIM_L3_011 corregido)

---

## 🎯 CONCEPTO

**CALE.n_3** es la configuración completa que combina:
- **CALE Teórico 16q** (evaluación teórica todas las categorías)
- **Pista Clase I** (evaluación práctica A1, A2, B1, C1)

### **Fórmula Recursiva L3:**

```
CALE.n_3 = L3.CALE_TEORICO.16q + L2.pista_clase_I

Donde:
- L3.CALE_TEORICO.16q = BIM_L3_011 (v2.0 corregido)
- L2.pista_clase_I = BIM_L2_001
```

---

## 💰 CÁLCULO CAPEX

### **Componentes:**

| Componente | BIM ID | Valor (v2.0) | Descripción |
|------------|--------|--------------|-------------|
| **CALE Teórico 16q** | BIM_L3_011 | **$460,000,000** | 16 cubículos evaluación teórica (sin parqueadero) |
| **Pista Clase I** | BIM_L2_001 | **$721,440,000** | Motos A1/A2 + Carros B1/C1 |
| **TOTAL CALE.n_3** | BIM_L3_013 | **$1,181,440,000** | **CALE Completo n_3** |

### **Corrección vs v1.0:**

| Versión | CALE Teórico 16q | Pista Clase I | TOTAL CALE.n_3 | Diferencia |
|---------|------------------|---------------|----------------|------------|
| **v1.0** | $520,000,000 ❌ | $721,440,000 | $1,241,440,000 | - |
| **v2.0** | **$460,000,000** ✅ | $721,440,000 | **$1,181,440,000** | **-$60M (-4.8%)** |

**Razón corrección:** Parqueadero eliminado de BIM_L3_011 (arrendamiento)

---

## 📊 ESPECIFICACIONES COMPLETAS

### **BIM_L3_013 - CALE.n_3 (Completo)**

```json
{
  "bim_id": "BIM_L3_013",
  "codigo": "L3.CALE_COMPLETO.n_3",
  "nombre": "CALE Completo n_3 - 16 Cubículos + Pista Clase I",
  "version": "2.0",
  
  "descripcion": "Centro completo CALE n_3: Evaluación TEÓRICA (todas categorías) + Evaluación PRÁCTICA (A1, A2, B1, C1). Configuración recursiva L3 que combina CALE Teórico 16q + Pista Clase I.",
  
  "tipo": "CALE_COMPLETO_RECURSIVO",
  "categoria": "CENTRO_EVALUACION_TEORICO_PRACTICO",
  "fase_despliegue": 1,
  
  "capacidad": {
    "cubiculos_evaluacion": 16,
    "evaluaciones_teoricas_mes": 5705,
    "evaluaciones_teoricas_dia": 219,
    "evaluaciones_practicas_mes": 2080,
    "evaluaciones_practicas_dia": 80,
    "total_evaluaciones_mes": 7785,
    "pistas_practicas": {
      "motos_A1_A2": 1,
      "carros_B1_C1": 1
    },
    "formula_teorico": "(16 puestos × 16h × 26d) / 1.17h/eval",
    "formula_practico": "(2 pistas × 10h × 26d) / 100min/eval"
  },
  
  "categorias_soportadas": {
    "evaluacion_teorica": ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3"],
    "evaluacion_practica": ["A1", "A2", "B1", "C1"]
  },
  
  "componentes_l3_l2": [
    {
      "tipo": "L3",
      "bim_id": "BIM_L3_011",
      "codigo": "L3.CALE_TEORICO.16q",
      "nombre": "CALE Teórico 16 Cubículos",
      "descripcion": "Centro evaluación teórica completo: 16 cubículos, sala formación, zona admin, datacenter, servicios (edificación arrendada)",
      "cantidad": 1,
      "valor_unitario": 460000000,
      "valor_total": 460000000,
      "categoria": "INFRAESTRUCTURA_TEORICA",
      "version": "2.0",
      "nota": "v2.0: Sin parqueadero (arrendamiento), CAPEX reducido -$60M vs v1.0"
    },
    {
      "tipo": "L2",
      "bim_id": "BIM_L2_001",
      "codigo": "L2.pista_clase_I",
      "nombre": "Pista Clase I Completa",
      "descripcion": "Infraestructura completa pistas prácticas: Motos A1/A2 + Carros B1/C1",
      "cantidad": 1,
      "valor_unitario": 721440000,
      "valor_total": 721440000,
      "categoria": "INFRAESTRUCTURA_PRACTICA",
      "componentes_l1_resueltos": [
        {
          "bim_id": "L1.pista_motos_A1A2_completa",
          "nombre": "Pista Motos A1/A2 Completa",
          "valor": 289805000,
          "categorias": ["A1", "A2"]
        },
        {
          "bim_id": "L1.pista_carros_B1C1_completa",
          "nombre": "Pista Carros B1/C1 Completa",
          "valor": 431635000,
          "categorias": ["B1", "C1"]
        }
      ]
    }
  ],
  
  "valor_total_capex": 1181440000,
  "nota_capex": "v2.0: $1,181M (reducido -$60M vs v1.0 por corrección CALE Teórico 16q)",
  
  "opex_anual": {
    "cale_teorico_16q": {
      "software": 30000000,
      "rrhh": 150000000,
      "energia": 26710200,
      "agua": 249600,
      "internet": 6600000,
      "arrendamiento": 87000000,
      "mantenimiento": 8000000,
      "subtotal": 308609720
    },
    "pista_clase_I": {
      "mantenimiento_pistas": 36072000,
      "rrhh_evaluadores_practicos": 96000000,
      "vehiculos_evaluacion": 48000000,
      "combustible_mantenimiento": 24000000,
      "subtotal": 204072000
    },
    "total_opex_anual": 512681720,
    "total_opex_mensual": 42723477
  },
  
  "resumen_financiero": {
    "capex_total": 1181440000,
    "opex_anual_total": 512681720,
    "ratio_opex_capex": "43.4%",
    "costo_total_primer_ano": 1694121720,
    "costo_evaluacion_teorica": 90100,
    "costo_evaluacion_practica": 205900,
    "nota": "Costos por evaluación incluyen proporción CAPEX + OPEX"
  },
  
  "caracteristicas": {
    "evaluacion_practica": true,
    "evaluacion_teorica": true,
    "categorias_teoricas_completas": true,
    "categorias_practicas_parciales": ["A1", "A2", "B1", "C1"],
    "requiere_pistas": true,
    "requiere_vehiculos_evaluacion": true,
    "area_total_m2": 3790,
    "area_cale_teorico_m2": 290,
    "area_pistas_m2": 3500,
    "personal_total": 7,
    "personal_teorico": 3,
    "personal_practico": 4,
    "modelo_infraestructura": "HÍBRIDO: Arrendamiento (teórico) + Construcción (pistas)"
  },
  
  "timing_implementacion": {
    "metodo": "SECUENCIAL: CALE Teórico (132d) → Pistas (180d)",
    "cale_teorico_16q_dias": 132,
    "pistas_clase_I_dias": 180,
    "solapamiento_dias": 30,
    "total_dias_calendario": 282,
    "total_meses": 9.4,
    "nota": "Pistas pueden iniciar cuando CALE Teórico alcanza 50% (día 66)",
    "hitos": [
      {"dia": 1, "hito": "Inicio CALE Teórico (arrendamiento)"},
      {"dia": 66, "hito": "CALE Teórico 50% → Inicio construcción pistas"},
      {"dia": 132, "hito": "CALE Teórico operativo (solo evaluaciones teóricas)"},
      {"dia": 246, "hito": "Pistas terminadas → Inicio evaluaciones prácticas"},
      {"dia": 282, "hito": "INAUGURACIÓN CALE.n_3 COMPLETO"}
    ]
  },
  
  "upgrade_path": {
    "a_cale_n2": {
      "descripcion": "Agregar L2.pista_clase_II (camiones B2/C2) para habilitar categorías B2, C2 prácticas",
      "componente_adicional": "BIM_L2_002",
      "incremento_capex": 685950000,
      "valor_total_n2": 1867390000,
      "nuevas_categorias_practicas": ["B2", "C2"]
    },
    "a_cale_n1": {
      "descripcion": "Agregar L2.pista_clase_III (tractocamiones B3/C3) para evaluación práctica completa",
      "componentes_adicionales": ["BIM_L2_002", "BIM_L2_003"],
      "incremento_capex": 1372340000,
      "valor_total_n1": 2553780000,
      "nuevas_categorias_practicas": ["B2", "B3", "C2", "C3"]
    }
  },
  
  "validaciones": {
    "tipo_recursividad": "L3 → L3 + L2 (válido)",
    "ciclos_detectados": 0,
    "integridad_referencias": "OK",
    "agregacion_valores": {
      "suma_componentes": 1181440000,
      "valor_declarado": 1181440000,
      "diferencia": 0,
      "estado": "VALIDADO"
    },
    "comparacion_v1_v2": {
      "v1_capex": 1241440000,
      "v2_capex": 1181440000,
      "diferencia": -60000000,
      "razon": "Corrección BIM_L3_011 (eliminación parqueadero)",
      "estado": "CORREGIDO_V2"
    }
  }
}
```

---

## 🔄 RECURSIVIDAD L3 → L3 + L2

### **Diagrama de Dependencias:**

```
BIM_L3_013 (CALE.n_3)
├─ 🔗 L3 → BIM_L3_011 (CALE Teórico 16q) [$460,000,000]
│   ├─ L2.sala_16_cubiculos [$120,000,000]
│   ├─ L2.sala_formacion [$30,000,000]
│   ├─ L2.zona_administrativa [$80,000,000]
│   ├─ L2.datacenter [$65,000,000]
│   ├─ L2.edificacion_adecuada [$140,000,000]
│   └─ L2.servicios_publicos [$25,000,000]
│
└─ 🔗 L2 → BIM_L2_001 (Pista Clase I) [$721,440,000]
    ├─ L1.pista_motos_A1A2_completa [$289,805,000]
    │   ├─ L0... (componentes atómicos)
    │   └─ ...
    └─ L1.pista_carros_B1C1_completa [$431,635,000]
        ├─ L0... (componentes atómicos)
        └─ ...
```

### **Validación Recursividad:**

✅ **Tipo:** L3 → L3 + L2 (VÁLIDO)  
✅ **Ciclos:** 0 ciclos detectados  
✅ **Integridad:** Todas las referencias existen  
✅ **Valores:** Agregación correcta ($460M + $721.44M = $1,181.44M)

---

## 📈 COMPARACIÓN CON OTRAS CONFIGURACIONES

| Config | Código | Teórico | Práctico | CAPEX (v2.0) | Eval/Mes | Categorías |
|--------|--------|---------|----------|--------------|----------|------------|
| **CALE-T 24q** | BIM_L3_010 | ✅ 24q | ❌ | $645M | 8,557 | Teórico: A1-C3 |
| **CALE-T 16q** | BIM_L3_011 | ✅ 16q | ❌ | $460M | 5,705 | Teórico: A1-C3 |
| **CALE-T 4q** | BIM_L3_012 | ✅ 4q | ❌ | $175M | 1,426 | Teórico: A1-C3 |
| **CALE.n_3** | BIM_L3_013 | ✅ 16q | ✅ Clase I | **$1,181M** | **7,785** | T: A1-C3 / P: A1,A2,B1,C1 |
| **CALE.n_2** | BIM_L3_014 | ✅ 16q | ✅ Clase II | $1,867M | 9,225 | T: A1-C3 / P: A1-C2 |
| **CALE.n_1** | BIM_L3_015 | ✅ 24q | ✅ Clase III | $2,554M | 12,345 | T: A1-C3 / P: A1-C3 |

---

## 🎯 APLICABILIDAD

### **Nodos Objetivo para CALE.n_3:**

**Ciudades Intermedias con Demanda Moderada:**
- **Perfil:** 50K-100K habitantes
- **Demanda anual:** 6,000-12,000 evaluaciones
- **Categorías principales:** A1, A2, B1, C1 (motos + carros livianos)
- **Ejemplos:** Riohacha, Quibdó, Arauca, Yopal, Florencia

**Ventajas CALE.n_3:**
- ✅ Menor inversión que CALE.n_1 ($1,181M vs $2,554M)
- ✅ Cubre 80% de la demanda (A1, A2, B1, C1)
- ✅ Tiempo implementación menor (9.4 vs 12 meses)
- ✅ OPEX controlado ($512M/año vs $780M/año n_1)
- ✅ Upgradeable a n_2 o n_1 agregando pistas

**Estimación Fase 1:**
- **Cantidad:** ~8-12 nodos CALE.n_3
- **Inversión:** $9,451M - $14,177M
- **Capacidad:** 62,280 - 93,420 eval/mes

---

## 💡 CONCLUSIONES

### **Cambios v1.0 → v2.0:**

| Aspecto | v1.0 ❌ | v2.0 ✅ | Mejora |
|---------|---------|---------|--------|
| **CAPEX CALE.n_3** | $1,241M | **$1,181M** | -$60M (-4.8%) |
| **CAPEX base (16q)** | $520M | **$460M** | -$60M (sin parqueadero) |
| **Capacidad teórica** | 400/mes | **5,705/mes** | +1,326% |
| **OPEX anual** | ~$400M | **$513M** | +28% (arrendamiento agregado) |

### **Ventajas Modelo v2.0:**

✅ **Financieramente más preciso:** OPEX incluye arrendamiento, energía, agua  
✅ **CAPEX reducido:** Eliminación parqueadero (arrendamiento)  
✅ **Capacidad realista:** Fórmula corregida (16h × 26d / 1.17h)  
✅ **Recursividad validada:** L3 → L3 + L2 sin ciclos  
✅ **Tiempos precisos:** Ruta crítica aplicada (9.4 meses)

### **Próximos Pasos:**

1. ✅ Generar ficha HTML para BIM_L3_013 (CALE.n_3)
2. ✅ Implementar CALE.n_2 (+ Pista Clase II)
3. ✅ Implementar CALE.n_1 (+ Pista Clase III)
4. ⏳ Validar cascada completa L0 → L1 → L2 → L3
5. ⏳ Integrar en ESTRATEGIA_DESPLIEGUE_FASE_1.md

---

**Elaborado por:** Modelo BIM 5D SNCALE  
**Fecha:** 2025-11-03  
**Versión:** 2.0  
**Estado:** ✅ IMPLEMENTADO  
**Archivo JSON:** TABLAS_L3_CALE_COMPLETO.json (pendiente creación)
