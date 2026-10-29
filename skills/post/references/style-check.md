# Style check

Used after writing: run with high stakes when the voice comes from the user's posts, reference texts or a named person; offered otherwise. It compares the finished post with the approved traits, with a reader who has only those and the sample.

## Running the check
- If the session can start a separate agent, start one and give it only what this file says to give it.
- Otherwise, give the user the prompt below, filled in, to paste after the cold reader's prompts in the same new conversation (see `cold-reader.md`), and ask them to paste the answers back.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the reader receives
- The finished post, unit by unit.
- The voice traits, rewritten without any person's name, account or source: a reader given a name judges against its own idea of that person instead of the traits that were approved.
- The approved sample passage.
- Never the conversation, the central idea, the objective, the material or the reference posts the user brought.

## Prompt
Write it in the user's language and fill in the brackets.

```
Below are a list of voice traits, a sample approved as the reference for how a post should sound, and the finished post.

1. For each trait: does the post keep it (yes / mostly / no)? Quote up to three passages that break it, and say how.
2. Name up to three posts or slides that sound least like the sample, and why.
3. List habits that run through the post but aren't in the traits: repeated constructions, stock phrases, network clichés.
4. Quote any sentence that sounds copied or closely paraphrased from a published text.

Judge only how it sounds, not whether the content is right.

Traits:
[traits]

Sample:
[sample]

Post:
[post]
```

## Using the answers
- Fix the passages that break a trait.
- If a trait breaks all over the post, ask whether the trait is wrong for this post and change it in the script with the user's approval, instead of forcing it.
- Cut the habits from answer 3.
- Rewrite anything flagged in answer 4.
