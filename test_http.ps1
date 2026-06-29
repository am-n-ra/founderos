$p = Start-Process -NoNewWindow python -ArgumentList 'test_http_server.py' -PassThru
Start-Sleep 4
try {
    $r = Invoke-WebRequest -Uri http://127.0.0.1:8743/health -UseBasicParsing | Select -ExpandProperty Content
    Write-Output $r
} catch {
    Write-Output "Request failed: $_"
}
Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
