# -*- coding: utf-8 -*-
"""River's Chemistry unit test material — two units, the v122 pattern.

A) unit-sci-chem-practice — the teacher's own "Practice for Chemistry Unit Test
   (21 Points)" transcribed VERBATIM as a guide unit, so she can do it on paper
   and enter her 21 letters. Option order is fixed (the whole mode is a lie
   otherwise). Every answer was re-derived independently and matched the
   teacher's circled key. The two picture questions (15, 16) carry what the
   picture shows in the stem, so a miss that comes back in the Growth Zone can
   still be answered without the paper.

B) unit-sci-chem-test — a parallel study test over the same skills plus the two
   the shelf had not taught (mixtures and solutions, the periodic table), on
   fresh scenarios from a kitchen rather than the atmosphere and plants.
"""
import json, io, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def V(text, opts, ans, main, steps):
    """A rescue-round variant: same skill, fresh example, hand-verified."""
    return {'q': text, 'opts': [str(o) for o in opts], 'ans': ans,
            'steps': steps, 'ex': {'main': main}}

# Arithmetic the paper and the study test lean on, checked here, not by hand.
assert 14 - 6 == 8                 # Q15: filled minus empty
assert 3 * 1 * 2 == 6              # Q16: L x W x H
assert 1.25 > 1                    # Q17: denser than water sinks
assert 37 - 12 == 25               # study test: sugar by subtraction
assert 4 * 2 * 3 == 24             # study test: block volume
assert 48 / 24 == 2                # study test: density of that block
assert 0.24 < 1 and 2.6 > 1        # study test: cork floats, pebble sinks
assert 9 - 4 == 5 and 5 * 2 * 1 == 10   # variants for 15 and 16

# ============================================================ A — the replica
C, Q = [], []

card(C, 'Matter',
     '**Matter is anything that has mass and takes up space.**'
     '\n• Dirt (a solid) and carbon dioxide (a gas) are both matter.'
     '\n• Sunlight is not: light is energy, and energy is not matter.',
     'Your teacher wrote it in the margin: matter is not energy or feelings.')
card(C, 'Air is a gas',
     '**Air is a mixture of gases — mostly nitrogen and oxygen, with a little carbon dioxide and water vapor.**'
     '\n• All of it is in the gas phase.',
     'Your teacher\'s note: know your water examples. Water vapor in the air is water as a gas.')
card(C, 'Temperature and particle speed',
     '**Colder means the particles slow down. Warmer means they speed up.**'
     '\n• High in the atmosphere it is colder, so air particles move more slowly.'
     '\n• A raindrop falling into warmer air has molecules that speed up.',
     'Your teacher\'s margin note: colder, particles slow down; warmer, speeds up.')
card(C, 'Water\'s phase changes',
     '**Condensation is gas to liquid. Freezing is liquid to solid. Melting is solid to liquid. Evaporation is liquid to gas.**'
     '\n• Clouds form by condensation: water vapor turns into tiny liquid droplets.'
     '\n• Hail forms by freezing: raindrops pushed up into air below 0°C turn solid.',
     'Your teacher wrote "know freezing too" beside the condensation question.')
card(C, 'Water\'s density, phase by phase',
     '**Liquid water is the densest, ice is in the middle, and water vapor is the least dense.**'
     '\n• Gas to liquid (a cloud forming): density goes UP.'
     '\n• Liquid to solid (rain turning to hail): density goes DOWN, which is why ice floats.',
     'Your teacher\'s ranking on the key: water vapor lowest, ice medium, liquid water high.')
card(C, 'Mixture',
     '**A mixture is substances put together that you can still pick apart.**'
     '\n• Compost — kitchen scraps, dead leaves, grass clippings — is a mixture.',
     'Your teacher\'s note: you can pick out pieces.')
card(C, 'Solution',
     '**A solution is a mixture where one substance dissolves completely and does not settle to the bottom.**'
     '\n• Potassium oxide stirred into water until it disappears is a solution.')
card(C, 'Solvent and solute',
     '**The solvent does the dissolving. The solute is what you add, and it dissolves.**'
     '\n• In lemonade, water is the solvent and the lemonade powder is the solute.',
     'Your teacher\'s note: solvent — the thing that does the dissolving; solute — you add it, it dissolves.')
card(C, 'Finding mass on a balance',
     '**Weigh the empty container, weigh it again with the object in, and subtract.**'
     '\n• Filled minus empty = the mass of the object.'
     '\n• 14 g − 6 g = 8 g for the grape.', 'Your teacher\'s note: filled minus empty.')
card(C, 'Volume of a rectangular prism',
     '**V = length × width × height, measured in cubic centimetres (cm³).**'
     '\n• 3 cm × 1 cm × 2 cm = 6 cm³.'
     '\n• cm measures a length; cm³ measures a volume, so the unit matters.', eq='V = L × W × H')
card(C, 'Float or sink',
     '**Water\'s density is 1 g/cm³. More than 1 sinks; less than 1 floats.**'
     '\n• A grape at 1.25 g/cm³ sinks because it is denser than water.',
     'Your teacher\'s note: more than 1, sink; less than 1, float.')
card(C, 'Element',
     '**An element is one kind of atom — if you can find it in a box on the periodic table, it is an element.**'
     '\n• He (helium) is an element. CO₂ and C₆H₁₂O₆ are not.',
     'Your teacher\'s note: think, can you find it on the periodic table?')
card(C, 'Molecule',
     '**A molecule is two or more atoms joined together, of the same kind or different kinds.**'
     '\n• H₂O is a molecule. Nb, B and C are each a single element symbol.',
     'Your teacher\'s note: has 2 or more of same or different atoms.')
card(C, 'The periodic table',
     '**Each box on the periodic table is one element, and most of the elements are metals.**')

def gq(lv, text, opts, ans, hint, steps, main, tip, variant, frm='source'):
    q(Q, lv, text, opts, ans, hint, steps, main, tip, frm=frm)
    Q[-1]['variant'] = variant

