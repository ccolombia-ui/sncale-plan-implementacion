# Árbol de Jerarquía BIM - Sistema CALE
**Estructura Corregida con Recursividad L2→L2**
Generado: 2025-11-03 13:39:56

## 📊 Estadísticas Generales

```
Nivel L0 (Atómicos):      82 componentes
Nivel L1 (Ensamblajes):   6 componentes
Nivel L2 (Configuraciones): 3 componentes
Nivel L3 (CALE Completo):   4 componentes

TOTAL: 95 componentes BIM
```

## 🧩 Nivel L0: Componentes Atómicos

### IC: Infraestructura Civil (4 componentes)


### DR: Drenajes (3 componentes)


### SV: Señalización Vial (4 componentes)


### SEG: Seguridad (4 componentes)


### EDIF: Edificación (1 componentes)


### MAT: Materiales (3 componentes)


### ADEC: Adecuaciones (5 componentes)


### ELE: Instalaciones Eléctricas (11 componentes)


### ILU: Iluminación (2 componentes)


### HVAC: Climatización (2 componentes)


### HID: Instalaciones Hidráulicas (4 componentes)


### MOB: Mobiliario (14 componentes)


### TEC: Tecnología (7 componentes)


### AV: Audiovisual (3 componentes)


### ACC: Accesorios (3 componentes)


### VEH: Vehículos (5 componentes)


### CERT: Certificaciones (1 componentes)


### OTROS: Otros (15 componentes)


## ⚙️ Nivel L1: Ensamblajes

### BIM_L1_001: Pista motos A1A2 completa

- **Código**: `L1.pista_motos_A1A2_completa`
- **Tipo**: CONSTRUCTOR
- **Descripción**: Infraestructura motocicletas ≤125cc y >125cc
- **Valor**: $289,805,000

**Componentes L0** (6):

  - `L0.IC_001`
  - `L0.DR_003`
  - `L0.ILU_001`
  - `L0.ILU_002`
  - `L0.VEH_001`
  - `L0.VEH_002`

**Maniobras Soportadas** (geometría embebida, NO componentes):

<details>
<summary>14 especificaciones geométricas</summary>

  - MANIOBRA_00: Estacionamiento en línea recta
  - MANIOBRA_01: Estacionamiento en batería
  - MANIOBRA_02: Estacionamiento paralelo
  - MANIOBRA_03: Circuito en ocho
  - MANIOBRA_04: Línea recta con cono
  - MANIOBRA_05: Slalom
  - MANIOBRA_06: Retroceso en línea
  - MANIOBRA_07: Frenado controlado
  - MANIOBRA_08: Giro cerrado
  - MANIOBRA_09: Ascenso pendiente
  - MANIOBRA_10: Descenso controlado
  - MANIOBRA_11: Esquiva de obstáculos
  - MANIOBRA_12: Arranque pendiente
  - MANIOBRA_13: Circuito completo

</details>

---

### BIM_L1_002: Pista carros B1C1 completa

- **Código**: `L1.pista_carros_B1C1_completa`
- **Tipo**: CONSTRUCTOR
- **Descripción**: Infraestructura automóviles livianos
- **Valor**: $431,635,000

**Componentes L0** (5):

  - `L0.IC_002`
  - `L0.DR_003`
  - `L0.ILU_001`
  - `L0.ILU_002`
  - `L0.VEH_003`

**Maniobras Soportadas** (geometría embebida, NO componentes):

<details>
<summary>14 especificaciones geométricas</summary>

  - MANIOBRA_00: Estacionamiento en línea recta
  - MANIOBRA_01: Estacionamiento en batería
  - MANIOBRA_02: Estacionamiento paralelo
  - MANIOBRA_03: Circuito en ocho
  - MANIOBRA_04: Línea recta con cono
  - MANIOBRA_05: Slalom
  - MANIOBRA_06: Retroceso en línea
  - MANIOBRA_07: Frenado controlado
  - MANIOBRA_08: Giro cerrado
  - MANIOBRA_09: Ascenso pendiente
  - MANIOBRA_10: Descenso controlado
  - MANIOBRA_11: Esquiva de obstáculos
  - MANIOBRA_12: Arranque pendiente
  - MANIOBRA_13: Circuito completo

</details>

---

### BIM_L1_003: Pista camiones B2C2 completa

- **Código**: `L1.pista_camiones_B2C2_completa`
- **Tipo**: CONSTRUCTOR
- **Descripción**: Infraestructura camiones rígidos
- **Valor**: $685,950,000

**Maniobras Soportadas** (geometría embebida, NO componentes):

<details>
<summary>17 especificaciones geométricas</summary>

  - MANIOBRA_00: Estacionamiento en línea recta
  - MANIOBRA_01: Estacionamiento en batería
  - MANIOBRA_02: Estacionamiento paralelo
  - MANIOBRA_03: Circuito en ocho
  - MANIOBRA_04: Línea recta con cono
  - MANIOBRA_05: Slalom
  - MANIOBRA_06: Retroceso en línea
  - MANIOBRA_07: Frenado controlado
  - MANIOBRA_08: Giro cerrado
  - MANIOBRA_09: Ascenso pendiente
  - MANIOBRA_10: Descenso controlado
  - MANIOBRA_11: Esquiva de obstáculos
  - MANIOBRA_12: Arranque pendiente
  - MANIOBRA_13: Circuito completo
  - MANIOBRA_14: Puente de equilibrio
  - MANIOBRA_15: Rampa de frenado
  - MANIOBRA_16: Rampa de arranque

