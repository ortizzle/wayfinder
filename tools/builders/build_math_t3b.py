# Topic 3, second half: lessons 3-5 to 3-7 and the Topic Review capstone.
# See build_math_t3.py for the sourcing note.
from math_common import card, q, build

SRC = "Textbook Topic 3, Lessons 3-1 to 3-7 (Drive)"
SRCLONG = "enVision Math, Topic 3 textbook scan — Lessons 3-1 to 3-7 (Drive)"

def oq(Q, lv, text, opts, hint, steps, main, tip):
    # kind:'order' — opts listed in the CORRECT sequence, ans 0; she sees them shuffled.
    Q.append({'id': 'q%d' % len(Q), 'lv': lv, 'from': 'source', 'kind': 'order',
              'q': text, 'opts': [str(o) for o in opts], 'ans': 0, 'hint': hint,
              'steps': steps, 'ex': {'main': main, 'tip': tip}})

# ---------------------------------------------------------------- 3-5
C, Q = [], []
card(C, 'Line up the points',
     '**To compare decimals, write them with the decimal points stacked.**\n'
     '• 3.576 vs 3.432 — points aligned, seats aligned.\n'
     '• Then it is the same left-to-right comparison as whole numbers.',
     hint='Stack the points and the seats take care of themselves.')
card(C, 'Compare from the left',
     '**Walk left to right; the first seat where the digits differ decides.**\n'
     '• 3.576 vs 3.432: ones tie (3), tenths differ (5 > 4) — done.\n'
     '• Nothing further right can overturn an earlier seat.',
     hint='The first disagreement wins. Everything after is noise.')
card(C, 'Annex zeros to compare',
     '**Different lengths? Attach end zeros until they match.**\n'
     '• 12.8 vs 12.68 → 12.80 vs 12.68 — now 8 > 6 in the tenths.\n'
     '• More digits never means bigger.',
     hint='Pad with free zeros, then compare seat by seat.')
card(C, 'Between any two decimals',
     '**There is always another decimal between two different ones.**\n'
     '• Between 0.33 and 0.34 sit 0.331, 0.335, 0.339…\n'
     '• Go one seat smaller and the room appears.',
     hint='Zoom in one seat and the gap opens up.')
card(C, 'A number line settles it',
     '**Further right on the number line means greater — decimals included.**\n'
     '• 0.5 sits right of 0.45, so 0.5 is greater.\n'
     '• Drawing the line beats arguing about digits.',
     hint='When two decimals argue, the number line is the referee.')

q(Q, 1, 'Two seeds sprouted to 4.29 cm and 4.31 cm. Which comparison is true?',
  ['4.31 > 4.29', '4.29 > 4.31', '4.29 = 4.31', '4.31 < 4.29'], 0,
  'Ones tie — walk to the tenths.',
  ['Line up the points: 4.29 and 4.31.',
   'Ones tie at 4.',
   'Tenths: 3 > 2, so 4.31 is greater.'],
  '**4.31 > 4.29.** The tenths seat decides; the hundredths never get a vote.',
  'The first differing seat always finishes the comparison.')
q(Q, 1, 'Which number makes this true?  ___ > 6.35',
  ['6.4', '6.29', '6.35', '6.349'], 0,
  'Pad everything to hundredths and compare.',
  ['6.4 = 6.40; compare with 6.35: tenths tie? No — 4 > 3. Greater. ✓',
   '6.29: tenths 2 < 3. Smaller.',
   '6.349: 6.349 vs 6.350 — hundredths 4 < 5. Smaller.',
   'Only 6.4 clears the bar.'],
  '**6.4.** Padded to 6.40, its tenths beat 6.35\'s.',
  'A shorter decimal can absolutely be the bigger one.')
q(Q, 2, 'Tomas says 12.68 is greater than 12.8 because 68 is greater than 8. What should you tell him?',
  ['Pad 12.8 to 12.80 — then 80 hundredths beats 68 hundredths',
   'He is right — more digits after the point means a bigger number',
   'The two numbers are equal once you drop the zeros',
   'You cannot compare decimals with different lengths'], 0,
  'The digits after the point are not a whole number — they are seats.',
  ['68 and 8 are not comparable as written — they occupy different seats.',
   'Annex a zero: 12.8 = 12.80.',
   'Now compare hundredths against hundredths: 80 > 68.',
   'So 12.8 is the greater number.'],
  '**Pad first, then compare.** 12.80 vs 12.68 — the tenths seat (8 > 6) settles it.',
  'Reading decimal digits as one whole number is the single commonest comparison error.')
q(Q, 2, 'Which decimal sits between 0.42 and 0.43?',
  ['0.425', '0.435', '0.415', '0.44'], 0,
  'Zoom in one seat — thousandths.',
  ['Write the ends as thousandths: 0.420 and 0.430.',
   '0.425 sits between 420 and 430 thousandths. ✓',
   '0.415 is below 0.420; 0.435 and 0.44 are above 0.430.'],
  '**0.425.** One seat deeper and there is room to stand between any two decimals.',
  'This trick — pad, then slide between — works between ANY two unequal decimals.')
q(Q, 2, 'At a gymnastics meet, the beam scores were 14.200, 15.133, 15.500, and 15.166. Which score was highest?',
  ['15.500', '15.166', '15.133', '14.200'], 0,
  'Whole parts first, then walk right.',
  ['14.200 loses on the whole part immediately.',
   'Among the 15s, compare tenths: 5, 1, 1.',
   '15.500\'s five tenths beats both others.'],
  '**15.500.** One seat of tenths outweighs any amount of hundredths.',
  'Judges write three decimals so ties are rare — the comparison rules are the same ones you know.')
