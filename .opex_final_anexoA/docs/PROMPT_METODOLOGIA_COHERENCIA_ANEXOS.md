# Metodología de Coherencia: Anexos A, B, C y Plan v4.1

## Contexto del Modelo de Inversión OPEX

El Sistema Nacional de Centros de Enseñanza de Conductores y Evaluación para Licencias (SNCALE) se diseña bajo un **modelo de gestión 100% OPEX**, donde toda la inversión inicial se convierte en gasto operativo recurrente a través de tres mecanismos:

### 1. Infraestructura Física y Equipamiento → Arrendamiento/Leasing
- **Anexo B** documenta la inversión inicial de infraestructura y equipamiento operativo/TIC
- **Fichas Técnicas (Anexo C)** proveen el detalle técnico BIM 5D para cada componente
- **Modelo OPEX**: Se gestiona mediante arrendamiento de inmuebles + leasing de equipamiento
- **Regla clave**: `vr_unitario(AnexoB) = vr_unitario(FichaTécnica)` → coherencia valor técnico

### 2. Plataformas Tecnológicas → PaaS (Platform as a Service)
- **Anexo A** documenta costos mensuales de plataformas (Munay, Aleya) y licencias TIC
- **Modelo OPEX**: Plataforma tecnológica + infraTIC + equipoTIC se gestionan como servicio bajo demanda
- **Valores mensuales**: `anxA.vr_mes_munay`, `anxA.vr_mes_aleya`, `anxA.vr_mes_infraTIC`

### 3. Talento Humano → Demanda Asegurada (UPTC)
- **Anexo A** documenta costos mensuales de talento humano por configuración CALE
- **Modelo OPEX**: Personal operativo contratado bajo demanda/nómina mensual
- **Valor mensual**: `vr_mes_tthh` (coordinador + auxiliares + recepción)

## Arquitectura Documental

```
┌─────────────────────────────────────────────────────────────────┐
│  ANEXO A: Modelo Financiero OPEX                                │
│  https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLG... │
│  ────────────────────────────────────────────────────────────   │
│  • Talento Humano (mensual)                                     │
│  • Plataformas Tecnológicas (Munay, Aleya, licencias)          │
│  • Presupuesto Operativo (última sección)                       │
│  • Filosofía: TODO se gestiona como OPEX                        │
└─────────────────────────────────────────────────────────────────┘
                           ↓ valores mensuales
┌─────────────────────────────────────────────────────────────────┐
│  ANEXO B: Inversión Infraestructura + Equipamiento              │
│  https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krj... │
│  ────────────────────────────────────────────────────────────   │
│  • Infraestructura física (edificación, adecuaciones)           │
│  • Equipamiento operativo (mobiliario, vehículos)               │
│  • Equipamiento TIC (servidores, red, cubículos evaluación)     │
│  • Suficiencia Técnica (cumplimiento normativo)                 │
└─────────────────────────────────────────────────────────────────┘
                           ↓ vr_unitario = vr_ficha
┌─────────────────────────────────────────────────────────────────┐
│  ANEXO C: Fichas Técnicas BIM 5D                                │
│  https://ccolombia-ui.github.io/sncale-plan-implementacion/     │
│  ────────────────────────────────────────────────────────────   │
│  • Detalle técnico por componente L0, L1, L2, L3                │
│  • Modelo BIM recursivo (composición por niveles)               │
│  • Especificaciones, normativa, APUs                            │
│  • Valores unitarios = Anexo B (coherencia técnico-financiera)  │
└─────────────────────────────────────────────────────────────────┘
                           ↓ agregación L3 → CALE
┌─────────────────────────────────────────────────────────────────┐
│  PLAN v4.1: Presupuesto Consolidado Nacional                    │
│  https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRU... │
│  ────────────────────────────────────────────────────────────   │
│  • CALE-P (Pistas): Clase I, II, III por configuración          │
│  • CALE-T (Teórico): 24q, 16q, 4q                               │
│  • Presupuesto nacional agregado                                │
│  • Cantidades por tipo de CALE (n_1, n_2, n_3, n_1+)            │
└─────────────────────────────────────────────────────────────────┘
                           ↓ referencia cruzada
┌─────────────────────────────────────────────────────────────────┐
│  REFERENCIA USCO: Proyecto Calemania (externo)                  │
│  C:\raziel\aktriel\01__min_transporte\02__uscocalemania\...     │
│  ────────────────────────────────────────────────────────────   │
│  • Valores referenciales de proyecto similar                    │
│  • Benchmark para validar coherencia                            │
│  • Considera más vehículos (pistas completas desde Fase 1)      │
└─────────────────────────────────────────────────────────────────┘
```