MNM = ['Matter', 'Not Matter']

gq(1, 'Identify whether the substance is Matter or Not Matter: Dirt', MNM, 0,
   'Does it have mass, and does it take up space?',
   ['Matter has mass and takes up space.', 'Dirt is a solid you can hold and weigh.',
    'So dirt is matter.'],
   '**Matter.** Dirt is a solid: it has mass and takes up space.',
   'Solids, liquids and gases are all matter.',
   V('Which of these is NOT matter?', ['A rock from the garden', 'A glass of orange juice', 'The sound of a bell', 'Steam from a kettle'], 2,
     '**The sound of a bell.** Sound is energy. The rock, the juice and the steam all have mass and take up space.',
     ['Matter has mass and takes up space.', 'A rock is a solid, juice is a liquid, steam is a gas.',
      'Sound is energy moving through the air, not a thing itself.', 'So the sound is not matter.']))

gq(1, 'Identify whether the substance is Matter or Not Matter: Sunlight', MNM, 1,
   'Is light a thing with mass, or is it energy?',
   ['Matter has mass and takes up space.', 'Sunlight is light, and light is energy.',
    'Energy is not matter.', 'So sunlight is not matter.'],
   '**Not Matter.** Sunlight is energy. It has no mass and takes up no space.',
   'Matter is not energy or feelings — the teacher\'s own margin note.',
   V('Which of these is NOT matter?', ['Sand', 'Heat from a fire', 'Milk', 'Air in a balloon'], 1,
     '**Heat from a fire.** Heat is energy. Sand, milk and air all have mass and take up space.',
     ['Check each one for mass and space.', 'Sand, milk and air are a solid, a liquid and a gas.',
      'Heat is energy, like light and sound.', 'So the heat is not matter.']))

gq(1, 'Identify whether the substance is Matter or Not Matter: Carbon Dioxide (CO₂)', MNM, 0,
   'It is a gas. Do gases count?',
   ['Carbon dioxide is a gas.', 'Gases have mass and take up space, even when you cannot see them.',
    'So carbon dioxide is matter.'],
   '**Matter.** Carbon dioxide is a gas, and gases are matter.',
   'Invisible does not mean not matter: air is all gases, and it is all matter.',
   V('Which of these IS matter?', ['A shadow', 'Happiness', 'Oxygen gas', 'Moonlight'], 2,
     '**Oxygen gas.** A gas has mass and takes up space. A shadow, a feeling and light do not.',
     ['Matter has mass and takes up space.', 'A shadow is just an area where light is blocked.',
      'Happiness is a feeling, and moonlight is light.', 'Oxygen is a gas, so it is matter.']))

gq(1, 'Our atmosphere on earth is filled with air, which is mostly oxygen (O₂) and nitrogen (N₂), a '
      'little carbon dioxide (CO₂), and a few other very small amounts of other substances. Air also '
      'contains water vapor (H₂O). What PHASE OF MATTER is air?',
   ['Solid', 'Liquid', 'Gas', 'None of the above'], 2,
   'Every substance listed is a gas, water vapor included.',
   ['Oxygen, nitrogen and carbon dioxide are gases.', 'Water vapor is water in the gas phase.',
    'So air is a gas.'],
   '**Gas.** Everything air is made of is in the gas phase.',
   'Water vapor is the gas version of water.',
   V('Steam rising from a pot of boiling water is water in which phase?',
     ['Solid', 'Liquid', 'Gas', 'Plasma'], 2,
     '**Gas.** Steam is water vapor, which is water as a gas.',
     ['Boiling turns liquid water into a gas.', 'That gas is called water vapor, or steam.',
      'So steam is water in the gas phase.']))

gq(2, 'As we go higher up in the atmosphere, away from the surface of the earth, the temperature gets '
      'colder. How does this affect the motion or speed of the particles that make up air?',
   ['they would slow down', 'they would speed up', 'they would stay the same', 'it is impossible to tell'], 0,
   'Colder means less energy. What does less energy do to moving particles?',
   ['Temperature is how fast the particles are moving.', 'Colder air has less energy.',
    'Less energy means the particles move more slowly.'],
   '**They would slow down.** Colder means the particles have less energy, so they move more slowly.',
   'Colder slows them down; warmer speeds them up.',
   V('A pot of soup is taken off the stove and left to cool. What happens to the particles in the soup as it cools?',
     ['They speed up', 'They slow down', 'They stop completely', 'They stay the same speed'], 1,
     '**They slow down.** As the soup cools, its particles lose energy and move more slowly. They never stop completely.',
     ['Cooling means the temperature goes down.', 'A lower temperature means less energy.',
      'Less energy means slower particles.', 'They slow down; they do not stop.']))

gq(2, 'Clouds form because of the phase change when water vapor (gas phase water) changes to a liquid. '
      'What PHYSICAL PROCESS is responsible for cloud formation?',
   ['melting', 'condensation', 'evaporation', 'deposition'], 1,
   'Which process goes from gas to liquid?',
   ['Melting is solid to liquid.', 'Evaporation is liquid to gas.', 'Deposition is gas straight to solid.',
    'Condensation is gas to liquid, which is what makes a cloud.'],
   '**Condensation.** Water vapor (a gas) turns into tiny liquid droplets, and those droplets are the cloud.',
   'conDENSation turns a gas into the denser liquid.',
   V('Water droplets appear on the outside of a cold glass of lemonade on a hot day. Which process made them?',
     ['Evaporation', 'Melting', 'Condensation', 'Freezing'], 2,
     '**Condensation.** Water vapor in the air touched the cold glass and turned into liquid droplets.',
     ['The droplets came from the air, not from inside the glass.', 'The air held water as a gas.',
      'The cold glass turned that gas into a liquid.', 'Gas to liquid is condensation.']))

