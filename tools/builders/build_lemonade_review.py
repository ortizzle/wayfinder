# The Lemonade Crime · Novel Test Review — a whole-book review for the novel
# test of 11/20 ("the whole book").
#
# SOURCE: the four shipped reading companions ONLY (content/lemonade-crime-1..4.json),
# which were built from the full text of the book and verified. No class material
# for the novel test was in Drive. Nothing here is written from memory of the
# book: every quoted passage is copied, character for character, out of those
# four files (the builder asserts it), and the plot-stage definitions are the
# ones her class's plot-diagram unit uses (content/english-plot-diagram.json).
#
# Book units assemble their dict themselves and borrow card()/q()/_balance()
# (see build_lemonade_2.py). Passages are attached AFTER _balance() by
# question id: _balance swaps options inside a question but never reorders
# questions, so ids stay stable.
import json, io, time, sys, os, re, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance, REPO

LC = []
for n in (1, 2, 3, 4):
    d = json.load(io.open(os.path.join(REPO, 'content', 'lemonade-crime-%d.json' % n), encoding='utf-8'))
    LC.append(list(d['records'].values())[0])

# What a passage may be copied from: a companion's passage plate or card text.
QUOTABLE = []
for u in LC:
    QUOTABLE += [x['passage'] for x in u['questions'] if x.get('passage')]
    QUOTABLE += [c['def'] for c in u['cards']] + [c.get('hint', '') for c in u['cards']]
LC_STEMS = [x['q'] for u in LC for x in u['questions']]
PLOT = list(json.load(io.open(os.path.join(REPO, 'content', 'english-plot-diagram.json'),
                              encoding='utf-8'))['records'].values())[0]

def P(lc, kind, ident, start=None, end=None):
    """Copy a passage out of a companion unit, never retype it. `kind` is
    'q' (a question's passage) or 'c' (a card's def); start/end cut a quote
    out of a card by its own first and last words."""
    u = LC[lc - 1]
    if kind == 'q':
        s = next(x['passage'] for x in u['questions'] if x['id'] == ident)
    else:
        s = next(c['def'] for c in u['cards'] if c['id'] == ident)
    if start:
        i = s.index(start); j = s.index(end, i) + len(end)
        s = s[i:j]
    assert any(s in t for t in QUOTABLE), s
    return s

PIGEONS    = P(1, 'q', 'q9')
CIRC       = P(3, 'q', 'q7')
PERJURY    = P(3, 'q', 'q4')
AMENDS     = P(4, 'q', 'q7')
IMPARTIAL  = P(2, 'q', 'q0')
NOFRIENDS  = P(4, 'c', 'c17', 'Not friends.', 'any rules.')
FAKE       = P(4, 'c', 'c12', "It wasn", 'great big fake.')
GRANDMA    = P(4, 'c', 'c9', 'Lying is wrong', 'loving your brother.')

# The class's plot-diagram vocabulary, read from her own plot unit so the
# words cannot drift from what she was taught.
STAGE = {c['term']: c['def'].split('**')[1] for c in PLOT['cards'][:5]}
for k in ('Exposition', 'Rising action', 'Climax', 'Falling action', 'Conclusion (resolution)'):
    assert k in STAGE, k

C, Q = [], []

# ------------------------------------------------------------ the plot diagram
card(C, 'Exposition',
     "**%s**\n"
     "• In this book: who Evan, Jessie, Scott and Megan are, the $208 that vanished at Jack's pool party, and the note about Scott's Xbox 20/20.\n"
     "• Your class quizzed chapters 1–5 as the exposition — it ends with Jessie serving Scott a warrant and setting a trial for Friday."
     % STAGE['Exposition'],
     "Ex-position: the position everything starts in.", frm='added')
card(C, 'Rising action',
     "**%s**\n"
     "• Your class quizzed chapters 6–10 as the rising action: the role cards, Megan's objection to the map, Evan's friends drifting to Scott's house, the playground courtroom, the first witnesses.\n"
     "• The trial keeps building after that: Evan admits taking the money from Jessie's lock box, Jessie lies under oath, Megan defends Scott, and the jury says not guilty."
     % STAGE['Rising action'],
     "The tension rises — it is a climb, one beat after another.", frm='added')
card(C, 'Climax',
     "**%s**\n"
     "• In this book there are two good answers: the trial's verdict, or the basketball game right after it.\n"
     "• For the game: after the verdict Evan calls out \"This is not over\", so things still get worse. After the elbow shot, he heads toward an apology.\n"
     "• For the trial: it is the biggest event the whole book builds toward. Ask which one your teacher uses, and in a short answer say why."
     % STAGE['Climax'],
     "If the story could still go either way afterwards, you are not at the top yet.", frm='added')
