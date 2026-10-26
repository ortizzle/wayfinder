#!/usr/bin/env python3
"""Chemistry · 4 Molecules and Compounds.

Source: "molecules and compounds.pdf", her completed Science 4 lesson check
(24 points, one page), uploaded to Drive on 2026-10-13. It is a photo of the
paper with no text layer, so it was rendered with pypdfium2 and read as an
image. It asks one thing twelve times: circle each substance as atom, element,
molecule or compound, and "each one has TWO answers". The twelve are Na, H2,
W, K2S, NaOH, N2, Al, B, CaSO4, NaCl, Mg and H2O. Twelve items at two marks
each make the 24 points, so the one page is the whole sheet.

Per the standing rule (Chris, 2026-09-27) the sheet was read for WHAT IT ASKS.
Her marks on it are not graded, summarised or recorded anywhere.

THE PAIRING RULE is the whole lesson, and it is computed, not typed: pair()
reads a formula's capital letters (kinds of element) and subscripts (atoms),
and every pair a question claims is asserted against it.

THE IONIC NUANCE. NaCl, NaOH, K2S and CaSO4 are ionic. A chemist would not
strictly call them molecules, but a sheet that says every item has TWO answers
can only mean "molecule and compound" for them. The unit teaches the class's
framing (a compound is atoms joined, so at this level it pairs with molecule).
No graded question's answer turns on the ionic distinction: every compound in
a graded pair question is molecular (CO2, CH4, NH3, H2O2). The nuance is one
line in the parentNote, for later grades.

READING A FORMULA is something the sheet expects and never explains, so the two
formula-reading cards are flagged 'added', the same call build_density.py made
for the density formula.
"""
import io, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

SUBS = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
def F(f):
    """ASCII formula -> the subscripted form she reads."""
    return f.translate(SUBS)

def parse(f):
    """{element: atom count} for a simple formula (no brackets needed here)."""
    out = {}
    for el, n in re.findall(r'([A-Z][a-z]?)(\d*)', f):
        out[el] = out.get(el, 0) + (int(n) if n else 1)
    return out

def atoms(f): return sum(parse(f).values())
def kinds(f): return len(parse(f))

PAIRS = ('Atom and element', 'Element and molecule', 'Molecule and compound')
WRONG = 'Element and compound'   # cannot both be true of one substance
def pair(f):
    if kinds(f) > 1: return PAIRS[2]
    return PAIRS[0] if atoms(f) == 1 else PAIRS[1]

# The sheet's own twelve, checked against the rule so the example cards are right.
for f in ('Na', 'W', 'Al', 'B', 'Mg'): assert pair(f) == PAIRS[0], f
for f in ('H2', 'N2'): assert pair(f) == PAIRS[1], f
for f in ('K2S', 'NaOH', 'CaSO4', 'NaCl', 'H2O'): assert pair(f) == PAIRS[2], f
# Counts written into cards and questions.
assert (atoms('H2O'), kinds('H2O')) == (3, 2)
assert (atoms('CaSO4'), kinds('CaSO4')) == (6, 3)
assert (atoms('NH3'), kinds('NH3')) == (4, 2)
assert (atoms('C6H12O6'), kinds('C6H12O6')) == (24, 3)
assert (atoms('O3'), kinds('O3')) == (3, 1)
assert kinds('Co') == 1 and kinds('CO') == 2

def pair_opts(f):
    """The three real pairs plus the one impossible one; the right pair is computed."""
    o = list(PAIRS) + [WRONG]
    return o, o.index(pair(f))

C, Q = [], []

# ------------------------------------------------------------------ cards

card(C, 'Atom',
     "**The smallest piece of an element that is still that element.**\n"
     "• One single particle, on its own\n"
     "• Cut a piece of aluminum in half again and again, and the last piece that is "
     "still aluminum is one aluminum atom",
     hint="Atom is the one. One particle, nothing joined to it.")

