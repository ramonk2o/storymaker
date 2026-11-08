# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### Training skeleton contradicts the lesson path
- **Type:** Bug
- **Motivation:** A lesson made with the lesson skill became a deck whose slides "jumped from puddle to puddle, back and forth". While testing the fix (2026-11-08), a cold reader building slides from a lesson file noticed that `cases/training.md`'s "Typical skeleton" opens with "What you will be able to do at the end" and has a separate "Common mistakes" slide near the end, while the same file's lesson path opens with the hook and keeps each mistake inside its module.
- **Description:** The skeleton agrees with the lesson path, so a model reading it doesn't gather the mistakes at the end or open with the objective, which would recreate the jumping order. Reproduce: run the deck from a lesson file and see whether a "common mistakes" slide appears after the modules.
- **Open questions:**
  - Is the priority over the other deck entries agreed?

### No place for the question to the room
- **Type:** Idea
- **Motivation:** Same cold reader (2026-11-08): the storyline marks are `[hook | moment | objection | breather | ask]`, and a lesson's question to the room fits none. The reader made it an unmarked slide, unsure whether it should be a slide or a speaker note, and before or after the module's example.
- **Description:** The deck states where a lesson's question to the room goes in the storyline: its mark, whether it is a slide or a note, and where in its module.

### Express storyline has no role column
- **Type:** Idea
- **Motivation:** Same cold reader (2026-11-08): the express proposal's storyline line is `Title — evidence — visual — mark`, without the full mode's role, so for lesson slides nobody sees whether a module has its key idea, example and mistake.
- **Description:** The express storyline shows each slide's role, at least for the slides of a lesson.

## lesson

### Minutes and the overrun buffer disagree
- **Type:** Bug
- **Motivation:** A cold reader planning a 40-minute lesson (2026-11-08) found that step 1.4 says module minutes add up to the duration, while `learning.md` says live lessons run about 20% over. It had to choose whether the modules sum to 40 or to about 33.
- **Description:** The skill says whether the buffer sits inside the duration, so the map's minutes fit the slot. Reproduce: plan a live lesson and see what the minutes add up to.

### The user's topic order: decision or hypothesis
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) received topics in an order that reversed their dependencies and reordered them into a staircase, deducing it from "you propose, the user adjusts"; nothing says whether a topic order the user brings is theirs to keep.
- **Description:** When the dependencies call for it, the skill reorders the user's topics as a labeled proposal with the reason, for the user to confirm.
