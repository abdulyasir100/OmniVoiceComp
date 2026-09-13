@echo off
rem Build OmniVoice Studio.exe (PyInstaller) + the installer (Inno Setup).
rem One-time prereqs:  .venv\Scripts\pip install pyinstaller
rem                    winget install -e --id JRSoftware.InnoSetup
cd /d "%~dp0.."

echo === [1/2] Freezing launcher with PyInstaller ===
.venv\Scripts\pyinstaller.exe --noconfirm --onefile --windowed ^
  --name "OmniVoice Studio" --icon "%~dp0icon.ico" ^
  --paths gui --distpath "%~dp0dist" ^
  --workpath "%~dp0build" --specpath "%~dp0build" ^
  "%~dp0launcher.py"
if errorlevel 1 exit /b 1

echo === [2/2] Compiling installer with Inno Setup ===
set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" set "ISCC=%LocalAppData%\Programs\Inno Setup 6\ISCC.exe"
"%ISCC%" "%~dp0omnivoice-studio.iss"
if errorlevel 1 exit /b 1

echo.
echo Done. Installer: %~dp0Output\
