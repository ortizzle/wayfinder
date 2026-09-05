# -*- coding: utf-8 -*-
"""Topic 3 · Decimals on the Number Line — River's first number-line unit.
Every question is kind:'slider': she drags a marker to where the decimal
belongs. Placement on a number line is the best-evidenced activity there is
for number sense, and the Unit 1 math test (9/10) is place value and
decimals. Lines zoom in for hundredths so a thumb's width is never the
difference between right and wrong."""
import json, io, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, slider
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

C, Q = [], []
card(C, 'A number line is a ruler for numbers',
     '**Every number has exactly one place on the line, and the space between two labelled marks is split into equal parts.**'
     '\n• 0.5 sits exactly halfway between 0 and 1.'
     '\n• Bigger is always further right.', 'Half of the way is half of the number.')
card(C, 'Tenths split a whole into ten',
     '**Between 0 and 1 there are ten equal spaces; each one is a tenth (0.1).**'
     '\n• 0.3 is three spaces along from 0.'
     '\n• 2.6 is six spaces along from 2.', 'Count the spaces, not the marks.')
card(C, 'Hundredths split a tenth into ten',
     '**Zoom in on one tenth and it splits into ten hundredths (0.01 each).**'
     '\n• 0.34 is four hundredths past 0.3 — almost halfway to 0.4.'
     '\n• 0.07 is seven hundredths past 0 — most of the way to 0.1.', 'Two decimal places means you are counting the small spaces.')
card(C, 'When the marks are not tenths',
     '**Work out what one space is worth first: the gap between two labels ÷ the number of spaces.**'
     '\n• On a line from 0 to 2 with four spaces, each space is 0.5.'
     '\n• Then count spaces from the label just below your number.', 'Same rule as reading a thermometer or a cylinder.')

T = lambda d: [d, 'Find the label just below the number, then count spaces.', 'Drag the marker there and place it.']
slider(Q, 1, 'Place 0.5 on the line.', {'lo':0,'hi':1,'ans':0.5,'tol':0.03,'step':0.01,'ticks':0.1,'labels':[0,0.5,1]},
       'Half of one is halfway along.', T('0.5 is five tenths — halfway between 0 and 1.'),
       '**0.5 sits exactly halfway between 0 and 1.** Five of the ten spaces.', 'A decimal ending in 5 is always a halfway point of something.')
slider(Q, 1, 'Place 0.35 on the line.', {'lo':0,'hi':1,'ans':0.35,'tol':0.025,'step':0.01,'ticks':0.1,'labels':[0,0.5,1]},
       'Three tenths, and then halfway to the fourth.', T('0.35 is three tenths plus half of a tenth.'),
       '**0.35 is halfway between 0.3 and 0.4.** Three full spaces, then half a space more.', 'Say it as “thirty-five hundredths” and the picture appears.')
slider(Q, 1, 'Place 0.8 on the line.', {'lo':0,'hi':1,'ans':0.8,'tol':0.03,'step':0.01,'ticks':0.1,'labels':[0,0.5,1]},
       'Eight of the ten spaces.', T('0.8 is eight tenths — two spaces short of 1.'),
       '**0.8 is eight tenths along — two spaces before 1.** Counting back from 1 is quicker here.', 'Near the top of the line, count down from the top label.')
slider(Q, 2, 'Place 2.6 on the line.', {'lo':2,'hi':3,'ans':2.6,'tol':0.03,'step':0.01,'ticks':0.1,'labels':[2,2.5,3]},
       'The whole number tells you which line; the tenths tell you where on it.', T('2.6 is 2 and six tenths — six spaces past 2.'),
       '**2.6 is six tenths past 2.** Just past the halfway mark at 2.5.', 'The line runs from 2 to 3, so the digit before the point is already handled.')
slider(Q, 2, 'Place 7.25 on the line.', {'lo':7,'hi':8,'ans':7.25,'tol':0.03,'step':0.01,'ticks':0.1,'labels':[7,7.5,8]},
       'A quarter of the way from 7 to 8.', T('7.25 is two tenths past 7, then half of the next tenth.'),
       '**7.25 is a quarter of the way from 7 to 8** — halfway between 7.2 and 7.3.', '0.25 is a quarter: the same as 25 cents in a dollar.')
slider(Q, 2, 'Place 0.07 on the line from 0 to 0.1.', {'lo':0,'hi':0.1,'ans':0.07,'tol':0.004,'step':0.001,'ticks':0.01,'labels':[0,0.05,0.1]},
       'This line is one tenth long, so its spaces are hundredths.', T('0.07 is seven hundredths — seven spaces along a line of ten hundredths.'),
       '**0.07 is seven hundredths, seven spaces past 0 on a line that ends at 0.1.** Most of the way along.', 'A zoomed-in line: the whole thing is only one tenth.')
slider(Q, 2, 'Place 0.34 on the line from 0.3 to 0.4.', {'lo':0.3,'hi':0.4,'ans':0.34,'tol':0.004,'step':0.001,'ticks':0.01,'labels':[0.3,0.35,0.4]},
       'The line starts at 0.3, so only the hundredths digit is left to place.', T('0.34 is four hundredths past 0.3.'),
       '**0.34 is four spaces past 0.3 on a line split into hundredths.** Just short of the halfway mark at 0.35.', 'Start from the left label — the tenths are already done for you.')
