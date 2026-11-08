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

### Where the light path gets the learners' mistakes
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) on the light path saw that 1.1 asks the user for the mistakes learners make, while the light path starts at 1.2, and couldn't tell whether to propose the mistakes as hypotheses or leave them `[TO CONFIRM]`.
- **Description:** The light path says where the mistakes each module tackles come from.
