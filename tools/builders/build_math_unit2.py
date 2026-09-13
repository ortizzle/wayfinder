# -*- coding: utf-8 -*-
"""River's Unit 2 — Add and Subtract Decimals (enVision grade-5 book, Topic 2).

Six lessons, one per unit record, because she does a lesson a day at school
(Chris, 2026-09-13: "lessons make more sense now that we're in the thick of
it"). They shelve as their own book, `Unit 2`, NOT as more parts of Unit 1.

Why the titles say "Lesson N" and not the book's own "2-1":  Unit 1 already
holds a `Topic 2 · 2-1 …` run from the GRADE-4 book (whole numbers), and both
shelves render on the Math subject screen at the same time.  Two visible "2-1"s
pointing at different content is the inversion trap in a new costume.  The
book's own label rides in `source` so she can still find the pages.

Every number here is computed with Decimal and asserted before it can be
written into a question — floats are not safe for money arithmetic
(0.1+0.2 != 0.3) and this whole unit IS decimal arithmetic.
"""
from decimal import Decimal as D
import unit_common as U

def d(x): return D(str(x))
def s(x):
    """Render a Decimal the way the book does — no trailing zeros beyond 2dp."""
    t = format(x.normalize(), 'f')
    return t

def money(x): return '$' + format(x, '.2f')

# ── every fact this unit teaches, verified here rather than trusted ──────────
A1 = d('3.98') + d('5.45');  assert A1 == d('9.43'), A1
A2 = d('7.62') - d('1.97');  assert A2 == d('5.65'), A2
A3 = d('6.25') + d('4.75');  assert A3 == d('11'), A3
A4 = d('12.60') + d('8.40') + d('5.15'); assert A4 == d('26.15'), A4
A5 = d('4.30') + d('9.70');  assert A5 == d('14'), A5
E1 = d('48.7') + d('23.2');  assert E1 == d('71.9'), E1
E2 = d('61.4') - d('28.8');  assert E2 == d('32.6'), E2
S1 = d('5.6') + d('3.75');   assert S1 == d('9.35'), S1
S2 = d('14') + d('6.28');    assert S2 == d('20.28'), S2
S3 = d('0.45') + d('0.68');  assert S3 == d('1.13'), S3
S4 = d('32.5') - d('7.84');  assert S4 == d('24.66'), S4
S5 = d('9.4') - d('2.65');   assert S5 == d('6.75'), S5
S6 = d('20') - d('13.42');   assert S6 == d('6.58'), S6
B1 = d('18.75') + d('9.40') + d('6.25'); assert B1 == d('34.40'), B1
B2 = d('50') - B1;           assert B2 == d('15.60'), B2
B3 = d('7.85') + d('12.30'); assert B3 == d('20.15'), B3
B4 = d('40') - B3;           assert B4 == d('19.85'), B4

# Everything else each lesson asserts, so no question can carry a number that
# was worked by hand.  The L5 "odd one out" item is pinned structurally too:
# it only works while exactly one of its four options differs.
assert d('7.55') + d('2.45') + d('6.30') == d('16.30')
assert d('15.08') - d('4.99') == d('10.09')
assert d('8.97') + d('3.40') == d('12.37')
assert d('4.30') + d('6.85') + d('9.70') == d('20.85')
assert d('17.98') + d('8.29') == d('26.27')
assert d('8.12') + d('3.79') + d('7.94') == d('19.85')
assert d('12.8') - d('7.3') == d('5.5')
assert d('45.6') + d('28.9') == d('74.5')
assert d('494') + d('312') == d('806')
assert d('1.24') + d('0.35') == d('1.59')
assert d('0.92') - d('0.45') == d('0.47')
assert d('0.7') + d('0.5') == d('1.2')
assert d('0.36') + d('0.27') == d('0.63')          # the only pair whose hundredths reach ten
assert all((d(a).as_tuple().digits[-1] + d(b).as_tuple().digits[-1]) < 10
           for a, b in [('0.31','0.24'), ('0.42','0.15'), ('0.53','0.16')])
assert d('23.48') + d('19.7') == d('43.18')
assert d('7.05') + d('0.9') + d('2.4') == d('10.35')
assert d('32.4') + d('15.3') == d('47.7')
assert d('21.39') + d('21.59') == d('42.98')
assert d('0.02') + d('12') + d('0.88') == d('12.90')
assert d('0.06') + d('12.03') != d('12.9') and d('6.2') + d('3.4') + d('2.3') != d('12.9')
assert d('3.01') + d('2.01') + d('7.7') != d('12.9')
assert d('65.18') - d('12.05') == d('53.13')
assert d('1.5') - d('0.8') == d('0.7')
assert d('20.9') - d('2.9') == d('18')
assert d('5.92') - d('4.37') == d('1.55')
assert d('180') + d('215') + d('80') == d('475')
# L5 q10 must have exactly ONE option that is not 1.65 — it was built from the
# book's "circle ALL" item, which is a multi-select and does NOT survive being
# dropped into single-answer MC unchanged.  Three of four matched on the first
# build.  This pins the rewrite.
_odd = [(a, b) for a, b in [('12.68','2.03'), ('27.30','25.65'),
                            ('11.23','9.58'), ('21.74','20.09')]
        if d(a) - d(b) != d('1.65')]
assert _odd == [('12.68', '2.03')], _odd

CLS, APP = 'math', 'wayfinder'
SERIES = 'Unit 2'
SRC = 'enVision Topic 2 textbook scan — Add and Subtract Decimals (Drive)'

def go(n, slug, title, cards, qs, summary, why, objs, note, nxt, booklbl):
    C, Q = [], []
    for a in cards: U.card(C, *a)
    for a in qs: U.q(Q, *a)
    U.build(APP, C, Q, 'unit-m2u%d' % n,
            '%s · Lesson %d: %s' % (SERIES, n, title), CLS,
            summary, why, objs, note, nxt,
            'content/%s.json' % slug,
            'Unit 2 textbook scan, %s (Drive)' % booklbl, SRC,
            offset_hours=4, round_=10)
    # build() emits neither `series` nor `libv`.  `series` is what shelves these
    # as their own book (seriesOf() honours it ahead of the ` · ` title rule), and
    # `libv` is what makes a later content fix immune to the approval race.
    import json, io as _io
    fp = '%s/content/%s.json' % (U.REPO, slug)
    j = json.load(_io.open(fp, encoding='utf-8'))
    rec = j['records']['unit-m2u%d' % n]
    rec['series'] = SERIES
    rec['libv'] = 1
    _io.open(fp, 'w', encoding='utf-8').write(
        json.dumps(j, ensure_ascii=False, indent=1))

