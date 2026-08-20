# Wordly Wise Lesson 1 · Synonyms & Antonyms study guide — built from
# "Lesson 1 synonyms and antonyms.pdf" in the Drive English/Wordly Wise
# folder. The sheet itself says "The UNIT TEST will include synonyms and
# antonyms from this list!" — this is the class's own test-prep material,
# covering the SAME 15 words as unit-ww501 but a different fact about each.
#
# Shelves alongside "Wordly Wise · Lesson 1" with NO order field — the shelf
# sorts primarily by order (absent = 0) and only falls back to title for
# ties, so an Ad-Astra-style order:1 would bucket this after ALL FIVE
# lessons (which also default to order 0), not specifically after Lesson 1.
# Caught by rendering the shelf, not by reading the sort code: it landed at
# position 6, after Lesson 5. Titled "Lesson 1 Synonyms & Antonyms" with no
# order, plain numeric-aware title sort already places it exactly where it
# belongs — right after "Lesson 1", before "Lesson 2" — verified directly:
# ['Lesson 1', 'Lesson 1 Synonyms & Antonyms', 'Lesson 2', 'Lesson 3', ...].
#
# A note on the source: it's a 3-column table (Term / Synonyms / Antonyms)
# flattened by OCR into a single stream. Two words (jostle, pedestrian) have
# no antonym in the flattened text at all — re-checked twice, same result
# both times, so this reads as the sheet genuinely leaving them blank, not
# an extraction glitch — and "Patient" carries synonyms for BOTH of its
# senses (tolerant/composed as an adjective, victim/sufferer as the noun for
# a person under a doctor's care) with only the adjective sense given an
# antonym. Nothing is invented for the blanks: no antonym is tested for
# jostle or pedestrian, or for patient's noun sense.
from unit_common import card, q, build

SRC = "Lesson 1 synonyms and antonyms.pdf (Drive)"
SRCLONG = "Vocabulary Unit 1: Synonyms and Antonyms — Wordly Wise Lesson 1 study sheet (Drive)"

SP = {  # reused from unit-ww501 so the two units agree on pronunciation
    'accustom':'uh-KUSS-tum','alert':'uh-LURT','assign':'uh-SYNE','budge':'buj',
    'burly':'BUR-lee','companion':'kum-PAN-yun','compatible':'kum-PAT-uh-bul',
    'concept':'KAHN-sept','distract':'dih-STRAKT','jostle':'JAH-sul',
    'obedient':'oh-BEE-dee-unt','obstacle':'AHB-stuh-kul','patient':'PAY-shunt',
    'pedestrian':'puh-DESS-tree-un','retire':'rih-TIRE',
}

C, Q = [], []

def sacard(term, syns, ant, note):
    lead = 'Synonyms: %s.' % ', '.join(syns)
    if ant: lead += ' Antonym: %s.' % ant
    d = '**%s**\n• %s' % (lead, note)
    card(C, term, d, hint=None, frm='added')
    C[-1]['sp'] = SP[term]

sacard('accustom', ['adapt', 'adjust'], 'neglect, ignore',
       "If you're accustomed to a sound, you stop noticing it; if you neglect or ignore it, you never got used to it at all.")
sacard('alert', ['attentive', 'watchful'], 'inattentive',
       'An alert lookout is attentive; an inattentive one misses what is right in front of them.')
sacard('assign', ['set', 'give'], 'reject',
       'A teacher can assign extra credit, or a student can reject it and turn it down.')
sacard('budge', ['stir', 'shift'], 'oppose',
       "A team that won't budge on a plan is refusing to shift; a team that opposes it is fighting it outright.")
sacard('burly', ['sturdy', 'well-built'], 'slight',
       'A burly wrestler and a slight, narrow-framed gymnast are built in opposite ways.')
sacard('companion', ['partner', 'friend'], 'foe',
       'A companion travels beside you; a foe works against you.')
sacard('compatible', ['together', 'cooperative'], 'disagreeable',
       'Compatible roommates get along easily; disagreeable ones argue over everything.')
sacard('concept', ['idea', 'notion'], 'fact',
       'A concept is still just an idea being worked out; a fact has already been proven true.')
sacard('distract', ['divert', 'sidetrack'], 'focus',
       'Noise in the hallway can distract you from homework; closing the door helps you focus instead.')
sacard('jostle', ['bump', 'knock', 'shove'], None,
       'A crowded hallway is full of jostling — everyone bumping and knocking into everyone else.')
sacard('obedient', ['compliant', 'dutiful'], 'defiant',
       'An obedient dog sits the first time you ask; a defiant one plants its paws and refuses.')
sacard('obstacle', ['barrier', 'hurdle'], 'advantage',
       'A locked gate is an obstacle in your way; a shortcut is an advantage that helps you along.')
