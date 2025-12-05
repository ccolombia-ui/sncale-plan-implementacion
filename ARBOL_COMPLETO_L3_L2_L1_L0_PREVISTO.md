# 🌳 ÁRBOL COMPLETO JERARQUÍA BIM - ESTRUCTURA PREVISTA

**Fecha:** 2025-11-03  
**Estado:** PROPUESTA para revisión antes de implementar  
**Fuente:** `JERARQUIA_BIM_CORRECTA.json` (generado de Google Doc oficial)

---

## 📊 RESUMEN EJECUTIVO

```
Total niveles BIM extraídos:
├─ L3: 4 configuraciones CALE (PENDIENTE extraer - usar JSON existente)
├─ L2: 5-7 configuraciones (PENDIENTE extraer completamente)
├─ L1: 6 componentes principales (✅ EXTRAÍDOS)
└─ L0: 91 componentes atómicos (✅ EXTRAÍDOS)
```

---

## 🏗️ NIVEL L3: CONFIGURACIONES CALE COMPLETAS

**FUENTE:** `TABLAS_L3_OFICIALES.json` (YA EXISTE - probablemente correcto)

```
📦 L3.CALE.n_1 - CALE Nacional (BIM_L3_001)
│  Valor: $141.320.000.000
│  Descripción: CALE habilitado para todas las categorías (A1, A2, B1, B2, B3, C1, C2, C3)
│  Área total: TBD
│  Fuente: Tabla #3
│  
│  Componentes L2 que incluye:
│  ├─ L2.pista_clase_III (incluye clase II y clase I)
│  ├─ L2.sala_teorica_24_cubiculos
│  ├─ L2.sala_formacion_50_pax
│  ├─ L2.datacenter_12m2
│  └─ L2.parqueadero_* (TBD)
│
│
📦 L3.CALE.n_2 - CALE Habilitado (BIM_L3_002)
│  Valor: $4.010.000.000
│  Descripción: CALE para categorías específicas (A1, A2, B1, C1)
│  Área total: TBD
│  Fuente: Tabla #5
│  
│  Componentes L2 que incluye:
│  ├─ L2.pista_clase_I (motos + carros)
│  ├─ L2.sala_teorica_24_cubiculos
│  └─ L2.parqueadero_* (TBD)
│
│
📦 L3.CALE.n_3 - CALE Formación (BIM_L3_003)
│  Valor: $2.890.000.000
│  Descripción: CALE básico para formación (A1, B1, C1)
│  Área total: TBD
│  Fuente: Tabla #7
│  
│  Componentes L2 que incluye:
│  ├─ L2.pista_clase_I (motos + carros)
│  └─ L2.sala_formacion_50_pax
│
│
📦 L3.CALE.satelite - CALE Satélite (BIM_L3_004)
│  Valor: $1.450.000.000
│  Descripción: CALE urbano compacto
│  Área total: TBD
│  Fuente: Tabla #9
│  
│  Componentes L2 que incluye:
│  ├─ L2.pista_clase_I_compacta (versión reducida)
│  └─ L2.sala_teorica_compacta
```

**ESTADO L3:** ✅ Ya extraído en commit anterior (310a0b7)  
**ACCIÓN PREVISTA:** Mantener JSON existente, verificar referencias L2

---

## 🏗️ NIVEL L2: CONFIGURACIONES BASE

**FUENTE:** `TABLAS_L2_OFICIALES.json` (EXISTE PERO CON ERRORES - necesita corrección)

### **COMPONENTES L2 DE PISTAS:**

