# -*- coding: utf-8 -*-
"""River's Unit 5 — Lessons 4, 5 and 7 (enVision grade-5, Topic 5: dividing
whole numbers by two-digit divisors).

Same shape as Lessons 1 to 3 (build_math_unit5.py): one lesson per unit record,
shelved on the `Unit 5` book with `series`, `round:10`, no `order`, no `prep`.
Source: her `5-4_`, `5-5_` and `5-7_ Student Edition Practice.pdf` pages
(Drive, uploaded 11/1), read for what they ASK — never for her answers.
There is no 5-6 page in the folder, so there is no Lesson 6 here.

The pages print no lesson name, only each lesson's Essential Question. Each
title is that question shortened into the skill it names:
  5-4 "How Can You Use Partial Quotients to Solve Division Problems?"
  5-5 "How Can You Record Division with a Two-Digit Divisor?"
  5-7 "What Are Some Different Strategies I Can Use to Solve a Division Problem?"

Nothing is worked by hand. Every quotient and remainder is computed below, and
every WRONG option on a "What is a ÷ b?" question comes from a named slip
(a remainder left off, a remainder too big to keep, a partial quotient left
out, two partial quotients written side by side, a zero lost or added, the
remainder written into the quotient). Each slip is asserted NOT to be a true
answer. `use()` refuses every division printed on any Unit 5 practice page,
5-1 to 5-7: they were read for shape only.

This is a separate builder so Lessons 1 to 3 are not rebuilt (and re-stamped)
when these are. Its BOOK set repeats theirs and adds the new pages.
"""
import json, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unit_common as U

D, X, MINUS = '÷', '×', '−'

def f(n): return '{:,}'.format(n)

# Every division printed on the Unit 5 practice pages, as (dividend, divisor).
BOOK = {
    # 5-1
    (18000, 90), (10000, 50), (210, 30), (12000, 40), (480, 60), (15000, 30),
    (8100, 90), (2800, 70), (30000, 50), (1800, 60), (560, 70), (360, 60),
    (6000, 50), (24000, 60), (2000, 20), (6300, 90), (240, 10), (21000, 30),
    (2500, 50), (72000, 90), (56000, 70), (1000, 10), (45000, 90), (42000, 70),
    (64000, 80), (32000, 80), (27000, 90), (480, 80), (2400, 80), (420, 60),
    (4200, 6), (4200, 60), (4200, 600), (180, 90), (1800, 90),
    # 5-2
    (159, 75), (160, 80), (230, 75), (425, 20), (287, 42), (320, 11), (208, 72),
    (554, 62), (815, 23), (2491, 48), (412, 84), (288, 37), (2964, 73),
    (228, 19), (1784, 64), (7260, 83), (2280, 12), (485, 92), (540, 61),
    (1710, 32), (2740, 67), (4322, 81), (5700, 58), (7810, 44), (6395, 84),
    (180, 20), (270, 32), (360, 50), (817, 91), (3128, 55), (225, 12), (617, 30),
    (400, 80), (280, 40), (2800, 70),
    # 5-3
    (360, 20), (408, 12), (154, 11), (156, 12), (682, 22), (143, 11), (182, 13),
    (342, 38), (720, 16), (608, 19), (752, 47), (375, 25), (576, 24), (210, 15),
    (714, 21), (391, 23), (512, 16), (286, 22),
    # 5-4 (new, 11/1)
    (375, 15), (233, 11), (220, 11), (210, 15), (286, 13), (575, 25), (960, 32),
    (247, 19), (631, 14), (132, 11), (845, 21), (304, 16), (480, 32), (715, 23),
    (660, 30), (731, 43), (610, 16), (969, 19), (272, 8), (325, 13), (500, 20),
    (1400, 4), (704, 32), (420, 12), (1078, 49), (875, 25), (1890, 30),
    (7700, 22), (1430, 65), (14000, 40), (4500, 50),
    # 5-5 (new, 11/1)
    (258, 12), (250, 10), (200, 12), (196, 14), (766, 80), (304, 19), (593, 61),
    (360, 11), (544, 17), (250, 50), (867, 68), (966, 23), (492, 79), (375, 40),
    (980, 60), (660, 48), (3200, 10), (975, 15), (975, 72), (500, 30), (500, 40),
    (500, 50), (335, 40), (360, 40), (365, 40), (409, 40), (415, 40),
    (670, 60), (290, 60), (920, 60), (670, 48), (290, 48), (920, 48),
    # 5-7 (new, 11/1)
    (3720, 15), (3000, 15), (4500, 15), (4618, 32), (4500, 30), (452, 21),
    (378, 54), (664, 83), (761, 5), (510, 30), (7704, 24), (7830, 33),
    (3136, 64), (6253, 71), (3300, 12), (3300, 18), (3300, 24), (9690, 34),
    (4600, 10), (966, 21), (2385, 53), (946, 43), (2116, 46),
}
USED = set()

def use(a, b):
    """Every division a question asks goes through here, so none of the
    practice pages' own problems can slip back in."""
    assert (a, b) not in BOOK, ('reuses the practice page', a, b)
    USED.add((a, b))
    return a // b, a % b

def fmt(qt, r):
    return f(qt) + (' R%d' % r if r else '')

def valid(a, b, qt, r):
    """True only for the real answer: quotient × divisor + remainder = dividend,
    with a remainder smaller than the divisor."""
    return qt * b + r == a and 0 <= r < b

def opts4(ans, *wrong):
    o = [ans] + list(wrong)
    assert len(o) == 4 and len(set(o)) == 4, o
    return o

# ── Named slips. Each returns (quotient, remainder) as the slip would write it.
def s_dropped(a, b):        # the remainder left off
    qt, r = divmod(a, b); assert r; return qt, 0
def s_short(a, b):          # stopped one group short: remainder as big as the divisor
    qt, r = divmod(a, b); return qt - 1, r + b
def s_over(a, b):           # one group too many: the last subtraction would go below zero
    qt, r = divmod(a, b); return qt + 1, 0
def s_extra_zero(a, b):     # a zero too many in the quotient
    qt, r = divmod(a, b); return qt * 10, r
def s_lost_zero(a, b):      # skipped the zero inside the quotient
    qt, r = divmod(a, b); s = str(qt)
    assert '0' in s[1:]; i = s.index('0', 1)
    return int(s[:i] + s[i + 1:]), r
def s_missing(a, b):        # left the biggest partial quotient out of the sum
    qt, r = divmod(a, b); s = str(qt)
    assert len(s) >= 2 and s[1] != '0'; return int(s[1:]), r
