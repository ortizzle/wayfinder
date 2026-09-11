# -*- coding: utf-8 -*-
# Chemistry · Phases of Matter — from "Phases of Matter.pdf" (her completed
# 20-point Science 4 practice sheet, Drive, uploaded 2026-09-10). The sheet
# is the class's own practice for the new Chemistry unit the 9/3 newsletter
# announced; the pages are photographs of the paper, so they were rendered
# with pypdfium2 and read as images rather than trusted to Drive's OCR.
#
# Its own shelf ("Chemistry"), NOT the existing "Science" shelf: that shelf
# is an explicit order:0..5 sequence of Nature of Science (Unit 1) parts, and
# a chemistry lesson appended as order:6 would read as part seven of a unit
# it has nothing to do with. One shelf per unit of study — the same call
# River's maths shelf settled in v160.
#
# Every scenario is fresh. The sheet's own items (guilt, rain, happiness, the
# Goldilocks liquid, the three container diagrams) are used only to calibrate
# what the class asks; none is reused as a question.
import sys, os, json, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

C, Q = [], []

# ---- cards -----------------------------------------------------------------
card(C, 'Chemistry',
     '**Chemistry is the study of matter — what things are made of and how they '
     'behave.**\n'
     '• It is NOT the study of energy and how energy is created.\n'
     '• Energy still turns up constantly in chemistry, because energy is what '
     'makes particles move. It is just not what chemistry is *about*.')
card(C, 'Matter',
     '**Matter is anything that has mass and takes up space.**\n'
     '• Both parts have to be true. If you cannot weigh it and it does not sit '
     'anywhere, it is not matter.\n'
     '• Feelings, ideas, sounds and light are real — they are just not made of '
     'particles, so they are not matter.')
card(C, 'Mass',
     '**Mass is how much stuff an object is made of — how many tiny particles are '
     'packed into it.**\n'
     '• More particles means more mass.\n'
     '• Mass is not the same as size. A brick and a loaf of bread can be the same '
     'size and the brick still has far more mass.',
     hint='Mass = the amount of MATTER. Say "mass, matter" — same first letter, '
          'same idea.')
card(C, 'Volume',
     '**Volume is the amount of space something takes up.**\n'
     '• Measured in millilitres and litres for liquids, or cubic centimetres for '
     'solid blocks.\n'
     '• Two objects can have the same volume and very different masses.')
card(C, 'Temperature',
     '**Temperature measures how FAST the particles in something are moving — not '
     'how close together they are.**\n'
     '• Hotter means the particles are moving faster.\n'
     '• Colder means they are moving slower. They never stop completely.',
     hint='Fast = hot. Picture particles jiggling harder as the temperature climbs.')
card(C, 'Fast, not close — the easy mix-up',
     '**Heating something usually spreads its particles out, but spreading out is '
     'the RESULT. Speed is what temperature actually measures.**\n'
     '• Steam is hot and its particles are far apart; ice is cold and its '
     'particles are packed tight — so "hot means far apart" looks right.\n'
     '• But squeeze a gas into a tiny can and its particles get much closer '
     'together without getting any colder. Closeness changed; temperature did not.',
     frm='added')
card(C, 'Particles are always moving',
     '**In solids, liquids AND gases, the particles are always in motion.**\n'
     '• In a solid they cannot travel anywhere, but they still vibrate on the '
     'spot.\n'
     '• In a liquid they slide past each other.\n'
     '• In a gas they fly around freely.')
card(C, 'Solid',
     '**A solid keeps its own shape AND its own volume, whatever container you put '
     'it in.**\n'
     '• Its particles are locked together in place and can only vibrate.\n'
     '• Lowest energy of the three main phases.\n'
     '• Drop a marble into a jar, a bowl or a bucket and it is still the same '
     'marble, same shape, same size.')
card(C, 'Liquid',
     '**A liquid keeps its own volume but takes the shape of its container.**\n'
     '• Its particles stay close together but can slide past one another.\n'
     '• Middle energy of the three main phases.\n'
     '• Pour 200 mL of juice into a tall glass or a flat dish and it is still '
     '200 mL — just a different shape.')
