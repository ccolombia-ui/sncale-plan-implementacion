# PLAN DE EXTRACCIÓN DE DATOS REALES - SISTEMA CALE UPTC
**Fecha**: Octubre 28, 2025  
**Estado**: PLANIFICACIÓN  
**Objetivo**: Extraer únicamente información verificable de los documentos oficiales

---

## 🎯 OBJETIVO GENERAL

Construir el sistema CALE UPTC basándose **exclusivamente** en información contenida en los tres documentos oficiales proporcionados, sin inventar, estimar o proyectar datos.

---

## 📋 FASE 1: ACCESO Y LECTURA DE DOCUMENTOS OFICIALES

### PASO 1.1: Verificar Acceso a Documentos
**Duración estimada**: 15 minutos  
**Responsable**: Usuario + Sistema

**Tareas**:
1. ✅ Verificar acceso a Plan General CALE UPTC
   - URL: https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg/edit?tab=t.0
   - Confirmar permisos de lectura
   - Identificar estructura del documento (capítulos, secciones)

2. ✅ Verificar acceso a Base de Datos Oficial
   - URL: https://docs.google.com/spreadsheets/d/10k6SjOScnCte9Awh4JNhpiQ-zBWLvAHflyIWsVqvMYU/edit?gid=241106151#gid=241106151
   - Confirmar permisos de lectura
   - Identificar pestañas disponibles
   - Listar columnas y estructura de datos

3. ✅ Verificar acceso a Carta de Solicitud
   - URL: https://docs.google.com/document/d/1O1NC0exeH3LjTJ92keo2Dqc7JT0nG76fOVvcP5nosgI/edit?pli=1&tab=t.3f90yibt0luf
   - Confirmar permisos de lectura
   - Identificar contenido principal

**Entregables**:
- [ ] Checklist de acceso a documentos
- [ ] Índice de contenidos de cada documento
- [ ] Lista de pestañas/secciones disponibles

**Criterios de Éxito**:
- ✅ Acceso confirmado a los 3 documentos
- ✅ Estructura documentada de cada fuente
- ✅ Sin errores de autenticación

---

### PASO 1.2: Extraer Índice y Estructura del Plan General
**Duración estimada**: 30 minutos  
**Prioridad**: ALTA

**Tareas**:
1. Leer tabla de contenidos del Plan General
2. Identificar secciones con información estructural:
   - Estructura organizacional de nodos CALE
   - Categorías de nodos (Cat.A, Cat.B, Cat.C)
   - Componentes técnicos (CALE-T, CALE-P)
   - Modelo de gobernanza
   - Fases de implementación

3. Documentar ubicación exacta de cada sección:
   - Número de página/sección
   - Títulos exactos
   - Subsecciones relevantes

**Entregables**:
- [ ] `INDICE_PLAN_GENERAL.md` con estructura completa
- [ ] Mapa de ubicación de información crítica
- [ ] Lista de secciones con datos cuantitativos

**Criterios de Éxito**:
- ✅ Índice completo del Plan General documentado
- ✅ Ubicación de secciones clave identificada
- ✅ Sin asumir contenido, solo documentar lo visible

---

### PASO 1.3: Extraer Estructura de Base de Datos
**Duración estimada**: 30 minutos  
**Prioridad**: ALTA

**Tareas**:
1. Listar todas las pestañas del Google Sheet
2. Para cada pestaña, documentar:
   - Nombre exacto
   - Columnas presentes
   - Tipo de datos (texto, número, fórmula)
   - Número aproximado de filas con datos

3. Identificar pestañas con:
   - Costos y presupuestos
   - Especificaciones técnicas
   - Listados de productos/componentes
   - Catálogos de equipamiento

**Entregables**:
- [ ] `ESTRUCTURA_BASE_DATOS.md` con todas las pestañas
- [ ] Diccionario de columnas por pestaña
- [ ] Identificación de datos maestros vs calculados

**Criterios de Éxito**:
- ✅ Todas las pestañas documentadas
- ✅ Estructura de datos clara
- ✅ Identificación de fuentes primarias de datos

