#!/usr/bin/env python3
"""Chemistry · 3 Density and Buoyancy.

Source: "density and buoyancy.pdf" — River's own completed Science 4 Lesson
Check, 20 points, Drive, uploaded 2026-09-25. Rendered with pypdfium2 and
read as images: her answers are circled by hand and the teacher's ticks are
in pen, neither of which any text extraction can see.

SHE GOT 20/20. Marked A+ in pen, every one of the twenty ticked. So unlike
the Phases of Matter sheet (v161) and the Matter Phase Changes check (v165),
there are no mistakes of hers to target here — this unit covers the material
for the test rather than repairing anything. parentNote says so plainly,
because "she aced it" is the useful thing for a grown-up to know.

SHELF: it joins Chemistry as part 3 rather than starting its own. The sheet's
own question 5 asks her to rank the phases of matter by density, which is
exactly what "Chemistry · 1 Phases of Matter" teaches — density is being used
here as a property OF the phases she has just studied, not as a new unit. The
Drive file also sits loose in Science rather than in a numbered unit folder,
so there is no folder name to defer to (the math-program rule). If her teacher
turns out to number it separately, it is a retitle keeping the id.

TWO THINGS THE SHEET NEEDS BUT NEVER STATES, both added here:
  * the density formula itself. The sheet asks which two properties density
    compares, and never that it is mass divided by volume.
  * water's density, 1 g/cm3. Questions 14 and 15 give her 0.32 and 1.7 and
    ask float or sink, which is unanswerable without the number to compare
    against — she clearly knows it, but it is nowhere on the paper.
"""
import io, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

C, Q = [], []

# ------------------------------------------------------------------ cards

card(C, 'Density',
     "**How much mass is packed into a given amount of space.**\n"
     "• The two properties being compared are MASS and VOLUME\n"
     "• Not weight and size, and nothing to do with color or temperature\n"
     "• Two things can be exactly the same size and still have very different densities",
     hint="How much stuff, in how much room.")

card(C, 'The formula',
     "**Density = mass ÷ volume.**\n"
     "• Mass is usually in grams, volume in cubic centimeters (cm³)\n"
     "• So density is usually written in g/cm³\n"
     "• 60 g of something filling 20 cm³ has a density of 3 g/cm³",
     eq="density = mass / volume",
     hint="Divide what it weighs by how much room it takes up.",
     frm='added')

card(C, 'Reading it from the particles',
     "**In the same amount of space, more particles packed in means a higher density.**\n"
     "• Particles crowded tightly together — high density\n"
     "• The same box with only a few particles spread out — low density\n"
     "• This is why a picture of two boxes is enough to compare them without any numbers",
     hint="Same box, count the dots. More dots, denser.")

card(C, 'Same size, different density',
     "**Two objects can take up exactly the same amount of space and still have different "
     "densities.**\n"
     "• Their volumes match, so the difference has to be in the mass\n"
     "• A rock and a sponge of the same size are the classic pair — the rock has far more "
     "material packed into that space",
     hint="If the volume is equal, only the mass can be different.")

card(C, 'Volume of a rectangular prism',
     "**Multiply length × width × height.**\n"
     "• All three, not two — length × width alone gives you an area, not a volume\n"
     "• A box 4 cm by 3 cm by 2 cm holds 4 × 3 × 2 = 24 cm³",
     eq="V = l × w × h",
     hint="Three dimensions means three numbers multiplied.")

card(C, 'Finding the mass on a scale',
     "**Weigh the container with the object in it, then subtract the container on its own.**\n"
     "• Whatever the container weighs is not part of what you are measuring\n"
     "• A full dish reading 47 g on a dish that weighs 12 g empty holds 47 − 12 = 35 g",
     hint="The bowl is not the cereal. Take the bowl off the total.")

card(C, 'Phases, from densest to least dense',
     "**For a typical substance: solid, then liquid, then gas.**\n"
     "• Solid — particles locked tightly together, the most packed in\n"
     "• Liquid — particles still touching but able to slide past one another\n"
     "• Gas — particles far apart with a lot of empty space between them\n"
     "• Gases are by far the least dense, which is why they rise through liquids",
     hint="The tighter the packing, the higher the density. Solids win.")

