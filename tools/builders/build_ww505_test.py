# -*- coding: utf-8 -*-
# Wordly Wise · Lesson 5 — question bank rebuilt to her real test's format.
# Same five sections as Lesson 4; see build_ww504_test.py for the reasoning.
# Cards reloaded from the shipped file and left untouched.
import sys, os, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import build
from vocab_test_common import ctx, syn, fit, pos, assoc

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
old = json.load(io.open(os.path.join(REPO, 'content/wordly-wise-5-05.json'),
                        encoding='utf-8'))['records']['unit-ww505']
C = old['cards']
Q = []

# ---- Section 1: reading passage, context clues -----------------------------
ctx(Q, 2,
    'Anya stopped a meter short of the crevice. It was barely wider than her '
    'boot, but her torch found no bottom to it, and the blue ice on either '
    'side fell away into the dark.',
    'crevice',
    'How is the word "crevice" used in this passage?',
    ['To name a narrow split in the ice that runs deep down',
     'To name a wide, flat shelf of ice safe enough to cross',
     'To describe the beam of the torch as it swept the ground',
     'To describe the bright blue color of the ice at the surface'], 0,
    'Two facts are given about it: how wide, and how deep.',
    ['The passage says it is barely wider than her boot, so it is narrow.',
     'Her torch finds no bottom, so it is deep.',
     'The ice falling away on either side tells you it is a split, not a shelf.',
     'Narrow, deep and split open is what a crevice is.'],
    '**To name a narrow split in the ice that runs deep down.** The passage '
    'gives you both measurements — barely a boot wide, and no bottom the '
    'torch can find.',
    'When a passage gives you two facts about a thing, it is usually defining '
    'it. Collect both before you choose.')

ctx(Q, 3,
    'Rob wanted to push for the top with two hours of light left and no rope. '
    'The others called it foolhardy, and by the time the mist came down even '
    'Rob had stopped arguing.',
    'foolhardy',
    'What do the context clues tell you "foolhardy" means?',
    ['Brave in a way that ignores real danger',
     'Careful and unwilling to take any risk at all',
     'Slow and unsure about which way to go',
     'Unfriendly towards the rest of the group'], 0,
    'Look at what Rob actually proposed, and at what happened next.',
    ['Rob wants to go up with little light and no rope — that is bold.',
     'It is also plainly dangerous, which is why the others object.',
     'The mist coming down shows the others were right to object.',
     'Bold in a way that ignores real danger is what foolhardy means.'],
    '**Brave in a way that ignores real danger.** The passage gives you both '
    'halves: the daring plan, and the danger — no rope, fading light, mist on '
    'the way.',
    'Foolhardy is not the opposite of brave, which is what makes the '
    '"careful" option tempting. It is brave with the judgement left out.')

ctx(Q, 2,
    'They built a makeshift shelter from a torn tarpaulin and two walking '
    'poles. It kept the worst of the wind off for one night, and in the '
    'morning they left it where it stood.',
    'makeshift',
    'How is the word "makeshift" used here?',
    ['To show the shelter was put together from whatever was to hand, just for now',
     'To show the shelter was solidly built and meant to last for years',
     'To explain that the shelter was bought ready-made before the trip',
     'To explain that the shelter was the largest one in the whole camp'], 0,
    'Notice what it was built from, and what they did with it next.',
    ['It is built from a torn tarpaulin and two walking poles — not shelter parts.',
     'It lasts one night and keeps off only the worst of the wind.',
     'They walk away and leave it standing, so it was never meant to last.',
     'Improvised, and only for the moment, is what makeshift means.'],
    '**To show the shelter was put together from whatever was to hand, just '
    'for now.** A torn tarpaulin and two walking poles are not shelter parts, '
    'and they abandon it the next morning.',
    'The detail after a word often does the defining. "They left it where it '
    'stood" is doing as much work here as the word itself.')

ctx(Q, 3,
    'We asked how much further it was. "Two hours. Uphill." The guide\'s '
    'answer was terse, and she had already turned back to the path before '
    'anyone could think of a second question.',
    'terse',
    'How is the word "terse" used in this passage?',
    ['To say her answer was short and to the point, with nothing added',
     'To say her answer was long and full of unnecessary detail',
     'To say her answer was friendly and full of encouragement',
     'To say her answer was confusing and hard for the group to follow'], 0,
    'Count the words she actually used.',
    ['Her entire answer is three words: "Two hours. Uphill."',
     'It answers the question completely — distance in time, and the effort.',
     'She turns away at once, adding nothing further.',
     'Short, complete and with nothing spare is what terse means.'],
    '**To say her answer was short and to the point, with nothing added.** '
    'Three words that answer the question fully, and then she turns back to '
    'the path.',
    'Terse does not mean rude and it does not mean unclear — her answer is '
    'perfectly clear. It means nothing spare was said.')

