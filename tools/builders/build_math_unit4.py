# -*- coding: utf-8 -*-
"""River's Unit 4 — multiplying decimals (enVision grade-5, Topic 4, lessons
4-1 to 4-4). Her class teaches this unit AFTER Unit 5.

Same shape as the Unit 5 lessons (build_math_unit5.py): one lesson per unit
record, shelved on the `Unit 4` book with `series`, `round:10`, no `order`, no
`prep`. Source: her `4-1_` to `4-4_ Student Edition Practice.pdf` pages
(Drive, `Unit 4 - Math`, uploaded 11/16), read for what they ASK — never for
her answers. Each title is the page's Essential Question shortened into the
skill it names:
  4-1 "What Patterns Can Help You Multiply Decimals by Powers of 10?"
  4-2 "What Are Some Ways to Estimate Products of Decimals and Whole Numbers?"
  4-3 "How Can You Model Multiplying a Decimal by a Whole Number?"
  4-4 "How Do You Multiply a Decimal by a Whole Number?"

Nothing is worked by hand. Every product is computed below with Decimal (a
float would print 0.1 × 3 as 0.30000000000000004), and every WRONG option on
a "What is a × b?" question comes from a named slip, asserted not to equal
the real product. `use()` refuses every multiplication printed on any of the
four pages: they were read for shape only.
"""
import json, io, os, sys
from decimal import Decimal as Dm, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unit_common as U

X, MINUS = '×', '−'
SUP = {1: '¹', 2: '²', 3: '³', 4: '⁴'}

def d(x): return x if isinstance(x, Dm) else Dm(str(x))

def f(x):
    """Plain decimal with thousands commas and no trailing zeros: 3630.0 → 3,630."""
    s = format(d(x).normalize(), 'f')
    if '.' in s:
        i, frac = s.split('.')
        frac = frac.rstrip('0')
    else:
        i, frac = s, ''
    neg = i.startswith('-'); i = i.lstrip('-')
    i = '{:,}'.format(int(i))
    return ('-' if neg else '') + i + ('.' + frac if frac else '')

def places(x):
    s = format(d(x).normalize(), 'f')
    return len(s.split('.')[1]) if '.' in s else 0

def p10(n): return '10' + SUP[n]

# Every multiplication printed on the four practice pages, as an unordered pair.
def pair(a, b): return frozenset([d(a).normalize(), d(b).normalize()])
BOOK = set(pair(a, b) for a, b in [
    # 4-1
    (1.275, 10), (1.275, 100), (1.275, 1000), (26.014, 10), (26.014, 100), (26.014, 1000),
    (0.4, 10), (0.4, 100), (0.4, 1000), (363, 10), (363, 100), (363, 1000),
    (3.63, 10), (3.63, 100), (3.63, 1000), (4.58, 1000), (0.009, 10), (3.1, 1000),
    (42.3, 10), (42.3, 100), (0.062, 100), (1.24, 10000), (0.086, 10), (0.086, 100),
    (0.086, 1000), (63.7, 10), (563.7, 100), (0.365, 10000), (5.02, 100), (94.6, 1000),
    (0.9463, 100), (0.678, 100), (681.7, 10000), (0.629, 100), (0.056, 10000),
    (0.123, 10), (0.008, 100), (0.011, 100), (0.0025, 100), (0.004, 100), (0.0075, 100),
    (0.43, 10), (9.5, 10), (4.82, 1000), (4.82, 100), (0.482, 10), (0.482, 1000),
    (48.2, 10000), (0.37, 100), (0.037, 100), (3.7, 100),
    # 4-2
    (2.15, 16), (2.15, 20), (2, 20), (2, 15), (3.95, 18), (105, 0.75), (105, 1), (100, 0.8),
    (0.87, 112), (104, 0.33), (9.02, 80), (0.54, 24), (33.05, 200), (0.79, 51),
    (0.12, 105), (45.3, 4), (99.2, 82), (37, 0.93), (1.67, 4), (3.2, 184), (12, 0.37),
    (0.904, 75), (12.50, 5), (1.95, 10), (12.50, 4), (18.8, 1.28), (39.45, 1.7),
    (27.54, 0.74), (9.91, 8.74), (78.95, 1.26), (18.19, 2.28), (11.6, 9.5), (4.49, 8.3),
    (12.9, 0.9), (0.62, 1.5), (8.46, 7.38), (23.7, 4), (21.8, 4),
    # 4-3
    (4, 0.36), (5, 1.27), (0.8, 4), (0.7, 3), (0.5, 6), (0.6, 5), (0.55, 3), (0.45, 2),
    (5, 0.5), (4, 0.27), (6, 0.13), (0.78, 5), (10, 0.32), (6, 2.03), (1.35, 5),
    (100, 0.12), (4, 0.15), (3, 2.5), (0.9, 7), (0.35, 3), (3, 1.25), (3, 12.5),
    (5, 0.50), (9, 0.989),
    # 4-4
    (0.15, 12), (0.15, 24), (0.33, 19), (3.3, 19), (9.8, 2), (0.67, 8), (34, 5.3), (4.6, 21),
    (0.6, 15), (55, 1.1), (34.6, 9), (64.2, 20), (40, 0.22), (57, 2.3), (5.8, 11),
    (56, 0.4), (170, 0.003), (0.3, 99), (26, 1.61), (50, 0.914), (10.76, 100), (2.54, 12),
    (0.07, 956), (18.4, 2), (5.5, 1), (5.5, 9), (75, 3), (75, 0.3), (7.5, 3), (75, 0.03),
    (50, 12), (50, 0.12), (0.5, 12), (50, 1.2),
])
USED = set()

def use(a, b):
    """Every multiplication a question asks goes through here, so none of the
    practice pages' own problems can slip back in."""
    k = pair(a, b)
    assert k not in BOOK, ('reuses the practice page', a, b)
    USED.add(k)
    return d(a) * d(b)

def opts4(ans, *wrong):
    o = [ans] + list(wrong)
    assert len(o) == 4 and len(set(o)) == 4, o
    return o

def one_true(stmts):
    """stmts: list of (a, b, claimed). Exactly one is true, and it is the first."""
    hits = [i for i, (a, b, c) in enumerate(stmts) if d(a) * d(b) == d(c)]
    assert hits == [0], (stmts, hits)
    for a, b, c in stmts: use(a, b)
    return ['%s %s %s = %s' % (f(a), X, f(b), f(c)) for a, b, c in stmts]

def one_false(stmts):
    """Exactly one of stmts is FALSE, and it is the first."""
    miss = [i for i, (a, b, c) in enumerate(stmts) if d(a) * d(b) != d(c)]
    assert miss == [0], (stmts, miss)
    for a, b, c in stmts: use(a, b)
    return ['%s %s %s = %s' % (f(a), X, f(b), f(c)) for a, b, c in stmts]

def rnd(x, q='1'):
    return d(x).quantize(Dm(q), rounding=ROUND_HALF_UP)

CLS, APP, SERIES = 'math', 'wayfinder', 'Unit 4'
SRC = 'enVision Topic 4 Student Edition practice pages — multiplying decimals (Drive)'

def go(n, title, cards, qs, summary, why, objs, note, nxt):
    C, Q = [], []
    for a in cards: U.card(C, *a)
    for a in qs: U.q(Q, *a)
    slug, uid = 'math-u4-l%d' % n, 'unit-m4u%d' % n
    U.build(APP, C, Q, uid, '%s · Lesson %d: %s' % (SERIES, n, title), CLS,
            summary, why, objs, note, nxt, 'content/%s.json' % slug,
            'Lesson 4-%d Student Edition practice pages (Drive)' % n, SRC,
            offset_hours=3, round_=10)
    fp = '%s/content/%s.json' % (U.REPO, slug)
    j = json.load(io.open(fp, encoding='utf-8'))
    rec = j['records'][uid]
    rec['series'] = SERIES
    rec['libv'] = 1
    rec['quarter'] = 2
    io.open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))

