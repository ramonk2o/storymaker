# Cold reader

Used after writing: run in the full path, offered in one line in the light path. A model inside this conversation knows what the email means to say; a reader standing in for each recipient shows how it lands, and the reply they would write shows it best.

## Running the check

- If the session can start a separate agent, start one per reader and give each only what this file says to give it.
- Otherwise, give the user the prompt below, filled in, to paste into a new conversation with no access to this one, one conversation per reader, since a reader who has played someone else already knows too much. Ask them to paste the answers back.
- If the user prefers to skip it, record "not run" in the delivery.

## How many readers

- **One reader:** one, with the recipient's profile.
- **A few:** one per recipient who matters, up to three.
- **Many:** three: the reader most affected, the most skeptical, and someone who receives it forwarded without the thread.

## What each reader receives

- The email as it will arrive: the subject, the sender's relationship to them, the To and Cc line, the body; for a reply, the thread they already have.
- Their profile from the card: who they are, what they know, want and fear, and what they are probably feeling now. Check that it doesn't hint at what the email wants.
- Never the conversation, the card, the objective, the move, the tone positions or the moves that weren't chosen.

## Prompt

Write it in the user's language and fill in the brackets.

```
You are [reader profile]. You receive this [email | message] from [the sender's relationship to you].

[the thread so far, for a reply]

[the email as it arrives]

Answer briefly, as that person:
1. In one sentence, what is this telling you, and what does it want from you?
2. What do you feel reading it? Quote the line that most caused it.
3. What would you do now, and by when?
4. Which line would you take badly, or read differently from what the sender probably meant?
5. What do you need that is missing, or what would you doubt?
6. Write the reply you would send.

Answer only from what you received; don't guess what the sender meant.
```

For the forwarded reader, add: "You weren't in this thread. What do you conclude about the sender?"

## Using the answers

- Compare answer 1 with the message and answer 3 with the objective and the close. A difference is a problem of the email, not of the reader.
- Answers 2 and 4 point to lines to rewrite; a line flagged by more than one reader goes.
- Answer 5 asks for a fact, or a `[TO CONFIRM]` marker.
- Answer 6 is the most revealing: compare it with the reply the user hopes for. A reply that argues with a line the email didn't need shows what to cut.
- Show the answers next to what was expected and propose fixes. Any fix that changes an approved decision needs the user's ok and is written back into the card.
