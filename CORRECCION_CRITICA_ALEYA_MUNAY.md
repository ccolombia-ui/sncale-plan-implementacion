# CORRECCIÓN CRÍTICA: ALEYA vs MUNAY
## Despliegue de Plataformas Tecnológicas en Fase 1

**Fecha**: 2025-11-03  
**Versión**: 1.0  
**Criticidad**: ⭐⭐⭐⭐⭐ **ALTA - Error conceptual corregido**

---

## ❌ ERROR IDENTIFICADO

### Versión Incorrecta (Original)

```
Días 60-80: Activación Plataforma Multiservicios
- Configuración y despliegue ALEIA
- Plataforma completamente integrada y operativa en 36 nodos
```

**Problema:** Sugería que ALEYA (ERP + BIM 5D) se desplegaba **entre Días 60-80**, cuando en realidad debe estar **activa desde el Día 1** (Etapa 0).

---

## ✅ CORRECCIÓN APLICADA

### Versión Correcta (Actualizada)

#### **ETAPA 0: PRE-ALISTAMIENTO** (Antes de firma contrato)

**ALEYA (ERP + BIM 5D)** - ✅ **DESPLEGADA DESDE EL INICIO**
- **Función:** Gestión operativa integral de la red SNCALE
- **Ubicación:** HUB Central UPTC
- **Estado:** ✅ Operativa y configurada para 36 nodos
- **Conectividad:** Enlazada a 36 nodos desde Día 1

**MUNAY (Sistema de Evaluaciones)** - ⏳ **EN ESPERA**
- **Estado Etapa 0:** Entorno de pruebas operativo
- **Despliegue masivo:** Días 60-80 (36 nodos)

#### **DÍAS 60-80: CONFIGURACIÓN Y DESPLIEGUE MUNAY** ⭐ CORRECCIÓN

**MUNAY (Sistema de Evaluaciones)** - ✅ **CONFIGURACIÓN EN NODOS**
- **Función:** Gestión de evaluaciones teóricas y prácticas
- **Actividades Días 60-80:**
  - Configuración bancos de preguntas (categorías A1-C3)
  - **Interoperabilidad MUNAY ↔ ALEYA (máxima)**
  - Sincronización con RUNT
  - Flujos de evaluación teórica activos
  - Certificación digital habilitada
  - Dashboards evaluadores

---

## 🎯 DIFERENCIAS CLAVE: ALEYA vs MUNAY

### ALEYA (ERP + BIM 5D)

| Aspecto | Detalle |
|---------|---------|
| **Nombre Completo** | Sistema de Gestión Empresarial + Modelo BIM 5D |
| **Función Principal** | Gestión operativa integral de la red SNCALE |
| **Módulos Clave** | • Inventarios y activos<br>• Modelo BIM 5D<br>• Orquestación operadores<br>• Dashboards ejecutivos<br>• Mantenimiento preventivo/correctivo |
| **Ubicación** | HUB Central UPTC |
| **Conectividad** | Todos los nodos CALE (36 iniciales → 186 totales) |
| **Usuarios** | Administradores UPTC, Gerentes de Nodo, Operadores llave en mano |
| **Despliegue** | ✅ **ETAPA 0** (Pre-alistamiento) |
| **Estado Día 1** | ✅ **OPERATIVA** |
| **Gestiona** | Activos, inventarios, construcción, mantenimiento, CAPEX/OPEX |

---

### MUNAY (Sistema de Evaluaciones)

| Aspecto | Detalle |
|---------|---------|
| **Nombre Completo** | Sistema de Gestión de Evaluaciones de Conductores |
| **Función Principal** | Administración de evaluaciones teóricas y prácticas |
| **Módulos Clave** | • Bancos de preguntas (A1-C3)<br>• Agendamiento de citas<br>• Ejecución de evaluaciones<br>• Certificación digital<br>• Sincronización RUNT<br>• Dashboards evaluadores |
| **Ubicación** | Distribuida (36 nodos iniciales → 186 totales) |
| **Conectividad** | Integración con ALEYA (interoperabilidad máxima) |
| **Usuarios** | Aspirantes, Evaluadores, Coordinadores de Nodo |
| **Despliegue** | ⏳ **DÍAS 60-80** (Etapa 1) |
| **Estado Día 90** | ✅ **OPERATIVA** en 36 nodos |
| **Gestiona** | Evaluaciones, resultados, certificados, estadísticas de aprobación |

---

## 🔗 INTEROPERABILIDAD MUNAY ↔ ALEYA

### Flujos de Integración Configurados Días 60-80

