# Cold reader

Used in step 5, on the outline the user reviewed, before the gate. A model inside this conversation already knows what the text wants to say, so it can't play the reader.

## Running it

- If the session can start a separate agent, start a fresh one that doesn't inherit this conversation, with only the prompt below, filled in, and the instruction not to open any other file.
- Otherwise, give the user the filled prompt to paste into a new conversation with no access to this one, and ask them to bring back the answers.
- If the user prefers to skip it, say in one line what it would catch; if they still skip, write "cold reader: not run" in the gate request.

## What the reader gets

- **The reader profile:** who they are, what they know about the subject, what they believe and do about it today. Never the objective, the central idea, what the reader should do after, or anything else from the conversation; check that the profile doesn't hint at them.
- **The outline,** in order: the title and the paragraph lines, without the part headings, which the reader never sees.
- **How it reaches them:** a blog post they clicked, a newsletter in their inbox, a column in a publication, a document someone sent them.

## Prompt

Write it in the user's language and fill in the brackets.

```
You are [reader profile].
A text is about to reach you as [how it reaches them]. Before it is written, here is its title and one line for each paragraph, in order, saying what that paragraph will say:

[outline]

Read it as that person would, and answer briefly:
1. In one sentence, what does this text want you to think or do?
2. Where would you stop reading, or where does it seem to jump ahead or go back?
3. What would you doubt or resist, and why?
4. What does it assume you know that you don't?
5. After reading it, what would you think or do?

Answer only from what is in front of you; don't guess what the author meant.
```

## Using the answers

Show the answers next to what the text intends: the central idea, and what the reader should understand or do (steps 1 and 2). Where they diverge, the outline is at fault, not the reader: propose the fix, such as a line that states its point, a missing step between two parts, an argument without its evidence, or a doubt the text doesn't answer. A fix that changes no decision goes straight into the outline, marked, so the user sees it at the gate.
