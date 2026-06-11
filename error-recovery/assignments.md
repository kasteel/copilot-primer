# Assignments

## Assignment 1: Recover From A Broken Query Limit

Goal: repair a small behavioral defect without restarting the task.

Embedded patch to apply:

```diff
-    safe_limit = max(1, min(limit, 20))
+    safe_limit = limit
```

Tasks:

1. Apply the patch to the relevant service.
2. Observe the broken behavior or missing guardrail.
3. Ask Copilot to repair the issue using the failing expectation as context.
4. Re-run the same validation.

## Assignment 2: Recover From A Layering Mistake

Goal: steer Copilot away from an architectural regression.

Embedded patch to apply:

```diff
-        return [RecentOrder.model_validate(row) for row in self.repository.list_recent_orders(safe_limit)]
+        from app.db.connection import open_connection
```

Tasks:

1. Apply the patch and explain why it violates the architecture.
2. Ask Copilot to repair the code without moving SQL out of the repository layer.
3. Validate the fix.

Expected observations:

- Better recovery prompts refer to the exact defect.
- Validation should stay focused on the broken slice.
