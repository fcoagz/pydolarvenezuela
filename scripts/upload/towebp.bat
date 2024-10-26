@echo off
setlocal enabledelayedexpansion

set "carpeta=./icons"

if not exist "%carpeta%/webp" (
    mkdir "%carpeta%/webp"
)

for %%f in ("%carpeta%\*.png") do (
    set "nombre=%%~nf"
    set "extension=%%~xf"
    
    if /i "!extension!"==".png" (
        "ffmpeg" -i "%%f" "%carpeta%\webp\!nombre!.webp" -y
    )
)

endlocal