# -*- coding: utf-8 -*-
# Wordly Wise · Lesson 3 — question bank rebuilt to her real test's format.
# Same five sections as Lessons 4 and 5; see build_ww504_test.py.
#
# This lesson's five kind:'spell' questions are KEPT and appended after the
# twenty. No section of her real paper tests spelling, so they do not earn a
# place in the five-section mix — but they are genuinely useful practice that
# already shipped, and removing them was not asked for. Flagged for Chris in
# the parentNote instead of decided silently.
import sys, os, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import build
from vocab_test_common import ctx, syn, fit, pos, assoc

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
old = json.load(io.open(os.path.join(REPO, 'content/wordly-wise-5-03.json'),
                        encoding='utf-8'))['records']['unit-ww503']
C = old['cards']
SPELL = [x for x in old['questions'] if x.get('kind') == 'spell']
assert len(SPELL) == 5, len(SPELL)
Q = []

# ---- Section 1: reading passage, context clues -----------------------------
ctx(Q, 2,
    'No one has seen a dodo since the 1680s. Sailors took the last of them '
    'from the island, and the bird is now extinct — there is nothing left of '
    'it but bones, drawings and a few written accounts.',
    'extinct',
    'How is the word "extinct" used in this passage?',
    ['To say that no members of the species are left alive anywhere',
     'To say that the species is rare but can still be found on the island',
     'To explain that the bird was hunted but later recovered in number',
     'To explain that the bird was never properly recorded by scientists'], 0,
    'Look at what the passage says is left of the bird.',
    ['The last of them were taken from the island in the 1680s.',
     'What remains is bones, drawings and written accounts — no living birds.',
     'That rules out rare-but-still-there, and it rules out recovering.',
     'Nothing left alive anywhere is what extinct means.'],
    '**To say that no members of the species are left alive anywhere.** The '
    'list of what survives is the clue: bones, drawings and accounts, but no '
    'birds.',
    '"Rare" is the tempting answer because rare things are also hard to find. '
    'Extinct is stronger than rare — it means none at all.')

ctx(Q, 2,
    'The chicks hatched a full three weeks premature. Their eyes were still '
    'sealed, they had almost no down on them, and the keepers had to move '
    'every one of them straight into a warm box.',
    'premature',
    'What do the context clues tell you "premature" means?',
    ['Happening earlier than it should have done',
     'Happening later than everyone had expected',
     'Happening exactly on the day that was predicted',
     'Happening more slowly than is usual for the species'], 0,
    'Three details describe the chicks. Are they ready or not ready?',
    ['The chicks hatch three weeks before they were due.',
     'Sealed eyes and almost no down are signs of not being ready yet.',
     'Needing a warm box straight away confirms it.',
     'Arriving before the proper time is what premature means.'],
    '**Happening earlier than it should have done.** Every detail after the '
    'word — sealed eyes, no down, straight into a warm box — is a sign of '
    'something that arrived before it was ready.',
    'The number in the sentence does a lot of work here. "Three weeks" plus '
    'the state of the chicks tells you which direction in time to go.')

ctx(Q, 3,
    'By four o\'clock the fog had obscured the far bank completely. The '
    'watchers knew the herd was still out there, because they could hear it, '
    'but there was nothing at all to see.',
    'obscured',
    'How is the word "obscured" used here?',
    ['To say the fog hid the far bank from view',
     'To say the fog made the far bank easier to pick out',
     'To say the fog had drifted away from the river',
     'To say the far bank had been washed away by the water'], 0,
    'The passage tells you what they could still do, and what they could not.',
    ['The watchers can hear the herd, so the herd is still there.',
     'There is "nothing at all to see", so the problem is seeing, not the herd.',
     'The fog is what came between them and the bank.',
     'Covering something up so it cannot be seen is what obscured means.'],
    '**To say the fog hid the far bank from view.** The passage separates the '
    'two senses on purpose: they can still HEAR the herd, so what changed is '
    'only what can be seen.',
    'When a passage tells you one sense still works and another does not, it '
    'is usually pointing straight at the word it wants you to work out.')

