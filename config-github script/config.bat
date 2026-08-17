@echo off
chcp 65001 > nul

echo Creating PowerShell script...

> temp_script.ps1 (
    echo $outputFile = "merged.txt"
    echo.
    echo if ^(Test-Path $outputFile^) ^{
    echo     Remove-Item $outputFile
    echo ^}
    echo.
    echo for ^($i = 1; $i -le 10; $i++^) ^{
    echo.
    echo     $url = "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray_configs_no$i.txt"
    echo.
    echo     Write-Host "Downloading: $url"
    echo.
    echo     try ^{
    echo         $content = Invoke-RestMethod -Uri $url
    echo         Add-Content -Path $outputFile -Value "===== v2ray_configs_no$i.txt ====="
    echo         Add-Content -Path $outputFile -Value $content
    echo         Add-Content -Path $outputFile -Value ""
    echo     ^}
    echo     catch ^{
    echo         Write-Host "Failed to download file $i"
    echo     ^}
    echo ^}
    echo.
    echo for ^($i = 1; $i -le 12; $i++^) ^{
    echo.
    echo     $url = "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub$i.txt"
    echo.
    echo     Write-Host "Downloading: $url"
    echo.
    echo     try ^{
    echo         $content = Invoke-RestMethod -Uri $url
    echo         Add-Content -Path $outputFile -Value "===== barry-far_Sub$i.txt ====="
    echo         Add-Content -Path $outputFile -Value $content
    echo         Add-Content -Path $outputFile -Value ""
    echo     ^}
    echo     catch ^{
    echo         Write-Host "Failed to download file $i"
    echo     ^}
    echo ^}
    echo.
    echo Write-Host "Done! Output saved to $outputFile"
)

echo Running script...
echo.

PowerShell -ExecutionPolicy Bypass -File temp_script.ps1

del temp_script.ps1

echo.
echo ==============================
echo Finished! Check merged.txt
echo ==============================
pause
