# -*- coding: utf-8 -*-
"""River's Nature of Science unit test material — two units.

A) unit-sci-nos-practice — the teacher's own "Practice for Nature of Science
   Unit Test (19 Points)" transcribed VERBATIM as a guide unit, so she can do
   it on paper and enter her 19 letters. Option order is fixed (the whole mode
   is a lie otherwise). Every answer was independently re-derived and matched
   the teacher's circled key with zero discrepancies.

B) unit-sci-nos-test — a parallel study test, same 19 skills, an entirely
   fresh experiment (salt water and melting ice), ordinary shuffled quiz.
   Graphs are ours, so the plotted data and the answer agree by construction.
"""
import json, io, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def V(text, opts, ans, main, steps):
    """A rescue-round variant: same skill, fresh numbers, hand-verified."""
    return {'q': text, 'opts': [str(o) for o in opts], 'ans': ans,
            'steps': steps, 'ex': {'main': main}}

# ============================================================ A — the replica
C, Q = [], []

card(C, 'A scientific question',
     '**It has to be testable, about the natural world, and free of opinion.**'
     '\n• "How does the amount of sunlight per day affect how high plants grow?" works — you can measure it.'
     '\n• "Which baseball team is best?" is an opinion, and magic spells are not the natural world.',
     'Your teacher wrote it in the margin: no opinions, and it needs to be about the natural world.')
card(C, 'The Scientific Method',
     '**The process scientists use to answer a question.**'
     '\n• Ask a question → make a hypothesis → test it → collect data → draw a conclusion.'
     '\n• The Engineering Design Process is for building a solution, not answering a question.')
card(C, 'Hypothesis (prediction)',
     '**Your best guess at what the results will be, made BEFORE you test.**'
     '\n• It is a statement about the outcome, not a description of the setup.'
     '\n• Analysing data and writing down careful details are different steps that come later.')
card(C, 'Independent vs dependent variable',
     '**The independent variable is what YOU change. The dependent variable is what you MEASURE.**'
     '\n• Your teacher\'s trick: the independent variable comes right after "How does…"'
     '\n• In "How does the volume of water given daily affect the growth height of sunflower plants?" — '
     'volume of water is independent, growth height is dependent.',
     'Dependent DEPENDS on what you changed, so it is the thing you measure at the end.')
card(C, 'Controlled variables',
     '**Everything else you deliberately keep the same.**'
     '\n• Only ONE thing should change in an experiment — that is what makes it a fair test.'
     '\n• Same pot size, same soil, same spot in the yard, same time of day.',
     'Your teacher\'s note: only 1 thing changing, everything else kept the same.')
card(C, 'PPE — personal protective equipment',
     '**When a step has more than one hazard, wear all of the gear that fits it.**'
     '\n• Mixing fertiliser can splash (eyes), touch your skin (hands) and spill (feet).'
     '\n• Safety glasses, gloves and closed-toed shoes each answer a different hazard.')
card(C, 'Volume of a rectangular prism',
     '**V = length × width × height, and the answer is in cubic units (cm³).**'
     '\n• A pot 5 cm × 5 cm × 10 cm holds 5 × 5 × 10 = 250 cm³.'
     '\n• cm measures length, cm² measures area, cm³ measures volume — the unit tells you which.',
     'Three measurements multiplied means three little marks: cm³.', eq='V = l × w × h')
card(C, 'cm and mm',
     '**1 cm = 10 mm, so to go from cm to mm you multiply by 10.**'
     '\n• 23 cm × 10 = 230 mm.'
     '\n• Going the other way (mm to cm) you divide by 10.',
     'The smaller the unit, the BIGGER the number — mm are small, so the number grows.')
card(C, 'The metric system',
     '**Scientists measure in metric: metres, grams, litres and degrees Celsius.**'
     '\n• It is the same everywhere, so any scientist can repeat your experiment.',
     'Your teacher underlined this one: scientists use the metric system when doing experiments.')
card(C, 'Reading a scale',
     '**Work out what ONE space is worth first, then count spaces from the last labelled number.**'
     '\n• Gap between labels ÷ number of spaces = the value of one space.'
     '\n• Then answer in the unit the question asked for — 26 mm and 2.6 cm are the same length, '
     'but only one of them answers "to the nearest millimetre".')
card(C, 'Repeated trials',
     '**One trial is never enough — you run several and compare.**'
     '\n• A single plant might just be unlucky; ten plants show what is really happening.'
     '\n• More trials make your results more trustworthy, not just more work.',
     'Your teacher\'s margin note: should do multiple!')
card(C, 'Observation vs inference',
     '**An observation is what you notice. An inference is your explanation for WHY.**'
     '\n• Observation: "light green leaves", "25.4 cm tall", "thick, hairy stem".'
     '\n• Inference: "the shiny leaves reflect light to help the plant stay cool" — nobody measured that, '
     'it is a reason someone worked out.')
card(C, 'Quantitative vs qualitative',
     '**Quantitative data has numbers. Qualitative data describes.**'
     '\n• Quantitative: 38.7 cm tall, 34 petals, 11 leaves.'
     '\n• Qualitative: wavy edges on leaves, dark green bud, large flower with many yellow petals.',
     'QUANTity = a number you can count. QUALity = what it is like.')
card(C, 'Picking a graph',
     '**A double line graph shows a trend over time for two groups at once.**'
     '\n• A pie chart shows parts of a whole.'
     '\n• A bar graph compares amounts between categories.'
     '\n• Line graphs need quantitative data — you cannot plot "wavy leaves" on one.',
     'Your teacher wrote "know bar graphs too" — expect the same question about those.')
card(C, 'What every graph needs',
     '**A title, labels on both axes, and units on those labels.**'
     '\n• Numbers running up the side mean nothing until something says "Growth Height (cm)".'
     '\n• Check each one separately: a graph can have a title and still be missing its axis labels.')
card(C, 'A scientific diagram',
     '**A realistic drawing, with a title and every part labelled.**'
     '\n• A cartoon with a smiling face is art, not a diagram.'
     '\n• Labels with no title, or a drawing with no labels, each fail on their own.')
card(C, 'An evidence-based claim',
     '**Answer the question that was asked, then back it with data from your graph.**'
     '\n• "The more water, the bigger they grew" answers it but gives no evidence.'
     '\n• Describing the trends without saying what they mean gives evidence but no answer.'
     '\n• No "I saw…" or "I think…" — a claim is written about the plants, not about you.',
     'Your teacher\'s note: answer the question AND give evidence.')

def gq(lv, text, opts, ans, hint, steps, main, tip, variant, frm='source'):
    q(Q, lv, text, opts, ans, hint, steps, main, tip, frm=frm)
    Q[-1]['variant'] = variant

gq(1, 'Which of the following questions might a scientist ask?',
   ['What is the best baseball team New York: Yankees or Mets?',
    'What percentage of people like to eat sushi?',
    'How does the amount of sunlight per day affect how high plants will grow?',
    'How does the temperature of the air affect how well magic spells work?'], 2,
   'Two of these are about opinions or people\'s tastes, and one is not about the real world at all.',
   ['A scientific question has to be testable by measuring something.',
    'It also has to be about the natural world.',
    '"Best team" is an opinion, and magic spells are not part of the natural world.',
    'Sunlight and plant height can both be measured, so that is the scientific question.'],
   '**How does the amount of sunlight per day affect how high plants will grow?** '
   'You can change the sunlight, measure the height, and anyone could repeat it.',
   'Your teacher\'s margin note says it in five words: no opinions, natural world.',
   V('Which of these is a scientific question?',
     ['Which flavour of ice cream out of all of them tastes the very best?',
      'How does the amount of salt in water affect how fast an ice cube melts?',
      'Are the unicorns in stories faster runners than the dragons are?',
      'Should our school start an hour later than it does at the moment?'], 1,
     '**How does the amount of salt in water affect how fast an ice cube melts?** '
     'Salt can be measured out and melting time can be timed. The others are opinions or not real.',
     ['Ask whether you could measure the answer.',
      '"Tastes the best" and "should we" are opinions.',
      'Unicorns and dragons are not part of the natural world.',
      'Salt and melting time are both measurable, so that one is scientific.']))