card(C, 'Element',
     "**A substance made of only ONE kind of atom.**\n"
     "• It can be single atoms, like Na (sodium) or W (tungsten)\n"
     "• Or atoms of that one kind joined together, like H₂ (hydrogen gas)\n"
     "• Every element has its own symbol and its own box on the periodic table",
     hint="One kind. However many atoms there are, they are all the same.")

card(C, 'Molecule',
     "**Two or more atoms joined together.**\n"
     "• The atoms can be the SAME kind, like the two hydrogens in H₂\n"
     "• Or DIFFERENT kinds, like the hydrogens and oxygen in H₂O\n"
     "• A single atom on its own is never a molecule",
     hint="Molecule means joined. At least two atoms, holding on to each other.")

card(C, 'Compound',
     "**Two or more DIFFERENT elements joined together.**\n"
     "• Water, H₂O, is hydrogen and oxygen joined\n"
     "• If every atom in it is the same kind, it is not a compound, however many atoms there are",
     hint="Compound means a combination of different kinds.")

card(C, 'Every substance gets two words',
     "**One atom alone: atom and element. Same kind joined: element and molecule. "
     "Different kinds joined: molecule and compound.**\n"
     "• First ask: is it one atom, or are atoms joined?\n"
     "• Then ask: is there one kind of atom, or more than one?\n"
     "• Those two answers always give you the pair",
     hint="Two questions, two words. How many atoms, then how many kinds.")

card(C, 'Atom and element',
     "**A symbol with no small number after it, standing on its own.**\n"
     "• Na (sodium), W (tungsten), Al (aluminum), B (boron), Mg (magnesium)\n"
     "• One atom, so it is an atom; one kind, so it is an element",
     hint="Just a symbol, nothing joined. The easiest pair to spot.")

card(C, 'Element and molecule',
     "**One kind of atom, with more than one of them joined.**\n"
     "• H₂ (hydrogen gas) and N₂ (nitrogen gas)\n"
     "• Joined, so it is a molecule; all one kind, so it is still an element",
     hint="One capital letter and a small number after it.")

card(C, 'Molecule and compound',
     "**Different kinds of atom, joined.**\n"
     "• H₂O (water), NaCl (table salt), K₂S, NaOH, CaSO₄\n"
     "• Joined, so it is a molecule; more than one kind, so it is a compound",
     hint="Two or more capital letters means two or more kinds.")

card(C, 'Every compound is a molecule, not the other way round',
     "**Every compound is a molecule, but not every molecule is a compound.**\n"
     "• A compound is atoms joined, so it is always a molecule too\n"
     "• H₂ is a molecule, but both atoms are hydrogen, so it is not a compound",
     hint="Compound is the pickier word. It needs joined AND different.")

card(C, 'Capital letters count the elements',
     "**Every capital letter in a formula starts a new element.**\n"
     "• A small letter belongs to the capital in front of it: Na is ONE element, sodium\n"
     "• NaOH has three capitals, N, O and H, so three elements: sodium, oxygen, hydrogen\n"
     "• Count the capitals and you know how many kinds of atom there are",
     hint="Big letter, new element. Small letter, same element.",
     frm='added')

card(C, 'Small numbers count the atoms',
     "**A small number after a symbol tells you how many atoms of that element there are.**\n"
     "• No number means one\n"
     "• H₂O is 2 hydrogen + 1 oxygen = 3 atoms\n"
     "• CaSO₄ is 1 calcium + 1 sulfur + 4 oxygen = 6 atoms, of 3 kinds",
     hint="The little number belongs to the letter just before it.",
     frm='added')

card(C, 'Co and CO are different',
     "**Co is cobalt, one element. CO is carbon monoxide, two elements joined.**\n"
     "• Co has one capital, so it is one element\n"
     "• CO has two capitals, C for carbon and O for oxygen\n"
     "• This is why a second letter is always written small",
     hint="Count the capitals. That one detail changes the whole substance.",
     frm='added')

card(C, 'Elements that come in pairs',
     "**Some elements are found as two atoms joined: hydrogen, nitrogen, oxygen and chlorine.**\n"
     "• Written H₂, N₂, O₂ and Cl₂\n"
     "• They are molecules, but still elements, because both atoms are the same kind",
     hint="Two of the same is still one kind.",
     frm='added')

