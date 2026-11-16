# -*- coding: utf-8 -*-
"""River's Unit 4 · Test Review, Part 1: Lessons 1–4.

The 11/13 newsletter: Unit 4's quiz is done, lessons 4-5 to 4-8 come the week
of 11/16, and no test date is printed. Only the 4-1 to 4-4 pages are in Drive,
so this is Part 1, built from those four lessons. Part 2 waits for the 4-5 to
4-8 pages rather than guessing what they cover.

Same shape as Unit 3's test review (v189): `series:'Unit 4'`, `prep:true`,
`round:10`, and no `order` ("Test" sorts after "Lesson" on title alone). The
teacher's standing emphasis is checking work, so a third of it is find-the-
mistake: a worked answer that is wrong, and which slip produced it. Every
wrong number is MADE by a slip function, and the builder asserts that no
other offered slip makes the same number.

The helpers, the page guard (BOOK) and `use()` come from build_math_unit4.py,
executed only up to its first lesson so that the four lessons are not rebuilt
and re-stamped. Every multiplication here is also refused if any of the four
LESSONS already asks it.
"""
import json, io, os, re, sys
from decimal import Decimal as Dm
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import unit_common as U

_src = io.open(os.path.join(HERE, 'build_math_unit4.py'), encoding='utf-8').read()
_ns = {'__file__': os.path.join(HERE, 'build_math_unit4.py'), '__name__': 'u4helpers'}
exec(compile(_src.split('# ══ Lesson 1')[0], 'build_math_unit4.py', 'exec'), _ns)
d, f, places, p10, SUP, use, opts4, one_false, rnd, pair = (
    _ns[k] for k in ('d', 'f', 'places', 'p10', 'SUP', 'use', 'opts4', 'one_false', 'rnd', 'pair'))
X, MINUS = '×', '−'

# Every multiplication the four lessons already ask.
LESSON = set()
for n in (1, 2, 3, 4):
    j = json.load(io.open(os.path.join(U.REPO, 'content', 'math-u4-l%d.json' % n), encoding='utf-8'))
    u = j['records']['unit-m4u%d' % n]
    for q in u['questions']:
        for s in [q['q']] + q['opts']:
            for a, b in re.findall(r'([\d.,]+) × (10[¹²³⁴]|[\d.,]+)', s):
                b = str(10 ** {'¹': 1, '²': 2, '³': 3, '⁴': 4}[b[-1]]) if b.startswith('10') and b[-1] in '¹²³⁴' else b
                a, b = a.replace(',', '').rstrip('.'), b.replace(',', '').rstrip('.')
                if re.fullmatch(r'\d+(\.\d+)?', a) and re.fullmatch(r'\d+(\.\d+)?', b):
                    LESSON.add(pair(a, b))

def ask(a, b):
    assert pair(a, b) not in LESSON, ('a lesson already asks this', a, b)
    return use(a, b)

# ── Slips. Each takes (a, b) and returns the number the slip writes.
def whole_of(a, b):
    return (a, b) if d(a) == d(a).to_integral() else (b, a)
def digits(x): return int(format(d(x).normalize(), 'f').replace('.', ''))

def p_left(a, n):  return d(a) / 10 ** n
def p_few(a, n):   return d(a) * 10 ** (n - 1)
def p_many(a, n):  return d(a) * 10 ** (n + 1)
def p_times(a, n): return d(a) * 10 * n
def w_out(a, b):
    w, x = whole_of(a, b); return Dm(digits(x) * int(d(w)))
def w_big(a, b):   return d(a) * d(b) * 10
def w_small(a, b): return d(a) * d(b) / 10
def w_side(a, b):
    w, x = whole_of(a, b); w = int(d(w))
    ip, fp = format(d(x).normalize(), 'f').split('.')
    return Dm(str(w * int(ip)) + '.' + ''.join(str(w * int(c)) for c in fp))
