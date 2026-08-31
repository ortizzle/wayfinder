# The Lemonade Crime · Ch. 10-13 — reading companion 3 of 4.
# Source: the OCR'd Google Doc of "Lemonade Crime Chapters 10-14.pdf" in
# River's Drive folder (pp. 85-118). Quoted passages are verbatim from it.
import json, io, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import card, q, _balance

C, Q = [], []

# ---------------------------------------------------------------- vocabulary
card(C, 'trial by jury',
     "**A legal proceeding in which the guilt or innocence of a person accused of a crime is decided by a group of his or her peers, rather than by a judge or panel of judges.**\n"
     "• The book's own definition, at the top of chapter 10.\n"
     "• Peers means equals — here, the other fourth-graders. Not the judge, and not a grownup.",
     "A jury of your peers means people like you decide, not an expert.")
card(C, 'perjury',
     "**Purposely telling a lie in a court of law after taking an oath to tell the truth and only the truth.**\n"
     "• The book's own definition, at the top of chapter 11.\n"
     "• The word 'purposely' is doing a lot of work: being wrong is not perjury. Lying on purpose is.",
     "An honest mistake under oath is not perjury. A deliberate lie is.")
card(C, 'Sixth Amendment',
     "**The part of the U.S. Constitution that explains the rights of anyone who is accused of a crime and brought to trial, including the right to legal counsel.**\n"
     "• The book's own definition, at the top of chapter 12.\n"
     "• Legal counsel means a lawyer. It is the rule Megan has been arguing for since she saw Jessie's map.",
     "It is the rule that says even someone everybody thinks is guilty gets a lawyer.")
card(C, 'circumstantial evidence',
     "**Indirect evidence that makes a person seem guilty. For example, if a suspect is seen running away from the scene of a crime, a jury might assume that he's guilty of the crime, even though no one saw him commit it.**\n"
     "• The book's own definition, at the top of chapter 13.\n"
     "• Everything against Scott is this kind: he went inside alone, came down dressed, and left in a hurry. Nobody saw him take anything.",
     "It points at someone without ever showing them doing it.")

# ---------------------------------------------------------------- ch 10
card(C, 'The jury stops being just kids',
     "**Evan knows every face in the jury box, but seeing them together as a jury makes them look unfamiliar — even Adam, his best friend.**\n"
     "• One at a time they are the kids he has known most of his life.\n"
     "• Together, in the box Jessie made of jump ropes, they have turned into something much bigger: the people who decide.",
     "A group can be something different from the people in it.")
card(C, 'Everyone agreed to the rules',
     "**Every fourth-grader turned up after school and put on a nametag — as if a whole new set of rules had appeared and everyone agreed to follow them.**\n"
     "• Even Malik, who taped his nametag to his backside, is standing in the witness box ready to testify.\n"
     "• That agreement is the only thing holding the court together. There is no grownup making anyone do this.",
     "The court is real only because everybody decided to treat it as real.")
card(C, 'Scott always spins it his way',
     "**Evan remembers playing pick-up sticks for pennies in first grade: the moment he got ahead, Scott fetched his dad, who stopped the game and made Evan give back everything he had won.**\n"
     "• Scott's rule was never spoken out loud — but Evan noticed. Betting wasn't allowed. Losing was.\n"
     "• It is why Evan cannot let this go: it is not really about $208, it is about Scott always coming out on top.",
     "Watch how Scott changes the rules once he starts losing.")

# ---------------------------------------------------------------- ch 11
card(C, "Jack's testimony",
     "**Both boys changed into borrowed swimsuits and left their clothes in Jack's room, and Scott went into the house alone, came down dressed, and left in a hurry.**\n"
     "• Jessie makes the jury hear one fact twice: Evan's shorts and Scott's shorts were in the SAME room.\n"
     "• Jack never saw anything taken. He only saw Scott go in and rush out.",
     "Every fact Jack gives is about opportunity, not about the act itself.")