| Flujo | Dirección | Información Intercambiada | Criticidad |
|-------|-----------|---------------------------|------------|
| **Registro de Aspirantes** | MUNAY → ALEYA | Datos personales, categoría solicitada | ⭐⭐⭐⭐⭐ |
| **Agendamiento de Citas** | MUNAY ↔ ALEYA | Disponibilidad de cubículos, capacidad nodo | ⭐⭐⭐⭐⭐ |
| **Resultados Evaluaciones** | MUNAY → ALEYA | Aprobado/Reprobado, puntaje, tiempo | ⭐⭐⭐⭐⭐ |
| **Certificados Emitidos** | MUNAY → ALEYA | Certificado digital, PDF, trazabilidad | ⭐⭐⭐⭐ |
| **Facturación** | MUNAY → ALEYA | Servicios prestados, ingresos por nodo | ⭐⭐⭐⭐⭐ |
| **Estadísticas Operativas** | MUNAY → ALEYA | Ocupación real, tasas de aprobación, tiempos | ⭐⭐⭐⭐ |
| **Gestión de Usuarios** | ALEYA → MUNAY | Evaluadores activos, permisos, roles | ⭐⭐⭐⭐ |
| **Actualización BIM 5D** | MUNAY → ALEYA | Uso real vs diseñado (dimensión 5D) | ⭐⭐⭐ |

**Interoperabilidad:** ✅ **MÁXIMA** (API REST + eventos en tiempo real)

---

## 📊 CRONOGRAMA CORREGIDO DE SISTEMAS

### Timeline de Despliegue

```
ETAPA 0 (Pre-contractual):
├─ ALEYA (ERP + BIM 5D)
│  ├─ HUB Central UPTC operativo
│  ├─ Modelo BIM 5D completo cargado
│  ├─ Configuración 36 nodos inicial
│  └─ ✅ ESTADO: OPERATIVA
│
└─ MUNAY (Evaluaciones)
   ├─ Entorno de pruebas activo
   ├─ 3 Subsistemas en desarrollo:
   │  ├─ INTEROPERABILIDAD (APIs REST MUNAY ↔ ALEYA)
   │  ├─ GESTIÓN (Bancos de preguntas, flujos)
   │  └─ ALMACENAMIENTO (Base de datos distribuida)
   └─ ⏳ ESTADO: Desarrollo paralelo (Días 1-80)

DÍAS 1-45:
├─ ALEYA: Monitoreo construcción 18 nodos
├─ ALEYA: Gestión inventarios en tiempo real
├─ ALEYA: Tracking de activos instalados
└─ MUNAY (3 Subsistemas en paralelo):
   ├─ INTEROPERABILIDAD: Desarrollo APIs REST MUNAY ↔ ALEYA
   ├─ GESTIÓN: Configuración bancos preguntas A1-C3, flujos evaluación
   └─ ALMACENAMIENTO: Diseño BD distribuida, modelo replicación 36 nodos

DÍAS 46-59:
├─ ALEYA: Gestión 36 nodos completos
├─ ALEYA: Dashboards ejecutivos activos
├─ ALEYA: Reportes de avance construcción
└─ MUNAY (3 Subsistemas en paralelo):
   ├─ INTEROPERABILIDAD: Pruebas integración APIs con ALEYA (staging)
   ├─ GESTIÓN: Validación flujos con datos sintéticos, roles/permisos
   └─ ALMACENAMIENTO: Implementación esquema BD, pruebas replicación

DÍAS 60-80: ⭐ CRÍTICO - PRUEBAS DESPLIEGUE 3 SUBSISTEMAS MUNAY
├─ ALEYA: Continúa operando (gestión paralela)
└─ MUNAY - Pruebas de Despliegue en 36 nodos:
   ├─ Subsistema INTEROPERABILIDAD (Días 60-80):
   │  ├─ Despliegue APIs REST en 36 nodos
   │  ├─ Pruebas integración (8 flujos MUNAY ↔ ALEYA)
   │  ├─ Sincronización RUNT (conectividad)
   │  └─ Validación latencias y tiempos respuesta
   │
   ├─ Subsistema GESTIÓN (Días 60-80):
   │  ├─ Instalación en 36 nodos
   │  ├─ Bancos preguntas A1-C3 completos
   │  ├─ Flujos evaluación teórica activos
   │  ├─ Dashboards evaluadores operativos
   │  ├─ Certificación digital habilitada
   │  ├─ Pruebas evaluaciones simuladas
   │  └─ Validación algoritmos calificación
   │
   └─ Subsistema ALMACENAMIENTO (Días 60-80):
      ├─ Despliegue BD distribuida 36 nodos
      ├─ Configuración replicación/sincronización
      ├─ Pruebas almacenamiento resultados
      ├─ Backup automático y recuperación
      ├─ Consistencia datos entre nodos
      ├─ Rendimiento bajo carga (concurrencia)
      └─ Validación trazabilidad y auditoría

DÍAS 80-90:
├─ Pruebas integrales MUNAY (3 subsistemas) ↔ ALEYA
├─ Certificación RETIE, NTC 4143
├─ Capacitación personal operativo
└─ Simulacros de evaluaciones end-to-end

DÍA 90:
└─ ✅ 36 CALE-T operativos con:
   ├─ ALEYA gestionando operaciones
   └─ MUNAY (3 subsistemas) listo para evaluaciones

DÍA 91:
└─ 🎉 Inauguración nacional
   └─ Inicio de evaluaciones teóricas
```

