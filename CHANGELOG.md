# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

## [0.5.0] - 2026-11-09

Lets a lesson leave practice for afterwards, adds counting scripts to post and lesson, and makes how much is still open choose each skill's path while the stakes choose its checks.

### Added

- lesson: practice can happen in the lesson or afterwards, on the learners' own. A lesson with practice afterwards (expository, close to a talk) keeps each module's key idea, worked example and mistake, opens with a hook, may ask a quick question to the room and ends with a take-home challenge, which the cold learner tries. A talk meant to teach is now in scope, and the description names it.
- post: `scripts/count.py` counts the characters of each post or slide against the limit, as the reader sees them (accents, emoji and flags count once), with the network's weights for links and emoji from the research, and shows where the "see more" cut falls; without code execution, the counts are labeled approximate. The research now looks up how the network counts emoji and other characters.
- lesson: `scripts/minutes.py` counts the words of each section of a lesson file, apart from the quote blocks, and converts them to minutes of talk at 130 words a minute or another pace, leaving out the sections not taught; a module's planned minutes include its practice, so with practice in the lesson its talk plus its practice time fit them. The delivery note says whether the minutes were counted or estimated.

### Changed

- deck, essay, lesson: how much is still open chooses the path, and the stakes choose the checks. Each skill defines its light path exactly and full is everything else, so no piece fits both: essay's light path needs a settled position and a known voice, in a new text under about 1,500 words, a recurring issue or a rework that keeps the argument; lesson's needs command of the subject and a lesson of about an hour or less, a recurring one or settled content; deck's express mode takes settled content (a recurring update, a lesson's slides) or a deck of about 15 minutes or 10 slides or fewer. On the light path, high stakes run the checks after writing (in deck, the title check before the gate) instead of offering them. High stakes are a client, a decision, money or approval, readers or learners likely to resist, the user's reputation directly at play, or a wrong fact that could harm someone; being published under the user's name, reaching many people or teaching students or the public isn't on its own. lesson: the fact check also runs with high stakes. The gate documents carry a Stakes line. Principle 4 states the two axes.
- lesson: the map's rules for practice afterwards and for the buffer live only in `references/learning.md`, which step 1.4 points to, instead of being stated in both.
- deck: the description names the lesson condition as the body does (when the session can load the lesson skill), and its wording is trimmed to fit; a trigger suite for the deck skill now lives in `evals/triggers/deck-*`.
- deck: in the training case, every training deck names each slide's role and marks questions to the room `[question]`, with or without a lesson file, and the slide on where to get help has its own role; the rule moved out of the lesson-file section.
- lesson: in the light path, each module's mistake comes from what the Opening heard learners get wrong; where it left that open, the proposal brings a typical mistake of the subject marked `(hypothesis)`, not `[TO CONFIRM]`, for the gate to confirm.
- deck: a talk meant to teach goes to the lesson skill (or the training case without it); slides of an approved lesson map get express mode unless they face clients or the public; the training case covers practice afterwards.
- The principles of the lesson and deck skills state their boundary: a lesson's shift is a capability, a deck's a belief, a decision or a start.
- deck: the storyline groups slides under the parts of the arc (for a lesson's slides, its modules) unless the deck is about 8 slides or fewer; a part's slides stay together and a closed part isn't reopened except on purpose. The cold reader also says where the deck seemed to jump ahead or go back. The training case keeps each module's slides together, in the lesson map's order.
- lesson: with practice afterwards, the map keeps what each module builds on (a `Builds on:` line in place of the recall), and the key ideas, read in order, must each stand on the ones before.
- deck: for a lesson's slides, each storyline line names its role (in a module: recall, key idea, example, mistake, question, practice or check), in express mode too; a question to the room is a slide of its own, marked `[question]`, inside its module, with its answer in the speaker notes; with practice in the lesson, the final task comes before the recap; with practice afterwards, the recap comes before the take-home challenge, which closes the deck.
- deck: express mode's proposal says where the speaker notes come from and gives the hook's exact line, so they no longer appear for the first time at delivery. For slides from a lesson file, the questions the lesson leaves open join the proposal's round instead of a separate Opening message, and a figure in the lesson that doesn't match its source or another part of it goes to the user as a proposal.
- deck: the lesson path follows one rule: the lesson is the deck's content and the deck decides only how to show it; anything it finds wrong or not doable in the lesson, not only a figure, goes to the user as a proposal. What the learner sees becomes slides in the lesson's order and the teacher blocks become speaker notes; with practice afterwards, the lesson's body goes into the notes as written. A lesson file is enough without its map, and full mode says what it skips. The express proposal's first line names the resistance. lesson: the lesson file carries the one thing, and the slide mapping is stated once, in `lesson-file.md`. A slide that asks learners a question (recall, check, a question to the room) takes the question as its title, the one exception the deck's title principle now names; the lesson's header gives the objective slide and the memorable moment, and the slide count is what the lesson yields. lesson: the cold learner no longer gets the header's objective and one thing.
- deck: in the training case without a lesson file, the length doesn't decide the mode, so an internal training is express unless it meets a full-mode criterion; live or hybrid, about 20% of the duration is buffer, shares of time such as practice are of the minutes left, and only talk time counts toward the slide count, with one slide per practice block or final task. The length rule counts minutes of talk.
- deck, lesson: what the user decided (the topics or points they bring, their order, a split of time) stays, in every path; a change the material, the objective or the time calls for, such as reordering topics whose dependencies run backwards, is a labeled proposal with the reason, next to the user's version, asked before anything is built on it (in the light path and express mode too, before the single proposal), instead of a silent reorder. Whether a module or slide stands on the ones before it is judged by what it needs, not by how its recall is phrased.

### Fixed

- deck: the training case's typical skeleton keeps each mistake inside its module and adds the final task, instead of gathering the common mistakes on one slide after the modules, which contradicted the lesson's order. Its opening with what learners will be able to do stays, as in a lesson with practice in the session.
- deck: for slides of a lesson, the proposal and the script no longer offer an alternative central idea or an arc choice: the central idea is the lesson's one thing and the arc is its modules, in the map's order.
- deck: a deck handed over by the lesson skill no longer offers itself again before starting.
- lesson: taught live, the minutes of the opening, the modules and the close add up to about 80% of the duration, the time budget and the practice share count from there, and the map shows the rest as buffer, instead of filling the slot that `learning.md` says runs about 20% over.
- email, post: approval at the Strategy card or the Post script counts for the plan as shown. Picking another move or hook, or an answer that changes what the plan says, brings the revised plan, in post with the sample passage rewritten from the chosen hook, and asks for approval again, so the user never approves blocks or a sample written for another option. The revised plan comes whole, with the changes marked; the pre-mortem isn't rerun, but a change that undoes how it resolved an objection is named in one line. A changed fact, figure, name or date counts as a change, not wording.
- deck: when the build option leaves no rendered deck (a prompt for an external tool, a build checklist), the cold reader's filled prompt goes with the delivery, marked pending, to run on the exported slides. The prompt's framing follows the format: presented live, sent to read alone, or, for a hybrid deck, missed and read afterwards, with the speaker notes when they travel in the file.
- post: a long single post (one the user asks to be long, or a text or article to turn into one post on a network that allows a long one) starts like a thread or carousel: the Opening when the skill is called by name, the offer when the subject starts it. When the length isn't clear, it is a short post, and a short post whose idea can't be told in about 150 words proposes the script path instead of the draft (declined, the draft follows). When one idea goes to several networks and any of them takes the script path, the whole request does, with each short post drafted whole inside the Post script, approved at the same gate and kept as its final text; each network gets its own hooks and sample passage.
- post: the short post's cold reader gets the whole post in one call only when it fits before the "see more" cut. A short post that runs past the cut keeps the two calls, so the reader decides whether to stop before reading the rest, and the second call still asks whether the rest paid off the opening. A post that fits whole is framed as seen in the feed and no longer asked what it expects from a rest it doesn't have; the second prompt names the network.
- deck: a hybrid deck shared in a form that drops speaker notes (a PDF, images, a view-only link) sends its reading notes as a separate Markdown file, one section per slide, named in the build line of the Production plan or the express proposal, so the readers who weren't there get the text the slides were written to lean on. The cold reader of a hybrid deck gets those notes too.
- deck: the description names a lesson file's slides, so a finished lesson pasted with a request for slides fires the deck instead of slides built with no skill; the trigger suite has more lesson-file cases.
- essay, post, lesson, email: the rules after the checks read the same in every skill. A fix the checks call for needs approval only when it changes an approved decision, as each skill's check step already said, instead of "approved one by one"; without a separate agent, the piece is shown first with the filled prompts and the fixes come once the user pastes the answers back (essay, post and email didn't say); fixes that change no decision are already in the piece shown; and `references/handoff.md` is read before the message that brings the delivery options, whether or not checks ran, so a low-stakes post or a light essay no longer offers them without its rules; without a separate agent, the options come with the fixes, once the answers are back.
- essay, lesson: a tutorial, guide or how-to is lesson material, planned as self-study, for a blog too; essay takes one only when the user explicitly wants an essay instead of a tutorial, and its How-to arc is only for that. A tutorial asked for as a post, thread or carousel stays with the post skill, which now says so. Both Starting sections draw the same line, the lesson's description names tutorials and guides, and the trigger suite has a case for each side.