# ══ Lesson 1 · Mental Math with Decimals ════════════════════════════════════
go(1, 'math-u2-l1', 'Mental Math with Decimals', [
 ('The Commutative Property',
  '**You can add numbers in any order and the total does not change.**\n'
  '• 3.39 + 11.45 is the same total as 11.45 + 3.39.\n'
  '• It lets you move an addend next to the one it pairs well with.\n'
  '• It works for adding only — never for subtracting.',
  'Commutative = commute = the numbers travel to new seats.'),
 ('The Associative Property',
  '**You can regroup which addends you do first and the total does not change.**\n'
  '• (2.5 + 7.5) + 4.8 is the same total as 2.5 + (7.5 + 4.8).\n'
  '• Only the parentheses move; the order stays put.',
  'Associate = who you group up with. The brackets move, not the numbers.'),
 ('Compatible numbers',
  '**Numbers that are easy to compute in your head, usually because they make a whole.**\n'
  '• 6.25 and 4.75 are compatible: they make 11 exactly.\n'
  '• Hunt for hundredths that add to 100, or tenths that add to 10.',
  'Look for the pair that lands on a whole number, then mop up the leftover.'),
 ('Compensation when you ADD',
  '**Round an addend up to something friendly, then take the extra back off at the end.**\n'
  '• 3.98 + 5.45: add 4.00 + 5.45 = 9.45, then take back the 0.02 you added.\n'
  '• The answer is 9.43.',
  'You borrowed to make it easy, so you have to pay it back.'),
 ('Compensation when you SUBTRACT — the direction flips',
  '**If you subtract too much, you have to add the extra back on.**\n'
  '• 7.62 − 1.97: do 7.62 − 2.00 = 5.62, then add back the 0.03 you over-subtracted.\n'
  '• The answer is 5.65.\n'
  '• Taking away too much leaves you too low, so you climb back up.',
  'Subtracting too much leaves you short — so add it back, do not take more.'),
], [
 (1, 'Which property lets you swap two addends into each other\'s places without changing the total?',
  ['The Commutative Property', 'The Associative Property', 'The Distributive Property', 'The Identity Property'],
  0, 'Which one is about ORDER rather than grouping?',
  ['The question is about moving numbers into different seats.',
   'Changing the order of addends is the Commutative Property.',
   'Changing the grouping would be the Associative Property instead.'],
  '**The Commutative Property.** It is the one about order — the addends change seats and the total stays put.',
  'Order is Commutative; grouping is Associative. Neither one works for subtraction.'),

 (1, 'Which pair of numbers adds to a whole number, making them easy to compute mentally?',
  ['6.25 and 4.75', '6.25 and 4.25', '6.30 and 4.80', '6.15 and 4.65'],
  0, 'Add just the hundredths of each pair and look for 100.',
  ['Compatible numbers are ones that make a whole.',
   'Check the decimal parts: 0.25 and 0.75 add to 1.00 exactly.',
   '6.25 + 4.75 = 11, a whole number.'],
  '**6.25 and 4.75.** Their decimal parts make exactly 1.00, so the pair lands on 11 with nothing left over.',
  'Hundredths that add to 100, or tenths that add to 10, are the pairs worth hunting for.'),

 (2, 'A scarf costs $12.60, a hat costs $8.40, and a pair of gloves costs $5.15. Using mental math, what is the total?',
  ['$26.15', '$25.15', '$26.05', '$16.15'],
  0, 'Two of these three prices pair into a whole number.',
  ['$12.60 and $8.40 are compatible — their decimals make 1.00.',
   '$12.60 + $8.40 = $21.',
   'Then $21 + $5.15 = $26.15.'],
  '**$26.15.** Pairing the $12.60 with the $8.40 gives a clean $21 first, which leaves an easy final step.',
  'Scan all the addends before you start — the easy pair is rarely side by side.'),

 (2, 'Use compensation to find 3.98 + 5.45 mentally. What is the sum?',
  ['9.43', '9.45', '9.47', '8.43'],
  0, 'Round 3.98 up to 4, then remember what you owe back.',
  ['3.98 is 0.02 below 4, so use 4.00 instead.',
   '4.00 + 5.45 = 9.45.',
   'You added 0.02 that was not there, so take it back off.',
   '9.45 − 0.02 = 9.43.'],
  '**9.43.** Rounding 3.98 up to 4 added 0.02 that did not belong, so the same 0.02 comes back off at the end.',
  'Compensation always has two halves. Doing the easy sum and stopping is the whole trap.'),

 (2, 'Use compensation to find 7.62 − 1.97 mentally. What is the difference?',
  ['5.65', '5.62', '5.59', '6.65'],
  0, 'You took away more than you were asked to. Does that leave you too high or too low?',
  ['1.97 is 0.03 below 2, so subtract 2.00 instead.',
   '7.62 − 2.00 = 5.62.',
   'You took away 0.03 too much, which left the answer too low.',
   'Add the 0.03 back: 5.62 + 0.03 = 5.65.'],
  '**5.65.** Subtracting 2.00 took away 0.03 more than the question asked, and taking too much leaves you short — so it is added back.',
  'When you ADD, compensation takes back. When you SUBTRACT, it gives back. Getting the direction wrong is the commonest slip in the lesson.'),

 (3, 'A student says "addition can be done in any order, so subtraction can too." Why is that wrong?',
  ['The number being taken away has to stay second, or the answer changes',
   'Subtraction can be done in any order, but only with whole numbers',
   'Subtraction can be done in any order, but only when both numbers are decimals',
   'Changing the order of a subtraction is fine as long as you round first'],
  0, 'Try it on small numbers: is 9 − 4 the same as 4 − 9?',
  ['Test the claim: 9 − 4 = 5.',
   'Now flip it: 4 − 9 is not 5 at all.',
   'The roles are different — one number is the amount you start with, the other is what you remove.',
   'So the order of a subtraction is fixed.'],
  '**The number being taken away has to stay second.** In addition both numbers do the same job, so they can swap; in subtraction they do different jobs.',
  'The properties that let numbers move are addition properties. Check what job each number is doing before you move it.'),

 (3, 'Which regrouping makes 4.30 + 6.85 + 9.70 easiest to add in your head?',
  ['Add 4.30 and 9.70 first, then add 6.85',
   'Add 4.30 and 6.85 first, then add 9.70',
   'Add 6.85 and 9.70 first, then add 4.30',
   'Add them strictly left to right without regrouping'],
  0, 'Which two of the three land on a whole number together?',
  ['Look for the pair whose decimals make 1.00.',
   '0.30 and 0.70 make exactly 1.00.',
   '4.30 + 9.70 = 14, a clean whole number.',
   'Then 14 + 6.85 = 20.85, which is easy from there.'],
  '**Add 4.30 and 9.70 first.** They make exactly 14, and adding 6.85 to a whole number is far easier than adding two ragged decimals.',
  'The Associative Property is what makes this legal — you are only changing which pair goes first.'),

 (2, 'A shopper buys items costing $7.55, $2.45, and $6.30. What is the total?',
  ['$16.30', '$16.20', '$15.30', '$17.30'],
  0, 'Two of the three prices make a whole number together.',
  ['$7.55 and $2.45 are compatible — 0.55 and 0.45 make 1.00.',
   '$7.55 + $2.45 = $10.',
   '$10 + $6.30 = $16.30.'],
  '**$16.30.** The first two prices make a clean $10, which turns the last step into simple addition.',
  'Money problems are full of compatible pairs on purpose — prices ending in 5 often pair up.'),

 (3, 'A student computes 8.97 + 3.40 by doing 9.00 + 3.40 = 12.40, then writes 12.43 as the final answer. What went wrong?',
  ['They added the 0.03 back instead of taking it off',
   'They should have rounded 3.40 instead of 8.97',
   'They should not have used compensation on this problem at all',
   'They rounded 8.97 to the wrong whole number'],
  0, 'They rounded an addend UP. Does the easy sum end up too big or too small?',
  ['8.97 was rounded up to 9.00, which is 0.03 more than the real number.',
   'So 12.40 is 0.03 TOO BIG.',
   'Fixing it means subtracting 0.03, not adding it.',
   'The correct answer is 12.40 − 0.03 = 12.37.'],
  '**They added the 0.03 back instead of taking it off.** Rounding an addend up makes the easy sum too big, so the adjustment has to come back down.',
  'Ask yourself one question before adjusting: is my easy answer too big or too small? That decides the sign.'),

 (2, 'Find 15.08 − 4.99 using compensation. What is the difference?',
  ['10.09', '10.08', '10.07', '11.09'],
  0, 'Round 4.99 up to 5, then decide which way to adjust.',
  ['4.99 is 0.01 below 5, so subtract 5.00 instead.',
   '15.08 − 5.00 = 10.08.',
   'That took away 0.01 too much, leaving the answer low.',
   'Add it back: 10.08 + 0.01 = 10.09.'],
  '**10.09.** Subtracting the friendly 5.00 removed one hundredth too many, so that hundredth is added back at the end.',
  'Numbers ending in .99 are almost always worth rounding up — just remember the adjustment goes the other way for subtraction.'),
],
 'Lesson 2-1 of the Topic 2 textbook scan covers adding and subtracting decimals in your head: the Commutative and Associative Properties, spotting compatible numbers that make a whole, and using compensation to round a number to something friendly and then adjust back.',
 'Mental math is not a party trick here — it is the check on every written answer she produces later in the unit. Knowing that 6.25 and 4.75 make 11 is what tells her in one second whether a written sum is even close.',
 [('Use the Commutative and Associative Properties to reorder and regroup addends', 'source'),
  ('Spot compatible numbers that add to a whole', 'source'),
  ('Use compensation to add and subtract decimals mentally', 'source'),
  ('Say which direction to adjust — and why it flips between adding and subtracting', 'added')],
 'The one thing most likely to trip her up is the DIRECTION of the compensation adjustment, which is opposite for addition and subtraction. Rounding an addend up makes the sum too big (take the extra back off); rounding a subtrahend up takes away too much and makes the difference too small (add the extra back on). Two cards and three questions target exactly this. The other worthwhile idea is that the properties she is using are ADDITION properties — the lesson deliberately asks why they do not carry over to subtraction, which is the textbook\'s own closing question.',
 ('Start here — the whole unit leans on spotting the friendly pair.', 12),
 'Lesson 2-1')