card(C, 'Water is the famous exception',
     "**Solid water is LESS dense than liquid water — which is why ice floats.**\n"
     "• Almost every other substance is densest as a solid\n"
     "• Water's particles lock into a pattern with gaps in it when it freezes, so the same "
     "mass takes up MORE room\n"
     "• A lesson-check question that says \"a typical substance\" is leaving room for exactly this",
     hint="Ice cubes float in the glass. That is not what a typical solid does.",
     frm='added')

card(C, 'The density of water',
     "**1 g/cm³ — and it is the number every float-or-sink question is really comparing against.**\n"
     "• Less than 1 g/cm³ → less dense than water → it floats\n"
     "• More than 1 g/cm³ → more dense than water → it sinks\n"
     "• So a density on its own is not enough; you have to compare it to something",
     hint="One. Everything gets measured against it.",
     frm='added')

card(C, 'Float or sink',
     "**An object sinks if it is MORE dense than the liquid, and floats if it is LESS dense.**\n"
     "• It is a comparison, never a property of the object alone\n"
     "• Heavy does not mean sinking — a huge log floats and a small pebble sinks\n"
     "• The same object can float in one liquid and sink in another",
     hint="Denser than what it is in, it goes down. Less dense, it comes up.")

card(C, 'Buoyancy',
     "**The upward push a liquid gives to anything placed in it.**\n"
     "• If something is described as buoyant, it floats — buoyant and sinking are opposites\n"
     "• The push is there even for objects that sink; it is just not enough to hold them up",
     hint="Buoyant means it is being held up, not dragged down.")

card(C, 'Why a steel ship floats',
     "**Because a ship is mostly air, so the whole ship is less dense than water even though "
     "steel is not.**\n"
     "• What matters is the density of the entire object, hull and air together\n"
     "• Flatten the same steel into a solid block and it sinks — same material, different volume\n"
     "• This is the clearest proof that floating is about density, not about weight",
     hint="It is the whole ship you have to average, not the metal.",
     frm='added')

card(C, 'Heating a liquid',
     "**It becomes LESS dense and rises.**\n"
     "• Heating makes the particles move faster and spread further apart\n"
     "• The same mass now fills more space, so the density goes down\n"
     "• Less dense than the liquid around it means up it goes",
     hint="Warm spreads out, spread out is lighter for its size, and up it goes.")

card(C, 'Cooling a liquid',
     "**It becomes MORE dense and sinks.**\n"
     "• Cooling slows the particles, and they settle closer together\n"
     "• The same mass in less space means a higher density\n"
     "• Denser than its surroundings means it falls",
     hint="Cool pulls in, packed in is heavier for its size, and down it goes.")

card(C, 'Convection',
     "**The movement of warm and cool fluids — warm rises because it is less dense, cool sinks "
     "because it is more dense.**\n"
     "• A fluid means anything that flows, so both liquids and gases\n"
     "• The two halves happen at once, which sets up a circle called a convection current\n"
     "• It is what moves heat around a pan of soup, a room, an ocean and the atmosphere",
     hint="Warm up, cool down, round and round.")

card(C, 'Why convection keeps going',
     "**Because the fluid that rises cools down, and the fluid that sinks warms up.**\n"
     "• Warm fluid rises, moves away from the heat, and loses its heat\n"
     "• Now denser, it sinks back toward the heat source\n"
     "• Warmed again, it rises again — the loop only stops when the heating stops",
     hint="Nothing stays warm at the top or cold at the bottom. That is what makes it a cycle.",
     frm='added')

# -------------------------------------------------------------- questions