card(C, 'Gas',
     '**A gas takes BOTH the shape and the volume of whatever container it is in.**\n'
     '• Its particles are far apart and zoom around freely, so they spread out '
     'until they hit the walls.\n'
     '• Highest energy of the three main phases.\n'
     '• This is the only phase whose volume changes when you change the '
     'container.')
card(C, 'The shape-and-volume table',
     '**Solid: own shape, own volume. Liquid: container’s shape, own volume. Gas: '
     'container’s shape, container’s volume.**\n'
     '• Read it down the "shape" column and you lose one each time.\n'
     '• The gas is the only one that gives up both.',
     frm='added')
card(C, 'Energy, lowest to highest',
     '**Solid, then liquid, then gas.**\n'
     '• Using water: ice, then liquid water, then steam.\n'
     '• Adding energy is what moves you rightwards along that list; taking energy '
     'away moves you back left.')
card(C, 'Moving a solid to a new container',
     '**Nothing happens. Neither the shape nor the volume changes.**\n'
     '• The particles are locked to each other, not to the container.\n'
     '• This is the one case where the honest answer is "no change at all", which '
     'is easy to skip past when the other options all sound like something '
     'happened.',
     frm='added')
card(C, 'Moving a liquid to a new container',
     '**The volume stays the same; the shape changes to match the new container.**\n'
     '• The particles rearrange but stay just as close together, so the amount of '
     'space they fill is unchanged.\n'
     '• It will look wider, taller or flatter — there is still exactly as much of '
     'it.',
     frm='added')
card(C, 'Moving a gas to a new container',
     '**The volume changes to match the new container — bigger container, bigger '
     'volume; smaller container, smaller volume.**\n'
     '• A gas always spreads until it hits the walls, so the container decides.\n'
     '• Watch the direction: "the volume stays the same" is the LIQUID answer, and '
     'it is the wrong one here.',
     frm='added')
card(C, 'Not matter — the usual suspects',
     '**Feelings, thoughts, sounds, light, heat and time are not matter.**\n'
     '• None of them has mass, and none of them takes up space.\n'
     '• The test for each one is the same two questions: could I weigh it? does it '
     'sit somewhere?',
     frm='added')

# ---- sort set (matter or not) ----------------------------------------------
SORT = {
 'id': 's1', 'title': 'Is it matter?', 'a': 'Matter', 'b': 'Not matter',
 'items': [
  {'t': 'A snowball packed in your hands', 'k': 'a',
   'why': 'It has mass and takes up space — a solid.'},
  {'t': 'The smell drifting out of a bakery', 'k': 'a',
   'why': 'A smell is made of real gas particles floating to your nose.'},
  {'t': 'Boredom during a long car ride', 'k': 'b',
   'why': 'A feeling. Nothing to weigh, no space taken up.'},
  {'t': 'The helium inside a balloon', 'k': 'a',
   'why': 'A gas, and gases are made of particles — that is why the balloon '
          'weighs a tiny bit more once it is filled.'},
  {'t': 'The beam from a torch', 'k': 'b',
   'why': 'Light is energy travelling, not particles of stuff.'},
  {'t': 'A puddle after the rain', 'k': 'a',
   'why': 'A liquid, so it has mass and fills space.'},
  {'t': 'Your favourite song playing', 'k': 'b',
   'why': 'Sound is energy shaking the air. The air is stuff; the sound is not.'},
  {'t': 'An idea for a science fair project', 'k': 'b',
   'why': 'A thought. You cannot put it on a balance.'},
  {'t': 'The steam rising off hot soup', 'k': 'a',
   'why': 'Steam is water in its gas phase — still made of particles.'},
  {'t': 'The heat coming off a radiator', 'k': 'b',
   'why': 'Heat is energy moving. The radiator is stuff; the heat is not.'},
  {'t': 'A handful of dry sand', 'k': 'a',
   'why': 'Millions of tiny solid grains, each with mass.'},
  {'t': 'How long you have waited', 'k': 'b',
   'why': 'Time. Real, measurable, and not made of anything.'},
 ]}

