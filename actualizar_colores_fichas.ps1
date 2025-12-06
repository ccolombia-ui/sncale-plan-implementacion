# Script para actualizar los colores de todos los archivos HTML en la carpeta fichas
# Cambia el esquema de colores oscuro azul a blanco/gris claro

$carpetaFichas = "c:\Users\USER\Desktop\Juan Steven\Programacion\Plan-Implementacion\Plan-Implementacion\fichas"
$archivos = Get-ChildItem "$carpetaFichas\BIM_L0_*.html" | Sort-Object Name

Write-Host "Encontrados $($archivos.Count) archivos HTML" -ForegroundColor Green
Write-Host "Actualizando colores de oscuro a blanco/gris claro..." -ForegroundColor Yellow

$contador = 0
$actualizados = 0

foreach ($archivo in $archivos) {
    $contador++
    Write-Host "[$contador/$($archivos.Count)] Procesando $($archivo.Name)..." -ForegroundColor Cyan
    
    try {
        # Leer el contenido del archivo
        $contenido = Get-Content $archivo.FullName -Raw -Encoding UTF8
        
        # Realizar los reemplazos
        $contenidoNuevo = $contenido
        
        # 1. Cambiar variables CSS
        $contenidoNuevo = $contenidoNuevo -replace '--primary-color: #2c3e50;', '--primary-color: #333;'
        $contenidoNuevo = $contenidoNuevo -replace '--secondary-color: #3498db;', '--secondary-color: #666;'
        $contenidoNuevo = $contenidoNuevo -replace '--accent-color: #e74c3c;', '--accent-color: #999;'
        $contenidoNuevo = $contenidoNuevo -replace '--bg-light: #ecf0f1;', '--bg-light: #f5f7fa;'
        
        # 2. Cambiar fondo del sidebar
        $contenidoNuevo = $contenidoNuevo -replace 'background: linear-gradient\(180deg, #1e3a5f 0%, var\(--primary-color\) 100%\);', 'background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);'
        $contenidoNuevo = $contenidoNuevo -replace '(\s+)color: white;(\s+overflow-y: auto;)', '$1color: #000;$2'
        
        # 3. Cambiar borde del sidebar header
        $contenidoNuevo = $contenidoNuevo -replace 'border-bottom: 2px solid rgba\(255,255,255,0\.2\);', 'border-bottom: 2px solid #ddd;'
        
        # 4. Cambiar fondo del header BIM
        $contenidoNuevo = $contenidoNuevo -replace 'background: linear-gradient\(135deg, var\(--primary-color\), var\(--secondary-color\)\);(\s+)color: white;', 'background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);$1color: #000;'
        
        # Solo guardar si hubo cambios
        if ($contenido -ne $contenidoNuevo) {
            Set-Content $archivo.FullName -Value $contenidoNuevo -Encoding UTF8 -NoNewline
            Write-Host "  ✓ Actualizado" -ForegroundColor Green
            $actualizados++
        } else {
            Write-Host "  - Sin cambios" -ForegroundColor Gray
        }
    }
    catch {
        Write-Host "  ✗ Error: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "COMPLETADO" -ForegroundColor Green
Write-Host "Archivos procesados: $contador" -ForegroundColor Cyan
Write-Host "Archivos actualizados: $actualizados" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
