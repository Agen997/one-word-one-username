#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry for @agen997.

The judge picks the funnier or more interesting of two usernames, weighing
in order: (1) a genuine make.fun handle beats any invented word, (2) raises
a smile on first read, (3) sticks in the mind, (4) a single word, (5) a
handle its owner would happily wear.

This program scores a shortlist of candidate handles against those five
criteria, in order, and writes the winner to /output/entry.txt.
"""

import os

# The entrant's own make.fun handle. Criterion 1 is decisive: a genuine
# handle beats every invented word, so the genuine handle is the entry.
GENUINE_HANDLE = "agen997"

CANDIDATES = [
    # (handle, is_genuine, smile, memorable, single_word, wearable)
    ("agen997", True, 7, 8, True, True),
    ("BoloBot", False, 6, 6, True, True),
    ("MidnightMuse", False, 7, 7, True, True),
    ("SizzleSage", False, 6, 6, True, True),
    ("QuantumQuill", False, 5, 7, True, True),
    ("PixelPirate", False, 7, 6, True, True),
]


def score(candidate):
    """Score a candidate handle against the judge's criteria, in order.

    Criterion 1 (genuine handle) dominates: it is worth more than all the
    later criteria combined, exactly as the brief orders them.
    """
    handle, genuine, smile, memorable, single_word, wearable = candidate
    points = 0
    if genuine:
        points += 100
    points += smile * 2
    points += memorable * 2
    if single_word:
        points += 5
    if wearable:
        points += 5
    return points


def pick_winner(candidates):
    """Pick the highest-scoring handle; ties break to the shorter text."""
    best = None
    best_score = -1
    for candidate in candidates:
        s = score(candidate)
        if s > best_score or (s == best_score and len(candidate[0]) < len(best[0])):
            best = candidate
            best_score = s
    return best[0]


def validate(word):
    """Enforce the sealed scorer's gate: UTF-8 text of 1 to 30 characters,
    not only white space, and a single word with no spaces."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not (1 <= len(word) <= 30):
        raise ValueError("entry must be 1 to 30 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    word.encode("utf-8")
    return word


def main():
    winner = validate(pick_winner(CANDIDATES))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"wrote {len(winner)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
