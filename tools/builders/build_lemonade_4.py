# The Lemonade Crime · Ch. 14-16 — reading companion 4 of 4 (the ending).
# Source: the OCR'd Google Doc of "Lemonade Crime Chapters 10-14.pdf", which
# actually runs to the end of the book (pp. 119-152).
import json, io, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance

C, Q = [], []

# ---------------------------------------------------------------- vocabulary
card(C, 'fighting words',
     "**Words that are so venomous and full of malice that they cause another person to fight back physically. Fighting words are not protected as free speech under the First Amendment.**\n"
     "• The book's own definition, at the top of chapter 14.\n"
     "• Venomous means poisonous; malice means wanting to hurt someone.\n"
     "• \"This is not over. You and me. On the court.\" — that is the whole chapter in one line.",
     "Some words are treated as the first punch, not as speech.")
card(C, 'balance',
     "**A device used for weighing that has a pivoted horizontal beam from which hang two scales. In statues and paintings, the figure of Justice is often shown holding a balance.**\n"
     "• The book's own definition, at the top of chapter 15.\n"
     "• Two meanings run through the chapter: the scales of justice, and Jessie standing on one foot in tree pose.",
     "Justice holds a balance. So does anyone standing on one leg.")
card(C, 'amends',
     "**Legal compensation (of money or other valuable assets) as a repair for loss, damage, or injury of any kind.**\n"
     "• The book's own definition, at the top of chapter 16.\n"
     "• Making amends is repairing the damage — not winning, not being proved right.\n"
     "• It is the last chapter title for a reason: it is the book's actual answer.",
     "Amends is about repair. A verdict was never going to do that.")

# ---------------------------------------------------------------- ch 14
card(C, "Evan's rules for the game",
     "**Play to seven by ones, straight up, king's court, clear the ball past the big crack — and no ref, no fouls.**\n"
     "• \"If the ball falls through the hoop, it's a point. If it doesn't, go home and cry to your mother.\"\n"
     "• \"No fouls\" sounds fair when you say it. It is the part that lets everything else happen.",
     "He wrote the rules. Notice which rule he leaves out.")
card(C, 'Revenge ball',
     "**Evan realises it himself, mid-game: \"He's right. This isn't basketball. It's revenge ball.\"**\n"
     "• He mauls Scott on the first play, plows him to the blacktop on the second, and runs it to six-nothing.\n"
     "• Scott's knees and elbow are bloody. Evan knows exactly what he is doing and keeps going.\n"
     "• The book does not let him off: he sees it clearly and chooses it anyway.",
     "He names what he is doing while he is doing it, and does not stop.")
card(C, "Megan won't watch",
     "**\"Why even call it basketball if you're going to play like that?\" — and then: \"This is gross. I'm going home.\"**\n"
     "• She asks Jessie to come with her. Jessie stays, sitting on the grass with her knees pulled up.\n"
     "• Evan notices her leaving and tells himself: Who cares?\n"
     "• He does care. That is the point of putting the thought in his head at all.",
     "The person he was trying to impress is the one who leaves.")
card(C, "Scott's only point",
     "**He fakes it — \"Oh, my god! Jessie, are you okay?\" — and drives past Evan while he turns to look.**\n"
     "• Paul calls it the oldest trick in the book.\n"
     "• It works because Evan does care about his sister, even in the middle of all this.\n"
     "• Scott cannot beat Evan for strength or speed, so tricking him is the only route left.",
     "The trick only works on someone who would actually turn around.")
card(C, 'The elbow, and the ball in the swamp',
     "**Evan could have simply won. Instead he sets up his turnaround jumper, throws an elbow into Scott's face, and sinks it — nothing but net.**\n"
     "• He wanted a shot people would tell stories about for years.\n"
     "• Nobody cheers. Nobody moves for the ball.\n"
     "• Scott gets up, drop-kicks the ball over the fence into the swamp, and runs.",
     "He got the shot he had practised for months, and it cost him everything he wanted.")

# ---------------------------------------------------------------- ch 15
card(C, "Jessie calls her grandmother",
     "**She tells her everything — the trial, the game, the ball in the swamp, Evan not eating — and then blurts out that she lied in court.**\n"
     "• Grandma listens to the whole story without interrupting once.\n"
     "• Her advice for the rest: let it go, and be the tree.",
     "She confesses to the person furthest from the playground.")