sacard('patient', ['tolerant', 'composed'], 'complains',
       "As an adjective, patient means willing to wait calmly — the opposite of someone who complains at every delay. Patient is also a noun: victim and sufferer are close synonyms for the person a doctor is treating.")
sacard('pedestrian', ['walker', 'hiker'], None,
       'A pedestrian crosses at the light on foot, the way a walker or a hiker covers ground — no engine involved.')
sacard('retire', ['quit', 'stop', 'turn in', 'call it a day'], 'rise, wake',
       'You retire to bed when you are tired and ready to stop for the night; you rise or wake once you are done sleeping.')

assert len(C) == 15

def mc(term, prompt_word_desc, ans_word, wrong, lv, steps, tip):
    opts = [ans_word] + wrong
    q(Q, lv, prompt_word_desc, opts, 0, 'Think about what "%s" means, then find its match.' % term,
      steps, '**%s.**' % ans_word.capitalize(), tip, frm='added')

# ---- antonym questions (13 words with a clean given antonym) ----
mc('accustom', "Which word means the OPPOSITE of accustom (to get used to something)?",
   'ignore', ['burly', 'pedestrian', 'companion'], 1,
   ['Accustom means to get used to something — you stop noticing it.',
    'The opposite of getting used to something is failing to notice or care about it at all.',
    'That is "ignore."'],
   'You can also say "neglect" — both mean never paying it any attention.')
mc('alert', "Which word means the OPPOSITE of alert (attentive, watchful)?",
   'inattentive', ['obedient', 'compatible', 'retire'], 1,
   ['Alert means watchful and paying close attention.',
    'The opposite of paying attention is not paying attention.',
    'That is "inattentive."'],
   'The prefix "in-" flips a word to its opposite — attentive becomes inattentive.')
mc('assign', "Which word means the OPPOSITE of assign (to give someone a job or task)?",
   'reject', ['alert', 'budge', 'concept'], 1,
   ['Assign means to hand someone a task or job.',
    'The opposite of handing something to someone is refusing to accept it.',
    'That is "reject."'],
   'A teacher assigns homework; a student cannot reject it, but the WORD reject is still its opposite.')
mc('budge', "Which word means the OPPOSITE of budge (to move or shift slightly)?",
   'oppose', ['assign', 'burly', 'distract'], 2,
   ['Budge means to move or give way, even a little.',
    'The opposite of giving way is standing firmly against something.',
    'That is "oppose."'],
   'A stuck jar lid "won\'t budge"; someone who opposes a plan won\'t give an inch either.')
mc('burly', "Which word means the OPPOSITE of burly (big and strongly built)?",
   'slight', ['companion', 'obstacle', 'patient'], 1,
   ['Burly describes someone big and strongly built.',
    'The opposite build is small and thin.',
    'That is "slight."'],
   'A "slight" person has a light, narrow frame — the opposite of burly.')
mc('companion', "Which word means the OPPOSITE of companion (a friend who spends time with you)?",
   'foe', ['compatible', 'concept', 'retire'], 1,
   ['A companion is a friend who is on your side.',
    'The opposite of a friend is an enemy.',
    'That is "foe."'],
   '"Foe" is an old, short word for enemy — still used in stories about rivals and battles.')
mc('compatible', "Which word means the OPPOSITE of compatible (getting along well)?",
   'disagreeable', ['obedient', 'alert', 'pedestrian'], 2,
   ['Compatible things or people get along smoothly together.',
    'The opposite is not getting along — arguing or clashing.',
    'That is "disagreeable."'],
   'Disagreeable roommates fight about everything compatible ones would settle easily.')
mc('concept', "Which word means the OPPOSITE of concept (a general idea)?",
   'fact', ['budge', 'companion', 'distract'], 1,
   ['A concept is an idea still being worked out — it might be true or it might not.',
    'The opposite of an unproven idea is something already known to be true.',
    'That is "fact."'],
   'Scientists start with a concept and test it until it becomes an established fact.')
mc('distract', "Which word means the OPPOSITE of distract (to pull attention away)?",
   'focus', ['obstacle', 'retire', 'burly'], 1,
   ['Distract means to pull someone\'s attention away from what they are doing.',
    'The opposite of pulling attention away is keeping it locked on one thing.',
    'That is "focus."'],
   'Closing your door to focus is the direct opposite of letting noise distract you.')
mc('obedient', "Which word means the OPPOSITE of obedient (doing what you are asked)?",
   'defiant', ['compatible', 'concept', 'assign'], 1,
   ['Obedient means doing what you are asked or told to do.',
    'The opposite is refusing to do what you are told.',
    'That is "defiant."'],
   'A defiant dog plants its paws and will not budge — the exact opposite of an obedient one.')
mc('obstacle', "Which word means the OPPOSITE of obstacle (something blocking your way)?",
   'advantage', ['distract', 'patient', 'alert'], 2,
   ['An obstacle is something in your way that makes progress harder.',
    'The opposite of something that slows you down is something that helps you along.',
    'That is "advantage."'],
   'A locked gate is an obstacle; a spare key someone hands you is an advantage.')