q(Q, 1, "Which two physical properties are being compared when you talk about density?",
  ["Mass and volume", "Length and mass", "Volume and temperature", "Mass and color"], 0,
  "One of them is how much stuff there is; the other is how much room it fills.",
  ["Density is about how tightly material is packed into a space.",
   "How much material there is, is its mass.",
   "How much space it fills, is its volume.",
   "So density compares mass and volume."],
  "**Mass and volume.** Density is how much mass is packed into a given volume — nothing else "
  "comes into it. Color and temperature do not change how much material is in the space.",
  "If you know both of those numbers you can work the density out. Nothing else will do it.")

q(Q, 1, "A block has a mass of 60 g and a volume of 20 cm³. What is its density?",
  ["3 g/cm³", "80 g/cm³", "40 g/cm³", "1,200 g/cm³"], 0,
  "The formula divides one of the numbers by the other.",
  ["Density = mass ÷ volume.",
   "The mass is 60 g and the volume is 20 cm³.",
   "60 ÷ 20 = 3.",
   "So the density is 3 g/cm³."],
  "**3 g/cm³.** Density = mass ÷ volume, so 60 ÷ 20 = 3. Adding or subtracting the two numbers "
  "gives you something that is not a density at all — the units tell you: grams PER cubic "
  "centimeter means grams divided by cubic centimeters.",
  "Read the unit out loud. g/cm³ is 'grams per cubic centimeter', and 'per' means divide.")

q(Q, 1, "For a typical substance, which order puts the phases from HIGHEST density to LOWEST?",
  ["Solid, liquid, gas", "Gas, liquid, solid", "Liquid, solid, gas", "Solid, gas, liquid"], 0,
  "Picture how close together the particles are in each one.",
  ["In a solid the particles are locked tightly together — the most packed in.",
   "In a liquid they still touch but can slide past each other — slightly less packed.",
   "In a gas they are far apart with a lot of empty space between them — by far the least packed.",
   "So the order is solid, liquid, gas."],
  "**Solid, liquid, gas.** Density follows how tightly the particles are packed, and that is "
  "exactly the order of the three phases. Water is the famous exception, which is why ice floats "
  "— but the question says a typical substance.",
  "Tightest packing first. That is all this ordering is.")

q(Q, 1, "What is the volume of a box measuring 4 cm long, 3 cm wide and 2 cm high?",
  ["24 cm³", "9 cm³", "12 cm³", "14 cm³"], 0,
  "A volume needs all three measurements, not two of them.",
  ["The volume of a rectangular prism is length × width × height.",
   "That is 4 × 3 × 2.",
   "4 × 3 = 12, and 12 × 2 = 24.",
   "So the volume is 24 cm³."],
  "**24 cm³.** Multiply all three: 4 × 3 × 2 = 24. Multiplying only the length and width gives 12, "
  "which is an area rather than a volume — the cubed unit is the giveaway that three measurements "
  "went into it.",
  "Three dimensions, three numbers multiplied together.")

q(Q, 1, "An object will sink in water if it ______.",
  ["is more dense than water", "is less dense than water",
   "has the same density as water", "has a large mass"], 0,
  "Sinking is a comparison between two things, not a fact about one.",
  ["Whether something sinks depends on how its density compares with the liquid's.",
   "If the object is less dense than water it floats.",
   "If it has the same density it hovers, neither rising nor settling.",
   "So it sinks when it is more dense than water."],
  "**Is more dense than water.** It is always a comparison. A large mass is not enough on its own — "
  "a tree trunk has a huge mass and floats, because what matters is the mass compared with the "
  "space it fills.",
  "Denser than what it is sitting in — that is the whole rule.")

q(Q, 1, "True or false: if an object is buoyant, it sinks in water.",
  ["False", "True", "True, but only in salt water", "It depends on the object's mass"], 0,
  "Think about what the word buoyant is describing.",
  ["Buoyancy is the upward push a liquid gives an object.",
   "Calling something buoyant means that push is enough to hold it up.",
   "An object being held up is floating, not sinking.",
   "So the statement is false."],
  "**False.** Buoyant means it floats — buoyant and sinking are opposites. The upward push exists "
  "for sinking objects too; it is just not strong enough to hold them up.",
  "Buoyant describes something the liquid is winning against gravity with.")

