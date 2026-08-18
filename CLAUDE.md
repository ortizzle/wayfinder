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

### Student hours (v22, updated v33)

`STUDENT_HOURS` carries the teachers' help-hours (times only — teacher names
live in `roster`, never in this public file). Source of truth is the **weekly
newsletter** (which superseded the syllabi in week one): English & Writing on
Mondays, History on Tuesdays, Math & Science on Thursdays — 7:00–7:30 am or
3:30–4:00 pm. `HOURS_START` (2026-08-17, from the first newsletter) gates both
render sites so hours don't show before they exist. Rendered in three places:
a quiet card on Today for the day being shown, a hintline on the subject's
unit screen, and the parents' own hours in the grown-up Class details card.
When a newsletter changes the schedule, edit the constant and redeploy.

**Confirmed unchanged by the 8/14 newsletter** (v78): Math & Science Thursdays,
English & Writing Mondays, History Tuesdays, all 7:00–7:30 am or 3:30–4:00 pm,
starting the week of 8/17. The newsletter also carries each teacher's PARENT
hours, which the app does not store anywhere — a gap, if it is ever wanted.

**A window is only offered while it is still ahead of her** (`usableTimes`).
Two ways it can fail to be, both of which the runway card got wrong at first:
a slot on the day of the test that runs *after* school (the quiz is already
over), and a slot earlier today that has simply passed. Real case from that
newsletter — History hours are Tuesdays and the History quiz is Tuesday 8/18,
so "7:00–7:30 am or 3:30–4:00 pm — the last one before it" was half wrong. It
now trims to the morning and says "the morning of, and the last chance", and
drops the day entirely when nothing is left (Ad Astra's `algeo` hours are
afternoon-only, so a Tuesday test has no usable window at all).

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

Light mode is **blossom-warmed paper** (v75) — tinted ground, white cards,
washes visible — where Ad Astra's is sea-glass. The paper colours are
identity; the rule that every reading token holds 4.5:1 against the page,
the card, the raised surface and the wash-tinted worst case is engine
(`tools/contrast_light.js`).

Personalization (skies, celebration styles, subject icons, badge pins,
companion extras) works as documented in ad-astra/CLAUDE.md — only the rosters
differ here: skies are Starfield / Aurora / Blossom Drift / Deep Ocean / River,
and `ICON_CHOICES`/`AVATARS` lean playful. Rosters are identity; keep them
divergent.

### River, and what a sky is allowed to do (v72)

River asked for a water theme; it ships as a **sky**, not a replacement, so
she picks it herself and can back out for free. It is the first sky that is
not wash-only, which changes the contract:

- **Every other sky sets `--wash-1/2` and nothing else** — deliberately, so
  the contrast measurements taken against the plum canvas stay valid for all
  of them. River repaints the canvas itself (`--ink`, `--deep`, `--surface`,
  `--raised`, `--line`, `--text`, `--muted`, `--faint`).
- **So the rule is now: a sky MAY override the surface tokens, and when it
  does, every accent is re-measured against it in BOTH themes before it
  ships.** `contrast_sky.js` walks accent × sky × theme — 300 samples. River's
  worst case is **5.79:1**, the best of the five; its light `--muted`/`--faint`
  measured **4.39:1** on the first pass and were deepened to `#3a5c72` /
  `#3f647b`. A new full-canvas sky without that sweep is not shippable.
- **Blue, never teal.** Ad Astra owns teal-black and the two apps must never
  read as the same app.
- **The accent is untouched**, so her Blossom pink rides on top of deep water
  — that combination is the point, not a compromise.
- `--stars` becomes a **current** rather than a starfield: slow diagonals with
  a little spray caught in them. Dark mode only, `none` in light, same as
  every other sky.

The Sky Map (see ad-astra/CLAUDE.md) works identically, but this app's
`CONSTELLATIONS` are invented and playful (The Otter, The Skipping Stone…)
where Ad Astra's are the real sky. Same rule as everything else: the engine
travels, the roster does not.

### The companion (Wayfinder-only, v13)

