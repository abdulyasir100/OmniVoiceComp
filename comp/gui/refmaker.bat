@echo off
REM Launch the OmniVoice Reference Clip Maker using the venv's pythonw (no console window).
cd /d "%~dp0\.."
start "" ".venv\Scripts\pythonw.exe" "gui\refmaker.pyw"
