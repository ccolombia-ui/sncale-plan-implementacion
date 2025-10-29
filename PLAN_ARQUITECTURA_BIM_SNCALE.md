# 🏗️ PLAN MAESTRO: ARQUITECTURA BIM PARA SNCALE

**Sistema Nacional de Centros de Asesoría y Licenciamiento**

**Fecha:** 2025-10-23
**Versión:** 1.0
**Estado:** 📋 PLAN PROPUESTO - PENDIENTE APROBACIÓN

---

## 📋 RESUMEN EJECUTIVO

### Objetivo
Crear una **biblioteca completa de objetos BIM paramétricos y reutilizables** para los 197 nodos CALE (56 principales + 141 satélites) que conforman el Sistema Nacional.

### Alcance
- **197 configuraciones de nodos** (10 tipos principales + variantes)
- **Componentes BIM recursivos** (pistas, salas, datacenters, etc.)
- **Sistema de ensamblaje automático** en FreeCAD
- **Exportación a formatos estándar** (IFC4, JSON-BIM)
- **Integración futura con QGIS** para geolocalización
- **Conexión con pricing** CAMACOL/SECOP

---

## 📊 INVENTARIO DE OBJETOS BIM EXISTENTES

### ✅ Objetos Actuales (5 archivos)

| Archivo | Tipo | Descripción | LOD | Estado |
|---------|------|-------------|-----|--------|
| `CALE-T-24q_oficial_munay_4.1.json` | Teórico | 24 cubículos teóricos (Cat.A) | LOD_400 | ✅ Completo |
| `CALE-T-16q_oficial_munay_4.1.json` | Teórico | 16 cubículos teóricos (Cat.B) | LOD_400 | ✅ Completo |
| `CALE-P-CLASE1_oficial_munay_4.1.json` | Pista | Pista Clase I (livianos) | LOD_400 | ✅ Completo |
| `CALE-P-CLASE2_oficial_munay_4.1.json` | Pista | Pista Clase II (medianos) | LOD_400 | ✅ Completo |
| `CALE-P-CLASE3_oficial_munay_4.1.json` | Pista | Pista Clase III (pesados) | LOD_400 | ✅ Completo |

**Total existentes:** 5 objetos BIM base

---

## 🎯 ARQUITECTURA PROPUESTA: OBJETOS BIM REQUERIDOS

### Nivel 1: COMPONENTES ATÓMICOS (Building Blocks)

Estos son los **componentes básicos reutilizables** que se ensamblan para formar nodos completos.

#### 1.1 Componentes Teóricos

| ID | Componente | Capacidad | Área (m²) | CAPEX (COP) | Archivo Fuente |
|----|------------|-----------|-----------|-------------|----------------|
| **T-24q** | Sala teórica 24 cubículos | 24 simultáneos | 240 | $54,000,000 | ✅ Existente |
| **T-16q** | Sala teórica 16 cubículos | 16 simultáneos | 160 | $36,000,000 | ✅ Existente |
| **T-8q** | Sala teórica 8 cubículos | 8 simultáneos | 80 | $18,000,000 | ❌ **FALTA CREAR** |
| **T-4q** | Sala teórica 4 cubículos | 4 simultáneos | 40 | $9,000,000 | ❌ **FALTA CREAR** |
| **T-2q** | Sala teórica 2 cubículos | 2 simultáneos | 20 | $4,500,000 | ❌ **FALTA CREAR** |

#### 1.2 Componentes Prácticos (Pistas)

| ID | Componente | Tipo Vehículo | Área (m²) | CAPEX (COP) | Archivo Fuente |
|----|------------|---------------|-----------|-------------|----------------|
| **P-C3** | Pista Clase III | Pesados (>10.5 ton) | 3,236 | $2,500,000,000 | ✅ Existente |
| **P-C2** | Pista Clase II | Medianos (3.5-10.5 ton) | 2,100 | $1,600,000,000 | ✅ Existente |
| **P-C1** | Pista Clase I | Livianos (<3.5 ton) | 1,500 | $1,200,000,000 | ✅ Existente |

#### 1.3 Componentes de Infraestructura

| ID | Componente | Descripción | Área (m²) | CAPEX (COP) | Estado |
|----|------------|-------------|-----------|-------------|--------|
| **DC-001** | Datacenter básico | Centro de cómputo + energía solar | 40 | $17,980,000 | ❌ **FALTA CREAR** |
| **ADM-001** | Área administrativa | Oficinas + recepción | 120 | $45,000,000 | ❌ **FALTA CREAR** |
| **SERV-001** | Servicios generales | Baños + archivo + mantenimiento | 80 | $25,000,000 | ❌ **FALTA CREAR** |
| **SEG-001** | Seguridad y control | Control acceso + vigilancia | 30 | $12,000,000 | ❌ **FALTA CREAR** |

