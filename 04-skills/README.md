# Skills

**Builds on:** chapter 03 (skills vs instructions: rich workflows vs persistent rules).

## Where Skill Directories Must Live

For Copilot to discover a skill in-IDE, the skill directory must sit in one of these locations (per the [VS Code Agent Skills docs](https://code.visualstudio.com/docs/agent-customization/agent-skills)):

- **Project skills:** `.github/skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, or `.agents/skills/<name>/SKILL.md`
- **Personal skills:** `~/.copilot/skills/<name>/SKILL.md`, `~/.claude/skills/<name>/SKILL.md`, or `~/.agents/skills/<name>/SKILL.md`

The parent directory name **must match** the `name` field in the SKILL.md frontmatter, otherwise the skill silently fails to load.

The example in [examples/api-endpoint-skill/](examples/api-endpoint-skill) is a **template**. Copy the whole directory into `.github/skills/api-endpoint-skill/` before running the assignments.

> **Supply-chain warning.** A skill can carry scripts and tell Copilot to run them. Treat skills from any source you did not write as untrusted code: read the SKILL.md *and* every file it references before placing the directory in `.github/skills/`.

## What Skills Are Good For

Skills are useful when the assistant should recognize a particular kind of work and bring in richer, task-shaped guidance only when it is relevant.

That makes skills a better fit than instructions when you need:

- a repeatable workflow
- examples or supporting material tied to that workflow
- context that should activate only in a narrow problem area
- behavior that is more specific than a repo-wide rule

In this repository, a good candidate is FastAPI endpoint work that spans route shape, response models, and endpoint tests. The example skill in [examples/api-endpoint-skill/SKILL.md](examples/api-endpoint-skill/SKILL.md) is a good fit because it does more than state rules. It tells the assistant to inspect the route, find the related service and DTOs, keep SQL out of the route, extend endpoint tests, and validate the change. That is the difference between a rule and richer, task-shaped guidance.

## Skills Versus Instructions

You can use both skills and custom instructions to teach Copilot how to work in your repository and how to perform specific tasks.

We recommend using custom instructions for simple instructions relevant to almost every task (for example information about your repository's coding standards), and skills for more detailed instructions that Copilot should only access when relevant.

## How Skill Activation Should Be Understood

When performing tasks, Copilot will decide when to use your skills based on your prompt and the skill's description.

When Copilot chooses to use a skill, the SKILL.md file will be injected in the agent's context, giving the agent access to your instructions. It can then follow those instructions and use any scripts or examples you may have included in the skill's directory.

For Copilot code review on GitHub, keep the following in mind:
- If you want to ensure that Copilot code review will read and use a skill, use a review-focused skill directory name such as code-review.
- Existing skills within the .github/skills directory can also be used by Copilot code review automatically when they are relevant to the review.

## What Good Skills Look Like

Good skills are:

- narrow enough to activate for the right work
- rich enough to be more useful than a single sentence of instruction
- concrete enough that activation can be tested and explained

Good skill descriptions focus on the job to be done, not on the entire repository identity. A skill aimed at "adding or revising FastAPI endpoints, response models, and API tests" is much stronger than a skill that says "help with Python in this project."

## What Skills Can Package

One of the main advantages of skills is that they can carry more than plain advice.

A skill can package things like:

- a suggested workflow for the task (ex. if you change the db model, recreate a schema file)
- concrete file locations to inspect or update (ex. a specific README somewhere)
- examples that show the expected shape of the result
- command or validation sequences to run at the end
- supporting material such as snippets, schemas, or scripts

That last point is especially useful. A skill can bring in a script or other helper file that is only relevant for a certain class of work, instead of forcing that material into a global instruction file. For example, a testing skill might include a validation script, or a deployment skill might include a checked-in command sequence that should only appear for release tasks.

This is what makes skills feel powerful in practice. They let you package a small task kit: what kind of request this is, which files matter, what steps usually follow, and what supporting assets help complete the job.

That is why skills are a good fit for workflows that need more than one rule. They can carry procedure, examples, and artifacts together, while still staying scoped to the kind of work where that extra context is worth the cost.

