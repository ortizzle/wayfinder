# Science · Quiz 1 Part 2: Measurement — built from "Measurements.pdf", the
# graded 13-point lesson check that landed in the Drive "Quiz 1 - Material"
# folder. Same shelf as the Thinking Like a Scientist unit (series title
# "Science · …"), fresh scenarios throughout — the check is her homework;
# this app is extra.
from unit_common import card, q, build

C, Q = [], []
card(C, 'Quantitative data',
     '**Data you can count or measure — it comes as a number.**\n'
     '• 6 legs, 14 petals, 2.3 metres.\n'
     '• Numerical data can be graphed and compared exactly.',
     hint='QuaNtitative = Numbers.')
card(C, 'Qualitative data',
     '**Data that describes qualities — colours, textures, smells, shapes.**\n'
     '• Fuzzy, striped, shiny, sticky.\n'
     '• It comes from your senses as descriptions, not numbers.',
     hint='quaLitative = what it is Like.')
card(C, 'The two measurement systems',
     '**The U.S. Customary System and the Metric System.**\n'
     '• Customary: inches, feet, miles, gallons, pounds.\n'
     '• Metric: metres, litres, grams — built on tens.',
     hint='Two rulers for one world — know which one you are holding.')
card(C, 'Scientists use metric',
     '**Scientists everywhere — including the United States — collect data in metric units.**\n'
     '• Metric steps are powers of ten, so converting is just sliding the decimal.\n'
     '• Sharing data worldwide only works if everyone measures alike.',
     hint='Science speaks one measurement language, on purpose.')
card(C, 'Length',
     '**How long or far something is.**\n'
     '• Customary: inches for small things, feet, then miles for distances.\n'
     '• Metric: centimetres, metres, kilometres.',
     hint='Pick the unit sized to the thing — inches for a lizard, miles for a road trip.')
card(C, 'Volume',
     '**How much space something takes up.**\n'
     '• Liquids: gallons (customary) or litres (metric).\n'
     '• Solid shapes: cubic units like cm³.',
     hint='Volume fills — jugs, tanks, boxes.')
card(C, 'Mass',
     '**How much matter is in something.**\n'
     '• Metric: grams and kilograms.\n'
     '• A kilogram is about the mass of a litre of water.',
     hint='Kilograms answer "how much stuff", not "how long" or "how full".')
card(C, 'Volume of a rectangular prism',
     '**Multiply the three edge lengths: V = length × width × height.**\n'
     '• 2 cm × 10 cm × 3 cm = 60 cm³.\n'
     '• The answer is always in CUBIC units.',
     eq='V = l × w × h',
     hint='Three edges multiplied — never added.')
card(C, 'Why cubic units',
     '**Three lengths multiply, so the unit gets multiplied three times too.**\n'
     '• cm × cm × cm = cm³.\n'
     '• A cm³ is one little cube; the volume counts how many fit inside.',
     hint='The ³ remembers that three directions were used.')
card(C, 'Matching the unit to the job',
     '**A good unit is sized close to the thing being measured.**\n'
     '• A soccer field in metres, not kilometres; milk in gallons, not cups… of a tanker, anyway.\n'
     '• The wrong-sized unit buries the measurement in zeros or fractions.',
     hint='If the number comes out huge or tiny, the unit was the wrong size.')

q(Q, 1, 'A student watching a beetle writes down four observations. Which one is quantitative?',
  ['It has 6 legs', 'Its shell is glossy', 'It moves slowly', 'It smells earthy'], 0,
  'Hunt for the number.',
  ['Quantitative data can be counted or measured.',
   '"6 legs" is a count — a number.',
   'Glossy, slowly and earthy are descriptions from the senses: qualitative.'],
  '**It has 6 legs.** The only observation with a number in it.',
  'One number is worth spotting instantly — that reflex is the whole skill.')
q(Q, 1, 'Which of these observations is qualitative?',
  ['The blanket feels scratchy', 'The rope is 3 metres long', 'The jar holds 2 litres', 'The dog has 4 paws'], 0,
  'Three of these are measurements or counts.',
  ['Scratchy is a texture — sensed, not counted.',
   '3 metres, 2 litres and 4 paws are all numbers.',
   'The description without a number is the qualitative one.'],
  '**The blanket feels scratchy.** A quality, straight from the sense of touch.',
  'Qualitative data is not worse data — it is just not graphable as numbers.')
q(Q, 1, 'Which statement about qualitative data is TRUE?',
  ['It describes qualities you sense, like colour and texture',
   'It is numerical data that can be graphed',
   'It is always more accurate than quantitative data',
   'It can only be collected with instruments'], 0,
  'Qualitative and numerical are opposites here.',
  ['Qualitative data describes — fuzzy, red, smooth.',
   'Numerical, graphable data is the DEFINITION of quantitative, not qualitative.',
   'Neither kind is automatically more accurate; both are collected with plain senses or instruments.'],
  '**It describes qualities you sense.** The numerical-and-graphable description belongs to quantitative data.',
  'This exact true-or-false was on the lesson check — now you know why it is false.')
