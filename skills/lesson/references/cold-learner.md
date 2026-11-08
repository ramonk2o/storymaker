# Cold learner

Used in Phase 2, step 5 (run in the full path, offered in the light path). A cold learner checks whether the lesson teaches what it means to: someone with the learners' starting point works through the material and does its checks and its final task without the answers. Where they fail, the lesson failed.

## Running the check
- If the session can start a separate agent, start a fresh one that doesn't inherit this conversation, never a copy of it, and put in its prompt only what this file says to give it, with the instruction not to open any other file and not to search.
- Otherwise, give the user the prompt below, filled in, to paste into a new conversation with no access to this one, and ask them to paste the answers back.
- If the user prefers to skip it, record "not run" in the delivery note.

## What the learner receives
- The learner profile from the map: who they are and what they already know. Leave out the mistakes they usually make, which are what the modules tackle, and check that nothing in it hints at the objective.
- How the lesson reaches them: in a live class, online, or on their own.
- The lesson file **without** the teacher blocks, the Answers section, or the header's objective and one-thing lines.
- Never the conversation, the map, the objective or the answer key.

## The model's problem
A model knows most subjects already, so it would pass any test from memory. The prompt asks it to answer only from what the material taught, and the most useful signal is where it had to step outside the material to answer.

## Prompt
Write it in the user's language and fill in the brackets.

```
You are [learner profile: who you are, what you already know about this].
You are taking this lesson [in a live class | online | on your own]. Work through it in order, as that person would.

Rules: answer only with what the lesson taught you plus what the profile says you know. When you would need something the lesson didn't give you, don't answer from general knowledge: write "NOT TAUGHT" and say what was missing.

For each module:
1. Answer the recall question, the "Try it" practice and the "Check" question.
2. Where did you get lost, or what term did you not know?

At the end:
3. Do the final task, showing your work.
4. In one sentence, what can you now do that you couldn't before?
5. What would you remember tomorrow?
6. Which part felt too long, and which too fast?

[lesson for learners]
```

## With practice afterwards
The learner works through the lesson as a listener or reader, then tries the challenge as they would at home. In the prompt, item 1 becomes "Answer the question for the room, if the module has one" and item 3 becomes "Do the 'Try it on your own' challenge on a plausible case of yours, following its steps and showing your work; say where you got stuck". When the challenge needs a tool the learner doesn't have, it describes each step it would take, and is judged on whether the steps are complete and correct.

## Using the answers
- Compare each answer with the Answers section and the teacher blocks. A wrong hinge answer that matches one of its planned wrong options means the module didn't take that mistake apart; one that matches none means the question or the explanation is unclear.
- Every "NOT TAUGHT" is a gap: a missing step, a term not defined, a prerequisite the profile doesn't have.
- A failed final task or challenge sends you to the module it depends on; the task itself is rarely the problem.
- Compare answer 4 with the objective and answer 5 with the one thing; a difference is a problem of the lesson.
- Show the answers next to what was expected and propose fixes. Any fix that changes an approved decision needs the user's ok and is written back into the map.