</details>

---

### BIM_L1_004: Pista tractocamiones B3C3 completa

- **Código**: `L1.pista_tractocamiones_B3C3_completa`
- **Tipo**: CONSTRUCTOR
- **Descripción**: Infraestructura tractocamiones articulados
- **Valor**: $1,192,100,000

**Maniobras Soportadas** (geometría embebida, NO componentes):

<details>
<summary>17 especificaciones geométricas</summary>

  - MANIOBRA_00: Estacionamiento en línea recta
  - MANIOBRA_01: Estacionamiento en batería
  - MANIOBRA_02: Estacionamiento paralelo
  - MANIOBRA_03: Circuito en ocho
  - MANIOBRA_04: Línea recta con cono
  - MANIOBRA_05: Slalom
  - MANIOBRA_06: Retroceso en línea
  - MANIOBRA_07: Frenado controlado
  - MANIOBRA_08: Giro cerrado
  - MANIOBRA_09: Ascenso pendiente
  - MANIOBRA_10: Descenso controlado
  - MANIOBRA_11: Esquiva de obstáculos
  - MANIOBRA_12: Arranque pendiente
  - MANIOBRA_13: Circuito completo
  - MANIOBRA_14: Puente de equilibrio
  - MANIOBRA_15: Rampa de frenado
  - MANIOBRA_16: Rampa de arranque

</details>

---

### BIM_L1_REF_001: Pista Clase I completa

- **Código**: `L1.pista_clase_I`
- **Tipo**: REFERENCIA
- **Descripción**: Infraestructura completa motos + carros (REFERENCIA a L2.pista_clase_I)
- **Referencia L2**: `BIM_L2_001`
- **Resuelve a**: `BIM_L1_001`, `BIM_L1_002`

---

### BIM_L1_REF_002: Pista Clase II completa

- **Código**: `L1.pista_clase_II`
- **Tipo**: REFERENCIA
- **Descripción**: Infraestructura completa motos + carros + camiones (REFERENCIA a L2.pista_clase_II)
- **Referencia L2**: `BIM_L2_002`
- **Resuelve a**: `BIM_L2_001`, `BIM_L1_003`

---

## 🏗️ Nivel L2: Configuraciones

**NOTA**: Este nivel implementa recursividad L2→L2 (Single Source of Truth)

### BIM_L2_001: Pista Clase I

- **Código**: `L2.pista_clase_I`
- **Tipo**: CONFIGURACION_BASE
- **Descripción**: Infraestructura completa motos A1/A2 + carros B1/C1
- **Valor Total**: $721,440,000
- **Categorías**: A1, A2, B1, C1

**Componentes Directos** (2):

  - ⚙️ **L1**: `L1.pista_motos_A1A2_completa` - Pista motos A1A2 completa ($289,805,000)
  - ⚙️ **L1**: `L1.pista_carros_B1C1_completa` - Pista carros B1C1 completa ($431,635,000)

**Componentes L1 Resueltos** (total: 2):

<details>
<summary>Ver todos los L1 después de resolver recursividad</summary>

  - `L1.pista_motos_A1A2_completa` - Pista motos A1A2 completa ($0)
  - `L1.pista_carros_B1C1_completa` - Pista carros B1C1 completa ($0)

</details>

---

### BIM_L2_002: Pista Clase II

- **Código**: `L2.pista_clase_II`
- **Tipo**: CONFIGURACION_EXTENDIDA
- **Descripción**: Infraestructura completa clase I + camiones B2/C2
- **Valor Total**: $1,407,390,000
- **Categorías**: A1, A2, B1, B2, C1, C2

**Componentes Directos** (2):

  - 🔗 **REFERENCIA L2**: `BIM_L2_001`
    <details>
    <summary>Resuelve a 2 componentes L1</summary>

      - `L1.pista_motos_A1A2_completa`
      - `L1.pista_carros_B1C1_completa`

    </details>
  - ⚙️ **L1**: `L1.pista_camiones_B2C2_completa` - Pista camiones B2C2 completa ($685,950,000)

**Componentes L1 Resueltos** (total: 3):

<details>
<summary>Ver todos los L1 después de resolver recursividad</summary>

  - `L1.pista_motos_A1A2_completa` - Pista motos A1A2 completa ($0)
  - `L1.pista_carros_B1C1_completa` - Pista carros B1C1 completa ($0)
  - `L1.pista_camiones_B2C2_completa` - Pista camiones B2C2 completa ($0)

</details>

---

### BIM_L2_003: Pista Clase III

