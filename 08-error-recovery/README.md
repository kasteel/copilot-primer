# Error Recovery

## What Error Recovery Really Is

Error recovery is the practice of steering Copilot back onto the correct path after a local failure, such as:

- a boundary violation
- a broken test
- a missed edge case
- an invalid assumption about the code path
- a superficially plausible but wrong implementation

The goal is not to restart from zero. The goal is to use the failure as information.

## The Recovery Loop

The most reliable recovery loop is:

1. observe the failure concretely
2. narrow the defect to one slice
3. tell Copilot what is wrong and what must remain true
4. rerun the same focused validation

That last step matters. If you change the validation too, you lose the ability to prove that the repair actually addressed the defect.

## Why Recovery Often Fails

Recovery usually fails for one of three reasons.

The prompt is too broad:

- "this does not look right" is weak signal
- the model may rewrite unrelated code instead of fixing the defect

The defect is not localized:

- the user has not identified the actual failing boundary or behavior
- the assistant is forced to guess where the real problem lives

The validation changes midstream:

- the original failure is never retested
- the team cannot tell whether the fix addressed the same bug

Senior engineers should teach recovery as a controlled debugging loop, not as a second attempt at prompting.

## Good Recovery Prompts

Good recovery prompts usually contain:

- the observed failure
- the exact boundary that was violated
- the constraint that must remain true
- the narrowest useful target for the repair

Examples of strong recovery framing:

- the repository layer must continue to own SQL
- rerun the same failing test after the repair
- keep the response contract unchanged except for the bug fix

That kind of prompt gives the model a defect description rather than a vague dissatisfaction signal.

## Project-Specific Reading

This repository is a good fit for error recovery exercises because the architecture is explicit enough that learners can tell when Copilot moves logic into the wrong layer or breaks a testable contract.

That clarity makes recovery teachable. Students can see what was wrong, what constraint mattered, and whether the repair respected the architecture.