# ---- Section 2: synonyms and antonyms --------------------------------------
syn(Q, 1, 'conquer', True,
    ['defeat', 'surrender', 'admire', 'follow'], 0,
    'Think what an army does to the thing it has beaten.',
    ['To conquer is to defeat something, or to get the better of it.',
     'Surrender is giving in — the opposite side of the same fight.',
     'Admire and follow are things you can do to something without beating it.',
     'Defeat means the same thing: to overcome.'],
    '**Defeat.** Both mean to overcome something. "Surrender" is the word\'s '
    'own opposite, which is why it is the one to think twice about.',
    'You can conquer a mountain as well as an army — the word works for any '
    'difficulty you get the better of.')

syn(Q, 2, 'previous', False,
    ['following', 'earlier', 'distant', 'sudden'], 0,
    'Previous points one way along a line. Which word points the other way?',
    ['Previous means earlier — the one before this one.',
     '"Earlier" says the same thing, so it cannot be the opposite.',
     'Distant is about space and sudden is about speed; neither reverses time order.',
     'Following means the one after, which is the exact reverse.'],
    '**Following.** Previous and following are the two directions along the '
    'same line: the one before, and the one after.',
    '"Earlier" is in the list because it is a synonym. On an OPPOSITE '
    'question, cross the synonym off first — it is the commonest wrong answer.')

syn(Q, 2, 'thwart', True,
    ['block', 'assist', 'delay', 'announce'], 0,
    'Think what happens to a plan that never gets going at all.',
    ['To thwart is to stop someone\'s plan from succeeding.',
     'Assist is helping the plan along — the reverse.',
     'Delay only slows a plan down; the plan can still happen.',
     'Block is the match: the plan is stopped.'],
    '**Block.** Both mean to stop something going ahead. "Delay" is the near '
    'miss worth noticing — a delayed plan still happens, a thwarted one does '
    'not.',
    'Watch for the option that is almost right. Delay and thwart both get in '
    'the way, but only one of them ends the plan.')

syn(Q, 1, 'optimist', False,
    ['pessimist', 'dreamer', 'stranger', 'expert'], 0,
    'Two people look at the same half-full glass. What do you call the other one?',
    ['An optimist looks at things in the most positive way.',
     'A dreamer is hopeful too, so it is not the reverse.',
     'Stranger and expert say nothing at all about how someone sees things.',
     'A pessimist expects the worst, which is the exact opposite.'],
    '**Pessimist.** The pair is built for exactly this: one expects things to '
    'turn out well, the other expects them to turn out badly.',
    '"Dreamer" is there because it also sounds hopeful. An antonym has to '
    'reverse the meaning, not just sit somewhere else nearby.')

# ---- Section 3: sentence completion ----------------------------------------
fit(Q, 2, 'The promise of an easy path lured...',
    ['three of the group away from the marked trail and into deep snow.',
     'the tents down flat against the ground for the whole of that night.',
     'a thick mist across the valley shortly after four in the afternoon.',
     'and the temperature dropped below freezing before they had finished.'], 0,
    'To lure is to tempt — so ask who or what could be tempted.',
    ['Luring means tempting someone with the promise of something good.',
     'Only a person can be tempted; a tent, mist and temperature cannot.',
     'The opening even names the temptation: the promise of an easy path.',
     'So the ending about the three who left the trail is the one that fits.'],
    '**Three of the group away from the marked trail and into deep snow.** A '
    'lure works on people, and the sentence has already named the bait: the '
    'promise of an easy path.',
    'Check what the verb could act on. Three of these endings have no one in '
    'them who could be tempted by anything.')

fit(Q, 2, 'The route to the hut...',
    ['climbs steeply for an hour and then follows the ridge to the east.',
     'was the coldest night any of them could remember spending outdoors.',
     'tasted better than anything they had eaten in the previous four days.',
     'had forgotten to pack a spare torch before leaving in the morning.'], 0,
    'A route is a path. Ask what a path is able to do.',
    ['A route is the way that must be followed to get somewhere.',
     'A path can climb, turn, follow a ridge or drop down.',
     'It cannot be a night, it cannot be tasted, and it cannot forget anything.',
     'Only the ending about climbing and following the ridge describes a way.'],
    '**Climbs steeply for an hour and then follows the ridge to the east.** '
    'That ending describes a way of getting somewhere, which is what a route '
    'is.',
    'When the word is a thing rather than an action, test each ending by '
    'asking whether that thing could really do it.')