q(Q, 2, 'Which of these comparisons is true?',
  ['0.1 < 0.125', '0.2 < 0.125', '0.125 > 0.13', '0.126 < 0.125'], 0,
  'Pad everything to three places before judging.',
  ['0.1 = 0.100, and 100 < 125 thousandths. True. ✓',
   '0.2 = 0.200 > 0.125 — so that one is false.',
   '0.125 vs 0.130: 125 < 130 — false.',
   '0.126 vs 0.125: 126 > 125 — false.'],
  '**0.1 < 0.125.** Padding to thousandths turns every option into a plain integer comparison.',
  'Pad first, and the decimals stop being tricky at all.')
oq(Q, 2, 'Put these ribbon lengths in order from SHORTEST to longest.',
  ['0.309 m', '0.35 m', '0.39 m', '0.4 m'],
  'Pad all four to thousandths first.',
  ['Pad: 0.309, 0.350, 0.390, 0.400.',
   'As thousandths: 309, 350, 390, 400.',
   'Order: 0.309 < 0.35 < 0.39 < 0.4.'],
  '**0.309, 0.35, 0.39, 0.4.** Padded to thousandths the order reads straight off.',
  'The longest-looking decimal was the smallest — length of the writing means nothing.')
q(Q, 3, 'A scoreboard shows Ana\'s floor score as 15.■6, with one digit smudged. Her beam score is 15.36. Which smudged digit would make her floor score HIGHER than her beam score?',
  ['4', '2', '1', '0'], 0,
  'The smudge sits in the tenths seat.',
  ['Floor: 15.■6 — the smudge is the tenths digit.',
   'Beam: 15.36 has 3 in the tenths.',
   'Higher floor score needs tenths above 3 — of the choices, only 4 works: 15.46 > 15.36.'],
  '**4.** Any tenths digit greater than 3 wins; 4 is the only such choice offered.',
  'One seat pinned down the whole answer — that is place value doing the work.')
q(Q, 3, 'Maya weighed 4.16 kg of apples and Jo weighed some too. Jo\'s bag was heavier. Which could be Jo\'s weight?',
  ['4.2 kg', '4.09 kg', '4.15 kg', '4.106 kg'], 0,
  'Pad each option against 4.160.',
  ['Pad the target: 4.16 = 4.160.',
   '4.2 = 4.200 > 4.160. ✓',
   '4.09 (4.090), 4.15 (4.150) and 4.106 all fall below 4.160.'],
  '**4.2 kg.** The only option whose padded form beats 4.160.',
  'Carrying the units (kg) through the compare keeps the answer meaning something.')
q(Q, 3, 'If two decimals agree in every seat except the thousandths, what is the LARGEST amount they can differ by?',
  ['0.009', '0.9', '0.01', '0.1'], 0,
  'How far apart can two thousandths digits be?',
  ['Only the thousandths digits differ.',
   'The farthest apart two digits can be is 0 and 9.',
   'That difference is 9 thousandths: 0.009.'],
  '**0.009.** Nine thousandths — the widest gap a single seat can hold.',
  'A seat bounds how much it can matter. That is why early seats always outrank later ones.')
build(C, Q, 'unit-m35', 'Topic 3 · 3-5 Comparing and Ordering Decimals', 10,
      'Lesson 3-5: compare decimals by stacking the decimal points, annexing zeros to equal length, and walking left to right until the first seat disagrees. Order lists the same way, and find decimals between any two others by going one seat deeper.',
      'The "more digits looks bigger" instinct from whole numbers actively misleads here — 12.8 beats 12.68. Unlearning that one reflex is most of the lesson, and it matters everywhere measurements get compared.',
      [('Compare two decimals and say which seat decided it.', 'source'),
       ('Order a set of decimals by padding to equal length.', 'source'),
       ('Name a decimal between two given decimals.', 'source')],
      'The Tomas question is the lesson\'s core error, verbatim from how kids actually reason. The last question (largest possible thousandths difference) is stretch material — a miss there is fine; a miss on Tomas is worth a conversation.',
      ('Cards, then the quiz. The ordering question is worth doing slowly with the padding written out.', 12),
      'content/math-t3-35.json', SRC, SRCLONG)

# ---------------------------------------------------------------- 3-6
C, Q = [], []
card(C, 'The rounding place',
     '**Underline the seat you are rounding to — the decision happens there.**\n'
     '• Round 2.36 to the nearest tenth: the 3 is the rounding digit.\n'
     '• Everything left of it never changes.',
     hint='Mark the seat first; half of rounding errors are seat errors.')
card(C, 'Look one seat right',
     '**The single digit to the RIGHT of the rounding place decides.**\n'
     '• 5 or greater → the rounding digit goes up one.\n'
     '• Less than 5 → it stays.',
     hint='One digit votes. The rest of the number is not consulted.')
card(C, 'Drop what follows',
     '**After deciding, drop every digit right of the rounding place.**\n'
     '• 2.36 → 2.4 (not 2.40 — the hundredths seat is gone).\n'
     '• Rounding to a whole number drops the point too.',
     hint='Round, then cut. Never keep the tail.')
card(C, 'The number line picture',
     '**Rounding asks: which mark is this number closer to?**\n'
     '• 2.36 sits between 2.3 and 2.4, past the halfway mark 2.35.\n'
     '• Halfway itself rounds up, by agreement.',
     hint='Closer mark wins; exact middle goes up.')
