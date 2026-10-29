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

Each skill adds a section here when it is created, with the principles that apply only to it, including why its gates are where they are. There are none yet.

## Judging a proposal

1. Which real case does it come from?
2. Does it change behavior, or only wording?
3. Does it conflict with a principle, here or in the skill's own section? If so, is the case strong enough to change the principle?
4. Does it apply to most uses of the skill, or to one kind of piece? One kind belongs in `references/`, not in `SKILL.md`.
5. Does it add size, turns, steps or gates? If so, what does it save, and is it on the light path?

A proposal for a new skill also answers:

6. Is its plan or its check different from every existing skill's? Another kind of piece with the same plan and check is a case in an existing skill.
7. Which requests does it take from a sibling, and is the sibling's scope changed in the same branch?
