# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## deck

### A loose lesson file doesn't always fire the deck
- **Type:** Bug
- **Motivation:** The deck trigger suite (2026-11-08) case `deck-lesson-file`, a finished lesson pasted with "transforma essa aula em slides", fired deck in 2 of 3 runs: the deck's description speaks of content that "isn't settled" and the lesson's says "not for slides of settled content", so the model sometimes built slides with no skill. Accepted for now because the main path in is the lesson skill's handoff, which loads the deck directly.
- **Description:** The deck's description admits a lesson file's slides (e.g. "or a lesson file's slides"), within the 600-character limit, with more lesson-file cases in the suite.

### A hybrid deck's reading notes are lost when it is shared as a PDF
- **Type:** Bug
- **Motivation:** Cold reader test of the deck change `deck-cold-reader-format` (2026-11-08): a hybrid deck presented to the board, then sent "as a PDF to the directors who weren't there". `references/delivery.md` writes hybrid notes as "full reading text, so someone who gets the file later understands the slide without the presenter", but a PDF or a view-only link doesn't carry them, and nothing links how the deck will be shared (weighed when choosing how to build in `references/handoff.md`) to where those notes go. The absent readers get slides written to lean on notes they never see; the cold reader, which now gets the hybrid deck without notes in a PDF, catches it only after the build.
- **Description:** When a hybrid deck will be shared in a form that drops speaker notes, the choice of how to build says so and proposes where the reading text goes (on the slides, a file that keeps notes, or a written summary sent with it), before the Production plan or the express proposal is approved.

## post

### No first reply for a long single post or a request mixing paths
- **Type:** Bug
- **Motivation:** Consistency audit (2026-11-08). Paths sends "a post long enough that its order matters" (over about 150 words, a common LinkedIn post) to the script path, but Starting only has bullets for "Short post" (reply with the draft) and "Thread or carousel" (offer or Opening), so for "write a LinkedIn post about my layoff" the model guesses between a draft and an offer. The same gap for one idea going to networks on different paths ("this article as a LinkedIn post and an X thread"): "each network follows its own path inside the same gate" doesn't say whether the short post is drafted now or held for the Post script.
- **Description:** Starting covers the long single post, called by name and by subject, with the same first reply as its path; a request where any network takes the script path follows the script path, with the short units drafted inside the Post script.
- **Open questions:**
  - Is the length known at the start, or does the first reply pick the path from the request and the network?

### The short post's cold reader tests the stop after reading the whole post
- **Type:** Bug
- **Motivation:** Consistency audit (2026-11-08). `references/cold-reader.md` tests the stop first because "a reader handed the whole post can't unread it", then says "For a short post, merge both prompts into one call". A short post of up to 150 words usually runs past the "see more" cut, so the merged call asks whether the reader would stop after they read everything: the test principle post-1 depends on, on the high-stakes posts where the reader is required.
- **Description:** Merge the two calls only when the whole post fits before the cut; otherwise the first call gets the text before the cut, then the second the whole post.

## Plugin

### The after-checks rules drifted between skills
- **Type:** Debt
- **Motivation:** Consistency audit (2026-11-08). Shared rules about the checks differ across skills (principle 11):
  - essay, post, lesson and email say in "Why the gate sits where it does" that "fixes the checks call for are approved one by one", while their own Phase 3 (or check step) and principle 10 say only fixes that change an approved decision need approval and the rest "go straight", so the model can't tell whether to ask about each fix;
  - only lesson says what happens without a separate agent ("show the lesson first … bring the fixes once the user pastes the answers back"); essay, post and email don't;
  - essay, post and lesson bring "the delivery options" with the check results but read `references/handoff.md` only at Deliver, so the options are offered without its rules;
- **Description:** One wording for each rule, in every skill that states it: only fixes that change a decision are approved; without a separate agent, the piece is shown first with the filled prompts; `handoff.md` is read before the message with the check results.

### A how-to blog post or a written tutorial fits both essay and lesson
- **Type:** Bug
- **Motivation:** Consistency audit (2026-11-08). essay leaves out "written tutorials learners work through" but offers a How-to arc for practical blog posts; lesson takes "a written tutorial or guide that learners work through and practise with" and leaves out only posts "to readers who won't practise it". Readers of a how-to post follow its steps, so "a blog post on how to set up webhooks" can be claimed by both (an essay outline against modules, hinge questions and a final task), against principle 1. lesson's description names only "a class, training, workshop or teaching talk", so a request for a study guide or tutorial may fire neither.
- **Description:** Both Starting sections draw the same line: material built around exercises or checks the reader does is a lesson; a post that shows the steps without practice is an essay. lesson's description names self-study tutorials and guides, within the 600-character limit, with cases for both sides in the trigger suites.

### Counts the model does by hand: characters and spoken minutes
- **Type:** Idea
- **Motivation:** Consistency audit (2026-11-08). post's delivery gives each unit "its character count against the limit" (`references/handoff.md`), and lesson's Revise checks that "the minutes still fit" at about 130 spoken words a minute, up to about 6,000 words for an hour taught with practice afterwards. Models miscount at both sizes, especially with accents, emoji and links weighted by the network, so a post can be cut at publishing or a lesson run long with a delivery note that says it fits.
- **Description:** A small script in each skill's `scripts/` counts characters per unit (with the network's weighting from the plan) and words per module (converted to minutes); without code execution, the count is labeled approximate.

## Discarded

### What happens to a `(hypothesis)` mistake at and after the gate
- **Description:** The light path says what the gate does with a hypothesis mistake: approval confirms it and drops the mark, and a rejected one changes the map, and the sample module with it, before approval. The SKILL.md is at its size limit, so this needs an equal cut.
- **Why discarded:** The doubt came from a simulated cold reader, not a real use; the gate rules (explicit approval, a closed map after it) already cover a rejected mistake, and the remaining risk (the mark left in the file) doesn't justify a cut in a SKILL.md at its size limit. (2026-11-08)
