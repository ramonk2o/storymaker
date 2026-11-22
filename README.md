# Storymaker

Skills for work that tells a story: decks and essays. Each one plans the story with you first, then checks it with a reader who never saw the conversation, before making the piece.

Most AI-made slides and texts start from a blank page and a vague prompt. Storymaker starts from the point: what the piece must say, to whom, and in what order. Only then does it design or write.

## What you get

| Skill | You bring | You get |
|---|---|---|
| **deck** | A message to get across, plus any notes, data or a draft | The central idea, the arc, the text of every slide, visual concepts, then the built deck |
| **essay** | An argument to make, plus loose ideas, sources or a draft | The central idea, the arc, one line per paragraph, a sample in your voice, then the full text |

**Use deck when** the presentation must change what an audience understands or does, live or read alone.
**Use essay when** you want an essay, article, column or blog post that takes the reader through an argument.
**Not for:** agendas, status updates, summaries, minutes or proofreading.

## How it works

1. **You call the skill** with whatever you have: a topic, notes, a draft.
2. **It asks a few questions at a time** (up to five), each with a recommended answer, so you only confirm or correct. For example: "ok to all, except 3".
3. **It plans the story in writing**, then has it read by a reader who never saw the conversation. If that reader gets lost, the plan is fixed before anything is made.
4. **You approve the text.** Nothing moves on without a clear "OK".
5. **It makes the piece**: the slides, or the full text.

It never invents figures, facts or quotes. What only you know stays marked `[TO CONFIRM]` until you say it.

## Try it

**Claude Code**

```
/storymaker:deck I need to convince our leadership to move the support team to a 4-day week. I have survey results in survey.csv.
```

```
/storymaker:essay An op-ed arguing that remote work killed the office but not the city. Here are my notes: ...
```

**Claude apps**

> Use the deck skill. I need a 10-minute presentation for investors about our pilot results. Notes attached.

A first round looks like this:

```
1. Who is in the room, and what do they believe today?
   → I recommend: the leadership team, who see the 4-day week as a cost —
     the deck has to turn it into a retention argument.

2. What should they decide at the end?
   → I recommend: approve a 3-month pilot — a smaller ask than a permanent change.
```

You answer "ok to all", or correct the ones you disagree with.

You call the skills yourself; they never start on their own.

## Install

### Claude Code

```
/plugin marketplace add ramonk2o/storymaker
/plugin install storymaker@storymaker
```

### Claude apps (claude.ai, desktop, mobile)

1. Download `deck.zip` or `essay.zip` from the [latest release](https://github.com/ramonk2o/storymaker/releases/latest).
2. In Claude, open Settings and upload it as a skill.
3. Start a chat and ask Claude to use the skill by name.

Each skill installs on its own.

<details>
<summary>Updating in Claude Code</summary>

Auto-update is off by default for marketplaces outside Anthropic's. To turn it on, run `/plugin`, open the Marketplaces tab, select `storymaker` and choose Enable auto-update. To update by hand, run `claude plugin update storymaker@storymaker`.
</details>

## FAQ

**Which language does it use?** The skills are written in English and talk to you in yours.

**Can I bring a draft I already have?** Yes. Both skills work from loose ideas, notes, sources or a draft to rework.

**Will it write in my voice?** The essay skill proposes a sample passage first, in a register you pick, in your own texts, or in traits it researches from an author. It never copies passages.

**What tools does the deck skill build with?** Whatever your session has.

## Status

Early and experimental (before 1.0). See [CHANGELOG.md](CHANGELOG.md).

## Contributing

Issues and pull requests are welcome. The most useful report is a real case: what you asked the skill, what it did and what it should have done. The principles every skill follows are in [docs/principles.md](docs/principles.md).

## License

[MIT](LICENSE)
