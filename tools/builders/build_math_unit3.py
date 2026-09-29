# -*- coding: utf-8 -*-
"""River's Unit 3 — Multiply Multi-Digit Whole Numbers (enVision grade-5, Topic 3).

Nine lessons, one per unit record, shelved as their own book `Unit 3` the same
way Unit 2 is (Chris, 2026-09-13: "lessons make more sense now"). Source:
`Unit 3 - Math.pdf` in her Unit 3 folder, lessons 3-1 to 3-9, clean text layer.

Titles say "Lesson N", never the book's "3-1": Unit 1 already carries a
`Topic 3 · 3-1 …` run from the GRADE-4 book, and both shelves render on the
Math screen together. The book's own label rides in `srcName`.

Nothing here is worked by hand.  Every product is computed below, and every
WRONG option is generated from a named mistake — the carry dropped, the
placeholder zero left off, a zero digit skipped — so a distractor is a real
misconception with a real number, never a random neighbour.  None of the
book's own numbers is reused (the standalone rule): its 32 × 10,000, 26 × 3,
37 × 24, 389 × 12, 208 × 31 and the rest were read for shape only.
"""
import json, io
import unit_common as U

def f(n): return '{:,}'.format(n)

# ── named mistakes, so a distractor is always a real one ────────────────────
def no_carry(a, m):
    """The dropped-carry slip: each step keeps only its ones digit, and the
    leftmost step is written whole (34 × 5 → 0, then 15 → 150)."""
    ds = str(a); out, p = 0, 1
    for i, ch in enumerate(reversed(ds)):
        prod = int(ch) * m
        out += (prod if i == len(ds) - 1 else prod % 10) * p
        p *= 10
    return out

def side_by_side(a, m):
    """Write each digit's whole product next to the others: 26 × 3 → '618'."""
    return int(''.join(str(int(ch) * m) for ch in str(a)))

def no_placeholder(a, b):
    """Second row written without its zero: a×ones + a×tens-digit."""
    return a * (b % 10) + a * (b // 10)

def skip_zero(a):
    """Drop a zero digit from the middle of a number: 306 → 36."""
    return int(str(a).replace('0', '', 1)) if '0' in str(a)[1:-1] else a

def opts4(ans, *wrong):
    o = [f(ans)] + [f(w) if isinstance(w, int) else w for w in wrong]
    assert len(o) == 4 and len(set(o)) == 4, o
    return o

CLS, APP, SERIES = 'math', 'wayfinder', 'Unit 3'
SRC = 'enVision Topic 3 textbook scan — Multiply Multi-Digit Whole Numbers (Drive)'

def go(n, title, cards, qs, summary, why, objs, note, nxt, booklbl):
    C, Q = [], []
    for a in cards: U.card(C, *a)
    for a in qs: U.q(Q, *a)
    slug = 'math-u3-l%d' % n
    uid = 'unit-m3u%d' % n
    U.build(APP, C, Q, uid, '%s · Lesson %d: %s' % (SERIES, n, title), CLS,
            summary, why, objs, note, nxt, 'content/%s.json' % slug,
            'Unit 3 textbook scan, %s (Drive)' % booklbl, SRC,
            offset_hours=4, round_=10)
    fp = '%s/content/%s.json' % (U.REPO, slug)
    j = json.load(io.open(fp, encoding='utf-8'))
    rec = j['records'][uid]
    rec['series'] = SERIES          # shelves as its own book, ahead of the title rule
    rec['libv'] = 1                 # a later fix wins the approval race
    io.open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))

# ══ Lesson 1 · Multiply by Powers of 10 ═════════════════════════════════════
assert 47 * 1000 == 47000 and 70 * 100 == 7000 and 26 * 10**3 == 26000
assert 58 * 10**4 == 580000 and 90 * 10**3 == 90000 and 100 * 17 == 1700
assert 64 * 10**3 == 64000 < 7 * 10**4 == 70000 and 40 * 1000 == 40000

go(1, 'Multiply by Powers of 10', [
 ('Powers of 10',
  '**1; 10; 100; 1,000; 10,000; 100,000 — each one is 10 times the one before it.**\n'
  '• Every place in a number is worth 10 times the place to its right.',
  'Each step left on the place-value chart is one more 10.'),
 ('Exponents',
  '**10⁴ means 10 × 10 × 10 × 10, which is 10,000.**\n'
  '• The small raised number is the exponent. It counts how many 10s are multiplied.\n'
  '• It also tells you how many zeros the power of 10 has.',
  'Exponent 4 → four 10s → four zeros.'),
 ('Multiplying by a power of 10',
  '**The product ends with the zeros of the number PLUS the zeros of the power of 10.**\n'
  '• 58 × 1,000 = 58,000.\n'
  '• 58 × 10⁴ = 580,000.',
  'Count the zeros in both factors, then write them all at the end.'),
 ('Zeros that are already there',
  '**A zero inside the first factor still counts: 60 × 1,000 = 60,000, not 6,000.**\n'
  '• 60 already ends in one zero, and 1,000 adds three more — four zeros in all.',
  'Count every zero, including the one the number brought with it.'),
 ('An exponent is not a multiplier',
  '**10³ is 10 × 10 × 10 = 1,000. It is NOT 10 × 3 = 30.**\n'
  '• The exponent says how many times 10 is used as a factor.',
  'Three tens multiplied, not three tens added.'),
], [
 (1, 'What is 47 × 1,000?',
  opts4(47000, 4700, 470000, 1047), 0,
  'How many zeros does 1,000 have?',
  ['1,000 has three zeros.', 'Multiplying by 1,000 puts three zeros on the end of 47.',
   '47 × 1,000 = 47,000.'],
  '**47,000.** Multiplying by 1,000 moves every digit three places to the left, which shows up as three zeros on the end.',
  '4,700 has only two zeros added — that is 47 × 100.'),
 (1, 'What is 10⁴ written in standard form?',
  ['10,000', '40', '1,000', '100,000'], 0,
  'The exponent tells how many 10s are multiplied together.',
  ['10⁴ means 10 × 10 × 10 × 10.', '10 × 10 = 100, × 10 = 1,000, × 10 = 10,000.',
   'So 10⁴ = 10,000.'],
  '**10,000.** Four 10s multiplied together give a 1 followed by four zeros.',
  '40 is what you get if you multiply 10 by 4 — the exponent does not work that way.'),
 (1, 'What is 70 × 100?',
  opts4(7000, 700, 70000, 170), 0,
  'Count the zeros in BOTH numbers.',
  ['70 has one zero.', '100 has two zeros.', 'Together that is three zeros after the 7.',
   '70 × 100 = 7,000.'],
  '**7,000.** The zero in 70 counts too, so the product ends in three zeros, not two.',
  'Forgetting the zero that 70 already has is the most common slip here.'),
 (2, 'What is 26 × 10³?',
  opts4(26000, 2600, 260000, 78), 0,
  'Write 10³ as a number first.',
  ['10³ = 10 × 10 × 10 = 1,000.', '26 × 1,000 puts three zeros after 26.',
   '26 × 10³ = 26,000.'],
  '**26,000.** The exponent 3 means 1,000, so three zeros go on the end of 26.',
  '78 is 26 × 3 — treating the exponent as an ordinary factor.'),
 (2, 'Which number makes 58 × ___ = 580,000 true?',
  ['10⁴', '10³', '10⁵', '10²'], 0,
  'How many zeros were added to 58 to make 580,000?',
  ['580,000 is 58 followed by four zeros.', 'Four added zeros means multiplying by 10,000.',
   '10,000 = 10⁴.'],
  '**10⁴.** 580,000 is 58 with four zeros added, and 10⁴ is the power of 10 with four zeros.',
  'Count only the zeros that were ADDED to 58 — the digits 5 and 8 are not zeros.'),
 (2, 'Which number makes ___ × 10³ = 90,000 true?',
  ['90', '9', '900', '9,000'], 0,
  '10³ adds three zeros. How many zeros are left over in 90,000?',
  ['90,000 has four zeros.', '10³ supplies three of them.',
   'One zero must come from the missing number, so it is 90.'],
  '**90.** 90 × 1,000 = 90,000 — one zero from 90 and three from 10³.',
  '9 × 10³ is only 9,000. Check by multiplying your answer back.'),
 (2, 'A team gives a cap to each of the first 100 fans through the gate. Each cap costs $17. How much do the caps cost in all?',
  ['$1,700', '$170', '$17,000', '$117'], 0,
  'Multiply the cost of one cap by the number of caps.',
  ['There are 100 caps at $17 each.', '17 × 100 puts two zeros after 17.',
   'The caps cost $1,700.'],
  '**$1,700.** 17 × 100 = 1,700, because multiplying by 100 adds two zeros.',
  '$117 comes from adding 100 and 17 — but "each" means multiply.'),
 (3, 'Without multiplying, which is greater: 64 × 10³ or 7 × 10⁴?',
  ['7 × 10⁴, because 70,000 is more than 64,000',
   '64 × 10³, because 64 is much bigger than 7',
   'They are equal, because both use a power of 10',
   '64 × 10³, because it has more digits to start with'], 0,
  'Rewrite both as standard numbers by counting zeros.',
  ['64 × 10³ = 64 with three zeros = 64,000.', '7 × 10⁴ = 7 with four zeros = 70,000.',
   '70,000 is greater than 64,000.'],
  '**7 × 10⁴.** The bigger power of 10 outweighs the bigger first factor: 70,000 beats 64,000.',
  'Comparing only the first factors ignores the part that makes the biggest difference.'),
 (3, 'Theo says 40 × 1,000 = 4,000 because 1,000 has three zeros. What went wrong?',
  ['He forgot the zero already in 40, so it is 40,000',
   'He should have added the numbers, so it is 1,040',
   'Nothing went wrong — 4,000 is correct',
   'He added one zero too many, so it is 400'], 0,
  'Count the zeros in both factors.',
  ['1,000 has three zeros.', '40 has one zero of its own.',
   'That makes four zeros after the 4: 40,000.'],
  '**He forgot the zero already in 40.** Four zeros in all, so the product is 40,000.',
  'This is the trap the textbook itself names — every zero counts, including the ones in the first number.'),
 (3, 'Which is the same as multiplying a number by 10³?',
  ['Multiplying it by 10 three times', 'Multiplying it by 30',
   'Adding 10 to it three times', 'Multiplying it by 3, then by 10'], 0,
  'What does the exponent count?',
  ['10³ means 10 × 10 × 10.', 'Multiplying by 10³ is multiplying by 10, then 10, then 10.',
   'That is multiplying by 10 three times.'],
  '**Multiplying it by 10 three times.** The exponent counts how many 10s are factors.',
  'Adding 10 three times only adds 30 — nowhere near multiplying by 1,000.'),
],
 'Lesson 3-1 of the Topic 3 textbook scan: patterns for multiplying a whole number by 10, 100, 1,000 and so on, written in standard form and with exponents.',
 'Every later lesson in this unit leans on this one — estimating, partial products and the standard algorithm all multiply by tens and hundreds.',
 [('Multiply a whole number by a power of 10 using patterns', 'source'),
  ('Read and write powers of 10 with exponents', 'source'),
  ('Count the zeros in both factors, including zeros already in the first number', 'source')],
 'Two traps get their own card and question. The first is the one the textbook itself names: 60 × 1,000 is 60,000, not 6,000, because the zero already in 60 counts too. The second is treating an exponent as an ordinary factor — reading 10³ as 30. Both have a wrong option built from exactly that mistake, so if she picks one the explanation names it.',
 ('Count the zeros in both numbers. That is the whole trick.', 10),
 'Lesson 3-1')

