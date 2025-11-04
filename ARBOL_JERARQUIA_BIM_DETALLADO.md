# 🌳 ÁRBOL JERARQUÍA BIM COMPLETO - SNCALE

**Fuente Única:** Google Doc MUNAY_5.2__anexo_b__DEFINITIVO  
**Doc ID:** `16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE`  
**Fecha:** 3 de noviembre de 2025

---

## 📊 Resumen Estadístico

| Nivel | Cantidad | Descripción | Valorización Total |
|-------|----------|-------------|-------------------|
| **L3** | 4 configs | Configuraciones CALE (n_1, n_2, n_3, Satélites) | $145.332.930.021 COP |
| **L2** | 5 configs | Pistas Clase I/II/III + CALE Teóricos 24q/16q | $3.948.709.962 COP |
| **L1** | 29 componentes | Maniobras (0-19) + Infraestructura | N/A (componentes) |
| **L0** | 6 componentes base | Pavimentos, Señalización, Simuladores | N/A (componentes base) |

**Valorización Total Sistema:** $149.281.639.983 COP

---

## 🌲 Árbol de Jerarquía Detallado

### Leyenda
- 📦 **L3:** Configuración CALE completa (centro de enseñanza)
- 🏗️ **L2:** Configuración de pista o edificación
- 🔧 **L1:** Maniobra o componente funcional
- ⚙️ **L0:** Componente base (pavimento, señalización, etc.)

---

## 1️⃣ BIM_L3_001 - CALE.n_1 - Centro Metropolitano

```
📦 L3: BIM_L3_001
   Título: CALE.n_1 - Centro Metropolitano
   Valorización: $141.320.000.000 COP
   Nodos: 20 base + 3 variante+
   Fuente: Tabla #3
   
   Componentes directos (desde tabla #3):
   ├─ 🏗️ L2.pista_clase_3 (Pista Evaluación Clase III) - $37B
   ├─ 🏗️ L2.pista_clase_2 (Pista Evaluación Clase II) - $19.6B
   ├─ 🏗️ L2.pista_clase_1 (Pista Evaluación Clase I) - $15B
   ├─ 🔧 L1.sala_24_cubiculos (Sala Teórica 24q) - $3.72B
   ├─ ⚙️ L0.simulador_c3 (Simulador Clase III) - $18B
   └─ 🏗️ L2.edificacion_admin (Infraestructura Civil) - $48B
```

**Desglose L2 → L1 → L0:**

```
   └─ 🏗️ L2.pista_clase_3 (Pista Clase III) - $1.850.000.000/unidad
       ├─ 🔧 L1.maniobra_17 (Maniobras vehículos pesados)
       ├─ 🔧 L1.maniobra_18 (Reversa vehículo articulado)
       ├─ 🔧 L1.maniobra_19 (Maniobras espacio reducido)
       ├─ ⚙️ L0.pavimento_especial (Concreto Fc=35MPa)
       ├─ ⚙️ L0.señalizacion (Horizontal y vertical)
       └─ 📎 Incluye: L2.pista_clase_II + L2.pista_clase_I

   └─ 🏗️ L2.pista_clase_2 (Pista Clase II) - $980.000.000/unidad
       ├─ 🔧 L1.maniobra_14 (Maniobras con remolque)
       ├─ 🔧 L1.maniobra_15 (Reversa con remolque)
       ├─ 🔧 L1.maniobra_16 (Estacionamiento con remolque)
       ├─ ⚙️ L0.pavimento_reforzado (Concreto reforzado)
       ├─ ⚙️ L0.señalizacion
       └─ 📎 Incluye: L2.pista_clase_I

   └─ 🏗️ L2.pista_clase_1 (Pista Clase I) - $750.000.000/unidad
       ├─ 🔧 L1.maniobra_00 (Arranque en pendiente)
       ├─ 🔧 L1.maniobra_01 (Estacionamiento en paralelo)
       ├─ 🔧 L1.maniobra_02 (Estacionamiento en batería)
       ├─ 🔧 L1.maniobra_03 (Cambio de carril)
       ├─ 🔧 L1.maniobra_04 (Giro a la derecha)
       ├─ 🔧 L1.maniobra_05 (Giro a la izquierda)
       ├─ 🔧 L1.maniobra_06 (Giro en U)
       ├─ 🔧 L1.maniobra_07 (Paso por glorieta)
       ├─ 🔧 L1.maniobra_08 (Frenado de emergencia)
       ├─ 🔧 L1.maniobra_09 (Reversa controlada)
       ├─ 🔧 L1.maniobra_10 (Estacionamiento en línea)
       ├─ 🔧 L1.maniobra_11 (Slalom simple)
       ├─ 🔧 L1.maniobra_12 (Paso por intersección)
       ├─ 🔧 L1.maniobra_13 (Conducción en recta)
       ├─ ⚙️ L0.pavimento_flexible (Asfalto estándar)
       └─ ⚙️ L0.señalizacion
```

**Ficha:** [BIM_L3_001.html](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/BIM_L3_001.html)

---

## 2️⃣ BIM_L3_002 - CALE.n_2 - Centro Subregional