```
🏗️ L2.pista_clase_I (BIM_L2_001)
│  Valor REAL: $721.440.000 (NO $975M como se declaró antes)
│  Descripción: Pista completa para motocicletas y automóviles livianos
│  Categorías: A1, A2, B1, C1
│  Fuente: Tabla #11 (valorización), Tabla #19 (componentes L1)
│  
│  ❌ ESTRUCTURA ANTERIOR (INCORRECTA):
│  ├─ MANIOBRA_00: Estacionamiento en línea recta
│  ├─ MANIOBRA_01: Estacionamiento en batería
│  ├─ ... (14 maniobras más)
│  ├─ PAVIMENTO
│  └─ SEÑALIZACION
│  Total: 16 "componentes L1" ← ERROR
│  
│  ✅ ESTRUCTURA CORRECTA (NUEVA):
│  ├─ L1.pista_motos_A1A2_completa ($289.805.000)
│  │   ├─ L0.IC_001: Pavimento flexible asfalto e=12cm
│  │   ├─ L0.DR_003: Drenaje reforzado alta capacidad
│  │   ├─ L0.SV_001: Señalización horizontal termoplástica
│  │   ├─ L0.SV_003: Conos reflectivos 90cm
│  │   ├─ L0.ILU_001: Luminaria LED 150W poste 8m
│  │   ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│  │   ├─ L0.VEH_001: Motocicleta ≤125cc adaptada
│  │   ├─ L0.VEH_002: Motocicleta >125cc adaptada
│  │   └─ [Maniobras 0-13: geometría embebida en L0, no componentes BIM]
│  │
│  └─ L1.pista_carros_B1C1_completa ($431.635.000)
│      ├─ L0.IC_002: Pavimento rígido concreto Fc=21MPa e=15cm
│      ├─ L0.DR_003: Drenaje reforzado alta capacidad
│      ├─ L0.SV_001: Señalización horizontal termoplástica
│      ├─ L0.SV_003: Conos reflectivos 90cm
│      ├─ L0.ILU_001: Luminaria LED 150W poste 8m
│      ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│      ├─ L0.VEH_003: Automóvil B1/C1 adaptado
│      └─ [Maniobras 0-13: geometría embebida en L0]
│  
│  Total CORRECTO: 2 componentes L1 + múltiples L0
│
│
🏗️ L2.pista_clase_II (BIM_L2_002)
│  Valor REAL: $1.407.390.000
│  Descripción: Pista completa para automóviles y camiones rígidos
│  Categorías: A1, A2, B1, B2, C1, C2
│  Fuente: Tabla #13 (valorización), Tabla #20 (componentes L1)
│  
│  ❌ ESTRUCTURA ANTERIOR (INCORRECTA):
│  ├─ MANIOBRA_14: Puente de equilibrio
│  ├─ MANIOBRA_15: Rampa de frenado
│  ├─ MANIOBRA_16: Rampa de arranque
│  ├─ PAVIMENTO
│  ├─ SEÑALIZACION
│  └─ pista_clase_I (referencia)
│  Total: 6 "componentes L1" ← ERROR
│  
│  ✅ ESTRUCTURA CORRECTA (NUEVA):
│  ├─ L1.pista_clase_I ($721.440.000) [REFERENCIA JERÁRQUICA]
│  │   └─ (Incluye todos los L0 de motos + carros)
│  │
│  └─ L1.pista_camiones_B2C2_completa ($685.950.000)
│      ├─ L0.IC_003: Pavimento reforzado concreto Fc=28MPa e=20cm
│      ├─ L0.DR_003: Drenaje reforzado alta capacidad
│      ├─ L0.SV_001: Señalización horizontal termoplástica
│      ├─ L0.SV_004: Señalización vertical Tipo I
│      ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│      ├─ L0.SEG_001: Baranda metálica contención
│      ├─ L0.VEH_004: Camión B2/C2 adaptado
│      └─ [Maniobras 14-16: geometría embebida en L0]
│  
│  Total CORRECTO: 2 componentes L1 (1 referencia + 1 constructor)
│
│
🏗️ L2.pista_clase_III (BIM_L2_003)
│  Valor REAL: TBD (sumar clase_II + tractocamiones)
│  Descripción: Pista completa para todos los vehículos incluidos tractocamiones
│  Categorías: A1, A2, B1, B2, B3, C1, C2, C3
│  Fuente: Tabla #15 (valorización), Tabla #21 (componentes L1)
│  
│  ❌ ESTRUCTURA ANTERIOR (INCORRECTA):
│  ├─ MANIOBRA_17: Zona de articulación
│  ├─ MANIOBRA_18: Retroceso articulado
│  ├─ MANIOBRA_19: Giro especial
│  ├─ PAVIMENTO
│  ├─ SEÑALIZACION
│  ├─ pista_clase_II (referencia)
│  └─ pista_clase_I (referencia)
│  Total: 7 "componentes L1" ← ERROR
│  
│  ✅ ESTRUCTURA CORRECTA (NUEVA):
│  ├─ L1.pista_clase_II ($1.407.390.000) [REFERENCIA JERÁRQUICA]
│  │   └─ (Incluye todos los L0 de clase_I + camiones)
│  │
│  └─ L1.pista_tractocamiones_B3C3_completa (Valor TBD)
│      ├─ L0.IC_004: Pavimento especial concreto Fc=35MPa e=25cm
│      ├─ L0.DR_003: Drenaje reforzado alta capacidad
│      ├─ L0.SV_001: Señalización horizontal termoplástica
│      ├─ L0.SV_004: Señalización vertical Tipo I
│      ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│      ├─ L0.SEG_001: Baranda metálica contención
│      ├─ L0.VEH_005: Tractocamión B3/C3 articulado
│      └─ [Maniobras 17-19: geometría embebida en L0]
│  
│  Total CORRECTO: 2 componentes L1 (1 referencia + 1 constructor)
```

