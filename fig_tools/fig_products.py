"""Illustrations and example placeholders for the Week 1 data products page.

Captions, no figure numbers: nothing refers to these by number, so the numbered
sequence on Flight Basics and Common Flight Issues stays untouched.

The example tiles are deliberately separate files rather than one composite, so
each can be swapped for a real image independently as data becomes available.

Usage:
    python fig_tools/fig_products.py --png
    python fig_tools/fig_products.py --out docs/week_01/images

Outputs:
    w01_products_family.svg              what comes from what
    w01_products_surface_vs_terrain.svg  what the model keeps and removes
    w01_example_<product>.svg            one placeholder per product
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from svgkit import PALETTE as P  # noqa: E402
from svgkit import (Figure, arrow, circle, figure_name, g, line,  # noqa: E402
                    path, rect, render_png, text)

CARD = dict(rx=10, fill=P["white"], stroke="#dde3e9", stroke_width=1.5)
BOX_W, BOX_H = 132, 54


def box(cx, cy, label, sub=None, accent=False):
    grp = g(rect(cx - BOX_W / 2, cy - BOX_H / 2, BOX_W, BOX_H, rx=8,
                 fill="#cfe3f7" if accent else P["white"],
                 stroke=P["accent"] if accent else "#c5cdd5",
                 stroke_width=2 if accent else 1.5))
    grp.add(text(cx, cy + (-2 if sub else 5), label, text_anchor="middle",
                 font_size=13, font_weight="bold", fill=P["ink"]))
    if sub:
        grp.add(text(cx, cy + 15, sub, text_anchor="middle", font_size=10.5,
                     fill=P["muted"]))
    return grp


def elbow(x0, y0, x1, y1):
    """A right-angled connector, so nothing crosses anything else."""
    mid = x0 + (x1 - x0) / 2
    return g(path(f"M{x0},{y0} H{mid} V{y1} H{x1 - 12}", fill="none",
                  stroke="#b6c2cc", stroke_width=2.5),
             arrow(x1 - 16, y1, x1, y1, color="#b6c2cc", width=2.5, head=9))


# ---------------------------------------------------------------------------
# What comes from what
# ---------------------------------------------------------------------------
def build_family() -> Figure:
    fig = Figure(900, 585, "What comes from what",
                 "The sensor you fly decides which products you can make. "
                 "Everything below starts as overlapping images.")

    fig.add(text(30, 92, "From a normal camera", font_size=14,
                 font_weight="bold", fill=P["accent"]))
    photos = (96, 196)
    ortho = (296, 122)
    cloud = (296, 272)
    dsm = (486, 226)
    mesh = (486, 336)
    dtm = (664, 226)
    cont = (830, 226)
    for a, b in ((photos, ortho), (photos, cloud), (cloud, dsm),
                 (cloud, mesh), (dsm, dtm), (dtm, cont)):
        fig.add(elbow(a[0] + BOX_W / 2, a[1], b[0] - BOX_W / 2, b[1]))
    fig.add(box(*photos, "Photos", "the raw flight", accent=True))
    fig.add(box(*ortho, "Orthomosaic", "one flat image"))
    fig.add(box(*cloud, "Point cloud", "millions of points"))
    fig.add(box(*dsm, "DSM", "surface heights"))
    fig.add(box(*mesh, "3D model", "a solid, textured mesh"))
    fig.add(box(*dtm, "DTM", "bare ground"))
    fig.add(box(*cont, "Contours", "lines to draw with"))

    fig.add(line(30, 396, 870, 396, stroke="#dde3e9", stroke_width=2))
    fig.add(text(30, 428, "From a specialist sensor", font_size=14,
                 font_weight="bold", fill=P["accent"]))
    fig.add(text(262, 428, "(covered in Week 6)", font_size=12,
                 fill=P["muted"]))
    for y, src, srcsub, out, outsub in (
        (474, "Thermal camera", "temperature", "Thermal mosaic",
         "hot and cold across a site"),
        (534, "Multispectral", "extra light bands", "Index maps",
         "such as NDVI for plant health"),
    ):
        fig.add(elbow(96 + BOX_W / 2, y, 240, y))
        fig.add(box(96, y, src, srcsub, accent=True))
        fig.add(g(rect(240, y - BOX_H / 2, 192, BOX_H, rx=8,
                       fill=P["white"], stroke="#c5cdd5", stroke_width=1.5),
                  text(336, y - 2, out, text_anchor="middle", font_size=13,
                       font_weight="bold", fill=P["ink"]),
                  text(336, y + 15, outsub, text_anchor="middle",
                       font_size=10.5, fill=P["muted"])))

    fig.add(text(700, 494, "Same aircraft, same flight plan.",
                 text_anchor="middle", font_size=12.5, fill=P["muted"]))
    fig.add(text(700, 514, "Only the camera changes.",
                 text_anchor="middle", font_size=12.5, fill=P["muted"]))
    return fig


# ---------------------------------------------------------------------------
# Example placeholders, one per product
# ---------------------------------------------------------------------------
EXAMPLES = (
    ("ortho", "Orthomosaic", "a stitched, scaled top-down image of a site"),
    ("point_cloud", "Point cloud", "a screenshot with the points colored"),
    ("dsm", "DSM", "a height map, colored low to high"),
    ("dtm", "DTM", "the same site with buildings and trees removed"),
    ("model_3d", "3D model", "an oblique view of the textured mesh"),
    ("contours", "Contours", "contour lines over the site"),
    ("thermal", "Thermal", "a thermal image beside the same view in color"),
    ("multispectral", "Multispectral", "an NDVI or index map of vegetation"),
)


def build_example(label, hint) -> Figure:
    fig = Figure(560, 380, None, None)
    fig.add(rect(20, 20, 520, 340, rx=14, fill="#eef1f4", stroke="#c5cdd5",
                 stroke_width=2.5, stroke_dasharray="12 9"))
    cx, cy = 280, 158
    fig.add(rect(cx - 74, cy - 54, 148, 108, rx=8, fill=P["white"],
                 stroke="#c5cdd5", stroke_width=2))
    fig.add(path(f"M{cx - 62},{cy + 40} L{cx - 18},{cy - 12} "
                 f"L{cx + 12},{cy + 18} L{cx + 44},{cy - 22} "
                 f"L{cx + 62},{cy + 40} Z", fill="#dbe2e8"))
    fig.add(circle(cx + 40, cy - 30, 11, fill="#dbe2e8"))
    fig.add(text(cx, 252, label, text_anchor="middle", font_size=21,
                 font_weight="bold", fill=P["muted"]))
    fig.add(text(cx, 280, "example to come", text_anchor="middle",
                 font_size=14, fill="#8fa3b5"))
    fig.add(text(cx, 316, hint, text_anchor="middle", font_size=12,
                 font_style="italic", fill="#8fa3b5"))
    return fig


# ---------------------------------------------------------------------------
# Surface model against terrain model (moved here from the overview page)
# ---------------------------------------------------------------------------
def build_surface_vs_terrain() -> Figure:
    fig = Figure(900, 420, "What the model includes",
                 "Same flight, same site, two different surfaces. Which one you "
                 "need depends on the question.")

    for cx, keep in ((250, True), (650, False)):
        top, gy = 84, 268
        fig.add(rect(cx - 190, top, 380, 250, **CARD))
        fig.add(text(cx, top + 30,
                     "Surface model (DSM)" if keep else "Terrain model (DTM)",
                     text_anchor="middle", font_size=15, font_weight="bold",
                     fill=P["ink"]))
        fig.add(text(cx, top + 50,
                     "everything the drone saw" if keep
                     else "bare ground, trees and buildings stripped out",
                     text_anchor="middle", font_size=11.5, fill=P["muted"]))

        op = "1" if keep else "0.22"
        fig.add(g(rect(cx - 26, gy - 74, 52, 42, fill="#c2cad2",
                       stroke=P["line"], stroke_width=1.5), opacity=op))
        for tx, th in ((cx - 108, 46), (cx + 92, 38)):
            base = gy - 30 if tx < cx else gy - 44
            fig.add(g(line(tx, base, tx, base - th * 0.4, stroke="#8a6a45",
                           stroke_width=4),
                      circle(tx, base - th * 0.62, th * 0.42, fill="#7fa87f",
                             stroke="#5f855f", stroke_width=1.5), opacity=op))

        fig.add(path(f"M{cx - 150},{gy} L{cx - 60},{gy - 34} "
                     f"L{cx + 30},{gy - 22} L{cx + 150},{gy - 58}",
                     fill="none", stroke="#9a8f78", stroke_width=3))
        if keep:
            fig.add(path(f"M{cx - 150},{gy - 4} L{cx - 130},{gy - 12} "
                         f"L{cx - 108},{gy - 62} L{cx - 86},{gy - 22} "
                         f"L{cx - 26},{gy - 78} L{cx + 26},{gy - 74} "
                         f"L{cx + 70},{gy - 32} L{cx + 92},{gy - 70} "
                         f"L{cx + 114},{gy - 40} L{cx + 150},{gy - 62}",
                         fill="none", stroke=P["accent"], stroke_width=3,
                         stroke_linejoin="round"))
        else:
            fig.add(path(f"M{cx - 150},{gy} L{cx - 60},{gy - 34} "
                         f"L{cx + 30},{gy - 22} L{cx + 150},{gy - 58}",
                         fill="none", stroke=P["accent"], stroke_width=3,
                         stroke_dasharray="9 6"))

        fig.add(text(cx, top + 226,
                     "use it to check clearances and heights" if keep
                     else "use it for earthwork, drainage and grading",
                     text_anchor="middle", font_size=12.5, fill=P["muted"]))

    fig.add(text(450, 396,
                 "Digital Elevation Model (DEM) is the umbrella term you will "
                 "also hear for both of these.",
                 text_anchor="middle", font_size=13, font_style="italic",
                 fill=P["muted"]))
    return fig


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="review")
    ap.add_argument("--png", action="store_true")
    args = ap.parse_args()

    jobs = [(build_family, "products_family"),
            (build_surface_vs_terrain, "products_surface_vs_terrain")]
    for slug, label, hint in EXAMPLES:
        jobs.append((lambda l=label, h=hint: build_example(l, h),
                     f"example_{slug}"))

    for builder, slug in jobs:
        fname = os.path.join(args.out, figure_name(1, None, slug))
        builder().save(fname)
        print("wrote", fname)
        if args.png:
            png = render_png(fname)
            if png:
                print("wrote", png)


if __name__ == "__main__":
    main()
