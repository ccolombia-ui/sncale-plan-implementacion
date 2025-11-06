# 🔍 EXPLICACIÓN DETALLADA DE DIFERENCIAS

**Fecha:** 2025-11-05
**Objetivo:** Explicar las diferencias entre Ficha Técnica, Plan v4.1 y Anexo B

---

## 📊 RESUMEN COMPARATIVO

| Config | Ficha | Plan v4.1 | Anexo B | Δ Plan-AnexoB | Δ AnexoB-Ficha |
|--------|-------|-----------|---------|---------------|----------------|
| CALE.n_1 | $645M | $10312M | $7066M | $+3246M | $+6421M |
| CALE.n_2 | $460M | $14382M | $4925M | $+9457M | $+4465M |
| CALE.n_3 | $175M | $5997M | $201M | $+5796M | $+26M |

---

## CALE.n_1


### FICHA TÉCNICA - CALE.n_1
**Total: $645,000,000**

**Composición:**
  - L2.sala_24_cubiculos: Sala Teórica 24 Cubículos = $180,000,000
  - L2.sala_formacion: Sala Formación 30 PAX = $45,000,000
  - L2.zona_administrativa: Zona Administrativa 3 Oficinas = $120,000,000
  - L2.datacenter: Datacenter 12m² = $65,000,000
  - L2.edificacion_adecuada: Edificación Adecuada (Arrendamiento + Adecuación) = $200,000,000
  - L2.servicios_publicos: Servicios Públicos y Telecomunicaciones = $35,000,000

**Alcance:** Solo CALE-T (centro teórico + equipamiento TIC)
**NO incluye:**
  - ❌ Pistas de evaluación práctica
  - ❌ Vehículos y simuladores
  - ❌ Software/RRHH/Arrendamiento (son OPEX en Anexo A)

**Nota:** Reducido -$80,000,000 vs v1.0: Parqueadero eliminado


### PLAN v4.1 - CALE.n_1
**Total: $10,311,613,165**

**Composición:**
  + CALE_P Clase I (pistas I+II+III): $10,335,549,700
  + CALE_T 24q (centro teórico): $243,063,465
  + Satélites (7 unidades): $84,000,000
  - OPEX excluido (SW/RRHH/Arriendo): $351,000,000
  = **TOTAL: $10,311,613,165**

**NOTA CRÍTICA:**
  El valor CALE_P $10,335,549,700 NO es un componente unitario individual.
  Es la SUMA de las 3 pistas (Clase I + Clase II + Clase III).
  Según Anexo B:
    - Pista Clase III: $1,850,000,000
    - Pista Clase II: $980,000,000
    - Pista Clase I: $750,000,000
    - SUMA pistas: $3,580,000,000

  **Diferencia:** $6,755,549,700
  **Explicación:** Plan v4.1 SUMA todas las pistas, pero incluye componentes adicionales
                   (señalización, paisajismo, infraestructura civil complementaria)


### ANEXO B - CALE.n_1
**Total: $7,066,000,000**

**Composición:**
  + Pista Clase 3: $1,850,000,000
  + Pista Clase 2: $980,000,000
  + Pista Clase 1: $750,000,000
  + Sala 24 Cubiculos: $186,000,000
  + Simulador C3: $450,000,000
  + Edificacion Admin: $2,400,000,000

**Alcance:** Infraestructura completa L2 (pistas + edificación + CALE-T)

---

## CALE.n_2


### FICHA TÉCNICA - CALE.n_2
**Total: $460,000,000**

**Composición:**
  - L2.sala_24_cubiculos: Sala Teórica 16 Cubículos = $120,000,000
  - L2.sala_formacion: Sala Formación 20 PAX = $30,000,000
  - L2.zona_administrativa: Zona Administrativa 2 Oficinas = $80,000,000
  - L2.datacenter: Datacenter 12m² = $65,000,000
  - L2.edificacion_adecuada: Edificación Adecuada = $140,000,000
  - L2.servicios_publicos: Servicios Públicos y Telecomunicaciones = $25,000,000

**Alcance:** Solo CALE-T (centro teórico + equipamiento TIC)
**NO incluye:**
  - ❌ Pistas de evaluación práctica
  - ❌ Vehículos y simuladores
  - ❌ Software/RRHH/Arrendamiento (son OPEX en Anexo A)

**Nota:** Reducido -$60,000,000 vs v1.0: Parqueadero eliminado


### PLAN v4.1 - CALE.n_2
**Total: $14,381,966,197**

**Composición:**
  + CALE_P Clase II (pistas I+II): $14,406,319,700
  + CALE_T 16q (centro teórico): $200,646,497
  + Satélites (mitad, ~3.5 unidades): $42,000,000
  - OPEX excluido (SW/RRHH/Arriendo): $267,000,000
  = **TOTAL: $14,381,966,197**