gq(1, 'What process do scientists use to help answer questions?',
   ['The Engineering Design Process', 'The Scientific Method', 'Trial and Error', 'String Theory'], 1,
   'One of these is for building a solution, not for answering a question.',
   ['Scientists start with a question and work towards an answer.',
    'The Engineering Design Process is for designing and building something.',
    'Trial and error has no plan, and string theory is an idea in physics, not a method.',
    'The Scientific Method is the process.'],
   '**The Scientific Method.** Ask a question, make a hypothesis, test it, collect data, conclude.',
   'Engineers use the Engineering Design Process — same care, different goal.',
   V('A scientist wants to find out why a pond has fewer frogs this year. Which process should she follow?',
     ['The Scientific Method', 'The Engineering Design Process', 'Guess and check', 'The water cycle'], 0,
     '**The Scientific Method.** She has a question about the natural world and wants an answer, '
     'which is exactly what the Scientific Method is for.',
     ['Decide whether she is answering a question or building something.',
      'She wants to know WHY, so she is answering a question.',
      'The Engineering Design Process would be for building a frog habitat.',
      'The Scientific Method is the right process.']))

gq(1, 'When we make a prediction or state a hypothesis, what are we doing?',
   ['We are stating our best guess as to what we think the results will be in the experiment.',
    'Carefully examining all the things that could change in an experiment',
    'Analyzing the data we collected.',
    'Carefully observing the experiment and writing down accurate details.'], 0,
   'A hypothesis happens BEFORE you test. Which of these could you only do afterwards?',
   ['A hypothesis is made before the experiment starts.',
    'Analysing data and recording observations both need results, so they come later.',
    'Examining what could change is identifying variables, which is a different step.',
    'Stating your best guess at the results is the hypothesis.'],
   '**We are stating our best guess as to what we think the results will be.** '
   'It is a prediction about the outcome, written before you have any data.',
   'A hypothesis is allowed to turn out wrong — that is not a failed experiment.',
   V('A student writes: "I think the ice in salt water will melt faster than the ice in plain water." '
     'What has she written?',
     ['An observation', 'A hypothesis', 'A conclusion', 'A controlled variable'], 1,
     '**A hypothesis.** She has predicted the result before testing, which is exactly what a hypothesis is.',
     ['Check when she wrote it — before any data existed.',
      'An observation needs something to have happened already.',
      'A conclusion comes after the data is analysed.',
      'A prediction made in advance is a hypothesis.']))

gq(2, 'What is the DEPENDENT Variable for this scientific question: How does the volume of water '
      'given daily affect the growth height of sunflower plants?',
   ['Amount of sunlight', 'Volume of water', 'Growth height', 'Type of fertilizer in the soil'], 2,
   'Your teacher\'s trick: the INDEPENDENT variable comes right after "How does…"',
   ['The independent variable is what you change on purpose.',
    '"How does the volume of water…" — so volume of water is the independent variable.',
    'The dependent variable is what you measure to see the effect.',
    'You measure how tall the plants get, so growth height is the dependent variable.'],
   '**Growth height.** It is what you measure at the end. Volume of water is the independent variable — '
   'the one you changed — and sunlight and fertiliser are kept the same for every plant.',
   'Dependent DEPENDS on what you changed, so it is always the thing you measure.',
   V('In the question "How does the amount of salt in water affect how fast an ice cube melts?", '
     'what is the DEPENDENT variable?',
     ['Amount of salt in the water', 'How fast the ice melts', 'Size of the container', 'Room temperature'], 1,
     '**How fast the ice melts.** That is what gets measured. The amount of salt is what was changed, '
     'and container size and room temperature are kept the same.',
     ['Find what comes right after "How does" — that is the independent variable.',
      'The amount of salt is what you change.',
      'The dependent variable is what you measure.',
      'You time the melting, so melting speed is dependent.']))

gq(1, 'In order to do our experiment to answer our scientific question, we need to add fertilizer to '
      'the soil we plan to use and mix it vigorously to make sure it is well distributed in the soil. '
      'What Personal Protective Equipment (PPE) should we be using during this step if we want to be '
      'as safe as possible?',
   ['Safety Glasses', 'Gloves', 'Closed-toed shoes', 'All of the above'], 3,
   'Mixing something vigorously can go in more than one direction. Count the hazards.',
   ['Vigorous mixing can flick fertiliser upward, towards your eyes.',
    'Your hands are in contact with it the whole time.',
    'Anything spilled lands on your feet.',
    'Each piece of gear answers a different hazard, so you want all of them.'],
   '**All of the above.** The question asks how to be as safe as possible, and each item covers a '
   'hazard the others do not — eyes, skin, feet.',
   'When a question says "as safe as possible", check whether the options are covering different hazards.',
   V('A student is pouring salt into a beaker of water and stirring it hard. Which piece of PPE '
     'protects her from a splash reaching her eyes?',
     ['Closed-toed shoes', 'Gloves', 'Safety goggles', 'A lab apron'], 2,
     '**Safety goggles.** They are the only item on the list that covers the eyes. '
     'Each piece of PPE answers one particular hazard.',
     ['Name the hazard first: liquid flicking upward.',
      'Shoes protect feet and gloves protect hands.',
      'An apron protects clothes.',
      'Goggles are what guard the eyes.']))

gq(2, 'We will use separate pots for each seed that we plant. All the pots are the same size and have '
      'the same volume as the rectangular prism shown, with length 5 cm, width 5 cm and height 10 cm. '
      'What volume of soil will we need to use to completely fill each pot?',
   ['20 cm', '250 cm³', '25 cm²', '55 cm³'], 1,
   'Check the units as well as the number — volume is always in cubic units.',
   ['Volume of a rectangular prism is length × width × height.',
    '5 × 5 × 10 = 250.',
    'Three measurements were multiplied together, so the unit is cm³.',
    'That gives 250 cm³.'],
   '**250 cm³.** 5 × 5 × 10 = 250, and multiplying three lengths gives cubic centimetres. '
   '20 cm is what you get by adding, and 25 cm² is only the area of the base.',
   'The wrong options are each a real calculation done wrongly — check the unit and you catch them.',
   V('A box measures 4 cm long, 6 cm wide and 5 cm high. What is its volume?',
     ['15 cm', '24 cm²', '120 cm³', '120 cm²'], 2,
     '**120 cm³.** 4 × 6 × 5 = 120, and three lengths multiplied give cm³. '
     '24 cm² is just the area of one face.',
     ['Volume is length × width × height.',
      '4 × 6 = 24, and 24 × 5 = 120.',
      'Three measurements multiplied means cubic units.',
      'The answer is 120 cm³.']))

