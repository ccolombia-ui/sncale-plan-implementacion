# Metodología de Coherencia entre Anexos A, B y Fichas Técnicas

## Filosofía del Modelo: Todo como OPEX

El modelo SNCALE está diseñado para gestionar **toda la inversión como gasto operativo (OPEX)**, eliminando la barrera de entrada de grandes inversiones iniciales (CAPEX).

### Tres Pilares de la Inversión Inicial

1. **Infraestructura Física y Equipamiento Operativo/TIC** (Anexo B)
   - Manejo: Arrendamiento / Leasing
   - Fuente: Anexo B describe la suficiencia técnica
   - Fichas Técnicas (Anexo C): detallan especificaciones BIM 5D

2. **Plataformas Tecnológicas** (Anexo A)
   - Manejo: PaaS (Platform as a Service)
   - Componentes: Munay, Aleya, infraTIC, equipoTIC
   - Pago mensual por uso

3. **Talento Humano** (Anexo A)
   - Manejo: UPTC / Demanda CALE asegura costo
   - Contratación bajo demanda operativa
   - Escalable según necesidad

## Relación entre Documentos

### Anexo A - Modelo Financiero OPEX
- Documenta el presupuesto operativo mensual
- Última sección: cómo se opera el modelo
- Incluye:
  - Talento humano (TTHH) mensual por configuración
  - Plataformas tecnológicas (Munay, Aleya) mensuales
  - Proyección OPEX

### Anexo B - Inversión Infraestructura + Equipamiento
- Explica la inversión inicial de infraestructura
- Suficiencia técnica para operación
- **Valor unitario Anexo B = Valor unitario Ficha Técnica**
- No incluye: TTHH ni plataformas (esos van en Anexo A)

### Anexo C - Fichas Técnicas BIM 5D
- Detalle técnico para implementación BIM
- Modelo recursivo L0→L1→L2→L3→L4→L5
- Cada ficha describe:
  - Especificaciones técnicas
  - Valor unitario (coherente con Anexo B)
  - Componentes y subcomponentes
  - Normatividad aplicable

## Coherencia Requerida

Para cada configuración L3 (CALE.n_1, CALE.n_2, CALE.n_3, etc.):

```
L3.componente | vr_ficha | vr_plan.41 | vr_anexoB | ref_usco | vr_mes_tthh | anxA.vr_mes_munay | anxA.vr_mes_aleya | comentario_analisis | recomendacion
```

### Reglas de Coherencia

1. **vr_ficha ≈ vr_anexoB** (deben coincidir, representan infraestructura+equipamiento)
2. **vr_ficha NO incluye:**
   - Talento humano (va en vr_mes_tthh)
   - Plataformas tecnológicas (van en anxA.vr_mes_munay, anxA.vr_mes_aleya)
   - Arrendamiento (se maneja aparte como OPEX)

3. **vr_plan.41:** puede diferir si incluye elementos adicionales (vehículos, contingencias)
4. **ref_usco:** referencia externa para validación cruzada
5. **Discrepancias:** documentar en comentario_analisis con recomendación

## Fuentes de Verdad

1. **Anexo A (Google Doc):** https://docs.google.com/document/d/1n5PKZmVECilenC4joZ8k6HLGgh9CWFf8lVolBBHTSi4
2. **Anexo B (Google Doc):** https://docs.google.com/document/d/16_6wrNUMfenjXHPmFdq-krjN3yFoCB8HO_LUVX3WblE
3. **Plan v4.1 (Google Doc):** https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg
4. **Fichas Técnicas (GitHub Pages):** https://ccolombia-ui.github.io/sncale-plan-implementacion/
5. **USCO (Word local):** C:\raziel\aktriel\01__min_transporte\02__uscocalemania\draft_3\uscocalemania__v4.docx
6. **Resolución (PDF):** https://drive.google.com/file/d/1ShD6cUQIc07M7ye9JrsKvPVo6jmYBPiS/view

## Proceso de Reconciliación

### Paso 1: Extracción
- Leer directamente Google Docs (sin conversión) usando API
- Extraer valores por configuración L3
- Parsear documento USCO local
- Consolidar fichas técnicas del repo

### Paso 2: Consolidación
- Generar tabla maestra CSV con todas las fuentes
- Calcular deltas y discrepancias
- Identificar valores faltantes

### Paso 3: Análisis
- Documentar discrepancias
- Generar comentarios automáticos donde aplique
- Proponer recomendaciones

### Paso 4: Validación
- Revisar contra resolución de pertinencia
- Verificar coherencia interna
- Aprobar ajustes necesarios

## Ejemplo de Análisis

```csv
L3.componente,vr_ficha,vr_plan.41,vr_anexoB,ref_usco,vr_mes_tthh,anxA.vr_mes_munay,anxA.vr_mes_aleya,comentario_analisis,recomendacion
CALE.n_1,10311613165,10578613165,10311613165,10400000000,16500000,1500000,2000000,"vr_ficha y anxB coherentes (no incluyen tthh ni plataformas). plan.41 incluye sala_form. usco considera más vehículos","Validar diferencia plan.41 vs ficha (267M). Revisar vehículos en usco contra resolución"
```

## Notas Importantes

- **NO convertir Google Docs:** leer directamente usando API para mantener actualización
- **Valores en COP:** todos los montos en pesos colombianos
- **Mensual vs Anual:** clarificar en cada columna (tthh y plataformas son mensuales)
- **Exclusiones:** software, RRHH y arrendamiento NO van en fichas (van en Anexo A OPEX)