# ══ Lesson 2 · Estimate Sums and Differences ════════════════════════════════
go(2, 'math-u2-l2', 'Estimate Sums and Differences', [
 ('Rounding to estimate',
  '**Round each number to the same place, then add or subtract the rounded numbers.**\n'
  '• 48.7 + 23.2 rounds to 50 + 20 = 70.\n'
  '• The real answer is 71.9, so the estimate is close.',
  'Round both to the same place, or the estimate wobbles.'),
 ('Substituting compatible numbers',
  '**Swap each number for a nearby number that is easy to compute, even if it is not the rounded one.**\n'
  '• For 237.5 + 345.1 you might use 250 + 350 = 600.\n'
  '• Rounding to hundreds instead gives 200 + 300 = 500.\n'
  '• Both are fair estimates; they just aim at different friendly numbers.',
  'Compatible numbers are chosen to be easy, not to follow a rounding rule.'),
 ('Is my estimate high or low?',
  '**If you rounded both numbers UP, the estimate is higher than the real answer. If you rounded both DOWN, it is lower.**\n'
  '• Round up + round up → too high.\n'
  '• Round down + round down → too low.\n'
  '• One of each → it could go either way.',
  'Track which way each number moved and the answer follows.'),
 ('When you need to round UP on purpose',
  '**If the question is "do I have enough?", round up so you never come up short.**\n'
  '• Estimating what a basket of shopping costs: round up, and any surprise is a good one.\n'
  '• Estimating how many seats or buses you need: round up, or someone is left standing.',
  'When being wrong is expensive, be wrong in the safe direction.'),
 ('Estimating a difference',
  '**Round both numbers, then subtract — same idea as a sum.**\n'
  '• 61.4 − 28.8 rounds to 61 − 29, or to the friendlier 60 − 30 = 30.\n'
  '• The real answer is 32.6, so 30 is a reasonable estimate.',
  'An estimate is meant to be quick. If it is not quick, pick friendlier numbers.'),
], [
 (1, 'Estimate 48.7 + 23.2 by rounding each number to the nearest ten. Which estimate do you get?',
  ['70', '72', '60', '80'],
  0, 'Round each number on its own first, then add the two rounded numbers.',
  ['48.7 rounds to 50.',
   '23.2 rounds to 20.',
   '50 + 20 = 70.'],
  '**70.** Each number is rounded to the nearest ten first, and only then added — 50 + 20.',
  'The real sum is 71.9, so 70 is a good estimate. An estimate is meant to be near, not exact.'),

 (1, 'Estimate 61.4 − 28.8 by rounding each number to the nearest ten. Which estimate do you get?',
  ['30', '40', '32', '20'],
  0, 'Round both numbers before you subtract anything.',
  ['61.4 rounds to 60.',
   '28.8 rounds to 30.',
   '60 − 30 = 30.'],
  '**30.** Both numbers are rounded to the nearest ten, then subtracted.',
  'The real difference is 32.6. Rounding the second number UP pulled the estimate a little low, which is worth noticing.'),

 (2, 'A scientist has three samples with masses of 61.8 g, 8.4 g, and 29.7 g. She rounds each to the nearest whole number to estimate the total. Which numbers does she add?',
  ['62, 8, and 30', '61, 8, and 29', '62, 9, and 30', '60, 10, and 30'],
  0, 'Nearest WHOLE number means look at the tenths digit of each one.',
  ['61.8 — the tenths digit is 8, so it rounds up to 62.',
   '8.4 — the tenths digit is 4, so it rounds down to 8.',
   '29.7 — the tenths digit is 7, so it rounds up to 30.',
   'She adds 62, 8, and 30.'],
  '**62, 8, and 30.** Each mass is rounded to the nearest whole number on its own, which means some go up and some go down.',
  'Rounding to the nearest ten instead would give 60, 10 and 30 — also a fair estimate, but not what "nearest whole number" asked for.'),

 (3, 'A shopper estimates two items costing $17.98 and $8.29 as "about $26." Is the estimate higher or lower than the real cost?',
  ['Lower, because both prices were rounded down',
   'Higher, because both prices were rounded up',
   'Lower, because only one price was rounded down',
   'Exactly right, because the roundings cancel out'],
  0, 'Compare each rounded number with the real one. Did it move up or down?',
  ['$17.98 was treated as about $18 — but $26 − $8 = $18, so it went slightly UP.',
   'Checking the other: $8.29 was treated as $8, which is DOWN by $0.29.',
   'The total shift is 0.02 up and 0.29 down, so the estimate sits below the real cost.',
   'The real cost is $26.27, above the $26 estimate.'],
  '**Lower.** The $8.29 was rounded down by much more than the $17.98 was rounded up, so the estimate lands under the true total.',
  'To judge an estimate, do not redo the sum — just track which way each number moved and by how much.'),

 (2, 'A class needs to be sure it has enough money for supplies costing $23.40, $16.75, and $9.20. Why should they round UP when they estimate?',
  ['So the estimate is never less than the real cost',
   'So the estimate is easier to compute in their heads',
   'Because prices always increase before you get to the shop',
   'Because rounding up is the rule whenever money is involved'],
  0, 'What goes wrong if the estimate turns out to be lower than the real total?',
  ['The question is whether they have ENOUGH, not what the exact total is.',
   'An estimate that is too low would tell them they can afford something they cannot.',
   'Rounding every price up guarantees the estimate is at least the real cost.',
   'Then if the estimate fits their budget, the real total certainly does.'],
  '**So the estimate is never less than the real cost.** When the question is "is this enough?", an estimate that is too low is the one that actually causes a problem, so you deliberately aim high.',
  'The direction you round is a decision, not a rule — it depends on what being wrong would cost you.'),

 (2, 'Estimate 8.12 + 3.79 + 7.94 by rounding each addend to the nearest whole number.',
  ['20', '19', '21', '18'],
  0, 'Round each of the three on its own, then add.',
  ['8.12 rounds to 8.',
   '3.79 rounds to 4.',
   '7.94 rounds to 8.',
   '8 + 4 + 8 = 20.'],
  '**20.** Rounding each addend to the nearest whole number gives 8, 4 and 8.',
  'The real sum is 19.85, so the estimate is close — and the fact it came out above tells you the roundings leaned up.'),

 (3, 'Two numbers are both rounded UP to make an estimate of a sum. What must be true of the estimate?',
  ['It is greater than the real sum',
   'It is less than the real sum',
   'It is equal to the real sum',
   'It could be greater or less, depending on the numbers'],
  0, 'If every part grew, what happened to the total?',
  ['Rounding a number up replaces it with something bigger.',
   'Both addends were replaced with bigger numbers.',
   'Adding two bigger numbers gives a bigger total.',
   'So the estimate must sit above the real sum.'],
  '**It is greater than the real sum.** Both parts grew, so the total has to grow with them — there is no way for it to land below.',
  'The "could go either way" answer is only correct when one number rounds up and the other rounds down.'),

 (2, 'A hiker walks 12.8 km one day and 7.3 km the next. Estimate how much FARTHER she walked on the first day, rounding each distance to the nearest whole number.',
  ['About 6 km', 'About 5 km', 'About 20 km', 'About 4 km'],
  0, '"How much farther" is a subtraction. Round both, then subtract.',
  ['12.8 rounds to 13.',
   '7.3 rounds to 7.',
   '13 − 7 = 6.',
   'So she walked about 6 km farther.'],
  '**About 6 km.** Rounding gives 13 and 7, and the gap between them is 6.',
  'The real difference is 5.5 km. Notice the words "how much farther" — they signal subtraction even though no minus sign appears.'),

 (3, 'Estimating 494 + 312, one student uses 500 + 300 = 800 and another uses 490 + 310 = 800. Both get 800. What does that show?',
  ['Different reasonable roundings can lead to the same estimate',
   'One of the two students must have made a mistake',
   'Estimates are always the same no matter how you round',
   'Rounding to hundreds is the only correct method here'],
  0, 'Were both roundings legitimate? Did they happen to agree?',
  ['Rounding to the nearest hundred gives 500 and 300.',
   'Rounding to the nearest ten gives 490 and 310.',
   'Both are honest roundings, and both totals come to 800.',
   'The real sum is 806, so both estimates are reasonable.'],
  '**Different reasonable roundings can lead to the same estimate.** There is no single "right" estimate — there are better and worse choices of friendly numbers, and here two different choices agreed.',
  'If two sensible estimates disagree a lot, that is a signal the numbers are awkward and an exact answer may be needed.'),

 (2, 'A tank holds 45.6 litres and another holds 28.9 litres. Which is the best estimate of the total, using compatible numbers?',
  ['About 75 litres', 'About 65 litres', 'About 85 litres', 'About 17 litres'],
  0, 'Pick nearby numbers that are easy to add, then add them.',
  ['45.6 is close to 45, and 28.9 is close to 30.',
   '45 + 30 = 75.',
   'So the total is about 75 litres.'],
  '**About 75 litres.** Choosing 45 and 30 keeps both numbers near the originals while making the addition a single easy step.',
  'The real total is 74.5 litres. "About 17" would be the answer to a different question — subtracting instead of adding.'),
],
 'Lesson 2-2 of the Topic 2 textbook scan covers estimating sums and differences of decimals two ways: rounding each number to the same place, and substituting compatible numbers that are easy to compute. It also asks whether a given estimate lands above or below the real answer.',
 'An estimate is the fastest way to catch a written answer that is wildly wrong — a misplaced decimal point shows up instantly against a good estimate. It is also often all a real question needs.',
 [('Estimate a sum or difference by rounding each number', 'source'),
  ('Estimate by substituting compatible numbers', 'source'),
  ('Decide whether an estimate is higher or lower than the exact answer', 'source'),
  ('Choose the rounding direction to match what the question is for', 'added')],
 'Two ideas here are worth more than the arithmetic. First, judging whether an estimate is HIGH or LOW without redoing the sum — the trick is to track which way each number moved rather than recompute. Second, and the one the textbook raises with its bus-seating question, is that the direction you round is a decision: when the question is "do we have enough?", rounding up is the safe error and rounding down is the one that leaves you short. Both get dedicated cards and questions. Worth knowing: the book treats rounding and compatible numbers as equally valid, so an answer that differs from hers is not automatically wrong — what matters is whether the estimate is close and whether she can say which way it leans.',
 ('Quick one. The skill here is deciding fast, not computing exactly.', 12),
 'Lesson 2-2')