gq(2, 'After water vapor (gas phase water) changes to liquid water forming a cloud, how would the DENSITY of the water change?',
   ['Density would increase', 'Density would decrease', 'Density would stay the same', 'none of the above'], 0,
   'Which is denser: water as a gas, or water as a liquid?',
   ['Water vapor is the least dense form of water.', 'Liquid water is the densest form.',
    'Going from gas to liquid, the particles pack much closer together.', 'So the density increases.'],
   '**Density would increase.** Gas particles are spread far apart; liquid particles are packed close, so the same water takes up less space.',
   'Water vapor is lowest, ice is in the middle, liquid water is highest.',
   V('Steam from a shower turns into water droplets on a cold mirror. What happens to the density of that water?',
     ['It increases', 'It decreases', 'It stays the same', 'It drops to zero'], 0,
     '**It increases.** The water went from a gas to a liquid, and liquid water is much denser than water vapor.',
     ['Steam is water vapor, a gas.', 'The droplets on the mirror are liquid.',
      'Liquid water is denser than water vapor.', 'So the density increases.']))

gq(2, 'When the liquid water droplets in the clouds grow bigger and bigger, they get to a point when they '
      'can no longer be suspended in the air. These droplets then fall to earth as "precipitation." The '
      'most common form of precipitation is rain. As rain falls to the earth from the clouds, the '
      'temperature of the air increases as droplets come closer to the surface of the earth. What happens '
      'to the MOTION of the MOLECULES that make up a raindrop as the temperature gets warmer?',
   ['they would slow down', 'they would speed up', 'they would stay the same', 'it is impossible to tell'], 1,
   'Warmer means more energy.',
   ['The raindrop falls into warmer air.', 'Warmer means its molecules gain energy.',
    'More energy means faster motion.'],
   '**They would speed up.** As the raindrop warms, its molecules gain energy and move faster.',
   'Warmer speeds them up — the other half of the teacher\'s note.',
   V('A cold bottle of water is left in a sunny car. What happens to the water molecules as the water warms up?',
     ['They slow down', 'They speed up', 'They stay the same speed', 'They turn into air'], 1,
     '**They speed up.** The sun warms the water, so its molecules gain energy and move faster.',
     ['The water is getting warmer.', 'Warmer means more energy.',
      'More energy means the molecules move faster.']))

gq(2, 'Sometimes when a droplet of rain is falling from a storm cloud towards the earth, a strong gust of '
      'wind will push it back up higher in the atmosphere, further from the surface of the earth, where the '
      'temperatures are below 0°C. This is how "hail" is formed. In this situation, what PHASE OF MATTER '
      'would the water change into?',
   ['solid', 'liquid', 'gas', 'none of the above'], 0,
   'What does water become below 0°C?',
   ['0°C is the temperature water freezes at.', 'Below 0°C, liquid water turns into ice.',
    'Ice is a solid.'],
   '**Solid.** Below 0°C the raindrop freezes, and hail is ice: water as a solid.',
   'Hail is just raindrops that froze on the way down.',
   V('A tray of water is put in a freezer at −18°C overnight. What phase is the water in the morning?',
     ['Gas', 'Liquid', 'Solid', 'Half gas, half liquid'], 2,
     '**Solid.** −18°C is well below 0°C, the freezing point of water, so it has turned to ice.',
     ['Water freezes at 0°C.', '−18°C is colder than that.', 'So the water has frozen into ice, a solid.']))

gq(1, 'When raindrops turn into hail, what PHYSICAL PROCESS has occurred?',
   ['melting', 'condensation', 'evaporation', 'freezing'], 3,
   'Liquid water turning into solid ice.',
   ['A raindrop is liquid water.', 'Hail is solid ice.', 'Liquid to solid is freezing.'],
   '**Freezing.** The raindrop went from liquid to solid.',
   'Freezing is the reverse of melting.',
   V('An icicle forms as water dripping off a roof turns to ice. Which process is that?',
     ['Melting', 'Freezing', 'Evaporation', 'Condensation'], 1,
     '**Freezing.** Liquid water dripping off the roof turned into solid ice.',
     ['Dripping water is a liquid.', 'An icicle is solid ice.', 'Liquid to solid is freezing.']))

gq(3, 'How would the DENSITY of the water in the raindrop change AFTER it became hail?',
   ['Density would increase', 'Density would decrease', 'Density would stay the same', 'none of the above'], 1,
   'Water is unusual. Which is denser: liquid water or ice?',
   ['Most substances get denser when they freeze.', 'Water is the exception.',
    'Liquid water is denser than ice, which is why ice floats.', 'So the density decreases.'],
   '**Density would decrease.** Water is the exception: ice is less dense than liquid water, which is why ice floats.',
   'Liquid water is the densest form of water. Ice is in the middle; vapor is lowest.',
   V('A full bottle of water is frozen and the ice bulges out of the top. Why?',
     ['Ice is denser than water, so the ice shrinks and pulls away',
      'Ice is less dense than water, so the same water takes up more space',
      'Freezing adds extra water to the bottle from the cold air',
      'The plastic bottle shrinks in the cold and squeezes it out'], 1,
     '**Ice is less dense than water, so the same water takes up more space.** Water is the exception: it expands when it freezes.',
     ['Freezing does not add or remove any water.', 'Water becomes less dense when it freezes.',
      'Less dense means the same mass takes up more space.', 'So the ice needs more room than the water did.']))

gq(2, 'Fertilizers are sometimes added to help plants grow. Fertilizers provide key nutrients that plants '
      'need. Compost is sometimes used as a natural fertilizer for plants. Compost is made by collecting '
      'things like kitchen scraps, dead plant parts, and grass clippings, then allowing them to break down '
      'some before adding them to the plants to provide nutrients to them. What type of substance is compost?',
   ['Mixture', 'Solution'], 0,
   'Could you pick the pieces out?',
   ['Compost is made of scraps, leaves and grass clippings.', 'You can still see and pick out the pieces.',
    'Nothing has dissolved completely.', 'So compost is a mixture.'],
   '**Mixture.** You can still pick the pieces out, so nothing has dissolved into a solution.',
   'The teacher\'s note: can pick out pieces.',
   V('Which of these is a mixture you could pick apart by hand?',
     ['Salt stirred into a glass of water', 'Trail mix of nuts, raisins and pretzels', 'Sugar dissolved in a cup of hot tea', 'Lemonade made from a powder mix'], 1,
     '**Trail mix of nuts, raisins and pretzels.** You can pick out each piece. The other three are solutions.',
     ['In a solution, one substance dissolves and disappears.', 'Salt, sugar and lemonade powder all dissolve in water.',
      'Trail mix pieces stay separate.', 'So the trail mix is the mixture you could pick apart.']))

