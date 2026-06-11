Set-Location "$PSScriptRoot\..\..\python-app"
uv run ruff check app tests scripts
if ($LASTEXITCODE -ne 0) {
    exit 2
}
