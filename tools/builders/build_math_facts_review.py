"""Math Facts · All Facts Review — every table, mixed (v187).

Chris, on the four sets: "Math facts folder looks like practice for number
sets, but the quizzes will likely include all numbers. Can we make sure to
include a section for all numbers review?"

The pop quiz is 50 facts from every table, mixed, so knowing the x7 facts
inside a set of x7 facts is not the same as knowing 7 x 8 when it turns up
between 3 x 9 and 12 x 4. This part asks every fact from 0 to 12 in one pool:
the 66 facts from 2 x 2 to 12 x 12, plus the x0 and x1 rules on every table.

- The cards are the STRATEGIES, one per table, not 66 more fact cards: the
  fact cards already live in Sets 1-4. Mixed review means deciding which
  strategy a fact wants, so that is what the cards drill.
- Every product, step and distractor comes from the same helpers as the sets
  (build_math_facts.py), so the two can never disagree about a fact.
- `order:1` trails the whole shelf, after Set 4. The title alone would sort
  "All" ahead of "Set 1", and `order` is a whole-shelf bucket, which is
  exactly what a review of the whole shelf wants (the v102 note).
- `factsMixed:true` marks it as the review: the pop quiz pool deduplicates by
  fact and prefers the set that owns it, so adding this unit does not double
  any fact in a sprint.
"""
import json, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build, REPO
from build_math_facts import (X, HOOK, SPECIAL, steps_for, check_tip, distractors,
                              level, table_of)

UID = 'unit-mf-all'
PATH = 'content/math-facts-review.json'

C, Q = [], []

STRAT = [
    (0,  '**Always 0.**\n• Zero groups of anything is nothing.\n• 0 × 12 = 0 and 12 × 0 = 0.', 'No groups, nothing to count.'),
    (1,  '**The other number, unchanged.**\n• One group of 9 is just 9.\n• 1 × 11 = 11.', 'One group: nothing changes.'),
    (2,  '**Double the other number.**\n• 2 × 8: 8 + 8 = 16.', 'Twins.'),
    (3,  '**Double it, then add one more group.**\n• 3 × 7: double 7 is 14, plus 7 is 21.', 'Two groups and one more.'),
    (4,  '**Double it, then double again.**\n• 4 × 6: double 6 is 12, double 12 is 24.', 'Double, double.'),
    (5,  '**Half of times 10.**\n• 5 × 8: 10 × 8 = 80, half is 40.\n• The answer always ends in 0 or 5.', 'Half of a ten-fact.'),
    (6,  '**Times 5, plus one more group.**\n• 6 × 7: 5 × 7 = 35, plus 7 is 42.', 'One past the fives.'),
    (7,  '**Times 5 plus times 2.**\n• 7 × 8: 5 × 8 = 40, 2 × 8 = 16, 40 + 16 = 56.', 'Five and two make seven.'),
    (8,  '**Double, double, double.**\n• 8 × 6: 12, then 24, then 48.', 'Three doublings.'),
    (9,  '**Times 10, minus one group.**\n• 9 × 7: 70 − 7 = 63.\n• The digits of the answer add up to 9.', 'Ten groups, take one away.'),
    (10, '**Add a zero to the end.**\n• 10 × 7 = 70: seven ones become seven tens.', 'Ones become tens.'),
    (11, '**Times 10, plus one more group.**\n• 11 × 6: 60 + 6 = 66.\n• Up to 11 × 9, the digit just repeats.', 'Ten groups and one more.'),
    (12, '**Times 10 plus times 2.**\n• 12 × 7: 70 + 14 = 84.', 'Ten and two make twelve.'),
]
for t, d, h in STRAT:
    card(C, 'Any number × %d' % t, d, hint=h, frm='added')
card(C, 'Which strategy?', '**Use the smaller factor\'s strategy, unless the other one is easier.**\n'
     '• 7 × 2: double 7 is quicker than the sevens.\n• 9 × 6: either works; pick the one you trust.',
     hint='Turn the fact around if the other way is easier.', frm='added')
card(C, 'The hard ones', '**6 × 7 = 42, 6 × 8 = 48, 7 × 8 = 56, 8 × 8 = 64, 7 × 7 = 49.**\n'
     '• These are the facts most people miss under a clock.\n• 5, 6, 7, 8: 56 is 7 × 8.',
     hint='Say these five out loud until they come without counting.', frm='added')
