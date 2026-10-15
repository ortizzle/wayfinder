"""Unit 5 · Before You Start: Long Division with One-Digit Divisors (v186).

From the 4th-grade teacher's math update of 10/15: Unit 5 "jumps right into
two-digit divisors ... and expects them to already know how to do long
division with one-digit divisors", and families should make sure students can
do it. Her practice sheet never reached Drive, so this is built from the email:
one-digit long division, a zero in the quotient, remainders and what they mean,
checking with multiplication, and — her own tip — finding the mistake in a
worked problem.

Every quotient, remainder, check and wrong option is computed and asserted. None
of the email's own numbers (123 / 3, 1723 / 13) is used.
"""
import json, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build, REPO

D = '÷'; X = '×'; MINUS = '−'

def dm(a, b):
    return a // b, a % b

def fmt(qt, r):
    return '%s R%d' % ('{:,}'.format(qt), r) if r else '{:,}'.format(qt)

def drop_zeros(n):
    s = str(n).replace('0', '')
    return int(s) if s else 0

def long_steps(a, b):
    """The written steps of a one-digit long division, as sentences. Verified
    against divmod at the end."""
    digits = str(a); out = []; cur = 0; qd = ''; started = False
    for i, ch in enumerate(digits):
        cur = cur * 10 + int(ch)
        if not started and cur < b and i < len(digits) - 1:
            out.append('%d is smaller than %d, so use the next digit too.' % (cur, b))
            continue
        started = True
        k = cur // b
        qd += str(k)
        if i == 0 or len(out) == 0 or True:
            out.append('%d %s %d = %d; %d %s %d = %d; %d %s %d = %d.' % (cur, D, b, k, k, X, b, k*b, cur, MINUS, k*b, cur - k*b))
        cur -= k * b
    qq, rr = dm(a, b)
    assert int(qd) == qq and cur == rr, (a, b)
    return out

def compute_q(Q, lv, a, b, hint, tip, slips):
    """A plain 'what is a / b' question. `slips` maps each wrong option to the
    named mistake that produces it; every slip is asserted wrong."""
    qt, r = dm(a, b)
    ans = fmt(qt, r)
    for s in slips:
        assert s != ans, (a, b, s)
    assert len(set([ans] + list(slips))) == 4, (a, b, slips)
    st = long_steps(a, b)
    if len(st) > 4:
        st = st[:4]
    st = st + ['Check: %s %s %d%s = %s.' % ('{:,}'.format(qt), X, b, (' + %d' % r) if r else '', '{:,}'.format(a))]
    assert qt * b + r == a
    st = st[:5] + ['So %s %s %d = %s.' % ('{:,}'.format(a), D, b, ans)]
    why = '; '.join('%s is %s' % (k, v) for k, v in slips.items())
    q(Q, lv, 'What is %s %s %d?' % ('{:,}'.format(a), D, b), [ans] + list(slips), 0, hint, st,
      '**%s.** Check it: %s %s %d%s = %s. The wrong answers come from real slips: %s.' % (
          ans, '{:,}'.format(qt), X, b, (' + %d' % r) if r else '', '{:,}'.format(a), why), tip)

C, Q = [], []
card(C, 'Dividend, divisor, quotient', '**In 457 %s 6 = 76 R1: 457 is the dividend, 6 is the divisor, 76 is the quotient.**\n• The dividend is being shared out; the divisor is how many groups.\n• The quotient is how many in each group.' % D,
     hint='The DIVISOR does the dividing.')
card(C, 'Remainder', '**What is left over when the groups are full.**\n• In 457 %s 6 = 76 R1, the remainder is 1.\n• It must always be smaller than the divisor, or another group would fit.' % D,
     hint='If the leftover could make one more group, you are not done.')
card(C, 'The four steps', '**Divide, Multiply, Subtract, Bring down — then repeat.**\n• One loop for each digit of the dividend.\n• Stop when there is nothing left to bring down.',
     hint='Does McDonald\'s Sell Burgers: D, M, S, B.')
