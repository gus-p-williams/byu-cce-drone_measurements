"""Proposed figures for Week 4: SfM workflow and mission planning.

Written as proposals. They land in review/ by default and are only copied into
docs/week_04/images/ once approved.

Three are replacements for figures that already exist but sit outside the house
style. Three cover concepts the pages currently explain in prose only: overlap,
ground sample distance, and nadir against oblique.

Usage:
    python fig_tools/fig_week04.py --png
    python fig_tools/fig_week04.py --out docs/week_04/images
"""
from __future__ import annotations

import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parts import aircraft_mini_side, aircraft_mini_top  # noqa: E402
from svgkit import PALETTE as P  # noqa: E402
from svgkit import (Figure, arrow, circle, g, line, path, polygon,  # noqa: E402
                    rect, render_png, text, translate)

CARD = dict(rx=10, fill=P["white"], stroke="#dde3e9", stroke_width=1.5)
SHOT = "#4a90d9"


def bracket(x0, x1, y, label, colour=None, above=True):
    """A span marker with a label, for showing what a percentage covers."""
    colour = colour or P["ink"]
    tick = -7 if above else 7
    return g(path(f"M{x0},{y + tick} V{y} H{x1} V{y + tick}", fill="none",
                  stroke=colour, stroke_width=2),
             text((x0 + x1) / 2, y + (-13 if above else 22), label,
                  text_anchor="middle", font_size=12.5, font_weight="bold",
                  fill=colour))