# ══ Lesson 1 · Powers of 10 ══════════════════════════════════════════════════
# Named slips for a × 10ⁿ.
def s_left(x, n):  return d(x) / (10 ** n)          # moved the point the wrong way
def s_few(x, n):   return d(x) * (10 ** (n - 1))    # one place too few
def s_many(x, n):  return d(x) * (10 ** (n + 1))    # one place too many
def s_times(x, n): return d(x) * (10 * n)           # read 10ⁿ as 10 × n
N1 = {s_left: 'the point moved the wrong way, to the left',
      s_few: 'the point moved one place too few',
      s_many: 'the point moved one place too many',
      s_times: 'the exponent read as "times %d", so 10%s became %d'}

def pow_q(lv, x, n, slips, hint, tip, word='%s'):
    ans = use(x, 10 ** n)
    vals = [fn(x, n) for fn in slips]
    for v in vals: assert v != ans, (x, n, v)
    wrong = [f(v) for v in vals]
    names = [(N1[fn] % (n, SUP[n], 10 * n)) if fn is s_times else N1[fn] for fn in slips]
    why = '; '.join('%s is %s' % (w, nm) for w, nm in zip(wrong, names))
    steps = ['%s = %s, so the decimal point moves %d place%s to the right.' % (p10(n), f(10 ** n), n, '' if n == 1 else 's'),
             'Move it one place at a time: %s.' % ' → '.join(f(d(x) * 10 ** k) for k in range(n + 1)),
             'Multiplying by %s makes a number bigger, so %s makes sense.' % (f(10 ** n), f(ans))]
    return (lv, 'What is %s %s %s?' % (f(x), X, p10(n)), opts4(f(ans), *wrong), 0, hint, steps,
            '**%s.** %s has %d zero%s, so the point moves %d place%s right. The wrong answers come from real slips: %s.' % (
                f(ans), f(10 ** n), n, '' if n == 1 else 's', n, '' if n == 1 else 's', why), tip)

use(0.48, 1000); assert d('0.48') * 1000 == 480
use(5.06, 1000); assert d('5.06') * 1000 == 5060
use(0.6, 10); assert d('0.6') * 10 == 6
assert d('2.5') / 100 == d('0.025')
assert d('4.5') * 10 - d('4.5') == d('40.5')
Q1T = one_true([('6.15', 100, '615'), ('6.15', 1000, '61500'), ('0.615', 10, '61.5'), ('61.5', 1000, '6150')])

L1 = [
 (1, 'When you multiply a decimal by %s, which way does the decimal point move, and how far?' % p10(3),
  ['3 places to the right', '3 places to the left', '1 place to the right',
   'It stays put, and you write three zeros on the end'], 0,
  'Multiplying by a power of 10 makes a number bigger. Count the zeros in 1,000.',
  ['%s = 1,000, which has 3 zeros.' % p10(3), 'Each 10 moves the point one place.',
   'Bigger means the digits move left, so the point moves right.', 'So the point moves 3 places to the right.'],
  '**3 places to the right.** %s is 1,000, which has 3 zeros. Writing zeros after the last digit, 2.5 → 2.5000, changes nothing.' % p10(3),
  'Count the exponent or the zeros: that is how many places.'),
 (1, 'What does %s mean?' % p10(2),
  ['10 %s 10, which is 100' % X, '10 %s 2, which is 20' % X, '10 + 2, which is 12', '2 %s 10 %s 10, which is 200' % (X, X)], 0,
  'The small 2 says how many 10s are multiplied together.',
  ['The small raised number is the exponent.', 'It says how many 10s are multiplied.',
   '%s = 10 %s 10 = 100.' % (p10(2), X)],
  '**10 %s 10, which is 100.** The exponent counts the 10s; it is not a number to multiply by.' % X,
  'The exponent is a count of tens.'),
 (1, 'Mira\'s ribbon is 3.8 meters long. Theo\'s ribbon is 3.80 meters long. Whose ribbon is longer?',
  ['Neither: 3.8 and 3.80 are the same length', 'Theo\'s, because 380 is more than 38',
   'Mira\'s, because 3.8 has fewer digits to read', 'You cannot tell from these two numbers'], 0,
  'What is in the hundredths place of 3.8?',
  ['3.8 has 8 tenths and 0 hundredths.', '3.80 has 8 tenths and 0 hundredths too.',
   'A zero at the end, after the decimal point, does not change the value.', 'So the ribbons are the same length.'],
  '**Neither: they are the same length.** 3.80 just writes the 0 hundredths that 3.8 leaves out.',
  'Zeros at the end of a decimal do not change its value.'),
 (1, 'When a number is multiplied by 10, what happens to each digit?',
  ['It moves one place to the left and is worth 10 times as much', 'It moves one place to the right and is worth less',
   'It stays in its place and is worth 10 more', 'It stays in its place, and a zero joins the end'], 0,
  'Think of 4.2 × 10 = 42. Where did the 4 go?',
  ['In 4.2 the 4 is in the ones place.', 'In 42 the 4 is in the tens place.',
   'It moved one place left, so it is worth 10 times as much.'],
  '**Each digit moves one place left and is worth 10 times as much.** That is why the point seems to move right.',
  'The digits move; the point is just where it was.'),
 (1, '0.48 %s 10 to what power = 480?' % X,
  ['3', '2', '4', '1'], 0,
  'How many places did the point move to go from 0.48 to 480?',
  ['0.48 → 4.8 is one place.', '4.8 → 48 is two places.', '48 → 480 is three places.',
   'So the power is 3: 0.48 %s %s = 480.' % (X, p10(3))],
  '**3.** The point moves 3 places, so it is 10 %s 10 %s 10 = %s. 2 stops at 48, 4 goes on to 4,800, and 1 stops at 4.8.' % (X, X, p10(3)),
  'Count the moves, one place at a time.'),
 pow_q(2, '2.57', 2, [s_left, s_few, s_many], 'Count the zeros in 100.', 'Bigger, so the point moves right.'),
 pow_q(2, '0.064', 3, [s_left, s_few, s_many], 'The point moves 3 places. The zero in front stops mattering.', 'Leading zeros fall away as the number grows.'),
 pow_q(2, '13.8', 4, [s_left, s_few, s_many], 'Move the point 4 places. You will need to write zeros to fill the places.', 'Fill empty places with zeros as you move.'),
 pow_q(2, '7.3', 3, [s_left, s_few, s_times], '%s means 10 %s 10 %s 10, not 10 %s 3.' % (p10(3), X, X, X), 'The exponent counts places; it is not a factor.'),
 pow_q(2, '0.705', 2, [s_left, s_few, s_many], 'Watch the zero inside 0.705. It stays where it is.', 'A zero between digits never disappears.'),
 (2, '5.06 %s 10 to what power = 5,060?' % X,
  ['3', '2', '4', '1'], 0,
  'Count the places from 5.06 to 5,060.',
  ['5.06 → 50.6 is one place.', '50.6 → 506 is two places.', '506 → 5,060 is three places.',
   'So 5.06 %s %s = 5,060.' % (X, p10(3))],
  '**3.** Three moves of the point. 2 stops at 506, 4 goes on to 50,600, and 1 stops at 50.6.',
  'Count moves, not digits.'),
 (3, 'A magnifying lens makes things look 10 times their actual size. A ladybug is 0.6 cm long. How long does it look through the lens?',
  ['6 cm', '0.06 cm', '60 cm', '10.6 cm'], 0,
  'Find 0.6 %s 10.' % X,
  ['The lens multiplies the size by 10.', '0.6 %s 10: the point moves one place right.' % X,
   '0.6 → 6.', 'So it looks 6 cm long.'],
  '**6 cm.** 0.6 %s 10 = 6. 0.06 moves the point the wrong way, 60 moves it two places, and 10.6 adds 10 instead of multiplying.' % X,
  '"10 times" means multiply by 10, never add 10.'),
 (3, 'A microscope shows things at 100 times their actual size. Seen through it, a grain of pollen is 2.5 cm across. How big is it really?',
  ['0.025 cm', '250 cm', '0.25 cm', '25 cm'], 0,
  'The microscope multiplied by 100. To undo that, do the opposite.',
  ['Seen size = actual size %s 100.' % X, 'So actual size = seen size %s 100.' % '÷',
   'Dividing by 100 moves the point 2 places left: 2.5 → 0.25 → 0.025.', 'So the pollen is 0.025 cm across.'],
  '**0.025 cm.** The microscope multiplied by 100, so divide by 100 to undo it. 250 multiplies a second time, and 0.25 and 25 move the point the wrong number of places.',
  'Real things under a microscope are tiny. A huge answer is a sign you multiplied.'),
 (3, 'Which equation is true?',
  Q1T, 0,
  'Check each one by counting how many places the point should move.',
  ['6.15 %s 100: 2 places right is 615. True.' % X, '6.15 %s 1,000 is 6,150, not 61,500.' % X,
   '0.615 %s 10 is 6.15, not 61.5.' % X, '61.5 %s 1,000 is 61,500, not 6,150.' % X],
  '**6.15 %s 100 = 615.** Each of the others moves the point one place too many or one too few.' % X,
  'Count the zeros, then count the moves.'),
 (3, 'A rope is 4.5 meters long. A second rope is 10 times as long. How much longer is the second rope than the first?',
  ['40.5 meters', '45 meters', '49.5 meters', '4.05 meters'], 0,
  'First find the second rope\'s length. Then compare.',
  ['The second rope is 4.5 %s 10 = 45 meters.' % X, 'How much longer means subtract.',
   '45 %s 4.5 = 40.5.' % MINUS, 'So it is 40.5 meters longer.'],
  '**40.5 meters.** 4.5 %s 10 = 45, and 45 %s 4.5 = 40.5. 45 is the rope\'s length, not the difference, and 49.5 adds instead of subtracting.' % (X, MINUS),
  'Two steps: multiply, then subtract.'),
]