gq(2, 'Chemical fertilizers are often used to help plants grow. These come in a variety of forms. One '
      'substance that is used as a fertilizer to replenish potassium in the soil is called "potash" or '
      'potassium oxide (K₂O). Potassium is a key nutrient for plants as it is necessary for growth of strong '
      'stems, the transport of water within plants, and for encouraging flowering and fruiting. As a '
      'fertilizer, potassium oxide is mixed with water (H₂O) where it dissolves completely and does not '
      'settle to the bottom. It is then sprayed on the soil. What kind of substance is potassium oxide and water?',
   ['Mixture', 'Solution'], 1,
   'It dissolves completely and does not settle.',
   ['The potassium oxide dissolves completely in the water.', 'It does not settle to the bottom.',
    'Dissolving completely is what makes a solution.'],
   '**Solution.** The potassium oxide dissolves completely and does not settle, which is what a solution is.',
   'Watch for the words "dissolves completely" and "does not settle".',
   V('Sand is stirred into a glass of water. A minute later the sand is lying on the bottom. What is it?',
     ['A solution, because it was stirred', 'A mixture, because the sand settled out',
      'A solution, because water is involved', 'An element, because sand is natural'], 1,
     '**A mixture, because the sand settled out.** The sand never dissolved, so it is not a solution.',
     ['In a solution, the substance dissolves and does not settle.', 'The sand sank to the bottom.',
      'So it did not dissolve.', 'That makes it a mixture.']))

gq(1, 'When making lemonade, you mix lemonade powder into water. Which is the SOLVENT in this solution?',
   ['Ice', 'Lemonade powder', 'water', 'It is impossible to tell'], 2,
   'Which one does the dissolving?',
   ['The solvent is the substance that does the dissolving.', 'The solute is what you add, and it dissolves.',
    'The powder dissolves into the water.', 'So water is the solvent.'],
   '**Water.** Water does the dissolving, so it is the solvent. The powder is the solute.',
   'Solvent does the dissolving; the solute is what you add.',
   V('Sugar is stirred into hot tea until it disappears. Which is the SOLUTE?',
     ['The tea', 'The sugar', 'The cup', 'The spoon'], 1,
     '**The sugar.** The sugar is added and dissolves, so it is the solute. The tea does the dissolving, so it is the solvent.',
     ['The solute is the substance that gets dissolved.', 'The sugar is added to the tea.',
      'The sugar disappears into the tea.', 'So the sugar is the solute.']))

gq(2, 'A grape is placed on a balance in a container. (The picture shows: the empty container on the '
      'balance reads 6 g; with the grape inside it, the balance reads 14 g.) To find the density of this '
      'grape we need to find the MASS. What is the MASS of this grape? The balance units are grams.',
   ['14 g', '6 g', '8 g', '20 g'], 2,
   'The 14 g includes the container.',
   ['The balance read 6 g with only the container.', 'It read 14 g with the container and the grape.',
    'Subtract the container: 14 − 6 = 8.', 'The grape is 8 g.'],
   '**8 g.** Filled minus empty: 14 g − 6 g = 8 g. The 14 g counts the container too.',
   'Filled minus empty — the teacher\'s note on the key.',
   V('An empty cup on a balance reads 4 g. With a strawberry in it, the balance reads 9 g. What is the mass of the strawberry?',
     ['13 g', '9 g', '5 g', '4 g'], 2,
     '**5 g.** Filled minus empty: 9 g − 4 g = 5 g.',
     ['The cup alone is 4 g.', 'The cup and the strawberry are 9 g.', 'Subtract: 9 − 4 = 5.', 'The strawberry is 5 g.']), frm='source')

gq(2, 'To find the density of the grape, we need to find the VOLUME. (The picture labels it: length 3 cm, '
      'width 1 cm, height 2 cm.) What is the VOLUME of the grape? Assume it is a rectangular prism with the '
      'dimensions listed above.',
   ['5 cm³', '6 cm³', '6 cm', '7 cm³'], 1,
   'Multiply all three, then check the unit.',
   ['Volume of a rectangular prism is length × width × height.', '3 × 1 × 2 = 6.',
    'A volume is measured in cubic centimetres.', 'So the volume is 6 cm³.'],
   '**6 cm³.** 3 × 1 × 2 = 6, and a volume is in cm³, not cm.',
   '6 cm is the right number with the wrong unit: cm is a length.',
   V('A block is 5 cm long, 2 cm wide and 1 cm tall. What is its volume?',
     ['8 cm³', '10 cm', '10 cm³', '7 cm³'], 2,
     '**10 cm³.** 5 × 2 × 1 = 10, and a volume is in cm³.',
     ['Volume is length × width × height.', '5 × 2 × 1 = 10.', 'Volume uses cubic units: cm³.',
      'So it is 10 cm³. Adding the sides (8) is a different calculation.']))

gq(2, 'The density of the grape is 1.25 g/cm³. Would this grape FLOAT or SINK in water and WHY?',
   ['It floats because the density is higher than that of water.',
    'It sinks because the density is higher than that of water.',
    'It floats because the density is lower than that of water.',
    'It sinks because the density is lower than that of water.'], 1,
   'Water is 1 g/cm³. Is 1.25 more or less?',
   ['Water has a density of 1 g/cm³.', '1.25 is more than 1.', 'Denser than water sinks.',
    'So the grape sinks because its density is higher.'],
   '**It sinks because the density is higher than that of water.** 1.25 g/cm³ is more than water\'s 1 g/cm³.',
   'More than 1 sinks; less than 1 floats.',
   V('A piece of wood has a density of 0.6 g/cm³. What happens when it is put in water?',
     ['It sinks because it is denser than water', 'It floats because it is less dense than water',
      'It sinks because it is less dense than water', 'It floats because it is denser than water'], 1,
     '**It floats because it is less dense than water.** 0.6 g/cm³ is less than water\'s 1 g/cm³.',
     ['Water is 1 g/cm³.', '0.6 is less than 1.', 'Less dense than water floats.']))

