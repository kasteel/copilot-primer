# Assignments

> **Working in pairs.** Each assignment is designed for a pair. You do not need to write down every observation. Discuss with your partner and capture **2–3 take-aways** per assignment that you would share with the rest of the team.

## Assignment 1: Recover From A Broken Query Limit

Goal: repair a small behavioral defect without restarting the entire task.

Embedded patch to apply:

```diff
-    safe_limit = max(1, min(limit, 20))
+    safe_limit = limit
```

Tasks:

1. Apply the patch to the relevant service.
2. Identify the exact behavior or guardrail that is now broken.
3. Ask Copilot to repair the issue using the failing behavior as the primary signal.
4. Re-run the same validation after the repair.
5. Record whether the first repair was narrow or whether it widened the change unnecessarily.

Discuss with your pair and capture **2–3 take-aways**. Useful prompts:

- what defect you described to Copilot
- what constraint had to remain true
- whether the repair fixed the exact issue without drift

Expected outcome:

- You should end with a repair prompt that is specific enough to target one behavior rather than reopen the whole implementation.

## Assignment 2: Recover From A Layering Mistake

Goal: steer Copilot back to the correct architecture after a plausible but invalid change.

Embedded patch to apply:

```diff
-        return [RecentOrder.model_validate(row) for row in self.repository.list_recent_orders(safe_limit)]
+        from app.db.connection import open_connection
```

Tasks:

1. Apply the patch.
2. Explain why the change violates the route, service, and repository separation used in this repo.
3. Ask Copilot to repair the defect while preserving the architectural boundary.
4. Validate the repair.
5. Compare the quality of the result when the prompt names the violated boundary explicitly versus when it only says the code is wrong.

Expected insight:

- Strong recovery prompts identify the violated architectural rule, not just the existence of a bug.
