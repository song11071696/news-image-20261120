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

1. **World Court Myanmar genocide case** — the International Court of
   Justice hears the case against Myanmar over the treatment of the
   Rohingya.
2. **Shenzhen trilateral peace declaration** — three parties sign a
   peace declaration in Shenzhen.
3. **Anthropic Nasdaq debut up ~30%** — Anthropic lists on Nasdaq and
   closes its first day of trading up roughly 30%.
4. **Cyclone Akvan landfall** — Cyclone Akvan makes landfall, bringing
   destructive winds and flooding.
5. **Iran tanker caravan** — a caravan of Iranian tankers moves across
   the seas amid sanctions pressure.
6. **COP31 fossil-fuel language dropped** — the COP31 climate summit
   drops fossil-fuel phase-out language from its final text.

## Determinism

The output is deterministic: running `main.py` twice produces a
byte-identical `entry.png` in `/output`. The program only copies the
image file without modifying it, so the same input bytes always give
the same output bytes.

## License

See `LICENSE`.
