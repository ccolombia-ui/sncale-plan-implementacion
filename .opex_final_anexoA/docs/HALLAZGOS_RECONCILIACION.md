# 📊 HALLAZGOS - RECONCILIACIÓN ANEXO A, B Y FICHAS TÉCNICAS

**Fecha**: 2025-11-05  
**Documento**: Tabla Maestra de Reconciliación  
**Fuentes**: Anexo A (OPEX), Anexo B (CAPEX Infraestructura), Plan v4.1, Fichas Técnicas  

---

## 🎯 RESUMEN EJECUTIVO

Se realizó la reconciliación de **tres documentos oficiales** para asegurar coherencia en el modelo económico del Sistema Nacional de CALEs:

1. **Anexo A** (Google Doc): Modelo operativo y presupuesto OPEX
2. **Anexo B** (Google Doc): Infraestructura física y equipamiento CAPEX
3. **Plan v4.1** (Google Doc): Modelo IO Sistema Nacional de CALEs
4. **Fichas Técnicas** (TABLAS_L3_CALE_TEORICO.json): Valores unitarios componentes L3

### ✅ Conclusión Principal

**Los documentos presentan diferencias metodológicas esperadas** debido al alcance diferenciado de cada fuente:

- **Fichas Técnicas**: Solo CALE-T (centro teórico + equipamiento TIC)
- **Anexo B**: Infraestructura completa L2 (pistas + edificación + CALE-T + tecnología)
- **Plan v4.1**: Valores de implementación (incluye CALE_P + CALE_T + satélites - OPEX excluidos)

---

## 📋 VALORES UNITARIOS POR CONFIGURACIÓN

### CALE.n_1 (24 cubículos - Centros Metropolitanos)

| Fuente | Valor Unitario | Alcance |
|--------|----------------|---------|
| **Ficha Técnica** | $645,000,000 | Solo CALE-T (centro teórico 24q) |
| **Plan v4.1** | $10,578,613,165 | CALE_P + CALE_T + satélites - OPEX |
| **Anexo B** | $7,066,000,000 | Pistas + edificación + CALE-T completo |
| **OPEX Mensual** | $136,910,000/mes | TTHH $134.25M + Munay $1.48M + Aleya $1.18M |

**Diferencia Plan.41 vs AnexoB**: +$3,512M (+49.7%)  
**Explicación**: Plan.41 incluye satélites (7 × $12M = $84M) y equipamiento adicional no contemplado en AnexoB unitario base.

---

### CALE.n_2 (16 cubículos - Centros Subregionales)

| Fuente | Valor Unitario | Alcance |
|--------|----------------|---------|
| **Ficha Técnica** | $460,000,000 | Solo CALE-T (centro teórico 16q) |
| **Plan v4.1** | $14,606,966,197 | CALE_P + CALE_T + satélites (mitad) - OPEX |
| **Anexo B** | $4,925,000,000 | Pistas + edificación + CALE-T completo |
| **OPEX Mensual** | $93,826,666/mes | TTHH $91.17M + Munay $1.48M + Aleya $1.18M |

**Diferencia Plan.41 vs AnexoB**: +$9,681M (+196.6%)  
**Explicación**: Diferencia significativa requiere validación. Posible inclusión de componentes L2 adicionales (pistas Clase II ampliadas, edificación mejorada) o error de cálculo en Plan.41.

---

### CALE.n_3 (4 cubículos - Centros Locales)

| Fuente | Valor Unitario | Alcance |
|--------|----------------|---------|
| **Ficha Técnica** | $175,000,000 | Solo CALE-T (centro teórico 4q) |
| **Plan v4.1** | $6,263,963,197 | CALE_P + CALE_T + satélites (mitad) - OPEX |
| **Anexo B** | $200,646,497 | Solo CALE-T (CAPEX parcial, sin pistas) |
| **OPEX Mensual** | $53,993,333/mes | TTHH $51.33M + Munay $1.48M + Aleya $1.18M |