### **COMPONENTES L2 DE EDIFICACIONES:**

```
🏗️ L2.sala_teorica_24_cubiculos (BIM_L2_004)
│  Valor: TBD
│  Descripción: Sala de evaluación teórica con 24 estaciones
│  Fuente: Tabla #16 (valorización), Tablas de edificación
│  
│  Componentes L1 previstos (POR CONFIRMAR):
│  ├─ L1.edificacion_parametrica (estructura + acabados)
│  │   ├─ L0.EDIF_001: Edificación principal CALE
│  │   ├─ L0.MAT_002: Concreto premezclado 3000 PSI
│  │   ├─ L0.MAT_003: Acero estructural ASTM A36
│  │   ├─ L0.ADEC_001: Adecuaciones Drywall completas
│  │   ├─ L0.ADEC_003: Cielo raso suspendido
│  │   ├─ L0.ADEC_004: Piso vinílico LVT
│  │   └─ ...
│  │
│  ├─ L1.instalaciones_electricas
│  │   ├─ L0.ELE_001: Acometida trifásica 220V 30A
│  │   ├─ L0.ELE_002: Instalaciones eléctricas complementarias
│  │   ├─ L0.ELE_006: UPS 10kVA doble conversión
│  │   └─ ...
│  │
│  ├─ L1.mobiliario_sala_teorica
│  │   ├─ L0.ADEC_005: Cubículos evaluación (24 und)
│  │   ├─ L0.MOB_001: Escritorio ergonómico (24 und)
│  │   ├─ L0.MOB_002: Silla ergonómica (24 und)
│  │   └─ ...
│  │
│  └─ L1.equipamiento_tecnologico
│      ├─ L0.TEC_001: PC Desktop Core i5 (24 und)
│      ├─ L0.TEC_002: Monitor LED Full HD 24" (24 und)
│      ├─ L0.SALA_CONTROL_TEORICO: Estación supervisión
│      └─ ...
│
│
🏗️ L2.sala_formacion_50_pax (BIM_L2_005)
│  Valor: TBD
│  Descripción: Aula de formación teórica capacidad 50 personas
│  Fuente: Tabla #17 (valorización)
│  
│  Componentes L1 previstos (POR CONFIRMAR):
│  ├─ L1.edificacion_parametrica (estructura + acabados)
│  ├─ L1.instalaciones_electricas
│  ├─ L1.mobiliario_aula
│  │   ├─ L0.MOB_003: Sillas universitarias (50 und)
│  │   ├─ L0.MOB_004: Tablero acrílico 3.0×1.5m
│  │   ├─ L0.MOB_006: Mobiliario aula informática
│  │   └─ ...
│  │
│  └─ L1.equipamiento_audiovisual
│      ├─ L0.AV_001: Video proyector 5000 lúmenes
│      ├─ L0.AV_002: Pantalla eléctrica 4.0×3.0m
│      ├─ L0.AV_003: Sistema audio amplificado
│      └─ ...
│
│
🏗️ L2.datacenter_12m2 (BIM_L2_006?) [PENDIENTE CONFIRMAR]
│  Valor: TBD
│  Descripción: Sala técnica datacenter 12 m²
│  Fuente: TBD
│  
│  Componentes L1 previstos:
│  └─ L1.infraestructura_datacenter
│      ├─ L0.TEC_004: Rack servidor 42U
│      ├─ L0.TEC_005: Servidor HP ProLiant DL380 Gen10
│      ├─ L0.TEC_006: Switch Gigabit 48 Puertos PoE+
│      ├─ L0.HVAC_001: Sistema HVAC precision datacenter
│      ├─ L0.SEG_003: Sistema detección incendios
│      ├─ L0.ELE_006: UPS 10kVA doble conversión
│      └─ ...
│
│
🏗️ L2.parqueadero_* (BIM_L2_007?) [PENDIENTE CONFIRMAR]
│  Valor: TBD
│  Descripción: Áreas de parqueadeo
│  Fuente: TBD
│  
│  Componentes L1 previstos:
│  └─ L1.infraestructura_parqueadero
│      ├─ L0.IC_002: Pavimento rígido concreto (para parqueaderos)
│      ├─ L0.DR_001: Cuneta concreto perimetral
│      ├─ L0.DR_002: Sistema drenaje pluvial
│      ├─ L0.SV_002: Demarcación espacio vehicular
│      ├─ L0.ILU_001: Luminaria LED 150W
│      └─ ...
```

