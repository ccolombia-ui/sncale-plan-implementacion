# 📋 PLAN DE DESARROLLO BIM - NIVELES n0, n1, n2

**Fecha:** 2025-10-29  
**Estado:** ✅ Nivel n-1 (Atómicos) - Parcialmente completo  
**Estado:** 🔄 Nivel n0 - 1/15 productos  
**Estado:** ⏳ Nivel n1 - Pendiente  
**Estado:** ⏳ Nivel n2 - Pendiente  

---

## 🎯 OBJETIVO

Crear sistema BIM completo con referencias recursivas para SNCALE:
- **113 productos atómicos** (nivel n-1)
- **15 ensambles básicos** (nivel n0)
- **6 módulos estándar** (nivel n1)
- **5 configuraciones CALE** (nivel n2)

---

## ✅ NIVEL n-1: COMPONENTES ATÓMICOS

**Definición:** Productos sin subcomponentes, fuente única de verdad.

### Estado Actual: 5/113 completados

#### ✅ Completados (5)
1. **SILLA-ERG-001** - Silla Ergonómica ($450K)
2. **MESA-CUB-001** - Mesa Escritorio ($350K)
3. **DIV-MEL-1600** - Panel Divisor ($80K)
4. **LED-STRIP-12W** - Iluminación LED ($45K)
5. **CANAL-PVC-80** - Canaleta PVC ($15K)

#### ⏳ Pendientes (108)

##### Prioridad 1: Mobiliario (18 productos)
- **MESA-** (6 variantes)
  - [ ] MESA-DIR-001: Mesa Director 1800×900 ($650K)
  - [ ] MESA-CONF-001: Mesa Conferencia 2400×1200 ($1.2M)
  - [ ] MESA-REC-001: Mesa Recepción 1500×700 ($480K)
  - [ ] MESA-AUX-001: Mesa Auxiliar 800×600 ($180K)
  - [ ] MESA-INST-001: Mesa Instructor 1600×800 ($420K)
  - [x] MESA-CUB-001: Mesa Cubículo ✅

- **SILLA-** (5 variantes)
  - [x] SILLA-ERG-001: Silla Ergonómica ✅
  - [ ] SILLA-DIR-001: Silla Ejecutiva ($680K)
  - [ ] SILLA-VIS-001: Silla Visitante ($220K)
  - [ ] SILLA-CONF-001: Silla Conferencia ($380K)
  - [ ] SILLA-ESP-001: Silla Espera ($195K)

- **ARCHIV-** (3 variantes)
  - [ ] ARCHIV-ROD-001: Archivador Rodante 3 gavetas ($420K)
  - [ ] ARCHIV-VERT-001: Archivador Vertical 4 gavetas ($550K)
  - [ ] ARCHIV-LAT-001: Archivador Lateral ($380K)

- **DIVISON-** (4 variantes)
  - [x] DIV-MEL-1600: Panel 1600mm ✅
  - [ ] DIV-MEL-1200: Panel 1200mm ($65K)
  - [ ] DIV-VID-1600: Panel Vidrio 1600mm ($185K)
  - [ ] DIV-ACU-1600: Panel Acústico 1600mm ($145K)

##### Prioridad 2: Tecnología (12 productos)
- **TEC-** (Computación)
  - [ ] TEC-001: Computador All-in-One 24" ($2.8M)
  - [ ] TEC-002: Computador Desktop i5 ($2.2M)
  - [ ] TEC-003: Monitor 24" LED ($450K)
  - [ ] TEC-004: Teclado + Mouse ($85K)
  - [ ] TEC-005: Webcam HD ($180K)
  - [ ] TEC-006: Audífonos ($65K)

- **SERV-** (Servidores)
  - [ ] SERV-001: Servidor Dell R640 16 cores ($18M)
  - [ ] SERV-002: Servidor Storage 48TB ($12M)
  - [ ] SERV-003: Switch 48 puertos PoE ($3.5M)
  - [ ] SERV-004: UPS 10kVA ($8.5M)
  - [ ] SERV-005: Rack 42U ($2.2M)
  - [ ] SERV-006: PDU 32A ($850K)

