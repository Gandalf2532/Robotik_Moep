@echo off
setlocal

echo ====================================================
echo Robotik MOEP Installer
echo ====================================================
echo.

echo Du musst y eingeben, sonst funktioniert das skript nicht!
winget list

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
    set /p PROMPT=Willst du %PACKAGE_NAME% installieren? [Y/n] 
    if "%PROMPT%"=="n" (
        echo %PACKAGE_NAME% wird nicht installiert!
    ) else (
        winget install --id %PACKAGE_ID% --silent --accept-package-agreements --accept-source-agreements
    )
)