go(1, 'Multiply Decimals by Powers of 10', [
 ('Powers of 10',
  '**A power of 10 is 10 multiplied by itself: 10¹ = 10, 10² = 100, 10³ = 1,000.**\n'
  '• The small raised number, the exponent, counts the 10s.\n'
  '• It also equals the number of zeros.',
  'Exponent = number of zeros.'),
 ('Multiply by 10, 100, 1,000',
  '**Multiplying by a power of 10 moves the decimal point to the right, one place for each zero.**\n'
  '• 2.57 %s 100 = 257 (2 places).\n'
  '• 0.064 %s 1,000 = 64 (3 places).' % (X, X),
  'One zero, one place.'),
 ('Why the point moves',
  '**Really the digits move: each one shifts one place left and is worth 10 times as much.**\n'
  '• In 4.2 the 4 is ones; in 42 the 4 is tens.',
  'Digits left = point right.'),
 ('Filling with zeros',
  '**When the point runs past the last digit, write zeros to fill the empty places.**\n'
  '• 13.8 %s 10⁴ = 138,000.' % X,
  'Empty places get zeros.'),
 ('The exponent is not a factor',
  '**10³ means 10 %s 10 %s 10 = 1,000, never 10 %s 3 = 30.**\n'
  '• 7.3 %s 10³ is 7,300, not 219.' % (X, X, X, X),
  'Count the tens; do not multiply by the little number.'),
 ('Zeros at the end of a decimal',
  '**A zero after the last digit to the right of the point does not change the value.**\n'
  '• 3.8 = 3.80 = 3.800.',
  'Trailing zeros are just padding.'),
 ('Finding the missing exponent',
  '**Count how many places the point moved; that is the exponent.**\n'
  '• 0.48 → 480 moves 3 places, so it is %s 10³.' % X,
  'Count the moves.'),
 ('Bigger or smaller?',
  '**Multiplying by a power of 10 always makes a number bigger, so check that your answer grew.**\n'
  '• To undo it, divide, and the point moves left.\n'
  '• A microscope that shows 2.5 cm at %s 100 means the real thing is 0.025 cm.' % X,
  'Grew? Then you multiplied.'),
], L1,
 'Lesson 4-1 practice pages: using place-value patterns to multiply decimals by 10, 100, 1,000 and by powers of 10 written with exponents, finding a missing exponent, and word problems about magnified sizes.',
 'Multiplying by powers of 10 is the pattern the rest of the unit leans on: placing the decimal point in every later product uses the same idea.',
 [('Multiply a decimal by 10, 100, 1,000 or 10,000', 'source'),
  ('Read powers of 10 written with exponents', 'source'),
  ('Find a missing exponent from where the decimal point moved', 'source'),
  ('Explain why 3.8 and 3.80 are the same number', 'source')],
 'Built from the lesson 4-1 practice pages in her Unit 4 folder, read for what they ask. The numbers are fresh, not the page\'s own. Every wrong option on a worked product comes from a named slip: moving the point the wrong way, one place too few or too many, or reading 10³ as "10 times 3". The last one is the slip most worth a word, because 7.3 %s 30 gives a believable number. Her class teaches this unit after Unit 5.' % X,
 ('Count the zeros, move the point that many places right, then check that the number grew.', 12))

# ══ Lesson 2 · Estimate products ═════════════════════════════════════════════
def over_under(stmts, want_over):
    """Exactly one pair rounds (nearest whole number) to an estimate on the
    wanted side of the exact product; it is the first."""
    good = []
    for i, (a, b) in enumerate(stmts):
        est = rnd(a) * rnd(b); ex = d(a) * d(b)
        assert est != ex
        if (est > ex) == want_over: good.append(i)
        use(a, b)
    assert good == [0], (stmts, good)
    return ['%s %s %s' % (f(a), X, f(b)) for a, b in stmts]

OV = over_under([('5.7', '8.6'), ('3.2', '7.4'), ('9.1', '4.3'), ('6.4', '2.2')], True)
UN = over_under([('4.2', '6.3'), ('7.8', '3.6'), ('2.7', '5.9'), ('6.6', '3.8')], False)
use('3.86', 21); assert rnd('3.86') * 20 == 80
use('0.48', 205); assert d('0.5') * 200 == 100 and rnd('0.48') == 0
use('6.9', 42); assert 7 * 40 == 280 and 6 * 40 == 240
use('4.10', 19); assert 4 * 20 == 80 and 5 * 20 == 100
use('1.85', 28); assert 2 * 30 == 60 and 1 * 28 == 28
use('3.89', 12); assert 4 * 12 == 48 < 50 and d('3.89') * 12 < 48
use('12.4', 10); assert 12 * 2 * 5 == 120
use('0.76', 98); assert abs(d('0.75') * 100 - d('0.76') * 98) < abs(100 - d('0.76') * 98)
use('4.95', 31); assert 5 * 30 == 150