# ---- questions -------------------------------------------------------------
q(Q, 1, 'A new student asks what chemistry class is going to be about. Which '
        'answer is right?',
  ['What things are made of and how they behave',
   'How energy gets created out of nothing',
   'How living things grow and reproduce',
   'How forces make objects speed up'],
  0,
  'Chemistry shares its first three letters with nothing useful — but it does '
  'share its whole subject with one word: matter.',
  ['Chemistry is the study of matter.',
   'Matter is what things are made of, and how it behaves is the rest of the '
   'course.',
   'Energy is part of chemistry, but energy is not what the subject is about — and '
   'energy is never created out of nothing.',
   'So the right answer is what things are made of and how they behave.'],
  '**Chemistry is the study of matter.** Living things belong to biology and '
  'forces belong to physics. Energy comes up constantly in chemistry because it '
  'is what moves particles around, but "the study of energy and how it is '
  'created" is a description of no real subject — energy cannot be created.',
  'If an answer names a subject you already take under another name, it is not '
  'the one.')

q(Q, 1, 'Two identical measuring jugs are filled to the same line, one with '
        'water and one with cooking oil. What is the same about them?',
  ['Their volume', 'Their mass', 'Their temperature', 'Their number of particles'],
  0,
  'Filled to the same line means the same amount of what?',
  ['Volume is the amount of space something takes up.',
   'Both jugs are filled to the same line, so both liquids take up the same space.',
   'That means their volumes match.',
   'Mass would only match if the two liquids were equally heavy for their size, '
   'and oil is lighter than water.'],
  '**Volume is the amount of space something takes up, so filling to the same '
  'line makes the volumes equal.** Oil is lighter than water for the same '
  'space, so the oil jug has less mass and fewer particles even though it looks '
  'the same. Nothing here says anything about how warm either one is.',
  'Same line, same space, same volume — but never assume same mass.')

q(Q, 1, 'A kitchen scale says a bag of flour is 900 grams. What is that number '
        'telling you?',
  ['How much stuff the flour is made of',
   'How much space the bag takes up on the shelf',
   'How fast the flour’s particles are moving',
   'How tall the bag is'],
  0,
  'Grams are the unit for one particular property.',
  ['A scale measures mass.',
   'Mass is how much stuff something is made of — how many particles are in it.',
   'Space taken up would be volume, and speed of particles would be temperature.',
   'So 900 grams tells you how much stuff the flour is made of.'],
  '**Mass is the amount of matter in something — the number of particles it is '
  'made of — and that is what a scale reads.** A big fluffy bag and a small dense '
  'one can weigh exactly the same, which is the clearest sign that mass and size '
  'are two different things.',
  'Scale → mass. Measuring jug → volume. Thermometer → temperature.')

q(Q, 2, 'A thermometer in a mug of cocoa reads 70°C. Ten minutes later it '
        'reads 40°C. What has changed about the cocoa’s particles?',
  ['They are moving more slowly', 'There are fewer of them',
   'They have become heavier', 'They have stopped moving'],
  0,
  'Temperature is a measure of speed, and the number went down.',
  ['Temperature measures how fast particles are moving.',
   'The reading dropped from 70°C to 40°C, so the temperature fell.',
   'Falling temperature means the particles slowed down.',
   'They did not stop — particles are always in motion — and none of them left or '
   'gained mass.'],
  '**Temperature measures how fast particles move, so a cooling drink is one '
  'whose particles have slowed down.** Nothing was removed from the mug and '
  'nothing got heavier: the same particles are simply moving less energetically. '
  'And they never stop — in solids, liquids and gases alike the particles are '
  'always in motion.',
  'Cooling slows particles down. It does not switch them off.')

