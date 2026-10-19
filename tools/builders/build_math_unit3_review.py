# -*- coding: utf-8 -*-
"""River's Unit 3 · Test Review: Check Your Work (v189).

Chris forwarded the 4th-grade teacher's math update a second time on 10/19,
the day before the Unit 3 test (Tuesday 10/20), asking for the app to be
updated for it. Its assessment paragraph asks for two things, and they are the
whole of this unit:

  "When students are studying it is important that they are also studying how
   to double check their work. Students often know the skill, but will make
   simple calculation errors. If you are studying with them, give them a
   problem that is wrong and see if they can find the mistake."

So this is not a tenth lesson. It is the nine lessons' multiplication, served
as wrong answers to catch and products to check:

- **Find the mistake.** Each wrong answer is GENERATED from a named slip (the
  same helpers as build_math_unit3.py, copied so importing that builder does
  not rewrite its nine files): the dropped carry, each part's product written
  side by side, the second row missing its placeholder zero, a middle zero
  skipped, a power of ten losing a zero.
- **Check it four ways**, each with its own card: estimate, the ones digit,
  count the zeros, and undo it with division. A question asks which check
  catches a given wrong answer, and the wrong options are checks that would
  NOT catch it, so the item tests knowing what each check can see.
- Fresh numbers only. None of the textbook's (32 x 10,000, 26 x 3, 37 x 24,
  389 x 12, 208 x 31) or the nine lessons' own is reused.

Shelves last on the Unit 3 book on title alone ("Test" sorts after "Lesson"),
`prep:true` because it is built for a named test, `series:'Unit 3'`.
Her paper study guide (handed out Friday 10/16) is not in Drive, so the unit
is built from the update and the Unit 3 scan, and the note says so.
"""
import json, io
import unit_common as U

def f(n): return '{:,}'.format(n)

# ── the named slips (copied from build_math_unit3.py) ───────────────────────
def no_carry(a, m):
    ds = str(a); out, p = 0, 1
    for i, ch in enumerate(reversed(ds)):
        prod = int(ch) * m
        out += (prod if i == len(ds) - 1 else prod % 10) * p
        p *= 10
    return out

def side_by_side(a, m):
    return int(''.join(str(int(ch) * m) for ch in str(a)))