card(C, 'No chain rounding',
     '**Round in ONE step from the original number.**\n'
     '• 448 to the nearest hundred: 4 tens says stay — 400.\n'
     '• Rounding 448 → 450 → 500 uses a digit that was never the decider.',
     hint='One look, one decision. Rounding a rounding is a different number.')

q(Q, 1, 'A lizard measures 4.38 cm. What is its length to the nearest tenth?',
  ['4.4 cm', '4.3 cm', '4.0 cm', '4.39 cm'], 0,
  'The hundredths digit casts the only vote.',
  ['Rounding place: tenths — the 3.',
   'Look one right: 8, which is 5 or more.',
   'The 3 goes up: 4.4. The 8 is dropped.'],
  '**4.4 cm.** The 8 votes up, then disappears.',
  'The answer to a nearest-tenth question always ends at the tenths seat.')
q(Q, 1, 'A taxi charges by the whole mile, rounding the distance to the nearest mile. The meter reads 7.3 miles. How many miles is the fare based on?',
  ['7', '8', '7.5', '7.3'], 0,
  'Which whole number is 7.3 closer to?',
  ['Rounding place: the ones seat.',
   'One right: 3, less than 5.',
   'The 7 stays; drop the rest: 7.'],
  '**7 miles.** Three tenths is short of halfway, so the meter rounds down.',
  'Real systems round constantly — knowing WHICH way protects your wallet.')
q(Q, 1, 'What is 0.762 rounded to the nearest hundredth?',
  ['0.76', '0.77', '0.7', '0.762'], 0,
  'The thousandths digit is the voter.',
  ['Rounding place: hundredths — the 6.',
   'One right: 2, less than 5.',
   'The 6 stays; the 2 is dropped: 0.76.'],
  '**0.76.** A 2 in the deciding seat means nothing moves.',
  'Rounding never adds precision — it always shortens.')
q(Q, 2, 'Which numbers round to 12.7 when rounded to the nearest tenth?',
  ['12.66 and 12.74', '12.75 and 12.66', '12.64 and 12.74', '12.60 and 12.76'], 0,
  'The winners live from 12.65 up to (but not including) 12.75.',
  ['To land on 12.7, a number must be at least 12.65 and below 12.75.',
   '12.66 ✓ and 12.74 ✓ both sit inside that band.',
   '12.75 rounds up to 12.8; 12.64 rounds down to 12.6; 12.60 rounds to 12.6.'],
  '**12.66 and 12.74.** Both live inside the 12.65–12.749… band that rounds to 12.7.',
  'Every rounding target owns a band of numbers, half a seat wide on each side.')
q(Q, 2, 'A grocery scale shows 2.09 kg on one bag of rice and 2.36 kg on another. Nadia needs the bag closer to 2 kg. Rounding both to the nearest whole number says each is "about 2". How should she actually choose?',
  ['Compare the leftover parts: 0.09 < 0.36, so the 2.09 kg bag is closer',
   'Round to the nearest whole number again to double-check',
   'Pick the heavier bag, since rounding dropped more from it',
   'The bags are the same distance from 2 kg'], 0,
  'Rounding threw away exactly the information she needs.',
  ['Both bags round to 2 — rounding cannot break the tie.',
   'Look at the parts rounding discarded: 0.09 and 0.36.',
   '0.09 < 0.36, so 2.09 kg sits closer to 2 kg.'],
  '**Compare what rounding dropped.** 2.09 is only 0.09 away; 2.36 is 0.36 away.',
  'Rounding is for communicating, not for deciding — the dropped digits still exist.')
q(Q, 2, 'What is 84.735 rounded to the nearest hundredth?',
  ['84.74', '84.73', '84.7', '84.8'], 0,
  'The dropped digit is exactly 5.',
  ['Rounding place: hundredths — the 3.',
   'One right: 5 — the agreed rule says up.',
   '84.735 → 84.74.'],
  '**84.74.** Exactly halfway rounds up, every time, by agreement.',
  'The halfway rule is a convention — but it is THE convention, so use it.')
q(Q, 3, 'Priya says 448 rounds to 500, because 448 rounds to 450 and 450 rounds to 500. What should you tell her?',
  ['Round once from 448: the tens digit is 4, so it rounds to 400',
   'She is right — rounding in stages is more accurate',
   '448 is exactly halfway, so either answer works',
   'It rounds to 500 only when the ones digit is 8'], 0,
  'Who is allowed to vote when rounding to the nearest hundred?',
  ['Rounding 448 to the nearest hundred: the decider is the TENS digit.',
   'That digit is 4 — less than 5 — so 448 → 400.',
   'Chaining through 450 lets the ones digit influence a decision it has no vote in.',
   'On the number line: 448 is 48 from 400 but 52 from 500.'],
  '**Round once: 400.** Chain rounding lets the wrong digit vote; 448 is genuinely closer to 400.',
  'One original number, one look, one decision. Rounding a rounding answers a different question.')
q(Q, 3, 'To the nearest hundred, what is the GREATEST whole number that rounds to 6,200?',
  ['6,249', '6,250', '6,199', '6,299'], 0,
  'Where does the round-to-6,200 band end?',
  ['Numbers round to 6,200 from 6,150 up to 6,249.',
   '6,250 tips up to 6,300 by the halfway rule.',
   'So the greatest is 6,249.'],
  '**6,249.** One more and the halfway rule hands it to 6,300.',
  'Asking for the band\'s edges is rounding run backwards — same rule, reversed.')