L2 = [
 (1, 'A question asks "about how much" something costs. What does that tell you?',
  ['An estimate is enough; you do not need the exact amount', 'You must find the exact amount, to the cent',
   'You should always round every number up', 'You should add the numbers instead of multiplying them'], 0,
  'What does "about" mean in everyday talk?',
  ['"About" means close to, not exactly.', 'So a rounded answer is what the question wants.',
   'You can round to numbers that are easy to multiply in your head.'],
  '**An estimate is enough.** "About how much" asks for a close, easy answer, not the exact one.',
  'Read the question first: it tells you whether to estimate.'),
 (1, 'Rounding each factor, which is the best estimate of 3.86 %s 21?' % X,
  ['80', '8', '800', '60'], 0,
  'Round 3.86 to the nearest whole number and 21 to the nearest ten.',
  ['3.86 rounds to 4.', '21 rounds to 20.', '4 %s 20 = 80.' % X],
  '**80.** 4 %s 20 = 80. 8 and 800 put the point in the wrong place, and 60 rounds 3.86 down to 3 when it is closer to 4.' % X,
  'Round to the nearest, not always down.'),
 (1, 'What are compatible numbers?',
  ['Numbers close to the real ones that are easy to multiply in your head', 'The exact numbers in the problem, copied out again',
   'Numbers rounded up, so the answer always comes out bigger', 'Any two numbers that add up to exactly 10'], 0,
  'Think of 2.15 %s 16 becoming 2 %s 15.' % (X, X),
  ['Compatible numbers are near the real numbers.', 'They are picked because they are easy to work with.',
   'They give a quick estimate, not an exact answer.'],
  '**Numbers close to the real ones that are easy to multiply.** They make a mental estimate quick.',
  'Pick numbers that make the arithmetic friendly.'),
 (1, 'You round both factors UP to estimate a product. What kind of estimate do you get?',
  ['An overestimate: more than the exact product', 'An underestimate: less than the exact product',
   'The exact product', 'It depends on whether the numbers are decimals'], 0,
  'If both numbers got bigger, what happens to their product?',
  ['Rounding up makes each factor bigger.', 'Bigger factors make a bigger product.',
   'So the estimate is more than the exact answer.'],
  '**An overestimate.** Both factors grew, so the product grew too.',
  'Both up means over; both down means under.'),
 (1, 'You round both factors DOWN to estimate a product. What kind of estimate do you get?',
  ['An underestimate: less than the exact product', 'An overestimate: more than the exact product',
   'The exact product', 'It depends on how big the numbers are'], 0,
  'If both numbers got smaller, what happens to their product?',
  ['Rounding down makes each factor smaller.', 'Smaller factors make a smaller product.',
   'So the estimate is less than the exact answer.'],
  '**An underestimate.** Both factors shrank, so the product shrank too.',
  'An underestimate tells you the real answer is at least that much.'),
 (2, 'Which is the best estimate of 0.48 %s 205?' % X,
  ['100', '10', '1,000', '0'], 0,
  'Rounding 0.48 to a whole number gives 0, which tells you nothing. Try 0.5 instead.',
  ['0.48 is close to 0.5, which is one half.', '205 is close to 200.', 'Half of 200 is 100.'],
  '**100.** 0.5 %s 200 = 100. 0 comes from rounding 0.48 to the nearest whole number, which throws the whole product away. 10 and 1,000 put the point in the wrong place.' % X,
  'For a decimal less than 1, round to a friendly decimal like 0.5, not to 0.'),
 (2, 'Which is the best estimate of 6.9 %s 42?' % X,
  ['280', '28', '2,800', '240'], 0,
  'Round 6.9 to the nearest whole number and 42 to the nearest ten.',
  ['6.9 rounds to 7.', '42 rounds to 40.', '7 %s 40 = 280.' % X],
  '**280.** 7 %s 40 = 280. 240 drops 6.9 to 6 instead of rounding it to 7, and 28 and 2,800 misplace the point.' % X,
  '6.9 is almost 7. Round it, do not chop it.'),
 (2, 'About how much do 19 notebooks cost at $4.10 each?',
  ['About $80', 'About $8', 'About $800', 'About $100'], 0,
  'Round $4.10 to the nearest dollar and 19 to the nearest ten.',
  ['$4.10 rounds to $4.', '19 rounds to 20.', '$4 %s 20 = $80.' % X],
  '**About $80.** $4 %s 20 = $80. $100 rounds $4.10 up to $5, which it is not close to.' % X,
  'Round each number to the nearest, then multiply.'),
 (2, 'Rounding each factor to the nearest whole number, which gives an OVERestimate?',
  OV, 0,
  'An overestimate needs the factors to round up.',
  ['5.7 rounds up to 6, and 8.6 rounds up to 9.', 'Both went up, so 6 %s 9 = 54 is more than the exact product.' % X,
   'In each of the others, both factors round down.', 'So only 5.7 %s 8.6 gives an overestimate.' % X],
  '**5.7 %s 8.6.** Both factors round up, so 6 %s 9 = 54 is more than the exact 49.02. Every other pair rounds both factors down.' % (X, X),
  'Look at the tenths: 5 or more rounds up.'),
 (2, 'Rounding each factor to the nearest whole number, which gives an UNDERestimate?',
  UN, 0,
  'An underestimate needs the factors to round down.',
  ['4.2 rounds down to 4, and 6.3 rounds down to 6.', 'Both went down, so 4 %s 6 = 24 is less than the exact product.' % X,
   'In each of the others, both factors round up.', 'So only 4.2 %s 6.3 gives an underestimate.' % X],
  '**4.2 %s 6.3.** Both factors round down, so 4 %s 6 = 24 is less than the exact 26.46. Every other pair rounds both factors up.' % (X, X),
  'Look at the tenths: 4 or less rounds down.'),
 (3, 'A school buys 28 folders at $1.85 each. About how much do they cost?',
  ['About $60', 'About $6', 'About $600', 'About $28'], 0,
  'Round $1.85 to the nearest dollar and 28 to the nearest ten.',
  ['$1.85 rounds to $2.', '28 rounds to 30.', '$2 %s 30 = $60.' % X],
  '**About $60.** $2 %s 30 = $60. $28 rounds $1.85 down to $1, and $6 and $600 misplace the point.' % X,
  'A price just under $2 is about $2.'),
 (3, 'Leo has $50. He wants 12 notebooks at $3.89 each. He rounds up: $4 %s 12 = $48. What does that tell him?' % X,
  ['He has enough, because even an overestimate is under $50', 'He does not have enough, because $48 is so close to $50',
   'He cannot tell until he finds the exact cost', 'He will spend exactly $48'], 0,
  'Is $48 more or less than the real cost?',
  ['$4 is more than $3.89, so $48 is an overestimate.', 'The real cost is less than $48.',
   '$48 is under $50, so the real cost is under $50 too.'],
  '**He has enough.** He rounded up, so the real cost is less than $48, and $48 is already under $50.',
  'An overestimate that fits means the real amount fits.'),
 (3, 'A gardener drives 12.4 miles to a park and 12.4 miles back, 5 days a week. About how many miles is that each week?',
  ['About 120 miles', 'About 60 miles', 'About 12 miles', 'About 1,200 miles'], 0,
  'Each day has two trips.',
  ['12.4 is about 12.', 'Two trips a day: 12 %s 2 = 24 miles.' % X, '5 days: 24 %s 5 = 120 miles.' % X],
  '**About 120 miles.** 12 %s 2 %s 5 = 120. 60 counts only the trip there, not the trip back.' % (X, X),
  'Count every trip the story mentions.'),
 (3, 'To estimate 0.76 %s 98, Mia uses 1 %s 100 = 100 and Ben uses 0.75 %s 100 = 75. Whose estimate is closer, and why?' % (X, X, X),
  ['Ben\'s, because 0.75 is much closer to 0.76 than 1 is', 'Mia\'s, because rounding to whole numbers is always closer',
   'Both are equally close, because they both used 100', 'Neither, because you cannot estimate with a decimal less than 1'], 0,
  'How far is 0.76 from 1? How far from 0.75?',
  ['0.76 is 0.24 away from 1.', '0.76 is only 0.01 away from 0.75.', 'The exact product is 74.48, very close to 75.'],
  '**Ben\'s.** 0.75 is almost exactly 0.76, so 75 is very close to the exact 74.48. Rounding 0.76 up to 1 overshoots by a quarter.',
  'A compatible number close to the real one gives a closer estimate.'),
 (3, 'Ana says 4.95 %s 31 is about 15. Which estimate shows she is wrong?' % X,
  ['5 %s 30 = 150, so the answer is near 150, not 15' % X, '5 + 30 = 35, so the answer is near 35',
   '4 %s 3 = 12, so 15 is close enough' % X, '5 %s 3 = 15, so she is right' % X], 0,
  'Round 4.95 and 31, then multiply.',
  ['4.95 rounds to 5.', '31 rounds to 30, not 3.', '5 %s 30 = 150.' % X, '15 is ten times too small.'],
  '**5 %s 30 = 150.** Her 15 treats 31 as if it were 3, so the point landed a place too far left.' % X,
  'An estimate catches a misplaced point.'),
]

