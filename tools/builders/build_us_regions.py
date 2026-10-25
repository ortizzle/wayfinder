# -*- coding: utf-8 -*-
"""U.S. Regions, five parts, for the Regions quizzes (newsletter of 10/25).

No class material for the regions is in Drive: her History folder and both of
its subfolders were listed to the end, and full-text searches for the region
names found nothing but the Unit 5 maps guide. So this is built from the
standard five-region map (Northeast, Southeast, Midwest, Southwest, West) and
EVERY card and question is flagged from:'added'. Each parentNote says so, and
names the one real risk: schools draw the borders differently, Maryland and
Delaware above all.

The newsletter says Regions 3 is on Tuesday 10/27 and that the first two
regions quizzes are done. It does not say which region is third, so all five
ship; numbering follows the usual teaching order, which is a guess, and the
parentNote says that too.

Every capital, abbreviation and region list lives in REGIONS below and every
question is generated from it, so a fact is stated once. The capital traps are
the point: a state's biggest city is offered as a wrong option wherever there
is one (Albany, not New York City; Springfield, not Chicago)."""
import json, io, os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from unit_common import card, q, build, REPO

R = random.Random(1025)

# state: (capital, abbreviation, biggest-city trap or None, a hook or None)
REGIONS = [
 ('Northeast', 'The Northeast', [
  ('Maine', 'Augusta', 'ME', 'Portland', 'The most northeastern state of all, famous for lobster and rocky coast.'),
  ('New Hampshire', 'Concord', 'NH', 'Manchester', None),
  ('Vermont', 'Montpelier', 'VT', 'Burlington', 'Vermont is known for maple syrup.'),
  ('Massachusetts', 'Boston', 'MA', None, 'Here the capital IS the biggest city.'),
  ('Rhode Island', 'Providence', 'RI', None, 'The smallest state in the whole country.'),
  ('Connecticut', 'Hartford', 'CT', 'Bridgeport', None),
  ('New York', 'Albany', 'NY', 'New York City', 'New York City is the biggest city in the country, but it is not the capital.'),
  ('New Jersey', 'Trenton', 'NJ', 'Newark', None),
  ('Pennsylvania', 'Harrisburg', 'PA', 'Philadelphia', 'Philadelphia, home of the Liberty Bell, is bigger, but Harrisburg is the capital.'),
  ('Delaware', 'Dover', 'DE', 'Wilmington', 'The first state to approve the Constitution.'),
  ('Maryland', 'Annapolis', 'MD', 'Baltimore', None),
 ], [
  ('Cold, snowy winters and bright fall leaves', 'Hot desert summers with cactus', 'Flat prairie farmland as far as you can see', 'Warm winters and tropical swamps'),
  ('Niagara Falls', 'The Grand Canyon', 'Mount Rushmore', 'The Everglades'),
 ]),
 ('Southeast', 'The Southeast', [
  ('West Virginia', 'Charleston', 'WV', None, 'Called the Mountain State: it sits in the Appalachians.'),
  ('Virginia', 'Richmond', 'VA', 'Virginia Beach', None),
  ('Kentucky', 'Frankfort', 'KY', 'Louisville', None),
  ('Tennessee', 'Nashville', 'TN', None, 'Nashville is famous for country music.'),
  ('North Carolina', 'Raleigh', 'NC', 'Charlotte', None),
  ('South Carolina', 'Columbia', 'SC', None, None),
  ('Georgia', 'Atlanta', 'GA', None, 'Georgia is known for peaches.'),
  ('Florida', 'Tallahassee', 'FL', 'Jacksonville', 'Miami and Orlando are famous, but Tallahassee is the capital.'),
  ('Alabama', 'Montgomery', 'AL', None, None),
  ('Mississippi', 'Jackson', 'MS', None, 'The state is named for the river along its western side.'),
  ('Arkansas', 'Little Rock', 'AR', None, None),
  ('Louisiana', 'Baton Rouge', 'LA', 'New Orleans', 'New Orleans is the famous one; Baton Rouge is the capital.'),
 ], [
  ('Warm, humid summers and hurricanes', 'Long, freezing winters with deep snow', 'Dry desert with very little rain', 'Glaciers and snow-capped volcanoes'),
  ('The Everglades', 'The Great Lakes', 'The Rocky Mountains', 'Niagara Falls'),
 ]),
 ('Midwest', 'The Midwest', [
  ('Ohio', 'Columbus', 'OH', None, None),
  ('Indiana', 'Indianapolis', 'IN', None, 'The capital has the state in its name: Indiana + polis, Greek for city.'),
  ('Illinois', 'Springfield', 'IL', 'Chicago', 'Chicago is the giant city, but Springfield is the capital.'),
  ('Michigan', 'Lansing', 'MI', 'Detroit', 'Michigan is shaped like a mitten, with the Great Lakes all around it.'),
  ('Wisconsin', 'Madison', 'WI', 'Milwaukee', 'Wisconsin is known for cheese.'),
  ('Minnesota', 'Saint Paul', 'MN', 'Minneapolis', 'Saint Paul and Minneapolis sit side by side: the Twin Cities.'),
  ('Iowa', 'Des Moines', 'IA', None, None),
  ('Missouri', 'Jefferson City', 'MO', 'Kansas City', 'The Gateway Arch is in St. Louis, Missouri.'),
  ('Kansas', 'Topeka', 'KS', 'Wichita', None),
  ('Nebraska', 'Lincoln', 'NE', 'Omaha', None),
  ('South Dakota', 'Pierre', 'SD', 'Sioux Falls', 'Mount Rushmore is in South Dakota.'),
  ('North Dakota', 'Bismarck', 'ND', 'Fargo', None),
 ], [
  ('Flat plains and farms that grow corn and wheat', 'Tall red-rock canyons and desert', 'Sandy beaches and palm trees all year', 'Rainforests and volcanoes'),
  ('The Great Lakes', 'The Grand Canyon', 'The Everglades', 'The Golden Gate Bridge'),
 ]),
 ('Southwest', 'The Southwest', [
  ('Arizona', 'Phoenix', 'AZ', None, 'Your own state. The Grand Canyon is here.'),
  ('New Mexico', 'Santa Fe', 'NM', 'Albuquerque', 'Santa Fe is one of the oldest capital cities in the country.'),
  ('Texas', 'Austin', 'TX', 'Houston', 'Houston and Dallas are bigger, but Austin is the capital.'),
  ('Oklahoma', 'Oklahoma City', 'OK', None, 'The capital has the state in its name.'),
 ], [
  ('Hot, dry deserts with cactus', 'Cold, snowy winters and fall leaves', 'Swamps and hurricanes along the coast', 'Glaciers and long, dark winters'),
  ('The Grand Canyon', 'Niagara Falls', 'The Great Lakes', 'The Everglades'),
 ]),
 ('West', 'The West', [
  ('Colorado', 'Denver', 'CO', None, 'Denver is the Mile High City: a mile above sea level, at the edge of the Rocky Mountains.'),
  ('Wyoming', 'Cheyenne', 'WY', None, 'Most of Yellowstone National Park is in Wyoming.'),
  ('Montana', 'Helena', 'MT', 'Billings', None),
  ('Idaho', 'Boise', 'ID', None, 'Idaho is known for potatoes.'),
  ('Washington', 'Olympia', 'WA', 'Seattle', 'Seattle is the big city; Olympia is the capital. Not the same as Washington, D.C.'),
  ('Oregon', 'Salem', 'OR', 'Portland', None),
  ('Utah', 'Salt Lake City', 'UT', None, 'The capital is named for the Great Salt Lake beside it.'),
  ('Nevada', 'Carson City', 'NV', 'Las Vegas', 'Las Vegas is famous, but Carson City is the capital.'),
  ('California', 'Sacramento', 'CA', 'Los Angeles', 'Los Angeles is the biggest city; Sacramento is the capital.'),
  ('Alaska', 'Juneau', 'AK', 'Anchorage', 'The biggest state of all, far to the northwest.'),
  ('Hawaii', 'Honolulu', 'HI', None, 'The only state made of islands, out in the Pacific Ocean.'),
 ], [
  ('Tall mountains and a long Pacific coast', 'Flat prairie farmland with few hills', 'Swamps, bayous and hurricane season', 'Huge lakes and long, snowy winters'),
  ('The Rocky Mountains', 'The Great Lakes', 'The Everglades', 'Niagara Falls'),
 ]),
]
NAMES = [r[0] for r in REGIONS]
ALL = {s[0]: (rg[0],) + s[1:] for rg in REGIONS for s in rg[2]}
assert len(ALL) == 50, len(ALL)
assert sorted(len(r[2]) for r in REGIONS) == [4, 11, 11, 12, 12]
CAPS = {v[1] for v in ALL.values()}
# a trap must never itself be a state capital, or a "wrong" option is right somewhere
for st, v in ALL.items():
    assert v[3] is None or v[3] not in CAPS, (st, v[3])