fit(Q, 3, 'Reaching the summit before dark was a real challenge...',
    ['and it took every hour of daylight they had left to manage it.',
     'which they packed carefully into the top of the rucksack.',
     'so they decided to eat it slowly to make it last the evening.',
     'and it had been snowing there steadily since the previous Tuesday.'], 0,
    'A challenge is a difficulty, not an object and not a place.',
    ['A challenge is something that takes real skill or effort.',
     'It is not a thing you can pack, and it is not a thing you can eat.',
     'It is not a place either, so snow cannot fall on it.',
     'Only the ending about it taking all their daylight treats it as a difficulty.'],
    '**And it took every hour of daylight they had left to manage it.** A '
    'challenge is a difficulty to be met, and that ending says what meeting '
    'it cost them.',
    'Two of the wrong endings treat the challenge as an object and one treats '
    'it as a place. Deciding what KIND of thing the word is settles it fast.')

fit(Q, 2, 'The last section of the climb was almost vertical...',
    ['so they had to haul themselves up on ropes rather than walk it.',
     'and the view from there stretched for forty miles in every direction.',
     'because the guide had been up it four times the previous summer.',
     'although the snow underfoot had frozen hard again overnight.'], 0,
    'Vertical describes the angle. Which ending follows FROM that angle?',
    ['Vertical means running straight up and down.',
     'The ending has to be a consequence of the slope being that steep.',
     'A long view, an experienced guide and frozen snow are all true of many slopes.',
     'Needing ropes rather than being able to walk follows directly from vertical.'],
    '**So they had to haul themselves up on ropes rather than walk it.** That '
    'is the consequence of the angle — which is what the sentence is telling '
    'you about.',
    'The other three endings could follow almost any description of a slope. '
    'The right one could only follow THIS one.')

# ---- Section 4: parts of speech ---------------------------------------------
pos(Q, 1, 'They reached the summit a little after eleven in the morning.',
    'summit', 'noun',
    'Try putting "the" in front of the word.',
    ['Ask what job the word is doing in this sentence.',
     'It reads "the summit" — a place they reached.',
     'Only a noun takes "the" in front of it like that.',
     'So "summit" is a noun here.'],
    '**Noun.** "The summit" is the place they reached — a thing, with "the" '
    'in front of it.',
    'The test for a noun: can you put "a", "an" or "the" in front of it? If '
    'you can, it is doing a noun\'s job in that sentence.')

pos(Q, 2, 'The final pitch was very nearly vertical.',
    'vertical', 'adjective',
    'Ask which word it is telling you about.',
    ['Find the noun first: "pitch", meaning a section of the climb.',
     'The word is telling you what that pitch was like.',
     'Describing a noun is an adjective\'s job.',
     'So "vertical" is an adjective here.'],
    '**Adjective.** It describes the pitch — it tells you what kind of slope '
    'it was.',
    '"Very nearly" in front of a word is a strong hint: you can be very '
    'nearly vertical, but you cannot very nearly a noun.')

pos(Q, 2, 'A sudden blizzard thwarted their second attempt at the ridge.',
    'thwarted', 'verb',
    'Ask what the blizzard DID.',
    ['The sentence is about something that happened.',
     'The blizzard is doing it, and their attempt is what it was done to.',
     'A word that takes an object like that, and changes tense, is a verb.',
     'So "thwarted" is a verb here.'],
    '**Verb.** It is the action the blizzard performed, and "their second '
    'attempt" is what it acted on.',
    'If you can put "yesterday" at the front of the sentence and the word has '
    'to change with it, the word is a verb.')

pos(Q, 3, 'Getting down before dark was the real challenge.',
    'challenge', 'noun',
    'The word has "the" in front of it. What does that settle?',
    ['"Challenge" really can be a verb — you can challenge someone to a race.',
     'Here it reads "the real challenge", with "the" in front and "real" describing it.',
     'A word in that slot is a thing being named, not an action being done.',
     'So in THIS sentence it is a noun.'],
    '**Noun.** It is the thing being named — with "the" in front and "real" '
    'describing it. The same word is a verb elsewhere, which is exactly why '
    'the sentence decides and not the word.',
    'This is the trap that costs the most marks on a real paper: a word that '
    'is usually one part of speech doing a different job today.')

