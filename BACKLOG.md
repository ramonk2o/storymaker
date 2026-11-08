# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### A loose lesson file doesn't always fire the deck
- **Type:** Bug
- **Motivation:** The deck trigger suite (2026-11-08) case `deck-lesson-file`, a finished lesson pasted with "transforma essa aula em slides", fired deck in 2 of 3 runs: the deck's description speaks of content that "isn't settled" and the lesson's says "not for slides of settled content", so the model sometimes built slides with no skill. Accepted for now because the main path in is the lesson skill's handoff, which loads the deck directly.
- **Description:** The deck's description admits a lesson file's slides (e.g. "or a lesson file's slides"), within the 600-character limit, with more lesson-file cases in the suite.

## Discarded

### What happens to a `(hypothesis)` mistake at and after the gate
- **Description:** The light path says what the gate does with a hypothesis mistake: approval confirms it and drops the mark, and a rejected one changes the map, and the sample module with it, before approval. The SKILL.md is at its size limit, so this needs an equal cut.
- **Why discarded:** The doubt came from a simulated cold reader, not a real use; the gate rules (explicit approval, a closed map after it) already cover a rejected mistake, and the remaining risk (the mark left in the file) doesn't justify a cut in a SKILL.md at its size limit. (2026-11-08)
