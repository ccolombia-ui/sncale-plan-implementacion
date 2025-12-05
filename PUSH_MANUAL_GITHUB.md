# Push Manual a GitHub

## 🔴 Problema Actual

El push falló porque las credenciales en el sistema son de otro usuario (`manjushry`).

## ✅ Solución: Push Manual

### Paso 1: Abrir Terminal/CMD

1. Presiona `Win + R`
2. Escribe `cmd` y presiona Enter
3. Navega al directorio:
   ```bash
   cd c:\raziel\ia_formulacion
   ```

### Paso 2: Verificar que el commit está listo

```bash
git status
```

**Debe mostrar:**
```
On branch main
nothing to commit, working tree clean
```

### Paso 3: Hacer el push

```bash
git push -u origin main
```

**GitHub te pedirá autenticación.** Tienes 2 opciones:

#### Opción A: Con Personal Access Token (Recomendado)

1. **Crear un nuevo token** (EL ANTERIOR DEBES REVOCARLO):
   - Ve a: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Nombre: `sncale-push-token`
   - Expiration: 90 days (o lo que prefieras)
   - Scopes: Marca **"repo"** (acceso completo a repositorios)
   - Click "Generate token"
   - **COPIA EL TOKEN** (solo se muestra una vez)

2. **Usar el token como contraseña:**
   - Username: `ccolombia-ui`
   - Password: **[PEGA EL TOKEN AQUÍ]**

#### Opción B: Con GitHub Desktop

1. Descargar GitHub Desktop: https://desktop.github.com/
2. Instalar y hacer login con tu cuenta
3. File → Add Local Repository
4. Seleccionar: `C:\raziel\ia_formulacion`
5. Click "Push origin"

### Paso 4: Verificar que el push fue exitoso

```bash
git log --oneline
```

Debes ver:
```
1890ed1 (HEAD -> main, origin/main) Implementar mapa interactivo Red Nacional CALE con Google Sheets
```

## 🌐 Configurar GitHub Pages

Una vez que el push sea exitoso:

1. Ve a: https://github.com/ccolombia-ui/sncale-plan-implementacion
2. Click en **Settings**
3. En el menú lateral, click en **Pages**
4. En "Source":
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

**¡Listo!** En 1-2 minutos tu mapa estará disponible en:

```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_nacional.html
```

## 📊 URLs del Mapa

### Mapa Principal (Google Sheets)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_nacional.html
```

### Mapa Funcionando (CSV Fallback)
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_funcionando.html
```

### Utilidad Limpieza Cache
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/limpiar_cache.html
```

## 🔧 Alternativa: Cambiar URL a SSH

Si tienes SSH configurado:

```bash
git remote set-url origin git@github.com:ccolombia-ui/sncale-plan-implementacion.git
git push -u origin main
```

---

**Resumen:**
1. ✅ Commit creado con 56 archivos
2. ⏳ Pendiente: Push manual con tus credenciales
3. ⏳ Pendiente: Habilitar GitHub Pages
4. ⏳ Pendiente: Verificar mapa en producción