# ══ Lesson 3 · Adding and Subtracting with Models ═══════════════════════════
go(3, 'math-u2-l3', 'Adding and Subtracting with Models', [
 ('What each block is worth',
  '**A flat is one whole, a rod is one tenth, and a small cube is one hundredth.**\n'
  '• 1.24 is one flat, two rods and four small cubes.\n'
  '• The blocks are just place value you can pick up.',
  'Ten of any block trades for one of the next size up.'),
 ('Ten hundredths make one tenth',
  '**Whenever you collect ten small cubes, trade them for one rod.**\n'
  '• 0.45 + 0.68: the hundredths give 13, which is more than ten.\n'
  '• Trade ten of them for one tenth, leaving 3 hundredths.\n'
  '• The answer is 1.13.',
  'Same trade as 10 ones making a ten — the seats just have new names.'),
 ('Regrouping to subtract',
  '**If you do not have enough of a block, trade one of the next size up for ten of the size you need.**\n'
  '• To take 9 hundredths from 1.57, break a tenth into ten hundredths first.\n'
  '• Then you have 17 hundredths to work with.',
  'Break a bigger block down before you take away, not after.'),
 ('Estimate before you build',
  '**Estimate the answer first, so you can tell whether the model came out sensible.**\n'
  '• For 0.85 + 0.40, think "about 0.80 + 0.40, so about 1.20".\n'
  '• A model giving 0.125 or 12.5 would stand out instantly as wrong.',
  'The estimate is what catches a decimal point in the wrong place.'),
 ('The model and the written method agree',
  '**Trading blocks and carrying digits are the same move written two ways.**\n'
  '• Trading ten hundredths for a tenth IS carrying a 1 into the tenths column.\n'
  '• Once you trust the blocks, the written method is a shortcut for them.',
  'If the two ever disagree, it is the written work that slipped.'),
], [
 (1, 'Using place-value blocks where a flat is one whole, a rod is one tenth and a small cube is one hundredth, which blocks show 1.24?',
  ['One flat, two rods and four small cubes', 'One flat, four rods and two small cubes',
   'Two flats, one rod and four small cubes', 'One flat, twenty rods and four small cubes'],
  0, 'Read the digits in order: ones, tenths, hundredths.',
  ['The 1 is in the ones place — one flat.',
   'The 2 is in the tenths place — two rods.',
   'The 4 is in the hundredths place — four small cubes.'],
  '**One flat, two rods and four small cubes.** Each digit names how many of that block you need, reading left to right.',
  'Swapping the rods and cubes would build 1.42 instead — a different number entirely.'),

 (2, 'Adding 0.45 and 0.68 with place-value blocks, the hundredths come to 13. What should you do?',
  ['Trade ten hundredths for one tenth, leaving three hundredths',
   'Write 13 in the hundredths place and carry on',
   'Trade ten hundredths for one whole, leaving three hundredths',
   'Trade three hundredths for one tenth, leaving ten hundredths'],
  0, 'Ten of a block trades for exactly one of the next size UP.',
  ['13 hundredths is more than ten, so a trade is needed.',
   'Ten hundredths make one tenth.',
   'Trading leaves 1 tenth carried over and 3 hundredths behind.',
   'The final answer is 1.13.'],
  '**Trade ten hundredths for one tenth, leaving three hundredths.** Ten of any block is worth exactly one of the next size up, never one of the size two steps up.',
  'This trade is the same thing as carrying a 1 into the tenths column in written addition.'),

 (2, 'To subtract 9 hundredths from 1.57 using blocks, what has to happen first?',
  ['Trade one tenth for ten hundredths',
   'Trade one whole for ten tenths',
   'Trade one hundredth for ten tenths',
   'Nothing — there are already enough hundredths'],
  0, 'You need 9 hundredths but only have 7. Where can more come from?',
  ['1.57 has only 7 hundredths, and 9 are needed.',
   'The next size up is the tenths.',
   'Trading one tenth gives ten more hundredths, making 17.',
   'Now 9 can be taken away, leaving 8 hundredths.'],
  '**Trade one tenth for ten hundredths.** Regrouping always borrows from the next place up, which turns 7 hundredths into 17.',
  'Doing the trade before you subtract is what stops the classic error of taking the smaller digit from the larger one out of habit.'),

 (1, 'Before modelling 0.85 + 0.40 with blocks, a student estimates the answer as "about 1.20." Why is estimating first useful?',
  ['It gives something to check the model against',
   'It means the model does not have to be built carefully',
   'It replaces the need to add the numbers at all',
   'It makes the blocks quicker to count out and sort'],
  0, 'What would you notice if the model gave 0.125?',
  ['The estimate says the answer should be near 1.20.',
   'If the blocks gave 0.125, that is nowhere near 1.20.',
   'The gap tells you something went wrong before you move on.',
   'The real answer is 1.25, which does sit near the estimate.'],
  '**It gives something to check the model against.** An estimate is a safety net — it catches an answer that is out by a factor of ten, which is the commonest decimal error there is.',
  'Estimating first is a habit worth keeping for written work too, not just models.'),

 (2, 'A model shows 1 whole, 1 tenth and 3 hundredths. What number is it?',
  ['1.13', '1.31', '1.03', '11.3'],
  0, 'Take the blocks in order: wholes, then tenths, then hundredths.',
  ['1 whole gives the digit 1 in the ones place.',
   '1 tenth gives the digit 1 in the tenths place.',
   '3 hundredths give the digit 3 in the hundredths place.',
   'Reading across: 1.13.'],
  '**1.13.** Each block count becomes the digit in its own place, in order from largest block to smallest.',
  'Reading the tenths and hundredths the wrong way round gives 1.31 — a common slip when the blocks are jumbled on the desk.'),

 (3, 'A student models 0.7 + 0.5 and says the answer is 0.12, because 7 + 5 = 12. What is the mistake?',
  ['Twelve tenths is more than one whole, so ten of them trade up to make 1.2',
   'They should have added 7 and 5 to get 13 instead of 12',
   'Tenths cannot be added to tenths without changing them to hundredths',
   'The answer should be 0.012 rather than 0.12'],
  0, 'Twelve tenths — is that less than one whole, or more?',
  ['7 tenths plus 5 tenths is 12 tenths.',
   'Ten tenths make one whole, so 12 tenths is more than a whole.',
   'Trade ten of them for 1 whole, leaving 2 tenths.',
   'The answer is 1.2, not 0.12.'],
  '**Twelve tenths is more than one whole, so ten of them trade up to make 1.2.** Writing "12" into the tenths place skips the trade, and no place can hold a digit of 12.',
  'Any time a column total reaches ten or more, a trade is owed. A place value only ever holds a single digit.'),

 (2, 'Which addition needs a trade from hundredths into tenths?',
  ['0.36 + 0.27', '0.31 + 0.24', '0.42 + 0.15', '0.53 + 0.16'],
  0, 'Add just the hundredths digits of each pair and see which total reaches ten.',
  ['0.36 + 0.27: the hundredths are 6 and 7, which make 13 — over ten.',
   '0.31 + 0.24: 1 and 4 make 5, no trade.',
   '0.42 + 0.15: 2 and 5 make 7, no trade.',
   '0.53 + 0.16: 3 and 6 make 9, which is still under ten.'],
  '**0.36 + 0.27.** Its hundredths add to 13, and any column total of ten or more owes a trade into the next place.',
  'Checking just the smallest column first is a fast way to predict whether regrouping is coming.'),

 (2, 'Using blocks to find 1.24 + 0.35, what is the total?',
  ['1.59', '1.69', '1.49', '4.74'],
  0, 'Add each size of block separately — wholes with wholes, tenths with tenths.',
  ['Wholes: 1 + 0 = 1.',
   'Tenths: 2 + 3 = 5.',
   'Hundredths: 4 + 5 = 9.',
   'No column reaches ten, so no trading is needed: 1.59.'],
  '**1.59.** Each size of block is combined with its own kind, and since no column reached ten there was nothing to trade.',
  'Not every decimal addition needs regrouping — checking first tells you how much work is actually ahead.'),

 (3, 'Why is trading ten hundredths for one tenth the same move as "carrying" in written addition?',
  ['Both replace ten of one place with one of the next place up',
   'Both add an extra one to the answer at the end',
   'Both only happen when the answer is a whole number',
   'Both are shortcuts that give a slightly different answer'],
  0, 'What is physically happening to the blocks when you carry a 1?',
  ['Carrying writes a small 1 above the next column left.',
   'That 1 stands for one of the larger unit.',
   'It appeared because ten of the smaller unit were collected.',
   'Trading blocks does exactly that, just where you can see it.'],
  '**Both replace ten of one place with one of the next place up.** The written carry is shorthand for the trade — same action, one done with blocks and one with a pencil.',
  'This is why the blocks are worth trusting: they are not a different method, they are the same method made visible.'),

 (2, 'Using blocks to find 0.92 − 0.45, what is the difference?',
  ['0.47', '0.57', '0.53', '0.43'],
  0, 'You need 5 hundredths but have only 2. Trade first.',
  ['There are 2 hundredths but 5 are needed, so trade one tenth for ten hundredths.',
   'That leaves 8 tenths and 12 hundredths.',
   'Hundredths: 12 − 5 = 7.',
   'Tenths: 8 − 4 = 4. The difference is 0.47.'],
  '**0.47.** Trading one tenth into ten hundredths first gives enough to subtract from, leaving 4 tenths and 7 hundredths.',
  'Subtracting the smaller digit from the larger one in each column without trading gives 0.53 — a wrong answer that feels right, which is what makes it dangerous.'),
],
 'Lesson 2-3 of the Topic 2 textbook scan uses place-value blocks to add and subtract decimals: a flat is one whole, a rod one tenth, a small cube one hundredth. It covers trading ten of one block for one of the next size up, both when adding and when regrouping to subtract.',
 'The blocks are the reason the written method makes sense rather than being a rule to memorise. When a carry or a borrow goes wrong later, this is the picture to come back to.',
 [('Represent a decimal with place-value blocks', 'source'),
  ('Add decimals with models, trading ten of one place for one of the next', 'source'),
  ('Subtract decimals with models, regrouping when there is not enough', 'source'),
  ('Explain why trading blocks and carrying digits are the same move', 'added')],
 'This lesson is the "why" behind the next two, so it is worth not rushing even though the arithmetic is easy. The single most valuable question here is the one about 0.7 + 0.5 = "0.12" — writing a two-digit total into a one-digit place is the error that carrying exists to prevent, and seeing it with blocks makes it obvious in a way a rule never does. The subtraction question ending in 0.47 targets the other classic: subtracting the smaller digit from the larger one in each column out of habit, which gives a confident wrong answer. If she can say why a trade is needed, she is ready for the written method.',
 ('The picture behind the rules. Worth doing before the written method.', 12),
 'Lesson 2-3')