gq(1, 'Which of the following is an ELEMENT?', ['CO₂', 'C₅₅H₇₂O₅N₄Mg', 'C₆H₁₂O₆', 'He'], 3,
   'Which one could you find in a single box on the periodic table?',
   ['An element is one kind of atom.', 'CO₂, C₅₅H₇₂O₅N₄Mg and C₆H₁₂O₆ each have more than one capital letter.',
    'More than one capital letter means more than one kind of element joined.', 'He is helium, one box on the table.'],
   '**He.** Helium is one element with its own box on the periodic table. The others are made of several elements joined.',
   'Think: can you find it on the periodic table?',
   V('Which of these is an ELEMENT?', ['NaCl', 'H₂O', 'Fe', 'CO₂'], 2,
     '**Fe.** Fe is iron, one element with its own box. NaCl, H₂O and CO₂ each join two elements.',
     ['Count the capital letters.', 'NaCl, H₂O and CO₂ each have two kinds of element.',
      'Fe has one capital letter: it is iron.', 'So Fe is the element.']))

gq(2, 'Which of the following is a MOLECULE?', ['Nb', 'B', 'C', 'H₂O'], 3,
   'Which one has two or more atoms joined?',
   ['A molecule is two or more atoms joined together.', 'Nb, B and C are each one element symbol.',
    'H₂O is two hydrogen atoms and one oxygen atom joined.', 'So H₂O is the molecule.'],
   '**H₂O.** Two hydrogen atoms and one oxygen atom joined together make a molecule.',
   'A molecule has 2 or more atoms, of the same kind or different kinds.',
   V('Which of these is a MOLECULE?', ['Cu', 'Ne', 'CO₂', 'Au'], 2,
     '**CO₂.** One carbon atom and two oxygen atoms joined together. Cu, Ne and Au are each a single element.',
     ['A molecule is two or more atoms joined.', 'Cu, Ne and Au are single element symbols.',
      'CO₂ is three atoms joined.', 'So CO₂ is the molecule.']))

gq(1, 'A box on the periodic table represents what?', ['An element', 'A molecule', 'A compound', 'A planet'], 0,
   'The table lists the building blocks, one per box.',
   ['The periodic table lists every element.', 'Each box holds one element and its symbol.',
    'So a box represents an element.'],
   '**An element.** Every box is one element, with its own symbol.',
   'Molecules and compounds are built FROM elements, so they are not on the table.',
   V('Where would you look to find the symbol for oxygen?',
     ['A long list of molecules', 'A box on the periodic table', 'A long list of compounds', 'A map of the solar system'], 1,
     '**A box on the periodic table.** Oxygen is an element, and every element has its own box.',
     ['Oxygen is an element.', 'The periodic table has one box for each element.',
      'So oxygen\'s symbol is in its box on the table.']))

gq(1, 'The periodic table is mainly made up of ________.', ['Metals', 'Semi-Metals', 'Metalloids', 'Halogens'], 0,
   'Most of the boxes belong to one big group.',
   ['The periodic table has well over 100 elements.', 'Most of them are metals.',
    'Metalloids and halogens are much smaller groups.'],
   '**Metals.** Most of the elements on the periodic table are metals.',
   'Iron, copper, gold, aluminum, sodium — the metals fill most of the table.',
   V('Most of the elements on the periodic table are ________.',
     ['Gases', 'Liquids', 'Metals', 'Molecules'], 2,
     '**Metals.** Most elements are metals. Only a few are gases, and very few are liquids at room temperature.',
     ['Think about how many elements are metals.', 'Iron, copper, gold and many more are metals.',
      'Gases and liquids are only a small part of the table.', 'So most elements are metals.']))

assert len(Q) == 21, len(Q)
for x in Q:
    assert x.get('variant'), x['id']
    v = x['variant']; assert len(v['opts']) == 4 and len(set(v['opts'])) == 4 and 0 <= v['ans'] < 4
    assert v['q'].strip() != x['q'].strip()

PAPER_KEY = 'ABACABABADBABCCBBDDAA'
got = ''.join('ABCD'[x['ans']] for x in Q)
assert got == PAPER_KEY, (got, PAPER_KEY)   # option order is FIXED: never _balance a guide unit

