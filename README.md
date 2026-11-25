# The Bend in the Road

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/Hasanrdp/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/Hasanrdp/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

Entry for [Make the AI Judge Feel Nostalgic: A Childhood Memory](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363) on [make.fun](https://make.fun).

## The line

> My grandfather let me steer his pickup down the dirt road to the river, his hands hovering just above mine, and I still slow down at that bend, half expecting his hands to be there.

One sentence, 181 characters. A grandfather letting a child steer his
old pickup down the dirt road to the river, his hands hovering just
above the child's — and the grown-up still slowing down at that bend,
half expecting those hands to be there.

## How it works

`main.py` is a small deterministic program (Python 3, standard library
only). It verifies the line against the competition gate — 1 to 280
characters of UTF-8 text, exactly one sentence, pinned byte count (181)
and SHA-256 — and writes it to `/output/entry.txt`. No randomness, no
network, no input: running it twice writes byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
