# ANEXO A - RESUMEN MODELO FINANCIERO OPEX (versión resumida)

Fecha: 2025-11-04
Fuente: Consolidación L5 (`TABLAS_L5_RESUMEN_NACIONAL.json`) y Anexo A (documento detallado).

## Objetivo
Resumir y reorganizar el modelo OPEX nacional usando los valores reales consolidados en L5, asegurando que la inversión del proyecto se gestione como OPEX (estrategia llave en mano / leasing / financiación) y produciendo un escenario prudente de ingresos y recuperación en 5-6 años.

---

## 1. Valores L5 (fuente)
- CAPEX total (L5 consolidado): COP 206.704.800.000
- OPEX anual total (L5 consolidado): COP 135.500.000.000
- Capacidad anual total (evaluaciones): 2.565.072 evaluaciones/año
- Total nodos: 197

> Nota: L5 es la fuente "real" solicitada; en `TABLAS_L5_RESUMEN_NACIONAL.json` se consignan los valores por grupo y el consolidado nacional.

---

## 2. Principio de diseño solicitado
- Toda la inversión debe gestionarse como OPEX. Para ello proponemos:
  1. Infraestructura: contratación llave en mano con esquema de financiación o arrendamiento operativo (operating lease) y/o pago fraccionado (anualidades) que convierta CAPEX en gasto operativo anual.
  2. Equipamiento TIC: contratar como PaaS/SaaS/managed services (suscripción), trasladando coste a OPEX periódico.
  3. Vehículos: operar en modalidad leasing o contratos llave en mano con operador (lease + maintenance) y registrar como gasto operativo.
  4. Equipamiento específico (simuladores, equipamiento pruebas) podrá financiarse en contratos de suministro + mantenimiento (OPEX).

Suposiciones (a falta de una tasa/condición exacta del contrato — proponemos valores prudentes y ajustables):
- Tasa de financiamiento anual nominal para anualizar CAPEX (turnkey): 8.0% (puede ajustarse a 6-10% según mercado).
- Plazo de anualización propuesto: 5 años (alternativa: 6 años). Esto define la anualidad que convierte CAPEX en cargo OPEX anual.

---

## 3. Conversión CAPEX → OPEX (anualización)
Fórmula de anualidad (anualización financiera):

A = CAPEX * (r*(1+r)^n) / ((1+r)^n - 1)

Cálculos (supuestos r=8%):
- CAPEX total: 206.704.800.000 COP
- Anualidad (n = 5 años, r = 8%): factor ≈ 0.250488 → Pago anual ≈ COP 51.783.046.000
- Anualidad (n = 6 años, r = 8%): factor ≈ 0.216336 → Pago anual ≈ COP 44.754.000.000

### OPEX ajustado (CAPEX tratado como OPEX)
- OPEX operativo base (L5): 135.500.000.000 COP/año
- OPEX + anualidad(5a): 135.500.000.000 + 51.783.046.000 = **187.283.046.000 COP/año**
- OPEX + anualidad(6a): 135.500.000.000 + 44.754.000.000 = **180.254.000.000 COP/año**

> Comentario: usando la anualidad a 5 años el OPEX consolidado queda muy cercano al documento original de Anexo A (~188B), lo que confirma coherencia entre L5 y la propuesta de gestionar la inversión como gasto operativo.

---

## 4. Escenario prudente de ingresos (tarifas y utilización)
Requisitos del encargo:
- No superar tarifas máximas de la resolución.
- Escenario prudente.

Supuestos prudentes (pueden ajustarse si aportas la resolución o tarifas locales):
- Tarifa promedio prudente aplicada: COP 180.000 por evaluación completa (inferior a la tarifa promedio reportada en Anexo A).
- Utilización nacional prudente: 65% de la capacidad L5 (valor conservador y operativo).

Cálculos:
- Evaluaciones anuales (65%): 2.565.072 * 0.65 = 1.667.297 evaluaciones/año
- Ingresos anuales (tarifa 180.000): 1.667.297 * 180.000 = **COP 300.113.460.000**

