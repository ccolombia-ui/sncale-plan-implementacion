# 🧪 PRUEBA VISOR XEOKIT - Cat.C5

## 🚀 Acceso Directo

**Probemos primero con el más simple (Cat.C5):**

```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Leticia&categoria=Cat.C5
```

---

## 📋 URLs de Prueba - Todas las Categorías

### Cat.C5 - Más Simple (1×CLASE1 + 1×T16q)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Leticia&categoria=Cat.C5
```

### Cat.C4 - Remoto
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Arauca&categoria=Cat.C4
```

### Cat.C1 - Local Mayor
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Valledupar&categoria=Cat.C1
```

### Cat.B - Regional (1×C2 + 2×C1 + 1×T16q)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Pereira&categoria=Cat.B
```

### Cat.A - Principal (1×C3 + 1×C2 + 1×T24q)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=Cali&categoria=Cat.A
```

### Cat.A+ - Metropolitana (3×CALE-P + 1×T24q)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/fichas_bim/visor_xeokit.html?centro=BOGOTÁ%20NORTE&categoria=Cat.A+
```

---

## ✅ ¿Qué Esperar Ver?

1. **Panel Izquierdo**: Lista de componentes BIM con costos
2. **Visor 3D (xeokit)**: Modelo 3D interactivo
   - 🔴 **Pistas** en rojo (práctico)
   - 🔵 **Salas teóricas** en azul con cubículos
   - 🟡 **Edificio administrativo** en amarillo
   - 🟢 **Vehículos** en verde
   - ⚪ **Terreno** en gris

3. **Controles**:
   - 🔄 Reset Vista
   - ⬆️ Vista Superior
   - ➡️ Vista Frontal
   - 📐 Perspectiva/Ortho

4. **Interacción**:
   - Click en componente del panel → Se resalta en 3D
   - Rotar: Click derecho + arrastrar
   - Zoom: Scroll del mouse
   - Pan: Click rueda + arrastrar

---

## 🔬 Diferencias vs Three.js

| Característica | Three.js (anterior) | xeokit (nuevo) |
|----------------|---------------------|----------------|
| **CDN** | jsdelivr (bloqueado) | jsdelivr (mismo CDN) |
| **Optimización** | Genérica 3D | Específica para BIM |
| **Performance** | Buena | Excelente (millones de objetos) |
| **Funciones BIM** | Manual | Integradas (SAO, LOD, IFC) |
| **Uso** | Juegos, visualización | Arquitectura, construcción |

---

## ⚠️ Nota sobre CDN

Si xeokit tampoco carga desde CDN, podemos:

**Plan B**: Descargar xeokit localmente
```bash
cd fichas_bim
mkdir lib
cd lib
# Descargar xeokit-sdk.min.js
```

**Plan C**: Convertir a IFC y usar IFC.js

---

## 🎯 Próximos Pasos

1. ✅ **Probar Cat.C5** → Ver si carga xeokit
2. Si funciona → Probar Cat.A+ (más complejo)
3. Si no funciona (CDN bloqueado) → Descargar xeokit local
4. Ajustar colores y posiciones según feedback
5. Agregar más detalles (ventanas, puertas, etc.)

---

## 📊 Resumen de Inversión

| Categoría | Componentes | Inversión | Capacidad/año |
|-----------|-------------|-----------|---------------|
| Cat.C5 | 1×C1 + 1×T16q | $10,532 M | 19,140 |
| Cat.B | 1×C2 + 2×C1 + 1×T16q | $35,274 M | 50,140 |
| Cat.A | 1×C3 + 1×C2 + 1×T24q | $20,713 M | 37,210 |
| Cat.A+ | 3×CALE-P + 1×T24q | $26,776 M | 59,210 |

**Total Nacional (197 centros)**: $2.38 Billones COP