def w_zero(a, b):
    w, x = whole_of(a, b); w = int(d(w)); assert w % 10 == 0
    return Dm(digits(x) * (w // 10)).scaleb(-places(x))
def w_add(a, b):   return d(a) + d(b)

SAY = {p_left: 'The point moved left, the wrong way',
       p_few: 'The point moved one place too few',
       p_many: 'The point moved one place too many',
       p_times: 'The exponent was used as a factor',
       w_out: 'The decimal point was left out',
       w_big: 'The point went one place too far right',
       w_small: 'The point went one place too far left',
       w_side: 'Each place was multiplied, not regrouped',
       w_zero: 'The zero in the whole number was dropped',
       w_add: 'The numbers were added, not multiplied'}
def mistake(lv, a, b, slip, others, who, hint, tip):
    """A worked answer made by `slip`; options name the slip and three others."""
    pw = isinstance(b, int) and b in (1, 2, 3, 4) and slip in (p_left, p_few, p_many, p_times)
    true = ask(a, 10 ** b) if pw else ask(a, b)
    wrong = slip(a, b)
    assert wrong != true, (a, b)
    for o in others:
        assert o(a, b) != wrong, ('two slips make the same number', a, b, SAY[o])
    shown = '%s %s %s' % (f(a), X, p10(b) if pw else f(b))
    if pw:
        n = b
        steps = ['%s = %s, so the point should move %d places to the right.' % (p10(n), f(10 ** n), n),
                 'The right answer is %s.' % f(true),
                 '%s is what you get when %s.' % (f(wrong), SAY[slip][0].lower() + SAY[slip][1:]),
                 'Check: multiplying by %s makes a number bigger, and %s %s.' % (
                     f(10 ** n), f(wrong), 'did not grow' if wrong < d(a) else 'grew by the wrong amount')]
    else:
        w, x = whole_of(a, b)
        steps = ['Multiply as whole numbers: %s %s %s = %s.' % (f(w), X, f(digits(x)), f(digits(x) * int(d(w)))),
                 '%s has %d decimal place%s, so the product is %s.' % (f(x), places(x), '' if places(x) == 1 else 's', f(true)),
                 '%s is what you get when %s.' % (f(wrong), SAY[slip][0].lower() + SAY[slip][1:]),
                 'Check with an estimate: %s %s %s is about %s.' % (
                     f(rnd(x, '0.1') if d(x) < 1 else rnd(x)), X, f(w),
                     f((rnd(x, '0.1') if d(x) < 1 else rnd(x)) * d(w)))]
    return (lv, '%s worked out %s and wrote %s. What went wrong?' % (who, shown, f(wrong)),
            opts4(SAY[slip], *[SAY[o] for o in others]), 0, hint, steps,
            '**%s.** The right answer is %s.' % (SAY[slip], f(true)), tip)

def pow_q(lv, a, n, slips, hint, tip):
    true = ask(a, 10 ** n)
    vals = [s(a, n) for s in slips]
    for v in vals: assert v != true
    return (lv, 'What is %s %s %s?' % (f(a), X, p10(n)), opts4(f(true), *[f(v) for v in vals]), 0, hint,
            ['%s = %s, so the point moves %d places to the right.' % (p10(n), f(10 ** n), n),
             'One place at a time: %s.' % ' → '.join(f(d(a) * 10 ** k) for k in range(n + 1)),
             'So %s %s %s = %s.' % (f(a), X, p10(n), f(true))],
            '**%s.** %s has %d zeros, so the point moves %d places right.' % (f(true), f(10 ** n), n, n), tip)

def mul_q(lv, a, b, slips, hint, tip):
    true = ask(a, b)
    vals = [s(a, b) for s in slips]
    for v in vals: assert v != true
    assert len(set([true] + vals)) == 4
    w, x = whole_of(a, b)
    est = (rnd(x, '0.1') if d(x) < 1 else rnd(x)) * d(w)
    return (lv, 'What is %s %s %s?' % (f(a), X, f(b)), opts4(f(true), *[f(v) for v in vals]), 0, hint,
            ['Multiply as whole numbers: %s %s %s = %s.' % (f(w), X, f(digits(x)), f(digits(x) * int(d(w)))),
             '%s has %d decimal place%s, so the product has %d: %s.' % (
                 f(x), places(x), '' if places(x) == 1 else 's', places(x),
                 format(Dm(digits(x) * int(d(w))).scaleb(-places(x)), 'f')),
             'Check with an estimate: about %s.' % f(est)],
            '**%s.** %s.' % (f(true), '; '.join('%s is what you get when %s' % (
                f(v), SAY[s][0].lower() + SAY[s][1:]) for v, s in zip(vals, slips))), tip)

# ── The checks.
assert ask('0.47', 2) == Dm('0.94') and w_side('0.47', 2) == Dm('0.814')
assert abs(Dm('0.814') - 1) < Dm('0.2')          # close to the estimate, so the estimate does not catch it
assert ask('0.58', 9) == Dm('5.22') and w_big('0.58', 9) == Dm('52.2')
ou = [('3.6', '4.7'), ('2.3', '6.1'), ('8.4', '5.2'), ('9.3', '1.4')]
over = [i for i, (a, b) in enumerate(ou) if rnd(a) * rnd(b) > d(a) * d(b)]
assert over == [0], over
for a, b in ou: ask(a, b)
assert ask('7.92', 31) and 8 * 30 == 240 and 7 * 30 == 210
assert ask('0.85', 14) == Dm('11.90')
assert ask('2.75', 6) == Dm('16.5') and d('2.75') * 3 == Dm('8.25') and d('2.75') * 2 == Dm('5.5')
NT = one_false([('4.8', 5, '2.4'), (48, 5, '240'), (48, '0.5', '24'), ('0.48', 5, '2.4')])

Q = [
 mistake(2, '4.06', 3, p_left, [p_few, p_many, p_times], 'Jada', 'Should the answer be bigger or smaller than 4.06?',
         'Multiplying by a power of 10 always makes a number bigger.'),
 mistake(2, '0.73', 2, p_few, [p_left, p_many, p_times], 'Owen', 'How many zeros does 100 have?',
         'Count the zeros, then count your moves.'),
 mistake(3, '2.9', 3, p_times, [p_left, p_few, p_many], 'Nia', 'What does 10³ mean? It is not 10 %s 3.' % X,
         'The exponent counts tens; it is never a factor.'),
 mistake(2, '0.64', 8, w_out, [w_big, w_small, w_add], 'Eli', 'Is 512 a sensible size for 0.64 %s 8?' % X,
         'Times a number less than 1 makes the answer smaller than 8.'),
 mistake(3, 3, '1.27', w_side, [w_out, w_big, w_add], 'Rosa', 'Work out 3 %s 1.27 properly and compare.' % X,
         'Regroup: 21 hundredths is 2 tenths and 1 hundredth.'),
 mistake(3, '4.15', 60, w_zero, [w_big, w_out, w_add], 'Sam', 'Multiply by 60 itself, not by 6.',
         'A zero in the whole number is part of it.'),
 mistake(2, '0.45', 8, w_add, [w_out, w_big, w_small], 'Ivy', 'Read the sign again.',
         'Read the sign before you start.'),
 (3, 'Ben wrote 2 %s 0.47 = 0.814. That is close to his estimate, 2 %s 0.5 = 1. Which check shows his answer is wrong?' % (X, X),
  ['Counting places: 0.47 has two, so the answer cannot have three',
   'The estimate: 0.814 is far too far from 1 to be right',
   'No check does; being close to 1 means 0.814 is right',
   'Whole numbers: a whole number times anything is whole'], 0,
  'An estimate only says roughly how big. What else can you check?',
  ['2 %s 47 = 94, so 2 %s 0.47 = 0.94.' % (X, X), '0.814 is close to 1, so the estimate does not catch it.',
   '0.47 has two decimal places, so the product has two. 0.814 has three.',
   'He wrote 2 %s 4 = 8 and 2 %s 7 = 14 side by side instead of regrouping.' % (X, X)],
  '**Counting places.** 0.47 has two decimal places, so the product has two: 0.94. 0.814 slips past the estimate because it is close to 1, which is why one check is not always enough.',
  'Use more than one check. Each one catches different slips.'),
 (3, 'Mia wrote 0.58 %s 9 = 52.2. Which check shows her answer is wrong?' % X,
  ['An estimate: 0.6 %s 9 = 5.4, so 52.2 is about ten times too big' % X,
   'Counting places: 52.2 has one place, so the point is fine',
   'Nothing: 58 %s 9 = 522, so 52.2 checks out' % X,
   'Rounding 9 to 10: 0.58 %s 10 = 58, so 52.2 is close enough' % X], 0,
  'Round 0.58 to a friendly decimal and multiply.',
  ['0.58 is about 0.6.', '0.6 %s 9 = 5.4.' % X, '52.2 is about ten times 5.4, so the point slipped one place.',
   'The right answer is 5.22.'],
  '**An estimate.** 0.6 %s 9 = 5.4, and 52.2 is ten times too big. The right answer is 5.22. (0.58 %s 10 is 5.8, not 58.)' % (X, X),
  'An answer about ten times too big or small means the point slipped.'),
 pow_q(1, '3.08', 2, [p_left, p_few, p_many], 'Count the zeros in 100. Keep the zero inside 3.08.', 'A zero inside a number stays.'),
 pow_q(1, '0.052', 4, [p_left, p_few, p_times], '%s means 10 %s 10 %s 10 %s 10.' % (p10(4), X, X, X), 'Fill empty places with zeros as you move.'),
 mul_q(2, '0.86', 9, [w_out, w_big, w_small], '86 %s 9 first, then two decimal places.' % X, 'Estimate: 0.9 %s 9 is about 8.' % X),
 mul_q(2, 12, '4.05', [w_out, w_big, w_small], '12 %s 405 first. Keep the zero.' % X, 'Estimate: 12 %s 4 = 48.' % X),
 mul_q(2, '3.15', 20, [w_zero, w_big, w_out], '315 %s 20 first, then two decimal places.' % X, 'Multiply by 20, not by 2.'),
 mul_q(3, '0.004', 25, [w_out, w_big, w_small], '4 %s 25 first, then three decimal places.' % X, 'Three places: write zeros after the point if you need them.'),
 (1, 'Which is the best estimate of 7.92 %s 31?' % X,
  ['240', '24', '2,400', '210'], 0,
  'Round 7.92 to the nearest whole number and 31 to the nearest ten.',
  ['7.92 rounds to 8.', '31 rounds to 30.', '8 %s 30 = 240.' % X],
  '**240.** 8 %s 30 = 240. 210 chops 7.92 down to 7 instead of rounding it to 8, and 24 and 2,400 put the point in the wrong place.' % X,
  '7.92 is almost 8. Round it, do not chop it.'),
 (2, 'Rounding each factor to the nearest whole number, which gives an OVERestimate?',
  ['%s %s %s' % (f(a), X, f(b)) for a, b in ou], 0,
  'An overestimate needs the factors to round up.',
  ['3.6 rounds up to 4, and 4.7 rounds up to 5.', '4 %s 5 = 20 is more than the exact 16.92.' % X,
   'In each of the others, both factors round down.'],
  '**3.6 %s 4.7.** Both factors round up, so 4 %s 5 = 20 is more than the exact 16.92. Every other pair rounds both factors down.' % (X, X),
  'Both up, over. Both down, under.'),
 (3, 'Ribbon costs $0.85 a yard. Lila buys 14 yards. How much does she pay?',
  ['$11.90', '$119.00', '$1.19', '$14.85'], 0,
  'Find 0.85 %s 14. Estimate first.' % X,
  ['85 %s 14 = 1,190.' % X, '0.85 has two decimal places: 11.90.', 'Check: $1 %s 14 = $14, a little more than $11.90.' % X],
  '**$11.90.** 85 %s 14 = 1,190, and two places makes 11.90. $14.85 adds instead of multiplying, and the others misplace the point.' % X,
  'Money keeps two places.'),
 (3, 'A trail is 2.75 km long. Theo walks it there and back, on 3 days. How far does he walk in all?',
  ['16.5 km', '8.25 km', '5.5 km', '165 km'], 0,
  'Each day has two trips.',
  ['There and back is 2 trips a day: 6 trips in all.', '2.75 %s 6 = 16.5.' % X, 'Check: about 3 km %s 6 = 18 km.' % X],
  '**16.5 km.** 2.75 %s 6 = 16.5. 8.25 counts only the trip there, 5.5 is one day, and 165 drops the point.' % X,
  'Count every trip the story mentions.'),
 (1, 'Which equation is NOT true?',
  NT, 0,
  'Check where the point goes in each product.',
  ['48 %s 5 = 240.' % X, '48 %s 0.5 has one decimal place: 24.0, which is 24.' % X,
   '0.48 %s 5 has two: 2.40, which is 2.4.' % X, '4.8 %s 5 has one place: 24.0, so it is 24, not 2.4.' % X],
  '**4.8 %s 5 = 2.4.** 4.8 has one decimal place, so the product is 24.0, which is 24. The other three are true.' % X,
  'Count the places in the factors; the product has the same.'),
]

C = [
 ('Powers of 10', '**Multiplying by 10, 100 or 10³ moves the point right, one place for each zero.**\n'
  '• 3.08 %s 10² = 308.\n• The exponent counts the zeros; it is never a factor.' % X, 'One zero, one place.'),
 ('Estimate a product', '**Round to friendly numbers and multiply in your head.**\n'
  '• 7.92 %s 31 → 8 %s 30 = 240.\n• For a decimal less than 1, use 0.5 or 0.25, never 0.' % (X, X), 'Round, do not chop.'),
 ('Over or under', '**Round both factors up and you overestimate; round both down and you underestimate.**', 'Both up, over.'),
 ('Multiply, then place the point', '**Multiply as whole numbers, then give the product as many decimal places as the factors have.**\n'
  '• 0.86 %s 9 → 86 %s 9 = 774 → 7.74.' % (X, X), 'Digits first, point second.'),
 ('Check 1 · estimate', '**Round and multiply: an answer about ten times too big or small means the point slipped.**\n'
  '• 0.58 %s 9 is about 5.4, so 52.2 is wrong.' % X, 'Estimates catch slipped points.'),
 ('Check 2 · count the places', '**The product has as many decimal places as the factors (before you drop end zeros).**\n'
  '• 2 %s 0.47 cannot be 0.814: three places where there should be two.' % X, 'Places in = places out.'),
 ('Check 3 · bigger or smaller', '**Times a power of 10 grows; times a decimal less than 1 shrinks.**\n'
  '• 0.64 %s 8 must be less than 8, so 512 is wrong.' % X, 'Ask which way the answer should go.'),
 ('Slips with powers of 10', '**Watch for the point moving the wrong way, one place too few or too many, or 10³ read as 30.**', 'Count, then move.'),
 ('Slips with decimals', '**Watch for the point left out or misplaced, no regrouping, a dropped zero, or adding instead of multiplying.**\n'
  '• 3 %s 1.27 is 3.81, not 3.621.\n• 4.15 %s 60 is 249, not 24.9.' % (X, X), 'Name the slip, then fix it.'),
 ('Find the mistake', '**Work it out yourself, compare with the wrong answer, then ask what move would make that number.**', 'Every wrong answer came from somewhere.', None, 'added'),
]

go_C, go_Q = [], []
for a in C: U.card(go_C, *a)
for a in Q: U.q(go_Q, *a)
uid, slug = 'unit-m4-review', 'math-u4-review'
U.build('wayfinder', go_C, go_Q, uid, 'Unit 4 · Test Review, Part 1: Lessons 1–4', 'math',
        'A review of Unit 4 lessons 4-1 to 4-4: multiplying decimals by powers of 10, estimating products, and multiplying a decimal by a whole number, with a third of it on finding the mistake in a worked answer.',
        'The test checks whether she can multiply, and also whether she catches her own slips. This review practises both.',
        [('Multiply a decimal by a power of 10', 'source'),
         ('Estimate a product and say whether it is over or under', 'source'),
         ('Multiply a decimal by a whole number and place the point', 'source'),
         ('Find the slip in a worked answer and say which check catches it', 'added')],
        'Built from the lesson 4-1 to 4-4 practice pages in her Unit 4 folder and the 11/13 newsletter, with fresh numbers that neither the pages nor the four lessons use. This is Part 1: the newsletter says lessons 4-5 to 4-8 are taught the week of 11/16, and their pages are not in Drive yet, so they are not covered here. Part 2 can be built when they arrive. No test date is printed yet. Seven questions give a wrong worked answer and ask which slip made it; two ask which check catches a slip, including one an estimate misses (2 %s 0.47 written as 0.814), which is why counting decimal places matters too.' % X,
        ('Work each one out yourself before you look at the choices, then check it two ways.', 12),
        'content/%s.json' % slug, 'Lesson 4-1 to 4-4 Student Edition practice pages and the 11/13 newsletter (Drive)',
        'enVision Topic 4 Student Edition practice pages — multiplying decimals (Drive)',
        offset_hours=3, round_=10)
fp = '%s/content/%s.json' % (U.REPO, slug)
j = json.load(io.open(fp, encoding='utf-8'))
rec = j['records'][uid]
rec.update({'series': 'Unit 4', 'prep': True, 'libv': 1, 'quarter': 2})
io.open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('lesson multiplications refused:', len(LESSON))
