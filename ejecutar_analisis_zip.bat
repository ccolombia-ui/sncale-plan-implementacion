@echo off
REM Script para extraer y analizar el ZIP del Plan de Implementación

echo ============================================
echo EXTRACCION Y ANALISIS DEL ZIP
echo ============================================
echo.

cd /d c:\proyectos\sncale-plan-implementacion-main\sncale-plan-implementacion-main

echo Ejecutando extraccion...
python extraer_zip_analisis.py

echo.
echo Presione cualquier tecla para continuar...
pause >nul
