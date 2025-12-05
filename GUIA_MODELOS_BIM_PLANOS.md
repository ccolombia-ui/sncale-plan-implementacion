# GUÍA: MODELOS BIM Y PLANOS ARQUITECTÓNICOS
## SISTEMA NACIONAL CALE

---

**Fecha:** 2025-10-23
**Versión:** 1.0
**Autor:** Alianza MUNAY - MinTransporte

---

## ÍNDICE

1. [Introducción](#introducción)
2. [Modelos BIM Generados](#modelos-bim-generados)
3. [Planos 2D Arquitectónicos](#planos-2d-arquitectónicos)
4. [Cómo Abrir y Usar los Modelos](#cómo-abrir-y-usar-los-modelos)
5. [Exportación a Otros Formatos](#exportación-a-otros-formatos)

---

## INTRODUCCIÓN

Este documento describe los modelos BIM 3D y planos 2D generados para el Sistema Nacional CALE, basados en el **[Catálogo de Inventario BIM Definitivo](CATALOGO_INVENTARIO_BIM_DEFINITIVO.md)** con 109 productos atómicos.

### Estándares Utilizados

- **BIM:** Industry Foundation Classes (IFC) ISO 16739
- **CAD:** FreeCAD 1.0 (formato nativo .FCStd)
- **Planos:** DXF (AutoCAD compatible), PDF
- **LOD (Level of Development):** LOD 300 (diseño detallado)

### Herramientas

- **Modelado 3D:** FreeCAD 1.0
- **Visualización:** FreeCAD, Blender, Autodesk Viewer
- **Planos 2D:** FreeCAD TechDraw, AutoCAD (DXF)

---

## MODELOS BIM GENERADOS

### 1. CALE-T-24q: Sala de Evaluación Teórica (24 cubículos)

**Archivo:** `services/auto_freeCAD/projects/CALE_T24q_BIM.FCStd`

**Descripción:**
- Sala de evaluación teórica para CALE Categoría A
- 24 cubículos de evaluación distribuidos en layout 6×4
- Infraestructura completa: muros, piso, zona instructor

**Componentes del Modelo:**

| Componente | Cantidad | IFC Class | Precio Unitario | Total |
|------------|----------|-----------|-----------------|-------|
| **Cubículo MOB-001** | 24 | IfcFurniture | $1,100,000 | $26,400,000 |
| Muros perimetrales | 4 | IfcWall | - | Incluido |
| Piso sala | 1 | IfcSlab | - | Incluido |
| Escritorio instructor | 1 | IfcFurniture | $2,000,000 | $2,000,000 |
| Pizarra | 1 | IfcFurnishingElement | - | Incluido |
| Puerta acceso universal | 1 | IfcDoor | $1,800,000 | $1,800,000 |

**Dimensiones:**
- Ancho: 8.0 m
- Largo: 10.0 m
- Alto: 3.0 m
- Área neta: 48 m²

**Precio Total Sala:** $243,063,465 (incluye toda la infraestructura Cat.A)

**Propiedades BIM Incluidas:**
```python
Cubiculo_01:
  BIM_ID: "MOB-001"
  IFC_Class: "IfcFurniture"
  Precio_Unitario: 1100000.0
  Dimensiones: 1.2m × 0.8m × 1.6m
```

**Captura de Pantalla (vista isométrica):**

```
┌─────────────────────────────────────┐
│  CALE-T-24q - Sala Evaluación      │
│  Vista Isométrica 3D                │
│                                      │
│  ┌──────────────────────────────┐  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │1│ │2│ │3│ │4│  Fila 1      │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │5│ │6│ │7│ │8│  Fila 2      │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │9│ │10 │11 │12│  Fila 3     │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │13 │14 │15 │16│  Fila 4     │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │17 │18 │19 │20│  Fila 5     │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐              │  │
│  │ │21 │22 │23 │24│  Fila 6     │  │
│  │ └─┘ └─┘ └─┘ └─┘              │  │
│  │                                │  │
│  │ [Instructor] [Pizarra]        │  │
│  │                                │  │
│  └──────────────────────────────┘  │
│                                      │
│  24 cubículos × $1.1M = $26.4M     │
└─────────────────────────────────────┘
```

---

### 2. CALE-P: Sala de Simuladores Prácticos (3 simuladores)

**Archivo:** `services/auto_freeCAD/projects/CALE_P_Simuladores_BIM.FCStd` (próximo modelo)

**Descripción:**
- Sala de simuladores de conducción para evaluación práctica
- 3 simuladores: Básico (A1,A2,B1), Avanzado (B2,B3), Pesados (C1,C2,C3)
- Área requerida: 15m × 10m

**Componentes del Modelo:**

| Componente | Cantidad | IFC Class | Precio Unitario | Total |
|------------|----------|-----------|-----------------|-------|
| **Simulador Básico SIM-001** | 1 | IfcTransportElement | $180,000,000 | $180,000,000 |
| **Simulador Avanzado SIM-002** | 1 | IfcTransportElement | $320,000,000 | $320,000,000 |
| **Simulador Pesados SIM-003** | 1 | IfcTransportElement | $450,000,000 | $450,000,000 |
| Muros perimetrales | 4 | IfcWall | - | Incluido |
| Piso reforzado | 1 | IfcSlab | - | Incluido |

**Precio Total Equipamiento:** $950,000,000

**Características Simuladores:**

**SIM-001: Simulador Básico**
- Categorías: A1 (motos ≤125cc), A2 (motos >125cc), B1 (automóviles)
- 3 pantallas LED 55" (180° campo visual)
- Asiento ajustable auto/moto intercambiable
- Pedales: acelerador, freno, embrague (±2% precisión)
- Volante force feedback 900°
- Software: 50+ escenarios Colombia
- IA tráfico: 50+ vehículos NPC
- Integración MUNAY 1.0
- Durabilidad: 30,000 horas

**SIM-002: Simulador Avanzado**
- Categorías: B2 (buses 9+ pasajeros), B3 (articulados pasajeros)
- Cabina real de bus
- 5 pantallas LED 65" (240° campo visual)
- Espejos retrovisores LCD 15"
- Sistemas bus: puertas neumáticas, suspensión, freno motor
- Escenarios BRT: TransMilenio, Metrolínea, MÍO, Megabús
- Simulación pasajeros virtuales

**SIM-003: Simulador Pesados**
- Categorías: C1 (camionetas), C2 (camiones >10.5 ton), C3 (tracto-camiones)
- Cabina tracto-camión Kenworth/Freightliner
- Sistemas: motor diésel, frenos aire, retardador
- Acoplamiento quinta rueda
- Escenarios montaña: Bogotá-Villavicencio, Medellín-Costa
- Sistema anti-jackknife

---

## PLANOS 2D ARQUITECTÓNICOS

### Planos Generados Automáticamente

Para cada modelo BIM se generan automáticamente los siguientes planos:

#### 1. Planta Arquitectónica (Vista Superior)

**Archivo:** `CALE_T24q_BIM_planta.dxf`

**Contenido:**
- Distribución de 24 cubículos
- Muros perimetrales
- Zona instructor
- Puerta de acceso
- Cotas principales
- Ejes estructurales

**Escala:** 1:50

**Formato:** DXF (compatible con AutoCAD, LibreCAD, QCAD)

#### 2. Cortes Arquitectónicos

**Archivo:** `CALE_T24q_BIM_corte_AA.dxf`

**Contenido:**
- Corte transversal mostrando altura cubículos
- Altura libre sala (3.0m)
- Detalles piso/techo
- Niveles (NPT)

**Escala:** 1:50

#### 3. Elevaciones (Fachadas)

**Archivos:**
- `CALE_T24q_BIM_fachada_frontal.dxf`
- `CALE_T24q_BIM_fachada_lateral.dxf`

**Contenido:**
- Vista exterior de muros
- Puertas y ventanas
- Altura total edificación

**Escala:** 1:50

#### 4. Planos de Presentación (PDF)

**Archivo:** `CALE_T24q_BIM_planos.pdf`

**Contenido:**
- Lámina A1 (594×841mm landscape)
- Planta arquitectónica
- Cortes principales
- Tabla de áreas
- Cuadro de especificaciones
- Membrete proyecto SNCALE

---

## CÓMO ABRIR Y USAR LOS MODELOS

### Opción 1: Abrir en FreeCAD (Recomendado)

**Requisitos:**
- FreeCAD 1.0 o superior
- Descarga gratuita: https://www.freecad.org/

**Pasos:**

1. Abrir FreeCAD
2. File → Open → Navegar a `services/auto_freeCAD/projects/`
3. Seleccionar `CALE_T24q_BIM.FCStd`
4. Explorar el modelo:
   - **Vista 3D:** Rotar con botón central del mouse
   - **Zoom:** Scroll del mouse
   - **Pan:** Shift + botón central
   - **Vistas predefinidas:** View → Standard Views → Isometric

**Explorar Propiedades BIM:**

1. Seleccionar un cubículo en la vista 3D
2. Ver panel "Properties" (lado derecho)
3. Expandir secciones:
   - **BIM:** Contiene BIM_ID
   - **Costos:** Contiene Precio_Unitario
   - **IFC:** Contiene IFC_Class

**Modificar Modelo:**

1. Seleccionar objeto en árbol de objetos (izquierda)
2. Modificar propiedades en panel Properties
3. Para mover: Usar herramienta Draft → Move
4. Para duplicar: Edit → Duplicate Selection
5. Guardar: File → Save

### Opción 2: Exportar a IFC y Abrir en Revit/ArchiCAD

**Exportar desde FreeCAD:**

```python
# En la consola Python de FreeCAD:
import Ifc
doc = FreeCAD.ActiveDocument
objetos = doc.Objects
Ifc.export(objetos, "CALE_T24q.ifc")
```

**Abrir en Revit:**
1. File → Open → IFC Files
2. Seleccionar `CALE_T24q.ifc`
3. El modelo se importa con todas las propiedades BIM

**Abrir en ArchiCAD:**
1. File → Interoperability → Merge → IFC
2. Seleccionar `CALE_T24q.ifc`

### Opción 3: Visualizar Online (Sin Instalación)

**Usando Autodesk Viewer:**

1. Visitar: https://viewer.autodesk.com/
2. Upload file → Seleccionar `CALE_T24q_BIM.FCStd` (o exportar a STEP primero)
3. Visualizar en navegador web

**Exportar a STEP desde FreeCAD:**
```
File → Export → Seleccionar formato STEP (*.step, *.stp)
```

---

## EXPORTACIÓN A OTROS FORMATOS

### Desde FreeCAD

El modelo BIM puede exportarse a múltiples formatos según necesidad:

| Formato | Extensión | Uso | Comando FreeCAD |
|---------|-----------|-----|-----------------|
| **IFC** | .ifc | BIM estándar (Revit, ArchiCAD) | File → Export → IFC |
| **STEP** | .step, .stp | CAD 3D estándar | File → Export → STEP |
| **STL** | .stl | Impresión 3D, visualización | File → Export → Mesh Formats → STL |
| **OBJ** | .obj | Render 3D (Blender, 3ds Max) | File → Export → Mesh Formats → OBJ |
| **DXF** | .dxf | Planos 2D (AutoCAD) | File → Export → DXF |
| **PDF** | .pdf | Presentación planos | TechDraw → Export Page |
| **PNG/JPG** | .png, .jpg | Imágenes renders | View → Save Image |

### Script de Exportación Automática

**Archivo:** `services/auto_freeCAD/scripts/exportar_formatos.py`

```python
import FreeCAD
import sys

# Abrir modelo
doc = FreeCAD.open("projects/CALE_T24q_BIM.FCStd")

# Exportar IFC
import Ifc
Ifc.export(doc.Objects, "projects/CALE_T24q.ifc")

# Exportar STEP
import ImportGui
ImportGui.export(doc.Objects, "projects/CALE_T24q.step")

# Exportar STL (para visualización)
import Mesh
Mesh.export(doc.Objects, "projects/CALE_T24q.stl")

print("Exportación completada:")
print("  - CALE_T24q.ifc (BIM)")
print("  - CALE_T24q.step (CAD 3D)")
print("  - CALE_T24q.stl (Mesh 3D)")
```

**Ejecutar:**
```bash
"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe" services/auto_freeCAD/scripts/exportar_formatos.py
```

---

## INTEGRACIÓN CON CATÁLOGO BIM

Todos los modelos están vinculados al **[CATALOGO_INVENTARIO_BIM_DEFINITIVO.md](CATALOGO_INVENTARIO_BIM_DEFINITIVO.md)**.

### Correspondencia Modelo ↔ Catálogo

| Objeto en Modelo | ID Catálogo | Categoría | Precio |
|------------------|-------------|-----------|--------|
| Cubiculo_01 a Cubiculo_24 | MOB-001 | CAT-07: Mobiliario Evaluación | $1,100,000 |
| Piso_Sala_T24q | MAT-003 | CAT-01: Materiales Construcción | $95,000/m² |
| Muro_Frontal | MAT-001 | CAT-01: Materiales Construcción | $45,000/m² |
| Escritorio_Instructor | MOB-003 | CAT-07: Mobiliario Evaluación | $2,000,000 |
| Puerta_Acceso | CAR-001 | CAT-05: Carpintería | $1,800,000 |

### Calcular Costo Total desde Modelo

**Script Python en FreeCAD:**

```python
import FreeCAD

doc = FreeCAD.ActiveDocument
total = 0

for obj in doc.Objects:
    if hasattr(obj, 'Precio_Unitario'):
        precio = obj.Precio_Unitario
        total += precio
        print(f"{obj.Label}: ${precio:,.0f}")

print(f"\nCosto total componentes con precio: ${total:,.0f}")
print(f"Costo total sala completa: $243,063,465")
```

---

## PRÓXIMOS MODELOS A GENERAR

### Fase 2: Modelos Adicionales

1. **CALE-T-16q:** Sala 16 cubículos (Cat.B)
2. **CALE-P-Pista-C1:** Pista evaluación Clase I (3,000 m²)
3. **CALE-P-Pista-C2:** Pista evaluación Clase II (2,500 m²)
4. **CALE-P-Pista-C3:** Pista evaluación Clase III (2,500 m²)
5. **Datacenter:** Cuarto de servidores con racks
6. **CALE-Completo:** Edificio completo Cat.A (teórico + práctico)

### Fase 3: Modelos Detallados LOD 400

- Cubículo con PC, monitor, teclado detallados (importar meshes)
- Simuladores con cabinas realistas
- Vehículos de evaluación 3D
- Señalización vial completa

---

## RECURSOS ADICIONALES

### Bibliotecas de Modelos 3D

Para mejorar nivel de detalle (LOD 400), descargar modelos de:

1. **GrabCAD** (https://grabcad.com)
   - Buscar: "office desk", "computer monitor", "office chair"
   - Formatos: STEP, STL
   - Licencia: Verificar por modelo

2. **BIMobject** (https://www.bimobject.com)
   - Mobiliario de oficina con IFC
   - Equipos TI (servidores, switches)

3. **Free3D** (https://free3d.com)
   - Modelos gratuitos OBJ/FBX
   - Convertir a STEP usando Blender

### Tutoriales FreeCAD

- **Manual oficial:** https://wiki.freecad.org/Manual
- **BIM Workbench:** https://wiki.freecad.org/BIM_Workbench
- **YouTube:** "FreeCAD BIM tutorial" (40+ videos)

---

## SOPORTE Y CONTACTO

**Equipo Técnico BIM:**
- Alianza MUNAY - MinTransporte
- Email: [Agregar email de contacto]
- Documentación: Este repositorio

**Reportar Issues:**
- Modelos BIM con errores
- Precios desactualizados
- Solicitar nuevos modelos

---

**Fin del documento**
**Versión:** 1.0
**Última actualización:** 2025-10-23