q(Q, 2, 'Air is squeezed from a big pump into a small bicycle tyre. Nobody '
        'heats or cools it. What happens to the air’s particles?',
  ['They get closer together but keep the same speed',
   'They get closer together and slow right down',
   'They speed up because the space is smaller',
   'They stop moving until the tyre is opened again'],
  0,
  'Which property did the squeezing actually change — closeness, or speed?',
  ['Squeezing the air into a smaller space pushes its particles closer together.',
   'Temperature is a measure of particle SPEED, and nothing here heated or '
   'cooled the air.',
   'So the speed is unchanged even though the closeness changed a lot.',
   'That leaves: closer together, same speed.'],
  '**Closeness and temperature are two different things, and this is the '
  'clearest proof.** Packing particles tighter does not by itself make them move '
  'faster or slower, so the air is no hotter or colder for being squeezed. '
  'Temperature is only ever about how fast the particles are going.',
  'If you are tempted to answer "closer, so colder", this question is the '
  'reason not to.')

q(Q, 1, 'Which of these is NOT matter?',
  ['The sound of a doorbell', 'The air inside a beach ball',
   'A drop of glue', 'A grain of salt'],
  0,
  'Run both tests on each one: could you weigh it, and does it sit somewhere?',
  ['Matter is anything with mass that takes up space.',
   'Air is a gas made of particles, glue is a liquid and salt is a solid — all '
   'three have mass and fill space.',
   'Sound is energy travelling through the air. It has no mass of its own.',
   'So the sound of a doorbell is the one that is not matter.'],
  '**Sound is energy moving through matter, not matter itself.** The air it '
  'travels through is absolutely matter — a gas is made of particles, and a '
  'filled beach ball really does weigh slightly more than an empty one. But the '
  'shaking that your ear hears has nothing to weigh.',
  'Sound, light, heat and feelings all fail the same two tests.')

q(Q, 1, 'Which of these IS matter?',
  ['The fog over a field on a cold morning', 'A happy memory',
   'The warmth of the sun on your face', 'A sudden good idea'],
  0,
  'Three of these are things that happen inside you or arrive as energy.',
  ['Matter has mass and takes up space.',
   'A memory and an idea happen in your mind — nothing to weigh.',
   'Warmth is heat energy arriving, not stuff arriving.',
   'Fog is millions of tiny water droplets hanging in the air, so it is matter.'],
  '**Fog is made of real water droplets, which is why you can walk into it and '
  'come out damp.** Memories and ideas have no mass at all, and warmth is energy '
  'being transferred rather than a substance landing on you.',
  'If you could collect it in a jar, it is matter.')

q(Q, 1, 'A substance has particles that are locked in place and can only '
        'vibrate where they are. Which phase is it?',
  ['Solid', 'Liquid', 'Gas', 'None — those particles would not be moving'],
  0,
  'Locked in place is not the same as still.',
  ['Particles in every phase are always moving.',
   'In a liquid they slide past each other and in a gas they fly around freely.',
   'Only in a solid are they held in position, vibrating on the spot without '
   'travelling.',
   'So the answer is solid.'],
  '**A solid’s particles vibrate without going anywhere, which is exactly what '
  '"locked in place but still moving" describes.** The trap here is the answer '
  'claiming particles like that would not be moving at all: '
  'it sounds careful, but particles never stop moving in any phase — being held '
  'in place and being motionless are two different things.',
  'Solid particles jiggle. They just do not travel.')

q(Q, 2, 'Exactly 250 mL of lemonade is poured from a tall thin bottle into a '
        'wide shallow bowl. What is true afterwards?',
  ['It still takes up 250 mL, in a new shape',
   'It takes up more space now that it is spread out',
   'It takes up less space because the bowl is shorter',
   'Both its shape and the space it fills are unchanged'],
  0,
  'Which does a liquid keep — its shape, or the space it fills?',
  ['A liquid keeps its own volume but takes the shape of its container.',
   'Pouring it does not add or remove any lemonade, so the volume is still '
   '250 mL.',
   'The bowl is a different shape, so the lemonade is a different shape.',
   'That is: same volume, new shape.'],
  '**A liquid keeps its volume and gives up its shape.** Looking wider and '
  'flatter is a change of shape, not a change of amount — pour it back and you '
  'get your 250 mL returned. Keeping BOTH its shape and the space it fills '
  'would make it a solid, not a liquid.',
  'Spreading out is not the same as growing.')

