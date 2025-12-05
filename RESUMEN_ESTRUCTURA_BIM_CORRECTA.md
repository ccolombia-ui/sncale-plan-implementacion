# 📊 RESUMEN ESTRUCTURA BIM CORRECTA

**Fecha extracción:** 2025-11-03  
**Fuente:** Google Doc `MUNAY_5.2__anexo_b__DEFINITIVO`  
**Doc ID:** `16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE`

---

## ✅ CORRECCIÓN CRÍTICA APLICADA

### ❌ ESTRUCTURA INCORRECTA (Anterior)
```
L2.pista_clase_I ($975M declarado)
  ├─ L1.MANIOBRA_00 (❌ NO ES COMPONENTE BIM)
  ├─ L1.MANIOBRA_01 (❌ NO ES COMPONENTE BIM)
  ├─ L1.MANIOBRA_02 (❌ NO ES COMPONENTE BIM)
  ...
  ├─ L1.MANIOBRA_13 (❌ NO ES COMPONENTE BIM)
  ├─ L1.PAVIMENTO (❌ INCOMPLETO)
  └─ L1.SEÑALIZACION (❌ INCOMPLETO)
  
Total: 16 "componentes L1" ← ERROR FUNDAMENTAL
```

### ✅ ESTRUCTURA CORRECTA (Nueva)
```
L2.pista_clase_I ($721.440.000 real)
  │
  ├─ L1.pista_motos_A1A2_completa ($289.805.000)
  │   ├─ L0.IC_001: Pavimento flexible asfalto e=12cm
  │   ├─ L0.DR_001: Cuneta concreto perimetral
  │   ├─ L0.DR_003: Drenaje reforzado alta capacidad
  │   ├─ L0.SV_001: Señalización horizontal termoplástica
  │   ├─ L0.SV_003: Conos reflectivos 90cm
  │   ├─ L0.ILU_001: Luminaria LED 150W poste 8m
  │   ├─ L0.VEH_001: Motocicleta ≤125cc adaptada
  │   ├─ L0.VEH_002: Motocicleta >125cc adaptada
  │   └─ [MANIOBRAS 0-13: especificaciones geométricas DENTRO de L0]
  │
  └─ L1.pista_carros_B1C1_completa ($431.635.000)
      ├─ L0.IC_002: Pavimento rígido concreto Fc=21MPa e=15cm
      ├─ L0.DR_001: Cuneta concreto perimetral
      ├─ L0.DR_003: Drenaje reforzado alta capacidad
      ├─ L0.SV_001: Señalización horizontal termoplástica
      ├─ L0.SV_003: Conos reflectivos 90cm
      ├─ L0.ILU_001: Luminaria LED 150W poste 8m
      ├─ L0.VEH_003: Automóvil B1/C1 adaptado
      └─ [MANIOBRAS 0-13: especificaciones geométricas DENTRO de L0]

Total: 2 componentes L1 + múltiples L0 ← CORRECTO
```

---

## 📈 JERARQUÍA COMPLETA CORRECTA

### Nivel L3: CALE Completas (4 configuraciones)
```
📦 L3.CALE.n_1  (Nacional - Todas las categorías)
📦 L3.CALE.n_2  (Habilitados - Categorías específicas)
📦 L3.CALE.n_3  (Formación - Categorías básicas)
📦 L3.CALE.satélite  (Satélites urbanos)
```

### Nivel L2: Configuraciones Base (5-7 esperadas)
```
🏗️ L2.pista_clase_I   (Motos + Carros)
🏗️ L2.pista_clase_II  (Clase I + Camiones)
🏗️ L2.pista_clase_III (Clase II + Tractocamiones)
🏗️ L2.sala_teorica_*  (Edificaciones)
🏗️ L2.parqueadero_*   (Parqueaderos)
```

### Nivel L1: Ensamblajes de Infraestructura (6 principales)

**COMPONENTES L1 DE PISTAS:**

1. **L1.pista_motos_A1A2_completa** ($289.805.000)
   - Fuente: Tabla #19, Fila 2
   - Descripción: Infraestructura motocicletas ≤125cc y >125cc
   - Componentes L0 asociados: 6
     - L0.IC_001: Pavimento flexible asfalto
     - L0.VEH_001: Motocicleta ≤125cc
     - L0.VEH_002: Motocicleta >125cc
     - L0.ILU_001: Luminaria LED 150W
     - L0.DR_003: Drenaje reforzado
     - [+ señalización, seguridad]