go(2, 'Estimate Products of Decimals', [
 ('About how much',
  '**"About how much" means an estimate is enough.**\n'
  '• Round, multiply in your head, done.',
  'About = close, not exact.'),
 ('Estimate by rounding',
  '**Round each factor, then multiply.**\n'
  '• 3.86 %s 21 → 4 %s 20 = 80.' % (X, X),
  'Round to the nearest, not always down.'),
 ('Compatible numbers',
  '**Swap in nearby numbers that are easy to multiply.**\n'
  '• 0.76 %s 98 → 0.75 %s 100 = 75.\n'
  '• 0.48 %s 205 → 0.5 %s 200 = 100.' % (X, X, X, X),
  'Pick friendly numbers.'),
 ('Decimals less than 1',
  '**Do not round a decimal like 0.48 to 0; use a friendly decimal such as 0.5 or 0.25.**\n'
  '• Half of something is easy to find.',
  '0.5 is half; 0.25 is a quarter.'),
 ('Overestimate',
  '**If you round the factors up, your estimate is more than the exact product.**\n'
  '• Good for checking you have enough money.',
  'Both up, over.'),
 ('Underestimate',
  '**If you round the factors down, your estimate is less than the exact product.**\n'
  '• The real answer is at least that much.',
  'Both down, under.'),
 ('Using an estimate to decide',
  '**An overestimate that fits your budget means the real cost fits too.**\n'
  '• $4 %s 12 = $48 is under $50, so $3.89 %s 12 is too.' % (X, X),
  'Over and still fine means fine.'),
 ('Checking a product',
  '**Compare an exact answer with your estimate. If it is about 10 times too big or small, the point slipped.**\n'
  '• 4.95 %s 31 is near 150, so 15 is wrong.' % X,
  'Estimates catch misplaced points.'),
], L2,
 'Lesson 4-2 practice pages: estimating products of decimals and whole numbers by rounding or with compatible numbers, telling overestimates from underestimates, and estimating in money and distance word problems.',
 'Estimating first is how she will catch a decimal point in the wrong place in lessons 3 and 4.',
 [('Estimate a product of a decimal and a whole number by rounding', 'source'),
  ('Estimate with compatible numbers', 'source'),
  ('Tell whether an estimate is an overestimate or an underestimate', 'source'),
  ('Use an estimate to solve or check a word problem', 'source')],
 'Built from the lesson 4-2 practice pages in her Unit 4 folder, read for what they ask. The numbers are fresh, not the page\'s own. Two slips are worth a word: rounding a decimal less than 1 to 0 (0.48 %s 205 "about 0"), and chopping 6.9 down to 6 instead of rounding it to 7. Both are offered as wrong options. Her class teaches this unit after Unit 5.' % X,
 ('Round or pick friendly numbers, multiply in your head, and say whether you went over or under.', 12))

# ══ Lesson 3 · Model a decimal times a whole number ══════════════════════════
def m_whole(a, b):                                                     # decimal point left out
    w, x = (a, b) if d(a) == d(a).to_integral() else (b, a)
    return Dm(int(format(d(x).normalize(), 'f').replace('.', '')) * int(d(w)))
def m_big(a, b):    return d(a) * d(b) * 10                            # point one place too far right
def m_small(a, b):  return d(a) * d(b) / 10                            # point one place too far left
def m_add(a, b):    return d(a) + d(b)                                 # added instead of multiplied
def m_side(a, b):
    """Each place's product written side by side with no regrouping:
    4 × 1.36 → 4, 12, 24 → '4.1224'. Whole is the whole-number factor."""
    w, x = (a, b) if d(a) == d(a).to_integral() else (b, a)
    w = int(d(w)); s = format(d(x).normalize(), 'f'); ip, fp = s.split('.')
    return Dm(str(w * int(ip)) + '.' + ''.join(str(w * int(c)) for c in fp))
NM = {m_whole: 'the decimal point left out', m_big: 'the point one place too far right',
      m_small: 'the point one place too far left', m_add: 'adding instead of multiplying',
      m_side: 'each place\'s product written side by side, with no regrouping'}

def steps_mul(a, b, model=False):
    p = d(a) * d(b)
    w, x = (a, b) if d(a) == d(a).to_integral() else (b, a)
    digits = int(format(d(x).normalize(), 'f').replace('.', ''))
    est = (rnd(x, '0.1') if d(x) < 1 else rnd(x)) * d(w)
    out = []
    if model:
        out.append('%s %s %s means %s groups of %s.' % (f(w), X, f(x), f(w), f(x)))
    out.append('Multiply as whole numbers: %s %s %s = %s.' % (f(w), X, f(digits), f(digits * int(d(w)))))
    out.append('%s has %d decimal place%s, so the product has %d: %s.' % (
        f(x), places(x), '' if places(x) == 1 else 's', places(x),
        format(Dm(digits * int(d(w))).scaleb(-places(x)), 'f')))
    if est != 0 and est != p:
        r = rnd(x, '0.1') if d(x) < 1 else rnd(x)
        out.append('Check with an estimate: %s %s %s = %s, close to %s.' % (f(r), X, f(w), f(est), f(p)))
    else:
        out.append('So %s %s %s = %s.' % (f(w), X, f(x), f(p)))
    return out

def mul_q(lv, a, b, slips, hint, tip, model=False):
    ans = use(a, b)
    vals = [fn(a, b) for fn in slips]
    for v in vals: assert v != ans, (a, b, v)
    wrong = [f(v) for v in vals]
    why = '; '.join('%s is %s' % (w, NM[fn]) for w, fn in zip(wrong, slips))
    return (lv, 'What is %s %s %s?' % (f(a), X, f(b)), opts4(f(ans), *wrong), 0, hint, steps_mul(a, b, model),
            '**%s.** The wrong answers come from real slips: %s.' % (f(ans), why), tip)

use(3, '0.25'); assert 3 * d('0.25') == d('0.75')
use(7, '0.6'); assert 7 * d('0.6') < 7
use(7, '0.896'); assert 7 * d('0.896') == d('6.272')
use(4, '2.35'); assert 4 * d('2.35') == d('9.4')
use(3, '8'); use(3, '0.8'); assert 3 * 8 - 3 * d('0.8') == d('21.6')
use(6, '0.75'); assert 6 * 75 == 450
LT9 = []
for w, x in [(9, '0.8'), (9, '1.2'), (9, '2.5'), (9, '1.05')]:
    use(w, x); LT9.append((w, x))