**ESTADO L2:** ⚠️ Parcialmente extraído con ERRORES en pistas  
**ACCIÓN PREVISTA:** Corregir L2 de pistas (3 componentes), extraer/validar L2 de edificaciones (4-5 componentes)

---

## 🔧 NIVEL L1: ENSAMBLAJES DE INFRAESTRUCTURA

**FUENTE:** `JERARQUIA_BIM_CORRECTA.json` - ✅ YA EXTRAÍDO

### **L1 PRINCIPALES (PISTAS):**

```
🔧 L1.pista_motos_A1A2_completa (Tabla #19, Fila 2)
│  BIM_ID: BIM_L1_001
│  Código: L1.pista_motos_A1A2_completa
│  Descripción: Infraestructura motocicletas ≤125cc y >125cc
│  Valor: $289.805.000
│  Cantidad: 1 glb
│  Categorías: A1 (≤125cc), A2 (>125cc)
│  
│  Componentes L0 (6 identificados):
│  ├─ L0.IC_001: Pavimento flexible asfalto e=12cm
│  ├─ L0.DR_003: Drenaje reforzado alta capacidad
│  ├─ L0.ILU_001: Luminaria LED 150W poste 8m
│  ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│  ├─ L0.VEH_001: Motocicleta ≤125cc adaptada
│  └─ L0.VEH_002: Motocicleta >125cc adaptada
│  
│  Maniobras soportadas (NO componentes BIM):
│  - MANIOBRA_00: Estacionamiento en línea recta
│  - MANIOBRA_01: Estacionamiento en batería
│  - MANIOBRA_02: Estacionamiento paralelo
│  - MANIOBRA_03: Circuito en ocho
│  - MANIOBRA_04: Línea recta con cono
│  - MANIOBRA_05: Slalom
│  - MANIOBRA_06: Retroceso en línea
│  - MANIOBRA_07: Frenado controlado
│  - MANIOBRA_08: Giro cerrado
│  - MANIOBRA_09: Ascenso pendiente
│  - MANIOBRA_10: Descenso controlado
│  - MANIOBRA_11: Esquiva de obstáculos
│  - MANIOBRA_12: Arranque pendiente
│  - MANIOBRA_13: Circuito completo
│
│
🔧 L1.pista_carros_B1C1_completa (Tabla #19, Fila 3)
│  BIM_ID: BIM_L1_002
│  Código: L1.pista_carros_B1C1_completa
│  Descripción: Infraestructura automóviles livianos
│  Valor: $431.635.000
│  Cantidad: 1 glb
│  Categorías: B1 (automóvil), C1 (campero/camioneta)
│  
│  Componentes L0 (7+ identificados):
│  ├─ L0.IC_002: Pavimento rígido concreto Fc=21MPa e=15cm
│  ├─ L0.DR_003: Drenaje reforzado alta capacidad
│  ├─ L0.SV_001: Señalización horizontal termoplástica
│  ├─ L0.SV_003: Conos reflectivos 90cm
│  ├─ L0.ILU_001: Luminaria LED 150W poste 8m
│  ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│  └─ L0.VEH_003: Automóvil B1/C1 adaptado
│  
│  Maniobras soportadas (MISMAS que motos: 0-13)
│
│
🔧 L1.pista_camiones_B2C2_completa (Tabla #20, Fila 3)
│  BIM_ID: BIM_L1_003
│  Código: L1.pista_camiones_B2C2_completa
│  Descripción: Infraestructura camiones rígidos
│  Valor: $685.950.000
│  Cantidad: 1 glb
│  Categorías: B2 (camión rígido), C2 (bus)
│  
│  Componentes L0 (PREVISTOS, pendiente confirmar):
│  ├─ L0.IC_003: Pavimento reforzado concreto Fc=28MPa e=20cm
│  ├─ L0.DR_003: Drenaje reforzado alta capacidad
│  ├─ L0.SV_001: Señalización horizontal termoplástica
│  ├─ L0.SV_004: Señalización vertical Tipo I
│  ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│  ├─ L0.SEG_001: Baranda metálica contención
│  └─ L0.VEH_004: Camión B2/C2 adaptado
│  
│  Maniobras soportadas:
│  - MANIOBRA_14: Puente de equilibrio
│  - MANIOBRA_15: Rampa de frenado
│  - MANIOBRA_16: Rampa de arranque
│  - (más maniobras 0-13 básicas)
│
│
🔧 L1.pista_tractocamiones_B3C3_completa (Tabla #21, Fila 3)
│  BIM_ID: BIM_L1_004
│  Código: L1.pista_tractocamiones_B3C3_completa
│  Descripción: Infraestructura vehículos articulados
│  Valor: TBD (pendiente extracción)
│  Cantidad: 1 glb
│  Categorías: B3 (tractocamión), C3 (bus articulado)
│  
│  Componentes L0 (PREVISTOS):
│  ├─ L0.IC_004: Pavimento especial concreto Fc=35MPa e=25cm
│  ├─ L0.DR_003: Drenaje reforzado alta capacidad
│  ├─ L0.SV_001: Señalización horizontal termoplástica
│  ├─ L0.SV_004: Señalización vertical Tipo I
│  ├─ L0.ILU_002: Luminaria LED 200W poste 10m
│  ├─ L0.SEG_001: Baranda metálica contención
│  └─ L0.VEH_005: Tractocamión B3/C3 articulado
│  
│  Maniobras soportadas:
│  - MANIOBRA_17: Zona de articulación
│  - MANIOBRA_18: Retroceso articulado
│  - MANIOBRA_19: Giro especial
│  - (más maniobras 0-16 anteriores)
```