---

## 📊 FASE 2: EXTRACCIÓN DE DATOS ESTRUCTURALES

### PASO 2.1: Extraer Categorías Reales de Nodos CALE
**Duración estimada**: 1 hora  
**Prioridad**: CRÍTICA

**Tareas**:
1. Buscar en Plan General:
   - Sección que define categorías de nodos
   - Nombres exactos de categorías (Cat.A, Cat.B, Cat.C2, etc.)
   - Descripción de cada categoría
   - Criterios de clasificación

2. Documentar para cada categoría:
   - Nombre oficial completo
   - Tipo de evaluación (teórica, práctica, ambas)
   - Función dentro del sistema (coordinador, satélite, etc.)
   - Componentes incluidos
   - Texto EXACTO del documento (citar)

3. Validar contra datos locales:
   - Verificar coincidencia con `LISTADO_141_MUNICIPIOS_SATELITE.csv`
   - Confirmar categorías C2, C3, C4, C5
   - Identificar categorías principales (Cat.A, Cat.B)

**Entregables**:
- [ ] `CATEGORIAS_CALE_OFICIAL.md` con definiciones exactas
- [ ] Tabla comparativa: Documento vs CSV local
- [ ] Citas textuales del Plan General

**Criterios de Éxito**:
- ✅ Categorías oficiales documentadas con citas
- ✅ Coherencia entre fuentes verificada
- ✅ Sin categorías inventadas o asumidas

**Reglas Estrictas**:
- 🚫 NO inventar nombres de categorías
- 🚫 NO asumir subcategorías no mencionadas
- ✅ SÍ citar texto exacto del documento
- ✅ SÍ marcar como "no encontrado" si aplica

---

### PASO 2.2: Extraer Componentes Técnicos CALE-T
**Duración estimada**: 1 hora  
**Prioridad**: ALTA

**Tareas**:
1. Localizar en Plan General:
   - Sección "Blueprint de Infraestructura Física Teórica"
   - Especificaciones CALE-T-24q
   - Especificaciones CALE-T-16q
   - Componentes principales

2. Extraer datos específicos:
   - Número de cubículos por tipo
   - Componentes de Etapa 1 (mínimo normativo)
   - Áreas y dimensiones
   - Equipamiento incluido

3. Buscar en Base de Datos:
   - Pestaña con especificaciones técnicas
   - Costos asociados a CALE-T
   - Listado de productos/componentes

**Entregables**:
- [ ] `ESPECIFICACIONES_CALE_T.md` con datos exactos
- [ ] Tabla de componentes con fuente
- [ ] Costos extraídos de Base de Datos (si existen)

**Criterios de Éxito**:
- ✅ Especificaciones técnicas documentadas
- ✅ Componentes listados con fuente
- ✅ Costos reales (no estimados) si están disponibles

**Reglas Estrictas**:
- 🚫 NO inventar dimensiones o áreas
- 🚫 NO estimar costos sin fuente
- ✅ SÍ copiar especificaciones textuales
- ✅ SÍ indicar "no especificado" si falta información

---

### PASO 2.3: Extraer Componentes Técnicos CALE-P
**Duración estimada**: 1 hora  
**Prioridad**: ALTA

**Tareas**:
1. Localizar en Plan General:
   - Sección "Especificación Técnica CALE-P"
   - Blueprints de infraestructura práctica
   - Clasificación (Clase I, Clase II, Clase III)

2. Extraer datos específicos:
   - Descripción de cada clase
   - Componentes incluidos (pistas, vehículos, etc.)
   - Áreas de terreno requeridas
   - Equipamiento específico

3. Buscar en Base de Datos:
   - Costos de construcción CALE-P
   - Especificaciones de vehículos
   - Equipamiento de pistas

**Entregables**:
- [ ] `ESPECIFICACIONES_CALE_P.md` con datos exactos
- [ ] Clasificación oficial documentada
- [ ] Costos y componentes verificados

**Criterios de Éxito**:
- ✅ Clases de CALE-P documentadas oficialmente
- ✅ Componentes listados con fuente
- ✅ Diferencias entre clases claras

