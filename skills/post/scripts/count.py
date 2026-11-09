#!/usr/bin/env python3
"""Count the characters of each unit of a post against the network's limit.

Usage: python3 count.py POST.txt --limit 280 [--url 23] [--wide 2] [--cut 210]

The units (the posts of a thread, the slides of a carousel, or a single post)
are separated by a line holding only ---. Read from stdin when no file is given.

Characters are counted as the reader sees them: accented letters, emoji built
from several code points and flags count once. The network's own weighting
comes from the plan (references/research.md), never from this script or
from memory:
  --url N   each link counts as N characters (links with http(s)://, www.
            or a bare domain such as example.com; trailing punctuation is
            left out of the link)
  --wide N  each emoji or wide (CJK) character counts as N
  --cut N   show where the "see more" cut falls in the first unit
"""
import argparse
import re
import sys
import unicodedata

URL = re.compile(r"(?:https?://|www\.)\S+|\b[\w-]+(?:\.[\w-]+)*\.[a-z]{2,}(?:/\S*)?", re.I)
TRAIL = ".,;:!?)]}\"'»”’"
JOINERS = {"‍", "︎", "️"}


def clusters(text):
    """Split text into what the reader sees as single characters."""
    out = []
    join_next = False
    for ch in unicodedata.normalize("NFC", text):
        cp = ord(ch)
        attach = (
            join_next
            or unicodedata.combining(ch)
            or ch in JOINERS
            or 0x1F3FB <= cp <= 0x1F3FF  # skin tones
            or 0xE0020 <= cp <= 0xE007F  # tag sequences
        )
        if out and attach:
            out[-1] += ch
        elif out and 0x1F1E6 <= cp <= 0x1F1FF and len(out[-1]) == 1 and 0x1F1E6 <= ord(out[-1]) <= 0x1F1FF:
            out[-1] += ch  # second half of a flag
        else:
            out.append(ch)
        join_next = ch == "‍"
    return out


def is_wide(cluster):
    ch = cluster[0]
    cp = ord(ch)
    if unicodedata.east_asian_width(ch) in ("W", "F"):
        return True
    return cp >= 0x1F000 or 0x2600 <= cp <= 0x27BF or len(cluster) > 1 and "️" in cluster


def weigh(text, url, wide):
    total = 0
    pos = 0
    for m in URL.finditer(text):
        link = m.group().rstrip(TRAIL)
        if "@" in text[max(0, m.start() - 1):m.start()]:
            continue  # part of an email address or a mention
        total += weigh_plain(text[pos:m.start()], wide)
        total += url if url else len(clusters(link))
        pos = m.start() + len(link)
    return total + weigh_plain(text[pos:], wide)


def weigh_plain(text, wide):
    return sum(wide if wide and is_wide(c) else 1 for c in clusters(text))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--url", type=int, default=0)
    ap.add_argument("--wide", type=int, default=0)
    ap.add_argument("--cut", type=int)
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    units = [u.strip("\n") for u in re.split(r"^---\s*$", text, flags=re.M)]
    units = [u for u in units if u.strip()]
    over = 0
    for i, u in enumerate(units, 1):
        n = weigh(u, a.url, a.wide)
        line = f"{i}: {n}"
        if a.limit:
            line += f"/{a.limit}"
            if n > a.limit:
                line += f"  OVER by {n - a.limit}"
                over += 1
        print(line)
    if a.cut and units:
        seen = "".join(clusters(units[0])[: a.cut])
        print(f"\nBefore the cut ({a.cut}):\n{seen}")
    if over:
        sys.exit(1)


if __name__ == "__main__":
    main()
