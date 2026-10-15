"""Math Facts — multiplication facts 0–12, four units on one shelf (v185).

From the 4th-grade teacher's math update (Chris forwarded it, 2026-10-15):
a "pop quiz" of 50 multiplication facts in 3 minutes is coming, and some
students are shaky on their facts. Her attachments (flashcards and a timed
practice sheet) never reached Drive, so these are built from the email
itself: every product 2–12 x 2–12, plus the x0 and x1 rules.

Every product, every strategy step and every distractor is COMPUTED here and
asserted, never typed. Each fact question carries `fact:[a,b]`, which is what
the in-app Facts sprint draws from — so a fact missed in the sprint lands on
this unit's own question in the Growth Zone.
"""
import json, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build, REPO

UNITS = [
    (1, 'unit-mf-1', 'x0, x1, x2, x5 and x10', [2, 10, 5]),
    (2, 'unit-mf-2', 'x3 and x4', [3, 4]),
    (3, 'unit-mf-3', 'x6 and x7', [6, 7]),
    (4, 'unit-mf-4', 'x8, x9, x11 and x12', [11, 9, 12, 8]),
]
X = '×'
TITLE = lambda s: s.replace('x', X)

def steps_for(t, n, a, b):
    p = t * n
    final = 'So %d %s %d = %d.' % (a, X, b, p)
    S = {
      2:  ['Times 2 means double.', 'Double %d: %d + %d = %d.' % (n, n, n, p)],
      10: ['Times 10 makes each one worth ten.', '%d ones become %d tens.' % (n, n), '%d tens is %d.' % (n, p)],
      5:  ['Times 5 is half of times 10.', '10 %s %d = %d.' % (X, n, 10*n), 'Half of %d is %d.' % (10*n, p)],
      3:  ['Times 3 is a double plus one more group.', 'Double %d: %d.' % (n, 2*n), 'Add one more %d: %d + %d = %d.' % (n, 2*n, n, p)],
      4:  ['Times 4 is double, then double again.', 'Double %d: %d.' % (n, 2*n), 'Double %d: %d.' % (2*n, p)],
      6:  ['Times 6 is times 5 plus one more group.', '5 %s %d = %d.' % (X, n, 5*n), 'Add one more %d: %d + %d = %d.' % (n, 5*n, n, p)],
      7:  ['Times 7 is times 5 plus times 2.', '5 %s %d = %d.' % (X, n, 5*n), '2 %s %d = %d.' % (X, n, 2*n), '%d + %d = %d.' % (5*n, 2*n, p)],
      8:  ['Times 8 is double, double, double.', 'Double %d: %d.' % (n, 2*n), 'Double again: %d.' % (4*n), 'Double once more: %d.' % p],
      9:  ['Times 9 is times 10, minus one group.', '10 %s %d = %d.' % (X, n, 10*n), 'Take away one %d: %d %s %d = %d.' % (n, 10*n, '−', n, p)],
      11: ['Times 11 is times 10 plus one more group.', '10 %s %d = %d.' % (X, n, 10*n), 'Add one more %d: %d + %d = %d.' % (n, 10*n, n, p)],
      12: ['Times 12 is times 10 plus times 2.', '10 %s %d = %d.' % (X, n, 10*n), '2 %s %d = %d.' % (X, n, 2*n), '%d + %d = %d.' % (10*n, 2*n, p)],
    }[t]
    # Every arithmetic claim in a step is re-checked: "x + y = z" and "x - y = z".
    for s in S:
        for op, f in (('+', lambda x, y: x + y), ('−', lambda x, y: x - y)):
            parts = s.rstrip('.').split(': ')[-1].split(' = ')
            if len(parts) == 2 and (' %s ' % op) in parts[0]:
                l, r = parts[0].split(' %s ' % op)
                assert f(int(l), int(r)) == int(parts[1]), s
    return S + [final]