**Reglas Estrictas**:
- 🚫 NO asumir clases no mencionadas
- 🚫 NO inventar especificaciones técnicas
- ✅ SÍ extraer texto literal del Plan General
- ✅ SÍ documentar limitaciones de información

---

## 💰 FASE 3: EXTRACCIÓN DE DATOS FINANCIEROS

### PASO 3.1: Extraer Presupuestos de Base de Datos
**Duración estimada**: 1.5 horas  
**Prioridad**: CRÍTICA

**Tareas**:
1. Identificar pestaña con presupuestos:
   - Buscar pestañas con "presupuesto", "costos", "CAPEX", "OPEX"
   - Verificar estructura de datos
   - Identificar moneda (COP, USD, millones, etc.)

2. Extraer datos por categoría:
   - Costos CALE-T por tipo (24q, 16q)
   - Costos CALE-P por clase (I, II, III)
   - Costos de equipamiento
   - Costos de plataforma MUNAY

3. Documentar totales:
   - CAPEX total (si está calculado)
   - OPEX anual (si está calculado)
   - Desglose por componente
   - Fuente de cada cifra

**Entregables**:
- [ ] `PRESUPUESTO_OFICIAL.md` con datos de Base de Datos
- [ ] Tabla de costos por componente con fuente
- [ ] Totales verificados (no calculados por nosotros)

**Criterios de Éxito**:
- ✅ Costos extraídos directamente de Base de Datos
- ✅ Fuente de cada cifra documentada
- ✅ Moneda y unidades claramente especificadas

**Reglas Estrictas**:
- 🚫 NO calcular totales si no están en la fuente
- 🚫 NO convertir monedas sin tasa oficial
- 🚫 NO proyectar costos futuros
- ✅ SÍ copiar cifras exactas de la hoja de cálculo
- ✅ SÍ documentar fórmulas si existen
- ✅ SÍ indicar "no disponible" si falta información

---

### PASO 3.2: Validar Coherencia Financiera
**Duración estimada**: 30 minutos  
**Prioridad**: MEDIA

**Tareas**:
1. Comparar costos entre fuentes:
   - Plan General menciona costos → verificar con Base de Datos
   - Carta de Solicitud menciona montos → verificar coherencia

2. Documentar discrepancias:
   - Si hay diferencias, NO asumir cuál es correcta
   - Documentar ambas versiones con fuente
   - Solicitar aclaración al usuario

3. Identificar brechas de información:
   - Costos mencionados pero no cuantificados
   - Componentes sin precio
   - Totales sin desglose

**Entregables**:
- [ ] `VALIDACION_FINANCIERA.md` con comparaciones
- [ ] Lista de discrepancias encontradas
- [ ] Consultas pendientes para el usuario

**Criterios de Éxito**:
- ✅ Comparación documentada entre fuentes
- ✅ Discrepancias identificadas sin resolverlas arbitrariamente
- ✅ Brechas de información listadas

---

## 🗺️ FASE 4: EXTRACCIÓN DE DATOS GEOGRÁFICOS

### PASO 4.1: Extraer Ubicaciones Reales de Nodos
**Duración estimada**: 1 hora  
**Prioridad**: ALTA

**Tareas**:
1. Buscar en Plan General:
   - Sección con distribución territorial
   - Listado de municipios sede de CALE
   - Criterios de selección de ubicaciones

2. Buscar en Base de Datos:
   - Pestaña con listado de nodos
   - Columnas con departamento, municipio
   - Coordenadas geográficas (si existen)

3. Validar con CSV local:
   - `LISTADO_141_MUNICIPIOS_SATELITE.csv` → 141 municipios confirmados
   - `cales_iebm_dane_mejor_opcion.csv` → ubicaciones principales
   - Verificar coincidencia de nombres

**Entregables**:
- [ ] `UBICACIONES_NODOS_CALE.md` con listado oficial
- [ ] Tabla: Departamento | Municipio | Categoría | Fuente
- [ ] Mapa de cobertura (solo municipios confirmados)

