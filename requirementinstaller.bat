@echo off
color 09
title python installer
echo installing python to PATH if not already installed...
set PYTHON_VERSION=3.10.5
set INSTALL_PATH=C:\Python%PYTHON_VERSION%


if not exist python-%PYTHON_VERSION%-amd64.exe (
    curl -o python-%PYTHON_VERSION%-amd64.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
)

echo Installing Python %PYTHON_VERSION%...
python-%PYTHON_VERSION%-amd64.exe /quiet InstallAllUsers=1 TargetDir=%INSTALL_PATH% Include_test=0 PrependPath=1

if exist %INSTALL_PATH%\python.exe (
    echo Python %PYTHON_VERSION% installed successfully!
) else (
    echo Installation failed. Please check for issues.
    exit /b 1
)


echo.
echo Verifying Python version in PATH...
python --version
title requirements installer
echo press any key to install....
pause > nul
cls
pip install -r requirements.txt
cls
color 0a
echo done! you can now close the program
pause > nul

