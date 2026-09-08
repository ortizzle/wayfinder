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

### The batch of four (v118 / Wayfinder v96, both apps)

Four small improvements from the v117 review's idea list, shipped together.

**The resume door on Today.** A round parked earlier today renders as a hero
card — "Pick your round back up · <unit> · N of M answered" — straight back
into the quiz. Rules that are the point:

- **It outranks every suggestion, and the generic hero yields to it** (`pkLive`
  joins the dupe conditions): a half-finished round is not advice, it is her
  own work made findable.
- **Same validity rules as `loadRound`, WITHOUT consuming the save** — today
  only, a real approved unit, matching question fingerprint. The quiz screen
  still owns the actual pickup.
- **The save fires before Next advances**, so an answered question still sits
  at `pk.i` — the door's "questions left" check steps past it the way the
  quiz's own resume does, or it shows for a finished round and tapping it
  starts a fresh one (caught live: "3 of 3 answered" with nothing to resume).
- `saveRound` now stores `classId` (it lived only in nav ctx), so the door can
  route without guessing at `__all__` units.

**The star sky gate is content-shaped, and Latin joined it.** The old gate was
`/wordly wise/i` on the title; now it also needs **≥6 single-word cards**
(`skyCards` filters multi-word terms — 'First declension' or 'C — vacca' are
cards, not words you can say into a microphone), and Latin units qualify.
Measured on the real shelf: Unit 1's eight case names get the game; the
Pronunciation & Greetings unit (3 single-word cards after filtering) rightly
does not. Deliberately NOT opened to science units with single-word terms —
the allowlist stays vocabulary. Belt and braces: the clue line is now run
through `skyBlank` too, so a future def that uses its own word cannot hand
the answer over.

**A right answer buzzes back** — `[12, 40, 12]`, the star sky's win pattern
scaled down. **A miss deliberately gets nothing: the phone never scolds.**

**Growth Zone group headers wear their subject's rule** (`.subjline`,
direction A carried to the screen where she acts on it). Same grammar as a
Coming up row: this colour = this subject, wherever she meets it.

### The Spelling Bee (v99, THIS APP ONLY)