mc('patient', "As an ADJECTIVE, which word means the OPPOSITE of patient (tolerant, willing to wait)?",
   'complains', ['alert', 'obedient', 'burly'], 2,
   ['As an adjective, patient means calm and willing to wait without a fuss.',
    'The opposite of waiting calmly is not waiting calmly at all.',
    'That describes someone who complains.'],
   'Someone stuck in a slow line either waits patiently, or complains the whole time — opposite responses to the same wait.')
mc('retire', "Which words mean the OPPOSITE of retire (to go to bed / stop for the day)?",
   'rise, wake', ['budge', 'assign', 'obstacle'], 1,
   ['Retire can mean to go to bed or stop working for the day.',
    'The opposite of going to sleep is coming out of sleep.',
    'That is "rise" or "wake."'],
   'You retire tired at night and rise or wake once you are done sleeping — a clean before-and-after pair.')

# ---- synonym questions: the 2 words with no antonym, plus a few for spread ----
mc('jostle', "Which word means almost the same as jostle (to push or shove)?",
   'shove', ['assign', 'alert', 'concept'], 1,
   ['Jostle means to bump or push against someone, often in a crowd.',
    'A close match for "bump against someone" is "shove."',
    'So the synonym is "shove."'],
   '"Bump," "knock" and "shove" all describe the same kind of crowded jostling.')
mc('pedestrian', "Which word means almost the same as pedestrian (a person traveling on foot)?",
   'walker', ['companion', 'obstacle', 'retire'], 1,
   ['A pedestrian is someone traveling on foot, not by car or bike.',
    'Someone traveling on foot is simply called a walker.',
    'So the synonym is "walker."'],
   'A hiker is also a synonym — both describe covering ground on foot.')
mc('companion', "Which word means almost the same as companion (a friend who spends time with you)?",
   'partner', ['obstacle', 'jostle', 'burly'], 1,
   ['A companion is someone who spends time with you or does things with you.',
    'Another word for someone you team up with is "partner."',
    'So the synonym is "partner."'],
   'A travel companion and a travel partner mean essentially the same thing.')
mc('obstacle', "Which word means almost the same as obstacle (something blocking your way)?",
   'barrier', ['companion', 'patient', 'assign'], 1,
   ['An obstacle is something that blocks your path or progress.',
    'A word that means the same kind of blocking thing is "barrier."',
    'So the synonym is "barrier."'],
   'A fallen tree on a trail is both an obstacle and a barrier — same idea, two words.')
mc('concept', "Which word means almost the same as concept (a general idea)?",
   'idea', ['burly', 'retire', 'obedient'], 1,
   ['A concept is a general idea or thought about something.',
    'The plainest match for "a general idea" is simply "idea."',
    'So the synonym is "idea."'],
   '"Notion" is another synonym — all three describe a thought still taking shape.')
mc('retire', "Which word means almost the same as retire (to stop for the day)?",
   'quit', ['alert', 'companion', 'budge'], 1,
   ['Retire can mean to stop working or stop for the day.',
    'A plain word for stopping something is "quit."',
    'So the synonym is "quit."'],
   '"Turn in" and "call it a day" are two more ways people say the same thing.')

assert len(Q) == 19

build('wayfinder', C, Q, 'unit-ww501-syn', 'Wordly Wise · Lesson 1 Synonyms & Antonyms', 'english',
      'The class study sheet for Lesson 1, built around one synonym and one antonym for each of the 15 vocabulary words — the same list unit-ww501 already covers, tested a different way. The sheet itself says the unit test draws directly from these pairs.',
      'A synonym or antonym is really a small proof that you understand a word\'s meaning, not just its spelling — you have to know what "accustom" means before you can spot "ignore" as its opposite. That is exactly the kind of recall a unit test checks.',
      [('State a synonym and, where the sheet gives one, an antonym for each Lesson 1 word.', 'source'),
       ('Recognize a word\'s synonym or antonym among other Lesson 1 vocabulary.', 'added')],
      'Built from "Lesson 1 synonyms and antonyms.pdf," which says outright that the unit test draws from this list. The source is a 3-column table flattened by text extraction, and two words — jostle and pedestrian — come out with no antonym at all (checked twice, same result both times, so this reads as the sheet leaving them blank rather than a misread). Nothing is invented for those gaps: only their synonyms are tested. "Patient" carries synonyms for both of its senses — tolerant/composed as an adjective, victim/sufferer as the noun for someone under a doctor\'s care — and only the adjective sense had a antonym given, so that is the only one tested.',
      ('The cards first, since a synonym only means something once the base word is solid — then the questions.', 12),
      'content/wordly-wise-5-01-syn.json', SRC, SRCLONG, round_=8)
print('--- ww lesson 1 synonyms & antonyms built ---')
