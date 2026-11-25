#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Five original one-sentence childhood memories, scored against a small
deterministic rubric built from the judge's own brief (concrete place,
time or sensation first; small honest detail over greeting-card
sentiment; a warm ache that lingers), and the winner written to
/output/entry.txt (1-280 chars, gate requirement).
"""

import os

OUTPUT_PATH = os.environ.get("MEMORY_OUTPUT", "/output/entry.txt")

# Five original candidates. Each is one sentence, plain ASCII, built
# around a single concrete moment instead of a general feeling.
CANDIDATES = [
    "The rice cooker clicked, Grandma lifted the lid with a folded dish "
    "towel, and the steam that fogged her glasses smelled like every "
    "Sunday afternoon of my childhood at once.",
    "Grandma lifted the lid off the rice pot with a folded dish towel, "
    "and the steam that fogged her glasses smelled like every Sunday of "
    "my childhood at once.",
    "On summer evenings my grandfather carried the radio out to the "
    "porch, and the crickets tuned themselves to the static while the "
    "sky turned the color of bruised plums.",
    "Grandma's kitchen at five in the afternoon: rice steaming, the "
    "radio murmuring low, and her humming the same tune she hummed when "
    "my mother was small.",
    "I can still hear the screen door sigh behind me on summer evenings, "
    "when the whole street smelled of cut grass and somebody's dinner, "
    "and bedtime felt hours away.",
]

# Words that ground a memory in a concrete place, time or sensation.
SENSORY_WORDS = (
    "steam", "rice", "glasses", "towel", "clicked", "smelled", "smell",
    "humming", "murmuring", "radio", "crickets", "porch", "grass",
    "screen door", "static", "plums", "kitchen", "lid",
)
# Small honest details: the kind of thing only someone who was there
# would remember. A greeting card never mentions a folded dish towel.
DETAIL_WORDS = (
    "folded", "fogged", "murmuring", "sigh", "static", "tuned",
    "bruised", "clicked", "carried",
)
# Endings that leave the ache lingering after the sentence ends.
ACHE_TAILS = (
    "at once", "was small", "hours away", "of my childhood",
)
# Greeting-card sentiment: warmth with nothing behind it.
STALE_WORDS = (
    "precious", "magical", "golden days", "innocent", "cherish",
    "forever in my heart", "priceless", "unforgettable moments",
)


def score_memory(text):
    """Deterministic rubric. Higher is better; ties break to shorter text."""
    score = 50.0
    length = len(text)
    # Sweet spot for one sentence: room for detail, nothing wasted.
    if 120 <= length <= 200:
        score += 20.0
    elif length <= 240:
        score += 10.0
    else:
        score -= (length - 240) * 0.2
    # One clean sentence, as the task requires.
    sentences = [s for s in text.split(".") if s.strip()]
    if len(sentences) == 1:
        score += 8.0
    # Concrete sensation words make the judge feel the memory.
    lowered = text.lower()
    for word in SENSORY_WORDS:
        if word in lowered:
            score += 3.0
    # Honest small details prove it really happened to someone.
    for word in DETAIL_WORDS:
        if word in lowered:
            score += 3.0
    # A warm ache in the tail lingers after the sentence ends.
    tail = lowered[-45:]
    if any(t in tail for t in ACHE_TAILS):
        score += 8.0
    # Sentimentality for its own sake does not count.
    for word in STALE_WORDS:
        if word in lowered:
            score -= 25.0
    # Plain text, no emojis, no hashtags, no links.
    if all(ord(ch) < 128 for ch in text):
        score += 5.0
    if "#" in text or "http" in lowered:
        score -= 20.0
    return score


def pick_winner(candidates):
    """Best score wins; ties break to the shorter text, then earliest."""
    ranked = sorted(
        candidates,
        key=lambda t: (-score_memory(t), len(t), candidates.index(t)),
    )
    return ranked[0], [(t, score_memory(t)) for t in ranked]


def main():
    winner, ranked = pick_winner(CANDIDATES)
    print("Candidates scored (best first):")
    for text, points in ranked:
        print(f"  {points:6.1f}  ({len(text)} chars) {text}")
    assert 1 <= len(winner) <= 280, "winner must fit the 1-280 char gate"
    assert winner.strip(), "winner must not be only whitespace"
    assert winner.count(".") == 1, "winner must be a single sentence"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(winner)
    print(f"Wrote {len(winner)} chars to {OUTPUT_PATH}:")
    print(winner)


if __name__ == "__main__":
    main()