2. **L1.pista_carros_B1C1_completa** ($431.635.000)
   - Fuente: Tabla #19, Fila 3
   - Descripción: Infraestructura automóviles livianos
   - Componentes L0 asociados: 7
     - L0.IC_002: Pavimento rígido concreto Fc=21MPa
     - L0.VEH_003: Automóvil B1/C1 adaptado
     - L0.ILU_001: Luminaria LED 150W
     - L0.DR_003: Drenaje reforzado
     - [+ señalización, seguridad]

3. **L1.pista_camiones_B2C2_completa** ($685.950.000)
   - Fuente: Tabla #20, Fila 3
   - Descripción: Infraestructura camiones rígidos
   - Componentes L0 asociados: TBD
     - L0.IC_003: Pavimento reforzado concreto Fc=28MPa
     - L0.VEH_004: Camión B2/C2 adaptado
     - L0.ILU_002: Luminaria LED 200W
     - [+ señalización, drenaje reforzado]

4. **L1.pista_tractocamiones_B3C3_completa** (Valor TBD)
   - Fuente: Tabla #21, Fila 3
   - Descripción: Infraestructura vehículos articulados
   - Componentes L0 asociados: TBD
     - L0.IC_004: Pavimento especial concreto Fc=35MPa
     - L0.VEH_005: Tractocamión B3/C3 articulado
     - L0.ILU_002: Luminaria LED 200W
     - [+ señalización, drenaje reforzado]

5. **L1.pista_clase_I** (Referencia jerárquica)
   - Fuente: Tabla #20, Fila 2
   - Descripción: Pista Clase I completa (suma de motos + carros)
   - Valor: $721.440.000
   - **IMPORTANTE:** Este es un componente de REFERENCIA, no constructor

6. **L1.pista_clase_II** (Referencia jerárquica)
   - Fuente: Tabla #21, Fila 2
   - Descripción: Pista Clase II completa (clase_I + camiones)
   - Valor: $1.407.390.000
   - **IMPORTANTE:** Este es un componente de REFERENCIA, no constructor

**OTROS COMPONENTES L1 (Edificaciones, etc.):**
- TBD: Revisar tablas de edificaciones para extraer L1 adicionales

### Nivel L0: Componentes Atómicos (91 total)

**CATEGORÍAS DE L0 IDENTIFICADAS:**

1. **IC - Infraestructura Civil** (4 componentes)
   - L0.IC_001: Pavimento flexible asfalto e=12cm
   - L0.IC_002: Pavimento rígido concreto Fc=21MPa e=15cm
   - L0.IC_003: Pavimento reforzado concreto Fc=28MPa e=20cm
   - L0.IC_004: Pavimento especial concreto Fc=35MPa e=25cm

2. **DR - Drenajes** (3 componentes)
   - L0.DR_001: Cuneta concreto perimetral
   - L0.DR_002: Sistema drenaje pluvial
   - L0.DR_003: Drenaje reforzado alta capacidad

3. **SV - Señalización Vial** (4 componentes)
   - L0.SV_001: Señalización horizontal termoplástica
   - L0.SV_002: Demarcación espacio vehicular
   - L0.SV_003: Conos reflectivos 90cm
   - L0.SV_004: Señalización vertical Tipo I

4. **SEG - Seguridad** (3 componentes)
   - L0.SEG_001: Baranda metálica contención
   - L0.SEG_002: Kit seguridad evaluación
   - L0.SEG_003: Sistema detección incendios

5. **EDIF/MAT - Edificación y Materiales** (~5 componentes)
   - L0.EDIF_001: Edificación principal CALE
   - L0.MAT_001: Construcción área sanitarios
   - L0.MAT_002: Concreto premezclado 3000 PSI
   - L0.MAT_003: Acero estructural ASTM A36

6. **ADEC - Adecuaciones** (5 componentes)
   - L0.ADEC_001: Adecuaciones Drywall completas
   - L0.ADEC_002: Drywall paredes y divisiones
   - L0.ADEC_003: Cielo raso suspendido
   - L0.ADEC_004: Piso vinílico LVT
   - L0.ADEC_005: Cubículos evaluación

