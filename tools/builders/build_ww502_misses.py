# -*- coding: utf-8 -*-
# Wordly Wise · Lesson 2 — six questions APPENDED for what her real Unit 2
# Vocabulary Test actually caught (20/25, Drive 2026-09-20).
#
# Her five misses are two ideas, not five:
#   · cultivate — three of the five touched it. She chose "merge" as its
#     synonym, missed its figurative sense in a sentence completion, and then
#     chose "cultivate" again for the juice/oil/syrup association that wanted
#     "extract".
#   · parts of speech in context — "export" in "an important export" (she put
#     adjective) and "craving" in "had a craving" (she put verb). Both nouns.
#
# The lesson ALREADY teaches cultivate's figurative sense (q7) and extract as
# a noun (q10), so the material was not the gap. The gap is the form: q3 and
# q10 ask "In which sentence is X used as a VERB?", which is a hunt across
# four sentences, where the paper asks "What part of speech is X in THIS
# sentence?" — parsing one slot. Those are different tasks, and only the
# second one is what she sat.
#
# Appended, never renumbered: this unit has been tested on, so every existing
# question id keeps its meaning and anything already attached stays attached.
# New ids are minted from max(existing)+1, never from len() (v149).
import sys, os, io, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import q
from vocab_test_common import pos, assoc, syn, fit

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(REPO, 'content/wordly-wise-5-02.json')
doc = json.load(io.open(P, encoding='utf-8'))
u = doc['records']['unit-ww502']
# Idempotent: drop anything this script added on a previous run before
# appending, so re-running cannot stack six more questions onto the unit.
BASE = 15
u['questions'] = [x for x in u['questions']
                  if int(re.sub(r'\D', '', x['id'])) < BASE]
start = BASE
NQ = []

# Two PRE-EXISTING length-bias outliers, fixed while this unit is re-drafting
# anyway: q1's answer ran 157% longer than the next longest option and q7's
# 69%, either of which she could pick without reading the question. Fixed by
# giving the distractors real substance, never by trimming the answer into
# something vaguer (v185).
_fix = {x['id']: x for x in u['questions']}
_fix['q1']['opts'] = ['Easily broken or snapped in two',
                      'Lacking a strong flavor or seasoning',
                      'Not irritating or exciting; deliberately calm',
                      'Hot and moist, the way tropical air is']
_fix['q1']['ans'] = 2
_fix['q7']['opts'] = ['Prepared land ready for planting crops',
                      'Helped something grow by steady attention',
                      'Harvested a crop at the end of the season',
                      'Removed something with a great deal of effort']
_fix['q7']['ans'] = 1

# --- parts of speech, in the paper's own form -------------------------------
pos(NQ, 2, 'Coffee is Ethiopia\'s largest export.', 'export', 'noun',
    'The word has "Ethiopia\'s largest" in front of it. What does that settle?',
    ['"Export" really can be a verb — a country exports coffee.',
     'Here it sits after "Ethiopia\'s" and after "largest", which describes it.',
     'A word being owned and described like that is a thing, not an action.',
     'So in THIS sentence "export" is a noun.'],
    '**Noun.** It names the thing Ethiopia sends abroad. The very same word is '
    'a verb in other sentences — Ethiopia exports coffee — which is exactly '
    'why the sentence decides and not the word.',
    'A possessive ("Ethiopia\'s") and an adjective ("largest") in front of a '
    'word both point the same way: it is doing a noun\'s job here.')

pos(NQ, 2, 'After the long walk she had a craving for something salty.',
    'craving', 'noun',
    'Ask what she HAD. The thing you had is a noun.',
    ['The verb in this sentence is "had" — that is the action.',
     'What she had was "a craving", with "a" in front of it.',
     'A word cannot be the action when another word is already doing that job.',
     'So "craving" is a noun here.'],
    '**Noun.** The action in the sentence is "had", and what she had was a '
    'craving. Once a sentence already has its verb, the word after "a" is a '
    'thing, not a second action.',
    'Find the verb FIRST. If the sentence already has one, the word you are '
    'asked about is very unlikely to be another.')

pos(NQ, 1, 'They cultivate rice on the terraces above the village.',
    'cultivate', 'verb',
    'Ask what "they" DO.',
    ['The sentence is about something people do.',
     '"They" are doing it, and the rice is what it is done to.',
     'A word that takes an object like that is a verb.',
     'So "cultivate" is a verb here.'],
    '**Verb.** It is the action the villagers perform, and "rice" is what '
    'they perform it on.',
    'Swap the subject for "she" and see whether the word has to change — '
    '"she cultivates" — that change only happens to verbs.')