def no_placeholder(a, b):
    return a * (b % 10) + a * (b // 10)

def skip_zero(a):
    return int(str(a).replace('0', '', 1)) if '0' in str(a)[1:-1] else a

def opts4(ans, *wrong):
    o = [f(ans)] + [f(w) if isinstance(w, int) else w for w in wrong]
    assert len(o) == 4 and len(set(o)) == 4, o
    return o

BOOK = {(32, 10000), (26, 3), (37, 24), (389, 12), (208, 31)}
LESSONS = {(34, 5), (37, 4), (34, 26), (48, 52), (62, 285), (400, 63), (2085, 6),
           (38, 150), (45, 210)}
USED = []
def use(a, b):
    assert (a, b) not in BOOK | LESSONS and (b, a) not in BOOK | LESSONS, (a, b)
    USED.append((a, b)); return a * b

C, Q = [], []

# ══ cards ═══════════════════════════════════════════════════════════════════
U.card(C, 'Why check at all',
       '**Most mistakes on a multiplication test are slips, not "I do not know how".**\n'
       '• A carry forgotten, a zero left off, two numbers copied wrong.\n'
       '• A minute of checking catches most of them.',
       'Know the skill, then guard it.', frm='source')
U.card(C, 'Check 1 · Estimate',
       '**Round both numbers and multiply. The real answer should be close.**\n'
       '• 68 × 42 → 70 × 40 = 2,800. An answer of 286 or 28,560 is far off.\n'
       '• An estimate catches a lost or extra place, not a small slip.',
       'Too big or too small by a lot? Something went wrong.', frm='added')
U.card(C, 'Check 2 · The ones digit',
       '**The ones digit of the answer comes only from the two ones digits.**\n'
       '• 46 × 23: 6 × 3 = 18, so the answer must end in 8.\n'
       '• If your answer ends in anything else, there is a slip.',
       'Last digits make the last digit.', frm='added')
U.card(C, 'Check 3 · Count the zeros',
       '**When you multiply by 10, 100 or 1,000, count the zeros on both sides.**\n'
       '• 60 × 4,000: one zero plus three zeros is four zeros: 240,000.\n'
       '• If the basic fact already ends in 0 (5 × 8 = 40), that zero is extra.',
       'Zeros in, zeros out, plus any the fact makes.', frm='added')
U.card(C, 'Check 4 · Undo it',
       '**Division undoes multiplication: divide your answer by one factor, and you should get the other.**\n'
       '• 125 × 8 = 1,000, so 1,000 ÷ 8 should be 125.',
       'Multiply forward, divide back.', frm='added')
U.card(C, 'Slip · The dropped carry',
       '**Writing only the ones digit of a step and forgetting to carry the tens.**\n'
       '• 47 × 6: 7 × 6 = 42, write 2, carry 4. 4 × 6 = 24, plus 4 is 28. Answer 282.\n'
       '• Forgetting the carry gives 242.',
       'Every carry has to be added somewhere.', frm='added')
U.card(C, 'Slip · Side by side',
       '**Writing each part\'s whole product next to the others instead of adding by place.**\n'
       '• 38 × 4: 3 × 4 = 12 and 8 × 4 = 32 written as 1,232. The real answer is 152.',
       'Products go in place value, not in a row.', frm='added')
U.card(C, 'Slip · The missing zero',
       '**In the second row of a 2-digit multiplication you are multiplying by TENS, so it needs a 0 in the ones place.**\n'
       '• 43 × 27: 43 × 7 = 301, and 43 × 20 = 860, not 86.\n'
       '• 301 + 860 = 1,161. Forgetting the zero gives 387.',
       'The tens row starts with a zero.', frm='added')
U.card(C, 'Slip · Skipping a zero',
       '**A zero inside a number still holds a place.**\n'
       '• 507 × 6 is 3,042. Treating 507 like 57 gives 342.',
       'Zeros hold places, even when they make nothing.', frm='added')
U.card(C, 'Find the mistake',
       '**Redo the problem step by step and compare each line with the one written.**\n'
       '• The first line that does not match is where the mistake is.\n'
       '• Then name it: a carry, a zero, a wrong fact, or a split that does not add up.',
       'Find the first line that differs.', frm='source')
U.card(C, 'Show your work',
       '**Write every row, every carry and every partial product.**\n'
       '• Work you can see is work you can check, and homework is marked on it.',
       'If it is not written, it cannot be checked.', frm='source')

# ══ questions ═══════════════════════════════════════════════════════════════
SLIP = ['They forgot to add a carry', 'They wrote each part\'s product side by side',
        'They left the zero off the second row', 'They skipped the zero inside a number']

# — find the mistake, one per named slip (two numbers each) —
for who, a, m in (('Jada', 47, 6), ('Ben', 58, 7)):
    p, w = use(a, m), no_carry(a, m)
    assert w != p
    U.q(Q, 2, '%s worked out %d × %d and wrote %s. What went wrong?' % (who, a, m, f(w)), SLIP, 0,
        'Work the ones step and look at what it carries.',
        ['%d × %d = %d: write %d and carry %d.' % (a % 10, m, (a % 10) * m, (a % 10) * m % 10, (a % 10) * m // 10),
         '%d × %d = %d, plus the carried %d is %d.' % (a // 10, m, (a // 10) * m, (a % 10) * m // 10, (a // 10) * m + (a % 10) * m // 10),
         'So %d × %d = %s, not %s.' % (a, m, f(p), f(w)),
         'The carry was dropped.'],
        '**They forgot to add a carry.** %d × %d is %s.' % (a, m, f(p)),
        'Check the ones digit too: it is right, which is why only the carry is wrong.', frm='added')

for who, a, m in (('Leo', 38, 4), ('Mia', 29, 6)):
    p, w = use(a, m), side_by_side(a, m)
    assert w != p
    U.q(Q, 2, '%s worked out %d × %d and wrote %s. What went wrong?' % (who, a, m, f(w)), SLIP, 1,
        'Look at the two parts and where they were written.',
        ['%d × %d = %d and %d × %d = %d.' % (a // 10, m, (a // 10) * m, a % 10, m, (a % 10) * m),
         'Those were written next to each other: %s.' % f(w),
         'The tens part is %d tens, so add by place: %d + %d = %d.' % ((a // 10) * m, (a // 10) * m * 10, (a % 10) * m, p),
         'They wrote the products side by side.'],
        '**They wrote each part\'s product side by side.** %d × %d is %s.' % (a, m, f(p)),
        'An estimate catches it fast: %d × %d is near %s, not %s.' % (a, m, f(round(a, -1) * m), f(w)), frm='added')

for who, a, b in (('Sam', 43, 27), ('Ava', 52, 36)):
    p, w = use(a, b), no_placeholder(a, b)
    assert w != p
    r1, r2 = a * (b % 10), a * (b // 10) * 10
    U.q(Q, 3, '%s worked out %d × %d and wrote %s. What went wrong?' % (who, a, b, f(w)), SLIP, 2,
        'What should the second row be worth?',
        ['First row: %d × %d = %s.' % (a, b % 10, f(r1)),
         'Second row: %d × %d = %s. It is multiplying by tens.' % (a, (b // 10) * 10, f(r2)),
         '%s + %s = %s.' % (f(r1), f(r2), f(p)),
         'They wrote %s instead of %s, leaving off the zero.' % (f(a * (b // 10)), f(r2))],
        '**They left the zero off the second row.** %d × %d is %s.' % (a, b, f(p)),
        'The estimate %d × %d = %s shows %s is far too small.' % (round(a, -1), round(b, -1), f(round(a, -1) * round(b, -1)), f(w)), frm='added')

for who, a, m in (('Noah', 507, 6), ('Zoe', 803, 4)):
    p, w = use(a, m), skip_zero(a) * m
    assert w != p
    U.q(Q, 2, '%s worked out %d × %d and wrote %s. What went wrong?' % (who, a, m, f(w)), SLIP, 3,
        'Look at the middle digit of %d.' % a,
        ['%d has a 0 in the tens place.' % a,
         '%s is what %d × %d makes, so the zero was skipped.' % (f(w), skip_zero(a), m),
         'Hundreds: %d × %d = %d hundreds. Tens: 0. Ones: %d × %d = %d.' % (a // 100, m, (a // 100) * m, a % 10, m, (a % 10) * m),
         'So %d × %d = %s.' % (a, m, f(p))],
        '**They skipped the zero inside a number.** %d × %d is %s.' % (a, m, f(p)),
        'Estimate: %d × %d is about %s, so %s is too small.' % (a, m, f(round(a, -2) * m), f(w)), frm='added')

# — which check catches it —
assert 68 * 42 == 2856 and use(68, 42) == 2856
U.q(Q, 3, 'Ana says 68 × 42 = 286. Which quick check shows her answer is wrong?',
    ['Estimate: 70 × 40 = 2,800, so 286 is far too small',
     'The ones digit: 8 × 2 = 16, so the answer cannot end in 6',
     'It is even, but 68 × 42 has to be odd',
     'Undo it: 286 ÷ 2 should be 68'], 0,
    'Which check looks at the size of the answer?',
    ['286 ends in 6, and 8 × 2 = 16 does end in 6, so the ones digit looks fine.',
     '68 and 42 are both even, so an even answer is fine too.',
     'Estimate: 70 × 40 = 2,800.', '286 is about ten times too small, so the estimate catches it.'],
    '**The estimate.** 70 × 40 = 2,800, and 286 is nowhere near it.',
    'A ones-digit check cannot see a missing place. An estimate can.', frm='added')

assert use(46, 23) == 1058
U.q(Q, 1, 'Without working out the whole problem, what must the ones digit of 46 × 23 be?',
    ['8', '3', '6', '9'], 0,
    'Multiply only the two ones digits.',
    ['The ones digits are 6 and 3.', '6 × 3 = 18.', 'The ones digit of 18 is 8.', 'So 46 × 23 must end in 8.'],
    '**8.** 6 × 3 = 18, and only that step reaches the ones place. (46 × 23 = 1,058.)',
    'If your answer does not end in 8, look for the slip.', frm='added')

assert use(54, 37) == 1998
U.q(Q, 2, 'Eli says 54 × 37 = 2,008. Which quick check shows it is wrong?',
    ['The ones digit: 4 × 7 = 28, so the answer cannot end in 8',
     'It is even, but 54 × 37 has to come out odd',
     'Undo it: 2,008 ÷ 37 should come out to 54, and it does not',
     'Estimate: 50 × 40 = 2,000, so 2,008 is far too big'], 2,
    'The answer is close to the estimate and ends in 8. What is left?',
    ['2,008 ends in 8, and 4 × 7 = 28 ends in 8, so the ones check passes.',
     'Estimate: 50 × 40 = 2,000. 2,008 is close, so the estimate passes too.',
     'Undo it: 37 × 54 is 1,998, so 2,008 ÷ 37 does not come out to 54.',
     'Only undoing it, or redoing it carefully, catches this one.'],
    '**Undo it.** 54 × 37 = 1,998, so 2,008 cannot be right, even though it ends in 8 and is near the estimate.',
    'A small slip can pass the quick checks. That is why you also redo it line by line.', frm='added')

# — count the zeros —
assert use(60, 4000) == 240000
U.q(Q, 2, 'Leo wrote 60 × 4,000 = 24,000. What went wrong?',
    ['He lost one of the zeros: the answer is 240,000',
     'He added an extra zero: the answer is 2,400',
     'He used the wrong fact: 6 × 4 is 20',
     'Nothing: 24,000 is right'], 0,
    'Count the zeros in 60 and in 4,000.',
    ['6 × 4 = 24.', '60 has one zero, 4,000 has three: four zeros.', 'Put four zeros after 24: 240,000.',
     '24,000 has only three, so one zero was lost.'],
    '**He lost a zero.** 60 × 4,000 = 240,000.',
    'Count zeros in, then make sure the same number come out.', frm='added')

assert use(50, 800) == 40000
U.q(Q, 3, 'What is 50 × 800?',
    opts4(40000, 4000, 400000, 4800), 0,
    'The fact 5 × 8 already makes a zero.',
    ['5 × 8 = 40.', '50 and 800 have three zeros between them.', 'Put three zeros after 40: 40,000.',
     'The zero in 40 is extra, on top of the three.'],
    '**40,000.** 5 × 8 = 40, then three more zeros.',
    'Writing 4,000 means the zero inside 40 was treated as one of the three.', frm='added')

# — undo it —
assert use(125, 8) == 1000
U.q(Q, 1, 'Jo found that 125 × 8 = 1,000. Which fact checks it?',
    ['1,000 ÷ 8 = 125', '1,000 − 8 = 125', '125 + 8 = 1,000', '1,000 ÷ 125 = 9'], 0,
    'What undoes multiplying?',
    ['Division undoes multiplication.', 'Divide the answer by one factor: 1,000 ÷ 8.',
     'If you get the other factor, 125, the product checks.', 'So the check is 1,000 ÷ 8 = 125.'],
    '**1,000 ÷ 8 = 125.** Dividing gives back the other factor.',
    '1,000 ÷ 125 would also work, but it equals 8, not 9.', frm='added')

# — pick the right product among real slips —
for a, m, lv in ((76, 8, 1), (409, 7, 2)):
    p = use(a, m)
    wrong = [w for w in (no_carry(a, m), side_by_side(a, m), skip_zero(a) * m) if w != p]
    wrong = list(dict.fromkeys(wrong))
    while len(wrong) < 3: wrong.append(p + 10 * (len(wrong) + 1))
    U.q(Q, lv, 'What is %d × %d?' % (a, m), opts4(p, *wrong[:3]), 0,
        'Multiply each place and carry.',
        ['%d × %d = %d.' % (a % 10, m, (a % 10) * m),
         'Write the ones digit and carry the rest.',
         'Multiply the next place and add the carry.',
         '%d × %d = %s.' % (a, m, f(p))],
        '**%s.**' % f(p),
        'Estimate: %d × %d is near %s.' % (a, m, f(round(a, -1) * m)), frm='added')

for a, b in ((312, 19), (64, 35)):
    p = use(a, b); w1 = no_placeholder(a, b); w2 = p * 10; w3 = a * b - a
    assert len({p, w1, w2, w3}) == 4
    est = round(a, -2 if a >= 100 else -1) * round(b, -1)
    U.q(Q, 2, 'Which answer is correct for %d × %d?' % (a, b), opts4(p, w1, w2, w3), 0,
        'Estimate first, then check the ones digit.',
        ['Estimate: about %s.' % f(est),
         'The ones digit must come from %d × %d = %d.' % (a % 10, b % 10, (a % 10) * (b % 10)),
         '%s is near the estimate and ends in %d.' % (f(p), p % 10),
         'So %d × %d = %s.' % (a, b, f(p))],
        '**%s.** It is the only option that is near %s and ends in the right digit.' % (f(p), f(est)),
        '%s is the missing-zero slip, and %s has one place too many.' % (f(w1), f(w2)), frm='added')

# — story problems: is it reasonable —
assert use(24, 36) == 864
U.q(Q, 2, 'A school orders 24 boxes of markers with 36 markers in each box. Sam says that is 864 markers. Is that reasonable?',
    ['Yes: 24 × 36 = 864, and 20 × 40 = 800 is close',
     'No: it should be 24 + 36 = 60 markers',
     'No: 864 is too big, since 20 × 30 is only 600',
     'Yes: any answer in the hundreds is fine'], 0,
    'Estimate with numbers that are easy to multiply.',
    ['24 is about 20 and 36 is about 40.', '20 × 40 = 800.', '864 is close to 800.',
     'Exact check: 24 × 36 = 864, so Sam is right.'],
    '**Yes.** 24 × 36 = 864, close to the estimate of 800.',
    'Rounding both down to 20 × 30 gives a low estimate, so 864 being bigger is expected.', frm='added')

assert use(18, 25) == 450
U.q(Q, 3, 'A theater has 18 rows with 25 seats in each row. Priya says, "18 × 25 = 450, and 20 × 25 = 500, so 450 makes sense." Does her check make sense?',
    ['Yes: she rounded 18 up to 20, so the real answer should be a little less than 500',
     'No: rounding 18 up means the real answer must be more than 500',
     'No: she should have added 18 and 25 to check her answer instead',
     'No: an estimate and the real answer have to come out exactly equal'], 0,
    'She rounded 18 up. Should the real answer be bigger or smaller?',
    ['18 was rounded UP to 20.', 'So 20 × 25 = 500 is an overestimate.',
     'The real answer should be a little less than 500.', '450 is a little less, so her check makes sense.'],
    '**Yes.** Rounding 18 up makes 500 an overestimate, and 450 sits just under it.',
    'Knowing which way you rounded tells you which side of the estimate to expect.', frm='added')

assert len(Q) == 20, len(Q)
for x in Q:
    assert len(set(x['opts'])) == 4

U.build('wayfinder', C, Q, 'unit-m3-review', 'Unit 3 · Test Review: Check Your Work', 'math',
        'A test review for Unit 3: finding the mistake in a wrong multiplication, and four quick ways to check your own answer before you hand it in.',
        'Your teacher says most mistakes on this test are simple slips, not missing skills. Catching your own slip before the test does is the whole skill here.',
        [('Find and name the mistake in a wrong multiplication.', 'source'),
         ('Check an answer with an estimate, the ones digit, the zeros, or division.', 'source'),
         ('Decide whether an answer to a story problem is reasonable.', 'added')],
        ('Built from the teacher\'s math update for the Unit 3 test on Tuesday 10/20. She asks families to practise '
         'double-checking and to "give them a problem that is wrong and see if they can find the mistake", so this '
         'review is mostly that: twelve find-the-mistake and which-check-catches-it items, plus products to choose '
         'and two story problems. Every wrong answer comes from a named slip (a dropped carry, products written side '
         'by side, the missing zero in the second row, a skipped zero, a lost zero with powers of ten). Her paper study '
         'guide (handed out Friday 10/16) is not in Drive, so this does not mirror it; it uses fresh numbers on the nine '
         'lessons\' skills. Worth approving today if she is to see it before the test.'),
        ('Take one round tonight, and for every mistake you catch, say out loud which check found it.', 12),
        'content/math-u3-review.json', 'Teacher\'s math update, 10/15', 'Math update (teacher) and the Unit 3 textbook scan',
        offset_hours=2, round_=10)

fp = '%s/content/math-u3-review.json' % U.REPO
j = json.load(io.open(fp, encoding='utf-8'))
rec = j['records']['unit-m3-review']
rec.update(series='Unit 3', prep=True, libv=1, quarter=2)
io.open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('review:', len(C), 'cards,', len(Q), 'questions; numbers', USED)
