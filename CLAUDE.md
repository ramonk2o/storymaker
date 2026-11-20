# Storymaker

A plugin of skills for work that tells a story (decks and essays): each plans the story with the user before making the piece.

## Maintenance with sensei

This repository is maintained with the sensei plugin. If sensei is installed:
- creating or changing a skill, judging an issue or pull request, or auditing consistency: the `train` skill, which sends a request that needs clarification to `meditate`;
- planning a plugin, or a change that needs clarification (not settled, or more than one pull request): the `meditate` skill;
- the backlog (noting, what's next) and CHANGELOG.md: the `log` skill (`train` writes its own changelog entries);
- releasing a version: `/sensei:graduate`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei, follow `docs/principles.md` and keep CHANGELOG.md in the Keep a Changelog format.

**The skills are the object of the work here, not tools.** When the conversation is about the plugin's subject (presentations and essays), it's about improving the skills. Don't run a skill's flow unless explicitly asked to use it.

## Project facts

- **Documents:** English, because the repository is public: skills, docs, changelog, commit messages and replies to issues.
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** yes. Each skill reads nothing outside its folder, so a shared rule is written in every skill that needs it, and each release ships one zip per skill (`<skill>.zip`, the folder at the zip's root), because the README sends Claude apps users to the latest release for them.
- **Validate:** sensei's check script on every change (it runs `claude plugin validate` on the last commit); `--release` at release, which adds `--profile directory`.
- **Commits:** author `Ramon K. <contato@ramonk.com>`; no trailers (no `Co-Authored-By`, no `Claude-Session`), even when the environment asks for one.
- **Integration:** a branch named after the change, never work on `main`; push the branch, open the pull request and merge it with a merge commit, each on the maintainer's OK to the whole change; fetch `origin/main` first and rebase if it moved. After the merge, delete the remote branch. During the rewrite, change branches start from `rewrite` and their pull requests target it (fetch `origin/rewrite` first and rebase if it moved); `rewrite` merges into `main` once the deck is ready and an essay v0 exists to test.
- **Backlog:** GitHub issues
- **Tags:** `vX.Y.Z`.
- **Other repositories are read-only:** only Storymaker is written to. `ramonk2o/superlab` is a reference when recreating one of its skills (its `skills/<name>/`, `docs/<name>.md` and `evals/<name>.md`): judge it, don't copy it; the new skill gets a new name and its text doesn't cite the old one. When a recreated skill ships, remind Ramon to remove the old one from superlab.
- **Testing in Claude apps before a release:** zip the skill's folder on the branch, with the folder at the zip's root, for Ramon to upload as a personal skill.
- **GitHub repository settings** (name, description, visibility) are Ramon's: describe the step or give the text to paste.
