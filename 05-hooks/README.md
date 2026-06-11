# Hooks

## What Hooks Are Good For

Hooks are appropriate when you need the system to actually run something, not merely remember something.

Good hook use cases include:

- running lint or format checks after edits
- enforcing a validation step before accepting changes
- blocking obviously dangerous operations
- making a repeatable guardrail visible to the team

This is the key conceptual difference from instructions and skills:

- instructions shape behavior
- skills package workflows
- hooks execute deterministic automation

## Why Senior Developers Should Care

Hooks are not just a convenience feature. They are a way to close the gap between AI-generated code and the repository's actual quality contract.

If your team says "all Python edits should pass Ruff" and nothing actually runs Ruff, that rule is aspirational.

Once a hook runs the check, the workflow becomes operational rather than rhetorical.

## How To Think About Hook Design

Good hooks are:

- narrow in scope
- obvious in effect
- cheap enough to run regularly
- tied to a clear quality or safety outcome

Bad hooks are:

- too broad
- too slow
- too surprising
- too complicated to debug

The fastest way to make a hook unpopular is to let it fire constantly for marginal value.

## Instructions Versus Hooks

This is a distinction worth teaching explicitly.

If the desired behavior is "please prefer Ruff," that is instruction-shaped.

If the desired behavior is "run Ruff after relevant edits," that is hook-shaped.

One steers. The other enforces.

Teams often need both:

- instructions to bias the model toward good behavior
- hooks to catch the cases where guidance was ignored or insufficient

## Failure Modes

Common hook failure modes include:

- triggering too often
- running an expensive command for a tiny change
- producing noisy output with little actionability
- making the workflow feel hostile rather than informative

The teaching point is not "hooks are powerful." The teaching point is "hooks are a tradeoff between enforcement value and workflow friction."