card(C, 'Falling action',
     "**%s**\n"
     "• In this book: Jessie phones her grandmother and confesses she lied in court.\n"
     "• Megan comes to the door and explains why she defended Scott.\n"
     "• Jessie holds tree pose for one second, and Evan goes almost a day without eating, thinking about the Day of Atonement."
     % STAGE['Falling action'],
     "Coming down the other side of the mountain.", frm='added')
card(C, 'Conclusion (resolution)',
     "**%s**\n"
     "• In this book: Evan rides to Scott's house, takes a share of the blame for the broken television, and Scott hands him the envelope with the $208.\n"
     "• The last page is the Solemn Pact of Silence, signed by Evan, Jessie and Scott."
     % STAGE['Conclusion (resolution)'],
     "Con-clusion: everything closes up.", frm='added')

# ------------------------------------------------------------ conflict and characters
card(C, 'The central conflict',
     "**Evan is certain Scott took his $208, and nobody can prove it.**\n"
     "• Everything against Scott is circumstantial: he went into Jack's house alone and left in a hurry. Nobody saw the money taken.\n"
     "• The trial is how the kids try to settle it. The money comes back through an apology, not a verdict.",
     "Certain and proved are two different problems. The whole book lives in the gap.")
card(C, 'Evan',
     "**The one who lost the money, and the one who has to change most.**\n"
     "• He tells his friends Scott took it, though he never saw it happen.\n"
     "• The pick-up sticks memory shows why he cannot let go: to him, Scott always comes out on top.\n"
     "• He wins the game with revenge ball, regrets it, and rides to Scott's house to apologize.",
     "Revenge at the start, amends at the end. Evan makes that whole trip.")
card(C, 'Jessie',
     "**Evan's younger sister, for whom rules and fairness are the way to handle a wrong.**\n"
     "• She serves the warrant, writes the judge's script, and works so hard it is due diligence.\n"
     "• Then she lies under oath to protect Evan: she breaks the rule she cares about most, for the person she cares about most.\n"
     "• She tells Megan, \"I wanted to win. But you're right. You did the right thing.\"",
     "She organizes against unfairness, and the book tests her on it.")
card(C, 'Scott Spencer',
     "**The accused: he boasts he bought the Xbox 20/20 with \"All my own money\", and that boast starts the case.**\n"
     "• Under oath he admits his parents bought it. That is a lie caught, but not proof he took anything.\n"
     "• Found not guilty, he later hands back the envelope and says \"I'm sorry I stole your money.\"\n"
     "• Asked why, he says only: \"'Cause you had it, I guess.\" The book never explains it.",
     "He confesses after he has already won. Nobody made him.")
card(C, 'Megan Moriarty',
     "**The friend who asks whether anyone actually saw it.**\n"
     "• Her test: \"Did you see him take the money or the candy bar?\"\n"
     "• She spots that Jessie's map is not symmetrical, then defends Scott when his mother drives away.\n"
     "• She still thinks Scott took the money. She knows thinking it is not the same as proving it.",
     "The best defence of Scott came from someone who believed he was guilty.")

# ------------------------------------------------------------ the legal words
card(C, 'The chapter titles are a trial, in order',
     "**Fraud → Revenge → Eyewitness → Hearsay → Accused → Impartial → Due Diligence → Defense → Bona Fide → Trial by Jury → Perjury → Sixth Amendment → Circumstantial Evidence → Fighting Words → Balance → Amends.**\n"
     "• Every chapter opens with a real legal term and the book's own definition.\n"
     "• The list walks the whole path of a real case, and it ends on Amends: making things right, not winning.",
     "The contents page is a map of the plot.")
card(C, 'Words for evidence',
     "**Eyewitness: someone who actually saw it. Hearsay: repeating what someone else said; rumor. Circumstantial evidence: indirect evidence that makes a person seem guilty.**\n"
     "• Nobody at the trial is an eyewitness to the money being taken.\n"
     "• Hearsay is not allowed as evidence in a court of law.\n"
     "• Jack's testimony is circumstantial: Scott went in alone and left in a hurry.",
     "Ask of any evidence: whose eyes saw this?")
card(C, 'Words for a fair trial',
     "**Impartial: taking no side. Trial by jury: peers decide. Sixth Amendment: the accused has the right to legal counsel. Perjury: purposely lying under oath.**\n"
     "• David Kirkorian is judge because he is impartial.\n"
     "• The Sixth Amendment is why Megan may defend Scott.\n"
     "• Being wrong under oath is not perjury. Lying on purpose is.",
     "Each word is a rule that makes a trial fair.")