##### Prioridad 3: Iluminación (8 productos)
- **LED-** (Iluminación)
  - [x] LED-STRIP-12W: Tira LED ✅
  - [ ] LED-PANEL-001: Panel LED 60×60 ($120K)
  - [ ] LED-DOWN-001: Downlight LED 12W ($45K)
  - [ ] LED-EMER-001: Luz Emergencia ($95K)
  - [ ] LED-SPOT-001: Spot LED direccional ($75K)
  - [ ] LED-SENSOR-001: Sensor movimiento ($35K)
  - [ ] LED-DRIVER-001: Driver 12V/60W ($28K)
  - [ ] LED-DIMMER-001: Dimmer inteligente ($65K)

##### Prioridad 4: Instalaciones Eléctricas (15 productos)
- **ELEC-** (Eléctricos)
  - [ ] ELEC-TOM-001: Tomacorriente doble ($12K)
  - [ ] ELEC-TOM-002: Tomacorriente regulado ($45K)
  - [ ] ELEC-INT-001: Interruptor simple ($8K)
  - [ ] ELEC-TAB-001: Tablero 12 circuitos ($380K)
  - [ ] ELEC-TIERRA-001: Sistema puesta a tierra ($850K)
  - [x] CANAL-PVC-80: Canaleta ✅
  - [ ] CANAL-METAL-001: Canaleta metálica ($35K)
  - [ ] COND-001: Conduit PVC 3/4" ($8K/m)
  - [ ] CABLE-POW-001: Cable 3×12 AWG ($15K/m)
  - [ ] CABLE-DATA-001: Cable UTP Cat6 ($2.5K/m)
  - [ ] FACE-RJ45-001: Faceplate RJ45 ($18K)
  - [ ] PATCH-001: Patch panel 24 puertos ($220K)
  - [ ] RACK-WALL-001: Rack pared 6U ($450K)
  - [ ] BANDEJA-001: Bandeja portacables ($25K/m)
  - [ ] PISO-TEC-001: Piso técnico 60×60 ($85K/m²)

##### Prioridad 5: Acabados (20 productos)
- **PISO-** (Pisos)
  - [ ] PISO-VINIL-001: Piso vinílico ($45K/m²)
  - [ ] PISO-CERAMICA-001: Piso cerámica ($35K/m²)
  - [ ] PISO-ALFOMBRA-001: Alfombra modular ($65K/m²)
  - [ ] PISO-MADERA-001: Piso laminado ($75K/m²)

- **PARED-** (Revestimientos)
  - [ ] PINTURA-INT-001: Pintura interior ($8K/m²)
  - [ ] PINTURA-EXT-001: Pintura exterior ($12K/m²)
  - [ ] REVEST-MADERA-001: Revestimiento madera ($95K/m²)
  - [ ] REVEST-ACUS-001: Panel acústico pared ($120K/m²)

- **CIELO-** (Cielorrasos)
  - [ ] CIELO-SUSP-001: Cielo suspendido 60×60 ($35K/m²)
  - [ ] CIELO-DRYWALL-001: Cielo drywall ($28K/m²)
  - [ ] CIELO-GYPSUM-001: Cielo yeso ($42K/m²)

- **PUER-** (Puertas)
  - [ ] PUER-MADERA-001: Puerta madera 0.90×2.10 ($650K)
  - [ ] PUER-VID-001: Puerta vidrio templado ($1.2M)
  - [ ] PUER-METAL-001: Puerta metálica ($480K)
  - [ ] PUER-EMERGENCIA-001: Puerta emergencia ($850K)

- **VENT-** (Ventanas)
  - [ ] VENT-ALU-001: Ventana aluminio 1.20×1.50 ($480K)
  - [ ] VENT-PVC-001: Ventana PVC 1.00×1.20 ($380K)
  - [ ] VENT-FIJA-001: Ventana fija vidrio ($320K)
  - [ ] PERSIANA-001: Persiana vertical ($125K)