q(Q, 2, 'A wooden building block is moved from a small box into a much larger '
        'crate. What happens to it?',
  ['Nothing — its shape and its volume both stay the same',
   'Its volume stays the same but its shape changes',
   'Its volume gets bigger to fill the crate',
   'Its shape stays the same but its volume gets bigger'],
  0,
  'Which parts of a solid belong to the solid, and which belong to the '
  'container?',
  ['A solid has its own shape and its own volume.',
   'Neither one is borrowed from whatever it is sitting in.',
   'Moving the block to a bigger crate changes nothing about the block itself.',
   'So the answer is that nothing happens.'],
  '**A solid is the one phase that keeps both its shape and its volume, so '
  'moving it changes nothing at all.** The tempting wrong answer is "volume the '
  'same, shape changes" — true of a liquid, never of a solid. A block does not '
  'flow into the corners of a crate.',
  'When the honest answer is "nothing happens", that really is one of the '
  'choices.')

q(Q, 3, 'A sealed syringe holds a gas. Its plunger is pushed halfway in, with '
        'nothing escaping and no heating or cooling. What happens to the gas?',
  ['Its volume halves and it still fills the space completely',
   'Its volume stays the same and it just changes shape',
   'Its volume stays the same and half of it turns into a liquid',
   'Its volume halves and the rest of the syringe is left empty'],
  0,
  'A gas always spreads out until it reaches the walls. Where are the walls now?',
  ['A gas takes both the shape and the volume of its container.',
   'Pushing the plunger halfway in makes the container half the size it was.',
   'The gas spreads out to the new walls, so its volume is now half what it was.',
   'None of it escaped and none of it needed to become a liquid — the same '
   'particles are simply packed into half the room.'],
  '**A gas is the only phase whose volume is set by its container, so shrinking '
  'the container shrinks the gas.** "Volume stays the same, shape changes" is the '
  'liquid answer and is the commonest wrong pick here. There is also no empty '
  'space left over: a gas always fills whatever it is in, right to the walls.',
  'Container decides the gas. Gas never decides the container.')

q(Q, 3, 'A gas is released from a small canister into a much larger sealed '
        'tank. Which pair of statements is right?',
  ['Its volume gets bigger; the number of particles is unchanged',
   'Its volume gets bigger; the number of particles goes up too',
   'Its volume is unchanged; the particles just spread out',
   'Its volume gets smaller; the particles spread out'],
  0,
  'Two separate questions: how much space, and how much stuff?',
  ['A gas spreads until it hits the walls, so in a bigger tank it fills a bigger '
   'volume.',
   'Nothing was added — the same gas simply moved.',
   'So the particle count is exactly what it was.',
   'Bigger volume, same number of particles.'],
  '**The gas spreads to fill the tank, so its volume grows — but spreading out '
  'never makes more particles.** The same handful of particles is now covering '
  'far more ground, so they are much further apart. Volume changed; the amount '
  'of stuff did not.',
  'More room does not mean more matter.')

q(Q, 2, 'Which list puts these in order from LOWEST energy to HIGHEST energy?',
  ['A steel nail, milk in a glass, the air in the room',
   'The air in the room, milk in a glass, a steel nail',
   'Milk in a glass, a steel nail, the air in the room',
   'A steel nail, the air in the room, milk in a glass'],
  0,
  'Name the phase of each one first, then use solid → liquid → gas.',
  ['Energy goes up in the order solid, liquid, gas.',
   'A steel nail is a solid, milk is a liquid and the air is a gas.',
   'So the order is nail, milk, air.',
   'Any list that starts with the air is starting at the highest, not the '
   'lowest.'],
  '**Solid, then liquid, then gas — that is the energy ladder, and the phase is '
  'what decides a thing’s place on it.** The whole question is really "which of '
  'these is a solid, which a liquid, which a gas", with the ordering falling out '
  'once you have named them.',
  'Read the direction words in the question before you pick. Lowest first here.')