card(C, 'A compound is something new',
     "**A compound behaves completely differently from the elements it is made of.**\n"
     "• Sodium is a soft metal that reacts wildly with water; chlorine is a poisonous gas\n"
     "• Joined, they make table salt, which you sprinkle on food\n"
     "• Water is made of two gases, hydrogen and oxygen, and it is a liquid",
     hint="Joined elements do not keep their old personalities.",
     frm='added')

card(C, 'Symbols that do not match the name',
     "**Some symbols come from an older name for the element.**\n"
     "• Na is sodium, from its Latin name natrium\n"
     "• K is potassium (kalium), Fe is iron (ferrum)\n"
     "• W is tungsten, from its other name, wolfram",
     hint="If the letters do not fit the English name, the name is older than English.",
     frm='added')

# -------------------------------------------------------------- questions
LV1, LV2, LV3 = 1, 2, 3

q(Q, LV1, "What is an atom?",
  ["The smallest piece of an element that is still that element",
   "Two or more atoms of different kinds joined together",
   "A mixture of several substances stirred into one container",
   "Any substance that has a small number written in its formula"], 0,
  "Think of the very last piece you could cut off and still have the same stuff.",
  ["An atom is a single particle.",
   "It is the smallest piece that is still that element.",
   "Atoms joined together are a molecule, not an atom.",
   "So an atom is the smallest piece of an element that is still that element."],
  "**The smallest piece of an element that is still that element.** Atoms joined together "
  "make a molecule, and different kinds joined make a compound. An atom is the single "
  "particle all of those are built from.",
  "Atom is the one. Everything else in this lesson is atoms joined.")

q(Q, LV1, "What do you call a substance that is made of only ONE kind of atom?",
  ["An element", "A compound", "A mixture", "A solution"], 0,
  "It is the word that each box on the periodic table stands for.",
  ["The substance has only one kind of atom in it.",
   "A compound needs at least two different kinds, so it is not that.",
   "A mixture and a solution both mean several substances stirred together.",
   "A substance of only one kind of atom is an element."],
  "**An element.** It does not matter how many atoms there are. Hydrogen gas has two atoms "
  "joined, and it is still an element because both are hydrogen.",
  "One kind of atom, one element.")

q(Q, LV1, "What do you call two or more DIFFERENT elements joined together?",
  ["A compound", "An element", "An atom", "A mixture"], 0,
  "The word means a combination of different kinds.",
  ["The atoms are joined, so this is not a loose mixture.",
   "They are different kinds, so it is not a single element.",
   "It is more than one atom, so it is not an atom.",
   "Different elements joined together make a compound."],
  "**A compound.** Water is the most famous one: hydrogen and oxygen joined. A mixture is "
  "different, because its parts are only stirred together and can be separated again without "
  "breaking anything apart.",
  "Joined and different. Both have to be true.")

q(Q, LV1, "In a chemical formula, what does a small number after a symbol tell you?",
  ["How many atoms of that element there are",
   "How many different elements are in the substance",
   "How heavy one atom of that element is",
   "Which row of the periodic table the element is in"], 0,
  "Look at H₂O. What is there two of?",
  ["In H₂O the small 2 sits after the H.",
   "It means there are two hydrogen atoms.",
   "The O has no number, so there is one oxygen atom.",
   "So the small number counts the atoms of the element just before it."],
  "**How many atoms of that element there are.** The number of different elements comes from "
  "counting the capital letters instead. No small number at all means there is just one atom.",
  "The little number belongs to the letter in front of it.", frm='added')

f = 'He'; o, a = pair_opts(f)
q(Q, LV1, "Helium is written %s. Which two words describe it?" % F(f), o, a,
  "Is there anything joined to it?",
  ["%s is one symbol with no small number after it." % F(f),
   "So it is a single atom, with nothing joined to it.",
   "Only one kind of atom is there, so it is an element.",
   "One atom, one kind: atom and element."],
  "**Atom and element.** A single atom on its own is always both. It cannot be a molecule, "
  "because nothing is joined to it, and it cannot be a compound, because there is only one kind.",
  "Just a symbol, nothing joined: atom and element.")