**Criterios de Éxito**:
- ✅ Municipios listados solo si están en fuentes oficiales
- ✅ Coordenadas incluidas solo si existen en datos
- ✅ Sin asumir ubicaciones no documentadas

**Reglas Estrictas**:
- 🚫 NO inventar coordenadas geográficas
- 🚫 NO asumir municipios no listados
- 🚫 NO proyectar cobertura sin fuente
- ✅ SÍ usar coordenadas de CSV si existen
- ✅ SÍ marcar "coordenadas pendientes" si no hay datos
- ✅ SÍ limitar mapa a puntos verificados

---

### PASO 4.2: Extraer Demanda por Municipio
**Duración estimada**: 45 minutos  
**Prioridad**: MEDIA

**Tareas**:
1. Extraer de `LISTADO_141_MUNICIPIOS_SATELITE.csv`:
   - Columna `demanda_anual` por municipio
   - Sumar por categoría (C2, C3, C4, C5)
   - Verificar totales

2. Buscar en Plan General o Base de Datos:
   - Metodología de cálculo de demanda
   - Fuente de datos de demanda
   - Proyecciones (si existen)

3. Validar coherencia:
   - Demanda total vs capacidad instalada
   - Distribución geográfica razonable

**Entregables**:
- [ ] `DEMANDA_POR_MUNICIPIO.md` con datos del CSV
- [ ] Totales por categoría verificados
- [ ] Metodología de cálculo documentada

**Criterios de Éxito**:
- ✅ Demanda extraída directamente del CSV
- ✅ Totales calculados sin errores
- ✅ Metodología documentada (si está disponible)

---

## 🛠️ FASE 5: EXTRACCIÓN DE ESPECIFICACIONES TÉCNICAS

### PASO 5.1: Extraer Catálogo de Productos/Componentes
**Duración estimada**: 2 horas  
**Prioridad**: ALTA

**Tareas**:
1. Buscar en Base de Datos:
   - Pestaña "SNCALE_Presupuesto_Nivel_1" (ya existe localmente)
   - Columnas: Código, Descripción, Precio, Categoría
   - Total de productos listados

2. Extraer información por categoría:
   - Mobiliario (MOB-*)
   - Tecnología (TEC-*)
   - Vehículos (VEH-*)
   - Materiales (MAT-*)
   - Pistas (PIS-*)
   - Señalización (SEÑ-*)

3. Documentar especificaciones:
   - Descripción exacta del producto
   - Precio unitario
   - Unidad de medida
   - Normas aplicables

**Entregables**:
- [ ] `CATALOGO_PRODUCTOS_OFICIAL.md` con listado completo
- [ ] Tabla estructurada por categoría
- [ ] Referencias a normas técnicas

**Criterios de Éxito**:
- ✅ Catálogo completo extraído de Base de Datos
- ✅ Precios verificados y actualizados
- ✅ Descripciones textuales exactas

**Reglas Estrictas**:
- 🚫 NO modificar descripciones de productos
- 🚫 NO estimar precios faltantes
- 🚫 NO agregar productos no listados
- ✅ SÍ copiar datos exactamente como aparecen
- ✅ SÍ indicar "precio no disponible" si falta
- ✅ SÍ mantener códigos originales

---

### PASO 5.2: Extraer Plataforma MUNAY
**Duración estimada**: 1 hora  
**Prioridad**: MEDIA

**Tareas**:
1. Buscar en Plan General:
   - Sección "Producto P2.1.1: Blueprint de Plataforma (MUNAY v1.0)"
   - Descripción de funcionalidades
   - Componentes tecnológicos
   - Versiones (v1.0 CALE-T, v2.0 CALE-P)

2. Extraer especificaciones:
   - Stack tecnológico (si está especificado)
   - Módulos funcionales
   - Integraciones (RUNT, SICOV, etc.)

3. Buscar costos en Base de Datos:
   - OPEX de plataforma
   - Costos de implementación
   - Licencias de software

**Entregables**:
- [ ] `PLATAFORMA_MUNAY_OFICIAL.md` con especificaciones
- [ ] Diagrama de componentes (si está en fuente)
- [ ] Costos asociados verificados