Chris added the real 2026-27 Scripps "Two Bee" fourth-grade study list (50
words) to River's Drive folder and asked for bee-shaped flashcards plus a
voice game where she spells each word aloud, letter by letter, after hearing
it read to her. Built for River specifically — not ported to Ad Astra, the
same bar the companion was held to ("the agreed bar for porting it was her
asking"). All 50 official words, split into four lessons of ~12-13
(`unit-bee1..4`, `content/spelling-bee-1..4.json`), classId `english`,
shelving as one book via the ` · ` title convention. Every definition and
example sentence was written fresh and verified independently — the source
is a bare word list with no definitions to copy, so nothing in `def`/`ex`
carries `from:'source'`; only the word itself is sourced.

**The flashcards are honeycomb-shaped, not bee-shaped, on purpose.** A
literal bee silhouette would clip text off the card; the shape reads instead
as a honeycomb cell — an octagon (`clip-path`) with generous flat top/bottom
edges, so the reading area never nears a clipped corner. Colours are FIXED,
not theme tokens, gated on a new content flag `u.bee` (never inferred, same
rule as `book`/`guide`/`capstone`): like the note-from-home post-it, this
card is meant to feel like a physical object, not UI chrome, so it looks
identical in light and dark. Measured directly: ink on the honey gradient's
darker stop is 10.0:1 worst case, both faces, both themes.

> ⚠️ **`.face.back:not(.subj)` already sets its own background at (0,3,0)
> specificity — higher than a bare `.face.bee` at (0,2,0).** The back face
> silently kept the dark accent gradient instead of the honey card until the
> selector became `.face.bee,.face.back.bee`, tying at (0,3,0) and winning on
> source order. Caught by flipping the card, not by reading the CSS — the
> exact trap the pattern-layer comment two rules above already warns about.

**The Bee Round is a voice game, built to mirror an actual bee.** The word is
*announced* (`say()`), never shown as text, until she has spelled it or given
up — showing it first would make this copying, not spelling. She may ask to
hear it again, hear its meaning, or hear it used in a sentence (reusing
`skyDefLine`/`skyExamples` from Star Sky) — exactly what a contestant may ask
a real pronouncer. Then she taps "Spell it" and says the word letter by
letter; a row of boxes (`.beeword`/`.beebox`) fills in left to right as each
letter is confirmed, and a mismatch never erases letters already heard
correctly.

- **Letter NAMES are a harder recognition problem than whole words** —
  B/D/E/G/P/T/V/Z are famously confusable even to a human ear, which is why
  the NATO alphabet exists. `BEE_LETTERS` maps the common spoken/misheard
  forms of each letter name (`"bee"`→B, `"you"`→U, `"double u"`→W, …) and is
  deliberately conservative: an unmapped or unmatched sound is skipped, never
  guessed. `continuous:true, interimResults:true` lets the session survive
  the natural pause between letters (a single non-continuous recognition
  would likely cut off after the first one or two).
- **Typing is offered from the very first render of every word, not earned
  by failing first.** This is a deliberate departure from Star Sky, which
  hides its typed fallback behind a failed whole-word attempt: here the
  fallback produces the *identical* outcome (a spelled word), so there is no
  reason to make her earn the escape hatch, and it doubles as the only way to
  cancel a stuck listening session (`beeState._rec.stop()`).
- **Two stalled letters in one attempt auto-hands off to typing** — mirrors
  Star Sky's `tried >= 2` rule, but checked inline where the mismatch is
  detected (not deferred to `onend`), since `continuous:true` means the
  session might otherwise keep listening indefinitely while she is already
  trying to type.
- **A 22-second safety timeout stops the recognizer.** `continuous:true`
  never auto-stops on a pause — that is the point — but it also never
  auto-stops on its own, so an abandoned session would otherwise listen
  forever.
- **"Skip for now" always lights `'dim'`, never blocks.** Same Sky Map rule
  as everywhere else: showing up counts, a hard word is information not a
  fault, and the round always has an end.
- No new record types. One ordinary `log` (`mode:'bee'`) per session,
  written on leaving or finishing, same shape as Star Sky's `mode:'starsky'`.
  The finish screen reuses `roundBand`'s `opt.state` + the quiz results
  `.tally` chip pattern, rather than pulling in `showModal()`'s mood/
  companion machinery, which doesn't apply to a casual practice mode.
- Beat the clock is dropped for `u.bee` units for the same reason as `u.book`
  units: `pickRound` already excludes `kind:'spell'` from timed rounds
  (typing against a countdown tests typing, not spelling), so the tile would
  serve an empty round.

**Verified end-to-end with a mocked `SpeechRecognition`**, since no real mic
is available in a headless harness: all 50 words round-trip correctly through
canonical letter names including the two-word "double u"; progress survives
an interleaved unmapped/noise chunk without resetting; two stalled attempts
correctly hand off to typing and stop the recognizer; two wrong typed
attempts correctly trigger the reveal (reusing `.skyreveal`/`.a` from the
star-sky-reveal fix); and the real browser's own mic-blocked error path fired
organically in this sandbox and degraded exactly as designed.

`unit_common.py`'s local validator never special-cased `kind:'spell'`
(opts:[word], one option) — every spell question would have failed the
builder's own asserts before reaching `check_content.py`, which already
skips them correctly. Fixed alongside the new `bee_` build flag.

**The mic that keeps listening (v100).** River reported it live: "I can only
spell about 3 letters before it resets on me." The cause was `continuous:true`
— Android Chrome's `SpeechRecognition` does not reliably honor it; the
platform's underlying speech service ends the session after a single
utterance regardless of the flag, and there was no code path bringing the mic
back without her re-tapping "Spell it" by hand. Fixed by not fighting the
platform: the Bee Round now uses `continuous:false, interimResults:false` —
the exact well-supported single-utterance mode Star Sky already uses
successfully on her phone — and supplies "keep listening" itself. `onend`
silently starts a fresh session unless the word is finished, she has
cancelled, a fatal error occurred, or the budget (50s / 30 restarts) is
spent; from her side the mic never stops. `stillLive()` guards every callback
against a stray restart firing after she has left the screen.

Verified with a fake recognizer that ends its own session after every single
final result — deliberately reproducing the Android behaviour rather than the
"one long session" shape the original code assumed: spelling "cuddle" letter
by letter now creates six auto-restarted sessions, one per letter, with
`beeState.listening` staying true throughout and the word completing
normally. The two escape hatches were re-verified under the new restart
loop too: two stalled single-utterance attempts still hand off to typing
(unchanged), and tapping "Type it instead" mid-chain stops it for good — no
restart sneaks in afterward, confirmed by checking the session count is
unchanged even after a delay.

**A moment to see it spelled (v101).** River again, same session: "I can't
see how the correct word is spelled after the correct spelling. It goes
straight to celebration and next word." `lightIt()` used to advance `i` and
reset the word's state in the same call that marked it correct, so the win
was only ever visible as a flash inside `celebrate()` — never as text she
could actually read. It now holds the round open on a `beeState.won` panel
(mirrors Star Sky's `skywon` card exactly: green eyebrow, the word itself in
`.skyword`, the `sp` respelling, a "Hear it" replay) until she taps "Next
word →" — or "See how it went" on the last one. `resetWord()` clears `won`
alongside everything else, so the next word always opens fresh. Verified
live: the confirmation panel shows the correct word and phonetic spelling
immediately after a correct attempt, "Next word" advances and resets state
correctly, and the last word's button correctly reads "See how it went" and
reaches the finish screen with the right tally.

### Wordly Wise Lesson 1 · Synonyms & Antonyms (v102)

A second unit for the same 15 Lesson 1 words, built from "Lesson 1 synonyms
and antonyms.pdf" — the class's own study sheet, which says outright "The
UNIT TEST will include synonyms and antonyms from this list!" `unit-ww501`
already tests definitions, part of speech and usage; this tests the one fact
it doesn't cover. Shelves as "Wordly Wise · Lesson 1 Synonyms & Antonyms",
right after "Lesson 1" — pure title sort, no `order` field (see the trap
below).

**The source is an OCR-flattened 3-column table, and two words came out with
no antonym at all.** Re-extracted twice, identical result both times, so
this reads as the sheet genuinely leaving `jostle` and `pedestrian` blank
rather than a misread — nothing is invented for the gap, only their
synonyms are tested. `patient` carries synonyms for BOTH of its senses
(tolerant/composed as an adjective; victim/sufferer as the noun for a
person under a doctor's care) with an antonym given only for the adjective
sense, so that is the only one tested. Flagged in `parentNote` rather than
silently smoothed over.

**Direct MC, not `kind:'analogy'`, on purpose.** The engine already supports
analogy questions and CLAUDE.md documents them as built "at Chris's request
for Wordly Wise" — but a clean analogy question needs wrong options that
each hold a genuinely different, nameable relationship, and none of the
OTHER antonym pairs on this same sheet can be used as a distractor without
creating a second valid answer (Concept:Fact is itself a real antonym pair
from three rows down the same table). Getting that wrong once already cost
a shipped Ad Astra item a rewrite. Direct "which word means the
opposite/same as X" questions map 1:1 onto what the sheet and the unit test
actually ask, with no such ambiguity risk — the safer choice for content
that feeds a real grade.

> ⚠️ **`order` is a WHOLE-SHELF sort key, not a per-lesson one.** Every
> lesson in a series defaults to `order:0` and sorts among the others by
> title; giving one supplementary unit `order:1` (mirroring Ad Astra's
> `Topic N · Test N Study Guide` convention) does not slot it in after the
> ONE lesson it responds to — it buckets it after every order-0 lesson in
> the whole series. Built this way first, it landed at position 6, after
> Lesson 5, not position 2. Ad Astra's convention works there because the
> Study Guide is meant to trail the WHOLE topic; here the sheet answers to
> one lesson specifically. Fixed by dropping `order` entirely: titled
> "Lesson 1 Synonyms & Antonyms" with no order field, plain numeric-aware
> title sort already lands it exactly right — verified directly,
> `['Lesson 1', 'Lesson 1 Synonyms & Antonyms', 'Lesson 2', 'Lesson 3', …]`.

`check_content.py` flagged one real length-bias outlier (88% longer, the
`patient` antonym option) before the fix and three minor ones (12–25%,
within the library's existing accepted range) after — fixed by shortening
"complains a lot" to "complains" against its distractors. Answer positions
balance 5/5/5/4 across the 19 questions.

### Your week — the brief (v104 / Ad Astra v121, both apps)

Chris asked for "a brief section to highlight more about the week and
expectations for how the girls can spend their day and align for the week
ahead," prototyped three ways in `prototype-brief.html`. He chose **C (prose
+ ledger) with B's load bars**, and — the second half of the call — retiring
the week-ahead card: *"we can probably move the week ahead since that
information will be in Your week anyway."*

`weekAhead()` is gone; `weekBrief(date)` replaces it, and the five-cell day
strip with it. The brief is: two written sentences, a load bar per subject, a
ledger of the week day by day, and the "where to actually study" block.

**The ordering in that last block is the point, and it is Chris's:** CJ
first, then Schoology / class notes / worksheets / study guides, and only
then this app. It is the app saying out loud that it is not the source. That
copy is FIXED and must stay fixed — the app cannot know whether her CJ is up
to date, and a checkbox that pretended to track it would be surveillance of
the one habit she is meant to own herself.

- **One evening's work per subject, never the whole pile.** A load is the
  review that is due plus the ONE next lesson — the same "name one lesson,
  never a pile" rule the runway established. `q` counts *unattempted*
  questions, so a half-finished lesson reports what is left, not its size.
- **Minutes come from her real pace.** `quizLimit()` already measured
  seconds-per-question; `cardLimit()` is its flashcard twin. Card logs never
  stored a count (`total:0`), but `xp` is `min(seen*5,150)`, so `seen` is
  recoverable exactly while the cap is unhit — logs *at* the cap are skipped
  rather than guessed at. Both clamp so one strange session cannot make an
  estimate absurd.
- **Bars are scaled against the biggest subject**, not each against its own
  total — self-scaled bars would make every subject look equally heavy, which
  is the one thing the bar is there to disprove. The legend earns its place
  because "mostly review" is readable off the bar and nowhere else.
- **The last free day before a multi-test day goes to mixed practice** — the
  exam-ramp rule, already documented: in test week the right work changes
  *shape*, not just minutes.
- **Test days ask for nothing new.** A plan that scheduled cramming on the
  morning of the test would be the app working against her.
- **The three yield rules survived the swap** and now read off the brief:
  `wk.namesDue` replaces the old `lines.some(kind==='due')` for the Growth
  tile, `wk.namedCids` replaces the `lines` scan for the hero, and `covers()`
  still hides the runway when its test is inside the week. Verified live: the
  due count appears exactly once on the screen.

**The prose is the risky half of this design and got tested hardest.** Seven
week shapes were exercised before shipping — no tests, one test, three on one
day, two spread across days, a test today, opened Thursday with one evening
left, and opened on the test day itself. Four real bugs came out of that pass
and are worth remembering, because every one of them is the kind of thing
that makes generated writing sound generated:

> ⚠️ **"a English quiz"** — the article has to be chosen from the *assembled*
> phrase, since the subject short-name leads it, not from the kind word.
>
> ⚠️ **"one evening, and roughly 9 minutes each"** — "each" needs a plural to
> attach to.
>
> ⚠️ **"roughly 5 minutes each" under a ledger reading 7, 9, 7, 7, 9.** The
> average was taken over the subject list, but the ledger cycles subjects when
> the week is longer than the queue. Average the DAYS AS PLANNED.
>
> ⚠️ **"That gives you 4 evenings"** printed under a test that was *today*.
> That sentence promises preparation time; it is only true while a test is
> still ahead. With the week's tests already sat it becomes "the rest of the
> week is yours."
>
> ⚠️ **"a Theatre test and an Alg/Geo quiz, all on the same day"** — "both"
> for two, "all" for three or more. Caught on Ad Astra, whose seeded week had
> exactly two.

> ⚠️ **"The studying days are behind you now — the work is done."** Chris
> caught both halves overreaching: "the work is done" is a claim the app
> cannot verify, and studying time always exists — the plan running out must
> never read as the door closing. Now: before a test still ahead, "No study
> evenings left before it — nothing new now. A flip through the cards on the
> way in is plenty." After the week's last test, "Studying never closes,
> though — your shelves and the Growth Zone are open whenever you want a
> round." The rule this adds to the prose list: the brief may say what is
> scheduled, never what is finished — completion is hers to declare, not
> the app's.

Also fixed on the way: `.ledger-row.now` used a negative margin to bleed its
tint to the card edge, which gave the whole page a horizontal scroll — the
row is padded on both sides instead, and the bottom border still spans the
full width because padding sits inside the border box. And the comet-glass
rule (`.card.ac.daycard, .card.ac.week`) was left pointing at a class nothing
carries any more; it names `.card.ac.brief` now, so the two top cards still
let the sky through. ~2.5KB of dead week-card CSS removed with it.

Contrast measured across all 26 new reading tokens, both themes, composited
over the *glass* card rather than an opaque one: worst case 5.01:1.

**The strip goes too (v105 / Ad Astra v122).** Chris circled the three-tile
strip and asked for it to go, and the brief is why every tile had stopped
earning its place: tile one printed "40m suggested · Math" directly under the
brief's own "Tonight: Accelerated Math" button, and its Growth variant was
already yielding to the brief's review counts. Reading has a whole card on
Study. Level went to Stars — a nav tab — and a level with nowhere new to go is
scorekeeping, which the strip's own founding rule (v51) named as
disqualifying: *"if a tile is ever added that only displays a number, it
belongs on Stars instead."* Checked before removing rather than after: Growth
keeps its live count badge in the nav, the reading log keeps its Study card,
and Stars is one tap away in the nav either way — so nothing became
unreachable. `countedDue` and `mRead` died with it; `dueNow2` and `plan2`
stay, because the hero's duplicate-check still reads them.

**Tonight belongs to tomorrow (v106 / Ad Astra v123).** Five items from
Chris's session with the girls, all on the brief and the results modal.

- **After 3pm the brief promotes the NEXT day.** 900 minutes is the same
  after-school line the rest of the app draws. Three things follow: a test
  sat this morning drops out of the prose ("The week's tests are behind you"
  when nothing is left), a test-day evening turns back into a study row for
  the next test instead of showing the test that already happened, and the
  queue sorts soonest-test-first before weight/neediness — a quiz tomorrow
  wins tonight over a bigger test on Friday, because tonight's slot belongs
  to whatever she meets next.
- **The minutes are that evening's practice at her measured pace** — Chris
  asked what they meant, which meant they didn't say. They wear `~` now and
  the footnote says it outright.
- **The load-bar rows are doors** (buttons to the subject, `›` affordance) —
  the same stats-as-navigation rule the strip lived by; Chris caught them
  inert on River's phone. And the CTA **falls forward**: when today's row
  isn't pressable (closed day, test morning), the button offers the first
  workable day as "Get ahead: X" instead of vanishing. It still disappears
  when the whole week genuinely asks nothing — a CTA with nothing behind it
  would be a nag.
- **The results modal shows the percentage again** — River reported the
  science quizzes "did not provide grades", including Beat the clock. Both
  were tested live and NOT broken: the v91 tally said "4 of 5", which is the
  grade — but not in the language school has taught her grades come in. This
  amends v91's "the percentage is not printed at all": it is now one chip
  ("80%") in the tally, said once; the completion-first headline is
  unchanged.

> ⚠️ **`.card p` beats a bare `.brief-prose` on specificity** — the prose had
> been rendering at `.card p`'s 14px muted style since the day it shipped;
> the styled 17px never applied. This is why Chris asked for a bigger font.
> Now `.card p.brief-prose` (the `.card.pnote p` precedent) at 18.5px,
> full-text colour, verified 18.5px computed in BOTH apps. The lesson
> repeats: measure the computed style, not the stylesheet.

**Said once, and quieter by Tuesday (v108 / Ad Astra v125).** The measured
review of Today after the brief landed — six changes, all approved together.

- **"Where to actually study" folds after Monday.** It was 361px of the
  1,005px brief and identical every day — banner blindness in the making. Full
  on Sunday and Monday when the week gets planned; one tappable line
  ("CJ first → Schoology, notes, study guides → then here ›") the rest of the
  week, expanding via `ctx._studyPath`. Nothing removed, only deferred — the
  Settings-pickers move. Folded, the brief drops to ~650px.
- **Coming up skips tests the ledger already lists.** `weekBrief` returns
  `ledgerTestIds`; `upcomingAssessments` filters against it. The ledger says
  this week day by day; Coming up keeps what it cannot — events, and anything
  beyond Friday. The last same-fact-twice on the tab.
- **The after-school day card names tomorrow's first class** instead of
  repeating a study nudge that is now the brief's whole job. "Tomorrow starts
  with Accelerated Math at 7:40 AM" — on the rotating timetable that is
  genuinely news daily. Falls to the weekday name across weekends and breaks;
  says "Nothing on the timetable ahead" past the last day.
- **Ledger study rows wear their subject** (`.ledger-row.subj`, added to BOTH
  `--pc-fg` declaration lists — the resolve-where-declared trap). Today's row
  keeps the accent: `.now` sits later in the block, and today is a different
  axis from topic. Verified: a plain WED science row computes the lifted
  green, today stays accent.
- **The load bars dropped their minutes** — the same number printed twice
  inside one card (bar and ledger row). The bar's job is composition; the
  ledger says when, and keeps the `~min`.
- **The generic thread hero is retired.** Once the brief named up to four
  subjects, the dupe rules meant it almost never fired. The parked-round
  resume door stays; Study keeps its own Pick-up-the-thread; the `#thread`
  shortcut still resolves through `threadTarget()`. `dueNow2`/`plan2` died
  with it.

### Cards of her own (v110 / Ad Astra v127, both apps)

Chris asked for a way for each girl to make her own flashcards per subject.
One deck per subject (`unit-own-<classId>`, deterministic id so two devices
can never mint duplicates), created lazily on her first card, edited in
`SCREENS.owncards` (add / edit / delete with a real confirm), reviewed
through the ordinary flashcard player. The subject screen shows a "Your own
cards" card once the deck has cards, and a quiet "Make your own flashcards"
tool button until then.

Rules that are the point:

- **Her own words skip the review queue.** The draft gate exists to catch
  what the MODEL got wrong before it reaches her; these are her words, like
  the weekly aim, the motto and the teach-backs — gating them behind a
  grown-up would turn making flashcards into being checked on. The deck is
  born `status:'approved'`.
- **Making a card earns nothing.** Writing a card IS studying — deciding
  what matters and saying it in your own words is generation practice, the
  strongest encoding there is — and pricing it would cheapen it, the same
  rule teach-backs follow. REVIEWING the deck earns ordinary flashcard XP.
- **`own:true` keeps the deck out of every door that needs questions** —
  quiz, clock, shuffle, star sky, the brief, threadTarget — all of which
  already guard on `questions.length`, verified one by one. The one
  render-site trap: the deck has no ` · ` in its title so `shelvesFor` puts
  it in the LOOSE list, where `unitCard` would offer a quiz it cannot hold —
  the loose render now filters `!u.own`, and the deck's own card is the only
  door.
- **`finishCards` forks on `questions.length`:** a normal deck still offers
  "Take the quiz"; hers says "You wrote these and now you have studied them —
  that is the whole loop" with no quiz to dangle.
- It is a real unit record, so sync, the day view ("Flashcards · My Science
  cards") and minutes all work for free. Content, not progress: Fresh start
  leaves her deck alone.

**Filed in the back of the book (v111 / Ad Astra v128).** Chris asked whether
her deck could join an existing book. It can now: the editor offers "Keep
these cards — on their own / in <book>", writing `series` on the deck, which
`seriesOf()` already honours over the title convention, so nothing is
renamed. Filing can also be changed without adding a card.

**A deck can BELONG to a book without being COUNTED as one.** That is the
whole design, and it is what stops five things breaking:

- `unitDone()` needs questions, so her deck can never be done. Counted as a
  lesson it would freeze any book she filed cards in at N-1 forever and
  silently cost the gilt spine. `shelvesFor` now returns `lessons`
  (`units.filter(!own)`) and the spine, the shelf header and the gilt test
  all read that instead of `units`. **Verified by stamping full coverage on
  a book with her deck filed in: still goes 6/6 and gilt.**
- The bookmark is drawn from `lessons` only — it answers "where was I
  reading", and a deck of flashcards is never the answer.
- Her deck sorts to the BACK of the book regardless of title (`a.own` leads
  the comparator) — it is not lesson N, it is her notes tucked in behind
  them.
- `topicMap` gives it its own stop: ✍️ mark, "Your cards", the card count,
  no coverage bar, and it does not consume a lesson number (the numbering
  counter skips it).
- `SCREENS.shelf` opens her stop with `ownCardsCard()` rather than
  `unitCard()` — the same offer-a-quiz-it-cannot-hold trap the loose list
  already hit.

The subject screen shows the deck loosely **only while it is unfiled**; once
it lives in a book, the book is where it lives. The editor door stays on the
subject screen either way, so a filed deck is never stranded.

### Science Quiz 1 Part 3: Variables (v112)

Chris uploaded a new Quiz 1 handout to River's folder — "Variables (Check for
Understanding)," 10 points, covering independent/dependent/control variables
and what makes a test fair. `content/science-variables.json` (`unit-sci-vars`)
shelves as "Science · Quiz 1 Part 3: Variables," `order:2`, right after the
existing Part 1 (Thinking Like a Scientist) and Part 2 (Measurement). 16
fresh questions across 8 cards — every scenario is new (a baker's yeast, a
runner's shoe brand, a dog's water bowl…), none reuse the sheet's own
snake-venom, magnet, hot-air-balloon, ice-cube, salmon or tree examples, so
she can't answer from memory of the worksheet. Two "choose the pair that
both belong" control-variable questions mirror the sheet's own "select 2"
items in a format the engine's single-answer MC actually supports — the
correct pair is the ONE option combining two genuine control variables,
with the other three options each smuggling in the independent or dependent
variable as a decoy.

### Flag this question (v136 / Ad Astra v136, both apps)

Chris asked for a way for the girls to flag a question they think might be
wrong, so he can remove it from the material or explain it to them. Every
answered question (right or wrong, in an ordinary round, a Growth Zone
review, or a shuffle round) gets a quiet "🚩 Something wrong with this
question?" ghost button under its explanation. Tapping it opens a modal with
an optional textarea — say what seems off, or just flag it — and writes one
`flag` record (`{unitId, classId, qid, q, note, date}`). The button then
relabels itself "🚩 Flagged for a grown-up" and disables, so she can't
double-flag the same question, and gets no other feedback: no XP, no
Growth Zone entry, nothing gamified.

- **This is not the Growth Zone.** The Growth Zone is about what SHE knows;
  a flag is about whether the QUESTION ITSELF is right — a typo'd answer key,
  a confusing scenario, a graph that doesn't match its own text. The two
  systems don't touch: flagging changes nothing about her tally, her ladder,
  or her XP.
- **Nothing happens automatically.** A flag only ever surfaces to a
  grown-up; it never edits, hides, or skips the question by itself. The
  parent view gets an accent card ("N questions were flagged") in the
  Topics section, leading to `SCREENS.flagged` — subject-grouped, the
  question, her optional note in quotes, and two actions: **Remove the
  question** (filters it out of the live unit's `questions[]` for good, and
  tombstones any existing `miss` record for that unit/qid too, so a question
  pulled for being wrong can't keep resurfacing in the Growth Zone from an
  old snapshotted miss) or **Dismiss — it checked out** (softDeletes the
  flag, question untouched, for when it turns out fine on a second look).
- **`_srcUnit`/`_srcClass`/`_srcQid` are used exactly like the "not sure it
  will stick" 🌱 button already does**, so a flag raised mid-review-round or
  mid-shuffle-round correctly attributes to the real unit and question, not
  a synthetic round id.
- **Excluded on a rescue-round variant** (`q._rescue`) — a variant is a
  sub-field of another question, not a top-level array entry, so there's no
  clean "remove this" target.
- **Not in `PROGRESS_TYPES`.** A flag is a content-correctness signal, not
  her activity — Fresh start leaves it alone, same as units, assessments,
  prefs and roster.
- `tools/test_flag.js` covers the whole loop both ways: flagging a right
  answer and a wrong one, the note saving, the no-double-flag guard, the
  parent card appearing, removing (unit shrinks by exactly one question, the
  matching miss is tombstoned, the flag clears) and dismissing (flag clears,
  question and unit untouched). This is engine, ported to both apps in step.

### Grades, tabulated by subject (v113 / Ad Astra v135, both apps)

Shipped Ad Astra-only at first, then ported here once Chris pointed out the
gap — grades-by-subject is engine, not identity, and had no reason to stay
one-sided. Same everything as documented in ad-astra/CLAUDE.md:
`gradesBySubject(date)` derives per-subject averages from `assess` records
at render time (nothing stored), scoped to the current quarter, with a "By
subject" card at the top of Tests & quizzes. Every `STUDY_CLASSES` subject
renders even at zero — "No grades entered yet" stays visible rather than the
subject silently dropping off the list, which was the entire point of the
feature. `tools/test_gradesbysubj.js` is the same test file, unchanged.

### Extra reps before the tests (v117)

Two new prep-flagged units from Chris's fresh Drive uploads, plus the
week-of-8/28 newsletter's tests added to `SUGGESTED_ASSESS` (Plot Diagram
Quiz 9/2, Cursive Quiz 9/2, Nature of Science Test 9/3, Unit 1 math test
9/10).

- **`math-t3-extra.json`** (`unit-m3x`) — "Topic 3 · Decimals Extra
  Practice", from the "extra practice" sheets in the Topic 3 Drive folder:
  expanded form WITH FRACTIONS (the class's convention — 2 × (1/10), not
  exponents), word form to numerals, and place-value vs. digit-value
  tables. All numbers fresh; the two classic traps (interior zeros in
  expanded form, the digit value of 0) each get a dedicated card and
  question. No `order` field — "Decimals Extra Practice" title-sorts
  between 3-7 and Topic Review, verified. The class calls this unit
  "unit 1" (test 9/10) but the folder says Topic 3 — folder names are
  authoritative, per the math-program rule, and the shelf's own 3-1..3-7
  lessons confirm the content matches.
- **`science-scales.json`** (`unit-sci-scales`) — "Science · Reading Scales
  Practice" (`order:3`, after Variables), from the measuring-practice
  sheets + answer key. **Honest-scope call:** the sheets' pictures (where
  a bar ends, where a meniscus sits) can't be reproduced without inventing
  them, so the unit drills the REASONING every reading depends on — the
  what-is-each-line-worth step (gap ÷ spaces), cm↔mm conversion, meniscus,
  between-the-marks readings, below-zero thermometers — and the parentNote
  says outright that the paper sheets stay the eye-practice half. The
  answer key was checked against the sheet; clean.