f = 'O2'; o, a = pair_opts(f)
q(Q, LV1, "The oxygen you breathe is written %s. Which two words describe it?" % F(f), o, a,
  "Count the atoms, then count the kinds.",
  ["The small 2 means two oxygen atoms.",
   "Two atoms joined together make a molecule.",
   "Both atoms are oxygen, so there is only one kind.",
   "One kind of atom means it is an element: element and molecule."],
  "**Element and molecule.** It is joined, so it is a molecule. But both atoms are oxygen, so "
  "it is still an element, not a compound.",
  "Two of the same is still one kind.")

f = 'CO2'; o, a = pair_opts(f)
q(Q, LV1, "Carbon dioxide is written %s. Which two words describe it?" % F(f), o, a,
  "How many capital letters are there?",
  ["C and O are two capital letters, so there are two elements: carbon and oxygen.",
   "The atoms are joined, so it is a molecule.",
   "Different elements joined together make a compound.",
   "So it is a molecule and a compound."],
  "**Molecule and compound.** Carbon and oxygen are two different elements, joined. That makes "
  "it a compound, and every compound is a molecule too.",
  "Two capitals, two kinds. Different kinds joined is a compound.")

f = 'Fe'; o, a = pair_opts(f)
q(Q, LV2, "Iron is written %s. Which two words describe it?" % F(f), o, a,
  "One letter is a capital and one is small. What does that mean?",
  ["%s has one capital letter, F, so it is one element." % F(f),
   "The small e belongs to the F; it is not a second element.",
   "There is no small number, so it is one atom.",
   "One atom, one kind: atom and element."],
  "**Atom and element.** Two letters do not mean two elements. Only a capital letter starts a "
  "new element, and the small e is part of iron's symbol.",
  "Count capitals, not letters.")

f = 'Cl2'; o, a = pair_opts(f)
q(Q, LV2, "Chlorine gas is written %s. Which two words describe it?" % F(f), o, a,
  "Two letters, one capital, then a small number.",
  ["Cl has one capital, so it is one element: chlorine.",
   "The small 2 means two chlorine atoms.",
   "Two atoms joined make a molecule.",
   "Both are chlorine, so it stays an element: element and molecule."],
  "**Element and molecule.** Chlorine is one of the elements found as joined pairs, like "
  "hydrogen, nitrogen and oxygen. Joined makes it a molecule, but one kind keeps it an element.",
  "One capital and a small number: element and molecule.")

f = 'CH4'; o, a = pair_opts(f)
q(Q, LV2, "Methane, the gas burned on a kitchen stove, is written %s. Which two words describe it?"
  % F(f), o, a,
  "How many capital letters, and are the atoms joined?",
  ["C and H are two capitals, so two elements: carbon and hydrogen.",
   "The 4 means four hydrogen atoms, joined to the carbon.",
   "Atoms joined make a molecule.",
   "Different elements joined make a compound: molecule and compound."],
  "**Molecule and compound.** It has %d atoms of %d kinds. The number of atoms does not decide "
  "it; the number of KINDS does." % (atoms('CH4'), kinds('CH4')),
  "Two capitals is enough to make a compound.")

n = atoms('NH3')
q(Q, LV2, "Ammonia is written %s. How many atoms are in one molecule of it?" % F('NH3'),
  [str(n), str(n - 1), str(kinds('NH3')), str(n + 1)], 0,
  "Count every atom, including the ones with no number.",
  ["N has no small number, so there is 1 nitrogen atom.",
   "H has a 3 after it, so there are 3 hydrogen atoms.",
   "1 + 3 = %d." % n,
   "So one molecule has %d atoms." % n],
  "**%d.** One nitrogen and three hydrogen. Answering 3 forgets the nitrogen, because it has no "
  "number written after it, and answering 2 counts the kinds of element instead of the atoms."
  % n,
  "No number means one. It still counts.", frm='added')

