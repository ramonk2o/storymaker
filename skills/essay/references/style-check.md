# Style check

Used in Phase 3: run in the full path when the voice comes from the user's texts, reference texts or a named person; offered otherwise. It compares the finished text with the approved style sheet, with a reader who has only the two and the sample.

## Running the check
- If the session can start a separate agent, start one and give it only what this file says to give it.
- Otherwise, give the user the prompt below, filled in, to paste after the cold reader's prompts in the same new conversation (see `cold-reader.md`), and ask them to paste the answers back.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the reader receives
- The finished text.
- The traits of the style sheet, rewritten without any person's name, book or source line: a reader given a name judges against its own idea of that person instead of the traits that were approved.
- The approved sample passage, as the reference for how the text should sound.
- Never the conversation, the central idea, the objective, the material or the reference texts the user brought.

## Prompt
Write it in the user's language and fill in the brackets.

```
Below are a style sheet, a sample passage approved as the reference for how a text should sound, and the finished text.

1. For each trait: does the text keep it (yes / mostly / no)? Quote up to three passages that break it, and say how.
2. Name up to three passages that sound least like the sample, and why.
3. List habits that run through the text but aren't in the style sheet: repeated constructions, stock phrases, reflexive patterns.
4. Quote any sentence that sounds copied or closely paraphrased from a published text.

Judge only how it sounds, not whether the content is right.

Style sheet:
[traits]

Sample passage:
[sample]

Text:
[text]
```

## Using the answers
- Fix the passages that break a trait.
- If a trait breaks all over the text, ask whether the trait is wrong for this text and change it in the outline with the user's approval, instead of forcing it.
- Cut the habits from answer 3.
- Rewrite anything flagged in answer 4.
