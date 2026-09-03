# Backlog

Open items, ideas, and known gaps. Move items to "Done" with the date rather than deleting them.

## Build warnings

`mkdocs build --strict` currently passes with no warnings. Keep it that way.

- [ ] `docs/coming_soon.md` is not in the nav. Decide whether it and
      `docs/images/logo_with_coming_soon.png` are still needed. (Reported as INFO, not a warning.)
- [ ] `docs/week_05/Week_5_60_Question_Exam_Instructor_Key (1).md` is a stray duplicate of the
      instructor key and is not in the nav. Confirm and remove.

## Content gaps

- [ ] Week 5 `FAA_Exam_Planning_and_Overview.md` has captions for Figures 15, 16, 19, 20, 24, 25,
      and 27, but no matching image files exist. Those captions currently sit under nothing.
      Either draw the figures or remove the captions.
- [ ] Neither flight checklist links to drone-specific lists yet. Both pages now say those will be
      added rather than promising links that do not exist. Write them when the fleet is settled.

## Housekeeping

- [ ] Week 6 uses raw `<img src="../images/...">` tags in seven places. MkDocs does not rewrite
      paths inside raw HTML, so these work only because clean URLs are on. Convert them to Markdown
      images with `attr_list` for sizing, matching the other weeks.
- [ ] `test_image.jpg` and `mkdocs_thermal_page.html` sit at the repository root. Move them into
      `docs/` if they are used, otherwise remove them.
- [ ] `docs/requirements.txt` is published to the site root, because MkDocs copies every file in
      `docs/`. Harmless, but worth knowing before putting anything else in `docs/`.

## Ideas

- [ ] Add a course-wide glossary page for acronyms (UAS, SfM, GSD, AGL, VLOS, GCP, RTK).
- [ ] Add "Check Your Understanding" questions to Weeks 1 through 4 to match the Week 5 practice exams.
- [ ] Decide whether instructor answer keys should stay on the public site or move to a private
      location.

## In progress: Week 1 Flight Basics

Plan agreed September 2026. Generic, figure-led page in Week 1, with detail moved to linked pages.

- [x] Phase 0 — figure style approved; `fig_tools/` toolkit and generic controller figure built.
- [x] Phase 1 — page skeleton, flight checklist landing page, post-flight list, nav fix,
      clean strict build. Awaiting instructor review of the checklist overview prose.
- [ ] Phase 2 — sections, each as figure then caption. Done: aircraft parts (fig 1), how a drone
      flies (figs 4-6), the controller (fig 7), stick controls (figs 8-9). Remaining: payloads
      (fig 3), basic flight (figs 10-11), automated functions (figs 12-15), rules, check your
      understanding, resources. Figure 2 (underside view) still optional.
- [ ] Phase 3 — linked pages: common flight issues, feature-availability table, checklist cross-links.
- [ ] Phase 4 — optional animation on three figures, full read-through, backlog update.

## Done

- 2026-09-03 — Added tracked `planning/` folder, root `CLAUDE.md`, git-ignored `.claude/local/`
  and `review/` folders.
- 2026-09-03 — Built `fig_tools/` (SVG toolkit, reusable parts, controller figure script) and
  recorded the figure style rules in `instructions.md`. Folder named `fig_tools`, not `figures`,
  so it is not mistaken for a folder of images.
- 2026-09-03 — Week 1 Flight Basics: aircraft parts, how a drone flies, the controller, and
  stick controls written, with seven generated figures. Automated Flight Functions moved below
  A Basic Flight so students meet manual flying first.
- 2026-09-03 — Fixed the Week 1 nav entry (`DJI_Mini_Basics.md` never existed) by adding
  `week_01/flight_basics.md`. Added `flight_check_list/index.md`, filled the empty post-flight
  checklist, and removed the dangling "links below" promise from both checklist pages. The strict
  build is now clean.