def s_side(a, b):           # wrote the partial quotients next to each other: 20 and 6 → 206
    qt, r = divmod(a, b); assert 10 <= qt < 100 and qt % 10
    return int(str(qt // 10 * 10) + str(qt % 10)), r
def s_rem_in(a, b):         # wrote the remainder into the quotient: 12 R5 → 125
    qt, r = divmod(a, b); assert r; return int(str(qt) + str(r)), 0

NAMES = {s_dropped: 'the remainder left off',
         s_short: 'one group short, which leaves a remainder too big to keep',
         s_over: 'one group too many',
         s_extra_zero: 'a zero too many',
         s_lost_zero: 'the zero in the quotient skipped',
         s_missing: 'a partial quotient left out of the sum',
         s_side: 'the partial quotients written side by side',
         s_rem_in: 'the remainder written into the quotient'}

def chunks(qt):
    """The place-value partial quotients of qt: 236 → [200, 30, 6]."""
    s = str(qt); n = len(s)
    return [int(c) * 10 ** (n - 1 - i) for i, c in enumerate(s) if c != '0']

def pq_steps(a, b):
    """Partial-quotient steps, one place-value chunk at a time."""
    qt, r = divmod(a, b); left = a; out = []
    ch = chunks(qt)
    for c in ch:
        left -= b * c
        out.append('Take away %d groups of %d: %s %s %s = %s left.' % (c, b, f(left + b * c), MINUS, f(b * c), f(left)))
    assert left == r
    if r: out.append('%d is less than %d, so %d is the remainder.' % (r, b, r))
    if len(ch) > 1:
        out.append('Add the partial quotients: %s = %s.' % (' + '.join(f(c) for c in ch), f(qt)))
    out.append('Check: %d %s %s%s = %s.' % (b, X, f(qt), (' + %d' % r) if r else '', f(a)))
    assert 3 <= len(out) <= 6, (a, b, out)
    return out

def long_steps(a, b):
    """The written steps of long division with a two-digit divisor."""
    digits = str(a); out = []; cur = 0; qd = ''; started = False
    for i, ch in enumerate(digits):
        cur = cur * 10 + int(ch)
        if not started and cur < b and i < len(digits) - 1:
            continue
        if not started:
            out.append('%d does not fit into %s, so start with %d.' % (b, digits[:i], cur)
                       if i > 0 else 'Start with %d.' % cur)
        started = True
        k = cur // b; qd += str(k)
        if i < len(digits) - 1:
            nxt = (cur - k * b) * 10 + int(digits[i + 1])
            tail = ' Bring down the %s to make %d.' % (digits[i + 1], nxt)
        else:
            tail = ''
        if k == 0:
            out.append('%d is less than %d, so write 0 in the quotient.%s' % (cur, b, tail))
        else:
            out.append('%d %s %d is %d: %d %s %d = %d, and %d %s %d = %d.%s' % (
                cur, D, b, k, k, X, b, k * b, cur, MINUS, k * b, cur - k * b, tail))
        cur -= k * b
    qt, r = divmod(a, b)
    assert int(qd) == qt and cur == r, (a, b)
    out.append('Check: %d %s %s%s = %s.' % (b, X, f(qt), (' + %d' % r) if r else '', f(a)))
    assert 3 <= len(out) <= 6, (a, b, out)
    return out

def div_q(lv, a, b, hint, tip, slips, steps_fn):
    """A plain 'What is a ÷ b?' question. Every wrong option is a named slip,
    asserted not to be a true answer."""
    qt, r = use(a, b)
    ans = fmt(qt, r)
    vals = [fn(a, b) for fn in slips]
    for v in vals: assert not valid(a, b, *v), (a, b, v)
    wrong = [fmt(*v) for v in vals]
    why = '; '.join('%s is %s' % (w, NAMES[fn]) for w, fn in zip(wrong, slips))
    return (lv, 'What is %s %s %d?' % (f(a), D, b), opts4(ans, *wrong), 0, hint, steps_fn(a, b),
            '**%s.** Check: %d %s %s%s = %s. The wrong answers come from real slips: %s.' % (
                ans, b, X, f(qt), (' + %d' % r) if r else '', f(a), why), tip)

def one_of(target, exprs):
    """Exactly one of the (a, b) divisions comes out to target (a pair (q, r))."""
    hits = [e for e in exprs if divmod(*e) == target]
    assert len(hits) == 1 and hits[0] == exprs[0], (target, exprs)
    for e in exprs: use(*e)
    return ['%s %s %d' % (f(a), D, b) for a, b in exprs]

CLS, APP, SERIES = 'math', 'wayfinder', 'Unit 5'
SRC = 'enVision Topic 5 Student Edition practice pages — dividing by two-digit divisors (Drive)'

def go(n, title, cards, qs, summary, why, objs, note, nxt):
    C, Q = [], []
    for a in cards: U.card(C, *a)
    for a in qs: U.q(Q, *a)
    slug, uid = 'math-u5-l%d' % n, 'unit-m5u%d' % n
    U.build(APP, C, Q, uid, '%s · Lesson %d: %s' % (SERIES, n, title), CLS,
            summary, why, objs, note, nxt, 'content/%s.json' % slug,
            'Lesson 5-%d Student Edition practice pages (Drive)' % n, SRC,
            offset_hours=3, round_=10)
    fp = '%s/content/%s.json' % (U.REPO, slug)
    j = json.load(io.open(fp, encoding='utf-8'))
    rec = j['records'][uid]
    rec['series'] = SERIES
    rec['libv'] = 1
    rec['quarter'] = 2
    io.open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))

# ══ Lesson 4 · How Can You Use Partial Quotients to Solve Division Problems? ══
use(486, 18); assert divmod(486, 18) == (27, 0) and 18 * 20 == 360
use(527, 24); assert divmod(527, 24) == (21, 23) and 24 * 20 == 480 and 24 * 30 == 720
use(525, 15); assert divmod(525, 15) == (35, 0) and 15 * 30 + 15 * 5 == 525 and 15 * 10 * 3 + 15 * 5 == 525
use(672, 24); assert divmod(672, 24) == (28, 0)
use(504, 12); assert 504 // 12 == 42 and 42 // 2 == 21 and 504 % 12 == 0
use(713, 23); assert divmod(713, 23) == (31, 0) and 700 // 20 == 35
use(638, 22); assert divmod(638, 22) == (29, 0) and 22 * 20 == 440 and 22 * 9 == 198 and 638 - 440 == 198
use(470, 18); assert divmod(470, 18) == (26, 2) and 25 * 18 + 20 == 470
Q45 = one_of((45, 0), [(1080, 24), (10800, 24), (1170, 13), (1035, 45)])
assert 10800 // 24 == 450 and 1170 // 13 == 90 and 1035 // 45 == 23

