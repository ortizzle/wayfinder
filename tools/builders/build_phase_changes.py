# -*- coding: utf-8 -*-
# Chemistry · 2 Phase Changes — from the teacher's Science update of 9/10,
# which names the first chemistry quiz (17 Sep) as covering "the phases of
# matter AND the phase changes". v161 shipped the phases half; this is the
# other half, and without it the shelf would have been silent on a third of
# what the quiz asks.
#
# Second part of the Chemistry shelf v161 started. BOTH parts carry a lesson
# number, which is structural, not decoration: "Phase Changes" title-sorts
# AHEAD of "Phases of Matter" (a space beats 's'), which is backwards for the
# order she meets them. Numbering fixes it by construction — the v180 Biology
# lesson, applied on a two-part shelf before it can go wrong rather than
# after.
#
# No `prep` flag. The quiz is real and six days out, but v139's rule is that
# `prep:true` says what a unit IS, never when it matters — this is the
# lesson itself. The runway and the brief already own the urgency.
import sys, os, json, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

C, Q = [], []

# ---- cards -----------------------------------------------------------------
card(C, 'Phase change',
     '**A phase change is matter switching between solid, liquid and gas.**\n'
     '• The stuff itself does not change — ice, water and steam are all water.\n'
     '• What changes is how much energy the particles have, and therefore how '
     'they are arranged and how fast they move.')
card(C, 'Melting',
     '**Melting is solid → liquid, and it needs energy IN.**\n'
     '• Adding heat makes the particles vibrate harder until they break free of '
     'their fixed positions and start sliding past one another.\n'
     '• An ice cube on a warm counter is melting because heat is moving INTO it.')
card(C, 'Freezing',
     '**Freezing is liquid → solid, and it gives energy OUT.**\n'
     '• The particles slow down until they lock into place.\n'
     '• Freezing is melting run backwards, which is why they happen at the same '
     'temperature.')
card(C, 'Evaporation and boiling',
     '**Both are liquid → gas, and both need energy IN. The difference is where '
     'and when.**\n'
     '• Evaporation happens only at the SURFACE, and at any temperature — a puddle '
     'dries up on a cool day.\n'
     '• Boiling happens all the way THROUGH, and only once the liquid reaches its '
     'boiling point — that is what the bubbles from the bottom are.')
card(C, 'Condensation',
     '**Condensation is gas → liquid, and it gives energy OUT.**\n'
     '• The particles slow down enough to stick together into a liquid again.\n'
     '• The water on the outside of a cold glass did not leak through it — it is '
     'water vapour from the air turning back into liquid on the cold surface.')
card(C, 'Sublimation',
     '**Sublimation is solid → gas, skipping liquid entirely, and it needs '
     'energy IN.**\n'
     '• Dry ice is the famous one: it goes straight to a gas and leaves no puddle.\n'
     '• Snow can slowly sublime away on a cold sunny day without ever melting.')
card(C, 'Deposition',
     '**Deposition is gas → solid, skipping liquid, and it gives energy OUT.**\n'
     '• Frost on a window forms this way — water vapour in the air becomes ice '
     'directly, without being liquid water first.\n'
     '• It is sublimation run backwards.')
card(C, 'Energy in, or energy out — the one rule',
     '**Moving UP the ladder (solid → liquid → gas) always takes energy IN. Moving '
     'DOWN always gives energy OUT.**\n'
     '• In: melting, evaporation, boiling, sublimation.\n'
     '• Out: freezing, condensation, deposition.\n'
     '• Work out which direction the change goes and you already know the answer — '
     'there is nothing else to memorise.',
     hint='Up the ladder costs you. Down the ladder pays you back.',
     frm='added')
card(C, 'Melting point and freezing point are the same number',
     '**For water, 0°C (32°F) — the one temperature where ice melts and water '
     'freezes.**\n'
     '• They are two names for one boundary; which one happens depends on whether '
     'heat is going in or coming out.\n'
     '• Different substances have different values — iron melts near 1,538°C.')
