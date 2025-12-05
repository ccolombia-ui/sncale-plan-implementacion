# CAMBIO 1: RECURSIVIDAD L3→L3 (CALE VARIANTES)
## Separación BASE + VARIANTE con Herencia de Configuraciones

**Fecha:** 2025-11-03  
**Estado:** ✅ **IMPLEMENTANDO**  
**Versión:** 1.0  
**Cambio:** PROMPT_MAESTRO_MODELO_BIM_5D_V2.md - CAMBIO 1

---

## 🎯 OBJETIVO

Modelar **CALE.n_1+** y **CALE.n_2**/** como **BIM independientes** que heredan de sus configuraciones base mediante **recursividad L3→L3**.

---

## 📊 PROBLEMA ACTUAL

Actualmente, las variantes CALE están mezcladas sin estructura clara:

```json
// PROBLEMA: Configuración monolítica sin recursividad
{
  "BIM_L3_001": {
    "nombre": "CALE.n_1 Metropolitano",
    "nodos_aplicables": "20 base + 3 variante+",
    "componentes": [/* todos mezclados */]
    // ❌ No se distingue qué es base vs qué es variante
    // ❌ Duplicación implícita de componentes
    // ❌ No hay herencia explícita
  }
}
```

---

## ✅ SOLUCIÓN PROPUESTA

### **Patrón: HERENCIA_CONFIGURACION**

Separar cada CALE en:
1. **_BASE**: Configuración estándar (20 nodos)
2. **_PLUS / _STAR**: Variante extendida que **HEREDA** de BASE + componentes adicionales

```
L3.CALE.n_1.base (20 nodos)
    ↓ HEREDA
L3.CALE.n_1.plus (3 nodos)
    = BASE + componentes adicionales
