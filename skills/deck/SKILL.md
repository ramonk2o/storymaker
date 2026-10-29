---
name: deck
description: "Plans a presentation with the user before any slide is built: what it must change in the audience, the message, the story and how it holds attention; then the visual concept and production plan; only then builds it and checks it with a reader who never saw the plan. Use whenever the user is putting together a deck, slides or a talk and the content isn't settled yet, in any language, including 'make a deck out of this' with data or loose ideas (e.g., 'turn this report into slides for the director', 'monta um deck com esses resultados'). Not when the slide-by-slide script is already written."
---

# Deck

A deck is rarely weak because of its visuals; it is weak because it doesn't know what it wants to change in the audience. So this skill separates three decisions that usually come mixed — **what to say**, **how to show it** and **building it** — and moves from one to the next only when the user approves. Building early spends effort on slides that will be thrown away and anchors the conversation to a first version.

People often come here before they know what they want to say. That is the point: the skill helps them find it, by proposing hypotheses from what they bring and letting them react, instead of asking them to arrive with the answer.

```
Full:    Opening → PHASE 1 Story → [GATE 1: Script] → PHASE 2 Visual and production → [GATE 2: Production plan] → PHASE 3 Build and check
Express: Opening → Proposal with prototype → [SINGLE GATE] → PHASE 3 Build and check
```

Converse in the user's language, and write the gate documents in it; the templates below are molds, not fixed text.

## Starting

How the skill started decides the first reply, because someone who asked for slides didn't necessarily ask for a planning process.

- **Out of scope:** a deck whose slide-by-slide script is already written, including restyling or fixing a finished deck; the report or document the deck would present; the email that sends the deck; coaching how to deliver the talk; a carousel for a social network, which the post skill plans. Don't offer the skill; handle the request without it.
- **Called by name:** start the Opening.
- **Started by the subject of the request:** the first reply only offers the skill, in two or three sentences: what it does differently (settles what the deck must change in the audience before any slide is built) and what it costs (a few rounds, or one proposal and one approval in express mode). Ask whether to plan with it, with your recommended answer and a one-line reason drawn from the request. Don't read the materials or ask anything else yet.
- **Accepted:** start the Opening. **Declined:** handle the request as you would without the skill, with no rounds, gates or documents, and don't offer it again in this conversation.

If a request turns out midway to be out of scope, say so in one line and offer to continue without the skill.

## Modes

Recommend one in the Opening, with a one-line reason.

- **Full** — a deck that goes to a client, asks for a decision, money or approval, faces a skeptical room or will be presented under the user's name to many people. Two gates.
- **Express** — an internal, low-risk, short or recurring deck. Same Opening, then one message with the whole proposal and a prototype, and one gate. If something changes the course midway (the audience is different, the main figure doesn't exist, the central idea doesn't hold), suggest switching to full mode.

**Why the gates sit where they do.** Gate 1 closes what the deck says before any visual work, because a visual built on a story that later moves is thrown away. Gate 2 closes how it looks and how it is built before the build, because a built deck is the most expensive thing to redo. Express mode joins them because a short, low-risk deck costs little to redo.

## How to run it

**No slides before the production gate** (Gate 2, or the single gate in express). Don't generate slides, layouts or deck code, or call build tools, before it. The only exception is the low-fidelity prototype. If the user asks to skip ahead, say in one sentence what closing the content first gains and offer express mode; if they insist, the decision is theirs: leave the skill.

**Questions in rounds, always with your answer.** Each message brings a round of up to five numbered questions, each with the answer you recommend and a one-line reason, so the user only confirms or corrects ("ok to all, except 3").

```
1. [Question]
   → I recommend: [answer] — [reason, in one line]
```

- Only independent questions in a round: if one answer changes the others, ask it now and leave its dependents for the next round.
- Order by risk: first what, if wrong, changes the deck the most.
- For a choice between paths (mode, arc, visual concept), number the options and mark the recommended one.
- If the material answers a question, don't ask it: use the answer and say where it came from.
- Requests without urgency ("send the template if you have it") go in one line, outside the numbering.

**Help the user think.** Never require a clear vision to move on. When the user doesn't know yet what the deck should say or change, propose: two or three candidate central ideas drawn from the material or from what they said, what could have prompted the deck, what a win would look like. Ask which one is true for them. Reacting to a hypothesis is far easier than answering an open question. Without material, invite them to dump loose ideas as they are and work from that.