card(C, "Grandma's answer about the lie",
     "**\"Lying is wrong, but at least you did it from a good place in your heart. You don't need to feel ashamed about loving your brother.\"**\n"
     "• Then the harder half: feel bad for a while, always remember what you learned, move on and be a better person — but don't beat yourself up.\n"
     "• When Jessie says she still feels awful, Grandma says that is good. She would be worried if she didn't.",
     "It is neither 'you were terrible' nor 'it was fine'. Both halves matter.")
card(C, "What Jessie can and cannot control",
     "**\"Some things are beyond your control, Jessie. You need to learn to accept that. You can't run the whole world.\"**\n"
     "• But the lie is different: nobody can make you lie, so that part she does control.\n"
     "• That is the balance the chapter is named for — knowing which side of the line a thing sits on.",
     "The verdict was never hers. The lie was.")
card(C, 'Grandma is getting older',
     "**She sent Jessie the same book twice, and she thinks Jessie is seven when she has been eight for almost a year.**\n"
     "• Jessie asks why she forgets things now, when she never used to.\n"
     "• \"Oh, Jessie Bean, I'm getting old... And that's something neither of us has any control over.\"\n"
     "• It is a quiet, sad thread the book slips in without making a fuss of it.",
     "Read this one gently. It is not a joke about Grandma.")
card(C, 'Why Megan defended Scott',
     "**\"It wasn't really your trial. It was all of ours... in a real court of law, everyone has the right to a lawyer. Otherwise, the trial would have been a great big fake.\"**\n"
     "• She tells Jessie she did a great thing by giving them a real court, not a pretend one.\n"
     "• Jessie admits it out loud: \"I wanted to win. But you're right. You did the right thing.\"\n"
     "• And Megan still thinks Scott took the money. She just knows that isn't the same as proving it.",
     "The best defence of Scott came from someone who believed he was guilty.")
card(C, 'Be the tree',
     "**Jessie finds the yoga book, turns to page 48, lifts her left foot onto her right knee, and holds her balance for one blissful second.**\n"
     "• One second. The book does not pretend she has fixed anything.\n"
     "• It is the chapter title made literal: after all that, she finds a little balance.",
     "One second of balance is what the whole chapter builds to.")

# ---------------------------------------------------------------- ch 16
card(C, "Evan's fast",
     "**He goes almost twenty-four hours without food — not planned, not for a religion he belongs to.**\n"
     "• He started because he wondered whether Adam and Paul would make it through Yom Kippur, and whether he could.\n"
     "• The less he ate, the more he thought — sitting in his Climbing Tree, thinking about the Day of Atonement.\n"
     "• The rule he works out: when he feels really bad, it usually means he did something he regrets.",
     "He borrows someone else's holiday to think with.")
card(C, 'What Evan actually regrets',
     "**Not the trial — the basketball game.**\n"
     "• Every perfect shot loops through his head and makes him feel sick.\n"
     "• He works out that he is never going to know what happened to the money, and that crushing Scott was never going to change that.\n"
     "• So he puts on his baseball hat and rides to Scott's house with no plan beyond a handshake and an apology.",
     "He goes to apologise before he has any idea he will get anything back.")
card(C, 'The broken television',
     "**Scott throws a baseball across the room, it cracks the new TV, and his father erupts — and Evan steps in and says \"we\" did it.**\n"
     "• Mr. Spencer asks directly whether Evan threw the ball. He says no, but keeps saying we anyway.\n"
     "• Scott thanks him afterwards: \"my dad loves that TV. I mean, he really loves it. So thanks.\"\n"
     "• Evan's answer comes out before he can stop it: \"That's what friends do.\"",
     "He takes a share of blame that isn't his — the opposite of the whole trial.")
card(C, 'Not friends, not enemies',
     "**After he says it, Evan realises he does not know what he and Scott are: \"Not friends. But not enemies. Somewhere between. Someplace that didn't have a name, or even any rules.\"**\n"
     "• The whole book has been about rules — warrants, oaths, verdicts, fouls.\n"
     "• The thing that finally works between them has none.",
     "The book spends 150 pages on rules, then lands somewhere without any.")