- Both ship `prep:true`, so they wear the new gold treatment. The checker
  caught three real standalone violations in the scales unit's first draft
  ("That same cylinder…" stems) — rewritten to restate their facts inline;
  the back-reference rule bites even when you know it's there.
- `tools/test_extraprep.js` covers shelving positions, the gold stops and
  band, and a full quiz round on each.

### Test prep, in gold (v116 / Ad Astra v139, both apps)

The test-prep standout treatment, ported in step: a unit flagged
`prep:true` — or any `guide:true` unit — wears the opaque gold
"✍️ TEST PREP" band and gold card edge, and a gold pip ring on the topic
map. See ad-astra/CLAUDE.md's section of the same name for the full rules
(explicit flag, never inferred; the measured gold pair; done outranks
prep). This app ships the engine with no prep-flagged content yet — the
first study guide River's classes issue picks it up by adding `prep:true`
(or `guide:true`) to the unit.

### Fewer, clearer gridlines (v145, engine also in Ad Astra)

Chris, immediately after v144 shipped: "better but the longitude lines are
hard to read." Real, and measured before touching anything: the map's 12
longitude ticks (5° apart across the 60°-wide window) sit only ~21px apart
in `renderGraph()`'s 300-unit-wide SVG, and each label like "125°W" renders
~29px wide — every adjacent pair was overlapping by several pixels, not
just crowded.

**`renderGraph()` gained optional `g.lx`/`g.ly`** — a label step, in the
same units as `gx`/`gy`, that must be a whole multiple of it. The grid
itself is unchanged: every gridline at the `gx`/`gy` spacing still draws.
Only which lines get a printed NUMBER changes — `g.lx:10` on this map's
`gx:5` grid labels every other line, halving the tick count from 12 to 6
and roughly doubling the space each label gets. Every existing graph spec
in both apps omits `lx`/`ly`, so `lx` defaults to `gx` (label every line,
exactly as before) — zero behavior change anywhere else. Carried into Ad
Astra's copy too, unused there for now, keeping the shared block identical.

- **Thinning labels, not gridlines, was the deliberate choice.** The fine
  5° grid is what makes the map genuinely usable for estimating a position
  between labeled lines (the whole point of the "estimating between
  gridlines" card) — coarsening the grid itself to 10° would have fixed the
  crowding by removing exactly the precision the unit is built to teach.
- Only the LONGITUDE axis needed thinning on this map — the 6 latitude
  ticks were never crowded (confirmed by measuring, not assumed), so `g.ly`
  is left unset and latitude labels every line as before.

`tools/test_az_latlong.js`'s existing label-overlap check (built for the
city-label collision two versions ago) now checks EVERY text element on
every graph in the unit, not just the bold city labels — so this same
measurement would have caught the axis-crowding bug too, and catches it as
a permanent regression check going forward.

### The map, on tap (v146 / Ad Astra v164, engine in both apps)

Chris, right after the readability fix: "can we make the actual map, a
tool to reference when questions are asked?" Every lat/long question
already carries its own narrow `graph` (four cities at a time), but there
was no way to pull up the fuller picture mid-question the way Calculator
and Sheet already let a math or science quiz reach a tool without leaving
the question.

**A unit may now carry `mapRef`** — an ordinary graph spec, opened via
`openMapRef(u)` exactly like `openSheet()` opens a `SHEETS` entry: a plain
modal, `graphNode(u.mapRef)` inside it, an optional `mapTitle` and
`mapNote`. Two doors open the same graph:

- **A door on the unit's own card** (`unitCard()`, next to the Sort doors),
  labelled with `u.mapLabel` or a generic fallback — reachable any time she
  is looking at the lesson, not only mid-quiz.
- **A "🗺️ Map" button in the quiz's own tool row**, alongside Hint/
  Calculator/Sheet, so it is live exactly where "reference it while
  answering" actually means something.

Rules that are the point:

- **Content-shaped, like `sorts`/`bee`/`guide` — a unit opts in by carrying
  the field, never inferred.** A generic "every unit with a graph gets a
  map button" rule would have put a Map door on ordinary physics/algebra
  graph questions that have nothing to do with a reference map.
- **The tool row resolves the REAL source unit, not the synthetic wrapper.**
  `mru = unitFor(q._srcUnit || u.id) || u` — the exact same `_srcUnit`
  resolution `answer()` already uses for qstats and misses — so a laddered,
  reviewed, or shuffled question from the lat/long unit still offers its
  map even though `u` in that moment is `__ladder__`/`__review__`/
  `__shuffle__`, none of which carry `mapRef` themselves.
- **The reference map is a SUPERSET, not a duplicate of any one question's
  graph.** `unit-az-latlong`'s `mapRef` plots all 11 cities the unit's
  questions ever mark (the overview card's original 8, plus Dallas, Memphis
  and San Francisco from individual questions) on the same 5°-grid window —
  so opening it mid-question shows more context than that question's own
  four dots, which is the entire reason to open it.
- **Measured for label overlap before shipping, same discipline as the v145
  fix**: `getBBox()` across every `<text>` element in the 11-point graph,
  zero overlaps. The existing overlap-regression test in
  `tools/test_az_latlong.js` was extended to also check `u.mapRef`, not
  just `cards[].graph`/`questions[].graph`.

Engine only in Ad Astra — no unit there carries `mapRef` yet, so
`unitCard()`'s new block and the tool row's new button are both dead code
until a unit opts in, same posture as `SHEETS` before a teacher issues a
reference sheet.

`tools/test_az_latlong.js` gained four assertions: the unit's `mapRef`
carries all 11 cities, the shelved unit's own card offers the Map door
(this unit shelves as a one-lesson book via its ` · ` title, so the door
is one tap inside the spine — same as any other shelved lesson), the
quiz's tool row offers a Map button that opens the graph in a real modal,
and the no-overlap sweep now covers `mapRef` too.

### Atlas paper (v147 / Ad Astra v165, engine in both apps)

Chris, looking at the new map tool: "can we make the map have its own
white background so it looks like it was ripped out of an Atlas."

