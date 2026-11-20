---
name: deck
description: "Plans a presentation that must get a message across, presented or read alone: the idea, the arc and every slide's text, then the visual, then the build. Not for agendas, status updates or settled slides."
disable-model-invocation: true
---

# Deck

Plans a presentation that has a message to get across, presented live or read alone, before building it: first what the deck says, down to the text of every slide, then how it looks, then the build. Slides that only support a meeting are left out: an agenda, a recurring status, content the user already settled slide by slide, restyling a finished deck. A text in prose goes to the essay skill. The test: the deck must change what its audience understands or does, and what it should say isn't settled yet.

Talk to the user in their language, and write every proposal in it.

## Starting

The skill runs only when the user calls it. A request that is out of scope, from the start or midway: say so in one line, naming the essay skill for a text in prose, and offer to go on without this skill; if the user wants the skill anyway, go on with it. Otherwise, go to step 1.

## Rules for every step

**Rounds.** Each message brings up to five numbered questions, each with your recommended answer and a one-line reason, so the user only confirms or corrects ("ok to all, except 3"):

```
1. [Question]
   → I recommend: [answer] — [reason]
```

Order them by risk: what would change the deck most if wrong goes first, and a question whose answer changes others goes alone, its dependents in the next round. For a choice between options (a concept, an arc), number the options and mark the recommended one. When the material answers a question, use that answer and say where it came from; when the material contradicts itself, ask before building on either side. Missing material never blocks: draft, state the hypothesis and say where the information might be.

**Nothing invented.** Every figure, fact and quote comes from the material or the user; derived figures (sums, changes) are fine once checked. A fact only the user knows (a price, a date, a commitment, what the audience knows today) is never guessed in a recommended answer: the recommendation asks for it, and it stays `[TO CONFIRM]` until the user gives it, at the latest before Gate 2. When someone else will fill it in after delivery (a manager's prices), it stays a marked placeholder in the deck, and the Gate 2 request says so.

**Gates.** A gate asks for explicit approval of real text or a sample. "OK" or "go ahead" approve; silence, a passing comment or "ok to all" on a round's answers don't. What a gate approved is closed: a later step that needs to change it proposes the change, marked, and waits for approval. If its foundation changes (a figure doesn't exist, the audience changed, the central idea fell), say so and reopen that step instead of building on it.

**Form after content.** No visual work, layout or deck file before Gate 1, and no build before Gate 2, because effort spent on form anchors the conversation to a first version and is thrown away when the content moves.

## 1. The material

Read everything the user brought: notes, data, files about the client or the subject, a visual guide. One message with:
- your reading in a few lines: what the deck must achieve, for whom, and what the material already settles;
- a round on what is still open: the audience (who receives it, what they know and believe today, what they should understand or do after), the format (presented live, or sent to be read alone), and every doubt or contradiction in the material, each with your recommended way to resolve it. When they don't fit in one round, the riskiest go first and the rest follow in the next round, still before step 2.

Without material, invite the user to dump loose ideas as they are, and work from those.

## 2. Central idea

The one idea the deck must leave with its audience, in one sentence they could repeat, with what is at stake for them. When the user has a clear view, phrase it more sharply; when not, propose two or three candidates drawn from the material. Adjust until the user recognizes it as theirs.

## 3. Arguments and ideas

Three to five arguments that hold up the central idea, each with the concrete element that makes it visible: a number with its comparison, a case, a quote, a deliverable. Say what from the material stays out, and why.

## 4. Arc

The order in which the arguments reach the audience, as parts, each with its job in the story. When the user gave an order, that is the arc; a different one is a marked alternative with its reason, next to theirs. Otherwise, propose two or three arcs, one recommended.

Then the stress test on the recommended arc, in the same message (again on the user's arc, if they pick another): open with the pre-mortem, "The deck was received and nothing changed. Why?" Give the two or three most likely reasons for this deck and this audience, each grounded in the material (a fragile figure, a claim without evidence, a jump in the reasoning) and with how the arc answers it. Each one changes the arc, or is left on purpose and the user is told.

## 5. Slide text — Gate 1

Write the text of every slide in one message, grouped under the arc's parts:

```
I. [Part] — its job
  1. [Title: a sentence that states the slide's point]
     [Body: the text as the audience will read it]
```

- One idea per slide: a title that needs an "and" is probably two slides. The body proves the title, nothing more.
- Density follows the format: presented live, short phrases the presenter talks over; read alone, each slide explains itself.
- Before showing it, read only the titles, in order: they must tell the story on their own.

The user adjusts the text. Then read `references/cold-reader.md` and run the cold reader on the text the user reviewed. Then, in one message: its answers next to what the deck intends, with the fixes you propose, and the text of every slide with the fixes that went straight in marked in it. Ask for approval of the slide text: Gate 1. `[TO CONFIRM]` items may pass Gate 1 if the user agrees.

## 6. Visual — Gate 2

Read `references/visual.md`. Two messages:
1. **Concepts:** the forms the deck's kinds of information take, and two or three visual concepts built on them, one recommended.
2. Once the user picks one: **the illustration plan** for every slide, the text changes it needs (marked), and a sample of two or three slides drawn in the concept. Ask for approval of the concept, the plan, the text changes and the sample: Gate 2.

## 7. Build

Read `references/build.md`. Offer the build options the session has, build from the two gates as the specification, review the rendered deck, and hand it over. The user then judges it; their fixes go into the built deck. The deck is done when the user is satisfied with it.