card(C, 'Revenge and amends',
     "**Revenge answers harm with harm. Amends repairs the harm.**\n"
     "• Revenge is chapter 2, and its last line is \"Evan wanted revenge.\"\n"
     "• Fighting Words (chapter 14) is the revenge ball game.\n"
     "• Amends is the last chapter title, and the book's actual answer.",
     "Look at the second title and the last one. That is the book in two words.")

# ------------------------------------------------------------ themes
card(C, 'Not guilty is not the same as innocent',
     "**A fair trial can only decide what was proved, and nothing was proved.**\n"
     "• The kids followed all the rules and came out with an answer that felt wrong to almost everyone.\n"
     "• Later Scott admits he stole the money. The verdict was still fair: nobody saw anything.",
     "Not guilty means not proven.", frm='added')
card(C, 'Rumors are like pigeons',
     "**Evan's mom: \"Rumors are like pigeons. They fly everywhere and make a mess wherever they go.\"**\n"
     "• Evan told everyone Scott took the money, though he never saw it.\n"
     "• Even the stories about David Kirkorian are rumors nobody has checked.",
     "Before you repeat it, ask who saw it.", frm='added')
card(C, 'Fair, even when it costs you',
     "**Two characters choose fairness over their own side.**\n"
     "• Megan defends Scott, though she thinks he took the money.\n"
     "• Jessie rules it is \"Yes. It's... fair.\" for Megan to do it, against her own case.\n"
     "• Megan's reason: without a lawyer for both sides, \"the trial would have been a great big fake.\"",
     "Doing the right thing at your own expense is the hardest kind.", frm='added')
card(C, 'Two documents bracket the book',
     "**It starts with a warrant, an accusation. It ends with the Solemn Pact of Silence, an agreement.**\n"
     "• In between sits the Agreement of Atonement, which set the stakes for the trial.\n"
     "• The last page closes the matter \"now and forever.\"",
     "First document: an accusation. Last document: a promise.", frm='added')

# ------------------------------------------------------------ short answer
card(C, 'Short answer: answer it, then prove it',
     "**Answer the question in one sentence, then back it up with evidence from the book.**\n"
     "• Evidence is something that happens or something a character says. Name the moment.\n"
     "• Add one sentence saying how that evidence proves your answer.\n"
     "• \"Because the book says so\" is not evidence.",
     "Claim, evidence, explain. Three sentences is plenty.", frm='added')
card(C, 'A model short answer',
     "**Question: Why does Megan defend Scott? Answer: She believes everyone has the right to a lawyer, even someone she thinks is guilty.**\n"
     "• Evidence: she tells Jessie that without one, \"the trial would have been a great big fake.\"\n"
     "• Explain: she still thinks Scott took the money, so she is defending a fair trial, not Scott.",
     "Notice the explain sentence. It is what turns a quote into an answer.", frm='added')

# ------------------------------------------------------------ ponder
card(C, 'Ponder: was justice done?',
     "**The trial said not guilty. The money came back anyway, through an apology.**\n"
     "• Did the trial help at all, or did it only make things worse?\n"
     "• Is Scott forgiven too easily? Was Evan's apology enough for revenge ball?\n"
     "• Would knowing why Scott took it change your answer?",
     "No wrong answers. Notice whether 'justice' means a verdict or a repair.", frm='added')

# ============================================================ questions
STG = "Which stage of the plot is this?"

def stage(lv, moment, opts, ans, hint, steps, main, tip, frm='added'):
    q(Q, lv, moment + ' ' + STG, opts, ans, hint, steps, main, tip, frm=frm)

stage(1, "Evan and Jessie start the school year in the same fourth-grade class, because Jessie skipped third grade.",
      ['Exposition', 'Rising action', 'Climax', 'Falling action'], 0,
      "Is anything being built up yet, or are you meeting people?",
      ["The exposition shows who is in the story and what is normal.",
       "This moment introduces Evan and Jessie and their class.",
       "Nothing is being argued or fought over in it.",
       "So it is the exposition."],
      "**Exposition.** It sets up who the story is about and where they are.",
      "Meeting the characters is the exposition.")
stage(1, "Jessie hands out color-coded role cards at recess and names David Kirkorian as the judge.",
      ['Rising action', 'Exposition', 'Falling action', 'Climax'], 0,
      "Is the problem settling, or is a trial being built?",
      ["The trial has been set, but has not happened yet.",
       "Handing out the roles builds toward it.",
       "Your class quizzed chapters 6–10 as the rising action, and this is chapter 6.",
       "So it is rising action."],
      "**Rising action.** Each role handed out builds the problem up toward the trial.",
      "Getting ready for the big event is still the climb.")