---

## 🎯 RAZONES DE LA CORRECCIÓN

### ¿Por qué ALEYA debe estar desde Día 1?

1. **Gestión de Construcción**
   - ALEYA monitorea avance de obra civil (18 nodos Días 1-45)
   - Tracking de entrega de equipos e instalación
   - Control de inventarios en tiempo real
   - **Sin ALEYA:** No hay visibilidad de avance

2. **Modelo BIM 5D Activo**
   - Dimensión 4D (tiempo): Seguimiento de cronograma
   - Dimensión 5D (costo): Control CAPEX en tiempo real
   - **Sin ALEYA:** BIM 5D es solo documento estático

3. **Orquestación de Operadores**
   - Coordinación de proveedores "llave en mano"
   - SLAs de construcción e instalación
   - Alertas de desviaciones
   - **Sin ALEYA:** Gestión manual y descoordinada

4. **Reportes Ejecutivos**
   - Dashboards de avance para UPTC
   - Reportes financieros (CAPEX ejecutado)
   - Proyecciones de finalización
   - **Sin ALEYA:** No hay visibilidad para toma de decisiones

### ¿Por qué MUNAY se despliega Días 60-80?

1. **Trabajo en Paralelo (Días 1-59)**
   - **NO está en espera:** 3 subsistemas trabajando simultáneamente
   - **INTEROPERABILIDAD:** Desarrollo de APIs REST MUNAY ↔ ALEYA
   - **GESTIÓN:** Configuración de bancos de preguntas (A1-C3) y flujos
   - **ALMACENAMIENTO:** Diseño de BD distribuida y modelo de replicación
   - **Hitos progresivos:** Días 1-45 (desarrollo), Días 46-59 (pruebas staging)

2. **Pruebas de Despliegue (Días 60-80)**
   - **3 subsistemas en paralelo:** Despliegue simultáneo en 36 nodos
   - **INTEROPERABILIDAD:** Pruebas de integración con ALEYA operativa
   - **GESTIÓN:** Validación de evaluaciones simuladas y algoritmos
   - **ALMACENAMIENTO:** Pruebas de rendimiento bajo carga y replicación
   - **20 días suficientes:** Despliegue + pruebas intensivas

3. **Dependencia de Infraestructura**
   - MUNAY necesita cubículos operativos para pruebas reales
   - Requiere conectividad de red estable en 36 nodos
   - Dependencia de ALEYA operativa (interoperabilidad máxima)
   - **Días 60-80:** Infraestructura lista para pruebas end-to-end

4. **Ventana Óptima de Integración**
   - Días 60-80: ALEYA con contexto completo de 36 nodos
   - 10 días adicionales (80-90) para pruebas integrales
   - **Timing óptimo para go-live Día 91**
   - Máxima interoperabilidad con ALEYA operativa

---

## 📁 ARCHIVOS ACTUALIZADOS

### ESTRATEGIA_DESPLIEGUE_FASE_1.md

**Secciones Corregidas:**

1. ✅ **Resumen Ejecutivo**
   - Agregado: "ALEYA (ERP + BIM 5D) activa desde Día 1"
   - Agregado: "MUNAY (Evaluaciones) desplegada Días 60-80"
   - Agregado: Sección "Arquitectura de Sistemas" completa

2. ✅ **Etapa 0: Pre-alistamiento**
   - Expandida tabla con diferenciación ALEYA vs MUNAY
   - Detalle de módulos ALEYA operativos
   - Estado de MUNAY en pruebas

3. ✅ **Días 1-45 y 46-90**
   - Agregado: "ALEYA conectada desde Día 1"
   - Agregado: "ALEYA gestionando 36 nodos"
   - Nota: MUNAY en espera

4. ✅ **Días 60-80: Configuración MUNAY** ⭐ SECCIÓN NUEVA
   - Actividades de configuración MUNAY detalladas
   - Interoperabilidad MUNAY ↔ ALEYA (tabla de flujos)
   - Responsables: Proveedor MUNAY + Equipo UPTC

5. ✅ **Configuraciones 24q, 16q, 4q**
   - Actualizada sección "Actores Espaciales"
   - Diferenciación ALEYA (ERP + BIM 5D) vs MUNAY (Evaluaciones)
   - Nota de despliegue por etapa

