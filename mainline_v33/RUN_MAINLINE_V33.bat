@echo off
setlocal EnableExtensions
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0RUN_MAINLINE_V33.ps1" %*
exit /b %ERRORLEVEL%