# ---------------------------------------------------------------------------
# 1. Overlap: what 80% and 70% actually mean
# ---------------------------------------------------------------------------
def build_overlap() -> Figure:
    fig = Figure(900, 560, "What overlap actually means",
                 "Overlap is how much of each photo repeats the one before it. "
                 "It is not wasted effort; it is what makes the maths work.")

    # ---- forward overlap, along one flight line ----
    fig.add(rect(30, 84, 400, 440, **CARD))
    fig.add(text(230, 114, "Forward overlap, 80%", text_anchor="middle",
                 font_size=15, font_weight="bold", fill=P["ink"]))
    fig.add(text(230, 134, "between one photo and the next", text_anchor="middle",
                 font_size=11.5, fill=P["muted"]))

    fw, fh, step = 150, 96, 30          # 30 of 150 is new ground: 80% overlap
    x0, y0 = 92, 200
    fig.add(line(x0 + 10, y0 - 40, x0 + 10 + 3 * step + 130, y0 - 40,
                 stroke="#c5cdd5", stroke_width=2, stroke_dasharray="7 5"))
    for i in range(4):
        fig.add(translate(x0 + i * step + fw / 2, y0 - 40,
                          aircraft_mini_side(0.34, nose=False)))
        fig.add(rect(x0 + i * step, y0, fw, fh, rx=3, fill=SHOT,
                     fill_opacity="0.18", stroke=SHOT, stroke_width=1.5))
    # one photo's width, split into the part that repeats and the part that is new
    bar_y = y0 + fh + 22
    fig.add(rect(x0 + 3 * step, bar_y, fw - 3 * step, 14, fill=SHOT,
                 fill_opacity="0.45", stroke=SHOT, stroke_width=1.5))
    fig.add(rect(x0 + fw, bar_y, step, 14, fill="#c5cdd5", stroke=P["muted"],
                 stroke_width=1.5))
    fig.add(text(230, bar_y + 44, "80% of each photo repeats the one before",
                 text_anchor="middle", font_size=12.5, font_weight="bold",
                 fill=SHOT))
    fig.add(text(230, bar_y + 64, "only the grey 20% is new ground",
                 text_anchor="middle", font_size=12.5, fill=P["muted"]))
    fig.add(text(230, bar_y + 96, "Every point on the ground ends up in 5 to 9",
                 text_anchor="middle", font_size=12, fill=P["muted"]))
    fig.add(text(230, bar_y + 114, "photos, which is what the maths needs.",
                 text_anchor="middle", font_size=12, fill=P["muted"]))

    # ---- side overlap, between neighbouring flight lines ----
    fig.add(rect(470, 84, 400, 440, **CARD))
    fig.add(text(670, 114, "Side overlap, 70%", text_anchor="middle",
                 font_size=15, font_weight="bold", fill=P["ink"]))
    fig.add(text(670, 134, "between one flight line and the next",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))

    sw, sh, sstep = 230, 108, 32        # 32 of 108 is new: about 70% overlap
    sx, sy = 555, 180
    for i, lbl in enumerate(("line 1", "line 2", "line 3")):
        fig.add(rect(sx, sy + i * sstep, sw, sh, rx=3, fill=SHOT,
                     fill_opacity="0.18", stroke=SHOT, stroke_width=1.5))
        fig.add(text(sx - 12, sy + i * sstep + 16, lbl, text_anchor="end",
                     font_size=11, fill=P["muted"]))
        fig.add(arrow(sx + 30, sy + i * sstep + 8, sx + sw - 30,
                      sy + i * sstep + 8, color="#9aa7b2", width=2, head=8)
                if i % 2 == 0 else
                arrow(sx + sw - 30, sy + i * sstep + 8, sx + 30,
                      sy + i * sstep + 8, color="#9aa7b2", width=2, head=8))
    ov0, ov1 = sy + sstep, sy + sh          # the band lines 1 and 2 share
    fig.add(path(f"M{sx + sw + 20},{ov0} V{ov1} "
                 f"M{sx + sw + 14},{ov0} H{sx + sw + 26} "
                 f"M{sx + sw + 14},{ov1} H{sx + sw + 26}",
                 stroke=SHOT, stroke_width=2, fill="none"))
    fig.add(text(sx + sw + 32, (ov0 + ov1) / 2 - 2, "70%", font_size=13,
                 font_weight="bold", fill=SHOT))
    fig.add(text(sx + sw + 32, (ov0 + ov1) / 2 + 16, "shared", font_size=12.5,
                 fill=SHOT))
    fig.add(text(670, 400, "70% of each strip is photographed twice,",
                 text_anchor="middle", font_size=12.5, font_weight="bold",
                 fill=SHOT))
    fig.add(text(670, 424, "Too little sidelap leaves gaps between lines",
                 text_anchor="middle", font_size=12, fill=P["muted"]))
    fig.add(text(670, 442, "that no software can fill in afterwards.",
                 text_anchor="middle", font_size=12, fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# 2. GSD against altitude
# ---------------------------------------------------------------------------
def build_gsd() -> Figure:
    fig = Figure(900, 540, "Altitude decides detail, and how long you fly",
                 "Double the height and every pixel covers twice as much "
                 "ground, but each photo covers four times the area.")

    ground_y = 408
    fig.add(rect(30, 84, 840, ground_y - 84, rx=10, fill="#eef4fa",
                 stroke="#dde3e9", stroke_width=1.5))
    fig.add(line(40, ground_y, 860, ground_y, stroke="#9aa7b2", stroke_width=3,
                 stroke_linecap="round"))

    for cx, alt_y, half, label, gsd, note, col in (
        (260, 300, 62, "40 m", "1 cm per pixel", "small area, many photos",
         "#2f8f4e"),
        (640, 150, 150, "120 m", "3 cm per pixel", "9x the area, far fewer photos",
         "#c0392b"),
    ):
        fig.add(path(f"M{cx},{alt_y + 14} L{cx - half},{ground_y} "
                     f"L{cx + half},{ground_y} Z", fill=SHOT,
                     fill_opacity="0.12", stroke=SHOT, stroke_width=1.5,
                     stroke_dasharray="6 4"))
        fig.add(translate(cx, alt_y, aircraft_mini_side(0.62, nose=False)))
        fig.add(line(cx - half, ground_y, cx + half, ground_y, stroke=col,
                     stroke_width=5, stroke_linecap="round"))
        fig.add(text(cx, alt_y - 30, label, text_anchor="middle", font_size=16,
                     font_weight="bold", fill=P["ink"]))
        fig.add(text(cx, ground_y + 26, gsd, text_anchor="middle",
                     font_size=13.5, font_weight="bold", fill=col))
        fig.add(text(cx, ground_y + 44, note, text_anchor="middle",
                     font_size=12, fill=P["muted"]))
        # what one pixel covers, drawn to the same scale in both panels
        px = 10 if col == "#2f8f4e" else 30
        fig.add(rect(cx - px / 2, ground_y - px - 8, px, px, fill=col,
                     fill_opacity="0.35", stroke=col, stroke_width=1.5))
        fig.add(text(cx, ground_y - px - 16, "one pixel", text_anchor="middle",
                     font_size=10.5, fill=P["muted"]))

    fig.add(text(450, 500,
                 "A 5 mm crack needs roughly 1 cm pixels to show up at all. "
                 "No amount of processing recovers detail you never captured.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# 3. Nadir against oblique
# ---------------------------------------------------------------------------
def build_nadir_oblique() -> Figure:
    fig = Figure(900, 540, "Nadir, oblique, and why you often fly both",
                 "A camera pointing straight down never sees a wall. That is "
                 "the whole reason oblique passes exist.")

    for cx, nadir in ((250, True), (650, False)):
        top, gy = 84, 320
        fig.add(rect(cx - 190, top, 380, 366, **CARD))
        fig.add(text(cx, top + 30, "Nadir, camera at 0" if nadir
                     else "Oblique, camera at 30 to 45",
                     text_anchor="middle", font_size=15, font_weight="bold",
                     fill=P["ink"]))
        fig.add(line(cx - 160, gy, cx + 160, gy, stroke="#9aa7b2",
                     stroke_width=3, stroke_linecap="round"))

        bx0, bx1, roof = cx - 34, cx + 34, gy - 96
        fig.add(rect(bx0, roof, bx1 - bx0, gy - roof, fill="#c2cad2",
                     stroke=P["line"], stroke_width=1.5))

        if nadir:
            dx, dy = cx, top + 76
            fig.add(path(f"M{dx},{dy + 14} L{dx - 92},{gy} L{dx + 92},{gy} Z",
                         fill=SHOT, fill_opacity="0.12", stroke=SHOT,
                         stroke_width=1.5, stroke_dasharray="6 4"))
            fig.add(line(bx0, roof, bx1, roof, stroke="#2f8f4e",
                         stroke_width=5, stroke_linecap="round"))
            for wx in (bx0, bx1):
                fig.add(line(wx, roof, wx, gy, stroke=P["bad"],
                             stroke_width=4, stroke_dasharray="5 4"))
            fig.add(text(cx, top + 282, "roof captured, walls missed",
                         text_anchor="middle", font_size=13,
                         font_weight="bold", fill=P["bad"]))
        else:
            dx, dy = cx - 150, top + 66
            fig.add(path(f"M{dx},{dy + 14} L{cx - 6},{gy} L{cx + 74},{gy - 6} Z",
                         fill=SHOT, fill_opacity="0.12", stroke=SHOT,
                         stroke_width=1.5, stroke_dasharray="6 4"))
            fig.add(line(bx0, roof, bx1, roof, stroke="#2f8f4e",
                         stroke_width=5, stroke_linecap="round"))
            fig.add(line(bx0, roof, bx0, gy, stroke="#2f8f4e", stroke_width=5))
            fig.add(line(bx1, roof, bx1, gy, stroke=P["bad"], stroke_width=4,
                         stroke_dasharray="5 4"))
            fig.add(text(cx, top + 282, "roof and the near wall captured",
                         text_anchor="middle", font_size=13,
                         font_weight="bold", fill="#2f8f4e"))
        fig.add(translate(dx, dy, g(aircraft_mini_side(0.56, nose=False),
                                    transform="" if nadir else "rotate(18)")))
        fig.add(text(cx, top + 310, "green: surfaces the camera sees",
                     text_anchor="middle", font_size=11, fill=P["muted"]))
        fig.add(text(cx, top + 330, "red dashed: surfaces it cannot",
                     text_anchor="middle", font_size=11, fill=P["muted"]))

    fig.add(text(450, 512,
                 "One oblique pass still leaves three walls unseen. Orbit the "
                 "structure, or fly obliques from four directions.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# 4. Flight grid, redrawn
# ---------------------------------------------------------------------------
def build_grid() -> Figure:
    fig = Figure(900, 560, "A mapping grid, and when to add a second pass",
                 "Lines run one way for the survey. A perpendicular pass over "
                 "the same ground fixes what a single direction cannot.")

    fx0, fy0, fx1, fy1 = 90, 96, 690, 440
    fig.add(rect(fx0, fy0, fx1 - fx0, fy1 - fy0, rx=6, fill="#eef4ea",
                 stroke="#8aa06e", stroke_width=2))
    fig.add(text(fx0 + 8, fy0 - 10, "site boundary", font_size=12,
                 fill=P["muted"]))

    rows = [fy0 + 34 + i * 55 for i in range(6)]
    for i, y in enumerate(rows):
        left_to_right = i % 2 == 0
        fig.add(line(fx0 + 26, y, fx1 - 26, y, stroke=SHOT, stroke_width=3,
                     stroke_linecap="round"))
        if left_to_right:
            fig.add(arrow(fx1 - 70, y, fx1 - 26, y, color=SHOT, width=3))
        else:
            fig.add(arrow(fx0 + 70, y, fx0 + 26, y, color=SHOT, width=3))
        for j in range(9):
            fig.add(circle(fx0 + 40 + j * 68, y, 4.5, fill=P["white"],
                           stroke=SHOT, stroke_width=2))

    for x in (fx0 + 150, fx0 + 300, fx0 + 450):
        fig.add(line(x, fy0 + 18, x, fy1 - 18, stroke="#2f8f4e",
                     stroke_width=2.5, stroke_dasharray="9 7"))

    lx, ly = 712, 130
    fig.add(rect(lx - 12, ly - 26, 176, 150, **CARD))
    for i, (col, dash, label) in enumerate((
        (SHOT, None, "survey lines"),
        ("#2f8f4e", "9 7", "second pass,"),
    )):
        fig.add(line(lx, ly + i * 34, lx + 30, ly + i * 34, stroke=col,
                     stroke_width=3, stroke_dasharray=dash))
        fig.add(text(lx + 38, ly + i * 34 + 4, label, font_size=12,
                     fill=P["muted"]))
    fig.add(text(lx + 38, ly + 52, "at 90 degrees", font_size=12,
                 fill=P["muted"]))
    fig.add(circle(lx + 15, ly + 82, 4.5, fill=P["white"], stroke=SHOT,
                   stroke_width=2))
    fig.add(text(lx + 38, ly + 86, "photo taken", font_size=12,
                 fill=P["muted"]))

    fig.add(text(450, 500,
                 "Flat, open ground rarely needs the second pass. Tall trees, "
                 "buildings and steep slopes usually do.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# 5. Feature matching, redrawn around real photo frames
# ---------------------------------------------------------------------------
SCENE = ((0.24, 0.62), (0.40, 0.35), (0.58, 0.55), (0.74, 0.30), (0.86, 0.66))


def build_matching() -> Figure:
    fig = Figure(900, 520, "How the software ties photos together",
                 "The same corner of the same rock has to appear in several "
                 "photos before it can become a 3D point.")

    fw, fh, fy = 236, 158, 110
    frames = (78, 332, 586)
    for k, fx in enumerate(frames):
        fig.add(rect(fx, fy, fw, fh, rx=4, fill="#e4ead9", stroke=P["line"],
                     stroke_width=2))
        fig.add(rect(fx + 22 + k * 8, fy + 30, 64, 46, fill="#c2cad2",
                     stroke="#9aa7b2", stroke_width=1.2))
        fig.add(circle(fx + 176 - k * 10, fy + 108, 15, fill="#7fa87f"))
        fig.add(text(fx + fw / 2, fy - 12, f"photo {k + 1}",
                     text_anchor="middle", font_size=12.5, font_weight="bold",
                     fill=P["muted"]))
        for i, (u, v) in enumerate(SCENE):
            shifted = min(max(u - 0.10 * k, 0.06), 0.94)
            fig.add(circle(fx + shifted * fw, fy + v * fh, 4.5,
                           fill="none", stroke=P["bad"], stroke_width=2))

    # the same three features, linked between neighbouring photos
    for a, b in ((0, 1), (1, 2)):
        for u, v in SCENE[1:4]:
            ua = min(max(u - 0.10 * a, 0.06), 0.94)
            ub = min(max(u - 0.10 * b, 0.06), 0.94)
            fig.add(line(frames[a] + ua * fw, fy + v * fh,
                         frames[b] + ub * fw, fy + v * fh, stroke=P["bad"],
                         stroke_width=1.2, stroke_dasharray="4 3",
                         opacity="0.75"))

    fig.add(text(450, 316, "matched features, seen in more than one photo",
                 text_anchor="middle", font_size=12.5, fill=P["bad"]))

    # triangulation down to one 3D point
    apex = (450, 430)
    for fx in frames:
        fig.add(line(fx + fw / 2, fy + fh + 6, *apex, stroke="#9aa7b2",
                     stroke_width=1.5, stroke_dasharray="5 4"))
    fig.add(circle(*apex, 8, fill=SHOT, stroke=P["line"], stroke_width=1.5))
    fig.add(text(450, 462, "one 3D point, fixed by rays from every photo "
                 "that saw it", text_anchor="middle", font_size=12.5,
                 fill=P["muted"]))
    fig.add(text(450, 494,
                 "Blank asphalt, still water and fresh snow give the software "
                 "nothing to match, and reconstruct badly.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# 6. Orbits around a tall structure, redrawn
# ---------------------------------------------------------------------------
def build_orbit() -> Figure:
    fig = Figure(900, 500, "Orbiting a structure",
                 "A grid maps the ground. Vertical faces need the camera to "
                 "come round the side, usually at more than one height.")

    # plan view
    fig.add(rect(40, 84, 380, 330, **CARD))
    fig.add(text(230, 112, "From above", text_anchor="middle", font_size=14,
                 font_weight="bold", fill=P["ink"]))
    cx, cy = 230, 268
    fig.add(circle(cx, cy, 108, fill="none", stroke=SHOT, stroke_width=2.5,
                   stroke_dasharray="10 7"))
    fig.add(rect(cx - 30, cy - 30, 60, 60, fill="#c2cad2", stroke=P["line"],
                 stroke_width=1.5))
    for i in range(10):
        a = math.radians(i * 36 - 90)
        px, py = cx + 108 * math.cos(a), cy + 108 * math.sin(a)
        fig.add(circle(px, py, 5, fill=P["white"], stroke=SHOT,
                       stroke_width=2))
        fig.add(line(px, py, cx + 36 * math.cos(a), cy + 36 * math.sin(a),
                     stroke="#b6c2cc", stroke_width=1.2,
                     stroke_dasharray="4 3"))
    fig.add(text(230, 400, "camera always pointed inward",
                 text_anchor="middle", font_size=12, fill=P["muted"]))

    # elevation view
    fig.add(rect(460, 84, 400, 330, **CARD))
    fig.add(text(660, 112, "From the side", text_anchor="middle", font_size=14,
                 font_weight="bold", fill=P["ink"]))
    gy = 372
    fig.add(line(500, gy, 820, gy, stroke="#9aa7b2", stroke_width=3,
                 stroke_linecap="round"))
    fig.add(rect(628, 168, 64, gy - 168, fill="#c2cad2", stroke=P["line"],
                 stroke_width=1.5))
    fig.add(path("M628,168 h64", stroke=P["line"], stroke_width=1.5))
    for i, ay in enumerate((196, 262, 328)):
        for sx in (556, 764):
            fig.add(translate(sx, ay, aircraft_mini_side(0.42, nose=False)))
            fig.add(arrow(sx + (34 if sx < 660 else -34), ay,
                          sx + (74 if sx < 660 else -74), ay, color=SHOT,
                          width=2, head=8))
        fig.add(line(500, ay, 820, ay, stroke=SHOT, stroke_width=1,
                     stroke_dasharray="4 5", opacity="0.5"))
    fig.add(text(660, 400, "one ring per height, so no band of wall is missed",
                 text_anchor="middle", font_size=12, fill=P["muted"]))

    fig.add(text(450, 456,
                 "A single orbit at one height leaves the top and bottom of a "
                 "tall structure poorly reconstructed.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig



# ---------------------------------------------------------------------------
# 7. Resolution, accuracy, and how you know
# ---------------------------------------------------------------------------
def build_accuracy() -> Figure:
    fig = Figure(900, 500, "Resolution and accuracy are different questions",
                 "A map can show tiny detail and still sit in the wrong place. "
                 "Only a surveyed point tells you which you have.")

    top, w, h = 84, 270, 300
    cols = (155, 450, 745)

    # 1. resolution: can you see it at all
    cx = cols[0]
    fig.add(rect(cx - w / 2, top, w, h, **CARD))
    fig.add(text(cx, top + 32, "Resolution", text_anchor="middle",
                 font_size=15, font_weight="bold", fill=P["ink"]))
    fig.add(rect(cx - 78, top + 60, 156, 104, fill="#d9dde1",
                 stroke=P["line"], stroke_width=1.5))
    fig.add(path(f"M{cx - 66},{top + 150} L{cx - 24},{top + 108} "
                 f"L{cx + 6},{top + 128} L{cx + 62},{top + 76}",
                 fill="none", stroke="#5a6570", stroke_width=2.5))
    grid = g(stroke="#9aa7b2", stroke_width=0.6, opacity="0.9")
    for i in range(1, 12):
        grid.add(line(cx - 78 + i * 13, top + 60, cx - 78 + i * 13, top + 164))
    for j in range(1, 8):
        grid.add(line(cx - 78, top + 60 + j * 13, cx + 78, top + 60 + j * 13))
    fig.add(grid)
    fig.add(text(cx, top + 196, "Can you see it at all?", text_anchor="middle",
                 font_size=13, font_weight="bold", fill=SHOT))
    fig.add(text(cx, top + 220, "Set by GSD. A 5 mm crack needs",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 238, "pixels of about 1 cm to appear.",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 268, "Fly lower to improve it.",
                 text_anchor="middle", font_size=11.5, font_style="italic",
                 fill=P["muted"]))

    # 2. accuracy: is it in the right place
    cx = cols[1]
    fig.add(rect(cx - w / 2, top, w, h, **CARD))
    fig.add(text(cx, top + 32, "Accuracy", text_anchor="middle", font_size=15,
                 font_weight="bold", fill=P["ink"]))
    ty = top + 112
    for r in (58, 40, 22):
        fig.add(circle(cx, ty, r, fill="none", stroke="#c5cdd5",
                       stroke_width=1.5))
    fig.add(line(cx - 68, ty, cx + 68, ty, stroke="#c5cdd5", stroke_width=1))
    fig.add(line(cx, ty - 68, cx, ty + 68, stroke="#c5cdd5", stroke_width=1))
    fig.add(circle(cx, ty, 4, fill="#2f8f4e"))
    fig.add(text(cx + 10, ty + 16, "true position", font_size=10.5,
                 fill="#2f8f4e"))
    for dx, dy in ((26, -30), (34, -22), (30, -38), (40, -30), (24, -22)):
        fig.add(circle(cx + dx, ty + dy, 4, fill=P["bad"]))
    fig.add(arrow(cx + 4, ty - 4, cx + 26, ty - 26, color=P["bad"], width=2,
                  head=8))
    fig.add(text(cx, top + 196, "Is it in the right place?",
                 text_anchor="middle", font_size=13, font_weight="bold",
                 fill=SHOT))
    fig.add(text(cx, top + 220, "Tight measurements can still all be",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 238, "shifted together, and look convincing.",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 268, "Flying lower does not fix this.",
                 text_anchor="middle", font_size=11.5, font_style="italic",
                 fill=P["muted"]))

    # 3. ground truth: how you would know
    cx = cols[2]
    fig.add(rect(cx - w / 2, top, w, h, **CARD))
    fig.add(text(cx, top + 32, "Ground truth", text_anchor="middle",
                 font_size=15, font_weight="bold", fill=P["ink"]))
    gy2 = top + 140
    fig.add(line(cx - 92, gy2, cx + 92, gy2, stroke="#9aa7b2", stroke_width=3,
                 stroke_linecap="round"))
    for i, tx in enumerate((cx - 62, cx + 4, cx + 66)):
        fig.add(rect(tx - 13, gy2 - 26, 26, 26, fill=P["white"],
                     stroke=P["line"], stroke_width=1.5))
        fig.add(rect(tx - 13, gy2 - 26, 13, 13, fill=P["line"]))
        fig.add(rect(tx, gy2 - 13, 13, 13, fill=P["line"]))
    fig.add(text(cx, gy2 + 22, "surveyed targets on the ground",
                 text_anchor="middle", font_size=11, fill=P["muted"]))
    fig.add(text(cx, top + 196, "How would you know?", text_anchor="middle",
                 font_size=13, font_weight="bold", fill=SHOT))
    fig.add(text(cx, top + 220, "Ground control points fix the map to",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 238, "real coordinates. Extra checkpoints,",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))
    fig.add(text(cx, top + 256, "held back, prove how close you got.",
                 text_anchor="middle", font_size=11.5, fill=P["muted"]))

    fig.add(text(450, 456,
                 "Without ground control, a map with 1 cm pixels can sit "
                 "several metres from where it belongs.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="review")
    ap.add_argument("--png", action="store_true")
    args = ap.parse_args()

    for builder, slug in (
        (build_overlap, "w04_proposed_overlap"),
        (build_gsd, "w04_proposed_gsd_altitude"),
        (build_nadir_oblique, "w04_proposed_nadir_oblique"),
        (build_grid, "w04_proposed_grid"),
        (build_matching, "w04_proposed_matching"),
        (build_orbit, "w04_proposed_orbit"),
        (build_accuracy, "w04_proposed_accuracy"),
    ):
        fname = os.path.join(args.out, slug + ".svg")
        builder().save(fname)
        print("wrote", fname)
        if args.png:
            png = render_png(fname)
            if png:
                print("wrote", png)


if __name__ == "__main__":
    main()