card(C, 'Five witnesses, one story',
     "**Each boy says the same thing, and the book notes that hearing it five times made it seem like it was the absolute truth.**\n"
     "• That line is a warning, not a compliment.\n"
     "• Repeating a story does not add evidence to it. Five people describing the same door is still nobody seeing the money.",
     "Repetition feels like proof. It isn't.")
card(C, 'Jessie calls Evan — and it backfires',
     "**She puts Evan on the stand because everyone likes him, without planning a single question — and the court immediately demands the one question she was avoiding.**\n"
     "• Jurors and audience start chanting for it: where did Evan get all that money?\n"
     "• Jessie insists a lawyer picks her own questions, but David tells her he will end up answering it anyway. And he is right.",
     "She controlled everything about this trial except what people wanted to know.")
card(C, "Evan's answer",
     "**\"I took it from your lock box\" — Evan admits he took the $208 from Jessie in the first place.**\n"
     "• Jessie already knew and had forgiven him; the class did not know.\n"
     "• Then Megan asks whether half of it was hers from the lemonade stand. It was.\n"
     "• None of the background matters to the courtroom. In everyone's eyes, Evan looks like a thief.",
     "The trial dug up a truth nobody was hunting for.")
card(C, "Jessie's lie",
     "**\"He didn't steal it. I told him to take the money. I gave it to him for safekeeping.\" — said under oath, and untrue.**\n"
     "• She says it to protect Evan, in front of everyone.\n"
     "• She knows instantly what she has done, and so does everyone else. That is the chapter's word: perjury.",
     "She broke the rule she cared about most, for the person she cared about most.")

# ---------------------------------------------------------------- ch 12
card(C, "Scott's mother never gets out of the car",
     "**The SUV pulls up, Scott runs over, and it drives away — she has a big meeting. \"Real stuff, not kids' stuff.\"**\n"
     "• Scott shrugs it off twice and stares straight ahead, avoiding everyone's eyes.\n"
     "• He spent the whole week promising she would bury Jessie in court.",
     "He is not shrugging because he doesn't care.")
card(C, 'Megan defends Scott',
     "**She stands up from the audience and says \"That would be me\" when the judge calls for the defense lawyer.**\n"
     "• Evan is furious — he nearly shouts that she is supposed to be on his side.\n"
     "• Asked whether it is allowed, Jessie says: \"Yes. It's... fair.\" She rules against her own case.\n"
     "• Scott's answer to being offered a girl lawyer this time: \"You're all I got. I guess it's okay.\"",
     "Two people do the right thing here at their own expense.")
card(C, 'Winning by forfeit',
     "**Evan usually hates forfeit wins — he would rather play and lose — but he decides he will take this one any way he can get it.**\n"
     "• He is already picturing the 20/20 at his house with all his friends around.\n"
     "• Jessie, who should be delighted, is glum. She can already tell a win like this proves nothing.",
     "Notice which sibling is thinking about winning and which about the truth.")

# ---------------------------------------------------------------- ch 13
card(C, "Megan's method",
     "**She asks short yes-or-no questions aimed at one thing: did anyone actually SEE the money?**\n"
     "• Her first question to Jack — \"did you ever see the money in Evan's shorts pocket?\" — gets a plain no.\n"
     "• She is not arguing that Scott is innocent. She is showing that nobody knows.",
     "She never claims Scott didn't do it. That is the whole trick.")
card(C, 'Megan calls Scott to the stand',
     "**Her last witness is the defendant himself, and she asks one question: did you really pay for the Xbox 20/20 with your own money?**\n"
     "• Scott refuses, David threatens contempt, and Megan says quietly: \"Remember. You're under oath.\"\n"
     "• Scott: \"No. I didn't. You happy? My parents bought it for me.\"\n"
     "• So the boast that started the whole case was a lie — but it is not proof he took anything.",
     "His own lawyer catches him lying, and it still doesn't decide the case.")
card(C, 'The two closing arguments',
     "**Jessie asks the jury who they believe. Megan says nobody can know, because nobody saw anything and the money never turned up.**\n"
     "• Jessie never gets to use the closing argument she practised twenty times — there is no time left.\n"
     "• One argument asks for trust. The other asks for proof. The jury goes with proof.",
     "Two ways to end a case: who do you trust, or what can you show.")