HOOK = {2: 'Double it.', 10: 'Tens: the ones become tens.', 5: 'Half of times 10.',
        3: 'Double, plus one more group.', 4: 'Double, double.', 6: 'Times 5, plus one more group.',
        7: 'Times 5 plus times 2.', 8: 'Double, double, double.', 9: 'Times 10, minus one group.',
        11: 'Times 10, plus one more group.', 12: 'Times 10 plus times 2.'}
SPECIAL = {(7, 8): '5, 6, 7, 8 — 56 is 7 %s 8.' % X, (12, 12): '12 %s 12 = 144, a dozen dozens.' % X,
           (6, 8): 'Double 24 (that is 6 %s 4) to land on 48.' % X}

def check_tip(a, b, p):
    """A way to CHECK the answer — the teacher's ask: students know the skill and
    still make simple calculation errors, so every fact carries a check."""
    if 9 in (a, b) and p != 99:
        return 'Check a %s9 answer: its digits add up to 9 (%s).' % (X, ' + '.join(str(p)))
    if 5 in (a, b):
        return 'Check: a %s5 answer always ends in 0 or 5.' % X
    if a % 2 == 0 or b % 2 == 0:
        return 'Check: one factor is even, so the answer must be even too.'
    return 'Check with the turn-around: %d %s %d is the same fact.' % (b, X, a)

def distractors(a, b):
    p = a * b
    cand = [a * (b - 1), a * (b + 1), (a - 1) * b, (a + 1) * b, int(str(p)[::-1]) if p >= 10 else p + 10,
            p + 10, p - 10, a + b]
    out = []
    for c in cand:
        if c > 0 and c != p and c not in out: out.append(c)
    assert len(out) >= 3, (a, b)
    return out[:3]

def level(p): return 1 if p <= 20 else 2 if p <= 50 else 3

def table_of():
    """Each fact belongs to the first set, in learning order, holding either factor.
    Returns [(t, n)] in set order: t is the table whose strategy works it out."""
    done, out = set(), []
    for num, uid, sub, tables in UNITS:
        for t in tables:
            for n in range(2, 13):
                key = tuple(sorted((t, n)))
                if key in done: continue
                done.add(key); out.append((t, n))
    return out

