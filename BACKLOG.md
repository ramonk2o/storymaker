# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### Mode and length rules ignore practice time
- **Type:** Idea
- **Motivation:** A cold reader planning a one-hour support training with practice in the session, without the lesson skill (2026-11-08), found that "internal, low-risk, short" fits it only half, so it picked full mode by judgment; and "about one slide per one to two minutes" gives 30 to 60 slides, though much of the hour is hands-on practice.
- **Description:** The training case says how practice time counts in the mode choice and in the slide count.

### A handoff from the lesson skill still gets the offer
- **Type:** Bug
- **Motivation:** A cold reader given the deck's files and a lesson the user had just accepted turning into slides (2026-11-08) offered the deck skill again before starting, because "Starting" knows only "called by name" and "started by the subject of the request"; the lesson's handoff says the deck starts without its offer, but the deck never says so.
- **Description:** When a sibling hands a step over, the deck starts the Opening (or the express Proposal) without the offer. Reproduce: hand the deck a lesson file right after the lesson skill's offer is accepted and see whether the first reply is an offer.

### No rule for a question to the room outside a module
- **Type:** Idea
- **Motivation:** Same cold reader (2026-11-08): the lesson's opening had a teacher note to ask the room who already saves monthly, but the training case defines `[question]` slides only inside modules; the reader kept it in the speaker notes by judgment.
- **Description:** The training case says where a question to the room in the lesson's opening or close goes: a `[question]` slide where the lesson places it, or only the speaker notes when it is a teacher note.

### Flaws other than figures in an approved lesson
- **Type:** Idea
- **Motivation:** Same cold reader (2026-11-08) found the take-home challenge asked for 120 and 240 monthly periods of compound interest "on the phone calculator", hardly doable; the deck can't reopen the content and only the cold reader's findings can lead to a content proposal, so nothing covers what the deck itself notices.
- **Description:** Something in the lesson that the deck finds wrong or not doable goes to the user as a labeled proposal, as a mismatched figure already does.
- **Open questions:**
  - How far the deck may question an approved lesson without reopening its map.

## lesson

### Minutes and the overrun buffer disagree
- **Type:** Bug
- **Motivation:** A cold reader planning a 40-minute lesson (2026-11-08) found that step 1.4 says module minutes add up to the duration, while `learning.md` says live lessons run about 20% over. It had to choose whether the modules sum to 40 or to about 33.
- **Description:** The skill says whether the buffer sits inside the duration, so the map's minutes fit the slot. Reproduce: plan a live lesson and see what the minutes add up to.

### The user's topic order: decision or hypothesis
- **Type:** Idea
- **Motivation:** A cold reader (2026-11-08) received topics in an order that reversed their dependencies and reordered them into a staircase, deducing it from "you propose, the user adjusts"; nothing says whether a topic order the user brings is theirs to keep.
- **Description:** When the dependencies call for it, the skill reorders the user's topics as a labeled proposal with the reason, for the user to confirm.
