# Cold reader

Used in step 1.3 (before Gate 1, or the single gate in express, on the slide titles) and in Phase 3 (on the finished deck). A cold reader checks whether the deck communicates what is intended, and whether it would move its audience, through someone who never saw the conversation.

## Running the check
- If the session can start a separate agent, start a fresh one that doesn't inherit this conversation, never a copy of it, and put in its prompt only what this file says to give it, with the instruction not to open any other file.
- Otherwise, give the user the prompt below, filled in, to paste into a new conversation with no access to this one, and ask them to paste the answers back.
- When the build option leaves no rendered deck (a prompt for an external tool, a build checklist), give the user the filled prompt with the delivery, to run on the exported slides as the audience will receive them (see below; the notes line kept or dropped to match), and say in the delivery that the check is pending. If they bring the exported deck back to this conversation, run it then.
- If the user prefers to skip it, record "not run" where the result is reported.

## What the reader receives
- The audience profile: role, what they know about the subject, what they believe and do about it today.
- Before Gate 1 (or the single gate): the slide titles, in order. After the build: the finished deck as the audience will receive it, as images or a PDF of the rendered slides. Live or to read: without speaker notes. Hybrid: as it will be sent to those who weren't there, with the speaker notes when they travel in the file, without them in a PDF or a view-only link (how it will be shared, weighed when choosing how to build in `handoff.md`).
- Never the conversation, the objective, the central idea, the intended shift or your notes. Check that the profile doesn't hint at what the deck wants.

## Prompt
Write it in the user's language and fill in the brackets.

```
You are [audience profile: role, what you know about the subject, what you believe and do about it today].
[Live: Someone is about to show you a presentation.] [To read: Someone sent you this deck to read on your own; nobody will present it.] [Hybrid: You missed a presentation; someone sent you its deck to read on your own.] [Before the gate: Here are its slide titles, in order: …] [After the build: The deck is attached.] [Hybrid with notes: Each slide's notes are included.]

Read it as that person would, and answer briefly:
1. In one sentence, what does this deck want you to think or do?
2. What is the first question or objection you would raise?
3. At what point would you lose interest?
4. At what point did it seem to jump ahead, or go back to something already covered?
5. What would you still resist accepting, and why?
6. At the end, what would you actually do?
[After the build only:] 7. What would you remember tomorrow?

Answer only from what is in front of you; don't guess what the presenter meant.
```

## Using the answers
- Show the answers next to what was expected (the central idea, the shift and the resistance recorded in the Opening or the Proposal) and propose adjustments where they diverge.
- Divergence in answers 1 or 6 is a storyline problem, not the reader's.
- A jump or a return named in answer 4 is an order problem, unless the storyline plans it (a recap, a close that returns to the hook): propose moving the slide into its part, or the missing step between two parts.
- Answer 5 measures whether the deck answers the resistance: if it names one the storyline doesn't address, propose an objection beat or an appendix slide.
- Answer 7 should be the memorable moment or the central idea; if it isn't, propose the adjustment.
- A new objection is resolved as in `stress-test.md`. After the build, a fix that changes content needs the user's approval and is written back into the gate documents.
