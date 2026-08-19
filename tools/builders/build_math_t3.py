# Topic 3 — Patterns and Products (the class's numbering; the material is the
# Grade 5 enVision book's Topic 1, which is how an accelerated 4th-grade year
# works). Source: "Textbook Topic 3 Lessons 3-1 to 3-7.pdf" in the Drive
# folder "Topic 3 - Patterns and Product". Seven lesson-a-day units + the
# Topic Review capstone, following the Topic 1/2 shelf exactly.
#
# Content rules in force: fresh scenarios (never the textbook's own items),
# every stem standalone, no positional references, both directions, at least
# one critique-reasoning item per lesson (the book's own signature move),
# balanced answer positions and option lengths.
from math_common import card, q, build

SRC = "Textbook Topic 3, Lessons 3-1 to 3-7 (Drive)"
SRCLONG = "enVision Math, Topic 3 textbook scan — Lessons 3-1 to 3-7 (Drive)"

# ---------------------------------------------------------------- 3-1
C, Q = [], []
card(C, 'Exponent',
     '**The small raised number that tells how many times to use the base as a factor.**\n'
     '• In 10³, the 3 means: multiply three 10s together.\n'
     '• 10³ = 10 × 10 × 10 = 1,000.',
     hint='The exponent counts copies, it never multiplies itself.')
card(C, 'Base',
     '**The number the exponent repeats.**\n'
     '• In 10³, the base is 10 — it is the number being multiplied.\n'
     '• The exponent only says how many times.',
     hint='Base = the big number on the ground floor.')
card(C, 'Power of 10',
     '**10 multiplied by itself one or more times: 10, 100, 1,000, 10,000…**\n'
     '• 10¹ = 10, 10² = 100, 10³ = 1,000.\n'
     '• Every step up multiplies by another 10.',
     hint='Each power is one storey higher — ten times higher.')
card(C, 'The zeros pattern',
     '**For a power of 10, the exponent equals the number of zeros in the product.**\n'
     '• 10⁴ = 10,000 — four zeros.\n'
     '• This is the pattern that makes exponents fast to read.',
     hint='Count the zeros; you have read the exponent.')
card(C, 'Multiplying by a power of 10',
     '**Write the other factor, then attach as many zeros as the exponent.**\n'
     '• 7 × 10³ = 7,000.\n'
     '• The factor does not change — only zeros are attached.',
     hint='The 7 stays a 7; the 10s only bring zeros.')

q(Q, 1, 'What is the value of 10⁴?',
  ['100', '1,000', '10,000', '40'], 2,
  'The exponent counts how many zeros the answer has.',
  ['The base is 10 and the exponent is 4.',
   'That means four 10s multiplied: 10 × 10 × 10 × 10.',
   '10 × 10 = 100, × 10 = 1,000, × 10 = 10,000.'],
  '**10,000.** Four 10s multiplied together — and four zeros, matching the exponent.',
  'The trap answer 40 comes from multiplying 10 × 4. The exponent never multiplies.')
q(Q, 1, 'How is 100,000 written as a power of 10?',
  ['10⁵', '10⁴', '10⁶', '5 × 10'], 0,
  'Count the zeros.',
  ['Count the zeros in 100,000: there are five.',
   'For a power of 10, zeros and exponent match.',
   'So 100,000 = 10⁵.'],
  '**10⁵.** Five zeros, exponent 5 — the pattern in both directions.',
  'Writing big round numbers this way is why scientists love exponents.')
q(Q, 1, 'In the expression 10⁶, which number is the base?',
  ['10', '6', '60', '1,000,000'], 0,
  'The base is the number being repeated.',
  ['The base is the number the exponent copies.',
   'Here 10 is copied six times.',
   'So the base is 10, and 6 is the exponent.'],
  '**10.** The 6 is the exponent — it counts, it is never a factor itself.',
  '1,000,000 is the VALUE of 10⁶, not its base.')
q(Q, 2, 'A crate holds 4 × 10³ oranges. How many oranges is that?',
  ['400', '4,000', '40,000', '4,300'], 1,
  'Write the 4, then attach zeros.',
  ['10³ = 1,000.',
   'So 4 × 10³ = 4 × 1,000.',
   'Write the 4 and attach three zeros: 4,000.'],
  '**4,000.** The exponent 3 attaches three zeros to the 4.',
  'A quick check: the number of zeros in the product matches the exponent.')
