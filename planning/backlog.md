# Backlog

Open items, ideas, and known gaps. Move items to "Done" with the date rather than deleting them.

## Build warnings (a clean `mkdocs build --strict` should pass)

- [ ] `mkdocs.yml` links Week 1 "Flight Basics" to `week_01/DJI_Mini_Basics.md`, but that file does
      not exist and is not in git history. Commit `d173bd4` added the nav entry without staging the
      page. Being replaced by the new `week_01/flight_basics.md` (see the Flight Basics section
      below). This is the only warning in the current build.
- [ ] `docs/coming_soon.md` is not in the nav. Decide whether it and
      `docs/images/logo_with_coming_soon.png` are still needed.
- [ ] `docs/week_05/Week_5_60_Question_Exam_Instructor_Key (1).md` is a stray duplicate of the
      instructor key and is not in the nav. Confirm and remove.

## Content gaps

- [ ] Week 5 `FAA_Exam_Planning_and_Overview.md` has captions for Figures 15, 16, 19, 20, 24, 25,
      and 27, but no matching image files exist. Those captions currently sit under nothing.
      Either draw the figures or remove the captions.
- [ ] `docs/flight_check_list/post_flight/post_general.md` has an empty checklist, and its intro is
      a copy of the pre-flight text that still says "before every flight".
- [ ] `docs/flight_check_list/pre_flight/pre_general.md` says "click on the links below for
      drone-specific pre-flight checklists" but has no links.

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
- [ ] Phase 1 — page skeleton, flight checklist landing page, nav fix, clean strict build.
- [ ] Phase 2 — sections, each as figure then caption: aircraft parts, controller, stick controls,
      how it flies, automated functions, basic flight, payloads and rules.
- [ ] Phase 3 — linked pages: common flight issues, feature-availability table, checklist cross-links.
- [ ] Phase 4 — optional animation on three figures, full read-through, backlog update.

## Done

- 2026-09-03 — Added tracked `planning/` folder, root `CLAUDE.md`, git-ignored `.claude/local/`
  and `review/` folders.
- 2026-09-03 — Built `fig_tools/` (SVG toolkit, reusable parts, controller figure script) and
  recorded the figure style rules in `instructions.md`. Folder named `fig_tools`, not `figures`,
  so it is not mistaken for a folder of images.
