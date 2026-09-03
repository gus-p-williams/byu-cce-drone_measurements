"""Figures: what each control stick does, and why nose-in flying feels reversed.

Usage:
    python fig_tools/fig_sticks.py --png
    python fig_tools/fig_sticks.py --out docs/week_01/images

Outputs:
    fig08_stick_controls.svg   eight panels, one per stick direction
    fig09_nose_in.svg          the same right-stick input, seen two ways
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parts import (aircraft_mini_side, aircraft_mini_top,  # noqa: E402
                   rotation_arrow, stick_pair)
from svgkit import PALETTE as P  # noqa: E402
from svgkit import Figure, arrow, g, rect, text, translate  # noqa: E402

COLS = (150, 350, 550, 750)


def panel(cx, top, side, dx, dy, label, sub, motion):
    """One panel: both sticks with the active one highlighted, the aircraft
    response, and a caption."""
    grp = g(rect(cx - 96, top, 192, 250, rx=10, fill=P["white"],
                 stroke="#dde3e9", stroke_width=1.5))
    grp.add(translate(cx, top + 50, stick_pair(side, dx, dy)))
    grp.add(translate(cx, top + 145, motion))
    grp.add(text(cx, top + 212, label, text_anchor="middle",
                 font_weight="bold", fill=P["ink"]))
    grp.add(text(cx, top + 230, sub, text_anchor="middle", font_size=11,
                 fill=P["muted"]))
    return grp


def vertical_motion(up: bool):
    """Side view, with the arrow held clear of the stick above it."""
    return g(aircraft_mini_side(0.85),
             arrow(64, 22 if up else -22, 64, -38 if up else 38, width=3))


def yaw_motion(clockwise: bool):
    return g(aircraft_mini_top(0.85),
             rotation_arrow(0, 0, 40, clockwise=clockwise, start_deg=150,
                            sweep_deg=230, width=3))


def linear_motion(dx: float, dy: float):
    """Top view. Vertical arrows sit beside the aircraft so they do not run
    into the stick above or the caption below."""
    if dy:
        return g(aircraft_mini_top(0.85),
                 arrow(40, dy * 22, 40, dy * 56, width=3))
    return g(aircraft_mini_top(0.85),
             arrow(dx * 46, 0, dx * 86, 0, width=3))


def build_sticks() -> Figure:
    fig = Figure(900, 700,
                 "Figure 8: What each stick does",
                 "Mode 2 layout, the default on nearly every ready-to-fly drone. "
                 "All directions are relative to the nose of the aircraft.")

    fig.add(text(60, 92, "Left stick — altitude and heading", font_size=14,
                 font_weight="bold", fill=P["ink"]))
    row1 = [
        (0, -1, "Climb", "rises straight up", vertical_motion(True)),
        (0, 1, "Descend", "comes straight down", vertical_motion(False)),
        (-1, 0, "Turn left", "nose swings left", yaw_motion(False)),
        (1, 0, "Turn right", "nose swings right", yaw_motion(True)),
    ]
    for cx, (dx, dy, label, sub, motion) in zip(COLS, row1):
        fig.add(panel(cx, 106, "left", dx, dy, label, sub, motion))

    fig.add(text(60, 396, "Right stick — moving over the ground", font_size=14,
                 font_weight="bold", fill=P["ink"]))
    row2 = [
        (0, -1, "Fly forward", "in the direction the nose points",
         linear_motion(0, -1)),
        (0, 1, "Fly backward", "away from the nose", linear_motion(0, 1)),
        (-1, 0, "Slide left", "nose keeps pointing the same way",
         linear_motion(-1, 0)),
        (1, 0, "Slide right", "nose keeps pointing the same way",
         linear_motion(1, 0)),
    ]
    for cx, (dx, dy, label, sub, motion) in zip(COLS, row2):
        fig.add(panel(cx, 410, "right", dx, dy, label, sub, motion))

    return fig


def build_nose_in() -> Figure:
    fig = Figure(900, 470,
                 "Figure 9: The same input, flying away and flying toward you",
                 "The aircraft always moves relative to its own nose, which is "
                 "why nose-in flight catches out new pilots.")

    for i, (cx, heading, title, result) in enumerate((
        (260, 0, "Nose pointing away from you",
         "The drone slides to YOUR right"),
        (640, 180, "Nose pointing back at you",
         "The drone slides to YOUR left"),
    )):
        fig.add(rect(cx - 165, 84, 330, 340, rx=12, fill=P["white"],
                     stroke="#dde3e9", stroke_width=1.5))
        fig.add(text(cx, 112, title, text_anchor="middle", font_weight="bold",
                     fill=P["ink"]))

        # the same stick input in both panels
        fig.add(translate(cx, 168, stick_pair("right", 1, 0, 22, 42)))
        fig.add(text(cx, 214, "right stick pushed right", text_anchor="middle",
                     font_size=11, fill=P["muted"]))

        # aircraft, rotated to face away or toward the pilot
        fig.add(translate(cx, 292, g(aircraft_mini_top(0.95),
                                     transform=f"rotate({heading})")))
        nose_y = 292 - 46 if heading == 0 else 292 + 46
        fig.add(text(cx - 62, nose_y + 4, "nose", text_anchor="middle",
                     font_size=11, font_style="italic", fill=P["muted"]))
        # ground-frame motion: right for nose-away, left for nose-toward
        direction = 1 if heading == 0 else -1
        fig.add(arrow(cx + direction * 52, 292, cx + direction * 118, 292,
                      width=3.5))
        fig.add(text(cx, 372, result, text_anchor="middle",
                     font_weight="bold", fill=P["bad"]))
        fig.add(text(cx, 398, "arrow shows movement over the ground",
                     text_anchor="middle", font_size=11, fill=P["muted"]))

    # pilot marker between the panels
    fig.add(text(450, 300, "you", text_anchor="middle", font_size=12,
                 fill=P["muted"]))
    fig.add(text(450, 322, "▲", text_anchor="middle", font_size=14,
                 fill=P["muted"]))
    return fig


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="review")
    ap.add_argument("--png", action="store_true")
    args = ap.parse_args()

    from svgkit import render_png
    for builder, name in ((build_sticks, "fig08_stick_controls.svg"),
                          (build_nose_in, "fig09_nose_in.svg")):
        fname = os.path.join(args.out, name)
        builder().save(fname)
        print("wrote", fname)
        if args.png:
            png = render_png(fname)
            if png:
                print("wrote", png)


if __name__ == "__main__":
    main()