card(C, 'Mixed, against a clock', '**Answer the ones you know first, skip the ones you don\'t.**\n'
     '• On paper a skipped fact costs nothing; a stuck one costs the clock.\n'
     '• Come back to the skips if time is left.', hint='Skip, don\'t stall.', frm='added')

# Every fact from 2 x 2 to 12 x 12, each worked by the strategy of the set
# that owns it, so the walkthrough matches the card she studied it on.
for t, n in table_of():
    a, b = (t, n) if (t + n) % 2 else (n, t)
    p = t * n
    hook = SPECIAL.get(tuple(sorted((t, n))), HOOK[t])
    st = steps_for(t, n, a, b)
    q(Q, level(p), 'What is %d %s %d?' % (a, X, b), [p] + distractors(t, n), 0,
      hook, st, '**%d.** %s' % (p, ' '.join(st[1:-1])), check_tip(a, b, p))
    Q[-1]['fact'] = [a, b]

# The x0 and x1 rules on facts the sets never ask, so "all numbers" means all.
for a, b in ((0, 11), (6, 0), (1, 7), (12, 1), (0, 0), (1, 1)):
    p = a * b
    z = 0 in (a, b)
    big = max(a, b)
    st = (['Any number times 0 is 0.', 'There are no groups to count.', 'So %d %s %d = 0.' % (a, X, b)] if z else
          ['Any number times 1 is itself.', 'One group of %d is %d.' % (big, big), 'So %d %s %d = %d.' % (a, X, b, p)])
    opts = [p] + ([big or 1, 10, 2] if z and big == 0 else [big, 1, 10 * big] if z else
                  [2, 0, 11] if big == 1 else [1, big + 1, 0])
    assert len(set(opts)) == 4 and opts[0] == a * b, (a, b, opts)
    q(Q, 1, 'What is %d %s %d?' % (a, X, b), opts, 0, 'Zero groups.' if z else 'One group.', st,
      '**%d.** %s' % (p, st[0]), 'The rule never changes, however big the other number is.')
    Q[-1]['fact'] = [a, b]

assert len(Q) == 72, len(Q)

build('wayfinder', C, Q, UID, 'Math Facts · All Facts Review', 'math',
      'Every multiplication fact from 0 to 12, mixed together the way the pop quiz will ask them, with a strategy card for each table.',
      'The pop quiz takes facts from every table at once. Knowing the sevens inside a set of sevens is not the same as knowing 7 × 8 when it turns up between 3 × 9 and 12 × 4.',
      [('Answer any fact from 0 × 0 to 12 × 12 from memory, in any order.', 'added'),
       ('Pick the quickest strategy for a fact you are not sure of.', 'added'),
       ('Skip and come back rather than stall on one fact.', 'added')],
      ('The mixed review for the multiplication facts pop quiz (50 facts in 3 minutes). '
       'It asks all 66 facts from 2 × 2 to 12 × 12 in one pool, plus the × 0 and × 1 rules, '
       'so a round mixes every table the way the real quiz will. The cards are one strategy per table '
       'rather than repeats of the fact cards in Sets 1 to 4. Every answer and wrong option was computed, '
       'not typed, by the same code that built the sets. The facts run to 12 × 12, which is an assumption '
       'until her teacher\'s sheet arrives; if it stops at 10 × 10, the × 11 and × 12 facts are extra.'),
      ('Take a round of twenty mixed facts, then try the pop quiz sprint.', 12),
      PATH, 'Teacher\'s math update, 10/15', 'Math facts (from the teacher\'s update)',
      offset_hours=2, round_=20, order_=1)

fp = os.path.join(REPO, PATH)
d = json.load(io.open(fp, encoding='utf-8'))
u = d['records'][UID]
u.update(facts=True, factsMixed=True, prep=True, libv=1, quarter=2)
for x in u['questions']:
    a, b = x['fact']
    assert x['opts'][x['ans']] == str(a * b), x['id']
    assert len(set(x['opts'])) == 4
io.open(fp, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print('review:', len(C), 'cards,', len(Q), 'questions')