L4 = [
 (1, 'To find 486 %s 18 with partial quotients, a student first takes away 18 %s 20 = 360. What does the 20 stand for?' % (D, X),
  ['20 groups of 18 have been taken away so far', 'There are 20 left over at the end',
   'The divisor has changed from 18 to 20', 'The final answer is exactly 20'], 0,
  'A partial quotient counts groups of the divisor.',
  ['Each partial quotient counts how many groups of 18 are taken away.', '18 %s 20 = 360, so 20 groups of 18 are gone.' % X,
   '486 %s 360 = 126 is still left to share.' % MINUS, 'More groups come next, so 20 is only part of the answer.'],
  '**20 groups of 18 have been taken away.** 126 is still left, and 18 %s 7 = 126, so the full answer is 20 + 7 = 27.' % X,
  'A partial quotient is a part of the answer, not the whole of it.'),
 (1, 'After you finish taking away groups, how do you find the quotient?',
  ['Add all the partial quotients together', 'Write the partial quotients next to each other',
   'Multiply the partial quotients together', 'Keep only the biggest partial quotient'], 0,
  'Each partial quotient is a number of groups. How do you find the total number of groups?',
  ['Each partial quotient says how many groups you took away that time.', 'The quotient is the total number of groups.',
   'So you add them: 20 + 5 = 25, not 205.'],
  '**Add all the partial quotients.** Each one is a count of groups, and the quotient is the total count.',
  'Adding, not writing side by side, is what makes 20 and 5 into 25.'),
 (1, 'For 527 %s 24, which first partial quotient takes away the most without going over?' % D,
  ['20, because 24 %s 20 = 480' % X, '30, because 24 %s 30 = 720' % X,
   '2, because 24 %s 2 = 48' % X, '200, because 24 %s 200 = 4,800' % X], 0,
  'Try multiplying 24 by tens: 10, 20, 30.',
  ['24 %s 20 = 480, which is less than 527.' % X, '24 %s 30 = 720, which is more than 527.' % X,
   '2 fits, but it takes away far less than 20 does.', 'So 20 is the best first chunk.'],
  '**20.** 24 %s 20 = 480 fits under 527, and 30 groups would go over. 527 %s 24 = 21 R23.' % (X, D),
  'Bigger chunks mean fewer steps, as long as they fit.'),
 (1, 'When do you stop taking away groups in partial quotients?',
  ['When what is left is smaller than the divisor', 'When you have taken away exactly ten groups',
   'When what is left is smaller than 10', 'When you reach a number that ends in zero'], 0,
  'Could another whole group still fit?',
  ['Keep going while at least one more group fits.', 'Once what is left is smaller than the divisor, no group fits.',
   'What is left then is the remainder.'],
  '**When what is left is smaller than the divisor.** No more whole groups fit, so what is left is the remainder.',
  'A remainder that is as big as the divisor means you stopped too early.'),
 div_q(2, 416, 16, 'Try 16 %s 20 first.' % X, 'Add the partial quotients; never write them side by side.',
       [s_side, s_missing, s_over], pq_steps),
 div_q(2, 703, 19, 'Try 19 %s 30 first.' % X, 'Check: your answer %s 19 must make 703.' % X,
       [s_side, s_missing, s_over], pq_steps),
 div_q(2, 562, 17, 'Take away 17 %s 30, then see how many more fit.' % X, 'The remainder must be smaller than 17.',
       [s_dropped, s_short, s_missing], pq_steps),
 div_q(2, 845, 26, 'Take away 26 %s 30 first.' % X, 'Check: 26 %s your answer + the remainder must make 845.' % X,
       [s_dropped, s_short, s_side], pq_steps),
 (2, 'Two students find 525 %s 15. Lena takes away 15 %s 30, then 15 %s 5. Omar takes away 15 %s 10 three times, then 15 %s 5. Who is right?' % (D, X, X, X, X),
  ['Both, because 30 + 5 and 10 + 10 + 10 + 5 both make 35', 'Only Lena, because she used fewer chunks to get there',
   'Only Omar, because every chunk has to be a group of 10', 'Neither, because the quotient is 305, not 35'], 0,
  'Add up each student\'s partial quotients.',
  ['Lena: 15 %s 30 = 450, then 15 %s 5 = 75, and 450 + 75 = 525.' % (X, X), 'Her quotient is 30 + 5 = 35.',
   'Omar: 150 + 150 + 150 + 75 = 525.', 'His quotient is 10 + 10 + 10 + 5 = 35.'],
  '**Both are right.** Any chunks that fit will work. Lena needed fewer steps, but both quotients are 35.',
  'There is more than one right way to choose partial quotients.'),
 (2, 'A library has 672 books to put on shelves, 24 books on each shelf. How many shelves does it fill?',
  ['28 shelves', '208 shelves', '20 shelves', '29 shelves'], 0,
  'Find 672 %s 24. Start with 24 %s 20.' % (D, X),
  ['24 %s 20 = 480, and 672 %s 480 = 192.' % (X, MINUS), '24 %s 8 = 192, and 192 %s 192 = 0.' % (X, MINUS),
   'Add the partial quotients: 20 + 8 = 28.', 'Check: 24 %s 28 = 672.' % X],
  '**28 shelves.** 20 + 8 = 28, and 24 %s 28 = 672. 208 writes 20 and 8 side by side, 20 leaves the 8 out, and 29 is one group too many.' % X,
  'Read the answer back into the story: 28 shelves of 24 books.'),
 (2, 'Which division has a quotient of 45?',
  Q45, 0,
  'Work out each one. Watch the zeros.',
  ['1,080 %s 24: 24 %s 40 = 960, and 24 %s 5 = 120, so 45.' % (D, X, X), '10,800 %s 24 has one more zero in the dividend, so it is 450.' % D,
   '1,170 %s 13 = 90.' % D, '1,035 %s 45 = 23.' % D],
  '**1,080 %s 24.** 24 %s 45 = 1,080. 10,800 %s 24 is 450, ten times as much, because the dividend has an extra zero.' % (D, X, D),
  '45 and 450 look alike. Multiply back to tell them apart.'),
 (3, 'A printer prints 504 pages in 12 minutes, at the same speed the whole time. How many pages does it print in 30 seconds?',
  ['21 pages', '42 pages', '252 pages', '84 pages'], 0,
  'First find the pages in one minute. How much of a minute is 30 seconds?',
  ['504 %s 12 = 42 pages each minute.' % D, '30 seconds is half a minute.', 'Half of 42 is 21.',
   'So it prints 21 pages in 30 seconds.'],
  '**21 pages.** 504 %s 12 = 42 pages a minute, and 30 seconds is half a minute. 42 stops after the first step, 252 halves all 504 pages, and 84 doubles instead of halving.' % D,
  'Two steps: divide to find one minute, then take half.'),
 (3, 'Kai found 713 %s 23 = 13. Which estimate shows that his answer is not reasonable?' % D,
  ['700 %s 20 = 35, so the answer should be close to 35, not 13' % D,
   '700 %s 20 = 35, so 13 is close enough to count as right' % D,
   '7 %s 2 is about 3, so an answer of 13 is about right' % D,
   '713 %s 23 = 690, so his answer of 13 must be right' % MINUS], 0,
  'Round to numbers that divide easily, then compare.',
  ['713 is close to 700, and 23 is close to 20.', '700 %s 20 = 35.' % D, '13 is far from 35, so it cannot be right.',
   'The real answer is 31: 23 %s 31 = 713.' % X],
  '**700 %s 20 = 35, so 13 is far too small.** The real quotient is 31, and 23 %s 31 = 713.' % (D, X),
  'Estimate first, and a wrong answer shows up before you even check it.'),
 (3, 'Zoe used partial quotients for 638 %s 22. She took away 22 %s 20 = 440, then 22 %s 9 = 198, and wrote 209. What went wrong?' % (D, X, X),
  ['She wrote 20 and 9 side by side; the quotient is 29', 'Her first chunk, 22 %s 20, was too big to take from 638' % X,
   'She should multiply the partial quotients: 20 %s 9 = 180' % X, 'Nothing went wrong, because 209 is the right quotient'], 0,
  'Check her answer: does 22 %s 209 make 638?' % X,
  ['638 %s 440 = 198, so her chunks are right.' % MINUS, 'Her partial quotients are 20 and 9.',
   'Added together, 20 + 9 = 29.', 'Check: 22 %s 29 = 638.' % X],
  '**She wrote them side by side.** The partial quotients add up to 20 + 9 = 29, and 22 %s 29 = 638. 22 %s 209 would be 4,598.' % (X, X),
  'Partial quotients are added, the same way partial products are.'),
 (3, 'Eli found 470 %s 18 = 25 R20. What should he fix?' % D,
  ['20 is more than 18, so one more group fits: 26 R2', 'Nothing, because 25 %s 18 + 20 = 470, so it checks out' % X,
   'He should drop the remainder and write just 25', 'The remainder must be 0, so the answer is exactly 26'], 0,
  'Compare the remainder with the divisor.',
  ['25 %s 18 = 450, and 470 %s 450 = 20.' % (X, MINUS), '20 is more than 18, so another group of 18 fits.',
   '20 %s 18 = 2 is left.' % MINUS, 'So 470 %s 18 = 26 R2.' % D],
  '**One more group fits: 26 R2.** His multiplication check works, but a remainder of 20 is bigger than the divisor, so he stopped too soon.',
  'The check and the remainder rule are two tests. An answer has to pass both.'),
]