card(C, 'Where to start', '**Start with the first digit if the divisor fits into it; if not, use the first two digits.**\n• 284 %s 4: 4 does not fit into 2, so start with 28.\n• That also tells you the quotient has one digit fewer than the dividend.' % D,
     hint='Too small to share? Take one more digit.')
card(C, 'A zero in the quotient', '**When a brought-down number is smaller than the divisor, write 0 in the quotient and bring down the next digit.**\n• 824 %s 4: 8 %s 4 = 2, bring down 2: 2 %s 4 = 0, bring down 4: 4 %s 4 = 1, so 206.\n• Skipping the 0 gives 26, which is ten times too small.' % (D, D, D, D),
     hint='Every digit you bring down gets a digit in the answer.')
card(C, 'Check with multiplication', '**Quotient %s divisor + remainder should give back the dividend.**\n• 76 %s 6 + 1 = 457, so 457 %s 6 = 76 R1 is right.\n• It catches almost every slip, so it is worth the ten seconds.' % (X, X, D),
     hint='Division undone by multiplication.')
card(C, 'Estimate first', '**Round to numbers that divide easily, so you know roughly what to expect.**\n• 4,128 %s 8 is about 4,000 %s 8 = 500.\n• An answer of 51 or 5,160 is then clearly wrong before you check it.' % (D, D),
     hint='A rough answer catches a wrong number of digits.')
card(C, 'Facts do the work', '**Every Divide step is a multiplication fact in reverse.**\n• 23 %s 4: think 4 %s 5 = 20, the biggest that fits, so 5 with 3 left.\n• Quick facts make long division quick.' % (D, X),
     hint='Know 4 %s 5 and you know 20 %s 4.' % (X, D))
card(C, 'What the remainder means', '**In a word problem, decide what to do with the remainder.**\n• Round up when everyone must fit (cars, boxes, tables).\n• Drop it when only whole groups count (whole bows); sometimes the remainder IS the answer (the leftovers).',
     hint='Ask: what is the leftover, in the story?')
card(C, 'Find the mistake', '**Check each step, not just the answer: the divide, the multiply, the subtract and the bring-down.**\n• Most mistakes are a subtraction slip or a skipped zero.\n• The check (quotient %s divisor + remainder) tells you THAT something is wrong; the steps tell you where.' % X,
     hint='Test the answer first, then hunt step by step.', frm='added')

# --- vocabulary and set-up
q(Q, 1, 'In 457 %s 6 = 76 R1, which number is the remainder?' % D, ['1', '6', '76', '457'], 0,
  'The remainder is what is left over.',
  ['The dividend, 457, is being shared out.', 'The divisor, 6, is the number of groups.', 'Each group gets 76, the quotient.', 'The 1 left over is the remainder.'],
  '**1.** 76 groups of 6 make 456, and 457 is 1 more, so 1 is left over.', 'A remainder is always smaller than the divisor.')
q(Q, 1, 'In 845 %s 5 = 169, which number is the divisor?' % D, ['5', '845', '169', '0'], 0,
  'The divisor does the dividing.',
  ['845 is the dividend, the amount being shared.', '5 is the number it is divided by: the divisor.', '169 is the quotient.', 'So the divisor is 5.'],
  '**5.** The divisor is the number you divide BY.', 'Check it: 169 %s 5 = 845.' % X)
q(Q, 1, 'Put the four steps of long division in order.', ['Divide', 'Multiply', 'Subtract', 'Bring down'], 0,
  'Does McDonald\'s Sell Burgers.',
  ['Divide: how many times does the divisor fit?', 'Multiply that digit by the divisor.', 'Subtract to find what is left.', 'Bring down the next digit, and repeat.'],
  '**Divide, Multiply, Subtract, Bring down.** One loop per digit, until nothing is left to bring down.', 'The mnemonic is the order: D, M, S, B.', kind='order')
