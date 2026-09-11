# Wordly Wise Lesson 2 · Synonyms & Antonyms — built from "Synonyms and
# Antonyms - Lesson 2.pdf" (Drive, English/Wordly Wise, uploaded 2026-09-11).
# Same 15 words unit-ww502 already covers, tested on the one fact it does not:
# the synonym/antonym pairs the class's own unit test draws from.
#
# ── READ THIS BEFORE EDITING, AND BEFORE TRUSTING build_ww1_synonyms.py ──
# Lesson 1's builder is STALE: it still contains the glossed stems and filler
# distractors that v121 identified as a real bug and removed from the shipped
# JSON. Re-running that script would silently reintroduce the bug. THIS file
# follows the shipped, fixed pattern, which is the one that binds:
#
#   1. The stem NEVER glosses the word. "Which word means the OPPOSITE of
#      aroma?" — not "...of aroma (a pleasant smell)?" A gloss hands over the
#      very fact being tested, and in a SYNONYM question the gloss usually IS
#      the answer. Where a word genuinely has two senses, disambiguate with a
#      part-of-speech tag — context, never a definition.
#   2. Every option is the same part of speech as the answer, and each holds a
#      different REAL relationship to the stem word. The strongest distractor
#      is the word's own opposite number: the synonym sits in every antonym
#      question and the antonym in every synonym question, so she has to read
#      which was actually asked.
#   3. The hint is a real etymology hook where one exists, or a named warning
#      about this item's specific trap. Never boilerplate — a hint costs 5 XP
#      and must be worth it.
#   4. ex.main says WHY, and names the near-miss distractor outright.
#
# ── The source, and the one row worth a grown-up's eye ──
# The table is a clean 3-column grid but text extraction flattens it into a
# single stream that interleaves the columns; it was read by RENDERING the
# page (pypdfium2) and checking the grid directly, the same discipline every
# scanned or multi-column source in this repo gets. All 15 rows carry both a
# synonym and an antonym — unlike Lesson 1, where two were genuinely blank.
#
# EXTRACT is the row to know about. Its synonyms are "excerpt, juice" — both
# NOUNS — so the sheet is treating extract as a noun (a concentrated essence,
# or a passage pulled from a text), not the verb "to pull out". That is what
# makes its antonym "refuse" correct: REF-yooss, the noun meaning waste, the
# worthless part left behind once the good part is taken. Read as the verb
# ri-FYOOZ ("to say no"), it looks like a misprint. It is not. The card says
# so, the question carries an "As a NOUN" tag, and parentNote flags it.
from unit_common import card, q, build

SRC = "Synonyms and Antonyms - Lesson 2.pdf (Drive)"
SRCLONG = "Vocabulary: Wordly Wise Unit 2 — Synonyms and Antonyms study sheet (Drive)"

SP = {  # reused from unit-ww502 so the two units agree on pronunciation
    'aroma':'uh-ROH-muh','beverage':'BEV-ur-ij','bland':'bland','brittle':'BRIT-ul',
    'cluster':'KLUS-tur','combine':'kum-BYNE','consume':'kun-SOOM','crave':'krayv',
    'cultivate':'KUL-tih-vayt','equivalent':'ih-KWIV-uh-lunt','export':'ek-SPORT',
    'extract':'ek-STRAKT','introduce':'in-truh-DOOSS','purchase':'PUR-chuss',
    'tropical':'TRAHP-ih-kul',
}

C, Q = [], []

def sacard(term, syns, ants, note):
    d = '**Synonyms: %s. Antonym%s: %s.**\n• %s' % (
        ', '.join(syns), 's' if len(ants) > 1 else '', ', '.join(ants), note)
    card(C, term, d, hint=None, frm='added')
    C[-1]['sp'] = SP[term]

# ---- the 15 cards, straight off the sheet ----
sacard('aroma', ['odor', 'scent'], ['stench', 'stink'],
       'An aroma is a smell you are glad to meet; a stench is one you back away from. Odor sits in the middle — it can go either way.')