# ---- Section 5: word association --------------------------------------------
assoc(Q, 1, ['driving snow', 'a howling wind', 'no visibility at all'],
      ['blizzard', 'avalanche', 'crevice', 'summit'], 0,
      'All three describe the same kind of weather.',
      ['Driving snow and a howling wind are both weather.',
       'Losing all visibility is what happens when they come together.',
       'An avalanche is snow moving downhill, not snow falling.',
       'Snow, wind and no visibility together make a blizzard.'],
      '**Blizzard.** A blizzard is exactly a heavy snowfall driven by strong '
      'wind, and losing sight of everything is the result.',
      'Avalanche is the trap: also snow, also a mountain. The difference is '
      'that a blizzard falls and an avalanche slides.')

assoc(Q, 2, ['a torn tarpaulin', 'two walking poles', 'one night only'],
      ['makeshift', 'vertical', 'previous', 'terse'], 0,
      'Ask what these three add up to, not what each one is.',
      ['A torn tarpaulin and two walking poles are not shelter parts.',
       'They are simply whatever happened to be in the bags.',
       '"One night only" says it was never meant to last.',
       'Improvised from what is to hand, and only for now, is makeshift.'],
      '**Makeshift.** Built from whatever came to hand, standing in for the '
      'real thing, and not meant to last.',
      'The third item in the list is doing the most work here. "One night '
      'only" rules out anything built properly.')

assoc(Q, 2, ['free samples', 'a bright shop sign', 'a holiday advert'],
      ['lure', 'thwart', 'conquer', 'challenge'], 0,
      'What are all three of these TRYING to do to you?',
      ['A free sample, a bright sign and an advert are all put there on purpose.',
       'Each one is meant to draw you towards something.',
       'Each works by promising something good.',
       'Tempting someone with the promise of something good is to lure them.'],
      '**Lure.** Every one of the three is designed to tempt you towards '
      'something by promising you something good.',
      'The three things are very different objects. What they share is their '
      'PURPOSE, which is what an association question is really asking about.')

assoc(Q, 3, ['a narrow split in the ice', 'deep shadow', 'a dropped glove gone for good'],
      ['crevice', 'avalanche', 'blizzard', 'route'], 0,
      'The third item tells you how deep it goes.',
      ['A narrow split in the ice is the shape of the thing.',
       'Deep shadow means the light does not reach the bottom.',
       'A dropped glove gone for good means there is real depth below.',
       'Narrow, deep and split open is a crevice.'],
      '**Crevice.** Narrow enough to step over, deep enough that what falls '
      'in does not come back.',
      'Avalanche and blizzard are both mountain words, which is why they are '
      'here. Only one of the four is a shape in the ice.')

build('wayfinder', C, Q, 'unit-ww505', old['title'], 'english',
      old['summary']['text'], old['why']['text'],
      [(o['text'], o['from']) for o in old['objectives']],
      'Rebuilt to the five sections of her real vocabulary test — context '
      'clues from a passage, synonyms and antonyms, sentence completion, '
      'parts of speech, and word association — four questions each, replacing '
      'a bank that was mostly "What does this word mean?". See the Lesson 4 '
      'note for why each context question carries its own short passage '
      'instead of five sharing one long one. Two things worth knowing about '
      'this lesson in particular: "foolhardy" is taught as brave with the '
      'judgement left out rather than as the opposite of brave, because the '
      'tempting wrong answer on a paper is always "careful"; and "terse" is '
      'taught as nothing-spare rather than as rude or unclear, which is the '
      'other way it gets misread. The cards are unchanged.',
      ('Five shapes, four questions each — the same five your test uses. '
       'Watch the parts-of-speech ones: "challenge" is a noun in one sentence '
       'and a verb in another, and only the sentence can tell you which.', 16),
      'content/wordly-wise-5-05.json',
      old.get('srcName', 'Wordly Wise Book 5, Lesson 5'),
      old.get('source', 'Wordly Wise Book 5'),
      offset_hours=3)

p = os.path.join(REPO, 'content/wordly-wise-5-05.json')
j = json.load(io.open(p, encoding='utf-8'))
j['records']['unit-ww505']['libv'] = 2   # shipped at 1; pinned, not incremented
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + libv %d' % j['records']['unit-ww505']['libv'])