## Tabla de Reconciliación (Objetivo del Análisis)

La tabla maestra de coherencia debe consolidar por cada configuración L3:

| Columna | Descripción | Fuente |
|---------|-------------|--------|
| `L3.componente` | Código configuración CALE (ej: CALE.n_1, CALE.n_2, CALE.n_3, CALE.n_1+) | TABLAS_L3_CALE_TEORICO.json |
| `vr_ficha` | Valor unitario CAPEX según ficha técnica (infraestructura + equipamiento, **SIN** TTHH ni plataformas) | Fichas Técnicas HTML + JSON |
| `vr_plan.41` | Valor unitario según Plan v4.1 (CALE-P + CALE-T + satélites) | Plan v4.1 Google Doc |
| `vr_anexoB` | Valor unitario según Anexo B (debe coincidir con `vr_ficha`) | Anexo B Google Doc |
| `ref_usco` | Valor referencial proyecto USCO-Calemania | uscocalemania__v4.docx |
| `vr_mes_tthh` | Costo mensual talento humano (coordinador + auxiliares + recepcionista) | Anexo A (sección TTHH) |
| `anxA.vr_mes_munay` | Costo mensual plataforma Munay (check-in + reportes + biometría) | Anexo A (sección plataformas) |
| `anxA.vr_mes_aleya` | Costo mensual plataforma Aleya (evaluación teórica + banco preguntas) | Anexo A (sección plataformas) |
| `comentario_analisis` | Observaciones sobre coherencia/discrepancias entre fuentes | Análisis automatizado |
| `recomendacion` | Acción propuesta para resolver inconsistencias | Análisis automatizado |

### Ejemplo de fila esperada:

```csv
L3.componente,vr_ficha,vr_plan.41,vr_anexoB,ref_usco,vr_mes_tthh,anxA.vr_mes_munay,anxA.vr_mes_aleya,comentario_analisis,recomendacion
CALE.n_1,10311613165,10335549700,10311613165,12500000000,16500000,1500000,2000000,"vr_ficha y anexoB coherentes (igual). Plan.41 incluye +24M (posible sala_form). USCO +2.2B (más vehículos fase 1). TTHH y plataformas NO incluidos en CAPEX (correcto según modelo OPEX).","Validar si Plan.41 debe incluir sala_form en CALE.n_1 base. Revisar USCO contra Resolución de pertinencia para ajustar vehículos fase 1."
```

## Reglas de Coherencia

### 1. Infraestructura y Equipamiento
- ✅ `vr_ficha == vr_anexoB` (obligatorio)
- ⚠️ `vr_plan.41 ≈ vr_ficha + ajustes_explícitos` (satélites, sala_form)
- 📊 `ref_usco` es referencia externa; puede variar por alcance de proyecto

### 2. OPEX (Talento + Plataformas)
- ✅ `vr_ficha` **NO** incluye `vr_mes_tthh` ni plataformas (estos son OPEX puro)
- ✅ `vr_anexoB` **NO** incluye TTHH ni plataformas
- ✅ Anexo A documenta OPEX mensual; conversión anual = `vr_mes * 12`

### 3. Exclusiones del CAPEX (aplicadas)
- Software (Munay, Aleya, licencias) → Anexo A mensual
- RRHH (talento humano) → Anexo A mensual
- Arrendamiento → Anexo A mensual (no es inversión, es OPEX)

### 4. Modelo de Conversión OPEX
```
CAPEX_inicial (Anexo B + Fichas) 
  → Arrendamiento mensual (inmueble) 
  + Leasing mensual (equipamiento)
  = OPEX_infraestructura/mes

CAPEX_plataformas (software) 
  → PaaS mensual (Munay + Aleya + licencias)
  = OPEX_tecnologia/mes

CAPEX_TTHH (contratación inicial) 
  → Nómina mensual (demanda asegurada UPTC)
  = OPEX_personal/mes

═══════════════════════════════════════════
TOTAL_OPEX_mensual = infraestructura + tecnologia + personal
```

