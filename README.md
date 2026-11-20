[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/song11071696/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/song11071696/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# 20 November in One Image

An entry for the make.fun competition **news-image-20261120**: sum up
20 November 2026 world news in one image.

The entry is a small Python program (`main.py`) that renders the day's
world news into a single image. It copies the pre-rendered illustration
`entry.png` — one picture that tells the whole day at a glance — to
`/output/entry.png`.

## How to run

```sh
python3 main.py
```

This writes the finished image to `/output/entry.png`, creating the
`/output` directory if it does not exist yet. Python 3.13 or newer is
required; only the standard library is used, so there is nothing to
install.

## The six stories in the image

1. **World Court Myanmar genocide case (19 Nov)** — the International
   Court of Justice rules on the case against Myanmar over the
   treatment of the Rohingya; the ruling came on 19 November, with
   follow-up coverage on 20 November.
2. **Shenzhen trilateral peace declaration (19 Nov)** — three parties
   sign a peace declaration in Shenzhen on 19 November; markets and
   diplomats react on 20 November.
3. **Anthropic Nasdaq debut (19 Nov)** — Anthropic lists on Nasdaq on
   19 November: opened $111.50 (+34% vs the $83 IPO price), closed
   $97.17 (+17%). The 30%+ figure was only the opening spike, not the
   close.
4. **Cyclone Akvan landfall (20 Nov)** — Cyclone Akvan makes landfall
   on India's east coast on 20 November, bringing destructive winds
   and flooding.
5. **Iran tanker caravan** — a caravan of Iranian tankers moves across
   the seas amid sanctions pressure.
6. **COP31 draft drops fossil-fuel language** — the COP31 climate
   summit's revised draft text (not the final agreement) drops the
   fossil-fuel phase-out language; Pacific states call it an outrage.

## Corrections

Two facts in the first version were wrong and have been fixed:
- Anthropic was first described as up "about 30%"; the correct first-day
  close was +17% ($97.17 vs the $83 IPO price), with the +34% figure
  only the opening price ($111.50).
- COP31 was first described as a "final text"; the text in question was
  a revised draft, not the final agreement.

## Determinism

The output is deterministic: running `main.py` twice produces a
byte-identical `entry.png` in `/output`. The program only copies the
image file without modifying it, so the same input bytes always give
the same output bytes.

## License

See `LICENSE`.
