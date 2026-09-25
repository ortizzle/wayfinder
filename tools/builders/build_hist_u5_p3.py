#!/usr/bin/env python3
"""Unit 5 · 3 Time Zones, Elevation and the Globe  (Wayfinder / History 4)

Source: "Unit 5 - History.pdf" — sections 6 to 8 of her class's optional Unit
5 Test Study Guide (items 26-33), plus the two class maps bound into it: the
Core Knowledge "Time Zones in the United States" map and the world map she is
asked to fill in with the continents and oceans.

Read the same way as part 1: the PDF is an image-only scan with no text layer,
rendered with pypdfium2 and read page by page.

EVERY TIME ANSWER WAS WORKED FROM HER CLASS MAP, not from memory of real time
zones, and the two happen to agree here: the map reads Hawaii 5:00, Alaska
6:00, Pacific 7:00, Mountain 8:00, Central 9:00, Eastern 10:00, and places
Arizona in the Mountain block. So Arizona to Hawaii is three hours back and
Mountain to Eastern is two hours forward, both on the map and in real life.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, build

C, Q = [], []

# ---------------------------------------------------------------- time zones
card(C, 'Why time zones exist',
     "**The sun cannot be overhead everywhere at once, so the world is divided "
     "into bands that each keep the same clock time.**\n"
     "• Without them, noon in one town would be mid-morning in the next\n"
     "• Everyone inside one band agrees to read the same time",
     hint='One sun, one planet turning — the clocks have to give somewhere.')
card(C, 'The United States has six time zones',
     "**Six altogether, and four of them lie between the East and West "
     "Coasts.**\n"
     "• The four between the coasts: Pacific, Mountain, Central, Eastern\n"
     "• The other two are Alaska and Hawaii, out past the Pacific zone\n"
     "• \"Six in total, four between the coasts\" is the sentence to remember",
     hint='Six in all. Four you could drive across.')
card(C, 'West to east across the country',
     "**Pacific, then Mountain, then Central, then Eastern — going east, each "
     "one is an hour later.**\n"
     "• Pacific 7:00 → Mountain 8:00 → Central 9:00 → Eastern 10:00\n"
     "• Hawaii and Alaska sit further back still, west of Pacific",
     hint='P-M-C-E, and each step east adds an hour.')
card(C, 'Which way the clock moves',
     "**Travel EAST and you set the clock forward. Travel WEST and you set it "
     "back.**\n"
     "• East is toward the sunrise, so the day there is already further along\n"
     "• This one rule answers every time-zone question on the guide",
     hint='East = earlier sunrise = later clock.')
card(C, 'Counting the hours between two places',
     "**Count how many zone lines you cross, then add that many hours going "
     "east or subtract them going west.**\n"
     "• Mountain to Eastern crosses two lines, so add two hours\n"
     "• Getting the direction right matters more than the counting does",
     hint='Count the lines, then decide forward or back.',
     frm='added')
card(C, 'The day can change too',
     "**If adding or subtracting the hours carries you past midnight, the day "
     "changes with it.**\n"
     "• 11:30pm Wednesday plus two hours is 1:30am on THURSDAY\n"
     "• A question that gives you a day as well as a time is asking for exactly this",
     hint='Past midnight, the date moves.')
card(C, 'Arizona and daylight saving time',
     "**On the class map Arizona is in the Mountain zone, and that is the "
     "answer to use for the test.**\n"
     "• In real life Arizona is unusual: it does not change its clocks in spring\n"
     "• So for part of the year Arizona matches California instead\n"
     "• Real, interesting, and NOT what the class map is asking about",
     hint='Test answer: Mountain. Real life: Arizona just never moves its clocks.',
     frm='added')
card(C, 'The international date line',
     "**A line down the Pacific Ocean where the date changes.**\n"
     "• Cross it heading WEST and you jump forward a day — Monday becomes Tuesday\n"
     "• Cross it heading EAST and you go back a day and live the same date twice\n"
     "• It runs roughly opposite the Prime Meridian, on the far side of the world",
     hint='West across it, skip a day. East across it, repeat one.')

# ---------------------------------------------------------------- elevation
card(C, 'Elevation',
     "**How high the land is above sea level.**\n"
     "• Measured from the ocean's surface, which counts as zero\n"
     "• Physical maps usually use colour to show it — greens low, browns high",
     hint='How far above the sea the ground stands.')
card(C, 'Peak',
     "**The top, or highest point, of a mountain.**\n"
     "• A mountain range has many peaks\n"
     "• The peak is a point; the mountain is the whole shape underneath it",
     hint='The very top.')
card(C, 'Valley',
     "**An area of low land with higher land on either side.**\n"
     "• Often cut by a river running along the bottom\n"
     "• Low is only low compared with what is beside it",
     hint='Low ground with high ground around it.')
card(C, 'Reading a physical map by colour',
     "**The key tells you what each colour is worth, so check it before "
     "deciding anything is high.**\n"
     "• Two maps can use the same brown for very different heights\n"
     "• Blue on a physical map is usually water, not low land",
     hint='The same colour means different heights on different maps.',
     frm='added')

# ---------------------------------------------------------------- the globe
card(C, 'Oceans cover about 70% of the earth',
     "**Roughly seven tenths of the surface is ocean.**\n"
     "• The five oceans: Pacific, Atlantic, Indian, Arctic and Antarctic\n"
     "• The Antarctic Ocean is also called the Southern Ocean\n"
     "• The Pacific alone is bigger than all the land put together",
     hint='Seven tenths water.')
card(C, 'Continents cover about 30% of the earth',
     "**Roughly three tenths of the surface is land.**\n"
     "• The seven continents: Africa, Antarctica, Asia, Australia, Europe, "
     "North America and South America\n"
     "• The two numbers have to add to 100, so remembering one gives the other",
     hint='Three tenths land — and 70 and 30 make 100.')
card(C, 'Seven continents, five oceans',
     "**Seven and five, and the guide asks you to label them on a blank map.**\n"
     "• Largest continent: Asia. Smallest: Australia\n"
     "• Largest ocean: Pacific. Smallest: Arctic\n"
     "• Antarctica is a continent even though it is under ice",
     hint='7 continents, 5 oceans.',
     frm='added')

# ================================================================ questions
# LEVEL 1 — recall
q(Q, 1, 'How many time zones does the United States have in total?',
  ['Four', 'Six', 'Three', 'Nine'], 1,
  'More than the ones you could drive between.',
  ['The four you could drive across are Pacific, Mountain, Central and Eastern.',
   'Alaska and Hawaii each have one of their own.',
   'Four plus those two makes six.'],
  '**Six.** Four of them lie between the East and West Coasts, and Alaska and '
  'Hawaii add the other two.',
  'Six in all, four between the coasts.')

q(Q, 1, 'What does elevation tell you about a piece of land?',
  ['How high it is above sea level', 'How much rain it gets in a year',
   'How many people live on it', 'How far north of the equator it is'], 0,
  'Measured up from the sea.',
  ['Elevation is a height measurement.',
   'It is measured from the surface of the ocean, which counts as zero.',
   'So it tells you how high the land stands above sea level.'],
  '**How high it is above sea level.** Physical maps usually show it in '
  'colour — greens for low ground, browns and whites for high.',
  'Sea level is the zero that every elevation is measured from.')

q(Q, 1, 'What is the peak of a mountain?',
  ['The path that leads up it', 'The flat land at its base',
   'Its top, or highest point', 'The side that faces the sun'], 2,
  'The very top.',
  ['A mountain rises to a single highest point.',
   'That point is called the peak.',
   'A whole range of mountains has many peaks, one for each.'],
  '**Its top, or highest point.** The peak is a point; the mountain is the '
  'whole shape underneath it.',
  'Summit means the same thing.')

q(Q, 1, 'What is a valley?',
  ['A wide flat area with no hills at all',
   'An area of low land with higher land around it',
   'The highest ridge in a mountain range',
   'A stretch of coast where the sea cuts inland'], 1,
  'Low, but only compared to what is beside it.',
  ['A valley is low ground.',
   'What makes it a valley is the higher land on either side.',
   'Often a river runs along the bottom of it.'],
  '**An area of low land with higher land around it.** Low is always relative '
  'here — a valley high in the mountains can still be well above sea level.',
  'No higher land beside it and it is a plain, not a valley.')

q(Q, 1, 'About how much of the earth’s surface is covered by oceans?',
  ['About 30%', 'About 50%', 'About 70%', 'About 90%'], 2,
  'Far more water than land.',
  ['The earth’s surface is either ocean or land.',
   'The oceans take roughly seven tenths of it.',
   'That leaves about three tenths for the continents.'],
  '**About 70%.** Roughly seven tenths ocean and three tenths land — and the '
  'two have to add to 100, so knowing either one gives you the other.',
  'The Pacific on its own is bigger than all the land put together.')

q(Q, 1, 'How many continents are there?',
  ['Five', 'Six', 'Eight', 'Seven'], 3,
  'One more than the number of oceans.',
  ['Africa, Antarctica, Asia, Australia, Europe, North America, South America.',
   'Counting them gives seven.',
   'Antarctica counts even though it is buried under ice.'],
  '**Seven.** Africa, Antarctica, Asia, Australia, Europe, North America and '
  'South America — seven continents against five oceans.',
  'Asia is the biggest, Australia the smallest.')

# LEVEL 2 — apply
q(Q, 2, 'You fly from a city in the Central time zone to a city in the Eastern '
     'time zone. What do you do to your watch?',
  ['Set it forward one hour', 'Set it back one hour',
   'Set it forward two hours', 'Leave it exactly as it is'], 0,
  'Which direction are you flying?',
  ['Eastern is one zone east of Central.',
   'Travelling east means setting the clock forward.',
   'One zone crossed means one hour.',
   'So the watch goes forward one hour.'],
  '**Set it forward one hour.** East is toward the sunrise, so the day there is '
  'already an hour further along.',
  'East = forward. West = back. Then count the zones.')

q(Q, 2, 'It is 4:00pm in the Mountain time zone. What time is it in the Pacific '
     'time zone?',
  ['5:00pm', '6:00pm', '3:00pm', '4:00pm'], 2,
  'Pacific is west of Mountain.',
  ['Pacific sits one zone west of Mountain.',
   'Travelling west means setting the clock back.',
   'One zone back from 4:00pm is 3:00pm.'],
  '**3:00pm.** Pacific is one hour behind Mountain, so the afternoon there is '
  'an hour younger than it is here.',
  'The zone on the left of the map always reads the earlier time.')

q(Q, 2, 'It is 7:00pm in the Mountain time zone. What time is it in Hawaii?',
  ['10:00pm', '4:00pm', '8:00pm', '5:00pm'], 1,
  'Hawaii sits three hours back from Mountain on the class map.',
  ['The class map reads Mountain 8:00 and Hawaii 5:00.',
   'That is a three-hour difference, with Hawaii behind.',
   'Hawaii is west, so the clock goes back.',
   '7:00pm minus three hours is 4:00pm.'],
  '**4:00pm.** Hawaii runs three hours behind the Mountain zone, so an evening '
  'here is still afternoon there.',
  'Read the two clock pictures on the map and subtract — that is where the 3 comes from.')

q(Q, 2, 'Which of these describes a valley?',
  ['A peak that rises above every other peak in the range',
   'A coastline that curves in toward the land',
   'A wide plain with no high ground anywhere near it',
   'A strip of low ground with hills rising on both sides'], 3,
  'It needs the higher land as much as the low.',
  ['A valley is low ground.',
   'It also needs higher land on either side of it.',
   'A plain is low too, but nothing rises beside it, so it is not a valley.'],
  '**A strip of low ground with hills rising on both sides.** The higher land '
  'is half the definition — without it you have a plain.',
  'Low compared to WHAT is the question a valley answers.')

q(Q, 2, 'On a physical map, two areas are shaded in the same shade of brown. What '
     'can you safely say about them?',
  ['They are both at a similar elevation on THIS map',
   'They are both above 5,000 feet, because brown always means that',
   'They both get the same amount of rain as each other every year',
   'They are both inside the borders of the same country or state'], 0,
  'Where does the meaning of a colour come from?',
  ['A physical map uses colour to show elevation.',
   'The key on that map says which heights each colour stands for.',
   'So the same colour on the same map means a similar height.',
   'A different map could use that same brown for something else entirely.'],
  '**They are both at a similar elevation on THIS map.** Colours only mean '
  'what a map’s own key says they mean, so always check the key before '
  'comparing two maps.',
  'Rainfall would be a climate map, and countries would be a political one.')

q(Q, 2, 'Which of these is an OCEAN rather than a continent?',
  ['Antarctica', 'Australia', 'Arctic', 'Africa'], 2,
  'One of these is water.',
  ['Africa, Australia and Antarctica are all continents.',
   'The Arctic is the ocean around the North Pole.',
   'Antarctica, with the -a on the end, is the continent at the South Pole.'],
  '**Arctic.** The Arctic Ocean surrounds the North Pole; Antarctica is the '
  'continent at the other end, and the Antarctic Ocean is the water around it.',
  'Arctic = the ocean up north. Antarctica = the land down south.')

# LEVEL 3 — analyze
q(Q, 3, 'It is 11:00pm on Tuesday in the Central time zone. What time and day is '
     'it in the Eastern time zone?',
  ['10:00pm on Tuesday', '11:00pm on Wednesday',
   '12:00am on Wednesday', '1:00am on Wednesday'], 2,
  'Adding the hour carries you past something.',
  ['Eastern is one zone east of Central, so add one hour.',
   '11:00pm plus one hour is 12:00am.',
   'Midnight ends Tuesday and starts the next day.',
   'So it is 12:00am on Wednesday.'],
  '**12:00am on Wednesday.** Adding the hour carries the clock past midnight, '
  'and the date has to move with it — which is exactly why the question gives '
  'you a day as well as a time.',
  'Whenever a time-zone question names a day, check whether you crossed midnight.')

q(Q, 3, 'Two cities are in the same time zone, but one is much further north than '
     'the other. What does that tell you about their clocks?',
  ['The northern city’s clock runs an hour ahead',
   'The northern city’s clock runs an hour behind',
   'Their clocks read the same time as each other',
   'It depends which side of the equator they are on'], 2,
  'Which direction do time zones run in?',
  ['Time zones are bands that run north to south, not east to west.',
   'So moving north or south inside one does not change the zone.',
   'Both cities are in the same zone.',
   'Everyone in one zone agrees to read the same clock time.'],
  '**Their clocks read the same time as each other.** Time depends on how far '
  'EAST or WEST you are, because that is what changes when the sun rises. '
  'North and south change the seasons and the daylight, not the clock.',
  'Zones are tall and narrow for exactly this reason.')

q(Q, 3, 'A ship sails WEST across the international date line on a Monday. What '
     'happens to the date on board?',
  ['It jumps forward to Tuesday', 'It goes back to Sunday',
   'It stays Monday until the ship reaches land', 'Monday happens twice'], 0,
  'West across the line and you lose a day off the calendar.',
  ['The international date line runs down the Pacific, opposite the Prime Meridian.',
   'Crossing it westward moves you into the next day.',
   'So Monday becomes Tuesday the moment the ship crosses.',
   'Going the other way, east, is what makes a day happen twice.'],
  '**It jumps forward to Tuesday.** West across the line skips a day forward; '
  'east across it takes you back one, so you live the same date twice.',
  'It is the one place on earth where the date changes without a night passing.')

q(Q, 3, 'A hiker reaches a spot the map shades for high elevation, but the ground '
     'around her is flat in every direction. Can both things be true?',
  ['No — elevation counts how steep the ground is, so high land cannot be flat',
   'No — the map must be shading how much rain falls there, not the height',
   'Yes — elevation is height above sea level, and flat land can be high up',
   'Yes — but only while she is standing on the single highest peak nearby'], 2,
  'Elevation compares her to the sea, not to the ground beside her.',
  ['Elevation measures height above sea level.',
   'It says nothing about whether the land nearby rises or falls.',
   'A plateau is a large flat area that sits high above sea level.',
   'So flat ground and high elevation fit together perfectly well.'],
  '**Yes — elevation is height above sea level, and flat land can be high up.** '
  'A high flat area is a plateau, and much of the state she lives in is '
  'exactly that.',
  'High and steep are two different questions about the same place.')

q(Q, 3, 'Put these four United States time zones in order from WEST to EAST.',
  ['Pacific', 'Mountain', 'Central', 'Eastern'], 0,
  'Start at the coast where the sun sets last.',
  ['Pacific is the furthest west of the four, along the western coast.',
   'Mountain comes next, inland.',
   'Central covers the middle of the country.',
   'Eastern is the furthest east, along the Atlantic coast.'],
  '**Pacific, Mountain, Central, Eastern.** Going east, each one is an hour '
  'later than the one before — 7:00, 8:00, 9:00, 10:00.',
  'P-M-C-E, left to right across the map.',
  kind='order')

q(Q, 3, 'Someone says "the oceans cover about 30% of the earth." What is wrong, '
     'and how do you know?',
  ['Nothing is wrong — 30% is the oceans, and the continents are about 70%',
   'The number belongs to something else — 30% is the land, and the oceans are about 70%',
   'The number is far too small — the oceans cover more like 90% of the earth',
   'Neither one is right — ocean and land each cover about half the earth'], 1,
  'The two figures are a pair, and they have been swapped.',
  ['The surface of the earth is either ocean or land.',
   'That means the two percentages have to add up to 100.',
   'Oceans are the bigger share at about 70%.',
   'So 30% is the continents’ figure, used on the wrong one.'],
  '**The number belongs to something else — 30% is the land, and the oceans are '
  'about 70%.** The two figures always add to 100, which makes this the '
  'easiest kind of mistake to catch.',
  'If you only remember one of the pair, subtract from 100 for the other.')

u = build(
  'wayfinder', C, Q, 'unit-hist-u5-p3',
  'Unit 5 · 3 Time Zones, Elevation and the Globe', 'history',
  'The last three sections of the Unit 5 Test Study Guide: the six United '
  'States time zones and which way the clock moves, the international date '
  'line, reading elevation on a physical map, and the seven continents and '
  'five oceans.',
  'Time zones are the part of this unit most often got backwards, and the fix '
  'is one sentence: east is forward, west is back. Everything else on this '
  'part of the guide is vocabulary you either know or can look at once.',
  [('Say how many time zones the United States has, and how many lie between the coasts', 'source'),
   ('Work out the time in another zone, including when the day changes', 'source'),
   ('Say what happens to the date when you cross the international date line', 'source'),
   ('Define elevation, peak and valley', 'source'),
   ('Name the seven continents and five oceans and say roughly how much of the earth each covers', 'source')],
  'Sections six to eight of the same optional study guide part one is built '
  'from — time zones, reading a physical map, and continents and oceans.\n\n'
  'EVERY TIME ANSWER HERE WAS WORKED FROM HER CLASS’S OWN MAP rather than '
  'from real-world time zones, and the two agree: the map reads Pacific 7:00, '
  'Mountain 8:00, Central 9:00, Eastern 10:00, Alaska 6:00 and Hawaii 5:00, '
  'and it puts Arizona in the Mountain block. So Arizona to Hawaii is three '
  'hours back either way you work it.\n\n'
  'ONE THING WORTH KNOWING ABOUT, and it is on a card rather than in a graded '
  'question: Arizona really is unusual, because it does not move its clocks in '
  'spring. For part of the year that puts it on California’s time instead of '
  'Denver’s. That is true, it is the kind of thing a nine-year-old who lives '
  'here notices, and it is NOT what the class map is asking about — so the '
  'card says outright that the test answer is Mountain, and leaves the real '
  'story as an aside rather than letting it cast doubt on a test answer.\n\n'
  'Her class map labels the water around Antarctica the ANTARCTIC OCEAN. The '
  'same ocean is called the Southern Ocean in a lot of books, so the card '
  'gives her class’s name first and the other one beside it.\n\n'
  'The guide also asks her to label a blank world map with the continents and '
  'oceans, with a note telling her to try it without her notes. That is a '
  'drawing task this app cannot do for her; the cards give her the lists to '
  'check herself against afterwards.',
  ('Time zones first — one rule, east is forward and west is back, and the '
   'rest of the section falls out of it.', 12),
  'content/history-u5-p3.json',
  'Unit 5 Test Study Guide (History, sections 6–8)',
  'Her class’s optional Unit 5 Test Study Guide, with the class time-zone and world maps',
  offset_hours=3)

import json, io
p = 'content/history-u5-p3.json'
j = json.load(io.open(p, encoding='utf-8'))
uu = [v for v in j['records'].values() if v['type'] == 'unit'][0]
uu['libv'] = 1
io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
print('  + libv 1')
