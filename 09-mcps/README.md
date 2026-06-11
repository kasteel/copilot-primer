# MCPs

## What An MCP Is Good For

Model Context Protocol is useful when Copilot needs controlled access to something outside the default workspace context, such as:

- a database
- a service
- a local tool
- a restricted operational surface

The keyword is controlled. The value of an MCP is not merely that it exposes capabilities. The value is that it exposes them through a deliberate boundary.

## Why Guardrails Matter So Much

An MCP is an expansion of what the assistant can do.

That means every design choice matters:

- what tools are exposed
- what inputs are accepted
- what outputs are returned
- what operations are forbidden
- how much data can flow through the interface

The right question is not "can Copilot reach the database?" The right question is "what is the safest interface that still solves the use case?"

## Project-Specific Reading

This repository uses a local read-only SQLite MCP against the same bootstrapped database that powers the FastAPI application.

That is a good teaching design because:

- the data is real enough to be useful
- the interface can be small and concrete
- read-only constraints are easy to reason about
- students can see that MCP value comes from design, not from unlimited access

## What Good MCP Design Looks Like

Good MCP design is:

- purpose-built
- narrow
- explicit about allowed operations
- defensive about inputs and outputs

For a database-oriented MCP in this repo, that usually means:

- read-only access
- schema discovery tools with limited scope
- query tools with validation
- result-size limits
- multi-statement blocking

That is enough to be useful without turning the tool into a general database shell.

## Common Failure Modes

The common failures are predictable.

Too much surface area:

- too many tools
- overly generic query power
- insufficient limits on data returned

Too little validation:

- destructive patterns are not blocked
- inputs are not constrained
- the read-only story is based on trust rather than design

Too little purpose:

- the MCP exists because it is interesting, not because it solves a real workflow problem

The right lesson for advanced users is that MCP usefulness and MCP restraint should grow together.

