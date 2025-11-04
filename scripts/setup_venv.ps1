param(
  [string]$venvPath = ".venv",
  [string]$req = "requirements.txt"
)

Write-Host "Creating virtual environment at: $venvPath"
python -m venv $venvPath

Write-Host "Temporarily setting ExecutionPolicy to allow activation in this session"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

Write-Host "Activating virtual environment"
& "$venvPath\Scripts\Activate.ps1"

if (Test-Path $req) {
  Write-Host "Found $req — installing dependencies"
  pip install -r $req
} else {
  Write-Host "No requirements.txt found at $(Resolve-Path $req) — skipping pip install"
}

Write-Host "Setup complete. To activate later, run: .\$venvPath\Scripts\Activate.ps1"