### **L1 REFERENCIAS JERÁRQUICAS:**

```
🔗 L1.pista_clase_I (Tabla #20, Fila 2)
│  BIM_ID: BIM_L1_REF_001
│  Código: L1.pista_clase_I
│  Descripción: Pista Clase I completa (REFERENCIA a motos + carros)
│  Valor: $721.440.000 (suma de L1.pista_motos + L1.pista_carros)
│  Tipo: REFERENCIA JERÁRQUICA (no constructor directo)
│  
│  Componentes que incluye:
│  ├─ L1.pista_motos_A1A2_completa ($289.805.000)
│  └─ L1.pista_carros_B1C1_completa ($431.635.000)
│
│
🔗 L1.pista_clase_II (Tabla #21, Fila 2)
│  BIM_ID: BIM_L1_REF_002
│  Código: L1.pista_clase_II
│  Descripción: Pista Clase II completa (REFERENCIA a clase_I + camiones)
│  Valor: $1.407.390.000
│  Tipo: REFERENCIA JERÁRQUICA
│  
│  Componentes que incluye:
│  ├─ L1.pista_clase_I ($721.440.000)
│  └─ L1.pista_camiones_B2C2_completa ($685.950.000)
```

### **L1 DE EDIFICACIONES (PENDIENTE CONFIRMAR):**

```
🔧 L1.edificacion_parametrica [POR CONFIRMAR]
│  Descripción: Estructura principal edificación CALE
│  Componentes L0: EDIF_001, MAT_001-003, ADEC_001-005
│
🔧 L1.instalaciones_electricas [POR CONFIRMAR]
│  Descripción: Sistema eléctrico completo
│  Componentes L0: ELE_001-012
│
🔧 L1.instalaciones_hidrosanitarias [POR CONFIRMAR]
│  Descripción: Agua potable + desagües
│  Componentes L0: HID_001-002, HVAC_001
│
🔧 L1.mobiliario_sala_* [POR CONFIRMAR]
│  Descripción: Mobiliario por tipo de sala
│  Componentes L0: MOB_001-012, LOCKERS, ARCHIVO
│
🔧 L1.equipamiento_tecnologico [POR CONFIRMAR]
│  Descripción: Tecnología completa CALE
│  Componentes L0: TEC_001-009, AV_001-003, PLAT_TEC
```

**ESTADO L1:** ✅ 6 componentes principales extraídos (4 constructores + 2 referencias)  
**ACCIÓN PREVISTA:** Confirmar asociaciones L0, extraer L1 de edificaciones

---

## ⚙️ NIVEL L0: COMPONENTES ATÓMICOS

**FUENTE:** `JERARQUIA_BIM_CORRECTA.json` - ✅ YA EXTRAÍDO (91 componentes)

### **CATEGORÍA IC - INFRAESTRUCTURA CIVIL (4 componentes)**