card(C, 'Boiling point',
     '**For water, 100°C (212°F) — the temperature at which a liquid boils all '
     'the way through.**\n'
     '• Below it, water can still evaporate from its surface; it just cannot boil.\n'
     '• Like the melting point, it belongs to the substance, not to water alone.')
card(C, 'It is the same stuff throughout',
     '**A phase change rearranges particles. It never turns one substance into '
     'another.**\n'
     '• Melt an ice cube and you get exactly the same water, in a different '
     'phase.\n'
     '• Nothing is created and nothing is destroyed — a sealed jar of ice weighs '
     'the same once the ice has melted.')
card(C, 'Every phase change can run backwards',
     '**Add energy and it goes one way; take energy away and it goes back.**\n'
     '• Melt and freeze, evaporate and condense, sublime and deposit — three '
     'pairs, each the reverse of the other.\n'
     '• So a puddle that dried up can come back as rain later. The water did not '
     'go anywhere.')
card(C, 'Evaporation or condensation? The commonest mix-up',
     '**Evaporation makes a gas. Condensation makes a liquid.**\n'
     '• The two words get swapped more often than any other pair in this unit.\n'
     '• A hook: conDENSation makes something DENSer — gas is the least dense '
     'phase, liquid is denser, so the arrow points from gas to liquid.',
     hint='Condense → denser → towards liquid. Evaporate → vapour → towards gas.',
     frm='added')
card(C, 'Dew and frost are the same story at two temperatures',
     '**Dew is condensation; frost is deposition.**\n'
     '• On a cool night, water vapour in the air becomes liquid droplets on the '
     'grass — dew.\n'
     '• On a night below freezing, that vapour becomes ice crystals directly, '
     'with no liquid step — frost.\n'
     '• Both give energy out; only the destination differs.')
card(C, 'Heating does two different jobs',
     '**Sometimes heat makes something warmer; sometimes it changes its phase '
     'instead.**\n'
     '• Heating ice below 0°C makes it warmer ice.\n'
     '• Once it reaches 0°C, the heat goes into melting it rather than raising '
     'the temperature — which is why an iced drink stays cold until the last ice '
     'is gone.',
     frm='added')
card(C, 'Naming all six',
     '**Melting, freezing, evaporation (and boiling), condensation, sublimation, '
     'deposition.**\n'
     '• Four of them pass through liquid; two skip it.\n'
     '• The two that skip liquid — sublimation and deposition — are the pair most '
     'often left off a list, so name them first when you are checking your work.',
     frm='added')

# ---- sort set --------------------------------------------------------------
SORT = {
 'id': 's1', 'title': 'Does it take heat in, or give heat off?',
 'a': 'Takes heat in', 'b': 'Gives heat off',
 'items': [
  {'t': 'An ice cube turning into a puddle', 'k': 'a',
   'why': 'Melting — solid to liquid, up the ladder.'},
  {'t': 'Water in a tray turning to ice in the freezer', 'k': 'b',
   'why': 'Freezing — liquid to solid, down the ladder.'},
  {'t': 'A puddle slowly disappearing on a warm day', 'k': 'a',
   'why': 'Evaporation — liquid to gas, up the ladder.'},
  {'t': 'Droplets forming on the outside of a cold can', 'k': 'b',
   'why': 'Condensation — gas to liquid, down the ladder.'},
  {'t': 'Dry ice smoking away without leaving a puddle', 'k': 'a',
   'why': 'Sublimation — solid straight to gas, up the ladder.'},
  {'t': 'Frost forming on a window overnight', 'k': 'b',
   'why': 'Deposition — gas straight to solid, down the ladder.'},
  {'t': 'A pot of water bubbling on a hot stove', 'k': 'a',
   'why': 'Boiling — liquid to gas throughout, up the ladder.'},
  {'t': 'Fog on a bathroom mirror after a shower', 'k': 'b',
   'why': 'Condensation — the warm vapour becomes liquid on the cool glass.'},
  {'t': 'A chocolate bar going soft in a warm pocket', 'k': 'a',
   'why': 'Melting — solid to liquid.'},
  {'t': 'Dew appearing on the grass before sunrise', 'k': 'b',
   'why': 'Condensation — vapour in the air becomes liquid droplets.'},
  {'t': 'Wet clothes drying on a line', 'k': 'a',
   'why': 'Evaporation — the water leaves as a gas.'},
  {'t': 'Melted candle wax hardening again', 'k': 'b',
   'why': 'Freezing — liquid to solid. It does not have to be cold to count.'},
 ]}

