# -*- coding: utf-8 -*-
"""River's Unit 5 — Lessons 1 to 3 (enVision grade-5, Topic 5: dividing by
two-digit divisors).

Three lessons, one per unit record, shelved on the `Unit 5` book behind
"Before You Start: Long Division with One-Digit Divisors" (v186) — the same
shape as Units 2 and 3. Source: her `5-1_`, `5-2_` and `5-3_ Student Edition
Practice.pdf` pages, which have a clean text layer. Read for what they ASK.

The practice pages print no lesson name, only each lesson's Essential Question
in the header box. The title is that question shortened into the skill it
names (the Unit 3 lessons' shape), never a book lesson name from memory. The book's
"5-1" label rides in `srcName`; titles say "Lesson N" (v164/v178).

Nothing here is worked by hand. Every quotient is computed below, and every
WRONG option comes from a named slip — a zero not cancelled, the zeros added
instead of taken away, the divisor rounded the wrong way, the tens part left
off, the two parts written side by side — so a distractor is a real mistake
with a real number. `use()` refuses every dividend/divisor pair printed on the
practice pages (the standalone rule): they were read for shape only.
"""
import json, io, math
import unit_common as U

D, X, MINUS = '÷', '×', '−'

def f(n): return '{:,}'.format(n)

# Every division printed on the three practice pages, as (dividend, divisor).
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
}
USED = set()

def use(a, b):
    """Every division a question asks goes through here, so none of the
    practice pages' own problems can slip back in."""
    assert (a, b) not in BOOK, ('reuses the practice page', a, b)
    USED.add((a, b))
    return a // b, a % b

def opts4(ans, *wrong):
    o = [ans if isinstance(ans, str) else f(ans)] + [w if isinstance(w, str) else f(w) for w in wrong]
    assert len(o) == 4 and len(set(o)) == 4, o
    return o

# ── Lesson 1 slips: dividing multiples of 10 ────────────────────────────────
def tz(n):
    z = 0
    while n and n % 10 == 0: n //= 10; z += 1
    return z

def fact(a, b):
    """The basic fact a pattern division rests on. 4,000 ÷ 80 needs one zero
    from the dividend (40 ÷ 8), which is `borrowed`."""
    za, zb = tz(a), tz(b)
    a0, b0 = a // 10**za, b // 10**zb
    borrowed = False
    if a0 % b0:
        a0 *= 10; za -= 1; borrowed = True
    assert a0 % b0 == 0 and a0 // b0 < 10, (a, b)
    fq = a0 // b0
    assert fq * 10**(za - zb) == a // b and a % b == 0, (a, b)
    return a0, b0, fq, za, zb, borrowed