A creature she picks and names in Settings (`prefs.companion = {sp, nm}`,
synced; `null` = off, and "—" in the picker is a real choice). It is a
**messenger, not a second voice**: every line comes from the curated
`COMPANION_*` pools or is assembled from `studyPlan()`/`dueMisses()` — never
from the model. Deliberate rules, do not relax:

- **Never interrupts.** It appears in exactly two places: a perch on Study
  (one deterministic line per day — due reviews first, else top of the study
  plan, else an idle line) and in the quiz-results modal. Never mid-question,
  never over the timer.
- **Never sad or disappointed.** Under-80% quizzes get the `COMPANION_STEADY`
  pool — calm and forward-looking. A drooping creature would re-moralize the
  Growth Zone and import the Duolingo guilt mechanic on purpose-built grounds.
- **Process praise only**, same Dweck grounding as the affirmations. No trait
  praise, no exclamation marks.
- **No care-and-feeding mechanics, no stored counters.** It owns no records
  and no XP.

Ad Astra started without one — a mascot is high-risk condescension at 13 —
but she asked (2026-08), which was the agreed bar, so it now has its own:
different roster (night-sky/ocean, no unicorns), drier copy, same rules.
The two are still **not** parity items: rosters and line pools are identity
and are meant to diverge; only the rules travel.

**Species voices** (`COMPANION_VOICES`): a species listed there overrides the
default pools; everyone else falls back. The dolphin's voice is hers — bright,
warm, openly affectionate. Warmth lands on the PROCESS (she showed up, she
kept going), never on traits, and the hard rules hold: no exclamation marks,
no baby talk, never sad. Ad Astra's dragon is the sibling equivalent — dry and
a shade dark — and the two must not converge.

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

### Parity with Ad Astra: complete as of v23 (2026-08)