#### 1.4 Componentes Modulares (Contenedores)

| ID | Componente | Tipo | Dimensiones | CAPEX (COP) | Estado |
|----|------------|------|-------------|-------------|--------|
| **MOD-40HC** | Contenedor 40' HC | ISO High Cube | 12.2×2.4×2.9m | $80,000,000 | ❌ **FALTA CREAR** |
| **MOD-20** | Contenedor 20' | ISO estándar | 6.1×2.4×2.6m | $40,000,000 | ❌ **FALTA CREAR** |

---

### Nivel 2: CONFIGURACIONES DE NODOS (Ensamblajes)

Estos son **ensamblajes de componentes atómicos** que forman nodos CALE completos.

#### 2.1 Categoría A - Nodos Metropolitanos (20 nodos)

| Config | Descripción | Componentes | Demanda | Cantidad | Estado |
|--------|-------------|-------------|---------|----------|--------|
| **Cat.A** | Básico solo C3 | T-24q + P-C3 + DC + ADM + SERV | <10K | 2 | ❌ **FALTA** |
| **Cat.A+C1** | Con pistas C1 | T-24q + P-C3 + 2×P-C1 + DC + ADM | 10-52K | 11 | ❌ **FALTA** |
| **Cat.A+C2+C1** | Con C2 y C1 | T-24q + P-C3 + P-C2 + 2×P-C1 + DC | 52-60K | 3 | ❌ **FALTA** |
| **Cat.A+C2+C1***  | 3 pistas C1 | T-24q + P-C3 + P-C2 + 3×P-C1 + DC | ~50K | 2 | ❌ **FALTA** |
| **Cat.A+C2+C1**** | 4 pistas C1 (ampliado) | T-24q + P-C3 + P-C2 + 4×P-C1 + DC | 57-80K | 3 | ❌ **FALTA** |

**Subtotal Cat.A:** 5 configuraciones únicas

#### 2.2 Categoría B - Nodos Subregionales (20 nodos)

| Config | Descripción | Componentes | Demanda | Cantidad | Estado |
|--------|-------------|-------------|---------|----------|--------|
| **Cat.B** | Solo teórico | T-16q + ADM (sin pistas) | 2-8K | 4 | ❌ **FALTA** |
| **Cat.B** | Con pistas C2+C1 | T-16q + P-C2 + 2×P-C1 + MOD-40HC | 8-34K | 16 | ❌ **FALTA** |

**Subtotal Cat.B:** 2 configuraciones únicas

#### 2.3 Categoría C1 - Nodos Micro-regionales (16 nodos)

| Config | Descripción | Componentes | Demanda | Cantidad | Estado |
|--------|-------------|-------------|---------|----------|--------|
| **Cat.C1** | Evaluación C1 | T-8q + P-C1 + MOD-20 | 6-16K | 16 | ❌ **FALTA** |

**Subtotal Cat.C1:** 1 configuración única

#### 2.4 Satélites C2-C5 (141 nodos)

| Config | Descripción | Componentes | Demanda | Cantidad | Estado |
|--------|-------------|-------------|---------|----------|--------|
| **Cat.C2** | Satélite medio | T-4q (adaptado) | 3-7.5K | 50 | ❌ **FALTA** |
| **Cat.C3** | Satélite pequeño | T-2q (adaptado) | 1.5-3K | 45 | ❌ **FALTA** |
| **Cat.C4** | Satélite micro | T-2q (básico) | 800-1.5K | 30 | ❌ **FALTA** |
| **Cat.C5** | Satélite mínimo | T-2q (mínimo) | 300-800 | 16 | ❌ **FALTA** |

**Subtotal Satélites:** 4 configuraciones únicas

---

### Nivel 3: RED SATÉLITE (Agrupaciones)

Cada nodo Cat.A coordina **7 satélites** promedio (C2-C5).

| Agrupación | Descripción | Componentes | Cantidad | Estado |
|------------|-------------|-------------|----------|--------|
| **Red-Cat.A** | 1 Cat.A + 7 satélites | Cat.A + mix(C2,C3,C4,C5) | 20 redes | ❌ **FALTA** |

---

## 🔢 RESUMEN CUANTITATIVO

### Objetos BIM a Crear

