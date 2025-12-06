@echo off
echo ========================================
echo   SERVIDOR LOCAL SNCALE
echo   Mapa Interactivo Nacional
echo ========================================
echo.
echo Iniciando servidor en puerto 8085...
echo.
echo Accede al mapa en:
echo   http://localhost:8085/visualizacion/mapa-interactivo.html
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

cd /d "%~dp0"
python -m http.server 8085