sacard('beverage', ['drink'], ['food'],
       'A beverage is something you drink, so the sheet pairs it against food — the thing you chew instead.')
sacard('bland', ['boring'], ['exciting', 'interesting'],
       'Bland food has had nothing done to it; bland writing is the same idea applied to words.')
sacard('brittle', ['breakable', 'frail'], ['unbreakable'],
       'Brittle means it snaps rather than bends — dry pasta is brittle, a rubber band is not.')
sacard('cluster', ['bundle', 'collection'], ['individual'],
       'A cluster is several things gathered tight together, so its opposite is one thing standing on its own.')
sacard('combine', ['blend', 'merge'], ['divide', 'separate'],
       'Combine puts things together into one; divide and separate pull one thing back into parts.')
sacard('consume', ['deplete'], ['save', 'fill'],
       'Consume is to use something up until it is gone — which is why saving it up is the opposite.')
sacard('crave', ['covet'], ['dislike'],
       'To crave is to want something badly. Covet is the same wanting, usually for something that belongs to someone else.')
sacard('cultivate', ['manage', 'prepare'], ['destroy', 'ignore'],
       'Cultivate is tending something so it grows — a field, or a friendship. Ignoring it is the quiet opposite; destroying it is the loud one.')
sacard('equivalent', ['comparable', 'equal'], ['opposite', 'unlike'],
       'Equivalent things are worth the same even when they are not identical — four quarters and a dollar.')
sacard('export', ['ship', 'transport'], ['hold', 'keep'],
       'Export sends goods out of a country. Its true mirror word is import, but the sheet pairs it with holding onto them instead.')
sacard('extract', ['excerpt', 'juice'], ['refuse'],
       'Careful — the sheet uses the NOUN. An extract is the good part taken out: a passage from a book, or vanilla extract. Its opposite is refuse (say REF-yooss), the waste left behind. That is not the verb ri-FYOOZ meaning "to say no".')
sacard('introduce', ['announce', 'offer'], ['conceal', 'hide'],
       'To introduce is to bring something into view — a person, an idea, a new rule. To conceal is to keep it out of view.')
sacard('purchase', ['investment'], ['sale'],
       'Purchase and sale are the two sides of one deal: the buyer makes a purchase, the seller makes a sale.')
sacard('tropical', ['lush', 'sweltering'], ['cool', 'frigid'],
       'Tropical describes the hot, wet band of the Earth near the equator — sweltering is the heat, lush is what the heat and rain grow.')

assert len(C) == 15

def mc(text, ans_word, wrong, lv, hint, steps, main, tip):
    """opts lead with the answer; build()'s _balance() rotates the correct
    slot across positions, so never hand-place it here."""
    q(Q, lv, text, [ans_word] + wrong, 0, hint, steps, main, tip, frm='added')

TRAP = 'One of these means the SAME as the word, not the opposite. Read the question again before you pick.'
TRAPS = 'One of these is the word’s OPPOSITE, not a match for it. Read the question again before you pick.'

# ---- antonym questions: all 15 words, since every row has one ----
mc("Which word means the OPPOSITE of aroma?", 'stench', ['scent', 'juice', 'investment'], 1,
   'Aroma comes from the Greek word for spice — it starts out meaning a GOOD smell.',
   ['Aroma is a smell you are pleased to notice.',
    'Its opposite has to be a smell you are not pleased to notice.',
    'That is "stench."'],
   '**Stench.** All four are nouns, and scent is the near-miss: it means the same as aroma, not the reverse of it.',
   'Stink works too. Odor is the neutral one — it can describe either.')

mc("Which word means the OPPOSITE of beverage?", 'food', ['drink', 'aroma', 'purchase'], 1,
   'Beverage traces back to the Latin bibere, to drink — the same root hiding inside "imbibe."',
   ['A beverage is something you drink.',
    'The sheet pairs it against the other half of a meal.',
    'That is "food."'],
   '**Food.** Drink is the trap: it is beverage’s synonym. Food is what you eat rather than drink.',
   'This pair is about HOW it reaches you — swallowed as liquid, or chewed first.')