card(C, 'The envelope',
     "**Scott unlocks the file cabinet, hands Evan the envelope with the $208 in it, and says: \"I'm sorry I stole your money.\"**\n"
     "• The jury had already found him not guilty. Nobody made him do this.\n"
     "• Evan expects to be furious and finds he isn't — he feels emptied out, with no anger left.\n"
     "• Asked why he took it, Scott shrugs: \"I don't know. 'Cause you had it, I guess.\"",
     "The confession arrives after the verdict, from someone who had already won.")
card(C, 'The Solemn Pact of Silence',
     "**The last page of the book is a contract signed by Evan, Jessie and Scott, swearing never to tell anyone — classmates or adults — what really happened to the $208.**\n"
     "• The matter is \"considered closed, now and forever.\"\n"
     "• The book that began with a warrant ends with another signed document. But this one is an agreement, not an accusation.",
     "First document: an arrest warrant. Last document: a promise between three people.")

# ---------------------------------------------------------------- ponder
card(C, 'Ponder: why did Scott take it?',
     "**\"I don't know. 'Cause you had it, I guess.\" Evan says it doesn't make sense to him — and the book agrees: \"But some things never do.\"**\n"
     "• Is that a good enough answer? Does a reason even exist?\n"
     "• Would knowing why have made Evan feel better?",
     "No wrong answers. Notice the book refuses to explain it, on purpose.",
     frm='added')
card(C, 'Ponder: was Evan right not to be angry?',
     "**He gets his money back and feels nothing — no triumph, no fury.**\n"
     "• Should he have been angry? Had he already used it all up on the basketball court?\n"
     "• And the harder one: does Scott deserve to be forgiven this easily?",
     "Try answering once as Evan, once as Jessie, and once as Megan.",
     frm='added')

# ---------------------------------------------------------------- questions
q(Q, 2, "Evan sets the rules for the basketball game himself. Which rule matters most for what follows?",
  ["No ref and no fouls",
   "First to seven points, counted by ones",
   "King's court, so the scorer keeps the ball",
   "Clear the ball past the crack in the blacktop"],
  0,
  "Ask which rule makes the rest of the chapter possible.",
  ["Evan lists several rules: seven by ones, straight up, king's court, clear past the crack.",
   "Then he adds: no ref, no fouls — just play.",
   "Without a referee, nothing Evan does can be called against him.",
   "That is what lets him maul, plow and elbow Scott without the game ever stopping."],
  "**No ref, no fouls.** It sounds like the fairest rule of the lot — nobody gets special treatment — and it is the one that removes every protection. Compare it with the trial, which had rules for everything.",
  "Scott agrees to it, which is why he can only complain, not stop the game.")

q(Q, 3, "Mid-game, Evan thinks: \"This isn't basketball. It's revenge ball.\" Why does the book have him notice it himself?",
  ["Because he understands exactly what he is doing and keeps doing it anyway",
   "Because he is looking for an excuse to stop the game early",
   "Because Scott says it first and Evan is agreeing with him",
   "Because he wants the crowd to know he is winning fairly"],
  0,
  "Think about the difference between not knowing and knowing.",
  ["Evan has run the score to six-nothing, and Scott is bloody and gasping.",
   "He looks at Scott and thinks: he's right, this isn't basketball, it's revenge ball.",
   "Then he keeps playing — and finishes with an elbow to Scott's face.",
   "So the book does not let him off as someone who got carried away without realising."],
  "**Because it makes him responsible.** A boy who doesn't realise what he is doing is out of control; a boy who names it and continues has chosen it. That is why he feels so awful afterwards.",
  "Notice it echoes Scott's own words back at him — Scott had called it dirt ball.")

q(Q, 2, "Scott scores his only point. How?",
  ["He shouts that Jessie is hurt, and drives past while Evan turns to look",
   "He waits until Evan is tired and then outruns him to the basket",
   "He shoves Evan out of the way while nobody is refereeing",
   "He makes a long shot from behind the clearing line"],
  0,
  "It works because of something true about Evan.",
  ["Scott cannot beat Evan for strength or for speed, so his only route is a trick.",
   "He stops dribbling and shouts: \"Oh, my god! Jessie, are you okay?\"",
   "Evan spins round to look for his sister — and Scott is past him and driving to the basket.",
   "Paul calls it the oldest trick in the book, but it only worked because Evan really would turn around."],
  "**He fakes an emergency about Jessie.** It is a cheap trick that depends on Evan being a decent brother — which he is, even in the middle of the ugliest thing he has ever done.",
  "It is the one moment in the chapter where Evan's better side costs him something.")