q(Q, 2, "A sample is weighed in a dish. The dish and sample together read 47 g, and the empty dish "
        "on its own reads 12 g. What is the mass of the sample?",
  ["35 g", "59 g", "47 g", "12 g"], 0,
  "Part of what the scale is reading is not the thing you want to measure.",
  ["The scale reading of 47 g includes both the dish and the sample.",
   "The dish by itself accounts for 12 g of that.",
   "So the sample is 47 − 12.",
   "That is 35 g."],
  "**35 g.** The container is not part of what you are measuring, so subtract it. Adding the two "
  "would count the dish twice, and taking the 47 g as the answer counts it once too many.",
  "Weigh it all, then take the container back off.")

q(Q, 2, "Two boxes are the same size. One has eight particles spread out inside it; the other has "
        "twenty-four particles packed closely together. Which has the higher density, and why?",
  ["The one with twenty-four particles, because more mass is in the same volume",
   "The one with eight particles, because its particles can move more freely",
   "They are equal, because the two boxes are the same size",
   "It cannot be decided without knowing the temperature of each box"], 0,
  "The volume is the same for both, so only one thing can be making the difference.",
  ["Density is mass divided by volume.",
   "Both boxes have the same volume, so the volumes cancel out of the comparison.",
   "More particles means more mass.",
   "So the box with twenty-four particles has the higher density."],
  "**The one with twenty-four particles, because more mass is in the same volume.** When the "
  "volume is held equal, density comes down entirely to how much material is in there — which is "
  "why a picture of two boxes is enough to compare them without measuring anything.",
  "Equal volumes turn a density question into a counting question.")

q(Q, 2, "An object has a density of 0.6 g/cm³. Water has a density of 1 g/cm³. What happens when "
        "the object is placed in water?",
  ["It floats, because it is less dense than water",
   "It sinks, because its density is less than one",
   "It hovers halfway down, because 0.6 is close to 1",
   "It floats, but only if its mass is small"], 0,
  "Compare the two numbers, and remember which way round the rule goes.",
  ["Water's density is 1 g/cm³.",
   "The object's density is 0.6 g/cm³, which is less than 1.",
   "Less dense than the liquid means the object floats.",
   "So it floats, and the reason is the comparison with water."],
  "**It floats, because it is less dense than water.** Any density below 1 g/cm³ floats in water "
  "and any density above it sinks. The object's mass does not change that — mass is already "
  "accounted for inside the density.",
  "Under 1 floats, over 1 sinks — once you know water is 1.")

q(Q, 2, "A pan of soup is heated from below. What happens to the soup at the bottom of the pan?",
  ["It becomes less dense and rises", "It becomes more dense and rises",
   "It becomes less dense and sinks further", "It stays where it is until the whole pan is hot"], 0,
  "Two steps: what heating does to the density, then what that density does.",
  ["Heating makes the particles move faster and spread further apart.",
   "The same mass now fills more space, so the density goes down.",
   "Something less dense than the fluid around it moves upward.",
   "So the heated soup becomes less dense and rises."],
  "**It becomes less dense and rises.** This is the first half of convection. The soup that rises "
  "then cools away from the heat, becomes denser again and sinks back down — which is what keeps "
  "the whole pan circulating instead of only the bottom getting hot.",
  "Heat spreads particles out. Spread out means less dense, and less dense means up.")

q(Q, 2, "Convection happens because warm matter becomes ______ dense and rises, while cool matter "
        "becomes ______ dense and sinks.",
  ["less, more", "more, less", "less, less", "more, more"], 0,
  "Work out the warm half first, then the cool half must be its opposite.",
  ["Warming makes particles spread apart, so the same mass fills more space.",
   "More space for the same mass means a lower density — so warm matter is LESS dense, and rises.",
   "Cooling does the reverse: particles settle closer, so the density goes up.",
   "So it is less for warm, more for cool."],
  "**Less, more.** Warm is less dense and goes up; cool is more dense and comes down. If both "
  "blanks were the same word nothing would move at all, and it is the difference between the two "
  "that drives the whole current.",
  "Warm up, cool down. The densities have to be opposites or nothing circulates.")