assert [i for i, (w, x) in enumerate(LT9) if d(w) * d(x) < 9] == [0]
LT9 = ['%s %s %s' % (f(w), X, f(x)) for w, x in LT9]

L3 = [
 (1, 'In a place-value block model, one big flat square stands for 1. What does one small cube stand for?',
  ['0.01, because it takes 100 cubes to make the flat', '0.1, because it takes 10 cubes to make the flat',
   '1, because every block stands for 1', '100, because the flat holds 100 of them'], 0,
  'How many small cubes fit in one flat?',
  ['A flat is 10 rods, and a rod is 10 cubes.', 'So a flat is 100 cubes.', 'If the flat is 1, each cube is 1 hundredth, 0.01.'],
  '**0.01.** 100 cubes make the flat, so each cube is one hundredth. A rod of 10 cubes is 0.1.',
  'First decide which block is 1. Everything else follows.'),
 (1, 'What does 3 %s 0.42 mean?' % X,
  ['3 groups of 0.42, put together', '42 groups of 3, put together', '3 and 0.42 added together once', '0.42 taken away from 3, once'], 0,
  'Read %s as "groups of".' % X,
  ['3 %s 0.42 means 3 groups.' % X, 'Each group is 0.42.', '0.42 + 0.42 + 0.42 = 1.26.'],
  '**3 groups of 0.42.** Put together, they make 0.42 + 0.42 + 0.42 = 1.26.',
  'Multiplying a decimal by a whole number is repeated adding.'),
 (1, 'Without multiplying, is 7 %s 0.6 less than or greater than 7?' % X,
  ['Less, because you take less than one whole, 7 times', 'Greater, because multiplying always makes a number bigger',
   'Equal, because 0.6 is close to 1', 'Greater, because 6 is more than 1'], 0,
  'Is 0.6 more or less than 1?',
  ['0.6 is less than 1.', '7 groups of something less than 1 is less than 7 groups of 1.', '7 groups of 1 is 7, so 7 %s 0.6 is less than 7.' % X],
  '**Less.** 0.6 is less than one whole, so 7 of them make less than 7. (It is 4.2.)',
  'Times a decimal less than 1 makes a number smaller.'),
 (1, 'You combine some blocks and end up with 10 hundredths cubes. What can you trade them for?',
  ['1 tenth rod', '1 whole flat', '10 tenths rods', '100 tenths rods'], 0,
  'How many hundredths make a tenth?',
  ['10 hundredths = 1 tenth.', 'So 10 cubes make one rod.', 'Trading keeps the value the same and makes it easier to read.'],
  '**1 tenth rod.** 10 hundredths make 1 tenth, just as 10 ones make 1 ten.',
  'Regroup decimals the same way you regroup whole numbers.'),
 (1, 'A grid of 100 squares stands for 1. You shade 25 squares, three times, in three colors. Which equation matches?',
  ['3 %s 0.25 = 0.75' % X, '3 %s 25 = 75' % X, '0.3 %s 25 = 7.5' % X, '3 + 0.25 = 3.25'], 0,
  'Each square is 0.01. What is 25 squares?',
  ['Each square is 0.01, so 25 squares is 0.25.', 'You shaded it 3 times: 3 %s 0.25.' % X, '75 squares are shaded, which is 0.75.'],
  '**3 %s 0.25 = 0.75.** 75 of 100 squares are shaded. 3 %s 25 = 75 counts squares, not the value of the grid.' % (X, X),
  'Squares count hundredths.'),
 mul_q(2, '0.7', 6, [m_whole, m_small, m_add], '6 groups of 7 tenths. How many tenths is that?', '42 tenths is 4.2.', True),
 mul_q(2, 3, '0.26', [m_whole, m_side, m_big], '3 groups of 0.26. Regroup the hundredths.', '18 hundredths is 1 tenth and 8 hundredths.', True),
 mul_q(2, 8, '0.09', [m_whole, m_big, m_small], '8 groups of 9 hundredths.', '72 hundredths is 0.72.', True),
 mul_q(2, 4, '1.36', [m_whole, m_side, m_big], '4 groups of 1.36. Regroup as you go.', 'Regroup: 24 hundredths is 2 tenths and 4 hundredths.', True),
 mul_q(2, 6, '0.15', [m_whole, m_big, m_small], '6 groups of 15 hundredths. How many hundredths?', '90 hundredths is 0.90, which is 0.9.', True),
 (3, 'Rafi multiplied 7 by 0.896 and got 62.72. Which estimate shows his answer is wrong?',
  ['0.896 is about 1, and 7 %s 1 = 7, so the answer is near 7, not 62.72' % X,
   '7 + 0.896 is about 8, so the answer is near 8',
   '0.896 is about 9, and 7 %s 9 = 63, so 62.72 is about right' % X,
   '7 %s 0.896 must be bigger than 7, so 62.72 is fine' % X], 0,
  'Is 0.896 closer to 1 or to 9?',
  ['0.896 is just under 1.', '7 %s 1 = 7, so the answer is a bit less than 7.' % X,
   '62.72 is about ten times too big.', 'The real product is 6.272: the point slipped one place.'],
  '**0.896 is about 1, so the answer is near 7.** The real product is 6.272. He put the point one place too far right, as if 0.896 were 8.96.',
  'A decimal less than 1 makes the product smaller than the whole number.'),
 (3, 'A path has 4 sections, each 2.35 meters long. How long is the path?',
  ['9.4 meters', '94 meters', '0.94 meters', '6.35 meters'], 0,
  'Find 4 %s 2.35.' % X,
  ['4 %s 235 = 940.' % X, '2.35 has 2 decimal places, so 9.40, which is 9.4.', 'Check: 4 %s 2 = 8, close to 9.4.' % X],
  '**9.4 meters.** 4 %s 2.35 = 9.40. 94 and 0.94 misplace the point, and 6.35 adds 4 instead of multiplying.' % X,
  'Four sections means 4 groups.'),
 (3, 'A town planned 3 gardens of 0.8 acre each. It now makes each garden 8 acres instead. How many more acres do the gardens take up in all?',
  ['21.6 acres', '24 acres', '7.2 acres', '2.4 acres'], 0,
  'Find the total area before and after, then subtract.',
  ['Before: 3 %s 0.8 = 2.4 acres.' % X, 'After: 3 %s 8 = 24 acres.' % X, '24 %s 2.4 = 21.6 acres more.' % MINUS],
  '**21.6 acres.** 24 %s 2.4 = 21.6. 24 is the new total, not the increase, and 7.2 is the increase for only one garden.' % MINUS,
  'More in all: compare the totals, not one garden.'),
 (3, 'Sam works out 6 %s $0.75 = $4.50. How can whole-number multiplication check it?' % X,
  ['6 %s 75 = 450 cents, and 450 cents is $4.50' % X, '6 + 75 = 81, so the answer should be $81',
   '6 %s 7 = 42, so the answer should be $42' % X, 'It cannot; whole numbers never check a decimal'], 0,
  '$0.75 is 75 cents.',
  ['$0.75 is 75 cents.', '6 %s 75 = 450 cents.' % X, '450 cents is $4.50, so his answer checks.'],
  '**6 %s 75 = 450 cents, which is $4.50.** Thinking in cents turns a money problem into whole numbers.' % X,
  'Cents are whole numbers. Use them to check.'),
 (3, 'Which product is less than 9?',
  LT9, 0,
  'Which factor is less than 1?',
  ['9 %s a number bigger than 1 is bigger than 9.' % X, '9 %s a number less than 1 is less than 9.' % X,
   'Only 0.8 is less than 1.', '9 %s 0.8 = 7.2.' % X],
  '**9 %s 0.8.** 0.8 is less than one whole, so the product, 7.2, is less than 9. Every other factor is more than 1.' % X,
  'Compare the decimal with 1 before you multiply.'),
]

