# Package Registry (Artifactory)

All `uv` installs in this primer are routed through the internal Alliander JFrog Artifactory mirror. The index is already configured as the default in `python-app/pyproject.toml`, so `just setup` pulls from Artifactory out of the box — you only need to authenticate (below).

## The configured index

`python-app/pyproject.toml` already contains:

```toml
[[tool.uv.index]]
name = "allianderartifactory"
url = "https://alliander.jfrog.io/artifactory/api/pypi/pypi-all/simple/"
default = true
```

You do not need to add this yourself. If you prefer a machine-wide setting instead, you can mirror it in `~/.config/uv/uv.toml` (see below).

## Authenticate

Authentication uses a personal JFrog **Identity Token** (generated from your profile in the Artifactory UI), not your normal password. Follow the official Alliander setup guides rather than copying credentials by hand:

- [Configuration tutorial](https://alliander.atlassian.net/wiki/spaces/CLOUD/pages/3796762841/Configuration+tutorial) — request the Artifactory role via SID, generate the Identity Token, then run the JFrog “Set Me Up” wizard. Select the **pypi-all** repository and **UV** as the client (it defaults to Poetry).
- [Artifactory configureren (JFrog)](https://alliander.atlassian.net/wiki/spaces/OMEGA/pages/3867574555/Artifactory+configureren+JFrog) — short checklist version, including the `UV_INDEX_*` environment-variable exports to put in your shell profile.

The index in `python-app/pyproject.toml` is named `allianderartifactory`, which lines up with the `UV_INDEX_*` exports in the OMEGA guide. Put these in your shell profile (`.bashrc` / `.zshrc`) with your own username and Identity Token:

```sh
export UV_INDEX_ALLIANDERARTIFACTORY_USERNAME=al#####
export UV_INDEX_ALLIANDERARTIFACTORY_PASSWORD=<your identity token>
```

Alternatively, set `UV_INDEX_URL` with embedded credentials as shown in the Configuration tutorial.

For a machine-wide index definition instead of the per-project one, mirror it in `~/.config/uv/uv.toml`:

```toml
[[index]]
name = "allianderartifactory"
url = "https://alliander.jfrog.io/artifactory/api/pypi/pypi-all/simple/"
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

If you see `pypi.org` in the index column, your Artifactory configuration is not active for that environment — check that the `[[tool.uv.index]]` block is present and that your Identity Token / `UV_INDEX_*` credentials are configured in the current shell (see the guides linked under [Authenticate](#authenticate)).