# ---- questions -------------------------------------------------------------
q(Q, 1, 'What happens to a substance during a phase change?',
  ['Its particles rearrange, but it is still the same substance',
   'It turns into a completely different substance altogether',
   'Some of its particles are destroyed and the rest survive',
   'It gains extra new particles from the air all around it'],
  0,
  'Ice, water and steam — how many different substances is that?',
  ['A phase change moves matter between solid, liquid and gas.',
   'What changes is how much energy the particles have and how they are '
   'arranged.',
   'The particles themselves are exactly the same ones as before.',
   'So it rearranges without becoming anything new.'],
  '**Ice, liquid water and steam are all water — a phase change rearranges '
  'particles rather than replacing them.** Nothing is created or destroyed '
  'either, which is why a sealed jar weighs the same before and after the ice '
  'in it melts.',
  'Same stuff, new arrangement. That is the whole idea.')

q(Q, 1, 'A tray of water is left in the freezer overnight. What is this change '
        'called?',
  ['Freezing', 'Melting', 'Condensation', 'Sublimation'],
  0,
  'Name the phase it starts in and the phase it ends in.',
  ['The water starts as a liquid and ends as a solid.',
   'Liquid to solid is freezing.',
   'Melting is the reverse of that.',
   'So the answer is freezing.'],
  '**Liquid to solid is freezing.** Naming a change is always the same two '
  'steps: what phase did it start in, and what phase did it end in. '
  'Condensation ends as a liquid and sublimation ends as a gas, so neither '
  'fits.',
  'Start phase, end phase, then name it. Never guess from the setting.')

q(Q, 2, 'Which pair of changes both need energy to be ADDED?',
  ['Melting and evaporation', 'Freezing and condensation',
   'Freezing and deposition', 'Condensation and deposition'],
  0,
  'Which direction on the solid-liquid-gas ladder does each one travel?',
  ['Adding energy moves a substance UP the ladder: solid to liquid to gas.',
   'Melting is solid to liquid and evaporation is liquid to gas — both are '
   'upward.',
   'Freezing, condensation and deposition all move downward, so all three '
   'give energy off.',
   'So the pair that takes energy in is melting and evaporation.'],
  '**Up the ladder always takes energy in; down always gives energy out — and '
  'that single rule answers every question of this kind.** There is nothing '
  'to memorise per change: work out which direction it travels and the energy '
  'follows.',
  'Solid → liquid → gas costs energy. The way back returns it.')

q(Q, 2, 'Water droplets appear on the outside of a cold glass of lemonade. '
        'Where did they come from?',
  ['Water vapour in the air turned to liquid on the cold glass',
   'Lemonade seeped out through tiny holes in the glass',
   'The cold made new water out of the air’s nitrogen',
   'The glass melted slightly and the drips are glass'],
  0,
  'Air has water in it, even when it does not look wet.',
  ['The air around the glass carries invisible water vapour.',
   'The cold glass cools that vapour down, slowing its particles.',
   'Slowed enough, the vapour becomes liquid water on the surface — '
   'condensation.',
   'Nothing came through the glass, and nothing new was created.'],
  '**This is condensation: water vapour already in the air becomes liquid on '
  'the cold surface.** Glass has no holes for lemonade to escape through, and '
  'a phase change never makes water out of a different substance — the water '
  'was already there, just invisible.',
  'If a cold thing gets wet on the outside, think condensation first.')