gq(1, 'We measured the size of the pots the plant will be going in. We calculate that they are 23 cm. '
      'How many mm is this?',
   ['23 mm', '2.3 mm', '230 mm', '10 mm'], 2,
   'Millimetres are smaller than centimetres, so the number has to get bigger.',
   ['There are 10 mm in 1 cm.',
    'Going from cm to mm means multiplying by 10.',
    '23 × 10 = 230.',
    'So 23 cm is 230 mm.'],
   '**230 mm.** 1 cm = 10 mm, so 23 × 10 = 230. Dividing instead would give 2.3, which is the trap.',
   'A smaller unit always needs a bigger number to measure the same length.',
   V('A leaf is 9 cm long. How many millimetres is that?',
     ['0.9 mm', '90 mm', '9 mm', '900 mm'], 1,
     '**90 mm.** There are 10 mm in every centimetre, so 9 × 10 = 90.',
     ['1 cm = 10 mm.',
      'Centimetres to millimetres means multiply by 10.',
      '9 × 10 = 90.',
      'The leaf is 90 mm long.']))

gq(2, 'Outside air temperature where the plants are growing needs to be measured every day. '
      'The thermometer looks like this on day 1. What temperature is indicated on the thermometer? '
      'Round to the nearest °C.',
   ['30°C', '27°C', '25°C', '33°C'], 1,
   'Find the labelled number below the liquid first, then count the small marks up from it.',
   ['The thermometer is labelled every 10 °C, and ten small marks divide each 10 into single degrees.',
    'The red column stops between the 20 and the 30.',
    'Counting up from 20, the top of the column sits on the seventh mark.',
    '20 + 7 = 27 °C.'],
   '**27°C.** Work out what one mark is worth before you read anything: 10 °C split into 10 spaces '
   'means each mark is 1 °C.',
   'Guessing "about 30" because it looks close is the mistake this question is built to catch.',
   V('A thermometer is labelled every 10 °C, and the marks divide each 10 °C into 10 equal spaces. '
     'The liquid stops 4 spaces above the 30 °C label. What is the temperature?',
     ['30.4 °C', '34 °C', '40 °C', '3.4 °C'], 1,
     '**34 °C.** Each space is 10 ÷ 10 = 1 °C, so four spaces above 30 is 34 °C.',
     ['Work out one space: 10 °C ÷ 10 spaces = 1 °C each.',
      'Start at the labelled number, 30 °C.',
      'Count up 4 spaces, which is 4 °C.',
      '30 + 4 = 34 °C.']))

gq(2, 'Twenty sunflower seeds are each planted in a separate pot. They are all placed outside in the '
      'same place in the yard. They are watered once per day. Ten plants receive 50 mL per day and the '
      'other ten plants receive 100 mL per day. While measuring water for one of the plants that should '
      'get 50 mL, we overfill the graduated cylinder. What is the volume of water indicated on this '
      'graduated cylinder? Measure to the nearest milliliter (mL).',
   ['80 mL', '99 mL', '81 mL', '83 mL'], 2,
   'Read the bottom of the curved surface, and check which labelled line it is just past.',
   ['The cylinder is labelled every 10 mL, with ten marks dividing each 10 into single millilitres.',
    'The water surface sits just above the line labelled 80.',
    'It is one mark above it, and one mark is 1 mL.',
    '80 + 1 = 81 mL.'],
   '**81 mL.** Reading exactly 80 ignores that the surface is above the line; 99 comes from counting '
   'down from 100 instead of up from 80.',
   'Always read a liquid at the bottom of its curve — that dip is called the meniscus.',
   V('A graduated cylinder is labelled every 10 mL, and the marks divide each 10 mL into 5 equal spaces. '
     'The bottom of the meniscus sits 2 spaces above the 40 mL line. What volume is in the cylinder?',
     ['42 mL', '50 mL', '44 mL', '46 mL'], 2,
     '**44 mL.** Each space is 10 ÷ 5 = 2 mL, so two spaces above 40 mL is 40 + 4 = 44 mL.',
     ['Find the value of one space: 10 mL ÷ 5 spaces = 2 mL.',
      'Start at the labelled line, 40 mL.',
      'Two spaces is 2 × 2 = 4 mL.',
      '40 + 4 = 44 mL.']))

gq(2, 'After one week, the tiny seedlings are not very tall, but each one is measured from the top of '
      'the soil to the top of the stem. Measure this seedling to the nearest millimeter (mm).',
   ['26 mm', '2.6 mm', '2.6 cm', '34 mm'], 0,
   'Two of these are the same length written differently. Which unit did the question ask for?',
   ['The ruler is marked in centimetres with 10 small marks in each one, so each mark is 1 mm.',
    'The top of the stem reaches just past the 2 cm line, on the sixth small mark.',
    'That is 2 cm and 6 mm, which is 26 mm.',
    'The question asked for millimetres, so the answer is 26 mm.'],
   '**26 mm.** 2.6 cm is the same length and your teacher wrote "know cm too" beside it — but the '
   'question asked for millimetres, and only one option is in millimetres and correct.',
   'When two options are the same length in different units, the question\'s own unit decides it.',
   V('A ruler is marked in centimetres with 10 small marks inside each centimetre. A worm reaches from '
     '0 to 4 small marks past the 7 cm line. How long is the worm in millimetres?',
     ['11 mm', '7.4 mm', '74 mm', '7.4 cm'], 2,
     '**74 mm.** Each small mark is 1 mm, so 7 cm and 4 mm is 70 + 4 = 74 mm. '
     '7.4 cm is the same length, but the question asked for millimetres.',
     ['Each small mark inside a centimetre is 1 mm.',
      '7 cm is 70 mm.',
      'Four more marks adds 4 mm.',
      '70 + 4 = 74 mm.']))

gq(1, 'True or False: We should only do one trial during any experiment.',
   ['True', 'False'], 1,
   'Think about what happens if the single plant you picked happened to be a weak seed.',
   ['One trial gives you one result, with nothing to compare it against.',
    'Anything unusual about that one plant would look like a real finding.',
    'Running many trials shows what is actually happening rather than a one-off.',
    'So the statement is false.'],
   '**False.** Repeated trials are what make a result trustworthy — that is why the experiment uses '
   'ten plants at each watering level rather than one.',
   'Your teacher\'s margin note: should do multiple!',
   V('Why does an experiment testing melting ice use ten ice cubes in each group instead of one?',
     ['Because a single cube on its own would take far too long to finish melting',
      'Because a single odd result cannot then be mistaken for a real finding',
      'Because ten is the number of trials that scientists always have to use',
      'Because a graph drawn from ten cubes looks a good deal better than one'], 1,
     '**Because a single odd result cannot then be mistaken for a real finding.** '
     'Repeated trials show what is really happening rather than one cube\'s bad luck.',
     ['Imagine the one cube you picked was slightly bigger than the rest.',
      'With a single trial you would have no way of knowing.',
      'Several trials let you see the pattern across all of them.',
      'That is why repeated trials matter.']))

gq(2, 'Three weeks into the experiment, we make the following observations for one of the plants. '
      'Which of these observations is actually an INFERENCE?',
   ['Light green leaves', '25.4 cm tall',
    'The wide, shiny leaves reflect light as a way to help the plant stay cool on hot days.',
    'Thick, hairy stem'], 2,
   'Three of these you could write down just by looking. One of them explains WHY.',
   ['An observation is something you notice directly with your senses or a measuring tool.',
    'Light green, 25.4 cm and thick and hairy are all noticed directly.',
    'Nobody measured that the leaves are cooling the plant — that is a reason someone worked out.',
    'So the shiny-leaves statement is the inference.'],
   '**The wide, shiny leaves reflect light as a way to help the plant stay cool on hot days.** '
   'The shine can be observed; the PURPOSE behind it is an explanation, and explanations are inferences.',
   'The words "as a way to" and "because" are usually a sign an inference has crept in.',
   V('A student writes four notes about a melting ice cube. Which one is an INFERENCE?',
     ['The cube measures 3 cm across at its very widest point',
      'A puddle has spread out all the way around the base of the cube',
      'The cube melted faster because the salt lowered the freezing point',
      'The water sitting in the cup looks cloudy rather than clear'], 2,
     '**The cube melted faster because the salt lowered the freezing point.** '
     'The other three were noticed directly. This one gives a reason, which nobody observed.',
     ['Ask which ones you could write down just by looking or measuring.',
      'Size, puddle and cloudiness are all directly noticed.',
      'The word "because" introduces an explanation.',
      'An explanation of why is an inference.']))