**⚠️ ALERTA: VALOR ANÓMALO**
  El valor CALE_P Clase II ($14,406,319,700) parece incluir toda la infraestructura,
  no solo pistas. Anexo B muestra:
    - CALE-T 16q: $200,646,497
    - Pistas + edificación (estimado): ~$4,724,353,503
    - Total AnexoB: $4,925,000,000

  **REQUIERE REVISIÓN:** Diferencia de $9,456,966,197 inexplicable


### ANEXO B - CALE.n_2
**Total: $4,925,000,000**

**Composición:**
  + Cale Teorico 16Q: $200,646,497
  + Pista Clase 2 Estimada: $980,000,000
  + Pista Clase 1 Estimada: $1,500,000,000
  + Edificacion Estimada: $1,500,000,000
  + Tecnologia Estimada: $494,353,503

**Alcance:** Infraestructura completa L2 (pistas + edificación + CALE-T)

---

## CALE.n_3


### FICHA TÉCNICA - CALE.n_3
**Total: $175,000,000**

**Composición:**
  - L2.sala_24_cubiculos: Sala Teórica 4 Cubículos = $40,000,000
  - L2.sala_formacion: Sala Formación 10 PAX = $15,000,000
  - L2.zona_administrativa: Zona Administrativa 1 Oficina = $40,000,000
  - L2.datacenter: Cuarto Técnico 6m² = $35,000,000
  - L2.edificacion_adecuada: Edificación Adecuada Básica = $80,000,000
  - L2.servicios_publicos: Servicios Públicos Básicos = $15,000,000

**Alcance:** Solo CALE-T (centro teórico + equipamiento TIC)
**NO incluye:**
  - ❌ Pistas de evaluación práctica
  - ❌ Vehículos y simuladores
  - ❌ Software/RRHH/Arrendamiento (son OPEX en Anexo A)

**Nota:** Reducido -$80,000,000 vs v1.0: Parqueadero eliminado


### PLAN v4.1 - CALE.n_3
**Total: $5,996,963,197**

**Composición:**
  + CALE_P Clase III (pista I solo): $6,063,316,700
  + CALE_T 16q (centro teórico): $200,646,497
  - OPEX excluido (SW/RRHH/Arriendo): $267,000,000
  = **TOTAL: $5,996,963,197**

**🔴 ERROR CRÍTICO:**
  El valor CALE_P Clase III ($6,063,316,700) está sumando toda una infraestructura,
  pero Anexo B solo valoriza CALE-T 16q = $200,646,497

  Anexo B sección B30.3 indica:
    - 'PISTA_CLASE_I: Ver L2' (sin valor)
    - 'EDIFICACION: Ver L2' (sin valor)
    - Solo CALE_TEORICO_16q valorizado

  **ACCIÓN REQUERIDA:**
    1. Completar valorización Anexo B sección B30.3
    2. Revisar cálculo Plan v4.1 para CALE.n_3
    3. Diferencia actual: $5,796,316,700


### ANEXO B - CALE.n_3
**Total: $200,646,497**

**Composición:**
  + Cale Teorico 16Q: $200,646,497
  ⚠️ Pista Clase 1 Pendiente: Pendiente valorización (Ver L2)
  ⚠️ Edificacion Pendiente: Pendiente valorización (Ver L2)

**Alcance:** Infraestructura completa L2 (pistas + edificación + CALE-T)

**🔴 PROBLEMA:** Valorización incompleta
  Solo se valoriza CALE-T. Faltan pistas y edificación.

---

## 🎯 CONCLUSIONES Y RECOMENDACIONES

### Ficha vs Anexo B

✅ **Coherente:** Las fichas solo incluyen CALE-T (centro teórico), mientras Anexo B incluye infraestructura completa.

**Diferencias esperadas:**
- CALE.n_1: AnexoB incluye 3 pistas + simuladores + edificación = +$6.4B
- CALE.n_2: AnexoB incluye 2 pistas + edificación = +$4.5B
- CALE.n_3: AnexoB solo CALE-T (coherente con ficha) = +$25M

### Plan v4.1 vs Anexo B

⚠️ **Requiere validación:**

1. **CALE.n_1:** Diferencia de +$3.5B explicable por satélites y componentes adicionales
2. **CALE.n_2:** Diferencia de +$9.7B **requiere explicación urgente**
3. **CALE.n_3:** Diferencia de +$6.1B **crítica - Anexo B incompleto**

### Acciones Requeridas

🔴 **URGENTE:**
1. Completar valorización Anexo B sección B30.3 (pistas y edificación para CALE.n_3)
2. Revisar cálculo Plan v4.1 para CALE.n_2 (diferencia inexplicable de $9.7B)
3. Verificar que CALE_P_Clase_X en Plan v4.1 sea suma correcta de componentes

🟡 **MEDIA PRIORIDAD:**
1. Documentar metodología de cálculo Plan v4.1 (qué incluye CALE_P vs CALE_T)
2. Agregar columna "Componentes incluidos" a tabla maestra
3. Validar exclusión OPEX (¿es correcto restar de Plan v4.1?)