card(C, 'The verdict',
     "**Not guilty — and nobody cheers except Scott.**\n"
     "• The book's own line: the kids followed all the rules and somehow came out with the wrong answer.\n"
     "• Jessie feels it, and she is sure everyone else does too.\n"
     "• Then Evan calls out: \"This is not over.\" And challenges Scott to the basketball court.",
     "A fair process can still land somewhere that feels wrong. Sit with that.")

# ---------------------------------------------------------------- ponder
card(C, 'Ponder: was the verdict wrong?',
     "**The jury followed every rule and reached a verdict almost nobody believed.**\n"
     "• Was the verdict wrong, or was it right that they could not prove it?\n"
     "• Those are two different questions. See if you can say which one you are answering.",
     "No wrong answers. But notice: 'not guilty' and 'innocent' are not the same words.",
     frm='added')
card(C, "Ponder: Jessie's lie",
     "**Jessie lied under oath to protect her brother, and she knew it was wrong while she was doing it.**\n"
     "• Would you have said it? Should she tell anyone?\n"
     "• Does it matter that it was for someone else and not for herself?",
     "Try answering once as Jessie and once as somebody in the jury box.",
     frm='added')

# ---------------------------------------------------------------- questions
q(Q, 1, "The book defines a trial by jury as one where guilt is decided by a group of the accused person's peers. Who are the peers in this trial?",
  ["Twelve of the fourth-graders from his own class",
   "The judge, David Kirkorian, deciding on his own",
   "The five witnesses who were at Jack's house",
   "Mrs. Overton and the other teachers on duty"],
  0,
  "Peers means equals — people like the person on trial.",
  ["A jury of peers means ordinary people like the accused, not experts and not a judge.",
   "Scott is a fourth-grader, so his peers are the other fourth-graders.",
   "Jessie hands out twelve jury cards and insists the jury be split evenly.",
   "The judge runs the trial but does not decide the verdict."],
  "**The twelve classmates in the jury box.** That is what makes it a trial by jury rather than a trial by judge — the deciding is done by equals, which is exactly why the verdict lands so hard on everyone.",
  "Evan notices they stop looking like his friends the moment they become a jury.")

q(Q, 2, "Jessie puts Evan on the stand without planning any questions. Why does she pick him, and what goes wrong?",
  ["Everyone likes him, but the court demands the question she was avoiding",
   "He saw Scott take the money, but he refuses to say so out loud",
   "He is the plaintiff, but the judge rules he cannot testify",
   "He had rehearsed with her, but he forgets the answers"],
  0,
  "Her reason is about how the jury feels, not about what he knows.",
  ["Jessie is feeling confident, and reckons a likable witness is good strategy.",
   "She has not written a single question for him.",
   "The jurors and audience immediately start shouting for the one thing she does not want asked: where Evan got the money.",
   "David tells her Evan will end up answering it anyway — and she knows he is right."],
  "**She picks him because he is well liked, and then loses control of the questions.** Her strategy worked on the wrong thing: she managed how the jury felt about her witness, not what they wanted to know.",
  "A lawyer chooses her questions, but she cannot choose what a room is curious about.")

q(Q, 3, "The book says that hearing the same story from five witnesses \"made it seem like it was the absolute truth.\" Why is that a warning rather than a compliment?",
  ["All five described the same door, and none of them saw the money taken",
   "The five witnesses had agreed on their story before the trial",
   "Five witnesses is fewer than a real court would require",
   "The witnesses were all friends of Evan and wanted him to win"],
  0,
  "Ask what each of the five actually saw with their own eyes.",
  ["Each boy says Scott went into the house alone, came down dressed and rushed off.",
   "That is the same observation repeated, not five different pieces of evidence.",
   "Not one of them saw money in Evan's pocket, or saw Scott take anything.",
   "So repeating it five times makes it FEEL more certain without making it more proven."],
  "**They all saw the same thing, and none of it was the crime.** Repetition feels like proof and isn't — the same trap Megan warned Evan about with rumours earlier in the book.",
  "This is why circumstantial evidence is so persuasive: it stacks up without ever showing the act.")