## [0.4.1] - 2026-11-07

Trims the email skill's description back under the 600-character limit, with the same triggers.

### Fixed

- email: description trimmed back under the 600-character limit, with the same triggers.

## [0.4.0] - 2026-11-04

### Added

- lesson: new skill that plans a lesson (a class, a training or a workshop, on any subject) before writing it: what learners should be able to do at the end and the task that proves it, the cut against the time, and a map of every module with its key idea, recall, worked example, the mistake it tackles, practice in steps and a hinge question. One gate, the Lesson map, judged on one module written in full. When the user is learning the subject to teach it, it researches the terrain before the map and the rest after the gate, in a single call to a research skill when the session has one. Writes a lesson file with a learner layer and notes for whoever teaches; a fact check against the sources and a cold learner who works through the exercises run after writing. Offers to turn the file into slides when the session can load the deck skill.
- Principles of the lesson skill in `docs/principles.md`.

### Changed

- deck: a lesson or training whose content isn't settled is planned by the lesson skill first when the session has it; the training case says how to build from a lesson file without reopening its content.
- essay: its out-of-scope list names the lesson skill for lesson or training material.

## [0.3.0] - 2026-11-03

### Changed

- deck, essay, post, email: the cold reader and the style check run in a fresh agent that doesn't inherit the conversation, with the material in its prompt and the instruction not to open other files; the deck's cold reader gets the rendered slides without speaker notes.
- post: being signed by the user no longer makes a post high stakes on its own; high stakes are a position others will push back on, a brand's or public figure's account, a sensitive subject, or the user's professional reputation directly at play. A high-stakes short post now gets the pre-mortem's likeliest failures below the draft, which it skipped before.
- Principles: depth matches the stakes now notes that a skill whose path follows the format says in its own section what the stakes decide; the post's checks principle follows the new definition of high stakes.
- deck, essay: the central-idea examples in the case files no longer use dashes or "not X, but Y" reversals, so they don't teach the habits the writing rules forbid.