q(Q, 2, 'Dry ice is put on a table and slowly disappears, leaving no puddle '
        'behind. What is happening?',
  ['It is going straight from solid to gas',
   'It is melting, and the puddle dries too fast to see',
   'It is condensing into the air',
   'It is freezing even harder'],
  0,
  'What is missing that would be there if it had melted?',
  ['A solid that melts leaves a liquid behind.',
   'There is no liquid here at all.',
   'So it must be going straight from solid to gas, skipping liquid — '
   'sublimation.',
   'That is exactly what dry ice is known for.'],
  '**Sublimation is solid straight to gas, with no liquid step — which is why '
  'there is no puddle.** The absence of the liquid is the whole clue. '
  'Condensation would produce a liquid, and freezing would make it more solid, '
  'not less.',
  'No puddle means no liquid stage. That rules melting out immediately.')

q(Q, 3, 'Frost forms on a car windscreen overnight. Which change is that, and '
        'does it take heat in or give heat off?',
  ['Deposition, and it gives heat off', 'Condensation, and it gives heat off',
   'Sublimation, and it takes heat in', 'Freezing, and it takes heat in'],
  0,
  'Frost is ice. What was it immediately before it was ice — a liquid, or a '
  'gas?',
  ['Frost forms from water vapour in the air, not from liquid water sitting '
   'on the glass.',
   'Gas straight to solid, skipping liquid, is deposition.',
   'That is a move DOWN the ladder, so it gives heat off.',
   'Freezing would be right if liquid water had been there first, but it was '
   'not.'],
  '**Frost is deposition: water vapour becomes ice directly, and going down '
  'the ladder always gives heat off.** The tempting answer is freezing — but '
  'freezing starts from a liquid, and dry glass on a cold night has vapour on '
  'it, not water. Dew is the version that stops at liquid.',
  'Dew stops at liquid. Frost goes all the way to solid in one step.')

q(Q, 2, 'A puddle dries up completely on a cool, breezy day — nowhere near '
        '100°C. How is that possible?',
  ['Evaporation happens at the surface, at any temperature',
   'The puddle must have reached its boiling point somehow',
   'The water soaked into the air as a liquid',
   'Cool air destroys water'],
  0,
  'What is the difference between evaporating and boiling?',
  ['Boiling happens all the way through a liquid, and only at its boiling '
   'point.',
   'Evaporation happens only at the surface, and at any temperature.',
   'A puddle has a large surface and plenty of time, so it can evaporate away '
   'entirely.',
   'So it evaporated, without ever boiling.'],
  '**Evaporation needs no particular temperature — it happens at the surface '
  'whenever particles there have enough energy to escape.** Boiling is the one '
  'that waits for a specific temperature and happens throughout. Water is '
  'never destroyed; it left as an invisible gas.',
  'Bubbles from the bottom mean boiling. A puddle just quietly shrinking is '
  'evaporation.')

q(Q, 1, 'Which change is the exact reverse of melting?',
  ['Freezing', 'Evaporation', 'Condensation', 'Deposition'],
  0,
  'Melting goes solid to liquid. Which change goes the other way along that '
  'same step?',
  ['Melting is solid to liquid.',
   'Its reverse must be liquid to solid.',
   'That is freezing.',
   'Condensation is gas to liquid, which is a different step of the ladder.'],
  '**Freezing is melting run backwards — same two phases, opposite direction, '
  'which is why they happen at the same temperature.** The six changes come in '
  'three reverse pairs: melt/freeze, evaporate/condense, sublime/deposit.',
  'Learn them in pairs and you have only three things to remember.')

