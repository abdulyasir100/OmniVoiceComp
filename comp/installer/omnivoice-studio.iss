; OmniVoice Studio installer — Inno Setup script.
; Build with installer\build.bat (PyInstaller exe first, then this).

#define MyAppName "OmniVoice Studio"
#define MyAppVersion "1.1.0"   ; keep in sync with gui\appconfig.py APP_VERSION
#define MyAppExeName "OmniVoice Studio.exe"

[Setup]
AppId={{7E3A9C41-5B2F-4D8A-9C6E-2B84D1F0A317}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher=Venomaru
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
PrivilegesRequired=lowest
DisableProgramGroupPage=yes
OutputDir=Output
OutputBaseFilename=OmniVoiceStudio-Setup-{#MyAppVersion}
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Change OmniVoice Folder"; Filename: "{app}\{#MyAppExeName}"; Parameters: "--reconfigure"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent
