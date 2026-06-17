set shell := ["sh", "-cu"]

app_dir := "python-app"

setup:
    cd {{app_dir}} && uv sync --frozen --group dev

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

doctor:
    @echo "=== copilot-primer environment check ==="
    @command -v uv      >/dev/null 2>&1 && echo "uv:      $(uv --version)"      || echo "uv:      MISSING (https://docs.astral.sh/uv/)"
    @command -v just    >/dev/null 2>&1 && echo "just:    $(just --version)"    || echo "just:    MISSING"
    @command -v python3 >/dev/null 2>&1 && echo "python3: $(python3 --version)" || echo "python3: MISSING"
    @command -v code    >/dev/null 2>&1 && echo "code:    $(code --version | head -n1)" || echo "code:    MISSING (VS Code CLI not on PATH)"
    @test -f {{app_dir}}/uv.lock && echo "uv.lock: present" || echo "uv.lock: MISSING (run 'cd {{app_dir}} && uv lock')"
