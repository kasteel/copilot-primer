# Debugging Requests

## What It Is

VS Code provides debugging views and logs that let you inspect what GitHub Copilot actually sent and received. This is useful when behavior looks surprising or inconsistent.

## When To Use It

Use request debugging when:

- instructions seem to be ignored
- a skill activates unexpectedly or fails to activate
- the wrong files appear to influence the answer
- you want to understand why a tool was or was not available

## How It Works

The prompt sent to the model is assembled from several sources, including:

- your current request
- conversation history
- open files and selections
- instructions
- tools and model metadata
- other context gathered by the editor

The debug view helps you inspect the final request instead of guessing.

## Advantages

- You can explain Copilot behavior with evidence.
- You can verify whether instructions or skills were actually included.
- You can teach better prompting and better repo configuration.

## Disadvantages

- Debug output can be noisy.
- Logs may contain sensitive project context and should be reviewed before sharing.
- It is easy to over-focus on raw logs without connecting them back to the user task.

## Project-Specific Example

In this repository, compare a request made while editing `python-app/app/api/orders.py` with one made while editing `python-app/app/repositories/order_repository.py`. The difference is useful when you want to see why an API-focused skill should activate in one place but not the other.

## Tips

- Use request debugging to confirm, not just speculate.
- Compare two similar requests with one meaningful variable changed.
- Review logs before exporting or sharing them.