##### Prioridad 6: Sanitarios (12 productos)
- **SANIT-** (Sanitarios)
  - [ ] SANIT-IND-001: Sanitario inodoro ($280K)
  - [ ] SANIT-LAV-001: Lavamanos ($185K)
  - [ ] SANIT-URI-001: Orinal ($165K)
  - [ ] SANIT-DUC-001: Ducha ($95K)
  - [ ] SANIT-ACCES-001: Accesorio set ($45K)
  - [ ] SANIT-ESPE-001: Espejo 60×80 ($85K)
  - [ ] SANIT-DISPEN-001: Dispensador papel ($25K)
  - [ ] SANIT-JABON-001: Dispensador jabón ($22K)
  - [ ] SANIT-SECA-001: Secador manos ($320K)
  - [ ] SANIT-MUEBLE-001: Mueble bajo lavabo ($280K)
  - [ ] SANIT-CANCEL-001: Cancel baño ($650K)
  - [ ] SANIT-ACCESIBLE-001: Set accesibilidad ($420K)

##### Prioridad 7: HVAC (10 productos)
- **HVAC-** (Climatización)
  - [ ] HVAC-SPLIT-001: Split 24000 BTU ($2.8M)
  - [ ] HVAC-VRF-001: VRF multi-split ($12M)
  - [ ] HVAC-FAN-001: Ventilador techo ($180K)
  - [ ] HVAC-EXTRACTOR-001: Extractor baño ($125K)
  - [ ] HVAC-REJILLA-001: Rejilla ventilación ($35K)
  - [ ] HVAC-DUCTO-001: Ducto rectangular ($45K/m)
  - [ ] HVAC-DIFUSOR-001: Difusor circular ($65K)
  - [ ] HVAC-TERMOSTATO-001: Termostato digital ($95K)
  - [ ] HVAC-FILTRO-001: Filtro aire HEPA ($120K)
  - [ ] HVAC-DESHUMID-001: Deshumidificador ($1.2M)

##### Prioridad 8: Seguridad (8 productos)
- **SEG-** (Seguridad)
  - [ ] SEG-CAM-001: Cámara IP 4MP ($650K)
  - [ ] SEG-NVR-001: NVR 16 canales ($2.2M)
  - [ ] SEG-CONTROL-001: Control acceso biométrico ($1.8M)
  - [ ] SEG-ALARMA-001: Panel alarma ($850K)
  - [ ] SEG-DETECTOR-001: Detector humo ($95K)
  - [ ] SEG-EXTINTOR-001: Extintor 10 lbs ($85K)
  - [ ] SEG-LUZ-EMER-001: Luz emergencia LED ($125K)
  - [ ] SEG-SEÑAL-001: Señalización evacuación ($15K)

##### Prioridad 9: Señalización (10 productos)
- **SEÑAL-** (Señalización)
  - [ ] SEÑAL-EVAC-001: Señal evacuación ($12K)
  - [ ] SEÑAL-ACCESO-001: Señal acceso ($15K)
  - [ ] SEÑAL-PROHIB-001: Señal prohibición ($12K)
  - [ ] SEÑAL-INFO-001: Señal informativa ($18K)
  - [ ] SEÑAL-BRAILLE-001: Señal braille ($25K)
  - [ ] SEÑAL-PISO-001: Señal piso táctil ($8K/m)
  - [ ] SEÑAL-RAMPA-001: Señal rampa accesible ($45K)
  - [ ] SEÑAL-BAÑO-001: Señal sanitarios ($22K)
  - [ ] SEÑAL-EXTINTOR-001: Señal extintor ($10K)
  - [ ] SEÑAL-SALIDA-001: Señal salida emergencia ($28K)

### 📊 Resumen Nivel n-1
- **Total productos:** 113
- **Completados:** 5 (4.4%)
- **Pendientes:** 108 (95.6%)
- **Inversión estimada total:** ~$850M COP

---