| Nivel | Tipo | Existentes | Faltantes | Total |
|-------|------|------------|-----------|-------|
| **Nivel 1: Atómicos** | Componentes base | 5 | 9 | 14 |
| **Nivel 2: Nodos** | Configuraciones ensambladas | 0 | 12 | 12 |
| **Nivel 3: Redes** | Agrupaciones satélites | 0 | 1 | 1 |
| **TOTAL** | | **5** | **22** | **27** |

### Estadísticas

- ✅ **Objetos existentes:** 5 (18.5%)
- ❌ **Objetos faltantes:** 22 (81.5%)
- 🎯 **Cobertura requerida:** 197 nodos físicos
- 📦 **Configuraciones únicas:** 12 tipos de nodo

---

## 🏗️ ARQUITECTURA TÉCNICA PROPUESTA

### Stack Tecnológico

```
┌─────────────────────────────────────────┐
│   INTERFAZ USUARIO (Claude Code)        │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│   SERVICIO: services/bim_cale/          │
│   ├── biblioteca/  (componentes base)   │
│   ├── ensamblajes/ (configuraciones)    │
│   ├── parametros/  (variables config)   │
│   └── exportadores/ (IFC, JSON-BIM)     │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│   MOTOR 3D: FreeCAD 1.0                 │
│   - Python API                          │
│   - Modelado paramétrico                │
│   - Operaciones booleanas               │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│ EXPORTACIÓN   │   │ VISUALIZACIÓN │
│ - IFC4        │   │ - FreeCAD GUI │
│ - JSON-BIM    │   │ - Web viewer  │
│ - STEP        │   │               │
└───────────────┘   └───────────────┘
```

### Estructura de Datos BIM

```json
{
  "component": {
    "id": "string (único)",
    "type": "atomic|node|network",
    "ifc_class": "IfcBuilding|IfcSpace|IfcSlab",
    "geometry": {
      "primitive": "box|cylinder|mesh",
      "parameters": {
        "length": "float (mm)",
        "width": "float (mm)",
        "height": "float (mm)"
      }
    },
    "properties": {
      "area_m2": "float",
      "capacity": "int",
      "cost_cop": "float"
    },
    "children": ["component_id"],
    "position": [x, y, z],
    "rotation": [rx, ry, rz]
  }
}
```

---

## 📐 SISTEMA DE PARÁMETROS

### Parámetros Globales

```python
GLOBAL_PARAMS = {
    # Estándares colombianos
    "altura_piso_techo": 3000,  # mm (NSR-10)
    "espesor_muro": 150,  # mm
    "modulo_cubicul o": 1200,  # mm (ancho estándar)

    # Pistas (INVIAS)
    "ancho_carril": 3500,  # mm
    "radio_minimo_giro": 12000,  # mm

    # Energía
    "potencia_solar_kw": 5.0,
    "capacidad_bateria_kwh": 10.0,

    # Costos base (COP)
    "costo_m2_construccion": 2500000,
    "costo_m2_pista": 850000,
    "costo_cubicu lo_equipado": 2250000
}
```

### Parámetros por Configuración

Cada configuración tendrá un archivo YAML:

```yaml
# config_cat_a_c2_c1.yaml
config:
  id: "cat_a_c2_c1"
  nombre: "Cat.A + C2 + C1"
  demanda_min: 52000
  demanda_max: 60000

componentes:
  teorico:
    - type: "T-24q"
      quantity: 1

  practico:
    - type: "P-C3"
      quantity: 1
    - type: "P-C2"
      quantity: 1
    - type: "P-C1"
      quantity: 2

  infraestructura:
    - type: "DC-001"
      quantity: 1
    - type: "ADM-001"
      quantity: 1
    - type: "SERV-001"
      quantity: 1

costos:
  capex_total: 243063465  # COP
  opex_anual: 2400000000  # COP

personal:
  total: 32
  roles:
    - coordinador: 1
    - evaluadores: 20
    - instructores: 8
    - administrativos: 3
```

---

## 🔄 FLUJO DE TRABAJO

### Fase 1: Componentes Atómicos (Semanas 1-3)

```
1. Crear componente T-8q
2. Crear componente T-4q
3. Crear componente T-2q
4. Crear componente DC-001
5. Crear componente ADM-001
6. Crear componente SERV-001
7. Crear componente SEG-001
8. Crear componente MOD-40HC
9. Crear componente MOD-20
```

**Entregable:** 14 componentes BIM atómicos (5 existentes + 9 nuevos)

### Fase 2: Configuraciones de Nodos (Semanas 4-6)

