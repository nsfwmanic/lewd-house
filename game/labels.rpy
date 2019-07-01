label Prologue:
    scene bg MyRoom
    show LisaNeutral
    "This is your sister Lisa. She is the brains of the house. Her experiments might get out of hand, but alas that is the price of science."
    hide LisaNeutral
    show LisaTalk
    lisa "I need your assistance with something I’m working on."
    linc "Sure, I have time."
    "You agree to listen to what Lisa has to say."
    lisa "Not here. Let’s converse in my room."
    hide LisaTalk

    scene bg LilyLisaRoom
    "This is the shared room of your two youngest sisters. "
    show LisaNeutral
    linc "So what kind of weird experiment are you working on now?"
    hide LisaNeutral
    show LisaTalk
    lisa "Something that will be in your best interests to assist me with. You will see what I mean in the later stages of my experiment."
    lisa "I would like you to observe our other siblings."
    lisa "In particular, their general behavior and attitudes towards you."
    lisa "Report to me after you have talked with each one of them."
    hide LisaTalk
    show LisaNeutral
    linc "Observe and talk to them? That’s it?"
    hide LisaNeutral
    show LisaTalk
    lisa "Even one such as yourself should not have a problem doing this."
    hide LisaTalk
    show LisaNeutral
    linc "What’s the catch, how’s that different from our everyday lives?"
    hide LisaNeutral
    show LisaTalk
    lisa "I shall explain in more detail after you have returned and reported your observations."

    "Upon saying this Lisa pushes you out of the room."
    scene bg DoorClosed
    "As the door closes behind you, the sound of clinking vials and bubbling chemicals can be faintly heard from within."
    "Better leave Lisa to her work. Should go back to my room and get dressed."
    jump MyRoom

label TalkLori:
    show LoriNeutralOwnRoom
    "This is Lori."
    "She is oldest sister in the family."
    "Lori tends to be very condescending toward you."
    "She spends most of her time texting with her boyfriend, Bobby Santiago."
    hide LoriNeutralOwnRoom
    show LoriTalkOwnRoomBlush
    lori "How's it going, t-twerp?"
    hide LoriTalkOwnRoomBlush
    show LoriNeutralOwnRoomBlush
    linc "Hi, Lori. Just wanted to see how you were doing."
    hide LoriNeutralOwnRoomBlush
    show LoriTalkOwnRoomBlush
    lori "You look sort of different. Jeez, a-are you working out or something!?"
    hide LoriTalkOwnRoomBlush
    show LoriNeutralOwnRoomBlush
    linc "No, not really."
    hide LoriNeutralOwnRoomBlush
    show LoriTalkOwnRoomBlush
    lori "Well, it certainly looks like it. Literally any girl could go head of heels for..."
    hide LoriTalkOwnRoomBlush
    show LoriTalkOwnRoomBlush2
    lori "Ugh! What are you even doing here!? Stop talking to me, I'm busy"
    hide LoriTalkOwnRoomBlush
    show LoriNeutralOwnRoomBlush
    linc "Alright, I'll leave you to your own... thing."
    $ LoriAffection = 10
    $ TalkedLori = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LeniLoriRoom

label TalkLeni:
    show LeniNeutralOwnRoom
    "This is Leni, the second oldest sister of the house."
    "Although, she is not the smartest; she loves fashion and is gifted with her hands."
    "She is kind hearted but also very easily distracted."
    "Hey Leni!"
    hide LeniNeutralOwnRoom
    show LeniTalkOwnRoomBlush
    leni "Woah... Hey there~"
    leni "I like the new look! It's totes your style."
    hide LeniTalkOwnRoomBlush
    show LeniNeutralOwnRoomBlush
    linc "What do you mean? I don't look that different."
    hide LeniNeutralOwnRoomBlush
    show LeniTalkOwnRoomBlush
    leni "Wait, you don't? Aww jeez, have you always looked like this? I forget. Man, I've been missing out..."
    leni "I should, like, make some new clothes for you. You'll look totally hot."
    hide LeniTalkOwnRoomBlush
    show LeniNeutralOwnRoomBlush
    linc "Uh... thanks, I guess."
    hide LeniNeutralOwnRoomBlush
    show LeniTalkOwnRoomBlush
    leni "I'll see you later. I have a... top to, uh, un...button. Yeah. Bye~"
    hide LeniTalkOwnRoomBlush
    show LeniNeutralOwnRoomBlush
    linc "Okay. Bye, Leni."
    hide LeniNeutralOwnRoomBlush
    linc "That was weird, even for her."
    $ LeniAffection = 40
    $ TalkedLeni = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LeniLoriRoom

