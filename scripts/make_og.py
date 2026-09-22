#!/usr/bin/env python3
"""Regenerate the site's Open Graph card at source/img/og_image.png.

One card for the whole site. The theme falls back to /img/og_image.png for any
page without an inline image, so this covers the home page, /about/ and every
text-only post; posts that carry images keep advertising their own.

Usage:  python3 scripts/make_og.py        (from the repo root)
Needs:  pillow
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
WORDMARK = ROOT / "source/img/space_moon.png"
TARGET = ROOT / "source/img/og_image.png"

W, H = 1200, 630

# A near-white diagonal wash. Link previews sit on white chrome in Slack, Kakao
# and Notion, so a flat white card loses its edges entirely; a couple of levels
# of tint give it a boundary without reading as a colour.
TINT_A = (249, 249, 250)
TINT_B = (242, 241, 243)

# Sized by height, not width: the mark's height is what sets its weight in a
# feed, and a wordmark's width drifts with its length.
MARK_HEIGHT = 100

# Supersample, then downscale — antialiases the scaled wordmark in one pass
# instead of relying on per-op filters.
S = 2

# The accent the theme compiles into its CSS, kept here because it lives only in
# the theme's Stylus source: style.styl sets `$blue` before Bulma's `?=` default
# can claim it, which is the one hook that repaints links, buttons and the navbar.
ACCENT = "#cd5c5c"


def wash():
    """Diagonal two-stop gradient, drawn tiny and upscaled so it stays smooth."""
    w, h = 64, 34
    grad = Image.new("RGB", (w, h))
    px = grad.load()
    for y in range(h):
        for x in range(w):
            t = (x / (w - 1) + y / (h - 1)) / 2
            px[x, y] = tuple(round(a + (b - a) * t) for a, b in zip(TINT_A, TINT_B))
    return grad.resize((W * S, H * S), Image.BICUBIC)


def main():
    canvas = wash()

    mark = Image.open(WORDMARK).convert("RGB")
    mh = MARK_HEIGHT * S
    mark = mark.resize((round(mark.width * mh / mark.height), mh), Image.LANCZOS)
    # The wordmark ships on an opaque white plate and has no alpha channel, so
    # key it out by luminance or it lands as a white box on the wash.
    canvas.paste(
        mark,
        ((W * S - mark.width) // 2, (H * S - mark.height) // 2),
        mark.convert("L").point(lambda v: 255 if v < 235 else 0),
    )

    canvas.resize((W, H), Image.LANCZOS).save(TARGET, optimize=True)
    print(f"wrote {TARGET.relative_to(ROOT)}  mark {round(mark.width / S)}x{MARK_HEIGHT}px")


if __name__ == "__main__":
    main()