f = 'C6H12O6'
q(Q, LV2, "Sugar (glucose) is written %s. How many different ELEMENTS are in it?" % F(f),
  [str(kinds(f)), str(atoms(f)), '6', '12'], 0,
  "The question asks for kinds of atom, not how many atoms.",
  ["Count the capital letters: C, H and O.",
   "Each capital starts a new element: carbon, hydrogen and oxygen.",
   "The small numbers count atoms, which is a different question.",
   "So there are %d elements." % kinds(f)],
  "**%d.** Carbon, hydrogen and oxygen. There are %d atoms in all, but that answers how many "
  "atoms, not how many kinds." % (kinds(f), atoms(f)),
  "Elements: count the capitals. Atoms: add the numbers.", frm='added')

q(Q, LV2, "Co is cobalt and CO is carbon monoxide. Which one is a compound, and why?",
  ["CO, because its two capital letters are two different elements",
   "Co, because its two letters stand for two different elements",
   "Both, because each one is written with exactly two letters",
   "Neither, because a compound always needs a small number"], 0,
  "Look at which letters are capitals.",
  ["Co has one capital, C, and a small o that belongs to it.",
   "So Co is one element, cobalt.",
   "CO has two capitals, C for carbon and O for oxygen.",
   "Two different elements joined make a compound, so CO is the compound."],
  "**CO, because its two capital letters are two different elements.** Co is a single element, "
  "cobalt. A compound does not need a small number either: CO has one carbon and one oxygen, "
  "and that is enough.",
  "Capitals count elements. The size of a letter changes the whole substance.", frm='added')

q(Q, LV2, "Which statement is true?",
  ["Every compound is a molecule, but not every molecule is a compound",
   "Every molecule is a compound, but not every compound is a molecule",
   "A molecule and a compound always mean exactly the same thing",
   "A substance can never be both a molecule and a compound"], 0,
  "Test each statement against H₂, which is two hydrogen atoms joined.",
  ["A compound is different elements joined, so its atoms are joined: it is a molecule.",
   "H₂ is atoms joined, so it is a molecule.",
   "But both of its atoms are hydrogen, so it is not a compound.",
   "So every compound is a molecule, but not every molecule is a compound."],
  "**Every compound is a molecule, but not every molecule is a compound.** H₂ is the example "
  "that proves it: a molecule made of one kind of atom, so it is not a compound.",
  "Compound is the pickier word. It needs joined AND different.")

f = 'O3'; o, a = pair_opts(f)
q(Q, LV3, "Ozone, a gas high in the sky, is written %s. It has three atoms. Which two words "
          "describe it?" % F(f), o, a,
  "Three atoms is a lot. Does that make it a compound?",
  ["The small 3 means three oxygen atoms, joined.",
   "Atoms joined make a molecule.",
   "All three are oxygen, so there is only one kind of atom.",
   "One kind means it is an element, not a compound: element and molecule."],
  "**Element and molecule.** The number of atoms never makes something a compound. Only "
  "different KINDS do, and every atom in ozone is oxygen.",
  "More atoms is not more kinds.")

q(Q, LV3, "Someone says hydrogen gas, H₂, is a compound because it has two atoms. What is wrong "
          "with that?",
  ["Both atoms are hydrogen, and a compound needs different elements",
   "Nothing is wrong; any substance with two atoms is a compound",
   "H₂ is a single atom, so it cannot be joined to anything",
   "A compound needs at least three atoms, and H₂ only has two"], 0,
  "Two atoms tells you it is joined. What else does a compound need?",
  ["H₂ has two atoms joined, so it is a molecule.",
   "A compound needs two or more DIFFERENT elements.",
   "Both of H₂'s atoms are hydrogen, one kind.",
   "So it is an element and a molecule, not a compound."],
  "**Both atoms are hydrogen, and a compound needs different elements.** Two atoms joined only "
  "makes a molecule. Water, H₂O, is a compound because oxygen joins the hydrogen.",
  "Joined makes a molecule. Different makes a compound.")

