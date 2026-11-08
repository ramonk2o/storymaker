# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### Mode and length rules ignore practice time
- **Type:** Idea
- **Motivation:** A cold reader planning a one-hour support training with practice in the session, without the lesson skill (2026-11-08), found that "internal, low-risk, short" fits it only half, so it picked full mode by judgment; and "about one slide per one to two minutes" gives 30 to 60 slides, though much of the hour is hands-on practice.
- **Description:** The training case says how practice time counts in the mode choice and in the slide count.

## lesson

### Minutes and the overrun buffer disagree
- **Type:** Bug
- **Motivation:** A cold reader planning a 40-minute lesson (2026-11-08) found that step 1.4 says module minutes add up to the duration, while `learning.md` says live lessons run about 20% over. It had to choose whether the modules sum to 40 or to about 33.
- **Description:** The skill says whether the buffer sits inside the duration, so the map's minutes fit the slot. Reproduce: plan a live lesson and see what the minutes add up to.

### The user's topic order: decision or hypothesis
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) received topics in an order that reversed their dependencies and reordered them into a staircase, deducing it from "you propose, the user adjusts"; nothing says whether a topic order the user brings is theirs to keep.
- **Description:** When the dependencies call for it, the skill reorders the user's topics as a labeled proposal with the reason, for the user to confirm.