q(Q, 2, 'A city library has 8,000,000 pages across all its books. Which expression equals 8,000,000?',
  ['8 × 10⁵', '8 × 10⁶', '8 × 10⁷', '8 × 10⁸'], 1,
  'Count the zeros after the 8.',
  ['Count the zeros in 8,000,000: six of them.',
   'The exponent must match: 10⁶.',
   'So 8,000,000 = 8 × 10⁶.'],
  '**8 × 10⁶.** Six zeros, exponent 6 — reading the pattern backwards.',
  'Going from the big number back to the exponent is the same pattern in reverse.')
q(Q, 2, 'How many zeros does the product 5 × 10⁴ have?',
  ['3', '4', '5', '9'], 1,
  'The 5 brings no zeros of its own.',
  ['10⁴ = 10,000 — four zeros.',
   '5 × 10,000 = 50,000.',
   'The product keeps exactly the four zeros the power of 10 brought.'],
  '**4.** The zeros come from the power of 10; the 5 just sits in front of them.',
  'If the front factor ended in 0 (like 50), the product would gain an extra zero — watch for that case later.')
q(Q, 2, 'A farm ships 3 × 10² melons. If the exponent changed from 2 to 3, what would happen to the number of melons?',
  ['It would be 10 times as many', 'It would double', 'It would grow by 10 melons', 'It would be 100 times as many'], 0,
  'One more 10 joins the multiplication.',
  ['3 × 10² = 300 melons.',
   'Raising the exponent by one multiplies by one more 10.',
   '3 × 10³ = 3,000 — ten times 300.'],
  '**10 times as many.** Each step up in the exponent is one more ×10.',
  'Exponents grow multiplicatively — one step never just adds.')
q(Q, 3, 'A student writes 10 × 10 × 10 × 10 = 40. What mistake did they make?',
  ['They added the 10s instead of multiplying them',
   'They used the wrong base',
   'They multiplied one 10 too many',
   'They forgot to attach zeros to the 4'], 0,
  'Check: what operation actually produces 40 from four 10s?',
  ['10 + 10 + 10 + 10 = 40 — that is addition.',
   '10 × 10 × 10 × 10 multiplies: 100, then 1,000, then 10,000.',
   'The student added where the expression says multiply.'],
  '**They added instead of multiplied.** Four 10s multiplied make 10,000, not 40.',
  'Saying HOW an answer went wrong is a stronger skill than just marking it wrong.')
q(Q, 3, 'Which equation is true?',
  ['6 × 10⁵ = 600,000', '6 × 10⁵ = 60,000', '6 × 10⁵ = 650,000', '6 × 10⁵ = 6,500'], 0,
  'The exponent says how many zeros follow the 6.',
  ['10⁵ = 100,000.',
   '6 × 100,000 = 600,000.',
   'Five zeros after the 6 — matching the exponent.'],
  '**6 × 10⁵ = 600,000.** Write the 6, attach five zeros.',
  'The 650,000 trap slips a digit into the zeros — the front factor never leaks into them.')
q(Q, 3, 'A telescope can see about 90,000 stars on a clear night. Which expression equals 90,000?',
  ['9 × 10³', '9 × 10⁴', '9 × 10⁵', '90 × 10⁴'], 1,
  'How many zeros follow the 9?',
  ['Split 90,000 into 9 × 10,000.',
   '10,000 has four zeros, so it is 10⁴.',
   'So 90,000 = 9 × 10⁴.'],
  '**9 × 10⁴.** Four zeros after the 9, exponent 4.',
  '90 × 10⁴ is a trick worth pausing on: it equals 900,000 — the zero inside 90 counts too.')
build(C, Q, 'unit-m31', 'Topic 3 · 3-1 Patterns with Exponents and Powers of 10', 10,
      'Lesson 3-1 introduces exponents: the base is the number being repeated, the exponent counts how many times, and a power of 10 has exactly as many zeros as its exponent. Multiplying a number by a power of 10 attaches that many zeros.',
      'Exponents are how big numbers stay readable — 10⁶ is easier to compare than 1,000,000 with the zeros counted by eye. The zeros pattern from this lesson is also the engine behind the decimal place-value work in the rest of the topic.',
      [('Write a power of 10 using an exponent, and read one back into a whole number.', 'source'),
       ('Multiply a single digit by a power of 10 using the zeros pattern.', 'source'),
       ('Explain the mistake when exponents are added instead of multiplied.', 'added')],
      'First lesson of Topic 3, and the class has jumped books — this is 5th-grade material, which is how her accelerated track works. The classic error to watch for: reading 10⁴ as 10 × 4 = 40. The lesson check and everything after leans on the zeros-equals-exponent pattern.',
      ('Cards first — exponent and base have to be solid words before the pattern makes sense. Then the quiz.', 12),
      'content/math-t3-31.json', SRC, SRCLONG)

