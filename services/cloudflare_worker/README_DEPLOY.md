# 🚀 DEPLOY DEL CLOUDFLARE WORKER - GUÍA RÁPIDA

**Tiempo total:** 15 minutos
**Costo:** GRATIS (100,000 requests/día)

---

## ✅ PASO 1: CREAR SERVICE ACCOUNT (5 min)

### 1.1 Ir a Google Cloud Console
```
https://console.cloud.google.com/iam-admin/serviceaccounts
```

### 1.2 Crear Service Account
1. Clic **"+ Create Service Account"**
2. Nombre: `cale-bim-readonly`
3. Clic **"Create"** → **"Continue"** → **"Done"** (sin roles)

### 1.3 Descargar Clave JSON
1. Buscar `cale-bim-readonly` en la lista
2. Clic 3 puntos → **"Manage keys"**
3. **"Add Key"** → **"Create new key"** → **JSON**
4. Se descarga automáticamente

### 1.4 Compartir Google Sheets
1. Abrir el archivo JSON descargado
2. Copiar el `client_email` (ej: `cale-bim-readonly@proyecto.iam.gserviceaccount.com`)
3. Ir a tu Google Sheets
4. Clic **"Share"** → Pegar el email → Rol: **Viewer** → **"Share"**

✅ **Listo el service account!**

---

## 🌐 PASO 2: CREAR CLOUDFLARE WORKER (5 min)

### 2.1 Registrarse en Cloudflare Workers
```
https://workers.cloudflare.com/
```

- Clic **"Sign Up"** (gratis)
- Completar registro
- Verificar email

### 2.2 Crear Worker
1. Dashboard de Cloudflare → **"Workers & Pages"**
2. Clic **"Create application"**
3. Seleccionar **"Create Worker"**
4. Nombre: `cale-proxy` (o el que quieras)
5. Clic **"Deploy"**

✅ **Worker creado!**

---

## 📝 PASO 3: COPIAR CÓDIGO DEL WORKER (3 min)

### 3.1 Abrir Editor
1. En el worker recién creado, clic **"Edit code"**
2. Se abrirá el editor en línea

### 3.2 Reemplazar Código
1. **Borrar TODO** el código que viene por defecto
2. **Copiar TODO** el contenido de: `cale-proxy-worker.js`
3. **Pegar** en el editor

### 3.3 Configurar Credenciales
Buscar estas líneas en el código (arriba):

```javascript
const SERVICE_ACCOUNT = {
  client_email: "TU_SERVICE_ACCOUNT_EMAIL@proyecto.iam.gserviceaccount.com",
  private_key: `-----BEGIN PRIVATE KEY-----
TU_PRIVATE_KEY_AQUI_MULTIPLES_LINEAS
-----END PRIVATE KEY-----`
};
```

**Reemplazar con tus valores del archivo JSON:**

1. **client_email:** Copiar del JSON
2. **private_key:** Copiar del JSON (TODO, incluir `-----BEGIN` y `-----END`)

### 3.4 Deploy
1. Clic **"Save and Deploy"** (arriba derecha)
2. Esperar ~10 segundos

✅ **Worker desplegado!**

---

## 🔗 PASO 4: OBTENER URL Y PROBAR (2 min)

### 4.1 Copiar URL del Worker
En Cloudflare, verás algo como:
```
https://cale-proxy.tu-usuario.workers.dev
```

**Copiar esta URL.**

### 4.2 Probar que Funciona
Abrir en navegador:
```
https://cale-proxy.tu-usuario.workers.dev?health
```

Deberías ver algo como:
```json
{
  "status": "healthy",
  "timestamp": "2025-10-31T...",
  "sheets_available": ["nodos", "municipios"]
}
```

✅ Si ves esto, **¡funciona!**

### 4.3 Probar Carga de Datos
```
https://cale-proxy.tu-usuario.workers.dev?sheet=nodos
```

Deberías ver JSON con los 197 nodos.

---

## ⚙️ PASO 5: CONFIGURAR FRONTEND (2 min)

### 5.1 Actualizar data-loader.js

**Opción A: Reemplazar archivo completo**
1. Renombrar `data-loader.js` a `data-loader-OLD.js`
2. Renombrar `data-loader-proxy.js` a `data-loader.js`

**Opción B: Editar línea 16**
Abrir `data-loader-proxy.js` y buscar:
```javascript
PROXY_URL: 'https://cale-proxy.TU-USUARIO.workers.dev',
```

Reemplazar con tu URL del worker.

### 5.2 Actualizar mapa_interactivo.html

Buscar la línea:
```html
<script src="js/data-loader.js"></script>
```

Si usaste Opción A, está listo.
Si usaste Opción B, cambiar a:
```html
<script src="js/data-loader-proxy.js"></script>
```