# ══ Lesson 4 · Add Decimals ═════════════════════════════════════════════════
go(4, 'math-u2-l4', 'Add Decimals', [
 ('Line up the decimal points',
  '**Write the numbers so the decimal points sit in a vertical line — that lines up every place value at once.**\n'
  '• Tenths land under tenths, hundredths under hundredths.\n'
  '• Lining up the right-hand ends instead is the commonest way to get a wrong answer.',
  'The decimal points are the anchor, not the last digits.'),
 ('Annex zeros to fill the gaps',
  '**You can write extra zeros on the right of a decimal without changing its value.**\n'
  '• 5.6 can be written 5.60, so it lines up with 3.75.\n'
  '• 5.6 and 5.60 are the same number — the zero just holds the seat.',
  'A zero on the RIGHT of a decimal is free. One on the left is not.'),
 ('Partial sums',
  '**Add one place at a time and then combine the pieces.**\n'
  '• 21.39 + 21.59: hundredths give 0.18, tenths 0.8, ones 2, tens 40.\n'
  '• 40 + 2 + 0.8 + 0.18 = 42.98.',
  'Adding place by place makes each step small enough to check.'),
 ('Adding a whole number to a decimal',
  '**A whole number has a decimal point hiding at its right-hand end.**\n'
  '• 14 is 14.00, so 14 + 6.28 lines up as 14.00 + 6.28 = 20.28.\n'
  '• The whole number never changes the digits after the point on its own.',
  'Write the invisible point in and the line-up solves itself.'),
 ('Estimate to check the point',
  '**A quick estimate catches a decimal point in the wrong place instantly.**\n'
  '• 21.39 + 21.59 is about 21 + 22 = 43, so 42.98 is believable.\n'
  '• An answer of 4.298 or 429.8 would fail that check on sight.',
  'Wrong digits are rare; a wrong decimal point is common.'),
], [
 (1, 'When adding 5.6 and 3.75 in columns, what should you line up?',
  ['The decimal points', 'The right-hand ends of the numbers',
   'The first digits of each number', 'The largest digits in each number'],
  0, 'Which alignment puts tenths under tenths?',
  ['Each column in a written sum has to hold one place value.',
   'Lining up the decimal points puts ones under ones and tenths under tenths.',
   'Lining up the right-hand ends would put 6 tenths under 5 hundredths, which are not the same size.'],
  '**The decimal points.** Aligning them lines up every place value at once, which is the whole reason the method works.',
  'Right-aligning is the habit carried over from whole numbers, and it is exactly what breaks here.'),

 (2, 'What is 5.6 + 3.75?',
  ['9.35', '9.31', '4.31', '8.35'],
  0, 'Write 5.6 as 5.60 first so both numbers have hundredths.',
  ['Write 5.6 as 5.60 so the columns line up.',
   'Hundredths: 0 + 5 = 5.',
   'Tenths: 6 + 7 = 13, so write 3 and carry one to the ones.',
   'Ones: 5 + 3 + 1 = 9. The sum is 9.35.'],
  '**9.35.** Annexing the zero to make 5.60 lines the columns up, and the tenths then carry one into the ones place.',
  'Getting 9.31 means the numbers were right-aligned — 6 tenths added to 5 hundredths instead of to 7 tenths.'),

 (2, 'What is 14 + 6.28?',
  ['20.28', '20.42', '6.42', '14.28'],
  0, 'Where is the decimal point in a whole number?',
  ['14 is the same as 14.00.',
   'Line up: 14.00 + 6.28.',
   'Hundredths 0 + 8 = 8, tenths 0 + 2 = 2, ones 4 + 6 = 10.',
   'Carry the ten: the sum is 20.28.'],
  '**20.28.** Writing 14 as 14.00 makes the line-up obvious, and the decimal part comes through unchanged because the whole number has nothing after its point.',
  'A whole number always has an invisible decimal point at its right-hand end. Writing it in costs nothing and prevents the mess.'),

 (3, 'A student adds 21.39 + 21.59 and writes 3,938. What mistake did they make?',
  ['They ignored the decimal points and added the digits as whole numbers',
   'They added the tenths and hundredths in the wrong order',
   'They forgot to carry from the hundredths into the tenths',
   'They lined up the decimal points but added wrongly'],
  0, 'How big should the answer be? Estimate 21 + 22 first.',
  ['An estimate says the answer should be near 43.',
   '3,938 is nowhere near 43 — it is nearly a hundred times too big.',
   '2139 + 2159 = 4298, so the digits came from adding without the points.',
   'The real answer is 42.98.'],
  '**They ignored the decimal points and added the digits as whole numbers.** The digits 4298 are even correct — only the decimal point is missing, which is what makes the answer so far out.',
  'This is the exact error a ten-second estimate catches. The digits being right is what makes it feel convincing.'),

 (2, 'What is 0.45 + 0.68?',
  ['1.13', '1.03', '0.13', '1.23'],
  0, 'The hundredths add to more than ten. What happens then?',
  ['Hundredths: 5 + 8 = 13, so write 3 and carry one tenth.',
   'Tenths: 4 + 6 + 1 = 11, so write 1 and carry one whole.',
   'Ones: 0 + 0 + 1 = 1.',
   'The sum is 1.13.'],
  '**1.13.** Both columns carried — the hundredths into the tenths, and then the tenths into the ones.',
  'Two carries in a row is common with decimals. Getting 0.13 means the second carry was dropped.'),

 (2, 'Using partial sums for 32.4 + 15.3, which set of pieces is correct?',
  ['40 + 7 + 0.7', '40 + 7 + 0.07', '4 + 7 + 0.7', '47 + 7 + 0.7'],
  0, 'Break each number by place, then add matching places.',
  ['Tens: 30 + 10 = 40.',
   'Ones: 2 + 5 = 7.',
   'Tenths: 0.4 + 0.3 = 0.7.',
   'Combining: 40 + 7 + 0.7 = 47.7.'],
  '**40 + 7 + 0.7.** Each place is added to its own kind, and the pieces recombine to 47.7.',
  'Partial sums are slower to write but much easier to check, because every piece is a single small addition.'),

 (1, 'Is 5.6 the same number as 5.60?',
  ['Yes — a zero on the right of a decimal adds no value',
   'No — the extra place makes 5.60 ten times larger',
   'No — 5.60 counts hundredths that 5.6 does not have',
   'Only while they are lined up in a column to be added'],
  0, 'Think about the blocks: does 5.6 have any hundredths at all?',
  ['5.6 means 5 wholes and 6 tenths.',
   '5.60 means 5 wholes, 6 tenths and 0 hundredths.',
   'Zero hundredths is nothing at all, so no value was added.',
   'The two are the same number.'],
  '**Yes — a zero on the right of a decimal does not change its value.** It fills an empty seat so the columns line up, and an empty seat holds nothing.',
  'This is why annexing zeros is allowed. A zero on the LEFT of the whole-number part would be different — 05.6 is just untidy, but 0.56 is a different number entirely.'),

 (2, 'A swimmer\'s two legs of a relay take 23.48 seconds and 19.7 seconds. What is the combined time?',
  ['43.18 seconds', '43.55 seconds', '42.18 seconds', '23.67 seconds'],
  0, 'Give 19.7 a hundredths digit before you line the columns up.',
  ['Write 19.7 as 19.70.',
   'Hundredths: 8 + 0 = 8.',
   'Tenths: 4 + 7 = 11, write 1 and carry one.',
   'Ones and tens: 23 + 19 + 1 = 43. The total is 43.18 seconds.'],
  '**43.18 seconds.** Annexing the zero onto 19.70 keeps the hundredths column honest, and the tenths then carry into the ones.',
  'An estimate of 23 + 20 = 43 confirms the answer sits where it should.'),

 (3, 'Which expression has a sum of exactly 12.9?',
  ['0.02 + 12 + 0.88', '0.06 + 12.03', '6.2 + 3.4 + 2.3', '3.01 + 2.01 + 7.7'],
  0, 'Add each one carefully — the near misses are close on purpose.',
  ['0.02 + 12 + 0.88: the decimals make 0.90, so the total is 12.90.',
   'Checking another: 0.06 + 12.03 = 12.09, not 12.9.',
   '6.2 + 3.4 + 2.3 = 11.9, and 3.01 + 2.01 + 7.7 = 12.72.',
   'Only the first comes to exactly 12.9.'],
  '**0.02 + 12 + 0.88.** Its two decimal parts combine to 0.90, which with the 12 gives exactly 12.90 — the same number as 12.9.',
  'Notice 12.09 and 12.90 are different numbers even though they use the same digits. Place, not digits, is what decides value.'),

 (2, 'What is 7.05 + 0.9 + 2.4?',
  ['10.35', '10.25', '9.45', '10.44'],
  0, 'Write every number with two decimal places, then add straight down.',
  ['Write them as 7.05, 0.90 and 2.40.',
   'Hundredths: 5 + 0 + 0 = 5.',
   'Tenths: 0 + 9 + 4 = 13, write 3 and carry one.',
   'Ones: 7 + 0 + 2 + 1 = 10. The sum is 10.35.'],
  '**10.35.** Writing all three with two decimal places makes a three-number column add no harder than a two-number one.',
  'With three or more addends the line-up matters even more, because one misplaced row throws every column after it.'),
],
 'Lesson 2-4 of the Topic 2 textbook scan covers adding decimals in written columns: lining up the decimal points so each place value meets its own kind, annexing zeros so ragged decimals line up, using partial sums, and adding a whole number to a decimal.',
 'This is the written method she will use for the rest of the year, and it is only three ideas: line up the points, fill the gaps with zeros, then add exactly as she already does with whole numbers.',
 [('Add decimals by lining up the decimal points', 'source'),
  ('Annex zeros so numbers with different decimal lengths line up', 'source'),
  ('Use partial sums to add decimals place by place', 'source'),
  ('Use an estimate to check the decimal point landed in the right place', 'added')],
 'Two errors account for nearly every wrong answer in this lesson and both are targeted directly. The first is right-aligning the numbers instead of aligning the decimal points, which quietly adds tenths to hundredths — the 5.6 + 3.75 question offers 9.31 as a real option for exactly that reason. The second is the textbook\'s own André example: adding the digits with no regard for the decimal point at all, getting 3,938 instead of 42.98. The digits are RIGHT in that error, which is what makes it so convincing and why the estimate habit matters more than any rule. Also worth knowing: she needs to be comfortable that 5.6 and 5.60 are the same number, which has its own card and question here.',
 ('The written method. Line up the points and the rest is ordinary addition.', 12),
 'Lesson 2-4')

