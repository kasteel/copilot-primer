# Before You Start

Read this once before opening chapter 01. It covers two things you cannot pick up from the chapter material on its own:

1. Which files you must keep **local** and never push, and why.
2. How the workshop expects you to work in pairs.

---

## Local-only files (do not commit, do not push)

Throughout the course you will create files that customize Copilot's behavior:

- skills under `.github/skills/`
- hooks under `.github/hooks/`
- agent customization files under `.claude/` or `.agents/`
- VS Code workspace files under `.vscode/` (`settings.json`, `tasks.json`, `mcp.json`, …)

**Create them locally. Do not push them.**

We have a restriction on adding the categories of files that are related to the recent incident — for example `.claude/settings.json`, `.vscode/tasks.json`, and the other paths listed above. A ruleset on the remote already blocks pushes that touch them, so nothing "bad" can happen if you forget. But every blocked push triggers alerting at security, and we want to keep the false-positive rate low. So: please do not try.

The repo's `.gitignore` is set up to keep these directories out of `git status`. If you ever see one of them appear in `git status`, that is a signal that something escaped the ignore list — check before staging anything else.

If you want a record of what you built during an exercise, share via the ODS techies Teams Channel.

---

## Working in groups

The assignments can be completed in groups of two or more colleagues. You do not need to write down every observation. Write down the take-aways from the discussion with your partner to share with the rest of the devs. The assignment files state this explicitly per exercise. If `uv` is not working on your device due to the security incident, work together with somebody who can run `just doctor` (instructions below) succesfully.

## Environment check

Before starting chapter 01, run:

```sh
just doctor
```

This verifies `uv`, `just`, `python3`, and the VS Code CLI. Fix anything reported as MISSING before you start.

## Authenticate to Artifactory (before installing)

All Python dependencies are installed through the internal Alliander JFrog Artifactory mirror — never public PyPI. The index is already configured as the default in `python-app/pyproject.toml`, so you do not need to edit anything. You do need to authenticate before running `just setup`, using a personal JFrog **Identity Token**. Follow the official Alliander guides:

- [Configuration tutorial (CLOUD space)](https://alliander.atlassian.net/wiki/spaces/CLOUD/pages/3796762841/Configuration+tutorial) — request the Artifactory role via SID, generate the Identity Token, and run the JFrog “Set Me Up” wizard for the **pypi-all** repository with **UV** selected as the client.
- [Artifactory configureren (JFrog) (OMEGA space)](https://alliander.atlassian.net/wiki/spaces/OMEGA/pages/3867574555/Artifactory+configureren+JFrog) — short checklist version, including the `UV_INDEX_*` shell exports.

See [docs/registry.md](docs/registry.md) for how this maps onto the `alliander` index in this repo and how to verify an install actually came from Artifactory. If `just setup` fails to resolve packages, your authentication is not active in the current shell.

Then install dependencies and bootstrap the database:

```sh
just setup
just bootstrap
```

You are ready when `just test` is green.