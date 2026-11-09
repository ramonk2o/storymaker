# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## Plugin

### A how-to blog post or a written tutorial fits both essay and lesson
- **Type:** Bug
- **Motivation:** Consistency audit (2026-11-08). essay leaves out "written tutorials learners work through" but offers a How-to arc for practical blog posts; lesson takes "a written tutorial or guide that learners work through and practise with" and leaves out only posts "to readers who won't practise it". Readers of a how-to post follow its steps, so "a blog post on how to set up webhooks" can be claimed by both (an essay outline against modules, hinge questions and a final task), against principle 1. lesson's description names only "a class, training, workshop or teaching talk", so a request for a study guide or tutorial may fire neither.
- **Description:** Both Starting sections draw the same line: material built around exercises or checks the reader does is a lesson; a post that shows the steps without practice is an essay. lesson's description names self-study tutorials and guides, within the 600-character limit, with cases for both sides in the trigger suites.

### Counts the model does by hand: characters and spoken minutes
- **Type:** Idea
- **Motivation:** Consistency audit (2026-11-08). post's delivery gives each unit "its character count against the limit" (`references/handoff.md`), and lesson's Revise checks that "the minutes still fit" at about 130 spoken words a minute, up to about 6,000 words for an hour taught with practice afterwards. Models miscount at both sizes, especially with accents, emoji and links weighted by the network, so a post can be cut at publishing or a lesson run long with a delivery note that says it fits.
- **Description:** A small script in each skill's `scripts/` counts characters per unit (with the network's weighting from the plan) and words per module (converted to minutes); without code execution, the count is labeled approximate.

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
