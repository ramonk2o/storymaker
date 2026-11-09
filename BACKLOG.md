# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## Discarded

### Likely questions for a deck nobody presents
- **Description:** For a deck sent to read, `references/delivery.md` frames each likely question with "a short answer the presenter can say", though no one presents it; say whether they are written, and for whom.
- **Why discarded:** Raised by a simulated cold reader, not a real use. The questions still serve whoever answers the readers afterwards, and writing them anyway costs little. (2026-11-08)

### The external-tool prompt doesn't say it carries the speaker notes
- **Description:** `references/handoff.md` describes the prompt for an external slide tool as "title, visual, data and text" per slide, without the speaker notes.
- **Why discarded:** Raised by a simulated cold reader, not a real use. The same file says to pass everything decided to the build, the speaker notes included, and the delivery hands the notes over separately anyway, so nothing is lost. (2026-11-08)

### What happens to a `(hypothesis)` mistake at and after the gate
- **Description:** The light path says what the gate does with a hypothesis mistake: approval confirms it and drops the mark, and a rejected one changes the map, and the sample module with it, before approval. The SKILL.md is at its size limit, so this needs an equal cut.
- **Why discarded:** The doubt came from a simulated cold reader, not a real use; the gate rules (explicit approval, a closed map after it) already cover a rejected mistake, and the remaining risk (the mark left in the file) doesn't justify a cut in a SKILL.md at its size limit. (2026-11-08)