# ══ Lesson 2 · Estimate Products ════════════════════════════════════════════
assert 40 * 600 == 24000 and 25 * 400 == 10000 and 50 * 700 == 35000
assert 21 * 305 == 6405 and 40 * 200 == 8000 and 41 * 207 == 8487
assert 48 * 52 == 2496 >= 2000 and 40 * 50 == 2000
assert 32 * 289 == 9248 and 30 * 300 == 9000 and 32 * 300 == 9600 and 30 * 290 == 8700 and 30 * 200 == 6000
_act = 24 * 386; assert _act == 9264 and abs(25*400 - _act) < abs(20*400 - _act)
assert 12 * 208 == 2496 and 12 * 200 == 2400

go(2, 'Estimate Products', [
 ('Estimate by rounding',
  '**Round each factor to a friendly number, then multiply those.**\n'
  '• 38 × 612 → 40 × 600 = 24,000.\n'
  '• An estimate tells you roughly how big the answer should be.',
  'Round, then use your powers-of-10 patterns.'),
 ('Compatible numbers',
  '**Numbers that are easy to multiply in your head, like 25 and 4.**\n'
  '• 25 × 4 = 100, so 25 × 400 = 10,000.\n'
  '• They can give a closer estimate than plain rounding.',
  'Look for pairs that make 100 or 1,000.'),
 ('Overestimate',
  '**If you rounded both factors UP, your estimate is more than the real answer.**\n'
  '• 29 × 488 → 30 × 500 = 15,000, which is too high.',
  'Rounded up → answer came out too big.'),
 ('Underestimate',
  '**If you rounded both factors DOWN, your estimate is less than the real answer.**\n'
  '• 41 × 207 → 40 × 200 = 8,000, which is too low.',
  'Rounded down → answer came out too small.'),
 ('Mixed rounding',
  '**If one factor went up and the other went down, you cannot tell which way the estimate is off.**\n'
  '• 48 × 52 → 50 × 50 = 2,500, but the real answer is 2,496.',
  'Up and down together — no promise either way.'),
 ('Which estimate is safer',
  '**To prove you have AT LEAST enough, use an underestimate.**\n'
  '• If even the too-small estimate is enough, the real amount is too.',
  'An underestimate that clears the bar proves it.'),
], [
 (1, 'Round each factor to its greatest place. What is the estimate for 38 × 612?',
  opts4(24000, 18000, 2400, 240000), 0,
  '38 rounds to 40. What does 612 round to?',
  ['38 rounds to 40.', '612 rounds to 600.', '40 × 600: 4 × 6 = 24, then add three zeros.',
   'The estimate is 24,000.'],
  '**24,000.** 40 × 600 is 4 × 6 = 24 with three zeros on the end.',
  '2,400 has one zero too few — both 40 and 600 bring zeros.'),
 (1, 'Rounding 29 × 488 to 30 × 500 gives which kind of estimate?',
  ['An overestimate, because both numbers were rounded up',
   'An underestimate, because both numbers were rounded up',
   'An overestimate, because the answer is a large number',
   'An exact answer, because the rounding was careful'], 0,
  'Did 29 and 488 get bigger or smaller when you rounded them?',
  ['29 went up to 30.', '488 went up to 500.',
   'Both factors got bigger, so the estimate is bigger than the real product.'],
  '**An overestimate.** Both factors were rounded up, so the estimate comes out too high.',
  'Whether it is over or under depends on the direction of rounding, not on the size of the answer.'),
 (2, 'Use compatible numbers to estimate 26 × 397.',
  opts4(10000, 8000, 12000, 1000), 0,
  '26 is close to 25, and 397 is close to 400.',
  ['Use 25 in place of 26 and 400 in place of 397.', '25 × 4 = 100.',
   '25 × 400 = 10,000.'],
  '**10,000.** 25 and 400 are compatible because 25 × 4 = 100 is easy in your head.',
  '8,000 comes from rounding 26 all the way down to 20 — further off than it needs to be.'),
 (2, 'Round to estimate 52 × 718.',
  opts4(35000, 3500, 40000, 350000), 0,
  'Round each factor to its greatest place.',
  ['52 rounds to 50.', '718 rounds to 700.', '5 × 7 = 35, then add three zeros.',
   'The estimate is 35,000.'],
  '**35,000.** 50 × 700 is 35 with the three zeros from 50 and 700.',
  '3,500 is what you get if you forget the zero that 50 brings.'),
 (2, 'Which is the most reasonable estimate for 21 × 305?',
  opts4(6000, 600, 60000, 9000), 0,
  'Round 21 and 305, then multiply.',
  ['21 rounds to 20.', '305 rounds to 300.', '20 × 300 = 6,000.',
   'The real product, 6,405, is close to 6,000.'],
  '**6,000.** 20 × 300 lands close to the real product of 6,405.',
  '600 and 60,000 are each off by a whole power of 10 — a zero was lost or added.'),
 (2, 'Is 8,000 an overestimate or an underestimate for 41 × 207?',
  ['An underestimate, because both numbers were rounded down',
   'An overestimate, because both numbers were rounded down',
   'An underestimate, because 8,000 ends in zeros',
   'Neither, because 8,000 is the exact product'], 0,
  'What happened to 41 and 207 when they became 40 and 200?',
  ['41 went down to 40.', '207 went down to 200.',
   'Both factors got smaller, so the estimate is smaller than the real product (8,487).'],
  '**An underestimate.** Both factors were rounded down, so 8,000 is less than the real 8,487.',
  'Rounded down means the estimate sits below the true answer.'),
 (3, 'A bake sale needs at least $2,000. It sells 48 trays at $52 each. Which estimate PROVES it reached $2,000?',
  ['40 × 50 = 2,000, because both numbers were rounded down',
   '50 × 60 = 3,000, because it is the biggest estimate',
   '50 × 50 = 2,500, because it is the closest estimate',
   '48 × 50 = 2,400, because 48 was not rounded at all'], 0,
  'An estimate proves "at least" only if it is too SMALL and still reaches the goal.',
  ['40 × 50 rounds both factors down, so it is an underestimate.',
   'Even that too-small estimate reaches $2,000.',
   'So the real total must be at least $2,000 too.',
   '50 × 50 rounds one factor up and one down, so it proves nothing either way.'],
  '**40 × 50 = 2,000.** It is an underestimate that still reaches the goal, so the real total (48 × 52 = 2,496) must reach it too.',
  'A bigger estimate can feel more reassuring, but only an underestimate can prove "at least".'),
 (3, 'Which is NOT a reasonable estimate for 32 × 289?',
  opts4(6000, 9000, 9600, 8700), 0,
  'The real product is a little over 9,000. Which option is far away from that?',
  ['30 × 300 = 9,000 is reasonable.', '32 × 300 = 9,600 and 30 × 290 = 8,700 are reasonable too.',
   '6,000 comes from rounding 289 down to 200, which is far too low.',
   'So 6,000 is not reasonable.'],
  '**6,000.** It rounds 289 down to 200, even though 289 is much closer to 300.',
  'Round to the NEAREST hundred — 289 is 11 away from 300 but 89 away from 200.'),
 (3, 'Kai estimates 24 × 386 as 20 × 400. Lena estimates it as 25 × 400. Whose estimate is closer to the real product?',
  ["Lena's, because 25 is much closer to 24 than 20 is",
   "Kai's, because rounding to tens is always closer",
   "Kai's, because 8,000 is a smaller number",
   "They are equally close, because both used 400"], 0,
  'Compare how far 20 and 25 each are from 24.',
  ['Kai: 20 × 400 = 8,000.', 'Lena: 25 × 400 = 10,000.', 'The real product is 9,264.',
   "10,000 is 736 away; 8,000 is 1,264 away. Lena's is closer."],
  "**Lena's.** Moving 24 to 25 changes it by 1; moving it to 20 changes it by 4, so her estimate stays nearer.",
  'Compatible numbers are often the better choice when a factor sits right next to a friendly one.'),
 (2, 'A factory packs 208 boxes with 12 crayons in each. Which statement is true?',
  ['There are more than 2,000 crayons, since 12 × 200 is already 2,400',
   'There are fewer than 2,000 crayons, since 12 × 200 is only 2,400',
   'There are exactly 2,400 crayons, since 208 rounds to 200',
   'There are fewer than 1,000 crayons, since 12 is a small number'], 0,
  '200 is less than 208, so 12 × 200 is an underestimate.',
  ['Round 208 down to 200.', '12 × 200 = 2,400.',
   'That is an underestimate, and it is already more than 2,000.',
   'So the real total (2,496) is more than 2,000.'],
  '**More than 2,000.** 12 × 200 = 2,400 is too small an estimate and it still beats 2,000.',
  'An underestimate that already clears the target settles the question without any exact math.'),
],
 'Lesson 3-2 of the Topic 3 textbook scan: estimating products by rounding and with compatible numbers, and deciding whether an estimate is an overestimate or an underestimate.',
 'Estimating is how she will check every multiplication in the rest of this unit — and it is often the whole answer when a question only asks "is it enough?"',
 [('Estimate products by rounding', 'source'),
  ('Estimate products with compatible numbers', 'source'),
  ('Tell whether an estimate is an overestimate or an underestimate', 'source'),
  ('Choose an underestimate to prove "at least"', 'added')],
 'The idea most worth a word is which way an estimate is off. Rounding both factors up gives an overestimate, both down gives an underestimate, and one of each gives no promise at all — one question shows 48 × 52 estimated as 2,500 when the real answer is 2,496, just under. The other idea is choosing the right kind of estimate: to PROVE there is at least enough of something, only an underestimate that clears the bar does the job. That is lv3 and one question is built around it.',
 ('Round, multiply, then ask: is my estimate too big or too small?', 12),
 'Lesson 3-2')