```
⚙️ L0.IC_001 - Pavimento flexible asfalto e=12cm
   BIM_ID: BIM_L0_001
   Descripción: Carpeta asfáltica MDC-19 sobre base granular
   Unidad: m²
   Normatividad: INVIAS Art. 450
   Valor Unitario: $85.000/m²
   Usado en: L1.pista_motos_A1A2_completa
   Fuente: Tabla #59, Fila 2

⚙️ L0.IC_002 - Pavimento rígido concreto Fc=21MPa e=15cm
   BIM_ID: BIM_L0_002
   Descripción: Losa concreto hidráulico sobre subbase
   Unidad: m²
   Normatividad: INVIAS Art. 500
   Valor Unitario: $95.000/m²
   Usado en: L1.pista_carros_B1C1_completa, L1.parqueadero_*
   Fuente: Tabla #59, Fila 3

⚙️ L0.IC_003 - Pavimento reforzado concreto Fc=28MPa e=20cm
   BIM_ID: BIM_L0_003
   Descripción: Losa reforzada malla electrosoldada
   Unidad: m²
   Normatividad: NSR-10
   Valor Unitario: $115.000/m²
   Usado en: L1.pista_camiones_B2C2_completa
   Fuente: Tabla #59, Fila 4

⚙️ L0.IC_004 - Pavimento especial concreto Fc=35MPa e=25cm
   BIM_ID: BIM_L0_004
   Descripción: Losa alta resistencia vehículos pesados
   Unidad: m²
   Normatividad: NSR-10
   Valor Unitario: $145.000/m²
   Usado en: L1.pista_tractocamiones_B3C3_completa
   Fuente: Tabla #59, Fila 5
```

### **CATEGORÍA DR - DRENAJES (3 componentes)**

```
⚙️ L0.DR_001 - Cuneta concreto perimetral
   BIM_ID: BIM_L0_005
   Descripción: Cuneta tipo 1 sección 0.30×0.30m
   Unidad: ml
   Valor Unitario: $35.000/ml
   Usado en: L1.pista_clase_*, L1.parqueadero_
   Fuente: Tabla #60, Fila 2

⚙️ L0.DR_002 - Sistema drenaje pluvial
   BIM_ID: BIM_L0_006
   Descripción: Rejillas + tubería PVC sanitaria
   Unidad: ml
   Valor Unitario: $55.000/ml
   Usado en: L1.parqueadero_*
   Fuente: Tabla #60, Fila 3

⚙️ L0.DR_003 - Drenaje reforzado alta capacidad
   BIM_ID: BIM_L0_007
   Descripción: Sistema para cargas pesadas
   Unidad: ml
   Valor Unitario: $75.000/ml
   Usado en: L1.pista_clase_II/III
   Fuente: Tabla #60, Fila 4
```

### **CATEGORÍA SV - SEÑALIZACIÓN VIAL (4 componentes)**

```
⚙️ L0.SV_001 - Señalización horizontal termoplástica
   BIM_ID: BIM_L0_008
   Descripción: Pintura termoplástica reflectiva blanca/amarilla
   Unidad: ml
   Valor Unitario: $8.500/ml
   Usado en: L1.pista_*
   Fuente: Tabla #61, Fila 2

⚙️ L0.SV_002 - Demarcación espacio vehicular
   BIM_ID: BIM_L0_009
   Descripción: Líneas demarcación parqueadero
   Unidad: und
   Valor Unitario: $25.000/und
   Usado en: L1.parqueadero_*
   Fuente: Tabla #61, Fila 3

⚙️ L0.SV_003 - Conos reflectivos 90cm
   BIM_ID: BIM_L0_010
   Descripción: Conos viales reflectivos naranja
   Unidad: und
   Valor Unitario: $45.000/und
   Usado en: L1.pista_*
   Fuente: Tabla #62, Fila 2

⚙️ L0.SV_004 - Señalización vertical Tipo I
   BIM_ID: BIM_L0_011
   Descripción: Señal reglamentaria/preventiva 0.75×0.75m
   Unidad: und
   Valor Unitario: $185.000/und
   Usado en: L1.pista_*, L1.parqueadero_
   Fuente: Tabla #62, Fila 3
```

### **CATEGORÍA SEG - SEGURIDAD (3 componentes)**

```
⚙️ L0.SEG_001 - Baranda metálica contención
   BIM_ID: BIM_L0_012
   Descripción: Defensa metálica doble onda galvanizada
   Unidad: ml
   Valor Unitario: $125.000/ml
   Usado en: L1.pista_*
   Fuente: Tabla #63, Fila 2

⚙️ L0.SEG_002 - Kit seguridad evaluación
   BIM_ID: BIM_L0_013
   Descripción: Conos + señales + extintores + botiquín
   Unidad: glb
   Valor Unitario: $1.500.000/glb
   Usado en: L1.pista_*
   Fuente: Tabla #63, Fila 3

⚙️ L0.SEG_003 - Sistema detección incendios
   BIM_ID: BIM_L0_014
   Descripción: Detectores de humo + alarma + rociadores
   Unidad: und
   Valor Unitario: $2.800.000/und
   Usado en: L1.datacenter_12m2
   Fuente: Tabla #63, Fila 4
```