stage(2, "Scott went into Jack's house alone, came down dressed and left in a hurry, a witness tells the jury.",
      ['Rising action', 'Climax', 'Falling action', 'Conclusion'], 0,
      "Does this testimony settle anything?",
      ["A witness testifying is part of the trial.",
       "Nothing is settled by it: nobody saw the money taken.",
       "The tension keeps building toward a verdict and beyond.",
       "So it is rising action."],
      "**Rising action.** The testimony adds to the case without turning the story.",
      "Many beats build; only one turns.")
stage(2, "The day after the game, Jessie phones her grandmother and admits that she lied in court.",
      ['Falling action', 'Rising action', 'Climax', 'Exposition'], 0,
      "Is this building the problem, or dealing with what already happened?",
      ["The trial and the game are over.",
       "Jessie is facing what she did, not starting something new.",
       "That is the problem beginning to settle.",
       "So it is falling action."],
      "**Falling action.** It comes right after the climax, as things start to settle.",
      "After the peak, characters deal with what happened.")
stage(1, "Scott unlocks the file cabinet, hands Evan the envelope with the $208 inside, and apologizes.",
      ['Conclusion', 'Exposition', 'Climax', 'Rising action'], 0,
      "Is the problem still open after this?",
      ["The whole book has been about the missing $208.",
       "Here the money comes back, with an apology.",
       "The problem is settled, and a new normal begins.",
       "So it is the conclusion."],
      "**Conclusion.** The problem the book opened with is finally settled.",
      "When the central problem is solved, you are at the end.")
q(Q, 2, "These four moments come from four different parts of the book. Which order do they come in?",
  ["The $208 vanishes from Evan's shorts at Jack's pool party",
   'Jessie serves Scott a homemade warrant for his arrest',
   'The jury finds Scott not guilty, and Evan calls out a challenge',
   'Scott gives Evan the envelope and says he is sorry'], 0,
  "Start with the crime, end with the money coming back.",
  ["The money goes missing before the book's school year starts.",
   "Jessie's warrant sets up the trial.",
   "The trial ends with the verdict and Evan's challenge.",
   "The envelope comes back in the last chapter."],
  "**Crime, warrant, verdict, envelope.** That is the whole book in four beats.",
  "Exposition, rising action, then the end: the order matches the plot diagram.",
  kind='order')
q(Q, 2, "From getting ready for the trial to the visit at the end: which order do these four moments come in?",
  ['Megan notices that the courtroom map is not symmetrical',
   "Evan admits he took the money from Jessie's lock box",
   'Evan wins the basketball game with an elbow and a jumper',
   'Evan tells Mr. Spencer that "we" broke the television'], 0,
  "Preparing, the trial, the game, the visit.",
  ["Megan sees the map while she and Jessie prepare for the trial.",
   "Evan's admission comes on the stand, during the trial.",
   "The basketball game follows the verdict.",
   "The television breaks when Evan visits Scott's house at the end."],
  "**Map, admission, game, television.** Preparation, trial, revenge, repair.",
  "When in doubt, place each event before or after the trial first.",
  kind='order')

q(Q, 1, "What is the central conflict that drives the whole book?",
  ['Evan is sure Scott took his $208, but nobody can prove it',
   'Jessie wants to be judge, but the class picks David instead',
   'Megan and Jessie fall out over who gets to sit on the jury',
   'Scott wants the Xbox 20/20, but his parents refuse to buy it'], 0,
  "What does everyone keep arguing about, from the first chapter on?",
  ["Evan's money went missing at Jack's pool party.",
   "He is certain Scott took it.",
   "Nobody saw it happen, so nobody can prove it.",
   "That gap between certain and proved drives the whole book."],
  "**Evan is sure Scott took the $208, and nobody can prove it.** Every event, the trial included, comes out of that.",
  "The central conflict is the problem that is not settled until the end.")
q(Q, 2, "Jessie turns Evan's quarrel with Scott into a trial with warrants, oaths and a jury. What drives her to handle it that way?",
  ['Rules and fairness are how she makes sense of a wrong',
   'She wants the Xbox 20/20 for herself if Scott loses',
   'Mrs. Overton has asked her to run a court for the class',
   'She is afraid that Evan will get into a fight at recess'], 0,
  "What is Jessie like, from her very first pages?",
  ["Jessie believes in rules and fairness more than anyone.",
   "When something is unfair, she organizes against it.",
   "A trial is the most organized kind of fairness she knows.",
   "So she runs the conflict like a courtroom."],
  "**Rules and fairness are how Jessie handles a wrong.** She learned how trials work from her mother's booklet and built one.",
  "A character's choices come from what they care about most.")