unitA = {
  'id': 'unit-sci-chem-practice', 'type': 'unit', 'classId': 'science',
  'title': 'Chemistry · Practice Unit Test', 'status': 'draft',
  'guide': True, 'prep': True, 'order': 1, 'quarter': 2, 'libv': 1,
  'srcName': 'Practice for Chemistry Unit Test + answer key (Drive)',
  'source': 'source',
  'summary': {'from': 'source', 'text':
    'Your teacher\'s "Practice for Chemistry Unit Test", all 21 questions, in the same A/B/C/D order '
    'as the paper. It follows water through the atmosphere and into plants: matter, phases, particle '
    'speed, phase changes, density, mixtures and solutions, mass and volume, elements, molecules and '
    'the periodic table.'},
  'why': {'from': 'added', 'text':
    'This is the shape of the real Chemistry unit test. Every question is a different chemistry idea '
    'applied to something real, so the useful thing is spotting which idea each one is asking for.'},
  'objectives': [
    {'from': 'source', 'text': 'Tell matter from things that are not matter, like light and energy.'},
    {'from': 'source', 'text': 'Say how temperature changes the speed of particles.'},
    {'from': 'source', 'text': 'Name condensation and freezing, and say how water\'s density changes with each.'},
    {'from': 'source', 'text': 'Tell a mixture from a solution, and a solvent from a solute.'},
    {'from': 'source', 'text': 'Find mass by subtraction and volume by length × width × height.'},
    {'from': 'source', 'text': 'Tell an element from a molecule, and say what a box on the periodic table is.'}],
  'parentNote': {'from': 'added', 'text':
    'This is the teacher\'s practice test copied out word for word, with the options in the same order '
    'as the paper, so the "I did it on paper" door works: she does the 21 questions on the printout and '
    'taps in the letters she wrote. Every answer was re-derived independently and all 21 match the '
    'teacher\'s circled key. Questions 15 and 16 lean on a picture (a balance reading 6 g empty and '
    '14 g with the grape, and a prism labelled 3 cm × 1 cm × 2 cm); the stems here say what the picture '
    'shows, so a miss that comes back later can still be answered without the paper. The teacher\'s '
    'margin notes on the key are on the flashcards as written: "matter is not energy or feelings", '
    '"know water examples", "know freezing too", the water-density ranking (vapor lowest, ice medium, '
    'liquid high), "can pick out pieces", the solvent and solute definitions, "filled minus empty", '
    '"more than 1 sinks", "can you find it on the periodic table", and "2 or more atoms". The test date '
    'was not in anything uploaded, so the app still has it as the week of 10/20.'},
  'nextUp': {'from': 'added', 'minutes': 25, 'text':
    'Do the paper first with the printout in front of you, then tap in your 21 letters. '
    'Anything you miss, the rescue round asks again with a fresh example.'},
  'cards': C, 'questions': Q,
  'updatedAt': int(time.time() * 1000) - 3 * 3600 * 1000,
}

# ======================================================== B — the study test
C2, Q2 = [], []

card(C2, 'Matter or not',
     '**Matter has mass and takes up space. Energy, light, sound and feelings do not.**'
     '\n• A gas you cannot see is still matter.')
card(C2, 'Hotter is faster',
     '**Heating speeds particles up. Cooling slows them down.**'
     '\n• Cooling never stops them completely; it only slows them.')
card(C2, 'Four phase changes to know cold',
     '**Melting: solid to liquid. Freezing: liquid to solid. Evaporation: liquid to gas. Condensation: gas to liquid.**'
     '\n• Clouds, dew and a foggy mirror are condensation.'
     '\n• Hail, icicles and ice cubes are freezing.')
card(C2, 'Water is the exception',
     '**Liquid water is denser than ice, and ice is denser than water vapor.**'
     '\n• Freezing makes water LESS dense, which is why ice floats.'
     '\n• Condensing makes water MORE dense.')
card(C2, 'Mixture or solution',
     '**If you can see or pick out the parts, it is a mixture. If one part dissolves completely and does not settle, it is a solution.**'
     '\n• Salad, trail mix, sand in water: mixtures.'
     '\n• Salt water, sweet tea, lemonade from powder: solutions.')
card(C2, 'Solvent and solute',
     '**The solvent does the dissolving; the solute gets dissolved.**'
     '\n• In salt water, water is the solvent and salt is the solute.'
     '\n• Water is the most common solvent there is.', frm='source')
card(C2, 'Density in three steps',
     '**Find the mass, find the volume, then divide mass by volume.**'
     '\n• Mass: filled minus empty on the balance.'
     '\n• Volume of a box shape: length × width × height, in cm³.'
     '\n• Compare with water\'s 1 g/cm³ to say float or sink.', eq='density = mass ÷ volume', frm='added')
card(C2, 'Element, molecule, periodic table',
     '**An element is one kind of atom and has its own box on the periodic table. A molecule is two or more atoms joined.**'
     '\n• One capital letter, no numbers (Fe, He): one element.'
     '\n• Most of the boxes on the table are metals.', frm='source')

def sq(lv, text, opts, ans, hint, steps, main, tip, frm='source'):
    q(Q2, lv, text, opts, ans, hint, steps, main, tip, frm=frm)

sq(1, 'Which of these is NOT matter?', ['Steam from a kettle', 'The smell of toast', 'The heat from an oven', 'A grain of rice'], 2,
   'Three of these are made of particles. One is energy.',
   ['Matter has mass and takes up space.', 'Steam is water vapor, a gas.',
    'The smell of toast is tiny particles in the air.', 'Heat is energy, so it is not matter.'],
   '**The heat from an oven.** Heat is energy. Steam, a smell (particles in the air) and rice all have mass and take up space.',
   'A smell is matter: it is particles reaching your nose.')
sq(1, 'Which of these IS matter?', ['A rainbow', 'An echo', 'The air inside a soccer ball', 'A feeling of excitement'], 2,
   'Which one could you weigh, if you had a fine enough balance?',
   ['A rainbow is light.', 'An echo is sound.', 'A feeling is not a thing at all.',
    'Air is a mixture of gases, so it is matter.'],
   '**The air inside a soccer ball.** Air is gases, and gases have mass and take up space. The ball is heavier pumped up than flat.',
   'Light, sound and feelings are never matter.')
sq(1, 'A puddle on the sidewalk dries up on a sunny afternoon. Which process happened?',
   ['Condensation', 'Freezing', 'Evaporation', 'Melting'], 2,
   'The water went from liquid into the air.',
   ['The puddle was liquid water.', 'It went into the air as water vapor, a gas.', 'Liquid to gas is evaporation.'],
   '**Evaporation.** The liquid water turned into water vapor and went into the air.',
   'Evaporation is the reverse of condensation.')
sq(2, 'Your bathroom mirror fogs up while you take a hot shower. Which process made the fog?',
   ['Evaporation', 'Condensation', 'Melting', 'Freezing'], 1,
   'The fog is tiny liquid droplets. Where did they come from?',
   ['The hot shower filled the air with water vapor.', 'The vapor touched the cooler mirror.',
    'It turned into tiny liquid droplets.', 'Gas to liquid is condensation.'],
   '**Condensation.** Water vapor from the shower turned back into liquid droplets on the cooler mirror.',
   'The same process makes clouds and dew.')