q(Q, 3, "Evan could have simply driven to the basket and won. Why does he set up the turnaround jumper instead?",
  ["He wanted a final shot people would talk about for years",
   "It was the only shot Scott could not block",
   "He wanted to prove his weak hand had improved",
   "He was too tired to run all the way to the basket"],
  0,
  "It is about the story afterwards, not about the point.",
  ["The game is already his; one easy shot would end it.",
   "He wants people telling the story of how Scott Spencer got crushed, for days and weeks and years.",
   "So he sets up the turnaround jumper he has practised for months.",
   "And he throws an elbow into Scott's face first, to make sure he gets the shot he pictured."],
  "**He wanted to be remembered for it.** The shot he had worked on since chapter 8 — the one his dad's advice was about — gets used for this. It goes in, nothing but net, and not one person cheers.",
  "His dad's line was about making yourself impossible to defend against. It says nothing about what to do with the skill.")

q(Q, 2, "Jessie tells her grandmother about the lie. What does Grandma say?",
  ["Lying is wrong, but she did it from a good place in her heart",
   "That she must confess it to the whole class on Monday",
   "That it was not really a lie because the trial was pretend",
   "That she should forget it, since nobody was harmed by it"],
  0,
  "Her answer has two halves that do not agree with each other.",
  ["Grandma listens to the entire story without interrupting.",
   "First half: lying is wrong, but at least she did it from a good place — she needn't be ashamed of loving her brother.",
   "Second half: feel bad for a while, remember what you learned, then move on and be a better person.",
   "And when Jessie says she still feels awful, Grandma says that is good — she'd be worried if she didn't."],
  "**That it was wrong, and that her reason still counts for something.** She neither excuses it nor crushes Jessie with it. Feeling bad is treated as the correct response, and also as something you are meant to walk out of.",
  "The one thing Grandma insists on: nobody can make you lie, so that part was genuinely Jessie's own choice.")

q(Q, 3, "Megan explains why she defended Scott. What is her reason?",
  ["It was everyone's trial, and a real court gives everyone a lawyer",
   "She had begun to believe that Scott was innocent",
   "Scott asked her to, and she felt sorry for him",
   "She wanted to prove she could argue better than Jessie"],
  0,
  "She tells Jessie what would have happened if she hadn't.",
  ["Megan says it wasn't really Jessie's trial — it was all of theirs.",
   "She tells Jessie she did a great thing by giving them a real court, not a pretend one.",
   "But in a real court everyone has the right to a lawyer, so somebody had to stand up for Scott.",
   "Without that, the whole trial would have been a great big fake."],
  "**Because a court where one side has no lawyer isn't a real court.** She was protecting Jessie's trial, not attacking it — and she still thinks Scott took the money. Believing someone is guilty and defending their rights turn out to be two different jobs.",
  "Jessie's reply is the honest one: \"I wanted to win. But you're right. You did the right thing.\"")

q(Q, 1, "The chapter called Balance ends with Jessie doing something. What?",
  ["Standing in tree pose and holding her balance for one second",
   "Weighing the evidence again on a set of kitchen scales",
   "Writing out a fair verdict of her own and signing it",
   "Splitting the lemonade money evenly between herself and Megan"],
  0,
  "Her grandmother had told her twice to be the tree.",
  ["Grandma keeps telling Jessie to let it go and be the tree.",
   "After Megan leaves, Jessie fetches the yoga book Grandma gave her and turns to page 48.",
   "She lifts her left foot onto her right knee and stands there.",
   "She holds her balance for one blissful second."],
  "**Tree pose, held for one second.** The chapter's title works both ways — the scales that Justice holds, and a girl on one leg. The book is careful not to claim she has sorted everything out. One second is what she gets.",
  "The definition of balance at the top of the chapter is about the scales of justice. That is not an accident.")

