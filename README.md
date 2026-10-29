# Storymaker

Skills for creative work. Each skill plans the piece with you before making it — what it has to say, what goes in, how it holds attention and what a good result looks like — and only then builds it, so what you end up with does its job the first time.

The skills are written in English and talk to you in your own language.

## Skills

- **deck** — plans a presentation with you before any slide is built: what it must change in the audience, the message, the story and how it holds attention, then the visual concept and production plan. Then it builds the deck, reviews the rendered slides, checks it with a reader who never saw the plan, and hands over speaker notes and the likely questions with their answers.
- **essay** — plans a long text with you before writing it — essays, blog posts, opinion columns and newsletter issues: the point it makes, the arc, a one-line outline of every paragraph so you can judge the order before any prose exists, and the voice, taken from a register, your own texts, texts you admire or someone you want to take inspiration from, shown on a sample passage. Then it writes the text and checks it with a reader who never saw the plan. Bring a draft and it starts by outlining it back, so you can see where the order breaks.

## Status

Early and experimental (before 1.0). Skills are being built one at a time. See [CHANGELOG.md](CHANGELOG.md) for what has changed.

## Install

### Claude Code

```
/plugin marketplace add ramonk2o/storymaker
/plugin install storymaker@storymaker
```

The plugin updates when a new version is released.

### Claude apps (claude.ai, desktop, mobile)

Each skill can be installed on its own: download its zip (`deck.zip`, `essay.zip`) from the [latest release](https://github.com/ramonk2o/storymaker/releases/latest) and upload it as a skill in your Claude settings.

## How it is built

The principles every skill follows, and the questions used to judge a proposed change, are in [docs/principles.md](docs/principles.md).

## Contributing

Issues and pull requests are welcome. The most useful report is a real case: what you asked the skill, what it did and what it should have done.

## License

[MIT](LICENSE)