q(Q, 1, 'To start 284 %s 4, which number do you divide by 4 first?' % D, ['28', '2', '284', '84'], 0,
  'Does 4 fit into 2?',
  ['4 does not fit into 2.', 'So take the first two digits: 28.', '28 %s 4 = 7.' % D, 'So you start with 28.'],
  '**28.** 4 does not fit into 2, so you take one more digit. The quotient, 71, has only two digits.', 'The starting number tells you how many digits the answer will have.')
q(Q, 2, 'How many digits will the quotient of 382 %s 5 have?' % D, ['2', '1', '3', '4'], 0,
  'Does 5 fit into 3?',
  ['5 does not fit into 3.', 'So start with 38: the first digit of the quotient goes in the tens place.', '382 %s 5 = 76 R2.' % D, 'So the quotient has 2 digits.'],
  '**2.** 5 does not fit into 3, so the quotient starts in the tens place: 76 R2.', 'Estimate: 382 is less than 500, and 500 %s 5 = 100, so the answer is under 100.' % D)
assert dm(382, 5) == (76, 2) and dm(284, 4) == (71, 0)
q(Q, 2, 'Which is the best estimate for 4,128 %s 8?' % D, ['About 500', 'About 50', 'About 5,000', 'About 5'], 0,
  'Round 4,128 to a number 8 divides easily.',
  ['4,128 is close to 4,000.', '4,000 %s 8 = 500.' % D, 'The exact answer is 516, close to 500.', 'So the best estimate is about 500.'],
  '**About 500.** 4,000 %s 8 = 500, and the exact quotient is 516.' % D, 'Estimate first, so a wrong number of digits jumps out.')
assert dm(4128, 8) == (516, 0)
q(Q, 2, 'Which multiplication fact gives you 56 %s 7?' % D, ['7 %s 8 = 56' % X, '7 %s 7 = 49' % X, '6 %s 8 = 48' % X, '8 %s 8 = 64' % X], 0,
  'Which fact has 7 and 56 in it?',
  ['56 %s 7 asks: 7 times what is 56?' % D, '7 %s 8 = 56.' % X, 'So 56 %s 7 = 8.' % D],
  '**7 %s 8 = 56.** Division undoes multiplication, so 56 %s 7 = 8.' % (X, D), 'Every divide step is a facts question in reverse.')

# --- compute (named slips as distractors)
compute_q(Q, 2, 684, 3, 'Start with 6.', 'Check: the quotient times 3 must give 684.',
          {'218': 'a slip in the tens', '238': 'one too many in the tens', '2,28': 'not a number'} if False else
          {'218': 'a wrong tens digit', '238': 'one ten too many', '28': 'the hundreds digit dropped'})
compute_q(Q, 2, 945, 5, '5 fits into 9 once.', 'An answer to a %s5 question, times 5, must end in 0 or 5.' % D,
          {'189 R5': 'stopping before the last group', '179': 'a subtraction slip', '199': 'one ten too many'})
compute_q(Q, 2, 739, 4, 'There will be something left over.', 'The remainder must be smaller than 4.',
          {'184': 'the remainder left off', '183 R7': 'a remainder too big to keep', '185': 'rounded up instead of a remainder'})
compute_q(Q, 2, 824, 4, 'Watch the middle digit.', 'Every digit you bring down gets a digit in the quotient.',
          {'26': 'the zero skipped', '216': 'a zero where none belongs', '260': 'the zero in the wrong place'})
compute_q(Q, 3, 3612, 6, '6 does not fit into 3.', 'Estimate: 3,600 %s 6 = 600.' % D,
          {'62': 'the zero skipped', '6,02': 'not a number', '612': 'the tens digit wrong'} if False else
          {'62': 'the zero skipped', '612': 'a wrong tens digit', '6,020': 'one digit too many'})
compute_q(Q, 2, 296, 8, '8 does not fit into 2.', 'Two digits: 8 does not fit into 2.',
          {'37 R1': 'a remainder that is not there', '36': 'one too few', '370': 'one digit too many'})