**Criterios de Éxito**:
- ✅ Especificaciones extraídas del Plan General
- ✅ Componentes listados con fuente
- ✅ Sin asumir tecnologías no mencionadas

---

## 📐 FASE 6: CREACIÓN DE SISTEMA CON DATOS REALES

### PASO 6.1: Crear Portal Web Basado en Datos Reales
**Duración estimada**: 3 horas  
**Prioridad**: ALTA

**Tareas**:
1. Diseñar portal con secciones verificadas:
   - Documentación Oficial (enlaces directos)
   - Categorías CALE (solo las confirmadas)
   - Ubicaciones (solo municipios verificados)
   - Presupuesto (solo cifras de Base de Datos)
   - Especificaciones (solo del Plan General)

2. Implementar visualizaciones:
   - Tablas con datos extraídos
   - Gráficos solo con datos reales
   - Mapas con ubicaciones confirmadas únicamente

3. Agregar advertencias:
   - "Datos preliminares" donde aplique
   - "Pendiente de verificación" en brechas
   - "Fuente: [documento]" en cada dato

**Entregables**:
- [ ] `portal_cale_verificado.html` completamente basado en fuentes
- [ ] Tablas de datos con referencias
- [ ] Sin estimaciones ni proyecciones

**Criterios de Éxito**:
- ✅ Todo dato tiene fuente documentada
- ✅ Sin números inventados
- ✅ Advertencias claras de limitaciones

---

### PASO 6.2: Crear Mapa Interactivo Real
**Duración estimada**: 2 horas  
**Prioridad**: MEDIA

**Tareas**:
1. Usar solo ubicaciones con coordenadas verificadas:
   - Extraer lat/lon de CSV si existen
   - No asumir coordenadas de centros de municipio
   - Marcar "ubicación aproximada" si aplica

2. Mostrar información real:
   - Categoría del nodo (de fuente oficial)
   - Demanda anual (del CSV)
   - Componentes (del Plan General)

3. Implementar filtros:
   - Por categoría verificada
   - Por departamento
   - Por demanda

**Entregables**:
- [ ] `mapa_cale_verificado.html` con ubicaciones reales
- [ ] Leyenda clara de fuentes de datos
- [ ] Advertencia de datos parciales

**Criterios de Éxito**:
- ✅ Solo puntos con coordenadas verificadas
- ✅ Información completa por nodo
- ✅ Filtros funcionales

---

## 📝 FASE 7: DOCUMENTACIÓN Y VALIDACIÓN

### PASO 7.1: Crear Documentación Técnica
**Duración estimada**: 2 horas  
**Prioridad**: ALTA

**Tareas**:
1. Documentar metodología de extracción:
   - Proceso paso a paso
   - Fuentes consultadas
   - Decisiones tomadas (ej: qué hacer con discrepancias)

2. Crear índice de fuentes:
   - Documento → Sección → Página → Dato extraído
   - Tabla de trazabilidad completa

3. Documentar limitaciones:
   - Datos no encontrados en fuentes
   - Información incompleta
   - Brechas de conocimiento

**Entregables**:
- [ ] `METODOLOGIA_EXTRACCION.md` completa
- [ ] `INDICE_FUENTES.md` con trazabilidad
- [ ] `LIMITACIONES_DATOS.md` honesta

**Criterios de Éxito**:
- ✅ Metodología replicable documentada
- ✅ Cada dato trazable a su fuente
- ✅ Limitaciones claramente expuestas

---

### PASO 7.2: Validación con Usuario
**Duración estimada**: 1 hora  
**Prioridad**: CRÍTICA

**Tareas**:
1. Presentar datos extraídos al usuario:
   - Categorías identificadas
   - Presupuestos encontrados
   - Ubicaciones verificadas
   - Especificaciones técnicas

2. Solicitar confirmación:
   - ¿Los datos extraídos son correctos?
   - ¿Hay información adicional en los documentos que no se encontró?
   - ¿Hay discrepancias que el usuario puede aclarar?

