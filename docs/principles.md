# Storymaker principles

Storymaker's skills help people make pieces for an audience: presentations, essays, posts and the like. Each skill settles with the user what the piece has to say and what a good result is before making it, and checks the result with a reader who never saw the conversation. This file holds the principles every skill follows, the principles specific to each skill, and the questions for judging a change. A change that breaks a principle is a design decision and needs the maintainer's explicit agreement.

## Taking a request

1. **One skill per request; steps can be handed over.** Each skill states at the start of its `SKILL.md` the requests it leaves out and which sibling covers them, so two skills never offer themselves for the same request; a request no skill fits is handled without the plugin. During the work, when a sibling the session can load does a step better, the skill hands that step over and takes the result back; the sibling starts without its offer and treats what was approved as settled. When no sibling is available, the skill does the step itself.
2. **Offer before taking over, unless the draft costs less.** A skill started by the subject of a request, not by its name, first offers itself in one short message: what it does differently, what it costs, and a recommended answer. When the piece is a few lines, such as a short post, the first reply is the draft, with one line on what the skill adds. If the user declines, the request is handled without the skill, which isn't offered again in that conversation.
3. **The request is a hypothesis.** A request names a piece but answers a situation. When something shows the piece won't bring the change the user wants (a deck asking for a decision already made, an essay where the argument isn't settled yet), the skill says so in the first round, with what would, and follows the user's answer. When nothing points to a mismatch, it doesn't ask.

## Planning with the user