def others(pool, k, avoid, like=None):
    p = [x for x in pool if x not in avoid]
    if like:
        # draw from the names closest in length, so a two-word answer is not
        # the only two-word option on the list
        p.sort(key=lambda x: abs(len(x) - len(like)))
        p = p[:max(k + 4, 8)]
    return R.sample(p, k)

TWINS = {'South Carolina': 'North Carolina', 'North Carolina': 'South Carolina',
         'North Dakota': 'South Dakota', 'South Dakota': 'North Dakota',
         'Virginia': 'West Virginia', 'West Virginia': 'Virginia'}

def build_region(i, reg):
    name, label, states, feats = reg
    C, Q = [], []
    roster = ', '.join(s[0] for s in states)
    card(C, label + ' — the states',
         '**%d states: %s.**\n• Say them in order around the map until it feels like a list you know, not a list you read.' % (len(states), roster),
         hint='Count them on your fingers: %d.' % len(states), frm='added')
    if name == 'Northeast':
        card(C, 'Washington, D.C.',
             '**The capital of the whole country, and NOT a state.**\n• It sits between Maryland and Virginia.\n• D.C. stands for District of Columbia.',
             hint='A district, not a state: that is what the D stands for.', frm='added')
    for st, cap, ab, trap, hook in states:
        d = '**Capital: %s.**\n• Abbreviation: %s' % (cap, ab)
        if trap: d += '\n• Not %s, even though %s is bigger.' % (trap, trap)
        card(C, st, d, hint=hook, frm='added')
    card(C, label + ' — what it is like',
         '**%s.**\n• Famous place: %s.' % (feats[0][0], feats[1][0]), frm='added')

    # 1. which state is in this region (x2)
    pick = R.sample(states, 2)
    for s in pick:
        wrong = others([k for k, v in ALL.items() if v[0] != name], 3, [], like=s[0])
        opts = [s[0]] + wrong
        q(Q, 1, 'Which of these states is in the %s region?' % name, opts, 0,
          'Picture the %s on the map, then look for the one state that sits inside it.' % name,
          ['The %s region has %d states.' % (name, len(states)),
           'Check each option: which region is it in?',
           ', '.join('%s is in the %s' % (w, ALL[w][0]) for w in wrong) + '.',
           'So the answer is %s.' % s[0]],
          '**%s is in the %s.** The other three are each in a different region.' % (s[0], name),
          'Learn the region list as one group, the way the card says it.', frm='added')
    # 2. capitals (traps first)
    trapped = [s for s in states if s[3]]
    plain = [s for s in states if not s[3]]
    cap_qs = (trapped + plain)[:6 if len(states) > 4 else 4]
    reg_caps = [s[1] for s in states]
    for st, cap, ab, trap, hook in cap_qs:
        wrong = []
        if trap: wrong.append(trap)
        # wrong capitals come from the SAME region first, so the question asks
        # which of this region's capitals, not which name sounds far away
        near = [c for c in reg_caps if c != cap and c not in wrong]
        far = [v[1] for k, v in ALL.items() if v[0] != name]
        take = min(len(near), 3 - len(wrong))
        wrong += R.sample(near, take)
        wrong += others(far, 3 - len(wrong), [cap] + wrong)
        opts = [cap] + wrong
        q(Q, 1 if not trap else 2, 'What is the capital of %s?' % st, opts, 0,
          hook if (hook and cap not in hook and (not trap or trap not in hook)) else 'The capital is where the state government meets, and it is not always the biggest city.',
          ['A capital is where the state\'s government meets.',
           ('%s is the biggest city, but that does not make it the capital.' % trap) if trap else 'Some of these are capitals of other states.',
           'The capital of %s is %s.' % (st, cap)],
          '**%s.**%s' % (cap, (' %s is bigger, which is exactly why it is the trap.' % trap) if trap else ''),
          'When a famous city is on the list, ask yourself: biggest, or capital?', frm='added')
    # 3. capital -> state (x2)
    for st, cap, ab, trap, hook in R.sample(states, 2):
        wrong = [TWINS[st]] if st in TWINS else []
        wrong += others([s[0] for s in states], min(3, len(states) - 1) - len(wrong), [st] + wrong, like=st)
        if len(wrong) < 3: wrong += others(list(ALL), 3 - len(wrong), [st] + wrong)
        q(Q, 2, '%s is a state capital. Which state is it the capital of?' % cap, [st] + wrong, 0,
          'Run through the %s states and their capitals.' % name,
          ['%s is in the %s region.' % (cap, name),
           'Match it to its state.',
           '%s is the capital of %s.' % (cap, st)],
          '**%s.** Its capital is %s.' % (st, cap),
          'Practise capitals in both directions: state to capital, and capital to state.', frm='added')
    # 4. state -> region (x2)
    for st, *_ in R.sample(states, 2):
        wrong = others([n for n in NAMES if n != name], 3, [])
        q(Q, 2, 'Which region is %s in?' % st, [name] + wrong, 0,
          'Find %s on the map, then think about which group it belongs to.' % st,
          ['There are five regions: Northeast, Southeast, Midwest, Southwest and West.',
           'Look at where %s sits on the map.' % st,
           '%s is in the %s.' % (st, name)],
          '**The %s.**' % name, 'Region first, then the state: it narrows the map fast.', frm='added')
    # 5. what the region is like / a famous place
    for k, f in enumerate(feats):
        stem = ('Which description fits the %s region best?' if k == 0 else 'Which famous place is in the %s region?') % name
        q(Q, 2, stem, list(f), 0,
          'Think about the weather and land where these states are.',
          ['Each option describes a different part of the country.',
           'Picture the %s: %s.' % (name, ', '.join(s[0] for s in states[:3])),
           'The one that fits is: %s.' % f[0]],
          '**%s.**' % f[0], 'Tie each region to one picture in your head.', frm='added')
    # 6. abbreviation
    st, cap, ab, *_ = R.choice(states)
    same = [v[2] for v in ALL.values() if v[2][0] == ab[0] and v[2] != ab]
    abwrong = R.sample(same, min(3, len(same)))
    abwrong += others([v[2] for v in ALL.values()], 3 - len(abwrong), [ab] + abwrong)
    q(Q, 2, 'What is the two-letter abbreviation for %s?' % st, [ab] + abwrong, 0,
      'Abbreviations are always two capital letters.',
      ['Each state has its own two-letter abbreviation.',
       'Several states start with the same letter, so check the second letter too.',
       'The abbreviation for %s is %s.' % (st, ab)],
      '**%s.**' % ab, 'States that share a first letter are the ones worth drilling.', frm='added')
    # 7. two states, same region (analyze)
    a, b = R.sample(states, 2)
    outs = [k for k, v in ALL.items() if v[0] != name]
    o1, o2, o3, o4 = R.sample(outs, 4)
    opts = ['%s and %s' % (a[0], b[0]), '%s and %s' % (a[0], o1), '%s and %s' % (o2, b[0]), '%s and %s' % (o3, o4)]
    q(Q, 3, 'Which pair of states are BOTH in the %s region?' % name, opts, 0,
      'Both halves of the pair have to be in the region, not just one.',
      ['Check every state in every pair.',
       '%s is in the %s, and %s is in the %s.' % (o1, ALL[o1][0], o2, ALL[o2][0]),
       '%s and %s are both in the %s.' % (a[0], b[0], name)],
      '**%s and %s.** Two of the other pairs have one state right and one wrong.' % (a[0], b[0]),
      'A half-right pair is still wrong, so check both names.', frm='added')
    return C, Q

