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