Resultados financieros básicos (caso anualidad 5 años):
- OPEX ajustado (5a): 187.283.046.000
- Ingresos (prudente): 300.113.460.000
- Margen operativo anual: **COP 112.830.414.000**
- OPEX por evaluación (ajustado): 187.283.046.000 / 1.667.297 ≈ **COP 112.300 / eval.**
- Ingreso por evaluación: COP 180.000 → margen por evaluación ≈ COP 67.700

Escenario con tarifa "base" del Anexo A (200.333) y 65% utiliz.:
- Ingresos ≈ 1.667.297 * 200.333 ≈ **COP 334.3B**
- Margen ≈ **~COP 147B/año**

---

## 5. Recuperación y horizonte 5-6 años
- Si la intención es que la inversión total (CAPEX) sea recuperada en 5 años, la anualidad a 5 años (COP ~51.78B/año) ya incorpora capital + costo financiero; con el margen proyectado (COP 112.8B), la estructura es holgadamente sostenible.
- A 6 años la anualidad baja a COP ~44.75B/año y mejora aún más la cobertura.

Interpretación práctica:
- La estrategia llave en mano + financiación a 5 años produce un cargo fijo anual (anualidad) que **se equipa** dentro del OPEX consolidado y es cubierta ampliamente por ingresos aun en escenario prudente (65% utilización y tarifa 180k).
- Por tanto, es viable gestionar la inversión como OPEX y planear una recuperación financiera a 5 años manteniendo márgenes coherentes.

---

## 6. Tratamiento contable/operativo recomendado
1. Infraestructura: contratar via contrato llave en mano con pago fraccionado (arrendamiento operativo o contrato de FFOO vendor-finance). Registrar pago anual como gasto operativo; incluir cláusulas de mantenimiento SLA.
2. TIC: migrar a PaaS/SaaS con tarifas por usuario/instancia; priorizar modelos con costos por uso para alinear con actividad y evitar CAPEX dedicado.
3. Vehículos: operar mediante leasing operativo; contratos incluir mantenimiento y seguros.
4. Herramientas críticas (simuladores): evaluar contrato de supply+maintenance donde el proveedor asume obsolescencia dentro del fee.
5. Contratos nacionales: negociar volúmenes (licencias, cloud) centralmente para reducir OPEX unitario.

---

## 7. Riesgos y controles (resumen)
- Riesgo demanda baja: mitigar con campañas, alianzas y oferta complementaria (cursos).
- Riesgo tasa financiación elevada: negociar plazos/garantías o ampliar a 6 años; cuantificar sensibilidad a tasa ±2%.
- Riesgo tarifa regulatoria: mantener tarifas dentro de la resolución; modelar escenarios -15% y -30% (el sistema sigue viable según Anexo A).

---

## 8. Entregables y siguientes pasos (lo que puedo ejecutar ahora)
1. Entregable inmediato: este resumen (`ANEXO_A_MODELO_FINANCIERO_OPEX_SUMMARY.md`) y un JSON con los cálculos clave (anualidades, OPEX ajustado, ingresos, márgenes).
2. Siguientes pasos opcionales a ejecutar:
   - Generar una hoja Excel con escenarios (tarifas 3 niveles, utilzaciones 50/65/80%), sensibilidad a tasa (6/8/10%) y plazos (5/6 años).
   - Integrar modelo en `MODELO_FINANCIERO_OPEX_SNCALE.xlsx` si quieres que quede como versión oficial.
   - Ajustar parámetros con la tasa de interés y tarifas exactas de la resolución si me las proporcionas.

---

### Resumen ejecutivo (2 líneas)
Tratando CAPEX como OPEX mediante anualización a 5 años (8% nominal), el OPEX ajustado nacional queda en ~COP 187.3B/año; con una tarifa prudente de COP 180.000 y 65% de utilización, los ingresos estimados (~COP 300.1B) permiten cubrir el OPEX y generar un margen anual de ~COP 112.8B, haciendo coherente un horizonte de recuperación de 5 años.


---

*Archivo generado automáticamente — puedo ajustar supuestos (tasa, plazo, tarifa, %utilización) y generar la hoja Excel y CSV/JSON de detalle a pedido.*