q(Q, 2, "Evan remembers Scott fetching his dad to stop a game of pick-up sticks the moment Evan got ahead. What does that memory explain about why Evan will not drop the case?",
  ['To him it is about Scott always coming out on top',
   "He thinks Scott's dad will pay back the $208 himself",
   'He wants to win back the pennies he lost that day',
   "He believes Scott's dad was the one who took the money"], 0,
  "Is the memory about money, or about something bigger?",
  ["In the memory, Scott changes the rules as soon as he starts losing.",
   "Evan noticed: betting was allowed until Scott lost.",
   "So the case is not really about $208 to Evan.",
   "It is about Scott always coming out on top."],
  "**For Evan the case is about Scott always coming out on top.** The pick-up sticks memory shows a pattern, not one wrong.",
  "Look for what a memory tells you about why a character acts now.")
q(Q, 3, "By the end of the book, which pair of beliefs does Megan hold at the same time?",
  ['Scott probably took the money, and he still deserved a lawyer',
   'Scott is innocent, so the not-guilty verdict was the right one',
   'Evan is the real thief, so Scott should not have been on trial',
   "The trial was fair, so Jessie's lie in court did not matter"], 0,
  "Did Megan defend Scott because she thought he was innocent?",
  ["Megan defends Scott at the trial.",
   "Afterwards she tells Jessie everyone has the right to a lawyer.",
   "She still thinks Scott took the money.",
   "So she believes both things: probably guilty, and owed a lawyer."],
  "**Megan thinks Scott probably took the money, and that he still deserved a lawyer.** She was defending a fair trial, not Scott.",
  "A character can believe two things that seem to pull apart. That is often the point.",
  frm='added')
q(Q, 3, "Scott hands back the $208 after the jury has already found him not guilty. Why does it matter that he does it after the verdict?",
  ['Nobody could make him do it, so the choice was his own',
   'The jury had ordered him to return it within a week',
   'His mother found the envelope and made him give it back',
   "Evan had threatened another basketball game if he didn't"], 0,
  "Once he was found not guilty, could anyone force him?",
  ["The not-guilty verdict means he does not owe anything by the rules.",
   "So nobody could make him return the money.",
   "He does it anyway, and apologizes.",
   "That makes the return his own choice."],
  "**Nobody could make him, so returning it was his own choice.** The repair comes from Scott, not from the trial.",
  "Ask what a character did when nothing forced them to.",
  frm='added')
q(Q, 1, "In the last chapter, why does Evan ride his bike over to Scott's house?",
  ['To apologize for how he played in the basketball game',
   'To demand the money back now that the trial is over',
   'To tell Scott that the jury reached the wrong verdict',
   'To return the gavel David had lent the court for trial'], 0,
  "What does Evan regret most after the game?",
  ["After the game, every shot loops through Evan's head and makes him feel sick.",
   "He works out that crushing Scott changed nothing about the money.",
   "He goes with no plan beyond a handshake and an apology.",
   "So he goes to apologize for the game."],
  "**To apologize for the basketball game.** He goes before he has any idea he will get anything back.",
  "The money comes back only after Evan sets out to make amends.")

q(Q, 2, "Scott left the pool, went into the house alone, and ran out saying he had to go home. Using this definition, why does that evidence fall short?",
  ['It makes Scott seem guilty, but nobody saw him take the money',
   'Jack is only repeating what another boy told him at the party',
   'Jack was lying on purpose after taking an oath in the court',
   'Scott was never inside the house at all on the day of the party'], 0,
  "Did anyone see the money being taken?",
  ["Circumstantial evidence makes a person seem guilty without showing the act.",
   "Scott going in alone and leaving fast points at him.",
   "But nobody saw him take the money.",
   "So it falls short of proof."],
  "**It points at Scott, but nobody saw him take the money.** That is exactly what circumstantial evidence is.",
  "Seeming guilty and being proved guilty are different.")
q(Q, 2, "Which of these would NOT count as perjury in a court?",
  ['A witness who honestly remembers the wrong day',
   'A witness who lies on purpose to protect her brother',
   'A witness who swears an oath, then invents a story',
   'A witness who knows the truth but says the opposite'], 0,
  "Look at the word 'purposely' in the definition.",
  ["Perjury is purposely lying in court after an oath.",
   "Lying on purpose, inventing a story, or saying the opposite of the truth all count.",
   "An honest mistake is not on purpose.",
   "So remembering the wrong day is not perjury."],
  "**An honest mistake is not perjury.** Perjury needs a lie told on purpose, like Jessie's.",
  "Being wrong and lying are different things.")