q(Q, 3, 'A rain gauge reads 3.472 inches. Marcus rounds it to the nearest tenth and writes 3.4. What went wrong?',
  ['The hundredths digit is 7, so the tenths should have gone up to 3.5',
   'Nothing — 3.472 does round to 3.4',
   'He should have kept three decimal places',
   'He rounded to the nearest hundredth by mistake'], 0,
  'Find the voter and count its vote.',
  ['Rounding place: tenths — the 4.',
   'One right: 7, which is 5 or more.',
   'The 4 must go up: 3.472 → 3.5.'],
  '**The 7 votes up — it is 3.5.** He looked at the right seat but ignored its vote.',
  'The commonest rounding slip is doing every step except the actual increase.')
q(Q, 3, 'Which number, rounded to the nearest tenth, gives a DIFFERENT result than rounded to the nearest hundredth first and then to the nearest tenth?',
  ['0.348', '0.32', '0.36', '0.371'], 0,
  'Hunt for a number where chaining flips the tenths decision.',
  ['0.348 direct to tenths: hundredths digit 4 → stays 0.3.',
   '0.348 to hundredths first: 0.35. Then to tenths: 5 votes up → 0.4.',
   'Direct and chained disagree: 0.3 vs 0.4.',
   'The other options give the same answer both ways.'],
  '**0.348.** Direct rounding says 0.3; chaining through 0.35 says 0.4 — proof the chain is a different calculation.',
  'This is Priya\'s error from earlier, caught in the act with decimals.')
build(C, Q, 'unit-m36', 'Topic 3 · 3-6 Rounding Decimals', 10,
      'Lesson 3-6: round decimals by marking the rounding place, letting the single digit to its right decide (5 or greater rounds up), and dropping everything after. The number line shows why, and rounding must happen in one step from the original number.',
      'Rounding is the everyday math skill — money, measurements, estimates all pass through it. The chain-rounding error is worth killing early because it FEELS more careful while being wrong.',
      [('Round a decimal to a named place: whole, tenth, or hundredth.', 'source'),
       ('Name the numbers that round to a given target — the band, both edges.', 'source'),
       ('Explain why rounding in stages can give a wrong answer.', 'source')],
      'Two critique questions carry this lesson: Priya\'s chain rounding (448 → 450 → 500) and Marcus stopping short of the actual increase. The last question shows chaining failing with decimals — it is hard, and a miss there costs nothing.',
      ('Cards, then the quiz. If the band questions (which numbers round TO 12.7) wobble, draw the number line.', 12),
      'content/math-t3-36.json', SRC, SRCLONG)

# ---------------------------------------------------------------- 3-7
C, Q = [], []
card(C, 'A decimal chart has structure',
     '**In a hundredths chart, each step right adds 0.01 and each step down adds 0.1.**\n'
     '• Across a row: 0.31, 0.32, 0.33…\n'
     '• Down a column: 0.02, 0.12, 0.22…',
     hint='Right = pennies. Down = dimes.')
card(C, 'The thousandths chart',
     '**Same shape, smaller steps: right adds 0.001, down adds 0.01.**\n'
     '• Across: 0.031, 0.032, 0.033…\n'
     '• Down: 0.004, 0.014, 0.024…',
     hint='Same map, zoomed in ten times.')
card(C, 'The row-end change',
     '**The last cell of a row completes the next tenth (or hundredth).**\n'
     '• …0.08, 0.09, then 0.1 — the row ends by rolling the seat over.\n'
     '• Like an odometer: the small wheel fills up and the next one ticks.',
     hint='Rows end on a rollover, not on a pattern break.')
card(C, 'Use structure',
     '**Find the rule the chart follows, then let the rule fill the gaps.**\n'
     '• One missing cell = its neighbour plus one step.\n'
     '• Check a fill by walking to it two ways — row and column must agree.',
     hint='Do not compute cells — walk to them.')

q(Q, 1, 'In a hundredths chart, what number comes immediately to the right of 0.36?',
  ['0.37', '0.46', '0.35', '0.361'], 0,
  'One step right is one hundredth.',
  ['Across a row, each cell adds 0.01.',
   '0.36 + 0.01 = 0.37.',
   'Check against the down rule: below 0.36 would be 0.46 — a different move.'],
  '**0.37.** One penny more.',
  '0.46 would be the cell BELOW — down adds a dime, not a penny.')
q(Q, 1, 'In a hundredths chart, what number sits directly BELOW 0.24?',
  ['0.34', '0.25', '0.23', '0.14'], 0,
  'Down a column adds a tenth.',
  ['Down one row adds 0.1.',
   '0.24 + 0.1 = 0.34.',
   'The hundredths digit (4) never moves — only the tenths ticks.'],
  '**0.34.** The hundredths digit stays; the tenths digit ticks up.',
  'Below and to-the-right are different moves — a dime versus a penny.')
q(Q, 1, 'A thousandths chart row reads: 0.041, 0.042, ■, 0.044. What is the missing number?',
  ['0.043', '0.05', '0.0425', '0.34'], 0,
  'The row counts by thousandths.',
  ['Across this chart each cell adds 0.001.',
   '0.042 + 0.001 = 0.043.',
   'Check the other side: 0.043 + 0.001 = 0.044. ✓'],
  '**0.043.** Both neighbours agree, which is the check that matters.',
  'A gap with two neighbours can always be verified twice.')
