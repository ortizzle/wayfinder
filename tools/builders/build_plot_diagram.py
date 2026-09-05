# -*- coding: utf-8 -*-
"""Plot Diagram · Pixar Shorts — from the class's own quiz study guide (with
answers), English 4. Five stages applied to four shorts she watched in class:
Geri's Game, Partly Cloudy, Lifted, Piper. Every event below is the guide's own
beat, reworded only where the guide's shorthand needed a full sentence."""
import json, io, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

C, Q = [], []
card(C, 'Exposition', '**The beginning: who is in the story, where they are, and what is normal before anything changes.**'
     '\n• Geri\'s Game opens with two Geris at a park about to play chess.'
     '\n• Piper opens with a mother bird showing her chick how to find food by the ocean.',
     'Ex-position: the position everything starts in.')
card(C, 'Rising action', '**The events that build the problem up, one after another, toward the biggest moment.**'
     '\n• Usually several beats, not one.'
     '\n• In Lifted, every fumbled attempt to beam the sleeping man up is rising action.',
     'The tension rises — it is a climb.')
card(C, 'Climax', '**The turning point: the single most tense moment, where the problem comes to a head.**'
     '\n• Shy Geri faking a health scare is the climax of Geri\'s Game.'
     '\n• Piper copying the crab and burying herself as the wave comes is the climax of Piper.',
     'The peak of the mountain. Only one point is the top.')
card(C, 'Falling action', '**What happens right after the climax, as the problem starts to settle.**'
     '\n• The stork comes back to the storm cloud wearing football gear.'
     '\n• The supervisor alien sets the bedroom back the way it was.',
     'Coming down the other side of the mountain.')
card(C, 'Conclusion (resolution)', '**How it ends: the new normal, with the problem solved or settled.**'
     '\n• Shy Geri wins the game and the dentures.'
     '\n• The chick sleeps, well fed.',
     'Con-clusion: everything closes up.')
card(C, 'Telling the climax from the rising action', '**Rising action has many beats; the climax is one beat, and it is the one the whole story turns on.**'
     '\n• Ask: after this moment, does the problem start to resolve? If yes, that was the climax.'
     '\n• A big moment that only makes things worse is still rising action.',
     'If the story could still go either way afterwards, you are not at the top yet.')
card(C, "Geri's Game — the diagram", '**One old man plays chess against himself; the shy side wins by trickery.**'
     '\n• Rising: Aggressive Geri keeps winning and takes pieces; Shy Geri is losing; then Aggressive Geri has checkmate.'
     '\n• Climax: Shy Geri fakes a health injury and Aggressive Geri is worried.'
     '\n• Falling: Shy Geri spins the board. Conclusion: Shy Geri wins and gets the dentures.', frm='source')
card(C, 'Partly Cloudy — the diagram', '**A storm cloud makes dangerous babies; its stork keeps getting hurt.**'
     '\n• Rising: sunny clouds make nice babies; the storm cloud makes dangerous ones; the stork keeps getting hurt.'
     '\n• Climax: the stork leaves, and the storm cloud goes from angry to sad.'
     '\n• Falling: the stork returns with football gear. Conclusion: deliveries carry on, padded.', frm='source')
card(C, 'Lifted — the diagram', '**A trainee alien tries to abduct a sleeping man and cannot manage the controls.**'
     '\n• Rising: the trainee keeps fumbling; the man bangs off the walls; at last he floats up toward the ship.'
     '\n• Climax: the beam pulls him in, the trainee lets go, and the man falls with the door still open.'
     '\n• Falling: the supervisor puts everything back. Conclusion: the trainee is let fly the ship, crashes, and leaves with no human.', frm='source')
card(C, 'Piper — the diagram', '**A sandpiper chick learns to feed herself after a wave scares her.**'
     '\n• Rising: she tries alone, gets too close, a wave crashes over her, and she is afraid; she watches a crab burrow into the sand.'
     '\n• Climax: she copies the crab, buries herself, and stops being afraid of the water.'
     '\n• Falling: she can feed herself and shows the others. Conclusion: she sleeps, well fed.', frm='source')

def stage(lv, short, event, ans_stage, hint, why, tip):
    opts = ['Exposition','Rising action','Climax','Falling action']
    # 'Conclusion' appears as an option where it is the answer; keep four options
    if ans_stage == 'Conclusion': opts = ['Rising action','Climax','Falling action','Conclusion']
    ans = opts.index(ans_stage)
    steps = ['Place the moment on the story\'s mountain: is the problem still building, at its peak, or settling?',
             why, 'So this moment is the ' + ans_stage.lower() + '.']
    q(Q, lv, f'In {short}, which stage of the plot diagram is this moment: {event}', opts, ans, hint, steps,
      f'**{ans_stage}.** {why}', tip, frm='source')

stage(1, "Geri's Game", 'the two Geris are at a park, about to play chess.', 'Exposition',
      'Nothing has gone wrong yet.', 'It is the setup — who, where, and the normal before the problem starts.', 'Exposition is always before the first move of the problem.')
