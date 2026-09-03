"""Figure: the flying rules that apply to every flight.

Usage:
    python fig_tools/fig_rules.py --png
    python fig_tools/fig_rules.py --out docs/week_01/images

Outputs:
    fig16_rules.svg   line of sight, the altitude limit, and people
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parts import aircraft_mini_side  # noqa: E402
from svgkit import PALETTE as P  # noqa: E402
from svgkit import (Figure, arrow, circle, g, line, path, rect,  # noqa: E402
                    render_png, text, translate)

GROUND_Y = 366
CEILING_Y = 152


def person(x, y, scale=1.0, fill=None):
    fill = fill or P["dark"]
    return translate(x, y, g(
        circle(0, -13, 6.5, fill=fill),
        path("M-7,6 a7,9 0 0,1 14,0 z", fill=fill),
        transform=f"scale({scale})" if scale != 1 else None))


def car(x, y, scale=1.0):
    return translate(x, y, g(
        path("M-30,4 l7,-13 h32 l9,13 z", fill="#7a8794", stroke=P["line"],
             stroke_width=1.5),
        rect(-34, 4, 68, 11, rx=4, fill="#8f9aa6", stroke=P["line"],
             stroke_width=1.5),
        circle(-18, 16, 6, fill=P["dark"]),
        circle(18, 16, 6, fill=P["dark"]),
        transform=f"scale({scale})" if scale != 1 else None))


def control_tower(x, y, scale=1.0):
    return translate(x, y, g(
        rect(-9, -8, 18, 30, fill="#8f9aa6", stroke=P["line"], stroke_width=1.5),
        rect(-15, -22, 30, 15, rx=3, fill="#c2cad2", stroke=P["line"],
             stroke_width=1.5),
        line(-15, -14, 15, -14, stroke=P["line"], stroke_width=1.2),
        line(0, -22, 0, -32, stroke=P["line"], stroke_width=2),
        transform=f"scale({scale})" if scale != 1 else None))


def no_symbol(x, y, r=44):
    """The red circle and bar that marks each prohibition."""
    d = r * 0.68
    return g(circle(x, y, r, fill="none", stroke=P["bad"], stroke_width=5),
             line(x - d, y - d, x + d, y + d, stroke=P["bad"], stroke_width=5,
                  stroke_linecap="round"))


def build() -> Figure:
    fig = Figure(900, 664,
                 "Figure 16: The rules that apply on every flight",
                 "Keep it in sight, keep it low, and know what you must never "
                 "fly over. Week 5 covers the full set.")

    # ---- upper scene: line of sight and the altitude limit ----
    sky_top, ground_y, ceiling_y = 78, 300, 132
    fig.add(rect(40, sky_top, 820, ground_y - sky_top, rx=10, fill="#e8f2fb",
                 stroke="#cfe0ee", stroke_width=1.5))
    fig.add(rect(40, ground_y, 820, 18, fill="#e4ead9"))
    fig.add(line(40, ground_y, 860, ground_y, stroke="#9aa7b2",
                 stroke_width=3, stroke_linecap="round"))

    fig.add(line(56, ceiling_y, 844, ceiling_y, stroke=P["bad"],
                 stroke_width=2.5, stroke_dasharray="10 6"))
    fig.add(text(60, ceiling_y - 12, "400 ft (120 m) above the ground",
                 font_size=13, font_weight="bold", fill=P["bad"]))
    fig.add(arrow(806, ground_y - 6, 806, ceiling_y + 6, color="#8fa3b5",
                  width=2, head=8))
    fig.add(arrow(806, ceiling_y + 6, 806, ground_y - 6, color="#8fa3b5",
                  width=2, head=8))

    fig.add(person(150, ground_y, 1.3))
    fig.add(text(150, ground_y + 32, "you", text_anchor="middle",
                 font_size=12.5, fill=P["muted"]))
    fig.add(translate(470, 200, aircraft_mini_side(0.78)))
    fig.add(line(167, ground_y - 30, 434, 204, stroke=P["accent"],
                 stroke_width=2, stroke_dasharray="7 5"))
    fig.add(text(300, 284, "keep it in sight, without binoculars",
                 text_anchor="middle", font_size=12.5, fill=P["accent"]))

    # ---- three things you must never fly over ----
    top, h, w = 348, 252, 270
    for cx, icon, label, lines in (
        (155, "people", "Never over people",
         ("anyone not taking part", "in your operation")),
        (450, "traffic", "Never over moving traffic",
         ("roads, rail, and", "waterways in use")),
        (745, "airspace", "Never in restricted airspace",
         ("no FAA authorization", "means no flight")),
    ):
        fig.add(rect(cx - w / 2, top, w, h, rx=10, fill=P["white"],
                     stroke="#dde3e9", stroke_width=1.5))
        mid = top + 84
        if icon == "people":
            for dx in (-34, 0, 34):
                fig.add(person(cx + dx, mid + 26, 1.25, fill="#7a8794"))
        elif icon == "traffic":
            fig.add(rect(cx - 92, mid + 12, 184, 26, rx=3, fill="#b9c1c9"))
            fig.add(g(*[line(cx - 76 + i * 32, mid + 25, cx - 60 + i * 32,
                             mid + 25) for i in range(5)],
                      stroke=P["white"], stroke_width=3))
            fig.add(car(cx, mid - 8, 1.15))
        else:
            fig.add(path(f"M{cx - 96},{mid + 36} a96,42 0 0,1 192,0",
                         fill="none", stroke=P["bad"], stroke_width=2.5,
                         stroke_dasharray="8 6"))
            fig.add(control_tower(cx, mid + 12, 1.15))
            fig.add(text(cx, mid + 70, "controlled airspace",
                         text_anchor="middle", font_size=11, fill=P["muted"]))
        fig.add(no_symbol(cx, mid + 6))

        fig.add(text(cx, top + 188, label, text_anchor="middle", font_size=14,
                     font_weight="bold", fill=P["ink"]))
        for i, ln in enumerate(lines):
            fig.add(text(cx, top + 212 + i * 18, ln, text_anchor="middle",
                         font_size=12, fill=P["muted"]))

    fig.add(text(450, 640,
                 "Daylight only, one aircraft at a time, and never from a "
                 "moving vehicle.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="review")
    ap.add_argument("--png", action="store_true")
    args = ap.parse_args()

    fname = os.path.join(args.out, "fig16_rules.svg")
    build().save(fname)
    print("wrote", fname)
    if args.png:
        png = render_png(fname)
        if png:
            print("wrote", png)


if __name__ == "__main__":
    main()
