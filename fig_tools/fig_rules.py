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


def build() -> Figure:
    fig = Figure(900, 470,
                 "Figure 16: The rules that apply on every flight",
                 "These three are the ones you can break without noticing. "
                 "Week 5 covers the full set.")

    fig.add(rect(40, 84, 820, GROUND_Y - 84, rx=10, fill="#e8f2fb",
                 stroke="#cfe0ee", stroke_width=1.5))
    fig.add(rect(40, GROUND_Y, 820, 22, fill="#e4ead9"))
    fig.add(line(40, GROUND_Y, 860, GROUND_Y, stroke="#9aa7b2",
                 stroke_width=3, stroke_linecap="round"))

    # altitude ceiling
    fig.add(line(56, CEILING_Y, 844, CEILING_Y, stroke=P["bad"],
                 stroke_width=2.5, stroke_dasharray="10 6"))
    fig.add(text(60, CEILING_Y - 12, "400 ft (120 m) above the ground",
                 font_size=13, font_weight="bold", fill=P["bad"]))

    # the measured height, at the right-hand edge
    fig.add(arrow(800, GROUND_Y - 6, 800, CEILING_Y + 6, color="#8fa3b5",
                  width=2, head=8))
    fig.add(arrow(800, CEILING_Y + 6, 800, GROUND_Y - 6, color="#8fa3b5",
                  width=2, head=8))

    # pilot, watching the aircraft
    fig.add(person(150, GROUND_Y, 1.35))
    fig.add(text(150, GROUND_Y + 30, "you", text_anchor="middle",
                 font_size=12.5, fill=P["muted"]))

    # aircraft, comfortably under the ceiling
    fig.add(translate(455, 236, aircraft_mini_side(0.8)))
    fig.add(line(168, GROUND_Y - 30, 420, 240, stroke=P["accent"],
                 stroke_width=2, stroke_dasharray="7 5"))
    fig.add(text(300, 338, "keep it in sight, without binoculars",
                 text_anchor="middle", font_size=12.5, fill=P["accent"]))

    # people on the ground, and the rule about them
    for i, dx in enumerate((-26, 0, 26)):
        fig.add(person(700 + dx, GROUND_Y, 1.15, fill="#7a8794"))
    fig.add(circle(700, 268, 22, fill="none", stroke=P["bad"], stroke_width=3.5))
    fig.add(line(685, 253, 715, 283, stroke=P["bad"], stroke_width=3.5,
                 stroke_linecap="round"))
    fig.add(text(700, 226, "never fly over people", text_anchor="middle",
                 font_size=12.5, font_weight="bold", fill=P["bad"]))

    fig.add(text(450, 424,
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
