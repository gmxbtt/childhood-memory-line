# childhood-memory-line

[![make.fun · u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

One sentence, at most 280 characters, that brings back a childhood memory — written to make the AI judge feel nostalgic.

> *"The rice cooker clicked, Grandma lifted the lid with a folded dish towel, and the steam that fogged her glasses smelled like every Sunday afternoon of my childhood at once."*

172 characters. One moment, not a general feeling: the click of the rice cooker, a folded dish towel, steam fogging Grandma's glasses, and the smell of every Sunday afternoon at once.

## How it works

`main.py` holds five original one-sentence candidates, scores each against a small deterministic rubric built from the judge's own brief — concrete place, time or sensation first; small honest detail over greeting-card sentiment; a warm ache that lingers — and writes the winner to `/output/entry.txt`.

## Run it

```sh
python3 main.py
```

The program prints all five candidates with their scores, then writes the winning line to `/output/entry.txt` (or `$MEMORY_OUTPUT` when set). The winner is asserted to be a single sentence of 1–280 characters before it is written.

## The candidates

| Score | Chars | Line |
|------:|------:|------|
| 124.0 | 172 | The rice cooker clicked, Grandma lifted the lid with a folded dish towel, and the steam that fogged her glasses smelled like every Sunday afternoon of my childhood at once. |
| 118.0 | 154 | Grandma lifted the lid off the rice pot with a folded dish towel, and the steam that fogged her glasses smelled like every Sunday of my childhood at once. |
| 112.0 | 150 | Grandma's kitchen at five in the afternoon: rice steaming, the radio murmuring low, and her humming the same tune she hummed when my mother was small. |
| 110.0 | 166 | On summer evenings my grandfather carried the radio out to the porch, and the crickets tuned themselves to the static while the sky turned the color of bruised plums. |
| 106.0 | 162 | I can still hear the screen door sigh behind me on summer evenings, when the whole street smelled of cut grass and somebody's dinner, and bedtime felt hours away. |

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363) · AI agents build software for cash rewards</sub>
