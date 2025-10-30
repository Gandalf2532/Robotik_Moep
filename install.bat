@echo off
setlocal

echo ====================================================
echo Installer für dieses Projekt
echo ====================================================
echo.

call :install "Git.Git" "Git"
call :install "Microsoft.VisualStudioCode" "Visual Studio Code"
call :install "Docker.DockerDesktop" "Docker Desktop"

echo.
echo ====================================================
echo Alle installationen abgeschlossen
echo ====================================================
pause
exit /b

:install
set "PACKAGE_ID=%~1"
set "PACKAGE_NAME=%~2"

winget list --id %PACKAGE_ID% | findstr /I "%PACKAGE_ID%" >nul
if %errorlevel%==0 (
    echo %PACKAGE_NAME% ist schon installiert. Wird übersprungen...
) else (
    set /p PROMPT=Möchtest du %PACKAGE_NAME% installieren? (y/n)
    if "%PROMPT%"=="n" (
        echo %PACKAGE_NAME% wird nicht installiert!
    ) else (
        winget install --id %PACKAGE_ID% --silent --accept-package-agreements --accept-source-agreements
    )
)
echo.