7. **ELE - Instalaciones Eléctricas** (12 componentes)
   - L0.ELE_001: Acometida trifásica 220V 30A
   - L0.ELE_002: Instalaciones eléctricas complementarias
   - L0.ELE_003: Puesta tierra varilla 5/8"×2.4m
   - L0.ELE_004: Supresor de picos 6 tomas
   - L0.ELE_006: UPS 10kVA doble conversión
   - L0.ELE_007: Panel solar fotovoltaico 550Wp
   - L0.ELE_008: Inversor solar híbrido 10kW
   - L0.ELE_009: Batería litio 5kWh
   - L0.ELE_010: Controlador de carga solar MPPT 60A
   - L0.ELE_011: Estructura montaje paneles solares
   - L0.ELE_012: Cableado DC fotovoltaico 6mm²

8. **ILU - Iluminación** (2 componentes)
   - L0.ILU_001: Luminaria LED 150W poste 8m
   - L0.ILU_002: Luminaria LED 200W poste 10m

9. **HVAC - Climatización** (1 componente)
   - L0.HVAC_001: Sistema HVAC precision datacenter

10. **HID - Instalaciones Hidráulicas** (2 componentes)
    - L0.HID_001: Tubería PVC + válvulas
    - L0.HID_002: Baño completo instalado

11. **MOB - Mobiliario** (18 componentes)
    - L0.MOB_001: Escritorio ergonómico 1.20×0.60m
    - L0.MOB_002: Silla ergonómica ajustable
    - L0.MOB_003: Sillas universitarias
    - L0.MOB_004: Tablero acrílico 3.0×1.5m
    - L0.MOB_005: Mobiliario completo CALE
    - L0.MOB_006: Mobiliario aula informática
    - L0.MOB_007-012: Mobiliario oficinas y salas
    - L0.MOB_RECEPCION: Counter recepción
    - L0.MOB_SILLAS_ESPERA: Sillas tandem
    - L0.LOCKERS_ASPIRANTES: Locker metálico
    - L0.ARCHIVO_ACTIVO: Estantería archivo
    - L0.ARCHIVADOR_VERTICAL: Archivador 4 gavetas

12. **TEC - Tecnología** (10 componentes)
    - L0.TEC_001: PC Desktop Core i5
    - L0.TEC_002: Monitor LED Full HD 24"
    - L0.TEC_003: Teclado + Mouse USB
    - L0.TEC_004: Rack servidor 42U
    - L0.TEC_005: Servidor HP ProLiant DL380 Gen10
    - L0.TEC_006: Switch Gigabit 48 Puertos PoE+
    - L0.TEC_009: Cámara IP Seguridad 4MP PoE
    - L0.SALA_CONTROL_TEORICO: Estación supervisión
    - L0.SALA_CONTROL_PRACTICO: Centro control
    - L0.PLAT_TEC: Plataforma tecnológica CALE

13. **AV - Audiovisual** (3 componentes)
    - L0.AV_001: Video proyector 5000 lúmenes
    - L0.AV_002: Pantalla eléctrica 4.0×3.0m
    - L0.AV_003: Sistema audio amplificado

14. **ACC - Accesorios** (3 componentes)
    - L0.ACC_001: Mousepad ergonómico
    - L0.ACC_002: Equipamiento sala teórica
    - L0.ACC_003: Señalización interior

15. **VEH - Vehículos** (5 componentes)
    - L0.VEH_001: Motocicleta ≤125cc adaptada
    - L0.VEH_002: Motocicleta >125cc adaptada
    - L0.VEH_003: Automóvil B1/C1 adaptado
    - L0.VEH_004: Camión B2/C2 adaptado
    - L0.VEH_005: Tractocamión B3/C3 articulado

16. **SEG (Seguros)** + **CERT (Certificaciones)** (2 componentes)
    - L0.SEG_100: Paquete seguros obligatorios
    - L0.CERT_ISO: Paquete certificaciones ISO

