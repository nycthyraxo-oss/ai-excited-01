# Moon Koi — Make the AI Judge Excited

[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

An entry for the [make.fun](https://make.fun) competition
[Make the AI judge excited](https://make.fun/bounty/ai-excited-01)
(`ai-excited-01`).

## The image

A colossal koi fish — scales of molten gold and magenta — bursts out of a
dark ink-blue ocean straight toward the viewer, water exploding into a crown
of spray around it. A huge full moon burns behind it, and far below, a tiny
red torii gate stands on a lonely cliff, the one small thing that tells you
just how enormous the fish really is.

One look, one focal point: a creature the size of a mountain, mid-leap,
lit like a lantern against the night sea. No text, no clutter — the shape
reads at a glance, even small.

## How it works

`main.py` (Python 3.13, standard library only) copies the entry image
`entry.png` into the output directory given by `MAKEFUN_OUTPUT_DIR`
(or an `out` folder when the variable is unset), as `entry.png`. It uses no
network and no randomness, so repeated runs write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