q(Q, 2, "Why does Evan go almost twenty-four hours without eating?",
  ["He wondered whether he could do it, and it got him thinking about atonement",
   "His mother grounded him after the fight on the basketball court",
   "He is Jewish and was observing Yom Kippur with his family",
   "He gave up his food to make amends to Scott"],
  0,
  "It started as curiosity, not as a punishment.",
  ["Adam and Paul were fasting for Yom Kippur, and Evan wondered if they would manage it.",
   "Then he wondered whether he had the strength to go twenty-four hours himself.",
   "He hadn't planned it — he just didn't eat, and by Saturday afternoon he wasn't even hungry.",
   "The less he ate, the more he thought, sitting up in his Climbing Tree, about the Day of Atonement."],
  "**Curiosity that turned into thinking.** He is not Jewish and says so; he borrows the shape of someone else's holiday because it gives him a way to think about what he has done. The fasting is what slows him down enough to work it out.",
  "Adam's apology in chapter 6 planted this. Evan laughed at it then.")

q(Q, 3, "Evan rides to Scott's house to apologise. What does he actually say when the door opens?",
  ["\"I wanted to see your new 20/20\"",
   "\"I'm sorry about the basketball game\"",
   "\"I know you took the money\"",
   "\"Can we just forget the whole thing?\""],
  0,
  "He had no plan, and Scott's face was full of hatred.",
  ["Evan has no speech ready — just a vague idea that a handshake and an I'm sorry are coming.",
   "Scott opens the door with a look of pure hatred and asks what he wants.",
   "Evan's mind goes blank, and the only thing he can think of is asking to see the 20/20.",
   "It changes everything: Scott's arms loosen, he says okay, and lets him in."],
  "**He asks to see the 20/20.** It is not the noble line he intended, and it is the one that works — because Scott has always liked showing off his new things. Sometimes the door opens on something ordinary rather than something brave.",
  "The apology does come. It just comes much later, after something else has happened first.")

q(Q, 2, "Scott's baseball cracks the new television and his father erupts. What does Evan do?",
  ["He says \"we\" did it, taking a share of blame that isn't his",
   "He tells Mr. Spencer that it was Scott who threw the ball",
   "He slips upstairs and goes home before anyone notices him",
   "He offers to pay for the broken television out of the $208"],
  0,
  "Mr. Spencer asks him directly whether he threw it.",
  ["Scott chucks the baseball, his aim is off, and it cracks the screen.",
   "Mr. Spencer runs downstairs shouting that Scott will pay for it out of his allowance and birthday money.",
   "Evan steps sideways toward Scott and says: we're sorry, we didn't mean to do it, it was an accident.",
   "Asked directly whether he threw the ball, Evan says no — but keeps saying we anyway."],
  "**He shares the blame on purpose.** It is the exact opposite of everything the trial was for: instead of proving who was responsible, he deliberately blurs it to protect someone. And it is the moment that changes things between them.",
  "Scott thanks him for it afterwards, and Evan answers without thinking: \"That's what friends do.\"")

q(Q, 2, "How does Evan get his $208 back?",
  ["Scott unlocks a cabinet, hands it over, and apologises",
   "The jury reverses its verdict after Scott confesses",
   "Mr. Spencer finds the envelope and returns it himself",
   "Jessie tracks the envelope down and gives it back"],
  0,
  "It happens after Evan has already given up on knowing.",
  ["Evan is at the top of the stairs, leaving, when Scott calls him back.",
   "Scott takes a key from his pocket and unlocks the file cabinet in the corner.",
   "He pulls out Jessie's envelope — the one with the $208 in it — and hands it over.",
   "And he says: \"I'm sorry I stole your money.\""],
  "**Scott gives it back and admits it, after being found not guilty.** Nobody made him. The trial couldn't get it out of him and the basketball game couldn't either; being treated decently for five minutes did.",
  "Evan expects to be furious and isn't — he says he feels emptied out, with no anger left.")

