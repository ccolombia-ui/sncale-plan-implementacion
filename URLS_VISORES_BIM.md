# 🎨 VISORES BIM SNCALE - URLS PÚBLICAS

## 🌐 **GitHub Pages (LIVE)**

### 📦 **Visor 3D BIM - Xeokit (ACTUALIZADO)**
**Mejor versión para visualización BIM/IFC**

**URL Base:**
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html
```

**Ejemplos con parámetros:**

1. **Cat.A+ - BOGOTÁ NORTE:**
   ```
   https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html?centro=BOGOTÁ%20NORTE&categoria=Cat.A+
   ```

2. **Cat.C5 - Leticia:**
   ```
   https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html?centro=Leticia&categoria=Cat.C5
   ```

3. **Cat.A - Medellín:**
   ```
   https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_bim_3d.html?centro=Medellín&categoria=Cat.A
   ```

---

### 📐 **Visores 2D - Canvas Fabric.js (NUEVOS)**

#### **Visor Sala T-4q (Nivel 1 - 4 Cubículos)**
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/planos_2d/visor_sala_t4q.html
```

**Características:**
- ✅ Grid 2×2 con 4 cubículos MOB-001
- ✅ Referencias recursivas automáticas
- ✅ Precio total: $4,400,000
- ✅ Carga dinámica de JSONs desde datos_json/

#### **Visor Cubículo MOB-001 (Nivel 0)**
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/planos_2d/visor_cubiculo.html
```

**Características:**
- ✅ Vista detallada del cubículo individual
- ✅ Componentes: Mesa + Silla + 3 Divisiones + LED + Canaleta
- ✅ Precio: $1,100,000
- ✅ Composición atómica visible

---

## 🔧 **Características del Visor 3D Xeokit**

### **Mejoras sobre Three.js:**
- ✅ **Optimizado para BIM/IFC** - Diseñado específicamente para modelos arquitectónicos
- ✅ **Carga de archivos .ifc** - Soporta formato IFC estándar de la industria
- ✅ **Navegación intuitiva** - Controles específicos para exploración arquitectónica
- ✅ **Selección de objetos** - Click para seleccionar componentes individuales
- ✅ **Panel de información** - Muestra propiedades BIM de elementos seleccionados
- ✅ **Árbol de objetos** - Navegación jerárquica del modelo
- ✅ **Mediciones** - Herramientas de medición integradas
- ✅ **Secciones** - Cortes dinámicos del modelo
- ✅ **Mejor rendimiento** - Optimizado para modelos grandes (>100k objetos)

### **Tecnologías:**
- **xeokit SDK** v2.x - https://xeokit.io
- **WebGL 2.0** - Renderizado acelerado por GPU
- **IFC.js** - Parser de archivos IFC

---

## 📊 **Jerarquía de Componentes BIM**

```
SNCALE (Sistema Nacional)
│
├─ CALE-CAT-A+ (Centro Categoría A+)
│  │
│  ├─ SALA-T-24q (Nivel 2 - 24 Cubículos)
│  ├─ SALA-T-16q (Nivel 2 - 16 Cubículos)
│  ├─ SALA-T-8q (Nivel 1 - 8 Cubículos)
│  └─ SALA-T-4q (Nivel 1 - 4 Cubículos) ✅ IMPLEMENTADO
│     │
│     └─ MOB-001 × 4 (Nivel 0 - Cubículo) ✅ IMPLEMENTADO
│        │
│        ├─ MESA-CUB-001 (Atómico) ✅
│        ├─ SILLA-ERG-001 (Atómico) ✅
│        ├─ DIV-MEL-1600 × 3 (Atómico) ✅
│        ├─ LED-STRIP-12W (Atómico) ✅
│        └─ CANAL-PVC-80 (Atómico) ✅
│
├─ CALE-CAT-A (Centro Categoría A)
├─ CALE-CAT-B** (Centro Categoría B**)
├─ CALE-CAT-B (Centro Categoría B)
└─ CALE-CAT-C1/C2/C3/C4/C5 (Centros Categoría C)
```

---

## 🚀 **Cómo Usar los Visores**

### **Visor 3D (Xeokit):**
1. Abrir URL con parámetros `?centro=XXX&categoria=YYY`
2. **Navegar:**
   - 🖱️ Click izquierdo + Drag: Rotar
   - 🖱️ Click derecho + Drag: Pan
   - 🖱️ Scroll: Zoom
3. **Seleccionar:** Click en cualquier objeto
4. **Ver propiedades:** Panel derecho muestra datos BIM
5. **Cargar IFC:** Botón "Cargar IFC" para subir archivos .ifc

### **Visores 2D (Canvas):**
1. Abrir URL directamente (sin parámetros)
2. **Navegar:**
   - 🖱️ Scroll: Zoom
   - 🖱️ Ctrl + Drag: Pan
   - 🖱️ Click en cubículo: Ver detalles
3. **Exportar:** Botón "Exportar PNG" para guardar imagen
4. **Cuadrícula:** Toggle para mostrar/ocultar grid

---

## 📁 **Estructura de Datos JSON**

### **Ubicación de archivos:**
```
planos_2d/
├─ datos_json/
│  ├─ atomicos/
│  │  ├─ SILLA-ERG-001.json
│  │  ├─ MESA-CUB-001.json
│  │  ├─ DIV-MEL-1600.json
│  │  ├─ LED-STRIP-12W.json
│  │  └─ CANAL-PVC-80.json
│  │
│  ├─ nivel_0/
│  │  └─ MOB-001.json (Cubículo)
│  │
│  └─ nivel_1/
│     └─ SALA-T-4q.json (Sala 4 cubículos)
│
├─ visor_cubiculo.html
└─ visor_sala_t4q.html
```

---

## 🔄 **Sistema de Referencias Recursivas**

**Ejemplo: Cambiar precio de SILLA-ERG-001**

1. Editar `atomicos/SILLA-ERG-001.desc.md` → cambiar precio de $450,000 a $500,000
2. Ejecutar `python generar_json_bim.py`
3. **Resultado automático:**
   - ✅ `SILLA-ERG-001.json` → $500,000
   - ✅ `MOB-001.json` → $1,150,000 (recalculado: +$50K)
   - ✅ `SALA-T-4q.json` → $4,600,000 (recalculado: 4 × $1,150,000)

**No se requiere editar manualmente 3 archivos!** 🎉

---

## 📞 **Soporte y Documentación**

- **Repositorio:** https://github.com/ccolombia-ui/sncale-plan-implementacion
- **Issues:** https://github.com/ccolombia-ui/sncale-plan-implementacion/issues
- **Xeokit Docs:** https://xeokit.github.io/xeokit-sdk/docs/
- **IFC Spec:** https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/

---

**Última actualización:** 29 de octubre de 2025
**Versión visor 3D:** Xeokit SDK v2.x
**Versión visores 2D:** Fabric.js v5.3.0