## 🔧 NIVEL n0: ENSAMBLES BÁSICOS

**Definición:** Productos compuestos por atomicos (nivel n-1).  
**Característica:** Usan referencias `$ref` a nivel n-1.

### Estado Actual: 1/15 completados

#### ✅ Completados (1)
1. **MOB-001** - Cubículo Evaluación ($1.1M)
   - Referencias: MESA-CUB-001, SILLA-ERG-001, DIV-MEL-1600×3, LED-STRIP-12W, CANAL-PVC-80

#### ⏳ Pendientes (14)

##### Prioridad 1: Estaciones de Trabajo (5)
- [x] **MOB-001** - Cubículo Evaluación 1200×800 ✅
- [ ] **MOB-002** - Cubículo Estándar 1000×700 ($850K)
  - Referencias: MESA-CUB-002, SILLA-ERG-001, DIV-MEL-1200×3
  
- [ ] **MOB-003** - Estación Instructor 1600×900 ($1.8M)
  - Referencias: MESA-INST-001, SILLA-DIR-001, ARCHIV-ROD-001, TEC-003×2
  
- [ ] **MOB-004** - Puesto Director 2000×1000 ($3.2M)
  - Referencias: MESA-DIR-001, SILLA-DIR-001, ARCHIV-VERT-001, TEC-001
  
- [ ] **MOB-005** - Recepción Completa 1500×700 ($2.5M)
  - Referencias: MESA-REC-001, SILLA-ERG-001×2, TEC-001, TELEFONO-001

##### Prioridad 2: Módulos Tecnológicos (4)
- [ ] **TEC-MOD-001** - Módulo Evaluación Completo ($3.5M)
  - Referencias: TEC-001, TEC-003, TEC-004, TEC-005, TEC-006, ELEC-TOM-002
  
- [ ] **TEC-MOD-002** - Módulo Formación ($4.2M)
  - Referencias: TEC-001, TEC-003×2, TEC-004, PIZARRA-DIGITAL-001
  
- [ ] **SERV-RACK-001** - Rack Servidor Completo ($45M)
  - Referencias: SERV-001×2, SERV-002, SERV-003, SERV-004, SERV-005, SERV-006
  
- [ ] **DATA-PATCH-001** - Panel Patcheo Completo ($1.2M)
  - Referencias: RACK-WALL-001, PATCH-001×2, SWITCH-24P-001, ORGANIZADOR-001

##### Prioridad 3: Módulos Sanitarios (3)
- [ ] **SANIT-MOD-001** - Módulo Sanitario Estándar ($2.8M)
  - Referencias: SANIT-IND-001, SANIT-LAV-001, SANIT-ESPE-001, SANIT-ACCES-001×5
  
- [ ] **SANIT-MOD-002** - Módulo Sanitario Accesible ($4.2M)
  - Referencias: SANIT-IND-001, SANIT-LAV-001, SANIT-ACCESIBLE-001, SANIT-CANCEL-001
  
- [ ] **SANIT-MOD-003** - Batería Sanitarios (Hombres) ($8.5M)
  - Referencias: SANIT-IND-001×3, SANIT-URI-001×2, SANIT-LAV-001×2

##### Prioridad 4: Sistemas Integrados (3)
- [ ] **ILUM-MOD-001** - Sistema Iluminación Sala ($850K)
  - Referencias: LED-PANEL-001×12, LED-EMER-001×2, LED-SENSOR-001×4, LED-DRIVER-001×4
  
- [ ] **SEG-MOD-001** - Sistema Seguridad Básico ($8.5M)
  - Referencias: SEG-CAM-001×8, SEG-NVR-001, SEG-CONTROL-001, SEG-ALARMA-001
  
- [ ] **HVAC-MOD-001** - Sistema Climatización Zona ($15M)
  - Referencias: HVAC-VRF-001, HVAC-DIFUSOR-001×8, HVAC-REJILLA-001×4, HVAC-TERMOSTATO-001

