# Start Powershell using this to run the script:  powershell -ExecutionPolicy bypass
$gitVersion = "2.42.0"
$gitInstaller = "Git-$gitVersion-64-bit.exe"
$downloadUrl = "https://github.com/git-for-windows/git/releases/download/v$gitVersion.windows.1/$gitInstaller"
$destination = "$env:TEMP\$gitInstaller"
Invoke-WebRequest -Uri $downloadUrl -OutFile $destination
Start-Process -FilePath $destination -ArgumentList "/VERYSILENT" -NoNewWindow -Wait
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
try {
    $gitVersionOutput = & git --version
    Write-Output "Git installation successful: $gitVersionOutput"
} catch {
    Write-Output "Git installation failed or Git is not in PATH."
}
