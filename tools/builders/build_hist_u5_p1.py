#!/usr/bin/env python3
"""Unit 5 · 1 Features, Maps and Directions  (Wayfinder / History 4)

Source: "Unit 5 - History.pdf" (Drive, History folder) — her class's OPTIONAL
Unit 5 Test Study Guide, 33 items over seven sections. The PDF is an
image-only scan with no text layer at all, so it was rendered with pypdfium2
and read page by page as images; nothing came through Drive's extractor.

The guide is BLANK — she has not filled it in — so unlike the two science
sheets there are no answers of hers to check and nothing of hers to repair.
This is coverage: teach the material so she can fill the guide in herself,
which is what its own directions ask her to do.

SCOPE, decided before a word was written (the v142/v189 discipline).
`unit-az-latlong` already teaches section 5 of this guide thoroughly —
latitude, longitude, the equator, the Prime Meridian, reading a coordinate
pair, hemispheres, comparing and estimating on this exact US Bingo map, which
is page 7 of this very PDF. None of it is repeated here. It is retitled onto
the same Unit 5 shelf as part 2 instead.

This file is guide sections 1-4 (items 1-19): natural and human features,
the four types of map, the compass rose, and letter/number grid maps.

Every scenario is FRESH. The guide's own examples (Old Faithful, Lake
Michigan, Chandler, the prime meridian, the ancestry/provinces/elevation/
fast-food maps, Shanghai, New Orleans, the St. Joseph street map) are her
homework; a graded question she can answer from memory of the page tests
nothing. They appear on CARDS where they are useful reference, never as the
graded item.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

C, Q = [], []

# ---------------------------------------------------------------- features
card(C, 'Natural feature',
     "**A feature of the earth's surface that people did NOT make.**\n"
     "• Mountains, rivers, lakes, deserts, canyons, geysers, oceans\n"
     "• It would still be there if nobody had ever lived nearby\n"
     "• The test wording is \"not created by human beings\"",
     hint='Nature built it. Nobody had to.')
card(C, 'Human feature',
     "**A feature of the earth's surface that human beings created.**\n"
     "• Cities, roads, bridges, dams, farms, borders between countries\n"
     "• If every person vanished, it would not have been built in the first place\n"
     "• The test wording is \"created by human beings\"",
     hint='Somebody had to build it or decide it.')
card(C, 'The trap: a line nobody can see',
     "**The equator, the Prime Meridian and every border are HUMAN features, "
     "even though you cannot touch them.**\n"
     "• People agreed where to draw them; the earth has no line painted on it\n"
     "• A river can be a border — the river is natural, the border is human\n"
     "• \"Natural\" does not mean \"invisible\", it means nobody decided it",
     hint='Did a person decide where it goes? Then a person made it.',
     frm='added')
card(C, 'A city is a human feature, the land under it is not',
     "**The buildings and streets are human; the hill, river or bay they sit on "
     "is natural.**\n"
     "• Naming a city names the human feature\n"
     "• Naming the valley the city sits in names the natural one",
     hint='The place is natural. What got built on it is not.',
     frm='added')

# ---------------------------------------------------------------- map types
card(C, 'Physical map',
     "**Shows the NATURAL features of the earth.**\n"
     "• Mountains, rivers, lakes, deserts, and how high the land is\n"
     "• Usually coloured by elevation rather than by country",
     hint='Physical = the physical earth, the part people did not make.')
card(C, 'Political map',
     "**Shows the HUMAN features of the earth.**\n"
     "• Countries, states, provinces, cities and the borders between them\n"
     "• Usually coloured one flat colour per country or state",
     hint='Politics is about people and who is in charge of where.')
card(C, 'Climate map',
     "**Shows the permanent weather conditions of a given area.**\n"
     "• Climate is what the weather is USUALLY like over many years\n"
     "• Not today's forecast — a rainy Tuesday does not change a climate map",
     hint='Weather is this week. Climate is always.')
card(C, 'Cultural map',
     "**Shows behaviors of a country or region's populations.**\n"
     "• What people there speak, believe, eat, or where their families came from\n"
     "• Anything about how the PEOPLE live rather than where things are",
     hint='Culture is what the people do.')
card(C, 'Telling them apart in one question',
     "**Ask what the map is really about: the land, the borders, the weather, "
     "or the people.**\n"
     "• The land → physical\n• The borders → political\n"
     "• The usual weather → climate\n• The people → cultural\n"
     "• Every map on the test fits exactly one of those four",
     hint='Land, borders, weather, people.',
     frm='added')

# ---------------------------------------------------------------- compass
card(C, 'Compass rose',
     "**The little cross on a map that tells you which way is north.**\n"
     "• On most maps north is up, but the compass rose is what makes it certain\n"
     "• Always find it before you answer a direction question",
     hint='It is the map telling you which way it is facing.')
card(C, 'Cardinal directions',
     "**The four main directions: north, south, east and west.**\n"
     "• North is toward the North Pole, south toward the South Pole\n"
     "• Facing north, east is on your right and west is on your left",
     hint='The four points of the compass rose.')
card(C, 'Intermediate directions',
     "**The four in-between directions: northeast, northwest, southeast and "
     "southwest.**\n"
     "• Each one is halfway between two cardinal directions\n"
     "• Northeast means up AND right on a north-is-up map\n"
     "• They are written north-or-south first: southwest, never westsouth",
     hint='Two directions at once, and the north-or-south half comes first.')
card(C, 'Reading a direction off a map',
     "**Put your finger on the starting place and ask which way you have to "
     "move to reach the other one.**\n"
     "• Moved up and to the right → northeast\n"
     "• Moved down and to the left → southwest\n"
     "• If you barely moved up or down at all, it is just east or west",
     hint='Which way did your finger travel?',
     frm='added')

# ---------------------------------------------------------------- grid maps
card(C, 'A grid map',
     "**Some maps use letters and numbers instead of latitude and longitude.**\n"
     "• Letters run down the side, numbers run across the top\n"
     "• A place is named by its letter and number together, like B3\n"
     "• It works the same way as a coordinate, just with a smaller map",
     hint='Letters down the side, numbers across the top.')
card(C, 'Finding a place in a grid square',
     "**Slide across to the number, down to the letter, and the square where "
     "they meet is the place.**\n"
     "• The index at the back of a street atlas gives exactly this\n"
     "• The square is an area, not a point — the place is somewhere inside it",
     hint='Across, then down. The square is where they cross.')
card(C, 'Grid letters and directions agree',
     "**On a north-is-up grid map, A is the most northern row and 1 is the most "
     "western column.**\n"
     "• Moving from A toward D is moving south\n"
     "• Moving from 1 toward 5 is moving east\n"
     "• So B2 → D1 is south and west, which is southwest",
     hint='Later letter = further south. Bigger number = further east.',
     frm='added')

# ================================================================ questions
# LEVEL 1 — recall
q(Q, 1, 'A feature on the earth’s surface that human beings created is called '
     'what kind of feature?',
  ['A human feature', 'A natural feature', 'A physical feature', 'A climate feature'], 0,
  'People built it or decided it.',
  ['The question says human beings created it.',
   'A feature people made is a human feature.',
   'Natural features are the ones nobody made.',
   'So the answer is a human feature.'],
  '**A human feature.** Cities, roads, bridges, dams and borders are all human '
  'features — none of them exists until somebody builds or agrees on it.',
  'The wording "created by human beings" is the whole clue.')

q(Q, 1, 'A feature on the earth’s surface that was NOT created by human beings '
     'is called what kind of feature?',
  ['A cultural feature', 'A political feature', 'A natural feature', 'A human feature'], 2,
  'Nature put it there.',
  ['The question says human beings did NOT create it.',
   'Anything on the surface that people did not make is natural.',
   'Mountains, rivers and lakes are the usual examples.',
   'So the answer is a natural feature.'],
  '**A natural feature.** It would be there whether or not anyone ever lived '
  'nearby — a mountain, a river, a desert, a lake.',
  'Natural and human are the only two options for a feature; every one is one or the other.')

q(Q, 1, 'Which kind of map shows the natural features of the earth?',
  ['A cultural map', 'A physical map', 'A political map', 'A climate map'], 1,
  'The word means the physical earth itself.',
  ['Natural features are mountains, rivers and how high the land is.',
   'A physical map is the one that shows the land itself.',
   'Political maps show borders, which are human.',
   'So a physical map shows natural features.'],
  '**A physical map.** It shows the earth’s own shape — mountains, rivers, '
  'deserts — usually coloured by how high the land is.',
  'Physical = the physical earth, the part people did not make.')

q(Q, 1, 'Which kind of map shows the human features of the earth?',
  ['A physical map', 'A climate map', 'A cultural map', 'A political map'], 3,
  'Countries and borders are human features.',
  ['Human features are cities, borders, states and countries.',
   'A political map is the one drawn around borders.',
   'Physical maps show the land, not the borders.',
   'So a political map shows human features.'],
  '**A political map.** Countries, states and cities are all things people '
  'decided on, so the map of them is the map of human features.',
  'Politics is about people and who is in charge of where.')

q(Q, 1, 'Which kind of map shows the permanent weather conditions of a given area?',
  ['A climate map', 'A physical map', 'A political map', 'A cultural map'], 0,
  'Weather that lasts is called something else.',
  ['"Permanent weather conditions" is the definition of climate.',
   'Climate is what the weather is usually like, not what it is today.',
   'So the map of it is a climate map.'],
  '**A climate map.** Climate is the weather an area usually gets over many '
  'years — which is why one unusual week never changes the map.',
  'Weather is this week. Climate is always.')

q(Q, 1, 'Which kind of map shows behaviors of a country or region’s populations?',
  ['A physical map', 'A cultural map', 'A political map', 'A climate map'], 1,
  'A population is the people who live somewhere.',
  ['Behaviors of a population means how the people there live.',
   'What people speak, believe or eat is their culture.',
   'So the map of it is a cultural map.'],
  '**A cultural map.** Languages spoken, religions followed, foods eaten — '
  'anything about the people rather than the place.',
  'Culture is what the people do.')

q(Q, 1, 'What is the compass rose on a map for?',
  ['To show how far apart two places really are',
   'To explain what the symbols on the map mean',
   'To show which way is north',
   'To list every city the map includes'], 2,
  'It is the map telling you which way it is facing.',
  ['The compass rose is the little cross of arrows on the map.',
   'Its arrows are labelled N, S, E and W.',
   'That tells you which direction each way across the map is.',
   'Showing distance is the scale bar’s job, and explaining symbols is the key’s.'],
  '**To show which way is north.** Most maps put north at the top, but the '
  'compass rose is what makes it certain — so check it before answering any '
  'direction question.',
  'Scale bar = distance. Key = symbols. Compass rose = direction.')

# LEVEL 2 — apply
q(Q, 2, 'Is the border between two countries a natural feature or a human feature?',
  ['Human, because people agreed where to draw it',
   'Natural, because you can see it on the ground',
   'Natural, because borders usually follow rivers',
   'Human, but only when the border is a wall or a fence'], 0,
  'Could you find it without being told it was there?',
  ['A border is a line people decided on.',
   'Nothing on the earth marks it until somebody builds a sign or a fence.',
   'A feature people decided is a human feature.',
   'A river that happens to be the border is natural — but the border itself is not.'],
  '**Human, because people agreed where to draw it.** This is the trap worth '
  'remembering: a human feature does not have to be something you can touch. '
  'Lines people invented count too.',
  '"Natural" means nobody decided it, not that it is invisible.')

q(Q, 2, 'A map is shaded to show which language most families speak in each part '
     'of a country. Which kind of map is it?',
  ['A physical map', 'A political map', 'A cultural map', 'A climate map'], 2,
  'Ask what the map is really about: land, borders, weather or people.',
  ['The map is about what language people speak.',
   'Language is something the people do, not something about the land.',
   'Behaviors of a population are culture.',
   'So this is a cultural map.'],
  '**A cultural map.** It is shaded by country shapes, which makes it look '
  'political — but what it is actually reporting is how the people live.',
  'Look at what the colours MEAN, not at what shapes they are painted inside.')

q(Q, 2, 'A map shows which parts of a state get snow every winter and which parts '
     'almost never do. Which kind of map is it?',
  ['A climate map', 'A cultural map', 'A political map', 'A physical map'], 0,
  'Every winter, not this winter.',
  ['The map describes what happens every year, not one particular day.',
   'Weather that repeats year after year is climate.',
   'So this is a climate map.'],
  '**A climate map.** "Every winter" is the giveaway — one snowy day would be '
  'weather, and weather does not get its own map in this unit.',
  'If the map would still be true next year, it is climate.')

q(Q, 2, 'A map shows the rivers, mountain ranges and deserts of a continent, with '
     'no country borders drawn at all. Which kind of map is it?',
  ['A cultural map', 'A climate map', 'A physical map', 'A political map'], 2,
  'Rivers and mountains are natural features.',
  ['Rivers, mountains and deserts are all natural features.',
   'A map of natural features is a physical map.',
   'No borders are drawn, so it is definitely not political.'],
  '**A physical map.** Leaving the borders off is a clue as well as the '
  'contents — borders are the one thing a political map cannot do without.',
  'A physical map can show a whole continent without naming a single country.')

q(Q, 2, 'On a map with north at the top, which direction is up and to the RIGHT?',
  ['Southeast', 'Northwest', 'Southwest', 'Northeast'], 3,
  'Name the up-or-down half first.',
  ['Up on a north-is-up map is north.',
   'Right on a map is east.',
   'North and east together make northeast.',
   'The north-or-south half is always said first.'],
  '**Northeast.** Up is north, right is east, so up-and-right is northeast — '
  'and it is said north first, never "eastnorth".',
  'Up-right = NE, up-left = NW, down-right = SE, down-left = SW.')

q(Q, 2, 'Two towns sit on the same road. Riverton is up and to the LEFT of Alder '
     'on the map, and north is at the top. In which direction do you travel to '
     'get from Alder to Riverton?',
  ['Southeast', 'Northwest', 'Northeast', 'Southwest'], 1,
  'Which way does your finger move starting from Alder?',
  ['Start at Alder and move toward Riverton.',
   'You move up, which is north.',
   'You also move left, which is west.',
   'North and west together make northwest.'],
  '**Northwest.** Start at the place the question starts from — going the '
  'other way, Riverton to Alder, would be southeast instead.',
  'The direction depends on which place you start at, so read that first.')

q(Q, 2, 'On a grid map, the letters run down the side and the numbers run across '
     'the top. The museum is listed at C4. How do you find it?',
  ['Count to the 4th row, then across to the letter C',
   'Look in the 4th square of the top row',
   'Slide across to column 4, then down to row C',
   'Count 4 squares diagonally from the top left corner'], 2,
  'Across for the number, down for the letter.',
  ['The numbers are across the top, so 4 tells you which column.',
   'The letters are down the side, so C tells you which row.',
   'The museum is in the square where that column and that row cross.',
   'It is an area, not a dot — the museum is somewhere inside that square.'],
  '**Slide across to column 4, then down to row C.** A grid reference works '
  'like a coordinate on a smaller map: one number for across, one letter for '
  'down, and the place is where they meet.',
  'The index at the back of a street atlas gives you exactly this pair.')

# LEVEL 3 — analyze
q(Q, 3, 'Which of these is a NATURAL feature?',
  ['The line halfway between the North and South Poles',
   'A canyon cut by a river over millions of years',
   'A reservoir made by damming a valley',
   'A state line that runs straight across a desert'], 1,
  'Three of these were decided or built by people.',
  ['The line halfway between the poles is the equator — people agreed where it goes.',
   'A reservoir only exists because somebody built the dam.',
   'A straight state line across a desert was drawn on paper by people.',
   'A canyon carved by a river happened with no people involved at all.'],
  '**A canyon cut by a river over millions of years.** The other three are all '
  'human features, and two of them are the kind you cannot touch — an agreed '
  'line counts as human just as much as a dam does.',
  'A valley is natural; the reservoir filling it is not.')

q(Q, 3, 'A river forms the whole border between two states. Is that river a '
     'natural feature or a human feature?',
  ['Both — the river is natural, and the border people put on it is human',
   'Natural, so the border must be natural too',
   'Human, because people chose to use it as a border',
   'Neither, because a border is not a feature of the surface at all'], 0,
  'There are two different things here, not one.',
  ['The river was cut by water long before anyone used it for anything.',
   'That makes the river itself a natural feature.',
   'The decision to treat it as a border was made by people.',
   'So the border is a human feature that happens to sit on a natural one.'],
  '**Both — the river is natural, and the border people put on it is human.** '
  'Using a natural feature does not make a human decision natural, and '
  'deciding something about a river does not make the river human-made.',
  'Ask about each one separately and the answer stops being confusing.')

q(Q, 3, 'A map of a country is painted in bright colours, one colour per region, '
     'and the key says each colour is the crop that region grows most. Which '
     'kind of map is it, and why?',
  ['Political, because it is painted one colour per region',
   'Physical, because crops grow out of the land',
   'Climate, because crops depend on the weather',
   'Cultural, because it reports something the people there do'], 3,
  'The shapes and the meaning are two different things.',
  ['The colours are painted inside regions, which looks political.',
   'But what each colour REPORTS is which crop people choose to grow.',
   'Growing a crop is a behavior of the population.',
   'So the map is cultural, even though it is drawn on political shapes.'],
  '**Cultural, because it reports something the people there do.** Almost every '
  'cultural map is drawn on top of political shapes — so read the key, not the '
  'outlines, to decide what kind of map it is.',
  'The key tells you what a map is about; the borders only tell you where it is.')

q(Q, 3, 'On a north-is-up grid map, the park is in square B2 and the school is in '
     'square D1. In which direction do you travel from the park to the school?',
  ['Southwest', 'Northeast', 'Southeast', 'Northwest'], 0,
  'Later letter means further down; smaller number means further left.',
  ['B to D moves further down the side of the map.',
   'Down on a north-is-up map is south.',
   '2 to 1 moves back toward the left side of the map.',
   'Left is west, so the trip is south and west — southwest.'],
  '**Southwest.** Going from B to D is going south, and going from 2 to 1 is '
  'going west, so the whole trip is southwest.',
  'Letters going forward = going south. Numbers going up = going east.')

q(Q, 3, 'Your friend tells you a place is "in square 3" on a grid map. Why is that '
     'not enough to find it?',
  ['Because grid maps never use numbers on their own',
   'Because a number alone only narrows it to one whole column',
   'Because you also need to know the map’s scale',
   'Because the compass rose has not been checked yet'], 1,
  'How much of the map does a single number rule out?',
  ['The number 3 tells you which column the place is in.',
   'That column runs all the way from the top of the map to the bottom.',
   'The place could be anywhere along it.',
   'The letter is what narrows it to one square in that column.'],
  '**Because a number alone only narrows it to one whole column.** You need '
  'both halves of a grid reference for the same reason a coordinate needs both '
  'latitude and longitude — one on its own is a whole line, not a place.',
  'Two numbers, or a letter and a number: it always takes two to name a place.')

SORT = {
  'id': 's1',
  'title': 'Natural, or made by people?',
  'a': 'Nobody made it',
  'b': 'People made it',
  'items': [
    {'t': 'A waterfall on a mountain stream', 'k': 'a',
     'why': 'Water cut it over a very long time with nobody involved.'},
    {'t': 'A bridge carrying a road over a canyon', 'k': 'b',
     'why': 'Somebody designed and built it.'},
    {'t': 'A desert that gets almost no rain', 'k': 'a',
     'why': 'Its dryness comes from where it sits on the earth, not from anyone.'},
    {'t': 'The straight line where one state stops and the next begins', 'k': 'b',
     'why': 'People agreed where to draw it — and an agreed line still counts.'},
    {'t': 'A lake filling a hollow left by an ancient glacier', 'k': 'a',
     'why': 'The ice dug the hollow long before anyone lived there.'},
    {'t': 'A reservoir behind a concrete dam', 'k': 'b',
     'why': 'The valley is natural; the water standing in it is there because of the dam.'},
    {'t': 'The equator', 'k': 'b',
     'why': 'There is no line on the ground — people agreed where the halfway line goes.'},
    {'t': 'A cave carved into limestone by underground water', 'k': 'a',
     'why': 'Water dissolving rock, with no help from anyone.'},
    {'t': 'A harbour wall built to keep the waves out', 'k': 'b',
     'why': 'The bay is natural; the wall across it was constructed.'},
    {'t': 'A bay where the coastline curves inward', 'k': 'a',
     'why': 'The shape of the coast is the earth’s own.'},
    {'t': 'A highway interchange with four levels of ramps', 'k': 'b',
     'why': 'About as constructed as anything gets.'},
    {'t': 'A forest that has grown on a hillside for centuries', 'k': 'a',
     'why': 'It seeded and spread on its own.'},
  ]
}

u = build(
  'wayfinder', C, Q, 'unit-hist-u5-p1',
  'Unit 5 · 1 Features, Maps and Directions', 'history',
  'The first four sections of the Unit 5 Test Study Guide: what makes a '
  'feature natural or human, the four kinds of map (physical, political, '
  'climate and cultural), the compass rose and its eight directions, and how '
  'a letter-and-number grid map works.',
  'Every question on this part of the test comes down to two habits: asking '
  'whether a person decided something, and asking what a map is really about. '
  'Get those two and the section answers itself.',
  [('Say what makes a feature natural or human, including features you cannot touch', 'source'),
   ('Name what each of the four kinds of map shows', 'source'),
   ('Use a compass rose to give a cardinal or intermediate direction', 'source'),
   ('Find a place from a letter-and-number grid reference', 'source'),
   ('Decide which kind of map you are looking at from its key rather than its shapes', 'added')],
  'Built from the OPTIONAL Unit 5 Test Study Guide in her History folder — a '
  'clean, unfilled copy, so there is nothing of hers to check here and nothing '
  'to repair. Worth knowing: her teacher will take the completed guide on the '
  'day of the test for one extra credit point, and says outright it will not '
  'be collected earlier because she needs it to study from. So the guide '
  'itself is the assignment; this unit is here so she can fill it in.\n\n'
  'The guide has thirty-three items in seven sections. This is sections one to '
  'four — features, map types, the compass rose and grid maps. Sections five '
  'to seven are the other two parts of this shelf: latitude and longitude was '
  'already built back in September and has simply been moved onto the Unit 5 '
  'shelf beside these, and time zones, elevation and the continents are part '
  'three.\n\n'
  'ONE ITEM IS WORTH A GROWN-UP’S EYE. The guide asks her to mark "the prime '
  'meridian" as a human (H) or natural (N) feature, and the answer is HUMAN — '
  'it is a line people agreed on, not something on the ground. It sits in a '
  'list with a geyser, a lake and a city, so it reads as the odd one out and '
  'it is the single likeliest item on the page to be marked wrong. A card and '
  'two questions target exactly that idea, using fresh examples.\n\n'
  'None of the guide’s own examples is used as a graded question here — the '
  'guide is her homework and this app is extra, so answering from memory of '
  'the page would not tell her anything.',
  ('Start with the sort — twelve things, natural or made by people. '
   'The two the guide is most likely to catch you on are in there.', 12),
  'content/history-u5-p1.json',
  'Unit 5 Test Study Guide (History, sections 1–4)',
  'Her class’s optional Unit 5 Test Study Guide',
  offset_hours=3)

import json, io
p = 'content/history-u5-p1.json'
j = json.load(io.open(p, encoding='utf-8'))
uu = [v for v in j['records'].values() if v['type'] == 'unit'][0]
uu['sorts'] = [SORT]
uu['libv'] = 1
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + sort set "%s" (%d items), libv 1' % (SORT['title'], len(SORT['items'])))