q(Q, 2, 'In a thousandths chart, what number sits directly below 0.032?',
  ['0.042', '0.033', '0.132', '0.032'], 0,
  'Down adds 0.01 in this chart.',
  ['In a thousandths chart, down one row adds 0.01.',
   '0.032 + 0.01 = 0.042.',
   'Check: ten across-steps of 0.001 make one down-step. ✓'],
  '**0.042.** The hundredths seat ticks; the thousandths digit rides along unchanged.',
  'Zoomed in ten times, "down adds a dime" becomes "down adds a penny".')
q(Q, 2, 'A hundredths chart row ends: …, 0.28, 0.29, ■. What is the last number in the row?',
  ['0.3', '0.291', '0.299', '0.4'], 0,
  'The row ends by completing a tenth.',
  ['One more hundredth after 0.29 is 0.30.',
   '0.30 = 0.3 — the row ends on the rolled-over tenth.',
   'The next row then starts at 0.31.'],
  '**0.3.** Twenty-nine hundredths plus one more makes three full tenths.',
  'The rollover is why 0.3 belongs at the end of the 0.2-something row.')
q(Q, 2, 'Ravi walks four cells RIGHT from 0.052 in a thousandths chart. Where does he land?',
  ['0.056', '0.092', '0.452', '0.0524'], 0,
  'Four steps, one thousandth each.',
  ['Each step right adds 0.001.',
   'Four steps add 0.004.',
   '0.052 + 0.004 = 0.056.'],
  '**0.056.** Steps accumulate — four thousandths in total.',
  '0.092 is the four-steps-DOWN answer; direction is half the question.')
q(Q, 2, 'One cell of a hundredths chart can be reached by going right from 0.43 or down from 0.34. What number is in it?',
  ['0.44', '0.35', '0.43', '0.53'], 0,
  'Both walks must land on the same value.',
  ['Right from 0.43 adds 0.01: 0.44.',
   'Down from 0.34 adds 0.1: 0.44.',
   'Both roads agree: the cell holds 0.44.'],
  '**0.44.** Two different walks, one destination — the chart\'s structure guarantees it.',
  'Agreeing paths are the built-in answer check. Use them.')
q(Q, 3, 'A chart counts by thousandths across each row. If the chart instead counted by hundredths, how would the down-a-column step change?',
  ['It would become 0.1 instead of 0.01', 'It would become 0.001', 'It would stay 0.01', 'Columns would stop following a pattern'], 0,
  'The down-step is always ten times the across-step.',
  ['In every chart of this shape, down = 10 × across.',
   'Across by hundredths (0.01) makes down 0.1.',
   'The structure survives the zoom — only the step sizes scale.'],
  '**Down becomes 0.1.** A row holds ten cells, so a full row is ten across-steps — that is the down-step.',
  'Understanding WHY down is 10 × across beats memorising either number.')
oq(Q, 3, 'Put these chart cells in the order you would meet them reading a thousandths chart left to right: they are the last two of one row and the first two of the next.',
  ['0.019', '0.02', '0.021', '0.022'],
  'One of these is a rollover in disguise.',
  ['0.019 + 0.001 = 0.020 = 0.02 — the rollover ends the row.',
   'The next row starts 0.021, then 0.022.',
   'Order: 0.019, 0.02, 0.021, 0.022.'],
  '**0.019, 0.02, 0.021, 0.022.** The short-looking 0.02 is really 0.020 sitting snugly in sequence.',
  'Written length says nothing — pad to three places and the order is obvious.')
q(Q, 3, 'Jun fills a missing hundredths-chart cell by adding 0.01 to the cell ABOVE it. His answer disagrees with the row neighbours. What did he do wrong?',
  ['Above-to-below adds 0.1 in this chart, not 0.01',
   'Nothing — neighbours in a chart often disagree',
   'He should have subtracted 0.01 instead',
   'He read the wrong chart entirely'], 0,
  'Which move adds 0.01 in a hundredths chart?',
  ['In a hundredths chart, 0.01 is the ACROSS step.',
   'The down step is 0.1.',
   'He applied the across rule to a down move, so his cell is off by 0.09.',
   'The row neighbours caught it — two paths must agree.'],
  '**He used the across-step for a down move.** Down adds 0.1 here; his fill is 0.09 short.',
  'The disagreement was the chart itself telling him to recheck — structure is self-auditing.')
build(C, Q, 'unit-m37', 'Topic 3 · 3-7 Patterns in Decimal Charts', 10,
      'Lesson 3-7 is the topic\'s thinking lesson: hundredths and thousandths charts follow two rules (a small step across, a step ten times bigger down), rows end on a rollover, and missing cells are found by walking the structure — with two agreeing paths as the built-in check.',
      'This is less about decimals than about USING structure — finding a rule and letting it do the work. That habit is the difference between computing forty cells and understanding one chart.',
      [('State the across-step and down-step of a hundredths or thousandths chart.', 'source'),
       ('Fill a missing cell and verify it by a second path.', 'source'),
       ('Explain the rollover at the end of a row.', 'source')],
      'The rollover (…0.019, 0.02, 0.021…) is where the wheels come off for most kids — 0.02 looks too short to belong. The ordering question targets exactly that. The counterfactual (how the down-step scales) is stretch material.',
      ('Cards, then the quiz — and the second card is worth an extra beat, since the thousandths chart runs the whole show.', 12),
      'content/math-t3-37.json', SRC, SRCLONG)