```
10. Ensamblar Cat.A (básico)
11. Ensamblar Cat.A+C1
12. Ensamblar Cat.A+C2+C1
13. Ensamblar Cat.A+C2+C1***
14. Ensamblar Cat.A+C2+C1****
15. Ensamblar Cat.B (teórico)
16. Ensamblar Cat.B** (con pistas)
17. Ensamblar Cat.C1
18. Ensamblar Cat.C2 (satélite)
19. Ensamblar Cat.C3 (satélite)
20. Ensamblar Cat.C4 (satélite)
21. Ensamblar Cat.C5 (satélite)
```

**Entregable:** 12 configuraciones de nodos completas

### Fase 3: Sistema de Ensamblaje Automático (Semana 7)

```
22. Motor de ensamblaje basado en YAML
23. Validador de configuraciones
24. Calculadora de costos automática
25. Generador de reportes BIM
```

**Entregable:** Sistema automatizado de generación de nodos

### Fase 4: Exportación y Validación (Semana 8)

```
26. Exportador IFC4
27. Exportador JSON-BIM (compatibilidad con JSON existentes)
28. Validación contra estándares colombianos
29. Documentación técnica completa
```

**Entregable:** Biblioteca BIM completa exportable

---

## 📁 ESTRUCTURA DE ARCHIVOS PROPUESTA

```
services/
└── bim_cale/
    ├── README.md
    ├── scripts/
    │   ├── bim_builder.py          # Motor principal
    │   ├── component_library.py     # Biblioteca de componentes
    │   ├── assembler.py             # Ensamblador de nodos
    │   ├── exporter_ifc.py          # Exportador IFC4
    │   └── exporter_jsonbim.py      # Exportador JSON-BIM
    │
    ├── components/                  # Componentes atómicos
    │   ├── teoricos/
    │   │   ├── T-24q.py
    │   │   ├── T-16q.py
    │   │   ├── T-8q.py
    │   │   ├── T-4q.py
    │   │   └── T-2q.py
    │   ├── pistas/
    │   │   ├── P-C3.py
    │   │   ├── P-C2.py
    │   │   └── P-C1.py
    │   ├── infraestructura/
    │   │   ├── DC-001.py
    │   │   ├── ADM-001.py
    │   │   ├── SERV-001.py
    │   │   └── SEG-001.py
    │   └── modulares/
    │       ├── MOD-40HC.py
    │       └── MOD-20.py
    │
    ├── configuraciones/             # Configs de nodos
    │   ├── cat_a_basico.yaml
    │   ├── cat_a_c1.yaml
    │   ├── cat_a_c2_c1.yaml
    │   ├── cat_a_c2_c1_3.yaml
    │   ├── cat_a_c2_c1_4.yaml
    │   ├── cat_b_teorico.yaml
    │   ├── cat_b_pistas.yaml
    │   ├── cat_c1.yaml
    │   ├── cat_c2.yaml
    │   ├── cat_c3.yaml
    │   ├── cat_c4.yaml
    │   └── cat_c5.yaml
    │
    ├── parametros/
    │   └── global_params.py
    │
    ├── output/                      # Salidas generadas
    │   ├── ifc/
    │   ├── json_bim/
    │   └── freecad/
    │
    ├── tests/
    │   ├── test_components.py
    │   ├── test_assembler.py
    │   └── test_exporters.py
    │
    └── docs/
        ├── ARQUITECTURA.md
        ├── COMPONENTES.md
        ├── CONFIGURACIONES.md
        └── API.md
```

---

## 🎯 ENTREGABLES FINALES

### 1. Biblioteca de Componentes BIM
- **14 componentes atómicos** parametrizables en FreeCAD
- **12 configuraciones de nodos** ensambladas
- **Documentación técnica completa**

### 2. Sistema de Ensamblaje Automático
- Motor Python que lee YAML y genera nodos 3D
- Validación automática de configuraciones
- Cálculo automático de costos y áreas

### 3. Exportadores
- **IFC4**: Estándar internacional BIM
- **JSON-BIM**: Formato compatible con MUNAY 4.1 existente
- **STEP**: Para interoperabilidad CAD

### 4. Integración
- Conectado con **FreeCAD MCP** (ya operativo)
- Preparado para **QGIS MCP** (geolocalización)
- Preparado para **Pricing MCP** (CAMACOL/SECOP)

---

## 🚀 ROADMAP DE IMPLEMENTACIÓN

| Fase | Duración | Entregables | Dependencias |
|------|----------|-------------|--------------|
| **Fase 1: Componentes** | 3 semanas | 9 componentes nuevos | FreeCAD MCP operativo ✅ |
| **Fase 2: Nodos** | 3 semanas | 12 configuraciones | Fase 1 completa |
| **Fase 3: Automatización** | 1 semana | Sistema ensamblaje | Fase 2 completa |
| **Fase 4: Exportación** | 1 semana | Exportadores IFC/JSON | Fase 3 completa |
| **TOTAL** | **8 semanas** | Biblioteca BIM completa | - |