mc("Which word means the OPPOSITE of bland?", 'exciting', ['boring', 'sweltering', 'brittle'], 1,
   'Bland comes from Latin blandus, smooth — nothing sharp enough to notice.',
   ['Bland means there is nothing in it to grab your attention.',
    'The opposite is something that does grab your attention.',
    'That is "exciting."'],
   '**Exciting.** Boring is the near-miss — it means the same as bland. All four are adjectives, so part of speech will not narrow it for you.',
   'Interesting works as well. Bland applies to food, colour, or writing alike.')

mc("Which word means the OPPOSITE of brittle?", 'unbreakable', ['breakable', 'individual', 'comparable'], 1,
   'Brittle shares a root with the old word brēotan, to break.',
   ['Brittle means it snaps instead of bending.',
    'The opposite is something that will not snap at all.',
    'That is "unbreakable."'],
   '**Unbreakable.** Breakable is the trap: it is brittle’s synonym, and the "un-" is the only thing separating the two options.',
   'Frail is another synonym. Read the prefix carefully on this one.')

mc("Which word means the OPPOSITE of cluster?", 'individual', ['collection', 'investment', 'beverage'], 1,
   'Cluster is a cousin of "clot" — a lump of things stuck together.',
   ['A cluster is several things gathered close together.',
    'The opposite is a single one, standing alone.',
    'That is "individual."'],
   '**Individual.** Collection is the near-miss: a collection IS a cluster, not the reverse of one.',
   'A cluster of grapes; one individual grape pulled off the stem. Bundle is cluster’s other synonym.')

mc("Which word means the OPPOSITE of combine?", 'separate', ['merge', 'announce', 'deplete'], 1,
   'Combine is com- (together) plus bini (two at a time) — literally "two together."',
   ['Combine means to put things together into one.',
    'The opposite is pulling that one thing back into parts.',
    'That is "separate."'],
   '**Separate.** Merge is the trap — it means the same as combine. Divide is the other correct opposite the sheet gives.',
   'All four are verbs here, so you cannot shortcut this by part of speech.')

mc("Which word means the OPPOSITE of consume?", 'save', ['deplete', 'conceal', 'cultivate'], 1,
   'Consume is con- (completely) plus sumere (to take up) — to take it all up.',
   ['Consume means to use something up until none is left.',
    'The opposite is keeping it instead of using it.',
    'That is "save."'],
   '**Save.** Deplete is the near-miss: to deplete a supply IS to consume it. "Fill" is the sheet’s other answer.',
   'You consume a tank of petrol; you save the rest for the trip home.')

mc("Which word means the OPPOSITE of crave?", 'dislike', ['covet', 'transport', 'blend'], 1,
   'Crave comes from an old word meaning to demand or beg for something.',
   ['To crave something is to want it badly.',
    'The opposite of wanting it badly is not wanting it at all.',
    'That is "dislike."'],
   '**Dislike.** Covet is the trap: coveting is craving, aimed at something that belongs to someone else.',
   'Crave is usually about food or comfort; covet is usually about possessions.')

mc("Which word means the OPPOSITE of cultivate?", 'destroy', ['prepare', 'merge', 'offer'], 2,
   'Cultivate comes from Latin colere, to tend or till — the same root as agriculture.',
   ['Cultivate means to tend something carefully so it grows.',
    'The opposite is tearing down what was growing.',
    'That is "destroy."'],
   '**Destroy.** Prepare is the near-miss — preparing ground IS part of cultivating it. "Ignore" is the sheet’s quieter opposite.',
   'You can cultivate a garden or a friendship; both can be destroyed or simply ignored.')

