@echo off
title Server Toyland.id (Tugas Digital Marketing)
echo ========================================================
echo        WEBSITE BISNIS TOYLAND.ID - MATA KULIAH
echo                  DIGITAL MARKETING
echo ========================================================
echo Membuka browser ke http://localhost:8080 ...
start http://localhost:8080
echo Server aktif di port 8080!
echo Jangan tutup jendela hitam ini selama website digunakan atau dipresentasikan.
echo Tekan CTRL + C untuk mematikan server.
echo.
"C:\Users\HP\AppData\Local\Programs\Python\Python314\python.exe" -m http.server 8080
if %ERRORLEVEL% NEQ 0 (
  python -m http.server 8080
)
pause
