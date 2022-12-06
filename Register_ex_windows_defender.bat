ECHO this bat file regist this exe to exclude from security scan
PAUSE
REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v %~dp0workss.exe /t REG_DWORD