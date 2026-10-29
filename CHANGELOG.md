# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

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