3. Incorporar retroalimentación:
   - Corregir interpretaciones erróneas
   - Agregar datos que se pasaron por alto
   - Actualizar documentación

**Entregables**:
- [ ] `VALIDACION_USUARIO.md` con confirmaciones
- [ ] Lista de correcciones aplicadas
- [ ] Sistema actualizado con retroalimentación

**Criterios de Éxito**:
- ✅ Usuario confirma exactitud de datos extraídos
- ✅ Discrepancias resueltas
- ✅ Sistema alineado con expectativas del usuario

---

## ⚙️ REGLAS DE GESTIÓN POR TIPO DE DATO

### 📊 REGLA 1: Datos Cuantitativos (Números, Costos, Cantidades)

**DEBE**:
- ✅ Copiar número exacto de la fuente
- ✅ Incluir unidad (pesos, metros, unidades, etc.)
- ✅ Documentar fuente específica (documento + sección + página)
- ✅ Indicar fecha del dato si está disponible

**NO DEBE**:
- 🚫 Redondear o aproximar
- 🚫 Convertir unidades sin factor oficial
- 🚫 Calcular totales si no están en la fuente
- 🚫 Estimar valores faltantes

**Ejemplo Correcto**:
```markdown
**Costo CALE-T-24q**: $243,000,000 COP
- Fuente: Plan General CALE UPTC, Sección 4.4.2, pág. 45
- Fecha: Octubre 2025
- Unidad: Pesos colombianos por nodo
```

**Ejemplo Incorrecto**:
```markdown
**Costo CALE-T-24q**: ~$240M (estimado)
```

---

### 📍 REGLA 2: Datos Geográficos (Ubicaciones, Coordenadas)

**DEBE**:
- ✅ Usar coordenadas exactas si existen en fuente
- ✅ Indicar sistema de coordenadas (WGS84, etc.)
- ✅ Listar solo municipios mencionados en documentos
- ✅ Marcar "ubicación aproximada" si se usa centroide

**NO DEBE**:
- 🚫 Asumir coordenadas del centro del municipio sin verificar
- 🚫 Agregar municipios no listados en fuentes
- 🚫 Proyectar cobertura sin datos

**Ejemplo Correcto**:
```markdown
**Municipio**: Medellín
- Departamento: Antioquia
- Categoría: Cat.A
- Coordenadas: Pendiente de verificación (no disponibles en fuente)
- Fuente: CSV cales_iebm_dane_mejor_opcion.csv, fila 2
```

**Ejemplo Incorrecto**:
```markdown
**Municipio**: Medellín
- Coordenadas: 6.2442° N, 75.5812° W (obtenidas de Google Maps)
```

---

### 🏗️ REGLA 3: Especificaciones Técnicas

**DEBE**:
- ✅ Citar texto literal del Plan General
- ✅ Usar comillas para transcripciones exactas
- ✅ Mantener nombres técnicos originales
- ✅ Referenciar normas técnicas mencionadas

**NO DEBE**:
- 🚫 Parafrasear especificaciones críticas
- 🚫 Agregar detalles técnicos no mencionados
- 🚫 Asumir componentes "implícitos"

**Ejemplo Correcto**:
```markdown
**CALE-T-24q - Componentes Etapa 1**:

Según Plan General, Sección 4.4.3:
> "Componentes Principales - Etapa 1 (Mínimo Normativo) para CALE-T-24q:
> - Centro de Cómputo
> - Sala Evaluación Teórica
> - Oficinas Administrativas
> - Recepción y Control
> - Servicios Generales
> - Señalización
> - Plataforma Multiservicios"
```

**Ejemplo Incorrecto**:
```markdown
**CALE-T-24q - Componentes Etapa 1**:
- Centro de cómputo con 10 servidores (estimado)
- Sala de evaluación de 150m²
- Oficinas administrativas y recepción
```

---

### 🏛️ REGLA 4: Categorías y Taxonomías

**DEBE**:
- ✅ Usar nombres exactos del Plan General
- ✅ Mantener formato original (Cat.A, Cat.C2, etc.)
- ✅ Documentar criterios de clasificación si están disponibles
- ✅ Citar definición textual de cada categoría