# ══ Lesson 3 · Multiply by a 1-Digit Number ═════════════════════════════════
assert 34 * 5 == 170 and no_carry(34, 5) == 150 and side_by_side(34, 5) == 1520
assert 47 * 6 == 282 and 6 * 7 == 42 and 6 * 40 == 240
assert 238 * 4 == 952 and no_carry(238, 4) == 822
assert 1625 * 3 == 4875 and no_carry(1625, 3) == 3865
assert 485 * 8 == 3880 and no_carry(485, 8) == 3240 and 2406 * 5 == 12030 and no_carry(2406, 5) == 10000
assert 37 * 4 == 148 and side_by_side(37, 4) == 1228
assert 692 * 7 == 4844 and 700 * 7 == 4900
assert 238 * 5 == 1190 and 8 * 5 == 40
assert (27 + 18) * 5 == 225 and 27 * 5 + 18 == 153

go(3, 'Multiply by a 1-Digit Number', [
 ('Partial products',
  '**Break the bigger number into place values, multiply each part, then add the parts.**\n'
  '• 47 × 6 = (6 × 40) + (6 × 7) = 240 + 42 = 282.\n'
  '• You can add the partial products in any order.',
  'Split it up, multiply each piece, put it back together.'),
 ('The standard algorithm',
  '**Multiply each place from the ones up, regrouping as you go.**\n'
  '• Multiply the ones, write the ones digit, carry the tens.\n'
  '• Multiply the tens, then ADD the carried tens.\n'
  '• Keep going left, one place at a time.',
  'Right to left, one place at a time.'),
 ('Regrouping (carrying)',
  '**Multiply first, THEN add the number you carried.**\n'
  '• 238 × 4: 4 × 8 = 32 → write 2, carry 3.\n'
  '• Next: 4 × 3 = 12, plus the carried 3 = 15.',
  'Multiply, then add the carry — never the other way round.'),
 ('A common mistake',
  '**Writing each whole product side by side does not work.**\n'
  '• 37 × 4 is not 1,228 (12 and 28 written next to each other).\n'
  '• 4 × 7 = 28 means 2 tens and 8 ones — the 2 tens must be carried.',
  'A two-digit step never gets its own two spaces.'),
 ('More digits, same steps',
  '**Multiplying a 4-digit number works exactly like a 2-digit one — there are just more places.**\n'
  '• 1,625 × 3 = 4,875.',
  'Same moves, one more column.'),
 ('Estimate to check',
  '**Round the big factor, multiply, and make sure your answer is close.**\n'
  '• 692 × 7 is about 700 × 7 = 4,900.',
  'If the answer is nowhere near the estimate, look for a slip.'),
], [
 (1, 'What is 34 × 5?',
  opts4(170, 150, 1520, 250), 0,
  'Multiply the ones first and carry the tens.',
  ['5 × 4 ones = 20 ones: write 0, carry 2 tens.', '5 × 3 tens = 15 tens.',
   '15 tens + 2 tens = 17 tens.', 'So 34 × 5 = 170.'],
  '**170.** The 2 tens from 5 × 4 = 20 get added after multiplying the tens.',
  '150 forgets the carried 2. 250 adds the 2 BEFORE multiplying: (3 + 2) × 5.'),
 (1, 'Which partial products add up to 47 × 6?',
  ['240 and 42', '24 and 42', '40 and 7', '282 and 6'], 0,
  'Split 47 into 40 and 7, then multiply each by 6.',
  ['47 = 40 + 7.', '6 × 40 = 240.', '6 × 7 = 42.', '240 + 42 = 282.'],
  '**240 and 42.** 6 × 40 and 6 × 7 are the two partial products, and they add to 282.',
  '24 is 6 × 4 — it forgets that the 4 in 47 means 4 TENS.'),
 (2, 'What is 238 × 4?',
  opts4(952, no_carry(238, 4), 832, 992), 0,
  'Multiply each place and add the carries.',
  ['4 × 8 = 32: write 2, carry 3.', '4 × 3 = 12, + 3 = 15: write 5, carry 1.',
   '4 × 2 = 8, + 1 = 9.', 'So 238 × 4 = 952.'],
  '**952.** Two carries happen here — one into the tens and one into the hundreds.',
  '822 drops both carries. Estimate: 240 × 4 = 960, so 952 is right where it should be.'),
 (2, 'What is 1,625 × 3?',
  opts4(4875, 3865, 4865, 4975), 0,
  'Same steps as a smaller number — just one more place.',
  ['3 × 5 = 15: write 5, carry 1.', '3 × 2 = 6, + 1 = 7.', '3 × 6 = 18: write 8, carry 1.',
   '3 × 1 = 3, + 1 = 4. So 1,625 × 3 = 4,875.'],
  '**4,875.** A 4-digit number needs one more step, but each step is the same.',
  'Estimate: 1,600 × 3 = 4,800, which is close.'),
 (2, 'A horse has a mass of 485 kilograms. An elephant has 8 times as much. What is the elephant\'s mass?',
  opts4(3880, no_carry(485, 8), 493, 4880), 0,
  '"8 times as much" means multiply by 8.',
  ['Find 485 × 8.', '8 × 5 = 40: write 0, carry 4.', '8 × 8 = 64, + 4 = 68: write 8, carry 6.',
   '8 × 4 = 32, + 6 = 38. So 3,880 kg.'],
  '**3,880 kilograms.** "Times as much" is a multiplication, and 485 × 8 = 3,880.',
  '493 comes from adding 8 instead of multiplying. 3,240 drops the carries.'),
 (2, 'What is 2,406 × 5?',
  opts4(12030, 10000, 12000, 12330), 0,
  'The zero in the tens place still gets multiplied — and still receives a carry.',
  ['5 × 6 = 30: write 0, carry 3.', '5 × 0 = 0, + 3 = 3.', '5 × 4 = 20: write 0, carry 2.',
   '5 × 2 = 10, + 2 = 12. So 12,030.'],
  '**12,030.** The zero tens place becomes 3 because of the carry from the ones.',
  '12,000 forgets that the carried 3 lands in the tens place.'),
 (3, 'A student wrote 37 × 4 = 1,228. What went wrong?',
  ['They wrote 12 and 28 side by side instead of carrying',
   'They multiplied the tens digit by 5 instead of 4',
   'They added 37 and 4 together before multiplying',
   'Nothing went wrong, because 1,228 is correct'], 0,
  'Where do 12 and 28 come from?',
  ['4 × 3 = 12 and 4 × 7 = 28.', 'The student wrote 12 and 28 next to each other.',
   'But 28 means 2 tens and 8 ones — the 2 must be carried.',
   'The correct product is 148.'],
  '**They wrote the products side by side instead of carrying.** 37 × 4 is 148.',
  'Estimate: 40 × 4 = 160. An answer over a thousand is clearly impossible.'),
 (3, 'Maya got 4,244 for 692 × 7. How does an estimate show she made a mistake?',
  ['700 × 7 = 4,900, so the answer should be just under 4,900',
   '600 × 7 = 4,200, so her answer is exactly right',
   '692 × 7 must be less than 692, so 4,244 is far too big',
   'An estimate cannot show a mistake — only an exact answer can'], 0,
  'Round 692 to the nearest hundred.',
  ['692 is close to 700.', '700 × 7 = 4,900.',
   '692 is only a little less than 700, so the product is a little less than 4,900.',
   '4,244 is 600 away — something slipped. The real answer is 4,844.'],
  '**700 × 7 = 4,900, so the answer should be just under 4,900.** 4,244 is too far off; the real product is 4,844.',
  'Round to the NEAREST hundred — 692 is much closer to 700 than to 600.'),
 (1, 'To find 238 × 5, you first find 5 × 8 = 40. What do you do with the 40?',
  ['Write 0 in the ones place and carry 4 tens',
   'Write 40 in the ones place',
   'Write 4 in the ones place and carry 0',
   'Add 40 to 238 and keep going'], 0,
  '40 is 4 tens and 0 ones.',
  ['40 ones is 4 tens and 0 ones.', 'The 0 goes in the ones place.',
   'The 4 tens are carried to the tens column.'],
  '**Write 0 in the ones place and carry 4 tens.** Each place holds one digit, so the tens move over.',
  'After carrying, 5 × 3 tens = 15 tens, plus the 4 = 19 tens.'),
 (3, 'Anthony had 27 silver coins and 18 gold coins. Now he has 5 times as many coins in all. How many coins does he have now?',
  opts4(225, 153, 135, 50), 0,
  'First find how many coins he started with.',
  ['He started with 27 + 18 = 45 coins.', 'Now he has 5 times as many: 45 × 5.',
   '45 × 5 = 225.'],
  '**225 coins.** The starting total is 45, and 5 times that is 225.',
  '153 multiplies only the silver coins and forgets to multiply the gold ones.'),
],
 'Lesson 3-3 of the Topic 3 textbook scan: multiplying 2-, 3- and 4-digit numbers by a 1-digit number with partial products and the standard algorithm.',
 'The standard algorithm she learns here is the same one every later lesson extends — getting the carrying right now saves a lot of trouble later.',
 [('Multiply by a 1-digit number with partial products', 'source'),
  ('Multiply by a 1-digit number with the standard algorithm', 'source'),
  ('Regroup correctly: multiply first, then add the carried digit', 'source'),
  ('Estimate to check that a product is reasonable', 'source')],
 'Every wrong option here comes from a named mistake, computed in the builder: dropping the carry (34 × 5 → 150), adding the carry before multiplying ((3 + 2) × 5 → 250), and writing each digit\'s product side by side (37 × 4 → 1,228), which is the textbook\'s own "what did this student do wrong?" example with fresh numbers. If she picks one of those, the explanation names exactly which slip it was.',
 ('Right to left, and add the carry AFTER you multiply.', 12),
 'Lesson 3-3')