---

## 💰 ESTIMACIÓN DE ESFUERZO

| Tarea | Horas | Complejidad |
|-------|-------|-------------|
| Componentes atómicos (9×) | 72h | Media |
| Configuraciones nodos (12×) | 48h | Baja |
| Motor de ensamblaje | 24h | Alta |
| Exportadores (2×) | 16h | Media |
| Testing y validación | 20h | Media |
| Documentación | 12h | Baja |
| **TOTAL** | **192h** (~**24 días hábiles**) | |

---

## ⚠️ RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Complejidad de FreeCAD Python API | Media | Alto | Usar componentes existentes como template |
| Incompatibilidad con JSON existentes | Baja | Alto | Validar estructura temprano (Fase 1) |
| Performance en ensamblajes grandes | Media | Medio | Optimizar geometría, usar LOD dinámico |
| Cambios en especificaciones CALE | Alta | Medio | Sistema paramétrico adaptable |

---

## ✅ CRITERIOS DE ACEPTACIÓN

### Para Componentes Atómicos
- ✅ Modelado paramétrico funcional
- ✅ Dimensiones según especificaciones MUNAY 4.1
- ✅ Costos calculados automáticamente
- ✅ Exportable a IFC4 y JSON-BIM

### Para Configuraciones de Nodos
- ✅ Ensamblaje correcto de componentes
- ✅ Áreas y costos validados vs INFORME_FINAL
- ✅ Todos los 12 tipos implementados
- ✅ Generación automática desde YAML

### Para Sistema Completo
- ✅ Genera los 197 nodos sin errores
- ✅ Archivos IFC válidos (validador IfcOpenShell)
- ✅ JSON-BIM compatible con archivos existentes
- ✅ Documentación completa y ejemplos

---

## 📝 NOTAS IMPORTANTES

### Compatibilidad con Archivos Existentes
Los 5 archivos JSON-BIM existentes deben:
- ✅ **Mantenerse sin cambios** (backward compatibility)
- ✅ **Servir como referencia** para estructura JSON
- ✅ **Integrarse** con nuevos componentes generados

### Estándares Colombianos
Todos los componentes deben cumplir:
- NSR-10 (Norma Sismo Resistente)
- RETIE (Reglamento Técnico de Instalaciones Eléctricas)
- INVIAS (Normas para pistas de evaluación)
- ANSV (Agencia Nacional de Seguridad Vial)

### Naming Conventions
```
Componentes: [TIPO]-[CAPACIDAD]
  Ejemplo: T-24q, P-C3, MOD-40HC

Configuraciones: cat_[categoria]_[variante]
  Ejemplo: cat_a_c2_c1, cat_b_pistas

Archivos exportados: [NODO_ID]_[CONFIG]_[TIMESTAMP]
  Ejemplo: CALE-BOG-SUR_cat_a_c2_c1_4_20251023.ifc
```

---

## 🎯 PRÓXIMOS PASOS

### Para Aprobar Este Plan:

1. **Revisar arquitectura propuesta**
   - ¿Es correcta la división en 3 niveles (Atómicos/Nodos/Redes)?
   - ¿Faltan componentes o configuraciones?
   - ¿La estructura de archivos es adecuada?

2. **Validar el inventario**
   - ¿Los 12 tipos de nodo cubren todas las configuraciones?
   - ¿Los componentes atómicos son suficientes?

3. **Confirmar prioridades**
   - ¿Empezamos con Fase 1 (componentes atómicos)?
   - ¿O hay alguna configuración crítica que debamos hacer primero?

4. **Aprobar naming y estándares**
   - ¿Nombres de componentes son claros?
   - ¿Sistema de parámetros es adecuado?

---

## ❓ DECISIONES PENDIENTES

- [ ] ¿Aprobada la arquitectura de 3 niveles?
- [ ] ¿Inventario de 27 objetos BIM es completo?
- [ ] ¿Sistema paramétrico YAML es adecuado?
- [ ] ¿Estructura de carpetas `services/bim_cale/` es correcta?
- [ ] ¿Roadmap de 8 semanas es aceptable?
- [ ] ¿Comenzamos con Fase 1 (componentes atómicos)?

---

**🔴 IMPORTANTE:** Este es un plan propuesto. **NO iniciaremos implementación** hasta recibir confirmación de que esta arquitectura es correcta y completa.

---

**Fin del Plan Maestro**
**Estado:** 📋 Esperando aprobación
**Versión:** 1.0
**Fecha:** 2025-10-23
