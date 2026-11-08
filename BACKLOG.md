# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### The description and the body name the lesson condition differently
- **Type:** Debt
- **Motivation:** A consistency audit of the lesson-to-deck path (2026-11-08) found the description says "when the lesson skill exists" while the body says "when the session can load the lesson skill"; it was left out of that change because a description change needs the trigger suite.
- **Description:** The description uses the body's wording, at the next description change that runs the trigger suite.

## lesson

### The user's topic order: decision or hypothesis
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) received topics in an order that reversed their dependencies and reordered them into a staircase, deducing it from "you propose, the user adjusts"; nothing says whether a topic order the user brings is theirs to keep.
- **Description:** When the dependencies call for it, the skill reorders the user's topics as a labeled proposal with the reason, for the user to confirm.