q(Q, 2, "What does Evan admit on the stand, and why does it damage his case so badly?",
  ["That he took the $208 from Jessie's lock box, so he looks like a thief himself",
   "That he never actually counted the money before the pool party",
   "That he had already forgiven Scott earlier that week",
   "That he asked Jessie to write the arrest warrant for him"],
  0,
  "The question the court forced was about where the money came from.",
  ["Pressed for where he got the money, Evan says he took it from Jessie's lock box.",
   "Jessie had already forgiven him, and half the money was Megan's without her knowing.",
   "But none of that background comes across in the courtroom.",
   "To everyone watching, the boy accusing someone of stealing turns out to have taken the money himself."],
  "**He took it from Jessie's lock box.** The context that would soften it — she forgave him, they earned Megan's share back — never reaches the jury. A courtroom flattens a complicated story into one bad-looking fact.",
  "Megan's follow-up, asking whether half of it was hers, is what makes the moment truly awful.")

q(Q, 3, "Jessie says under oath: \"He didn't steal it. I told him to take the money.\" Why is this perjury?",
  ["It is a deliberate lie told in court after taking an oath",
   "It is hearsay, because she is quoting somebody who is absent",
   "It is a guess she has no way of checking",
   "It is evidence she failed to share with the defense first"],
  0,
  "Check the definition's key word: purposely.",
  ["Perjury is purposely telling a lie in a court of law after swearing to tell the truth.",
   "Jessie did not tell Evan to take the money — she knows that as she says it.",
   "Being mistaken would not count; saying something she knows is false does.",
   "The book is blunt about it: she had just told a lie in court, and everyone knew it."],
  "**Because she said something she knew was false, on purpose, under oath.** Her reason was love rather than gain, and the book does not treat that as nothing — but it is still the thing the chapter is named for.",
  "Her grandmother's later verdict is worth waiting for: wrong, but done from a good place in her heart.")

q(Q, 2, "Scott's mother arrives at the playground. What actually happens?",
  ["She never gets out of the car — she has a meeting and drives away",
   "She defends Scott and cross-examines Evan sharply",
   "She refuses to take part because the trial is not real",
   "She arrives too late, after the verdict has been read"],
  0,
  "Watch what Scott does with his face afterwards.",
  ["A large grey SUV pulls up and Scott runs over, delighted.",
   "He talks to her through the window; the engine keeps running.",
   "The car drives away and Scott comes back and sits down on his basketball.",
   "He shrugs and says she has a big meeting — \"Real stuff, not kids' stuff\" — then avoids everyone's eyes."],
  "**She drives off without leaving the car.** He had promised all week that she would demolish Jessie, and the shrug is an act — Evan can tell. It is the first moment Scott is easy to feel sorry for.",
  "Notice it happens right after the chapter about the right to a lawyer.")

q(Q, 3, "Megan stands up to defend Scott. Jessie could have objected — why doesn't she?",
  ["Because a trial where only one side has a lawyer would not be fair",
   "Because the judge had already ruled that she could not object",
   "Because she was still ashamed of having lied a moment earlier",
   "Because she wanted the trial over before the jury had to leave"],
  0,
  "It is the rule Megan had already argued for over the map.",
  ["The Sixth Amendment gives anyone accused of a crime the right to legal counsel.",
   "Megan had already told Jessie the trial was not fair with a lawyer on only one side.",
   "David asks Jessie directly whether it is allowed.",
   "She nods and says: \"Yes. It's... fair\" — even though it costs her the easy win."],
  "**Because fairness required it, and she said so out loud.** It is the best thing Jessie does in the whole trial: she applies the rule against herself when nobody would have made her.",
  "That hesitation in \"It's... fair\" is the sound of someone choosing the rule over the win.")

