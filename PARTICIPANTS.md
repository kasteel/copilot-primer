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

The assignments can be completed in groups of two or more colleagues. You do not need to write down every observation. Write down the take-aways from the discussion with your partner to share with the rest of the devs. The assignment files state this explicitly per exercise.

## Environment check

Before starting chapter 01, run:

```sh
just doctor
```

This verifies `uv`, `just`, `python3`, the VS Code CLI, and the Copilot extension. Fix anything reported as MISSING before you start.

Then install dependencies and bootstrap the database:

```sh
just setup
just bootstrap
```

You are ready when `just test` is green.