label TalkLuan:
    scene bg LuanWall
    show LuanNeutral
    "This is Luan. She’s The fourth-oldest sister in the family."
    "She loves telling puns which her other siblings do not enjoy."
    "Also, she is a frequent prankster."
    "Hey Luan, what’s going on?"
    hide LuanNeutral
    show LuanTalkBlush
    luan "Wow. I'd say you're looking sharp, but I think that'd sound a little dull!"
    luan "You are looking pretty nice today. That's no joke. Like, is it hot in here or is it just you?"
    hide LuanTalkBlush
    show LuanNeutralBlush
    linc "What?"
    hide LuanNeutralBlush
    show LuanTalkBlush
    luan "Ha ha, w-wow did I really got say that!? Ha, boy wasn't that a crazy joke!?"
    luan "You never know what's gonna come into my mouth- I mean out off!!"
    hide LuanTalkBlush
    show LuanNeutralBlush
    linc "What are you talking about?"
    hide LuanNeutralBlush
    show LuanTalkBlush
    luan "Welp, sorry to cut this short, but I'm really busy! So bye!"
    hide LuanTalkBlush
    show LuanNeutralBlush
    linc "Uh... bye?"
    $ LuanAffection = 30
    $ TalkedLuan = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LuanLunaRoom

label TalkLuna:
    scene bg LuanLunaBeds
    show LunaNude
    "This is Luna. She is the third-oldest sister in the family."
    "A free spirit with a very laid back attitude."
    "Luna loves rock music and hopes to become a famous rockstar."
    "Hey Luna, what’s up?"
    hide LunaNeutral
    show LunaTalkBlush
    luna "How's it hanging, little dude. Or, should I say big dude?"
    luna "Damn, you're rockin' that look, man!"
    hide LunaTalkBlush
    show LunaNeutralBlush
    linc "What look? This is just me, I-I think?"
    linc "Not really trying anything different... I guess I'm no always wearing that orange shirt 24/7 anymore."
    hide LunaNeutralBlush
    show LunaTalkBlush
    luna "Well whatever it is, it's paying off."
    luna "Dude, you don't even know the sorta things I'd..."
    hide LunaTalkBlush
    show LunaTalkBlush2
    luna "u-uh. Nevermind."
    luna "A-anyway, keep rockin' little big dude!"
    luna "I-I'm a bit busy right now, writing a new song, I'll just be h-here though. You know, if you need anything."
    hide LunaTalkBlush2
    show LunaNeutralBlush
    linc "Okay. Talk to you later, Luna."
    hide LunaNeutralBlush
    show LunaTalkBlush
    luna "Later, little bro."
    $ LunaAffection = 30
    $ TalkedLuna = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LuanLunaRoom


label TalkLynn:
    show LynnNeutral
    "This is Lynn. Athletic and competitive, this tomboy enjoys playing every existing sport."
    "She is also skilled in various forms of martial arts such as kickboxing and wrestling."
    "Which she is always willing to demonstrate on you as her practice dummy (emphasis on dummy)."
    hide LynnNeutral
    show LynnTalkBlush
    lynn "Hey! Nice to see you drop in, lady killer."
    hide LynnTalkBlush
    show LynnNeutralBlush
    linc "\"Lady killer\"? Huh. That's unusually nice of you to say."
    hide LynnNeutralBlush
    show LynnTalkBlush
    lynn "Who, me? Nah. I might give you a hard time, but you know I love ya... right, bro?"
    lynn "A-anyway, I was about to go for a jog. I'd love the company."
    hide LynnTalkBlush
    show LynnNeutralBlush
    linc "Sorry, I think I'll pass. I got some stuff to do."
    hide LynnNeutralBlush
    show LynnTalkBlush
    lynn "Yeah, that's cool. Ahh, you know what? Forget the jog, I'll just hang out here."
    lynn "See ya, man. I'll be here if you need me. Ha ha..."
    hide LynnTalkBlush
    show LynnNeutralBlush
    linc "I'll jog with you later, after I'm done. Promise."
    hide LynnNeutralBlush
    show LynnTalkBlush
    lynn "Thanks, bro. You're the best!"
    $ LynnAffection = 30
    $ TalkedLynn = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LucyLynnRoom