### Fixed

- deck: express mode names the references it builds from, and delivery points to `references/delivery.md` for speaker notes and likely questions in both modes.
- email: the light path's draft uses the move from `references/strategy.md`, as that file says.
- post: the short path's draft sets the voice by `references/style.md`, as that file says.
- README: says how to turn on auto-update or update by hand, since third-party marketplaces don't update on their own.

## [0.2.0] - 2026-10-29

### Added

- email: new skill that plans emails and long messages with something at stake (bad news, a no, a hard ask, a disagreement, an apology, an explanation, an announcement to many; also long Slack or WhatsApp messages and letters) before writing them: what the reader should do after reading, the shape of the audience (one, a few, many) and the direction of power, the move, the tone on three axes (proximity, firmness, warmth) and the subject line, with each move shown on a real opening. Light emails come back as a draft in the first reply; full ones have one gate, the Strategy card, after a pre-mortem. The voice is the user's own; a cold reader per recipient who matters writes the reply they would send. Delivered in the conversation, never sent.
- Principles of the email skill in `docs/principles.md`.

### Changed

- essay, post, deck: their out-of-scope lists name the email skill for emails and work messages.

## [0.1.0] - 2026-10-29

### Added

- essay: new skill that plans long texts (essays, blog posts, opinion columns, newsletter issues) before writing them: the central idea, the arc, a one-line outline of every paragraph and the voice, set by a register, the user's own texts, reference texts or a named person to take inspiration from, shown on a sample passage. One gate on the Essay outline; a reverse outline for reworking drafts; a cold reader that also outlines the text back to catch drift, and a style check.
- deck: plans a presentation with the user before any slide is built, then builds and checks it. The Opening settles the audience's shift (what they believe and do today, and after), its resistance (logical, emotional or practical) and the format, through hypotheses the user reacts to, so a user without a clear vision is helped to find one. The story phase proposes the central idea with a point of view and what is at stake (two or three candidates when the user has no clear view), the triage and a 3-minute version of the story; then answer first or tension, the arc, hook, memorable moment and close, a storyline of assertion titles and a stress test that opens with a pre-mortem; a cold reader checks the titles before the Script. The visual phase brings visual concepts, the build options the session has and a low-fidelity prototype in one message, then the full Production plan with speaker notes and likely questions. The build is reviewed on the rendered slides (the plan, a three-second glance test, layouts that vary by the slide's job) and read by a cold reader who also says what they would still resist. Express mode, for internal, low-risk or recurring decks, has one proposal and a single gate. Cases for results analysis, strategy proposals, idea pitches (with an investor-pitch variant), research, project status, training, campaign concepts and talks, and a Recurring blueprint for periodic decks.
- Principles of the essay skill in `docs/principles.md`.
- Principles of the deck skill in `docs/principles.md`.
- Repository skeleton: README, MIT license, changelog, plugin and marketplace manifests, skill principles and the maintenance project's instructions.
- post: new skill that plans social posts before writing them — single posts, captions, threads and carousels, for one network or several — with the hook picked from first lines written in full, a one-line script per post or slide, a voice from a register, the user's posts or someone they admire, and a cold reader who meets the post in a feed. Short posts come back as a draft in the first reply; it can also turn a text into a post.

### Changed

- essay: its out-of-scope list names the post skill for social posts, threads and carousels.
- deck: carousels for social networks are out of scope and go to the post skill.