gq(3, 'Four weeks into the experiment, we decide to graph our data that we have collected so far. '
      'For the plants that are receiving 100 mL water per day, predict what the average plant height '
      'will be at 5 weeks based on the current trend.',
   ['26 cm', '34 cm', '45 cm', '28 cm'], 1,
   'Work out how much the line climbs each week, then add one more week of that climb.',
   ['On the graph the 100 mL line reaches about 25 cm at week 4.',
    'Looking back, it has been climbing by roughly 8 to 9 cm each week.',
    'Adding one more week of that climb gives about 34 cm.',
    '45 cm would need the line to suddenly jump, and 26 or 28 cm would mean it almost stopped.'],
   '**34 cm.** Predicting from a trend means continuing the pattern the line is already making, '
   'not just reading the last point you can see.',
   'Extending a trend like this is called extrapolation — you are reading past the end of your data.',
   V('An ice cube in plain water loses about 6 g every 2 minutes. At 10 minutes it has 30 g left. '
     'Based on that trend, what will its mass be at 12 minutes?',
     ['30 g', '18 g', '24 g', '36 g'], 2,
     '**24 g.** The cube loses 6 g every 2 minutes, so from 30 g at 10 minutes it drops to 24 g at 12.',
     ['Find the pattern: 6 g lost every 2 minutes.',
      'Going from 10 minutes to 12 minutes is one more 2-minute step.',
      'So it loses 6 g more.',
      '30 − 6 = 24 g.']))

gq(2, 'Why did we decide to use a double line graph to plot our data?',
   ['Because it shows parts of a whole',
    'Because it allows us to graph only qualitative data',
    'Because we can see trends over time for both sets of plants',
    'Because it would look prettier'], 2,
   'Each wrong option describes a different graph, or no reason at all.',
   ['A pie chart is what shows parts of a whole.',
    'Line graphs need numbers, so they cannot plot qualitative data.',
    '"Prettier" is not a scientific reason for anything.',
    'A double line graph shows how both groups changed over time, side by side.'],
   '**Because we can see trends over time for both sets of plants.** '
   'Two lines on one pair of axes let you compare the 50 mL group and the 100 mL group directly.',
   'Your teacher wrote "know bar graphs too" beside this — a bar graph compares amounts between '
   'categories, where a line graph shows change over time.',
   V('A student measures the mass of two ice cubes every 2 minutes for 10 minutes. '
     'Which graph should she use?',
     ['A pie chart showing each cube as a slice',
      'A double line graph',
      'A single bar for the whole experiment',
      'A labelled diagram of the two cups'], 1,
     '**A double line graph.** She has two groups measured repeatedly over time, and a line graph '
     'is what shows change over time for both at once.',
     ['She has measurements at many points in time.',
      'She also has two groups to compare.',
      'A pie chart shows parts of a whole, not change.',
      'Two lines over time is a double line graph.']))

gq(1, 'Six weeks into the experiment, we make the following observations for one of the plants. '
      'Which of these observations is QUANTITATIVE?',
   ['Wavy edges on leaves', '38.7 cm tall', 'Dark green bud forming at top of stem', 'Thick, hairy stem'], 1,
   'Quantitative starts with the same letters as QUANTity.',
   ['Quantitative data is data with numbers in it.',
    'Wavy edges, dark green and thick and hairy are all descriptions.',
    'Only one option carries a measurement.',
    '38.7 cm tall is the quantitative observation.'],
   '**38.7 cm tall.** It is a measured number. The other three describe what the plant is like, '
   'which makes them qualitative.',
   'Your teacher\'s note here was a single word: numbers!',
   V('Which of these is QUANTITATIVE data about a melting ice cube?',
     ['It feels slippery', 'The water is cloudy', 'It took 14 minutes to melt', 'The edges look rounded'], 2,
     '**It took 14 minutes to melt.** It is a measured number. The other three describe what the '
     'cube was like, which is qualitative.',
     ['Quantitative data has numbers in it.',
      'Slippery, cloudy and rounded are all descriptions.',
      'Only one option gives a measurement.',
      '14 minutes is the quantitative one.']))

gq(2, 'At 8 weeks we also decide to graph all of our data collected so far. We make this graph, but we '
      'forget to add some of the necessary parts of the graph. What is missing from this graph?',
   ['Title and axis labels', 'Lines connecting data and units', 'Axis labels and units',
    'Trend lines and title'], 2,
   'Check each part separately. Does the graph have a title? Are the points joined up?',
   ['The graph does have a title across the top, so anything naming the title is out.',
    'The points are joined by lines, so nothing is missing there either.',
    'Numbers run up the side and across the bottom with nothing saying what they measure.',
    'What is missing is the axis labels and their units.'],
   '**Axis labels and units.** Numbers alone do not say whether the side is centimetres, grams or '
   'weeks — the label and its unit are what make a graph readable.',
   'Rule out the options one part at a time. Three of the four name something the graph already has.',
   V('A student\'s graph has a title, a legend, and both sets of points joined with lines. '
     'The numbers up the side and along the bottom have nothing written beside them saying what they '
     'measure. What is missing?',
     ['A title', 'Axis labels and units', 'Lines connecting the data', 'A legend'], 1,
     '**Axis labels and units.** Everything else in the list is described as already present. '
     'Numbers with no label do not tell you what is being measured.',
     ['Go through the list and cross off what the graph already has.',
      'It has a title, a legend and joined-up lines.',
      'The only thing described as absent is what the numbers mean.',
      'That is the axis labels and their units.']))

gq(2, 'At 9 weeks, one of the plants that received 100 mL of water per day blooms. Which of these '
      'images is the best scientific diagram of the sunflower plant?',
   ['Diagram A', 'Diagram B', 'Diagram C', 'Diagram D'], 3,
   'A scientific diagram needs three things at once. Check each picture for all three.',
   ['A scientific diagram needs a title, labelled parts, and a realistic drawing.',
    'Diagram A is a cartoon with a face — that is art, not science.',
    'Diagram B has no labels at all, and Diagram C has labels but no title.',
    'Diagram D has the title, the labels and a realistic drawing, so it is the best one.'],
   '**Diagram D.** Your teacher marked exactly why each of the others fails: A is a cartoon, '
   'B has no labels, C has no title. Only D does all three jobs.',
   'When a question asks for the BEST, look for the one option that fails on nothing.',
   V('Which of these describes the best scientific diagram of a plant?',
     ['A colourful cartoon drawing with a smiling face and no labels',
      'A realistic drawing with every part labelled and a title at the top',
      'A realistic drawing with no labels and no title',
      'A neat drawing with labelled parts but no title'], 1,
     '**A realistic drawing with every part labelled and a title at the top.** '
     'A scientific diagram needs all three: realistic, labelled, and titled. The others each miss one.',
     ['List what a scientific diagram needs: realistic, labelled, titled.',
      'A cartoon fails on realistic and on labels.',
      'The other two each drop one of the three.',
      'Only one option has all three.']))