### **CATEGORÍA VEH - VEHÍCULOS (5 componentes)**

```
⚙️ L0.VEH_001 - Motocicleta ≤125cc adaptada
   BIM_ID: BIM_L0_071
   Descripción: Moto escuela categoría A1
   Unidad: und
   Valor Unitario: $8.500.000/und
   Usado en: L1.pista_motos_A1A2_completa
   Fuente: Tabla #81, Fila 2

⚙️ L0.VEH_002 - Motocicleta >125cc adaptada
   BIM_ID: BIM_L0_072
   Descripción: Moto escuela categoría A2
   Unidad: und
   Valor Unitario: $14.000.000/und
   Usado en: L1.pista_motos_A1A2_completa
   Fuente: Tabla #81, Fila 3

⚙️ L0.VEH_003 - Automóvil B1/C1 adaptado
   BIM_ID: BIM_L0_073
   Descripción: Auto escuela categoría B1/C1
   Unidad: und
   Valor Unitario: $45.000.000/und
   Usado en: L1.pista_carros_B1C1_completa
   Fuente: Tabla #81, Fila 4

⚙️ L0.VEH_004 - Camión B2/C2 adaptado
   BIM_ID: BIM_L0_074
   Descripción: Camión escuela categoría B2/C2
   Unidad: und
   Valor Unitario: $120.000.000/und
   Usado en: L1.pista_camiones_B2C2_completa
   Fuente: Tabla #81, Fila 5

⚙️ L0.VEH_005 - Tractocamión B3/C3 articulado
   BIM_ID: BIM_L0_075
   Descripción: Tractocamión escuela categoría B3/C3
   Unidad: und
   Valor Unitario: $180.000.000/und
   Usado en: L1.pista_tractocamiones_B3C3_completa
   Fuente: Tabla #81, Fila 6
```

### **OTRAS CATEGORÍAS (71 componentes adicionales)**

```
📦 EDIF/MAT - Edificación y Materiales (5 componentes)
   L0.EDIF_001, L0.MAT_001-003

📦 ADEC - Adecuaciones (5 componentes)
   L0.ADEC_001-005

📦 ELE - Instalaciones Eléctricas (12 componentes)
   L0.ELE_001-012

📦 ILU - Iluminación (2 componentes)
   L0.ILU_001-002

📦 HVAC - Climatización (1 componente)
   L0.HVAC_001

📦 HID - Instalaciones Hidráulicas (2 componentes)
   L0.HID_001-002

📦 MOB - Mobiliario (18 componentes)
   L0.MOB_001-012, L0.MOB_RECEPCION, L0.MOB_SILLAS_ESPERA, 
   L0.LOCKERS_ASPIRANTES, L0.ARCHIVO_ACTIVO, L0.ARCHIVADOR_VERTICAL

📦 TEC - Tecnología (10 componentes)
   L0.TEC_001-009, L0.PLAT_TEC, L0.SALA_CONTROL_*

📦 AV - Audiovisual (3 componentes)
   L0.AV_001-003

📦 ACC - Accesorios (3 componentes)
   L0.ACC_001-003

📦 SEG/CERT - Seguros y Certificaciones (2 componentes)
   L0.SEG_100, L0.CERT_ISO

📦 Circulación y Accesibilidad (5 componentes)
   L0.PASILLO_INTERNO, L0.CIRCULACION_EXTERNA, L0.RAMPA_ACCESIBILIDAD,
   L0.ESCALERA_INTERNA, L0.ESCALERA_EMERGENCIA
```

**ESTADO L0:** ✅ 91 componentes extraídos completamente  
**ACCIÓN PREVISTA:** Usar datos existentes, validar asociaciones "Usado en"

---

## 📋 PLAN DE IMPLEMENTACIÓN PREVISTO

### **FASE 1: Corrección de JSONs Existentes**

1. **TABLAS_L0_OFICIALES.json** (NUEVO)
   - Crear archivo con 91 componentes L0
   - Estructura por categorías (IC, DR, SV, SEG, VEH, etc.)
   - Incluir "usado_en" para mapeo L0→L1

2. **TABLAS_L1_OFICIALES.json** (CORREGIR)
   - Reemplazar 3 entradas actuales (maniobras) con 6+ correctas
   - 4 constructores: pista_motos, pista_carros, pista_camiones, pista_tractocamiones
   - 2 referencias: pista_clase_I, pista_clase_II
   - Incluir asociaciones a componentes L0

