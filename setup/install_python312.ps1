$pythonVersion = "3.12.8"
$pythonInstaller = "python-$pythonVersion-amd64.exe"
$downloadUrl = "https://www.python.org/ftp/python/$pythonVersion/$pythonInstaller"
$destination = "$env:TEMP\$pythonInstaller"
Invoke-WebRequest -Uri $downloadUrl -OutFile $destination
Start-Process -FilePath $destination -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -NoNewWindow -Wait
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
try {
    $pythonVersionOutput = & python --version
    Write-Output "Python installation successful: $pythonVersionOutput"
} catch {
    Write-Output "Python installation failed or Python is not in PATH."
}