gq(1, 'After 10 weeks, our experiment is complete. We make the following observations for one of the '
      'plants that received 100 mL of water per day. Which of these is QUALITATIVE data?',
   ['Large flower with many yellow petals', 'Flower has 34 petals', 'Flower measures 23.5 cm across',
    '11 leaves on stem'], 0,
   'This one is the opposite of the earlier question. Which option has no number in it?',
   ['Qualitative data describes rather than counts.',
    '34 petals, 23.5 cm and 11 leaves are all measurements.',
    '"Large" and "many" describe without giving a number.',
    'So the large flower with many yellow petals is the qualitative observation.'],
   '**Large flower with many yellow petals.** "Large" and "many" are descriptions, not counts. '
   'Notice how close it is to "34 petals" — the difference is whether anyone actually counted.',
   'Your teacher\'s note: descriptive!',
   V('Which of these is QUALITATIVE data about a puddle?',
     ['It is 12 cm wide', 'The water looks murky and green', 'It is 3 mm deep',
      'It covers 40 square centimetres'], 1,
     '**The water looks murky and green.** It describes the puddle without measuring it. '
     'The other three are all numbers.',
     ['Qualitative data describes; quantitative data counts.',
      '12 cm, 3 mm and 40 square centimetres are measurements.',
      'Murky and green describe how it looks.',
      'That is the qualitative one.']))

gq(3, 'Now it is time to write our conclusion. Using the following graph as evidence, which of these '
      'written answers is the best evidence-based claim for the original question we asked in our '
      'experiment? [How does the volume of water given daily affect the growth height of sunflower plants?]',
   ['I saw that the plants with only 50 mL of water per day did well at the beginning, but then they '
    'kind of stopped growing, so I think 100 mL of water is the right amount.',
    'The more water the plants got, the bigger they grew.',
    'The plants that received 100 mL had an increasing trend in growth height, and the plants that '
    'only got 50 mL had no change after 5 weeks.',
    'A larger volume of water given daily resulted in larger growth heights for sunflower plants. '
    'Plants that received 100 mL of water per day showed a steadily increasing trend over time, while '
    'plants that only received 50 mL per day showed no change in growth height after 5 weeks.'], 3,
   'A good claim does TWO jobs. Check each option for both of them.',
   ['A claim has to answer the question that was asked.',
    'It also has to back that answer with evidence from the data.',
    'One option is written as "I saw" and "I think", which is personal rather than scientific.',
    'One answers with no evidence, and one gives evidence without ever answering.',
    'Only the last option answers the question AND supplies the trends as evidence.'],
   '**A larger volume of water given daily resulted in larger growth heights for sunflower plants…** '
   'Your teacher marked the other three: no pronouns, no evidence, no answer. This one does both jobs '
   'and keeps itself out of the sentence.',
   'Write a claim about the plants, never about yourself — "I saw" and "I think" do not belong in one.',
   V('A student tests whether salt makes ice melt faster. The salted cube was fully melted at '
     '10 minutes; the plain cube still had half its mass left. Which is the best evidence-based claim?',
     ['I think that salt probably melts ice quicker than plain water does, from what I saw.',
      'Salt made the ice melt faster than it would have done in ordinary plain water.',
      'Adding salt to the water made the ice melt faster. The salted cube had fully melted by '
      '10 minutes, while the cube in plain water still had half its mass left.',
      'The salted cube had melted away by 10 minutes and the plain cube still had half its mass '
      'sitting there at exactly the same moment.'], 2,
     '**Adding salt to the water made the ice melt faster, with the 10-minute results as evidence.** '
     'It answers the question and backs it with data. The first uses "I think", the second gives no '
     'evidence, and the last gives evidence but never states what it means.',
     ['A claim must answer the question and give evidence.',
      '"I think" makes it personal rather than scientific.',
      '"Salt made the ice melt faster" answers but proves nothing.',
      'Listing the results alone never says what they show.',
      'The one that names the effect AND quotes the 10-minute results does both jobs.']))

assert len(Q) == 19, len(Q)
for i, x in enumerate(Q):
    assert x.get('variant'), x['id']
    assert x['variant']['q'].strip() != x['q'].strip()

PAPER_KEY = 'CBACDBCBCABCBCBCDAD'
got = ''.join('ABCD'[x['ans']] for x in Q)
assert got == PAPER_KEY, (got, PAPER_KEY)   # option order is FIXED: never _balance a guide unit

unitA = {
  'id': 'unit-sci-nos-practice', 'type': 'unit', 'classId': 'science',
  'title': 'Science · Nature of Science Practice Test', 'status': 'draft',
  'guide': True, 'prep': True, 'order': 4, 'quarter': 1, 'libv': 1,
  'srcName': 'Practice for Nature of Science Unit Test + answer key (Drive)',
  'source': 'source',
  'summary': {'from': 'source', 'text':
    'Your teacher\'s "Practice for Nature of Science Unit Test", all 19 questions, exactly as they '
    'appear on the paper and in the same A/B/C/D order. It walks through one experiment from start '
    'to finish — how does the volume of water given daily affect the growth height of sunflower '
    'plants — and asks a different Nature of Science skill at each step.'},
  'why': {'from': 'added', 'text':
    'This is the shape of the real unit test, so the useful thing is not just getting the answers '
    'right but noticing which skill each question is testing. Nineteen questions, nineteen different '
    'moves: asking a testable question, naming variables, staying safe, reading instruments, telling '
    'observation from inference, reading a graph, and writing a claim that actually uses evidence.'},
  'objectives': [
    {'from': 'source', 'text': 'Tell a scientific question from an opinion or a made-up one.'},
    {'from': 'source', 'text': 'Name the independent and dependent variables in a question.'},
    {'from': 'source', 'text': 'Read a thermometer, a graduated cylinder and a ruler, and answer in the unit asked for.'},
    {'from': 'source', 'text': 'Tell observation from inference, and quantitative from qualitative.'},
    {'from': 'source', 'text': 'Read a double line graph and predict from its trend.'},
    {'from': 'added', 'text': 'Write a conclusion that answers the question and cites the data.'}],
  'parentNote': {'from': 'added', 'text':
    'This is the teacher\'s practice test copied out word for word, with the options in the same '
    'order as the paper, so the "I did it on paper" door works: she does the 19 questions on the '
    'printout and taps in the letters she wrote. Every answer was re-derived independently before '
    'this was built and all 19 matched the teacher\'s circled key exactly — no misprints this time. '
    'One thing to know: eight of the questions rely on a picture she has on paper (a prism, a '
    'thermometer, a graduated cylinder, a ruler, three graphs and four diagrams). Those pictures are '
    'not reproduced in the app, so the paper needs to be beside her; the walkthrough after grading '
    'describes what each picture showed. The teacher\'s own margin notes were the most useful thing '
    'in the key and are on the flashcards as written — "no opinions, natural world", "independent '
    'comes after How does", "should do multiple trials", "know bar graphs too", "numbers!", '
    '"descriptive!", "answer question and give evidence". Those read like a list of what the real '
    'test will ask.'},
  'nextUp': {'from': 'added', 'minutes': 25, 'text':
    'Do the paper first with the printout in front of you, then tap in your 19 letters. '
    'Anything you miss, the rescue round asks again with fresh numbers.'},
  'cards': C, 'questions': Q,
  'updatedAt': int(time.time() * 1000) - 3 * 3600 * 1000,
}

# ======================================================== B — the study test
C2, Q2 = [], []

card(C2, 'The four steps of a fair test',
     '**Change ONE thing, measure ONE thing, keep everything else the same, and repeat it.**'
     '\n• The one you change is the independent variable.'
     '\n• The one you measure is the dependent variable.'
     '\n• Everything else is a controlled variable.', frm='source')
