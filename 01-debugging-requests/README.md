# Debugging Requests

## What It Is

VS Code provides two complementary debugging surfaces for Copilot interactions:

- the Chat Debug view for the raw request and response payloads
- the Agent Debug Logs panel for session-level orchestration, token usage, timing, cache behavior, and tool activity

For advanced users, this chapter is not about "how to troubleshoot when something feels off." It is about learning to treat Copilot as an inspectable system.

## Chat Debug View Versus Agent Debug Logs

These two surfaces answer different questions.

### Chat Debug View

Use the Chat Debug view when the unit you care about is one model interaction.

It is the right tool when you want to inspect:

- the exact system prompt for a request
- the exact user prompt that was sent
- which context items were attached
- which tool payloads were sent or returned for that request
- how the final response maps back to that specific request

In short: Chat Debug View is request-centric.

### Agent Debug Logs

Use Agent Debug Logs when the unit you care about is the full session or orchestration flow.

It is the right tool when you want to inspect:

- which tools were called across the session
- how many model turns were made
- token usage and overall duration
- cache hits and cache misses across turns
- discovery events such as prompt or customization loading
- how subagents or multi-step orchestration behaved over time

In short: Agent Debug Logs is session-centric.

### Practical Distinction

If your question is "What exactly was in this prompt?" use Chat Debug View.

If your question is "What happened across this run, why did it take this long, and where did tokens go?" use Agent Debug Logs.

If your question is "Why did this one answer look wrong?" start with Chat Debug View.

If your question is "Why is this workflow expensive, slow, or behaving differently across turns?" start with Agent Debug Logs.

## When To Use It

Use request debugging when:

- you want to know what was actually sent to the model
- a response quality change might be caused by context drift rather than model quality
- the wrong files seem to influence the answer
- you want to understand token consumption, latency, or cache misses
- you want to know why a tool was or was not available
- you want evidence for how `Ask`, `Agent`, and `Plan` differ in practice

## How It Works

The request sent to the model is assembled from several building blocks, including:

- your current request
- conversation history
- open files and selections
- instructions
- tools and model metadata
- other context gathered by the editor

The important point is that Copilot behavior is not just a function of the text you typed. It is a function of the entire constructed request.

The Chat Debug view helps you inspect that constructed request directly. The Agent Debug Logs panel helps you inspect the larger session behavior around it.

## How To Open The Debug Views

### Chat Debug View

According to the VS Code documentation, you can open the Chat Debug view in either of these ways:

1. Open the Chat view.
2. Select the overflow menu in the Chat view.
3. Choose `Show Chat Debug View`.

Or:

1. Open the Command Palette.
2. Run `Developer: Show Chat Debug View`.

Official screenshot from the VS Code docs:

![Official VS Code Chat Debug view screenshot](https://code.visualstudio.com/assets/docs/agents/chat-debug-view/chat-debug-view.png)

### Agent Debug Logs

For session-level investigation, open the Agent Debug Logs panel:

1. Enable `github.copilot.chat.agentDebugLog.fileLogging.enabled`.
2. Open the Chat view.
3. Select the overflow menu.
4. Choose `Show Agent Debug Logs`.

You can also run `Developer: Open Agent Debug Logs` from the Command Palette.

Official screenshot from the VS Code docs:

![Official VS Code Agent Debug Logs summary screenshot](https://code.visualstudio.com/assets/docs/agents/chat-debug-view/agent-logs-summary-v3.png)

## What To Read In The Debug Output

The Chat Debug view is useful when you need the exact shape of one request. In practice, the most useful sections are:

- `System prompt`
- `User prompt`
- `Context`
- `Tool responses`
- `Response`

For this course, the key habit is comparison. One request in isolation is informative. Two nearby requests with one meaningful difference are far more informative.

The Agent Debug Logs panel answers a different class of questions. Its most useful views are:

- `Summary` for aggregate token usage, duration, and error counts
- `Logs` for the chronological event stream
- `Cache Explorer` for prompt-cache reuse and divergence
- `Agent Flow Chart` for multi-step or subagent orchestration

This is the operational difference:

- Chat Debug View explains one request deeply.
- Agent Debug Logs explains one session broadly.

## Token Consumption

Token consumption is not just a billing or performance concern. It also affects response quality.

Things to watch:

- whether the context included more files than the task needed
- whether repeated turns are getting prompt-cache reuse
- whether the request shape changed enough to break caching
- whether long conversations are pushing important context out of the request window

The Agent Debug Logs Summary view exposes aggregate token usage and duration. The Cache Explorer helps compare consecutive model turns and identify where the request prefix diverged.

This matters because a low cache hit rate can increase latency and token cost, and an overloaded context can lead to weaker or truncated responses.

## Cool

- You can explain Copilot behavior with evidence instead of intuition.
- You can inspect the actual building blocks of a request.
- You can reason about token cost, cache reuse, and context pressure.
- You can validate hypotheses about mode differences, instruction loading, and tool availability.

## Not Cool

- Debug output can be noisy.
- Logs may contain sensitive project context and should be reviewed before sharing.
- It is easy to over-focus on raw payloads without connecting them back to task quality.
- Some important orchestration behavior is only partly visible, so you still need to separate evidence from inference.

