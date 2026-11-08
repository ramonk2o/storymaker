# The lesson file

Used in step 1.6 (the sample module) and in Phase 2 (writing). The lesson is delivered as one Markdown file with a fixed structure, so it can be taught as it is, read by learners, or handed to the deck skill or another tool without rework. It has two layers: what the learner sees, and notes for whoever teaches, marked so they can be stripped.

## Structure

```markdown
# [Lesson title]

**For:** [learners] · **Duration:** [minutes] ([practice share] practice, or "practice afterwards") · **Format:** [live | online | self-study]
**Before this lesson:** [prerequisites, or "none"]
**By the end you will be able to:** [objective(s), as actions]
**The one thing:** [what learners should remember tomorrow]

## Why this matters
[Two to four sentences in the learners' terms.]

## M1. [Key idea, as a full sentence]
> **Recall:** [question]

[Explanation, short, next to its example.]

**Example:** [worked, step by step]

**Watch out:** [the mistake, why it is tempting, where it fails]

**Try it:** [guided practice, then practice alone]

**Check:** [hinge question with options]

> **For whoever teaches** · ~[minutes]
> - Hinge answers: [right one] · [wrong one] → [mistake it reveals, what to do]
> - [Where learners get stuck; what to say; what to cut if time runs short]

## M2. …

## Final task
[The task, the case and the tools allowed.]

> **For whoever teaches:** [what to look for while they work; the common wrong answers and what to say]

## Recap
[The key ideas, one line each, in order.]

## Support material
- **Glossary:** [term — definition, in the lesson's words]
- **To answer in a few days:** [three to five retrieval questions]
- **To go further:** [what was cut on purpose, with where to read it]

## Answers
[Per module: the answer to each practice and check, with why each wrong option is wrong; then the final task's model answer and the answers to the questions for later.]

## Sources
[Every source the lesson's facts rest on, with its date when it changes. Facts stated by the user: "stated by [role]".]
```

## Rules
- Headings and labels in the lesson's language; keep the structure.
- The key ideas are exactly the map's, word for word; read in order they are the recap.
- Teacher notes go only in the marked blocks. Answers for the learner go in the Answers section, after the lesson, so the learner tries first; a learner version strips the teacher blocks and keeps the Answers.
- Illustrative data is marked as such the first time it appears ("a fictional shop", "numbers for illustration").
- A `[TO CONFIRM]` marker stays visible in the text and is listed in the delivery note.

## When practice comes afterwards
- A module keeps its key idea, explanation, **Example** and **Watch out**; it drops **Recall**, **Try it** and **Check**, and one or two modules in the whole lesson carry a **Question for the room:** [question], with its answer in the teacher block.
- "Why this matters" opens with the hook.
- "Final task" becomes **Try it on your own:** the case (one of their own), the steps, what a good result looks like and where to look when stuck. Its teacher block says how to introduce it and where people usually get stuck.
- The body is what is said: the talk's script, written to be heard. The teacher blocks keep only cues, timing and the answers to the questions for the room.
- The Answers section keeps the questions for the room, a model result of the challenge and the answers to the questions for later.

## Into slides
When the deck skill builds slides from this file, the file is its content, with or without the map: what the learner sees becomes slides in the lesson's order (support material and sources stay in the file), with the key ideas as slide titles and one part per module; the teacher blocks become speaker notes; with practice afterwards, the body becomes the slides and their speaker notes, and the challenge closes the deck, after the recap. Say so in the handoff so the deck treats the content as settled.
