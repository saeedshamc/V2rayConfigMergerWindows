@echo off
chcp 65001 > nul
title V2Ray Merger - Build EXE

echo ==============================================
echo   ساخت فایل اجرایی V2Ray Config Merger
echo ==============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo پایتون پیدا نشد! لطفاً ابتدا Python را از python.org نصب کنید
    echo و در حین نصب گزینه "Add Python to PATH" را تیک بزنید.
    pause
    exit /b 1
)

echo در حال نصب PyInstaller ...
python -m pip install --upgrade pip >nul
python -m pip install pyinstaller >nul

echo.
echo در حال ساخت فایل exe ...
python -m PyInstaller --onefile --windowed --name "V2RayMerger" app.py

echo.
if exist dist\V2RayMerger.exe (
    echo ==============================================
    echo ساخت با موفقیت انجام شد.
    echo فایل خروجی: dist\V2RayMerger.exe
    echo ==============================================
) else (
    echo مشکلی در ساخت exe پیش آمد. خروجی بالا را بررسی کنید.
)

pause