- **Código**: `L2.pista_clase_III`
- **Tipo**: CONFIGURACION_EXTENDIDA
- **Descripción**: Infraestructura completa clase II + tractocamiones B3/C3
- **Valor Total**: $2,093,340,000
- **Categorías**: A1, A2, B1, B2, B3, C1, C2, C3

**Componentes Directos** (2):

  - 🔗 **REFERENCIA L2**: `BIM_L2_002`
    <details>
    <summary>Resuelve a 2 componentes L1</summary>

      - `L2.pista_clase_I`
      - `L1.pista_camiones_B2C2_completa`

    </details>
  - ⚙️ **L1**: `L1.pista_tractocamiones_B3C3_completa` - Pista tractocamiones B3C3 completa ($686,000,000)

**Componentes L1 Resueltos** (total: 4):

<details>
<summary>Ver todos los L1 después de resolver recursividad</summary>

  - `L1.pista_motos_A1A2_completa` - Pista motos A1A2 completa ($0)
  - `L1.pista_carros_B1C1_completa` - Pista carros B1C1 completa ($0)
  - `L1.pista_camiones_B2C2_completa` - Pista camiones B2C2 completa ($0)
  - `L1.pista_tractocamiones_B3C3_completa` - Pista tractocamiones B3C3 completa ($0)

</details>

---

## 🏢 Nivel L3: CALE Completo

### BIM_L3_001: CALE.n_1 - Centro Metropolitano

- **Nivel**: `cale_n1_metropolitano`
- **Descripción**: Configuración completa para centros de enseñanza en ciudades metropolitanas (20 nodos base + 3 variante+)
- **Tipo CALE**: Metropolitano
- **Cantidad Total**: 0

**Componentes** (6):

  - `L2.pista_clase_3` - Pista Evaluación Clase III ($37,000,000,000)
  - `L2.pista_clase_2` - Pista Evaluación Clase II ($19,600,000,000)
  - `L2.pista_clase_1` - Pista Evaluación Clase I ($15,000,000,000)
  - `L1.sala_24_cubiculos` - Sala Evaluación Teórica (24 cubículos) ($3,720,000,000)
  - `L0.simulador_c3` - Simulador Conducción Clase III ($18,000,000,000)
  - `L2.edificacion_admin` - Infraestructura Civil Base ($48,000,000,000)

---

### BIM_L3_002: CALE.n_2 - Centro Subregional

- **Nivel**: `cale_n2_subregional`
- **Descripción**: Configuración para centros en capitales subregionales (20 nodos base + 16 variante**)
- **Tipo CALE**: Subregional
- **Cantidad Total**: 0

**Componentes** (7):

  - `L2.pista_clase_II` - PISTA_CLASE_II ($0)
  - `L2.pista_clase_I` - PISTA_CLASE_I ($0)
  - `L2.edificacion` - EDIFICACION ($0)
  - `L2.cale_teorico_16q` - CALE_TEORICO_16q ($4,012,929,940)
  - `L2.tecnologia` - TECNOLOGIA ($0)
  - `L2.certificaciones` - CERTIFICACIONES ($0)
  - `L2.seguros` - SEGUROS ($0)

---

### BIM_L3_003: CALE.n_3 - Centro Local

- **Nivel**: `cale_n3_local`
- **Descripción**: Configuración básica para centros locales (16 nodos)
- **Tipo CALE**: Local
- **Cantidad Total**: 0

---

### BIM_L3_004: Red Nacional de Satélites

- **Nivel**: `red_satelites`
- **Descripción**: Distribución de 140 satélites en categorías C2-C5 para cobertura nacional
- **Tipo CALE**: Red Satélites
- **Cantidad Total**: 140

**Componentes** (3):

  - `L2.sala_teorica_basica` - ESPACIO_TEORICO¹ ($27)
  - `L2.equipamiento_tic` - EQUIPAMIENTO_TIC ($27)
  - `L2.mobiliario_basico` - MOBILIARIO_BASICO ($27)

---

## 📋 Resumen de Correcciones

### ✅ Estructura Correcta Implementada

1. **L0**: 91 componentes atómicos organizados en 18 categorías
   - Maniobras embebidas como especificaciones geométricas
   - NO como componentes BIM independientes

2. **L1**: 6 ensamblajes (4 constructores + 2 referencias)
   - Constructores muestran componentes L0
   - Maniobras como atributo descriptivo
   - Referencias apuntan a L2

3. **L2**: 3 configuraciones con recursividad L2→L2
   - Single Source of Truth implementado
   - L2.pista_clase_II → REFERENCIA a L2.pista_clase_I
   - L2.pista_clase_III → REFERENCIA a L2.pista_clase_II
   - 0% duplicación de datos

4. **L3**: 4 configuraciones completas de CALE
   - Referencias validadas a L2

### ❌ Errores Corregidos

- ~~31 "L1" maniobras~~ → 91 L0 atómicos + maniobras embebidas
- ~~L2 duplica L1~~ → L2 referencia otros L2 (recursividad)
- ~~600% duplicación~~ → 0% duplicación (SSOT)
- ~~Maniobras como componentes~~ → Maniobras como geometría

---

**Documento generado automáticamente**
Basado en estructura BIM oficial con recursividad L2→L2