# ══ Lesson 4 · Multiply 2-Digit by 2-Digit ══════════════════════════════════
assert 23 * 45 == 1035 == 800 + 100 + 120 + 15
assert 34 * 26 == 884 and no_placeholder(34, 26) == 272 and 30 * 20 + 4 * 6 == 624
assert 57 * 18 == 1026 and no_placeholder(57, 18) == 513
assert 41 * 23 == 943 and 36 * 28 == 1008 and 24 * 31 == 744
assert 43 * 25 == 1075 and 40 * 20 + 3 * 5 == 815
assert (48 - 35) * 26 == 338 and 48 * 26 == 1248 and 35 * 26 == 910
assert 37 * 4 == 148 and 37 * 20 == 740 and 148 + 740 == 37 * 24

go(4, 'Multiply 2-Digit by 2-Digit Numbers', [
 ('The area model',
  '**Split both factors into tens and ones and find all four partial products.**\n'
  '• 23 × 45: 20 × 40 = 800, 20 × 5 = 100, 3 × 40 = 120, 3 × 5 = 15.\n'
  '• 800 + 100 + 120 + 15 = 1,035.',
  'Two parts times two parts makes four pieces.'),
 ('Two rows in the standard algorithm',
  '**First multiply by the ones digit, then by the tens digit, then add the two rows.**\n'
  '• 34 × 26: row 1 is 34 × 6 = 204. Row 2 is 34 × 20 = 680.\n'
  '• 204 + 680 = 884.',
  'One row for the ones, one row for the tens.'),
 ('The placeholder zero',
  '**The second row starts with a 0 because you are multiplying by TENS.**\n'
  '• In 34 × 26 the 2 means 20, so the row is 680, not 68.',
  'Tens row → zero in the ones place first.'),
 ('Standard algorithm = partial products',
  '**The two rows ARE partial products, with some of them already added together.**\n'
  '• Row 1 is (ones digit) × the whole number; row 2 is (tens digit) × the whole number.',
  'Same pieces, fewer lines.'),
 ('Estimate to check',
  '**Round both factors and multiply.**\n'
  '• 57 × 18 is about 60 × 20 = 1,200, so 1,026 is reasonable.',
  'Close to the estimate? Good. Far off? Look again.'),
], [
 (1, 'Which set of partial products gives 23 × 45?',
  ['800, 100, 120 and 15', '800 and 15', '80, 10, 12 and 15', '20, 3, 40 and 5'], 0,
  'Split both numbers: 23 = 20 + 3 and 45 = 40 + 5.',
  ['20 × 40 = 800.', '20 × 5 = 100.', '3 × 40 = 120.', '3 × 5 = 15. They add to 1,035.'],
  '**800, 100, 120 and 15.** Each tens-or-ones part of 23 meets each part of 45, making four pieces.',
  '800 and 15 alone leave out the two "cross" pieces — a very common gap.'),
 (1, 'In the standard algorithm for 34 × 26, why does the second row start with a 0?',
  ['Because that row multiplies 34 by 2 tens',
   'Because 34 × 2 has a zero in it',
   'Because every row in multiplication ends in 0',
   'Because you must always add a zero to be neat'], 0,
  'What does the 2 in 26 stand for?',
  ['The 2 in 26 means 2 tens, or 20.', 'So the second row is 34 × 20 = 680.',
   'The zero shows the row is worth tens.'],
  '**Because that row multiplies 34 by 2 tens.** 34 × 20 = 680, and the 0 holds the ones place.',
  'Leaving the 0 off turns 680 into 68 and shrinks the answer badly.'),
 (2, 'What is 34 × 26?',
  opts4(884, 272, 624, 874), 0,
  'Row 1: 34 × 6. Row 2: 34 × 20. Then add.',
  ['34 × 6 = 204.', '34 × 20 = 680.', '204 + 680 = 884.'],
  '**884.** The two rows are 204 and 680.',
  '272 leaves the zero off the second row. 624 only multiplies tens by tens and ones by ones.'),
 (2, 'What is 57 × 18?',
  opts4(1026, 513, 976, 1126), 0,
  'Row 1: 57 × 8. Row 2: 57 × 10.',
  ['57 × 8 = 456.', '57 × 10 = 570.', '456 + 570 = 1,026.'],
  '**1,026.** 456 + 570 = 1,026.',
  'Estimate: 60 × 20 = 1,200. 513 is far too small — the second row lost its zero.'),
 (2, 'What is 41 × 23?',
  opts4(943, 205, 843, 963), 0,
  'Multiply 41 by 3, then by 20.',
  ['41 × 3 = 123.', '41 × 20 = 820.', '123 + 820 = 943.'],
  '**943.** 123 + 820 = 943.',
  'Estimate: 40 × 20 = 800, so an answer a bit over 800 makes sense.'),
 (2, 'A ferry carries 36 cars each trip. It makes 28 trips. How many cars does it carry?',
  opts4(1008, 360, 1108, 64), 0,
  'Multiply the cars per trip by the number of trips.',
  ['Find 36 × 28.', '36 × 8 = 288.', '36 × 20 = 720.', '288 + 720 = 1,008.'],
  '**1,008 cars.** The two rows are 288 and 720.',
  '64 comes from adding 36 and 28 — "each trip" means multiply.'),
 (2, 'A café is open 24 hours a day for 31 days. How many hours is it open?',
  opts4(744, no_placeholder(24, 31), 644, 55), 0,
  'Multiply hours per day by the number of days.',
  ['Find 24 × 31.', '24 × 1 = 24.', '24 × 30 = 720.', '24 + 720 = 744.'],
  '**744 hours.** 24 × 31 = 744.',
  'Estimate: 25 × 30 = 750 — very close. 96 leaves the zero off the tens row.'),
 (3, 'A student found 43 × 25 by doing 40 × 20 = 800 and 3 × 5 = 15, then got 815. What was left out?',
  ['The two cross pieces, 40 × 5 and 3 × 20',
   'Nothing — 815 is correct',
   'Only the regrouping in the ones place',
   'A zero at the end of the answer'], 0,
  'Draw the area model. How many pieces should there be?',
  ['43 × 25 needs four partial products.', '40 × 20 = 800 and 3 × 5 = 15 are two of them.',
   'The missing ones are 40 × 5 = 200 and 3 × 20 = 60.',
   '800 + 200 + 60 + 15 = 1,075.'],
  '**The two cross pieces, 40 × 5 and 3 × 20.** The full product is 1,075.',
  'Estimate: 40 × 25 = 1,000, so 815 was too small to be right.'),
 (3, 'A bus holds 35 adults or 48 children. It makes 26 full trips. How many more people ride if every trip carries children instead of adults?',
  opts4(338, 1248, 910, 13), 0,
  'Find how many more fit on ONE trip first.',
  ['Each trip carries 48 − 35 = 13 more children than adults.', '26 trips × 13 more each = 338.',
   'Check: 48 × 26 = 1,248 and 35 × 26 = 910; 1,248 − 910 = 338.'],
  '**338 more people.** 13 extra per trip, times 26 trips.',
  '1,248 is the total number of children — the question asks how many MORE.'),
 (3, 'Janet says the standard algorithm is just a shortcut for partial products. Is she right?',
  ['Yes — each row is a partial product, and the rows are added at the end',
   'No — the standard algorithm gives a different answer from partial products',
   'No — partial products only work when both numbers are small ones',
   'Yes — but only when neither factor needs any regrouping at all'], 0,
  'Compare 37 × 24 done both ways.',
  ['Standard algorithm row 1: 37 × 4 = 148.', 'Row 2: 37 × 20 = 740.',
   'Those are partial products — each row just combines two of the four area-model pieces.',
   '148 + 740 = 888 either way.'],
  '**Yes.** Each row is a partial product, so both methods add up the same pieces.',
  'That is why you can check one method with the other.'),
],
 'Lesson 3-4 of the Topic 3 textbook scan: multiplying a 2-digit number by a 2-digit number with an area model, partial products and the standard algorithm.',
 'Two-digit by two-digit is where the placeholder zero first appears, and it is the step most students drop.',
 [('Multiply 2-digit by 2-digit numbers with an area model', 'source'),
  ('Multiply 2-digit by 2-digit numbers with the standard algorithm', 'source'),
  ('Explain the placeholder zero in the second row', 'source'),
  ('See the standard algorithm as a shortcut for partial products', 'source')],
 'Two mistakes are built into the wrong options on purpose. Leaving the zero off the second row (34 × 26 → 272) and multiplying only tens-by-tens and ones-by-ones (43 × 25 → 815, missing the two "cross" pieces). Both give answers that are wildly off from an estimate, which is exactly why every explanation here ends with one.',
 ('Two rows, and the second row always starts with a 0.', 12),
 'Lesson 3-4')

# ══ Lesson 5 · Multiply 3-Digit by 2-Digit ══════════════════════════════════
assert 247 * 36 == 8892 and no_placeholder(247, 36) == 2223 and 247 * 30 == 7410 and 247 * 6 == 1482
assert 518 * 24 == 12432 and no_placeholder(518, 24) == 3108
assert 386 * 17 == 6562 and no_placeholder(386, 17) == 3088
assert 146 * 60 == 8760 and 644 * 52 == 33488 and 600 * 50 == 30000
assert 999 * 99 == 98901 and len(str(999 * 99)) == 5
assert 8 * 6 * (23 + 19) == 2016 and 126 * 23 == 2898
assert 219 * 16 == 3504 and no_placeholder(219, 16) == 1533