```
📦 L3: BIM_L3_002
   Título: CALE.n_2 - Centro Subregional
   Valorización: $4.012.929.940 COP
   Nodos: 20 base + 16 variante**
   Fuente: Tabla #5
   
   Componentes directos (desde tabla #5):
   ├─ 🏗️ L2.pista_clase_II (1 variante)
   ├─ 🏗️ L2.pista_clase_I (2 base + 1 variante)
   ├─ 🏗️ L2.edificacion (Arriendo, 1 variante)
   ├─ 🏗️ L2.cale_teorico_16q (16 cubículos) - $4.012.929.940
   ├─ 🏗️ L2.tecnologia (Plataforma CALE, 1 variante)
   ├─ 🏗️ L2.certificaciones (ISO x4, 1 variante)
   └─ 🏗️ L2.seguros (Pólizas, 1 variante)
```

**Desglose L2 → L1:**

```
   └─ 🏗️ L2.cale_teorico_16q (CALE Teórico 16 Cubículos) - $200.646.497
       └─ (Edificación - sin componentes L1 de maniobras)

   └─ 🏗️ L2.pista_clase_II (Pista Clase II) - $680.000.000
       ├─ 🔧 L1.maniobra_14 (Maniobras con remolque)
       ├─ 🔧 L1.maniobra_15 (Reversa con remolque)
       ├─ 🔧 L1.maniobra_16 (Estacionamiento con remolque)
       ├─ ⚙️ L0.pavimento_reforzado
       ├─ ⚙️ L0.señalizacion
       └─ 📎 Incluye: L2.pista_clase_I (14 maniobras adicionales)

   └─ 🏗️ L2.pista_clase_I (Pista Clase I) - $975.000.000
       ├─ 🔧 L1.maniobra_00 a L1.maniobra_13 (14 maniobras básicas)
       ├─ ⚙️ L0.pavimento_flexible
       └─ ⚙️ L0.señalizacion
```

**Ficha:** [BIM_L3_002.html](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/BIM_L3_002.html)

---

## 3️⃣ BIM_L3_003 - CALE.n_3 - Centro Local

```
📦 L3: BIM_L3_003
   Título: CALE.n_3 - Centro Local
   Valorización: $0* COP (datos incompletos en tabla #7)
   Nodos: 16 base
   Fuente: Tabla #7
   
   Componentes directos: 0 (tabla sin datos completos)
   
   ⚠️ NOTA: Requiere actualización de tabla #7 en Google Doc oficial
```

**Ficha:** [BIM_L3_003.html](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/BIM_L3_003.html)

---

## 4️⃣ BIM_L3_004 - Red Nacional de Satélites

```
📦 L3: BIM_L3_004
   Título: Red Nacional de Satélites
   Valorización: $81* COP (datos incompletos en tabla #9)
   Satélites: 140 total
   Distribución:
      ├─ C2: 31 satélites (< 50 km)
      ├─ C3: 69 satélites (50-100 km)
      ├─ C4: 27 satélites (100-150 km)
      └─ C5: 14 satélites (> 150 km)
   Fuente: Tabla #9
   
   Componentes directos (desde tabla #9):
   ├─ 🏗️ L2.sala_teorica_basica (Espacio teórico)
   ├─ 🏗️ L2.equipamiento_tic (Computadores y conectividad)
   └─ 🏗️ L2.mobiliario_basico (Sillas, mesas, archivadores)
   
   ⚠️ NOTA: Requiere actualización de tabla #9 en Google Doc oficial
```

**Ficha:** [BIM_L3_004.html](https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_l3/BIM_L3_004.html)

---

## 📋 Inventario Completo de Componentes

### Nivel L0 (Componentes Base) - 6 únicos

| ID | Componente | Descripción | Usado en |
|----|------------|-------------|----------|
| `L0.pavimento_flexible` | Pavimento asfalto estándar | Pavimento flexible asfáltico | Pista Clase I |
| `L0.pavimento_reforzado` | Pavimento concreto reforzado | Pavimento reforzado de concreto | Pista Clase II |
| `L0.pavimento_especial` | Pavimento concreto Fc=35MPa | Pavimento especializado alta resistencia | Pista Clase III |
| `L0.señalizacion` | Señalización H+V | Señalización horizontal y vertical | Todas las pistas |
| `L0.simulador_c3` | Simulador Clase III | Simulador avanzado 6 DOF NTC 5375 | CALE.n_1 |
| `L0.edificacion_base` | Edificación base | Infraestructura civil administrativa | CALE.n_1 |

### Nivel L1 (Maniobras y Componentes) - 29 únicos

**Maniobras Básicas (Clase I):** 14 componentes
- L1.maniobra_00 a L1.maniobra_13

**Maniobras Intermedias (Clase II):** 3 componentes
- L1.maniobra_14, L1.maniobra_15, L1.maniobra_16

**Maniobras Avanzadas (Clase III):** 3 componentes
- L1.maniobra_17, L1.maniobra_18, L1.maniobra_19

**Infraestructura:** 2 componentes
- L0.pavimento (3 variantes)
- L0.señalizacion