### 📊 Resumen Nivel n0
- **Total productos:** 15
- **Completados:** 1 (6.7%)
- **Pendientes:** 14 (93.3%)
- **Inversión estimada total:** ~$105M COP

---

## 🏗️ NIVEL n1: MÓDULOS ESTÁNDAR

**Definición:** Espacios funcionales compuestos por ensambles (nivel n0).  
**Característica:** Usan referencias `$ref` a nivel n0 y n-1.

### Estado Actual: 0/6 completados

#### ⏳ Pendientes (6)

##### Prioridad 1: Salas de Evaluación (5 configuraciones)
- [ ] **SALA-T-24q** - Sala Evaluación 24 Cubículos ($26.4M)
  - Layout: 6 filas × 4 columnas
  - Área: 120 m² (10×12m)
  - Referencias: MOB-001×24, ILUM-MOD-001×2, HVAC-MOD-001
  
- [ ] **SALA-T-16q** - Sala Evaluación 16 Cubículos ($17.6M)
  - Layout: 4 filas × 4 columnas
  - Área: 96 m² (8×12m)
  - Referencias: MOB-001×16, ILUM-MOD-001, HVAC-MOD-001
  
- [ ] **SALA-T-8q** - Sala Evaluación 8 Cubículos ($8.8M)
  - Layout: 2 filas × 4 columnas
  - Área: 64 m² (8×8m)
  - Referencias: MOB-001×8, ILUM-MOD-001, HVAC-SPLIT-001×2
  
- [ ] **SALA-T-4q** - Sala Evaluación 4 Cubículos ($4.4M)
  - Layout: 2 filas × 2 columnas
  - Área: 32 m² (8×4m)
  - Referencias: MOB-001×4, ILUM-MOD-001, HVAC-SPLIT-001
  
- [ ] **SALA-T-2q** - Sala Evaluación 2 Cubículos ($2.2M)
  - Layout: 1 fila × 2 columnas
  - Área: 24 m² (6×4m)
  - Referencias: MOB-001×2, LED-PANEL-001×6, HVAC-SPLIT-001

##### Prioridad 2: Módulo Formación (1)
- [ ] **MOD-FORM-001** - Aula Formación 30 personas ($18M)
  - Área: 72 m² (9×8m)
  - Referencias: 
    - MOB-003×1 (instructor)
    - MESA-CONF-001×1
    - SILLA-CONF-001×30
    - TEC-MOD-002×1 (proyector + pantalla)
    - ILUM-MOD-001×1
    - HVAC-MOD-001×1

### 📊 Resumen Nivel n1
- **Total productos:** 6
- **Completados:** 0 (0%)
- **Pendientes:** 6 (100%)
- **Inversión estimada total:** ~$77M COP

---

## 🏢 NIVEL n2: CONFIGURACIONES CALE COMPLETAS

**Definición:** Centros CALE completos (edificación funcional).  
**Característica:** Usan referencias `$ref` a niveles n1, n0 y n-1.

### Estado Actual: 0/5 completados

#### ⏳ Pendientes (5 categorías)

##### Categoría A+ (Grandes Capitales)
- [ ] **CALE-CAT-A-PLUS** - Centro CALE Categoría A+ ($243M)
  - Capacidad: 24 cubículos evaluación + formación + administración
  - Área construida: ~600 m²
  - Referencias:
    - SALA-T-24q×1 ($26.4M)
    - MOD-FORM-001×2 ($36M)
    - MOB-004×3 (director, subdirector, coordinador)
    - MOB-005×1 (recepción)
    - SANIT-MOD-002×2 (accesibles)
    - SANIT-MOD-003×2 (baterías H/M)
    - SERV-RACK-001×1 (datacenter)
    - SEG-MOD-001×1 (seguridad completa)
    - HVAC-MOD-001×3 (climatización total)

