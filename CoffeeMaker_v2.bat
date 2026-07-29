@echo off
cd /d "%~dp0" || exit /b 1

python -u turnvolume_v3.py
set "exitcode=%errorlevel%"

if not "%exitcode%"=="0" (
    echo.
    echo Caffeinate failed with exit code %exitcode%.
    pause
)

exit /b %exitcode%
