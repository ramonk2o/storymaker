# Fact check

Used in Phase 2, step 4 (run when the lesson states researched facts or ones the user wasn't sure of, or with high stakes; offered otherwise). A lesson's learners believe what it says, so every fact it presents as true is checked against its source by someone who didn't write it and doesn't know which facts the writer was unsure of.

## Running the check
- If the session can start a separate agent, start a fresh one that doesn't inherit this conversation, never a copy of it, and put in its prompt only what this file says to give it. It may search the web if the session allows; it doesn't open any other file.
- Otherwise, give the user the prompt below, filled in, to paste into a new conversation with no access to this one, and ask them to paste the answers back.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the checker receives
- The finished lesson file, with its source list.
- The text of the sources, or the links when the checker can open them.
- Never the conversation, the map, or which facts you doubted.

## Prompt
Write it in the user's language and fill in the brackets.

```
You are checking the facts in lesson material before it is taught to [learners].
Below are the lesson and its sources.

1. List every statement the lesson presents as fact (figures, rules, dates, definitions, how a tool or law works, claims about research). Skip examples the lesson marks as illustrative.
2. For each one, say: SUPPORTED (quote the source in a few words and name it), NOT IN THE SOURCES, CONTRADICTED (by which source, and how), or OUTDATED (newer information, with its source and date).
3. List anything taught as settled that the sources present as disputed.
4. List any worked example or exercise answer whose arithmetic or logic is wrong.

Judge only against the sources [and what you can verify by searching]; don't rely on what you remember.

[lesson]

[sources]
```

## Using the answers
- **Contradicted, outdated or wrong arithmetic:** fix it from the source and tell the user what changed. If the fix changes a key idea or a module's point, it is a proposal the user approves and is written back into the map.
- **Not in the sources:** find a source, ask the user, or mark it `[TO CONFIRM]`; never leave it unmarked.
- **Disputed:** propose in the delivery message whether to teach the disagreement or which side to take, and let the user choose.
- Show the result in the delivery note: how many facts were checked and what changed.
