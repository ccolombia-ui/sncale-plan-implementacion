# Script para eliminar enlaces BIM_L0_083 a BIM_L0_091 de archivos BIM_L0_001 a BIM_L0_081

$basePath = "c:\Users\USER\Desktop\Juan Steven\Programacion\sncale-plan-implementacion\sncale-plan-implementacion\fichas"

$archivosModificados = 0
$archivosError = 0

# Procesar archivos del 001 al 081
for ($i = 1; $i -le 81; $i++) {
    $numero = "{0:D3}" -f $i
    $archivo = Join-Path $basePath "BIM_L0_$numero.html"
    
    if (Test-Path $archivo) {
        try {
            Write-Host "Procesando: BIM_L0_$numero.html" -ForegroundColor Cyan
            
            # Leer contenido
            $contenido = Get-Content $archivo -Raw -Encoding UTF8
            
            # Verificar si contiene referencias a BIM_L0_083
            if ($contenido -match 'BIM_L0_083') {
                # Buscar y eliminar el bloque completo desde 083 hasta 091
                $patron = '(?s)<a href="BIM_L0_083\.html".*?091: Señalización inclusiva braille\s*</a>\s*'
                $nuevoContenido = $contenido -replace $patron, ''
                
                # Guardar archivo
                $nuevoContenido | Set-Content -Path $archivo -Encoding UTF8 -NoNewline
                
                Write-Host "  [OK] Modificado exitosamente" -ForegroundColor Green
                $archivosModificados++
            } else {
                Write-Host "  [--] No contiene el bloque o ya fue eliminado" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "  [ERROR] $_" -ForegroundColor Red
            $archivosError++
        }
    } else {
        Write-Host "  [!] Archivo no encontrado: BIM_L0_$numero.html" -ForegroundColor DarkYellow
    }
}

Write-Host "`n========================================"
Write-Host "RESUMEN:"
Write-Host "========================================"
Write-Host "Archivos modificados: $archivosModificados" -ForegroundColor Green
Write-Host "Archivos con error: $archivosError" -ForegroundColor Red
Write-Host "========================================`n"
