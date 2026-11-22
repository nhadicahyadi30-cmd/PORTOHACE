@echo off
cd /d "%~dp0"
where python >nul 2>nul && (set PY=python) || (set PY=py)
%PY% build.py
if errorlevel 1 (echo Build gagal. Pastikan Python terpasang. & pause & exit /b 1)
echo.
echo Website jalan di http://localhost:8000  (tutup jendela ini untuk berhenti)
start "" http://localhost:8000
cd dist
%PY% -m http.server 8000