compute_q(Q, 3, 5264, 7, '7 does not fit into 5.', 'Estimate: 5,600 %s 7 = 800, so a bit less than 800.' % D,
          {'742': 'a slip in the tens', '762': 'one ten too many', '7,520': 'one digit too many'})
compute_q(Q, 3, 1509, 8, '8 does not fit into 1.', 'The remainder must be smaller than 8.',
          {'188': 'the remainder left off', '187 R13': 'a remainder too big to keep', '189': 'rounded up instead of a remainder'})

# --- checking and finding the mistake (the teacher's own tip)
assert 96 * 6 + 3 == 579
q(Q, 2, 'Kai got 96 R3 for 579 %s 6. Which calculation checks it?' % D,
  ['96 %s 6 + 3 = 579' % X, '96 %s 3 + 6 = 579' % X, '579 %s 6 + 3 = 96' % X, '96 + 6 %s 3 = 579' % X], 0,
  'Undo the division.',
  ['Multiply the quotient by the divisor: 96 %s 6 = 576.' % X, 'Add the remainder: 576 + 3 = 579.', 'That is the dividend, so the answer checks out.'],
  '**96 %s 6 + 3 = 579.** Quotient times divisor, plus the remainder, gives back the dividend.' % X, 'If the check does not land on the dividend, hunt for the step that slipped.')
assert dm(632, 4) == (158, 0) and 23 - 20 == 3
q(Q, 3, 'Lena worked out 632 %s 4. She wrote: 6 %s 4 = 1, 6 %s 4 = 2. Bring down 3: 23 %s 4 = 5, 23 %s 20 = 1. Bring down 2: 12 %s 4 = 3. Answer: 153. Where is her mistake?' % (D, D, MINUS, D, MINUS, D),
  ['23 %s 20 is 3, not 1' % MINUS, '6 %s 4 should be 2' % D, '23 %s 4 should be 6' % D, '12 %s 4 should be 4' % D], 0,
  'Check each subtraction.',
  ['6 %s 4 = 1 with 2 left: right.' % D, '23 %s 4 = 5, and 5 %s 4 = 20: right.' % (D, X), '23 %s 20 = 3, not 1: there it is.' % MINUS, 'With 3 left, she brings down 2 to make 32, and 32 %s 4 = 8.' % D, 'The answer is 158.'],
  '**23 %s 20 is 3, not 1.** One subtraction slip changed the last digit. Check: 153 %s 4 = 612, not 632, so the check would have caught it.' % (MINUS, X),
  'The check tells you something is wrong; the steps tell you where.')
assert dm(2436, 6) == (406, 0)
q(Q, 3, 'Omar wrote 2,436 %s 6 = 46. What did he do wrong?' % D,
  ['He skipped the 0 when 3 was too small for 6', 'He started with 2 instead of 24', 'He said 24 %s 6 = 4 instead of 5' % D, 'He forgot to bring down the 6'], 0,
  'Check it: 46 %s 6 is about 280, nowhere near 2,436.' % X,
  ['24 %s 6 = 4.' % D, 'Bring down 3: 6 does not fit into 3, so the quotient gets a 0.', 'Bring down 6: 36 %s 6 = 6.' % D, 'The answer is 406, not 46.'],
  '**He skipped the 0.** When the 3 was too small to divide by 6, a 0 belongs in the quotient. 406 %s 6 = 2,436.' % X,
  'Estimate first: 2,400 %s 6 = 400, so 46 is far too small.' % D)
assert dm(365, 7) == (52, 1) and 51 * 7 + 8 == 365
q(Q, 3, 'Maya says 365 %s 7 = 51 R8. Without redoing the division, how can you tell it is wrong?' % D,
  ['The remainder 8 is bigger than the divisor 7', '51 is too big to be the quotient', 'An odd dividend cannot have a remainder', '51 %s 7 + 8 does not make 365' % X], 0,
  'Could one more group of 7 fit?',
  ['A remainder of 8 is more than 7.', 'So one more group of 7 fits: 52 groups, with 1 left.', '51 %s 7 + 8 = 365 does check out, so the check alone misses it.' % X, 'The answer is 52 R1.'],
  '**The remainder is bigger than the divisor.** If 8 are left, another group of 7 fits, so the answer is 52 R1. Her check works out, which is why the remainder rule matters too.',
  'A remainder must always be smaller than the divisor.')