q(Q, 2, "Megan's questions to the witnesses aim at one point. What is she trying to establish?",
  ["That nobody actually saw the money or saw it taken",
   "That Scott was never alone inside Jack's house",
   "That Evan made up the amount of money he lost",
   "That the witnesses had rehearsed their story together"],
  0,
  "She asks for one-word answers on purpose.",
  ["She starts with Jack and asks for yes or no answers only.",
   "Her first question is whether he ever saw the money in Evan's shorts pocket. No.",
   "She is not trying to prove Scott innocent, or to catch anyone lying.",
   "She is showing the jury that the whole case rests on what people assumed rather than saw."],
  "**That nobody saw anything.** She never argues Scott didn't do it — she argues nobody can know. That is a defense built exactly on the chapter's word: all the evidence is circumstantial.",
  "It is a much harder argument to beat than claiming innocence would have been.")

q(Q, 3, "Megan calls Scott himself as her last witness and asks whether he paid for the 20/20 with his own money. What happens, and why doesn't it settle the case?",
  ["He admits his parents bought it — but that still is not proof he took the money",
   "He admits taking the money, and the judge stops the trial",
   "He refuses to answer, so the jury has to assume he is guilty",
   "He proves he paid for it, which clears him completely"],
  0,
  "Separate the boast from the crime.",
  ["Scott does not want to answer; David threatens to hold him in contempt.",
   "Megan reminds him quietly that he is under oath.",
   "Scott admits it: his parents bought the 20/20 for him.",
   "So the boast that started the case was false — but a lie about who paid is not evidence that he stole $208."],
  "**He admits his parents bought it, and it still proves nothing about the theft.** The whole case began with Jessie's note asking where he got the money for it — and the answer turns out to be unrelated to the crime.",
  "His own lawyer got him to admit a lie. It is the most surprising move in the trial.")

q(Q, 2, "How do the two closing arguments differ?",
  ["Jessie asks the jury who they believe; Megan says nobody can know",
   "Jessie lists the evidence; Megan attacks the witnesses' honesty",
   "Jessie appeals to the judge; Megan appeals to the jury",
   "Jessie asks for mercy; Megan asks for a harsher punishment"],
  0,
  "One is about trust and the other is about proof.",
  ["Jessie runs out of time and never reads the argument she practised twenty times.",
   "She tells the jury the facts are the facts, and asks who they believe: Evan or Scott.",
   "Megan says there is no proof, nobody saw anything, and the money never turned up.",
   "So one closing asks the jury to trust a person, the other asks what can actually be shown."],
  "**Trust versus proof.** The jury goes with proof. Jessie's argument is the more emotionally satisfying one, and it loses — which is much of what this book is about.",
  "Jessie's index cards stay in her pocket. She never gets to use them.")

q(Q, 3, "After the not-guilty verdict, the book says the kids \"followed all the rules—but somehow come out with the wrong answer.\" What does that mean?",
  ["The process was fair, but the outcome still felt untrue to everyone there",
   "The jury broke a rule while huddled, which spoiled the verdict",
   "David read the verdict wrongly because he was in a hurry",
   "The trial was never real, so the verdict could not mean anything"],
  0,
  "Two different things can be judged here: how it was done, and where it landed.",
  ["The kids built a real court and ran it properly, start to finish.",
   "The verdict follows from the evidence: nothing was proven, so not guilty.",
   "Yet nobody cheers except Scott, and Jessie is sure everyone feels it.",
   "So a fair process produced an answer almost nobody believes is true."],
  "**A fair process can still land somewhere that feels wrong.** That is the uncomfortable idea the whole trial has been building to — and notice that 'not guilty' means not proven, which is not the same as innocent.",
  "Hold on to this feeling. The last chapters are the book's answer to it.")

q(Q, 1, "Why does Evan remember the game of pick-up sticks from first grade?",
  ["Because Scott fetched his dad and had the game stopped once Evan got ahead",
   "Because it was the first time Scott ever cheated him openly",
   "Because Scott's dad taught them both how to play it fairly",
   "Because Evan won eleven cents and Scott never paid him"],
  0,
  "Think about when in the game Scott went to get his father.",
  ["They were betting pennies, and at first Scott was winning.",
   "Then Evan caught up and got ahead by eleven cents.",
   "At that point Scott went and asked his dad to bring them a snack — and his dad stopped the game.",
   "Evan had to hand back everything he had won. Betting wasn't allowed; losing, he noticed, was."],
  "**Because Scott changed the game the moment he started losing.** It is why this is not really about $208 for Evan — it is about someone who always comes out on top, and never by accident.",
  "The memory arrives while Evan is sitting on a basketball waiting for his own trial to start. He is looking for a pattern.")