# ---------------------------------------------------------------- Topic Review
C, Q = [], []
card(C, 'The one chart behind Topic 3',
     '**Everything in this topic is a single place-value chart, read left or right of the point.**\n'
     '• Exponents name the big seats; thousandths name the small ones.\n'
     '• Every seat is worth 10 times its right-hand neighbour.',
     hint='One ladder. Powers of 10 go up it; decimals go down it.')
card(C, 'Exponents, in one line',
     '**The exponent counts the 10s, and equals the zeros in the product.**\n'
     '• 10⁵ = 100,000. And 6 × 10⁴ = 60,000.',
     hint='Count zeros ↔ read exponent, both directions.')
card(C, 'Decimal ↔ fraction, in one line',
     '**Decimal places match the zeros in the denominator.**\n'
     '• 0.083 = 83/1,000 — three places, three zeros.',
     hint='Places = zeros. Pad the front, never the back.')
card(C, 'Equivalence, in one line',
     '**End zeros are free; a zero between the point and the digits changes everything.**\n'
     '• 2.5 = 2.50 = 2.500, but 2.05 is a different number.',
     hint='WHERE the zero sits is the entire question.')
card(C, 'Comparing, in one line',
     '**Stack the points, pad to equal length, first differing seat wins.**\n'
     '• 12.8 vs 12.68 → 12.80 vs 12.68 → tenths decide.',
     hint='Pad, then walk left to right. Stop at the first disagreement.')
card(C, 'Rounding, in one line',
     '**Mark the seat, let the next digit vote (5 up), drop the tail — in ONE step.**\n'
     '• 448 to the nearest hundred is 400, never via 450.',
     hint='One look, one decision, no chaining.')
card(C, 'Chart structure, in one line',
     '**Across is the small step; down is ten of them; rows end on a rollover.**\n'
     '• Two paths to a cell must agree — that is your check.',
     hint='Walk the chart; don\'t compute it.')

q(Q, 1, 'A warehouse stores 7 × 10⁴ boxes. How many boxes is that?',
  ['70,000', '7,000', '700,000', '28'], 0,
  'Attach as many zeros as the exponent.',
  ['10⁴ = 10,000 — four zeros.',
   '7 × 10,000 = 70,000.',
   'Check: the product keeps exactly four zeros, matching the exponent.'],
  '**70,000.** Four zeros follow the 7.',
  'The 28 trap is 7 × 4 — the exponent never multiplies directly.')
q(Q, 1, 'What is the value of the 5 in 2,571,368?',
  ['500,000', '50,000', '5,000,000', '5,000'], 0,
  'Find the seat before the value.',
  ['Count seats from the right: ones, tens, hundreds, thousands, ten-thousands, hundred-thousands.',
   'The 5 lands in the hundred-thousands seat.',
   '5 × 100,000 = 500,000.'],
  '**500,000.** The seat multiplies the digit.',
  'Value questions are seat questions in disguise.')
q(Q, 1, 'Which decimal equals 6/1,000?',
  ['0.006', '0.06', '0.6', '6.000'], 0,
  'Three zeros in the denominator, three decimal places.',
  ['The denominator 1,000 says thousandths.',
   'Thousandths means exactly three decimal places.',
   '006 fills them: 0.006 — the front zeros hold the seats.'],
  '**0.006.** Pad the front to fill the seats.',
  'Places and zeros always match — count them both.')
q(Q, 1, 'Which decimal is equivalent to 8.20?',
  ['8.2', '8.02', '8.22', '0.82'], 0,
  'Which option only drops an END zero?',
  ['8.20\'s final zero is after the last nonzero digit — free.',
   'Dropping it gives 8.2, the same number.',
   'Say both: "twenty hundredths", "two tenths" — the same amount twice.'],
  '**8.2.** Twenty hundredths is two tenths.',
  '8.02 moves the 2 to a different seat — that zero is load-bearing.')
q(Q, 1, 'Two snail trails measure 0.54 m and 0.6 m. Which comparison is true?',
  ['0.6 > 0.54', '0.54 > 0.6', '0.54 = 0.6', '0.6 < 0.54'], 0,
  'Pad 0.6 before comparing.',
  ['0.6 = 0.60.',
   'Tenths: 6 > 5.',
   'So 0.6 is the longer trail.'],
  '**0.6 > 0.54.** The shorter-written decimal is the bigger number here.',
  'Pad first and the illusion disappears.')
q(Q, 1, 'What is 7.85 rounded to the nearest whole number?',
  ['8', '7', '7.9', '7.8'], 0,
  'The tenths digit votes.',
  ['Rounding place: ones — the 7.',
   'One right: 8, which is 5 or more.',
   '7.85 → 8, point and tail dropped.'],
  '**8.** The 8 in the tenths votes up.',
  'Whole-number rounding drops the decimal point entirely.')
q(Q, 2, 'A national park recorded 4,060,000 visitors. Which is its expanded form using exponents?',
  ['(4 × 10⁶) + (6 × 10⁴)', '(4 × 10⁶) + (6 × 10⁵)', '(4 × 10⁵) + (6 × 10⁴)', '(4 × 10⁶) + (6 × 10³)'], 0,
  'Seat each nonzero digit.',
  ['The 4 is in the millions seat: 4 × 10⁶.',
   'The 6 is in the ten-thousands seat: 6 × 10⁴.',
   'Sum: (4 × 10⁶) + (6 × 10⁴).'],
  '**(4 × 10⁶) + (6 × 10⁴).** Two filled seats, two terms.',
  'Silent seats appear in standard form as zeros and in expanded form not at all.')