**NO DEBE**:
- 🚫 Inventar subcategorías (Cat.A+, Cat.B**, etc.)
- 🚫 Renombrar categorías por claridad
- 🚫 Crear jerarquías no documentadas

**Ejemplo Correcto**:
```markdown
**Cat.A - CALE Principal**:
- Definición: "CALE Teórico-Práctico principal con función de coordinación regional"
- Fuente: Plan General, Sección 3.3.2
- Tipo: Teórico + Práctico
- Función: Coordinador regional
```

**Ejemplo Incorrecto**:
```markdown
**Cat.A+ - CALE Metropolitano Premium**:
- Nodos principales en ciudades grandes
- Incluye componentes adicionales
```

---

### 💰 REGLA 5: Datos Financieros

**DEBE**:
- ✅ Copiar cifras exactas de Base de Datos
- ✅ Incluir moneda y fecha
- ✅ Diferenciar CAPEX vs OPEX
- ✅ Documentar si es costo unitario o total

**NO DEBE**:
- 🚫 Calcular totales no presentes en fuente
- 🚫 Proyectar costos futuros
- 🚫 Convertir monedas sin tasa oficial
- 🚫 Agregar márgenes o contingencias

**Ejemplo Correcto**:
```markdown
**Presupuesto CALE-T-24q**:
- CAPEX Unitario: $243,000,000 COP
- Fuente: Google Sheets, Pestaña "Presupuesto_CALE_T", Celda B15
- Fecha: Octubre 2025
- Nota: Costo por nodo individual
```

**Ejemplo Incorrecto**:
```markdown
**Presupuesto Total Sistema**:
- Estimado: $850,000M COP
- Calculado: 56 nodos × ~$15M promedio
```

---

### 📝 REGLA 6: Textos y Descripciones

**DEBE**:
- ✅ Usar comillas para citas textuales
- ✅ Indicar fuente de cada párrafo importante
- ✅ Mantener terminología original
- ✅ Traducir solo si fuente está en otro idioma (indicar)

**NO DEBE**:
- 🚫 Parafrasear información crítica
- 🚫 Simplificar textos normativos
- 🚫 Omitir advertencias o limitaciones del documento

**Ejemplo Correcto**:
```markdown
**Resolución 20253040037125/2025**:

Según Plan General, Sección 4.4.2:
> "La Resolución 20253040037125/2025 establece los componentes
> mínimos normativos para CALE-T en su Etapa 1..."
```

---

### ❓ REGLA 7: Datos Faltantes o Incompletos

**DEBE**:
- ✅ Indicar claramente "No disponible en fuentes"
- ✅ Listar qué se buscó y dónde
- ✅ Solicitar al usuario si conoce la ubicación del dato
- ✅ Marcar como "Pendiente de verificación"

**NO DEBE**:
- 🚫 Asumir valores "razonables"
- 🚫 Buscar en fuentes externas no autorizadas
- 🚫 Dejar campos vacíos sin explicación

**Ejemplo Correcto**:
```markdown
**Coordenadas Nodo Medellín**:
- Estado: No disponible en fuentes proporcionadas
- Búsqueda realizada:
  - Plan General CALE UPTC: No contiene coordenadas
  - Base de Datos: Sin columna de coordenadas
  - CSV cales_iebm_dane: Coordenadas en 0,0 (no válidas)
- Acción requerida: Solicitar coordenadas al usuario o fuente oficial
```

---

### 🔄 REGLA 8: Discrepancias Entre Fuentes

**DEBE**:
- ✅ Documentar AMBAS versiones
- ✅ Indicar fuente de cada versión
- ✅ Solicitar aclaración al usuario
- ✅ NO resolver arbitrariamente

**NO DEBE**:
- 🚫 Elegir el dato "más reciente" sin confirmar
- 🚫 Promediar valores discrepantes
- 🚫 Asumir que una fuente es más confiable

