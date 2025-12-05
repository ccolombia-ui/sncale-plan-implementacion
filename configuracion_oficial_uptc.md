# CONFIGURACIÓN OFICIAL UPTC - IDENTIDAD INSTITUCIONAL
**Plan Implementación CALE - Universidad Pedagógica y Tecnológica de Colombia**

---

## 🏛️ **IDENTIDAD INSTITUCIONAL OFICIAL**

### **INFORMACIÓN GENERAL**
```yaml
nombre_completo: "Universidad Pedagógica y Tecnológica de Colombia"
sigla: "UPTC"
sitio_web: "uptc.edu.co"
lema: "Somos Todos"
ubicacion_principal: "TUNJA - DUITAMA - SOGAMOSO - CHIQUINQUIRÁ"
sede_principal: "AVENIDA CENTRAL DEL NORTE 39-115"
telefono: "PBX 57+8 7405626"
ciudad_sede: "TUNJA - BOYACÁ"
```

### **CERTIFICACIONES Y ACREDITACIONES**

#### **🏆 CEAI - ACREDITACIÓN INSTITUCIONAL INTERNACIONAL**
```yaml
certificacion: "ACREDITACIÓN INSTITUCIONAL INTERNACIONAL"
periodo: "2022 - 2027"
vigencia: "VIGENCIA 5 AÑOS"
tipo: "UDUAL - Unión de Universidades de América Latina"
icono: "Laurel dorado CEAI"
```

#### **🌟 ACREDITACIÓN INSTITUCIONAL DE ALTA CALIDAD**
```yaml
certificacion: "ACREDITACIÓN INSTITUCIONAL DE ALTA CALIDAD"
tipo: "MULTICAMPUS"
vigencia: "VIGENCIA 8 AÑOS"
periodo: "RESOLUCIÓN 003468 DE 2023 MINEDUCACIÓN"
nivel: "ALTA CALIDAD MULTICAMPUS"
```

#### **📍 COBERTURA TERRITORIAL**
```yaml
departamento: "BOYACÁ"
regiones: 
  - "TUNJA"
  - "DUITAMA" 
  - "SOGAMOSO"
  - "CHIQUINQUIRÁ"
alcance: "REGIONAL MULTICAMPUS"
```

---

## 🎨 **ELEMENTOS VISUALES OFICIALES**

### **LOGOTIPO PRINCIPAL**
```yaml
logo_principal: "Escudo UPTC con águila bicéfala"
colores_primarios:
  - amarillo: "#FFD700" # Amarillo UPTC
  - negro: "#000000"    # Negro institucional
  - blanco: "#FFFFFF"   # Blanco complementario
formato_preferido: "PNG con transparencia"
usos: "Documentos oficiales, sitio web, material institucional"
```

### **LOGO SECUNDARIO "SOMOS TODOS"**
```yaml
logo_secundario: "Somos Todos - Franja amarilla"
uso: "Campañas institucionales y material promocional"
colores:
  - amarillo: "#FFD700"
  - negro: "#000000"
posicion: "Complementario al logo principal"
```

### **PALETA DE COLORES INSTITUCIONAL**
```css
:root {
  /* Colores primarios UPTC */
  --uptc-amarillo: #FFD700;
  --uptc-negro: #000000;
  --uptc-blanco: #FFFFFF;
  
  /* Colores complementarios */
  --uptc-gris-claro: #F5F5F5;
  --uptc-gris-medio: #CCCCCC;
  --uptc-gris-oscuro: #333333;
  
  /* Colores de acento para certificaciones */
  --ceai-dorado: #DAA520;
  --acreditacion-azul: #0066CC;
}
```

---

## 📄 **PLANTILLAS DE ENCABEZADO Y PIE**

### **ENCABEZADO OFICIAL**
```html
<header class="uptc-header">
  <div class="header-container">
    <div class="logo-section">
      <img src="assets/logos/logo-uptc-oficial.png" alt="UPTC Logo" class="logo-principal">
      <div class="texto-institucional">
        <h1>UPTC</h1>
        <p>Universidad Pedagógica y Tecnológica de Colombia</p>
      </div>
    </div>
    
    <div class="slogan-section">
      <div class="somos-todos">
        <span class="somos">Somos</span>
        <span class="todos">TODOS</span>
      </div>
    </div>
    
    <div class="contacto-section">
      <p class="sitio-web">uptc.edu.co</p>
      <p class="ubicaciones">TUNJA - DUITAMA - SOGAMOSO - CHIQUINQUIRÁ</p>
    </div>
  </div>
</header>
```