q(Q, 2, 'Ice melts at 0°C. At what temperature does liquid water freeze?',
  ['0°C', '100°C', '32°C', 'It depends on how much water there is'],
  0,
  'Freezing and melting are the same boundary crossed in opposite directions.',
  ['Melting and freezing are reverses of each other.',
   'They happen at the same temperature — the boundary between solid and '
   'liquid.',
   'For water that boundary is 0°C.',
   'So water freezes at 0°C, the same temperature at which ice melts.'],
  '**The melting point and the freezing point are one temperature with two '
  'names — 0°C for water.** Which of the two actually happens depends on '
  'whether heat is going in or coming out. 32 is the same boundary in '
  'Fahrenheit, not in Celsius, and the amount of water makes no difference at '
  'all.',
  'One boundary, two names. The direction of the heat decides which.')

q(Q, 3, 'An iced drink sits in a warm room. The ice slowly melts, but the '
        'drink stays cold the whole time until the last ice is gone. Why?',
  ['The arriving heat goes into melting the ice, not warming the drink',
   'Ice keeps making more cold and pushes it into the drink around it',
   'The drink is already as cold as anything in the room can get',
   'Warm air can only reach a solid, so the liquid stays untouched'],
  0,
  'Heat can do two different jobs. Which one is it doing while ice is still '
  'present?',
  ['Heat arriving at something can either raise its temperature or drive a '
   'phase change.',
   'While ice is still melting, the arriving heat is spent on the melting '
   'itself.',
   'So the temperature stays put rather than climbing.',
   'Once the last ice has melted, the heat has nothing to melt and the drink '
   'starts warming up.'],
  '**Heat has two possible jobs, and while a phase change is underway it does '
  'that one instead of raising the temperature.** This is why ice keeps a '
  'drink cold so effectively, and why the drink warms up quickly the moment '
  'the ice is gone. Nothing "makes cold" — heat moves in, and the melting '
  'absorbs it.',
  'Cold is not a thing that travels. Heat is.')

q(Q, 2, 'A sealed jar holds an ice cube and nothing else. The ice melts '
        'completely. What happens to the jar’s total mass?',
  ['It stays exactly the same', 'It goes down, because ice is heavier',
   'It goes up, because liquid is denser', 'It goes down, because water escapes'],
  0,
  'The jar is sealed. Did anything get in or out?',
  ['A phase change rearranges particles; it does not create or destroy them.',
   'The jar is sealed, so nothing left and nothing entered.',
   'The same particles are inside, just arranged as a liquid instead of a '
   'solid.',
   'So the total mass is unchanged.'],
  '**Mass is conserved through every phase change — the same particles are '
  'still in the jar.** Liquid water IS denser than ice, which is why ice '
  'floats, but density is mass per space taken up: the water takes up slightly '
  'less room while weighing exactly the same.',
  'Density changing and mass changing are two different claims.')

q(Q, 3, 'Which statement about evaporation and condensation is correct?',
  ['Evaporation produces a gas; condensation produces a liquid',
   'Evaporation produces a liquid; condensation produces a gas',
   'Both produce a gas, at different speeds',
   'Both produce a liquid, at different temperatures'],
  0,
  'One hook: which word sounds like it is making something denser?',
  ['Evaporation turns a liquid into vapour — that is, into a gas.',
   'Condensation turns a gas back into a liquid.',
   'A gas is the least dense phase and a liquid is denser, so conDENSation '
   'points from gas towards liquid.',
   'So evaporation makes a gas and condensation makes a liquid.'],
  '**These two get swapped more than any other pair in the unit, so it is '
  'worth a hook: conDENSation moves towards the DENSer phase, the liquid.** '
  'They are exact reverses of each other, which also means one takes energy in '
  'and the other gives it off.',
  'Evaporate → vapour → gas. That half names itself.')

q(Q, 2, 'Which two changes skip the liquid phase completely?',
  ['Sublimation and deposition', 'Melting and freezing',
   'Evaporation and condensation', 'Boiling and melting'],
  0,
  'Four of the six changes pass through liquid. Which two do not?',
  ['Melting, freezing, evaporation and condensation all have liquid at one '
   'end.',
   'Sublimation goes solid straight to gas.',
   'Deposition goes gas straight to solid.',
   'So those two are the pair that skips liquid.'],
  '**Sublimation and deposition are the only two that jump between solid and '
  'gas directly.** They are also the two most often left off a list of the six, '
  'so naming them first is a good habit when checking your work — dry ice and '
  'frost are the everyday examples.',
  'Four go through liquid. Two do not. Learn the two.')