go(4, 'Divide with Partial Quotients', [
 ('Partial quotients',
  '**Take away easy groups of the divisor, one chunk at a time, then add up how many groups you took.**\n'
  '• 486 %s 18: take away 20 groups (360), then 7 groups (126).\n'
  '• 20 + 7 = 27.' % D,
  'Chunk, subtract, repeat, then add.'),
 ('Easy chunks',
  '**Groups of 10, 20, 100 or 200 are the easiest to take away, because they multiply quickly.**\n'
  '• 24 %s 20 = 480 is easier than 24 %s 17.' % (X, X),
  'Tens and hundreds are friendly numbers.'),
 ('The biggest chunk that fits',
  '**Start with the biggest easy chunk that does not go over.**\n'
  '• 527 %s 24: 24 %s 20 = 480 fits, 24 %s 30 = 720 does not.' % (D, X, X),
  'Fewer chunks, fewer steps.'),
 ('Different chunks, same answer',
  '**Any chunks that fit will work; they all add up to the same quotient.**\n'
  '• 525 %s 15: 30 + 5, or 10 + 10 + 10 + 5. Both make 35.' % D,
  'There is more than one right path.'),
 ('Add the partial quotients',
  '**The quotient is the SUM of the partial quotients.**\n'
  '• 20 and 9 make 29, not 209.',
  'Plus, never side by side.'),
 ('The remainder',
  '**When what is left is smaller than the divisor, stop: that is the remainder.**\n'
  '• A remainder as big as the divisor means one more group fits.',
  'Smaller than the divisor, always.'),
 ('Check two ways',
  '**Estimate first, then multiply back: divisor %s quotient + remainder = dividend.**\n'
  '• 713 %s 23: 700 %s 20 = 35, so 31 is reasonable.\n'
  '• 23 %s 31 = 713.' % (X, D, D, X),
  'Close to the estimate, and exact when you multiply.'),
 ('Watch the zeros',
  '**A division with one more zero in the dividend has a quotient ten times as big.**\n'
  '• 1,080 %s 24 = 45, but 10,800 %s 24 = 450.' % (D, D),
  '45 and 450 look alike; they are not.'),
], L4,
 'Lesson 5-4 practice pages: using partial quotients to divide by two-digit divisors, with and without remainders, checking with estimation, and spotting divisions with the same quotient.',
 'Partial quotients let her divide with chunks she can do in her head. Long division, next, is the same idea written more tightly.',
 [('Use partial quotients to divide by a two-digit divisor', 'source'),
  ('Find the remainder and check that it is smaller than the divisor', 'source'),
  ('Use an estimate to check that a quotient is reasonable', 'source'),
  ('Tell divisions like 1,080 %s 24 and 10,800 %s 24 apart by their quotients' % (D, D), 'source')],
 'Built from the lesson 5-4 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The slip most worth a word is writing the partial quotients side by side (20 and 9 as 209 instead of 29); one question shows a student doing exactly that. Every other wrong option comes from a named slip too: a partial quotient left out of the sum, the remainder left off, or stopping one group short so the remainder is bigger than the divisor. One question mirrors the page\'s own trap of quotients like 35 and 350.',
 ('Biggest easy chunk, subtract, repeat, then add the chunks and multiply back.', 13))

