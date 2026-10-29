# Cold reader

Used in Phase 3 (run in the full path, offered in the light path). A cold reader checks whether the text works for someone who has only the text, which is exactly the situation of its real reader, and outlines it back so you can see where the writing drifted from the plan.

## Running the check
- If the session can start a separate agent, start one and give it only what this file says to give it.
- Otherwise, give the user the prompts below, filled in, to paste into one new conversation with no access to this one, each only after the previous one has been answered, and ask them to paste the answers back. When the style check also runs, its prompt goes last in that same conversation, so the reader judges the text before learning how it was meant to sound.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the reader receives
- The finished text, as it will be read, with its title.
- The reader profile from the Essay outline: who they are, what they already know about the subject, what they think about it today. Check that it doesn't hint at what the text wants.
- How the text reaches them: an essay in a publication, a blog post they clicked, a newsletter in their inbox, a column in an outlet.
- Never the conversation, the outline, the central idea, the objective, the style sheet or the sample passage.

## Two calls
A reader handed the whole text can't unread it, so the opening is tested first. With a separate agent, the first call gets only the preview; the whole text goes to a second agent, or to the same one only after it has answered.

## Prompt 1 — the preview
Write it in the user's language and fill in the brackets. The preview is the title and the first paragraph; for a newsletter, the subject line, the preview text and the first paragraph.

```
You are [reader profile: who you are, what you already know about the subject, what you think about it today].
This is what you see of a text [in … | as a blog post | as a newsletter in your inbox | as a column in …] before choosing whether to read on:

[preview]

Answer briefly:
1. Would you keep reading? Why?
```

## Prompt 2 — the whole text
```
You are [the same reader profile].
You now have the whole text. Read it once, as that person would, and answer briefly:
2. In one sentence, what is this text telling you?
3. After reading, what would you think or do?
4. Where would you have stopped reading? Quote the first words.
5. Which claim would you not believe without more evidence?
6. What did the text assume you knew that you didn't?
7. Summarize each paragraph, in order, in one sentence of up to 12 words saying what it claims. Number them.

Answer only from the text; don't guess what the author meant.

[text]
```

## Using the answers
- Answer 1 tests the opening; a "no" sends you back to the title and the opening line of the outline.
- Compare answer 2 with the central idea and answer 3 with the objective. A difference in either is a problem of the text, not of the reader.
- Answer 4 points to something to cut, move or shorten.
- Answer 5 asks for evidence, or a `[TO CONFIRM]` marker.
- Answer 6 asks for context.
- Answer 7 is the reverse outline. Compare it with the approved outline line by line, as `outline.md` says: a paragraph whose summary doesn't match its planned claim drifted; two paragraphs with the same summary repeat; a planned claim no summary carries is missing from the text.
- Show the answers next to what was expected and propose fixes. Any fix that changes an approved decision needs the user's ok and is written back into the outline.
