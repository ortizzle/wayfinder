# Claude Guide — Wayfinder

> **This repo is public.** Names, schools, teachers and Drive folder IDs are
> deliberately absent here — they live in the `roster` record (entered in the
> grown-up settings, carried by the private Gist) and in Claude's private
> project memory. Do not paste them back into any tracked file.

A learning PWA for one **4th-grade** student on a rotating timetable, SY 2026–27.

Same engine as [Ad Astra](../ad-astra), the older sibling's app — record store, Gist sync,
study plan, tutor, focus timer, emotion checks, parent view all work identically.
**Read `../ad-astra/CLAUDE.md` first**; everything there applies unless listed
below. This file documents only what differs.

---

## Pitch it a year or two up

Both siblings attend a school that teaches roughly a year ahead, and they read and
behave accordingly. This student is 9, but the material and tone should land like
**middle school**, not lower primary. Ad Astra is pitched at high school for the
same reason.

Concretely: short sentences and ordinary words, but **never** baby
talk, never exclamation marks, never "great job!" — she gets a real explanation
said plainly. The model prompts for the tutor and unit generation both say this
explicitly; keep that if you edit them.

---

## The schedule rotates — this is the main structural difference

Ad Astra's timetable is identical every weekday, so it uses a flat `CLASSES`
array. This one rotates, so it uses:

- `SUBJECTS` — every subject once, with its room, icon and default colour.
- `SLOTS` — nine fixed time ranges, **identical every weekday**.
- `WEEK` — `{1..5}` (Mon–Fri) → nine subject ids, one per slot.
- `dayClasses(dateStr)` — merges the two into the day's actual line-up.
- `daysFor(id)` — "Every day", "Mon & Thu", "Mon, Tue & Fri".

Only slots 2, 6 and 8 change across the week. Slots 1, 3, 4, 5, 7 and 9 are
always Math, English, Recess, Lunch, Science, History.

| | Slot 2 (8:35) | Slot 6 (11:05) | Slot 8 (12:55) |
|---|---|---|---|
| Mon | Musical Theatre | PE | Writing |
| Tue | Visual Arts | PE: Martial Arts | Writing |
| Wed | Computer Enrichment | PE | Engineering & Tech |
| Thu | PE: Martial Arts | Musical Theatre | Study Hall |
| Fri | Engineering & Tech | Writing | Visual Arts |

**Anything reading the schedule must call `dayClasses(date)`** — never iterate a
global class list, because there isn't one.

This `.ics` has **no teacher names** (Ad Astra's did), so no teacher shows unless
one is entered in `roster`. The orientation unit drills rooms *and the rotation* instead, since
knowing that Art is Tue & Fri is the genuinely useful week-one fact.

---

## Calendar

`CAL.events` is populated here from the school's weekly newsletter and its
save-the-dates slide — Mini-Comps, Fast Bridge, early-release days, performances,
community evenings, and the 4th Grade Promotion. See `../ad-astra/CLAUDE.md` for
how the layer works. **Primary does have Mini-Comps** (Aug 11-12) despite having
no Pre-Comp or Comp exams; do not assume "no comps at primary".


the primary school publishes its own calendar. Same first/last day
(2026-08-03 → 2027-05-21), same quarters and the same closure dates as the upper
school, but: **parent/teacher conferences** on 10/2 and 3/12 instead of comp
exams, and **Project Week is 5/17–5/20** (the upper school's runs to 5/21). There are no
Pre-Comp or Comp exams in primary — don't copy those milestones across.

---

## Identity

Deliberately not a re-skin of Ad Astra — the siblings should not feel like they
got the same app.

- Base is a **plum-violet night sky** — deep purple canvas with a faint starfield
  layered above the colour washes (`--stars`, dark mode only; `none` in light).
  Ad Astra is teal-black, so the two never read as the same app.
- Default accent is **Blossom** (pink); her picker leads with pink and purple —
  Blossom / Orchid / Lilac / Rose / Sky / Mint. Pink and purple were her request.
- Avatars lean playful-celestial (🌸 🦄 🦋 🐉 🌙 ⭐ …).
- Every accent was measured against both canvases: worst case 6.4:1, so all of
  them clear WCAG AA. Keep new options in that range.
- Subject textures: graph paper (Math), ruled paper (English), tighter rules
  (Writing), cell dots (Science), columns (History), blueprint grid
  (Engineering), pixel grid (Computers), paint spatter (Art), curtain (Theatre).

Storage namespace is `wayfinder_` and the Gist file is `wayfinder-data.json`, so
the two apps never collide even on a shared device or a shared Gist token.

---

## Drive

Class material and the backup folder both live in Drive. The folder IDs are in
Claude's private project memory, and the backup link is set per-device in the
grown-up settings — neither belongs in this repo.

---

## Keeping the two apps in step

The engine is duplicated, not shared — deliberately, to keep both single-file and
buildless. When you fix an engine bug (sync, streaks, timer, quiz), **check
whether the other app has it too**. Content, schedule, calendar, palette and copy
are meant to diverge; the engine is not.

### Pending parity: Ad Astra v20–v22 (2026-08, Chris-approved for BOTH apps)

Ad Astra shipped a run of engine/UX features this app does not have yet. Port
them before (or alongside) River's first real study unit:

- **v20** — `renderGraph()` worksheet-style SVG graphs on cards/questions/review/
  Growth Zone; `\n• ` bullet rendering (white-space:pre-line); grid-stacked
  flashcard faces that grow to fit content; graph support in `UNIT_SCHEMA` +
  generation prompt.
- **v21** — back-stack navigation with ← chips; quiz **rounds of 5** picking
  least-practised questions; Beat-the-clock countdown calibrated from her
  measured per-answer pace (`ansSeconds`/`ansCount` on logs, clamped 8–40s);
  varied encouragement (`CHEER_RIGHT`/`CHEER_WRONG` + streak lines); left-aligned
  card definitions (terms stay centered); formulas in Fraunces italic.
- **v22** — `**bold**` answer-first card definitions via `richify()`; subject-
  coloured accent on study screens (`--ac` override on `#screen`); looser button
  spacing; visible `APP_VERSION` in Settings (bump with `CACHE_VERSION`, same
  number); orientation unit retired (schema v4 tombstones it on migrate);
  affirmation heart/read are toggles (undo removes the day's XP only when both
  come off).

### Content rules (apply here exactly as in Ad Astra)

See "Content rules" in ad-astra/CLAUDE.md — standalone questions (no worksheet
references), bold-answer-first defs with bullets, graphs wherever they teach,
formulas in `eq`, independently verified answers, drafts-only pushes, warm
varied encouragement. Same standards, River-appropriate pitch (a year up from
4th grade, per this file).