q(Q, 1, 'A scientist working in the United States is recording plant heights. Which system of units does she use?',
  ['The Metric System', 'The U.S. Customary System', 'Whichever system is closest to hand', 'Both systems, averaged together'], 0,
  'Where the scientist lives does not decide.',
  ['Scientists collect data other scientists must be able to use.',
   'The worldwide scientific standard is the Metric System.',
   'That holds inside the U.S. too, even though daily life there runs on customary units.'],
  '**The Metric System.** Science uses metric everywhere — the U.S. included.',
  'Her grocery list can stay in pounds; her lab notebook cannot.')
q(Q, 2, 'Using the U.S. Customary System, which unit fits measuring the length of a crayon?',
  ['Inches', 'Centimetres', 'Gallons', 'Pounds'], 0,
  'Right system first, then right size.',
  ['The question asks for a CUSTOMARY unit — centimetres are metric, so they are out.',
   'Gallons measure volume and pounds measure weight.',
   'Inches are customary, measure length, and suit a crayon-sized object.'],
  '**Inches.** Customary, length-sized, crayon-sized.',
  'Two filters: the right system, then the right property. Run both every time.')
q(Q, 2, 'Using the Metric System, which unit fits measuring the length of a basketball court?',
  ['Metres', 'Kilometres', 'Feet', 'Litres'], 0,
  'Metric, length, and court-sized.',
  ['Feet are customary — out, whatever the size.',
   'Litres measure volume.',
   'Kilometres are metric length but road-trip-sized; a court measures tens of metres.',
   'Metres fit the system, the property and the size.'],
  '**Metres.** A court is about 28 of them — a sensible number.',
  'If the answer would come out 0.028, the unit was too big. Size the unit to the thing.')
q(Q, 2, 'A water tower holds enough water for a whole town. Using the U.S. Customary System, which unit fits its volume?',
  ['Gallons', 'Litres', 'Miles', 'Ounces'], 0,
  'Customary, volume, enormous.',
  ['Litres are metric — the question says customary.',
   'Miles measure distance.',
   'Ounces are customary volume, but sized for juice glasses, not towers.',
   'Gallons are customary, volume, and big enough to count a tower in.'],
  '**Gallons.** Customary volume at town scale.',
  'The lesson check asked this about a milk tanker — same reasoning, new container.')
q(Q, 2, 'Gallons, litres and cubic centimetres can all be used to measure which property?',
  ['Volume', 'Mass', 'Length', 'Temperature'], 0,
  'What do a jug, a bottle and a little cube have in common?',
  ['Gallons: how much liquid fills a container.',
   'Litres: the metric version of the same idea.',
   'Cubic centimetres: space inside a solid shape.',
   'All three count filled space — volume.'],
  '**Volume.** Three different units, one property: how much space.',
  'Units cluster by property. Spotting the cluster answers the question.')
q(Q, 2, 'A supply list says each student needs 2 metres of string. What property are the students measuring?',
  ['Length', 'Volume', 'Mass', 'Time'], 0,
  'What do metres always measure?',
  ['Metres are a metric unit of length.',
   'String is measured end to end — a distance.',
   'So the property is length.'],
  '**Length.** Metres only ever measure how long or how far.',
  'From unit to property is the reverse of picking a unit — practise both directions.')
q(Q, 2, 'A bag of flour is labelled 2 kilograms. What property does that 2 kg describe?',
  ['Mass', 'Volume', 'Length', 'Area'], 0,
  'Kilograms count stuff, not space.',
  ['Kilograms are the metric unit of mass.',
   'Mass is how much matter the flour contains.',
   'The bag\'s size (volume) could change if squashed — its 2 kg would not.'],
  '**Mass.** The amount of flour, not the space it fills.',
  'Squash the bag and the volume changes but the mass stays — that is the difference.')
q(Q, 2, 'A jewellery box measures 4 cm long, 5 cm wide and 2 cm tall. What is its volume?',
  ['40 cm³', '11 cm³', '40 cm', '22 cm³'], 0,
  'Multiply all three edges — and mind the unit.',
  ['V = l × w × h.',
   '4 × 5 = 20, then 20 × 2 = 40.',
   'Three lengths multiplied make cubic units: 40 cm³.'],
  '**40 cm³.** Multiply the edges, cube the unit.',
  '11 comes from adding the edges; 40 cm forgets the ³ — both are nameable, catchable errors.')
q(Q, 2, 'A fish tank measures 10 cm by 3 cm by 6 cm. What is its volume? Show your work in your head as you go.',
  ['180 cm³', '19 cm³', '180 cm', '36 cm³'], 0,
  'Two multiplications, then the cubic unit.',
  ['V = l × w × h = 10 × 3 × 6.',
   '10 × 3 = 30.',
   '30 × 6 = 180 — in cubic centimetres, 180 cm³.'],
  '**180 cm³.** Multiply in any order — 10 × 18 or 30 × 6 — the volume is the same.',
  'Choosing friendly pairs to multiply first is the mental-math habit from her math topic, working here too.')