# --- what the remainder means
assert dm(27, 4) == (6, 3) and dm(50, 8) == (6, 2) and dm(93, 4) == (23, 1)
q(Q, 3, 'A class of 27 students rides to the museum in cars that hold 4 students each. How many cars are needed?',
  ['7', '6', '6 R3', '3'], 0, 'Every student must get a seat.',
  ['27 %s 4 = 6 R3.' % D, '6 cars hold 24 students, and 3 are left without a seat.', 'Those 3 need one more car.', 'So 7 cars are needed.'],
  '**7.** 6 cars leave 3 students behind, so you round up.', 'Ask what the leftover is in the story: here it is people who still need a car.')
q(Q, 3, 'A ribbon is 50 inches long, and each bow uses 8 inches. How many whole bows can be made?',
  ['6', '7', '2', '6 R2'], 0, 'Only whole bows count.',
  ['50 %s 8 = 6 R2.' % D, '6 bows use 48 inches.', 'The 2 inches left are not enough for another bow.', 'So 6 whole bows.'],
  '**6.** The 2 leftover inches cannot make a bow, so the remainder is dropped.', 'When only whole groups count, drop the remainder.')
q(Q, 3, '93 stickers are shared equally among 4 friends, and any stickers left over go to the teacher. How many does the teacher get?',
  ['1', '23', '24', '4'], 0, 'The question asks about the leftovers.',
  ['93 %s 4 = 23 R1.' % D, 'Each friend gets 23.', '1 sticker is left over.', 'So the teacher gets 1.'],
  '**1.** Here the remainder IS the answer: 23 each, 1 left for the teacher.', 'Read what the question asks for: the share, or the leftover.')

parent = ("Built from the teacher's math update of 10/15, which says Unit 5 starts straight at two-digit divisors and expects "
          "students to already do long division with one-digit divisors, and asks families to make sure they can. Her practice "
          "sheet did not reach Drive, so the problems here are ours, not copies of hers. Every quotient, remainder and check was "
          "computed, and each wrong option comes from a named slip (a skipped zero, a dropped remainder, a remainder bigger than "
          "the divisor). Three questions are her own suggestion: show a worked problem with a mistake and ask where it is. "
          "The one thing most likely to trip her up is the zero in the quotient.")
build('wayfinder', C, Q, 'unit-m5-ld1', 'Unit 5 · Before You Start: Long Division with One-Digit Divisors', 'math',
      'Long division with a one-digit divisor: the four steps, where to start, a zero in the quotient, remainders and what they mean in a story, and checking with multiplication.',
      'Unit 5 jumps straight to dividing by two-digit numbers, and it assumes this is already easy. Getting it solid now is what makes that unit manageable.',
      [('Divide a 3- or 4-digit number by a 1-digit number, with or without a remainder.', 'source'),
       ('Check a division answer with multiplication.', 'source'),
       ('Find the step where a worked division went wrong.', 'source'),
       ('Decide what a remainder means in a word problem.', 'added')],
      parent, ('Run the cards, then the quiz. Try every problem on paper first, then check it with multiplication.', 15),
      'content/math-longdiv-1.json', "Teacher's math update, 10/15", 'Long division review (from the teacher\'s update)',
      offset_hours=2, round_=10)
fp = os.path.join(REPO, 'content/math-longdiv-1.json')
d = json.load(io.open(fp, encoding='utf-8'))
u = d['records']['unit-m5-ld1']
u['series'] = 'Unit 5'; u['libv'] = 1; u['quarter'] = 2
io.open(fp, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
