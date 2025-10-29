# 🧪 GUÍA DE PRUEBAS - Fichas BIM Simples

## ✅ **VERSIÓN SIMPLE DESPLEGADA**

Ahora puedes ver las fichas BIM de **TODAS las categorías** desde una sola página HTML.

---

## 🎯 **CÓMO PROBAR - 2 FORMAS**

### 1️⃣ **Desde el Mapa** (Producción)

```
1. Abre: https://ccolombia-ui.github.io/sncale-plan-implementacion/mapa_cale.html
2. Click en CUALQUIER marcador
3. En el popup, click "🏗️ Ver Ficha BIM 3D"
4. ✅ Se abre ficha con información completa
```

### 2️⃣ **URLs Directas por Categoría**

#### 🟢 **Cat.C5 - Básico** (14 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Leticia&categoria=Cat.C5
```

#### 🟢 **Cat.C4 - Remoto** (27 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Magangue&categoria=Cat.C4
```

#### 🟢 **Cat.C3 - Satélite** (69 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Apartado&categoria=Cat.C3
```

#### 🟢 **Cat.C2 - Local Menor** (31 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Riohacha&categoria=Cat.C2
```

#### 🟡 **Cat.C1 - Local Mayor** (16 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Quibdo&categoria=Cat.C1
```

#### 🟠 **Cat.B - Regional** (4 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=PASTO&categoria=Cat.B
```

#### 🟠 **Cat.B** - Regional Mayor** (16 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=ARMENIA&categoria=Cat.B**
```

#### 🔴 **Cat.A - Principal** (17 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=MEDELLIN&categoria=Cat.A
```

#### 🔴 **Cat.A+ - Metropolitana** (3 centros)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=BOGOTA%20NORTE&categoria=Cat.A+
```

---

## 📊 **QUÉ VERÁS EN CADA FICHA**

### **Información Mostrada:**

✅ **Nombre del Centro** (según parámetro `centro`)  
✅ **Categoría con Badge de Color** (según parámetro `categoria`)  
✅ **Componentes BIM:**
- 🏁 **Práctico** (CALE-P-CLASE1/2/3)
  - Descripción técnica
  - Área terreno
  - Vehículos
  - Duración construcción
  - **Costo en millones**
  
- 📚 **Teórico** (CALE-T-16q/24q)
  - Descripción
  - Cubículos
  - Equipamiento
  - Duración
  - **Costo en millones**

✅ **Resumen Total:**
- 💰 **Inversión Total** de esa categoría
- ⚡ **Capacidad anual** de evaluaciones
- 🌍 **Cantidad de centros** a nivel nacional
- 💼 **Inversión total nacional** de esa categoría

---

## 🎨 **Colores por Categoría**

Cada categoría tiene su **degradado de color** único:

| Categoría | Color Principal | Visual |
|-----------|----------------|--------|
| Cat.A+ | Rojo oscuro #8B0000 | 🔴🔴 |
| Cat.A | Carmesí #DC143C | 🔴 |
| Cat.B** | Naranja fuerte #FF6B00 | 🟠🟠 |
| Cat.B | Naranja #FFA500 | 🟠 |
| Cat.C1 | Dorado #FFD700 | 🟡 |
| Cat.C2 | Verde claro #90EE90 | 🟢 |
| Cat.C3 | Verde medio #66CDAA | 🟢 |
| Cat.C4 | Verde oscuro #3CB371 | 🟢🟢 |
| Cat.C5 | Verde bosque #228B22 | 🟢🟢🟢 |

---

## 🧪 **PRUEBAS RECOMENDADAS**

### **Paso 1: Probar Cat.C5 (Más Simple)**
```
1. Copiar URL: https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=Leticia&categoria=Cat.C5
2. Pegar en navegador
3. Verificar:
   ✅ Header verde con "Leticia"
   ✅ Badge "Cat.C5 - Básico"
   ✅ 2 componentes (CLASE1 + T-16q)
   ✅ Costo total: $10,532 Millones
   ✅ Capacidad: 19,140 eval/año
```

### **Paso 2: Probar Cat.A+ (Más Complejo)**
```
1. URL: https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/ficha_simple.html?centro=BOGOTA%20NORTE&categoria=Cat.A+
2. Verificar:
   ✅ Header rojo oscuro con "BOGOTA NORTE"
   ✅ Badge "Cat.A+ - Metropolitana"
   ✅ 4 componentes (CLASE3 + CLASE2 + CLASE3 adicional + T-24q)
   ✅ Costo total: $26,776 Millones
   ✅ Capacidad: 59,210 eval/año
```

### **Paso 3: Probar desde Mapa**
```
1. Abrir mapa: https://ccolombia-ui.github.io/sncale-plan-implementacion/mapa_cale.html
2. Click marcador de MEDELLÍN (rojo)
3. Click "🏗️ Ver Ficha BIM 3D"
4. Verificar ficha Cat.A con 3 componentes
```

---

## 🔍 **VERIFICACIÓN TÉCNICA**

### **Archivo Principal:**
`fichas_bim/ficha_simple.html`

### **Configuración Interna:**
```javascript
const CONFIG = {
    'Cat.C5': { ... },
    'Cat.C4': { ... },
    'Cat.C3': { ... },
    ...
    'Cat.A+': { ... }
};
```

### **Parámetros URL Requeridos:**
- `centro`: Nombre del centro CALE
- `categoria`: Cat.C5, Cat.C4, Cat.C3, Cat.C2, Cat.C1, Cat.B, Cat.B**, Cat.A, Cat.A+

### **Valores por Defecto (sin parámetros):**
- Centro: "CENTRO DE PRUEBA"
- Categoría: "Cat.C5"

---

## ✅ **CHECKLIST DE FUNCIONALIDADES**

- [x] Configuración de 9 categorías completa
- [x] Colores CSS dinámicos por categoría
- [x] Componentes BIM detallados
- [x] Costos en millones (formato colombiano)
- [x] Capacidades anuales
- [x] Resumen inversión nacional
- [x] Diseño responsive
- [x] Hover effects en componentes
- [x] Botón "Cerrar" funcional
- [x] Integración con mapa_cale.html
- [x] Desplegado en GitHub Pages

---

## 🚀 **SIGUIENTE PASO: AGREGAR 3D**

Una vez verifiques que TODAS las fichas simples funcionan correctamente:

1. ✅ Copiar HTML a `ficha_con_3d.html`
2. ✅ Agregar canvas Three.js
3. ✅ Generar geometrías 3D simples
4. ✅ Mantener panel informativo izquierdo

**¿Quieres que continuemos con la versión 3D ahora que la versión simple funciona?** 🎮