q(Q, 3, "Evan asks Scott why he took the money. What is the answer, and what does the book do with it?",
  ["\"'Cause you had it, I guess\" — and the book never explains it",
   "Scott explains that his parents had cut off his allowance",
   "Scott says he only meant to borrow it and got scared",
   "Scott refuses to answer and Evan decides not to press him"],
  0,
  "Watch whether the book tries to explain it for us.",
  ["Evan asks straight out, holding the envelope.",
   "Scott shrugs and says he doesn't know — 'cause you had it, I guess.",
   "Evan thinks about it: Scott's parents buy him everything, so he didn't need the money.",
   "The book's own comment is one short line: it just didn't make sense to Evan. But some things never do."],
  "**\"'Cause you had it, I guess\" — and the book leaves it unexplained on purpose.** A tidier story would give Scott a sad secret reason. This one refuses, because sometimes there isn't one, and Evan has to live with that.",
  "That refusal is why the ending feels honest rather than neat.")

q(Q, 2, "The Lemonade Crime, ch. 14-16. Put these events in the order they happen.",
  ["Evan wins the basketball game and Scott kicks the ball into the swamp",
   "Jessie tells her grandmother that she lied in court",
   "Megan comes to the door and explains why she defended Scott",
   "Scott hands Evan the envelope with the $208 inside"],
  0,
  "The game, then Jessie's day, then Evan's.",
  ["Chapter 14 is the game: Evan wins seven-one and Scott kicks the ball over the fence.",
   "Chapter 15 opens the next day with Jessie on the phone to her grandmother, confessing the lie.",
   "Later in that same chapter Megan turns up at the front door.",
   "Chapter 16 is Evan's day — the fast, the ride to Scott's house, and the envelope."],
  "**Game, phone call, doorstep, envelope.** Two siblings, two days, two different ways of putting something right — and only one of them involved a court.",
  "Notice the book gives Jessie's repair and Evan's repair a chapter each.",
  kind='order')

q(Q, 2, "Which statement about the last three chapters is NOT true?",
  ["The jury meets again and changes its verdict to guilty",
   "Evan tells Mr. Spencer that he and Scott broke the television together",
   "Jessie admits to Megan that she had wanted to win",
   "Evan cancels nothing — Scott is the one who drops the Morning Meeting apology"],
  0,
  "Three of these happen. One is the tidy ending the book refuses to give.",
  ["The verdict is never revisited; Scott stays not guilty in the eyes of the class.",
   "Evan does say we about the television, and Mr. Spencer does ask him directly.",
   "Jessie does admit to Megan: \"I wanted to win. But you're right.\"",
   "And it is Scott who says to forget the Morning Meeting apology, not Evan."],
  "**The jury never reverses its verdict.** As far as class 4-O is concerned, Scott was found not guilty and that stands. What gets put right happens privately between three people, not in the court.",
  "That is why the last page is a private pact rather than a public announcement.")

q(Q, 3, "The book ends with a signed Solemn Pact of Silence. Why is that a fitting last page?",
  ["It opened with a signed accusation and ends with a signed agreement",
   "It proves that the three of them never really trusted each other",
   "It shows that Jessie is still in charge of all three of them",
   "It means the money was never really returned to Evan at all"],
  0,
  "Think about the first document in the book and the last.",
  ["The story began with Jessie serving Scott a written warrant for arrest.",
   "It ends with a contract signed by Evan, Jessie and Scott together.",
   "The first document was one person accusing another; the last is three people agreeing.",
   "They swear never to tell the class or any adult what really happened, and consider the matter closed."],
  "**It answers the warrant it began with.** Same family of paperwork, opposite purpose: an accusation against someone, versus a promise made with someone. That is the difference between a verdict and amends.",
  "It also means the class never learns the truth — which is worth arguing about.")

_balance(Q)

byid = {x['id']: x for x in Q}
byid['q0']['passage'] = ("fighting words (fiʼting würdz), n. Words that are so venomous and full of "
                         "malice that they cause another person to fight back physically. Fighting "
                         "words are not protected as free speech under the First Amendment.")
byid['q4']['passage'] = ("balance (bǎlʼǝns), n. A device used for weighing that has a pivoted "
                         "horizontal beam from which hang two scales. In statues and paintings, the "
                         "figure of Justice is often shown holding a balance.")
byid['q7']['passage'] = ("amends (ǝ-měndzʼ), n. Legal compensation (of money or other valuable "
                         "assets) as a repair for loss, damage, or injury of any kind.")