go(3, 'Model Multiplying a Decimal by a Whole Number', [
 ('Place-value blocks',
  '**Decide which block is 1 first: if a flat is 1, a rod is 0.1 and a small cube is 0.01.**\n'
  '• 10 cubes make a rod; 10 rods make a flat.',
  'Pick the one, then the rest follow.'),
 ('Groups of a decimal',
  '**3 %s 0.42 means 3 groups of 0.42, put together.**\n'
  '• 0.42 + 0.42 + 0.42 = 1.26.' % X,
  'Times = groups of.'),
 ('Regrouping',
  '**Trade 10 hundredths for 1 tenth, and 10 tenths for 1 whole.**\n'
  '• 4 %s 0.36: 12 tenths and 24 hundredths regroup to 1.44.' % X,
  'Same trading as whole numbers.'),
 ('Shading a grid',
  '**On a 100-square grid that stands for 1, each square is 0.01.**\n'
  '• Shade 25 squares 3 times: 3 %s 0.25 = 0.75.' % X,
  'Squares are hundredths.'),
 ('Less than one',
  '**A whole number times a decimal less than 1 gives a product less than the whole number.**\n'
  '• 7 %s 0.6 = 4.2, less than 7.' % X,
  'Less than one whole, so less in all.'),
 ('Same digits as whole numbers',
  '**Multiply as if there were no point, then place the point: 4 %s 1.36 → 4 %s 136 = 544 → 5.44.**' % (X, X),
  'Digits first, point second.'),
 ('Estimate to check',
  '**Round the decimal, multiply, and compare. An answer ten times too big means the point slipped.**\n'
  '• 7 %s 0.896 is near 7, so 62.72 is wrong.' % X,
  'An estimate catches a slipped point.'),
 ('Money in cents',
  '**Turn dollars into cents to check with whole numbers.**\n'
  '• 6 %s $0.75 → 6 %s 75 = 450 cents = $4.50.' % (X, X),
  'Cents are whole numbers.'),
], L3,
 'Lesson 4-3 practice pages: using place-value blocks, repeated groups and shaded grids to multiply a decimal by a whole number, deciding whether a product is less than the whole number, and using an estimate to find a misplaced decimal point.',
 'Seeing the groups is what makes the rule in lesson 4 make sense: the digits multiply like whole numbers, and the size tells you where the point goes.',
 [('Model multiplying a decimal by a whole number with blocks or a grid', 'source'),
  ('Regroup hundredths as tenths and tenths as ones', 'source'),
  ('Tell whether a product is less than or greater than the whole number', 'source'),
  ('Use an estimate to find a misplaced decimal point', 'source')],
 'Built from the lesson 4-3 practice pages in her Unit 4 folder, read for what they ask. The numbers are fresh, not the page\'s own. Every wrong option on a worked product comes from a named slip: the point left out, the point one place too far either way, adding instead of multiplying, or writing each place\'s product side by side without regrouping (4 %s 1.36 as 4.1224). One question mirrors the page\'s own critique, a product about ten times too big. Her class teaches this unit after Unit 5.' % X,
 ('Picture the groups, multiply as whole numbers, then use the size of the answer to place the point.', 12))