# ══ Lesson 5 · How Can You Record Division with a Two-Digit Divisor? ════════
use(739, 31); assert divmod(739, 31) == (23, 26) and 31 <= 73 and 31 > 7
use(517, 64); assert divmod(517, 64) == (8, 5) and 64 > 51
use(437, 21); assert divmod(437, 21) == (20, 17) and 21 * 20 + 17 == 437
use(214, 36); assert divmod(214, 36) == (5, 34)
use(500, 45); assert divmod(500, 45) == (11, 5)
use(330, 14); assert divmod(330, 14) == (23, 8)
use(900, 38); assert divmod(900, 38) == (23, 26) and 23 < 25
use(627, 29); assert divmod(627, 29) == (21, 18) and 20 * 29 + 47 == 627
Q7R12 = one_of((7, 12), [(187, 25), (175, 25), (212, 25), (162, 25)])
assert divmod(175, 25) == (7, 0) and divmod(212, 25) == (8, 12) and divmod(162, 25) == (6, 12)

L5 = [
 (1, 'In 739 %s 31, where does the first digit of the quotient go?' % D,
  ['The tens place', 'The hundreds place', 'The ones place', 'The thousands place'], 0,
  'Does 31 fit into 7? Does it fit into 73?',
  ['31 does not fit into 7 hundreds.', '31 does fit into 73 tens.', 'So the first digit goes in the tens place.',
   '739 %s 31 = 23 R26, a two-digit quotient.' % D],
  '**The tens place.** 31 is bigger than 7, so start with 73 tens. The quotient has two digits: 23 R26.',
  'Where the first digit goes tells you how many digits the answer has.'),
 (1, 'How many digits will the quotient of 517 %s 64 have?' % D,
  ['One digit', 'Two digits', 'Three digits', 'Four digits'], 0,
  'Compare 64 with the first two digits, 51.',
  ['64 is bigger than 51, so it does not fit into 51 tens.', 'So start with all of 517.',
   '64 %s 8 = 512, so 517 %s 64 = 8 R5.' % (X, D)],
  '**One digit.** 64 does not fit into 51 tens, so the quotient starts in the ones place: 8 R5.',
  'Estimate: 64 %s 10 = 640 is more than 517, so the answer is less than 10.' % X),
 (1, 'A quotient is written 18 R7. What does the R7 tell you?',
  ['7 are left over after the equal groups are made', 'There are 7 equal groups in all',
   'The answer is 18.7, a little more than 18', 'You need 7 more groups to finish'], 0,
  'R stands for remainder.',
  ['18 is the number in each group, or the number of groups.', 'R means remainder.',
   'R7 means 7 are left over that do not make a full group.'],
  '**7 are left over.** The R stands for remainder: what is left when no more full groups fit.',
  'The remainder is always smaller than the divisor.'),
 (1, 'Which multiplication checks that 437 %s 21 = 20 R17?' % D,
  ['21 %s 20 + 17 = 437' % X, '21 %s 20 = 437' % X, '21 %s 17 + 20 = 437' % X, '20 + 21 + 17 = 437'], 0,
  'Divisor times quotient, then add the remainder.',
  ['21 %s 20 = 420.' % X, 'Add the remainder: 420 + 17 = 437.', 'That is the dividend, so the answer checks out.'],
  '**21 %s 20 + 17 = 437.** Divisor %s quotient + remainder gives back the dividend.' % (X, X),
  'Forgetting to add the remainder makes a right answer look wrong.'),
 div_q(2, 851, 23, '23 fits into 85 tens. How many times?', 'Each subtraction must leave less than 23.',
       [s_short, s_over, s_extra_zero], long_steps),
 div_q(2, 693, 27, 'Start with 69 tens %s 27.' % D, 'The remainder must be smaller than 27.',
       [s_dropped, s_short, s_rem_in], long_steps),
 div_q(2, 2486, 34, '34 does not fit into 24, so start with 248.', 'Estimate: 2,400 %s 30 = 80, so expect a two-digit answer.' % D,
       [s_dropped, s_short, s_extra_zero], long_steps),
 div_q(2, 5412, 52, '52 fits into 54 once. What happens when you bring down the 1?', 'Every digit you bring down gets a digit in the quotient, even a 0.',
       [s_lost_zero, s_dropped, s_short], long_steps),
 div_q(2, 845, 70, 'Think of 84 tens %s 7 tens to start.' % D, 'Write the remainder after the R; it is not another digit.',
       [s_rem_in, s_short, s_dropped], long_steps),
 (2, 'A school is taking 214 students on a trip. Each bus holds 36 students. How many buses does the school need?',
  ['6 buses', '5 buses', '34 buses', '5 R34 buses'], 0,
  'Find 214 %s 36. Then ask: can the leftover students stay behind?' % D,
  ['36 %s 5 = 180, and 214 %s 180 = 34.' % (X, MINUS), '214 %s 36 = 5 R34.' % D,
   'The 34 students left over still need a bus.', 'So the school needs 5 + 1 = 6 buses.'],
  '**6 buses.** 214 %s 36 = 5 R34, and the 34 left over need a bus too. 5 leaves them behind, 34 is the remainder, not the buses, and "5 R34 buses" is not a number of buses.' % D,
  'When everyone must fit, round the quotient up.'),
 (2, 'A gardener has 500 tulip bulbs and plants 45 in each flower bed. How many beds can she fill completely?',
  ['11 beds', '12 beds', '5 beds', '111 beds'], 0,
  'Find 500 %s 45. Is the leftover enough for a whole bed?' % D,
  ['45 %s 11 = 495.' % X, '500 %s 495 = 5 bulbs left over.' % MINUS, '5 bulbs cannot fill a bed of 45.',
   'So she fills 11 beds.'],
  '**11 beds.** 500 %s 45 = 11 R5. The 5 leftover bulbs do not fill a bed, so the answer is 11. 12 rounds up, 5 is the remainder, and 111 writes the remainder in as a digit.' % D,
  'When only full groups count, drop the remainder.'),
 (3, 'A store packs 330 apples into bags of 14. How many apples are left over after it fills as many bags as it can?',
  ['8 apples', '23 apples', '24 apples', '14 apples'], 0,
  'Find 330 %s 14. Which part of the answer is the leftover?' % D,
  ['14 %s 23 = 322.' % X, '330 %s 322 = 8.' % MINUS, '330 %s 14 = 23 R8.' % D, 'The question asks for the leftover apples: 8.'],
  '**8 apples.** 330 %s 14 = 23 R8. 23 is the number of bags, 24 rounds up, and 14 is the bag size. Here the remainder IS the answer.' % D,
  'Read the question: it asks for what is left, not how many bags.'),
 (3, 'A coach has 900 stickers to share equally among 38 players. Can each player get 25 stickers?',
  ['No, each player can get only 23', 'Yes, each gets 25 with some left over',
   'Yes, each gets 26 and none are left', 'No, each player can get only 2'], 0,
  'Find 900 %s 38, then compare with 25.' % D,
  ['38 %s 20 = 760, and 900 %s 760 = 140.' % (X, MINUS), '38 %s 3 = 114, and 140 %s 114 = 26.' % (X, MINUS),
   '900 %s 38 = 23 R26.' % D, '23 is less than 25, so no.'],
  '**No, only 23 each.** 900 %s 38 = 23 R26. For 25 each she would need 38 %s 25 = 950 stickers. 2 is the tens digit alone, which loses a place.' % (D, X),
  'Check: 38 %s 25 = 950 is more than 900, which says no right away.' % X),
 (3, 'Max divided 627 %s 29 and wrote 20 R47. What should he fix?' % D,
  ['47 is bigger than 29, so one more group fits: 21 R18', 'Nothing, because 29 %s 20 + 47 = 627, so it checks out' % X,
   'He should drop the remainder and write just 20', 'He should start again with a first guess of 29 %s 30' % X], 0,
  'Compare the remainder with the divisor.',
  ['29 %s 20 = 580, and 627 %s 580 = 47.' % (X, MINUS), '47 is bigger than 29, so another group fits.',
   '47 %s 29 = 18 left.' % MINUS, 'So 627 %s 29 = 21 R18.' % D],
  '**One more group fits: 21 R18.** His check works out, but a remainder of 47 is more than the divisor, so the ones digit was too small.',
  'If a subtraction leaves the divisor or more, the digit above it is too small.'),
 (3, 'Which division has a quotient of 7 R12?',
  Q7R12, 0,
  'Try each one: 25 %s 7 = 175. Which dividend is 12 more than that?' % X,
  ['25 %s 7 = 175.' % X, '175 + 12 = 187, so 187 %s 25 = 7 R12.' % D,
   '175 %s 25 = 7 with no remainder.' % D, '212 %s 25 = 8 R12, and 162 %s 25 = 6 R12.' % (D, D)],
  '**187 %s 25.** 25 %s 7 + 12 = 187. 175 forgets the remainder, and 212 and 162 are one group too many and one too few.' % (D, X),
  'Build the dividend: divisor %s quotient + remainder.' % X),
]