unit = {
    'id': 'unit-lc4', 'type': 'unit',
    'updatedAt': int(time.time() * 1000) - 4 * 3600 * 1000,
    'classId': 'english', 'quarter': 1, 'status': 'draft', 'book': True, 'capstone': True,
    'title': 'The Lemonade Crime · Ch. 14–16: Amends',
    'srcName': 'The Lemonade Crime, chapters 14–16 (full text in Drive)',
    'source': 'The Lemonade Crime (Jacqueline Davies), reading companion 4 of 4',
    'summary': {'text':
        "The last three chapters of The Lemonade Crime. Evan beats Scott seven to one in a basketball "
        "game he admits to himself is revenge ball, finishing with an elbow to the face; Megan walks off "
        "in disgust and Scott kicks the ball into the swamp. The next day Jessie phones her grandmother, "
        "confesses that she lied in court, and hears that it was wrong but done from a good place — then "
        "Megan comes to the door and explains that she defended Scott because a court without a lawyer "
        "for both sides would have been a fake. Evan spends nearly a day without eating, thinking about "
        "the Day of Atonement, and rides to Scott's house to apologise. He takes a share of the blame "
        "for a broken television, and Scott quietly gives him back the envelope with the $208 in it.",
        'from': 'source'},
    'why': {'text':
        "This is where the book pays off everything it has been setting up. The trial couldn't get the "
        "truth out and the fight couldn't either — what finally works is Evan standing next to Scott "
        "when Scott's father is shouting. Three words carry it: fighting words, balance, amends. The "
        "last one is the answer: not winning, not being proved right, but repairing what was damaged. "
        "It is worth reading slowly, because the book deliberately refuses to explain why Scott did it.",
        'from': 'added'},
    'objectives': [
        {'text': "Define fighting words, balance and amends using the book's own definitions.", 'from': 'source'},
        {'text': "Explain what 'revenge ball' means and why it matters that Evan names it himself.", 'from': 'source'},
        {'text': "Say what Jessie's grandmother tells her about the lie, and why it has two halves.", 'from': 'source'},
        {'text': "Explain Megan's reason for defending Scott, in her own terms.", 'from': 'source'},
        {'text': "Describe what finally gets Scott to return the money, and why the trial could not.", 'from': 'added'},
    ],
    'parentNote': {'text':
        "The last of four reading-companion units, covering chapters 14–16 — the whole ending, so it "
        "should only be approved once she has finished the book. Built from the full text. Three things "
        "worth a conversation. First, chapter 14 is genuinely rough: Evan hurts Scott repeatedly in a "
        "basketball game, knows exactly what he is doing while he does it, and the book does not excuse "
        "him — the questions here follow that lead rather than softening it. Second, the grandmother's "
        "answer about Jessie's lie is the best piece of moral guidance in the book (wrong, but from a "
        "good place; feel bad for a while, learn from it, then move on and don't beat yourself up), and "
        "it is worth reading aloud together. Third, Scott returns the money and apologises after being "
        "found not guilty, and when asked why he took it says only \"'Cause you had it, I guess\" — the "
        "book states outright that it never makes sense, and refuses to explain further. That refusal is "
        "deliberate and the ponder cards ask her about it rather than supplying an answer. Note the book "
        "ends with the three children agreeing never to tell any adult what happened, which is a fair "
        "thing to raise with her.",
        'from': 'added'},
    'nextUp': {'text': "Finish the book first — this one covers the ending. Then cards once, and a couple of quiz rounds.",
               'minutes': 20, 'from': 'added'},
    'cards': C, 'questions': Q,
}

path = '/home/user/wayfinder/content/lemonade-crime-4.json'
io.open(path, 'w', encoding='utf-8').write(
    json.dumps({'v': 4, 'records': {'unit-lc4': unit}}, ensure_ascii=False, indent=1))
lv = {1: 0, 2: 0, 3: 0}
for x in Q: lv[x['lv']] += 1
print('lemonade-crime-4.json  %2d cards · %2d questions  %s' % (len(C), len(Q), lv))
print('passages:', sum(1 for x in Q if x.get('passage')), '| order:', sum(1 for x in Q if x.get('kind') == 'order'))