q(Q, 2, "Which of these best explains why a steel ship floats even though steel is much denser "
        "than water?",
  ["The ship is mostly air, so the whole ship is less dense than water",
   "The ship's engines push it upward as it moves",
   "Steel becomes less dense once it is shaped into a hull",
   "The ship's paint stops water from soaking into the steel"], 0,
  "Think about what you would have to include to work out the density of the whole ship.",
  ["Floating depends on the density of the whole object, not the material it is made from.",
   "A ship's hull encloses an enormous amount of air.",
   "Air has a very low density, so averaging it with the steel brings the whole ship's density down.",
   "That average comes out below water's density, so the ship floats."],
  "**The ship is mostly air, so the whole ship is less dense than water.** Melt the same steel into "
  "a solid block and it sinks immediately — identical material, different volume, different density. "
  "This is the clearest demonstration that floating is about density and not about weight.",
  "Average the whole thing, air included. That is the density that decides it.")

q(Q, 3, "Put these four steps of a convection current in order, starting with the fluid nearest "
        "the heat.",
  ["The fluid is heated and spreads out, lowering its density",
   "Now less dense than its surroundings, it rises",
   "Away from the heat it cools, and its density goes back up",
   "Now denser than its surroundings, it sinks back down"], 0,
  "Follow one piece of fluid all the way around the loop.",
  ["Heating comes first — it is what changes the density.",
   "A lower density than its surroundings is what makes it rise.",
   "Once it is away from the heat source it loses that heat and gets denser again.",
   "Denser than its surroundings, it falls back toward the heat, and the loop starts over."],
  "**Heat, rise, cool, sink.** The loop only keeps going because each half undoes the other: "
  "whatever goes up cools, and whatever comes down gets warmed. Stop the heating and the current "
  "stops with it.",
  "It is a circle, so the interesting part is what makes each step lead to the next.",
  kind='order')

q(Q, 3, "An ice cube floats in a glass of water. What does that tell you about solid water "
        "compared with liquid water?",
  ["Solid water is less dense than liquid water",
   "Solid water is more dense than liquid water",
   "Solid water and liquid water have the same density",
   "Solid water has less mass than the liquid water around it"], 0,
  "Apply the floating rule to the ice, and remember what the ice and the water are made of.",
  ["Anything that floats is less dense than the liquid it is floating in.",
   "The ice cube is floating in liquid water.",
   "So the ice must be less dense than the liquid water.",
   "Since both are water, solid water is less dense than liquid water."],
  "**Solid water is less dense than liquid water.** This makes water unusual — almost every other "
  "substance is densest as a solid, and a solid piece of it would sink in its own liquid. Water's "
  "particles lock into a pattern with gaps when they freeze, so the same mass takes up more room.",
  "Floating is always a comparison, and here both sides of the comparison are the same substance.")

q(Q, 3, "Two objects are made of the same material. One is a solid block and the other has been "
        "shaped into a hollow bowl. Which statement is correct?",
  ["The bowl has a lower density than the block, because it encloses air",
   "Both have the same density, because they are made of the same material",
   "The block has a lower density, because it has no air inside it",
   "Neither has a density until it is placed in a liquid"], 0,
  "Ask what counts as part of the object when you measure its volume.",
  ["Density is the mass of the whole object divided by the volume of the whole object.",
   "The bowl encloses air, which adds volume without adding much mass.",
   "More volume for roughly the same mass means a lower density.",
   "So the bowl has the lower density of the two."],
  "**The bowl has a lower density than the block, because it encloses air.** The material's own "
  "density has not changed — but the density of the OBJECT has, because shaping it added volume. "
  "That is exactly how a steel ship manages to float.",
  "Same material, different shape, different object density. The shape is doing real work.")