# ---------------------------------------------------------------- 3-2
C, Q = [], []
card(C, 'Place value',
     '**The value of a digit depends on WHERE it sits in the number.**\n'
     '• In 5,283 the 5 is worth 5,000 — not 5.\n'
     '• The chart runs ones, tens, hundreds, thousands… up through millions.',
     hint='Same digit, different seat, different value.')
card(C, 'Periods',
     '**Groups of three places separated by commas: ones, thousands, millions.**\n'
     '• 22,000,000 reads by periods: twenty-two million.\n'
     '• Commas are there to let your eyes find the periods fast.',
     hint='Read big numbers in threes, comma to comma.')
card(C, 'Expanded form',
     '**The number written as a sum of each digit times its place value.**\n'
     '• 3,514 = 3,000 + 500 + 10 + 4.\n'
     '• With exponents: (3 × 10³) + (5 × 10²) + (1 × 10¹) + (4 × 1).',
     hint='Pull the number apart seat by seat.')
card(C, 'Number name',
     '**The number written in words, period by period.**\n'
     '• 4,070,000 is "four million, seventy thousand".\n'
     '• A zero in a place means that place is silent — you never say it.',
     hint='Say each period, then its name: million, thousand.')
card(C, 'The 10-times relationship',
     '**A digit one place to the LEFT is worth 10 times as much.**\n'
     '• In 7,700 the left 7 (thousands) is worth 10 times the right 7 (hundreds).\n'
     '• Two places apart means 10 × 10 = 100 times — the places multiply.',
     hint='Every step left is one ×10. Steps stack.')

q(Q, 1, 'A stadium sold 3,000,000 tickets over its lifetime. What is the number name for 3,000,000?',
  ['Three million', 'Three hundred thousand', 'Thirty million', 'Three thousand'], 0,
  'Count off the periods from the right: ones, thousands, millions.',
  ['Group by commas: 3 | 000 | 000.',
   'The 3 sits in the millions period.',
   'So the name is three million.'],
  '**Three million.** Two full periods of zeros after the 3 puts it in the millions.',
  'Commas are not decoration — they name the periods for you.')
q(Q, 1, 'What is the value of the 8 in 4,829,157?',
  ['800,000', '80,000', '8,000', '8'], 0,
  'Find the 8\'s seat first, then its value.',
  ['Count places from the right: 7 ones, 5 tens, 1 hundreds, 9 thousands, 2 ten-thousands, 8 hundred-thousands.',
   'The 8 sits in the hundred-thousands place.',
   'So it is worth 8 × 100,000 = 800,000.'],
  '**800,000.** The digit is 8, but the seat makes it eight hundred thousand.',
  'Digit and value are different questions — the seat does the multiplying.')
q(Q, 1, 'Which number has a 6 in the ten-thousands place?',
  ['165,204', '615,204', '156,204', '105,264'], 0,
  'Ten-thousands is the fifth seat from the right.',
  ['Count five places from the right in each number.',
   'In 165,204 the fifth digit from the right is 6.',
   'The others put the 6 in a different seat or not at all in that one.'],
  '**165,204.** Fifth place from the right — count seats, do not eyeball.',
  'Counting from the right never lies; guessing from the left often does.')
q(Q, 2, 'Which is the standard form of (7 × 10⁶) + (2 × 10⁴) + (5 × 10²)?',
  ['7,020,500', '7,200,500', '7,020,050', '720,500'], 0,
  'Give every silent place its zero.',
  ['7 × 10⁶ = 7,000,000.',
   '2 × 10⁴ = 20,000 and 5 × 10² = 500.',
   'Add them, keeping zeros in the empty seats: 7,020,500.'],
  '**7,020,500.** The places with no term still need their zeros.',
  'Expanded form only lists the seats that are filled — standard form shows every seat.')