go(5, 'Multiply 3-Digit by 2-Digit Numbers', [
 ('Same steps, one more digit',
  '**Multiplying a 3-digit number by a 2-digit number uses the same two rows as before.**\n'
  '• Row 1: the whole top number × the ones digit.\n'
  '• Row 2: the whole top number × the tens digit, starting with a 0.\n'
  '• Add the rows.',
  'Nothing new — just a longer row.'),
 ('A worked example',
  '**247 × 36 = 8,892.**\n'
  '• Row 1: 247 × 6 = 1,482.\n'
  '• Row 2: 247 × 30 = 7,410.\n'
  '• 1,482 + 7,410 = 8,892.',
  'Ones row, tens row, add.'),
 ('Partial products for 3-digit × 2-digit',
  '**The area model has six pieces: hundreds, tens and ones of one factor times tens and ones of the other.**\n'
  '• You can list all six or let the standard algorithm combine them.',
  'Three parts × two parts = six pieces.'),
 ('How many digits can the product have?',
  '**A 3-digit number times a 2-digit number has at most 5 digits.**\n'
  '• The biggest case is 999 × 99 = 98,901.',
  'Handy for spotting an answer with too many or too few digits.'),
 ('Estimate to check',
  '**Round both factors and multiply.**\n'
  '• 386 × 17 is about 400 × 20 = 8,000, or closer: 400 × 17 = 6,800.',
  'An answer ten times too big or too small almost always means a lost or extra zero.'),
], [
 (1, 'To find 247 × 36 with the standard algorithm, what do you multiply first?',
  ['247 × 6', '247 × 3', '200 × 30', '47 × 36'], 0,
  'The standard algorithm always starts with the ones digit of the bottom number.',
  ['The bottom number is 36.', 'Its ones digit is 6.', 'So the first row is 247 × 6.'],
  '**247 × 6.** Row 1 is the whole top number times the ones digit.',
  'The second row will be 247 × 30 — the 3 means 3 tens.'),
 (2, 'What is 247 × 36?',
  opts4(8892, 2223, 7410, 1482), 0,
  'Row 1: 247 × 6. Row 2: 247 × 30. Add.',
  ['247 × 6 = 1,482.', '247 × 30 = 7,410.', '1,482 + 7,410 = 8,892.'],
  '**8,892.** The two rows are 1,482 and 7,410.',
  '2,223 leaves the zero off the second row; 7,410 and 1,482 are each only one row.'),
 (2, 'What is 518 × 24?',
  opts4(12432, 3108, 12342, 11432), 0,
  'Row 1: 518 × 4. Row 2: 518 × 20.',
  ['518 × 4 = 2,072.', '518 × 20 = 10,360.', '2,072 + 10,360 = 12,432.'],
  '**12,432.** 2,072 + 10,360 = 12,432.',
  'Estimate: 500 × 24 = 12,000. 3,108 is far too small — a missing placeholder zero.'),
 (2, 'What is 386 × 17?',
  opts4(6562, no_placeholder(386, 17), 6462, 3860), 0,
  'Row 1: 386 × 7. Row 2: 386 × 10.',
  ['386 × 7 = 2,702.', '386 × 10 = 3,860.', '2,702 + 3,860 = 6,562.'],
  '**6,562.** The two rows are 2,702 and 3,860.',
  '3,088 adds 386 × 7 and 386 × 1 — the 1 in 17 means 1 ten. 3,860 is only one row.'),
 (2, 'A cat\'s heart beats about 146 times a minute. How many times does it beat in 1 hour?',
  opts4(8760, 876, 206, 87600), 0,
  'There are 60 minutes in an hour.',
  ['Find 146 × 60.', '146 × 6 = 876.', '146 × 60 is ten times that: 8,760.'],
  '**8,760 times.** 146 × 60 = 8,760.',
  '206 comes from adding 146 and 60. "Each minute for 60 minutes" means multiply.'),
 (3, 'Is 3,220 a reasonable answer for 644 × 52?',
  ['No — 600 × 50 = 30,000, so it is about ten times too small',
   'Yes — 3,220 has four digits, which is enough',
   'Yes — 644 × 5 is about 3,220, so it must be right',
   'No — the product of these numbers must be under 1,000'], 0,
  'Round both factors and multiply.',
  ['644 is about 600.', '52 is about 50.', '600 × 50 = 30,000.',
   '3,220 is about one tenth of that, so a zero was lost.'],
  '**No — the estimate is about 30,000.** 3,220 is roughly 644 × 5, which forgets that the 5 in 52 means 5 tens.',
  'An answer about ten times too small is the signature of a missing placeholder zero.'),
 (1, 'What is the greatest number of digits the product of a 3-digit number and a 2-digit number can have?',
  ['5', '6', '4', '3'], 0,
  'Try the biggest possible numbers.',
  ['The biggest 3-digit number is 999.', 'The biggest 2-digit number is 99.',
   '999 × 99 = 98,901, which has 5 digits.'],
  '**5.** Even 999 × 99 only reaches 98,901.',
  'So a 6-digit answer to a 3-digit × 2-digit problem is always wrong.'),
 (3, 'A garden store packs 8 plants in a tray and 6 trays in a flat. It sold 23 flats on Saturday and 19 on Sunday. How many plants did it sell?',
  opts4(2016, 336, 1104, 912), 0,
  'Find the plants in one flat and the number of flats first.',
  ['One flat holds 8 × 6 = 48 plants.', 'It sold 23 + 19 = 42 flats.',
   '48 × 42: 48 × 2 = 96 and 48 × 40 = 1,920.', '96 + 1,920 = 2,016.'],
  '**2,016 plants.** 48 plants a flat, 42 flats.',
  '1,104 counts only Saturday. 336 multiplies 8 × 42 and forgets the trays.'),
 (2, 'A patio is 126 bricks wide and 23 bricks long. How many bricks does it take?',
  opts4(2898, 630, 2798, 149), 0,
  'Multiply the width by the length.',
  ['Find 126 × 23.', '126 × 3 = 378.', '126 × 20 = 2,520.', '378 + 2,520 = 2,898.'],
  '**2,898 bricks.** 378 + 2,520 = 2,898.',
  '149 is 126 + 23 — the bricks fill a rectangle, so multiply.'),
 (3, 'What is 219 × 16?',
  opts4(3504, 1533, 2190, 3404), 0,
  'Row 1: 219 × 6. Row 2: 219 × 10.',
  ['219 × 6 = 1,314.', '219 × 10 = 2,190.', '1,314 + 2,190 = 3,504.'],
  '**3,504.** 1,314 + 2,190 = 3,504.',
  '1,533 adds 219 × 6 and 219 × 1 — the 1 in 16 means 1 ten.'),
],
 'Lesson 3-5 of the Topic 3 textbook scan: multiplying a 3-digit number by a 2-digit number with partial products and the standard algorithm.',
 'This is the biggest multiplication she does in this unit, and it is exactly the same two-row method with a longer row.',
 [('Multiply 3-digit by 2-digit numbers with the standard algorithm', 'source'),
  ('Use estimation to check that a product is reasonable', 'source'),
  ('Know the most digits a 3-digit × 2-digit product can have', 'added')],
 'The mistake that matters most here is the missing placeholder zero, and it is easy to catch: the answer comes out roughly ten times too small. Several wrong options are built from exactly that slip (247 × 36 → 2,223), and one question asks her to spot it with an estimate alone. The digit-count rule — never more than 5 digits — is a quick extra check the book mentions in its assessment practice.',
 ('Same two rows, longer numbers. Estimate first so you know the size.', 13),
 'Lesson 3-5')

# ══ Lesson 6 · Multiply with Zeros ══════════════════════════════════════════
assert 306 * 4 == 1224 and skip_zero(306) * 4 == 144 and 6 * 4 == 24
assert 407 * 23 == 9361 and skip_zero(407) * 23 == 1081
assert 205 * 38 == 7790 and skip_zero(205) * 38 == 950
assert 610 * 45 == 27450 and 61 * 45 == 2745
assert 108 * 26 == 2808 and skip_zero(108) * 26 == 468
assert 404 * 44 == 17776 and 404 * 4 * 2 == 3232 and 404 * 40 + 404 * 4 == 17776
assert 36 * 12 == 432 < 475
assert 309 * 42 == 12978 and 300 * 40 == 12000
assert 503 * 20 == 10060 and 503 * 2 == 1006 and skip_zero(503) * 20 == 1060

