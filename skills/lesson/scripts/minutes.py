#!/usr/bin/env python3
"""Count the words of each section of a lesson file and convert them to minutes.

Usage: python3 minutes.py LESSON.md [--wpm 130]

Each "## " heading starts a section. Words outside quote blocks are what is
said or read in the lesson; words in quote blocks (the recall line and the
notes for whoever teaches) are counted apart and left out of the minutes.
A teacher block's planned minutes ("· ~12") are shown next to the count;
they include practice, which words can't measure (references/writing.md).
The last --not-taught sections (default 3: support material, answers and
sources, in the lesson file's order) are left out of the total.
The default of 130 words a minute is for what is said live; pass a lower
--wpm for text learners read.
"""
import argparse
import re
import sys

WORD = re.compile(r"[^\W_]+(?:['’-][^\W_]+)*", re.U)
PLANNED = re.compile(r"·\s*~\s*(\d+)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--wpm", type=float, default=130)
    ap.add_argument("--not-taught", type=int, default=3)
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    sections = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append({"title": line[3:].strip(), "said": 0, "quoted": 0, "planned": None})
            continue
        if not sections:
            continue
        s = sections[-1]
        if line.lstrip().startswith(">"):
            s["quoted"] += len(WORD.findall(line))
            m = PLANNED.search(line)
            if m and s["planned"] is None:
                s["planned"] = int(m.group(1))
        else:
            s["said"] += len(WORD.findall(re.sub(r"[*_`#]", " ", line)))
    if not sections:
        sys.exit("No '## ' sections found.")
    taught = len(sections) - a.not_taught if len(sections) > a.not_taught else len(sections)
    total = 0.0
    for i, s in enumerate(sections):
        mins = s["said"] / a.wpm
        plan = f"  (planned ~{s['planned']}, practice included)" if s["planned"] is not None else ""
        mark = "" if i < taught else "  [not taught]"
        if i < taught:
            total += mins
        print(f"{s['title']}: {s['said']} words, {mins:.1f} min of talk{plan}; {s['quoted']} words in quote blocks{mark}")
    print(f"\nTotal talk: {total:.1f} min at {a.wpm:g} words a minute, in the {taught} sections taught.")


if __name__ == "__main__":
    main()