q(Q, 2, 'An ant colony can hold about twenty-two million ants. How is that written in standard form?',
  ['22,000,000', '2,200,000', '220,000,000', '22,000'], 0,
  'Millions is a whole period — three zeros twice.',
  ['Twenty-two goes in the millions period: 22.',
   'The thousands and ones periods are empty: 000 and 000.',
   'So: 22,000,000.'],
  '**22,000,000.** Two full periods of zeros carry the 22 up to millions.',
  'Standard form is just the name translated seat by seat.')
q(Q, 2, 'In the number 5,500, how does the value of the left 5 compare to the right 5?',
  ['It is 10 times as great', 'It is 100 times as great', 'It is 5 times as great', 'The two are equal'], 0,
  'How many seats apart are the two 5s?',
  ['The left 5 is in the thousands place: 5,000.',
   'The right 5 is in the hundreds place: 500.',
   '5,000 ÷ 500 = 10 — one seat apart, one ×10.'],
  '**10 times as great.** Adjacent places always differ by a factor of 10.',
  'This ×10-per-seat rule is the whole reason the decimal system works.')
q(Q, 3, 'Mara says that in 6,367, one 6 is 10 times as great as the other. What should you tell her?',
  ['The 6s are two places apart, so the left one is 100 times as great',
   'She is right — neighbouring 6s always differ by 10 times',
   'The two 6s are equal because they are the same digit',
   'The left 6 is 1,000 times as great'], 0,
  'Find each 6\'s seat before comparing.',
  ['The left 6 is in the thousands place: 6,000.',
   'The right 6 is in the tens place: 60.',
   'They are two seats apart, so the factor is 10 × 10 = 100.',
   '6,000 ÷ 60 = 100 — not 10.'],
  '**100 times, not 10.** The ×10 rule is per seat, and these 6s are two seats apart.',
  'The rule she remembered is right — she skipped counting the seats between.')
q(Q, 3, 'A 4-digit number has all four digits the same, and the digit in the hundreds place is worth 200. What is the number?',
  ['2,222', '2,022', '2,220', '4,444'], 0,
  'What digit makes the hundreds place worth 200?',
  ['Hundreds worth 200 means the digit is 2.',
   'All four digits are the same, so every digit is 2.',
   'The number is 2,222.'],
  '**2,222.** One clue about one seat, plus "all the same", pins every digit.',
  'Each 2 in 2,222 is worth 10 times its right-hand neighbour: 2,000, 200, 20, 2.')
q(Q, 3, 'Ben writes the expanded form of two million, forty thousand, six as (2 × 10⁶) + (4 × 10⁴) + 6. Did he get it right?',
  ['Yes — each part lands in the correct place',
   'No — forty thousand needs 4 × 10⁵',
   'No — the 6 should be 6 × 10¹',
   'No — two million needs 2 × 10⁷'], 0,
  'Check each part against its place value.',
  ['Two million = 2,000,000 = 2 × 10⁶. ✓',
   'Forty thousand = 40,000 = 4 × 10⁴. ✓',
   'Six ones = 6. ✓',
   'Standard form: 2,040,006.'],
  '**Yes.** Every term matches its seat — the number is 2,040,006.',
  'Verifying someone right is the same skill as catching them wrong: check seat by seat.')
q(Q, 3, 'Which number is 100 times as great as 3,070?',
  ['307,000', '30,700', '3,070,000', '30,070'], 0,
  'Two ×10 steps — every digit moves two seats left.',
  ['100 times = two place-value steps left.',
   '3,070 × 10 = 30,700.',
   '30,700 × 10 = 307,000.'],
  '**307,000.** Multiplying by 100 slides the whole number two seats left.',
  'The digits never change — only their seats do.')
build(C, Q, 'unit-m32', 'Topic 3 · 3-2 Place Value Through Millions', 10,
      'Lesson 3-2 extends the place-value chart through the millions: reading and writing numbers in standard form, expanded form and number names, and the rule that a digit one place left is worth 10 times as much — with the factors stacking when places are further apart.',
      'Every skill in this topic — decimals, comparing, rounding — is the same chart read further right. Getting the ×10-per-seat rule solid on whole numbers now makes the decimal version feel like the same fact instead of a new one.',
      [('Read and write numbers through the millions in standard form, expanded form and words.', 'source'),
       ('State the value of any digit from its place.', 'source'),
       ('Compare two identical digits in different places and give the exact factor between them.', 'source')],
      'The trap in this lesson is the ×10 rule applied without counting seats — two 6s that sit two places apart differ by 100 times, not 10. One question makes her verify a CORRECT expanded form, because confirming right answers is rarer practice than catching wrong ones.',
      ('Cards, then the quiz. If the 10-times questions feel slippery, the fifth card is the one to re-read.', 12),
      'content/math-t3-32.json', SRC, SRCLONG)