sq(2, 'Water in an ice cube tray turns into ice cubes in the freezer. What happens to the water particles as it cools?',
   ['They speed up', 'They slow down', 'They stop completely', 'They stay the same speed'], 1,
   'Cooling takes energy away.',
   ['The freezer cools the water.', 'Cooling means the particles lose energy.',
    'Less energy means slower particles.', 'They slow down, but they never stop completely.'],
   '**They slow down.** Cooling takes energy away, so the particles move more slowly and lock into a solid.',
   '"They stop completely" is the trap: particles in ice still vibrate.')
sq(2, 'A pot of water is heated on the stove. What happens to the water molecules as the water gets hotter?',
   ['They slow down', 'They stay the same', 'They speed up', 'They get smaller'], 2,
   'Heating adds energy.',
   ['The stove adds heat.', 'Heat is energy.', 'More energy makes molecules move faster.'],
   '**They speed up.** Heating gives the molecules more energy, so they move faster.',
   'The molecules do not change size; only their speed changes.')
sq(3, 'A full, sealed bottle of water is left in the freezer and cracks open as the water freezes. Why?',
   ['Ice is denser than water, so it pulls the bottle in',
    'Ice is less dense than water, so the same water takes up more room',
    'Freezing turns some of the water into a gas that pushes out',
    'Cold air gets into the bottle and adds more water'], 1,
   'Water is the exception to the usual rule.',
   ['No water was added or lost.', 'Water becomes less dense when it freezes.',
    'Less dense means the same mass takes up more space.', 'The ice needed more room than the bottle had.'],
   '**Ice is less dense than water, so the same water takes up more room.** Water expands as it freezes, which is also why ice floats.',
   'Most substances get denser when they freeze. Water does the opposite.')
sq(3, 'Water vapor in the air condenses into liquid droplets on a cold window. What happens to the density of that water?',
   ['It increases', 'It decreases', 'It stays the same', 'It cannot be measured'], 0,
   'Which is denser: water as a gas or water as a liquid?',
   ['Water vapor is the least dense form of water.', 'Liquid water is the densest form.',
    'Going from gas to liquid packs the particles closer.', 'So the density increases.'],
   '**It increases.** Gas particles are spread far apart; in the liquid they are packed close together.',
   'Vapor lowest, ice in the middle, liquid highest.')
sq(1, 'Which of these is a solution?', ['A bowl of salad', 'Salt dissolved in water', 'Sand and pebbles in a bucket', 'Cereal in milk'], 1,
   'In which one does something disappear into the liquid?',
   ['In a solution, one substance dissolves completely.', 'Salt dissolves and you cannot see it any more.',
    'Salad, sand and pebbles, and cereal in milk can all be picked apart.', 'So the salt water is the solution.'],
   '**Salt dissolved in water.** The salt dissolves completely and does not settle. The others can be picked apart, so they are mixtures.',
   'Cereal in milk is a mixture: you can fish the cereal out.')
sq(2, 'A bag of trail mix holds peanuts, raisins and chocolate pieces. What kind of substance is it?',
   ['A solution', 'A mixture', 'An element', 'A molecule'], 1,
   'Can you pick the pieces out?',
   ['Each piece keeps its own look and taste.', 'You can pick the peanuts out by hand.',
    'Nothing has dissolved.', 'So it is a mixture.'],
   '**A mixture.** You can pick every piece out, so nothing has dissolved.',
   'Can pick out pieces: mixture.')
sq(2, 'Hot cocoa is made by stirring cocoa powder into hot milk until it dissolves. Which is the SOLVENT?',
   ['The cocoa powder', 'The hot milk', 'The spoon', 'The mug'], 1,
   'Which one does the dissolving?',
   ['The solvent does the dissolving.', 'The solute is added and dissolves.',
    'The cocoa powder dissolves into the milk.', 'So the milk is the solvent.'],
   '**The hot milk.** The milk does the dissolving, so it is the solvent; the cocoa powder is the solute.',
   'The solvent is usually the liquid you start with.')
sq(2, 'Salt is stirred into a pot of water until it disappears. Which is the SOLUTE?',
   ['The water', 'The pot', 'The salt', 'The steam'], 2,
   'Which one gets dissolved?',
   ['The solute is what you add, and it dissolves.', 'The salt is added to the water.',
    'The salt disappears into the water.', 'So the salt is the solute.'],
   '**The salt.** It is added and dissolves, so it is the solute; the water is the solvent.',
   'Solute: you add it, it dissolves.')
sq(2, 'An empty cup on a balance reads 12 g. After sugar is poured in, the balance reads 37 g. What is the mass of the sugar?',
   ['49 g', '37 g', '25 g', '12 g'], 2,
   'The 37 g includes the cup.',
   ['The cup alone is 12 g.', 'The cup and the sugar together are 37 g.', 'Subtract: 37 − 12 = 25.', 'The sugar is 25 g.'],
   '**25 g.** Filled minus empty: 37 g − 12 g = 25 g. Adding them (49 g) counts the cup twice.',
   'Filled minus empty.')
sq(2, 'A block is 4 cm long, 2 cm wide and 3 cm tall. What is its volume?',
   ['9 cm³', '24 cm', '24 cm³', '14 cm³'], 2,
   'Multiply all three, then check the unit.',
   ['Volume is length × width × height.', '4 × 2 × 3 = 24.', 'Volume is in cubic centimetres.', 'So it is 24 cm³.'],
   '**24 cm³.** 4 × 2 × 3 = 24, in cm³. 24 cm has the right number but a length unit; 9 is the sides added.',
   'Three lengths multiplied give cubic units.')
