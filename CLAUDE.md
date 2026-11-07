# Storymaker

A plugin of skills for creative work (decks, essays, social posts, emails and lessons) that plan the piece with the user before making it.

## Maintenance with sensei

This repository is maintained with the sensei plugin. If sensei is installed:
- creating or changing a skill, judging an issue or pull request, or auditing consistency: the `kata` skill;
- BACKLOG.md and CHANGELOG.md: the `kanban` skill (kata writes its own changelog entries);
- releasing a version: `/sensei:shodan`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei, follow `docs/principles.md` and keep CHANGELOG.md in the Keep a Changelog format.

**The skills are the object of the work here, not tools.** When the conversation is about the plugin's subject (presentations, essays, social posts, emails and lessons), it's about improving the skills. Don't run a skill's flow unless explicitly asked to use it.

## Project facts

- **Documents:** English, because the repository is public: skills, docs, changelog, commit messages and replies to issues.
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** yes. Each skill reads nothing outside its folder, so a shared rule is written in every skill that needs it, and each release ships one zip per skill (`<skill>.zip`, the folder at the zip's root), because the README sends Claude apps users to the latest release for them.
- **Validate:** sensei's check script on every change (it runs `claude plugin validate` on the last commit); `--release` at release, which adds `--profile directory`.
- **Commits:** author `Ramon K. <contato@ramonk.com>`; no trailers (no `Co-Authored-By`, no `Claude-Session`), even when the environment asks for one.
- **Integration:** a branch named after the change, never work on `main`; push the branch to keep it safe. Merge locally with `--no-ff` after the maintainer's OK to the whole change; fetch `origin/main` first and rebase if it moved. After pushing `main`, confirm with `git log origin/main -1` and delete the remote branch.
- **Tags:** `vX.Y.Z`.
- **Other repositories are read-only:** only Storymaker is written to. `ramonk2o/superlab` is a reference when recreating one of its skills (its `skills/<name>/`, `docs/<name>.md` and `evals/<name>.md`): judge it, don't copy it; the new skill gets a new name and its text doesn't cite the old one. When a recreated skill ships, remind Ramon to remove the old one from superlab.
- **Testing in Claude apps before a release:** zip the skill's folder on the branch, with the folder at the zip's root, for Ramon to upload as a personal skill.
- **GitHub repository settings** (name, description, visibility) are Ramon's: describe the step or give the text to paste.