q(Q, 1, "Everyone says David Kirkorian keeps an envelope of his own toenail clippings, but nobody has actually seen it. Which chapter-title word fits that story?",
  ['Hearsay', 'Perjury', 'Eyewitness', 'Bona fide'], 0,
  "Did the story reach people through their eyes or their ears?",
  ["Nobody has seen the envelope.",
   "The story is passed on from person to person.",
   "Repeating what others say, with nobody to check it, is rumor.",
   "The book's word for that is hearsay."],
  "**Hearsay.** It reached people's ears, not their eyes, and nobody can check it.",
  "HEAR-say: heard, not seen.", frm='source')
q(Q, 2, "Scott's mother drives off, and Megan stands up to defend him. Which chapter-title word names the rule she is acting on?",
  ['Sixth Amendment', 'Due diligence', 'Fighting words', 'Circumstantial evidence'], 0,
  "Which rule says the accused gets a lawyer?",
  ["Scott has just lost his lawyer.",
   "Megan steps in so he is not left without one.",
   "The right to legal counsel comes from the Sixth Amendment.",
   "So that is the rule she is acting on."],
  "**The Sixth Amendment.** It gives anyone accused of a crime the right to legal counsel.",
  "Legal counsel means a lawyer.")
q(Q, 3, "The second chapter is called Revenge and the last is called Amends. What change in Evan do those two titles mark?",
  ['He goes from wanting to hurt Scott to repairing the harm he did',
   'He goes from trusting Scott to never speaking to him again',
   'He goes from losing his money to winning the trial in court',
   "He goes from being Jessie's lawyer to being Scott's lawyer"], 0,
  "What does revenge do, and what do amends do?",
  ["Revenge causes harm because you were harmed.",
   "Evan plays revenge ball and hurts Scott.",
   "Amends repair harm, and Evan rides over to apologize.",
   "So the titles mark his change from hurting to repairing."],
  "**From wanting to hurt Scott to repairing the harm he did.** The two titles bracket Evan's whole change.",
  "When a book's titles are chosen this carefully, the first and last are worth comparing.",
  frm='added')
q(Q, 3, "The jury says not guilty, and later Scott admits he stole the money. Was the jury wrong to say not guilty?",
  ['No: nothing was proved, and not guilty means not proven',
   'Yes: the jury should have trusted the five witnesses',
   'Yes: a jury must side with whoever was harmed by a crime',
   'No: the jury knew Scott would give the money back later'], 0,
  "What could the jury actually know on the day of the trial?",
  ["The witnesses only saw Scott go in and leave.",
   "Nobody saw the money taken, and it never turned up.",
   "A jury can only decide what is proved.",
   "So not guilty was the fair verdict, even though Scott took it."],
  "**No. Nothing was proved, and not guilty means not proven.** The verdict was fair even though it felt wrong.",
  "Not guilty and innocent are not the same words.",
  frm='added')
q(Q, 2, "Evan's mom compares rumors to pigeons. Which moment in the book is an example of the mess she means?",
  ['Evan tells friends Scott took it, though he never saw it happen',
   'Megan asks Evan whether he saw Scott take the money himself',
   'Jack tells the jury exactly what he saw Scott do that day',
   'Scott admits under oath that his parents bought the 20/20'], 0,
  "Which one spreads a story nobody checked?",
  ["A rumor is a story passed on that nobody has checked.",
   "Megan's question checks a story; it does not spread one.",
   "Jack and Scott speak about what they know firsthand.",
   "Evan spreads a story he never saw. That is the mess."],
  "**Evan tells everyone Scott took the money, though he never saw it.** Once it is out, it flies everywhere.",
  "Spreading a story is different from checking one.",
  frm='added')
q(Q, 2, "A short-answer question asks why Megan defends Scott. Which answer is strongest?",
  ['She thinks everyone gets a lawyer. She says without one the trial would be "a great big fake."',
   'She believes that Scott is innocent. She says so to the jury in her closing argument.',
   'She thinks everyone deserves a lawyer. That is just what she is like as a person.',
   'She defends Scott at the trial. In the book she stands up from the audience to do it.'], 0,
  "A strong answer gives a reason AND evidence from the book.",
  ["Look for an answer that says why, not just what.",
   "Then look for evidence: a moment or a quote.",
   "One answer is wrong: Megan never says Scott is innocent.",
   "Only one gives a correct reason with a quote from the book."],
  "**The answer with the reason and Megan's own words.** It answers why, then proves it.",
  "Claim, evidence, explain.",
  frm='added')