go(5, 'Record Division with Two-Digit Divisors', [
 ('Estimate first',
  '**Round to numbers that divide easily, so you know about how big the answer should be.**\n'
  '• 2,486 %s 34 is about 2,400 %s 30 = 80.' % (D, D),
  'A rough answer catches a wrong digit.'),
 ('Where the first digit goes',
  '**If the divisor fits into the first two digits, the quotient starts in the tens place. If not, it starts in the ones place.**\n'
  '• 739 %s 31: 31 fits into 73, so the quotient has two digits.\n'
  '• 517 %s 64: 64 does not fit into 51, so it has one digit.' % (D, D),
  'Find the first part the divisor fits into.'),
 ('Divide, multiply, subtract, bring down',
  '**The same four steps as with one-digit divisors, repeated for each digit.**\n'
  '• Divide: how many times does the divisor fit?\n'
  '• Multiply, subtract, then bring down the next digit.',
  'D, M, S, B, then again.'),
 ('Too small, try again',
  '**If a subtraction leaves the divisor or more, the digit you wrote is too small.**\n'
  '• 627 %s 29: writing 20 leaves 47, and 47 is more than 29, so it is 21.' % D,
  'What is left must be smaller than the divisor.'),
 ('A zero in the quotient',
  '**If a brought-down number is smaller than the divisor, write 0 and bring down the next digit.**\n'
  '• 5,412 %s 52 = 104 R4, not 14 R4.' % D,
  'Every digit you bring down gets a digit in the quotient.'),
 ('Write the remainder',
  '**The remainder goes after an R. It is never another digit of the quotient.**\n'
  '• 845 %s 70 = 12 R5, not 125.' % D,
  'R for remainder.'),
 ('What the remainder means',
  '**In a story, decide what the remainder means.**\n'
  '• Round up when everyone must fit (buses).\n'
  '• Drop it when only full groups count (full flower beds).\n'
  '• Sometimes the remainder is the answer (apples left over).',
  'Ask: what is the leftover in this story?'),
 ('Check with multiplication',
  '**Divisor %s quotient + remainder should give back the dividend.**\n'
  '• 21 %s 20 + 17 = 437, so 437 %s 21 = 20 R17.' % (X, X, D),
  'Undo it to check it.'),
], L5,
 'Lesson 5-5 practice pages: recording division with a two-digit divisor, step by step, with remainders and zeros in the quotient, and deciding what a remainder means in a word problem.',
 'This is the written method she will use for every division from here on, so the steps and the remainder rule need to be solid.',
 [('Divide by a two-digit divisor, recording each step', 'source'),
  ('Decide where the first digit of the quotient goes', 'source'),
  ('Find a remainder that is smaller than the divisor', 'source'),
  ('Decide what a remainder means in a word problem', 'source'),
  ('Check a quotient with multiplication', 'added')],
 'Built from the lesson 5-5 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The two slips most worth a word are a digit that is too small (so what is left is bigger than the divisor, as in 627 ÷ 29 written as 20 R47) and the remainder written into the quotient (12 R5 as 125). Three word problems cover the three things a remainder can mean: round up for buses, drop it for full flower beds, and the remainder as the answer for apples left over. The page itself asks what a remainder means, so those are marked as from the class material.',
 ('Estimate, then divide, multiply, subtract, bring down, and check.', 13))

# ══ Lesson 7 · What Are Some Different Strategies I Can Use to Solve a Division Problem? ══
use(2890, 17); assert 2890 // 17 == 170 and 17 * 100 <= 2890 < 17 * 200
use(5600, 80); assert 5600 // 80 == 70 and 56 // 8 == 7
use(4176, 36); assert 4176 // 36 == 116 and 36 * 100 <= 4176 < 36 * 1000
use(9216, 48); assert divmod(9216, 48) == (192, 0)
use(2880, 12); assert 2880 // 12 == 240 and 240 * 3 == 720 and 2880 * 3 == 8640
use(4560, 19); assert divmod(4560, 19) == (240, 0) and 4600 // 20 == 230
use(1250, 32); assert divmod(1250, 32) == (39, 2) and 38 * 32 + 34 == 1250
use(6422, 26); assert divmod(6422, 26) == (247, 0)
use(1000, 24); assert divmod(1000, 24) == (41, 16)
Q64 = one_of((64, 0), [(2752, 43), (2795, 43), (27520, 43), (2709, 43)])
assert 2795 // 43 == 65 and 27520 // 43 == 640 and 2709 // 43 == 63