##### Categoría A (Ciudades Intermedias)
- [ ] **CALE-CAT-A** - Centro CALE Categoría A ($195M)
  - Capacidad: 16 cubículos
  - Área construida: ~480 m²
  - Referencias:
    - SALA-T-16q×1
    - MOD-FORM-001×1
    - MOB-004×2
    - MOB-005×1
    - SANIT-MOD-002×1
    - SANIT-MOD-001×2
    - SERV-RACK-001×1
    - SEG-MOD-001×1

##### Categoría B (Municipios Medianos)
- [ ] **CALE-CAT-B** - Centro CALE Categoría B ($125M)
  - Capacidad: 8 cubículos
  - Área construida: ~320 m²
  - Referencias:
    - SALA-T-8q×1
    - MOD-FORM-001×1
    - MOB-004×1
    - MOB-005×1
    - SANIT-MOD-001×2
    - DATA-PATCH-001×1
    - SEG-MOD-001×1 (reducido)

##### Categoría C1-C4 (Municipios Pequeños)
- [ ] **CALE-CAT-C** - Centro CALE Categoría C ($75M)
  - Capacidad: 4 cubículos
  - Área construida: ~180 m²
  - Referencias:
    - SALA-T-4q×1
    - MOB-004×1 (director)
    - SANIT-MOD-001×1
    - DATA-PATCH-001×1

##### Categoría C5 (Municipios Mínimos)
- [ ] **CALE-CAT-C5** - Centro CALE Categoría C5 ($45M)
  - Capacidad: 2 cubículos
  - Área construida: ~100 m²
  - Referencias:
    - SALA-T-2q×1
    - MOB-004×1
    - SANIT-MOD-001×1

### 📊 Resumen Nivel n2
- **Total productos:** 5 categorías
- **Completados:** 0 (0%)
- **Pendientes:** 5 (100%)
- **Inversión promedio:** $136M COP/centro

---

## 🚀 PLAN DE EJECUCIÓN

### Fase 1: Completar Atómicos Críticos (2-3 semanas)
**Objetivo:** 30 productos atómicos más usados

**Semana 1:** Mobiliario (15 productos)
- Día 1-2: MESA-* (6 variantes)
- Día 3-4: SILLA-* (4 variantes)
- Día 5: ARCHIV-* (3 variantes), DIV-* (2 faltantes)

**Semana 2:** Tecnología + Iluminación (15 productos)
- Día 1-2: TEC-* (6 productos)
- Día 3-4: SERV-* (6 productos)
- Día 5: LED-* (3 productos)

**Semana 3:** Instalaciones + Sanitarios (Resto según necesidad)

### Fase 2: Ensambles Nivel n0 (1 semana)
**Objetivo:** 14 ensambles faltantes

**Día 1-2:** Estaciones de trabajo (MOB-002 a MOB-005)
**Día 3-4:** Módulos tecnológicos (TEC-MOD-*, SERV-RACK-001)
**Día 5:** Módulos sanitarios e integrados

### Fase 3: Módulos Nivel n1 (3-4 días)
**Objetivo:** 6 módulos estándar

**Día 1:** Salas pequeñas (T-2q, T-4q)
**Día 2:** Salas medianas (T-8q, T-16q)
**Día 3:** Sala grande (T-24q)
**Día 4:** Módulo formación + validación

### Fase 4: Configuraciones Nivel n2 (2 días)
**Objetivo:** 5 categorías CALE

**Día 1:** Cat A+, Cat A, Cat B
**Día 2:** Cat C, Cat C5 + validación final

### Fase 5: Integración y Validación (3-5 días)
**Día 1:** Integrar JSON con HTML visualizadores
**Día 2:** Exportar IFC con referencias
**Día 3:** Validar precios recursivos completos
**Día 4:** Generar documentación automática
**Día 5:** Pruebas con usuarios + correcciones

---

## 📊 MÉTRICAS DE PROGRESO

### Estado Global
```
Nivel n-1 (Atómicos):    [██░░░░░░░░░░░░░░░░░░]  5/113  (4.4%)
Nivel n0 (Ensambles):    [█░░░░░░░░░░░░░░░░░░░]  1/15   (6.7%)
Nivel n1 (Módulos):      [░░░░░░░░░░░░░░░░░░░░]  0/6    (0%)
Nivel n2 (CALE):         [░░░░░░░░░░░░░░░░░░░░]  0/5    (0%)

Total General:           [░░░░░░░░░░░░░░░░░░░░]  6/139  (4.3%)
```

