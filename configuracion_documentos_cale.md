# CONFIGURACIÓN DOCUMENTOS CALE UPTC
# Portal Integral - Migración Google Docs → PDF
# Fecha: Octubre 28, 2025

## 📋 DOCUMENTOS MAESTROS

### Plan General CALE UPTC
- **Estado actual**: Google Docs
- **URL actual**: https://docs.google.com/document/d/1jffTX_IetOiIKOsGG_y-xpRUVDTbFp9AIgtnbcfTDpg/edit?tab=t.0
- **URL futura**: documentos/plan_general_cale_uptc.pdf
- **Migración**: Pendiente generación PDF oficial

### Carta de Solicitud Oficial  
- **Estado actual**: En preparación
- **URL futura**: documentos/carta_solicitud_oficial.pdf
- **Contenido**: Solicitud formal ante autoridades competentes

### Anexos Normativos

#### Anexo A - Marco Normativo
- **URL futura**: documentos/anexo_a_marco_normativo.pdf
- **Contenido**: Ley 769/2002, Decreto 1079/2015, Resoluciones aplicables

#### Anexo B - Especificaciones Técnicas
- **URL futura**: documentos/anexo_b_especificaciones.pdf
- **Contenido**: CALE-P, CALE-T, Equipamiento, Infraestructura

#### Anexo C - Plan de Implementación
- **URL futura**: documentos/anexo_c_implementacion.pdf
- **Contenido**: Cronograma, Fases, Presupuesto, Recursos

## 🔗 BASE DE DATOS EN LÍNEA

### Google Sheets Master
- **URL**: https://docs.google.com/spreadsheets/d/10k6SjOScnCte9Awh4JNhpiQ-zBWLvAHflyIWsVqvMYU/edit?gid=241106151#gid=241106151
- **Estado**: Disponible permanentemente
- **Contenido**: 197 nodos, costos, especificaciones

## 📁 ESTRUCTURA FUTURA DOCUMENTOS

```
documentos/
├── plan_general_cale_uptc.pdf
├── carta_solicitud_oficial.pdf
├── anexo_a_marco_normativo.pdf
├── anexo_b_especificaciones.pdf
├── anexo_c_implementacion.pdf
└── README.md
```

## 🔄 PROCESO DE MIGRACIÓN

1. **Generación PDFs**: Conversión desde Google Docs
2. **Validación**: Revisión contenido y formato
3. **Actualización enlaces**: Cambio automático en portal
4. **Respaldo**: Mantener Google Docs como fuente editable
5. **Notificación**: Usuarios informados del cambio

## ⚙️ CONFIGURACIÓN TÉCNICA

### Variables de entorno
```bash
DOCS_PATH="documentos/"
GDOCS_FALLBACK=true
PDF_GENERATION_TOOL="pandoc"
AUTO_UPDATE_LINKS=true
```

### Script actualización automática
```python
def actualizar_enlaces_pdf():
    # Detectar disponibilidad PDFs
    # Actualizar portal_integral_cale_uptc.html
    # Notificar cambios
    pass
```

---
**Nota**: Este archivo documenta la transición planificada de Google Docs a PDFs oficiales.
El portal mantiene compatibilidad con ambos formatos durante la migración.
