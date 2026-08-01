# Claude Guide — Wayfinder

River's learning PWA. **4th grade, BASIS Chandler Primary South, SY 2026–27.**

Same engine as [Ad Astra](../ad-astra) (Sedona's app) — record store, Gist sync,
study plan, tutor, focus timer, emotion checks, parent view all work identically.
**Read `../ad-astra/CLAUDE.md` first**; everything there applies unless listed
below. This file documents only what differs.

---

## Pitch it a year or two up

Both girls attend a school that teaches roughly a year ahead, and they read and
behave accordingly. River is 9 but the material and the tone should land like
**middle school**, not lower primary. Sedona's app is pitched at high school for
the same reason.

Concretely, for River: short sentences and ordinary words, but **never** baby
talk, never exclamation marks, never "great job!" — she gets a real explanation
said plainly. The model prompts for the tutor and unit generation both say this
explicitly; keep that if you edit them.

---

## The schedule rotates — this is the main structural difference

Sedona's timetable is identical every weekday, so hers is a flat `CLASSES` array.
River's rotates, so hers is:

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

Her `.ics` has **no teacher names** (Sedona's did), so nothing in the UI shows a
teacher. The orientation unit drills rooms *and the rotation* instead, since
knowing that Art is Tue & Fri is the genuinely useful week-one fact.

---

## Calendar

BASIS Chandler Primary South publishes its own calendar. Same first/last day
(2026-08-03 → 2027-05-21), same quarters and the same closure dates as the upper
school, but: **parent/teacher conferences** on 10/2 and 3/12 instead of comp
exams, and **Project Week is 5/17–5/20** (Sedona's runs to 5/21). There are no
Pre-Comp or Comp exams in primary — don't copy those milestones across.

---

## Identity

Deliberately not a re-skin of Ad Astra — the girls should not feel like they got
the same app.

- Base is **indigo-slate**, not teal-black. Default accent is **amber**; her
  picker is Amber / Sunset / Sky / Mint / Lilac / Rose.
- Avatars lean adventure rather than celestial (🧭 🦊 🐉 🚀 …).
- Subject textures: graph paper (Math), ruled paper (English), tighter rules
  (Writing), cell dots (Science), columns (History), blueprint grid
  (Engineering), pixel grid (Computers), paint spatter (Art), curtain (Theatre).

Storage namespace is `wayfinder_` and the Gist file is `wayfinder-data.json`, so
the two apps never collide even on a shared device or a shared Gist token.

---

## Drive

Class material lands in her folder `1Qtab_VqloYC7w1HdQRcri3hzdl1kzq0c`
("River" → BASIS Chandler Primary). Backups go to **Wayfinder Backups**,
`14BImMb-1W-3vNw54Kyc_OC31nOPjINrt`, linked from the parent settings.

---

## Keeping the two apps in step

The engine is duplicated, not shared — deliberately, to keep both single-file and
buildless. When you fix an engine bug (sync, streaks, timer, quiz), **check
whether the other app has it too**. Content, schedule, calendar, palette and copy
are meant to diverge; the engine is not.
