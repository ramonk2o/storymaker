# Cold reader

Used after writing: run when the stakes are high, offered in one line otherwise. A cold reader checks whether the post works for someone who meets it in a feed with no context, which is exactly the situation of its real reader, and summarizes it back unit by unit so you can see where the writing drifted from the script.

## Running the check
- If the session can start a separate agent, start one and give it only what this file says to give it.
- Otherwise, give the user the prompts below, filled in, to paste into one new conversation with no access to this one, each only after the previous one has been answered, and ask them to paste the answers back. When the style check also runs, its prompt goes last in that same conversation, so the reader judges the post before learning how it was meant to sound.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the reader receives
- The finished post, as it will appear: the units in order, with the visual notes of a carousel standing in for the images, and the caption.
- The reader profile from the plan: who they are, whether they follow the account, what they already think about the subject. Check that it doesn't hint at what the post wants.
- The network.
- Never the conversation, the script, the central idea, the objective, the voice traits or the hooks that weren't chosen.

## Two calls
A reader handed the whole post can't unread it, so the stop is tested first. With a separate agent, the first call gets only what the feed shows; the whole post goes to a second agent, or to the same one only after it has answered.

## Prompt 1 — the feed
Write it in the user's language and fill in the brackets. What the feed shows is: for a single post, the lines before the "see more" cut; for a thread, the first post; for a carousel, the cover slide (its words and visual note) and the caption's first line.

```
You are [reader profile]. You are scrolling [network], quickly, between other posts.
This is what you see of one post:

[what the feed shows]

Answer briefly:
1. Would you stop, expand or swipe? Why, in one line?
2. What do you expect the rest to give you?
```

## Prompt 2 — the whole post
```
You are [the same reader profile]. You stopped and now see the whole post. Read it as that person would, and answer briefly:
3. In one sentence, what did this post tell you?
4. Did the rest give you what the opening promised?
5. At which post or slide would you have stopped? Quote its first words.
6. Which claim would you not believe without more evidence?
7. Would you save, share, reply or do nothing? Why?
8. Summarize each post or slide, in order, in one sentence of up to 12 words saying what it claims. Number them.

Answer only from the post; don't guess what the author meant.

[post]
```

For a short post, merge both prompts into one call, skipping questions 4, 5 and 8.

## Using the answers
- A "no" on answer 1 sends you back to the hook; answer 2 against the script shows whether the hook promises the right thing, and answer 4 whether the post pays it off.
- Compare answer 3 with the central idea and answer 7 with the objective. A difference in either is a problem of the post, not of the reader.
- Answer 5 points to a unit to cut, merge or move.
- Answer 6 asks for evidence, or a `[TO CONFIRM]` marker.
- Answer 8 is the reverse outline. Compare it with the approved script line by line, as `outline.md` says.
- Show the answers next to what was expected and propose fixes. Any fix that changes an approved decision needs the user's ok and is written back into the plan.