```

---

## 📐 ESPECIFICACIÓN TÉCNICA

### **CALE.n_1 (Metropolitano)**

#### **BIM_L3_001_BASE: CALE.n_1 Base**

```json
{
  "bim_id": "BIM_L3_001_BASE",
  "codigo": "L3.CALE.n_1.base",
  "nombre": "CALE.n_1 Metropolitano - Configuración Base",
  "tipo": "CONFIGURACION_BASE",
  "categoria": "METROPOLITANO",
  "nivel_bim": "L3",
  "fase_despliegue": 1,
  
  "nodos_aplicables": 20,
  "ciudades_objetivo": [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Bucaramanga", "Cúcuta", "Pereira", "Santa Marta", "Ibagué",
    "Pasto", "Manizales", "Villavicencio", "Montería", "Valledupar",
    "Neiva", "Armenia", "Popayán", "Sincelejo", "Tunja"
  ],
  
  "componentes_l2": [
    {
      "bim_id": "BIM_L2_003",
      "codigo": "L2.pista_clase_III",
      "nombre": "Pista Clase III Completa",
      "cantidad": 1,
      "valor_unitario": 2093340000,
      "justificacion": "Evaluación práctica categorías A1-C3 (todas)"
    },
    {
      "bim_id": "BIM_L3_010",
      "codigo": "L3.CALE_TEORICO.24q",
      "nombre": "CALE Teórico 24 Cubículos",
      "cantidad": 1,
      "valor_unitario": 645000000,
      "justificacion": "Evaluación teórica máxima capacidad (v2.0 corregido)"
    },
    {
      "bim_id": "BIM_L2_007",
      "codigo": "L2.parqueadero",
      "nombre": "Parqueadero Vehicular",
      "cantidad": 1,
      "valor_unitario": 80000000,
      "justificacion": "Parqueadero propio (no arrendado)"
    }
  ],
  
  "valor_total_capex": 2818340000,
  "capacidad_evaluaciones_mes": 10637,
  "capacidad_evaluaciones_anual": 127644,
  
  "opex_anual_estimado": 680000000,
  "personal_total": 12,
  "area_total_m2": 4150,
  "tiempo_implementacion_meses": 12
}
```

#### **BIM_L3_001_PLUS: CALE.n_1+ Variante**

```json
{
  "bim_id": "BIM_L3_001_PLUS",
  "codigo": "L3.CALE.n_1.plus",
  "nombre": "CALE.n_1+ Metropolitano - Variante Extendida",
  "tipo": "CONFIGURACION_EXTENDIDA",
  "categoria": "METROPOLITANO_PLUS",
  "nivel_bim": "L3",
  "fase_despliegue": 2,
  
  "nodos_aplicables": 3,
  "ciudades_objetivo": [
    "Bogotá (zonas adicionales)",
    "Medellín (zonas adicionales)",
    "Cali (zonas adicionales)"
  ],
  
  "recursividad_l3": {
    "patron": "HERENCIA_CONFIGURACION",
    "referencia_base": "BIM_L3_001_BASE",
    "hereda_todos_componentes": true,
    
    "componentes_adicionales": [
      {
        "bim_id": "BIM_L2_009",
        "codigo": "L2.edificacion_adecuada",
        "nombre": "Edificación Adicional Adecuada",
        "cantidad": 1,
        "valor_unitario": 300000000,
        "justificacion": "Espacio adicional para demanda alta (salas espera, oficinas)"
      },
      {
        "bim_id": "BIM_L2_008",
        "codigo": "L2.datacenter",
        "nombre": "Datacenter Ampliado",
        "cantidad": 1,
        "valor_unitario": 150000000,
        "justificacion": "Mayor capacidad procesamiento para alta demanda"
      },
      {
        "bim_id": "BIM_L3_011",
        "codigo": "L3.CALE_TEORICO.16q",
        "nombre": "CALE Teórico 16 Cubículos Adicional",
        "cantidad": 1,
        "valor_unitario": 460000000,
        "justificacion": "Duplicar capacidad teórica en ciudades grandes"
      }
    ]
  },
  
  "valor_incremental": 910000000,
  "valor_total_capex": 3728340000,
  "nota_capex": "Valor total = BASE ($2,818M) + INCREMENTAL ($910M)",
  
  "capacidad_evaluaciones_mes": 16342,
  "capacidad_evaluaciones_anual": 196104,
  "incremento_capacidad": "53.7% vs base",
  
  "opex_anual_estimado": 960000000,
  "personal_total": 17,
  "area_total_m2": 5000,
  "tiempo_implementacion_meses": 15,
  
  "validaciones": {
    "herencia_base": "✅ Hereda todos los L2 de BIM_L3_001_BASE",
    "componentes_totales": 6,
    "componentes_heredados": 3,
    "componentes_nuevos": 3,
    "ciclos_detectados": 0
  }
}
```

---

### **CALE.n_2 (Intermedio)**

#### **BIM_L3_002_BASE: CALE.n_2 Base**

```json
{
  "bim_id": "BIM_L3_002_BASE",
  "codigo": "L3.CALE.n_2.base",
  "nombre": "CALE.n_2 Intermedio - Configuración Base",
  "tipo": "CONFIGURACION_BASE",
  "categoria": "INTERMEDIO",
  "nivel_bim": "L3",
  "fase_despliegue": 1,
  
  "nodos_aplicables": 20,
  "ciudades_objetivo": [
    "Riohacha", "Quibdó", "Mocoa", "Puerto Carreño", "Mitú",
    "Leticia", "Inírida", "San José del Guaviare", "Arauca", "Yopal",
    "Florencia", "San Andrés", "Tumaco", "Ipiales", "Apartadó",
    "Sogamoso", "Girardot", "Tuluá", "Palmira", "Magangué"
  ],
  
  "componentes_l2": [
    {
      "bim_id": "BIM_L2_002",
      "codigo": "L2.pista_clase_II",
      "nombre": "Pista Clase II Completa",
      "cantidad": 1,
      "valor_unitario": 1407390000,
      "justificacion": "Evaluación práctica categorías A1-C2"
    },
    {
      "bim_id": "BIM_L3_011",
      "codigo": "L3.CALE_TEORICO.16q",
      "nombre": "CALE Teórico 16 Cubículos",
      "cantidad": 1,
      "valor_unitario": 460000000,
      "justificacion": "Evaluación teórica capacidad media (v2.0 corregido)"
    },
    {
      "bim_id": "BIM_L2_007",
      "codigo": "L2.parqueadero",
      "nombre": "Parqueadero Vehicular",
      "cantidad": 1,
      "valor_unitario": 60000000,
      "justificacion": "Parqueadero propio escala intermedia"
    }
  ],
  
  "valor_total_capex": 1927390000,
  "capacidad_evaluaciones_mes": 9145,
  "capacidad_evaluaciones_anual": 109740,
  
  "opex_anual_estimado": 550000000,
  "personal_total": 9,
  "area_total_m2": 3790,
  "tiempo_implementacion_meses": 11
}
```

#### **BIM_L3_002_STAR: CALE.n_2** Variante**

```json
{
  "bim_id": "BIM_L3_002_STAR",
  "codigo": "L3.CALE.n_2.star",
  "nombre": "CALE.n_2** Intermedio - Variante Extendida",
  "tipo": "CONFIGURACION_EXTENDIDA",
  "categoria": "INTERMEDIO_STAR",
  "nivel_bim": "L3",
  "fase_despliegue": 2,
  
  "nodos_aplicables": 16,
  "ciudades_objetivo": [
    "Duitama", "Cartago", "Buga", "Ciénaga", "Maicao",
    "Rionegro", "Turbo", "Bello", "Envigado", "Itagüí",
    "Soledad", "Malambo", "Soacha", "Funza", "Chía",
    "Zipaquirá"
  ],
  
  "recursividad_l3": {
    "patron": "HERENCIA_CONFIGURACION",
    "referencia_base": "BIM_L3_002_BASE",
    "hereda_todos_componentes": true,
    
    "componentes_adicionales": [
      {
        "bim_id": "BIM_L2_001",
        "codigo": "L2.pista_clase_I",
        "nombre": "Pista Clase I Adicional",
        "cantidad": 1,
        "valor_unitario": 721440000,
        "justificacion": "Capacidad adicional para categorías A1/A2 (alta demanda motos)"
      },
      {
        "bim_id": "BIM_L2_005",
        "codigo": "L2.sala_formacion",
        "nombre": "Sala Formación",
        "cantidad": 1,
        "valor_unitario": 30000000,
        "justificacion": "Capacitación continua evaluadores"
      }
    ]
  },
  
  "valor_incremental": 751440000,
  "valor_total_capex": 2678830000,
  "nota_capex": "Valor total = BASE ($1,927M) + INCREMENTAL ($751M)",
  
  "capacidad_evaluaciones_mes": 11225,
  "capacidad_evaluaciones_anual": 134700,
  "incremento_capacidad": "22.7% vs base",
  
  "opex_anual_estimado": 720000000,
  "personal_total": 12,
  "area_total_m2": 4500,
  "tiempo_implementacion_meses": 13,
  
  "validaciones": {
    "herencia_base": "✅ Hereda todos los L2 de BIM_L3_002_BASE",
    "componentes_totales": 5,
    "componentes_heredados": 3,
    "componentes_nuevos": 2,
    "ciclos_detectados": 0
  }
}
```

---

## 📝 VALIDACIONES RECURSIVIDAD L3→L3

### **Reglas de Herencia:**

1. ✅ **Herencia completa**: Variante DEBE heredar TODOS los componentes L2 de la base
2. ✅ **Valor aditivo**: `valor_total = valor_base + valor_incremental`
3. ✅ **Sin ciclos**: No permitir `L3_A → L3_B → L3_A`
4. ✅ **Capacidad agregada**: Capacidad total = capacidad_base + capacidad_adicional
5. ✅ **Personal agregado**: Personal total = personal_base + personal_adicional

### **Función de Resolución:**

```python
def resolver_l3_recursivo(bim_id, tablas_l3, _visitados=None):
    """
    Resuelve recursivamente L3→L3
    Retorna lista de todos los componentes L2 (heredados + nuevos)
    """
    if _visitados is None:
        _visitados = set()
    
    if bim_id in _visitados:
        raise ErrorCicloDetectado(f"Ciclo L3: {bim_id}")
    
    _visitados.add(bim_id)
    
    config = tablas_l3[bim_id]
    componentes_l2 = []
    
    # Si tiene recursividad, resolver base primero
    if 'recursividad_l3' in config:
        base_id = config['recursividad_l3']['referencia_base']
        # RECURSIÓN: Obtener componentes de la base
        componentes_l2.extend(
            resolver_l3_recursivo(base_id, tablas_l3, _visitados)
        )
        # Agregar componentes adicionales
        componentes_l2.extend(
            config['recursividad_l3']['componentes_adicionales']
        )
    else:
        # Base: solo sus componentes directos
        componentes_l2 = config['componentes_l2']
    
    return componentes_l2
