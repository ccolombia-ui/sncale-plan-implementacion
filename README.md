# SNCALE - Plan de Implementación Red Nacional CALE

**Sistema Nacional de Capacitación en Logística Eléctrica - Proyecto MUNAY**

---

## 🗺️ Mapa Interactivo Red Nacional

**Ver mapa en vivo:** [Mapa Red Nacional CALE](https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_nacional.html)

### Características
- 197 centros CALE en todo Colombia
- 56 nodos principales
- 141 centros satélite
- Datos en tiempo real desde Google Sheets
- Visualización interactiva con Leaflet.js

---

## 📊 Proyecto MUNAY

Sistema integrado de formulación, planificación y visualización para la Red Nacional de Centros de Capacitación en Logística Eléctrica.

### Componentes Principales

1. **Mapa Interactivo** - Visualización geoespacial de 197 centros
2. **Google Sheets Integration** - Fuente única de verdad
3. **Sistema BIM** - Modelos 3D y fichas técnicas
4. **Scripts de Automatización** - Python + Google Sheets API

---

## 🚀 Uso Rápido

### Mapas Disponibles

#### Mapa Principal (Producción)
```
services/github_pages/mapa_cale_nacional.html
```
Lee datos en tiempo real desde Google Sheets (TSV format)

#### Mapa Funcionando (Fallback)
```
services/github_pages/mapa_cale_funcionando.html
```
Usa CSV local como fallback

#### Utilidades
```
services/github_pages/limpiar_cache.html
```
Limpia cache del navegador

---

## 📁 Estructura del Proyecto

```
sncale-plan-implementacion/
├── services/
│   └── github_pages/
│       ├── mapa_cale_nacional.html      # Mapa principal
│       ├── mapa_cale_funcionando.html   # Fallback CSV
│       ├── limpiar_cache.html           # Utilidad
│       └── data/
│           └── nodos_cale_197_MUNAY53.json
├── scripts/
│   ├── mapear_nodo_principal.py         # Script mapeo
│   └── actualizar_google_sheets_api.py  # Script actualización
├── arquitectura_red_cale_nacional_MAPEADO.csv
└── README.md
```

---

## 🛠️ Scripts de Automatización

### 1. Mapear nodo_principal
Convierte nombres de municipios a centro_id:
```bash
python scripts/mapear_nodo_principal.py
```

### 2. Actualizar Google Sheets
Actualiza la columna K (nodo_principal) via API:
```bash
python scripts/actualizar_google_sheets_api.py
```

---

## 📖 Documentación

- [Implementación Completada](IMPLEMENTACION_COMPLETADA.md)
- [Corrección TSV](CORRECCION_TSV_GOOGLE_SHEETS.md)
- [Estrategia Google Sheets](ESTRATEGIA_FINAL_GOOGLE_SHEETS_UNICA_FUENTE.md)
- [Resumen Actualización](RESUMEN_ACTUALIZACION_EXITOSA.md)
- [Instrucciones GitHub Pages](INSTRUCCIONES_GITHUB_PAGES.md)

---

## 🎯 Estado del Proyecto

| Componente | Estado | Descripción |
|------------|--------|-------------|
| Mapa Interactivo | ✅ Completado | 197 centros visualizados |
| Google Sheets Integration | ✅ Completado | Fuente única de verdad |
| Scripts Python | ✅ Completado | Mapeo y actualización |
| GitHub Pages | ✅ Desplegado | En producción |
| Visor BIM 3D | 📋 Pendiente | Xeokit ES6 |

---

## 🔗 Enlaces Útiles

### Producción
- [Mapa Principal](https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_nacional.html)
- [Google Sheets](https://docs.google.com/spreadsheets/d/1ibTlTyAELNoMg6eERPvddPBdsu-eRvWuXlIbI5kDFqU/)

### Repositorio
- [GitHub](https://github.com/ccolombia-ui/sncale-plan-implementacion)
- [Issues](https://github.com/ccolombia-ui/sncale-plan-implementacion/issues)

---

## 📊 Datos del Proyecto

```
Total centros CALE: 197
├─ Nodos principales: 56
│  ├─ Cat.A+ (HUB): 3
│  ├─ Cat.A: 17
│  └─ Cat.B**: 36
└─ Centros satélite: 141
   ├─ C2: 50
   ├─ C3: 45
   ├─ C4: 30
   └─ C5: 16
```

---

**Proyecto MUNAY** - Sistema Nacional de Capacitación en Logística Eléctrica
**Actualizado:** 29 de octubre de 2025
**Versión:** 1.0.0
