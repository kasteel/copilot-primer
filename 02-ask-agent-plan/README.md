# Ask, Agent, And Plan

## What It Is

`Ask`, `Agent`, and `Plan` are not just three tones of the same interaction. They express different operating contracts between the user, the model, the editor, and the tool system.

For an advanced user, the interesting question is not only "when should I click which mode?" but also "what changes under the hood when I do?"

## Working Hypothesis

The safest assumption is that mode selection changes more than presentation. In practice, the mode likely affects some combination of:

- the system or orchestration prompt
- what the model is instructed to optimize for
- whether tool use and editing are expected or suppressed
- how much of the answer is expected to be plan-shaped versus action-shaped
- how the UI and backend interpret the result

You should not teach this as folklore. You should verify it through request debugging.

## Likely Behavioral Differences

### Ask

`Ask` appears to optimize for explanation, comparison, and bounded help. The model is usually being asked to respond directly rather than to operate on the workspace autonomously.

Typical characteristics:

- answer-first behavior
- narrower action expectation
- lower need for orchestration scaffolding
- useful when you want judgment without handing over execution

### Agent

`Agent` appears to optimize for delegated execution. The model is expected to inspect files, decide on edits, validate them, and keep moving until the task is complete.

Typical characteristics:

- stronger bias toward tool use and file changes
- larger execution surface
- explicit or implicit validation loop
- better fit for multi-file implementation and repair

### Plan

`Plan` appears to optimize for structured intent before execution. It is useful when you want Copilot to externalize sequencing, assumptions, risks, and validation before edits happen.

Typical characteristics:

- decomposition before action
- clearer dependency ordering
- better surfacing of assumptions and missing context
- useful before broad or risky changes, but not because it magically increases context size

## Under The Hood: What To Investigate

You should assume that some differences are visible in the debug trace and some are not.

Visible candidates:

- the final message shape
- tool declarations or tool availability
- request options
- explicit planning language added to the prompt
- whether prior context is framed as implementation work or analysis work

Less directly visible candidates:

- backend routing logic
- policy or orchestration layers outside the raw user-visible prompt
- mode-specific post-processing of model output

This is why chapter 1 is request debugging. Debugging is the evidence layer for this chapter.

## Context Considerations

Mode choice does not replace context discipline.

Important points:

- `Plan` is not automatically better because the task is large. It is better when the main problem is sequencing, ambiguity, or risk.
- `Agent` is not automatically better because the task is executable. It is better when the surrounding context is good enough for safe autonomous work.
- `Ask` is often better than both when the main task is architectural judgment, API design discussion, or identifying the right abstraction boundary.

For larger changes, `Plan` can be valuable because it gives the model a structured scaffold to work from later, but that benefit comes from explicit decomposition, not from a special "large task context mode."

## Cool And Not Cool

### Ask

Cool:

- low commitment
- good for comparison and critique
- easier to challenge point by point

Not cool:

- can stall if you really needed action
- may produce good advice that never gets converted into concrete edits

### Agent

Cool:

- strongest fit for end-to-end change execution
- useful for validation loops and file coordination
- efficient when the target behavior is already clear

Not cool:

- can widen scope too quickly
- can confidently operationalize a bad assumption
- benefits most from explicit guardrails and good local context

### Plan

Cool:

- exposes assumptions early
- useful for larger or riskier change sets
- gives you a reviewable scaffold before code is touched

Not cool:

- can become performative if the task is already obvious
- may create a false sense of precision if the plan is not grounded in actual repository context

## Project-Specific Examples

In this repository:

- use `Ask` to compare whether a new architectural rule belongs in `03-instructions` or `05-hooks`
- use `Plan` before changing the shared FastAPI app across routes, services, repositories, and tests
- use `Agent` when implementing that approved change across `python-app/`

## What To Teach Your Students

Do not teach mode selection as a soft preference. Teach it as an engineering choice about orchestration.

The right questions are:

- Do I need explanation, execution, or decomposition?
- Is the main risk misunderstanding the task, or carrying out the task badly?
- Do I need a plan because the change is large, or because the dependencies are unclear?
- What does the debug trace show is actually different between these modes?

## Tips

- Start in `Ask` when you want judgment.
- Start in `Plan` when you need structure, tradeoffs, or dependency ordering.
- Start in `Agent` when the task is already concrete and you want execution.
- When in doubt, compare the constructed requests for the same task across all three modes instead of arguing from intuition.