sq(3, 'A block 4 cm long, 2 cm wide and 3 cm tall has a mass of 48 g. What is its density, and does it float in water?',
   ['2 g/cm³, and it sinks', '2 g/cm³, and it floats', '0.5 g/cm³, and it floats', '72 g/cm³, and it sinks'], 0,
   'Density is mass divided by volume. Its volume is 4 × 2 × 3.',
   ['Volume: 4 × 2 × 3 = 24 cm³.', 'Density: 48 ÷ 24 = 2 g/cm³.',
    'Water is 1 g/cm³, and 2 is more than 1.', 'So it sinks.'],
   '**2 g/cm³, and it sinks.** 48 g ÷ 24 cm³ = 2 g/cm³, which is more than water\'s 1 g/cm³.',
   '0.5 is volume divided by mass, the wrong way round.')
sq(2, 'A cork has a density of 0.24 g/cm³ and a pebble has a density of 2.6 g/cm³. What happens when both are dropped into water?',
   ['Both float', 'Both sink', 'The cork floats and the pebble sinks', 'The cork sinks and the pebble floats'], 2,
   'Compare each with water\'s 1 g/cm³.',
   ['Water is 1 g/cm³.', '0.24 is less than 1, so the cork floats.', '2.6 is more than 1, so the pebble sinks.'],
   '**The cork floats and the pebble sinks.** Less than 1 floats; more than 1 sinks.',
   'More than 1 sinks; less than 1 floats.')
sq(1, 'Which of these is an ELEMENT?', ['NaCl', 'Ne', 'H₂O', 'CO₂'], 1,
   'Which one has a single box on the periodic table?',
   ['An element is one kind of atom.', 'NaCl, H₂O and CO₂ each join two kinds of element.',
    'Ne is neon, one element.', 'So Ne is the element.'],
   '**Ne.** Neon is one element with its own box. The others each join two elements together.',
   'Count the capital letters: one capital, one element.')
sq(2, 'Which of these is a MOLECULE?', ['Fe', 'Cu', 'CO₂', 'Na'], 2,
   'Which one is two or more atoms joined?',
   ['A molecule is two or more atoms joined.', 'Fe, Cu and Na are each a single element symbol.',
    'CO₂ is one carbon atom and two oxygen atoms.', 'So CO₂ is the molecule.'],
   '**CO₂.** Three atoms joined together. Fe, Cu and Na are single elements.',
   'A small number after a symbol means more than one atom.')
sq(1, 'What does each box on the periodic table show?', ['One element', 'One molecule', 'One mixture', 'One solution'], 0,
   'The table lists the building blocks.',
   ['The periodic table lists all the elements.', 'Each box holds one element and its symbol.',
    'Molecules, mixtures and solutions are made from elements.'],
   '**One element.** Each box is one element. Molecules, mixtures and solutions are made from elements, so they are not on the table.',
   'Every box, one element.')
sq(1, 'Most of the elements on the periodic table are ________.', ['Gases', 'Metals', 'Liquids', 'Molecules'], 1,
   'Iron, copper, gold, aluminum…',
   ['There are well over 100 elements.', 'Most of them are metals.',
    'Only a few are gases, and very few are liquids at room temperature.'],
   '**Metals.** Most of the table is metals.',
   'Molecules are not elements, so they are never on the table.')

assert len(Q2) == 20, len(Q2)
_balance(Q2)

unitB = {
  'id': 'unit-sci-chem-test', 'type': 'unit', 'classId': 'science',
  'title': 'Chemistry · Study Test', 'status': 'draft',
  'prep': True, 'order': 2, 'quarter': 2, 'round': 20, 'libv': 1,
  'srcName': 'Built to match the Chemistry practice test (Drive)',
  'source': 'added',
  'summary': {'from': 'added', 'text':
    'A second test over the same chemistry ideas as the practice paper, set in a kitchen and a bathroom '
    'instead of the atmosphere: matter, particle speed, phase changes, water\'s density, mixtures and '
    'solutions, mass, volume, density, elements, molecules and the periodic table. Nothing here is '
    'copied from the paper.'},
  'why': {'from': 'added', 'text':
    'Doing the same test twice mostly tests whether you remember the answers. A different test on the '
    'same ideas shows whether you can actually use them.'},
  'objectives': [
    {'from': 'source', 'text': 'Tell matter from energy, light, sound and feelings.'},
    {'from': 'source', 'text': 'Name melting, freezing, evaporation and condensation from everyday examples.'},
    {'from': 'source', 'text': 'Say how water\'s density changes when it freezes or condenses.'},
    {'from': 'source', 'text': 'Tell a mixture from a solution, and a solvent from a solute.'},
    {'from': 'added', 'text': 'Find mass, volume and density, and say whether something floats.'},
    {'from': 'source', 'text': 'Tell an element from a molecule.'}],
  'parentNote': {'from': 'added', 'text':
    'This is the parallel test: the same ideas as the teacher\'s practice paper, all new examples, so '
    'she cannot answer from memory of the first one. It runs as an ordinary 20-question quiz in one '
    'sitting with the options shuffled, and anything she misses lands in the Growth Zone. Mixtures and '
    'solutions and the periodic table are on the practice paper but had no part on the Chemistry shelf '
    'yet, so this is the first place they are practised; no class notes for either were in Drive, so '
    'they are taught here only as far as the practice paper and its key go. One question goes a step '
    'past the paper and works a density out (48 g ÷ 24 cm³); the paper gives the density ready-made.'},
  'nextUp': {'from': 'added', 'minutes': 20, 'text':
    'Twenty questions in one sitting, the shape of the real test. Take it after the paper one and see '
    'which ideas still wobble.'},
  'cards': C2, 'questions': Q2,
  'updatedAt': int(time.time() * 1000) - 3 * 3600 * 1000,
}

for u, fn in ((unitA, 'science-chem-practice.json'), (unitB, 'science-chem-test.json')):
    path = os.path.join(REPO, 'content', fn)
    json.dump({'v': 1, 'records': {u['id']: u}},
              io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote %-28s %2d cards %2d questions  guide=%s prep=%s order=%s'
          % (fn, len(u['cards']), len(u['questions']), u.get('guide'), u.get('prep'), u['order']))
print('paper key preserved:', got)