label TalkLucy:
    show LucyNeutral
    "This is Lucy. She is fifth-youngest sister in the family."
    "Her ability to appear out of nowhere and scare her other siblings is one of the few joys in her life."
    "Along with talking with the spirits of the underworld."
    "Hey, Lucy!"
    hide LucyNeutral
    show LucyTalkBlush
    lucy "Oh! I-It's you. Hello."
    hide LucyTalkBlush
    show LucyNeutralBlush
    linc "This a bad time?"
    hide LucyNeutralBlush
    show LucyTalkBlush
    lucy "I was just w-working on some writing. It's okay, though. I can gladly make time for you."
    hide LucyTalkBlush
    show LucyNeutralBlush
    linc "What is it you're writing about all the time, anyway?"
    hide LucyNeutralBlush
    show LucyTalkBlush
    lucy "A-a lot of them are about darkness and despair."
    lucy "Some are about love though. It's love that p-pushes us though the saddest parts of life."
    lucy "A-and sometimes love can be found in the strangest of place, but we need to just follow our hearts and say how we feel."
    hide LucyTalkBlush
    show LucyNeutralBlush
    linc "...O-okay. Whatever you say, Luce."
    hide LucyNeutralBlush
    show LucyTalk
    lucy "I-I'm sorry. I don't know why I t-told you all that. Just forget I said anything."
    hide LucyTalk
    show LucyNeutral
    linc "It's fine, Lucy. You know you can always talk about that stuff with me. Your big brother's got your back."
    hide LucyNeutral
    show LucySmileTalkBlush
    lucy "Thank you. If you want to drop back in to write with me, I'd love to have you."
    hide LucySmileTalkBlush
    show LucySmileBlush
    linc "Sure. A bit later though, I have to help Lisa with something."
    $ LucyAffection = 30
    $ TalkedLucy = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LucyLynnRoom

label TalkLola:
    show LolaNeutral
    "This is Lola. Bratty and conceited she is the third-youngest child in the Loud family."
    "Lola's interests include anything girly - this includes fashion shows, makeup, and posing for photo shoots."
    "Often participates and wins in beauty pageants."
    hide LolaNeutral
    show LolaAnnoyedTalkBlush
    lola "And what exactly do you want!?"
    lola "I happen to be in the middle of practicing my award winning pageant walk for the Little Miss Runway show next weekend."
    lola "So go be handsome somewhere else! It's very distracting!"
    hide LolaAnnoyedTalkBlush
    show LolaAnnoyedNeutralBlush
    linc "I was just checking up on- Wait, \"Handsome\"?"
    hide LolaAnnoyedNeutralBlush
    show LolaAnnoyedTalkBlush
    lola "D-don't let that get to your head or anything! I've just learned that's it's always important to appreciate beauty. T-that's all."
    lola "Now get out!"
    $ LolaAffection = 20
    $ TalkedLola = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LanaLolaRoom



label TalkLana:
    show LanaNeutral
    "This is Lana."
    "The fourth-youngest of the sisters, and the older of the family's two twin girls. Lana loves to play in mud, much to her twin Lola's annoyance."
    "Also, she doesn't mind digging through garbage."
    hide LanaNeutral
    show LanaTalkBlush
    lana "Woah, when'd you get so big, big bro!?"
    lana "You know, it's good you've reached your growth spurt now."
    lana "It'll be pretty important in the long run if you're looking for a job in manual labor, you know?"
    lana "Man, I still can't get over this. You look like a total different guy-"
    hide LanaTalkBlush
    show LanaNeutralBlush
    linc "Alright! Alright, stop gushing."
    hide LanaNeutralBlush
    show LanaTalkBlush
    lana "I-I'm not gushing, you dork. It's just cool to see you this tall a-and built."
    hide LanaTalkBlush
    show LanaNeutralBlush
    linc "Thanks, Lana. Need to go, got some stuff to do."
    hide LanaNeutralBlush
    show LanaTalkBlush
    lana "OK, I'll see you around. And maybe later today you can give me a piggyback ride!?"
    hide LanaTalkBlush
    show LanaNeutralBlush
    linc "Sure."
    $ LanaAffection = 30
    $ TalkedLana = True
    if TalkedLori == True and TalkedLeni == True and TalkedLuan == True and TalkedLuna == True and TalkedLynn == True and TalkedLucy == True and TalkedLana == True and TalkedLola == True:
        jump LisaFinal
    else:
        jump LanaLolaRoom





