# storymaker principles

Storymaker's skills help with work that tells a story: a presentation that carries a message, an essay that takes its reader through an argument. Each skill plans the story with the user before making the piece, and checks it with a reader who never saw the conversation. A piece with no story to tell, such as slides that only support a meeting, is left out. This file holds the principles every skill follows, the principles specific to each skill, and the questions for judging a change. A change that breaks a principle is a design decision and needs the maintainer's explicit agreement.

## Taking a request

1. **One skill per request.** Each skill states at the start of its `SKILL.md` the requests it leaves out and which sibling covers them, so two skills never offer themselves for the same request; a request no skill fits is handled without the plugin.
2. **Offer before taking over.** A skill started by the subject of a request, not by its name, first offers itself in one short message: what it does differently, what it costs, and a recommended answer. If the user declines, the request is handled without the skill, which isn't offered again in that conversation.

## Planning with the user

3. **Propose before asking.** Each message brings a round of up to five numbered questions, each with the recommended answer and a one-line reason, ordered by risk; a question whose answer changes the others goes first, and its dependents wait. When the material answers a question, the skill uses that answer and says where it came from; when the material contradicts itself, the skill asks before building on either side. Missing material never blocks: the skill drafts, hypothesizes and says where the information might be.
4. **Nothing invented.** Every figure, fact and quote comes from the material or the user; derived figures (sums, changes) are fine once checked. A fact only the user can know is never guessed in a recommended answer; it stays `[TO CONFIRM]`. Facts about a tool (features, limits, syntax) come from its current official documentation, never from the model's memory.
5. **What to say, then how to show it, then making it.** A piece is rarely weak because of its surface; it is weak because it doesn't know what it wants to say. So the skills settle the content and its structure before the form, and both before making the piece, because effort spent on form anchors the conversation to a first version and is thrown away when the content moves. The only thing made early is a small sample (a passage, a few slides) that lets the user judge the plan on real material.
6. **Explicit approval at gates; what was approved is closed.** How many gates a skill has, and where, is part of that skill's design: each gate sits where a wrong decision would cost the work that comes after it, and the skill's own section below says why its gates are where they are. At a gate, the user judges real text or a sample, not a description of it. "OK" or "go ahead" approve; silence, a passing comment or approving a round's answers do not. Once approved, a decision is closed: a later stage that needs to change it proposes the change, marked, and waits for approval. If its foundation changes (a figure doesn't exist, the audience changed, the central idea fell), the skill says so and reopens that stage instead of building on it.

## Making and checking

7. **The build uses what the session has and is reviewed as rendered.** A skill doesn't depend on one building tool. It looks for the options the session actually has, weighs them against the piece (a mandatory template, how it will be shared and edited, whether the result can be reviewed) and recommends one; the build treats the approved plan as its specification. Before delivering, it looks at the rendered result (overflowing text, legibility, contrast) and fixes what doesn't match the plan.
8. **Checked before the costly step, by a reader who wasn't in the conversation.** Before the step that costs most to redo, a stress test opening with a pre-mortem ("it failed; why?") looks for where the piece breaks, and a cold reader sees only what the real audience would see — the piece, the audience's profile without hints of the objective, and how the piece reaches them — and says what they understood, what they would do and where they stopped following. When the session can start a separate agent, the skill runs it; when it can't, it gives the user a ready prompt for a new conversation, because a model inside this conversation already knows the answer. A fix that changes an approved decision is a proposal the user approves; only fixes that change no decision go straight. The piece is done when the user is satisfied with it: no check asks the user to prove what the audience remembered.

## Building a skill

9. **Each skill stands alone.** A skill can be installed on its own and reads nothing outside its folder, so it carries every shared rule it needs in full. A shared rule is changed in every skill that states it, in the same branch.
10. **A lean core.** `SKILL.md` loads in full on every activation, so it holds only the flow and the rules every stage needs, in under about 4,000 tokens; what a single step or a single kind of piece uses lives in `references/`. The description, under about 300 characters, says when to use the skill and when not to.
11. **Capabilities, not tool names.** A skill describes what the session can do ("if the session can start an agent") instead of naming tools or products, which change across Claude surfaces. What it knows about target platforms lives in `references/` and is checked against current documentation before use, because it goes stale.
12. **English inside, the user's language outside.** Skills, references and every file in the repo are written in English; the skills talk to the user in the user's language.

## Skill principles

Each skill adds a section here when it is created, with the principles that apply only to it, including why its gates are where they are.

### deck

- **Started only by its command.** The deck runs only when the user calls it, so whether a deck gets planned is the user's choice, not a description's; the offer of principle 2 doesn't apply, and its description only tells the user what it does.
- **Where its gates sit.** Gate 1 closes the text of every slide before any visual work, because what the audience understands and remembers is decided by that text, and a visual planned on text that later moves is thrown away. Gate 2 closes the visual concept, the plan of how each slide is illustrated and the text changes it asks for, before the build, because a built deck costs the most to redo.
- **The checks read the text.** The stress test runs on the arc and the cold reader on the full slide text, both before the visual, because a flaw in the story found after the build costs the visual and the build with it. After the build, the user judges.
- **One visual approach.** Each kind of information gets the form that shows it (a sequence as a flow, a comparison side by side, a set as dots, nested groups as nested circles, an abstract idea as a metaphor), the same kind the same way across the deck, because a slide that solves its visual alone turns the deck into a collage.

## Judging a proposal

1. Which case does it come from, and is it real or hypothetical?
2. Does it change behavior, or only wording?
3. Does it conflict with a principle, here or in the skill's own section? If so, is the case strong enough to change the principle?
4. Does it apply to most uses of the skill, or to one kind of piece? One kind belongs in `references/`, not in `SKILL.md`.
5. Does it add size, turns, steps or gates? If so, what does it save?

A proposal for a new skill also answers:

6. Is its plan or its check different from every existing skill's? Another kind of piece with the same plan and check is a case in an existing skill.
7. Which requests does it take from a sibling, and is the sibling's scope changed in the same branch?

<!-- sensei:limits
skill_tokens: 4000
description_chars: 300
-->