The approved v20–v22 backlog is fully ported: graphs (`renderGraph` +
`UNIT_SCHEMA`/prompt support), quiz rounds of 5 with least-practised
selection, Beat-the-clock calibrated to her measured pace, `CHEER_*` pools,
back-stack ← chips, grid-stacked left-aligned flashcards, `eq` formulas in
Fraunces italic, subject-coloured `--ac` on `#screen`, `.btn+.btn` spacing,
visible `APP_VERSION` in Settings, affirmation heart/read toggles, and the
orientation unit retired (schema v4 tombstones `unit-orientation` on
migrate — don't reintroduce boot-generated units). From here, keep the two
engines in step per "Keeping the two apps in step" above.

### The math program (v57)

Accelerated Math runs on the enVision G4 textbook. The material arrives as
scans in the Drive math folder, one subfolder per topic — and **the folder
names are authoritative over the book's printed topic numbers**, because the
course spans two volumes that each restart numbering (the folder called
"Topic 3" may print "Topic 1" inside).

- **Every lesson is one unit**, titled `Topic N · N-L Title` so the topic
  shelves as a book, with **~10 questions and `round:10`** — the quiz is one
  sitting, matching a lesson-a-day pace (Chris, 2026-08). Fewer is fine when
  the material is thin; never pad.
- **Each topic ends with `Topic N · Topic Review`**: a 24-question pool with
  `round:12` and recap cards. Questions are fresh, never copies of lesson
  questions. From Topic 2 onward ~6 review questions **spiral earlier
  topics** — the syllabus says most tests spiral, so the review practises
  deciding which skill a question even wants.
- Lessons are approved as the class reaches them; reviews when test week
  arrives. Everything ships draft as always.
- `unit-m11` (1-1) was retitled onto the shelf **keeping its id**, so the
  progress from before the shelf existed stayed attached. Retitle, never
  re-mint, when moving a unit into a series.
- School rounding rule throughout: 5 rounds up (and Python's banker-rounding
  `round()` disagrees — the builder uses its own `sround()`).

### Content rules (apply here exactly as in Ad Astra)

See "Content rules" in ad-astra/CLAUDE.md — standalone questions (no worksheet
references), bold-answer-first defs with bullets, graphs wherever they teach,
formulas in `eq`, independently verified answers, drafts-only pushes, warm
varied encouragement. Same standards, River-appropriate pitch (a year up from
4th grade, per this file).

### Direction A — the subject owns the colour (v116 / Wayfinder v94, both apps)

Chris, 2026-08: *"The main pages look too monochromatic... It would be nice for
the right things to be the center of attention."* Three directions were built as
real UI in `ad-astra/prototype-focus.html` and he chose **A**.

The diagnosis: one hue was doing every job — important, interactive, active,
decorative — so it signalled none of them. Under A the accent keeps **one** job,
*the thing you can tap*, and anything that belongs to a subject wears that
subject's own hue instead. Three render sites opt in by adding `subj-a` and
setting `--pc` from `classColor()`: the runway card (always — it is about one
subject's test), the week card (only when `wk.focusCid` resolves), and a Coming
up row (only when the item has a `classId`).

Rules that are the point:

- **A subject hue only ever appears where that subject is the topic.** It is
  never decoration. The three strip tiles (Growth / Reading / Level) deliberately
  keep the accent: they are not subject-bound, and colouring them would be
  exactly the "hue everywhere" problem this replaces.
- **`--pc-fg` is the subject colour as TEXT, exactly as `--ac-fg` is for the
  accent, and for the same reason.** The palette's `g1` values are FILLS,
  designed to sit behind white labels on a subject tile. Used as text they
  measured 4.37:1 for orchid in dark and failed on **all twelve** in light,
  worst 1.60:1. `--pc-fg` lifts 10% toward white in dark and deepens to 42%
  over ink in light: worst case **4.90:1** (orchid, dark) and **5.76:1** (lime,
  light) across every palette in both themes.
- **The 3px rules use `--pc-fg`, never raw `--pc`** — the same call `.row.now`
  already made for `--ac-fg`. Raw `--pc` as a rule measured **1.65:1** in light:
  a hue, not a mark. With `--pc-fg`, 5.98:1. The same upgrade was applied to the
  four pre-existing raw-`--pc` rules (`.rw.lead`, `.lk`, `.tile`, `.plan`);
  painted `.subj` tiles are unaffected — they hide their border by design
  because the fill IS the subject colour.
- **`--pc-fg` must be DECLARED on every element that can carry its own `--pc`.**
  An unregistered custom property resolves its `var()` references on the element
  where it is declared, so a week-card row that overrides `--pc` still inherits
  the CARD's already-computed `--pc-fg` — the lead rows wore the focus subject's
  colour no matter whose door they were. The declaration selector list therefore
  names `.rw.lead`, `.lk`, `.tile` and `.plan` alongside the `subj-a` classes.
- **The week card's doors are not all one subject.** A lesson door can point at
  another class, so the row rule lives on `.rw.lead` (which carries its own
  `--pc`), and the card-wide `.rw` rule is scoped to the runway — whose rows
  really are all the card's subject.
- **`.row.now` still wins over `.row.subj-a`** (later in the sheet, equal
  specificity), and that is correct: accent means "this lands today", subject
  hue means "this subject". Today is a different axis from topic.

Two cascade traps, both real, both caught by rendering rather than reading:

> ⚠️ **`.card.ac` sets the same `background-image` at equal specificity and
> later in the sheet.** The subject gradient written with the other `subj-a`
> rules was silently replaced by the accent one — the eyebrow and rules went
> subject-coloured while the card itself stayed accent. The wash therefore
> lives *after* `.card.ac` and is written `.card.subj-a,.card.ac.subj-a`.

> ⚠️ **That rule must NOT set `background-color`.** `.card.ac.week` and
> `.card.ac.daycard` carry the glass mix that lets the comet through, at the
> same specificity and earlier in the sheet — setting it would quietly make the
> two top cards opaque again.

**Directions B (depth, not hue) and C (one loud thing) were not chosen.**
`prototype-focus.html` stays as the reference; it is a dev artifact, not cached
by the service worker and not linked from the app.