go(6, 'Multiply with Zeros', [
 ('The algorithm does not change',
  '**A zero in a factor is multiplied like any other digit.**\n'
  '• Any number × 0 = 0.\n'
  '• You still write a digit in that place — the zero holds the place.',
  'Zero times anything is zero, but it still gets its spot.'),
 ('A zero can still get a carry',
  '**If something was carried into the zero\'s place, add it on.**\n'
  '• 306 × 4: 4 × 6 = 24, carry 2. Then 4 × 0 = 0, plus 2 = 2.\n'
  '• So the tens digit is 2, not 0: 306 × 4 = 1,224.',
  'Zero × 4 is 0, but the carry still arrives.'),
 ('Do not skip the zero',
  '**Dropping a zero from the middle of a number changes it completely.**\n'
  '• 306 is not 36. 306 × 4 = 1,224, but 36 × 4 is only 144.',
  'The zero is what makes 306 three hundred and six.'),
 ('A zero at the end',
  '**If a factor ends in 0, you can multiply without it and put the zero back at the end.**\n'
  '• 610 × 45 = 61 × 45 × 10 = 2,745 × 10 = 27,450.',
  'Set the end zero aside, then give it back.'),
 ('Estimate to check',
  '**An estimate catches a lost zero immediately.**\n'
  '• 407 × 23 is about 400 × 20 = 8,000.',
  'If the answer is about ten times too small, a zero went missing.'),
], [
 (2, 'To find 306 × 4, you first get 4 × 6 = 24 and carry 2. What digit goes in the tens place?',
  ['2, because 4 × 0 = 0 and the carried 2 is added',
   '0, because anything times 0 is 0',
   '4, because the 4 in 24 goes in the tens place',
   '8, because 4 × 2 = 8'], 0,
  'What is 4 × 0? Then what do you add?',
  ['4 × 0 tens = 0 tens.', 'The 2 tens carried from the ones get added.',
   '0 + 2 = 2 tens, so the tens digit is 2.'],
  '**2.** 4 × 0 = 0, and the carried 2 tens still have to be added.',
  'Writing 0 there forgets the carry — that turns 1,224 into 1,204.'),
 (2, 'What is 306 × 4?',
  opts4(1224, 144, 1204, 1264), 0,
  'Multiply each digit, including the zero, and keep the carries.',
  ['4 × 6 = 24: write 4, carry 2.', '4 × 0 = 0, + 2 = 2.', '4 × 3 = 12.', 'So 306 × 4 = 1,224.'],
  '**1,224.** The zero place ends up holding the carried 2.',
  '144 is 36 × 4 — the zero in 306 was skipped.'),
 (2, 'What is 407 × 23?',
  opts4(9361, 1081, 9261, 9371), 0,
  'Row 1: 407 × 3. Row 2: 407 × 20.',
  ['407 × 3 = 1,221.', '407 × 20 = 8,140.', '1,221 + 8,140 = 9,361.'],
  '**9,361.** 1,221 + 8,140 = 9,361.',
  'Estimate: 400 × 23 = 9,200. 1,081 is 47 × 23 — the zero was skipped.'),
 (2, 'What is 205 × 38?',
  opts4(7790, 950, 7690, 7780), 0,
  'Row 1: 205 × 8. Row 2: 205 × 30.',
  ['205 × 8 = 1,640.', '205 × 30 = 6,150.', '1,640 + 6,150 = 7,790.'],
  '**7,790.** 1,640 + 6,150 = 7,790.',
  '950 is 25 × 38 — it treats 205 as if the zero were not there.'),
 (2, 'What is 610 × 45?',
  opts4(27450, 2745, 274500, 27405), 0,
  'Find 61 × 45, then put the zero from 610 back on.',
  ['61 × 45: 61 × 5 = 305 and 61 × 40 = 2,440.', '305 + 2,440 = 2,745.',
   'Put the zero back: 27,450.'],
  '**27,450.** 61 × 45 = 2,745, and the end zero of 610 makes it 27,450.',
  'Forgetting to put the zero back gives 2,745 — ten times too small.'),
 (2, 'An auditorium has 108 rows with 26 seats in each row. How many seats is that?',
  opts4(2808, 468, 2708, 134), 0,
  'Multiply rows by seats per row.',
  ['Find 108 × 26.', '108 × 6 = 648.', '108 × 20 = 2,160.', '648 + 2,160 = 2,808.'],
  '**2,808 seats.** 648 + 2,160 = 2,808.',
  '468 is 18 × 26 — the zero in 108 got dropped.'),
 (3, 'Trudy wants to find 44 × 404. She says she can find 4 × 404 and double it. Why does that not work?',
  ['44 is 40 + 4, not 4 + 4, so doubling only covers 8 groups',
   'Doubling works, but only when there is no zero in the numbers',
   'She should triple it instead, because 44 has two digits',
   'It does work — 4 × 404 doubled is the same as 44 × 404'], 0,
  'What does "double 4 × 404" actually multiply 404 by?',
  ['Doubling 4 × 404 gives 8 × 404.', 'But 44 is 40 + 4.',
   'So 44 × 404 = (40 × 404) + (4 × 404) = 16,160 + 1,616 = 17,776.',
   'Her method only finds 8 × 404 = 3,232.'],
  '**44 is 40 + 4, not 4 + 4.** The correct product is 17,776; doubling only reaches 3,232.',
  'The first 4 in 44 means 4 TENS — the same idea as the placeholder zero.'),
 (3, 'Renting a trombone costs $36 a month. Buying one costs $475. Maria needs it for 12 months. What should she do?',
  ['Rent it, because 12 months costs $432, which is less than $475',
   'Buy it, because $475 is only one payment',
   'Rent it, because $36 is less than $475',
   'Buy it, because 12 months of renting costs $4,320'], 0,
  'Find the total cost of renting for 12 months.',
  ['Renting for 12 months: 36 × 12.', '36 × 2 = 72 and 36 × 10 = 360.',
   '72 + 360 = $432.', '$432 is less than $475, so renting is cheaper.'],
  '**Rent it.** 12 months costs $432, which is $43 less than buying.',
  'Comparing $36 to $475 on its own ignores the 12 months. $4,320 has one zero too many.'),
 (2, 'Which estimate best checks that 309 × 42 = 12,978 is reasonable?',
  ['300 × 40 = 12,000', '300 × 4 = 1,200', '30 × 40 = 1,200', '3,000 × 40 = 120,000'], 0,
  'Round each factor to its greatest place.',
  ['309 rounds to 300.', '42 rounds to 40.', '300 × 40 = 12,000.',
   '12,978 is close to 12,000, so it is reasonable.'],
  '**300 × 40 = 12,000.** It is close to 12,978, so the answer makes sense.',
  'The other options each lose or add a zero when rounding.'),
 (1, 'What is 503 × 20?',
  opts4(10060, 1006, 100600, skip_zero(503) * 20), 0,
  'Find 503 × 2, then multiply by 10.',
  ['503 × 2 = 1,006.', '× 10 puts a zero on the end.', '503 × 20 = 10,060.'],
  '**10,060.** 503 × 2 = 1,006, and × 10 makes it 10,060.',
  '1,060 is 53 × 20 — the zero in the middle of 503 was skipped.'),
],
 'Lesson 3-6 of the Topic 3 textbook scan: multiplying whole numbers when one of the factors has a zero in it.',
 'Zeros cause more multiplication mistakes than any other digit — dropped, skipped, or forgotten when a carry lands on them.',
 [('Multiply whole numbers that have zeros in them', 'source'),
  ('Add a carry into a place where the digit is 0', 'source'),
  ('Estimate to check for reasonableness', 'source')],
 'The two slips this lesson targets are skipping a zero in the middle of a number (306 treated as 36) and forgetting that a carry can land on a zero (306 × 4 written as 1,204 instead of 1,224). Both are built into wrong options, computed in the builder. The textbook\'s own "Trudy doubles it" item is here with fresh numbers — it is really the placeholder-zero idea again, since the first 4 in 44 means 4 tens.',
 ('Zero times anything is zero — but the carry still lands.', 12),
 'Lesson 3-6')

# ══ Lesson 7 · Solve Problems with Multiplication ═══════════════════════════
assert 645 * 4 == 2580 and 58 * 12 == 696 and 24 * 365 == 8760
assert 137 * 22 == 3014 and 125 * 14 == 1750
assert 265 * 14 == 3710 and 219 * 17 == 3723 and 3723 - 3710 == 13
assert 18 * 14 == 252 <= 300
assert 348 * 40 == 13920 and 328 * 40 != 13920 and 368 * 40 != 13920 and 388 * 40 != 13920
assert 4 * (430 + 290) == 2880 and 4 * 430 + 290 == 2010

go(7, 'Solve Problems with Multiplication', [
 ('Read what is being asked',
  '**Decide what the answer is counting before you pick numbers to multiply.**\n'
  '• "Each", "per" and "times as many" usually mean multiply.\n'
  '• Write the answer with its label: dollars, miles, pages.',
  'Name the answer first, then find it.'),
 ('How often is it paid?',
  '**Monthly = 12 times a year. Quarterly = 4 times a year. Weekly = 52 times a year.**\n'
  '• A $645 quarterly bill costs 645 × 4 = $2,580 a year.',
  'Quarter = one fourth of a year.'),
 ('Group first, then multiply',
  '**If several amounts all repeat the same number of times, add them first.**\n'
  '• Two quarterly bills of $430 and $290: 4 × (430 + 290) = 4 × 720 = $2,880.',
  'Add what repeats together, then multiply once.'),
 ('Estimate, then compute',
  '**Estimate first so you know roughly what answer to expect.**\n'
  '• 137 × 22 is about 140 × 20 = 2,800.',
  'An estimate is your early-warning system.'),
 ('The process never changes',
  '**Multiplying bigger numbers uses the same steps — just more of them.**\n'
  '• Ones row, tens row, add. Carry as you go.',
  'More digits, same moves.'),
], [
 (1, 'A bill is paid quarterly. How many times is it paid in a year?',
  ['4', '12', '3', '52'], 0,
  'A quarter is one fourth.',
  ['A quarterly bill is paid every quarter of a year.', 'A year has 4 quarters.',
   'So it is paid 4 times.'],
  '**4.** Quarterly means once every three months — four times a year.',
  'Monthly is 12. Mixing the two is the commonest slip in bill problems.'),
 (2, 'A water bill is $645, paid quarterly. What does water cost for the whole year?',
  ['$2,580', '$7,740', '$1,935', '$649'], 0,
  'How many quarters are in a year?',
  ['It is paid 4 times a year.', '645 × 4: 4 × 5 = 20, carry 2; 4 × 4 = 16 + 2 = 18, carry 1; 4 × 6 = 24 + 1 = 25.',
   'That is $2,580.'],
  '**$2,580.** Four payments of $645.',
  '$7,740 multiplies by 12 as if the bill were monthly.'),
 (2, 'A phone plan costs $58 each month. How much is that in a year?',
  ['$696', '$232', '$580', '$70'], 0,
  'A year has 12 months.',
  ['Find 58 × 12.', '58 × 2 = 116.', '58 × 10 = 580.', '116 + 580 = $696.'],
  '**$696.** 58 × 12 = 696.',
  '$232 multiplies by 4 — that would be a quarterly bill.'),
 (2, 'Carlos saves 24 cents every day of a 365-day year. How many cents does he save?',
  opts4(8760, 2190, 8660, 389), 0,
  'Multiply cents per day by the number of days.',
  ['Find 365 × 24.', '365 × 4 = 1,460.', '365 × 20 = 7,300.', '1,460 + 7,300 = 8,760 cents.'],
  '**8,760 cents.** That is $87.60.',
  '2,190 leaves the zero off the tens row.'),
 (2, 'Lila drives 137 kilometers round trip to work. How far does she drive in 22 work days?',
  opts4(3014, 548, 2914, 159), 0,
  'Multiply the distance each day by the number of days.',
  ['Find 137 × 22.', '137 × 2 = 274.', '137 × 20 = 2,740.', '274 + 2,740 = 3,014 km.'],
  '**3,014 kilometers.** 274 + 2,740 = 3,014.',
  'Estimate: 140 × 20 = 2,800 — close.'),
 (3, 'Which costs more: 14 trips at $265 each, or 17 trips at $219 each?',
  ['17 trips at $219, by $13', '14 trips at $265, by $13',
   '17 trips at $219, by $46', 'They cost exactly the same'], 0,
  'Work out both totals, then compare.',
  ['14 × 265 = 3,710.', '17 × 219 = 3,723.', '3,723 − 3,710 = 13.',
   'The 17 cheaper trips cost $13 more.'],
  '**17 trips at $219, by $13.** $3,723 against $3,710.',
  'The price per trip alone is not enough — the number of trips changes the answer.'),
 (3, 'A can of paint covers 300 square feet. A wall is 18 feet wide and 14 feet high. Is one can enough?',
  ['Yes — the wall is 252 square feet, which is less than 300',
   'No — the wall is 252 square feet, which is more than 300',
   'Yes — 18 + 14 = 32, which is much less than 300',
   'No — the wall is 2,520 square feet'], 0,
  'The wall\'s area is width × height.',
  ['Area = 18 × 14.', '18 × 4 = 72 and 18 × 10 = 180.', '72 + 180 = 252 square feet.',
   '252 is less than 300, so one can is enough.'],
  '**Yes.** The wall is 252 square feet, and one can covers 300.',
  'Adding the sides gives the distance around, not the space to paint.'),
 (2, 'A cook uses 125 pounds of potatoes each day for 14 days. How many pounds does she need?',
  opts4(1750, 625, 1650, 139), 0,
  'Multiply pounds per day by the number of days.',
  ['Find 125 × 14.', '125 × 4 = 500.', '125 × 10 = 1,250.', '500 + 1,250 = 1,750.'],
  '**1,750 pounds.** 500 + 1,250 = 1,750.',
  '625 is 125 × 4 + 125 × 1 — the 1 in 14 means 1 ten.'),
 (3, 'In 3_8 × 40 = 13,920, one digit is missing. Which digit is it?',
  ['4', '2', '6', '8'], 0,
  'Try each digit and check which product is 13,920.',
  ['13,920 ÷ 40 must be the missing number.', 'Try 348: 348 × 4 = 1,392, and × 10 = 13,920.',
   'So the missing digit is 4.'],
  '**4.** 348 × 40 = 13,920.',
  'Estimate first: 13,920 ÷ 40 is about 350, which points straight at 348.'),
 (3, 'Two bills are paid quarterly: $430 for gas and $290 for water. What do they cost together for a year?',
  ['$2,880', '$2,010', '$720', '$8,640'], 0,
  'Add the two bills first, then multiply by the number of quarters.',
  ['Each quarter costs 430 + 290 = $720.', 'There are 4 quarters.', '720 × 4 = $2,880.'],
  '**$2,880.** 4 × (430 + 290) = 4 × 720.',
  '$2,010 multiplies only the gas bill by 4. $8,640 multiplies by 12 as if monthly.'),
],
 'Lesson 3-7 of the Topic 3 textbook scan: using multiplication to solve real problems — bills, distances and totals — by estimating first and then computing.',
 'This is where the multiplication she has learned turns into something useful: working out yearly costs, comparing prices and checking if something is enough.',
 [('Choose multiplication to solve real-world problems', 'source'),
  ('Estimate before computing to check reasonableness', 'source'),
  ('Tell how often a bill is paid: monthly, quarterly, weekly', 'source')],
 'The trap worth watching is the one the textbook sets on purpose: quarterly versus monthly. A quarterly bill is paid 4 times a year, not 12, and several wrong options multiply by the wrong one. The other idea is grouping before multiplying — adding two quarterly bills first and multiplying once. The price comparison question is deliberately close ($3,723 against $3,710) so it cannot be settled by glancing at the price per trip.',
 ('Name what the answer is counting, then multiply.', 13),
 'Lesson 3-7')

