# Análisis de Categorías CALE - Datos Reales vs. Anexo B

**Fecha:** 31 de octubre de 2025
**Sistema:** BIM CALE - Red Nacional de Centros de Licenciamiento

---

## Resumen Ejecutivo

**Problema identificado:** Los filtros en el mapa no funcionan completamente porque las categorías con variantes (`CALE.n_1+`, `CALE.n_2*`, `CALE.n_2**`) definidas en el Anexo B **NO EXISTEN** en los datos de Google Sheets.

---

## 1. Categorías REALES en Google Sheets (Verificado)

**Total de categorías:** 7
**Total de centros:** 197

| Categoría | Centros | Color | Descripción |
|-----------|---------|-------|-------------|
| CALE.C2 | 31 | #dc2626 (Rojo) | Categoría C2 |
| CALE.C3 | 69 | #dc2626 (Rojo) | Categoría C3 |
| CALE.C4 | 27 | #dc2626 (Rojo) | Categoría C4 |
| CALE.C5 | 14 | #dc2626 (Rojo) | Categoría C5 |
| CALE.n_1 | 20 | #2563eb (Azul) | Nodos principales nivel 1 |
| CALE.n_2 | 20 | #16a34a (Verde) | Nodos nivel 2 |
| CALE.n_3 | 16 | #ea580c (Naranja) | Nodos nivel 3 |

**Fuente:** `arquitectura_red_cale_nacional` en Google Sheets
**Columna:** `categoria_cale` (columna 7)

---

## 2. Categorías ESPERADAS según Anexo B

Según el documento "MUNAY_5.2__anexo_b__DEFINITIVO", las categorías deberían incluir:

### Categorías con Variantes:

1. **CALE.n_1** - Base
2. **CALE.n_1+** - Con incremento de capacidad por CALE.n_2
3. **CALE.n_2** - Base
4. **CALE.n_2*** - Con incremento de capacidad por CALE.n_1
5. **CALE.n_2**** - Configuración reforzada
6. **CALE.n_3** - Base
7. **CALE.C2** - Categoría C2
8. **CALE.C3** - Categoría C3
9. **CALE.C4** - Categoría C4
10. **CALE.C5** - Categoría C5

### Significado de las Variantes:

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| `+` | Incremento en capacidad mediante CALE.n_2 adicionales | CALE.n_1+ |
| `*` | Incremento en capacidad mediante CALE.n_1 adicionales | CALE.n_2* |
| `**` | Configuración reforzada con múltiples incrementos | CALE.n_2** |

---

## 3. Comparación: Real vs. Esperado

### ✅ Categorías que SÍ existen:
- CALE.n_1
- CALE.n_2
- CALE.n_3
- CALE.C2
- CALE.C3
- CALE.C4
- CALE.C5

### ❌ Categorías FALTANTES (según Anexo B):
- CALE.n_1+ (con incremento n_2)
- CALE.n_2* (con incremento n_1)
- CALE.n_2** (configuración reforzada)

---

## 4. Impacto en el Mapa Interactivo

### Filtros que SÍ funcionan:
```javascript
✅ CALE.n_1 (20 centros)
✅ CALE.n_2 (20 centros)
✅ CALE.n_3 (16 centros)
✅ CALE.C2 (31 centros)
✅ CALE.C3 (69 centros)
✅ CALE.C4 (27 centros)
✅ CALE.C5 (14 centros)
```

### Filtros que NO funcionan (categorías no existen):
```javascript
❌ CALE.n_1+ (0 centros) - filtro definido pero sin datos
❌ CALE.n_2* (0 centros) - filtro definido pero sin datos
❌ CALE.n_2** (0 centros) - filtro definido pero sin datos
```

---

## 5. Código Correcto para el Mapa (Basado en Datos Reales)

```javascript
const CATEGORIAS_CALE = [
    // Nodos principales (Azul)
    { id: 'CALE.n_1', nombre: 'CALE.n_1', color: '#2563eb' },

    // Nodos secundarios (Verde)
    { id: 'CALE.n_2', nombre: 'CALE.n_2', color: '#16a34a' },

    // Nodos terciarios (Naranja)
    { id: 'CALE.n_3', nombre: 'CALE.n_3', color: '#ea580c' },

    // Categorías C (Rojo)
    { id: 'CALE.C2', nombre: 'C2', color: '#dc2626' },
    { id: 'CALE.C3', nombre: 'C3', color: '#dc2626' },
    { id: 'CALE.C4', nombre: 'C4', color: '#dc2626' },
    { id: 'CALE.C5', nombre: 'C5', color: '#dc2626' }
];
```