q(Q, 2, "Which piece of evidence best supports this claim: Jessie cares more about fairness than about winning her case?",
  ['She agrees it is fair for Megan to defend Scott, against her side',
   "She writes the arrest warrant with her grandmother's calligraphy pen",
   'She phones Megan four times so they will get to school on time',
   'She is given the nicknames Obsessie Jessie and the Queen of Fair'], 0,
  "Which one shows her choosing fairness when it costs her?",
  ["The claim is about fairness beating winning.",
   "Good evidence shows Jessie losing something for fairness.",
   "Letting Megan defend Scott hurts Jessie's own case.",
   "That is the moment that proves the claim."],
  "**She says it is fair for Megan to defend Scott, though it hurts her own case.** A nickname is someone else's opinion, not her choice.",
  "The best evidence is an action that costs the character something.",
  frm='added')
q(Q, 1, "Which of these would stop a judge from being impartial?",
  ['Being best friends with the person bringing the case',
   'Having never once sat inside a real courtroom before',
   'Being a fourth-grader in the class, not a grownup',
   'Collecting odd things at home, like old peach pits'], 0,
  "Impartial means taking no side.",
  ["An impartial judge has no favorite in the argument.",
   "Being best friends with one side gives the judge a favorite.",
   "Age, experience or odd hobbies do not pick a side.",
   "So friendship with the plaintiff is the problem."],
  "**Being best friends with one side.** That is why the judge had to be friends with neither Evan nor Scott.",
  "Ask: would this person want one side to win?")
q(Q, 3, "Jessie lies under oath to protect Evan. Which two things she cares about pull against each other in that moment?",
  ['The rules she believes in, and her love for her brother',
   'Winning the Xbox 20/20, and keeping Megan as a friend',
   "Her grandmother's advice, and Mrs. Overton's class rules",
   'Her closing argument, and getting home before dinner'], 0,
  "What does Jessie value most, and who is in trouble?",
  ["Jessie cares about rules and truth more than anyone.",
   "Evan has just admitted taking money and looks like a thief.",
   "She lies to protect him, breaking her own most important rule.",
   "So rules and love for Evan pull against each other."],
  "**Her rules and her love for her brother.** Her grandmother says lying is wrong, but she did it from a good place.",
  "An inner conflict is between two things a character values.",
  frm='added')
q(Q, 3, "At the very end, Evan thinks this about where he and Scott now stand. Why does the book leave them somewhere without any rules?",
  ['Rules ran the trial, but making things right needed something more',
   'Evan and Scott agree to quit playing basketball together for good',
   'Mrs. Overton finds out about the trial and bans any more of them',
   'Scott has broken so many rules that nobody trusts him any more'], 0,
  "What did all the rules in the book actually settle?",
  ["The book is full of rules: warrants, oaths, verdicts, fouls.",
   "The rules gave a fair verdict but settled nothing between the boys.",
   "What works is an apology and a returned envelope.",
   "That repair has no rules, which is the book's point."],
  "**Rules ran the trial, but making things right needed something more.** The thing that finally works between them has no rules.",
  "Endings often answer the question the whole book has been asking.",
  frm='added')
q(Q, 2, "Jessie's grandmother says this to her on the phone. What does she want Jessie to take from it?",
  ['The lie was wrong, but she can learn from it and move on',
   'The lie did not count, because the trial was only pretend',
   'She must tell the whole class at Morning Meeting on Monday',
   'She should never again try to help her brother with anything'], 0,
  "Grandma says two things at once. Find both halves.",
  ["Grandma says lying is wrong.",
   "She also says Jessie acted from a good place.",
   "Her advice is to feel bad for a while, learn, and move on.",
   "So: wrong, but something to learn from, not to be crushed by."],
  "**The lie was wrong, but she can learn from it and move on.** Both halves matter.",
  "Wise advice often holds two ideas together.",
  frm='source')

_balance(Q)
byid = {x['id']: x for x in Q}
def at(text_start, passage):
    hit = [x for x in Q if x['q'].startswith(text_start)]
    assert len(hit) == 1, text_start
    hit[0]['passage'] = passage
at("Scott left the pool", CIRC)
at("Which of these would NOT count as perjury", PERJURY)
at("The second chapter is called Revenge", AMENDS)
at("Evan's mom compares rumors", PIGEONS)
at("Which of these would stop a judge", IMPARTIAL)
at("At the very end, Evan thinks", NOFRIENDS)
at("Jessie's grandmother says this", GRANDMA)
at("By the end of the book, which pair", FAKE)

