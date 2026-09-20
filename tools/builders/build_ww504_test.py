# -*- coding: utf-8 -*-
# Wordly Wise · Lesson 4 — question bank rebuilt to her real test's format.
#
# The old bank was 20 questions and the first six were "What does accurate
# mean?", "What is a gale?", "What does depart mean?"… — bare recall, which is
# the one shape her actual Unit 2 Vocabulary Test never uses. This replaces it
# with the paper's own five sections, four questions each.
#
# The CARDS are untouched and reloaded from the shipped file: they are good,
# they carry the part of speech already, and re-minting them would detach
# anything already attached to them.
import sys, os, io, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import build
from vocab_test_common import ctx, syn, fit, pos, assoc

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, 'content/wordly-wise-5-04.json')
old = json.load(io.open(SRC, encoding='utf-8'))['records']['unit-ww504']
C = old['cards']
Q = []

# ---- Section 1: reading passage, context clues -----------------------------
ctx(Q, 2,
    'The lifeboat had hung on deck for thirty years, and it had deteriorated '
    'badly. Salt air had eaten through its ropes, the paint hung off in '
    'strips, and one plank was soft enough to push a thumb through.',
    'deteriorated',
    'How is the word "deteriorated" used in this passage?',
    ['To show that the boat had slowly fallen into worse and worse condition',
     'To show that the boat had been repainted and repaired several times',
     'To explain that the boat was built from unusually soft, light wood',
     'To explain that the boat had been moved below deck for safe storage'], 0,
    'Three details come straight after the word. What do they have in common?',
    ['The word is followed by three details: eaten ropes, peeling paint, a soft plank.',
     'Every one of them is a way the boat is worse than it used to be.',
     'None of them is about repairs, about materials, or about where it was kept.',
     'So "deteriorated" is telling you the boat fell into worse condition over time.'],
    '**To show that the boat had slowly fallen into worse and worse '
    'condition.** The three details right after the word are all examples of '
    'it — that list is the clue the passage gives you.',
    'When a word is followed by a list of examples, the examples ARE the '
    'definition. Read past the word before you decide what it means.')

ctx(Q, 2,
    'The forecast had promised a breeze. By midnight a gale was driving the '
    'rain flat across the deck, and it took two of the crew just to hold the '
    'wheel steady.',
    'gale',
    'What do the context clues tell you a "gale" is?',
    ['A very strong wind', 'A light and pleasant wind',
     'A thick bank of evening fog', 'A sudden drop in temperature'], 0,
    'The passage sets the word against another weather word on purpose.',
    ['The forecast promised a breeze, which is a light wind.',
     '"By midnight" signals that things had changed from what was promised.',
     'Rain driven flat, and two people needed on one wheel, both mean huge force.',
     'So a gale is a very strong wind — the opposite of the breeze promised.'],
    '**A very strong wind.** The passage deliberately sets "breeze" against '
    '"gale", then shows you the force: rain driven flat, and two people needed '
    'on a wheel one person normally holds.',
    'A contrast clue is as good as a definition. When a passage says what '
    'something was supposed to be, look for the word it is pushing against.')

ctx(Q, 3,
    'When the last climber reached the road, the waiting families broke into '
    'jubilation. Car horns went off, someone was crying, and a woman who had '
    'not slept in two days simply sat down and laughed.',
    'jubilation',
    'How is the word "jubilation" used here?',
    ['To name the great joy that broke out once the climbers were safe',
     'To name the worry the families felt during the long wait',
     'To describe how heavy the traffic on the road had become',
     'To describe how exhausted the families were by the third day'], 0,
    'Weigh all three reactions in the list, not just the strongest one.',
    ['Horns, crying and laughing all come straight after the word.',
     'They are all loud, outward reactions rather than private ones.',
     'The moment they happen is the moment the last climber arrives safe.',
     'So "jubilation" names the great joy that broke out at that moment.'],
    '**To name the great joy that broke out once the climbers were safe.** '
    'Crying sits in the middle of the list, which is the trap — here it is '
    'relief, and the horns and the laughter on either side of it say so.',
    'One item in a list can point the wrong way on its own. Weigh the whole '
    'list before you let a single word decide the answer for you.')

