
$outputFile = "merged.txt"

if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

for ($i = 1; $i -le 10; $i++) {

    $url = "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray_configs_no$i.txt"

    Write-Host "Downloading: $url"

    try {
        $content = Invoke-RestMethod -Uri $url

        Add-Content -Path $outputFile -Value "===== v2ray_configs_no$i.txt ====="
        Add-Content -Path $outputFile -Value $content
        Add-Content -Path $outputFile -Value "`n"
    }
    catch {
        Write-Host "Failed to download file $i"
    }
}

for ($i = 1; $i -le 12; $i++) {

    $url = "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub$i.txt"

    Write-Host "Downloading: $url"

    try {
        $content = Invoke-RestMethod -Uri $url

        Add-Content -Path $outputFile -Value "===== barry-far_Sub$i.txt ====="
        Add-Content -Path $outputFile -Value $content
        Add-Content -Path $outputFile -Value "`n"
    }
    catch {
        Write-Host "Failed to download file $i"
    }
}

Write-Host "Done! Output saved to $outputFile"