# ---------------------------------------------------------------- 3-3
C, Q = [], []
card(C, 'Thousandth',
     '**One of 1,000 equal parts of a whole — written 0.001.**\n'
     '• The thousandths place is the THIRD place right of the decimal point.\n'
     '• 4/1,000 = 0.004.',
     hint='Three zeros in 1,000 — three places right of the point.')
card(C, 'The chart continues rightward',
     '**Right of the decimal point the seats are tenths, hundredths, thousandths.**\n'
     '• Each seat right is worth one-tenth of the seat before.\n'
     '• The same ×10 ladder as whole numbers, just descending.',
     hint='Same ladder, going down: ÷10 every step right.')
card(C, 'Decimal ↔ fraction',
     '**A decimal in thousandths is a fraction with denominator 1,000.**\n'
     '• 0.444 = 444/1,000.\n'
     '• The number of decimal places matches the zeros in the denominator.',
     hint='Places right of the point = zeros in the bottom of the fraction.')
card(C, 'Reading a decimal name',
     '**Read the digits as a whole number, then say the last place\'s name.**\n'
     '• 0.309 → "three hundred nine thousandths".\n'
     '• 0.05 → "five hundredths".',
     hint='The last seat names the whole thing.')
card(C, 'Zeros right after the point',
     '**A zero between the point and the digits pushes everything one seat smaller.**\n'
     '• 97/1,000 is 0.097 — NOT 0.97.\n'
     '• Check by counting places: thousandths needs three.',
     hint='Count places, never just copy digits over.')

q(Q, 1, 'Which fraction equals 0.007?',
  ['7/1,000', '7/100', '7/10', '70/1,000'], 0,
  'Count how many places right of the point the 7 sits.',
  ['The 7 sits three places right of the decimal point.',
   'Three places right is the thousandths seat.',
   'So 0.007 = 7/1,000.'],
  '**7/1,000.** Third seat right of the point means thousandths.',
  'Places right of the point and zeros in the denominator always agree.')
q(Q, 1, 'A beetle measures 391/1,000 of a metre. How is that written as a decimal?',
  ['0.391', '3.91', '0.0391', '39.1'], 0,
  'Thousandths means three places right of the point.',
  ['The denominator 1,000 says thousandths.',
   'Thousandths means exactly three decimal places.',
   '391 fills them: 0.391.'],
  '**0.391 m.** Three digits, three places — a clean fit.',
  'The unit rides along: 0.391 of a METRE. Keep units attached to answers.')
q(Q, 1, 'Which digit of 2.583 is in the thousandths place?',
  ['3', '5', '8', '2'], 0,
  'Count seats rightward from the point.',
  ['First seat right of the point: 5 (tenths).',
   'Second: 8 (hundredths).',
   'Third: 3 (thousandths).'],
  '**3.** Third seat right of the point.',
  'The ones seat is three seats left of the thousandths seat — worth 1,000 times as much. Count seats; never guess the factor.')
q(Q, 2, 'How is "seven hundred five thousandths" written as a decimal?',
  ['0.705', '0.75', '700.5', '0.0705'], 0,
  'The missing tens place still needs a digit.',
  ['Seven hundred five = 705.',
   'Thousandths means three decimal places.',
   '705 fills them: 0.705 — the zero holds the hundredths seat.'],
  '**0.705.** The silent place in "seven hundred five" becomes a written 0.',
  'Words skip empty places; decimals never can.')
q(Q, 2, 'How does 0.04 compare to 0.004?',
  ['0.04 is 10 times as great', '0.04 is 100 times as great', 'The two are equal', '0.004 is 10 times as great'], 0,
  'One seat apart on the ladder.',
  ['0.04 has its 4 in the hundredths seat.',
   '0.004 has its 4 in the thousandths seat — one seat further right.',
   'One seat is one factor of 10, and leftward is greater.'],
  '**0.04 is 10 times as great.** Same ×10-per-seat rule as whole numbers.',
  'The ladder never changes — it just keeps going past the point.')
