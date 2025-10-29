# Solución: Token en Historial de Git

## 🔴 Problema

GitHub bloqueó el push porque detectó un token en el commit inicial (`1890ed1`).

## ✅ Solución Rápida (RECOMENDADA)

### 1. Permitir el secreto temporalmente

Ve a esta URL y click "Allow secret":
```
https://github.com/ccolombia-ui/sncale-plan-implementacion/security/secret-scanning/unblock-secret/34l5mdgoVxZ5mnVyddw5zYxjLjL
```

### 2. Hacer push

```bash
cd c:\raziel\ia_formulacion
git push origin main
```

### 3. IMPORTANTE: Revocar el token

Una vez que el push funcione, **DEBES** revocar el token:
1. Ve a: https://github.com/settings/tokens
2. Busca el token `ghp_TxH5XT93...`
3. Click "Delete" o "Revoke"

## ✅ Solución Limpia (SIN token en historial)

Si prefieres NO tener el token en el historial:

```bash
cd c:\raziel\ia_formulacion

# 1. Eliminar historial local
rm -rf .git

# 2. Reinicializar repositorio
git init
git branch -M main

# 3. Eliminar archivo con token
rm PROMPT_ARREGLAR_VISOR_3D.md

# 4. Agregar todos los archivos
git add .

# 5. Nuevo commit limpio
git commit -m "Implementar mapa CALE con Google Sheets

- Mapa interactivo 197 centros
- Integracion Google Sheets TSV
- Scripts Python automatizacion
- Documentacion completa

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. Agregar remote
git remote add origin https://github.com/ccolombia-ui/sncale-plan-implementacion.git

# 7. Force push (sobrescribir)
git push -u origin main --force
```

**⚠️ IMPORTANTE:** Esto sobrescribirá el repositorio remoto completamente.

## 🚀 Después del Push

Una vez que el push sea exitoso:

### 1. Habilitar GitHub Pages

1. Ve a: https://github.com/ccolombia-ui/sncale-plan-implementacion/settings/pages
2. Source:
   - Branch: `main`
   - Folder: `/ (root)`
3. Click "Save"

### 2. Verificar despliegue

Espera 1-2 minutos y visita:
```
https://ccolombia-ui.github.io/sncale-plan-implementacion/services/github_pages/mapa_cale_nacional.html
```

## 📋 Checklist

- [ ] Push exitoso
- [ ] Token revocado
- [ ] GitHub Pages habilitado
- [ ] Mapa funcionando en producción
- [ ] Google Sheets publicada como TSV

---

**Recomendación:** Usa Opción 1 (permitir secreto) si quieres desplegar rápido, luego revoca el token inmediatamente.