ctx(Q, 3,
    'For three days the island stayed a gray smudge on the horizon. Only on '
    'the fourth morning, with the sun behind them, could the crew make out '
    'trees and a thin pale line of beach.',
    'horizon',
    'What does this passage suggest about something on the horizon?',
    ['It is about as far off as a thing can be and still be seen',
     'It is close enough to be reached within an hour or so',
     'It is directly overhead, above the mast of the ship',
     'It is hidden from view completely until the weather clears'], 0,
    'Ask why the trees took another three days to appear.',
    ['At the horizon the island is only a gray smudge — no detail at all.',
     'Real detail, the trees and the beach, appears only on the fourth morning.',
     'So the horizon is the very limit of what the eye can pick out.',
     'It is not hidden — they can see it — and it is plainly not near.'],
    '**It is about as far off as a thing can be and still be seen.** The '
    'passage works by contrast: a smudge on day one, real detail only on day '
    'four, and three days of sailing in between.',
    '"Hidden completely" is the tempting answer, but they CAN see it — a '
    'smudge is still something. Answer from what the passage reports, not '
    'from what the word sounds like.')

# ---- Section 2: synonyms and antonyms --------------------------------------
syn(Q, 1, 'accurate', True,
    ['exact', 'careless', 'rapid', 'costly'], 0,
    'Think of a measurement you would trust down to the millimeter.',
    ['Accurate describes something with no mistakes in it.',
     'Careless is its opposite, so it cannot be the synonym.',
     'Rapid is about speed and costly is about price — neither is about being right.',
     'Exact means the same thing: correct, with nothing off.'],
    '**Exact.** Both mean free of error. "Careless" is the word\'s own '
    'opposite, which is exactly why it is the option worth pausing over.',
    'Check whether the question asked for SAME or OPPOSITE before you answer. '
    'The opposite is usually sitting right there among the choices.')

syn(Q, 1, 'depart', False,
    ['arrive', 'leave', 'steer', 'delay'], 0,
    'Picture the two boards hanging in an airport.',
    ['Depart means to go away from a place.',
     '"Leave" means the very same thing, so it cannot be the opposite.',
     'Steer is about direction and delay is about time — neither reverses it.',
     'Arrive is the true opposite: coming in rather than going out.'],
    '**Arrive.** Departures and arrivals are the two halves of the same board '
    'at every airport and every station.',
    '"Leave" is in the list because it is a synonym. In an OPPOSITE question '
    'the synonym is the single commonest wrong answer.')

syn(Q, 2, 'despair', False,
    ['hope', 'grieve', 'worry', 'celebrate'], 0,
    'Despair is what is left when one particular thing runs out.',
    ['To despair is to lose hope.',
     'Grieve and worry are unhappy feelings too, but neither is the exact reverse.',
     'Celebrate is positive, but it is the opposite of grieving rather than of despairing.',
     'The precise reverse of losing hope is to hope.'],
    '**Hope.** Despair is defined by the absence of hope, which makes hope its '
    'exact opposite — closer than any other cheerful word in the list.',
    'For an antonym, look for the word the target is the ABSENCE of, rather '
    'than for any word with the opposite mood.')

syn(Q, 2, 'sever', True,
    ['cut', 'join', 'tie', 'bend'], 0,
    'Think what happens to a rope that is no longer one rope.',
    ['To sever is to cut something in two, or to break it off completely.',
     'Join and tie both put things together, which is the reverse direction.',
     'Bend changes a shape without dividing anything at all.',
     'Cut is the match: what was one piece becomes two.'],
    '**Cut.** Severing is cutting right through, so that one thing becomes '
    'two. "Join" is the word\'s own opposite.',
    'Two of the wrong options here put things together and one only reshapes. '
    'Sorting options by what they DO to an object makes the odd one out show.')

# ---- Section 3: sentence completion ----------------------------------------
fit(Q, 2, 'The ship\'s course...',
    ['took it well south of the storm and added two days to the journey.',
     'was delicious, especially the thick soup that arrived first.',
     'repaired the broken mast and the torn sail before nightfall.',
     'arrived three weeks later than the harbor master had expected.'], 0,
    'A course is a path. Ask what a path can and cannot do.',
    ['Here "course" means the path the ship travels along.',
     'A path cannot repair a mast, and it cannot arrive anywhere — the ship does that.',
     'The meal sense of "course" is real, but it does not fit "the ship\'s".',
     'Only the ending about going south of the storm describes an actual path.'],
    '**Took it well south of the storm and added two days to the journey.** '
    'That ending describes a path through the water, which is what a course is.',
    '"Course" has a meal sense too, and it is among the choices on purpose. '
    'The two words before the gap — "the ship\'s" — are what rule it out.')

