# Ask, Agent, And Plan

## Core Mental Model

The useful simplification is:

- `Ask` optimizes for explanation and bounded reasoning
- `Plan` optimizes for decomposition, sequencing, and surfacing assumptions before execution
- `Agent` optimizes for delegated execution across the workspace with tools, edits, and validation

That simplification is good enough to work with, but it is still incomplete. Each mode changes multiple things at once:

- what the system wants the model to produce
- how strongly tool use is encouraged or suppressed
- whether edits are part of the expected outcome
- how much structure the response is pushed toward
- how the UI interprets and presents the result

Mode selection is therefore an orchestration decision. It changes the shape of the collaboration, not just the wording of the answer.

## Ask

`Ask` is usually the lowest-delegation path. It is strongest when the primary need is judgment rather than action.

Typical signals that `Ask` is the right choice:

- you want a comparison between two designs
- you want critique before implementation
- you want help understanding a local code path
- you suspect the task is under-specified and you do not want the model to operationalize assumptions yet

What tends to be good about `Ask`:

- it keeps the conversation narrower
- it is easier to challenge and redirect
- it is well suited to architecture review, naming, boundary decisions, and test strategy discussion

What tends to go wrong with `Ask`:

- it can stop one step short of useful execution
- it can produce high-quality reasoning that never becomes code
- users sometimes keep asking follow-up questions when the task has already crossed the line into implementation work

The failure mode is not that `Ask` is weak. The failure mode is that the user keeps the task in analysis mode after the main uncertainty has already been removed.

## Agent

`Agent` is the highest-delegation path in this course. It is the mode where Copilot is most likely to inspect files, call tools, change code, validate its own changes, and continue iterating.

Typical signals that `Agent` is the right choice:

- the target behavior is already clear
- the change spans multiple files or layers
- you want the assistant to execute, not merely advise
- there is a natural validation loop after the change

What tends to be good about `Agent`:

- it reduces the mechanical burden of multi-file work
- it is useful for repairs, refactors, and coordinated edits
- it can compress several boring implementation steps into one reviewed operation

What tends to go wrong with `Agent`:

- it can widen scope based on a weak assumption
- it can keep moving even when the original task definition was flawed
- it rewards vague prompts less than users expect

The failure mode is usually not "the model did something random." The failure mode is that the user delegated execution before the problem statement was precise enough.

## Plan

`Plan` is most useful when the problem is not code generation itself but uncertainty around sequencing, scope, or dependency ordering.

Typical signals that `Plan` is the right choice:

- the task touches several layers and you want the change decomposed first
- there are tradeoffs that should be surfaced before editing
- you want assumptions and risks written down explicitly
- you want a reviewable execution scaffold before granting autonomy

What tends to be good about `Plan`:

- it externalizes hidden assumptions early
- it often narrows later implementation work
- it gives you a concrete artifact to challenge before code changes happen

What tends to go wrong with `Plan`:

- it can become ceremonial for obvious tasks
- it can produce a polished but shallow sequence if the repository context is weak
- users sometimes treat the existence of a plan as proof that the plan is correct

The failure mode is not overthinking. The failure mode is mistaking structure for truth.

## What Probably Changes Under The Hood

Some differences are visible. Some are only inferable.

Things you can often investigate directly:

- message framing in the constructed request
- whether the request is shaped toward reasoning, planning, or execution
- whether tools are declared or expected differently
- whether the response is being pushed toward a plan artifact or an action artifact

Things you may only infer indirectly:

- backend routing
- orchestration policies outside the visible prompt
- mode-specific post-processing or validation behavior

The important teaching point is not to pretend you can see everything. The important point is to separate what the debug trace proves from what your team currently believes.

## Mode Choice And Context Discipline

Mode choice does not compensate for poor context.

Important distinctions:

- `Plan` is not better because a task is large. It is better when the task is ambiguous, risky, or structurally dependent.
- `Agent` is not better because a task is executable. It is better when the objective is clear enough to delegate safely.
- `Ask` is not just for beginners. It is often the best mode for senior work such as architectural critique, abstraction review, and failure analysis.

For experienced engineers, the real question is usually: what is the dominant risk right now?

- if the dominant risk is choosing the wrong direction, start with `Ask`
- if the dominant risk is sequencing the work badly, start with `Plan`
- if the dominant risk is mechanical implementation effort, start with `Agent`

