set shell := ["powershell.exe", "-NoLogo", "-Command"]

app_dir := "python-app"

setup:
    Set-Location {{app_dir}}; uv sync

bootstrap:
    Set-Location {{app_dir}}; uv run python scripts/bootstrap_db.py

run:
    Set-Location {{app_dir}}; uv run uvicorn app.main:app --reload

lint:
    Set-Location {{app_dir}}; uv run ruff check .

format:
    Set-Location {{app_dir}}; uv run ruff format .

test:
    Set-Location {{app_dir}}; uv run pytest

check:
    Set-Location {{app_dir}}; uv run ruff check .; uv run pytest
