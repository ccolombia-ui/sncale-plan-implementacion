# ✅ VERIFICACIÓN DE FUENTES ACTUALIZADAS

**Fecha de extracción:** 2025-11-05  
**Método:** Google Docs API (Service Account)  
**Estado:** ✅ Actualizado y verificado

---

## 📡 CONEXIÓN DIRECTA A GOOGLE DOCS

### Método de Extracción

Los documentos **NO son copias manuales**. Se extraen automáticamente usando:

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Autenticación
creds = service_account.Credentials.from_service_account_file(
    'c:/guezarel/.secrets/google-service-account.json',
    scopes=['https://www.googleapis.com/auth/documents.readonly']
)

# Conexión API
service = build('docs', 'v1', credentials=creds)

# Extracción directa
doc = service.documents().get(documentId=doc_id).execute()
```

### 🔗 Documentos Oficiales

| Documento | ID | URL | Estado |
|-----------|----|----|---------|
| **Anexo A** | `1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4` | [Ver Doc](https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4/edit) | ✅ Extraído |
| **Anexo B** | `16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE` | [Ver Doc](https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE/edit) | ✅ Extraído |
| **Plan v4.1** | `1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg` | [Ver Doc](https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg/edit) | ✅ Extraído |

---

## 📊 VALORES VERIFICADOS (Última Extracción)

### Anexo B - Valores CAPEX por Configuración

Extraídos directamente de las secciones B10.3, B20.3, B30.3:

#### CALE.n_1 (20 nodos)
```
CAPEX TOTAL CATEGORÍA CALE.N_1: $141,320,000,000 COP
```

**Desglose unitario** ($141.32B ÷ 20 = $7.066B por nodo):
- Pista Clase III: $1,850,000,000
- Pista Clase II: $980,000,000
- Pista Clase I: $750,000,000
- Sala 24 cubículos: $186,000,000
- Simulador C3: $450,000,000
- Edificación admin: $2,400,000,000
- **Subtotal pistas y sala:** $4,216,000,000
- **Diferencia (otros componentes):** $2,850,000,000

#### CALE.n_2 (20 nodos)
```
CAPEX TOTAL ESTIMADO CATEGORÍA CALE.N_2: ~$98,500,000,000 COP
CAPEX PARCIAL (solo componentes valorizados): $4,012,929,940 COP
```

**Unitario** ($98.5B ÷ 20 = $4.925B por nodo):
- CALE-T 16q: $200,646,497
- Pistas + edificación (estimado): ~$4,724,353,503

⚠️ **Nota:** Anexo B indica "componentes L2 pendientes de valorización"

#### CALE.n_3 (16 nodos)
```
CAPEX PARCIAL CATEGORÍA CALE.N_3: $3,210,343,952 COP
```

**Unitario** ($3.21B ÷ 16 = $200.6M por nodo):
- CALE-T 16q: $200,646,497
- Pista Clase I: **"Ver L2" (sin valorizar)**
- Edificación: **"Ver L2" (sin valorizar)**

🔴 **ALERTA:** Valorización incompleta. Solo incluye CALE-T.

---

## 🔄 PROCEDIMIENTO DE ACTUALIZACIÓN

### Para refrescar los datos:

1. **Ejecutar extractor:**
   ```bash
   python .opex_final_anexoA/scripts/extract_google_docs.py
   ```

2. **Regenerar tabla de reconciliación:**
   ```bash
   python .opex_final_anexoA/scripts/parse_and_consolidate.py
   ```

3. **Verificar actualización:**
   ```bash
   # Ver fecha de modificación de archivos extraídos
   dir .opex_final_anexoA\data\*.txt
   ```

### Archivos Generados

```
.opex_final_anexoA/
├── data/
│   ├── anexo_a_raw.txt    (81,188 chars) ← Extraído de API
│   ├── anexo_b_raw.txt    (113,045 chars) ← Extraído de API
│   └── plan_41_raw.txt    (96,996 chars) ← Extraído de API
├── output/
│   └── tabla_maestra_reconciliacion.csv ← Generado desde data/
└── scripts/
    ├── extract_google_docs.py ← Extractor API
    └── parse_and_consolidate.py ← Parser y generador tabla
```

---

## ✅ CONFIRMACIÓN DE COHERENCIA

### Valores Anexo B coinciden con extracción

| Config | Total Nacional | Nodos | Unitario | Verificado |
|--------|---------------|-------|----------|------------|
| CALE.n_1 | $141.32B | 20 | $7.066B | ✅ Sí |
| CALE.n_2 | $98.5B | 20 | $4.925B | ✅ Sí |
| CALE.n_3 | $3.21B | 16 | $200.6M | ✅ Sí |

### Componentes Verificados en Anexo B

✅ **Sección B10.3** (CALE.n_1): Tabla completa con 6 componentes valorizados  
✅ **Sección B20.3** (CALE.n_2): Tabla con valorización parcial (estimado)  
⚠️ **Sección B30.3** (CALE.n_3): Tabla con valorización incompleta (solo CALE-T)

---

## 🎯 PRÓXIMOS PASOS

### Para mantener sincronización:

1. **Automatizar extracción periódica** (ejemplo: GitHub Actions diario)
2. **Agregar notificación** cuando Google Docs cambien
3. **Validar cambios** antes de regenerar tabla maestra
4. **Versionado** de extracciones (guardar histórico)

### Script de automatización sugerido:

```python
# Ejemplo: extract_and_notify.py
import datetime
from pathlib import Path

def check_for_updates():
    old_hash = get_file_hash('anexo_b_raw.txt')
    extract_google_docs()  # Extraer versión actual
    new_hash = get_file_hash('anexo_b_raw.txt')
    
    if old_hash != new_hash:
        notify_slack(f'📄 Anexo B actualizado: {datetime.now()}')
        regenerate_tables()
```

---

## 📞 CONTACTO

**Service Account:** `aksobhya-googlesheet-806@aksobhya.iam.gserviceaccount.com`  
**Proyecto:** `aksobhya`  
**Credenciales:** `c:/guezarel/.secrets/google-service-account.json`

---

**Última verificación:** 2025-11-05  
**Próxima actualización recomendada:** Según cambios en Google Docs