**Diferencia Plan.41 vs AnexoB**: +$6,063M (+3,021.9%)  
**Explicación**: Discrepancia extrema. Plan.41 parece incluir componentes L2 completos (pistas, edificación) mientras AnexoB solo valoriza CALE-T. **Requiere revisión urgente**.

---

## 🔍 ANÁLISIS DETALLADO DE DISCREPANCIAS

### 1️⃣ Ficha vs Anexo B (ESPERADO)

**Ficha Técnica << Anexo B** en todos los casos:
- CALE.n_1: $645M vs $7,066M (×10.95)
- CALE.n_2: $460M vs $4,925M (×10.70)
- CALE.n_3: $175M vs $200M (×1.15)

**Explicación**: Las fichas técnicas **solo valorizan el componente CALE-T** (centro teórico + equipamiento TIC), mientras que el Anexo B incluye:
- ✅ Pistas de evaluación práctica (Clase I, II, III según configuración)
- ✅ Edificación administrativa y servicios
- ✅ CALE-T completo (24q, 16q, o 4q)
- ✅ Tecnología (datacenter, red, seguridad)
- ✅ Certificaciones y seguros

**Recomendación**: ✅ **Coherente - sin ajustes requeridos**. Esta diferencia es metodológica y esperada.

---

### 2️⃣ Plan v4.1 vs Anexo B (CRÍTICO)

**Plan.41 >> Anexo B** en todos los casos:
- CALE.n_1: $10,578M vs $7,066M (+49.7%)
- CALE.n_2: $14,606M vs $4,925M (+196.6%) ⚠️
- CALE.n_3: $6,263M vs $200M (+3,021.9%) ⚠️⚠️⚠️

**Posibles causas**:

#### CALE.n_1 (+$3,512M):
- ✅ Satélites incluidos en Plan.41: 7 × $12M = $84M
- ✅ CALE_P (pistas) valorizado diferente
- ✅ Equipamiento adicional (simuladores, vehículos)
- ⚠️ Verificar que OPEX fue correctamente excluido

#### CALE.n_2 (+$9,681M):
- ⚠️ **ALERTA**: Diferencia de ~$10B requiere explicación
- Posible duplicación de componentes L2 en Plan.41
- Verificar cálculo de compose_from_plan_v41.py
- Comparar con valores de TABLAS_L3_CALE_TEORICO.json

#### CALE.n_3 (+$6,063M):
- ⚠️⚠️⚠️ **CRÍTICO**: Diferencia de $6B es inaceptable
- Anexo B solo valoriza CALE-T ($200M) sin pistas
- Plan.41 parece incluir infraestructura completa
- **Acción requerida**: Revisar sección B30.3 del Anexo B para completar valorización de pistas y edificación CALE.n_3

---

### 3️⃣ OPEX Mensual (Anexo A)

Valores OPEX extraídos de **Anexo A, Sección A40**:

| Config | TTHH/mes | Munay/mes | Aleya/mes | Total OPEX/mes |
|--------|----------|-----------|-----------|----------------|
| CALE.n_1 (24q) | $134,250,000 | $1,480,000 | $1,180,000 | $136,910,000 |
| CALE.n_2 (16q) | $91,166,666 | $1,480,000 | $1,180,000 | $93,826,666 |
| CALE.n_3 (4q) | $51,333,333 | $1,480,000 | $1,180,000 | $53,993,333 |

**Fuente**:
- TTHH: Anexo A.40.1 (distribución por categoría Cat.A/B/C1)
- Munay: $3,500M/año ÷ 197 sedes ÷ 12 meses = $1.48M/sede/mes
- Aleya: $2,800M/año ÷ 197 sedes ÷ 12 meses = $1.18M/sede/mes

**Validación**: ✅ Valores coherentes con presupuesto OPEX consolidado Anexo A ($113.5B/año total)

---

## 🎯 RECOMENDACIONES

### 🔴 URGENTE

1. **Revisar cálculo CALE.n_3 en Plan v4.1**
   - Diferencia de $6B (+3,021%) es crítica
   - Verificar script `compose_from_plan_v41.py`
   - Comparar con valores L3 oficiales en TABLAS_L3_CALE_TEORICO.json