q(Q, 1, 'What is the boiling point of water?',
  ['100°C', '0°C', '212°C', '32°C'],
  0,
  'Two of these are the same temperature in different units — and only one is '
  'in Celsius.',
  ['Water boils at 100°C.',
   'That is the same temperature as 212°F, but the question asks in Celsius.',
   '0°C is where water freezes and melts, not where it boils.',
   'So the answer is 100°C.'],
  '**Water boils at 100°C, which is 212°F.** Check the unit before you pick: '
  '212 and 32 are the two Fahrenheit values in disguise, and 0°C is the '
  'melting-and-freezing boundary rather than the boiling one.',
  'Water: 0 and 100 in Celsius, 32 and 212 in Fahrenheit.')

q(Q, 3, 'A cook wants an ice cube to melt faster. Which of these would actually '
        'help, and why?',
  ['Put it somewhere warmer, so heat moves into it more quickly',
   'Put it somewhere colder, so it works harder',
   'Wrap it in a towel, so the cold cannot escape',
   'Leave it sealed in the freezer, where it has more time'],
  0,
  'Melting needs something moving INTO the ice. What is it, and how do you '
  'supply more?',
  ['Melting is a move up the ladder, so it needs heat going in.',
   'The faster heat arrives, the faster it melts.',
   'A warmer place delivers heat faster.',
   'Colder places, insulation and the freezer all slow the heat down, so all '
   'three would make it slower.'],
  '**Melting needs heat arriving, so anything that speeds the heat up speeds '
  'the melting up.** A towel is insulation — it slows heat moving in, which is '
  'exactly why a wrapped ice cube lasts longer. And nothing "keeps cold in": '
  'cold is the absence of heat, not a substance.',
  'Ask what has to move, then ask what makes it move faster.')

q(Q, 2, 'Steam from a kettle hits a cool window and beads of water appear. Name '
        'the change, and say which way the heat went.',
  ['Condensation, and heat left the water',
   'Condensation, and heat entered the water',
   'Evaporation, and heat left the water',
   'Deposition, and heat entered the water'],
  0,
  'Gas to liquid is which change, and which direction on the ladder is that?',
  ['The steam is a gas and the beads are a liquid.',
   'Gas to liquid is condensation.',
   'That is a move down the ladder.',
   'Down the ladder gives heat off, so heat left the water and went into the '
   'window.'],
  '**Condensation, and the heat went out of the water and into the cool '
  'window.** Both halves matter: naming the change is the first step, and the '
  'direction of travel then decides the energy without any extra memorising. '
  'Deposition would have made ice, not liquid beads.',
  'Name it, then read the direction off the ladder.')

q(Q, 3, 'Put these in the order they happen as a block of ice in a pan is '
        'heated steadily from well below freezing.',
  ['The ice warms up to 0°C', 'The ice melts into liquid water',
   'The water warms up to 100°C', 'The water boils into steam'],
  0,
  'Heat does two different jobs, and they take turns.',
  ['Heat first raises the temperature of the solid ice up to its melting '
   'point.',
   'At 0°C the heat goes into melting instead, turning the ice into liquid '
   'water.',
   'Once it is all liquid, the heat raises the temperature again, up to 100°C.',
   'At 100°C the heat goes into boiling, turning the water into steam.'],
  '**Warm, change, warm, change — heating alternates between raising the '
  'temperature and driving a phase change.** The two phase changes happen at '
  'fixed temperatures (0°C and 100°C for water) while the warming steps happen '
  'in between, which is the whole shape of a heating curve.',
  'A phase change is a pause in the temperature, not a jump in it.',
  kind='order')