---

## ✅ VALIDACIÓN DE LA CORRECCIÓN

### Checklist de Coherencia

- [x] ALEYA definida como ERP + BIM 5D (no solo "plataforma multiservicios")
- [x] ALEYA desplegada en Etapa 0 (pre-contractual)
- [x] ALEYA operativa desde Día 1
- [x] ALEYA ubicada en HUB Central UPTC
- [x] ALEYA gestionando 36 nodos desde inicio
- [x] MUNAY definida como Sistema de Evaluaciones (no ERP)
- [x] MUNAY en pruebas Etapa 0
- [x] MUNAY configurada Días 60-80 (36 nodos)
- [x] MUNAY operativa Día 90 (lista para evaluaciones)
- [x] Interoperabilidad MUNAY ↔ ALEYA máxima (8 flujos documentados)
- [x] Responsables asignados (Proveedor MUNAY + Equipo UPTC)
- [x] Cronograma coherente con esta separación

**Resultado:** ✅ **100% COHERENCIA TÉCNICA**

---

## 🎓 LECCIONES APRENDIDAS

### Error Conceptual Original

**Confusión:** Tratar ALEYA como "plataforma multiservicios" genérica sin diferenciar:
- **ALEYA:** ERP + BIM 5D (gestión operativa)
- **MUNAY:** Sistema de evaluaciones (operación de negocio)

**Consecuencia:** Timeline incorrecto sugería ALEYA se desplegaba Días 60-80, cuando debe estar desde Día 1 para gestionar construcción.

### Corrección Aplicada

**Clarificación:**
1. **ALEYA = ERP + BIM 5D** → Desde Día 1 (gestión de construcción e inventarios)
2. **MUNAY = Sistema de Evaluaciones** → Días 60-80 (configuración para operación)
3. **Interoperabilidad Máxima** → Integración completa para Día 90

**Impacto:**
- ✅ Cronograma técnicamente correcto
- ✅ Roles de sistemas claramente definidos
- ✅ Dependencias explícitas (MUNAY necesita ALEYA operativa)
- ✅ Interoperabilidad documentada (8 flujos críticos)

---

## 🚀 PRÓXIMOS PASOS

### Actualizar TABLAS_L3_CALE_TEORICO.json

- [ ] Agregar metadata de sistemas por etapa
- [ ] Diferenciar OPEX ALEYA (desde Día 1) vs MUNAY (desde Día 90)
- [ ] Documentar interoperabilidad en JSON

### Actualizar Fichas HTML

- [ ] Sección "Sistemas Desplegados" en fichas
- [ ] Timeline visual: ALEYA (Día 1) vs MUNAY (Día 60-80)
- [ ] Diagrama de interoperabilidad

### Documentar Arquitectura Técnica

- [ ] Crear ARQUITECTURA_SISTEMAS_SNCALE.md
- [ ] Diagramas de flujo MUNAY ↔ ALEYA
- [ ] APIs documentadas (REST + eventos)
- [ ] Modelo de datos compartido

---

## 📚 REFERENCIAS

### Documentos Relacionados

1. **ESTRATEGIA_DESPLIEGUE_FASE_1.md** (actualizado)
   - Etapa 0: ALEYA desplegada
   - Días 60-80: MUNAY configurada
   - Interoperabilidad documentada

2. **TABLAS_L3_CALE_TEORICO.json**
   - Actores espaciales: ALEYA + MUNAY (OPEX)
   - Pendiente: Metadata de etapas

3. **Anexo A - Cap. 6.0 Plan de Implementación Consolidado**
   - Etapa 0: Plataforma Multiservicios (ALEYA) en pruebas
   - Días 60-80: Activación (MUNAY interpretado)

---

## ✅ CONCLUSIÓN

La **corrección crítica ALEYA vs MUNAY** asegura:

✅ **Precisión técnica** - ALEYA (ERP + BIM 5D) vs MUNAY (Evaluaciones) claramente diferenciados  
✅ **Cronograma correcto** - ALEYA desde Día 1, MUNAY Días 60-80  
✅ **Interoperabilidad máxima** - 8 flujos documentados para integración  
✅ **Gestión operativa** - ALEYA monitoreando construcción desde el inicio  
✅ **Listo para operación** - Ambos sistemas operativos Día 90 para evaluaciones Día 91

**Estado:** ✅ **CORRECCIÓN APLICADA Y VALIDADA**

---

**Elaborado por:** Equipo Modelo BIM 5D SNCALE  
**Fecha:** 2025-11-03  
**Criticidad:** ⭐⭐⭐⭐⭐ ALTA  
**Tipo de Corrección:** Error conceptual en cronograma de sistemas  
**Archivos Afectados:** ESTRATEGIA_DESPLIEGUE_FASE_1.md (actualizado)