q(Q, 3, "A student says: \"This rock is heavier than that sponge, so the rock is denser.\" What is "
        "wrong with the reasoning, even though the conclusion happens to be right?",
  ["Being heavier does not settle it — the volumes have to be compared too",
   "Nothing is wrong; heavier always means denser",
   "Rocks and sponges cannot be compared because they are different materials",
   "Density can only be compared between objects of the same mass"], 0,
  "Check whether the reasoning would still work on a different pair of objects.",
  ["Density is mass divided by volume, so both numbers matter.",
   "Knowing only that one object is heavier leaves the volume unknown.",
   "A huge sponge could easily be heavier than a tiny pebble while still being far less dense.",
   "So being heavier does not settle it — the volumes have to be compared too."],
  "**Being heavier does not settle it — the volumes have to be compared too.** The conclusion is "
  "right here only because a rock and a sponge of similar size really do differ that way. The "
  "reasoning would fail the moment the two objects were different sizes, which is why it is worth "
  "catching now.",
  "A right answer from wrong reasoning is still worth fixing — it will not survive the next question.")

q(Q, 3, "A sealed bag of air is pushed down to the bottom of a swimming pool and released. Predict "
        "what happens, and why.",
  ["It rises, because the air inside makes it much less dense than water",
   "It stays at the bottom, because the water above is pressing down on it",
   "It rises only until it reaches the middle, where the densities match",
   "It sinks further, because the bag adds mass without adding volume"], 0,
  "Work out the density of the whole bag, contents included.",
  ["The bag's density is its total mass divided by its total volume.",
   "Air has a very low mass for the space it fills.",
   "So the bag as a whole is far less dense than water.",
   "Less dense than the liquid it is in means it rises."],
  "**It rises, because the air inside makes it much less dense than water.** Depth does not change "
  "the comparison — the bag is less dense than water at the bottom of the pool just as it is near "
  "the top, so it keeps rising until it reaches the surface.",
  "Density decides the direction. Depth does not change which of the two is denser.")

SORT = {
 'id': 's1', 'title': 'In water: does it come up, or go down?',
 'a': 'Comes up to the top', 'b': 'Goes down to the bottom',
 'items': [
  {'t': 'A wooden spoon, density 0.6 g/cm³', 'k': 'a',
   'why': '0.6 is below water\'s 1 g/cm³, so it is less dense than water.'},
  {'t': 'A steel bolt, density 7.8 g/cm³', 'k': 'b',
   'why': 'Far above 1 g/cm³ — much more dense than the water around it.'},
  {'t': 'A candle made of wax, density 0.9 g/cm³', 'k': 'a',
   'why': 'Just under 1 g/cm³, so it only just stays up — but it does.'},
  {'t': 'A glass marble, density 2.5 g/cm³', 'k': 'b',
   'why': 'Two and a half times water\'s density.'},
  {'t': 'An ice cube', 'k': 'a',
   'why': 'Water is the odd one out: frozen, it is less dense than the liquid.'},
  {'t': 'A rubber eraser, density 1.3 g/cm³', 'k': 'b',
   'why': 'Above 1 g/cm³, even though it is small and light to hold.'},
  {'t': 'An empty plastic bottle with the cap screwed on', 'k': 'a',
   'why': 'It is mostly air, so the whole bottle is far less dense than water.'},
  {'t': 'The same plastic bottle filled to the top with sand', 'k': 'b',
   'why': 'Same bottle, but the sand replaced the air and pushed the density well past 1.'},
  {'t': 'A tree trunk weighing 200 kg', 'k': 'a',
   'why': 'Heavy is not the test — wood is less dense than water however big the piece is.'},
  {'t': 'A small metal paperclip', 'k': 'b',
   'why': 'Light is not the test either — metal is denser than water at any size.'},
  {'t': 'A beach ball pushed under and let go', 'k': 'a',
   'why': 'Almost entirely air, so its density is a tiny fraction of water\'s.'},
  {'t': 'A solid block of the same steel a ship is built from', 'k': 'b',
   'why': 'With no air enclosed, the steel\'s own density is all that counts.'},
 ]
}