# --- cultivate, the word three of her five misses touched --------------------
syn(NQ, 2, 'cultivate', True,
    ['tend', 'merge', 'harvest', 'abandon'], 0,
    'Think about the months BEFORE anything is picked.',
    ['To cultivate is to prepare and work land so that things grow on it.',
     'Merge means to combine two things into one — a different idea entirely.',
     'Harvest is gathering the crop, which is what happens at the END of it.',
     'Abandon is leaving land to itself, the opposite of working it.',
     'Tend is the match: looking after something as it grows.'],
    '**Tend.** Cultivating is the long work of preparing ground and looking '
    'after what grows in it. "Harvest" is the closest wrong answer because it '
    'belongs to the same farm — but it is the last step, not the work itself.',
    '"Merge" is in this list on purpose. It shares no meaning with cultivate '
    'at all; the two only look alike as options if you are matching on feel '
    'rather than on meaning.')

fit(NQ, 3, 'Over three seasons the coach cultivated...',
    ['a habit of turning up early, until nobody needed reminding any more.',
     'the muddiest corner of the pitch with a roller and a bag of seed.',
     'her whistle twice to bring the players back in from the far goal.',
     'every match that season except the two that were rained off.'], 0,
    'Cultivate works on things that grow — and not all of them are plants.',
    ['Cultivating is growing something slowly, with steady care.',
     'It is used about plants, and also about things like habits and skills.',
     '"Over three seasons" tells you this is the slow, figurative sense.',
     'A habit that builds until nobody needs reminding is exactly that.'],
    '**A habit of turning up early, until nobody needed reminding any more.** '
    'Cultivating a habit is the figurative sense — growing something in '
    'people rather than in soil, slowly and on purpose.',
    'The pitch-and-seed ending is the literal sense and it is genuinely '
    'tempting. "Over three seasons" is the clue: that is too long for one '
    'afternoon with a roller.')

assoc(NQ, 2, ['olive oil', 'apple juice', 'vanilla essence'],
      ['extract', 'cultivate', 'consume', 'combine'], 0,
      'Ask how each of the three was GOT, not what it is.',
      ['Oil is pressed out of olives.',
       'Juice is squeezed out of apples.',
       'Vanilla essence is drawn out of vanilla pods.',
       'Every one of them is something taken out of something else — extracted.'],
      '**Extract.** Each of the three is a liquid that had to be taken out of '
      'a plant. That is what extracting is: removing something from what it '
      'was part of.',
      '"Cultivate" is the closest wrong answer, because olives, apples and '
      'vanilla are all grown. But growing them is a different step from '
      'getting the liquid out — the three things listed are the LIQUIDS.')

# Spread the six across the four slots rather than leaving five of them in A
# (the v167 all-answer-A trap). Same rotation _balance() uses, applied only to
# what this script adds — the existing fifteen are left exactly as they are.
for i, x in enumerate(NQ):
    x['id'] = 'q%d' % (start + i)
    want = i % len(x['opts'])
    if x['ans'] != want:
        x['opts'][x['ans']], x['opts'][want] = x['opts'][want], x['opts'][x['ans']]
        x['ans'] = want
u['questions'].extend(NQ)
u['libv'] = 2   # shipped with none; pinned so re-running is stable
u['updatedAt'] = int(__import__('time').time() * 1000) - 3 * 3600 * 1000
u['parentNote'] = {'from': 'added', 'text':
    'Six questions were added after her real Unit 2 Vocabulary Test came back '
    'at 20 out of 25. The five she missed are two ideas rather than five. '
    'Three of them touched "cultivate": she chose "merge" as its synonym, she '
    'missed its figurative sense in a sentence completion, and she then chose '
    '"cultivate" again for the juice-oil-syrup association that wanted '
    '"extract". The other two were parts of speech — "export" in "an '
    'important export" and "craving" in "had a craving", both nouns, marked '
    'as adjective and verb. Worth knowing: this lesson already taught '
    'cultivate\'s figurative sense and extract as a noun, so the material was '
    'not the gap. The form was. The existing questions ask "in which sentence '
    'is this word a verb?", which means hunting across four sentences; the '
    'paper asks "what part of speech is this word in THIS sentence?", which '
    'means parsing one slot. The three new parts-of-speech questions use the '
    'paper\'s form. Nothing was renumbered, so anything already attached to '
    'the older questions stays attached.'}
io.open(P, 'w', encoding='utf-8').write(json.dumps(doc, ensure_ascii=False, indent=1))
print('appended %d questions as %s..%s; libv %d; now %d total'
      % (len(NQ), NQ[0]['id'], NQ[-1]['id'], u['libv'], len(u['questions'])))
