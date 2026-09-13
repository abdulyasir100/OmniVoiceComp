@echo off
REM Launch the OmniVoice GUI using the venv's pythonw (no console window).
cd /d "%~dp0\.."
start "" ".venv\Scripts\pythonw.exe" "gui\app.pyw"