fit(Q, 2, 'Using only a compass and the stars, the crew navigated...',
    ['their way through three nights of open water without sighting land.',
     'the sails carefully until every one of them was completely dry.',
     'a large meal of salt beef and biscuit before turning in for the night.',
     'and mended the hull where the collision had split it open.'], 0,
    'Navigating is working out where you are and steering from there.',
    ['To navigate is to work out a position and steer a course from it.',
     'A compass and the stars are instruments for exactly that job.',
     'Drying sails, eating and mending a hull are all other kinds of work.',
     'Only the first ending describes finding a way across open water.'],
    '**Their way through three nights of open water without sighting land.** '
    'Navigating is working out a position and steering by it, which is what a '
    'compass and the stars are for.',
    'The opening of the sentence is the clue. A sentence-completion answer '
    'has to fit the whole sentence, not just the gap at the end of it.')

fit(Q, 2, 'A wave of nostalgia...',
    ['hit her the moment she smelled the pencil shavings in her old classroom.',
     'knocked the small boat sideways and soaked everyone sitting aboard it.',
     'improved the accuracy of the charts the mapmakers had been drawing.',
     'is the name given to a strong wind that blows across tropical seas.'], 0,
    'Nostalgia is a feeling, and a feeling is set off by something particular.',
    ['Nostalgia is a longing for a time in the past.',
     'A smell from a childhood classroom is exactly the sort of thing that sets it off.',
     'A wave of feeling cannot knock a boat over or improve a chart.',
     'So the ending about the pencil shavings is the one that fits.'],
    '**Hit her the moment she smelled the pencil shavings in her old '
    'classroom.** Nostalgia is a longing for a time that has passed, and a '
    'smell from childhood is the classic trigger for it.',
    '"A wave of" works for feelings and for water, which is why both are '
    'offered. The word straight after it decides which one you are reading.')

fit(Q, 3, 'The hot soup and the dry blankets revived...',
    ['the rescued hikers enough that they could walk to the road themselves.',
     'the temperature of the mountain air by a good several degrees.',
     'the narrow route that the rescue team had marked out that morning.',
     'and the storm finally passed away over the far side of the valley.'], 0,
    'Reviving brings strength back — so ask what had lost any.',
    ['To revive something is to make it strong again.',
     'Soup and blankets act on a person, not on air, a path or the weather.',
     'The hikers are the only thing in the sentence that had lost strength.',
     'So they are what the soup and blankets revived.'],
    '**The rescued hikers enough that they could walk to the road '
    'themselves.** To revive is to bring strength back, and the hikers are the '
    'only thing here that had any to lose.',
    'Match the ending to what the subject of the sentence could actually act '
    'on. Soup and a blanket do nothing whatever to a route or a storm.')

# ---- Section 4: parts of speech ---------------------------------------------
pos(Q, 1, 'The captain held a steady course all through the night.',
    'course', 'noun',
    'Try putting "a" or "the" in front of the word and see if it still works.',
    ['Ask what job the word is doing in this sentence.',
     'It reads "a steady course" — the word has "a" in front and "steady" describing it.',
     'Only a noun takes "a" in front and an adjective like that.',
     'So here "course" is a noun.'],
    '**Noun.** "A steady course" is a thing the captain held. The word '
    '"steady" describes it, and only a noun gets described that way.',
    'The test for a noun: can you put "a", "an" or "the" in front of it? If '
    'you can, it is doing a noun\'s job in that sentence.')

pos(Q, 1, 'Her measurements were accurate to the nearest millimeter.',
    'accurate', 'adjective',
    'Ask which word in the sentence it is telling you about.',
    ['Find the nouns first: "measurements" and "millimeter".',
     'The word is telling you what the measurements were like.',
     'Describing a noun is an adjective\'s job, not a noun\'s or a verb\'s.',
     'So "accurate" is an adjective here.'],
    '**Adjective.** It describes "measurements" — it tells you what kind they '
    'were.',
    'An adjective answers "what kind?" about a noun nearby. Find the noun '
    'first, then check whether the word is describing it.')

pos(Q, 2, 'A falling rock severed the rope just above the knot.',
    'severed', 'verb',
    'Ask what the rock actually DID.',
    ['The sentence is about something that happened.',
     'The rock is doing it, and the rope is what it was done to.',
     'A word that takes an object like that, and changes tense, is a verb.',
     'So "severed" is a verb here.'],
    '**Verb.** It is the action the rock performed. The "-ed" ending and the '
    'fact that it takes an object — the rope — both mark it out as the verb.',
    'A verb is the thing happening. If you can put "yesterday" at the front '
    'and the word has to change with it, it is a verb.')

pos(Q, 3, 'The guide gave us an approximate time for the descent.',
    'approximate', 'adjective',
    'The word is sitting between "an" and a noun. What job is that?',
    ['"Approximate" really can be a verb — you can approximate a total.',
     'But here it sits between "an" and "time".',
     'A word in that slot is describing the noun, not performing an action.',
     'So in THIS sentence it is an adjective.'],
    '**Adjective.** It describes what kind of time the guide gave. The very '
    'same word is a verb in other sentences — you can approximate a distance — '
    'which is exactly why the sentence decides, not the word.',
    'This is the trap that costs the most marks on a real paper: a word\'s '
    'usual job is not always its job today. Read the slot it is sitting in.')