ctx(Q, 2,
    'The eruption itself lasted under a minute. For the whole duration of it '
    'the ground shook hard enough to rattle the instruments, and then, just '
    'as suddenly, everything went quiet again.',
    'duration',
    'How is the word "duration" used in this passage?',
    ['To mean the length of time the eruption went on for',
     'To mean the loudness the eruption reached at its peak',
     'To mean the distance the shaking could be felt across',
     'To mean the damage the eruption left behind afterwards'], 0,
    'Look at what the sentence before it measures.',
    ['The first sentence measures the eruption in time: under a minute.',
     '"For the whole duration of it" then covers that same stretch of time.',
     'The passage says nothing about loudness, distance or damage.',
     'So duration means the length of time something lasts.'],
    '**To mean the length of time the eruption went on for.** The sentence '
    'before it has already given you the measurement — under a minute — and '
    '"the whole duration" covers exactly that.',
    'Look at the sentence BEFORE the word as well as the one after it. Here '
    'the clue arrives first.')

# ---- Section 2: synonyms and antonyms --------------------------------------
syn(Q, 1, 'gigantic', True,
    ['enormous', 'tiny', 'ancient', 'noisy'], 0,
    'Think about the word hiding inside it.',
    ['Gigantic means very large — like a giant.',
     'Tiny is its opposite, so it is out.',
     'Ancient is about age and noisy is about sound; neither is about size.',
     'Enormous means the same thing: very large indeed.'],
    '**Enormous.** Both mean very large. "Tiny" is the word\'s own opposite, '
    'which is what makes it the option to read twice.',
    'The word "giant" is sitting inside "gigantic". Broken-up words often '
    'carry their meaning on the surface like that.')

syn(Q, 2, 'puny', False,
    ['mighty', 'feeble', 'quiet', 'clever'], 0,
    'Which of these could describe a weightlifter?',
    ['Puny means weak.',
     'Feeble also means weak, so it is a synonym rather than the opposite.',
     'Quiet and clever describe other things entirely, not strength.',
     'Mighty means very strong, which is the exact reverse.'],
    '**Mighty.** Puny is weak and mighty is strong — the two ends of the same '
    'measure.',
    '"Feeble" is in the list because it is a synonym. On an OPPOSITE '
    'question, find the synonym and cross it off first.')

syn(Q, 1, 'comprehend', True,
    ['understand', 'confuse', 'ignore', 'announce'], 0,
    'What are you doing when a hard idea finally clicks?',
    ['To comprehend something is to understand it.',
     'Confuse is the reverse — it makes understanding harder.',
     'Ignore is refusing to attend to something, and announce is saying it out loud.',
     'Understand is the direct match.'],
    '**Understand.** They mean the same thing. "Confuse" is the opposite, and '
    '"ignore" is the near-miss — you can ignore something you understand '
    'perfectly well.',
    'Two of the wrong options here are about ATTENTION rather than about '
    'understanding. Sorting options into groups makes the real match stand out.')

syn(Q, 2, 'ferocious', False,
    ['gentle', 'savage', 'enormous', 'rapid'], 0,
    'Which word would you use about an animal that has never hurt anyone?',
    ['Ferocious means savage or fierce.',
     '"Savage" is the definition itself, so it is a synonym.',
     'Enormous is about size and rapid is about speed; a creature can be either and still be fierce.',
     'Gentle is the exact reverse of fierce.'],
    '**Gentle.** Ferocious and gentle are opposite ways for a creature to '
    'behave. Size and speed are different measures altogether.',
    'Watch for an option that is simply the word\'s definition in disguise — '
    '"savage" is exactly that, and on an OPPOSITE question it is wrong.')

# ---- Section 3: sentence completion ----------------------------------------
fit(Q, 2, 'The museum preserved...',
    ['the skeleton in a sealed case so that the damp could not reach it.',
     'its doors at half past five and asked the last visitors to leave.',
     'a long way from the station, at the far end of the high street.',
     'that the new exhibition would open some time in the early spring.'], 0,
    'To preserve is to keep something from harm. Ask what could be harmed.',
    ['Preserving means saving something and keeping it from harm.',
     'A skeleton in a sealed case is being kept safe from the damp.',
     'Closing doors, standing far from a station and announcing an opening are all different actions.',
     'Only the sealed case is about protecting something.'],
    '**The skeleton in a sealed case so that the damp could not reach it.** '
    'The ending even names the harm being kept out, which is what preserving '
    'is for.',
    'A good sentence-completion answer usually names the REASON as well as '
    'the action. "So that the damp could not reach it" is the giveaway.')

fit(Q, 3, 'Walking back in the dark was the only option...',
    ['left to them, because the last bus had gone an hour earlier.',
     'that the weather had been steadily improving throughout the afternoon.',
     'which they folded up carefully and put away inside the rucksack.',
     'and the museum would be closed again by the following Tuesday.'], 0,
    'An option is a choice. What makes something the ONLY choice?',
    ['An option is a choice, or a thing available as a choice.',
     'Saying it was the only one means every other choice had gone.',
     'The ending needs to explain why nothing else was available.',
     'The last bus having gone is exactly that explanation.'],
    '**Left to them, because the last bus had gone an hour earlier.** Calling '
    'something the only option is a claim that needs explaining, and that '
    'ending explains it.',
    'When a sentence says "the only", look for the ending that says WHY the '
    'alternatives are gone. The other three never mention a choice at all.')