### 5.3 Probar Localmente
1. Abrir `mapa_interactivo.html` en navegador
2. Abrir DevTools (F12) → Console
3. Deberías ver:
   ```
   [DataLoader] Módulo inicializado con proxy seguro
   [DataLoader] ✅ Proxy funcionando
   [DataLoader] 197 nodos cargados exitosamente
   ```

✅ **¡Funciona localmente!**

---

## 🚀 PASO 6: DEPLOY A GITHUB PAGES (3 min)

### 6.1 Commit y Push
```bash
cd c:\raziel\ia_formulacion

git add services/github_pages/js/data-loader-proxy.js
git add services/github_pages/mapa_interactivo.html
git add services/cloudflare_worker/

git commit -m "feat: Agregar proxy seguro con Cloudflare Worker

- Service Account para autenticación segura
- Credenciales nunca expuestas en frontend
- Worker como proxy entre HTML y Google Sheets
- 100% transparente para el usuario

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin main
```

### 6.2 Verificar en Producción
Esperar 2-3 minutos, luego abrir:
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_interactivo.html
```

✅ **¡Producción funcionando!**

---

## 🔐 SEGURIDAD - PREGUNTAS FRECUENTES

### ¿Es seguro exponer el Worker públicamente?

✅ **SÍ, completamente seguro:**
- Service Account tiene SOLO permisos de **lectura**
- Private key está SOLO en Cloudflare (no en HTML)
- Usuarios NO pueden ver las credenciales
- Rate limiting automático de Cloudflare

### ¿Qué puede hacer alguien con acceso al Worker?

Pueden:
- ✅ Leer datos de Google Sheets (que ya son públicos de solo lectura)
- ✅ Ver la cantidad de requests

NO pueden:
- ❌ Modificar datos
- ❌ Ver el private key
- ❌ Acceder a otras hojas no configuradas
- ❌ Hacer requests ilimitados (Cloudflare limita)

### ¿Alguien puede copiar el código del Worker?

❌ **NO.** El código del Worker NO es visible públicamente.
Solo tú puedes verlo/editarlo en el dashboard de Cloudflare.

### ¿Qué pasa si subo el archivo JSON a GitHub?

⚠️ **NO HACER ESTO.** Agregarlo a `.gitignore`:

```bash
# .gitignore
*.json
!package.json
services/cloudflare_worker/*.json
```

Si ya lo subiste, **rotar** las credenciales:
1. Ir a Google Cloud → Service Accounts
2. Eliminar la clave antigua
3. Crear clave nueva
4. Actualizar Worker con nueva clave

---

## 📊 MONITOREO

### Ver Requests en Tiempo Real
1. Dashboard Cloudflare → Tu Worker
2. Clic en **"Metrics"**
3. Ver:
   - Requests por minuto
   - Latencia promedio
   - Errores

### Límites Gratuitos
- **100,000 requests/día** (Cloudflare Free)
- **Latencia:** ~50-100ms promedio
- **Uptime:** 99.9%+

---

## 🐛 TROUBLESHOOTING

### Error: "Invalid grant"
**Causa:** Private key mal copiado.
**Solución:** Verificar que copiaste TODO el private_key (incluir BEGIN y END).

### Error: "Permission denied"
**Causa:** No compartiste Google Sheets con el service account.
**Solución:** Verificar que el email del service account está en "Share" del Google Sheets como Viewer.

### Worker responde pero no hay datos
**Causa:** Spreadsheet ID incorrecto.
**Solución:** Verificar la línea `const SPREADSHEET_ID` en el worker.

### CORS error en navegador
**Causa:** Headers CORS no configurados.
**Solución:** Ya están configurados en el código del worker. Si persiste, limpiar caché del navegador.

---

## ✅ CHECKLIST FINAL

- [ ] Service Account creado en Google Cloud
- [ ] Archivo JSON descargado
- [ ] Google Sheets compartido con service account (Viewer)
- [ ] Cloudflare Worker creado
- [ ] Código del worker copiado y configurado
- [ ] Worker desplegado
- [ ] URL del worker obtenida
- [ ] Health check funcionando (`?health`)
- [ ] Datos de nodos cargando (`?sheet=nodos`)
- [ ] Frontend actualizado con URL del worker
- [ ] Probado localmente (DevTools sin errores)
- [ ] Pusheado a GitHub
- [ ] Funcionando en producción

---

## 🎉 ¡COMPLETADO!

Tu sistema ahora es:
- ✅ **Seguro** - Credenciales nunca expuestas
- ✅ **Transparente** - Usuario no configura nada
- ✅ **Escalable** - 100k requests/día gratis
- ✅ **Rápido** - Cache de 1 hora
- ✅ **Mantenible** - Datos en Google Sheets

**Próximo paso:** Compartir URL con equipo y disfrutar 🎊

---

**Última actualización:** 2025-10-31
**Versión:** 1.0
**Soporte:** Ver logs en Cloudflare Dashboard → Worker → Logs