**The request is a hypothesis.** It answers a situation: what prompted it and what should change after it. When the material or the conversation shows that a deck won't bring that change (a decision already made, a problem a deck can't solve), say so in the first round as a labeled proposal, with what would, and follow the user's answer. When nothing points to it, don't ask.

**Nothing invented.** Every figure, fact and quote comes from the material or from the user; derived figures (sums, changes) are fine once checked. A fact only the user can know (a target, a date, who decides) never gets a guessed value as a recommended answer: it stays `[TO CONFIRM]` until resolved. One invented number destroys the credibility of everything else.

**Push, cut, keep the tension.** A planning assistant tends to agree too fast, add content, smooth over conflict and write long titles. Do the opposite: point out the weak spot, cut what doesn't serve the central idea, keep the tension the story needs, and keep titles short.

**Go back when needed.** If something from an earlier phase changes (a figure doesn't exist, the audience changed, the central idea fell), say so and reopen that phase instead of building on it.

**A gate is explicit approval.** "OK", "approved", "go ahead" count; silence, a change of subject or a passing comment don't. An "ok to all" in a round approves the answers, not the gate, which has its own request. After a gate, its document is a closed specification: what comes next doesn't add, drop or swap anything decided there without asking, and later content changes, even after delivery, are written back into it.

**Checks by someone who wasn't here.** A model inside this conversation already knows the objective, so never play the reader yourself. `references/cold-reader.md` says how to run the cold reader, with or without a separate agent. In express mode, offer the title check in one line.

## Opening

The Opening gathers what the deck needs, through hypotheses the user reacts to. It doesn't settle the central idea; that opens Phase 1. It usually takes one or two rounds.

**First reply** (after the offer was accepted, or right away when called by name):
- One sentence on how it works: first what the deck must say, then how it looks, then build and check.
- The deck type, from `references/cases/` (read the matching file): `results-analysis.md`, `strategy-proposal.md`, `idea-pitch.md`, `research-presentation.md`, `project-status.md`, `training.md`, `campaign-concept.md`, `talk.md`. A hybrid deck (results that end in a proposal) reads both and picks the primary one.
- **With material:** read all of it and bring a first reading: the findings that seem to matter and any risk an attentive audience would raise (a fragile figure, an unfair comparison). **Without material:** the case's typical skeleton adapted to what was said, and an invitation to dump loose ideas.
- A round that opens with the mode and covers what the request leaves open, each with your hypothesis:
  - **Audience and shift:** who they are, what they believe and do about this today, and what they should believe or do after the deck.
  - **Resistance:** what could stop them — logical (doubt about the evidence), emotional (values, threat, pride) or practical (cost, effort, risk to them).
  - **Format:** presented live, sent to read, or **hybrid** (presented, then sent to people who weren't there); duration; who presents.
  - **Constraints and recurrence:** what is mandatory or forbidden, the deadline; whether it is an edition of a periodic deck (if the user brings a Recurring blueprint, follow `references/recurring.md`).
- One line asking for everything that helps: data, previous decks for this audience, the template or brand manual, references they like.

Then ask the case's diagnosis questions the material and conversation leave open, until there is enough to propose central ideas.

## Phase 1 — Story

You propose, the user adjusts. Skip any step the material or the conversation already answers.

**1.1 Message.** One message that brings:
- **Central idea:** one sentence with a point of view (someone could disagree) and what is at stake for this audience (what they gain or lose). The case file shows how to phrase it. If the user has a clear view, phrase it more sharply and add one alternative that would make a different deck; if not, propose two or three candidates. Label alternatives as proposals, so approving the idea is a choice.
- **Supporting points:** three to five, each with a concrete element that makes it visible: a case, a customer, a real quote, a screenshot, a number with its comparison.
- **Triage:** a table of the material's relevant blocks — In, Appendix or Out, with the reason. What goes in supports the central idea or answers a likely objection.
- **The 3-minute story:** the whole deck told as a short paragraph, as the user would say it with no slides, so they can hear whether it holds. Ask: if the slot is cut to five minutes, what survives?
- **Gaps:** what is missing to support the idea.

Adjust until the user recognizes the idea and the story as theirs.

**1.2 Story.** Read `references/narrative.md` and `references/attention.md`. One message that brings:
- **Answer first or build tension**, chosen by the situation, with the arc that follows from it (two or three options when it isn't obvious, one recommended).
- **Hook, memorable moment and close**, each with your recommendation.
- **The storyline**, which carries the arc and marks the hook, the moment, any objection beat and the close:

```
1. [Assertion title] — role in the story — evidence/source — [hook | moment | objection | breather | ask]
```

- Titles are full sentences that state the slide's conclusion ("Repurchase fell 12% among inactive customers"), never labels ("Results"), and fit in two lines (about 15 words). One slide, one idea: a title that needs an "and" is probably two slides. The body proves the title, nothing more.
- Read only the titles in sequence: the story must hold.
- Length: live or hybrid, about one slide per one to two minutes; to read, fewer and denser slides.
- **First stress round:** read `references/stress-test.md` and open with its pre-mortem. Further rounds only for branches left open.

**1.3 Cold reader on the titles.** Run it as `references/cold-reader.md` says, before the gate.

### Gate 1 — Script

```
SCRIPT — [deck name]
Mode: full · Deck type: …
Audience: … · Today they … → after, they should …
Resistance: …
Format: live | reading | hybrid · duration · presenter
Central idea: …
Arc: … (why, in one line)

Storyline
1. [Title] — role — evidence — [mark]
…
Appendix: … · Left out: …
Cold reader: [what diverged and what changed, or "not run"]
Pending [TO CONFIRM]: …
```

Ask for explicit approval. Pending items may move on if the user agrees, but must be resolved before Gate 2.

## Phase 2 — Visual and production

As the story starts from a central idea, the visual starts from a **visual concept**: one idea that organizes how the whole deck looks. Without it, each slide solves its visuals alone and the deck becomes a collage.

**2.1 Direction.** Read `references/visual-concept.md`, `references/visuals-and-charts.md` and `references/handoff.md`. One message that brings:
- Two or three visual concepts derived from the central idea, the arc, the memorable moment, the audience and the identity materials, one recommended, with the global rules derived from it (palette, type, density by format, chart standard, use of images).
- The build options this session actually has, judged against this deck, one recommended.
- A low-fidelity prototype of two or three representative slides (the hook or cover, the hardest data slide, the memorable moment), drawn inline when the session allows. It validates the concept and the rules, not the deck: no build tools here.

Adjust with the user's reaction before moving on.

**2.2 Production plan.** Define every slide in one go: title (exactly the one in the Script; change it only with approval, and update the Script), visual (type, exact data, what to highlight), the minimum supporting text and, for live or hybrid decks, speaker notes. Add the likely questions with their answers, as `references/delivery.md` says. Before the gate, no `[TO CONFIRM]` is left.

### Gate 2 — Production plan

```
PRODUCTION PLAN — [deck name]
Visual concept: … · Global rules: palette · type · density · charts · images
Template/identity: … · Build: [option] — [why]
Prototype: approved

Slide 1 — [Title] — [mark]
  Visual: … · Data: … · Text: … · Notes: …
…
Appendix: … · Likely questions: …
```

Ask for explicit approval.

## Express proposal

After the Opening, one message brings: the Proposal block below, built by the rules of 1.1, 1.2 and 2.1; a low-fidelity prototype; and one round of the three to five highest-risk questions from `references/stress-test.md`, opening with the pre-mortem.

```
PROPOSAL — [deck name]
Mode: express · Audience · shift · format · deck type
Central idea: … (alternative: …)
Arc: … · Hook · moment · close

Storyline
1. [Title] — evidence — visual — [mark]
…
Visual concept: … · Global rules: … · Build: [option] — [why]
Pending [TO CONFIRM]: …
```

Ask for explicit approval; pending items are resolved before building.

## Phase 3 — Build and check

1. **Build** from the approved plan as a closed specification, following `references/handoff.md`.
2. **Review on the rendered slides** against the plan and the checks in `references/handoff.md`. Fix appearance; ask before changing content.
3. **Cold reader on the finished deck**, in both modes, as `references/cold-reader.md` says.
4. **Deliver** the deck, the speaker notes and the likely questions. For the first edition of a recurring deck, also the Recurring blueprint (`references/recurring.md`).
