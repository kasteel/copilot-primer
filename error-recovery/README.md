# Error Recovery

## What It Is

Error recovery is the ability to steer Copilot back on track after it produces the wrong implementation, wrong test, or wrong architectural move.

## When To Use It

Use error recovery when Copilot:

- puts SQL in the wrong layer
- writes weak tests
- misses an await or other control-flow detail
- breaks a route or response shape

## How It Works

The fastest recovery loop is usually:

1. observe the failure
2. narrow the defect
3. redirect Copilot with the smallest useful correction
4. rerun validation

## Advantages

- Builds confidence in working with AI output.
- Keeps progress moving without restarting.
- Turns failures into usable signal.

## Disadvantages

- Requires discipline around validation.
- It is easy to over-correct with a broad new prompt.
- If the failure source is unclear, the next prompt can drift.

## Project-Specific Example

This chapter uses embedded patches against the shared FastAPI app so learners can apply a small fault, observe the failure, and then guide Copilot back to a correct implementation.

## Tips

- Use the smallest failing example you can.
- Point at the concrete defect, not a general feeling.
- Re-run the same check after the repair.
