# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### The description and the body name the lesson condition differently
- **Type:** Debt
- **Motivation:** A consistency audit of the lesson-to-deck path (2026-11-08) found the description says "when the lesson skill exists" while the body says "when the session can load the lesson skill"; it was left out of that change because a description change needs the trigger suite.
- **Description:** The description uses the body's wording, at the next description change that runs the trigger suite.
