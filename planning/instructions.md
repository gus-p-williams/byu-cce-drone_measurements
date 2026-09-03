# Working Instructions

General conventions for anyone (human or AI) editing this repository.

## Voice and level

- Write for a first-semester student. Define every acronym on first use (UAS, SfM, GSD, AGL, VLOS).
- Prefer short paragraphs and concrete examples from civil engineering or construction sites.
- Tie techniques back to engineering judgment: accuracy needed, effort required, and why it matters.
- Use metric and US customary units together where students will see both in practice.

## Page structure

Each content page should follow the pattern established in Weeks 1 through 5:

1. `# Title` as the first line.
2. A `!!! abstract "Key Takeaways"` admonition with three to five bullets.
3. `---` separators between major sections.
4. `## Section` headings, with `###` for subsections. Avoid going deeper than `###`.
5. Optional closing sections: "Summary", "Check Your Understanding", or "Resources".

Use admonitions consistently: `abstract` for takeaways, `note` for asides, `warning` for safety or
regulatory cautions, `tip` for practical advice, `example` for worked problems.

## Files and naming

- Put each week's pages in `docs/week_NN/`. Images go in `docs/week_NN/images/`.
- Use descriptive file names with underscores, matching existing pages (for example
  `Mission_Planning_SfM.md`). Do not leave duplicate or numbered copies such as `file (1).md`.
- Prefer SVG for diagrams and keep raster images under a few hundred kilobytes.
- Any new page must be added to `nav:` in `mkdocs.yml`, or it will build but not appear.

## Figures

- Prefer a figure with a one-sentence caption over a paragraph. Aim for one figure per concept.
- All figures are SVG. Write the SVG directly for one-off drawings, or generate it with a script in
  `fig_tools/` when parts repeat or a numbered homework variant is needed. Scripts write their SVG
  into `docs/week_NN/images/`, and both the script and the SVG are committed.
- Style is fixed so every week matches: light gray background with rounded corners, Arial font
  stack, 14 px labels, 17 px bold title at the top of the figure, 12 px subtitle for caveats,
  blue leader lines ending in a dot on the part. Palette and sizes live in `fig_tools/svgkit.py`.
- Drawings are generic. Brand names go in captions or tables, not in the picture. Where hardware
  varies between models, say so in the subtitle or caption.
- Keep text as text in the SVG. Do not convert labels to paths.
- File names: `figNN_short_name.svg` inside the week's `images/` folder, numbered in page order.
  The Markdown caption is an italic line under the image: `*Figure NN: ...*`
- Check every figure by rendering it to PNG (Inkscape command line, or `--png` on the script)
  and looking at it before committing.

## Before committing

- Build locally to catch broken links and nav errors:

  ```
  pip install mkdocs pymdown-extensions python-markdown-math mkdocs-cinder
  mkdocs build --strict
  mkdocs serve
  ```

- Do not commit `site/`, large PDFs, or anything under `.claude/local/`.
- Write commit messages that say which week and which page changed, matching the existing history
  (for example, "Standardize Week 4 SfM and Mission Planning materials").

## Working with Claude Code

- Project-wide context lives in this folder and is loaded through the root `CLAUDE.md`.
- Session notes, drafts, experiments, and anything you would not want a collaborator to read go in
  `.claude/local/` (git-ignored). Promote anything durable into `planning/` when it is ready.
- Draft figures, renders, and page drafts that are ready for Gus to look at go in `review/`
  (git-ignored). Files there are temporary: once approved they are moved to their real home
  (`docs/week_NN/images/`, `docs/week_NN/`, or `fig_tools/`) and added to git there; once rejected
  they are deleted. Clean `review/` out after each approved batch. See `review/README.md`.
- When asked to create or reorganize a week, update `mkdocs.yml`, the page itself, and
  `planning/backlog.md` if the work leaves anything unfinished.
