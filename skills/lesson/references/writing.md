# Writing the lesson

Used in step 1.6 (the sample module) and in Phase 2. These are rules the model doesn't follow on its own; they hold for every kind of lesson, and the case file adds to them. Facts follow "Nothing invented" in `SKILL.md`; teaching rules are in `references/learning.md`.

## The map is the specification
- One module per map block, in order, landing its key idea with the example, the mistake and, when it has them, the practice and the hinge question listed there.
- A module that wants to teach something its block doesn't is a sign the map needs to change: stop and ask.

## Explaining
- Talk to the learner ("you"), in the register the learners use. Short sentences; one idea per paragraph.
- Concrete first when the idea is new: the example, then the rule it shows. Abstract claims get a specific detail or they go.
- Define a term the first time, in plain words, before using it; add it to the glossary. No jargon the learners don't have yet.
- One term per concept; never vary words for elegance.
- Certainty matches the source: state what is supported, say "usually" or "in most cases" only when the source does.

## Examples and practice
- Worked examples show every step, including the one experts skip.
- Exercise data is realistic for these learners; illustrative data is marked as such.
- Every practice has its answer in the Answers section, with why each wrong option is wrong.
- Instructions for an activity say what to do, with whom, for how long and what to bring back.

## Habits to avoid
These mark a lesson written on autopilot:
- An opening that restates the title or the agenda.
- A wall of explanation before the first example.
- "Not X, but Y" reversals; lists of three by reflex; rhetorical questions as transitions.
- Motivational filler ("this is a fascinating topic").
- Bullet lists where a worked example should be.
- Frequent dashes.

## Length
Write to the minutes in the map: about 130 spoken words a minute for what is said live, less for what learners read during the lesson. With practice afterwards, the body is what is said, so the count applies to it. A module that runs long gets cut, not squeezed. When the session can run code, check the written lesson with `scripts/minutes.py` (a lower `--wpm` for what learners read); otherwise the minutes are an estimate, and the delivery note says so.
