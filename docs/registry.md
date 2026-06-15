# Package Registry (Artifactory)

The primer runs against public PyPI by default so it works out of the box. In an Alliander-managed environment, route every `uv` install through the internal JFrog Artifactory mirror instead.

## Configure `uv` to use Artifactory

Add the index to `python-app/pyproject.toml`:

```toml
[[tool.uv.index]]
name = "alliander"
url = "https://artifactory.alliander.com/artifactory/api/pypi/pypi-virtual/simple/"
default = true
```

Authenticate non-interactively using a personal Artifactory token:

```sh
export UV_INDEX_ALLIANDER_USERNAME="$(whoami)"
export UV_INDEX_ALLIANDER_PASSWORD="<your artifactory token>"
```

Or, for the whole machine, in `~/.config/uv/uv.toml`:

```toml
[[index]]
name = "alliander"
url = "https://artifactory.alliander.com/artifactory/api/pypi/pypi-virtual/simple/"
default = true
```

## Lockfile and install discipline

- `uv.lock` is committed. Always install with `uv sync --frozen` (this is what `just setup` does).
- Never run `uv sync --upgrade` or `uv pip install <pkg>` on a managed device unless the resolved version comes from Artifactory.
- After adding or upgrading a dependency, run `uv lock` once and review the diff before keeping the change.

## Verifying the install actually came from Artifactory

```sh
cd python-app
uv pip list --verbose | grep -i 'fastapi\|index'
```

If you see `pypi.org` in the index column, your Artifactory configuration is not active for that environment.

## Confirm the URL with your platform team

The Artifactory URL above is illustrative. Confirm the canonical `pypi-virtual` (and `npm-virtual`, if relevant) endpoints for your tenant with the platform team before sharing this with participants.