## Plan de Trabajo: Reconciliación en 7 Pasos

### Paso 1: Extraer datos Anexo A (Google Doc)
- URL: https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4
- Buscar secciones:
  - Talento Humano por configuración (24q, 16q, 4q)
  - Plataforma Munay (costo mensual)
  - Plataforma Aleya (costo mensual)
  - Infraestructura TIC mensual
- **Acción**: Usar herramienta `fetch_webpage` o API Google Docs para extraer texto y parsear valores COP/mes

### Paso 2: Extraer datos Anexo B (Google Doc)
- URL: https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
- Buscar secciones por configuración CALE (n_1, n_2, n_3, n_1+)
- Identificar valores unitarios de infraestructura + equipamiento
- **Acción**: Parsear tablas/secciones y mapear a configuraciones L3

### Paso 3: Extraer datos Plan v4.1 (Google Doc)
- URL: https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg
- Buscar:
  - CALE-P Clase I, II, III (totales)
  - CALE-T 24q, 16q
  - Cantidades por tipo (17 n_1, 16 n_2**, 4 n_2, 3 n_1+, 16 n_3)
- **Acción**: Consolidar valores ya presentes en `scripts/compose_from_plan_v41.py` + validar contra doc

### Paso 4: Extraer referencia USCO (Word local)
- Path: `C:\raziel\aktriel\01__min_transporte\02__uscocalemania\draft_3\uscocalemania__v4.docx`
- Buscar valores por configuración (24q, 16q) o globales
- **Acción**: Usar `python-docx` o MCP markdown converter para extraer texto y parsear valores COP

### Paso 5: Consolidar fichas técnicas
- Fuente: `TABLAS_L3_CALE_TEORICO.json` + fichas HTML publicadas
- Extraer `valor_total_capex` por configuración (ya excluye OPEX si flags activos)
- **Acción**: Reutilizar lógica de `scripts/compose_from_plan_v41.py` y agregar a tabla maestra

### Paso 6: Generar tabla de reconciliación CSV
- Combinar todas las fuentes en un CSV con columnas definidas
- Implementar lógica de análisis:
  - Comparar `vr_ficha` vs `vr_anexoB` (deben ser iguales)
  - Explicar delta `vr_plan.41 - vr_ficha` (satélites, sala_form, etc.)
  - Marcar discrepancias con `ref_usco` (vehículos, alcance)
- Generar columnas `comentario_analisis` y `recomendacion` automáticamente
- **Salida**: `.opex_final_anexoA/output/tabla_reconciliacion_master.csv`

### Paso 7: Generar reporte ejecutivo
- Documento Markdown con:
  - Resumen de coherencia por configuración
  - Lista de inconsistencias detectadas
  - Recomendaciones priorizadas
  - Referencias cruzadas a Resolución de pertinencia
- **Salida**: `.opex_final_anexoA/output/REPORTE_COHERENCIA_ANEXOS.md`

## Referencias Normativas

- **Resolución de Pertinencia**: https://drive.google.com/file/d/1ShD6cUQIc07M7ye9JrsKvPVo6jmYBPiS/view?usp=drive_link
  - Validar alcance de vehículos por fase
  - Confirmar requisitos mínimos por configuración CALE
  - Contrastar con USCO para ajustar expectativas

## Criterios de Éxito

1. ✅ `vr_ficha == vr_anexoB` en todas las configuraciones
2. ✅ OPEX (TTHH + plataformas) documentado mensualmente en Anexo A
3. ✅ Deltas entre Plan.41 y fichas explicados con detalle técnico
4. ✅ Referencia USCO contextualizada (benchmark externo, no norma)
5. ✅ Tabla maestra CSV generada y validada
6. ✅ Reporte ejecutivo con recomendaciones accionables

---

**Fecha**: 2025-11-04  
**Versión**: 1.0  
**Responsable**: Copilot + Usuario (validación manual)  
**Próxima revisión**: Después de extraer datos de Google Docs y Word USCO