**A graph spec may carry `atlas:true`** — content-shaped like `xabs`/`xsuf`
and every other per-graph flag, never inferred, so an ordinary math or
physics graph (graph paper's own metaphor) is completely untouched.
`graphNode()` adds an `atlas` class to its `.graph-wrap` when the flag is
set; `.graph-wrap.atlas` paints an explicit white/cream page background
(`#fefcf5`), a soft border, a lifted-page box-shadow, a slight rotation,
and the SAME `feTurbulence` grain the flashcards' Cardstock treatment
(v142) already uses, at a slightly stronger opacity tuned for a much
larger flat area than a card face.

- **Deliberately theme-independent**, the same call Cardstock made: a
  physical page does not change color with dark mode, so the atlas
  background is a fixed light color regardless of `data-theme`. Verified
  by screenshotting both themes — the map itself is byte-identical either
  way, which is the point.
- **Every graph in `unit-az-latlong` carries it** — the overview card, all
  11 question graphs, and the new `mapRef` tool — because they are all the
  same real-world map at different zoom levels; giving only the `mapRef`
  tool the treatment while its sibling question graphs kept the plain
  graph-paper look would have read as two different maps.
- **Reuses the exact grain data-URI from Cardstock rather than inventing a
  new texture**, so the app's "this is a physical object" visual language
  (the note-from-home post-it, cardstock flashcards, now atlas pages) stays
  one consistent idiom rather than three.

`tools/test_az_latlong.js` gained an assertion that every graph in the
unit (cards, questions, `mapRef`) carries `atlas:true` and that
`graphNode()` renders the `atlas` class.

### The Trivia Ladder gets a memory (v147 / Ad Astra v165, engine in both apps)

Two related asks in one message: "can we have the girls see when they
finish the trivia" and "can we store game points in the stars tab or
other tab so the girls can see how they've done — we'll figure out a use
at a later time." Both are visibility, not a new mechanic, and both are
built on the same one-field addition.

**A finished board now stamps its log with `done:true` and `points`.**
`ladderLog()` already wrote a `mode:'ladder'` log on every tile answered;
it now also writes whether that write was the LAST tile (`done`, needed
because the same log record is updated in place tile by tile, so `total`
alone can't tell a finished 6-question board from a still-in-progress
10-question one) and the flavor score itself (`points`, the same number
`ladderPoints()` already computed for the results screen — extracted into
its own function so the finish screen and the log write share one
formula). This is a deliberate, narrow reversal of the v156 rule that
"the in-session points total... resets every play" — Chris asked for the
opposite, on purpose, so it changes.

- **"When they finish" — the door remembers.** Both Trivia Ladder buttons
  (`unitCard()`'s lesson door and the subject screen's "mix of everything"
  door) gain a quiet second line, `ladderLast(unitId, classId)`, reading
  "Last played Sep 7 · 5,500 pts" once she's finished that board at least
  once — the same "status on the door" rule Kat's v150 review established
  for the quiz door (`quizProgress()`) and the flashcard tile
  (`cardsProgress()`), now extended to the one door that had none.
  `.btnstack` is a small new class (a column-flex wrapper inside the
  existing `.btn.btn-secondary`) so the icon+title line and the status
  line stack rather than running together — the button's own centering is
  untouched.
- **"Store the points... we'll figure out a use later" — the Stars tab, not
  a new tab.** A "🎯 Trivia Ladder" card, right after Trophies, reads
  "N boards finished" and the all-time best score in the game's own gold
  pill (`.ladderworth`, the same `#f2ca63` reveal the finish screen and the
  in-question badge already use), plus which unit and when. `ladderGames()`
  (`logs().filter(done)`) and this card are deliberately the ONLY new
  surface — no leaderboard, no per-unit breakdown, no ranking against a
  sibling's device. Chris said the use is still open, so the summary stays
  a plain fact rather than guessing at a mechanic he didn't ask for.
- **Real XP is completely unaffected.** `ladderLog()`'s `xp` field, the
  qstat/miss crediting in `answer()`, and the badge/celebration triggers
  are all untouched — `points`/`done` are two new fields on a record that
  already existed, not a second ledger.

`tools/test_ladder.js` (same file, both apps) gained three assertions: the
finished log carries `done:true` and the same points the results screen
showed, the lesson's own door names when it was last played with the
score, and the Stars tab renders the "N boards finished" / best-score
summary.

### The companion does more, and a clearer voice (v153 / Ad Astra v171, both apps)

Chris, after agreeing with a scoped-down version of a bigger idea he'd
floated: *"I'd like to also explore their companion doing more work.
Specifically sharing words of encouragement during tests and games."* The
recommendation on the table was to extend the companion to pause points
that already exist in the app, rather than true mid-question interruption —
he agreed, so that is what shipped. Alongside it, one real bug fix he
reported separately: *"when the AI says the words, it rarely says them
correctly."*

**Two new companion moments, each firing exactly once.** The companion's
hard rule has always been "never interrupts... never mid-question, never
over the timer" — this does not relax that rule, it finds two places inside
the existing flow that are ALREADY pauses, not interruptions:

- **Mid-round, in the explanation card.** Right after she answers the
  question at the round's midpoint (`Math.floor(quizState.order.length/2)`),
  a companion bubble appears below the explanation, before the Next button —
  the same visual slot the explanation and steps already occupy, so it reads
  as part of the pause she is already in, not a popup. A new pool,
  `COMPANION_MID`, carries process-only, no-verdict lines ("Halfway. Whatever
  pace you are keeping, keep keeping it.") — it never says how the round is
  going, since that would turn a messenger into a scoreboard.
- **On a Junior Jeopardy Daily Double**, before she answers it — gone the
  moment she does. A new pool, `COMPANION_DD`, offers calm confidence
  specifically for the one tile in a board that raises the stakes ("Daily
  Double. The value went up; the way you answer it did not.").

**Both are deliberately narrow, and the exclusions are the point:**

- Skipped on **Beat the clock** (`quizState.timed`) — nothing should slow a
  countdown round down, and the whole point of that mode is speed.
- Skipped on the **Growth Zone review** and the **daily three** — both are
  built for low friction, a habit loop that runs most days; an extra beat
  there is exactly the friction those two features were built to avoid.
- Skipped on an ordinary Jeopardy tile, and the mid-round line is skipped
  **entirely** on a Junior Jeopardy round — the Daily Double already gets its
  own line, and two companion moments in one quiz screen would be one too
  many.
- Both pick their line **deterministically** (`mixHash`), so a re-render for
  any reason never swaps the line out mid-read.
- The existing end-of-activity lines (quiz results modal, Junior Jeopardy's
  finish screen) are completely unchanged — these are two NEW moments, not a
  replacement for the two that already existed.

**Only the flagship species has its own voice for the new pools**, same as
every other companion pool: the dragon (Ad Astra) and dolphin (Wayfinder)
each gained `mid`/`dd` entries in `COMPANION_VOICES`; every other companion
falls back to the shared `COMPANION_MID`/`COMPANION_DD` defaults, exactly
like `cheer`/`steady`/`idle` already work. `companionPool()`'s fallback map
gained the two new kinds.

**The voice fix.** `say()` never set `lang` or picked a `voice` on its
`SpeechSynthesisUtterance` — on Android Chrome that leaves the choice to
whatever the phone's default TTS engine and voice happen to be, which varies
by device and is often the lower-quality compact/network voice rather than
the best one actually installed. `pickTTSVoice()` now asks
`speechSynthesis.getVoices()` for the best real, on-device English voice
(preferring a local Google US English voice, since that is consistently the
highest quality on the Android/Chrome target), cached in `ttsVoice` and
re-picked on `onvoiceschanged` (voices load asynchronously on first use).
`say()` sets `u.lang = 'en-US'` unconditionally and `u.voice` when one was
found — so even on a device where no matching voice exists, the utterance
still carries the right language hint, which costs nothing and can only
help. This could not be verified by ear from this environment (no audio
output here, and the sandbox's own Chromium ships zero installed voices);
it is the standard, well-documented fix for "TTS sounds wrong on Android
Chrome" and degrades safely to the exact previous behavior when no voice is
available.

`tools/test_companion_mid.js` (same file, both apps) covers: an ordinary
round shows the bubble at exactly the midpoint question and nowhere else; a
timed round and a review round never show it; a Junior Jeopardy Daily Double
shows its own line before answering and clears it after; and an ordinary
(non-Daily-Double) tile never shows that line. Voice selection has no
dedicated test — there is nothing to assert against in a headless browser
with no TTS voices installed, and the fix is additive/inert in that
environment by design.

### One question, and it moves (v152 / Ad Astra v170, both apps)

Chris, three requests in one message, all about the emotion check: rethink
the pre-quiz mood questions, drop back to one question before plus the one
after (removing "teach it back"), and make the one remaining question much
bigger with no Skip — answering it should walk straight into the quiz.
Alongside that, a real bug: tapping the **+** to open a session's dropdown
in the parent's day view threw her back to the top of the screen instead of
opening the row in place.

**The day-view bug.** `daySessionRow`'s expand toggle called `go('day', {...})`
to update `ctx.openSes` — and `go()` always calls `window.scrollTo(0,0)` on
every navigation, since that is the right default for an actual screen
change. Toggling a row open is not a screen change; it now mutates
`ctx.openSes` directly and calls `render()`, the exact pattern `unitCard()`'s
own detail-fold already uses (`ctx._dtl = ...; render()`). One thing had to
travel with the fix: the OLD `go()`-based rebuild replaced `ctx` wholesale,
which had the side effect of always dropping `ctx.allQ` — the rule that
opening a session (or a different one) starts misses-first, never carrying
over a "show all" from whatever was open before. Mutating `ctx` in place
would have silently kept `allQ` around instead, so the click handler clears
it explicitly now. `tools/test_misses.js` caught this the moment it was
missed — a real regression from the scroll fix, not a hypothetical one.

**The check-in is one tap now, and it decides everything.** The pre-quiz
`FEELING` scale (a second question, "How are you feeling right now?") and
the "Skip and just quiz" button are both gone. `SCREENS.checkin` renders
one large card (`.checkin-big`/`.scale-big`, 40px emoji, 100px-tall buttons)
holding only the readiness `READY` scale, and tapping any option **is** the
answer and the way in — no Start button to confirm it a second time. Every
tap (re)sets the pick and restarts a 350ms beat before it commits and
navigates into the quiz; tapping a *different* option within that window
corrects a mis-tap, since there is no longer a separate confirm step to
catch that at.

- **A pool, not one fixed line** (`READY_PROMPTS`, `readinessPrompt(unitId)`)
  — asked before every quiz, the single remaining question needed enough
  variety not to go stale now that it is the whole screen. Deterministic per
  unit per day (`mixHash`), so a re-render mid-decision never swaps the
  question out from under her. Only the PROMPT WORDING rotates — the `READY`
  rating scale itself is unchanged, so `calibrationPairs()` keeps comparing
  the same 1–5 scale it always has.
- **The low-mood care note moved, it didn't disappear.** The old pre-quiz
  screen never auto-started on a feeling of 1–2, holding the "you can still
  do this, and you can also stop" note until it had its moment — a real
  wellbeing feature, not incidental copy. With the feeling question gone
  from before the quiz, that note now surfaces on **postmood** instead,
  reworded past tense ("well done for finishing it anyway") since the round
  is already behind her by the time she says how it felt. A feeling above 2
  still leaves immediately, same as always; the "tell someone you trust
  today" line is unchanged and is the one clause of this that must never be
  cut for brevity.
- **"Teach it back" is gone outright** (Chris: "remove the 'teach' question
  at the end") — the textarea, its 80%-round gate, and the save. `teach`
  stays a real record type: old answers still read verbatim in the parent
  view's "In her own words" and Fresh start still clears them, but nothing
  writes a new one. Postmood is back to exactly what it was built to be —
  one feeling tap, done.
- **The pre-quiz `mood` record no longer writes `feeling`** — omitted, not
  written `null`, so an old record with a real reading and a new one without
  it are told apart by the field's presence rather than a value that could
  read as "rough". Two downstream readers had to be checked for what an
  absent `feeling` does to them: `daySignals()`'s "logged a low mood" signal
  now reads `s.post.feeling` (which has always existed) instead of
  `s.pre.feeling`, so it keeps firing for every session, old and new, rather
  than only for history; and the parent view's "Average mood before
  studying" filters `undefined` out before averaging — unfiltered, one
  `undefined` in the array poisons `avg()`'s running sum to `NaN` the moment
  a single new-style record joins the historical ones. Caught by actually
  running the parent screen against seeded data, not by reading the diff.

`tools/test_polish.js` was rewritten for the new shape (a single tap moves
straight into the quiz; a low post-quiz feeling shows the care note and
waits for a real Done) and, as a side effect of using a dedicated seeded
unit instead of reusing one already mid-round from an earlier test in the
same file, incidentally fixed a second real bug it had been silently eating:
the OLD "check-in starts itself" check was quietly failing before this work
too, because reusing a unit that already had a parked/resumed round meant
the resume path's restored `quizState` won over the fresh `pre` the check-in
had just set — a genuine resume-path gap, unrelated to this feature, now
sidestepped in the test and left for a separate pass if it matters live.
`tools/test_misses.js` (the `allQ`-drop regression above) and
`tools/test_ux2.js` (a stale comment about teach-it-back) round out the
changes; `tools/test_ladder.js`'s own quizState-contamination test used the
old two-scale check-in to reach its ordinary quiz and now uses the one-tap
version.

### A wager, and a report of the game (v151 / Ad Astra v169, both apps)

Chris, after confirming the quizState-leak fix held across two full boards:
*"let's make double jeopardy a wager they can make, I think this might show
confidence in how well they know their material. It would nice to see a
report of this game on the parent side too. And to a smaller degree in the
kids Star tab."* Three pieces, and the third turned out to already exist.

**The wager is scoped to Double Jeopardy's Daily Double only.** Round 1's
Daily Double keeps the plain flat double it has always had — a fanfare
modal, "Bring it on," worth double either way. Real stakes only apply the
second time she plays a lesson, which mirrors the show itself (wagering is
a Daily-Double thing, not a universal one) and gives a clean progression:
simple the first time through a lesson, a real bet once she has finished it
once. `jjWorth(k)` reads `ladderState.wager` when the tile IS the Double's
Daily Double and a wager has been placed; every other tile is untouched.

- **The range is `[the tile's own face value, her current running score]`.**
  The floor means a wager can never pay LESS than the flat double would
  have — she is never worse off for engaging with the mechanic. The
  ceiling is her own score at that moment, so the biggest bet she can make
  is everything she has actually earned on the board so far, never a number
  invented for the occasion.
- **When her score has not yet caught up to the tile's value** (typically
  the very first tile she opens on a board, before anything else is
  banked), `max <= min` and the range collapses to nothing — there is no
  meaningful choice to offer. It degrades to the same flat-double modal
  Round 1 uses, worded to say why ("Your score isn't ahead of this tile
  yet, so it's worth N points either way"), rather than rendering a
  zero-width slider that pretends to be a choice.
- **A native range input, not a rebuild of `numberLine()`.** The math
  question widget is a different skill (read where a value falls on a
  fixed line); a wager is "pick a number within a range," so a lean
  standalone `.wager` component was built instead — a styled `<input
  type=range>`, a live gold readout above it, the two bounds printed at
  either end. Step size is computed to give roughly 20 increments,
  rounded to the nearest 10, so the slider feels continuous without
  landing on ugly numbers.
- **Winning pays the wager; losing costs exactly the wager**, not the
  tile's flat value — `jjWorth()` is the single source both `answer()`'s
  scoring and the on-screen "★ Daily Double · N" badge read, so the two
  can never disagree. The running floor-at-zero rule from the original
  Junior Jeopardy build (v149) is untouched: a wager that would take her
  below zero simply costs whatever is left.
- **The log carries `wager` and `wagerWon`** (`ladderLog()`), alongside the
  `done`/`points`/`round` fields v147 already added — two new fields on the
  existing record, not a second ledger. `wager` is null on a board where
  the Daily Double never got a real bet (the degraded flat-double case
  still stamps `wager` with the flat amount, since it WAS the amount risked
  — the field means "what was risked," not "was a slider shown").

**The parent-side report (`ladderParentReport()`).** A new "Junior
Jeopardy" card in the parent view, right after "What she asked for help
with" and before "Recent sessions" — boards finished (with a Double
Jeopardy count folded in), the best score and which lesson it came from,
accuracy across every board, and — only when at least one wager has been
placed — how many of them she won. A "Recent boards" list under it names
the last six by lesson, round, score and, where a wager was involved,
whether it won or lost. Everything is derived from `ladderGames()` at
render time, same discipline as the Stars-tab card: no new record type,
nothing that could drift out of sync with the logs themselves.

- **Deliberately fuller than the Stars-tab card**, per Chris's own framing
  — "a report... to a smaller degree in the kids Star tab." The
  boards-finished-and-best-score summary he asked for on her side already
  shipped in v147 ("The Trivia Ladder gets a memory"); nothing was added
  to it here. Wager detail — win rate, per-board outcomes — is grown-up
  information about how she plays, not something her own screen needs to
  editorialize on: the game already tells her in the moment whether she
  won or lost the bet.
- **"What she is using" gained one line**: "Junior Jeopardy boards
  finished N," alongside the existing tutor/quiz/flashcard counts that
  section already lists — the same treatment every other activity gets
  there.

**A real pre-existing bug turned up building the report, and got fixed
alongside it.** "Recent sessions" built its label with a three-way
ternary — focus, or `mode==='quiz'` said the bare word "Quiz," or
everything else said "Flashcards" — so a Junior Jeopardy log (or a Sort,
Star sky, Spelling Bee or reading session) rendered as "Flashcards"
regardless of what it actually was, and a Beat the clock / Growth Zone
review / Shuffle round / daily-three log — all `mode:'quiz'` under the
hood — all rendered as the identical bare "Quiz," losing the distinction
`modeLabel()` already knows how to draw everywhere else in the app. Fixed
by routing "Recent sessions" through `modeLabel()`, the same function the
day view, the Stars tab and everywhere else already use — one function,
one truth, rather than a second copy of the same logic that could drift.

`tools/test_ladder.js` (same file, both apps) gained: Round 1's Daily
Double confirmed still flat (no slider, ever); the degraded flat-bet modal
at zero score; the real slider's bounds, live readout, and that a loss
costs exactly the wager rather than the tile's flat value; the log
recording the wager and its outcome; the parent-view card's three
numbers and its "Recent boards" list; and the Recent-sessions fix, both
for a Junior Jeopardy log (never "Flashcards") and a Growth Zone review
log (never the bare word "Quiz").

### The board that followed her home (v149 fix / Ad Astra v167 fix, both apps)

Chris: "I tested out a jeopardy question, left the game and tested a quiz
question, but after the how do you feel questions, I was brought back to
the jeopardy game." Reproduced and root-caused, not guessed at.

**The bug had two parts, and only their combination reaches her.** Leaving
a Junior Jeopardy question by anything OTHER than the board's own Leave
button or answering all the way through — a bottom nav tab, the back chip,
the brand logo — left `quizState` DANGLING with `ladder:true` and
`unitId:'__ladder__'`. That is by design up to a point: `go()`'s own
leave-hook explicitly skips settling a ladder round, because the board
handles its own return-to-board and its own log (v156). What it did not
do was clear `quizState` at all, on the reasoning that the board's own code
would clean up after itself — true only when she leaves through the
board's own paths. Any other exit left the wrong `quizState` sitting there
indefinitely.

The second half: `SCREENS.quiz`'s rebuild check —
`if(!quizState || quizState.unitId!==u.id || quizState.timed !== !!ctx.timed)`
— correctly recognises that the dangling ladder state doesn't belong to
the NEW unit and enters its rebuild branch. But inside that branch, the
fresh-build fallback only fires `if(!quizState)` — true when quizState was
literally absent, false when it was merely WRONG. With no saved round for
the new unit (the ordinary case), the branch fell all the way through
having changed nothing, and the stale ladder `quizState` survived into
the next quiz untouched.

From there the rest follows mechanically: the next quiz's own "Next"
button reads `quizState.ladder` (still true) and calls `ladderReturn()`
instead of the ordinary `finishQuiz()` path — and `ladderReturn()`/
`ladderLog()` route off the ORIGINAL, unrelated `ladderState` global
(unitId and classId from the abandoned board), not the unit she is
actually looking at. That is what sent her back to the old board.

Fixed in both places, so the same class of bug can't recur from a
different leave path:

- **`go()`'s leave-hook now always resolves an abandoned quiz.** A ladder
  round gets `quizState = null` (still no settle, no log — an abandoned
  tile stays exactly as invisible as it always was); anything else keeps
  the existing partial-save-and-finish behavior.
- **`SCREENS.quiz`'s rebuild unconditionally discards the old `quizState`**
  the moment the outer condition says a rebuild is needed, before trying
  `loadRound()` or falling back to a fresh round — so a `quizState` that is
  merely WRONG can never survive this branch untouched, from this bug or
  any future one shaped like it.

`tools/test_ladder.js` (same file, both apps) gained the reproduction as a
permanent regression test: open a Jeopardy question, leave via a nav tab
without answering, then take a completely ordinary quiz on a different
lesson start to finish — check-in, every question, the results modal,
"How did that feel?", Done — and land on the subject page, never back on
the old board. Run against the pre-fix code, it does not fail cleanly; it
throws, because the stale `quizState.order` indexes into the wrong unit's
questions entirely.

### Fifty units, all answer A (v149 / Ad Astra v167, both apps)

Chris, after the first Junior Jeopardy board: "the first set of questions
I tried the answers were all A." Measured first: across 63 screens on
real content in both apps the on-screen position of the correct answer
spread over every letter — the render-time shuffle (v64) is working, on
the board and everywhere else. What the scan found underneath is the
thing: **fifty shipped units — 19 here, 31 in Ad Astra — were authored
with the correct answer in slot A on every question.** Nearly every math
lesson and Topic Review, every Wordly Wise lesson, History, Latin,
Biology, Physics. `_balance()` exists in `unit_common` for exactly this
and these files predate it or skipped it. The shuffle was the only thing
between the girls and a giveaway, and the grown-up review queue reads a
file as written.

Three things shipped, in that order:

- **`check_content.py` warns** when 70%+ of a unit's MC/analogy answers
  sit in one slot (guides exempt — their order is the paper's). 50
  warnings before the fix, 0 after; it stays as the guard.
- **`fetchLibrary()` carries an ORDER-ONLY update without re-drafting.**
  `orderOnly(old, new)`: every question keeps the same four options and
  the same correct answer text, only the order moved, and cards/meta/
  question text are identical — then the merged record keeps her
  approval and never enters the queue. Anything else is a real change
  and takes the ordinary re-draft path (`test_orderonly.js` checks both:
  a rotated unit stays approved with no `chg`; one reworded option
  re-drafts and is tagged as an update). Without this, the rebalance
  would have queued fifty "updates" for Chris to re-read for a change
  that is invisible on every screen she uses — "nothing reaches her
  unread" is satisfied precisely because nothing new reaches her.
- **The fifty files were rotated** (the `_balance()` rule: slots cycle
  A,B,C,D in question order), `libv` bumped, `updatedAt` stamped a minute
  back. `kind:'order'`/`spell`/`slider` untouched (their option order is
  semantic), guides untouched, variants untouched. Verified against HEAD
  file by file: identical after normalising options to a sorted set and
  `ans` to its text — nothing but the order moved. The diffs look larger
  than that because the writer re-serialised compact inline arrays one
  item per line; the content is byte-for-byte the same tokens.

Why the report could not be reproduced on the board itself is still
open — most likely a small first board on a lesson where the shuffle
happened to land the answer under A a few times running, which the
all-A authoring would have made no more or less likely. The authored
skew was real either way and is gone.

### Junior Jeopardy (v149 / Ad Astra v167, both apps)

Chris, one message, nine asks: rename the Trivia Ladder "Junior Jeopardy",
make the boxes look like the show's screens, harder questions on higher
values, a Double Jeopardy, category names, sounds for right and wrong,
wrong answers that subtract, smaller amounts the first time and bigger
amounts with harder questions the second, and — inside a lesson — a
category from an older lesson, "just a few though". All nine shipped as
one rebuild of the board; what did NOT move is the part that matters.

**Answering still runs through the real quiz screen and `answer()`.** The
board hands the quiz one question at a time through a synthetic
`__ladder__` unit (`ladderUnit`, registered in `unitFor`) whose questions
carry `_srcUnit/_srcClass/_srcQid` — the Shuffle round's own mechanism —
so qstats, misses, hints, steps, flags and the map tool all land on the
REAL lesson exactly as an ordinary untimed round's would. Playing a board
still finishes the lesson. `answer()` needed one line (the sound); the
ladder guards in `go()`, `saveRound` and `persistRound` are unchanged.

**The board is categories × values, and the row picks the difficulty.**
Three columns, three rows (`JJ_COLS`/`JJ_ROWS`; two columns on a 6–8
question unit). Round 1 deals 100/200/300 down each column and wants a
level-1 (recall) question at 100, level 2 at 200, level 3 at 300
(`JJ_TIERS`); the Double deals 200/400/600 and shifts the tiers to 2/3/3.

- **A column's three questions are the best MONOTONE fit to its tiers**,
  not a row-by-row greedy pick. The first cut picked each row's nearest
  level in turn and could hand a column holding levels 1,1,3,1 a 300 that
  was easier than its 200 (row two took the 3, row three had only 1s
  left). `buildLadder` now sorts a column's pool easy→hard and tries every
  triple in that order, taking the one whose levels sit closest to the
  tiers — so the 300 is never easier than the 200 by construction.
  `test_ladder.js` asserts it on every column.
- **Levels are dealt evenly across columns** (`jjSplit` sorts by level
  before dealing round-robin) — otherwise one column could be all recall
  and another all analysis, and the tiers would have nothing to fit.
- **Category names, in order of preference:** a question's authored
  `cat` when a unit carries them (content-shaped, like everything else
  about a unit — no shipped unit does yet); a lesson's analogies as their
  own "Analogies" column when it has three or more; the lesson itself,
  split I / II / III, otherwise. The subject-screen board makes every
  column a different lesson (`lessonLabel`), least-practised lessons
  first. The category is the eyebrow on the question screen — it is what
  the show reads out.

**Round 1 vs Double Jeopardy is decided by `ladderLast()`** — the same
finished-board log the door and the Stars card already read (v147). The
first board on a lesson is Round 1; once she has finished one, every board
after is the Double: bigger values, harder tiers, and on a lesson board
the LAST column is an older lesson in the same subject — same shelf
preferred, then the one she has worked most, three questions only. That
is "the second time they play" and "just a few though" in one rule. In
the Double, the lesson is dealt across only the columns it will keep;
splitting three ways and discarding one starved the survivors of hard
questions (caught by the test's "top row asks level 2+").

**One Daily Double per board, never in the top row** (`ladderState.dd`),
revealed only when she opens it — a modal, the show's little fanfare, then
the real question at double stakes. The played screen keeps a ★.

**A wrong answer costs the tile, and the score floors at zero AS SHE
GOES.** Points were already flavor (real XP follows the ordinary quiz rule
and is never subtracted; that is unchanged), and Chris asked for the
show's rule, so a miss now costs the tile's value, double on the Daily
Double. Two deliberate softenings: the score never shows below zero (a
negative number on a nine-year-old's screen is a verdict, and nothing
else in the app hands one out), and the floor is applied per answer in
the order she played them (`ladderState.seq`), not to the total — the
first cut floored the total, and a wrong Daily Double left her on "0 pts"
AFTER a right 300, which swallowed the one thing the strip exists to
show. Now a miss at zero simply costs nothing.

**Sounds, synthesized.** `sfx('right'|'wrong'|'dd')` builds two- and
four-note tones in WebAudio — no asset files, the app stays four files —
gated on the same `fx:'quiet'` opt-down `celebrate()` honours, so opting
down keeps costing nothing. The wrong sound is a soft low two-note, not a
buzzer. **They play only on this board** (`answer()` checks
`quizState.ladder`); everywhere else the phone still never scolds.

**The board is a wall of TVs, theme-independent.** `.jj-board`/`.jj-cat`/
`.jj-tile`: the show's blue, gold serif numbers with a drop shadow, faint
scanlines, played screens going dark with ✓/✕. Same call as the atlas page
and the cardstock — it is a set, not chrome, and it looks the same in the
dark. This reverses v156's "the board stays in the subject's accent" at
Chris's request; the gold `.ladderworth` pill is unchanged and still the
score's colour everywhere.

`mode:'ladder'` stays as the log's record key so boards played under the
old name still read; the log gains `round`. `modeLabel` says Junior
Jeopardy; both doors and the Stars card were renamed (the Stars eyebrow
adds "Double Jeopardy unlocked" once a Double has been finished).
`tools/test_ladder.js` (same file, both apps) was rewritten: the renamed
door, a 3×3 Round 1 with the right values, named categories, monotone
difficulty on every column, a Daily Double below the top row, gold-on-blue
screens, the reveal and the double-stakes question, the running floor
(a wrong DD at zero costs nothing → a right 300 → a wrong 100 leaves 200),
the miss and qstat landing on the real lesson, sounds playing and going
quiet, the finish and its log, the Double's values/tiers/older-lesson
column, the mix board's lesson categories, and `modeLabel`. Run three
times in each app before shipping — the Daily Double lands on a random
screen, and the first version of the test had assumed which one.

### A shorter, slower clock (v148 / Ad Astra v166, both apps)

Chris: "Rivers beat the clock seems long — what is the timer set at now
and can it be extended?" The honest answer had two parts, and they pulled
in different directions once looked at together. The PER-QUESTION
countdown (`quizLimit()`) was never fixed — it already calibrates to her
own measured pace from real untimed quizzes, clamped to 8–40s (20s until
there is data). But Beat the clock's ROUND SIZE was quietly borrowed from
the ordinary quiz's own sitting size (`u.round||QUIZ_ROUND`) — 10 on a
lesson-a-day math unit, 12 on a Topic Review — so a math Beat the clock
could mean up to 12 questions at up to 40 seconds each. Asked which one to
fix, Chris chose both: more time per question, fewer questions per round.

**The countdown is 1.5x more generous across the board**: 8–40s → 12–60s,
20s default → 30s. Straight scaling of the existing clamp, nothing new
invented — the calibration-to-her-pace mechanic is untouched, just given
more headroom at both ends.

**Beat the clock now deals its own fixed round, `BEAT_CLOCK_ROUND` (5),
regardless of `u.round`.** `pickRound(u, timed)` used the SAME sizing
formula whether or not the round was timed; it now branches on `timed` —
the ordinary quiz still serves the unit's full sitting exactly as before
(a lesson-a-day math quiz still clears all ~10 in one go), and only Beat
the clock is capped at 5. This is a genuine, deliberate split: **`u.round`
is content-side and means "how much of the lesson in one sitting"; racing
a countdown through the same 10–12 questions is a different, longer
activity than clearing the lesson, and gets its own engine constant
instead of inheriting the content knob.**

`tools/test_beatclock.js` (same file, both apps): `quizLimit()`'s new cold
default (30s) and both new clamp edges (a synthetic 90s/answer average
clamps to 60s, a synthetic 4s/answer average clamps to 12s), `pickRound`
on a `round:10` unit still deals 10 untimed but exactly `BEAT_CLOCK_ROUND`
(5) timed, and an end-to-end launch of Beat the clock on that same unit
serving a real 5-question round with its countdown inside the new range —
while the ordinary quiz on the identical unit is completely unaffected.

### Reading the map, not memorizing it (v144, THIS APP ONLY)

Two corrections from Chris after v143 shipped. First: *"are we able to use
the USA map that they studied in school and drive examples from that?"* —
her Drive folder had "US map -Longitude and Latitude.pdf", the Arizona
Geographic Alliance's "US Bingo" sheet, the actual map her class used for
latitude/longitude bingo (28 real US cities, a 5-degree grid from
130°W-70°W and 25°N-45°N). Second, and the bigger one: *"flashcards should
not quiz on exact longitude or latitude for a place. the focus is on how to
read a map."*

**Every card and question that reduced to "recall this place's exact
coordinate" is gone.** That was Phoenix/Tucson/Flagstaff/Yuma flashcards
each stating "roughly 33°N, 112°W" as a fact to learn, plus three questions
built the same way ("what is Phoenix's coordinate," "which city is at this
coordinate" — twice). All are memorization dressed as map-reading: the
correct answer is a specific number tied to a specific place, learnable as
a lookup table with enough repetition, which teaches recall instead of the
transferable skill. What survives and what replaced them is built around
two skills instead: **comparison** (furthest north/south/east/west among
cities actually shown on the map; two north-to-south and west-to-east
`kind:'order'` rankings) and **estimation** (reading a value between two
gridlines; judging which of several cities sits closest to a drawn
reference line). Every one of those is answerable only by looking at the
map in front of her that moment — there is nothing to have memorized in
advance, and repetition can't turn either skill into a lookup table the way
a fixed city-coordinate pair can.

**The real US map replaced the invented Arizona one, cities and grid taken
straight from her class sheet** (read via `download_file_content` +
`pypdfium2`, the same render-the-actual-PDF discipline every scanned source
gets — Drive's OCR snippet mangled the multi-column city/gridline layout
badly enough that trusting it would have misplaced several cities). The
bounding box and 5° gridlines match the class sheet exactly (widened a
couple of degrees at the edges so cities near 70°W/130°W aren't clipped).
**The country's outline is deliberately not drawn.** Arizona's near-rectangle
was simple enough to approximate honestly with about ten points; the
continental US coastline is a much bigger, more detailed shape, and a rough
attempt at it risked looking wrong rather than helpful. The grid and the
labeled cities carry the whole lesson without it — confirmed by building it
without an outline and finding nothing was lost.

**A real rendering bug turned up building this, caught by measuring, not by
eyeballing:** `renderGraph()`'s marked-point labels always render up-and-
right of their dot with no collision avoidance, so two cities close together
on the map can print on top of each other. It happened twice while choosing
which cities to pair per question — San Francisco's label ran into Denver's
on the overview card, and a "which of these two close cities is further
north" question (deliberately hard, Chicago vs. Detroit) picked a pair
whose labels physically overlapped into unreadable text, even though the
DOTS were exactly where they should be. Both were fixed by choosing a
different city or a different close pair (Chicago vs. Boston keeps the
same "closer than the others" difficulty with labels far enough apart in
longitude not to collide) — not by changing the engine, since real
collision-avoidance layout is a bigger job than this content needs.
`tools/test_az_latlong.js` now renders every graph in the unit and checks
every pair of city-label bounding boxes for overlap, so a future edit that
reintroduces this can't ship quietly.

`tools/test_az_latlong.js` also gained a content-safety sweep — parallel to
the one built for Ad Astra's TKAM re-chunk — that fails if any card states
a city's coordinate as a memorizable fact, or any question's stem asks to
state or match one.

### The Arizona map (v143, THIS APP ONLY, engine also in Ad Astra) — superseded by v144 above; kept for history, not accurate to what shipped

Chris added his own map for direct lat/long instruction and asked for a
further-practice quiz with a map, for Arizona specifically. `renderGraph()`
already drew math/physics graphs from a `{w, series, pts}` spec — a real
lat/long map turns out to be exactly that spec with longitude as x and
latitude as y, an equirectangular projection that introduces no meaningful
distortion at Arizona's size. Nothing new to build for the outline or the
city markers: a `series:[{type:'pts', pts:[...]}]` already draws an
arbitrary closed polyline (the state outline, hand-built from its real
bounding corners and a simplified path along the Colorado River), and the
existing `pts:[{x,y,label}]` marked-point mechanism already places and
labels cities.

**One real engine gap, though: signed degrees read wrong to a 4th grader.**
A map has to plot real signed longitude (west is negative, so the shape
lands in the right place on screen) but she reads "112°W", not "-112".
`renderGraph()` gained optional `g.xabs`/`g.yabs` (strip the sign for
display) and `g.xsuf`/`g.ysuf` (append the letter) — applied only to the
axis tick labels via a new `fmtAxis()`, so every existing math/physics graph
(which sets none of these) renders byte-identical to before. Carried into
Ad Astra's copy too, unused there for now, so the shared block stays
identical between repos.

**A second, unrelated gap turned up building this: this app's flashcard
screen never rendered `card.graph` at all.** Ad Astra's `SCREENS.cards` has
always appended a card's graph to the back face — several shipped Algebra
and Biology cards depend on it — but that line was never ported here, so a
card's own graph rendered only in the grown-up review queue and never
during her actual study. Nothing here had ever attached a `graph` to a CARD
before this unit, which is why no test had caught it. Fixed by porting Ad
Astra's one line (not `signImgNode`, which is ASL-only and doesn't exist in
this app).

**The outline is deliberately a simplified practice shape, not a survey-
accurate one** — said outright in `parentNote`. Arizona's real western
border follows the Colorado River closely; this map approximates it with
about ten vertices, which is honest for "read a one-degree grid over a
recognizable Arizona," the actual skill being taught, and not honest as a
cartographic reference. Every city coordinate was rounded to the nearest
degree and cross-checked for the specific comparisons each question makes
(furthest north/south/east/west, and two north-to-south / west-to-east
`kind:'order'` rankings) — one pair of cities (Flagstaff/Kingman) came out
within 0.01° of each other on latitude and was deliberately never used
against each other in a comparison question, since that's a rounding-noise
difference, not a teachable one.

- **Three questions test the N/W trap on purpose**: every real Arizona
  coordinate is °N and °W, never S or E, and a coordinate that swaps the
  order or the hemisphere points somewhere else on Earth entirely (or
  nowhere, since latitude can't exceed 90°). That's the mistake Chris's own
  request flagged as most likely.
- **Concept cards and questions (equator, Prime Meridian, hemispheres,
  reading order) stand alongside the map-application ones** rather than
  assuming his own instruction covered everything — a self-contained unit
  outlasts any one conversation.
- classId `history`, matching the real school unit (`SUGGESTED_ASSESS`
  already lists "History quiz · Unit 5: latitude & longitude").

`tools/test_az_latlong.js` covers the engine and the content together: the
axis ticks render "112°W"/"33°N" and never a bare negative number, the
outline and all four cities render as real SVG on a sampled card graph, a
full quiz round completes, a map question and an order question both play
with the map visible, and the flashcard deck steps through cleanly with the
map card's graph actually rendering (the parity-gap regression, caught by
checking `card.graph` appears live, not just that the deck completes).

### Cardstock (v142 / Ad Astra v161, both apps)

Engine, identical here — see ad-astra/CLAUDE.md's section of the same name.
Chris asked whether the flashcards could look more like paper; three grain
strengths were mocked live against real cards before shipping, and he picked
the middle one. Every face — subject-painted, plain, or her own handwritten
deck — now carries a fine `feTurbulence` noise behind the fill,
`soft-light`-blended at low opacity, strictly behind the legibility scrim
and the text.

**This app's copy needed a real fix the other didn't drive.** The Spelling
Bee honeycomb card's `.face.bee::before` already owned that pseudo-element
for its opaque striped top bar; the new grain rule's opacity and blend-mode
leaked through and washed the bar to near-invisible before `.face:not(.bee)`
was added — confirmed live, not just reasoned about. `tools/test_papertexture.js`
is the same file as Ad Astra's, with one Wayfinder-only assertion that the
bee bar stays fully opaque.

### Breathing room, take two (v141 / Ad Astra v160, both apps)

Engine, identical here — see ad-astra/CLAUDE.md's section of the same name.
Chris clarified v140's fix landed on the wrong 0px gap: the one he meant was
the last row of filter chips sitting flush against the due card below it,
not the button-to-caption gap inside the card (also real, also now fixed,
but a different pair of elements). Same shape of bug — `.gz-chips` has no
`margin-bottom`, `.card` has no `margin-top`, two block siblings collapse to
0 — fixed the same way: `.gz-chips+.card{margin-top:var(--gap)}`.
`tools/test_gzfilter.js` is the same file as Ad Astra's, with the same
second gap assertion.

### Breathing room under "Start review" (v140 / Ad Astra v159, both apps)

Engine, identical here — see ad-astra/CLAUDE.md's section of the same name.
The Growth Zone's due card stacked its caption ("Get one right and it goes
quiet for longer...") flush against the "Start review" button with a
measured 0px gap, because `.btn` carries no margin and `.card p` zeroes its
own margin-top — the one card in either app that puts its button BEFORE its
caption rather than after. Fixed with one shared rule,
`.card .btn+p,.card .btn-row+p{margin-top:var(--gap-row)}`, the same 10px
two stacked buttons already get. `tools/test_gzfilter.js` is the same file
as Ad Astra's, with the same added gap assertion.

### Where to start (v139 / Ad Astra v158, both apps)

Engine, identical here — see ad-astra/CLAUDE.md's section of the same name
for the full reasoning. Chris noticed the companion's due-review line on
Study was quoting a bare cross-subject total ("7 questions are back") with
nowhere to look; `threadTarget()`'s `due` case now ranks subjects the same
nearest-unscored-test-then-count way the Growth Zone screen's own chips do
and names the one leading the queue ("7 questions came back around — 4 in
English. That is where to start"), and the tap lands already filtered to it.
The perch's plan-line font dropped its inherited italic — now upright, 600
weight, 19px, `--ac-fg` — while the affirmation swap keeps its deliberate
Fraunces italic. And the daily three's not-yet-done door now wears the same
hero gradient/accent treatment as the resume-round and Grown-ups doors.
`tools/test_plan.js` and `tools/test_games.js` are the same files as Ad
Astra's, updated the same way.

### The grown-up door, and the ladder in gold (v138 / Ad Astra v157, both apps)

Two small polish requests from the same conversation, engine, identical
here — see ad-astra/CLAUDE.md's section of the same name for the full
reasoning. The Grown-ups door on Settings is now the first thing on the
screen, a `.hero` card carrying a live "🧪 Sandbox is on/off" eyebrow (Chris
and Kat check sandbox status often; the girls rarely open this screen at
all) — status only, never a toggle, so the ungated side of Settings still
cannot flip sandbox without the parent passcode. And the Trivia Ladder's
points wear the app's own existing gold (the done-pip/prep-band pair,
already measured) in exactly two places — the in-question "🎯 700" badge
and the finish screen's score — answering "make it feel like a game show,"
while the board's tiles keep the subject's own accent color.
`tools/test_settings_door.js` and the updated `tools/test_ladder.js` are
the same files as Ad Astra's.

### The Trivia Ladder (v137 / Ad Astra v156, both apps)

A phone-native, solo Jeopardy-style game — Chris's follow-up after mocking
one up as a standalone Artifact to decide whether it was worth building.
Engine, identical here — see ad-astra/CLAUDE.md's section of the same
name for the full design: up to ten of a unit's own MC/analogy questions
dealt onto point tiles she opens in any order, answered through the real
unmodified quiz screen (so hints, steps, the calculator, sheet and every
existing tool travel for free, and `answer()` needed zero changes), two
entry doors (a lesson's own bank, or a subject-wide mix via the same
`buildShuffleUnit()` the Shuffle round already uses), and points that are
pure flavor for the choosing — real XP still follows the ordinary
10-per-correct rule. `tools/test_ladder.js` is the same file as Ad Astra's.

### A fuller sky, and "Do now" (v136 / Ad Astra v155, both apps)

The living-sky starfield gained a 4th twinkle layer (112 points across four
layers, up from 42) and a minority of its points now carry real star color
— blue-white, gold, rose, mint, lavender — instead of plain white. Engine,
identical here (Wayfinder's `.skyfx` never had the aurora shimmer, only the
shooting stars — that stays as-is). "The daily three" on Today gained a
small "DO NOW" eyebrow, same size as a date header. See ad-astra/CLAUDE.md's
section of the same name.

### After the quiz, and Match removed (v135 / Ad Astra v154, both apps)

Two changes from living with the app, both Chris, both engine and
identical here — see ad-astra/CLAUDE.md's sections of the same names.

Finishing a quiz (or a flashcard deck) now lands on the **subject page**,
not the specific lesson — "in case there is more quizzes or stuff to
study." This reverses v150's "return to the lesson" rule; review rounds
still go to the Growth Zone and the daily three to Today. `lessonHome()`
is gone; every call site is a plain `go('unit',{classId})`.

**Memory Match is removed** ("it isn't very helpful") — the door, the
screen, and its state and functions are gone outright. `mixHash` (defined
inside Match's old block but load-bearing for swipe sort, `pickRound()`
and the plan-of-attack swap) moved to its own standalone definition.
`modeLabel()` keeps its `match` case so historical sessions in a synced
gist still display correctly; nothing writes a new one. The daily three,
Match's neighbor from the same original batch, is untouched.

`tools/test_ux2.js` and `tools/test_games.js` are the same files as
Ad Astra's, updated the same way.

### Bunch the plan (v134 / Ad Astra v153, both apps)

Caught on River's own app — a real test week stacked three subjects into
six pieces (a card, then a separate full-width Mixed round button,
repeated). The button now nests inside its subject's card instead of
following it, so a ramped subject is one block. Engine, identical here —
see ad-astra/CLAUDE.md's section of the same name, including the
`stopPropagation` that keeps the tap from also re-firing the card's own
navigation.

### Font and spacing on the plan (v133 / Ad Astra v152, both apps)

The companion's bubble on the plan perch is 17px in both its states (was
15px for the plan line, 17px only in the affirmation swap), and the
mixed-round button carries `.rampbtn` for the same 10px bottom margin
every `.plan` card gives itself, so a ramp subject's card is no longer
flush against the next one. Engine, identical here — see
ad-astra/CLAUDE.md's section of the same name.

### The plan of attack (v132 / Ad Astra v151, both apps)

Study opens on the companion's perch, whose line is the thread itself
(due reviews → a close test → the open lesson → the plan) and which is
the door; the affirmation card and the "Pick up the thread" hero are
gone, and roughly one day in three with nothing pressing the companion
says the day's affirmation instead. Engine, identical here — see
ad-astra/CLAUDE.md's section of the same name for the rules (never a
swap over a due review or a close test; the star stands in when no
companion is chosen; the weekly aim stays). River's due line keeps its
own wording ("came back around… stay caught"). `tools/test_plan.js` is
the same file as Ad Astra's.

### Practice, then the test (v131 / Ad Astra v150, both apps)

Kat's nine-point review, shipped in step — engine, identical here. See
ad-astra/CLAUDE.md's section of the same name for every rule and
measurement: status on the doors (`cardsProgress`, `quizProgress` in
rounds, `qstat.plain` so only the quiz moves the map), the Practice /
Test yourself sections with the quiz as the last, wide door, the details
folded behind the title and "What this covers" removed from her side, the
lesson opening under its own map stop, `lessonHome()` after a round, test
prompts opening the Growth Zone for their subject, and Today streamlined
with the timetable moved onto Study as the subject list.

Two things are this app's own. **Study's line-up rotates**: it is
`dayClasses()` for today, or for the next school day on a day off (the
divider says which — "Your subjects · Thursday's order"), and every
`STUDY_CLASSES` subject not on that day follows the line-up with its
`daysFor()` in place of a time, so Writing on a Wednesday still has its
row. And the Bee stays on the practice side with the other games; a bee
unit never gets the clock tile, as before.

`tools/test_ux2.js`, `tools/contrast_ux2.js`, `tools/test_horizon.js`,
`tools/test_tutoring.js` and `tools/test_clubs.js` are the same files as
Ad Astra's (worst measured contrast here 4.93:1, the door's status line).

### The number line (v130 / Ad Astra v149, both apps)

`kind:'slider'` — she drags a marker to where a number belongs. Engine and
rules in ad-astra/CLAUDE.md's section of the same name. Content here:
**`Topic 3 · Decimals on the Number Line`** (`unit-m3nl`, `prep:true`, twelve
sliders, `tools/builders/build_numberline.py`), built for the Unit 1 math
test on 9/10: tenths on 0–1, hundredths on zoomed-in lines (0.3–0.4,
5.1–5.2), two lines whose marks are halves rather than tenths (the
what-is-one-space-worth trap, the same as reading a cylinder), a halfway-
between question and a round-then-place question. Title-sorts after
"Decimals Extra Practice" and before "Topic Review" with no `order` field.
`tools/test_numberline.js` is the same file as Ad Astra's.

### The week of 9/9 (v129)

The 4th-grade newsletter of 9/3 (text layer, clean) adds two quizzes to
`SUGGESTED_ASSESS` for Wednesday 9/9 — Wordly Wise Unit 2 (the class calls
lessons "units"; `unit-ww502` is the shelf part) and History Unit 5,
latitude & longitude — the day before the Unit 1 math test already listed
for 9/10. Student hours confirmed unchanged. Science starts a Chemistry
unit (matter and its phases) the week of 9/7; nothing to build yet.

- **A content gap, flagged rather than filled:** there is no history unit
  for latitude & longitude and no source for one in Drive (the only Drive
  hits for "latitude" are the newsletter itself and an Ad Astra content
  backup). Her class has its own vocabulary for map components, so a unit
  from general knowledge would be guessing what Unit 5 covers.
- The 8/21 newsletter's four assessments (8/26–8/28) were never in
  `SUGGESTED_ASSESS`; they are past now, and the parent card filters to
  `sg.date >= today`, so adding them would render nothing. Chris can enter
  those grades by hand if he wants them tabulated.
- **The real Q1 progress report is in Drive now** (the earlier 62-byte file
  was a link). It is a course-level snapshot, not an assessment, so nothing
  in the app changes for it — the numbers are for Chris's eyes and were
  relayed to him, never written into this public repo.
- **Sedona's Paw Prints are unreadable from here**: image-only scans of
  78–221 MB each (9/4, 8/28, 8/21, 8/14, 8/7). `read_file_content` returns
  empty and the download cap is 10 MB. The Google Docs OCR route or a
  screenshot of the dates page, as with the Cub Hub slide, is the way in.

### Dress days, and the Cub Hub of 9/4 (v127 / Ad Astra v148 for the engine half)

Chris uploaded the 9/4 Cub Hub and asked for its special dress days in the
app. Two halves, one of which is still waiting on him.

**The engine half (both apps): `kind:'dress'`.** A day she dresses
differently for — Picture Day, a Spirit Week theme — pins on Today with its
own `Dress` label, never quiet, and lists in Coming up like any event. It
is a tone, exactly as `exam` and `benchmark` are: the row's copy is the
event's own `note`. Ad Astra carries the kind with no content yet.

**The content half (this app): the newsletter's dated list.** Its text
layer is only the "Important Upcoming Dates" list; pages 3–16 are image
slides, which is where the day-by-day Spirit Week themes live. The PDF is
12 MB — over `download_file_content`'s 10 MB cap — so it could be neither
rendered nor OCR'd from here. What the list gave: progress reports 9/4,
clubs begin 9/14 (a door to the clubs screen), **Fall Picture Day 9/16
(`dress`)**, hearing & vision screening 9/17, **Spirit Week 9/21–25
(`dress`, five days, with a note saying the daily list is in the
newsletter)**, Sandra Day O'Connor Day 9/25, SHINE lunch 9/30, Pledge
Signing Day 10/1. Nothing on the image pages was guessed at.

> **Resolved in v128:** Chris sent the Fall Week of Giving slide as a
> screenshot, which was faster than the OCR route. The five-day block is
> now five one-day `dress` events — Hat Day, Sport Day, Green & Seen,
> Disney Day, Bobcat Cub Pride — each with the slide's own instruction as
> its note, so every morning of that week names its theme. The slide is the
> Annual Teacher Fund's; the themes are what the app carries.

Also in the folders: **"Q1 Progress Report.pdf" is a 62-byte text file
holding a ParentSquare link**, not the report — nothing to read. And the
English folder gained the Plot Diagram quiz study guide, with answers.

**Plot Diagram: Pixar Shorts** (`unit-plot`, `content/english-plot-diagram.json`,
builder `tools/builders/build_plot_diagram.py`). The five stages applied
to the four shorts the guide covers — Geri's Game, Partly Cloudy, Lifted,
Piper. Ten cards (the five stages, a card on telling the climax from the
rising action, and one diagram card per short), 20 questions (18 "which
stage is this moment", two put-in-order), and a sort set — **before the
climax, or after it?** — which is the quickest drill for the one idea that
costs marks: many beats build the problem, only one turns it. Every event
is the guide's own beat. The quiz it was written for was dated 9/2, so the
`parentNote` says plainly this is for the skill going forward, not that
quiz. Titled without ` · ` on purpose: one part is not a shelf.

- The checker's own-bucket rule caught "takes piece after piece" in the
  sort set — the word *after* is bucket B's label. Reworded, not exempted.
- `tools/test_dress.js`: both dress days on the calendar and the rest as
  notes, the Picture Day row pinned with `Dress` and not quiet, Spirit Week
  reading Day 3 of 5, Coming up from a week out, and the plot unit shelving
  loose with its sort door and playing a round.
- `tools/test_clubs.js` had a time-bomb: it asked Today to show 9/1 via a
  ctx date the screen never reads, so it passed only while the real date
  sat inside the registration window. Now it points the clock, the way
  `test_dress.js` does.

> Stale tests, all failing on HEAD before this work and left for a cleanup
> pass: `test_polish.js` (the retired hero), `test_newsletter.js` and
> `test_runway.js` (both crash reading a field the brief rework removed).

### Swipe sort (v125 / Ad Astra v146, both apps)

Two buckets, one card, swipe or tap. Sets ride on units (`u.sorts`), draft
and review with them, and never touch the ladder. Three shipped here:
observation/inference on Quiz 1, quantitative/qualitative on Measurement,
changed-vs-measured on Variables — every item names its experiment so a
returned card stands alone. See ad-astra/CLAUDE.md's section of the same
name for the rules and the checker's own-bucket rule. `tools/test_sort.js`
is the same file in both repos.

### Match, and the daily three (v124 / Ad Astra v145, both apps)

Two zero-content games, engine, identical in both apps: memory Match on any
deck with 4+ matchable cards, and the daily three on Today — three
questions by date served as an ordinary round, misses to the Growth Zone,
done becoming three squares and a share line that carries no score. See
ad-astra/CLAUDE.md's section of the same name for the rules, the
`mixHash`-not-`hashStr` trap, and the scaled completion bonus.
`tools/test_games.js` is the same file in both repos.

### The Growth Zone, focused (v123 / Ad Astra v144, both apps)

Chips now scope the whole ladder (subject, then unit ranked most recently
missed), a second door reviews everything in the filter ahead of a test,
and rows fold to the question and its ladder bar. Engine, identical in both
apps — see ad-astra/CLAUDE.md's section of the same name for the rules,
the `on`-not-`updatedAt` trap, and the contrast measurements (worst
selected chip here 13.4:1). `tools/test_gzfilter.js` and
`tools/contrast_gzchip.js` are the same files in both repos.

### The practice test, twice (v122)

Chris: River has new Unit 1 science test material — make a replica of the
test she can submit answers to, with an answer key, and a generic test she
can take to study. Two PDFs in the Science "Quiz 1 - Material" folder:
"Unit 1 Review Test" (the teacher's *Practice for Nature of Science Unit
Test*, 19 points, explicitly labelled practice — not a live test) and its
answer key. The real test is the 9/3 Nature of Science Test already in
`SUGGESTED_ASSESS`.

**Two units, one builder** (`tools/builders/build_sci_nos.py`):

- **`unit-sci-nos-practice`** — the paper transcribed VERBATIM as a
  `guide:true` unit (which is `prep` for free), `order:4`, shelving right
  after Reading Scales. The builder asserts the answer string
  `CBACDBCBCABCBCBCDAD` against the key before it will write the file, and
  never calls `_balance()` — option order is the paper's, letter for letter.
  Every one of the 19 carries a hand-verified `variant` for the rescue
  round, built on a different experiment (salt water and melting ice).
- **`unit-sci-nos-test`** — the parallel: same skills, entirely fresh
  scenario, ordinary shuffled quiz, `prep:true`, `order:5`, `round:20` so
  it sits like a test. Two questions carry a real `graph` (the double line
  graph of ice mass over time), so the plotted data and the answer agree by
  construction; a labelled point at the end of each line names it, because
  `renderGraph` has no legend.

**Reading the material.** The student copy has a clean text layer, but
Drive's `read_file_content` returned it with classic multi-column reflow —
Q4's stem followed by Q5's and Q6's options. `pypdfium2`'s own
`get_textpage()` gave the same PDF in true reading order, which is how the
option order was confirmed. The key is a pure scan with the answers circled
in pink marker and has no text layer at all; it was rendered page by page
and read as images. **All 19 answers were independently re-derived first
and matched the circled key with zero discrepancies.**

**The teacher's margin notes are the best content in the folder** and are
on the flashcards as written: "no opinions, natural world", "independent
comes after *How does*", "dependent = what we measure", "should do
multiple!", "scientists use the metric system", "know cm too", "know bar
graphs too", "numbers!", "descriptive!", "answer question and give
evidence". They read as a list of exactly what the real test will ask.

**Honest-scope calls, same as `science-scales.json`:** eight of the paper's
questions hang on a picture (a prism, a thermometer, a graduated cylinder,
a ruler, three graphs, four diagrams). The guide unit does not reproduce
them — the paper is beside her, that is what "I did it on paper" means, and
a redrawn graph that read 33 where the paper read 34 would make a right
answer wrong. The walkthrough describes what each picture showed. The study
test asks the same skills without pictures: the instrument questions state
the scale in words ("labelled every 10 mL, five spaces between") and test
the divide-the-gap step, and the diagram question asks what MAKES a diagram
scientific. The study test's cylinder has 2 mL spaces where the paper's had
1 mL, on purpose.

**Three checker rules learned to recognise a guide unit**, each for the
same reason — a guide transcribes a real paper and its options never
shuffle — and each scoped to the MAIN question only, since variants are
ours and run in the shuffled rescue round:

- `POSITIONAL` no longer fires on a guide's main question. Q5's real answer
  is "All of the above", and it stays.
- A guide's main question may carry **2 options**: Q11 is True/False on the
  paper, and `SCREENS.guideentry` draws its letters from `opts.length`, so
  it renders A/B correctly. Inventing two extra options would change what
  she is entering.
- The length-bias warning skips a guide's main options: they are the
  teacher's words and editing them to even up lengths breaks the
  letter-for-letter contract. This retired 10 permanently-unfixable
  warnings on Ad Astra's three guides too; the checker file is identical in
  both repos and was copied across.

The checker still caught three real bugs of mine on the first build — a
study-test stem opening "In the same melting-ice experiment" (the
back-reference rule), and "Only the last option does both jobs" in a
walkthrough step (positional, in BOTH the study test and a variant). Fixed
by restating, not by exempting.

`tools/test_sci_nos.js` (17 checks): the key letter-for-letter, options
rendering unshuffled on the guide, the entry grid with A/B on row 11 and
A/B/C/D on the other 18, a realistic 14-of-19 paper pass grading to one
`paper:true` log with five misses on the ladder, the rescue round asking
exactly five fresh variants, the study test's 20-question round playing
with a graph actually rendered mid-round, and both stops gold-ringed in
order after Reading Scales.

### The question that answered itself (v121)

Chris: *"for the wordly wise quizzes, sometimes the questions give the
answer. it tells what the word means, even if the question asks for the
opposite it should not explain what the word means."*

He is right, and it was worse than one or two items: **all 19 questions** in
`wordly-wise-5-01-syn.json` glossed the word in their own stem — "Which word
means the OPPOSITE of accustom (to get used to something)?" Two of them
printed the answer outright, because for a synonym question the gloss *is*
the answer: "concept (a general idea)?" → `idea`, "jostle (to push or
shove)?" → `shove`. The unit tested nothing.

Scoped before fixing: **Sedona's seven Book 9 lessons are clean** (they use
context sentences, usage discrimination and analogies), and so are River's
other five Wordly Wise lessons. This was one unit — the one built in v102,
where the questions were generated off the syn/ant table mechanically.

Four leaks, not one, and the second is the half that would have been missed:

- **The gloss.** Gone from every stem. Where a word has two senses in play,
  the sense now comes from a part-of-speech tag (`As an ADJECTIVE, which word
  means the OPPOSITE of patient?`) or a usage sentence (`Grandma retired at
  nine and slept soundly.`) — **context, never a definition**. `retire` needed
  this in both directions: q12 asks the go-to-bed sense, q18 the stop-for-the-
  day sense.
- **The distractors were filler.** `accustom` offered *ignore, burly,
  pedestrian, companion* — three of them not even the right part of speech, so
  stripping the gloss alone would have left an item still answerable without
  knowing the word. Every option is now the same part of speech as the answer,
  and each holds a different real relationship: the word's own **synonym** sits
  in every antonym question (and its antonym in every synonym question), so
  she has to read which was actually asked. Each was checked for not
  accidentally also being correct.
- **All 19 hints were the same sentence** — "Think about what X means, then
  find its match" — priced at −5 XP for saying nothing. They are now etymology
  hooks where a real one exists (`ped-` = foot, as in pedal; `com-` + `panis` =
  someone you share bread with; `ob-` + *stare* = standing in your way) and a
  named warning about the trap where one does not.
- **Every `ex.main` was the bare answer word** ("**Ignore.**"), against the
  standing rule that it explains *why* the answer is right. All rewritten.

`tools/test_ww_syn.js` asserts the stems are bare, that no option appears
inside its own stem, that the boilerplate hint is gone and that explanations
say why — then plays a full round and re-checks the shelf position.
**Verified by running it against the pre-fix file**, where it fails on all
four counts including q13/q17 printing their own answers; a guard that passes
on the bug it was written for is not a guard.

Shipped with `libv:1` and `updatedAt` three hours back, so the fix wins the
merge whether or not the unit had been approved. The general rule went into
ad-astra/CLAUDE.md's shared **Content rules**, since it binds both apps.

### The Lemonade Crime · Ch. 6–9 (v119)

Second of three reading companions (`unit-lc2`, `content/lemonade-crime-2.json`),
built from "Lemonade Crime Chapters 6-9.pdf" that Chris uploaded 2026-08-30.
26 cards, 15 questions, spoiler-bounded at the end of chapter 9 — the
courtroom is built but the trial has not started. Shelves behind Ch. 1–5 on
the existing "The Lemonade Crime" spine by plain title sort; no `order` field
needed (`Ch. 1–5` before `Ch. 6–9`, verified).

- **The four chapter-title words carry the book's own definitions, quoted
  verbatim as `passage` plates** — impartial, due diligence, defense, bona
  fide — matching how unit 1 handled *fraud*. They were transcribed from the
  source text including the pronunciation respellings, not reworded.
- **`tools/builders/build_lemonade_2.py` is the first builder for a book
  unit.** `unit_common.build()` does not know about `book:true`, so the
  script assembles the unit dict itself and only borrows `card()`, `q()` and
  `_balance()`. Passages are attached AFTER `_balance()` by question id —
  `_balance` swaps options inside a question but never reorders questions, so
  ids stay stable.
- The two ungraded ponder cards ask the questions the chapters actually
  raise and refuse to answer: whether the trial is fair now that Scott has a
  grownup lawyer and Evan has his little sister, and whether Paul and Ryan
  are bad friends for going to Scott's house without ever saying Scott is
  innocent.
- `parentNote` flags one thing worth a grown-up's eye: the trial only works
  because the grownups do not know about it, which the book states outright
  as a playground rule. It is presented as something the plot depends on,
  never as advice.

### The rest of the book — Ch. 10–13 and Ch. 14–16 (v120)

`unit-lc3` ("The Trial", 21 cards / 15 questions) and `unit-lc4` ("Amends",
22 cards / 15 questions) finish the book at four parts. lc3 stops at the
verdict; lc4 covers chapters 14–16 and carries **`capstone:true`** — the
series has a real, defined end, so the crest can be earned and never
un-earned. All four shelve in chapter order on plain title sort.

**Getting the source out of Drive is the story here, and the fix is worth
remembering.** "Lemonade Crime Chapters 10-14.pdf" was unreadable two ways
at once: a pure image scan (`read_file_content` returned 66 empty page
tables) AND 18 MB, over `download_file_content`'s 10 MB cap — so it could
be neither text-extracted nor pulled down and rendered with `pypdfium2`.
Either problem alone is survivable; together they leave no path. `copy_file`
takes no target mimeType, so Claude cannot force a Docs conversion itself.

> **The unblock: ask Chris to right-click the PDF in Drive → Open with →
> Google Docs.** Drive runs its own OCR server-side and produces a Doc that
> `read_file_content` reads perfectly. Ten seconds of his time, no splitting
> and no re-export. Use this for ANY scanned source over the download cap
> rather than asking him to cut the file up.
>
> The OCR'd Doc also turned out to contain chapters 10 through **16** —
> the whole rest of the book, not the 10–14 the filename claimed — which is
> why both remaining units shipped at once. Check what a converted file
> actually contains rather than trusting its name.

- One OCR gap is real and was handled honestly: around p. 110, two of
  Megan's three yes/no questions to Jack are lost. Only her legible first
  question ("did you ever see the money in Evan's shorts pocket?") is used;
  nothing was invented to fill the hole.
- lc4's `parentNote` flags three things rather than smoothing them: chapter
  14 is genuinely rough (Evan hurts Scott knowingly and the unit does not
  excuse him), the grandmother's two-part answer about Jessie's lie is the
  best moral guidance in the book and is worth reading aloud, and Scott's
  "'Cause you had it, I guess" is left unexplained because the book itself
  refuses to explain it.
- **lc4 should only be approved once she has finished the book** — it covers
  the ending, including who returns the money.

`tools/test_lemonade2.js` covers shelving order, the book-unit rules (no
Beat the clock), a full quiz round, the passage plate actually rendering,
and the 26-card deck. The passage check walks whole ROUNDS rather than
single questions — a 5-question round drawn from 15 need not contain one of
the four, and the first version of the test failed for exactly that reason
rather than for a real bug.

### Tutoring on Today (v118 / Ad Astra v140, both apps)

Ported in step — same engine as Ad Astra's section of the same name.
`TUTORING` here holds River's real slots as read from the calendar (one-time
read granted 2026-08-30, at Chris's request that it "show up in the daily
briefing"): **Mondays and Tuesdays, 3:00–5:00 pm**, weekly. Keyed on the real
weekday, not `shownDate` — River's rotating-schedule Today can show a future
school day's line-up when today is not one, but tutoring is her own
appointment and runs regardless (verified against Labor Day, a Monday with
no school, in `tools/test_tutoring.js`). See ad-astra/CLAUDE.md's section of
the same name for the full reasoning: read-once not live-synced, times only
and no tutor name (same privacy rule as `STUDENT_HOURS`), and why it is a
separate card from Student hours rather than folded into it.

### The lesson you meant (v115 / Ad Astra v138, both apps)

The lesson-picking fixes from the UX review — a tapped map stop now
visibly selects (full-row wash, accent title), the opened card scrolls into
view instead of hiding below the map, and the check-in screen names the
unit about to be quizzed. Engine, identical in both apps; see
ad-astra/CLAUDE.md's section of the same name for the full reasoning and
the contrast measurements. `tools/test_shelfpick.js` is the same test file.

### Fall clubs (v114, THIS APP ONLY)

Chris asked for River's app to get the same club picker Sedona's has —
options she's eligible for in 4th grade, cost, a summary, and a way to star
or register. Ported the whole engine from ad-astra/CLAUDE.md's "Signed up,
and the club on the day" (v99): `CLUBS`/`CLUBS_CLOSED`, `clubPicks`/
`clubState`/`setClubState` (the same want/reg/null three-state map),
`clubMeetsOn`'s day+time+cadence placement rule, `clubDetails()`,
`SCREENS.clubs`, and the registered-club-joins-the-day `.evt.club` row on
Today. Same rules apply here as there — a star is a wish, registering is a
fact, only genuinely-derivable clubs land on the schedule, nothing is placed
on a guess.

- **Built from the real BCPS Fall 2026 Extracurricular Catalog** (ParentSquare,
  uploaded 2026-08-29). 11 clubs list 4th grade in their range; the other 5 —
  Code Ninjas' K-2 Scratch club, Snapology, Jr. Ballers (2nd only), Spanish
  Club, and the Friday Chess Emporium session — go in `CLUBS_CLOSED` so the
  screen and the real catalog reconcile row for row, same as Sedona's does.
- **Registration window (8/31–9/4/26) and the club start/end range
  (9/14–9/18 through 11/16–11/20) come straight from the catalog**, but the
  catalog never states a cadence in words the way ASL Club's teacher email
  did for Sedona. Every club here is marked `freq:'weekly'` on the reasoning
  that a ~9-week span between a stated start range and end range is exactly
  what a once-a-week club produces — flagged in case that assumption is
  wrong and a real per-club cadence surfaces later.
- **All 11 clubs run 3:30–4:30 pm**, stated outright in the catalog, so the
  screen's hintline says it once instead of repeating the same time on every
  row (same audit finding Sedona's screen already fixed).
- **The `screen:'clubs'` CAL.events door** ("Fall club registration",
  8/31–9/4) is the only way in, same as Ad Astra — no persistent Settings
  link either, matching parity rather than improving on it unasked.

> ⚠️ **`SCREENS.clubs = function(...)` was first written above `const
> STUDENT_HOURS`, which sits well before `const SCREENS = {}` is declared
> further down the file.** Assigning a property onto `SCREENS` before that
> `const` executes throws a temporal-dead-zone `ReferenceError` at BOOT —
> which aborts the whole top-level script before `loadLocal()` ever runs,
> so `DATA` itself never gets assigned. Every test failed with `DATA is not
> defined`, which reads like a totally unrelated data-loading bug and cost
> real time chasing before the actual cause (a misplaced `SCREENS.clubs`
> assignment 1,300 lines above `SCREENS`'s own declaration) turned up. Fixed
> by moving only the `SCREENS.clubs = ...` assignment down next to the other
> `SCREENS.*` definitions (right after `SCREENS.flagged`); `CLUBS`/
> `CLUBS_CLOSED`/`clubDetails()` and the rest of the plain data/helpers stay
> up with `STUDENT_HOURS`, since they never reference `SCREENS` and have no
> ordering constraint. **Any new top-level `SCREENS.xxx = function(){}`
> assignment must physically sit after `const SCREENS = {}`.**
- `tools/test_clubs.js` covers the three-state map, `clubMeetsOn`'s weekly
  placement (using Challenge Island's Monday cadence in place of Sedona's
  ASL Club, which has a real per-date schedule this catalog doesn't provide),
  a registered club joining Today and a starred one not, the clubs screen
  separating signed-up from starred, and the registration event appearing
  in its window.