q(Q, 3, 'Put these four in order of particle energy, from lowest to highest.',
  ['An ice cube from the freezer', 'A glass of cold milk',
   'A mug of hot tea', 'Steam above a boiling kettle'],
  0,
  'Two things decide it: the phase first, then how hot it is within that phase.',
  ['Solids sit lowest on the energy ladder, so the ice cube is first.',
   'Liquids come next, and the cold milk is the cooler of the two liquids.',
   'The hot tea is a liquid too, but hotter, so its particles move faster than '
   'the milk’s.',
   'A gas is highest of all, so the steam goes last.'],
  '**Ice, cold milk, hot tea, steam.** The phase does most of the sorting — solid '
  'below liquid below gas — and temperature separates the two liquids, because '
  'the hotter one has the faster-moving particles. Both ideas are needed here; '
  'neither one alone gets the whole list right.',
  'Sort by phase first, then break any ties on temperature.',
  kind='order')

q(Q, 2, 'A helium balloon is weighed before and after it is filled. Which '
        'statement is true?',
  ['The filled balloon has more mass, because a gas is matter',
   'The mass is identical, because a gas is not matter',
   'The filled balloon has less mass, because gases are weightless',
   'The mass cannot be compared, because gases have no volume'],
  0,
  'Is a gas made of particles?',
  ['Matter is anything with mass that takes up space.',
   'A gas is made of particles that are far apart but perfectly real.',
   'So the helium inside has mass, and adding it adds mass.',
   'The filled balloon is the heavier of the two.'],
  '**A gas is matter, so filling a balloon really does add mass to it.** The '
  'amount is small enough to be hard to notice on a kitchen scale, which is '
  'exactly why "gases weigh nothing" feels true — but particles are particles, '
  'and gases have volume too: a gas fills whatever it is in.',
  'Hard to weigh is not the same as weightless.')

q(Q, 1, 'A substance has particles that stay close together but can slide past '
        'one another. Which phase is it?',
  ['Liquid', 'Solid', 'Gas', 'It could be any of the three'],
  0,
  'Close together rules out one phase; sliding rules out another.',
  ['In a solid, particles are stuck in place and can only vibrate.',
   'In a gas, particles are far apart rather than close together.',
   'Staying close AND sliding past each other is the middle case.',
   'So it is a liquid.'],
  '**A liquid holds the middle ground: its particles keep touching, like a '
  'solid’s, but they can move past each other, like a gas’s.** That is exactly '
  'why a liquid keeps its own volume — the particles stay just as close — while '
  'still flowing into whatever shape it is poured into.',
  'Close plus sliding = liquid. Close plus stuck = solid. Far apart = gas.')

q(Q, 3, 'Rock salt is ground into a fine powder and poured into a jar, where '
        'it settles into the jar’s shape. Does that make it a liquid?',
  ['No — each grain is still a solid with its own shape',
   'Yes — it took the shape of its container, which is what liquids do',
   'Yes — anything that pours is a liquid',
   'No — because salt dissolves in water'],
  0,
  'Look at one single grain under a magnifier, not at the heap.',
  ['A liquid takes its container’s shape because its own particles slide past '
   'each other.',
   'In powdered salt, the particles inside each grain are still locked in place — '
   'each grain keeps its own shape and volume.',
   'What is sliding is whole grains tumbling over each other, not particles '
   'within one grain.',
   'So the powder is a heap of tiny solids, not a liquid.'],
  '**A powder pours because the grains slide over each other, but every grain is '
  'still a solid.** Judge the phase by what a single piece does, never by what a '
  'pile of pieces does. Whether salt dissolves in water is a true fact and '
  'completely beside the point here.',
  'Sand, sugar and flour all pour. None of them is a liquid.')