fit(Q, 2, 'Only two of the seedlings survived...',
    ['the frost, and both of those were the ones closest to the wall.',
     'a bright yellow color that they kept for the rest of the summer.',
     'the gardener carefully into the larger pots on the upper shelf.',
     'because the greenhouse had been built in the previous century.'], 0,
    'To survive is to stay alive where there was a real chance of dying.',
    ['Surviving means staying alive where dying was possible.',
     'So the ending has to name the danger they came through.',
     'A color, a gardener and the age of a greenhouse are not dangers.',
     'The frost is the danger, and the wall explains why those two made it.'],
    '**The frost, and both of those were the ones closest to the wall.** '
    'Surviving needs something to survive, and the frost is the only threat '
    'on offer.',
    'The word "survive" always implies a danger. If an ending does not '
    'contain one, it is not the ending you want.')

fit(Q, 2, 'It was evident from the tracks...',
    ['that a large animal had crossed the mud some time that morning.',
     'which the ranger had photographed from three different angles.',
     'before the rain began to fall heavily across the whole valley.',
     'and the visitor centre would not be opening again until Friday.'], 0,
    'Evident means easy to see and understand — so something follows from it.',
    ['If something is evident, there is a fact you can read straight off.',
     'The tracks are the thing being read.',
     'The ending therefore has to say what the tracks made clear.',
     'That a large animal crossed that morning is exactly such a fact.'],
    '**That a large animal had crossed the mud some time that morning.** '
    '"It was evident from X…" is a sentence waiting to be told WHAT was '
    'evident, and only one ending supplies it.',
    'Look at the grammar the opening sets up. "It was evident from the '
    'tracks…" almost demands the word "that" next.')

# ---- Section 4: parts of speech ---------------------------------------------
pos(Q, 1, 'A wolf is a carnivore and will not touch the grain.',
    'carnivore', 'noun',
    'Try putting "a" in front of the word.',
    ['Ask what job the word is doing here.',
     'It reads "a carnivore" — the sentence is naming what a wolf IS.',
     'Only a noun takes "a" in front of it like that.',
     'So "carnivore" is a noun.'],
    '**Noun.** The sentence names what a wolf is, and "a" sits in front of '
    'the word.',
    'The test for a noun: can you put "a", "an" or "the" in front of it? If '
    'you can, it is doing a noun\'s job in that sentence.')

pos(Q, 1, 'The ferocious storm tore the roof from the barn.',
    'ferocious', 'adjective',
    'Ask which word it is telling you about.',
    ['Find the nouns: "storm", "roof" and "barn".',
     'The word sits between "The" and "storm", telling you what kind of storm.',
     'Describing a noun is an adjective\'s job.',
     'So "ferocious" is an adjective here.'],
    '**Adjective.** It tells you what kind of storm it was — it describes '
    '"storm".',
    'A word wedged between "the" and a noun is nearly always describing that '
    'noun.')

pos(Q, 2, 'She could not comprehend a word of the instructions.',
    'comprehend', 'verb',
    'Ask what she could not DO.',
    ['The sentence is about something she was unable to do.',
     '"Could not" in front of a word is a strong sign a verb follows it.',
     'The word also takes an object — "a word of the instructions".',
     'So "comprehend" is a verb.'],
    '**Verb.** It is the action she could not perform, and "could not" in '
    'front of it can only be followed by a verb.',
    '"Can", "could", "will" and "must" are always followed by a verb. Spotting '
    'one of those is a shortcut to the answer.')

pos(Q, 3, 'The owl spotted its prey in the long grass below.',
    'prey', 'noun',
    'The word has "its" in front of it. What does that settle?',
    ['"Prey" really can be a verb — owls prey on mice.',
     'Here it reads "its prey", with a possessive word in front of it.',
     'A word in that slot is a thing being owned or sought, not an action.',
     'So in THIS sentence it is a noun.'],
    '**Noun.** "Its prey" names the animal the owl is hunting. The same word '
    'is a verb in other sentences — an owl preys on mice — which is exactly '
    'why the sentence decides and not the word.',
    'This is the trap that costs the most marks on a real paper. "My", "its", '
    '"their" in front of a word all point to a noun.')