slider(Q, 3, 'Place 5.18 on the line from 5.1 to 5.2.', {'lo':5.1,'hi':5.2,'ans':5.18,'tol':0.004,'step':0.001,'ticks':0.01,'labels':[5.1,5.15,5.2]},
       'Eight hundredths past 5.1 — nearly at 5.2.', T('5.18 is eight hundredths past 5.10.'),
       '**5.18 is eight spaces past 5.1, two spaces before 5.2.** Counting back from 5.2 is quicker.', 'Zoomed-in lines make hundredths as easy as tenths.')
slider(Q, 2, 'Place 0.9 on the line from 0 to 2.', {'lo':0,'hi':2,'ans':0.9,'tol':0.06,'step':0.01,'ticks':0.5,'labels':[0,1,2]},
       'This line is two whole numbers long — 1 is in the middle.', T('0.9 is just short of 1, which is the middle of this line.'),
       '**0.9 is one tenth short of 1, and 1 is the middle of a line from 0 to 2.** Just left of centre.', 'Find the whole number first, then nudge.')
slider(Q, 2, 'Place 1.75 on the line from 0 to 2.', {'lo':0,'hi':2,'ans':1.75,'tol':0.06,'step':0.01,'ticks':0.5,'labels':[0,1,2]},
       'The marks here are halves, not tenths.', T('1.75 is three quarters of the way from 1 to 2.'),
       '**1.75 is halfway between the 1.5 mark and 2.** Each mark on this line is worth 0.5, so 1.75 is half a space past the third mark.', 'Work out what one space is worth before you count.')
slider(Q, 3, 'Place the decimal that is exactly halfway between 0.6 and 0.7.', {'lo':0,'hi':1,'ans':0.65,'tol':0.025,'step':0.01,'ticks':0.1,'labels':[0,0.5,1]},
       'Halfway between two tenths is a hundredths number.', ['Halfway between 0.6 and 0.7 is 0.65.', 'Six full spaces, then half a space.', 'Drag the marker there and place it.'],
       '**0.65 is halfway between 0.6 and 0.7.** Six tenths and five hundredths.', 'Between any two tenths, the halfway point ends in 5.')
slider(Q, 3, 'Round 3.48 to the nearest tenth, and place the answer on the line.', {'lo':3,'hi':4,'ans':3.5,'tol':0.03,'step':0.01,'ticks':0.1,'labels':[3,3.5,4]},
       'Look at the hundredths digit to decide which tenth is nearer.', ['3.48 sits between 3.4 and 3.5.', 'The hundredths digit is 8, so it rounds up.', '3.48 rounds to 3.5 — place the marker on the halfway mark.'],
       '**3.48 rounds to 3.5.** The 8 in the hundredths place pushes it up to the next tenth — and 3.5 is the halfway mark of this line.', 'Rounding and placing are the same skill: which mark is nearest?')

assert len(Q) == 12 and all(x['kind']=='slider' for x in Q)
# every answer is where the stem says it is
for x in Q:
    L = x['line']; assert L['lo'] <= L['ans'] <= L['hi'] and 0 < L['tol']
unit = {
  'id':'unit-m3nl', 'type':'unit', 'classId':'math', 'title':'Topic 3 · Decimals on the Number Line', 'status':'draft',
  'prep':True, 'round':12, 'quarter':1, 'libv':1, 'srcName':'Topic 3 (enVision G4) — place value and decimals, Drive', 'source':'added',
  'summary': {'from':'added','text':'Twelve decimals to place on a number line by dragging a marker: tenths on a line from 0 to 1, hundredths on zoomed-in lines, and two lines whose marks are halves rather than tenths. Right means within a hair of the spot.'},
  'why': {'from':'added','text':'Knowing where a decimal LIVES is different from reading it. Placing numbers on a line is the single best-evidenced way to build number sense, and it is exactly what comparing and rounding decimals rest on.'},
  'objectives': [
    {'from':'source','text':'Place a decimal to the tenths on a number line.'},
    {'from':'source','text':'Place a decimal to the hundredths on a zoomed-in line.'},
    {'from':'added','text':'Work out what one space is worth when the marks are not tenths.'}],
  'parentNote': {'from':'added','text':'A new question type: she drags a marker along a number line instead of picking an option, and the app checks whether she landed within a small tolerance of the right spot (about a third of a space). Two lines use halves rather than tenths as their marks, on purpose — the trap is counting marks without first asking what each one is worth, which is the same trap as reading a cylinder. The hundredths questions zoom the line in (0.3 to 0.4, say) so a thumb-width is never the difference between right and wrong on a phone. Never served in Beat the clock — dragging against a countdown tests dragging.'},
  'nextUp': {'from':'added','minutes':8,'text':'Twelve drags. Look at the labels before you touch the marker, and say the number out loud as you land it.'},
  'cards': C, 'questions': Q,
  'updatedAt': int(time.time()*1000) - 3*3600*1000,
}
path = os.path.join(REPO, 'content', 'math-t3-numberline.json')
json.dump({'v':1,'records':{unit['id']:unit}}, io.open(path,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', path, len(C), 'cards', len(Q), 'sliders')
