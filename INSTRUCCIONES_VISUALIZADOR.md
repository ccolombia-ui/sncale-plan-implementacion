# 🚀 INSTRUCCIONES PARA USAR VISUALIZADOR BIM

**Fecha:** 2025-10-29

---

## ✅ OPCIÓN 1: STANDALONE (SIN SERVIDOR) - **RECOMENDADO**

### Archivo
`c:\raziel\ia_formulacion\visor_cubiculo_standalone.html`

### Características
- ✅ **NO requiere servidor HTTP**
- ✅ Funciona directamente con `file://`
- ✅ Datos embebidos en el HTML
- ✅ Doble clic para abrir en navegador

### Uso
```cmd
# Simplemente abre el archivo
start c:\raziel\ia_formulacion\visor_cubiculo_standalone.html

# O doble clic en Windows Explorer
```

### Ventajas
- Instantáneo (sin configuración)
- No hay problemas de CORS
- Portable (copiar y abrir en cualquier PC)

### Desventajas
- Datos embebidos (si cambias JSON, debes regenerar HTML)
- No carga archivos externos

---

## 🌐 OPCIÓN 2: CON SERVIDOR HTTP (PARA DESARROLLO)

### Archivo Servidor
`c:\raziel\ia_formulacion\servidor_http_simple.py`

### Paso 1: Copiar archivos al directorio correcto
```cmd
# Copiar visor al directorio de sncale-plan-implementacion
copy "c:\raziel\sncale-plan-implementacion\planos_2d\visor_cubiculo.html" .

# Copiar JSON generados
xcopy /Y /S "c:\raziel\ia_formulacion\services\json_bim\generados" "datos_json\"
```

### Paso 2: Iniciar servidor
```cmd
cd c:\raziel\ia_formulacion
python servidor_http_simple.py
```

**Salida esperada:**
```
🚀 Servidor HTTP iniciado en puerto 8765
📂 Directorio: C:\raziel\ia_formulacion
🌐 URL: http://localhost:8765/

✅ Visualizador cubículo: http://localhost:8765/visor_cubiculo.html

⏹️  Presiona Ctrl+C para detener
```

### Paso 3: Abrir en navegador
```cmd
start http://localhost:8765/visor_cubiculo_standalone.html
```

### Ventajas
- Carga JSON externos (fetch funciona)
- Más cercano a producción
- Referencias recursivas se resuelven dinámicamente

### Desventajas
- Requiere servidor corriendo
- Más complejo de configurar

---

## 🧪 VALIDACIÓN

### Checklist - Visualizador Funcionando

Al abrir `visor_cubiculo_standalone.html` debes ver:

**Panel Izquierdo:**
- ✅ Título: "💺 Cubículo Evaluación Estándar Plus"
- ✅ Código: MOB-001
- ✅ Dimensiones: 1200×800×1600mm
- ✅ Presupuesto: $1,100,000 CAPEX
- ✅ Lista de 5 subcomponentes:
  - 🪑 MESA-CUB-001 × 1 = $350,000
  - 💺 SILLA-ERG-001 × 1 = $450,000
  - 🧱 DIV-MEL-1600 × 3 = $240,000
  - 💡 LED-STRIP-12W × 1 = $45,000
  - 🔌 CANAL-PVC-80 × 1 = $15,000

**Canvas Derecho:**
- ✅ Rectángulo dorado (mesa)
- ✅ Círculo azul (silla)
- ✅ Líneas negras (divisiones)
- ✅ Rectángulo gris (canaleta)
- ✅ Texto "CUBÍCULO" centrado

**Interactividad:**
- ✅ Mouse scroll → Zoom in/out
- ✅ Ctrl + Drag → Mover vista
- ✅ Hover elementos → Tooltip aparece
- ✅ Botón "Exportar PNG" → Descarga imagen

---

## 🐛 TROUBLESHOOTING