# ---- Section 5: word association --------------------------------------------
assoc(Q, 1, ['sharp teeth', 'strong claws', 'a diet of meat'],
      ['carnivore', 'ancestor', 'option', 'duration'], 0,
      'All three are things you would notice about the same kind of animal.',
      ['Sharp teeth and strong claws are tools for catching and tearing.',
       'A diet of meat says what those tools are for.',
       'The three together describe one kind of animal.',
       'A flesh-eating animal is a carnivore.'],
      '**Carnivore.** Teeth, claws and a meat diet all belong to an animal '
      'that lives by eating other animals.',
      'Work out what the three things have in common before you read the '
      'options — the answer is usually obvious once you have named it yourself.')

assoc(Q, 2, ['a jar of jam', 'a museum case', 'a freezer'],
      ['preserve', 'comprehend', 'survive', 'obscure'], 0,
      'Ask what all three are FOR, not what they are.',
      ['A jar, a case and a freezer are three very different objects.',
       'Each one is designed to stop what is inside it from spoiling.',
       'Jam, an exhibit and frozen food are all being kept from harm.',
       'Keeping something from harm is to preserve it.'],
      '**Preserve.** All three exist to keep what is inside them safe from '
      'spoiling.',
      '"Survive" is the near miss worth noticing: the thing inside does '
      'survive, but the jar is what PRESERVES it. Match the word to the '
      'container, not to the contents.')

assoc(Q, 2, ['a family tree', 'a great-great-grandmother', 'a faded photograph'],
      ['ancestor', 'prey', 'option', 'carnivore'], 0,
      'All three point back along the same line.',
      ['A family tree maps who came before whom.',
       'A great-great-grandmother is four generations back.',
       'A faded photograph is a record of someone long ago.',
       'A person you are descended from is an ancestor.'],
      '**Ancestor.** Each one is a way of reaching back to the people you are '
      'descended from.',
      'The word "faded" and the string of "great"s are both doing the same '
      'job: telling you how far back to look.')

assoc(Q, 3, ['the dodo', 'the woolly mammoth', 'the sabre-toothed cat'],
      ['extinct', 'ferocious', 'gigantic', 'puny'], 0,
      'Two of these were fierce and two were huge. What do all THREE share?',
      ['The dodo was a flightless bird, not fierce and not huge.',
       'The mammoth was enormous; the sabre-toothed cat was a fierce hunter.',
       'So neither "ferocious" nor "gigantic" covers all three.',
       'What all three share is that none of them is alive today.'],
      '**Extinct.** The only thing true of all three is that no living '
      'member of any of them remains.',
      'When two options each fit SOME of the three, neither is the answer. '
      'The right word has to cover every one of them.')

Q.extend(SPELL)
for i, x in enumerate(Q):
    x['id'] = 'q%d' % i

build('wayfinder', C, Q, 'unit-ww503', old['title'], 'english',
      old['summary']['text'], old['why']['text'],
      [(o['text'], o['from']) for o in old['objectives']],
      'Rebuilt to the five sections of her real vocabulary test — context '
      'clues from a passage, synonyms and antonyms, sentence completion, '
      'parts of speech, and word association — four questions each. See the '
      'Lesson 4 note for why each context question carries its own short '
      'passage rather than five sharing one long one. Two words here are '
      'worth a grown-up\'s eye because they are the ones a paper will catch '
      'her on: "prey" is a noun in "its prey" and a verb in "preys on mice", '
      'and "obscure" means to cover up rather than merely to be unclear. One '
      'judgement call to flag: this lesson\'s five spelling questions are '
      'KEPT and sit after the twenty, even though no section of her real '
      'paper tests spelling. They are useful and they already shipped, so '
      'removing them was not something to decide quietly — say the word and '
      'they can go, which would bring this lesson into line with Lessons 4 '
      'and 5 at twenty questions. The cards are unchanged.',
      ('Five shapes, four questions each, then the five spellings. The '
       'parts-of-speech ones repay going slowly: "prey" changes its job '
       'depending on the sentence it is in.', 18),
      'content/wordly-wise-5-03.json',
      old.get('srcName', 'Wordly Wise Book 5, Lesson 3'),
      old.get('source', 'Wordly Wise Book 5'),
      offset_hours=3)

p = os.path.join(REPO, 'content/wordly-wise-5-03.json')
j = json.load(io.open(p, encoding='utf-8'))
j['records']['unit-ww503']['libv'] = 2   # shipped with none; pinned, not incremented
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + libv %d' % j['records']['unit-ww503']['libv'])
