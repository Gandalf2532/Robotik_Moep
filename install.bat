@echo off
setlocal

echo ====================================================
echo Robotik MOEP Installer
echo ====================================================
echo.

call :install "Git.Git" "Git"
call :install "Microsoft.VisualStudioCode" "Visual Studio Code"

echo Erweiterungen werden installiert...
set EXTENSIONS=ms-python.python ms-python.vscode-pylance esbenp.prettier-vscode Alexey-Strakh.stackoverflow-search github.vscode-github-actions NilsSoderman.batch-runner dusongpei.pybricks oliverdantzer.file-structure-tree
for %%E in (%EXTENSIONS%) do (
    code --list-extensions | findstr /I "%%E" >nul
    if errorlevel 1 (
        code --install-extension %%E
        timeout /t 2 /nobreak >nul
    ) else (
        echo %%E ist bereits installiert
    )
)

echo Repository wird geklont...
set /p GIT_USER="Gib den Nutzernamen ein: "
set /p GIT_EMAIL="Gib die Email ein: "
cd %USERPROFILE%/Documents
mkdir GitHub
cd GitHub
git clone https://github.com/MOEP-Robotik/Robotik_Moep
git config --global user.name %GIT_USER% && git config --global user.email %GIT_EMAIL%

echo Python requirements installieren...
cd %USERPROFILE%/Documents/GitHub/Robotik_Moep
pip install -r requirements

echo.
echo ====================================================
echo Alle installationen abgeschlossen
echo ====================================================
pause
exit /b

:install
set "PACKAGE_ID=%~1"
set "PACKAGE_NAME=%~2"

winget list --id %PACKAGE_ID% --accept-source-agreements | findstr /I "%PACKAGE_ID%" >nul
if %errorlevel%==0 (
    echo %PACKAGE_NAME% ist schon installiert. Wird übersprungen...
) else (
    set /p PROMPT="Willst du %PACKAGE_NAME% installieren? [Y/n] "
    if "%PROMPT%"=="n" (
        echo %PACKAGE_NAME% wird nicht installiert!
    ) else (
        winget install --id %PACKAGE_ID% --silent --accept-package-agreements --accept-source-agreements
    )
)


