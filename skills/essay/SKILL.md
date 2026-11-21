---
name: essay
description: "Plans a text that takes its reader through an argument: the idea, the arc and a line per paragraph, with a sample in the voice you want, yours or an author's; then writes it. Not for slides, summaries or proofreading."
disable-model-invocation: true
---

# Essay

Plans a text in prose that takes its reader through an argument or a story to a point, before writing it: first what the text says, down to a line for every paragraph, with a sample passage in the voice the user wants, then the whole text. The material can be loose ideas, notes, sources or a draft to rework. Slides go to the deck skill, including a deck meant to be read alone. Left out: a text with no point to get across (a summary, minutes, a factual report) and proofreading. The test: the text must change what its reader understands, believes or does.

Talk to the user in their language, and write every proposal in it.

## Starting

The skill runs only when the user calls it. A request out of scope, from the start or midway: say so in one line, naming the deck skill for slides, and offer to go on without this skill; if the user wants the skill anyway, go on with it. Otherwise, go to step 1.

## Rules for every step

**Rounds.** Each message brings up to five numbered questions, each with your recommended answer and a one-line reason, so the user only confirms or corrects ("ok to all, except 3"):

```
1. [Question]
   → I recommend: [answer] — [reason]
```

Order them by risk: what would change the text most if wrong goes first, and a question whose answer changes others goes alone, its dependents in the next round. For a choice between options (a central idea, an arc), number the options and mark the recommended one. When the material answers a question, use that answer and say where it came from; when the material contradicts itself, ask before building on either side. Missing material never blocks: draft, state the hypothesis and say where the information might be.

**Nothing invented.** Every figure, fact and quote comes from the material or the user; derived figures (sums, changes) are fine once checked. A fact only the user knows (a date, a result, what happened to them) is never guessed in a recommended answer: the recommendation asks for it, and it stays `[TO CONFIRM]` until the user gives it. One still open at the gate stays marked in the written text, and the gate request says so.

**Gates.** A gate asks for explicit approval of real text. "OK" or "go ahead" approve; silence, a passing comment or "ok to all" on a round's answers don't. What the gate approved is closed: a later step that needs to change it proposes the change, marked, and waits for approval. If its foundation changes (a fact doesn't hold, the reader changed, the central idea fell), say so and reopen that step instead of building on it.

**Prose after the plan.** No prose before the gate beyond the voice sample, because a text written on an outline that later moves is rewritten whole.

## 1. The material

Read everything the user brought: notes, sources, a draft, texts of theirs. One message with:
- your reading in a few lines: what the text must achieve, for whom, and what the material already settles;
- a round on what is still open: the reader (who they are, what they know and believe today, what they should understand or do after), where the text reaches them (a blog, a newsletter, a publication, a document sent to them) and its length, the voice (a register such as plain or conversational, the user's own texts, or an author they name), and every doubt or contradiction in the material, each with your recommended way to resolve it. When they don't fit in one round, the riskiest go first and the rest follow in the next round, still before step 2.

Without material, invite the user to dump loose ideas as they are, and work from those.

## 2. Central idea

The one idea the text must leave with its reader, in one sentence they could repeat, with what is at stake for them. When the user has a clear view, phrase it more sharply; when not, propose two or three candidates drawn from the material. Adjust until the user recognizes it as theirs.

## 3. Arguments

Three to five arguments that hold up the central idea, each with the concrete element that makes it visible: a fact, a case, an example, a quote. Say what from the material stays out, and why.

## 4. Arc

The order in which the arguments reach the reader, as parts, each with its job in the story. When the user gave an order (in a draft, too), that is the arc; a different one is a marked alternative with its reason, next to theirs. Otherwise, propose two or three arcs, one recommended.

Then the stress test on the recommended arc, in the same message (again on the user's arc, if they pick another): open with the pre-mortem, "The text was read and nothing changed. Why?" Give the two or three most likely reasons for this text and this reader, each grounded in the material (a fragile fact, a claim without evidence, a jump in the reasoning, a point the reader stops reading before) and with how the arc answers it. Each one changes the arc, or is left on purpose and the user is told.

## 5. Outline and voice — the gate

Write the outline in one message: the title, then one line per paragraph, grouped under the arc's parts:

```
[Title]
I. [Part] — its job
  1. [What the paragraph says, in one sentence, with its concrete element]
```

- One idea per paragraph: a line that needs an "and" is probably two paragraphs.
- Before showing it, read only the lines, in order: they must carry the argument on their own.

The user adjusts the outline. Then read `references/cold-reader.md` and run the cold reader on the outline the user reviewed. Then, in one message: its answers next to what the text intends, the outline with its fixes marked in it, and the voice sample: one or two paragraphs of the outline written in the voice from step 1 (read `references/patterns.md` first, and when the user named an author, `references/voice.md`), with the traits it follows named above it: tone, sentence rhythm, how it argues, how it uses examples. Ask for approval of the outline and the sample: the gate.

## 6. Writing

Read `references/patterns.md`, then write the whole text from the gate: every line of the outline as its paragraph, in order, in the approved voice. From a draft, keep its facts and examples, and its sentences that already fit the line and the voice. Before handing it over, reread it against the gate: each paragraph does its line's job, the voice keeps its traits, nothing is invented, the patterns follow `references/patterns.md`, and an author's voice keeps to the limits in `references/voice.md`. Hand it over the way the user will use it: in the conversation, or as a file when the session can make one and the user needs it. The user then judges it; their fixes go into the text. The text is done when the user is satisfied with it.
