# 🔄 Sincronización AKTRIEL

**Carpeta Google Drive vinculada al workspace local**

---

## 📁 Ubicaciones

### Google Drive Desktop:
```
G:\.shortcut-targets-by-id\1fENbpuTdON265HSA0icoN8nHYS4gWJHF\_rafEl\aktriel
```

### Workspace Local:
```
c:\raziel\ia_formulacion\aktriel
```

---

## 🔄 Estado de Sincronización

**Método:** Copia completa (copytree)
**Estado:** En progreso
**Archivos:** 3,934+ archivos sincronizados

### Contenido Principal:
- `01__min_transporte/` - Proyectos Ministerio de Transporte
- `02__hatonuevo_guajira/` - Proyectos Hato Nuevo, Guajira
- `03__creciverso/` - Proyectos Creciverso
- `99__emcosalud/` - Proyectos Emcosalud
- `tools/` - Herramientas
- `logs/` - Registros

---

## 🎯 Propósito

Esta carpeta contiene la documentación y proyectos relacionados con:

### **CALE (Colegios de Alto Logro Educativo)**
- Categoría A - Clase 3
- Componentes BIM reutilizables:
  - 🏃 Pistas deportivas
  - 🏫 Salas de clase
  - 💻 Datacenters
  - 🏗️ Otros componentes arquitectónicos

### Proyectos de Infraestructura:
- Ministerio de Transporte
- Proyectos municipales (Guajira)
- Otros proyectos de formulación

---

## 🚀 Próximos Pasos

### **FASE 1: FreeCAD → BIM Objects** (ACTUAL)
1. Estudiar especificaciones CALE en aktriel/
2. Identificar componentes arquitectónicos clave
3. Crear biblioteca de objetos BIM reutilizables en FreeCAD
4. Implementar sistema de ensamblaje paramétrico
5. Exportar a formato BIM estándar (IFC/JSON-BIM)

### **FASE 2: QGIS → Geolocalización** (Siguiente)
1. Ubicar instalación QGIS en el sistema
2. Configurar MCP server para QGIS
3. Cargar bases cartográficas de municipios colombianos
4. Identificar predios en mapas
5. Colocar objetos BIM del CALE en predios específicos
6. Visualizar proyectos en contexto geográfico

### **FASE 3: Pricing → CAMACOL/SECOP** (Final)
1. Crear MCP server para precios CAMACOL
2. Integrar API de SECOP para precios de referencia
3. Calcular costos automáticos de proyectos BIM
4. Generar presupuestos y análisis de precios unitarios (APU)
5. Exportar documentación de costos

---

## 📋 Script de Sincronización

### Sincronización Manual:
```bash
python sync_aktriel.py
```

Este script:
- ✓ Copia inicial completa
- ✓ Monitoreo bidireccional en tiempo real
- ✓ Sincroniza cambios automáticamente
- ✓ Mantiene ambas carpetas idénticas

### Sincronización Automática (futuro):
Configurar como servicio de Windows para sincronización continua.

---

## 🔍 Explorar Contenido

```bash
# Ver carpetas principales
ls aktriel/

# Buscar documentación CALE
find aktriel -name "*cale*" -o -name "*CALE*"

# Buscar especificaciones técnicas
find aktriel -name "*.pdf" -o -name "*.dwg" -o -name "*.rvt"
```

---

**Creado:** 2025-10-23
**Sincronización:** En progreso
**Próximo paso:** Estudiar especificaciones CALE y crear objetos BIM