q(Q, 2, 'A relay team ran 0.3 of the race in the rain. How many thousandths is 0.3?',
  ['300/1,000', '3/1,000', '30/1,000', '3,000/1,000'], 0,
  'Annex zeros until you reach the thousandths seat.',
  ['0.3 = 0.300 — annexing zeros changes nothing.',
   '0.300 read in thousandths is 300 of them.',
   'So 0.3 = 300/1,000.'],
  '**300/1,000.** Three tenths and three hundred thousandths are the same amount.',
  'Renaming into smaller pieces is the move that makes decimal addition line up later.')
q(Q, 3, 'Nadia says 97/1,000 can be written as 0.97. What should you tell her?',
  ['Thousandths needs three places, so it is 0.097',
   'She is right — 97 over 1,000 is 0.97',
   'It should be 9.7 instead',
   'It should be 0.0097 instead'], 0,
  'Count the decimal places her version uses.',
  ['0.97 uses only two decimal places — that is 97 HUNDREDTHS.',
   'The denominator 1,000 demands three places.',
   'Pad the front: 097 → 0.097.'],
  '**0.097.** Two places is hundredths; her digits are right but the seats are wrong.',
  'The zero in front of the 9 is doing real work — it is not decoration.')
q(Q, 3, 'Owen claims that in 0.555, the 5 in the thousandths place is worth 10 times the 5 in the hundredths place. What is wrong with his claim?',
  ['He has it backwards — the thousandths 5 is worth one-tenth as much',
   'Nothing — the claim is correct',
   'The two 5s are worth the same because the digits match',
   'The factor should be 100, not 10'], 0,
  'Which direction does the ladder grow?',
  ['The thousandths seat is one seat RIGHT of the hundredths seat.',
   'Each seat right is worth one-tenth as much, not ten times.',
   'So the thousandths 5 (0.005) is a tenth of the hundredths 5 (0.05).'],
  '**He has the direction backwards.** Rightward seats shrink; leftward seats grow.',
  'The size of the factor (10) was right — the direction is the whole question.')
q(Q, 3, 'A number has a 6 in the tenths place. If that 6 moved one seat to the right, what would happen to its value?',
  ['It would be worth one-tenth as much', 'It would be worth 10 times as much', 'It would keep the same value', 'It would be worth one-hundredth as much'], 0,
  'Moving right goes down the ladder.',
  ['In the tenths seat the 6 is worth 0.6.',
   'One seat right is the hundredths seat: 0.06.',
   '0.06 is one-tenth of 0.6.'],
  '**One-tenth as much.** Every seat rightward divides by 10.',
  'Same digit, same rule, either side of the point.')
q(Q, 3, 'Which decimal equals 40/1,000?',
  ['0.040', '0.400', '0.004', '4.000'], 0,
  'Three zeros below means three places — then place the 40.',
  ['Thousandths means three decimal places.',
   '040 fills them: 0.040.',
   'Check: 0.040 = 0.04 = 4 hundredths = 40 thousandths. ✓'],
  '**0.040.** Forty thousandths and four hundredths are the same number in two coats.',
  'A trailing zero changes nothing; a LEADING zero after the point changes everything.')
build(C, Q, 'unit-m33', 'Topic 3 · 3-3 Decimals to Thousandths', 10,
      'Lesson 3-3 pushes the place-value chart three seats right of the decimal point: reading and writing thousandths, converting between decimals and fractions over 1,000, and the same ×10-per-seat relationship running through the point.',
      'Thousandths are where money and measurement intuition run out and the chart has to carry you. The two classic errors — 97/1,000 as 0.97, and the ×10 rule pointed the wrong way — both come from trusting digits over seats, and both are in the quiz.',
      [('Write a thousandths fraction as a decimal and back.', 'source'),
       ('Name the seat of any digit through the thousandths place.', 'source'),
       ('Compare the values of one digit in neighbouring seats, in the correct direction.', 'source')],
      'Watch the 0.097-vs-0.97 error — it is the single most common slip in this lesson, and it comes from copying digits without counting places. If she gets the Owen question wrong, the direction of the ÷10 ladder is the thing to talk through.',
      ('Cards first — the last card is the one that prevents the classic mistake. Then the quiz.', 12),
      'content/math-t3-33.json', SRC, SRCLONG)

# ---------------------------------------------------------------- 3-4
C, Q = [], []
card(C, 'Equivalent decimals',
     '**Decimals that name the same amount.**\n'
     '• 1.4 = 1.40 = 1.400.\n'
     '• Four tenths, forty hundredths and four hundred thousandths are the same shaded amount.',
     hint='Zeros glued to the END change nothing.')
