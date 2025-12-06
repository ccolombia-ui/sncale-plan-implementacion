# 🚀 Guía para Ejecutar el Mapa Interactivo SNCALE

## 📋 Requisitos Previos

- **Python 3.x** instalado en el sistema
- Navegador web moderno (Chrome, Firefox, Edge)

## 🎯 ¿Por qué se necesita un servidor local?

El mapa interactivo (`visualizacion/mapa-interactivo.html`) carga archivos JSON desde la carpeta `data/` usando **fetch()**, que requiere un servidor HTTP debido a las políticas de seguridad CORS del navegador. No funciona abriendo el archivo HTML directamente.

### Archivos JSON que se cargan:
- `data/nodos_completos_mapa.json` - 197 nodos georreferenciados
- `data/tipos_l3_con_instancias_l4.json` - Fallback de tipos L3
- `data/relaciones_jerarquicas_completas.json` - Relaciones BIM L3→L2→L1→L0
- `data/relaciones_jerarquicas_nodos.json` - Fallback de relaciones

## 🚀 Método 1: Script Batch (Recomendado para Windows)

### Paso 1: Actualizar `iniciar_servidor.bat`

El archivo ya existe pero apunta a una ruta incorrecta. Se debe actualizar a:

```batch
@echo off
echo ========================================
echo   SERVIDOR LOCAL SNCALE
echo   Mapa Interactivo Nacional
echo ========================================
echo.
echo Iniciando servidor en puerto 8085...
echo.
echo Accede al mapa en:
echo   http://localhost:8085/visualizacion/mapa-interactivo.html
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

cd /d "%~dp0"
python -m http.server 8085
```

### Paso 2: Ejecutar

1. Hacer doble clic en `iniciar_servidor.bat`
2. Esperar a que aparezca el mensaje "Serving HTTP on..."
3. Abrir el navegador en: `http://localhost:8085/visualizacion/mapa-interactivo.html`

### Paso 3: Detener el servidor

- Presionar `Ctrl + C` en la ventana del CMD
- O cerrar la ventana directamente

## 🖥️ Método 2: Línea de Comandos Manual

### Windows (CMD)
```cmd
cd c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main
python -m http.server 8085
```

### Windows (PowerShell)
```powershell
cd c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main
python -m http.server 8085
```

Luego abrir: `http://localhost:8085/visualizacion/mapa-interactivo.html`

## 🌐 Método 3: Usar VS Code Live Server

Si tienes VS Code con la extensión "Live Server":

1. Abrir la carpeta del proyecto en VS Code
2. Click derecho en `visualizacion/mapa-interactivo.html`
3. Seleccionar "Open with Live Server"
4. Se abrirá automáticamente en el navegador

## ✅ Verificar que funciona correctamente

### En el navegador:

1. **Abrir las Herramientas de Desarrollo** (F12)
2. **Ir a la pestaña Console**
3. Deberías ver mensajes como:
   ```
   ✅ Cargados 197 nodos desde nodos_completos_mapa.json
   ✅ Cargadas 197 relaciones jerárquicas
   🗺️ Mapa inicializado
   ```

### Funcionalidades que deben funcionar:

✅ **Mapa cargado** con 197 marcadores en Colombia
✅ **Filtros de categorías** en el header (Cat.A+, Cat.A, Cat.B, etc.)
✅ **Búsqueda de nodos** por nombre
✅ **Click en marcadores** abre popup con información
✅ **Panel izquierdo** muestra detalles del nodo seleccionado
✅ **Sidebar derecha** muestra jerarquía BIM (L3→L2→L1→L0)

## 🐛 Solución de Problemas

### Error: "Failed to fetch" o "CORS error"
**Causa:** El HTML se abrió directamente sin servidor HTTP  
**Solución:** Usar uno de los métodos anteriores para iniciar servidor

### Error: "python: command not found"
**Causa:** Python no está instalado o no está en PATH  
**Solución:** 
1. Descargar Python desde https://www.python.org/downloads/
2. Durante instalación, marcar "Add Python to PATH"
3. Reiniciar CMD/PowerShell

### El mapa no muestra marcadores
**Causa:** Los archivos JSON no se encuentran  
**Solución:** Verificar que existe la carpeta `data/` con los archivos:
```
data/
  ├── nodos_completos_mapa.json
  ├── tipos_l3_con_instancias_l4.json
  ├── relaciones_jerarquicas_completas.json
  └── relaciones_jerarquicas_nodos.json
```

### Puerto 8085 ya está en uso
**Solución:** Cambiar el puerto en el comando:
```cmd
python -m http.server 8090
```
Y acceder en: `http://localhost:8090/visualizacion/mapa-interactivo.html`

## 📱 Acceder desde otros dispositivos en la red

1. Averiguar tu IP local:
   ```cmd
   ipconfig
   ```
   Buscar "IPv4 Address" (ej: 192.168.1.100)

2. En otro dispositivo conectado a la misma red WiFi, abrir:
   ```
   http://192.168.1.100:8085/visualizacion/mapa-interactivo.html
   ```

## 🎯 URLs Importantes

| Recurso | URL Local |
|---------|-----------|
| **Mapa Interactivo** | `http://localhost:8085/visualizacion/mapa-interactivo.html` |
| **Página Principal** | `http://localhost:8085/index.html` |
| **Fichas L0** | `http://localhost:8085/fichas_l0/` |
| **Fichas L1** | `http://localhost:8085/fichas_l1/` |
| **Fichas L2** | `http://localhost:8085/fichas_l2/` |
| **Fichas L3** | `http://localhost:8085/fichas_l3/` |

## 🚀 Para Producción (GitHub Pages)

El proyecto ya está configurado para GitHub Pages. Una vez desplegado, el mapa estará disponible en:

```
https://ccolombia-ui.github.io/sncale-plan-implementacion/visualizacion/mapa-interactivo.html
```

Sin necesidad de servidor local, ya que GitHub Pages sirve los archivos correctamente.

---

**Última actualización:** Diciembre 6, 2025  
**Versión:** 1.0
