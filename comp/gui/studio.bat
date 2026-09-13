@echo off
REM Launch OmniVoice Studio (all three tabs) using the venv's pythonw (no console window).
cd /d "%~dp0\.."
start "" ".venv\Scripts\pythonw.exe" "gui\studio.pyw"