# ══ Lesson 4 · Multiply a decimal by a whole number ═════════════════════════
def z_lost(a, b):
    """Counted the places from a product that dropped the whole factor's zero:
    7.25 × 40 → 725 × 4 = 2,900 → 29.00."""
    w, x = (a, b) if d(a) == d(a).to_integral() else (b, a)
    w = int(d(w)); assert w % 10 == 0
    digits = int(format(d(x).normalize(), 'f').replace('.', ''))
    return Dm(digits * (w // 10)) / 10 ** places(x)
NM[z_lost] = 'the zero in the whole number dropped before multiplying'

use('0.45', 6); assert d('0.45') * 6 == d('2.70') and places(d('0.45') * 6) == 1
use('4.7', 6); assert 47 * 6 == 282
use('0.35', 64); assert d('0.35') * 64 == d('22.40')
use('6.8', 2); assert 2 * d('6.8') + d('9.5') == d('23.1') < 25
use('3.5', 1); use('3.5', 9); assert d('3.5') * 9 == d('31.5')
for w, x in [('0.6', 48), (6, '4.8'), (60, '0.48')]: use(w, x)
assert d('0.6') * 48 == 6 * d('4.8') == 60 * d('0.48') == d('28.8')
assert 24 * 13 == 312
QNT = one_false([('6.4', 3, '1.92'), (64, 3, '192'), (64, '0.3', '19.2'), (64, '0.03', '1.92')])

L4 = [
 (1, 'What are the two steps to multiply a decimal by a whole number?',
  ['Multiply as if there were no decimal point, then place the point', 'Line up the decimal points, then add the numbers',
   'Round both numbers, then write the rounded product', 'Drop the decimal point, and leave it out of the answer'], 0,
  'Think of 0.36 %s 14 as 36 %s 14 first.' % (X, X),
  ['Multiply the digits as whole numbers.', 'Count the decimal places in the decimal factor.',
   'Give the product the same number of places.'],
  '**Multiply as whole numbers, then place the point.** Rounding is for estimating, not for the exact answer.',
  'Digits first, point second.'),
 (1, 'For 0.36 %s 14, how many decimal places does the product have before you drop any zeros?' % X,
  ['Two, the same as 0.36', 'One, because 14 has no decimal', 'Three, two plus one more for 14', 'None, because 14 is a whole number'], 0,
  'Count the digits after the point in each factor.',
  ['0.36 has 2 decimal places.', '14 has none.', 'So the product has 2 + 0 = 2.', '36 %s 14 = 504, so 0.36 %s 14 = 5.04.' % (X, X)],
  '**Two.** The places in the factors add up: 2 from 0.36 and 0 from 14. 0.36 %s 14 = 5.04.' % X,
  'Count the places in the factors.'),
 (1, 'What is the same about 24 %s 13 and 2.4 %s 13?' % (X, X),
  ['The digits of the product, 312; only the point is in a different place', 'Nothing; a decimal product always has different digits',
   'Both products are 312, exactly the same number', 'Both products have one decimal place, like 2.4'], 0,
  'Find 24 %s 13 first.' % X,
  ['24 %s 13 = 312.' % X, '2.4 %s 13 has the same digits.' % X, '2.4 has one decimal place, so 31.2.'],
  '**The digits, 312.** 24 %s 13 = 312 and 2.4 %s 13 = 31.2. Only the point moves.' % (X, X),
  'Same digits; the point tells the size.'),
 (1, '47 %s 6 = 282. Using number sense, what is 4.7 %s 6?' % (X, X),
  ['28.2', '2.82', '282', '0.282'], 0,
  '4.7 is about 5. What is 5 %s 6?' % X,
  ['4.7 is close to 5.', '5 %s 6 = 30.' % X, 'Of 28.2, 2.82, 282 and 0.282, only 28.2 is close to 30.'],
  '**28.2.** 4.7 %s 6 should be close to 5 %s 6 = 30, and 28.2 is.' % (X, X),
  'An estimate tells you where the point goes.'),
 (1, 'Which equation is NOT true?',
  QNT, 0,
  'Check where the point goes in each product.',
  ['64 %s 3 = 192.' % X, '64 %s 0.3 has one decimal place: 19.2.' % X, '64 %s 0.03 has two: 1.92.' % X,
   '6.4 %s 3 has one decimal place, so it is 19.2, not 1.92.' % X],
  '**6.4 %s 3 = 1.92.** 6.4 has one decimal place, so the product does too: 19.2. The other three are true.' % X,
  'Count the places in the factors; the product has the same.'),
 mul_q(2, '0.58', 7, [m_whole, m_big, m_small], '58 %s 7 first. Watch for a zero in the answer.' % X, 'A zero inside 4.06 is a real digit; keep it.'),
 mul_q(2, '3.4', 26, [m_whole, m_small, m_add], '34 %s 26 first, then one decimal place.' % X, 'Check: 3 %s 26 = 78, close to your answer.' % X),
 mul_q(2, '0.47', 16, [m_whole, m_big, m_small], '47 %s 16 first, then two decimal places.' % X, 'Estimate: 0.5 %s 16 is about 8.' % X),
 mul_q(2, 52, '0.006', [m_whole, m_big, m_small], '52 %s 6 first, then three decimal places.' % X, 'Three places: write a zero after the point if you need one.'),
 mul_q(2, '7.25', 40, [z_lost, m_big, m_whole], '725 %s 40 first, then two decimal places.' % X, 'Keep the zero in 40 when you multiply.'),
 (3, 'Ivy multiplies a whole number by a decimal with two decimal places. She says the product could have only one decimal place. Is she right?',
  ['Yes: 0.45 %s 6 = 2.70, which is the same as 2.7' % X, 'No: the product must always have exactly two places',
   'No: the product must have three places, two plus one', 'Yes, but only if the whole number is 1'], 0,
  'What happens when a product ends in 0?',
  ['45 %s 6 = 270.' % X, 'Two places gives 2.70.', 'A zero at the end does not change the value, so 2.70 = 2.7.'],
  '**Yes.** 0.45 %s 6 = 2.70, and 2.70 is 2.7. When the product ends in zero, it can be written with fewer places.' % X,
  'Count places first, then drop end zeros.'),
 (3, 'A bakery makes $0.35 on each muffin it sells. It sells 64 muffins. How much does it make?',
  ['$22.40', '$224.00', '$2.24', '$2,240.00'], 0,
  'Find 0.35 %s 64.' % X,
  ['35 %s 64 = 2,240.' % X, '0.35 has 2 decimal places: 22.40.', 'Check: 0.35 is about a third, and a third of 64 is about 21.'],
  '**$22.40.** 35 %s 64 = 2,240, and two places makes 22.40. The other amounts put the point in the wrong place.' % X,
  'Money keeps two places: $22.40.'),
 (3, 'A backpack may weigh at most 25 pounds. It holds two books of 6.8 pounds each and a lunchbox of 9.5 pounds. Is it within the limit?',
  ['Yes: 2 %s 6.8 + 9.5 = 23.1 pounds' % X, 'No: 2 %s 6.8 + 2 %s 9.5 = 32.6 pounds' % (X, X),
   'Yes: 6.8 + 9.5 = 16.3 pounds', 'No: 68 + 68 + 95 = 231 pounds'], 0,
  'Find the weight of the two books first.',
  ['2 %s 6.8 = 13.6 pounds of books.' % X, '13.6 + 9.5 = 23.1 pounds.', '23.1 is less than 25.'],
  '**Yes: 23.1 pounds.** 32.6 counts the lunchbox twice, 16.3 leaves a book out, and 231 drops the decimal points.',
  'Count each thing once, then compare.'),
 (3, 'A rectangle is 3.5 meters wide. Its length is a one-digit whole number of meters. What are its least and greatest possible areas?',
  ['3.5 and 31.5 square meters', '0 and 31.5 square meters', '3.5 and 35 square meters', '35 and 315 square meters'], 0,
  'The smallest one-digit length is 1, and the largest is 9.',
  ['Area = length %s width.' % X, 'Least: 1 %s 3.5 = 3.5.' % X, 'Greatest: 9 %s 3.5 = 31.5.' % X],
  '**3.5 and 31.5 square meters.** A length of 0 is not a rectangle, 10 is not one digit, and 35 and 315 drop the decimal point.',
  'One-digit whole numbers run from 1 to 9.'),
 (3, 'Compare 0.6 %s 48, 6 %s 4.8 and 60 %s 0.48.' % (X, X, X),
  ['All three equal 28.8', '60 %s 0.48 is the greatest' % X, '0.6 %s 48 is the least' % X, '6 %s 4.8 is the greatest' % X], 0,
  'Each one is 6 %s 48 = 288 with the point placed somewhere.' % X,
  ['0.6 %s 48: one place, 28.8.' % X, '6 %s 4.8: one place, 28.8.' % X, '60 %s 0.48: 2,880 with two places, 28.80.' % X,
   'So all three are 28.8.'],
  '**All three equal 28.8.** One factor got 10 times bigger while the other got 10 times smaller, so the product stayed the same.',
  'Ten times bigger and ten times smaller cancel out.'),
]

go(4, 'Multiply a Decimal by a Whole Number', [
 ('Multiply, then place the point',
  '**Multiply as if there were no decimal point, then put the point in the product.**\n'
  '• 0.15 %s 12 → 15 %s 12 = 180 → 1.80.' % (X, X),
  'Digits first, point second.'),
 ('Count the places',
  '**The product has as many decimal places as the factors have together.**\n'
  '• 0.36 has 2 and 14 has 0, so 0.36 %s 14 = 5.04 has 2.' % X,
  'Places in = places out.'),
 ('Use number sense',
  '**Estimate to place the point: 4.7 %s 6 is about 5 %s 6 = 30, so 28.2.**' % (X, X),
  'The estimate picks the place.'),
 ('Zeros inside the product',
  '**A zero between digits is a real digit; keep it.**\n'
  '• 0.58 %s 7 = 4.06, not 4.6.' % X,
  'Zeros inside stay.'),
 ('Zeros at the end',
  '**After placing the point you may drop zeros at the end: 2.70 is 2.7.**\n'
  '• So a two-place decimal times a whole number can show one place.',
  'End zeros can go.'),
 ('Keep the whole number\'s zeros',
  '**Multiply by the whole number exactly as written, zeros and all.**\n'
  '• 7.25 %s 40 = 290, not 29.' % X,
  'A zero in 40 is part of the number.'),
 ('Ten times and a tenth',
  '**If one factor is 10 times bigger and the other 10 times smaller, the product stays the same.**\n'
  '• 0.6 %s 48 = 6 %s 4.8 = 60 %s 0.48 = 28.8.' % (X, X, X),
  'Up 10, down 10, no change.'),
 ('Check every product',
  '**Estimate before or after: if the answer is about 10 times too big or small, move the point.**\n'
  '• $0.35 %s 64 is about $21, so $22.40 fits.' % X,
  'Estimate, then trust.'),
], L4,
 'Lesson 4-4 practice pages: multiplying a decimal by a whole number by multiplying as whole numbers and placing the point, using number sense to place it, telling which equation is not true, and word problems about money, weight and area.',
 'This is the lesson the unit has been building to: the rule she will use every time a decimal and a whole number are multiplied.',
 [('Multiply a decimal by a whole number and place the decimal point', 'source'),
  ('Use number sense or counting places to place the point', 'source'),
  ('Explain why a product can show fewer decimal places than the factor', 'source'),
  ('Solve word problems that multiply a decimal by a whole number', 'source')],
 'Built from the lesson 4-4 practice pages in her Unit 4 folder, read for what they ask. The numbers are fresh, not the page\'s own. Every wrong option on a worked product comes from a named slip: the point left out, the point one place too far either way, or the zero in a whole number like 40 dropped before multiplying. One question answers the page\'s own puzzle about a product with fewer decimal places (0.45 %s 6 = 2.70 = 2.7). Her class teaches this unit after Unit 5.' % X,
 ('Multiply as whole numbers, count the places, place the point, then check with an estimate.', 12))

print('multiplications asked:', len(USED), '— none from the practice pages')
