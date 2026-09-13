@echo off
REM Launch the OmniVoice Auto Cut & Merge tool using the venv's pythonw (no console window).
cd /d "%~dp0\.."
start "" ".venv\Scripts\pythonw.exe" "gui\merge.pyw"