q(Q, 2, "The Lemonade Crime, ch. 10-13. Put these events in the order they happen.",
  ["David opens the court and Jessie calls Jack as her first witness",
   "Evan admits on the stand that he took the money from Jessie's lock box",
   "Scott's mother drives away and Megan volunteers to defend him",
   "Scott admits under oath that his parents bought the 20/20"],
  0,
  "Prosecution first, then the defense — and each side has one bad surprise.",
  ["Chapter 10 ends with David banging the gavel and opening court; Jessie calls Jack first.",
   "Chapter 11 is the prosecution's case, which collapses when Evan is forced to say where the money came from.",
   "Chapter 12 is the handover: Scott's mother leaves and Megan takes the defense.",
   "Chapter 13 is Megan's case, ending with Scott admitting under oath that his parents paid for the console."],
  "**Court opens, Evan's admission, Megan takes over, Scott's admission.** Each side has its case wrecked by its own witness — which is why the verdict satisfies nobody.",
  "Getting this order straight makes the last chapters much easier to follow.",
  kind='order')

q(Q, 2, "Which statement about the trial is NOT true?",
  ["Scott's mother cross-examines Evan before the verdict is read",
   "Megan asks Scott whether he paid for the 20/20 with his own money",
   "Jessie says it is fair for Megan to defend Scott",
   "David threatens to hold people in contempt to keep order"],
  0,
  "Three of these happen exactly as written. One never happens at all.",
  ["Scott's mother pulls up in the SUV but never leaves the car, and drives away.",
   "Megan does question Scott under oath about who paid for the console.",
   "Jessie does agree that Megan defending him is fair.",
   "David does threaten contempt more than once, and explains it means being sent home."],
  "**Scott's mother never questions anyone.** She never gets out of the car — which is exactly why Megan ends up defending him, and why the Sixth Amendment chapter matters.",
  "With a NOT-true question, test every option against the text instead of picking the first one that sounds off.")

q(Q, 2, "Evan usually hates winning by forfeit, but decides he will take this one. What does that tell you about him here?",
  ["He wants to beat Scott more than he wants a fair contest",
   "He has stopped caring about the trial altogether",
   "He believes Scott deserves a second chance",
   "He is worried the jury will not reach a verdict in time"],
  0,
  "Compare it with how he normally feels about forfeits.",
  ["Normally Evan would rather play and lose than win by forfeit.",
   "Here, with no defense lawyer for Scott, he decides he will take the win any way he can get it.",
   "He starts picturing the 20/20 at his house with all his friends around.",
   "So the thing he usually values — a real contest — he is willing to give up to beat Scott."],
  "**Winning has started to matter more to him than winning fairly.** The book plants this quietly, just before he challenges Scott to a basketball game. Keep it in mind for what happens on that court.",
  "Jessie, meanwhile, is glum about the same news. The two of them want different things now.")

_balance(Q)

byid = {x['id']: x for x in Q}
byid['q0']['passage'] = ("trial by jury (triʼǝl bi joorʼē), n. A legal proceeding in which the guilt "
                         "or innocence of a person accused of a crime is decided by a group of his or "
                         "her peers, rather than by a judge or panel of judges.")
byid['q4']['passage'] = ("perjury (pûrʼjǝ-rē), n. Purposely telling a lie in a court of law after "
                         "taking an oath to tell the truth and only the truth.")
byid['q6']['passage'] = ("Sixth Amendment (siksth ǝ-měndʼmǝnt), n. The part of the U.S. Constitution "
                         "that explains the rights of anyone who is accused of a crime and brought to "
                         "trial, including the right to legal counsel.")
byid['q7']['passage'] = ("circumstantial evidence (sûrʼkǝm-stǎnʼshǝl evʼi-dǝns), n. Indirect evidence "
                         "that makes a person seem guilty.")