def main():
    done = set()
    for num, uid, sub, tables in UNITS:
        C, Q = [], []
        facts = []
        for t in tables:
            for n in range(2, 13):
                key = tuple(sorted((t, n)))
                if key in done: continue
                done.add(key); facts.append((t, n))
        if num == 1:
            card(C, 'Any number %s 0' % X, '**0.**\n• Zero groups of anything is nothing at all.\n• 9 %s 0 = 0, and 0 %s 9 = 0.' % (X, X),
                 hint='No groups, nothing to count.')
            card(C, 'Any number %s 1' % X, '**The number itself.**\n• One group of 7 is just 7.\n• 1 %s 12 = 12.' % X,
                 hint='One group: nothing changes.')
            card(C, 'Turn-around facts', '**Swapping the two numbers does not change the answer.**\n• 3 %s 8 = 8 %s 3 = 24.\n• So every fact you learn is really two facts.' % (X, X),
                 hint='Learn one, get its partner free.')
            card(C, 'Checking your answer', '**Check with a fact you are sure of, or with the turn-around.**\n• Not sure of 6 %s 7? 6 %s 6 = 36, plus one more 6 is 42.\n• On a timed quiz, check the ones you hesitated on, not every one.' % (X, X),
                 hint='Students know the facts and still slip: the check catches the slip.', frm='added')
        for t, n in facts:
            a, b = (t, n) if (t + n) % 2 else (n, t)
            p = t * n
            hook = SPECIAL.get(tuple(sorted((t, n))), HOOK[t])
            st = steps_for(t, n, a, b)
            partner = ('A square fact: the same number twice.' if a == b
                       else 'Same answer as %d %s %d.' % (b, X, a))
            card(C, '%d %s %d' % (a, X, b), '**%d**\n• %s\n• %s' % (p, partner, ' '.join(st[1:-1])),
                 hint=hook)
            ds = distractors(t, n)
            q(Q, level(p), 'What is %d %s %d?' % (a, X, b), [p] + ds, 0,
              hook, st, '**%d.** %s' % (p, ' '.join(st[1:-1])), check_tip(a, b, p))
            Q[-1]['fact'] = [a, b]
            assert int(Q[-1]['opts'][0]) == a * b
        if num == 1:
            for (a, b) in ((0, 7), (9, 0), (1, 8), (12, 1)):
                p = a * b
                rule0 = 0 in (a, b)
                st = ([('Any number times 0 is 0.'), 'There are no groups to count.', 'So %d %s %d = 0.' % (a, X, b)] if rule0 else
                      ['Any number times 1 is itself.', 'One group of %d is %d.' % (max(a, b), max(a, b)), 'So %d %s %d = %d.' % (a, X, b, p)])
                opts = [p] + ([max(a, b), 1, 10 * max(a, b)] if rule0 else [1, max(a, b) + 1, 0])
                q(Q, 1, 'What is %d %s %d?' % (a, X, b), opts, 0,
                  'Zero groups.' if rule0 else 'One group.', st, '**%d.** %s' % (p, st[0]),
                  'The rule never changes, however big the other number is.')
                Q[-1]['fact'] = [a, b]
            q(Q, 2, 'Mia knows that 4 %s 9 = 36. Without working anything out, what is 9 %s 4?' % (X, X),
              [36, 49, 94, 13], 0, 'Turn it around.',
              ['9 %s 4 has the same two numbers as 4 %s 9.' % (X, X), 'Swapping the order of a multiplication does not change the answer.', 'So 9 %s 4 = 36.' % X],
              '**36.** A turn-around fact has the same answer, so knowing one fact gives you its partner free.',
              'Every fact you learn is two facts.')
        title = 'Math Facts · Set %d: %s' % (num, TITLE(sub))
        path = 'content/math-facts-%d.json' % num
        n_f = len(facts)
        build('wayfinder', C, Q, uid, title, 'math',
              'Multiplication facts for the %s tables, one card per fact with a strategy for working it out and a way to check it.' % TITLE(sub),
              'Your class has a pop quiz coming: 50 multiplication facts in 3 minutes. That is under four seconds a fact, so the facts have to come from memory, and the strategies are how they get there.',
              [('Answer every %s fact from memory.' % TITLE(sub), 'added'),
               ('Use a strategy to work out a fact you are not sure of.', 'added'),
               ('Check an answer with a fact you know, or with the turn-around.', 'added')],
              ('Built from the teacher\'s math update about the multiplication facts pop quiz (50 facts in 3 minutes). '
               'Her attached flashcards and practice sheet did not reach Drive, so the facts and strategies here are ours, not copies of hers. '
               'This part covers %d facts. Every answer, strategy step and wrong option was computed, not typed. '
               'The facts run to 12 %s 12; if her sheet stops at 10 %s 10, the x11 and x12 facts are extra. '
               'The Facts sprint on each card is the pop quiz shape: typed answers against one clock.') % (n_f, X, X),
              ('Flip the cards once, then try a sprint and see which facts it catches.', 10),
              path, 'Teacher\'s math update, 10/15', 'Math facts (from the teacher\'s update)',
              offset_hours=2, round_=(len(Q) if len(Q) <= 15 else 12))
        fp = os.path.join(REPO, path)
        d = json.load(io.open(fp, encoding='utf-8'))
        u = d['records'][uid]
        u['facts'] = True
        u['libv'] = 1
        u['quarter'] = 2
        for x in u['questions']:
            if 'fact' in x:
                a, b = x['fact']
                assert x['opts'][x['ans']] == str(a * b), x['id']
                assert len(set(x['opts'])) == 4
        io.open(fp, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))

    assert len(done) == 66, len(done)
    print('facts covered:', len(done))

if __name__ == "__main__":
    main()