card(C, 'Annexing zeros',
     '**Attaching zeros after the last decimal digit renames, never changes.**\n'
     '• 0.6 → 0.60: six tenths become sixty hundredths.\n'
     '• Useful for lining decimals up to compare or add.',
     hint='Renaming into smaller pieces — the amount stays put.')
card(C, 'Where a zero DOES matter',
     '**A zero between the point and the digits changes the value.**\n'
     '• 7.63 and 7.630 are equal; 7.63 and 7.063 are not.\n'
     '• Only zeros after the final digit are free.',
     hint='End zeros are free; middle zeros are load-bearing.')
card(C, 'Decimal number names',
     '**"And" marks the decimal point; the last seat names the part.**\n'
     '• 4.068 → "four and sixty-eight thousandths".\n'
     '• 9.20 → "nine and twenty hundredths".',
     hint='Say "and" exactly where the point sits.')
card(C, 'Expanded form with decimals',
     '**Each digit times its seat, seats now including tenths, hundredths, thousandths.**\n'
     '• 6.308 = (6 × 1) + (3 × 1/10) + (8 × 1/1,000).\n'
     '• Empty seats simply do not appear.',
     hint='The fractions 1/10, 1/100, 1/1,000 are the right-hand seats.')

q(Q, 1, 'Which decimal is equivalent to 5.3?',
  ['5.30', '5.03', '5.33', '0.53'], 0,
  'Only one option adds a zero at the END.',
  ['Equivalent decimals differ only by zeros after the last digit.',
   '5.30 attaches a zero at the end — same amount.',
   '5.03 moves the 3 to a smaller seat — different amount.'],
  '**5.30.** Five and three tenths equals five and thirty hundredths.',
  'Say both out loud — "three tenths", "thirty hundredths" — and you can hear they match.')
q(Q, 1, 'How is "nine and twenty-four thousandths" written in standard form?',
  ['9.024', '9.24', '9.0024', '924'], 0,
  '"Thousandths" fixes how many decimal places there are.',
  ['"Nine and" gives the whole part: 9.',
   'Twenty-four thousandths needs three decimal places.',
   '024 fills them: 9.024.'],
  '**9.024.** The zero holds the tenths seat that "twenty-four" leaves empty.',
  '"And" is doing precise work in a number name — it is the decimal point.')
q(Q, 1, 'Which two decimals are equivalent?',
  ['2.60 and 2.6', '2.06 and 2.6', '2.600 and 2.06', '2.66 and 2.6'], 0,
  'Find the pair that differs only after its last nonzero digit.',
  ['2.60 just annexes a zero to 2.6 — equal.',
   '2.06 puts the 6 in the hundredths seat — smaller.',
   '2.66 adds six more hundredths — larger.'],
  '**2.60 and 2.6.** Sixty hundredths is six tenths.',
  'The zero\'s POSITION is the entire question, every time.')
q(Q, 2, 'What is the standard form of (6 × 1) + (3 × 1/10) + (8 × 1/1,000)?',
  ['6.308', '6.38', '6.038', '63.8'], 0,
  'One seat is missing from the sum — it still needs its zero.',
  ['6 × 1 = 6, whole part.',
   '3 × 1/10 = 0.3 and 8 × 1/1,000 = 0.008.',
   'The hundredths seat has no term, so it gets a 0: 6.308.'],
  '**6.308.** Expanded form skips empty seats; standard form writes their zeros.',
  'The same silent-seat rule as whole numbers, now right of the point.')
q(Q, 2, 'Of the 1,000 raffle tickets printed for the school fair, 0.35 of them sold in the first hour. How many tickets is that?',
  ['350', '35', '3.5', '530'], 0,
  'Rename 0.35 as thousandths first.',
  ['0.35 = 0.350 = 350/1,000.',
   'So 0.35 OF 1,000 tickets is 350 tickets.',
   'Check: 0.35 is a bit more than a third of 1,000. ✓ '],
  '**350 tickets.** Annex a zero and the thousandths read straight off.',
  'A decimal of a thousand is exactly why equivalent decimals earn their keep.')
q(Q, 2, 'Elena wrote 4.7 inches for a bug\'s length, but the real length is one-tenth of that. What is the correct measurement?',
  ['0.47 inches', '47 inches', '4.07 inches', '0.047 inches'], 0,
  'One-tenth slides every digit one seat right.',
  ['One-tenth of a number moves each digit one seat right.',
   '4.7 → 0.47.',
   'Check: 0.47 × 10 = 4.7. ✓'],
  '**0.47 inches.** A misplaced decimal point is always a ×10 or ÷10 error.',
  'When a measurement looks ten times too big, the point is the first suspect.')