**Ejemplo Correcto**:
```markdown
**Costo CALE-T-24q - DISCREPANCIA DETECTADA**:

- Versión Plan General (Sección 4.4.2): $243,000,000 COP
- Versión Base de Datos (Pestaña Costos, B15): $250,000,000 COP
- Diferencia: $7,000,000 COP (2.9%)
- Estado: Pendiente de aclaración con usuario
- Acción: Solicitar confirmación de cifra correcta
```

---

### 🎯 REGLA 9: Validación Continua

**DEBE**:
- ✅ Revisar cada dato antes de publicarlo
- ✅ Mantener log de cambios con fuente
- ✅ Volver a verificar si documento se actualiza
- ✅ Documentar fecha de última verificación

**NO DEBE**:
- 🚫 Confiar en datos extraídos previamente sin re-verificar
- 🚫 Asumir que documentos no cambian
- 🚫 Omitir versionado de datos

---

### 📋 REGLA 10: Transparencia Total

**DEBE**:
- ✅ Indicar claramente qué es dato real vs interpretación
- ✅ Mostrar advertencias de limitaciones
- ✅ Proporcionar enlaces directos a fuentes
- ✅ Admitir cuando algo no se encontró

**NO DEBE**:
- 🚫 Presentar estimaciones como datos oficiales
- 🚫 Ocultar brechas de información
- 🚫 Simular completitud cuando hay vacíos

**Ejemplo Correcto**:
```html
<div class="advertencia">
  ⚠️ <strong>Datos Preliminares</strong><br>
  La información presentada está basada en extracción manual de los documentos
  oficiales. Algunos datos pueden estar pendientes de verificación.
  Última actualización: Octubre 28, 2025.
</div>
```

---

## 📅 CRONOGRAMA ESTIMADO

| Fase | Duración | Dependencias |
|------|----------|--------------|
| Fase 1: Acceso y Lectura | 1.25 horas | Usuario proporciona acceso |
| Fase 2: Datos Estructurales | 3 horas | Fase 1 completa |
| Fase 3: Datos Financieros | 2 horas | Fase 1 completa |
| Fase 4: Datos Geográficos | 1.75 horas | Fase 2 completa |
| Fase 5: Especificaciones | 3 horas | Fase 2 completa |
| Fase 6: Creación Sistema | 5 horas | Fases 2-5 completas |
| Fase 7: Documentación | 3 horas | Fase 6 completa |
| **TOTAL** | **19 horas** | - |

---

## ✅ CRITERIOS DE ACEPTACIÓN FINAL

### El sistema estará completo cuando:

1. ✅ **Todo dato tiene fuente documentada**:
   - Nombre del documento
   - Sección/página específica
   - Fecha de extracción

2. ✅ **Sin datos inventados**:
   - No hay categorías no mencionadas en fuentes
   - No hay números calculados sin fuente
   - No hay coordenadas asumidas

3. ✅ **Brechas claramente identificadas**:
   - Datos no encontrados marcados como "No disponible"
   - Discrepancias documentadas sin resolver arbitrariamente
   - Limitaciones expuestas honestamente

4. ✅ **Usuario valida exactitud**:
   - Revisión completa de datos extraídos
   - Confirmación de interpretaciones
   - Aprobación para publicación

5. ✅ **Sistema funcional con datos reales**:
   - Portal web operativo
   - Mapas con ubicaciones verificadas
   - Tablas con presupuestos oficiales
   - Especificaciones técnicas citadas

---

## 🚀 INICIO DE EJECUCIÓN

**Para comenzar, el usuario debe**:
1. ✅ Confirmar acceso a los 3 documentos oficiales
2. ✅ Autorizar extracción de datos
3. ✅ Estar disponible para aclarar discrepancias
4. ✅ Aprobar metodología propuesta

**Comando para iniciar**:
```
INICIAR FASE 1 - PASO 1.1: Verificar acceso a documentos oficiales
```

---

**Responsable**: GitHub Copilot  
**Fecha creación**: Octubre 28, 2025  
**Versión**: 1.0  
**Estado**: PENDIENTE DE APROBACIÓN DEL USUARIO