```

---

## 📊 RESUMEN CONFIGURACIONES

| Config | BIM ID | Tipo | Nodos | CAPEX | Cap/Mes | Personal |
|--------|--------|------|-------|-------|---------|----------|
| **CALE.n_1 Base** | BIM_L3_001_BASE | BASE | 20 | $2,818M | 10,637 | 12 |
| **CALE.n_1+** | BIM_L3_001_PLUS | EXTENDIDA | 3 | $3,728M | 16,342 | 17 |
| **CALE.n_2 Base** | BIM_L3_002_BASE | BASE | 20 | $1,927M | 9,145 | 9 |
| **CALE.n_2**** | BIM_L3_002_STAR | EXTENDIDA | 16 | $2,679M | 11,225 | 12 |

**Total Fase 1:** 59 nodos CALE = $133,761M CAPEX

---

## 🚀 ARCHIVOS A CREAR

1. ✅ **TABLAS_L3_VARIANTES_RECURSIVAS.json**
   - 4 configuraciones (2 base + 2 extendidas)
   - Campo `recursividad_l3`
   - Validaciones integridad

2. ✅ **funciones_recursividad_l3.py**
   - `resolver_l3_recursivo()`
   - `validar_herencia_l3()`
   - `calcular_totales_agregados()`

3. ✅ **generar_fichas_l3_variantes.py**
   - Regenerar 4 fichas HTML
   - Sección "Recursividad L3→L3"
   - Visualización herencia base→extendida

4. ✅ **REPORTE_IMPLEMENTACION_CAMBIO_1.md**
   - Documentación completa
   - Validaciones ejecutadas
   - Próximos pasos

---

## ✅ ENTREGABLES

- [x] Especificación técnica CAMBIO 1 (este archivo)
- [ ] JSON con 4 configuraciones L3
- [ ] Script Python recursividad L3
- [ ] 4 fichas HTML regeneradas
- [ ] Reporte implementación

---

**Autor:** Modelo BIM 5D SNCALE  
**Fecha:** 2025-11-03  
**Estado:** Especificación completa - Listo para implementar