q(Q, 3, 'A box has a volume of 60 cm³. Its base is 5 cm long and 4 cm wide. How tall is it?',
  ['3 cm', '51 cm', '12 cm', '20 cm³'], 0,
  'Run V = l × w × h backwards.',
  ['The base contributes 5 × 4 = 20.',
   'The volume equation says 20 × height = 60.',
   'Height = 60 ÷ 20 = 3 cm.',
   'Check forward: 5 × 4 × 3 = 60 ✓.'],
  '**3 cm.** Divide the volume by the base\'s two edges.',
  'A height is a length, so the answer carries cm — not cm³.')
q(Q, 3, 'Theo measures a box: 8 cm by 2 cm by 5 cm. He writes its volume as 15 cm³. What did he do wrong?',
  ['He added the edges instead of multiplying them',
   'He used the wrong units on a correct number',
   'He multiplied only two of the edges',
   'He measured one edge twice'], 0,
  'Where could 15 come from?',
  ['8 + 2 + 5 = 15 — that is a SUM.',
   'Volume multiplies: 8 × 2 × 5 = 80 cm³.',
   'His unit was right; the operation underneath it was not.'],
  '**He added instead of multiplied.** The right answer is 80 cm³.',
  'Naming the wrong move — added, not multiplied — is better feedback than "wrong".')
q(Q, 3, 'Why is volume written in CUBIC units, like cm³?',
  ['Because three lengths are multiplied, the unit is multiplied three times too',
   'Because volume is always measured with cube-shaped tools',
   'Because the 3 shows the answer was rounded to three places',
   'Because liquids come in three standard sizes'], 0,
  'Follow the units through the multiplication.',
  ['V = l × w × h multiplies three measurements.',
   'Each carries a cm, so the units multiply as well: cm × cm × cm.',
   'That product is written cm³ — and it literally counts unit cubes that fit inside.'],
  '**Three lengths multiply, so the unit cubes.** The ³ is bookkeeping, not decoration.',
  'Units obey the same arithmetic the numbers do — that idea will carry through years of science.')
q(Q, 3, 'A box measures 4 cm × 3 cm × 2 cm. If ONLY its height doubled, what would happen to its volume?',
  ['It would double', 'It would quadruple', 'It would grow by 2 cm³', 'It would stay the same'], 0,
  'One factor doubles — what happens to a product?',
  ['Original: 4 × 3 × 2 = 24 cm³.',
   'Doubled height: 4 × 3 × 4 = 48 cm³.',
   '48 is exactly twice 24 — doubling one factor doubles the product.'],
  '**It would double.** Each edge is a factor, and doubling one factor doubles the whole product.',
  'If ALL THREE edges doubled, the volume would multiply by 2 × 2 × 2 = 8 — try it.')
build('wayfinder', C, Q, 'unit-sci-meas', 'Science · Quiz 1 Part 2: Measurement', 'science',
      'The Measurements lesson check covers two skills: sorting observations into quantitative (numbers you can count or measure) and qualitative (descriptions from your senses), and choosing measurement units — the U.S. Customary and Metric systems, matching a unit to the property and size of the thing, and calculating the volume of a rectangular prism with V = l × w × h in cubic units.',
      'Measurement is where science stops being opinions — two people can argue about "big" but not about 43 centimetres. The unit-choice habit (right system, right property, right size) and the volume formula both come back every year, in every lab.',
      [('Sort an observation as quantitative or qualitative and say how you know.', 'source'),
       ('Choose an appropriately sized unit from the named system for length, volume or mass.', 'source'),
       ('Calculate the volume of a rectangular prism and explain the cubic unit.', 'source'),
       ('Work the volume formula backwards to find a missing edge.', 'added')],
      'Built from the graded Measurements lesson check (13 points) in the Quiz 1 Drive folder. Every question here is a fresh scenario — the check\'s own items stay her classwork. The stretch material is the last three questions: the backwards volume, the why-cubic reasoning, and the doubling counterfactual go past what the check asked, on purpose.',
      ('Cards first — the two systems and three properties need to be words before the choosing gets quick. Then a round or two.', 14),
      'content/science-measurement.json',
      'Measurements lesson check — Quiz 1 folder (Drive)',
      'Science 4, Quiz 1 material — the Measurements lesson check (Drive)',
      round_=8,
      # order:1 so it shelves BEHIND 'Quiz 1: Thinking Like a Scientist' —
      # alphabetically 'Quiz 1 Part 2' sorts before 'Quiz 1:', which would put
      # Part 2 above Part 1 on the shelf. Verified by rendering.
      order_=1)
print('--- science measurement built ---')