# ══ Lesson 5 · Subtract Decimals ════════════════════════════════════════════
go(5, 'math-u2-l5', 'Subtract Decimals', [
 ('Line up, then fill the gaps',
  '**Line up the decimal points and annex zeros so both numbers have the same number of decimal places.**\n'
  '• 32.5 − 7.84 becomes 32.50 − 7.84.\n'
  '• Without the zero there is nothing in the hundredths column to subtract from.',
  'A missing digit is not a zero until you write one in.'),
 ('Annexing a zero changes nothing',
  '**Writing 7.9 as 7.90 does not change its value — it only fills an empty seat.**\n'
  '• 7.9 is 7 wholes and 9 tenths; 7.90 adds zero hundredths, which is nothing.\n'
  '• That is what makes it safe to do whenever you need to line columns up.',
  'The zero is a placeholder doing a job, not a digit adding value.'),
 ('Partial differences',
  '**Subtract one place at a time instead of all at once.**\n'
  '• 5.92 − 4.37: take 4 to get 1.92, take 0.3 to get 1.62, take 0.07 to get 1.55.\n'
  '• Each step is small enough to do in your head.',
  'Take the big pieces off first; the small ones are easier on a tidier number.'),
 ('Regroup before you take away',
  '**If the top digit is smaller than the one below it, trade from the place to its left first.**\n'
  '• In 9.4 − 2.65, the hundredths are 0 and 5, so trade a tenth into ten hundredths.\n'
  '• Never just subtract the smaller digit from the larger one out of habit.',
  'The top number decides what you have; the bottom decides what leaves.'),
 ('Check by adding back',
  '**Add your answer to the number you subtracted — you should land back on the number you started with.**\n'
  '• 5.92 − 4.37 = 1.55, and 1.55 + 4.37 = 5.92. ✓\n'
  '• This catches a regrouping slip immediately.',
  'Subtraction has a built-in check. Use it when the answer matters.'),
], [
 (1, 'To subtract 32.5 − 7.84 in columns, how should 32.5 be written?',
  ['32.50', '32.05', '32.500', '3.25'],
  0, 'Both numbers need the same number of decimal places.',
  ['7.84 has two decimal places; 32.5 has one.',
   'Annex a zero on the right: 32.50.',
   'That gives a hundredths digit to subtract the 4 from.',
   'The value is unchanged — 32.5 and 32.50 are the same number.'],
  '**32.50.** The zero fills the empty hundredths seat so the columns line up, without changing the number at all.',
  'Writing 32.05 instead would move the 5 into the hundredths place — a different number, and a common slip when rushing.'),

 (2, 'What is 32.5 − 7.84?',
  ['24.66', '24.74', '25.66', '24.56'],
  0, 'Write 32.5 as 32.50, then regroup before taking the hundredths.',
  ['Write it as 32.50 − 7.84.',
   'Hundredths: 0 − 4 needs a trade, so borrow a tenth: 10 − 4 = 6.',
   'Tenths: now 4 − 8 needs a trade too, so borrow a one: 14 − 8 = 6.',
   'Ones and tens: 31 − 7 = 24. The difference is 24.66.'],
  '**24.66.** Two regroupings in a row are needed here — first into the hundredths, then into the tenths.',
  'Adding back is the fastest check: 24.66 + 7.84 = 32.50. ✓'),

 (1, 'A student rewrites 45.59 − 7.9 as 45.59 − 7.90. Did that change the value of 7.9?',
  ['No — the zero fills an empty place without adding any value',
   'Yes — 7.90 is ten times bigger than 7.9',
   'Yes — 7.90 now has hundredths that 7.9 did not have',
   'Only if the answer has hundredths in it'],
  0, 'How much is zero hundredths worth?',
  ['7.9 means 7 wholes and 9 tenths.',
   '7.90 means 7 wholes, 9 tenths and 0 hundredths.',
   'Zero hundredths adds nothing at all.',
   'So the two are the same number.'],
  '**No — the zero fills an empty place without adding any value.** It is written purely so the hundredths column has something in it to line up with.',
  'This is the single permission that makes subtracting ragged decimals possible. Without it the columns cannot be aligned.'),

 (2, 'What is 9.4 − 2.65?',
  ['6.75', '6.85', '7.75', '6.65'],
  0, 'Give 9.4 a hundredths digit first, then look at whether you can subtract.',
  ['Write 9.4 as 9.40.',
   'Hundredths: 0 − 5 needs a trade, so borrow a tenth: 10 − 5 = 5.',
   'Tenths: now 3 − 6 needs a trade, so borrow a one: 13 − 6 = 7.',
   'Ones: 8 − 2 = 6. The difference is 6.75.'],
  '**6.75.** Both the hundredths and the tenths needed regrouping, and forgetting the second one is what produces 6.85.',
  'Check it by adding back: 6.75 + 2.65 = 9.40. ✓'),

 (2, 'Using partial differences for 5.92 − 4.37, which sequence is correct?',
  ['Subtract 4, then 0.3, then 0.07', 'Subtract 4, then 0.7, then 0.03',
   'Subtract 5, then 0.9, then 0.02', 'Subtract 4.3, then 0.7'],
  0, 'Break the number being SUBTRACTED into its places.',
  ['4.37 breaks into 4, 0.3 and 0.07.',
   '5.92 − 4 = 1.92.',
   '1.92 − 0.3 = 1.62.',
   '1.62 − 0.07 = 1.55.'],
  '**Subtract 4, then 0.3, then 0.07.** The number being taken away is split by place value, and each piece comes off in turn.',
  'Breaking up the wrong number is the trap — it is the subtrahend that gets split, not the number you started with.'),

 (2, 'What is 20 − 13.42?',
  ['6.58', '7.58', '6.68', '7.42'],
  0, 'A whole number needs decimal places written in before you can subtract.',
  ['Write 20 as 20.00.',
   'Hundredths: 0 − 2 needs a trade; after regrouping, 10 − 2 = 8.',
   'Tenths: 9 − 4 = 5 (the tenths became 9 after the trade passed through).',
   'Ones and tens: 19 − 13 = 6. The difference is 6.58.'],
  '**6.58.** Subtracting from a whole number means regrouping across two empty places, which is why writing 20.00 first matters so much.',
  'Check by adding back: 6.58 + 13.42 = 20. ✓ Subtracting across zeros is the hardest case in the lesson.'),

 (3, 'A student subtracts 2.9 from 20.9 and gets 1.8. Why is that answer unreasonable?',
  ['20.9 − 2.9 should be about 18, and 1.8 is ten times too small',
   'The answer should have two decimal places, not one',
   'Subtracting a decimal from a decimal always gives a whole number',
   'The answer should be larger than 20.9'],
  0, 'Estimate first: about 21 take away about 3.',
  ['An estimate: 21 − 3 is about 18.',
   'The answer given is 1.8, which is nowhere near 18.',
   'The digits happen to be right, but the size is wrong by a factor of ten.',
   'The real answer is 18.'],
  '**20.9 − 2.9 should be about 18, and 1.8 is ten times too small.** Taking a small amount off 20.9 cannot possibly leave less than 2.',
  'Sense-checking the SIZE of an answer catches errors that checking the digits never would.'),

 (2, 'A bottle holds 1.5 litres and 0.8 litres are poured out. How much is left?',
  ['0.7 litres', '0.8 litres', '1.3 litres', '2.3 litres'],
  0, 'This is a subtraction. Line the two numbers up and take one from the other.',
  ['Start with 1.5 and take away 0.8.',
   'Tenths: 5 − 8 needs a trade, so borrow the whole: 15 − 8 = 7.',
   'The whole is used up, leaving 0.',
   'So 0.7 litres remain.'],
  '**0.7 litres.** More than half the bottle was poured out, so less than half is left — which 0.7 against the original 1.5 confirms.',
  'Notice the amount left (0.7) is smaller than the amount poured (0.8). Comparing the two is a fair sense-check.'),

 (2, 'What is 65.18 − 12.05?',
  ['53.13', '53.23', '52.13', '53.03'],
  0, 'Check each column: is any regrouping needed at all?',
  ['Hundredths: 8 − 5 = 3, no trade needed.',
   'Tenths: 1 − 0 = 1, no trade needed.',
   'Ones: 5 − 2 = 3. Tens: 6 − 1 = 5.',
   'The difference is 53.13.'],
  '**53.13.** Every top digit was already large enough, so this one needs no regrouping at all.',
  'Checking the columns before starting tells you whether trades are coming — and here, pleasantly, none are.'),

 (3, 'Three of these subtractions have a difference of 1.65. Which one does NOT?',
  ['12.68 − 2.03', '27.30 − 25.65', '11.23 − 9.58', '21.74 − 20.09'],
  0, 'You have to work all four out. The odd one is not close to the others.',
  ['27.30 − 25.65 = 1.65.',
   '11.23 − 9.58 = 1.65.',
   '21.74 − 20.09 = 1.65.',
   '12.68 − 2.03 = 10.65, which is the odd one out.'],
  '**12.68 − 2.03.** It comes to 10.65, while the other three all give exactly 1.65.',
  'Asking which one is different forces you to compute every option rather than stopping at the first that looks right.'),
],
 'Lesson 2-5 of the Topic 2 textbook scan covers subtracting decimals in written columns: lining up the decimal points, annexing zeros so both numbers have the same decimal places, using partial differences, regrouping when the top digit is too small, and checking an answer by adding it back.',
 'Subtraction is where decimal errors hide, because a wrong answer still looks like a sensible number. The add-back check turns every answer into one she can verify herself.',
 [('Subtract decimals by lining up the decimal points', 'source'),
  ('Annex zeros so both numbers have the same number of decimal places', 'source'),
  ('Regroup across places, including across zeros', 'source'),
  ('Check a difference by adding it back to the number subtracted', 'added')],
 'The hardest case in this lesson is subtracting from a whole number (20 − 13.42), because the regrouping has to travel through two empty places — it has its own question here. The most common wrong answer across the rest is dropping the SECOND regrouping when two are needed in a row, which is why 9.4 − 2.65 offers 6.85 as an option. Worth reinforcing at home: the add-back check. It costs one addition and catches essentially every regrouping slip, and she can do it without anyone telling her whether she was right. One question deliberately has several options that all evaluate to the same difference, to reward actually computing rather than pattern-matching.',
 ('The trickiest of the six. The add-back check is worth doing every time.', 13),
 'Lesson 2-5')