# ---- guards: fresh stems, and no passage that answers its own question
for x in Q:
    for s in LC_STEMS:
        r = difflib.SequenceMatcher(None, x['q'].lower(), s.lower()).ratio()
        assert r < 0.6, (round(r, 2), x['q'], s)
    assert x['opts'][x['ans']].lower() not in x['q'].lower(), x['q']
    if x.get('passage'):
        assert len(x['passage'].split()) <= 45, x['id']

unit = {
    'id': 'unit-lc-review', 'type': 'unit',
    'updatedAt': int(time.time() * 1000) - 4 * 3600 * 1000,
    'classId': 'english', 'quarter': 2, 'status': 'draft', 'libv': 1,
    'book': True, 'prep': True, 'round': 12,
    'title': 'The Lemonade Crime · Novel Test Review',
    'srcName': 'The Lemonade Crime reading companions, parts 1–4',
    'source': 'The Lemonade Crime (Jacqueline Davies), whole-book review for the novel test',
    'summary': {'text':
        "The whole of The Lemonade Crime in one review. Evan is certain Scott Spencer stole his $208 at "
        "Jack's pool party, and his sister Jessie turns the quarrel into a trial on the playground. The "
        "trial is fair and returns a verdict of not guilty that almost nobody believes. Evan wins a basketball "
        "game with revenge ball, regrets it, and rides to Scott's house to apologize, and Scott hands back "
        "the money. The review lays the book on a plot diagram, then covers the characters, the conflict, "
        "the legal words in the chapter titles, and the themes, with evidence.",
        'from': 'source'},
    'why': {'text':
        "The novel test covers the whole book, and your class has quizzed it by plot stage. Seeing all "
        "sixteen chapters on one plot diagram, and being able to back an answer with a moment from the "
        "book, is what a whole-book test asks for.",
        'from': 'added'},
    'objectives': [
        {'text': "Place the book's main events on a plot diagram: exposition, rising action, climax, falling action, conclusion.", 'from': 'added'},
        {'text': "Name the central conflict and say what drives Evan, Jessie, Scott and Megan.", 'from': 'source'},
        {'text': "Use the chapter-title legal words: hearsay, circumstantial evidence, perjury, impartial, Sixth Amendment, revenge, amends.", 'from': 'source'},
        {'text': "State a theme and support it with evidence from the book.", 'from': 'added'},
        {'text': "Write a short answer that answers the question and gives evidence.", 'from': 'added'},
    ],
    'parentNote': {'text':
        "A whole-book review for the Lemonade Crime novel test on Friday 11/20. It draws on all four "
        "reading-companion parts (chapters 1–5, 6–9, 10–13 and 14–16), and every quotation in it is copied "
        "from those parts. No class material for the novel test was in Drive, so it is built from the "
        "companion units, not from a study guide. It covers the ending, including who returns the money, so "
        "it is only for after she has finished the book. She has, since the test is on the whole book. "
        "It follows her class's own plot split: chapters 1–5 as the exposition and 6–10 as the rising "
        "action, from the two earlier quizzes. One call is ours, and worth checking with her teacher: the "
        "book's climax can be read two ways: the trial's verdict, or the basketball game after it (after the verdict "
        "Evan says 'This is not over', so by the plot-diagram test the problem has not started to settle yet). "
        "Her teacher's answer is not in Drive, so the climax card gives both readings and tells her to explain "
        "her choice, and no quiz question depends on which one is right. "
        "Her class quizzes use short answer, so two cards (marked as study suggestions) practice answering "
        "and then giving evidence from the book.",
        'from': 'added'},
    'nextUp': {'text': "Cards once, saying each answer out loud before you flip. Then a quiz round or two.",
               'minutes': 25, 'from': 'added'},
    'cards': C, 'questions': Q,
}

path = os.path.join(REPO, 'content', 'lemonade-crime-review.json')
io.open(path, 'w', encoding='utf-8').write(
    json.dumps({'v': 4, 'records': {'unit-lc-review': unit}}, ensure_ascii=False, indent=1))
lv = {1: 0, 2: 0, 3: 0}
for x in Q: lv[x['lv']] += 1
print('lemonade-crime-review.json  %2d cards · %2d questions  %s' % (len(C), len(Q), lv))
print('passages:', sum(1 for x in Q if x.get('passage')), '| order qs:', sum(1 for x in Q if x.get('kind') == 'order'))
