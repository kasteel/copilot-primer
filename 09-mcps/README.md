# MCPs

## What It Is

Model Context Protocol lets Copilot interact with external tools and data sources through a standard interface.

## When To Use It

Use an MCP when Copilot needs controlled access to something outside the normal editor context, such as a database or service.

## How It Works

For this course, the MCP example is a local, read-only SQLite server connected to the same database used by the FastAPI application.

## Cool

- Connects Copilot to real project data.
- Makes tool boundaries explicit.
- Good for controlled automation and richer context.

## Not Cool

- Requires careful guardrails.
- Tool exposure should be deliberate.
- A bad MCP design can widen risk too much.

## Project-Specific Example

The MCP chapter uses the bootstrapped SQLite database from `python-app` and exposes safe read-only operations such as listing tables, describing schema, and running safe queries.

## Tips

- Keep the database connection read-only.
- Validate input before execution.
- Limit result size and block multi-statement SQL.