L7 = [
 (1, 'Can a remainder be greater than the divisor?',
  ['No, because then at least one more group would fit', 'Yes, whenever the dividend is very large',
   'Yes, a remainder can be any number at all', 'No, because a remainder must always be zero'], 0,
  'If 30 are left and the divisor is 24, what could you still do?',
  ['A remainder is what is left when no more full groups fit.', 'If it were as big as the divisor, one more group would fit.',
   'So the remainder is always smaller than the divisor.'],
  '**No.** If what is left is as big as the divisor, another group fits, so you are not finished.',
  'A remainder of 0 is fine; a remainder bigger than the divisor is not.'),
 (1, 'The quotient of 2,890 %s 17 is between which two numbers?' % D,
  ['100 and 200', '10 and 20', '1,000 and 2,000', '200 and 300'], 0,
  'Try 17 %s 100 and 17 %s 200.' % (X, X),
  ['17 %s 100 = 1,700, which is less than 2,890.' % X, '17 %s 200 = 3,400, which is more than 2,890.' % X,
   'So the quotient is between 100 and 200.', 'In fact 2,890 %s 17 = 170.' % D],
  '**100 and 200.** 17 %s 100 = 1,700 and 17 %s 200 = 3,400, and 2,890 is between them. The quotient is 170.' % (X, X),
  'Multiplying by 10, 100 and 1,000 brackets the answer fast.'),
 (1, 'Which strategy is quickest for 5,600 %s 80?' % D,
  ['A basic fact and patterns: 56 %s 8 = 7, so the answer is 70' % D,
   'Partial quotients, taking away one group of 80 at a time',
   'Adding 80 over and over until the total reaches 5,600',
   'Long division, starting with 80 %s 1,000 = 80,000' % X], 0,
  'Both numbers end in zero. Which lesson used that?',
  ['Cover the zeros: 56 %s 8 = 7.' % D, '5,600 has two zeros and 80 has one, so one zero is left.',
   'So 5,600 %s 80 = 70.' % D, 'Check: 70 %s 80 = 5,600.' % X],
  '**A basic fact and patterns.** 56 %s 8 = 7, and one zero is left over, so 70. The other ways work too, but take much longer.' % D,
  'Pick the strategy that fits the numbers.'),
 (1, 'How many digits will the quotient of 4,176 %s 36 have?' % D,
  ['Three digits', 'Two digits', 'Four digits', 'One digit'], 0,
  'Compare with 36 %s 100 and 36 %s 1,000.' % (X, X),
  ['36 %s 100 = 3,600, which is less than 4,176.' % X, '36 %s 1,000 = 36,000, which is far more.' % X,
   'So the quotient is in the hundreds: three digits.', '4,176 %s 36 = 116.' % D],
  '**Three digits.** 36 %s 100 = 3,600 fits under 4,176, but 36 %s 1,000 does not, so the answer is in the hundreds: 116.' % (X, X),
  'Knowing the number of digits first catches a lost or extra zero.'),
 div_q(2, 3264, 24, 'Try 24 %s 100 first.' % X, 'Estimate: 3,000 %s 20 = 150, so expect a three-digit answer.' % D,
       [s_missing, s_short, s_over], pq_steps),
 div_q(2, 5890, 38, 'Take away 38 %s 100 first.' % X, 'Check: 38 %s your answer must make 5,890.' % X,
       [s_missing, s_extra_zero, s_over], pq_steps),
 div_q(2, 7365, 42, 'Take away 42 %s 100 first, then tens.' % X, 'The remainder must be smaller than 42.',
       [s_dropped, s_short, s_missing], pq_steps),
 div_q(2, 6147, 61, '61 fits into 61 once. What about the 4 that comes next?', 'A zero in the quotient holds a place.',
       [s_lost_zero, s_dropped, s_short], long_steps),
 (2, 'A stadium has 9,216 seats in sections of 48 seats each. How many sections are there?',
  ['192 sections', '92 sections', '193 sections', '1,920 sections'], 0,
  'Estimate first: 48 is close to 50. Then take away 48 %s 100.' % X,
  ['48 %s 100 = 4,800, and 9,216 %s 4,800 = 4,416.' % (X, MINUS), '48 %s 90 = 4,320, and 4,416 %s 4,320 = 96.' % (X, MINUS),
   '48 %s 2 = 96, and nothing is left.' % X, 'Add: 100 + 90 + 2 = 192.'],
  '**192 sections.** 48 %s 192 = 9,216. 92 leaves the 100 out, 193 is one group too many, and 1,920 has a zero too many.' % X,
  'Estimate: 10,000 %s 50 = 200, so 192 is reasonable.' % D),
 (2, 'Which division has a quotient of 64?',
  Q64, 0,
  'Multiply 43 %s 64 and compare.' % X,
  ['43 %s 64 = 2,752.' % X, 'So 2,752 %s 43 = 64.' % D, '2,795 %s 43 = 65, and 2,709 %s 43 = 63.' % (D, D),
   '27,520 %s 43 = 640, ten times as much.' % D],
  '**2,752 %s 43.** 43 %s 64 = 2,752. The others are one group more, one group fewer, and ten times as much.' % (D, X),
  'To find a dividend, multiply the divisor by the quotient.'),
 (3, 'A farm packs 2,880 eggs into cartons of 12 and sells each carton for $3. How much money does it make if it sells every carton?',
  ['$720', '$240', '$8,640', '$72'], 0,
  'First find the number of cartons. Then find the money.',
  ['2,880 %s 12 = 240 cartons.' % D, 'Each carton sells for $3.', '240 %s 3 = 720.' % X, 'So the farm makes $720.'],
  '**$720.** 2,880 %s 12 = 240 cartons, and 240 %s $3 = $720. $240 stops after the first step, $8,640 multiplies the eggs instead of the cartons, and $72 loses a zero.' % (D, X),
  'The price is per carton, so you need the cartons first.'),
 (3, 'Ana says 4,560 %s 19 = 24. Which estimate shows her answer is not reasonable?' % D,
  ['4,600 %s 20 = 230, so the answer should be in the hundreds' % D,
   '4,600 %s 20 is about 23, so 24 is close enough to be right' % D,
   '45 %s 19 is about 2, so 24 is about the right size' % D,
   '4,560 %s 19 = 4,541, so an answer of 24 must be right' % MINUS], 0,
  'Round 19 to 20 and 4,560 to a number 20 divides easily.',
  ['4,560 is close to 4,600, and 19 is close to 20.', '4,600 %s 20 = 230.' % D,
   '24 is about ten times too small.', 'The real answer is 240: 19 %s 240 = 4,560.' % X],
  '**4,600 %s 20 = 230, so the answer is in the hundreds.** The real quotient is 240. She lost a zero.' % D,
  'An estimate catches a missing zero before you multiply.'),
 (3, 'Ben found 1,250 %s 32 = 38 R34. What should he fix?' % D,
  ['34 is more than 32, so one more group fits: 39 R2', 'Nothing, because 32 %s 38 + 34 = 1,250' % X,
   'He should drop the remainder and write 38', 'He should write the remainder as a digit: 3,834'], 0,
  'Compare the remainder with the divisor.',
  ['32 %s 38 = 1,216, and 1,250 %s 1,216 = 34.' % (X, MINUS), '34 is more than 32, so another group fits.',
   '34 %s 32 = 2.' % MINUS, 'So 1,250 %s 32 = 39 R2.' % D],
  '**One more group fits: 39 R2.** His check adds up, but a remainder must be smaller than the divisor.',
  'A remainder bigger than the divisor means one digit is too small.'),
 (3, 'A museum guide leads tours of exactly 26 people. One month, 6,422 people took a tour, and every tour was full. How many tours ran?',
  ['247 tours', '47 tours', '248 tours', '246 tours'], 0,
  'Find 6,422 %s 26. Start with 26 %s 200.' % (D, X),
  ['26 %s 200 = 5,200, and 6,422 %s 5,200 = 1,222.' % (X, MINUS), '26 %s 40 = 1,040, and 1,222 %s 1,040 = 182.' % (X, MINUS),
   '26 %s 7 = 182, and nothing is left.' % X, 'Add: 200 + 40 + 7 = 247.'],
  '**247 tours.** 26 %s 247 = 6,422. 47 leaves out the 200, 248 is one too many, and 246 stops one group short.' % X,
  'Every tour was full, so the division comes out with nothing left.'),
 (3, 'A school needs at least 1,000 pencils. Pencils come in boxes of 24. How many boxes should it order?',
  ['42 boxes', '41 boxes', '16 boxes', '41 R16 boxes'], 0,
  'Find 1,000 %s 24. Will 41 boxes be enough?' % D,
  ['24 %s 40 = 960, and 1,000 %s 960 = 40.' % (X, MINUS), '24 %s 1 = 24, and 40 %s 24 = 16.' % (X, MINUS),
   '1,000 %s 24 = 41 R16, so 41 boxes give only 984.' % D, 'One more box is needed: 42.'],
  '**42 boxes.** 41 boxes hold 984 pencils, 16 short of 1,000, so the school needs one more box. 16 is the remainder, and "41 R16 boxes" cannot be ordered.',
  'When you need at least a certain amount, round up.'),
]
assert 41 * 24 == 984

