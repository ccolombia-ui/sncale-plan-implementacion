# Instrucciones: Desplegar en GitHub Pages

**Fecha:** 29 de octubre de 2025
**Objetivo:** Desplegar mapa interactivo CALE en GitHub Pages

---

## ✅ Estado Actual

- ✅ Repositorio Git inicializado
- ✅ Commit creado con todos los archivos
- ✅ Archivos preparados para despliegue
- ⏳ Pendiente: Configurar remote y push

---

## 📋 Pasos para Desplegar

### Paso 1: Crear repositorio en GitHub (si no existe)

1. Ir a: https://github.com/new
2. Nombre del repositorio: `ia_formulacion` (o el que prefieras)
3. Descripción: "Proyecto MUNAY - Red Nacional CALE"
4. Visibilidad: **Public** (necesario para GitHub Pages gratis)
5. NO inicializar con README (ya tenemos uno)
6. Click "Create repository"

### Paso 2: Agregar remote y hacer push

```bash
# Agregar remote (reemplazar TU-USUARIO y NOMBRE-REPO)
git remote add origin https://github.com/TU-USUARIO/ia_formulacion.git

# Push inicial
git push -u origin master
```

**Alternativa si prefieres rama `main`:**
```bash
git branch -M main
git remote add origin https://github.com/TU-USUARIO/ia_formulacion.git
git push -u origin main
```

### Paso 3: Configurar GitHub Pages

1. Ir al repositorio en GitHub
2. Click en **Settings** (Configuración)
3. En el menú lateral, click en **Pages**
4. En "Source", seleccionar:
   - Branch: `master` (o `main`)
   - Folder: `/ (root)`
5. Click "Save"

**¡Listo!** GitHub Pages comenzará a construir tu sitio.

### Paso 4: Verificar despliegue

1. Esperar 1-2 minutos (primera vez puede tardar más)
2. GitHub mostrará la URL del sitio:
   ```
   https://TU-USUARIO.github.io/ia_formulacion/
   ```
3. Verificar que funcione:
   ```
   https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_nacional.html
   ```

---

## 🗺️ URLs del Mapa

Una vez desplegado, el mapa estará disponible en:

### Mapa Principal (Google Sheets)
```
https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_nacional.html
```

### Mapa Funcionando (CSV Local - Fallback)
```
https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_funcionando.html
```

### Mapa de Prueba (con Validación)
```
https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_test.html
```

### Utilidad Limpieza Cache
```
https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/limpiar_cache.html
```

---

## 🔧 Resolución de Problemas

### Problema: "Failed to fetch" en GitHub Pages

**Causa:** Google Sheets no está publicada como pública

**Solución:**
1. Ir a Google Sheets
2. File → Share → Publish to web
3. Sheet: `arquitectura_red_cale_nacional`
4. Format: **TSV** (Tab-separated values)
5. Click "Publish"
6. Copiar URL generada
7. Verificar que coincida con la del HTML

### Problema: 404 Not Found

**Causa:** GitHub Pages aún no ha terminado de construir

**Solución:**
1. Ir a Settings → Pages
2. Verificar estado: "Your site is ready to be published at..."
3. Esperar 1-2 minutos más
4. Refrescar página

### Problema: Mapa carga pero sin datos

**Causa:** CSV no se encuentra o ruta incorrecta

**Solución:**
1. Verificar que `arquitectura_red_cale_nacional_MAPEADO.csv` esté en la raíz
2. Verificar rutas relativas en HTML:
   ```javascript
   // Correcto para GitHub Pages:
   fetch('../../arquitectura_red_cale_nacional_MAPEADO.csv')
   ```

### Problema: CORS errors

**Causa:** Google Sheets tiene restricciones CORS

**Solución:**
1. Usar `mapa_cale_funcionando.html` como fallback
2. Este mapa usa CSV local (sin CORS issues)
3. O asegurarse que Google Sheets esté publicada correctamente

---

## 🔄 Actualizar el Mapa

### Actualizar datos en Google Sheets

1. Editar Google Sheets directamente
2. Los cambios se reflejan automáticamente
3. Cache del navegador: 5 minutos
4. Para forzar actualización: usar `limpiar_cache.html`

### Actualizar código del mapa

```bash
# 1. Hacer cambios en archivos HTML
# 2. Agregar cambios
git add services/github_pages/*.html

# 3. Commit
git commit -m "Actualizar mapa interactivo

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 4. Push
git push origin master
```

**Tiempo de despliegue:** 1-2 minutos

---

## 📊 Verificar que Google Sheets funciona

### Test manual de URL TSV

Abrir en navegador:
```
https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhmqT_SMan7EeQRmStRS0jofd0VMQPvKemLZ_70Oiruj-yI1jh9ShgSuR7ZsFLMfz8wwDq5hde9Jo/pub?gid=197105959&single=true&output=tsv
```

**Debe mostrar:**
```tsv
centro_id	tipo_centro	codigo_dane	municipio	...
NODO_01	NODO_PRINCIPAL	1111001.0	BOGOTÁ, D.C.	...
NODO_02	NODO_PRINCIPAL	1111001.0	BOGOTÁ, D.C.	...
```

### Verificar en consola del navegador

1. Abrir mapa desplegado
2. Presionar F12 (DevTools)
3. Ir a pestaña "Console"
4. Buscar mensajes:
   ```
   [GOOGLE SHEETS] Cargados 197 centros exitosamente
   ```

**Si aparece error:**
```
[GOOGLE SHEETS] Error al cargar: ...
[CSV LOCAL] Cargados 197 centros desde fallback
```

Esto significa que cayó al fallback CSV local (aún funcional).

---

## 🎯 Checklist Final

Antes de compartir el mapa, verificar:

- [ ] Repositorio creado en GitHub
- [ ] Push exitoso (`git push`)
- [ ] GitHub Pages habilitado (Settings → Pages)
- [ ] URL del sitio generada
- [ ] Mapa se abre sin errores
- [ ] 197 marcadores visibles en Colombia
- [ ] Popups funcionan al hacer click
- [ ] Estadísticas muestran: 56 nodos + 141 satélites
- [ ] Google Sheets publicada como TSV
- [ ] Cache funciona (indicador visible)

---

## 📱 Compartir el Mapa

### URL corta para compartir

Puedes crear un enlace corto apuntando a:
```
https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_nacional.html
```

### Embed en otras páginas

```html
<iframe
    src="https://TU-USUARIO.github.io/ia_formulacion/services/github_pages/mapa_cale_nacional.html"
    width="100%"
    height="800px"
    frameborder="0">
</iframe>
```

---

## 🚀 Próximos Pasos

Una vez desplegado exitosamente:

1. **Verificar funcionamiento** en diferentes navegadores
2. **Documentar URL** en documentos del proyecto
3. **Compartir** con equipo MUNAY
4. **Monitorear** uso y performance
5. **Continuar** con visor BIM 3D (Xeokit ES6)

---

**¡Listo para desplegar!**

*Última actualización: 29 de octubre de 2025*
