# Cold reader

Used in step 1.3 (before Gate 1, on the slide titles) and in Phase 3 (on the finished deck). A cold reader checks whether the deck communicates what is intended, and whether it would move its audience, through someone who never saw the conversation.

## Running the check
- If the session can start a separate agent, start one and give it only what this file says to give it.
- Otherwise, give the user the prompt below, filled in, to paste into a new conversation with no access to this one, and ask them to paste the answers back.
- If the user prefers to skip it, record "not run" where the result is reported.

## What the reader receives
- The audience profile: role, what they know about the subject, what they believe and do about it today.
- Before Gate 1: the slide titles, in order. After the build: the finished deck.
- Never the conversation, the objective, the central idea, the intended shift or your notes. Check that the profile doesn't hint at what the deck wants.

## Prompt
Write it in the user's language and fill in the brackets.

```
You are [audience profile: role, what you know about the subject, what you believe and do about it today].
Someone is about to show you a presentation. [Before Gate 1: Here are its slide titles, in order: …] [After the build: The deck is attached.]

Read it as that person would, and answer briefly:
1. In one sentence, what does this deck want you to think or do?
2. What is the first question or objection you would raise?
3. At what point would you lose interest?
4. What would you still resist accepting, and why?
5. At the end, what would you actually do?
[After the build only:] 6. What would you remember tomorrow?

Answer only from what is in front of you; don't guess what the presenter meant.
```

## Using the answers
- Show the answers next to what was expected (the central idea, the shift and the resistance recorded in the Opening) and propose adjustments where they diverge.
- Divergence in answers 1 or 5 is a storyline problem, not the reader's.
- Answer 4 measures whether the deck answers the resistance: if it names one the storyline doesn't address, propose an objection beat or an appendix slide.
- Answer 6 should be the memorable moment or the central idea; if it isn't, propose the adjustment.
- A new objection is resolved as in `stress-test.md`. After the build, a fix that changes content needs the user's approval and is written back into the gate documents.