build('wayfinder', C, Q, 'unit-sci-dens',
      'Chemistry · 3 Density and Buoyancy', 'science',

      "Her Density/Buoyancy lesson check, covered end to end: what density compares, reading it "
      "off how tightly particles are packed, ranking the phases of matter by density, finding a "
      "mass on a scale by subtracting the container, the volume of a rectangular prism, the "
      "float-or-sink rule against water, what buoyant means, and convection — why warm fluid "
      "rises and cool fluid sinks.",

      "Density is the idea that makes the phases of matter click into place rather than being "
      "three words to memorize, and it is the same reasoning behind weather, ocean currents and "
      "why a boat made of metal does not go straight to the bottom.",

      [("Say which two properties density compares, and work a density out from a mass and a volume.",
        'source'),
       ("Rank solid, liquid and gas by density, and explain the ranking from how the particles sit.",
        'source'),
       ("Find a mass on a scale by subtracting the container, and a volume by multiplying all three "
        "sides.", 'source'),
       ("Predict whether something floats or sinks by comparing its density with water's.", 'source'),
       ("Explain convection as warm fluid rising and cool fluid sinking, and say why the loop keeps "
        "going.", 'source'),
       ("Explain why a steel ship floats, using the density of the whole object rather than the "
        "material.", 'added')],

      "Built from her own completed Density/Buoyancy lesson check.\n\n"
      "FIRST, THE GOOD NEWS: she got 20 out of 20. It is marked A+ in pen and every one of the "
      "twenty is ticked, including the trickier ones — subtracting the container to find the mass "
      "of the candy (she wrote the 29 − 15 out by hand), ranking the phases by density, and both "
      "of the float-or-sink questions that give a number and expect her to compare it with water "
      "without being told water's density. So unlike the last two science sheets, there is nothing "
      "here to repair. This unit exists to keep the material fresh for the test rather than to fix "
      "anything.\n\n"
      "TWO THINGS THE SHEET LEANS ON WITHOUT EVER SAYING, and both are added here as cards "
      "flagged as ours rather than her class's. The paper asks which two properties density "
      "compares but never gives the formula, so 'density = mass ÷ volume' is spelled out. And "
      "questions 14 and 15 hand her 0.32 g/cm³ and 1.7 g/cm³ and ask float or sink, which cannot "
      "be answered without knowing water is 1 g/cm³ — a number that appears nowhere on the paper. "
      "She clearly knows both already; they are here so the reasoning is written down somewhere "
      "rather than carried in her head.\n\n"
      "One extension worth knowing about: the unit teaches that water is the exception to the "
      "solid-liquid-gas density order, because ice floats. Her question 5 says 'a typical "
      "substance', which deliberately leaves room for that — so this builds on the sheet rather "
      "than contradicting it.\n\n"
      "SHELVING: this lands as part 3 of Chemistry, behind Phases of Matter and Phase Changes, "
      "because the sheet's own question 5 asks her to rank the phases by density — density is "
      "being used as a property of the phases she just studied. The Drive file sits loose in "
      "Science rather than in a numbered unit folder, so there was no folder name to follow. If "
      "her teacher numbers it as its own unit, it is a retitle keeping the id.",

      ("Start with the cards — the float-or-sink rule and the density of water are the pair that "
       "make every other question on this topic answerable.", 20),
      'content/science-density-buoyancy.json',
      'density and buoyancy.pdf (Science 4 · Density/Buoyancy lesson check, Drive)',
      'source', offset_hours=3)

# sorts + libv are not part of build()'s schema; patch them in.
p = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'wayfinder/content/science-density-buoyancy.json')
if not os.path.exists(p):
    p = '/home/user/wayfinder/content/science-density-buoyancy.json'
j = json.load(io.open(p, encoding='utf-8'))
u = j['records']['unit-sci-dens']
u['sorts'] = [SORT]
u['libv'] = 1
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + sort set "%s" (%d items), libv 1' % (SORT['title'], len(SORT['items'])))
