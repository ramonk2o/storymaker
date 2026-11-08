# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### Slide roles in a training without a lesson file
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) on a training deck with no lesson file couldn't tell whether each slide's role and the `[question]` mark, stated under "When the lesson skill did the content", apply to it.
- **Description:** The training case says whether a training without a lesson file names each slide's role.

### The description and the body name the lesson condition differently
- **Type:** Debt
- **Motivation:** A consistency audit of the lesson-to-deck path (2026-11-08) found the description says "when the lesson skill exists" while the body says "when the session can load the lesson skill"; it was left out of that change because a description change needs the trigger suite.
- **Description:** The description uses the body's wording, at the next description change that runs the trigger suite.

## lesson

### What happens to a `(hypothesis)` mistake at and after the gate
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) on the light path, with the Opening silent on what learners get wrong, marked each module's mistake `(hypothesis)` as the skill now says, but couldn't tell whether approving the map drops the mark, or what to do when the user rejects a mistake the sample module's Watch out block and hinge answers rest on.
- **Description:** The light path says what the gate does with a hypothesis mistake: approval confirms it and drops the mark, and a rejected one changes the map, and the sample module with it, before approval. The SKILL.md is at its size limit, so this needs an equal cut.