17. **Circulación y Accesibilidad** (5 componentes)
    - L0.PASILLO_INTERNO: Pasillos interiores
    - L0.CIRCULACION_EXTERNA: Circulaciones exteriores
    - L0.RAMPA_ACCESIBILIDAD: Rampa acceso universal
    - L0.ESCALERA_INTERNA: Escalera principal
    - L0.ESCALERA_EMERGENCIA: Escalera emergencia

**TOTAL L0: 91 componentes atómicos**

---

## 🔑 CONCEPTO CLAVE: MANIOBRAS vs. COMPONENTES BIM

### ¿Qué son las MANIOBRAS?
Las maniobras (MANIOBRA_00 a MANIOBRA_19) **NO SON** componentes BIM independientes.

Son **especificaciones geométricas y funcionales** que describen:
- Trazados específicos de pista
- Áreas de maniobra (estacionamiento, paralelo, retroceso, etc.)
- Dimensiones y geometrías requeridas
- Capacidades funcionales de la infraestructura

### ¿Dónde están las maniobras en BIM?
Las maniobras están **EMBEBIDAS** dentro de los componentes L0 como:
- Geometría del pavimento (L0.IC_001-004)
- Diseño de señalización (L0.SV_001-004)
- Configuración espacial del conjunto

**Ejemplo:**
```
L0.IC_001 (Pavimento flexible asfalto)
  └─ Geometría incluye:
      ├─ MANIOBRA_00: Estacionamiento en línea
      ├─ MANIOBRA_01: Estacionamiento en batería
      ├─ MANIOBRA_02: Estacionamiento paralelo
      └─ ... (especificaciones geométricas)
```

---

## 📊 ESTADÍSTICAS FINALES

| Nivel | Cantidad | Descripción |
|-------|----------|-------------|
| **L3** | 4 | Configuraciones CALE completas |
| **L2** | ~5-7 | Pistas + edificaciones + parqueaderos |
| **L1** | 6 principales | Ensamblajes de infraestructura (pistas por categoría) |
| **L0** | 91 | Componentes atómicos (pavimentos, mobiliario, tecnología, etc.) |

---

## ✅ VALIDACIÓN

### ✅ Valores correctos
- L1.pista_motos_A1A2_completa: **$289.805.000** ✓
- L1.pista_carros_B1C1_completa: **$431.635.000** ✓
- **SUBTOTAL L1.pista_clase_I: $721.440.000** ✓

### ✅ Relaciones correctas
- L2.pista_clase_I → 2 componentes L1 (motos + carros) ✓
- L2.pista_clase_II → 2 componentes L1 (clase_I + camiones) ✓
- L2.pista_clase_III → 2 componentes L1 (clase_II + tractocamiones) ✓

### ✅ Mapeo L0→L1 correcto
- L0.IC_001 → L1.pista_motos_A1A2_completa ✓
- L0.IC_002 → L1.pista_carros_B1C1_completa ✓
- L0.IC_003 → L1.pista_camiones_B2C2_completa ✓
- L0.IC_004 → L1.pista_tractocamiones_B3C3_completa ✓

---

## 🚀 PRÓXIMOS PASOS

1. ✅ **COMPLETADO**: Extracción correcta de jerarquía BIM
2. ⏳ **PENDIENTE**: Regenerar `TABLAS_L0_OFICIALES.json` (91 componentes)
3. ⏳ **PENDIENTE**: Regenerar `TABLAS_L1_OFICIALES.json` (6+ componentes)
4. ⏳ **PENDIENTE**: Corregir `TABLAS_L2_OFICIALES.json` (5-7 configuraciones)
5. ⏳ **PENDIENTE**: Mantener `TABLAS_L3_OFICIALES.json` (probablemente correcto)
6. ⏳ **PENDIENTE**: Regenerar fichas L1 (4-6 fichas con L0 components)
7. ⏳ **PENDIENTE**: Regenerar fichas L2 (5 fichas con L1 components)
8. ⏳ **PENDIENTE**: Actualizar fichas L3 (4 fichas verificadas)
9. ⏳ **PENDIENTE**: Nuevo árbol de jerarquía BIM corregido
10. ⏳ **PENDIENTE**: Git commit reemplazando 310a0b7

---

**Archivo generado:** `JERARQUIA_BIM_CORRECTA.json` (1116 líneas)  
**Última actualización:** 2025-11-03
