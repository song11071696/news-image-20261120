# 20 November in One Image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/song11071696/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/song11071696/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

This entry squeezes 20 November's world news into a single 1024x1024 image: the World Court's landmark verdict that Myanmar committed genocide against the Rohingya leads the page — the first time a state has ever been found guilty of genocide — alongside the Trump-Xi-Putin peace declaration from Shenzhen, Anthropic's soaring Nasdaq debut at $111.50, Cyclone Akvan making landfall on India's east coast, Iran loading a tanker caravan to break the US naval blockade, and COP31 ending with fossil-fuel language cut from the deal. A ticker along the bottom carries the day's other big stories — Voyager 1 now one light-day from Earth, the Houthi strike on Riyadh's tallest tower, Fiona the hippo, and the EU's proposed €45B Ukraine loan. The backdrop is an AI-generated world map with no text on it at all; every headline was laid over it afterwards with PIL, so the picture reads cleanly at a glance.

## Run it

```bash
python3 main.py
```

That writes the bundled 1024x1024 image to `/output/entry.png`. The script uses only the Python standard library and makes no network calls. Run it twice and the output is byte-identical both times.

## Verification

Check the bundled image against its known hash before running:

```bash
sha256sum entry.png
```

Expected SHA-256 for `entry.png`:

```
0c4fec5ddc37a02d1866ead15f96e097633ebce16f968f5c93192f435e6ebb22
```

`main.py` re-checks the same hash, the file size, and the PNG magic bytes on every run, and exits non-zero if the copy in `/output/entry.png` does not match.

## Prize

This entry is for the make.fun news-image-20261120 bounty, a $250 prize pool split $50 / $30 / $15 for the top three, $5 for places 4–10, and $3 for places 11–50.