ORDER = ['He', 'O2', 'H2O', 'CH4']
assert [atoms(f) for f in ORDER] == sorted(atoms(f) for f in ORDER) == [1, 2, 3, 5]
q(Q, LV3, "Put these in order from FEWEST atoms to MOST atoms.",
  ["He (helium)", F('O2') + " (oxygen gas)",
   F('H2O') + " (water)", F('CH4') + " (methane)"], 0,
  "Add up the small numbers, and count a symbol with no number as one.",
  ["He has no number: 1 atom.",
   "O₂ has a 2: 2 atoms.",
   "H₂O is 2 hydrogen + 1 oxygen: 3 atoms.",
   "CH₄ is 1 carbon + 4 hydrogen: 5 atoms."],
  "**He, O₂, H₂O, CH₄: 1, 2, 3 and 5 atoms.** Count every symbol, and count a symbol with no "
  "small number after it as one.",
  "No number means one. Then add.", kind='order')

q(Q, LV3, "Sodium is a soft metal that reacts wildly with water. Chlorine is a poisonous gas. "
          "Joined, they make table salt, which is safe to eat. What does this show?",
  ["A compound has its own properties, different from the elements in it",
   "A compound keeps all the properties of the elements in it",
   "Table salt must be a mixture, because its elements can be tasted",
   "Elements only change when they are melted down together"], 0,
  "Compare what salt is like with what sodium and chlorine are like.",
  ["Sodium is a dangerous metal on its own.",
   "Chlorine is a poisonous gas on its own.",
   "Salt is neither: it is a safe white solid.",
   "So joining elements makes something with new properties of its own."],
  "**A compound has its own properties, different from the elements in it.** That is the big "
  "difference between a compound and a mixture. Stir sand and iron filings together and each "
  "keeps acting the way it always did; join sodium and chlorine and you get something new.",
  "Joined elements make something new.", frm='added')

q(Q, LV3, "Which of these formulas CANNOT be a compound?",
  [F('S8'), F('HCl'), F('NO2'), F('CO')], 0,
  "A compound needs at least two different elements. Count the capitals in each.",
  ["S₈ has one capital, S, so it has one element: sulfur.",
   "HCl has two capitals, H and C: hydrogen and chlorine.",
   "NO₂ has N and O, and CO has C and O.",
   "Only S₈ has a single kind of atom, so it cannot be a compound."],
  "**%s.** It has eight atoms, but they are all sulfur, so it is an element and a molecule. "
  "Each of the others has two capital letters, so two elements joined." % F('S8'),
  "A big number does not make a compound. A second capital does.")

assert kinds('S8') == 1 and all(kinds(f) == 2 for f in ('HCl', 'NO2', 'CO'))

f = 'H2O2'; o, a = pair_opts(f)
q(Q, LV3, "Hydrogen peroxide, used to clean a cut, is written %s. Which two words describe it?"
  % F(f), o, a,
  "It has the same two letters as water. Count the kinds of atom.",
  ["H and O are two capitals, so two elements: hydrogen and oxygen.",
   "The atoms are joined, so it is a molecule.",
   "Different elements joined make a compound.",
   "So it is a molecule and a compound, just like water."],
  "**Molecule and compound.** It has one more oxygen than water, which makes it a different "
  "substance, but it is still two kinds of atom joined.",
  "Different numbers, different substance. Same kinds, same pair of words.")

# ------------------------------------------------------------------- sort
SORT_ITEMS = [
  ('O2', 'oxygen gas', 'a', 'Two atoms, but both oxygen: one kind.'),
  ('CO2', 'carbon dioxide', 'b', 'Two capitals, carbon and oxygen: two kinds joined.'),
  ('Fe', 'iron', 'a', 'One capital, F. The small e belongs to it.'),
  ('CH4', 'methane', 'b', 'Carbon and hydrogen: two kinds joined.'),
  ('He', 'helium', 'a', 'One atom, one kind.'),
  ('NH3', 'ammonia', 'b', 'Nitrogen and hydrogen: two kinds joined.'),
  ('O3', 'ozone', 'a', 'Three atoms, but every one is oxygen.'),
  ('C6H12O6', 'sugar', 'b', 'Carbon, hydrogen and oxygen: three kinds joined.'),
  ('Co', 'cobalt', 'a', 'One capital, C, with a small o. One kind of atom.'),
  ('CO', 'carbon monoxide', 'b', 'Two capitals, C and O: carbon and oxygen joined.'),
  ('Cl2', 'chlorine gas', 'a', 'Two chlorine atoms joined are still only chlorine.'),
  ('H2O2', 'hydrogen peroxide', 'b', 'Hydrogen and oxygen, the same two kinds as water.'),
]
for f, _, k, _w in SORT_ITEMS:
    assert (kinds(f) > 1) == (k == 'b'), f