go(7, 'Use Different Strategies to Divide', [
 ('Estimate first',
  '**Before you divide, find two numbers the quotient sits between.**\n'
  '• 2,890 %s 17: 17 %s 100 = 1,700 and 17 %s 200 = 3,400, so between 100 and 200.' % (D, X, X),
  'Bracket it with 10s, 100s and 1,000s.'),
 ('Patterns with zeros',
  '**When both numbers end in zeros, use a basic fact and count the zeros.**\n'
  '• 5,600 %s 80: 56 %s 8 = 7, so 70.' % (D, D),
  'Fact first, zeros second.'),
 ('Partial quotients with big chunks',
  '**For a big dividend, take away hundreds of groups first, then tens, then ones.**\n'
  '• 9,216 %s 48: 100, then 90, then 2, for 192.' % D,
  'Hundreds, tens, ones.'),
 ('Long division',
  '**Divide, multiply, subtract, bring down, one digit at a time.**\n'
  '• Write 0 when a brought-down number is too small: 6,147 %s 61 = 100 R47.' % D,
  'Every brought-down digit gets a digit in the quotient.'),
 ('Choose a strategy',
  '**Pick the strategy that fits the numbers.**\n'
  '• Zeros on both numbers: patterns.\n'
  '• Messy numbers: partial quotients or long division.\n'
  '• "About how many": an estimate is enough.',
  'Let the numbers choose.'),
 ('The remainder rule',
  '**A remainder is always smaller than the divisor.**\n'
  '• 1,250 %s 32 is 39 R2, not 38 R34.' % D,
  'If another group fits, keep going.'),
 ('Is it reasonable?',
  '**Compare your answer with your estimate. If it is about ten times too big or too small, a zero slipped.**\n'
  '• 4,560 %s 19 is about 230, so 24 cannot be right.' % D,
  'Estimate catches lost zeros.'),
 ('Two-step problems',
  '**In a word problem, the quotient is often only the first step.**\n'
  '• 2,880 eggs %s 12 = 240 cartons, then 240 %s $3 = $720.' % (D, X),
  'Ask what the question wants at the very end.', None, 'added'),
], L7,
 'Lesson 5-7 practice pages: choosing a strategy to divide (estimating, patterns, partial quotients and long division), checking that a quotient is reasonable, deciding whether a remainder can be bigger than the divisor, and two-step word problems.',
 'This lesson ties the unit together: the point is knowing which tool fits a problem, not just how to use each one.',
 [('Choose a strategy that fits the numbers in a division', 'source'),
  ('Estimate a quotient and use it to check for reasonableness', 'source'),
  ('Explain why a remainder must be smaller than the divisor', 'source'),
  ('Divide four-digit numbers by two-digit divisors', 'source'),
  ('Solve two-step word problems that use division', 'source')],
 'Built from the lesson 5-7 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The slip most worth a word is a lost zero: 4,560 ÷ 19 is 240, and an estimate of 4,600 ÷ 20 = 230 catches an answer of 24 before she multiplies. Every wrong option on a worked division comes from a named slip (a partial quotient left out, a zero lost or added, the remainder left off, or a remainder bigger than the divisor). There was no lesson 5-6 page in the folder, so nothing was built for Lesson 6.',
 ('Estimate, choose a strategy, divide, then check against the estimate.', 13))

print('divisions asked:', len(USED), '— none from the practice pages')