mc("Which word means the OPPOSITE of equivalent?", 'unlike', ['comparable', 'brittle', 'tropical'], 2,
   'Equivalent is equi- (equal) plus valent (worth) — equal in worth.',
   ['Equivalent means worth the same, even if the two things are not identical.',
    'The opposite is being not the same at all.',
    'That is "unlike."'],
   '**Unlike.** Comparable is the trap: comparable things ARE equivalent. "Opposite" is the sheet’s other answer.',
   'Four quarters are equivalent to a dollar — different objects, same worth.')

mc("Which word means the OPPOSITE of export?", 'keep', ['ship', 'divide', 'announce'], 2,
   'Export is ex- (out) plus portare (to carry) — to carry out. Import carries in.',
   ['Export means sending goods out to another country.',
    'The opposite the sheet gives is not sending them anywhere.',
    'That is "keep."'],
   '**Keep.** Ship is the near-miss — shipping goods out IS exporting them. "Hold" is the sheet’s other answer.',
   'The truest mirror of export is import, but that word is not on this sheet.')

mc("As a NOUN, which word means the OPPOSITE of extract?", 'refuse', ['excerpt', 'bundle', 'scent'], 3,
   'Say the answer REF-yooss, rhyming with "goose" — the noun for waste, not the verb meaning to say no.',
   ['An extract is the good part taken out of something — a passage, or a juice.',
    'The opposite is the worthless part left behind once the good part is gone.',
    'That is "refuse," meaning waste.'],
   '**Refuse.** Excerpt is the trap: an excerpt IS an extract. Refuse here is the noun REF-yooss (rubbish), not ri-FYOOZ (to decline) — same spelling, two different words.',
   'Vanilla extract is the flavour pulled out of the bean; the spent bean is the refuse.')

mc("Which word means the OPPOSITE of introduce?", 'conceal', ['announce', 'consume', 'cultivate'], 2,
   'Introduce is intro- (inward) plus ducere (to lead) — to lead something in where it can be seen.',
   ['To introduce is to bring something or someone into view.',
    'The opposite is keeping it out of view.',
    'That is "conceal."'],
   '**Conceal.** Announce is the near-miss: announcing something introduces it. "Hide" is the sheet’s plainer answer.',
   'You introduce a new rule to a class, or conceal it until the last minute.')

mc("Which word means the OPPOSITE of purchase?", 'sale', ['investment', 'cluster', 'stink'], 1,
   'Purchase came into English meaning to chase after something until you got it.',
   ['A purchase is something you buy.',
    'The opposite side of that same deal belongs to the person selling.',
    'That is "sale."'],
   '**Sale.** Investment is the trap: an investment is a kind of purchase. Purchase and sale are one transaction seen from two sides.',
   'Every purchase is somebody else’s sale — the money just changes direction.')

mc("Which word means the OPPOSITE of tropical?", 'frigid', ['sweltering', 'unbreakable', 'boring'], 1,
   'Tropical names the hot band of the Earth between the Tropic of Cancer and the Tropic of Capricorn.',
   ['Tropical describes the hot, wet part of the world near the equator.',
    'The opposite is bitterly cold.',
    'That is "frigid."'],
   '**Frigid.** Sweltering is the near-miss — it means the same kind of heat as tropical. "Cool" is the sheet’s milder answer.',
   'The Frigid Zones are the real name for the polar caps, at the other end of the map.')

# ---- synonym questions: the same list asked the other way ----
mc("Which word means almost the same as cluster?", 'bundle', ['individual', 'refuse', 'sale'], 1,
   TRAPS,
   ['A cluster is a group of things packed close together.',
    'A word for several things gathered into one lot is "bundle."',
    'So the synonym is "bundle."'],
   '**Bundle.** Collection works too. Individual is there because it is cluster’s OPPOSITE — easy to grab if you read the question too fast.',
   'A cluster of stars, a bundle of sticks — same idea of things held together.')