stage(2, "Geri's Game", 'Aggressive Geri keeps winning and Shy Geri is losing pieces.', 'Rising action',
      'Is this the single biggest moment, or one of several that build up?', 'The problem is getting worse beat by beat, which is what rising action does.', 'A story can have many rising-action beats and only one climax.')
stage(2, "Geri's Game", 'Shy Geri fakes a health injury and Aggressive Geri is worried.', 'Climax',
      'After this moment, does the problem start to resolve?', 'It is the turning point — everything after it goes Shy Geri\'s way.', 'The climax is the one moment the story turns on.')
stage(2, "Geri's Game", 'Shy Geri spins the board round.', 'Falling action',
      'The trick has already been played. What is this?', 'The tables have turned and the game is settling toward its end.', 'Falling action is the slide from the peak to the ending.')
stage(1, "Geri's Game", 'Shy Geri wins the game and gets the dentures.', 'Conclusion',
      'Is there anything left to solve?', 'The problem is over and the new normal is set — that is the conclusion.', 'Conclusion and resolution mean the same stage.')
stage(2, 'Partly Cloudy', 'the stork keeps getting hurt delivering dangerous animal babies.', 'Rising action',
      'This happens more than once.', 'Each injury builds the problem up; it is not yet the moment things turn.', 'Repeated beats that build tension are rising action.')
stage(3, 'Partly Cloudy', 'the stork leaves, and the storm cloud goes from angry to sad.', 'Climax',
      'What is the one moment the whole story turns on?', 'The stork leaving is the peak of the problem; after it, the story heads toward making up.', 'The climax can be quiet — it is the turning point, not the loudest moment.')
stage(2, 'Partly Cloudy', 'the stork comes back wearing football equipment.', 'Falling action',
      'The big moment has already happened. Is this settling things?', 'It is the problem being solved after the turning point.', 'Falling action answers the climax.')
stage(1, 'Partly Cloudy', 'sunny clouds and a storm cloud float in the sky with their storks.', 'Exposition',
      'Has any problem started yet?', 'This is the world of the story before anything goes wrong.', 'Exposition sets the scene.')
stage(2, 'Lifted', 'the trainee alien keeps hitting the sleeping man against the walls.', 'Rising action',
      'Is the story turning here, or getting worse?', 'The mistakes pile up — tension building is rising action.', 'Piling-up mistakes are a classic rising action.')
stage(3, 'Lifted', 'the trainee lets go of the switch and the man falls with the door still open.', 'Climax',
      'Which moment is the peak of the disaster?', 'This is the top of the mountain: the worst moment, after which the supervisor takes over.', 'Ask what comes right after — if it is cleanup, this was the climax.')
stage(2, 'Lifted', 'the supervisor alien puts the bedroom back the way it was.', 'Falling action',
      'The disaster has happened. What is this?', 'The mess is being settled — that is what comes after the peak.', 'Cleanup after the peak is falling action.')
stage(2, 'Lifted', 'the trainee is allowed to fly the ship, crashes it, and flies away with no human.', 'Conclusion',
      'Is the story finished after this?', 'It is how things end up — the abduction failed and the aliens leave.', 'An ending does not have to be happy to be the conclusion.')
stage(1, 'Piper', 'a mother sandpiper shows her chick how to find food by the ocean.', 'Exposition',
      'Nothing has gone wrong yet.', 'This is the normal life the chick starts with.', 'Exposition comes before the first problem.')
stage(2, 'Piper', 'a big wave crashes over the chick and she is scared to go near the water.', 'Rising action',
      'Is the problem solved here, or made?', 'The wave creates the problem; the story still has to turn.', 'The event that CAUSES the problem is rising action, not the climax.')
stage(3, 'Piper', 'the chick copies the crab, buries herself in the sand, and stops being afraid.', 'Climax',
      'Where does the fear turn into courage?', 'This is the turning point — after it, she can feed herself.', 'The moment the character changes is usually the climax.')
stage(2, 'Piper', 'the chick shows the other sandpipers how to find food.', 'Falling action',
      'Her fear is already gone. What is this?', 'It follows the turning point and settles the story down.', 'Sharing what she learned is the story settling.')
stage(1, 'Piper', 'the chick sleeps, well fed.', 'Conclusion',
      'Is there anything left to solve?', 'The problem is solved and the story closes.', 'A quiet ending is still the conclusion.')

# Two put-in-order questions: the guide's own beats, in order.
q(Q, 3, "Put these moments from Geri's Game in the order they happen.",
  ['Aggressive Geri keeps winning and taking pieces', 'Shy Geri fakes a health injury', 'Shy Geri spins the board round', 'Shy Geri wins the dentures'], 0,
  'Rising action, then climax, then falling action, then conclusion.',
  ['Start with the rising action: the pieces being lost.', 'Then the turning point: the fake injury.', 'Then the falling action: the board is spun.', 'Then the ending: the dentures.'],
  '**Losing pieces → the fake injury → spinning the board → winning the dentures.** That is rising action, climax, falling action, conclusion, in order.',
  'A plot diagram IS an order: if you know the stages, you know the sequence.', frm='source', kind='order')
