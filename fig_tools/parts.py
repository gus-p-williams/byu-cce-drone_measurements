"""Reusable drawing parts: one controller, one aircraft, one stick glyph.

Every part is drawn in its own local coordinates and returned together with a
dictionary of anchor points (in the same local coordinates) that figure scripts
use to attach callouts. Place a part with svgkit.translate(x, y, part) and add
(x, y) to the anchors.

Keep the geometry here stable: students should recognize the same controller
and the same aircraft in every figure across the course.
"""
from __future__ import annotations

from svgkit import PALETTE as P
from svgkit import circle, comment, g, line, path, rect, text


# ---------------------------------------------------------------------------
# Controller
# ---------------------------------------------------------------------------
def controller(screen: str = "phone", mode_labels: bool = True):
    """A generic two-stick controller, 420 x 190 body at local origin (0, 0).

    screen: "phone"   a phone held in a clamp above the body
            "builtin" a screen built into the top of the body
            "none"    no screen

    Returns (element, anchors). Anchors point at the part edges that leader
    lines should touch.
    """
    grp = g(comment("generic controller"))

    # antennas
    grp.add(g(line(15, 2, -2, -95), line(405, 2, 422, -95),
              stroke=P["line"], stroke_width=7, stroke_linecap="round"))

    # screen options (drawn before the body so the body overlaps the join)
    if screen == "phone":
        grp.add(rect(136, -55, 14, 60, rx=3, fill="#555555"))
        grp.add(rect(270, -55, 14, 60, rx=3, fill="#555555"))
        grp.add(rect(130, -115, 160, 90, rx=10, fill=P["white"],
                     stroke=P["line"], stroke_width=2))
        grp.add(rect(140, -105, 140, 70, rx=4, fill=P["screen"],
                     stroke="#9bbbe0", stroke_width=1))
        screen_anchor = (210, -115)
    elif screen == "builtin":
        grp.add(rect(115, -78, 190, 90, rx=12, fill=P["body"],
                     stroke=P["line"], stroke_width=2))
        grp.add(rect(127, -68, 166, 62, rx=4, fill=P["screen"],
                     stroke="#9bbbe0", stroke_width=1))
        screen_anchor = (210, -78)
    else:
        screen_anchor = None

    # shoulder controls on the top edge
    grp.add(rect(45, -12, 44, 14, rx=7, fill=P["dark"], stroke="#222222"))
    grp.add(g(*[line(x, -10, x, 0) for x in (55, 62, 69, 76)],
              stroke="#888888", stroke_width=1))
    grp.add(rect(331, -12, 44, 14, rx=7, fill=P["dark"], stroke="#222222"))
    grp.add(circle(364, -5, 3.5, fill=P["bad"]))

    # body
    grp.add(rect(0, 0, 420, 190, rx=45, fill=P["body"], stroke=P["line"],
                 stroke_width=2))

    # sticks
    for cx in (90, 330):
        grp.add(circle(cx, 92, 32, fill="#b8c0c8", stroke=P["line"],
                       stroke_width=1.5))
        grp.add(circle(cx, 92, 15, fill=P["line"]))
        grp.add(circle(cx, 92, 6, fill="#666666"))

    # return-to-home / pause
    grp.add(circle(210, 45, 12, fill=P["white"], stroke=P["line"],
                   stroke_width=1.5))
    grp.add(text(210, 50, "H", text_anchor="middle", font_size=12,
                 font_weight="bold", fill=P["ink"]))

    # flight mode switch
    grp.add(rect(175, 72, 70, 16, rx=8, fill="#eeeeee", stroke=P["line"],
                 stroke_width=1.5))
    grp.add(circle(210, 80, 6, fill=P["accent"], stroke=P["ink"],
                   stroke_width=1))
    if mode_labels:
        for x, s in ((185, "C"), (210, "N"), (235, "S")):
            grp.add(text(x, 102, s, text_anchor="middle", font_size=9,
                         fill=P["muted"]))

    # power button and battery lights
    grp.add(circle(190, 152, 8, fill=P["white"], stroke=P["line"],
                   stroke_width=1.5))
    grp.add(path("M190 147 v5 M186.5 149.5 a4.5 4.5 0 1 0 7 0",
                 stroke=P["line"], stroke_width=1.5, fill="none",
                 stroke_linecap="round"))
    for i, cx in enumerate((215, 227, 239, 251)):
        grp.add(circle(cx, 152, 3.5, fill=P["ok"] if i < 3 else P["off"],
                       stroke=None if i < 3 else "#999999",
                       stroke_width=None if i < 3 else 0.5))

    # charging / data port
    grp.add(rect(201, 183, 18, 6, rx=3, fill=P["line"]))

    anchors = {
        "left_stick": (58, 92),
        "right_stick": (362, 92),
        "rth": (198, 45),
        "mode_switch": (247, 80),
        "power": (190, 161),
        "battery": (233, 158),
        "port": (210, 190),
        "gimbal_dial": (65, -12),
        "shutter": (353, -12),
        "antenna_left": (2, -75),
        "antenna_right": (418, -75),
        "screen": screen_anchor,
    }
    return grp, anchors


def shift(anchors: dict, dx: float, dy: float) -> dict:
    """Return anchors moved by (dx, dy), skipping None entries."""
    return {k: (v[0] + dx, v[1] + dy) for k, v in anchors.items() if v}