**Este es el código que debe usarse** mientras no se actualicen los datos en Google Sheets.

---

## 6. Opciones de Solución

### Opción A: Actualizar Google Sheets (Recomendado)

**Acciones:**
1. Revisar el Anexo B para identificar qué centros deben tener variantes
2. Actualizar la columna `categoria_cale` en Google Sheets con:
   - `CALE.n_1+` para centros n_1 con refuerzo n_2
   - `CALE.n_2*` para centros n_2 con refuerzo n_1
   - `CALE.n_2**` para centros n_2 con configuración reforzada

**Ventajas:**
- Datos quedan completos según especificación técnica
- Filtros funcionan correctamente
- Información más precisa para planificación

**Desventajas:**
- Requiere análisis técnico del Anexo B
- Modificación manual de datos

### Opción B: Simplificar Filtros (Temporal)

**Acciones:**
1. Eliminar filtros de variantes del mapa
2. Usar solo las 7 categorías existentes
3. Agregar nota aclaratoria en la interfaz

**Ventajas:**
- Solución inmediata
- Mapa funciona 100% con datos actuales

**Desventajas:**
- Pérdida de granularidad técnica
- No refleja especificación completa del Anexo B

---

## 7. Recomendación

**Implementar Opción B (Temporal) mientras se prepara Opción A (Definitiva)**

### Paso 1: Actualizar mapa con categorías reales
```javascript
// Usar solo las 7 categorías que existen
const CATEGORIAS_CALE = [
    { id: 'CALE.n_1', nombre: 'CALE.n_1', color: '#2563eb' },
    { id: 'CALE.n_2', nombre: 'CALE.n_2', color: '#16a34a' },
    { id: 'CALE.n_3', nombre: 'CALE.n_3', color: '#ea580c' },
    { id: 'CALE.C2', nombre: 'C2', color: '#dc2626' },
    { id: 'CALE.C3', nombre: 'C3', color: '#dc2626' },
    { id: 'CALE.C4', nombre: 'C4', color: '#dc2626' },
    { id: 'CALE.C5', nombre: 'C5', color: '#dc2626' }
];
```

### Paso 2: Preparar actualización de Google Sheets
1. Crear script Python para analizar Anexo B y determinar variantes
2. Generar CSV con categorías corregidas
3. Actualizar Google Sheets vía API
4. Actualizar mapa con categorías completas

---

## 8. Distribución Actual de Centros

**Resumen:**
```
Total centros CALE: 197

Categorías Principales:
  CALE.n_1:  20 centros (10.15%)
  CALE.n_2:  20 centros (10.15%)
  CALE.n_3:  16 centros ( 8.12%)

Categorías C:
  CALE.C2:   31 centros (15.74%)
  CALE.C3:   69 centros (35.03%) <- Mayor cantidad
  CALE.C4:   27 centros (13.71%)
  CALE.C5:   14 centros ( 7.11%)
```

---

## 9. Archivos de Referencia

**Datos Verificados:**
- `scripts/verificar_categorias_reales.py` - Script de verificación
- Google Sheets: `arquitectura_red_cale_nacional` (columna 7)

**Documentación Técnica:**
- `ANEXO_B_COMPLETO.txt` - Especificación completa (63,394 chars)
- Anexo B Google Docs: `16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE`

**Mapas:**
- `mapa_cale_v3_proxy_completo.html` - Versión actual (necesita actualización)
- `mapa_cale_test_diagnostico.html` - Tests funcionando

---

## 10. Próximos Pasos Inmediatos

1. ✅ **Actualizar `mapa_cale_v3_proxy_completo.html`** con las 7 categorías reales
2. ✅ **Probar filtros** - Deberían funcionar 100% ahora
3. ⏳ **Aplicar diseño profesional** (Revit/Google Earth style)
4. ⏳ **Analizar Anexo B** para determinar qué centros necesitan variantes
5. ⏳ **Actualizar Google Sheets** con categorías completas

---

**Generado el:** 31 de octubre de 2025
**Estado:** Análisis completado - Solución identificada
**Acción requerida:** Actualizar código del mapa con categorías reales

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