2. **Completar valorización Anexo B sección B30.3**
   - Actualmente solo incluye CALE-T ($200M)
   - Falta valorización de:
     - Pista Clase I (1 circuito × 16 sedes)
     - Edificación adecuada (arriendo)
     - Tecnología y certificaciones

3. **Validar CALE.n_2 en Plan v4.1**
   - Diferencia de $9.6B (+196%) requiere explicación detallada
   - Verificar si incluye componentes duplicados o OPEX no excluido

### 🟡 MEDIA PRIORIDAD

4. **Obtener documento USCO** (C:\raziel\...\uscocalemania__v4.docx)
   - Actualmente no accesible
   - Valores de referencia permitirían triangulación adicional

5. **Refinar valores OPEX plataformas**
   - Validar distribución Munay/Aleya por sede
   - Confirmar que $1.48M/mes y $1.18M/mes son correctos
   - Verificar si algunas configuraciones requieren valores diferenciados

### 🟢 BAJA PRIORIDAD

6. **Documentar diferencias metodológicas**
   - Crear tabla explicativa de alcance por fuente
   - Publicar en sección metodología de cada anexo

7. **Actualizar fichas técnicas GitHub Pages**
   - Asegurar que valores publicados NO incluyen OPEX
   - Agregar disclaimer explicando alcance (solo CALE-T)

---

## 📝 NOTAS METODOLÓGICAS

### Exclusiones OPEX aplicadas en Plan v4.1

El script `compose_from_plan_v41.py` resta los siguientes valores OPEX anuales:

| Config | Software/RRHH | Arrendamiento | Total Excluido |
|--------|---------------|---------------|----------------|
| CALE.n_1 (24q) | $267M/año | $84M/año | $351M/año |
| CALE.n_2 (16q) | $225M/año | $42M/año | $267M/año |
| CALE.n_3 (4q) | Pendiente cálculo | Pendiente cálculo | - |

**Fuente**: TABLAS_L3_CALE_TEORICO.json, función `read_l3_opex()`

### Modelo OPEX (Anexo A)

Todo el presupuesto de inversión se gestiona como **OPEX** bajo tres blueprints:

1. **Infraestructura física**: Arrendamiento/leasing (Anexo B)
2. **Plataformas tecnológicas**: PaaS (Anexo A.40.2)
3. **Talento humano**: Contratación UPTC (Anexo A.40.1)

Este modelo permite:
- ✅ Flexibilidad operativa
- ✅ Menor riesgo de inversión inicial
- ✅ Escalabilidad según demanda
- ✅ Mantenimiento incluido en contratos

---

## 📂 ARCHIVOS GENERADOS

```
.opex_final_anexoA/
├── data/
│   ├── anexo_a_raw.txt (81,188 chars - extraído Google Docs API)
│   ├── anexo_b_raw.txt (113,045 chars - extraído Google Docs API)
│   └── plan_41_raw.txt (96,996 chars - extraído Google Docs API)
├── scripts/
│   ├── extract_google_docs.py (extracción con service account)
│   └── parse_and_consolidate.py (parser y tabla maestra)
├── output/
│   └── tabla_maestra_reconciliacion.csv (tabla consolidada)
└── docs/
    ├── METODOLOGIA_COHERENCIA_ANEXOS.md
    └── HALLAZGOS_RECONCILIACION.md (este documento)
```

---

## 🔗 REFERENCIAS

- **Anexo A**: https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4/edit
- **Anexo B**: https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE/edit
- **Plan v4.1**: https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg/edit
- **Fichas Técnicas**: https://ccolombia-ui.github.io/sncale-plan-implementacion/
- **Resolución**: https://drive.google.com/file/d/1ShD6cUQIc07M7ye9JrsKvPVo6jmYBPiS/view

---

**Generado automáticamente por**: `parse_and_consolidate.py`  
**Última actualización**: 2025-11-05