q(Q, 2, 'Which of these is NOT one of the six phase changes?',
  ['Dissolving', 'Deposition', 'Sublimation', 'Condensation'],
  0,
  'A phase change moves between solid, liquid and gas. Which of these does '
  'something else?',
  ['The six are melting, freezing, evaporation, condensation, sublimation and '
   'deposition.',
   'Deposition, sublimation and condensation are all on that list.',
   'Dissolving is sugar disappearing into water — two substances mixing, not '
   'one substance changing phase.',
   'So dissolving is the odd one out.'],
  '**Dissolving mixes two substances together; a phase change moves one '
  'substance between solid, liquid and gas.** Dissolved sugar has not melted — '
  'it is still sugar, spread through the water, and it can be recovered by '
  'evaporating the water away.',
  'One substance changing, or two substances mixing? Different questions.')

# ---- assemble --------------------------------------------------------------
build('wayfinder', C, Q, 'unit-sci-phasechg',
      'Chemistry · 2 Phase Changes', 'science',
      'All six phase changes — melting, freezing, evaporation and boiling, '
      'condensation, sublimation and deposition — what each one starts and ends '
      'as, which way the energy travels, the temperatures where water changes, '
      'and why heating something sometimes changes its temperature and '
      'sometimes changes its phase instead.',
      'The first chemistry quiz covers phases of matter AND phase changes, so '
      'this is the other half of what is being asked. It is also the part with '
      'the most vocabulary in it, and almost all of that vocabulary collapses '
      'into one rule once you see it: up the ladder takes energy in, down the '
      'ladder gives energy out.',
      [('Name all six phase changes and say which phase each one starts and '
        'ends in.', 'source'),
       ('Say whether a given change takes energy in or gives energy off, using '
        'the direction it travels rather than memorising each one.', 'source'),
       ('Tell evaporation from boiling, and condensation from evaporation.',
        'source'),
       ('Give the melting/freezing point and the boiling point of water in '
        'both Celsius and Fahrenheit.', 'source'),
       ('Explain why an iced drink stays cold until the last ice melts.',
        'added'),
       ('Explain why mass does not change during a phase change.', 'added')],
      'Built from the teacher’s Science update of 9/10, which names the first '
      'chemistry quiz (September 17) as covering "the phases of matter and the '
      'phase changes" — the Phases of Matter lesson shipped a day earlier '
      'covers the first half, and this covers the second. Three things are '
      'worth knowing about how it is built. First, every energy question is '
      'taught through ONE rule rather than six facts: up the solid-liquid-gas '
      'ladder always takes energy in, down always gives it off, so naming the '
      'direction answers the energy question with nothing extra to memorise. '
      'Second, evaporation-versus-condensation is the pair students swap most '
      'often, so it gets its own card with a hook (conDENSation moves towards '
      'the DENSer phase) as well as a question. Third, two traps get deliberate '
      'airtime because they are reasoning errors rather than vocabulary gaps: '
      'frost is deposition and not freezing (freezing starts from a liquid, and '
      'there was never liquid water on that windscreen), and "keeping the cold '
      'in" is backwards — cold is the absence of heat, so insulation slows heat '
      'moving IN. The teacher also notes that for quizzes she should study her '
      'highlighted notes and past homework sheets; this app is the extra '
      'practice on top of those, not a replacement for them.',
      ('Get the six names cold first — what each one starts as and ends as. '
       'Then the energy half is free: up the ladder takes heat in, down gives '
       'it off.', 20),
      'content/science-phase-changes.json',
      'Science update of 9/10 (teacher email) + the class Chemistry unit',
      'Science update, 9/10 (ParentSquare/email)',
      offset_hours=3, round_=9)

p = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'content/science-phase-changes.json')
j = json.load(io.open(p, encoding='utf-8'))
u = j['records']['unit-sci-phasechg']
u['sorts'] = [SORT]
u['libv'] = 1
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + sort set "%s" (%d items), libv 1' % (SORT['title'], len(SORT['items'])))