card(C2, 'Finding the variables fast',
     '**The independent variable comes right after "How does". The dependent variable comes after "affect".**'
     '\n• "How does the amount of salt in water affect how fast an ice cube melts?"'
     '\n• Independent: amount of salt. Dependent: how fast it melts.',
     'Your teacher\'s own trick, written in the margin of the answer key.', frm='source')
card(C2, 'Reading any scale',
     '**Gap between two labelled numbers ÷ number of spaces between them = what one space is worth.**'
     '\n• Then count spaces up from the labelled number below.'
     '\n• Finish by answering in the unit the question asked for.', frm='added')
card(C2, 'Observation or inference?',
     '**If you noticed it, it is an observation. If you explained it, it is an inference.**'
     '\n• "The puddle is 12 cm wide" — observation.'
     '\n• "The puddle formed because the ice melted" — inference.'
     '\n• Watch for "because", "so that" and "as a way to".', frm='source')
card(C2, 'Quantitative or qualitative?',
     '**Quantitative has numbers. Qualitative describes.**'
     '\n• "34 petals" is quantitative; "many petals" is qualitative.'
     '\n• The same thing can be recorded either way — what matters is whether anyone counted.',
     'QUANTity = count. QUALity = what it is like.', frm='source')
card(C2, 'Which graph, and why',
     '**Line graph for change over time. Bar graph to compare categories. Pie chart for parts of a whole.**'
     '\n• Two groups measured over the same time period means a DOUBLE line graph.'
     '\n• Every one of them needs quantitative data — you cannot plot a description.', frm='source')
card(C2, 'What a finished graph has',
     '**A title, both axes labelled, units on those labels, and a legend when there is more than one line.**'
     '\n• Check them one at a time — a graph can have a title and still be missing its units.', frm='source')
card(C2, 'A claim that would earn full marks',
     '**Answer the question in a sentence, then give the numbers that prove it.**'
     '\n• No "I saw" or "I think" — write about the experiment, not about yourself.'
     '\n• An answer with no evidence, or evidence with no answer, only gets half the job done.',
     'Your teacher underlined "evidence-based" on the key.', frm='source')

MELT = {'w': [0, 12, 0, 70], 'xl': 'Time (minutes)', 'yl': 'Mass of ice (g)',
        'series': [
          {'type': 'pts', 'pts': [[0, 60], [2, 54], [4, 48], [6, 42], [8, 36], [10, 30]]},
          {'type': 'pts', 'pts': [[0, 60], [2, 48], [4, 36], [6, 24], [8, 12], [10, 2]]}],
        # renderGraph has no legend; a labelled point at the end of each line
        # names it on the plot itself, so "the plain-water cube" is unambiguous.
        'pts': [{'x': 10, 'y': 30, 'label': 'plain water'}, {'x': 10, 'y': 2, 'label': 'salt water'}]}

def sq(lv, text, opts, ans, hint, steps, main, tip, frm='added', graph=None):
    q(Q2, lv, text, opts, ans, hint, steps, main, tip, frm=frm)
    if graph: Q2[-1]['graph'] = graph

sq(1, 'Which of these could a scientist investigate?',
   ['Which season of the whole year is the most beautiful one to look at?',
    'How does the amount of salt in water affect how fast an ice cube melts?',
    'Are the fairies at the bottom of the garden real or completely imaginary?',
    'Should every family in the country be made to recycle their rubbish?'], 1,
   'Two of these ask for an opinion, and one is not about the real world.',
   ['A scientific question must be testable by measuring something.',
    'It must also be about the natural world.',
    '"Most beautiful" and "should everyone" ask for opinions.',
    'Fairies are not part of the natural world.',
    'Salt and melting time can both be measured, so that is the investigable question.'],
   '**How does the amount of salt in water affect how fast an ice cube melts?** '
   'You can measure out the salt, time the melting, and anyone could repeat it and check.',
   'Opinion words — best, most beautiful, should — are the quickest way to spot a question science cannot answer.',
   frm='source')

sq(1, 'A scientist wants to know why fewer bees are visiting a garden this summer. '
      'Which process should she follow?',
   ['The Engineering Design Process', 'Trial and error', 'The Scientific Method', 'The rock cycle'], 2,
   'One of these is for building something rather than finding something out.',
   ['She has a question about the natural world and wants an answer.',
    'The Engineering Design Process is for designing and building a solution.',
    'Trial and error has no plan behind it.',
    'The Scientific Method is the process for answering a question.'],
   '**The Scientific Method.** Ask, hypothesise, test, collect data, conclude. '
   'She would use the Engineering Design Process if she were building the bees a new habitat.',
   'Both processes are careful and both are science — they just answer different kinds of question.',
   frm='source')

sq(1, 'Before starting, a student writes: "I predict that the ice in salt water will melt faster than '
      'the ice in plain water." What has she written?',
   ['A conclusion', 'A hypothesis', 'An observation', 'A controlled variable'], 1,
   'Look at WHEN she wrote it — before there was any data at all.',
   ['A hypothesis is written before the experiment, predicting the outcome.',
    'A conclusion needs results, so it comes at the end.',
    'An observation needs something to have happened for her to notice.',
    'A prediction of the result, written in advance, is a hypothesis.'],
   '**A hypothesis.** It is a prediction of what will happen, made before any testing. '
   'It is allowed to turn out wrong — a wrong hypothesis is not a failed experiment.',
   'A hypothesis is a statement about the RESULT, not a description of the setup.',
   frm='source')

sq(2, 'In an experiment asking "How does the amount of salt in water affect how fast an ice cube '
      'melts?", what is the INDEPENDENT variable?',
   ['How long the cube takes to melt', 'The amount of salt added to the water',
    'The size of the container', 'The temperature of the room'], 1,
   'Your teacher\'s trick: the independent variable comes right after "How does".',
   ['The independent variable is the one you change on purpose.',
    'Reading the question: "How does the amount of salt…" — that is what is being changed.',
    'Melting time is what gets measured, so that is dependent.',
    'Container size and room temperature are kept the same for every cube.'],
   '**The amount of salt added to the water.** It is the one thing being deliberately changed, '
   'which is what makes it independent.',
   'Independent comes after "How does"; dependent comes after "affect".',
   frm='source')

sq(2, 'A student tests how the amount of salt in water affects how fast an ice cube melts. '
      'Which of these is a CONTROLLED variable?',
   ['The amount of salt in each cup', 'How long each cube takes to melt',
    'The starting mass of every ice cube', 'Whether salt makes ice melt faster'], 2,
   'A controlled variable is one you deliberately keep identical for every trial.',
   ['The amount of salt is what is being changed, so it is independent.',
    'Melting time is what is measured, so it is dependent.',
    'If some cubes started bigger, you could not tell whether salt or size caused the difference.',
    'Keeping every cube the same starting mass is a controlled variable.'],
   '**The starting mass of every ice cube.** Only one thing should change in a fair test, so '
   'everything else — cube size, water volume, room temperature — is deliberately held the same.',
   'A controlled variable is not "the control group". It is a condition you keep identical.',
   frm='source')

sq(2, 'A student is stirring salt into hot water hard enough to splash. Which piece of PPE guards '
      'the hazard of liquid reaching her eyes?',
   ['Closed-toed shoes', 'A lab apron', 'Gloves', 'Safety goggles'], 3,
   'Name the hazard first, then find the one piece of gear that covers that part of her.',
   ['The hazard is hot liquid flicking upward.',
    'Shoes protect her feet and an apron protects her clothes.',
    'Gloves protect her hands.',
    'Only goggles cover the eyes.'],
   '**Safety goggles.** Each piece of PPE answers one particular hazard — the trick is to name '
   'the hazard before choosing the gear.',
   'When a question instead asks how to be "as safe as possible", check whether several hazards '
   'are in play at once.',
   frm='source')