### Inversión Validada vs Total
```
Atómicos validados:      $1.14M     / $850M    (0.13%)
Ensambles validados:     $1.1M      / $105M    (1.05%)
Módulos validados:       $0         / $77M     (0%)
CALE validados:          $0         / $680M    (0%)

Total Sistema:           $2.24M     / $1,712M  (0.13%)
```

---

## 🎯 HITOS CLAVE

### ✅ Hito 1: Sistema Recursivo Funcional (COMPLETADO)
- [x] Generador JSON desde .desc.md
- [x] Verificador de referencias
- [x] Visualizador 2D básico
- [x] 5 atómicos + 1 ensamble de prueba

### 🔄 Hito 2: Mobiliario y Tecnología (En Progreso)
- [ ] 30 productos atómicos críticos
- [ ] 5 ensambles estaciones de trabajo
- [ ] Visualizador 2D completo

### ⏳ Hito 3: Salas de Evaluación
- [ ] 5 configuraciones salas (T-2q a T-24q)
- [ ] Visualizador 3D IFC
- [ ] Exportación automática BIM

### ⏳ Hito 4: Sistema CALE Completo
- [ ] 5 categorías CALE
- [ ] Presupuestos automáticos completos
- [ ] Dashboard interactivo 197 nodos

### ⏳ Hito 5: Producción
- [ ] 113 productos atómicos
- [ ] 15 ensambles
- [ ] 6 módulos
- [ ] 5 categorías
- [ ] Documentación completa
- [ ] Sistema desplegado

---

## 🛠️ HERRAMIENTAS A DESARROLLAR

### Generadores Automáticos
- [x] `generar_json_bim.py` - Convierte .desc.md → JSON
- [x] `verificar_referencias_json.py` - Valida coherencia
- [ ] `generar_desc_batch.py` - Crea .desc.md desde catálogo
- [ ] `exportar_ifc.py` - Genera IFC desde JSON
- [ ] `generar_presupuesto.py` - Calcula presupuestos completos

### Visualizadores
- [x] `visor_cubiculo.html` - Visualiza componente individual
- [ ] `visor_sala.html` - Visualiza sala completa
- [ ] `visor_cale.html` - Visualiza CALE completo
- [ ] `comparador.html` - Compara configuraciones
- [ ] `dashboard_nacional.html` - 197 nodos en mapa

### Validadores
- [ ] `validar_precios.py` - Verifica coherencia presupuestos
- [ ] `validar_dimensiones.py` - Verifica coherencia espacial
- [ ] `validar_normativa.py` - Verifica cumplimiento NSR-10, NTC

---

## 📝 NOTAS IMPORTANTES

### Priorización Justificada
1. **Mobiliario primero:** Es lo que más se replica (cubículos, mesas, sillas)
2. **Tecnología después:** Alto costo unitario, impacta presupuesto
3. **Sanitarios e instalaciones:** Estándares, menos variabilidad
4. **Acabados al final:** Más flexibles, menos críticos

### Optimizaciones Posibles
- **Generación batch:** Script que crea 20 .desc.md similares cambiando dimensiones
- **Templates por categoría:** Plantilla base para MESA-*, SILLA-*, etc.
- **IA asistida:** GPT-4 genera descripciones desde especificaciones texto

### Riesgos
- ⚠️ **Tiempo:** 113 productos × 30min/producto = ~56 horas trabajo manual
- ⚠️ **Coherencia:** Precios deben validarse contra mercado real
- ⚠️ **Normativa:** Cada producto debe cumplir NTC/NSR aplicable

---

**Próximo paso inmediato:** Validar que `visor_cubiculo.html` funcione correctamente, luego proceder con batch de mobiliario (MESA-*, SILLA-*).