q(Q, 3, 'Put these moments from Piper in the order they happen.',
  ['A wave crashes over the chick', 'The chick watches a crab burrow into the sand', 'The chick buries herself and stops being afraid', 'The chick shows the other birds how to find food'], 0,
  'Problem, then the clue, then the turning point, then the settling.',
  ['The wave makes the problem.', 'Watching the crab is the clue she needs.', 'Copying it is the turning point.', 'Teaching the others comes after she has changed.'],
  '**Wave → crab → burying herself → teaching the others.** The wave is rising action, the crab is still rising action, burying herself is the climax, teaching is falling action.',
  'Two rising-action beats in a row is normal — the climax is still only one moment.', frm='source', kind='order')

_balance(Q)
assert len(C) == 10 and len(Q) == 20

unit = {
  'id':'unit-plot', 'type':'unit', 'classId':'english', 'title':'Plot Diagram: Pixar Shorts', 'status':'draft',
  'quarter':1, 'libv':1, 'srcName':'Plot Diagram Quiz Study Guide — Pixar Shorts, with answers (Drive)', 'source':'source',
  'summary': {'from':'source','text':'The five stages of a plot diagram — exposition, rising action, climax, falling action, conclusion — applied to the four Pixar shorts from class: Geri\'s Game, Partly Cloudy, Lifted and Piper. Every event is one the study guide itself names.'},
  'why': {'from':'added','text':'Plot diagrams come back all year, for every story and novel. The skill is telling the climax from the rising action around it: many beats build the problem, but only one moment turns it.'},
  'objectives': [
    {'from':'source','text':'Name the five stages of a plot diagram in order.'},
    {'from':'source','text':'Place a moment from a story on the right stage.'},
    {'from':'added','text':'Tell the single climax from the rising-action beats around it.'}],
  'parentNote': {'from':'added','text':'Built from the class study guide with answers for the Plot Diagram quiz, which was dated 9/2 — so this is for the skill going forward (unit tests and every novel to come), not for that quiz. Every question is a beat the guide itself lists, placed on its stage the way the guide places it. The one idea worth a word: the guide marks the CLIMAX of Partly Cloudy as the stork leaving and the cloud turning sad, which is a quiet moment — she may expect the climax to be the loudest one. The sort set asks "before the climax or after?" for twelve moments, which is the quickest way to practise that.'},
  'nextUp': {'from':'added','minutes':12,'text':'Cards first for the five stages, then the quiz. Try the sort — before the climax or after it — when the quiz is done.'},
  'cards': C, 'questions': Q,
  'sorts': [{'id':'s-plot','title':'Before the climax, or after it?','a':'Before','b':'After','items':[
     {'t':"Geri's Game: Aggressive Geri takes one piece, then another",'k':'a','why':'The problem is still building — rising action comes first.'},
     {'t':"Geri's Game: Shy Geri spins the board",'k':'b','why':'The trick has already been played; this is the slide to the ending.'},
     {'t':"Geri's Game: Shy Geri gets the dentures",'k':'b','why':'The ending is the last thing on the diagram.'},
     {'t':'Partly Cloudy: the stork is bitten by a baby crocodile',' k':'a','k':'a','why':'One of the injuries that build the problem up.'},
     {'t':'Partly Cloudy: the stork returns wearing football gear','k':'b','why':'This settles the problem — it follows the turning point.'},
     {'t':'Partly Cloudy: the sunny clouds hand out puppies and kittens','k':'a','why':'Part of the setup and early build-up.'},
     {'t':'Lifted: the trainee bangs the sleeping man into the wall','k':'a','why':'A fumble that builds tension — the story has not turned yet.'},
     {'t':'Lifted: the supervisor sets the bedroom back','k':'b','why':'Cleanup comes after the peak.'},
     {'t':'Lifted: the trainee crashes the ship and flies off','k':'b','why':'The ending.'},
     {'t':'Piper: a wave crashes over the chick','k':'a','why':'This causes the problem; the turning point is still to come.'},
     {'t':'Piper: the chick watches a crab dig into the sand','k':'a','why':'The clue arrives before the turn — she has not copied it yet.'},
     {'t':'Piper: the chick teaches the other birds','k':'b','why':'She has already changed; this is the settling.'}]}],
  'updatedAt': int(time.time()*1000) - 3*3600*1000,
}
for it in unit['sorts'][0]['items']: it.pop(' k', None)
path = os.path.join(REPO, 'content', 'english-plot-diagram.json')
json.dump({'v':1,'records':{unit['id']:unit}}, io.open(path,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', path, len(C), 'cards', len(Q), 'questions', 'ans spread', [sum(1 for x in Q if x.get('kind')!='order' and x['ans']==i) for i in range(4)])