4. **Depth matches the stakes.** A piece that goes to clients, asks for a decision or money, faces a skeptical audience or will be published under the user's name gets the full flow. An internal, low-risk, short or recurring piece gets a light path, and every addition to a flow states whether it applies there.
5. **Propose before asking.** Each message brings a round of up to five numbered questions, each with the recommended answer and a one-line reason, ordered by risk; a question whose answer changes the others goes first, and its dependents wait. When the material answers a question, the skill uses that answer and says where it came from. Missing material never blocks: the skill drafts, hypothesizes and says where the information might be.
6. **Nothing invented.** Every figure, fact and quote comes from the material or the user; derived figures (sums, changes) are fine once checked. A fact only the user can know is never guessed in a recommended answer; it stays `[TO CONFIRM]`. Facts about a tool (features, limits, syntax) come from its current official documentation, never from the model's memory.
7. **What to say, then how to show it, then making it.** A piece is rarely weak because of its surface; it is weak because it doesn't know what it wants to say. So the skills settle the content and its structure before the form, and both before making the piece, because effort spent on form anchors the conversation to a first version and is thrown away when the content moves. The only thing made early is a small sample (a passage, a prototype of a few slides) that lets the user judge the plan on real material.
8. **Explicit approval at gates; what was approved is closed.** How many gates a skill has, and where, is part of that skill's design, decided when the skill is created from what it makes: a piece built in several stages may approve each one, a short one may approve a single plan or only the draft. This principle sets no number; it asks that each gate sit where a wrong decision would cost work that comes after it, and that the skill's own section below say why its gates are where they are. At a gate, the user judges real text or a sample, not a description of it. "OK" or "go ahead" approve; silence, a passing comment or approving a round's answers do not. Once approved, the decision is closed: later stages don't change it without asking. If its foundation changes (a figure doesn't exist, the audience changed, the central idea fell), the skill says so and reopens that stage instead of building on it.

## Making and checking

9. **The build uses what the session has and is reviewed as rendered.** A skill doesn't depend on one building tool. It looks for the options the session actually has, weighs them against the piece (a mandatory template, how it will be shared and edited, whether the result can be reviewed) and recommends one; the build treats the approved plan as its specification. Before delivering, it looks at the rendered result (overflowing text, legibility, contrast, a wrong highlight) and checks it against the plan, not only the code or text behind it.
10. **Checked by a reader who wasn't in the conversation.** A cold reader sees only what the real audience would see — the piece, the audience's profile without hints of the objective, and how the piece reaches them — and says what they understood, what they would do and where they stopped following. When the session can start a separate agent, the skill runs it; when it can't, it gives the user a ready prompt for a new conversation, because a model inside this conversation already knows the answer. A fix the reader calls for that changes an approved decision is a proposal the user approves; only fixes that change no decision go straight.

## Building a skill

11. **Each skill stands alone.** A skill can be installed on its own and reads nothing outside its folder, so it carries every shared rule it needs in full. A shared rule is changed in every skill that states it, in the same branch.
12. **A lean core.** `SKILL.md` loads in full on every activation, so it holds only the flow and the rules every stage needs, in under about 5,000 tokens; what a single step or a single kind of piece uses lives in `references/`. The description, under about 600 characters, says when to use the skill and when not to.
13. **Capabilities, not tool names.** A skill describes what the session can do ("if the session can start an agent") instead of naming tools or products, which change across Claude surfaces. What it knows about target platforms lives in `references/` and is checked against current documentation before use, because it goes stale.
14. **English inside, the user's language outside.** Skills, references and every file in the repo are written in English; the skills talk to the user in the user's language.

## Skill principles

Each skill adds a section here when it is created, with the principles that apply only to it, including why its gates are where they are.

### deck

The goal is decks that change what their audience believes or does: useful, holding attention, achieving their objective.

1. **Start from the shift in the audience.** What the audience believes and does today, what it should believe or do after, and what resistance stands between (logical, emotional or practical) come before the message, because a deck is judged by that change, not by its slides. The central idea carries a point of view and what is at stake for the audience.
2. **Help the user find what to say.** People come before they know their message. The skill never requires a clear vision to move on: it proposes candidate ideas, a likely shift and a draft of the story for the user to react to.
3. **Titles state conclusions.** Every slide title is a full sentence with the slide's conclusion, never a label, and fits in two lines. Read in sequence, the titles tell the whole story; each slide's body proves its title, nothing more.
4. **Attention is planned.** A hook tied to the central idea, one memorable moment at the turning point, and a close that is the concrete ask; answer first or tension is decided explicitly by the situation; every key number comes with a concrete case; what is interesting but doesn't serve the idea is cut.
5. **A visual concept comes before visual rules.** The whole deck orbits one visual idea, judged on a prototype; palette, type and chart rules derive from it and from the brand.
6. **Gates.** Full mode has two: the Script closes what the deck says before any visual work, because visuals built on a story that later moves are thrown away; the Production plan closes how it looks and how it is built before the build, because a built deck is the most expensive thing to redo. Express mode, for internal, low-risk, short or recurring decks, joins them in a single gate, because such a deck costs little to redo; it is the skill's light path.
7. **Checks.** A stress test opening with a pre-mortem, and a cold reader before Gate 1 (on the titles) and after the build (on the deck), who also says what they would still resist. The rendered review checks the plan, the glance test and the slides' layouts.
8. **The deck comes with its words.** The skill delivers speaker notes and the likely questions with their answers; it doesn't coach delivery.

A change that applies to one kind of deck belongs in a case file in `references/cases/`.

### essay

The goal is long texts (essays, blog posts, columns, newsletter issues) that a reader who can leave at any line reads to the end and comes away thinking differently.

1. **The argument is judged before the prose.** The outline has one line per paragraph, each a claim of about 12 words with its proof and a word estimate, grouped by the movements of the arc. Read in sequence, the lines tell the whole argument, so order, weight and gaps are fixed while they are cheap to fix. Writing follows the outline paragraph by paragraph.
2. **Help the user find what to say.** People come with a subject, a hunch or notes. The skill proposes candidate central ideas and a first reading to react to, and never requires a thesis to move on. The position, and every scene or result attributed to the author's life, belong to the author.
3. **The voice comes from wherever the user points.** A register, the user's own texts, reference texts by anyone, a brand's guide, or a named person to take inspiration from, alone or combined. Any of them becomes four to seven observable traits, shown on a sample passage. Traits are imitated, never passages: no reproduced or closely paraphrased text, no signature phrases.
4. **Rework starts from a reverse outline.** A draft brought to be reworked is first outlined back, one line per paragraph with what it actually claims, so the user sees where the order breaks before anything is rewritten.
5. **Gates.** One, the Essay outline, which closes what the text says, in what order and in what voice before writing, because writing is the expensive step and a draft built on an argument or a voice that later moves is rewritten whole. Nothing after writing depends on a new decision, so there is no second gate. The light path, for settled, short, low-risk or recurring texts, keeps the same gate with the whole proposal in one message.
6. **Checks.** A stress test opening with a pre-mortem before the outline. After writing, a cold reader who tests the opening first, then reads the whole text and outlines it back, so drift from the approved outline shows paragraph by paragraph; and a style check, without any name, when the voice comes from texts or a person. Both run in the full path and are offered in the light path.

A change that applies to one kind of text belongs in a case file in `references/cases/`; a change about voice in `references/style.md`; a writing rule for every kind of text in `references/writing.md`.

### post

The goal is social posts (single posts, captions, threads and carousels) that a reader scrolling past stops for, reads to the last unit and comes away with one idea they can use or repeat.

1. **The first unit decides.** Most readers see only the first lines, the first post or the cover. The opening is chosen from two or three hooks written in full from different angles, never described, and every hook must be paid off by the post as planned.
2. **The unit is the post or the slide.** A thread or carousel is planned as a script with one line per unit, each with its role and its claim, so the count and the order are judged before writing. Each unit carries one idea and reads on its own; the count is what the content earns.
3. **Help the user find what to say.** People come with a hunch, a link or a text to turn into a post. The skill proposes candidate ideas, and for a text, a reverse outline marking what survives in the format. The position, and every result or scene attributed to the author, belong to the author.
4. **Words, not images.** For a carousel the skill delivers each slide's words, a visual note, the caption and alt text; designing or generating the images is out of scope.
5. **Platform rules are looked up.** Limits and how links, hashtags and the "see more" cut behave come from the network's current documentation or the user, never from memory, and the figures used go into the plan.
6. **Gates.** A short post's draft is its gate, because a draft is cheaper to judge than a plan; the first reply is the draft. A thread or carousel has one gate, the Post script, which closes the point, the hook and what each unit does before the rest is written, because a hook that changes after writing means rewriting every unit that pays it off. Nothing after writing depends on a new decision, so there is no second gate. One idea for several networks shares one gate.
7. **Checks.** The stakes, not the format, decide them: for a post signed publicly, a position others will push back on, or a brand's or public figure's post, a stress test opening with a pre-mortem runs before the gate, and after writing a cold reader first sees only what the feed shows, says whether they would stop, then reads the whole post and summarizes it unit by unit; a style check runs when the voice comes from texts or a person. Otherwise the checks are offered in one line.

A change that applies to one format belongs in a case file in `references/cases/`; a change about voice in `references/style.md`; a writing rule for every format in `references/writing.md`.

## Judging a proposal

1. Which real case does it come from?
2. Does it change behavior, or only wording?
3. Does it conflict with a principle, here or in the skill's own section? If so, is the case strong enough to change the principle?
4. Does it apply to most uses of the skill, or to one kind of piece? One kind belongs in `references/`, not in `SKILL.md`.
5. Does it add size, turns, steps or gates? If so, what does it save, and is it on the light path?

A proposal for a new skill also answers:

6. Is its plan or its check different from every existing skill's? Another kind of piece with the same plan and check is a case in an existing skill.
7. Which requests does it take from a sibling, and is the sibling's scope changed in the same branch?
