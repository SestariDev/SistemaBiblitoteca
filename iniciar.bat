@echo off
echo ========================================
echo Sistema de Biblioteca - Fatec RP
echo ========================================
echo.

REM Verifica se o Python está instalado
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale o Python 3 antes de continuar.
    echo Consulte o arquivo INSTALACAO.md para instruções.
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.

REM Verifica se a biblioteca requests está instalada
python -c "import requests" > nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Biblioteca 'requests' nao encontrada.
    echo [INFO] Instalando dependencias...
    echo.
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERRO] Falha ao instalar dependencias!
        echo Tente executar manualmente: pip install requests
        echo.
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas com sucesso!
    echo.
)

echo [INFO] Iniciando o sistema...
echo.
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] O sistema encerrou com erros.
    echo.
)

pause