unit = {
    'id': 'unit-lc3', 'type': 'unit',
    'updatedAt': int(time.time() * 1000) - 4 * 3600 * 1000,
    'classId': 'english', 'quarter': 1, 'status': 'draft', 'book': True,
    'title': 'The Lemonade Crime · Ch. 10–13: The Trial',
    'srcName': 'The Lemonade Crime, chapters 10–13 (full text in Drive)',
    'source': 'The Lemonade Crime (Jacqueline Davies), reading companion 3 of 4',
    'summary': {'text':
        "Chapters 10–13 of The Lemonade Crime: the trial itself. David opens court and Jessie calls her "
        "witnesses, who all tell the same story — Scott went into Jack's house alone and left in a hurry. "
        "Then Jessie puts Evan on the stand, the court demands to know where he got the money, and he "
        "admits he took it from Jessie's lock box. Jessie lies under oath to protect him. Scott's mother "
        "drives up and leaves without getting out of the car, so Megan stands up and defends Scott "
        "instead — asking one question at a time about what anyone actually saw, and getting Scott to "
        "admit under oath that his parents bought the Xbox 20/20. The jury returns a verdict of not "
        "guilty, and almost nobody believes it.",
        'from': 'source'},
    'why': {'text':
        "This is the heart of the book, and it does something braver than most stories for your age: the "
        "good guys run a fair trial and get an answer they hate. Four legal words carry it — trial by "
        "jury, perjury, Sixth Amendment, circumstantial evidence — and each one turns out to matter in a "
        "way nobody planned. Reading these chapters closely is what makes the ending land, because the "
        "last three chapters are the book's answer to the question this trial leaves open.",
        'from': 'added'},
    'objectives': [
        {'text': "Define trial by jury, perjury, Sixth Amendment and circumstantial evidence using the book's own definitions.", 'from': 'source'},
        {'text': "Explain why five witnesses telling the same story is not the same as five pieces of evidence.", 'from': 'source'},
        {'text': "Say what Jessie's lie was, and why the book calls it perjury rather than a mistake.", 'from': 'source'},
        {'text': "Explain why Jessie allows Megan to defend Scott even though it costs her the case.", 'from': 'added'},
        {'text': "Tell the difference between 'not guilty' and 'innocent'.", 'from': 'added'},
    ],
    'parentNote': {'text':
        "Third of four reading-companion units, covering chapters 10–13 — the trial from opening gavel to "
        "verdict. It stops before the basketball game that follows, so nothing spoils the ending. Built "
        "from the full text of those chapters; the four quoted definitions are the book's own wording. "
        "Two things in here are worth a conversation. First, Evan admits under oath that he took the $208 "
        "from Jessie in the first place (that is the plot of the previous book, The Lemonade War), and "
        "Jessie then lies in court to protect him — the unit names it as perjury and does not soften it, "
        "but also does not moralise, because chapter 15 has the grandmother handle it better than we "
        "could. Second, the trial is scrupulously fair and returns a verdict almost nobody believes, "
        "which the book states outright. The two ungraded ponder cards ask her about both rather than "
        "telling her what to think. Worth knowing that 'not guilty' means 'not proven' — that distinction "
        "is the point of the whole section, and it comes up again in the last chapter.",
        'from': 'added'},
    'nextUp': {'text': "Read through chapter 13 first — stop at the verdict. Then cards once, and a couple of quiz rounds.",
               'minutes': 20, 'from': 'added'},
    'cards': C, 'questions': Q,
}

path = '/home/user/wayfinder/content/lemonade-crime-3.json'
io.open(path, 'w', encoding='utf-8').write(
    json.dumps({'v': 4, 'records': {'unit-lc3': unit}}, ensure_ascii=False, indent=1))
lv = {1: 0, 2: 0, 3: 0}
for x in Q: lv[x['lv']] += 1
print('lemonade-crime-3.json  %2d cards · %2d questions  %s' % (len(C), len(Q), lv))
print('passages:', sum(1 for x in Q if x.get('passage')), '| order:', sum(1 for x in Q if x.get('kind') == 'order'))