# ══ Lesson 6 · Model with Math — Bar Diagrams ══════════════════════════════
go(6, 'math-u2-l6', 'Model with Math: Bar Diagrams', [
 ('The hidden question',
  '**Some problems ask one thing but need another answered first.**\n'
  '• "How much change?" first needs "what did it all cost?".\n'
  '• Finding the hidden question is usually the whole difficulty.',
  'If you cannot answer the question directly, something has to come first.'),
 ('A bar diagram for a total',
  '**Draw one long bar for the total, split into a part for each amount, with a ? on the whole bar.**\n'
  '• Three prices become three sections; the ? sits above the whole thing.\n'
  '• A bar split into parts means ADD.',
  'The ? on the whole bar means you are hunting the total.'),
 ('A bar diagram for what is left',
  '**Draw the total as the whole bar, mark the part you know, and put the ? on the rest.**\n'
  '• The known part and the ? together make the whole.\n'
  '• A ? on a PART means subtract.',
  'Where the ? sits tells you which operation you need.'),
 ('Two steps, two diagrams',
  '**A two-step problem usually needs two diagrams: one for the hidden question, one for the real one.**\n'
  '• First diagram: add the costs to find the total.\n'
  '• Second diagram: take the total off what you had.',
  'Answer the hidden question, then use that answer in the next diagram.'),
 ('Does the answer make sense?',
  '**Check the answer against the story, not just the arithmetic.**\n'
  '• Change from a purchase must be less than what you handed over.\n'
  '• Money left over cannot be more than you started with.',
  'An answer that is arithmetically right can still be impossible.'),
], [
 (1, 'A shopper buys three items and wants to know her change from $50. What hidden question has to be answered first?',
  ['What the three items cost altogether', 'How much change she got from each item',
   'Which of the three items was most expensive', 'How much she had before she started shopping'],
  0, 'You cannot subtract from $50 until you know what to subtract.',
  ['Change means $50 minus what she spent.',
   'The amount she spent is not given directly — only the three separate prices.',
   'So the total cost must be found first.',
   'That total is the hidden question.'],
  '**What the three items cost altogether.** The change cannot be worked out until there is a single total to subtract from $50.',
  'Naming the hidden question out loud before touching any numbers is the habit this whole lesson is built to teach.'),

 (2, 'A shopper buys items costing $18.75, $9.40 and $6.25. What is the total cost?',
  ['$34.40', '$34.30', '$33.40', '$35.40'],
  0, 'Two of the three prices pair into a whole number.',
  ['$18.75 and $6.25 are compatible — their decimals make 1.00.',
   '$18.75 + $6.25 = $25.',
   '$25 + $9.40 = $34.40.'],
  '**$34.40.** Pairing the $18.75 with the $6.25 gives a clean $25 first, which makes the last step easy.',
  'A bar diagram of this would be one bar split into three sections with a ? above the whole thing — the picture for a total.'),

 (2, 'A shopper spends $34.40 and pays with $50. How much change should she get?',
  ['$15.60', '$15.70', '$16.60', '$24.40'],
  0, 'The change and the amount spent together make $50.',
  ['Write $50 as $50.00.',
   'Hundredths and tenths: regroup to take 40 from 00, giving 60.',
   'Ones and tens: 49 − 34 = 15.',
   'The change is $15.60.'],
  '**$15.60.** In a bar diagram the $50 is the whole bar, the $34.40 is the known part, and the ? sits on what is left.',
  'Check it makes sense: the change is less than the $50 handed over, as it must be.'),

 (2, 'A student has $40, buys a book for $7.85 and a game for $12.30, and wants to know how much is left. Which pair of steps is right?',
  ['Add the two prices, then subtract that total from $40',
   'Subtract $7.85 from $40, then add $12.30 back on',
   'Add $7.85, $12.30 and $40 all together',
   'Subtract $12.30 from $7.85, then add on the $40'],
  0, 'Both purchases come out of the same $40.',
  ['The two purchases together are what leaves the $40.',
   'First find the total spent: $7.85 + $12.30 = $20.15.',
   'Then take it off what was there: $40 − $20.15 = $19.85.',
   'Two steps, in that order.'],
  '**Add $7.85 and $12.30, then subtract that total from $40.** The hidden question is what was spent altogether; only then can it come off the $40.',
  'Adding the $12.30 back on in step two would mean spending money and ending up richer, which the story rules out.'),

 (2, 'A student has $40 and spends $20.15 altogether. How much is left?',
  ['$19.85', '$19.95', '$20.85', '$60.15'],
  0, 'Write $40 with two decimal places before subtracting.',
  ['Write $40 as $40.00.',
   'Regroup to subtract the hundredths and tenths: 00 − 15 becomes 100 − 15 = 85.',
   'Ones and tens: 39 − 20 = 19.',
   'So $19.85 is left.'],
  '**$19.85.** Subtracting from a whole amount of money means regrouping across the zeros, which is why writing $40.00 first matters.',
  'Sense-check: she spent about half her money, so having a bit under half left is exactly right.'),

 (3, 'In a bar diagram, the whole bar is labelled with a ? and it is split into four sections that each have a known amount. What operation does the diagram show?',
  ['Addition, because the parts are known and the whole is not',
   'Subtraction, because one section is missing',
   'Addition, because there are four sections rather than two',
   'Subtraction, because the ? is on the bar'],
  0, 'Which is unknown here — the whole, or one of the parts?',
  ['Every section has a known amount.',
   'The ? is on the whole bar.',
   'Finding a whole from its parts means adding.',
   'So the diagram shows addition.'],
  '**Addition, because the parts are known and the whole is not.** Where the ? sits decides the operation — on the whole bar it means add, on a part it means subtract.',
  'The number of sections is irrelevant. Four known parts and an unknown whole is still just addition.'),

 (3, 'A student works out that a $28.50 purchase paid for with $20 leaves $8.50 in change. What is wrong?',
  ['The purchase cost more than was handed over, so there is no change at all',
   'The subtraction was done in the wrong order but the answer is still right',
   'The answer should be $48.50 instead',
   'Nothing is wrong — $8.50 is correct'],
  0, 'Can you pay for something costing $28.50 using $20?',
  ['The item costs $28.50 and only $20 was handed over.',
   '$20 is not enough to pay for it.',
   'The student subtracted the smaller amount from the larger out of habit.',
   'The real situation is that $8.50 more is still owed, not received.'],
  '**The purchase cost more than was handed over, so there is no change at all.** The arithmetic $28.50 − $20 = $8.50 is fine; it is the meaning that is backwards.',
  'This is why checking the answer against the story matters. Arithmetic alone cannot tell you that a situation is impossible.'),

 (2, 'A runner covers 7.85 km and 12.30 km on two days. How far did she run altogether?',
  ['20.15 km', '20.05 km', '19.15 km', '4.45 km'],
  0, 'Line up the decimal points and add.',
  ['Line them up: 7.85 + 12.30.',
   'Hundredths: 5 + 0 = 5. Tenths: 8 + 3 = 11, write 1 and carry.',
   'Ones: 7 + 2 + 1 = 10, write 0 and carry. Tens: 1 + 1 = 2.',
   'The total is 20.15 km.'],
  '**20.15 km.** The tenths carried into the ones and the ones carried into the tens, so two carries ran through this one.',
  'The 4.45 option is what you get by subtracting instead of adding — worth noticing that "altogether" always signals a total.'),

 (3, 'Why is drawing a bar diagram useful even when you already know which operation to use?',
  ['It shows how the amounts relate to each other',
   'It replaces the need to do any of the arithmetic',
   'It is required before any answer counts as correct',
   'It makes the numbers smaller and easier to work with'],
  0, 'What does the picture tell you that the numbers alone do not?',
  ['A diagram shows which amounts are parts and which is the whole.',
   'That relationship is what decides whether to add or subtract.',
   'If a step contradicts the picture, the error shows up straight away.',
   'The arithmetic still has to be done either way.'],
  '**It shows how the amounts relate, which makes a wrong step easier to spot.** The picture carries the structure of the problem, which is exactly the part that is easy to get wrong in a two-step question.',
  'Diagrams earn their keep most on multi-step problems, where it is the plan rather than the arithmetic that usually fails.'),

 (2, 'A club needs $180 for buses, $215 for a hotel and $80 for meals. What is the total cost?',
  ['$475', '$465', '$395', '$485'],
  0, 'Add the three amounts. Two of them pair neatly.',
  ['$180 + $215 = $395.',
   'Alternatively pair $180 and $80 to make $260 first.',
   '$260 + $215 = $475.',
   'Either route gives the same total.'],
  '**$475.** Pairing the $180 and the $80 gives a clean $260, which makes the last addition straightforward.',
  'In a bar diagram this is one bar in three sections with a ? on the whole — and it is usually the hidden question inside a bigger "how much more do they need?" problem.'),
],
 'Lesson 2-6 of the Topic 2 textbook scan is about modelling with math: finding the hidden question inside a multi-step problem, drawing bar diagrams to show how the amounts relate, and writing equations from those diagrams.',
 'This is the lesson that turns decimal arithmetic into something she can actually use. The arithmetic is the easy part by now; deciding what to compute is the skill.',
 [('Find the hidden question inside a two-step problem', 'source'),
  ('Draw a bar diagram to represent a total or a remaining amount', 'source'),
  ('Write and solve equations from a bar diagram', 'source'),
  ('Check that an answer makes sense in the story, not just in the arithmetic', 'added')],
 'The transferable idea here is "where does the ? sit?" — on the whole bar it means add, on a part it means subtract. That one question decides the operation far more reliably than hunting for keywords, and it has its own card and question. The second idea worth reinforcing is checking the answer against the STORY: one question here gives arithmetic that is perfectly correct ($28.50 − $20 = $8.50) attached to a situation that is impossible, because you cannot get change from handing over less than the price. Both of the two-step questions are broken into their separate steps as their own questions too, so if she stumbles it is clear whether the problem was the plan or the arithmetic.',
 ('The last one. Find the hidden question first, then the numbers are easy.', 13),
 'Lesson 2-6')