q(Q, 2, 'A puddle of water is left out and slowly disappears over a hot '
        'afternoon. What happened to the water?',
  ['Its particles gained energy and spread out into the air as a gas',
   'The heat destroyed its particles and they stopped existing',
   'It froze into a solid and soaked down into the ground below',
   'Its particles lost energy until they had none left to move'],
  0,
  'Heat adds energy. Which way does that move something along the energy '
  'ladder?',
  ['Adding energy moves a substance up the ladder: solid to liquid to gas.',
   'A hot afternoon adds energy to the puddle.',
   'So the liquid water becomes a gas and mixes into the air.',
   'Matter is not destroyed — the water is still there, just spread out where you '
   'cannot see it.'],
  '**Heat gave the water’s particles enough energy to break away and become a '
  'gas, which then spread through the air.** The water was not destroyed and it '
  'did not lose energy — it gained some. Every particle that was in the puddle '
  'is still somewhere.',
  'Disappearing from sight is not disappearing from existence.')

# ---- assemble --------------------------------------------------------------
build('wayfinder', C, Q, 'unit-sci-phases',
      'Chemistry · Phases of Matter', 'science',
      'The start of the Chemistry unit: what chemistry actually studies, the '
      'three measurements it leans on most (mass, volume and temperature), how '
      'to tell matter from things that are real but are not matter, and the '
      'three main phases — solid, liquid and gas — including what each one keeps '
      'and what each one gives up when you move it to a new container.',
      'Almost everything later in chemistry is built on these words. Mixing up '
      'mass with volume, or temperature with how crowded particles are, makes '
      'later work quietly harder — and the shape-and-volume table for the three '
      'phases is the single most-asked fact in this unit.',
      [('Say what chemistry studies, and what mass, volume and temperature each '
        'measure.', 'source'),
       ('Decide whether something is matter by asking whether it has mass and '
        'takes up space.', 'source'),
       ('Describe how the particles move in a solid, a liquid and a gas.',
        'source'),
       ('Say which phases keep their own shape and which keep their own volume, '
        'and predict what happens when each is moved to a new container.',
        'source'),
       ('Put the three phases in order of energy, lowest to highest.', 'source'),
       ('Explain why temperature is about how FAST particles move, not how '
        'close together they are.', 'added')],
      'Built from her completed Phases of Matter practice sheet. Sixteen of her '
      'twenty answers were right, and the four she missed are worth a word '
      'because three of them are the same idea. (1) For "when we measure '
      'temperature, what are we really measuring?" she chose "how close '
      'particles are to one another"; the answer is "how fast particles are '
      'moving". That one is a genuinely common mix-up, since heating something '
      'usually does spread it out — the unit tackles it with its own card and '
      'two questions, including a squeezed-air one where closeness changes and '
      'temperature does not. (2) and (3) are both about solids: she named the '
      'phase with "a defined volume and a defined shape" as a gas, and for a '
      'diagram of a solid being moved to a bigger container she chose "the '
      'volume stays the same but the shape changes" rather than "nothing will '
      'happen". A solid keeps BOTH. (4) For a gas moved into a smaller '
      'container she chose the same "volume stays the same, shape changes" — '
      'that phrase is the liquid answer, and a gas always resizes to its '
      'container. So: the liquid rule is solid in her head and is currently '
      'being applied to all three phases. The shape-and-volume table card is '
      'the fix, and the three "moving it to a new container" cards say each '
      'case outright. Nothing here was marked by a teacher — these are her own '
      'answers on a practice sheet, so the unit teaches the correct chemistry '
      'rather than treating any of her four as an alternative convention.',
      ('Start with the flashcards and get the shape-and-volume table cold — '
       'which phase keeps its shape, which keeps its volume. Everything else '
       'in the quiz leans on it.', 20),
      'content/science-phases-matter.json',
      'Phases of Matter Practice (Science 4 practice sheet)',
      'Phases of Matter.pdf (Drive, Science)',
      offset_hours=3, round_=9)

# sorts + libv are not part of build()'s schema; patch them in.
p = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'content/science-phases-matter.json')
j = json.load(io.open(p, encoding='utf-8'))
u = j['records']['unit-sci-phases']
u['sorts'] = [SORT]
u['libv'] = 1
io.open(p, 'w', encoding='utf-8').write(
    json.dumps(j, ensure_ascii=False, indent=1))
print('  + sort set "%s" (%d items), libv 1' % (SORT['title'], len(SORT['items'])))