sq(2, 'Each ice cube is frozen in a mould shaped like a rectangular prism, 4 cm long, 3 cm wide and '
      '2 cm high. What volume of water fills one mould?',
   ['9 cm', '12 cm²', '24 cm³', '24 cm²'], 2,
   'Multiply all three, then think about how many little marks the unit needs.',
   ['Volume of a rectangular prism is length × width × height.',
    '4 × 3 = 12, and 12 × 2 = 24.',
    'Three lengths multiplied together give cubic units.',
    'So the volume is 24 cm³.'],
   '**24 cm³.** 4 × 3 × 2 = 24, and multiplying three measurements gives cm³. '
   '12 cm² is only the area of one face, and 9 cm comes from adding instead of multiplying.',
   'The unit is half the answer: cm is a length, cm² an area, cm³ a volume.',
   frm='source')

sq(1, 'A container is 8 cm tall. How many millimetres is that?',
   ['0.8 mm', '18 mm', '80 mm', '800 mm'], 2,
   'Millimetres are smaller than centimetres, so the number must get bigger — but only by ten times.',
   ['There are 10 mm in every centimetre.',
    'Going from cm to mm means multiplying by 10.',
    '8 × 10 = 80.',
    'So 8 cm is 80 mm.'],
   '**80 mm.** 1 cm = 10 mm, so 8 × 10 = 80. Dividing gives 0.8, and multiplying twice gives 800 — '
   'both are the same mistake in different directions.',
   'A smaller unit always needs a bigger number for the same length.',
   frm='source')

sq(2, 'A thermometer is labelled every 10 °C, and the small marks divide each 10 °C into 10 equal '
      'spaces. The liquid stops 3 spaces above the 20 °C label. What temperature is it showing?',
   ['20.3 °C', '23 °C', '26 °C', '50 °C'], 1,
   'Work out what one space is worth before you read anything off the scale.',
   ['The gap between labels is 10 °C, split into 10 spaces.',
    '10 ÷ 10 = 1, so each space is worth 1 °C.',
    'Start at the labelled number below the liquid, which is 20 °C.',
    'Three spaces up is 3 °C more, so 20 + 3 = 23 °C.'],
   '**23 °C.** Finding the value of one space first is the whole method — after that it is just '
   'counting up from the nearest labelled number.',
   'Never assume a small mark is worth 1. On a scale split into 5 spaces it would be worth 2.',
   frm='source')

sq(2, 'A graduated cylinder is labelled every 10 mL, and the marks divide each 10 mL into 5 equal '
      'spaces. The bottom of the meniscus sits 3 spaces above the 60 mL line. What volume of water '
      'is in the cylinder?',
   ['63 mL', '66 mL', '70 mL', '65 mL'], 1,
   'Five spaces to a 10 mL gap means each space is worth more than one millilitre.',
   ['The gap between labels is 10 mL, split into 5 spaces.',
    '10 ÷ 5 = 2, so each space is worth 2 mL.',
    'Three spaces above 60 mL is 3 × 2 = 6 mL.',
    '60 + 6 = 66 mL.'],
   '**66 mL.** Counting the spaces as 1 mL each would give 63 mL, which is exactly the trap. '
   'Always divide the gap by the number of spaces first.',
   'Read the liquid at the bottom of its curve — that dip is the meniscus.',
   frm='source')

sq(2, 'A ruler is marked in centimetres, with 10 small marks inside each centimetre. An ice cube '
      'measures from 0 to 4 small marks past the 3 cm line. How wide is it in millimetres?',
   ['3.4 mm', '34 mm', '7 mm', '3.4 cm'], 1,
   'Two of these are the same width written differently. Check which unit was asked for.',
   ['Ten marks inside each centimetre means each mark is 1 mm.',
    '3 cm is 30 mm.',
    'Four more marks adds 4 mm.',
    '30 + 4 = 34 mm.'],
   '**34 mm.** 3.4 cm is the very same width, but the question asked for millimetres, and only one '
   'option is both correct and in millimetres.',
   'When two options are the same length in different units, the question\'s own unit decides it.',
   frm='source')

sq(1, 'Why does the melting-ice experiment use ten cubes in each group instead of one?',
   ['Because ten is the number scientists always use',
    'Because one cube would melt too slowly to measure',
    'So that one unusual cube cannot be mistaken for a real result',
    'Because it makes the graph look fuller'], 2,
   'Imagine the single cube you picked happened to be slightly bigger than the rest.',
   ['One trial gives one result with nothing to compare it against.',
    'Anything odd about that cube would look like a real finding.',
    'Ten cubes let you see the pattern across all of them.',
    'Repeated trials are what make a result trustworthy.'],
   '**So that one unusual cube cannot be mistaken for a real result.** '
   'Repeated trials are how you tell a real effect from bad luck.',
   'There is no magic number of trials — more is better, and one is never enough.',
   frm='source')

sq(2, 'A student writes four notes while watching an ice cube melt. Which one is an INFERENCE?',
   ['The cube melted faster because the salt lowered the freezing point of the water',
    'A puddle of water has spread all the way around the base of the cube',
    'The cube measures 3 cm across at its widest point',
    'The water in the cup looks cloudy rather than clear'], 0,
   'Three of these you could write down just by looking. One of them explains why.',
   ['An observation is something you notice directly.',
    'A puddle, a width and cloudy water are all noticed directly.',
    'Nobody saw the freezing point change — that is a reason someone worked out.',
    'An explanation of why is an inference.'],
   '**The cube melted faster because the salt lowered the freezing point of the water.** '
   'The faster melting was observed; the reason behind it was reasoned out, which makes it an inference.',
   'The words "because", "so that" and "as a way to" almost always introduce an inference.',
   frm='source')

sq(3, 'The graph shown gives the mass of two ice cubes over 10 minutes, one in plain water and one in '
      'salt water. Based on the trend of the plain-water cube, what will its mass be at 12 minutes?',
   ['30 g', '36 g', '18 g', '24 g'], 3,
   'Work out how much that line drops in every 2-minute step, then take one more step.',
   ['Read the plain-water line: 60, 54, 48, 42, 36, 30 grams.',
    'It loses 6 g in every 2-minute step.',
    'Twelve minutes is one more step past ten minutes.',
    '30 − 6 = 24 g.'],
   '**24 g.** Predicting from a trend means continuing the pattern, not repeating the last value '
   'you can actually see on the graph.',
   'Reading past the end of your data like this is called extrapolation.',
   frm='added', graph=MELT)

sq(2, 'A student measures the mass of two groups of ice cubes every 2 minutes for 10 minutes. '
      'Which kind of graph should she use?',
   ['A pie chart', 'A double line graph', 'A single bar', 'A scientific diagram'], 1,
   'She has two things going on at once: two groups, and many points in time.',
   ['She measured repeatedly over time, which means change over time.',
    'A line graph is what shows change over time.',
    'She has two groups to compare, so she needs two lines.',
    'That is a double line graph. A pie chart would show parts of a whole instead.'],
   '**A double line graph.** Two lines on one pair of axes let you compare both groups over the '
   'same stretch of time.',
   'A bar graph compares amounts between categories; a line graph shows change over time.',
   frm='source')