mc("As a NOUN, which word means almost the same as extract?", 'excerpt', ['refuse', 'aroma', 'beverage'], 3,
   'All four are nouns, so part of speech will not narrow this one — you need the word itself.',
   ['As a noun, an extract is a piece taken out of something larger.',
    'A passage lifted out of a book is called an excerpt.',
    'So the synonym is "excerpt."'],
   '**Excerpt.** Juice is the sheet’s other synonym, for the squeezed-out kind of extract. Refuse is the trap: it is extract’s OPPOSITE, the part thrown away.',
   'A book review quotes an excerpt; a recipe calls for almond extract. Same idea, taken out.')

mc("Which word means almost the same as cultivate?", 'manage', ['destroy', 'consume', 'export'], 2,
   TRAPS,
   ['To cultivate is to look after something so that it grows.',
    'Looking after something carefully over time is to manage it.',
    'So the synonym is "manage."'],
   '**Manage.** Prepare works as well. Destroy is there because it is cultivate’s OPPOSITE, and it is the easiest wrong answer to reach for.',
   'A farmer cultivates a field by managing it season after season.')

mc("Which word means almost the same as equivalent?", 'comparable', ['opposite', 'unbreakable', 'sweltering'], 2,
   'Equi- means equal, and -valent means worth — the answer should mean "worth about the same."',
   ['Equivalent means two things are worth or count the same.',
    'A word for things that can be measured against each other as the same is "comparable."',
    'So the synonym is "comparable."'],
   '**Comparable.** Equal is the sheet’s other synonym. Opposite is the trap — it is one of equivalent’s own ANTONYMS, sitting right there in the list.',
   'Comparable does not mean identical: it means close enough to weigh against each other.')

mc("Which word means almost the same as aroma?", 'scent', ['stench', 'food', 'drink'], 1,
   TRAPS,
   ['An aroma is a smell, and a pleasant one.',
    'Another word for a pleasant smell is "scent."',
    'So the synonym is "scent."'],
   '**Scent.** Odor is the sheet’s other synonym, though odor can swing either way. Stench is the trap: it is aroma’s OPPOSITE.',
   'Perfume makers talk about a scent; a kitchen has an aroma; a bin has a stench.')

assert len(Q) == 20, len(Q)

build('wayfinder', C, Q, 'unit-ww502-syn', 'Wordly Wise · Lesson 2 Synonyms & Antonyms', 'english',
      'The class study sheet for Lesson 2, giving a synonym and an antonym for each of the 15 vocabulary words — the same list unit-ww502 already covers, tested a different way. Every row on this sheet has both, so every word is asked in both directions.',
      'Naming a word’s opposite is a small proof that you actually know what it means. You cannot pick the opposite of "equivalent" by guessing at the letters — you have to know the word, which is exactly what a unit test is checking.',
      [('State a synonym and an antonym for each Lesson 2 word.', 'source'),
       ('Tell a word’s synonym from its antonym when both are offered as choices.', 'added'),
       ('Read "extract" and "refuse" in their noun senses, which is how this sheet uses them.', 'added')],
      'Built from the class’s own Lesson 2 synonym/antonym sheet. Two things worth knowing. '
      'First, EXTRACT: the sheet gives "excerpt, juice" as its synonyms, both nouns, so it is using extract as a NOUN — the good part taken out of something — which is what makes its antonym "refuse" correct. That is REF-yooss, the noun meaning waste, not ri-FYOOZ meaning to say no. Read as the verb it looks like a misprint, and River may well read it that way, so the card says it outright and the question carries an "As a NOUN" tag. '
      'Second, every wrong option in this unit is another real word from the same sheet, and one of them is always the stem word’s own opposite number — the synonym inside an antonym question, and the reverse. That is deliberate: it means she has to read which was asked rather than eliminating on part of speech. If she is getting these wrong, it is usually the question she misread, not the word.',
      ('The cards first — a synonym only means something once the base word is solid — then the questions.', 12),
      'content/wordly-wise-5-02-syn.json', SRC, SRCLONG, round_=8)
print('--- ww lesson 2 synonyms & antonyms built ---')