# ---- Section 5: word association --------------------------------------------
assoc(Q, 1, ['a compass', 'the stars', 'charts'],
      ['navigate', 'depart', 'deteriorate', 'sever'], 0,
      'What would a sailor DO with all three of these?',
      ['A compass shows direction.',
       'The stars were how sailors found their position before instruments.',
       'Charts are maps of the water itself.',
       'All three are tools for working out a course and steering it — navigating.'],
      '**Navigate.** All three are instruments for working out where you are '
      'and steering towards where you mean to be.',
      'Work out what the three things have in common BEFORE you read the '
      'options. Deciding first stops a plausible word pulling you off course.')

assoc(Q, 1, ['old photographs', 'a song from childhood', 'your grandmother\'s kitchen'],
      ['nostalgia', 'jubilation', 'despair', 'destination'], 0,
      'All three point in the same direction in time.',
      ['A photograph, a song and a kitchen are very different things.',
       'What they share is that each one belongs to earlier in your life.',
       'Each is the sort of thing that brings a past time flooding back.',
       'That longing for a time gone by is nostalgia.'],
      '**Nostalgia.** Each one is a trigger for longing for a time that has '
      'already passed.',
      'Jubilation and despair are feelings too, which is what makes them the '
      'real competition. Nostalgia is the only one pointed at the PAST.')

assoc(Q, 2, ['rust', 'peeling paint', 'a sagging roof'],
      ['deteriorate', 'revive', 'navigate', 'approximate'], 0,
      'All three are signs of the same process, running one way.',
      ['Rust eats metal, paint peels, a roof sags under its own weight.',
       'Every one of them takes time, and every one makes the thing worse.',
       'Nothing here is being repaired or restored.',
       'Getting worse over time is what it means to deteriorate.'],
      '**Deteriorate.** All three are signs of something getting steadily '
      'worse as time passes.',
      '"Revive" is the opposite and it is among the choices on purpose. Always '
      'check which DIRECTION the three things point in.')

assoc(Q, 3, ['confetti', 'cheering', 'a medal ceremony'],
      ['jubilation', 'nostalgia', 'gale', 'voyage'], 0,
      'Ask when these three things are happening, not what they remind you of.',
      ['Confetti, cheering and a medal ceremony all belong to one moment.',
       'That moment is loud, public and happy.',
       'Nostalgia would need the moment to be in the past and looked back on.',
       'Great joy shown openly is jubilation.'],
      '**Jubilation.** All three belong to a moment of great joy shown out '
      'loud and in public.',
      'Nostalgia is the trap: a medal ceremony can certainly be remembered '
      'fondly years later, but the confetti and the cheering are happening NOW.')

build('wayfinder', C, Q, 'unit-ww504', old['title'], 'english',
      old['summary']['text'], old['why']['text'],
      [(o['text'], o['from']) for o in old['objectives']],
      'The question bank is rebuilt to match the shape of her real vocabulary '
      'test. Her Unit 2 paper had five sections worth five marks each — a '
      'reading passage with context-clue questions, synonyms and antonyms, '
      'sentence completion, parts of speech, and word association — and the '
      'old bank here was mostly "What does this word mean?", which is the one '
      'shape that paper never uses. There are now four questions in each of '
      'the five shapes. The one difference from the paper is deliberate: it '
      'hangs five questions off a single long passage, and this app serves '
      'five shuffled questions at a time, so every question has to stand on '
      'its own. Each context-clue question therefore carries its own short '
      'passage rather than sharing one long one — measured on her phone, a '
      '90-word passage pushes the first answer off the bottom of the screen, '
      'and she would re-read it on every question in the section. The skill '
      'is the same; only the staging differs. The cards are unchanged.',
      ('Five shapes, four questions each — the same five your test uses. The '
       'parts-of-speech ones are worth slowing down on: the word\'s usual job '
       'is not always its job in that sentence.', 16),
      'content/wordly-wise-5-04.json',
      old.get('srcName', 'Wordly Wise Book 5, Lesson 4'),
      old.get('source', 'Wordly Wise Book 5'),
      offset_hours=3)

p = os.path.join(REPO, 'content/wordly-wise-5-04.json')
j = json.load(io.open(p, encoding='utf-8'))
j['records']['unit-ww504']['libv'] = 2   # shipped at 1; pinned, not incremented
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + libv %d' % j['records']['unit-ww504']['libv'])