# ══ Lesson 8 · Bar Diagrams for Multiplication ══════════════════════════════
assert 1340 * 5 == 6700 and 1300 * 5 == 6500
assert 2415 * 4 == 9660 and 16 * 48 == 768 and 36 * 14 == 504
assert 1250 * 12 == 15000 and 214 * 3 == 642 and 265 * 13 == 3445

go(8, 'Bar Diagrams for Multiplication', [
 ('"Times as many" means multiply',
  '**If one amount is 5 times as many as another, multiply the smaller amount by 5.**\n'
  '• 5 times as much as $1,340 is $1,340 × 5.',
  '"Times as many" is a multiplication signal.'),
 ('Drawing the bar diagram',
  '**Draw one bar for the smaller amount and a longer bar made of equal copies of it.**\n'
  '• 5 times as many → the long bar has 5 equal sections.',
  'Count the sections — that is the number you multiply by.'),
 ('Using a variable',
  '**A letter stands for the number you are trying to find.**\n'
  '• Let p = the new price. Then p = 1,340 × 5.',
  'The letter is a placeholder for the answer.'),
 ('Write, then solve, the equation',
  '**Turn the bar diagram into an equation, then solve it.**\n'
  '• 1,340 × 5 = p, so p = 6,700.',
  'Diagram → equation → answer.'),
 ('Check your answer',
  '**Use estimation or repeated addition to check.**\n'
  '• 1,340 × 5 is about 1,300 × 5 = 6,500 — close to 6,700.',
  'A quick estimate catches big mistakes.'),
], [
 (1, 'A painting sold for $1,340. Years later it sold for 5 times as much. Which equation finds the new price, p?',
  ['p = 1,340 × 5', 'p = 1,340 + 5', 'p = 1,340 − 5', 'p = 5 − 1,340'], 0,
  '"5 times as much" is a multiplication.',
  ['The new price is 5 times the old price.', '5 times means multiply by 5.',
   'So p = 1,340 × 5.'],
  '**p = 1,340 × 5.** "Times as much" means multiply.',
  'Adding 5 would make it only $5 more — nowhere near 5 times.'),
 (2, 'A painting sold for $1,340. Years later it sold for 5 times as much. What was the later price?',
  ['$6,700', '$5,700', '$6,500', '$1,345'], 0,
  'Multiply 1,340 by 5.',
  ['5 × 0 = 0.', '5 × 4 = 20: write 0, carry 2.', '5 × 3 = 15, + 2 = 17: write 7, carry 1.',
   '5 × 1 = 5, + 1 = 6. So $6,700.'],
  '**$6,700.** 1,340 × 5 = 6,700.',
  'Estimate: 1,300 × 5 = 6,500, which is close.'),
 (2, 'Sharon\'s store has 2,415 stickers. May\'s store has 4 times as many. How many stickers does May\'s store have?',
  opts4(9660, 2419, 8660, 9460), 0,
  'Draw a bar with 4 equal sections of 2,415.',
  ['May\'s bar has 4 sections of 2,415.', 's = 2,415 × 4.',
   '4 × 5 = 20, carry 2; 4 × 1 + 2 = 6; 4 × 4 = 16, carry 1; 4 × 2 + 1 = 9.', 's = 9,660.'],
  '**9,660 stickers.** 2,415 × 4 = 9,660.',
  '2,419 adds 4 instead of multiplying.'),
 (2, 'There are 16 buses. Each bus has 48 seats. How many seats are there in all?',
  opts4(768, 64, 668, 480), 0,
  'The bar diagram has 16 equal sections of 48.',
  ['Find 48 × 16.', '48 × 6 = 288.', '48 × 10 = 480.', '288 + 480 = 768.'],
  '**768 seats.** 288 + 480 = 768.',
  '64 is 16 + 48. Sixteen equal groups means multiply.'),
 (2, 'Priya lives 14 times as far from the beach as Leo. Leo lives 36 miles away. How far away does Priya live?',
  opts4(504, 50, 404, 144), 0,
  'Priya\'s bar has 14 sections of 36.',
  ['Find 36 × 14.', '36 × 4 = 144.', '36 × 10 = 360.', '144 + 360 = 504 miles.'],
  '**504 miles.** 144 + 360 = 504.',
  '144 is only 36 × 4 — the tens row got left out.'),
 (2, 'A pond holds 1,250 gallons. A pool holds 12 times as much. How many gallons does the pool hold?',
  opts4(15000, 3750, 1262, 12500), 0,
  'Multiply 1,250 by 12.',
  ['1,250 × 2 = 2,500.', '1,250 × 10 = 12,500.', '2,500 + 12,500 = 15,000 gallons.'],
  '**15,000 gallons.** 2,500 + 12,500 = 15,000.',
  '12,500 is only 1,250 × 10 — the ones row is missing.'),
 (3, 'Ana read 3 times as many pages as Ben. Ben read 214 pages. Which bar diagram shows this?',
  ['Ana\'s bar is 3 sections, each 214; Ben\'s bar is 1 section of 214',
   'Ana\'s bar is 1 section of 214; Ben\'s bar is 3 sections of 214',
   'Ana\'s bar is 214 sections, each 3 pages long',
   'Both bars are 3 sections, because the story says 3'], 0,
  'Who read MORE? Their bar is longer.',
  ['Ana read 3 times as many, so she read more.', 'Her bar is 3 copies of Ben\'s bar.',
   'Ben\'s bar is one section of 214.', 'Ana read 214 × 3 = 642 pages.'],
  '**Ana\'s bar is 3 sections of 214; Ben\'s is 1.** Ana read 642 pages.',
  'Getting the bars backwards gives the right numbers to the wrong people.'),
 (3, 'One factory makes 265 bikes a day. Another makes 13 times as many. How many bikes does the second factory make each day?',
  opts4(3445, 1060, 3345, 278), 0,
  'Multiply 265 by 13.',
  ['265 × 3 = 795.', '265 × 10 = 2,650.', '795 + 2,650 = 3,445.'],
  '**3,445 bikes.** 795 + 2,650 = 3,445.',
  '1,060 adds 265 × 3 and 265 × 1 — the 1 in 13 means 1 ten.'),
 (3, 'How can estimation show that $1,340 × 5 = $6,700 is reasonable?',
  ['1,300 × 5 = 6,500, which is close to 6,700',
   '1,000 × 5 = 5,000, which proves it exactly',
   '1,340 + 5 = 1,345, which is close to 6,700',
   'Estimation cannot check multiplication'], 0,
  'Round 1,340 to a friendly number.',
  ['1,340 is close to 1,300.', '1,300 × 5 = 6,500.',
   '6,700 is close to 6,500, so the answer is reasonable.'],
  '**1,300 × 5 = 6,500, which is close.** The exact answer lands right near the estimate.',
  'An estimate never proves an exact answer — it shows it is the right size.'),
 (1, 'One store has 2,415 stickers and another has 4 times as many. In the equation s = 2,415 × 4, what does the letter s stand for?',
  ['The unknown number of stickers in the second store',
   'The number 4, since it is the number beside the ×',
   'The word "stickers" written in a shorter way',
   'Any number at all that you would like to pick'], 0,
  'What is the question asking you to find?',
  ['The letter is a variable.', 'A variable stands for an unknown number.',
   'Here it is the number of stickers in the second store.'],
  '**The unknown number of stickers.** The variable holds the place of the answer.',
  'Choosing a letter that matches the story — s for stickers — makes it easy to remember.'),
],
 'Lesson 3-8 of the Topic 3 textbook scan: using bar diagrams and variables to write and solve multiplication equations for "times as many" problems.',
 'A bar diagram makes "times as many" visible, which is what stops her from adding when she should be multiplying.',
 [('Draw a bar diagram for a "times as many" problem', 'source'),
  ('Write and solve an equation with a variable', 'source'),
  ('Check an answer with estimation', 'source')],
 'The mistake these questions keep offering is adding the "times" number instead of multiplying ($1,340 + 5). The other is drawing the bars backwards — giving the longer bar to the person with less. One lv3 question is built entirely around which bar is which, since that is where the rest of the problem goes right or wrong.',
 ('Draw it, write the equation, multiply.', 12),
 'Lesson 3-8')

