# Storymaker

Skills for work that tells a story. Each skill plans the story with you before making the piece, and checks it with a reader who never saw the conversation.

The skills are written in English and talk to you in your own language.

## Skills

- **deck** — plans a presentation that must get a message across, presented live or read alone: the central idea, the arguments, the arc and the text of every slide, settled with you and read by a reader who never saw the conversation before any visual work. Then it proposes visual concepts that give each kind of information a form (a flow, a side-by-side comparison, dots, a metaphor), plans how each slide is illustrated, shows a few slides drawn, and builds the deck with the tools your session has. Slides that only support a meeting, such as an agenda or a status update, are left out. It runs only when you call it: `/storymaker:deck` in Claude Code, or by asking Claude to use the deck skill in the Claude apps.
- **essay** — plans a text in prose that takes its reader through an argument, such as an essay, an article, a column or a blog post: the central idea, the arguments, the arc and one line for every paragraph, read by a reader who never saw the conversation, then a sample passage in the voice you want (a register, your own texts, or an author it researches and takes traits from, never passages). Then it writes the whole text. Summaries and proofreading are left out. It runs only when you call it: `/storymaker:essay` in Claude Code, or by asking Claude to use the essay skill in the Claude apps.

## Status

Early and experimental (before 1.0). Skills are being rebuilt one at a time. See [CHANGELOG.md](CHANGELOG.md) for what has changed.

## Install

### Claude Code

```
/plugin marketplace add ramonk2o/storymaker
/plugin install storymaker@storymaker
```

Auto-update is off by default for marketplaces outside Anthropic's. To get new versions automatically, run `/plugin`, open the Marketplaces tab, select `storymaker` and choose Enable auto-update. To update by hand, choose Update marketplace there, or run `claude plugin update storymaker@storymaker` in your shell.

### Claude apps (claude.ai, desktop, mobile)

Each skill can be installed on its own: download its zip (`deck.zip`, `essay.zip`) from the [latest release](https://github.com/ramonk2o/storymaker/releases/latest) and upload it as a skill in your Claude settings.

## How it is built

The principles every skill follows, and the questions used to judge a proposed change, are in [docs/principles.md](docs/principles.md).

## Contributing

Issues and pull requests are welcome. The most useful report is a real case: what you asked the skill, what it did and what it should have done.

## License

[MIT](LICENSE)