### **PIE DE PÁGINA OFICIAL**
```html
<footer class="uptc-footer">
  <div class="footer-container">
    
    <!-- Certificaciones -->
    <div class="certificaciones-section">
      <div class="ceai-cert">
        <div class="ceai-logo">🏆</div>
        <div class="ceai-text">
          <strong>CEAI</strong><br>
          <small>ACREDITACIÓN INSTITUCIONAL</small><br>
          <strong>INTERNACIONAL</strong><br>
          <small>2022 - 2027</small><br>
          <small>VIGENCIA 5 AÑOS</small>
        </div>
      </div>
      
      <div class="acreditacion-cert">
        <div class="acred-text">
          <strong>ACREDITACIÓN INSTITUCIONAL</strong><br>
          <strong>DE ALTA CALIDAD</strong><br>
          <strong>MULTICAMPUS</strong><br>
          <small>RESOLUCIÓN 003468 DE 2023 MINEDUCACIÓN</small><br>
          <small>VIGENCIA 8 AÑOS</small>
        </div>
      </div>
    </div>
    
    <!-- Información de contacto -->
    <div class="contacto-footer">
      <p><strong>AVENIDA CENTRAL DEL NORTE 39-115</strong></p>
      <p><strong>PBX 57+8 7405626</strong></p>
      <p><strong>TUNJA - BOYACÁ</strong></p>
    </div>
    
  </div>
</footer>
```

---

## 🎯 **APLICACIÓN AL PROYECTO CALE**

### **BRANDING CONSISTENTE**
```yaml
proyecto: "Plan Implementación CALE UPTC"
entidad_ejecutora: "Universidad Pedagógica y Tecnológica de Colombia"
respaldo_institucional: 
  - "Acreditación Internacional CEAI (2022-2027)"
  - "Alta Calidad Multicampus (Resolución 003468/2023)"
  - "Cobertura Regional Boyacá"
cobertura_proyecto: "Nacional (197 nodos en 32 departamentos)"
```

### **ELEMENTOS REQUERIDOS EN TODAS LAS PÁGINAS**
1. **Logo UPTC** en header
2. **"Somos Todos"** como complemento
3. **Certificaciones** en footer
4. **Información de contacto** completa
5. **Colores institucionales** consistentes
6. **uptc.edu.co** como referencia web

### **JERARQUÍA VISUAL**
```
NIVEL 1: Universidad Pedagógica y Tecnológica de Colombia (UPTC)
NIVEL 2: Plan Implementación CALE UPTC  
NIVEL 3: Sistema Nacional de Centros de Apoyo Logístico
NIVEL 4: Componentes específicos (nodos, categorías, etc.)
```

---

## 📋 **CHECKLIST DE IMPLEMENTACIÓN**

### **✅ ELEMENTOS VISUALES**
- [ ] Logo UPTC oficial en alta resolución
- [ ] Banner "Somos Todos" implementado
- [ ] Paleta de colores aplicada consistentemente
- [ ] Certificaciones CEAI y Alta Calidad visibles

### **✅ INFORMACIÓN INSTITUCIONAL**
- [ ] uptc.edu.co como sitio web de referencia
- [ ] Dirección oficial: Avenida Central del Norte 39-115
- [ ] PBX: 57+8 7405626
- [ ] Ubicaciones: Tunja - Duitama - Sogamoso - Chiquinquirá

### **✅ CERTIFICACIONES**
- [ ] CEAI 2022-2027 (5 años vigencia)
- [ ] Alta Calidad Multicampus (Res. 003468/2023, 8 años)
- [ ] UDUAL destacado apropiadamente

### **✅ RESPONSIVE Y ACCESIBILIDAD**
- [ ] Header adaptable a mobile
- [ ] Footer legible en todas las resoluciones
- [ ] Certificaciones visibles sin scroll horizontal
- [ ] Contraste adecuado (amarillo/negro)

---

**📅 Creado**: Octubre 28, 2025  
**🔄 Versión**: 1.0 - Configuración oficial UPTC  
**👤 Basado en**: Encabezado y pie oficial UPTC  
**📊 Aplicación**: Plan Implementación CALE UPTC