for i, reg in enumerate(REGIONS):
    name, label = reg[0], reg[1]
    C, Q = build_region(i, reg)
    uid = 'unit-hist-reg-%d' % (i + 1)
    path = 'content/history-regions-%d.json' % (i + 1)
    note = ('Built for the Regions quizzes in the 4th Grade Newsletter of 10/25. No class material for the regions '
            'was in Drive, so every card and question here is a study suggestion from the standard five-region map, '
            'not from her class. Schools draw the borders differently (Maryland and Delaware are the usual ones to '
            'move), so check this region\'s state list against her notes. The newsletter does not say which region '
            'is "Regions 3"; the numbering here is the usual teaching order and may not match hers. Capitals and '
            'abbreviations are included in case the quiz asks for them.')
    build('wayfinder', C, Q, uid, 'U.S. Regions · %d %s' % (i + 1, label), 'history',
          'The %d states of the %s region, their capitals and abbreviations, and what the region is like.' % (len(reg[2]), name),
          'Knowing the regions turns a map of fifty states into five groups you can actually remember.',
          [('Name every state in the %s region' % name, 'added'),
           ('Match each state to its capital, and each capital to its state', 'added'),
           ('Describe what the %s is like and name one famous place there' % name, 'added')],
          note,
          ('Say the state list out loud once, then do a round. Capitals are the part that needs repeating.', 10),
          path, 'Standard five-region map (no class material in Drive)',
          'Study suggestion: standard U.S. regions', offset_hours=3, round_=10)
    p = os.path.join(REPO, path)
    d = json.load(io.open(p, encoding='utf-8'))
    u = d['records'][uid]
    u['summary']['from'] = 'added'
    u['quarter'] = 2
    u['prep'] = True
    u['libv'] = 1
    io.open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
