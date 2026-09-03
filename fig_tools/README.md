# Figure tools

Python scripts that generate SVG figures for the course pages. This folder holds the **tools**, not
the pictures. Generated SVGs live with the page that uses them, in `docs/week_NN/images/`, and are
committed there, so Read the Docs never runs these scripts.

Re-run a script when a figure needs to change, then commit both the script and the regenerated SVG.

Nothing in this folder may move under `docs/`. MkDocs copies every file in `docs/` to the published
site, including scripts.

## Layout

| File | Purpose |
|------|---------|
| `svgkit.py` | Tiny SVG builder, shared palette and fonts, callout helper, optional PNG render through Inkscape |
| `parts.py` | Reusable drawings: controller, and later the aircraft and stick glyph, each with anchor points for callouts |
| `fig_*.py` | One script per figure or figure family. Each writes to `review/` by default |

No third-party packages are required. Any Python 3.8 or newer works.

## Running

```
python fig_tools/fig_controller.py --png
python fig_tools/fig_controller.py --out docs/week_01/images
```

`--png` renders a PNG next to each SVG using Inkscape if it is installed, which is the quickest
way to check a figure. The PNG is for checking only; the site uses the SVG.

If a script reports that Inkscape was not found, point it at the executable:

```
set INKSCAPE=C:\Program Files\Inkscape\bin\inkscape.com
```

## Conventions

- Draw in a fixed `viewBox` between 700 and 900 units wide. Height as needed.
- Title at the top inside the figure, subtitle when a caveat belongs with the picture.
- Labels are real text, never paths, so they stay searchable and editable.
- Colors and fonts come from `svgkit.PALETTE` and `svgkit.FONT`. Do not hard-code new colors.
- Generic drawings. Brand names appear only in captions or tables, never in the figure.
- Figures that need a numbered variant for homework build both from one script.