label LisaFinal:
    scene bg OutsideMyRoomHall
    "I should talk to Lisa."
    scene bg LilyLisaRoom
    show LisaNeutral
    linc "OK, they were all acting super weird. Though I kinda liked it, they were really nice to me."
    linc "Maybe a bit too nice."
    linc "Now, are you gonna tell me what you did, Lisa?"
    hide LisaNeutral
    show LisaTalk
    lisa "While you were all slumbering, I injected our sisters with a special serum I designed."
    lisa "A formula which triggers an accelerated production and release of oxytocin,"
    lisa "Along with the assisted stimulation of the erogenous zones of course."
    hide LisaTalk
    show LisaTalkSpit
    lisa "And, as I expected, our subjects exhibited attraction and a form of ritualistic behaviour of drawing in specimens of the opposite sex"
    lisa "such as compliments and sensual body language, towards a male they care about and deem most close to them."
    lisa "Which, again as I expected, is you, dear brother. I had some suspicions about Lori"
    lisa "But it seems that Bobby did not have such an impact on her as she wants us to believe."
    hide LisaTalkSpit
    show LisaNeutral
    linc "......"
    hide LisaNeutral
    show LisaTalk
    lisa "They are horny for you."
    hide LisaTalk
    show LisaNeutral
    linc "WHAT!?"
    linc "Wh...Why would you do that?"
    hide LisaNeutral
    show LisaTalk
    lisa "Gathering data for another experiment which is irrelevant, at least at the moment."
    lisa "Do not worry, their behaviour is temporary. A side effect of the increased amount of oxytocin in their body."
    lisa "They should return to normal tonight, or tomorrow morning at the latest. However, that takes us to the second phase of our experiment."
    lisa "Due to my formula our sisters will no longer resist seeing you as a copulative partner."
    lisa "They will still be relatively difficult to court just like any other human female"
    lisa "But they should slowly not be bothered by the idea of an incestuous relationship with you, or perhaps even be excited by it."
    lisa "So, dear brother, I want you to seduce our sisters. To whatever point you desire."
    hide LisaTalk
    show LisaNeutral
    linc "Lisa, that's insane! How could I do something like that, they're my sisters!"
    hide LisaNeutral
    show LisaTalk
    lisa "Please, Lincoln, I know everything about everyone in this house. I know how you've been thinking about our siblings, and not just because of puberty."
    hide LisaTalk
    show LisaNeutral
    linc "O-Oh... So you know. I'm sorry, Lis. I don't really know when I started feeling this way but I just can't help it."
    hide LisaNeutral
    show LisaTalk
    lisa "It's understandable considering your situation of being surrounded by 9 beautiful girls. I do not blame and and only want to help."
    lisa "Although I said 9, rest easy, I have done nothing to Lily. Even I have my limits in such experiments."
    lisa "There is no doubt, however, that she will grow into a fine female specimen so she should be taken in consideration in the years to come."
    hide LisaTalk
    show LisaNeutral
    linc "Hehe... y-yeah."
    linc "Anyway. Thanks, Lisa. So that formula of your is supposed to help me with... you know?"
    hide LisaNeutral
    show LisaTalkSpit
    lisa "Not by much. It's only the gateway, per se. Like I said, you will have to court them yourself just like any other girl."
    lisa "But I trust you can handle it. And perhaps I can offer some assistance in the future."
    hide LisaTalkSpit
    show LisaNeutral
    linc "I see. This is still a big decision to make. I'm not gonna lie, I want to do it but isn't... sex, you know, dangerous?"
    hide LisaNeutral
    show LisaTalk
    lisa "The only danger about incestuous intercourse is the posibility of procreation, but there are ways to prevent it. I, myself, can make sure of it."
    hide LisaTalk
    show LisaNeutral
    linc "That's reassuring, I guess."
    linc "Anyway, I have to go. Thanks again, Lisa. This was kind of weird but I guess I'm kinda weird myself."
    hide LisaNeutral
    show LisaSmileTalk
    lisa "Good luck in your endeavors. This may even prove to be... FON."
    hide LisaSmileTalk
    show LisaSmile
    linc "Also there are 10... I'm surrounded by 10 beautiful girls in this house."
    hide LisaSmile
    show LisaSmileBlush
    lisa "He's good."
    $ LisaAffection = 20
    return
    #jump MainHall