**Edificaciones:** 7 componentes
- L1.sala_24_cubiculos, L1.sala_16_cubiculos, etc.

### Nivel L2 (Configuraciones) - 5 únicos

| BIM ID | Título | Valorización | Componentes L1 |
|--------|--------|--------------|----------------|
| BIM_L2_001 | Pista Clase I | $975.000.000 | 16 |
| BIM_L2_002 | Pista Clase II | $680.000.000 | 6 (+ref a L2_001) |
| BIM_L2_003 | Pista Clase III | $1.850.000.000 | 7 (+ref a L2_002) |
| BIM_L2_004 | CALE Teórico 24q | $243.063.465 | 0 |
| BIM_L2_005 | CALE Teórico 16q | $200.646.497 | 0 |

### Nivel L3 (Configuraciones CALE) - 4 únicos

| BIM ID | Título | Valorización | Nodos |
|--------|--------|--------------|-------|
| BIM_L3_001 | CALE.n_1 Metropolitano | $141.320.000.000 | 20+3 |
| BIM_L3_002 | CALE.n_2 Subregional | $4.012.929.940 | 20+16 |
| BIM_L3_003 | CALE.n_3 Local | $0* | 16 |
| BIM_L3_004 | Red Satélites | $81* | 140 |

---

## 🔗 Referencias Cruzadas

### Jerarquía Incremental de Pistas

**Pista Clase III incluye:**
- ✅ Todas las maniobras de Clase III (3 maniobras: 17-19)
- ✅ Todas las maniobras de Clase II (3 maniobras: 14-16)
- ✅ Todas las maniobras de Clase I (14 maniobras: 0-13)
- ✅ Pavimento especial (Fc=35MPa)
- **Total:** 20 maniobras + infraestructura especializada

**Pista Clase II incluye:**
- ✅ Todas las maniobras de Clase II (3 maniobras: 14-16)
- ✅ Todas las maniobras de Clase I (14 maniobras: 0-13)
- ✅ Pavimento reforzado
- **Total:** 17 maniobras + infraestructura intermedia

**Pista Clase I:**
- ✅ Maniobras básicas (14 maniobras: 0-13)
- ✅ Pavimento flexible
- **Total:** 14 maniobras + infraestructura básica

---

## 📊 Matriz de Dependencias

```
L3_001 (CALE.n_1)
  ├─ Requiere: L2.pista_clase_3 (×20)
  │   └─ Requiere: L2.pista_clase_2 (incluida)
  │       └─ Requiere: L2.pista_clase_1 (incluida)
  │           └─ Requiere: L1.maniobra_00...13 (14 maniobras)
  │               └─ Requiere: L0.pavimento + L0.señalizacion
  ├─ Requiere: L1.sala_24_cubiculos (×20)
  ├─ Requiere: L0.simulador_c3 (×40)
  └─ Requiere: L2.edificacion_admin (×20)

L3_002 (CALE.n_2)
  ├─ Requiere: L2.pista_clase_II (×1)
  ├─ Requiere: L2.pista_clase_I (×2 base + ×1 variante)
  ├─ Requiere: L2.cale_teorico_16q (×1)
  ├─ Requiere: L2.edificacion (×1, arriendo)
  ├─ Requiere: L2.tecnologia (×1)
  ├─ Requiere: L2.certificaciones (×4)
  └─ Requiere: L2.seguros (×1)

L3_003 (CALE.n_3)
  └─ Datos pendientes (tabla #7)

L3_004 (Red Satélites)
  ├─ Requiere: L2.sala_teorica_basica (×140)
  ├─ Requiere: L2.equipamiento_tic (×140)
  └─ Requiere: L2.mobiliario_basico (×140)
```

---

## ✅ Validación de Trazabilidad

| Nivel | Tablas Google Doc | Estado | Componentes Extraídos |
|-------|-------------------|--------|----------------------|
| **L3** | #3, #5, #7, #9 + metadatos #2, #4, #6, #8 | ✅ Procesadas | 4 configuraciones |
| **L2** | #11, #13, #15, #16, #17 | ✅ Procesadas | 5 configuraciones |
| **L1** | #10, #12, #14 | ✅ Procesadas | 29 componentes |
| **L0** | Referenciados en L1 | ✅ Identificados | 6 componentes base |

---

## 🎯 Conclusión

El árbol de jerarquía BIM del SNCALE muestra una estructura completa de 4 niveles:

- **L3 (Tope):** 4 configuraciones CALE para diferentes tipos de centros
- **L2 (Medio-Alto):** 5 configuraciones de pistas y edificaciones
- **L1 (Medio-Bajo):** 29 maniobras y componentes funcionales
- **L0 (Base):** 6 componentes fundamentales (pavimentos, señalización, simuladores)

**Total valorizado:** $149.281.639.983 COP  
**Total componentes únicos:** 44 (6 L0 + 29 L1 + 5 L2 + 4 L3)

---

*Documento generado desde Google Doc oficial MUNAY_5.2__anexo_b__DEFINITIVO*  
*Sistema Nacional de Centros de Enseñanza - SNCALE | UPTC 2025*