sq(1, 'Which of these is QUANTITATIVE data about a melting ice cube?',
   ['The edges of the cube look smooth and rounded over',
    'It took 14 minutes to melt completely',
    'The water around the cube feels very cold',
    'The puddle underneath looks cloudy and grey'], 1,
   'Quantitative starts the same way as QUANTity.',
   ['Quantitative data has numbers in it.',
    'Rounded, cold and cloudy are all descriptions.',
    'Only one option carries a measurement.',
    '14 minutes is the quantitative observation.'],
   '**It took 14 minutes to melt completely.** It is a measured number. The other three describe '
   'what the cube or water was like, which makes them qualitative.',
   'The same thing can be recorded either way — what decides it is whether anyone measured.',
   frm='source')

sq(1, 'Which of these is QUALITATIVE data about a melting ice cube?',
   ['It lost 18 grams in 6 minutes', 'The puddle is 12 cm across',
    'The surface looks wet and glassy', 'It melted in 14 minutes'], 2,
   'This is the opposite of the last one. Which option has no number in it at all?',
   ['Qualitative data describes rather than counts.',
    '18 grams, 12 cm and 14 minutes are all measurements.',
    'Wet and glassy describe how it looks.',
    'So that is the qualitative observation.'],
   '**The surface looks wet and glassy.** It describes the cube without measuring anything.',
   'Descriptions are qualitative even when they sound precise — "glassy" is still not a number.',
   frm='source')

sq(2, 'A student\'s graph has a title, a legend, and both sets of points joined with lines. '
      'The numbers running up the side and along the bottom have nothing beside them saying what '
      'they measure. What is missing from her graph?',
   ['A title', 'Lines connecting the data', 'A legend', 'Axis labels and units'], 3,
   'Go through the list and cross off everything the question says she already has.',
   ['The question says the graph has a title, so that is not missing.',
    'It says the points are joined with lines, and that there is a legend.',
    'The only thing described as absent is what the numbers along each axis mean.',
    'That is the axis labels and their units.'],
   '**Axis labels and units.** Numbers alone do not say whether the side is grams, centimetres or '
   'minutes — the label and its unit are what make a graph readable.',
   'Check the parts of a graph one at a time. A graph can have a title and still be unreadable.',
   frm='source')

sq(2, 'Which of these describes the best scientific diagram of an ice cube experiment?',
   ['A neat drawing with labelled parts but no title',
    'A realistic drawing with a title at the top and every part labelled',
    'A colourful cartoon with a smiling ice cube and no labels',
    'A realistic drawing with no title and no labels'], 1,
   'A scientific diagram has to do three jobs at once. Check each option against all three.',
   ['A scientific diagram needs a realistic drawing, labelled parts, and a title.',
    'The cartoon fails on realistic and on labels.',
    'One option has labels but no title, and another has neither.',
    'Only one option does all three.'],
   '**A realistic drawing with a title at the top and every part labelled.** '
   'Miss any one of the three and it stops being a scientific diagram — a cartoon is art, and '
   'labels with no title leave the reader guessing what they are looking at.',
   'When a question asks for the BEST, look for the option that fails on nothing.',
   frm='source')

sq(3, 'The graph shown gives the mass of two ice cubes over 10 minutes, one in plain water and one '
      'in salt water. Which is the best evidence-based claim for the question "How does the amount '
      'of salt in water affect how fast an ice cube melts?"',
   ['I could really tell the salty one was going faster than the other one, so I think that salt '
    'must help ice melt more quickly than plain water does.',
    'Salt made the ice melt faster than it would have done in ordinary plain water.',
    'The cube sitting in the salt water dropped from 60 g all the way down to 2 g, while the cube '
    'in the plain water only came down as far as 30 g in the same ten minutes.',
    'Adding salt to the water made the ice melt faster. The cube in salt water lost about 58 g in '
    '10 minutes, while the cube in plain water lost only about 30 g in the same time.'], 3,
   'A claim has two jobs: answer the question, and back it with data. Check each option for both.',
   ['A claim must answer the question that was asked.',
    'It must also give evidence from the data.',
    'One option uses "I could tell" and "I think", which is personal rather than scientific.',
    'One answers with no evidence, and one lists evidence without ever saying what it means.',
    'The claim that states what the salt did AND quotes the two mass losses is the one that does both jobs.'],
   '**Adding salt to the water made the ice melt faster, backed by the 58 g and 30 g losses.** '
   'It states what the salt did AND cites the numbers that show it, and it keeps the writer out '
   'of the sentence.',
   'Write a claim about the experiment, never about yourself — "I saw" and "I think" do not belong.',
   frm='added', graph=MELT)

assert len(Q2) == 20, len(Q2)
_balance(Q2)

unitB = {
  'id': 'unit-sci-nos-test', 'type': 'unit', 'classId': 'science',
  'title': 'Science · Nature of Science Study Test', 'status': 'draft',
  'prep': True, 'order': 5, 'quarter': 1, 'round': 20, 'libv': 1,
  'srcName': 'Built to match the Nature of Science practice test (Drive)',
  'source': 'added',
  'summary': {'from': 'added', 'text':
    'A second test over the same 20 Nature of Science skills, built around a completely different '
    'experiment: how does the amount of salt in water affect how fast an ice cube melts. Nothing '
    'here is copied from the practice test, so getting these right means you know the skill rather '
    'than the paper.'},
  'why': {'from': 'added', 'text':
    'Doing the same test twice mostly tests whether you remember the answers. Doing a different '
    'test on the same skills tests whether you can actually do them — which is the thing the real '
    'unit test will find out.'},
  'objectives': [
    {'from': 'source', 'text': 'Pick out a testable scientific question.'},
    {'from': 'source', 'text': 'Name independent, dependent and controlled variables in a fresh experiment.'},
    {'from': 'source', 'text': 'Work out what one space on a scale is worth, then read it.'},
    {'from': 'source', 'text': 'Sort observations into inference or observation, quantitative or qualitative.'},
    {'from': 'source', 'text': 'Read a double line graph and predict from its trend.'},
    {'from': 'added', 'text': 'Write a claim that answers the question and cites the evidence.'}],
  'parentNote': {'from': 'added', 'text':
    'This is the parallel test — same 20 skills as the teacher\'s practice paper, entirely new '
    'scenario (salt water and melting ice), so she cannot answer from memory of the first one. '
    'It runs as an ordinary quiz with all 20 questions in one sitting, options shuffled, and '
    'anything she misses lands in the Growth Zone. Two questions carry a real graph the app draws '
    'itself, so the plotted data and the correct answer agree by construction — unlike the paper, '
    'nothing here depends on a picture she has to be holding. The three instrument-reading '
    'questions state the scale in words ("labelled every 10 mL, five spaces between") rather than '
    'showing a photo, which tests the same divide-the-gap reasoning without inventing a picture. '
    'Worth knowing: the practice paper\'s graduated cylinder had 1 mL spaces and this one has '
    '2 mL spaces on purpose — reading a scale without checking what one space is worth is the '
    'commonest way to lose these marks.'},
  'nextUp': {'from': 'added', 'minutes': 20, 'text':
    'Twenty questions in one sitting, the same shape as the real test. Take it after you have done '
    'the paper one, and see which skills still wobble.'},
  'cards': C2, 'questions': Q2,
  'updatedAt': int(time.time() * 1000) - 3 * 3600 * 1000,
}

for u, fn in ((unitA, 'science-nos-practice.json'), (unitB, 'science-nos-test.json')):
    path = os.path.join(REPO, 'content', fn)
    json.dump({'v': 1, 'records': {u['id']: u}},
              io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote %-30s %2d cards %2d questions  guide=%s prep=%s order=%s'
          % (fn, len(u['cards']), len(u['questions']), u.get('guide'), u.get('prep'), u['order']))
print('paper key preserved:', got)