SORT = {
  'id': 's1', 'title': 'One kind of atom, or different kinds joined?',
  'a': 'Element', 'b': 'Compound',
  'items': [{'t': '%s (%s)' % (F(f), name), 'k': k, 'why': w} for f, name, k, w in SORT_ITEMS],
}

build('wayfinder', C, Q, 'unit-sci-molcomp',
      'Unit 1 · 1.2 Molecules and Compounds', 'science',

      "The four words for what a substance is made of, and how they pair: an atom is one "
      "particle, an element is one kind of atom, a molecule is atoms joined, and a compound is "
      "different elements joined. Every substance gets two of the four. Also how to read a "
      "chemical formula: capital letters count the elements, small numbers count the atoms.",

      "These four words are how chemists describe everything there is, and they are the "
      "groundwork for the periodic table. Once you can read a formula, H₂O stops being a code "
      "and starts saying exactly what is inside it.",

      [("Say what an atom, an element, a molecule and a compound are.", 'source'),
       ("Name the two words that describe a substance, from its formula.", 'source'),
       ("Count the elements in a formula from its capital letters.", 'added'),
       ("Count the atoms in a formula from its small numbers.", 'added'),
       ("Explain why every compound is a molecule but not every molecule is a compound.",
        'source')],

      "Built from the completed Molecules and Compounds lesson check (one page, twelve "
      "substances, each with two answers).\n\n"
      "It was read for the QUESTIONS it asks, not to mark the answers, so nothing here is a "
      "correction and nothing about how it went is recorded anywhere. The unit covers the one "
      "skill the paper tests twelve times: naming the two words that fit a substance. Its own "
      "twelve substances appear on the cards as examples; the graded questions use fresh ones "
      "(He, O₂, CO₂, Fe, Cl₂, CH₄, O₃, H₂O₂ and others).\n\n"
      "ONE THING THE SHEET LEANS ON WITHOUT SAYING, added here as cards flagged as ours rather "
      "than the class's: how to read a formula. The paper expects her to know that NaOH is three "
      "elements and H₂ is one, but never says that capital letters count elements and small "
      "numbers count atoms.\n\n"
      "A NUANCE FOR LATER GRADES: NaCl, NaOH, K₂S and CaSO₄ are ionic compounds, and a chemist "
      "would not strictly call them molecules. The sheet says every item has two answers, so "
      "its framing is molecule and compound, and the unit teaches that. No graded question "
      "depends on the difference.\n\n"
      "SHELVING: part 4 of Chemistry, after Density and Buoyancy. The Drive file sits loose in "
      "Science, like the density sheet, so there was no unit folder to follow. No periodic-table "
      "material for her class was found in Drive yet.",

      ("Start with the card that gives every substance two words. Two questions decide the "
       "pair: how many atoms, then how many kinds.", 15),
      'content/science-molecules-compounds.json',
      'molecules and compounds.pdf (Science 4 · Molecules and Compounds lesson check, Drive)',
      'source', offset_hours=3)

p = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                 'content/science-molecules-compounds.json')
j = json.load(io.open(p, encoding='utf-8'))
u = j['records']['unit-sci-molcomp']
u['sorts'] = [SORT]
u['libv'] = 2
u['order'] = 9   # v195: Unit 1.2 on the one science Unit 1 shelf
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + sort set "%s" (%d items), libv 2' % (SORT['title'], len(SORT['items'])))
