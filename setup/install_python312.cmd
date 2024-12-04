@echo off
set pythonVersion=3.11.4
set pythonInstaller=python-%pythonVersion%-amd64.exe
set downloadUrl=https://www.python.org/ftp/python/%pythonVersion%/%pythonInstaller%
curl -o %TEMP%\%pythonInstaller% %downloadUrl%
%TEMP%\%pythonInstaller% /quiet InstallAllUsers=1 PrependPath=1
python --version