3. **TABLAS_L2_OFICIALES.json** (CORREGIR)
   - Actualizar pista_clase_I: 2 componentes L1 (NO 16 maniobras)
   - Actualizar pista_clase_II: 2 componentes L1 (NO 6)
   - Actualizar pista_clase_III: 2 componentes L1 (NO 7)
   - Validar/extraer edificaciones (salas teóricas, datacenter)

4. **TABLAS_L3_OFICIALES.json** (MANTENER)
   - Archivo ya existe y probablemente es correcto
   - Validar referencias a L2 corregidos

### **FASE 2: Regeneración de Fichas HTML**

1. **Fichas L1** (4-6 fichas)
   - BIM_L1_001: pista_motos_A1A2_completa
   - BIM_L1_002: pista_carros_B1C1_completa
   - BIM_L1_003: pista_camiones_B2C2_completa
   - BIM_L1_004: pista_tractocamiones_B3C3_completa
   - BIM_L1_REF_001: pista_clase_I (referencia)
   - BIM_L1_REF_002: pista_clase_II (referencia)
   
   **CONTENIDO:**
   - Tabla de componentes L0 (NO maniobras)
   - Sección descriptiva "Maniobras soportadas" (NO tabla BIM)
   - Especificaciones técnicas
   - Valorización por L0

2. **Fichas L2** (5+ fichas)
   - BIM_L2_001: pista_clase_I
   - BIM_L2_002: pista_clase_II
   - BIM_L2_003: pista_clase_III
   - BIM_L2_004: sala_teorica_24_cubiculos
   - BIM_L2_005: sala_formacion_50_pax
   
   **CONTENIDO:**
   - Tabla de componentes L1 (2-4 componentes)
   - Expandible a componentes L0
   - Valorización por L1
   - Especificaciones técnicas

3. **Fichas L3** (4 fichas)
   - Validar contenido existente
   - Actualizar referencias L2 si cambiaron BIM_IDs
   - Mantener estructura general

### **FASE 3: Documentación Corregida**

1. **Árbol de Jerarquía BIM**
   - Regenerar con 4 niveles completos
   - Estadísticas: L3(4), L2(5-7), L1(6+), L0(91)
   - Visualización interactiva

2. **Informe de Corrección**
   - Documentar error descubierto
   - Explicar diferencia maniobras vs. componentes BIM
   - Comparativa antes/después
   - Validación de valores

### **FASE 4: Despliegue Git**

1. Commit con mensaje: "CORRECCIÓN CRÍTICA: Estructura BIM L3→L2→L1→L0 según Google Doc oficial"
2. Deprecar commit 310a0b7
3. Push a GitHub
4. Validar GitHub Pages

---

## ❓ PREGUNTAS PARA DECISIÓN

1. **¿Procedo con la FASE 1** (corrección de JSONs)?
   - ¿O prefieres revisar primero alguna tabla específica?

2. **¿Los componentes L1 de edificaciones** (mobiliario_sala, equipamiento_tecnologico, etc.) **están correctos?**
   - ¿O necesitas que extraiga tablas específicas del Google Doc?

3. **¿Mantengo los BIM_IDs actuales** (BIM_L2_001-005, BIM_L1_001-003)?
   - ¿O renumero completamente con los nuevos componentes?

4. **¿Las fichas L1 deben incluir** sección "Maniobras soportadas"?
   - ¿O elimino completamente las maniobras de las fichas?

5. **¿Confirmas que el valor de pista_clase_I es $721.440.000?**
   - ¿No $975M como aparecía antes?

---

## 📊 RESUMEN FINAL

```
✅ DATOS EXTRAÍDOS Y LISTOS:
├─ L0: 91 componentes atómicos (COMPLETO)
├─ L1: 6 componentes principales (COMPLETO)
├─ L2: 3 pistas identificadas (PARCIAL - faltan edificaciones)
└─ L3: 4 CALE (YA EXISTENTE)

⚠️ DATOS POR CONFIRMAR:
├─ L1 de edificaciones (mobiliario, tecnología, etc.)
├─ L2 de edificaciones (salas teóricas, datacenter)
└─ Valores de pista_clase_III y pista_tractocamiones

❌ DATOS INCORRECTOS A CORREGIR:
├─ TABLAS_L1_OFICIALES.json (tiene maniobras)
├─ TABLAS_L2_OFICIALES.json (referencias a maniobras)
├─ Fichas L1 001-003 (muestran maniobras como componentes)
├─ Fichas L2 001-003 (muestran maniobras en L1)
└─ Árbol jerarquía (muestra 31 "L1" incorrectos)
```

**DECISIÓN REQUERIDA:** ¿Procedo con la implementación completa o revisamos alguna parte específica primero?
