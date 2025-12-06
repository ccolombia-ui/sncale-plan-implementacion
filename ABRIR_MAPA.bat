@echo off
echo ========================================
echo   ABRIENDO MAPA INTERACTIVO SNCALE
echo ========================================
echo.
echo El mapa se abrirá en tu navegador predeterminado...
echo.
timeout /t 2 /nobreak >nul
start http://localhost:8085/visualizacion/mapa-interactivo.html