q(Q, 2, 'How is "three and nine hundredths" written as a decimal?',
  ['3.09', '3.9', '3.009', '39.0'], 0,
  '"Hundredths" fixes two decimal places.',
  ['Whole part 3; "and" is the point.',
   'Nine hundredths needs two places: 09.',
   'So 3.09.'],
  '**3.09.** The zero holds the tenths seat.',
  '3.9 would be "three and nine TENTHS" — the seat name matters.')
q(Q, 2, 'In 44,000, how do the two 4s compare?',
  ['The left 4 is worth 10 times the right 4', 'The left 4 is worth 100 times the right 4', 'The 4s are worth the same', 'The right 4 is worth 10 times the left 4'], 0,
  'Adjacent seats.',
  ['Left 4: ten-thousands, worth 40,000.',
   'Right 4: thousands, worth 4,000.',
   'One seat apart: a factor of exactly 10.'],
  '**10 times.** Adjacent seats always differ by one factor of 10.',
  'Two seats apart would make it 100 — the steps stack.')
q(Q, 2, 'Which number sits between 7.1 and 7.2?',
  ['7.15', '7.21', '7.09', '7.25'], 0,
  'Pad the ends to hundredths.',
  ['7.1 = 7.10 and 7.2 = 7.20.',
   '7.15 sits between 710 and 720 hundredths. ✓',
   'The others land outside the band.'],
  '**7.15.** Zoom one seat deeper and the room appears.',
  'Between any two unequal decimals there is always another — always.')
q(Q, 2, 'A stopwatch shows 58.276 seconds. What is the time to the nearest hundredth?',
  ['58.28 s', '58.27 s', '58.3 s', '58.276 s'], 0,
  'The thousandths digit votes.',
  ['Rounding place: hundredths — the 7.',
   'One right: 6, five or more.',
   '58.276 → 58.28.'],
  '**58.28 s.** The 6 votes up and vanishes.',
  'Race times round to hundredths for exactly this reason — carrying the units matters.')
q(Q, 2, 'In a hundredths chart, one cell is reached going right from 0.67 or down from 0.58. What is in it?',
  ['0.68', '0.59', '0.77', '0.57'], 0,
  'Both walks must agree.',
  ['Right from 0.67: +0.01 = 0.68.',
   'Down from 0.58: +0.1 = 0.68.',
   'Agreement confirms it.'],
  '**0.68.** Two roads, one cell.',
  'When the two paths disagree, the error is yours, not the chart\'s.')
q(Q, 2, 'Which equation is FALSE?',
  ['9 × 10³ = 90,000', '9 × 10⁴ = 90,000', '9 × 10² = 900', '9 × 10⁵ = 900,000'], 0,
  'Count each option\'s zeros against its exponent.',
  ['9 × 10³ = 9,000 — but the option claims 90,000. False. ✓',
   '9 × 10⁴ = 90,000 ✓ true.',
   '9 × 10² = 900 and 9 × 10⁵ = 900,000 — both true.'],
  '**9 × 10³ = 90,000 is the false one.** Three zeros make 9,000.',
  'Hunting the FALSE statement forces you to verify all four — that is the point.')
q(Q, 3, 'Kavya says 0.480 is greater than 0.48 "because it has more digits". What should you tell her?',
  ['They are equal — the extra zero is after the last nonzero digit',
   'She is right — longer decimals are greater',
   '0.48 is actually the greater one',
   'They cannot be compared without a number line'], 0,
  'Is that zero free or load-bearing?',
  ['0.480 only annexes a zero to 0.48.',
   'End zeros rename tenths/hundredths into thousandths without changing the amount.',
   '480 thousandths = 48 hundredths.'],
  '**They are equal.** Written length says nothing about size.',
  'The same instinct wrongly says 12.68 > 12.8 — padding fixes both.')
q(Q, 3, 'A number rounds to 6.3 to the nearest tenth AND to 6.28 to the nearest hundredth. Which could it be?',
  ['6.283', '6.251', '6.292', '6.234'], 0,
  'Two bands must overlap — solve each, then intersect.',
  ['Nearest hundredth 6.28 needs: 6.275 up to but not including 6.285.',
   'Nearest tenth 6.3 needs: 6.25 up to but not including 6.35.',
   '6.283 sits inside both bands. ✓',
   '6.251 rounds to 6.25; 6.292 rounds to 6.29; 6.234 rounds to 6.23 and 6.2 — each fails a band.'],
  '**6.283.** Inside the 6.28 band, which itself sits inside the 6.3 band.',
  'Two rounding facts about one number are two overlapping bands — the answer lives in the overlap.')
q(Q, 3, 'Milo claims that moving a digit two seats left multiplies its value by 20. What should you tell him?',
  ['Each seat multiplies by 10, so two seats multiply by 100',
   'He is right — two seats, 10 each, makes 20',
   'Two seats left divides the value by 100',
   'The factor depends on which digit moves'], 0,
  'Do seat-factors add or multiply?',
  ['One seat left: × 10.',
   'A second seat left: × 10 again.',
   'The factors MULTIPLY: 10 × 10 = 100, not 10 + 10 = 20.'],
  '**× 100, not × 20.** Place-value steps multiply; they never add.',
  'His error is treating a multiplicative ladder like an additive one — the single deepest misconception in this topic.')
