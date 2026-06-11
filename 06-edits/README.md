# Edits

## When Edits Are The Right Tool

Use Edits when the change is inherently coordinated across layers, such as:

- route plus service plus repository
- DTO plus serialization plus tests
- naming changes that cross API and test boundaries
- response shape changes that require one consistent contract update

Do not use Edits just because a task is large. Use it when the work has a shared intent that benefits from being reviewed as one unit.

## What Edits Change About The Workflow

Edits change the review surface.

Instead of evaluating isolated one-file suggestions, you evaluate whether the whole chain of consequences has been handled:

- was the route updated
- was the service mapping updated
- was the repository query updated
- were tests updated
- does the new contract remain coherent end to end

This is why Edits pair naturally with validation. The broader the coordinated change, the less acceptable it is to review lazily.

## Why Senior Developers Should Care

Senior developers usually do not need help typing one local patch. They need help maintaining consistency across several architectural layers without dropping one link in the chain.

That is exactly where Edits can be valuable.

But the tradeoff is real: once several files move together, weak review habits become much more dangerous.

## Failure Modes

The common failure modes are:

- the change spreads farther than necessary
- one architectural layer is updated but another is missed
- the diff looks coherent at a glance but the contract is still inconsistent
- the user reviews the changes file by file and misses the end-to-end behavior

The correct response is not to avoid Edits. The correct response is to define the requested change narrowly and validate the result immediately.

## Good Edit Requests

Good edit requests are:

- small enough to review as a unit
- explicit about the desired contract change
- explicit about which layers are expected to move
- paired with a validation expectation

For example, "add one response field to `/orders/recent` and update route, service, repository, and tests" is a good Edits request.

"Refactor the order system" is not.