q(Q, 3, 'Kai says 7.63 and 7.063 are equivalent because both just add a zero to 7.63. What should you tell him?',
  ['The zero in 7.063 sits between digits, so it changed the value',
   'He is right — zeros never change a decimal',
   'Neither number is equivalent to anything',
   'They would only be equal if the zero were removed from both'], 0,
  'WHERE did the zero land?',
  ['7.630 attaches the zero after the last digit — that one is equivalent.',
   '7.063 slides the 6 and 3 into smaller seats.',
   '7.063 is seven and sixty-three thousandths; 7.63 is seven and sixty-three hundredths.',
   'Different seats, different number.'],
  '**The zero moved the digits.** End zeros are free; a zero pushed between the point and the digits re-seats everything after it.',
  'One rule, one exception-shaped trap — this is the whole lesson in a single question.')
q(Q, 3, 'Three friends shade hundredths grids. Priya shades half of one grid. Marco shades one full grid and one-tenth of another. What decimals show how much each shaded?',
  ['Priya 0.50, Marco 1.10', 'Priya 0.05, Marco 1.01', 'Priya 0.50, Marco 1.01', 'Priya 0.05, Marco 1.10'], 0,
  'Half a grid is how many hundredths?',
  ['Half of one hundredths grid is 50 squares: 0.50.',
   'A full grid is 1, and one-tenth more is 0.10.',
   'Marco: 1 + 0.10 = 1.10.'],
  '**Priya 0.50, Marco 1.10.** Both amounts read straight off the grids.',
  '0.5 and 0.50 are the same — the grid just makes the hundredths version visible.')
q(Q, 3, 'Which is the number name for 12.406?',
  ['Twelve and four hundred six thousandths', 'Twelve and forty-six thousandths', 'Twelve and four hundred six hundredths', 'One hundred twenty-four and six thousandths'], 0,
  'The part after "and" is 406, and its last seat is thousandths.',
  ['Whole part: twelve.',
   '"And" for the point.',
   'The decimal part is 406 ending in the thousandths seat.',
   'So: twelve and four hundred six thousandths.'],
  '**Twelve and four hundred six thousandths.** The middle zero is read inside 406, not skipped.',
  '"Forty-six thousandths" would be 0.046 — the name has to carry the zero\'s work.')
q(Q, 3, 'Which shows 0.85 in expanded form?',
  ['(8 × 1/10) + (5 × 1/100)', '(8 × 10) + (5 × 1)', '(8 × 1/100) + (5 × 1/1,000)', '(8 × 1) + (5 × 1/10)'], 0,
  'Name each digit\'s seat first.',
  ['The 8 is in the tenths seat: 8 × 1/10.',
   'The 5 is in the hundredths seat: 5 × 1/100.',
   'Sum: (8 × 1/10) + (5 × 1/100).'],
  '**(8 × 1/10) + (5 × 1/100).** Each digit times exactly its seat.',
  'Expanded form is the place-value chart written as arithmetic.')
build(C, Q, 'unit-m34', 'Topic 3 · 3-4 Equivalent Decimals and Decimal Forms', 10,
      'Lesson 3-4 covers equivalent decimals — zeros annexed after the last digit rename without changing — plus number names, standard form and expanded form for decimals, including the middle-zero cases where a zero is load-bearing.',
      'Every comparison and every lined-up addition for the rest of the year quietly uses equivalence. The end-zero-versus-middle-zero distinction is also the first place this topic asks her to argue WHY, not just compute.',
      [('Write two decimals equivalent to a given decimal.', 'source'),
       ('Convert between standard form, expanded form and number names for decimals.', 'source'),
       ('Explain which zeros change a decimal\'s value and which do not.', 'added')],
      'The Kai question is the heart of the lesson: end zeros are free, middle zeros re-seat everything. If she misses it, shading a hundredths grid for 7.63 vs 7.063 makes the difference visible in about thirty seconds.',
      ('Cards, then the quiz. The third card is the one that separates the free zeros from the load-bearing ones.', 12),
      'content/math-t3-34.json', SRC, SRCLONG)

print('--- lessons 3-1 to 3-4 built ---')