q(Q, 3, 'Which list is ordered from least to greatest?',
  ['0.098, 0.9, 0.908, 0.98', '0.9, 0.098, 0.908, 0.98', '0.098, 0.908, 0.9, 0.98', '0.098, 0.9, 0.98, 0.908'], 0,
  'Pad all four to thousandths.',
  ['Pad: 0.098, 0.900, 0.908, 0.980.',
   'As integers: 98, 900, 908, 980.',
   'That ascending order is exactly the first list.'],
  '**0.098, 0.9, 0.908, 0.98.** Padded, the order is just integer order.',
  'Every wrong list here trips on 0.9 looking small — padding is the cure.')
q(Q, 3, 'A relay team\'s four splits, in seconds, were 12.06, 12.6, 12.066, and 12.61. The anchor ran the FASTEST split. Which time was the anchor\'s?',
  ['12.06', '12.6', '12.066', '12.61'], 0,
  'Fastest means smallest — pad to thousandths.',
  ['Pad: 12.060, 12.600, 12.066, 12.610.',
   'Smallest is 12.060.',
   'So the anchor ran 12.06 seconds.'],
  '**12.06 s.** Smaller time, faster runner — and 12.06 < 12.066 by six thousandths.',
  'Fastest-vs-greatest is a reading question stacked on a math question. Read first.')
q(Q, 3, 'Round 9.996 to the nearest hundredth.',
  ['10.00', '9.99', '9.90', '9.996'], 0,
  'The vote forces a cascade of rollovers.',
  ['Rounding place: hundredths — the second 9.',
   'One right: 6 votes up.',
   '9.99 + 0.01 rolls all the way over: 10.00.',
   'The zeros after the point show the precision you rounded to.'],
  '**10.00.** The round-up ripples through every 9.',
  'Keeping the two zeros records that you rounded to hundredths — 10 alone loses that.')
q(Q, 3, 'One digit of 5.7■4 is hidden. Rounded to the nearest hundredth, the number is 5.72. What is the hidden digit?',
  ['2', '1', '3', '7'], 0,
  'The 4 in the thousandths votes DOWN.',
  ['The thousandths digit is 4 — less than 5 — so rounding leaves the hundredths digit alone.',
   'After rounding, the hundredths digit reads 2.',
   'Since nothing changed, the hidden digit IS 2.'],
  '**2.** A down-vote means the rounded digit was never touched.',
  'Running the rounding machine backwards is the surest test you understand it forwards.')
q(Q, 2, 'A thousandths chart row ends …0.038, 0.039, ■. What completes the row?',
  ['0.04', '0.0391', '0.05', '0.14'], 0,
  'The rollover completes a hundredth.',
  ['One more thousandth after 0.039 is 0.040.',
   '0.040 = 0.04 — the rolled-over hundredth ends the row.',
   'The next row then opens at 0.041.'],
  '**0.04.** Forty thousandths is four hundredths.',
  'The short-looking answer is the rollover in disguise — every row ends with one.')
oq(Q, 2, 'Order these from least to greatest.',
  ['3 × 10²', '3,200', '3 × 10⁴', '300,000'],
  'Turn everything into standard form first.',
  ['3 × 10² = 300.',
   '3 × 10⁴ = 30,000.',
   'Standard: 300, 3,200, 30,000, 300,000.',
   'That is the order.'],
  '**300, 3,200, 30,000, 300,000.** Convert first, order second.',
  'Mixed representations are only hard until everything speaks standard form.')
q(Q, 2, 'Which number is one-tenth of 4.7?',
  ['0.47', '47', '4.07', '0.047'], 0,
  'One seat right, every digit.',
  ['One-tenth slides each digit one seat right.',
   '4.7 → 0.47.',
   'Check: 0.47 × 10 = 4.7. ✓'],
  '**0.47.** The ladder works in both directions.',
  '47 is the ×10 answer — the direction of the slide is the whole question.')
q(Q, 1, 'Which fraction equals 0.219?',
  ['219/1,000', '219/100', '21.9/100', '219/10,000'], 0,
  'Count the decimal places.',
  ['Count the places right of the point: three.',
   'Three places means thousandths — denominator 1,000.',
   'So 0.219 = 219/1,000.'],
  '**219/1,000.** Three places, three zeros.',
  'The denominator is readable straight off the number of places.')
build(C, Q, 'unit-m3r', 'Topic 3 · Topic Review', 12,
      'The whole of Topic 3 in one pool: exponents and powers of 10, place value through millions, decimals to thousandths, equivalent decimals and their forms, comparing and ordering, rounding, and decimal-chart structure — served as mixed rounds so the skills interleave.',
      'A topic test asks everything at once, so practice should too. Deciding WHICH skill a question wants — exponent pattern, padding, rounding band — is itself the tested skill, and only mixed rounds train it.',
      [('Move between exponent, standard, expanded and word forms in both directions.', 'source'),
       ('Compare, order and squeeze between decimals by padding to equal length.', 'source'),
       ('Round decimals in one step and reason backwards from a rounded result.', 'source'),
       ('Use the ×10-per-seat structure to explain, not just compute.', 'added')],
      'The capstone for Topic 3. The three-level questions lean hard on critique-reasoning — Kavya, Milo, and the hidden-digit items are where understanding shows. If the mixed rounds go well, she is ready for whatever the class calls the Topic 3 test.',
      ('Two or three mixed rounds across different days beats one long sitting — the shuffle is the point.', 15),
      'content/math-t3-review.json', SRC, SRCLONG, capstone=True)

print('--- lessons 3-5 to 3-7 + review built ---')
