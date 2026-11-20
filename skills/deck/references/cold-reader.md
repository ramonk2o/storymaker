# Cold reader

Used in step 5, on the full slide text the user reviewed, before Gate 1. A model inside this conversation already knows what the deck wants to say, so it can't play the reader.

## Running it

- If the session can start a separate agent, start a fresh one that doesn't inherit this conversation, with only the prompt below, filled in, and the instruction not to open any other file.
- Otherwise, give the user the filled prompt to paste into a new conversation with no access to this one, and ask them to bring back the answers.
- If the user prefers to skip it, say in one line what it would catch; if they still skip, write "cold reader: not run" in the Gate 1 request.

## What the reader gets

- **The audience profile:** role, what they know about the subject, what they believe and do about it today. Never the objective, the central idea, what the audience should do after, or anything else from the conversation; check that the profile doesn't hint at them.
- **The slide text,** in order, as the audience will receive it: titles and bodies, without the part headings, which the audience never sees.
- **How it reaches them:** presented live by someone, or sent to be read alone.

## Prompt

Write it in the user's language and fill in the brackets.

```
You are [audience profile].
[Live: Someone is about to present these slides to you.] [Read alone: Someone sent you this deck to read on your own; nobody will present it.] Here is the text of each slide, in order:

[slide text]

Read it as that person would, and answer briefly:
1. In one sentence, what does this deck want you to think or do?
2. What would you remember tomorrow?
3. Where did you stop following, or where did it seem to jump ahead or go back?
4. What would you doubt or resist, and why?
5. What would you do next?

Answer only from what is in front of you; don't guess what the author meant.
```

## Using the answers

Show the answers next to what the deck intends: the central idea, and what the audience should understand or do (steps 1 and 2). Where they diverge, the text is at fault, not the reader: propose the fix, such as a title that states its point, a missing step between two parts, an argument without its evidence, or a doubt the text doesn't answer. A fix that changes no decision goes straight into the text, marked, so the user sees it at Gate 1.