def kept_zero(a, b):        # the divisor's zero never cancelled one: one zero too many
    return (a // b) * 10
def lost_zero(a, b):        # one zero too few
    assert (a // b) % 10 == 0; return (a // b) // 10
def zeros_added(a, b):      # counted the zeros of BOTH numbers onto the fact
    a0, b0, fq, za, zb, br = fact(a, b); return fq * 10**(tz(a) + tz(b))
def zero_twice(a, b):       # used a dividend zero for the fact, then counted it again
    a0, b0, fq, za, zb, br = fact(a, b); assert br; return fq * 10**(tz(a) - zb)

def pat_steps(a, b):
    a0, b0, fq, za, zb, br = fact(a, b)
    s = ['Basic fact: %d %s %d = %d.' % (a0, D, b0, fq)]
    if br:
        s.append('%d does not divide %d, so the fact borrows one zero: %d %s %d.' % (b0, a0 // 10, a0, D, b0))
    s.append('Zeros left to count: %s has %d%s, %s has %d, so %d %s.' % (
        f(a), za, ' (after the borrowed one)' if br else '', f(b), zb, za - zb,
        'zero' if za - zb == 1 else 'zeros'))
    s.append('So %s %s %s = %s.' % (f(a), D, f(b), f(a // b)))
    s.append('Check: %s %s %s = %s.' % (f(a // b), X, f(b), f(a)))
    return s

# ── Lesson 3 slips: area models ─────────────────────────────────────────────
def parts(a, b):
    qt, r = use(a, b)
    assert r == 0 and 10 <= qt < 100 and qt % 10, (a, b)
    return qt, qt // 10 * 10, qt % 10

def tens_only(a, b):        # stopped after the first piece of the area model
    return parts(a, b)[1]
def side_by_side(a, b):     # wrote the two parts next to each other: 20 and 2 → 202
    qt, t, o = parts(a, b); return int(str(t) + str(o))
def one_too_many(a, b):     # counted one group too many in the ones piece
    return parts(a, b)[0] + 1

def area_steps(a, b):
    qt, t, o = parts(a, b)
    return ['Estimate the tens: %d %s %d = %s, and %d %s %d = %s is too much.' % (
                b, X, t, f(b * t), b, X, t + 10, f(b * (t + 10))),
            'Take away the first piece: %s %s %s = %d.' % (f(a), MINUS, f(b * t), a - b * t),
            'Find the second piece: %d %s %d = %d.' % (b, X, o, b * o),
            'Add the two parts of the side: %d + %d = %d.' % (t, o, qt),
            'Check: %d %s %d = %s + %d = %s.' % (b, X, qt, f(b * t), b * o, f(a))]

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

def pat_q(lv, a, b, stem, unit, hint, tip, slips):
    """A pattern-division question whose wrong options are the named slips."""
    qt, r = use(a, b); assert r == 0
    vals = [fn(a, b) for fn in slips]
    for v in vals: assert v != qt and v * b != a, (a, b, v)
    names = {kept_zero: 'one zero too many', lost_zero: 'one zero too few',
             zeros_added: 'the zeros of both numbers added on',
             zero_twice: 'the borrowed zero counted twice'}
    why = '; '.join('%s is %s' % (f(v) + unit, names[fn]) for v, fn in zip(vals, slips))
    return (lv, stem, opts4(f(qt) + unit, *[f(v) + unit for v in vals]), 0, hint,
            pat_steps(a, b),
            '**%s%s.** %s The wrong answers come from real slips: %s.' % (
                f(qt), unit, 'Check: %s %s %s = %s.' % (f(qt), X, f(b), f(a)), why), tip)

def area_q(lv, a, b, stem, unit, hint, tip):
    qt, t, o = parts(a, b)
    vals = [tens_only(a, b), side_by_side(a, b), one_too_many(a, b)]
    for v in vals: assert v != qt and v * b != a, (a, b, v)
    return (lv, stem, opts4(f(qt) + unit, *[f(v) + unit for v in vals]), 0, hint,
            area_steps(a, b),
            '**%s%s.** The side is %d + %d = %d, and %d %s %d = %s. The wrong answers are real slips: %s is only the tens piece, %s writes %d and %d side by side, and %s is one group too many.' % (
                f(qt), unit, t, o, qt, b, X, qt, f(a), f(vals[0]) + unit, f(vals[1]) + unit, t, o, f(vals[2]) + unit),
            tip)

# ══ Lesson 1 · How Can Patterns Help You Divide Multiples of 10? ════════════
assert fact(4000, 80)[5] and fact(20000, 40)[5] and not fact(2700, 30)[5]
assert 2000 // 40 == 50 and 500 / 40 == 12.5 and 8000 // 20 == 400
assert [(3600, 40), (360, 40), (36000, 4), (3600, 400)] and 3600 // 40 == 90
assert [x for x in (3600 // 40, 360 // 40, 36000 // 4, 3600 // 400)].count(90) == 1
assert [x for x in (450 // 5, 450 // 50, 4500 // 5, 45000 // 5)].count(4500 // 50) == 1
for p in [(490, 70), (3600, 40), (360, 40), (36000, 4), (3600, 400), (4500, 50), (450, 5),
          (450, 50), (4500, 5), (45000, 5), (2000, 40), (500, 40), (8000, 20), (36000, 40),
          (48000, 80)]:
    use(*p)
assert 36000 // 400 == 90 and 36000 // 4 == 9000 and 36000 // 4000 == 9
assert 4800 // 80 == 60 and 480000 // 80 == 6000

L1 = [
 (1, 'Why can you find 490 %s 70 by thinking "49 tens %s 7 tens"?' % (D, D),
  ['Both numbers are counted in tens, and tens shared by tens gives ones',
   'The zeros do not matter, so you can drop them from both numbers',
   '70 has one zero, so the answer must always have one zero too',
   'Every division by 70 has an answer of exactly 7'], 0,
  'What is 490 written in tens? What is 70 written in tens?',
  ['490 is 49 tens.', '70 is 7 tens.', '49 tens %s 7 tens is like 49 %s 7 = 7.' % (D, D),
   'So 490 %s 70 = 7. Check: 7 %s 70 = 490.' % (D, X)],
  '**Both are counted in tens.** 49 tens shared into groups of 7 tens is 7 groups, the same as 49 %s 7.' % D,
  'Taking the same zero off both numbers leaves the quotient alone.'),
 pat_q(1, 2700, 30, 'What is 2,700 %s 30?' % D, '',
       'Start with the basic fact 27 %s 3.' % D, 'Each zero in the divisor cancels one zero in the dividend.',
       [kept_zero, lost_zero, zeros_added]),
 (1, 'Which basic fact helps you find 28,000 %s 40?' % D,
  ['28 %s 4 = 7' % D, '28 %s 7 = 4' % D, '24 %s 4 = 6' % D, '32 %s 4 = 8' % D], 0,
  'Cover the zeros. Which digits are left?',
  ['28,000 starts with 28.', '40 starts with 4.', 'The fact is 28 %s 4 = 7.' % D,
   'Then the zeros: 28,000 %s 40 = 700.' % D],
  '**28 %s 4 = 7.** The fact uses the digits in front of the zeros, then the zeros finish the job: 700.' % D,
  '28 %s 7 = 4 is a real fact, but it divides by the answer instead of by 4.' % D),
 pat_q(2, 28000, 40, 'What is 28,000 %s 40?' % D, '',
       'Basic fact first: 28 %s 4.' % D, 'Check by multiplying back: your answer %s 40 must give 28,000.' % X,
       [kept_zero, lost_zero, zeros_added]),
 pat_q(2, 4000, 80, 'What is 4,000 %s 80?' % D, '',
       '8 does not divide 4. Which fact uses 40?', 'When the fact borrows a zero, that zero is used up.',
       [zero_twice, lost_zero, zeros_added]),
 pat_q(2, 20000, 40, 'What is 20,000 %s 40?' % D, '',
       '4 does not divide 2. Use 20 %s 4.' % D, 'Check: 500 %s 40 = 20,000.' % X,
       [zero_twice, lost_zero, zeros_added]),
 (2, 'Which number makes 36,000 %s ___ = 900 true?' % D,
  ['40', '4', '400', '4,000'], 0,
  'Think: 900 times what number is 36,000?',
  ['The fact is 36 %s 4 = 9.' % D, '36,000 has three zeros and 900 has two.',
   'One zero is left over for the divisor, so it is 40.', 'Check: 36,000 %s 40 = 900.' % D],
  '**40.** 900 %s 40 = 36,000. With 4 the quotient is 9,000, with 400 it is 90, and with 4,000 it is 9.' % X,
  'Multiply your answer by 900 to check it lands on 36,000.'),
 (2, 'Which number makes ___ %s 80 = 600 true?' % D,
  ['48,000', '4,800', '480,000', '680'], 0,
  'The missing number is the dividend. Multiply to find it.',
  ['___ %s 80 = 600 means 600 %s 80 = ___.' % (D, X), '6 %s 8 = 48.' % X,
   '600 has two zeros and 80 has one: three zeros in all.', 'So the missing number is 48,000.'],
  '**48,000.** 600 %s 80 = 48,000. 4,800 has a zero too few (4,800 %s 80 = 60), and 680 adds 600 and 80 instead of multiplying.' % (X, D),
  'Undo a division with a multiplication.'),
 pat_q(2, 5400, 60, 'A sticker shop packs 5,400 stickers into rolls of 60. How many rolls does it fill?',
       ' rolls', 'Find 5,400 %s 60 with the fact 54 %s 6.' % (D, D), 'Check: 90 rolls %s 60 = 5,400 stickers.' % X,
       [kept_zero, lost_zero, zeros_added]),
 pat_q(2, 35000, 70, 'A theater sold 35,000 tickets over 70 shows, the same number for every show. How many tickets did it sell for each show?',
       ' tickets', 'Find 35,000 %s 70. Start with 35 %s 7.' % (D, D), 'Each show sold the same number, so this is a sharing division.',
       [kept_zero, lost_zero, zeros_added]),
 (3, 'Which division has a quotient of 90?',
  ['3,600 %s 40' % D, '360 %s 40' % D, '36,000 %s 4' % D, '3,600 %s 400' % D], 0,
  'Work out each one with the fact 36 %s 4 = 9 and count the zeros.' % D,
  ['3,600 %s 40: two zeros minus one leaves one, so 90.' % D, '360 %s 40: one minus one leaves none, so 9.' % D,
   '36,000 %s 4: three zeros stay, so 9,000.' % D, '3,600 %s 400: two minus two leaves none, so 9.' % D],
  '**3,600 %s 40.** It is the only one that leaves exactly one zero after the fact 36 %s 4 = 9. Check: 90 %s 40 = 3,600.' % (D, D, X),
  'Same fact, different zeros, different answers. Count them every time.'),
 (3, 'Which division has the same quotient as 4,500 %s 50?' % D,
  ['450 %s 5' % D, '450 %s 50' % D, '4,500 %s 5' % D, '45,000 %s 5' % D], 0,
  'What happens if you take one zero off BOTH numbers?',
  ['4,500 %s 50 = 90.' % D, '450 %s 5 takes one zero off each number: 450 %s 5 = 90.' % (D, D),
   '450 %s 50 = 9, 4,500 %s 5 = 900 and 45,000 %s 5 = 9,000.' % (D, D, D)],
  '**450 %s 5.** Taking one zero off the dividend AND the divisor leaves the quotient the same: both are 90.' % D,
  'Taking a zero off only one of the numbers changes the answer by ten times.'),
 (3, 'A cook uses 40 grams of pepper in each pot of soup. Pepper comes in a 2-kilogram jar or a 500-gram jar. Which jar gets used up exactly, with no pepper left over? (1 kilogram = 1,000 grams.)',
  ['The 2-kilogram jar, because 2,000 %s 40 = 50 with nothing left' % D,
   'The 500-gram jar, because 500 %s 40 = 12 with nothing left' % D,
   'The 2-kilogram jar, because 2 %s 40 comes out to a whole number' % D,
   'Both jars, because 40 divides any number that ends in zero'], 0,
  'Change kilograms to grams first, so both jars use the same unit.',
  ['2 kilograms = 2,000 grams.', '2,000 %s 40 = 50 pots, with nothing left.' % D,
   '500 %s 40 = 12 pots, with 20 grams left over.' % D, 'So the 2-kilogram jar is used up exactly.'],
  '**The 2-kilogram jar.** 2,000 grams makes exactly 50 pots. The 500-gram jar makes 12 pots and leaves 20 grams.',
  'Both amounts have to be in grams before you can compare them.'),
 (3, 'Ben says 8,000 %s 20 = 4,000, because 8 %s 2 = 4 and 8,000 has three zeros. What went wrong?' % (D, D),
  ['The zero in 20 cancels one of them, so it is 400',
   'He used the wrong fact, because 8 %s 2 is 6' % D,
   'Nothing went wrong, because 4,000 is correct',
   'He should add the zeros, so the answer is 40,000'], 0,
  'Check his answer: does 4,000 %s 20 make 8,000?' % X,
  ['8 %s 2 = 4 is right.' % D, '8,000 has three zeros, but 20 has one, and it cancels one of them.',
   'That leaves two zeros: 400.', 'Check: 400 %s 20 = 8,000, but 4,000 %s 20 = 80,000.' % (X, X)],
  '**The zero in 20 cancels one zero.** 8,000 %s 20 = 400, and 400 %s 20 = 8,000.' % (D, X),
  'Multiplying back catches a wrong number of zeros right away.'),
]

go(1, 'Patterns for Dividing Multiples of 10', [
 ('Start with a basic fact',
  '**Cover the zeros and divide the digits that are left.**\n'
  '• 2,700 %s 30 starts with 27 %s 3 = 9.\n'
  '• Then the zeros finish the answer.' % (D, D),
  'Fact first, zeros second.'),
 ('Tens divided by tens',
  '**490 %s 70 is the same as 49 tens %s 7 tens, which is 7.**\n'
  '• Tens shared into groups of tens gives a plain number of groups.' % (D, D),
  '49 tens in groups of 7 tens: 7 groups.'),
 ('Count the zeros that are left',
  '**Take away one zero for each zero in the divisor.**\n'
  '• 28,000 %s 40: 28 %s 4 = 7, then three zeros minus one leaves two, so 700.' % (D, D),
  'Dividend zeros, minus divisor zeros.'),
 ('When the fact needs a zero',
  '**Sometimes the fact borrows a zero: 4,000 %s 80 uses 40 %s 8 = 5, so the answer is 50.**\n'
  '• 8 does not divide 4, so the fact takes one zero from 4,000.\n'
  '• That zero is used up. It does not get counted again.' % (D, D),
  'A borrowed zero is spent.'),
 ('Same zeros off both numbers',
  '**Taking one zero off the dividend AND the divisor keeps the answer the same.**\n'
  '• 4,500 %s 50 = 450 %s 5 = 90.' % (D, D),
  'Both numbers shrink together, so the answer stays put.'),
 ('A missing number',
  '**Use multiplication to find a missing dividend or divisor.**\n'
  '• ___ %s 80 = 600 means 600 %s 80 = 48,000.\n'
  '• 36,000 %s ___ = 900: 900 %s 40 = 36,000, so the divisor is 40.' % (D, X, D, X),
  'Multiplication undoes division.'),
 ('Check with multiplication',
  '**Quotient %s divisor should give back the dividend.**\n'
  '• 700 %s 40 = 28,000, so 28,000 %s 40 = 700 is right.' % (X, X, D),
  'A wrong number of zeros shows up at once.'),
 ('Same units first',
  '**Before you divide, put both amounts in the same unit.**\n'
  '• 1 kilogram = 1,000 grams, so 2 kilograms is 2,000 grams.',
  'Grams with grams, kilograms with kilograms.', None, 'added'),
], L1,
 'Lesson 5-1 practice pages: using basic facts and place-value patterns to divide multiples of 10, including missing dividends and divisors and word problems.',
 'Every later lesson in this unit leans on this one. Estimating a quotient, and each step of the area model, divides by tens.',
 [('Divide multiples of 10 using a basic fact and place-value patterns', 'source'),
  ('Find a missing dividend or divisor in a division with multiples of 10', 'source'),
  ('Check a quotient by multiplying back', 'source'),
  ('Put both amounts in the same unit before dividing', 'added')],
 'Built from the lesson 5-1 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The trap most worth a word is the fact that borrows a zero: 4,000 ÷ 80 uses 40 ÷ 8 = 5, so the answer is 50, and counting that zero again gives 500. Two questions are built around it, and every wrong option comes from a named slip (a zero too many, a zero too few, the zeros of both numbers added on, or the borrowed zero counted twice). One question changes kilograms to grams first, like the page\'s own sea-salt problem.',
 ('Fact first, then count the zeros, then multiply back to check.', 12))

# ══ Lesson 2 · How Can You Use Compatible Numbers to Estimate Quotients? ═════
def near(a, b, A, B):
    """A compatible estimate: B is b rounded to its nearest ten, and A is a
    multiple of B close to a whose quotient is a basic-fact answer."""
    use(a, b)
    assert A % B == 0 and abs(a - A) * 10 < a and abs(b - B) <= 5, (a, b, A, B)
    e = A // B
    assert e // 10**tz(e) < 10, (a, b, e)
    assert abs(a / b - e) <= 0.2 * e, (a, b, e)
    return e

e413 = near(413, 58, 420, 60); assert e413 == 7 and 400 // 50 == 8 and 360 // 60 == 6
e1630 = near(1630, 41, 1600, 40); assert e1630 == 40 and 2000 // 40 == 50
e3467 = near(3467, 72, 3500, 70); assert e3467 == 50 and 3200 // 80 == 40
e238 = near(238, 61, 240, 60); assert e238 == 4 and 238 - 61 == 177 and 300 // 60 == 5
e638 = near(638, 79, 640, 80); assert e638 == 8 and 630 // 70 == 9 and 560 // 80 == 7
e2415 = near(2415, 62, 2400, 60); assert e2415 == 40 and 1800 // 60 == 30
e452 = 450 // 15; use(452, 15); assert e452 == 30 and 450 // 10 == 45
use(352, 58); assert 6 * 60 == 360 and 6 * 58 == 348
use(523, 48); assert 500 // 50 == 10 and 523 / 48 > 10
use(4738, 59); _r = 4738 / 59
_cands = {'4,800 %s 60 = 80' % D: 80, '5,000 %s 50 = 100' % D: 100, '4,200 %s 60 = 70' % D: 70, '4,500 %s 50 = 90' % D: 90}
assert min(_cands, key=lambda k: abs(_cands[k] - _r)).startswith('4,800') and len(set(_cands.values())) == 4
use(532, 19); assert 500 // 20 == 25 and 540 // 20 == 27 and round(532 / 19) == 28
use(358, 59); assert 360 // 60 == 6 and 350 % 60 and 360 % 50

def est_q(lv, stem, ans, wrong, hint, steps, main, tip):
    return (lv, stem, opts4(ans, *wrong), 0, hint, steps, main, tip)

L2 = [
 (1, 'Which pair of compatible numbers is best for estimating 358 %s 59?' % D,
  ['360 and 60', '350 and 60', '360 and 50', '400 and 59'], 0,
  'Round 59 first. Then find a number near 358 that it divides easily.',
  ['59 is close to 60.', '358 is close to 360.', '36 %s 6 = 6 is a basic fact, so 360 %s 60 = 6.' % (D, D),
   '350 %s 60 and 360 %s 50 do not come out evenly.' % (D, D)],
  '**360 and 60.** Both are close to the real numbers, and 360 %s 60 = 6 is a basic fact with a zero on each.' % D,
  'Compatible means close AND easy to divide, both at once.'),
 (1, 'What are compatible numbers, when you estimate a quotient?',
  ['Numbers close to the real ones that divide easily in your head',
   'The exact numbers in the problem, written with commas',
   'Any two numbers that both end in a zero',
   'Numbers rounded to the nearest hundred, every time'], 0,
  'They have two jobs to do at once.',
  ['They must be close to the real numbers, so the estimate is close.',
   'They must divide easily, usually with a basic fact.', 'Ending in zero is not enough on its own: 350 %s 60 is not easy.' % D],
  '**Numbers close to the real ones that divide easily.** 360 and 60 are compatible for 358 %s 59.' % D,
  'Rounding to the nearest hundred can land on numbers that do not divide easily.'),
 (1, 'A question asks, "About how many rings should she make each day?" What does the word "about" tell you?',
  ['An estimate is enough to answer it',
   'You must find the exact answer first',
   'The answer has to be a round hundred',
   'You should add the numbers, not divide'], 0,
  'What kind of answer does "about" ask for?',
  ['"About" asks for a close answer, not an exact one.', 'Compatible numbers give a close answer quickly.',
   'You can still check it with multiplication.'],
  '**An estimate is enough.** "About how many" means a close answer does the job.',
  'Read the question for words like "about", "roughly" or "estimate".'),
 est_q(2, 'Use compatible numbers to estimate 413 %s 58.' % D, '7', ['70', '8', '6'],
  'Round 58 to 60, then find a number near 413 that 60 divides.',
  ['58 rounds to 60.', '420 is close to 413, and 42 %s 6 = 7.' % D, 'So 420 %s 60 = 7.' % D,
   'Check: 7 %s 60 = 420, close to 413.' % X],
  '**7.** 420 %s 60 = 7. The wrong answers are real slips: 70 keeps a zero that should cancel, 8 rounds 58 down to 50 (400 %s 50), and 6 uses 360, which is too far from 413.' % (D, D),
  'Round the divisor to its nearest ten, not just any ten.'),
 est_q(2, 'Use compatible numbers to estimate 1,630 %s 41.' % D, '40', ['4', '400', '50'],
  'Round 41 to 40. Which number near 1,630 does 40 divide easily?',
  ['41 rounds to 40.', '1,600 is close to 1,630, and 16 %s 4 = 4.' % D,
   '1,600 %s 40 = 40.' % D, 'Check: 40 %s 40 = 1,600.' % X],
  '**40.** 1,600 %s 40 = 40. 4 loses a zero, 400 keeps one too many, and 50 rounds 1,630 all the way to 2,000, which is too far.' % D,
  'Pick the compatible number that is closest, not the roundest.'),
 est_q(2, 'Use compatible numbers to estimate 3,467 %s 72.' % D, '50', ['500', '5', '40'],
  '72 is close to 70. Which number near 3,467 divides by 70?',
  ['72 rounds to 70.', '3,500 is close to 3,467, and 35 %s 7 = 5.' % D,
   '3,500 %s 70 = 50.' % D, 'Check: 50 %s 70 = 3,500.' % X],
  '**50.** 3,500 %s 70 = 50. 500 keeps one zero too many, 5 loses one, and 40 rounds 72 the wrong way, up to 80 (3,200 %s 80).' % (D, D),
  '72 is 2 away from 70 but 8 away from 80, so round to 70.'),
 est_q(2, 'A club earned $238 by selling 61 mugs, all at the same price. About how much did each mug cost?',
  '$4', ['$40', '$177', '$5'],
  'Divide the money by the number of mugs. Use compatible numbers.',
  ['Find about 238 %s 61.' % D, '61 is close to 60, and 238 is close to 240.',
   '24 %s 6 = 4, so 240 %s 60 = 4.' % (D, D), 'Each mug cost about $4.'],
  '**About $4.** 240 %s 60 = 4. $40 keeps a zero that should cancel, $177 subtracts instead of dividing, and $5 rounds 238 up to 300, which is too far.' % D,
  'Check it: 61 mugs at $4 is about $240, close to $238.'),
 est_q(2, 'A camp has 452 campers. Each cabin holds between 14 and 16 campers. Which is the best estimate of the number of cabins?',
  '30 cabins', ['3 cabins', '300 cabins', '45 cabins'],
  'Pick one number for the cabin size, in the middle of 14 and 16.',
  ['Use 15 for the cabin size.', '452 is close to 450.', '450 %s 15 = 30.' % D, 'So about 30 cabins.'],
  '**30 cabins.** 450 %s 15 = 30. 3 and 300 have the wrong number of zeros, and 45 uses 10 campers to a cabin, which is not between 14 and 16.' % D,
  'For "between 14 and 16", the middle, 15, is a fair number to use.'),
 est_q(2, 'Maria has 638 shells to paint and 79 days to paint them, about the same number each day. About how many should she paint each day?',
  '8 shells', ['80 shells', '9 shells', '7 shells'],
  'Round 79 first.',
  ['79 rounds to 80.', '640 is close to 638, and 64 %s 8 = 8.' % D, '640 %s 80 = 8.' % D, 'About 8 shells a day.'],
  '**About 8 shells.** 640 %s 80 = 8. 80 keeps a zero too many, 9 rounds 79 down to 70 (630 %s 70), and 7 uses 560, too far from 638.' % (D, D),
  'Check: 8 shells %s 80 days = 640, close to 638.' % X),
 (2, 'Which multiplication shows that 6 is a reasonable estimate for 352 %s 58?' % D,
  ['6 %s 60 = 360, which is close to 352' % X, '6 %s 58 = 352, so it is exact' % X,
   '6 %s 352 = 2,112, which is close to 58' % X, '58 + 6 = 64, which is close to 60'], 0,
  'Multiply the estimate by the rounded divisor.',
  ['58 rounds to 60.', '6 %s 60 = 360.' % X, '360 is close to 352, so 6 is reasonable.',
   '6 %s 58 is really 348, not 352.' % X],
  '**6 %s 60 = 360, close to 352.** Multiplying back is how you check an estimate.' % X,
  'An estimate only has to land close. It does not have to be exact.'),
 (3, 'Ava estimates 523 %s 48 as 500 %s 50 = 10. Is the real answer more or less than 10?' % (D, D),
  ['More, because she made 523 smaller and 48 bigger',
   'Less, because she made 523 smaller and 48 bigger',
   'Exactly 10, because both numbers were rounded',
   'More, because 523 is an odd number'], 0,
  'What does a smaller dividend do to a quotient? What does a bigger divisor do?',
  ['She rounded 523 down to 500, which makes the quotient smaller.',
   'She rounded 48 up to 50, which also makes the quotient smaller.',
   'Both changes pushed her estimate down, so the real answer is more.',
   'Check: 48 %s 10 = 480, which is less than 523.' % X],
  '**More.** A smaller dividend and a bigger divisor both shrink the quotient, so 10 is too low. The real answer is a bit more than 10.',
  'Sharing less, or sharing among more groups, both give each group less.'),
 est_q(3, 'A school has 2,415 pencils. Each classroom needs 62 pencils. About how many classrooms can get the pencils they need?',
  '40 classrooms', ['400 classrooms', '4 classrooms', '30 classrooms'],
  'Round 62 first, then pick a number near 2,415.',
  ['62 rounds to 60.', '2,400 is close to 2,415, and 24 %s 6 = 4.' % D,
   '2,400 %s 60 = 40.' % D, 'About 40 classrooms.'],
  '**About 40 classrooms.** 2,400 %s 60 = 40. 400 and 4 have the wrong number of zeros, and 30 uses 1,800, which is far from 2,415.' % D,
  'Check: 40 %s 60 = 2,400, close to 2,415.' % X),
 (3, 'Which estimate is closest to the real value of 4,738 %s 59?' % D,
  list(_cands.keys()), 0,
  'Round 59 to its nearest ten. Then pick the dividend closest to 4,738.',
  ['59 rounds to 60, not 50.', 'With 60, the closest easy dividend is 4,800.',
   '4,800 %s 60 = 80.' % D, 'The real quotient is just over 80.'],
  '**4,800 %s 60 = 80.** It uses the nearest ten for 59 and the closest easy number to 4,738. The real answer is about 80.' % D,
  'Each change you make to the numbers moves the estimate. Make the smallest changes you can.'),
 (3, 'Leo estimates 532 %s 19 as 500 %s 20 = 25. Mia estimates it as 540 %s 20 = 27. Which is true?' % (D, D, D),
  ['Both estimates are reasonable, and the real answer is about 28',
   "Only Leo's is right, because 500 is a rounder number",
   "Only Mia's is right, because there is just one estimate",
   'Neither is reasonable, because 19 must be rounded to 10'], 0,
  'Are both pairs close to 532 and 19? Do both divide easily?',
  ['Both rounded 19 to 20.', 'Leo used 500 and Mia used 540, both close to 532.',
   'Both pairs divide easily.', 'The real answer is about 28, so both are close.'],
  "**Both are reasonable.** Different compatible numbers give different estimates. Mia's is a little closer, because 540 is closer to 532.",
  'There is often more than one good estimate. Closer compatible numbers give a closer one.'),
]

go(2, 'Estimate Quotients with Compatible Numbers', [
 ('When an estimate is enough',
  '**If a question asks "about how many" or "about how much", an estimate answers it.**\n'
  '• An estimate also checks an exact answer later.',
  '"About" means close is good.'),
 ('Compatible numbers',
  '**Numbers close to the real ones that divide easily in your head.**\n'
  '• For 358 %s 59, use 360 %s 60 = 6.' % (D, D),
  'Close and easy, both at once.'),
 ('Round the divisor first',
  '**Round a two-digit divisor to its nearest ten.**\n'
  '• 58 becomes 60, not 50.\n'
  '• 72 becomes 70, not 80.',
  'Which ten is it closer to?'),
 ('Then pick the dividend',
  '**Find a number close to the dividend that the rounded divisor divides with a basic fact.**\n'
  '• 413 %s 58: think 60, then 420, because 42 %s 6 = 7.' % (D, D),
  'Look for a basic fact hiding in the digits.'),
 ('Check with multiplication',
  '**Multiply your estimate by the rounded divisor. It should land close to the dividend.**\n'
  '• 7 %s 60 = 420, close to 413.' % X,
  'Close, not exact, is the goal.'),
 ('More than one good estimate',
  '**Different compatible numbers can give different estimates, and both can be reasonable.**\n'
  '• 532 %s 19: 500 %s 20 = 25 and 540 %s 20 = 27 both work.' % (D, D, D),
  'Closer numbers give a closer estimate.'),
 ('A range of numbers',
  '**When a problem gives a range, like "between 14 and 16", use a number in the middle.**\n'
  '• 452 campers in cabins of 14 to 16 is about 450 %s 15 = 30.' % D,
  'The middle of the range is fair.'),
 ('Too high or too low?',
  '**Making the dividend smaller or the divisor bigger makes the estimate smaller than the real answer.**\n'
  '• 523 %s 48 as 500 %s 50 = 10: both changes push it down, so the real answer is more than 10.' % (D, D),
  'Less to share, or more groups, means less in each.', None, 'added'),
], L2,
 'Lesson 5-2 practice pages: estimating quotients with two-digit divisors using compatible numbers, checking an estimate with multiplication, and using estimates in word problems.',
 'Estimating first tells her how big a quotient should be before she works it out. That is how she will check every division in the rest of the unit.',
 [('Estimate a quotient with a two-digit divisor using compatible numbers', 'source'),
  ('Check an estimate with multiplication', 'source'),
  ('Use an estimate to answer an "about how many" word problem', 'source'),
  ('Tell whether an estimate is too high or too low', 'added')],
 'Built from the lesson 5-2 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The slip most worth a word is rounding the divisor the wrong way (72 to 80 instead of 70), which several wrong options are built from. The others are a zero kept or lost, and a compatible dividend chosen too far from the real one. One question goes a step past the page and asks whether an estimate is too high or too low; it is marked as added.',
 ('Round the divisor, find a basic fact, then multiply back to check.', 12))

# ══ Lesson 3 · How Can You Use Area Models and Properties to Find Quotients? ══
assert 14 * 34 == 476 and 14 * 26 == 364 and 23 * 25 == 575 and 34 * 24 == 816
assert 18 * 31 == 558 and 16 * 28 == 448 and 29 * 23 == 667 and 28 * 24 == 672
assert 13 * 24 == 312 and 13 * 20 == 260 and 13 * 30 == 390
for p in [(476, 14), (364, 14), (575, 23), (816, 34), (558, 18), (448, 16), (667, 29),
          (672, 28), (312, 13)]:
    use(*p)
assert side_by_side.__name__ and int('20' + '8') == 208

L3 = [
 (1, 'A rectangle has an area of 476 square inches. One side is 14 inches long. Which equation finds the other side, w?',
  ['476 %s 14 = w' % D, '476 %s 14 = w' % X, '476 %s 14 = w' % MINUS, '14 %s 476 = w' % D], 0,
  'Area = length %s width. Which operation undoes the multiplying?' % X,
  ['Area = length %s width, so 14 %s w = 476.' % (X, X), 'To find a missing factor, divide.',
   'So w = 476 %s 14.' % D, '476 %s 14 = 34 inches.' % D],
  '**476 %s 14 = w.** A missing side is the area divided by the side you know. Here w = 34.' % D,
  'Dividing the smaller number by the bigger one gives less than 1, which cannot be the side.'),
 (1, 'In an area model for 476 %s 14, what does the missing side stand for?' % D,
  ['The quotient', 'The dividend', 'The divisor', 'The remainder'], 0,
  'The area is 476, and one side is 14.',
  ['The whole area is the dividend, 476.', 'The side you know is the divisor, 14.',
   'The side you are finding is the quotient.'],
  '**The quotient.** Area %s known side = missing side, so the missing side is the answer to the division: 34.' % D,
  'Dividend = area, divisor = known side, quotient = missing side.'),
 (1, 'What is the best first step for finding 312 %s 13 with an area model?' % D,
  ['Find the tens: 13 %s 20 = 260 fits, and 13 %s 30 = 390 is too much' % (X, X),
   'Find the ones first: 13 %s 2 = 26, so the answer must be 2' % X,
   'Add 312 and 13 to find the area of the whole rectangle first',
   'Divide 13 by 312 to find how wide the first piece should be'], 0,
  'Start by estimating how many tens will be in the quotient.',
  ['13 %s 20 = 260, which is less than 312.' % X, '13 %s 30 = 390, which is more than 312.' % X,
   'So the quotient has 2 tens.', '312 %s 260 = 52 is left, and 13 %s 4 = 52, so 312 %s 13 = 24.' % (MINUS, X, D)],
  '**Find the tens first.** 13 %s 20 = 260 fits and 13 %s 30 = 390 does not, so the first piece of the side is 20.' % (X, X),
  'Tens first, then the ones with what is left.'),
 area_q(2, 374, 17, 'What is 374 %s 17?' % D, '',
        'Start with 17 %s 20.' % X, 'Add the parts of the side; never write them side by side.'),
 area_q(2, 696, 29, 'What is 696 %s 29?' % D, '',
        '29 %s 20 = 580. How much is left?' % X, 'Check: the answer %s 29 must be 696.' % X),
 (2, 'Which shows 364 %s 14 using the Distributive Property?' % D,
  ['364 = 14 %s 20 + 14 %s 6 = 14 %s (20 + 6), so the quotient is 26' % (X, X, X),
   '364 = 14 %s 2 + 14 %s 6 = 14 %s (2 + 6), so the quotient is 8' % (X, X, X),
   '364 = 14 %s 20 + 14 %s 60 = 14 %s (20 + 60), so the quotient is 80' % (X, X, X),
   '364 = 10 %s 26 + 4 %s 6 = 284, so the quotient is 10' % (X, X)], 0,
  'Split the missing side into tens and ones. Do the pieces add back to 364?',
  ['14 %s 20 = 280.' % X, '364 %s 280 = 84, and 14 %s 6 = 84.' % (MINUS, X),
   '280 + 84 = 364, so 364 = 14 %s (20 + 6).' % X, 'The quotient is 26.'],
  '**14 %s 20 + 14 %s 6 = 14 %s (20 + 6) = 364.** The two pieces add back to 364, so the quotient is 26.' % (X, X, X),
  'Check that the pieces add back to the whole: 14 %s 2 + 14 %s 6 is only 112.' % (X, X)),
 area_q(2, 432, 18, 'A rectangular rug has an area of 432 square feet. One side is 18 feet. How many feet long is the other side?',
        ' feet', 'Find 432 %s 18. Start with 18 %s 20.' % (D, X), 'Area %s known side = missing side.' % D),
 area_q(2, 351, 13, 'A choir of 351 singers stands in 13 equal rows. How many singers are in each row?',
        ' singers', 'Find 351 %s 13. Start with the tens: 13 %s 20.' % (D, X), 'Check: 13 rows %s your answer must make 351.' % X),
 (2, 'In an area model for 575 %s 23, the first piece is 23 %s 20 = 460. Which multiplication fills the second piece?' % (D, X),
  ['23 %s 5 = 115' % X, '23 %s 15 = 345' % X, '23 %s 50 = 1,150' % X, '20 %s 5 = 100' % X], 0,
  'How much of 575 is left after the first piece?',
  ['575 %s 460 = 115 is left.' % MINUS, '23 %s 5 = 115, so the second piece is 5.' % X,
   'The side is 20 + 5 = 25.', 'So 575 %s 23 = 25.' % D],
  '**23 %s 5 = 115.** 575 %s 460 leaves 115, and 23 %s 5 is exactly 115, so 575 %s 23 = 25.' % (X, MINUS, X, D),
  'Every piece of the model uses the same side, 23.'),
 (2, 'How many tens will be in the quotient of 816 %s 34?' % D,
  ['2 tens', '3 tens', '8 tens', '20 tens'], 0,
  'Try 34 %s 20 and 34 %s 30.' % (X, X),
  ['34 %s 20 = 680, which is less than 816.' % X, '34 %s 30 = 1,020, which is more than 816.' % X,
   'So the quotient has 2 tens.', '816 %s 34 = 24.' % D],
  '**2 tens.** 34 %s 20 fits under 816 but 34 %s 30 goes over, so the quotient is in the twenties: 24.' % (X, X),
  'Estimating the tens first stops you from starting with a piece that is too big.'),
 (3, 'Jada found 558 %s 18 = 31. Which multiplication checks her answer?' % D,
  ['18 %s 31 = 18 %s 30 + 18 %s 1 = 540 + 18 = 558' % (X, X, X),
   '18 + 31 = 49, which is close to 50',
   '558 %s 18 = 10,044, which is bigger than 31' % X,
   '18 %s 3 + 18 %s 1 = 54 + 18 = 72' % (X, X)], 0,
  'Multiply the quotient by the divisor.',
  ['18 %s 30 = 540.' % X, '18 %s 1 = 18.' % X, '540 + 18 = 558, which is the dividend.',
   'So 31 is right.'],
  '**18 %s 31 = 540 + 18 = 558.** Quotient %s divisor gives back the dividend, so her answer checks out.' % (X, X),
  '18 %s 3 forgets that the 3 in 31 means 3 tens.' % X),
 (3, 'Noah used an area model for 448 %s 16. His pieces were 16 %s 20 = 320 and 16 %s 8 = 128, and he wrote the answer 208. What went wrong?' % (D, X, X),
  ['He wrote 20 and 8 side by side; he should add them to get 28',
   'His first piece was wrong, because 16 %s 20 is really 300' % X,
   'Nothing went wrong, because 208 is the correct quotient here',
   'He should multiply 20 and 8 to get 160, the real side length'], 0,
  'Check: does 16 %s 208 make 448?' % X,
  ['320 + 128 = 448, so both pieces are right.', 'The side is 20 + 8 = 28.',
   'Writing 20 and 8 side by side makes 208, which is far too big.',
   'Check: 16 %s 28 = 448.' % X],
  '**He wrote the parts side by side.** The side is 20 + 8 = 28, and 16 %s 28 = 448. 16 %s 208 would be 3,328.' % (X, X),
  'Add the parts of the side together, the same way you add partial products.'),
 (3, 'Priya says 667 %s 29 = 23. She checks: 29 %s 20 = 580 and 29 %s 3 = 87, and 580 + 87 = 667. Is she right?' % (D, X, X),
  ['Yes, because the two pieces add back to 667',
   'No, because 29 %s 3 is 97, so the answer is 24' % X,
   'No, because 667 is odd, so it cannot be divided by 29',
   'Yes, but only because 23 is close to 20'], 0,
  'Check each piece, then add.',
  ['29 %s 20 = 580 is right.' % X, '29 %s 3 = 87 is right.' % X, '580 + 87 = 667, the dividend.',
   'So 667 %s 29 = 23.' % D],
  '**Yes.** Both pieces are right and they add back to 667, so 23 is the quotient.',
  'A good check says so when an answer is right, too.'),
 (3, 'A garden bed has an area of 672 square feet and is 28 feet long. Will it fit in a space that is 25 feet wide?',
  ['Yes, because it is 24 feet wide', 'No, because it is 26 feet wide',
   'Yes, because it is 20 feet wide', 'No, because 672 is more than 25'], 0,
  'Find the width first: 672 %s 28.' % D,
  ['28 %s 20 = 560, and 672 %s 560 = 112.' % (X, MINUS), '28 %s 4 = 112.' % X,
   'So the width is 20 + 4 = 24 feet.', '24 feet is less than 25, so it fits.'],
  '**Yes, it is 24 feet wide.** 28 %s 24 = 672, and 24 feet fits in a 25-foot space with 1 foot to spare.' % X,
  'Answer the question that was asked: the width is a step, "will it fit" is the answer.'),
 area_q(3, 630, 45, 'A train travels 45 miles each hour. How many hours will it take to go 630 miles?',
        ' hours', 'Find 630 %s 45. Start with 45 %s 10.' % (D, X), 'Check: 45 miles %s your answer must make 630.' % X),
]

go(3, 'Divide with Area Models and Properties', [
 ('Area model for division',
  '**A rectangle shows a division: the area is the dividend, one side is the divisor, and the missing side is the quotient.**\n'
  '• 476 %s 14: area 476, side 14, missing side 34.' % D,
  'Area %s known side = missing side.' % D),
 ('Missing side',
  '**To find a missing side, divide the area by the side you know.**\n'
  '• 14 %s w = 476, so w = 476 %s 14.' % (X, D),
  'Division undoes the multiplying.'),
 ('Tens first',
  '**Estimate how many tens are in the quotient before anything else.**\n'
  '• 312 %s 13: 13 %s 20 = 260 fits, 13 %s 30 = 390 does not, so 2 tens.' % (D, X, X),
  'The biggest ten that still fits.'),
 ('Then what is left',
  '**Subtract the first piece, then find how many more groups fit.**\n'
  '• 312 %s 260 = 52, and 13 %s 4 = 52, so 4 more.' % (MINUS, X),
  'Take away, then share what remains.'),
 ('The Distributive Property',
  '**Split the missing side into tens and ones, and the pieces of area add back to the whole.**\n'
  '• 364 = 14 %s 20 + 14 %s 6 = 14 %s (20 + 6), so 364 %s 14 = 26.' % (X, X, X, D),
  'Two pieces, one rectangle.'),
 ('Add the parts, never side by side',
  '**The quotient is the tens part PLUS the ones part.**\n'
  '• 20 and 8 make 28, not 208.',
  'Plus, not next to.'),
 ('Check with multiplication',
  '**Divisor %s quotient should give back the area.**\n'
  '• 18 %s 31 = 540 + 18 = 558.' % (X, X),
  'Undo it to check it.'),
 ('Answer the real question',
  '**In a word problem, the quotient is often a step, not the answer.**\n'
  '• Find the width, then decide whether it fits the space.',
  'Read the question again before you write the answer.', None, 'added'),
], L3,
 'Lesson 5-3 practice pages: using area models, place value and the Distributive Property to divide by two-digit divisors, and multiplying to check.',
 'The area model shows WHY division works in tens and ones. Partial quotients and long division, next in the unit, are this same model written in a column.',
 [('Use an area model to divide by a two-digit divisor', 'source'),
  ('Use the Distributive Property to break a quotient into tens and ones', 'source'),
  ('Check a quotient by multiplying', 'source'),
  ('Use a quotient to answer a word problem\'s real question', 'added')],
 'Built from the lesson 5-3 practice pages in her Unit 5 folder, read for what they ask. The numbers are fresh, not the page\'s own. The slip most worth a word is writing the two parts of the side next to each other (20 and 8 as 208 instead of 28); one question shows a student doing exactly that. The other wrong options stop after the tens piece or count one group too many. One question shows a check that is right, because a good critique says so when an answer holds up.',
 ('Tens first, then what is left, then add the parts and multiply back.', 13))

print('divisions asked:', len(USED), '— none from the practice pages')
