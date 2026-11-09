#!/usr/bin/env python3
"""Count the words of each section of a lesson file and convert them to minutes.

Usage: python3 minutes.py LESSON.md [--wpm 130]

Each "## " heading starts a section. Words outside quote blocks are what is
said or read in the lesson; words in quote blocks (the recall line and the
notes for whoever teaches) are counted apart and left out of the minutes.
A teacher block's planned minutes ("~12") are shown next to the count.
The default of 130 words a minute is for what is said live
(references/writing.md); pass a lower --wpm for text learners read.
"""
import argparse
import re
import sys

WORD = re.compile(r"[^\W_]+(?:['’-][^\W_]+)*", re.U)
PLANNED = re.compile(r"~\s*(\d+)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--wpm", type=float, default=130)
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
    total = 0.0
    for s in sections:
        mins = s["said"] / a.wpm
        total += mins
        plan = f"  (planned ~{s['planned']})" if s["planned"] is not None else ""
        print(f"{s['title']}: {s['said']} words, {mins:.1f} min{plan}; {s['quoted']} words in quote blocks")
    print(f"\nTotal: {total:.1f} min at {a.wpm:g} words a minute, every section counted;"
          " leave out the ones not taught (answers, sources, support material).")


if __name__ == "__main__":
    main()