### Problema: "This site can't be reached"
**Causa:** Intentando usar versión con servidor sin tenerlo corriendo

**Solución:**
```cmd
# Usa versión standalone
start c:\raziel\ia_formulacion\visor_cubiculo_standalone.html
```

### Problema: "Canvas vacío (negro)"
**Causa:** Fabric.js no cargó desde CDN

**Solución:**
```
1. Verifica conexión a internet
2. Abre consola del navegador (F12)
3. Busca errores de red
```

### Problema: "Datos no aparecen"
**Causa:** JavaScript deshabilitado

**Solución:**
```
1. Abre configuración del navegador
2. Habilita JavaScript
3. Recarga página (Ctrl+R)
```

### Problema: "Servidor no inicia (puerto ocupado)"
**Causa:** Otro proceso usando puerto 8765

**Solución:**
```cmd
# Ver qué usa el puerto
netstat -ano | findstr :8765

# Matar proceso (reemplaza PID)
taskkill /PID <numero_pid> /F

# O cambiar puerto en servidor_http_simple.py
PORT = 8080  # Cambiar línea 12
```

---

## 📊 COMPARACIÓN DE OPCIONES

| Característica | Standalone | Servidor HTTP |
|---------------|------------|---------------|
| **Instalación** | ✅ Sin setup | ⚠️ Requiere Python |
| **Velocidad** | ✅ Instantáneo | ⚠️ Requiere iniciar servidor |
| **CORS** | ✅ Sin problemas | ✅ Configurado |
| **Datos dinámicos** | ❌ Embebidos | ✅ Carga JSON externos |
| **Portabilidad** | ✅ Copiar y abrir | ❌ Necesita servidor |
| **Desarrollo** | ⚠️ Regenerar HTML | ✅ Editar JSON directo |

---

## 🎯 RECOMENDACIÓN

### Para Validación Rápida (AHORA)
**Usar:** `visor_cubiculo_standalone.html`
- Doble clic y funciona
- Sin configuración
- Validar que el diseño funciona

### Para Desarrollo Continuo (DESPUÉS)
**Usar:** Servidor HTTP + visor con fetch
- Editar JSON sin regenerar HTML
- Agregar más componentes dinámicamente
- Workflow más profesional

---

## 🚀 PRÓXIMOS PASOS

### Si el visualizador standalone funciona ✅

1. **Validar visualmente:**
   - ¿Se ve el cubículo dibujado?
   - ¿Los precios suman correctamente?
   - ¿El zoom/pan funciona?

2. **Proceder con desarrollo:**
   - Generar batch de 20-30 componentes atómicos
   - Crear MOB-002, MOB-003, etc.
   - Crear visualizador para salas (nivel n1)

3. **Migrar a servidor HTTP:**
   - Cuando tengas 10+ componentes
   - Para cargar JSON dinámicamente
   - Para sistema más profesional

### Si NO funciona ❌

**Reportar:**
1. Captura de pantalla
2. Consola del navegador (F12 → Console)
3. Error exacto

---

## 📝 ARCHIVOS CREADOS

```
c:\raziel\ia_formulacion\
├── visor_cubiculo_standalone.html     ← ✅ USA ESTE
├── servidor_http_simple.py            ← Para después
├── services\json_bim\
│   ├── generados\
│   │   ├── atomicos\
│   │   │   ├── SILLA-ERG-001.json
│   │   │   ├── MESA-CUB-001.json
│   │   │   ├── DIV-MEL-1600.json
│   │   │   ├── LED-STRIP-12W.json
│   │   │   └── CANAL-PVC-80.json
│   │   └── nivel_0\
│   │       └── MOB-001.json
│   └── generators\
│       ├── generar_json_bim.py
│       └── verificar_referencias_json.py
└── PLAN_DESARROLLO_BIM_NIVELES.md
```

---

**¿Funciona el visualizador standalone?** 
→ Responde SI/NO para proceder con el plan de desarrollo.