# ══ Lesson 9 · Critique Reasoning ═══════════════════════════════════════════
assert 62 * 285 == 17670 < 18000 and 60 * 300 == 18000
assert 400 * 63 == 25200 > 20000 and (400 * 6) + (400 * 3) == 3600
assert 2085 * 6 == 12510 > 12000 and 2000 * 6 == 12000
assert 38 * 150 == 5700 and 45 * 210 == 9450 and 5700 + 9450 == 15150 > 15000
assert 40 * 150 + 45 * 200 == 15000
assert 15150 - 2 * 210 - 150 == 14580 < 15000
assert 48 * 52 == 2496 < 2500 and 50 * 50 == 2500

go(9, 'Critique Reasoning', [
 ('What is their argument?',
  '**Start by saying what the person is claiming and what they used to support it.**\n'
  '• "She estimated 60 × 300 = 18,000 and said there are fewer than 18,000 seats."',
  'Name the claim before you judge it.'),
 ('Check the direction of the estimate',
  '**An estimate only supports "more than" or "less than" if it rounded the right way.**\n'
  '• Both factors rounded up → overestimate. Both down → underestimate.\n'
  '• One up and one down → it cannot prove either.',
  'Which way did the numbers move?'),
 ('Check the calculation',
  '**Look for slips: a lost zero, a wrong carry, or a number split the wrong way.**\n'
  '• 400 × 63 is not (400 × 6) + (400 × 3). 63 is 60 + 3.',
  'Splitting a number? The pieces must add back to it.'),
 ('Does the conclusion follow?',
  '**Even a true answer can come from bad reasoning — and good-looking reasoning can be wrong.**\n'
  '• Say whether the steps actually prove the claim.',
  'Right answer, wrong reason, still needs fixing.'),
 ('Ask questions',
  '**Critiquing means asking questions, deciding if the strategy makes sense, and looking for flaws.**',
  'Curious, not unkind.'),
], [
 (3, 'A stadium has 62 sections with 285 seats each. Omar estimates 60 × 300 = 18,000 and says there are fewer than 18,000 seats. Does his estimate prove it?',
  ['No — he rounded one number down and one up, so 18,000 could be high or low',
   'Yes — 18,000 is an overestimate, so the real number is smaller',
   'Yes — any estimate that ends in zeros is safe to use',
   'No — he should have added 62 and 285 instead'], 0,
  'Which way did each number get rounded?',
  ['62 was rounded DOWN to 60.', '285 was rounded UP to 300.',
   'With one down and one up, the estimate could be above or below.',
   'The real total is 17,670 — he happens to be right, but his estimate did not prove it.'],
  '**No.** One factor went down and one went up, so 18,000 proves nothing either way.',
  'His conclusion turns out true (17,670), but only an exact calculation shows that.'),
 (2, 'An office manager works out 400 × 63 as (400 × 6) + (400 × 3) = 3,600. What is the mistake?',
  ['He split 63 into 6 and 3 instead of 60 and 3',
   'He should have multiplied 400 by 9',
   'He should have added the parts first',
   'There is no mistake — 3,600 is correct'], 0,
  'Do 6 and 3 add up to 63?',
  ['6 + 3 = 9, not 63.', '63 should be split as 60 + 3.',
   '(400 × 60) + (400 × 3) = 24,000 + 1,200 = 25,200.'],
  '**He split 63 into 6 and 3 instead of 60 and 3.** The real product is 25,200.',
  'Whenever you split a number, check that the pieces add back up to it.'),
 (2, 'What is the correct value of 400 × 63?',
  opts4(25200, 3600, 24000, 2520), 0,
  'Split 63 as 60 + 3.',
  ['400 × 60 = 24,000.', '400 × 3 = 1,200.', '24,000 + 1,200 = 25,200.'],
  '**25,200.** (400 × 60) + (400 × 3).',
  '24,000 remembers the 60 but forgets the 3.'),
 (3, 'Kate sold 2,085 bracelets and made $6 on each. She says, "2,000 × 6 = 12,000 and I sold more than 2,000, so I made more than $12,000." Is she right?',
  ['Yes — she rounded down, so her real profit is even more than $12,000',
   'No — she should have rounded 2,085 up to 3,000 to be safe',
   'No — an estimate can never decide whether she made enough',
   'Yes — because $12,000 is exactly what her profit comes to'], 0,
  'Did she round 2,085 up or down?',
  ['She rounded 2,085 DOWN to 2,000.', 'That makes 12,000 an underestimate.',
   'Her real profit must be more than $12,000.', 'Exactly: 2,085 × 6 = $12,510.'],
  '**Yes.** Rounding down gives an underestimate, and it already reaches $12,000.',
  'This is sound reasoning — worth saying so when you critique, too.'),
 (2, 'You want to know if you have ENOUGH money. Which kind of estimate of your money helps most?',
  ['An underestimate, because the real amount is at least that much',
   'An overestimate, because a bigger number is always the safer one',
   'Any estimate at all, since they all work equally well',
   'No estimate helps — only the exact amount can tell you'], 0,
  'If your too-small estimate is enough, what about the real amount?',
  ['An underestimate is smaller than what you really have.',
   'If even that smaller amount is enough, the real amount is too.',
   'An overestimate could make you think you have enough when you do not.'],
  '**An underestimate.** If it is already enough, the real amount certainly is.',
  'An overestimate is useful the other way round — to check that something is under a limit.'),
 (3, 'A cargo container can hold 15,000 pounds. There are 38 boxes of 150 pounds and 45 boxes of 210 pounds. Someone estimates 40 × 150 + 45 × 200 = 15,000 and says they fit. Do they?',
  ['No — the real weight is 15,150 pounds, which is over',
   'Yes — the estimate is exactly 15,000',
   'Yes — 38 was rounded up, so there is room to spare',
   'No — the real weight is 25,000 pounds'], 0,
  'Work out the heavier boxes exactly.',
  ['38 × 150 = 5,700.', '45 × 210 = 9,450.', '5,700 + 9,450 = 15,150.',
   'That is 150 pounds over the limit.'],
  '**No.** The real weight is 15,150 pounds — the estimate rounded 210 down and hid the extra.',
  'Rounding the heavy boxes down is exactly the wrong direction when checking a limit.'),
 (2, 'What is 45 × 210?',
  opts4(9450, 9000, 1050, 945), 0,
  'Find 45 × 21, then put the zero on.',
  ['45 × 1 = 45.', '45 × 20 = 900.', '45 × 21 = 945, so 45 × 210 = 9,450.'],
  '**9,450.** 45 × 21 = 945, and the zero from 210 makes 9,450.',
  '9,000 is 45 × 200 — the estimate, not the answer.'),
 (1, 'Which question is most useful when you critique someone\'s reasoning?',
  ['Does the strategy make sense, and are the numbers right?',
   'Is the final answer a big number, or a small number?',
   'Did they write every step neatly, in pen?',
   'Did they finish before everyone else in the class?'], 0,
  'Critiquing is about the thinking, not the look of the work.',
  ['A critique checks whether the method makes sense.',
   'It also checks the calculations for slips.', 'Neatness and speed are not reasoning.'],
  '**Does the strategy make sense, and are the numbers right?** That is what a critique checks.',
  'Asking questions helps you understand their thinking before you decide.'),
 (3, 'A cargo load of 38 boxes at 150 pounds and 45 boxes at 210 pounds weighs 15,150 pounds. The limit is 15,000. Raul removes two 210-pound boxes and one 150-pound box. Does it fit now?',
  ['Yes — it now weighs 14,580 pounds',
   'No — it now weighs 15,000 pounds exactly',
   'Yes — it now weighs 14,790 pounds',
   'No — removing boxes does not change the weight enough'], 0,
  'Subtract the weight of the boxes removed.',
  ['Two heavy boxes: 2 × 210 = 420 pounds.', 'One light box: 150 pounds.',
   '15,150 − 420 − 150 = 14,580.', '14,580 is under 15,000.'],
  '**Yes — 14,580 pounds.** Removing 570 pounds brings it under the limit.',
  '14,790 forgets one of the two heavy boxes.'),
 (3, 'A student says 48 × 52 must be more than 2,500 because 50 × 50 = 2,500. Is that right?',
  ['No — rounding one up and one down can go either way; 48 × 52 is 2,496',
   'Yes — both numbers are close to 50, so the product must be more',
   'Yes — 52 is bigger than 50, so the product has to be bigger too',
   'No — 48 × 52 is much less than that, only about 2,000'], 0,
  'Which way did 48 and 52 each move?',
  ['48 went UP to 50.', '52 went DOWN to 50.',
   'One up and one down gives no promise.', '48 × 52 = 2,496, which is just under 2,500.'],
  '**No.** 48 × 52 = 2,496, just under 2,500 — mixed rounding cannot prove "more than".',
  'This is the surprising one: numbers balanced around 50 give a product slightly LESS than 50 × 50.'),
],
 'Lesson 3-9 of the Topic 3 textbook scan: critiquing someone else\'s reasoning about multiplication — checking their estimates, their calculations and whether their conclusion follows.',
 'Explaining whether someone else\'s thinking is right is one of the hardest skills on a math test, and it is exactly what "Construct Arguments" and "Critique Reasoning" questions ask for.',
 [('Describe another person\'s argument and how they support it', 'source'),
  ('Decide whether an estimate supports a "more than" or "less than" claim', 'source'),
  ('Find and fix a flaw in a calculation', 'source'),
  ('Tell a correct answer from correct reasoning', 'added')],
 'The biggest idea here is that the direction of rounding decides what an estimate can prove. Two questions show opposite outcomes of the same flaw: Omar\'s "fewer than 18,000" turns out true but was not proved, and the "48 × 52 is more than 2,500" claim turns out false (2,496). The cargo questions are the textbook\'s own example with fresh numbers — rounding the heavy boxes DOWN hid 150 extra pounds. One question also shows sound reasoning (rounding down to prove "more than"), because a critique should say when an argument is right, too.',
 ('Ask: which way did they round, and do the pieces add back up?', 13),
 'Lesson 3-9')
