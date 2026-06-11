set shell := ["sh", "-cu"]

app_dir := "python-app"

setup:
    cd {{app_dir}} && uv sync --group dev

bootstrap:
    cd {{app_dir}} && uv run python scripts/bootstrap_db.py

run:
    cd {{app_dir}} && uv run uvicorn app.main:app --reload

lint:
    cd {{app_dir}} && uv run ruff check .

format:
    cd {{app_dir}} && uv run ruff format .

test:
    cd {{app_dir}} && uv run pytest

check:
    cd {{app_dir}} && uv run ruff check . && uv run pytest
