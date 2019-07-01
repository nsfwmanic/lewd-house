### Weekly

#===========
###


label MondayStart:
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
    return


label LoriMondayMorning1:
    scene bg BathroomEntrance
    "Lori is in the bathroom"
    call screen Hall
    return

label LoriMondayMorning2:
    scene bg LoriBed
    show LoriTalk at default_sprite
    linc "Hey Lori, what's up?"
    lori "Hey twerp, just talking to Carol."
    lori "She's literally the best. I can't believe I thought of her as a total B for so long, but she's actually a total A."
    linc "I see... I think. Glad you're happy."
    lori "Anyway, what's up with you?"
    lori "Do you want me to drive you somewhere or something?"
    linc "No, it's not that, it's just..."
    linc "You see, I had a talk with dad right before he left and he said some stuff like how I should be the man of the house while he's gone and all that."
    linc "And how I should take care of \"my girls\" or something."
    linc "Still not quite sure what he means by all that but still, I thought you're my sisters and I love you so \"Why not?\", you know?"
    linc "That I should be there for you girls."
    linc "So, is there anything I can help you with?"
    lori "..."
    lori "That's really sweet, Linc, but I'm good right now. Thanks"
    lori "I'll definitely take you up on that though - you best be prepared for what you signed up for."
    linc "Yes, sir... ma'am."
    hide LoriTalk
    $ DayPhase += 1
    jump LeniLoriRoom
    return

label LoriMondayMorning3:
    scene bg LoriBed
    show LoriTalk at default_sprite
    linc "Hey Lor{nw}"
    lori "Not now, Lincoln."
    lori "I need to focus on this, it's harder than you think."
    linc "Okay..."
    hide LoriTalk
    $ DayPhase += 1
    return

label LoriMondayAfternoon1:
    scene bg LoriBed
    show LoriTalk at default_sprite
    linc "Hey girls, what you doing?"
    lori "What does it look like we're doing?"
    leni "We're taking some totes cute selfies."
    leni "*gasp* Linky!"
    linc "W-What, what's wrong Leni?"
    leni "You're totes cute. You should definitely take some selfies with us."
    linc "I don't think I..."
    leni "Aww, come on Linky, I promise we'll take the best seflies together. Right, Lori?"
    lori "Eh, why not?"
    lori "Come on, twerp, we'll let you share them to your loser friends too if you want."
    hide LoriTalk
    $ DayPhase += 1
    jump LeniLoriRoom

label LoriMondayAfternoon2:
    scene bg LivingRoomCenter
    show LoriTalk at default_sprite
    "Lori is reading a magazine here. I've been thinking that they would talk about it or do something in it like a survey or whatever, but I dunno what exactly."
    hide LoriTalk
    $ DayPhase += 1
    return

label LoriMondayEvening:
    scene bg LoriBed
    show LoriTalk at default_sprite
    "if selfies taken earlier"
    lori "Hey little bro, check it out"
    lori "Those selfies we took actually got a lot of likes. You're pretty popular."
    linc "Oh wow, that's actually kind of... awesome."
    lori "It's official then: From now on you are taking selfies with us."
    linc "Sorry, Lori, but I'm not really interested in any of this."
    lori "Well you should be, it's literally a win-win."
    lori "Just think about it, not many people can take advantage of the brother-sister dynamic. Plus I think little brothers are kinda popular right now?"
    linc "What?"
    lori "And you can brag about hanging out with three total babes."
    linc "Three?"
    lori "Carol will be there too. You don't wanna pass up an opportunity like that, do you?"
    linc "Well, I guess it wouldn't hurt."
    hide LoriTalk
    $ DayPhase += 1
    return

label LeniMondayMorning1:
    scene bg LeniBed
    show LeniTalk at default_sprite
    "{i}Leni seems to be brushing her hair{/i}"
    linc "Morning, Leni."
    leni "Oh, morning, Linky"
    leni "Whatcha doin?"
    linc "Nothing, just checkin up on you, that's all."
    linc "Something wrong?"
    leni "Ugh, these split ends just won't let up."
    leni "This is a complete disaster."
    linc "I can give you a hand if you want."
    leni "Aw, really?"
    leni "Yes, please. Thanks Linky."
    linc "No problem. I'm always here for you girls, just so you know. I'll try my best."
    leni "I know."
    linc "You do?"
    leni "Totes... cause it's you, silly, the best little brother ever."
    linc "Thanks, Leni"
    hide LeniTalk
    $ DayPhase += 1
    return

label LeniMondayMorning2:
    scene bg Kitchen
    show LeniTalk at default_sprite
    linc "Hey Leni, what you doing?"
    leni "Making a smoothie."
    leni "Do you want one?"
    leni "It will, like, make you super fresh and ready for the day."
    linc "Okay, sure."
    hide LeniTalk
    $ DayPhase += 1
    call screen Kitchen
    return

label LeniMondayMorning3:
    scene bg LeniBed
    show LeniTalk at default_sprite
    "{i}Leni seems to be focused on something{/i}"
    "{i}Hmm... wouldn't hurt to fool around a bit everynow and then, would it?{/i}"
    "Poking Leni's side"
    leni "Oh, Linky, it's just you"
    leni "Is there something on my dress?"
    linc "No, sorry, I just couldn't help myself when I saw you so focused on whatever."
    leni "That's okay. You can do it again if you want."
    linc "No, I'm good Leni, thanks."
    linc "What are you doing anyway?"
    leni "Oh I'm thinking what to wear for tomorrow's fashion show."
    leni "Think you can help me out a teeny tiny bit?"
    leni "I just need you to tell me how I look in these clothes."
    linc "I don't see any downsides to that so, sure!"
    leni "Thank you!"
    hide LeniTalk
    $ DayPhase += 1
    return

label LeniMondayAfternoon1:
    scene bg LeniBed
    show LeniTalk at default_sprite
    linc "Hey girls, what you doing?"
    lori "What does it look like we're doing?"
    leni "We're taking some totes cute selfies."
    leni "*gasp* Linky!"
    linc "W-What, what's wrong Leni?"
    leni "You're totes cute. You should definitely take some selfies with us."
    linc "I don't think I..."
    leni "Aww, come on Linky, I promise we'll take the best seflies together. Right, Lori?"
    lori "Eh, why not?"
    lori "Come on, twerp, we'll let you share them to your loser friends too if you want."
    hide LeniTalk
    $ DayPhase += 1
    return

label LeniMondayAfternoon2:
    scene bg LeniBed
    show LeniTalk at default_sprite
    "Leni is sorting out and working with some textiles. Best not take her out of it"
    hide LeniTalk
    $ DayPhase += 1
    return

label LeniMondayEvening:
    scene bg LeniBed
    show LeniTalk at default_sprite
    leni "*gasp*"
    linc "GEH... w-what now, Leni?"
    leni "You're the perfect size."
    linc "For what?"
    leni "Please please please I need you to try out something for me."
    leni "It won't take long, and you'll look totes adorbs."
    "{i}Who could say no to that face{/i}"
    linc "Alright, I'm in."
    leni "Yay!"
    hide LeniTalk
    $ DayPhase += 1
    return

label LunaMondayMorning1:
    scene bg LuanLunaBeds
    "{i}Luna is still asleep{/i}"
    $ DayPhase += 1
    return

label LunaMondayMorning2:
    scene bg LuanLunaBeds
    show LunaTalk at default_sprite
    luna "Hey bro, how's it hangin?"
    linc "Hey Luna. You writing a new song?"
    luna "Yeah, but I'm having a bit of a block. Just nothing's coming out."
    luna "So what's up, need anything?"
    linc "No... actually I was here to ask you that, if you need my help with something. Anything at all"
    linc "I've been thinking I should be there for you girls more. Especially now with dad gone for a while."
    luna "Well who turned into a stiff and made you a bloke?"
    luna "Now you're not just taking advantage of pops leaving so you can be dancin' in the sheets with us, eh mate?"
    linc "Luna, please, I'm serious."
    luna "Heh, sorry, just messing with ya."
    luna "Gotcha bro, thanks for being the best dang brother anywhere around."
    hide LunaTalk
    $ DayPhase += 1
    jump LuanLunaRoom
    return

label LunaMondayMorning3:
    scene bg Kitchen
    show LunaTalk at default_sprite
    luna "Hey little bro, you're not gonna eat this, are you?"
    linc "What, what are you talking about?"
    "Luan turns around revealing she took Lincoln's pudding."
    linc "Hey, that's mine."
    luna "Aw come on, please?"
    luna "I need something sweet. I promise i'll make it worth for you."
    linc "Okay, fine. Take it."
    luna "Thanks bro."
    "Luna takes a spoon of pudding and suddenly puts it into Lincoln's mouth, then puts it in hers and walks away winking."
    hide LunaTalk
    $ DayPhase += 1
    return

label LunaMondayAfternoon1:
    scene bg Garage
    "Luna is rocking out."

label LunaMondayAfternoon2:
    scene bg LivingRoomCenter
    show LunaTalk at default_sprite
    linc "What you watching, Luna?"
    luna "Nothing yet, looking to see what's on."
    luan "Here, see if you can find anything."
    hide LunaTalk
    $ DayPhase += 1
    return

label LunaMondayEvening:
    scene bg LivingRoomCenter
    show LunaTalk at default_sprite
    "Luna is listening to her radio"
    hide LunaTalk
    $ DayPhase += 1
    return

label LuanMondayMorning1:
    scene bg LuanWall
    show LuanTalk at default_sprite
    linc "Morning, Luan."
    "Luan is taking a sec to stretch her arms, a lock of her unbound hair falling on the left side of her face."
    luan "Morning."
    luan "Have you seen my scrunchie?"
    linc "No, I don't think so."
    luan "So what's up?"
    linc "Just checking up you, that's all."
    luan "And here I thought you wanted my cute little beaver teeth to take care of that {i}log{/i} of you"
    linc "No, I don't... uh what?"
    luan "Nothing, just a little joke between me and Luna. You {i}woodn't{/i} know about it."
    linc "Okay... so I'm gonna take care of breakfast too, you want the usual?"
    luan "Sure, thanks Linc"
    hide LuanTalk
    $ DayPhase += 1
    return

label LuanMondayMorning2:
    scene bg LuanWall
    show LuanTalk at default_sprite
    linc "Hey, Luan. What are you watching?"
    luan "Looking over my recordings of you guys. Wanna join me, see if we can catch something good?"
    linc "I don't know, it feels a little weird."
    luan "Aw come on, you'll get over it in a {i}flash{/i}. Get it?"
    linc "No but, okay sure, why not. This might be interesting."
    hide LuanTalk
    $ DayPhase += 1
    jump LuanLunaRoom
    return
label LuanMondayMorning3:
    scene bg LuanWall
    show LuanTalk at default_sprite
    luan "Hey Linc, can you help me out for a sec?"
    linc "Sure, what's up?"
    luan "I'm practicing a magic trick, I just need you to be a volunteer okay?"
    linc "No problem. What do I have to do."
    luan "Um let's see..."
    luan "Let's try this one."
    luan "Pick"
    "..."
    hide LuanTalk
    $ DayPhase += 1
    if DayPhase == 5:
        hide screen LuanLunaRight
        jump Lunch
    return

label LuanMondayAfternoon1:
    scene bg LuanWall
    show LuanTalk at default_sprite
    "As you enter you see Luan immediately stop from what she was doing, puts her hands behind her back, blushes and breathes heavily"
    luan "Lincoln!"
    luan "Y-You should knock, you know?"
    linc "Sorry, just the door was open and uh well"
    linc "Were you... dancing?"
    luan "What, no way silly, I was just uh"
    luan "..."
    luan "I guess the {i}jig{/i} is up."
    luan "Okay, yeah, I was dancing. Please don't tell the others"
    linc "This isn't really like you."
    luan "I know. I shouldn't have stage fright or anything like that, what with Funny Business and all but..."
    luan "It's just so weird when it comes to dancing."
    luan "It's different when you're fooling around in front of a bunch of kids or that time when we all went crazy after the yard sale."
    luan "I'm not planning on dancing for my show either or anything like that, I just thought it would be fun for myself."
    linc "I understand. Sorry I barged in like that but even though I didn't see much, I think you were pretty good."
    luan "Really?"
    linc "Yeah. Well, I'll leave you to it then."
    luan "Wait!"
    luan "Since you already know and all that... would you mind uh"
    luan "Watching me, and tell me how I'm doing?"
    luan "Who knows, maybe we could have some fun dancing together. You know, it takes two to tango"
    linc "Alright, might be fun"
    luan "Great!"
    hide LuanTalk
    $ DayPhase += 1
    jump LuanLunaRoom
    return

label LuanMondayAfternoon2:
    scene bg LuanWall
    show LuanDialogueSprite at default_sprite
    "Luan is doing a show for Lola and Lana"
    hide LuanDialogueSprite
    $ DayPhase += 1
    if DayPhase == 8:
        hide screen LuanLunaRight
        jump Dinner
    return

label LuanMondayEvening:
    scene bg LivingRoomCenter
    linc "Hey Lu, what are watching?"
    luan "\"Liar Liar\". Come here, watch it with me. Bet you're gonna love it."
    linc "Okay"
    $ DayPhase += 1
    if DayPhase == 10:
        hide screen LuanLunaRight
        jump NightPhase
    return

label LynnMondayMorning1:
    scene bg LynnBed
    show LynnTalk at default_sprite
    "Lynn is doing her morning workout"
    lynn "Hey \"Stinkin\", what's up?"
    lynn "Finally thought about joining me in my workout?"
    linc "Uh, I... need more time to think about it."
    linc "Anyway I'm just here to check up on you; see what's up. You need anything?"
    lynn "Sure this isn't one of your master plans, Mr. \"Man-With-The-Plan\"?"
    lynn "Nothing's gonna get you out of roughousing with me, you know that, right?"
    linc "No, it's nothing like that, I promise. I guess I'm trying to be a better brother... or something."
    lynn "..."
    "Lynn smiles while putting an arm over Lincoln"
    lynn "You're already the best bro ever, bro. And I mean that."
    linc "...Thanks"
    linc "Ugh, Lynn, you stink of sweat."
    lynn "Hahaha that's how you know it's workin, bro. Don't act like you're not loving it."
    linc "So, you need me to get you anything?"
    lynn "Nah I'm good. Check out with the Slumbering Dark Queen of the Underworld there."
    hide LynnTalk
    $ DayPhase += 1
    if DayPhase == 2:
        hide screen LynnBed
        jump Breakfast
    return

label LynnMondayMorning2:
    scene bg LynnBed
    show LynnTalk at default_sprite
    lynn "ONII-CHAAAN"
    with hpunch
    linc "AHH!"
    "Lynn tackles you to the ground and pins your arm."
    linc "L-Lynn would you pl-wait... what did you call me?"
    lynn "\"Onii-chan\"?..."
    linc "..."
    lynn "Lucy told me. She said it was some sort of eastern battle cry."
    lynn "What, did I not say it right?"
    "You look at Lucy, it's obvious she's holding in a grin."
    linc "{i}Guess even she feels like messing around sometimes{/i}"
    linc "It's not a battle cry, Lynn. It's actually what little sisters call their brothers in Japan, in a cutesy, loveable way even."
    lynn "W-What the... I thought it sounded a bit too weird"
    "Lucy lets out her monotone laugh."
    lynn "L-LUCY, when did you turn out to be such a prankster!"
    linc "{i}You're smiling too though. Can't blame you, who could ever get mad at that cute little goth.{/i}"
    hide LynnTalk
    $ DayPhase += 1
    jump LucyLynnRoom
    return

label LynnMondayMorning3:
    scene bg Backyard
    lynn "Hey bro. Wanna give me a hand with this, I wanna practice some throws."
    linc "Sure."
    $ DayPhase += 1
    if DayPhase == 5:
        jump Lunch
    return

label LynnMondayAfternoon1:
    scene bg LivingRoomCenter
    show LynnTalk at default_sprite
    linc "Doing your ritual I see. Big game coming up?"
    lynn "Yeah"
    "Insert baseball/football teams here, she's rooting for whoever represents Michigan or whatever?"
    hide LynnTalk
    $ DayPhase += 1
    call screen LivingRoom
    return

label LynnMondayAfternoon2:
    scene bg Backyard
    lynn "You doing anything, Linc?"
    linc "Not really, no"
    lynn "Then you can be my goalkeeper. Come on, I promise I'll go easy."
    $ DayPhase += 1
    if DayPhase == 8:
        jump Dinner
    return

label LynnMondayEvening:
    scene bg LynnBed
    show LynnTalk at default_sprite
    linc "What you doin, Lynn?"
    lynn "Just chillin."
    lynn "Hey, bro, can I sleep with you again?"
    linc "What, why?"
    linc "Something up between you and Lucy again?"
    lynn "Nah, we cool. Just that it's fine every once in a while. She said so herself, she enjoys some time alone with her spells."
    lynn "Whatever that means."
    lynn "Plus, I don't know why but sleeping with you is so comfy. I slept like a log last time"
    linc "Okay, fine."
    lynn "Awesome."
    linc "{i}Hope I can find those earplugs{/i}"
    hide LynnTalk
    $ DayPhase += 1
    if DayPhase == 10:
        hide screen LynnBed
        jump NightPhase
    return

label LucyMondayMorning1:
    scene bg LucyBed
    show LucyTalk at default_sprite
    linc "{i}Good, looks like she's still breathing. Hard to tell sometimes.{/i}"
    linc "Psst. Psst, hey Luce."
    "She turns her head towards you"
    linc "Morning, sleepyhead."
    lucy "Morning, Lincoln."
    linc "How'd you sleep?"
    lucy "Great. As if I was embraced by a warm darkness."
    lucy "Must be the new \"spell\" I found out about recently."
    linc "Spell? What spell?"
    lucy "N-Nothing, just something from... aunt Harriet's book."
    linc "Okay."
    linc "You need me to get you anything?"
    lucy "Not really but, well..."
    linc "It's OK Luce. Anything you need, your big brother will take care of it. Just name it"
    lucy "I was hoping for maybe a good morning... k-kiss?"
    lucy "O-On the forehead, it's fine on the forhead."
    linc "How am I gonna kiss your forehead with your bangs in the way"
    lucy "Oh. Dangit"
    lucy "Then on the c-cheek is fine. Unless you don't want to."
    lucy "It's fine if you don{nw}"
    lucy "..."
    lucy "Thanks, big brother."
    linc "Anytime"
    hide LucyTalk
    $ DayPhase += 1
    if DayPhase == 2:
        hide screen LucyBed
        jump Breakfast
    return


label LucyMondayMorning2:
    scene bg LucyBed
    show LucyTalk at default_sprite
    linc "Hey Lucy, writing another poem?"
    lucy "Yes. Well, I'm trying at least."
    lucy "I'm having a bit of a block. Any ideas are welcome."
    linc "Hmmm..."
    linc "Sorry, Lucy, can't really think of anything right now."
    lucy "It's fine, it happens. It's a hurdle everyone must overcome every once in a while."
    linc "Glad you're dealing with it so well."
    linc "You'll think of something in no time."
    hide LucyTalk
    $ DayPhase += 1
    jump LucyLynnRoom
    return

label LucyMondayMorning3:
    scene bg LucyBed
    show LucyTalk at default_sprite
    linc "{i}She's holding another one of her seances I think. I wonder if I should let her be.{/i}"
    lucy "It's OK, big brother. We can talk if you want"
    linc "Oh, h-hey Luce. Thought you were busy with your uh thing."
    linc "{i}Could she tell what I was thinking?{/i}"
    lucy "It's too dangerous to fully go to the otherworld so I always keep a part of me aware in this plane."
    linc "I see."
    lucy "Was there something you wanted, or perhaps you want to try it out?"
    linc "Nothing in particular and, I don't know, I don't think there's anybody I want to talk to in there."
    lucy "This isn't exactly a seance, it's more just tightening your bond with the spirit realm."
    lucy "I do it so that I can be prepared for when I finally step into the world of the dark. It's like meditating... sort of."
    linc "Alright then. Promise you'll keep me safe?"
    lucy "Always!"
    linc "Thanks, Luce. Ready when you are."
    hide LucyTalk
    $ DayPhase += 1
    if DayPhase == 5:
        hide screen LucyBed
        jump Lunch
    return

label LucyMondayAfternoon1:
    scene bg Kitchen
    show LucyTalk at default_sprite
    linc "Lucy... that's fake, right?"
    lucy "Unfortunately yes."
    linc "What do you use that stuff for anyway?"
    lucy "Paint, summoning, makeup, that kind of stuff."
    lucy "Do you want some?"
    linc "Nah I'm good, thanks."
    hide LucyTalk
    $ DayPhase += 1
    call screen Kitchen
    return

label LucyMondayAfternoon2:
    scene bg LucyBed
    show LucyTalk at default_sprite
    "Lucy is attempting to hide a book she's reading as you enter."
    linc "It's OK Lucy, it's just me. You know I'm fine with you reading that pony book."
    lucy "Yes but, actually i-it was a... well"
    lucy "A manga."
    linc "Oh cool, what was it?"
    linc "Can I see it?"
    lucy "NO!"
    lucy "I-I mean, no it's not really... cool, i-it's got a lot g-gore and"
    lucy "Lot of boring words, a lot of talking and you know"
    lucy "I'm sure it's not something you'd like, e-even I'm not really that into it."
    linc "Oh, OK I guess."
    lucy "Maybe you have something we can read together... in your room?"
    lucy "If you want?"
    linc "Not sure."
    linc "Gonna go look and then let you know."
    lucy "Yes please."
    hide LucyTalk
    $ DayPhase += 1
    if DayPhase == 8:
        hide screen LucyBed
        jump Dinner
    return

label LucyMondayEvening:
    scene bg LucyBed
    show LucyTalk at default_sprite
    linc "{i}What is she reading, that looks like a horror book{/i}"
    linc "Hey Luce, is that a spooky novel?"
    lucy "I hope so."
    linc "Are you gonna be okay with that, cause I think Lynn wants to sleep in my bed again so you'll be alone."
    lucy "So?"
    linc "Well you know, you'll be sleeping alone after you read something spooky and you might..."
    lucy "..."
    linc "Nevermind."
    linc "Either way, you're welcome to join us if you want."
    linc "You know, like last time."
    lucy "Hmm, I'll consider it."
    hide LucyTalk
    $ DayPhase += 1
    if DayPhase == 10:
        hide screen LucyBed
        jump NightPhase
    return

label LanaMondayMorning1:
    scene bg LanaBed
    show LanaTalk at default_sprite
    linc "Morning, Lana."
    lana "Hey big bro, what's up?"
    linc "Just making a round of the house, checking if you guys need anything."
    linc "And I don't mean just now, anytime you need anything just give me the word OK?"
    linc "You can count on your big brother."
    lana "Well, if something's gonna need fixing in the house I might need a hand, with dad out on his trip and all."
    lana "Think you can help me out?"
    linc "What if I promise I'll do my best?"
    lana "Good enough for me."
    hide LanaTalk
    $ DayPhase += 1
    if DayPhase == 2:
        hide screen LanaBed
        jump Breakfast
    return

label LanaMondayMorning2:
    scene bg LanaBed
    show LanaTalk at default_sprite
    "Lola and Lana are playing together"
    lola "Oh, help me~! Who will have the honor of protecting this beautiful and charming lady from the dreaded monster?"
    lana "I'll save you princess!"
    lola "Ow!"
    lola "H-Hey, what are you... why are you attacking me?"
    lana "Oh, thought this dragon was the princess."
    lola "Why you little..."
    lola "Fascinating how you're calling ME a monster when we're twins, remember?"
    lana "And?"
    lana "Oh hey Lincoln."
    lana "Wanna play with us?"
    lola "Yes, Lincoln, my most valiant knight in the shiniest armor, you'll save me from this terrible traitorous beast won't you?"
    linc "Uh... sure, why not?"
    lola "HAH, try and get to me now, you vile, vicious and vulgar villain."
    "You play with the twins for a while as their knight"
    hide LanaTalk
    $ DayPhase += 1
    jump LanaLolaRoom
    return

label LanaMondayMorning3:
    scene bg Backyard
    "Lana is running around like a dog"
    linc "Lana!"
    linc "Come here, girl. Come on!"
    "She plays along and you pet her for a while."
    $ DayPhase += 1
    if DayPhase == 5:
        jump Lunch
    else:
        jump Backyard
    return

label LanaMondayAfternoon1:
    ##need to add in front lawn BG

label LanaMondayAfternoon2:
    return


label LanaMondayEvening:
    scene bg LanaBed
    show LanaTalk at default_sprite
    "Lana is laying on the floor wearing only her overalls"
    linc "Lana?"
    linc "Are you ok?"
    lana "Hey bro. I'm great, I just found this by accident but laying on the floor like this is super comfortable"
    lana "Here, try it with me."
    linc "I think I'll pass"
    lana "Come on, you read your comics in your underwear anyway. Just give it a shot."
    linc "Fair point."
    linc "..."
    lana "So what do you think."
    linc "Yeah, this is... surprisingly relaxing."
    "You spend some time with Lana like this, drifting away in your consciousness"
    show LanaTalk
    $ DayPhase += 1
    if DayPhase == 10:
        hide screen LanaBed
        jump NightPhase
        return
    return

label LolaMondayMorning1:
    return


label LolaMondayMorning2:
    scene bg LolaBed
    show LolaTalk at default_sprite
    "Lola and Lana are playing together"
    lola "Oh, help me~! Who will have the honor of protecting this beautiful and charming lady from the dreaded monster?"
    lana "I'll save you princess!"
    lola "Ow!"
    lola "H-Hey, what are you... why are you attacking me!?"
    lana "Oh, thought this dragon was the princess."
    lola "Why you little..."
    lola "You're calling ME a monster yet we're twins, remember that?"
    lana "Yeah, so?"
    lana "Oh hey Lincoln."
    lana "Wanna play with us?"
    lola "Yes, Lincoln, my most valiant knight in the shiniest armor! You'll save me from this terrible traitorous beast, won't you?"
    linc "Uh... sure, why not?"
    lola "HAH, try and get to me now, you vile, vicious and vulgar villain."
    "You play with the twins for a while as their knight"
    hide LolaTalk
    $ DayPhase += 1
    jump LanaLolaRoom
    return

label LolaMondayMorning3:
    scene bg LolaBed
    show LanaTalk at default_sprite
    lola "Linky, just in time, I need your help."
    linc "What's wrong, Lola?"
    lola "Here, sit down."
    lola "So... which one?"
    "Lola alternated between two tiaras"
    linc "Oh"
    linc "Does it matter, they don't look that much different to me."
    lola "Of course it matters you philistine. This one commands more authority while this one is more approachable."
    lola "Can't you see?"
    linc "..."
    linc "Ah, yes, it all makes sense now. Anyway doesn't that, more or less, depend on how you're feeling?"
    lola "Fair point. See you're not that useless, brother of mine."
    hide LanaTalk
    $ DayPhase += 1
    if DayPhase == 5:
        hide screen LolaBed
        jump Lunch
        return
    return

label LolaMondayAfternoon1:
    scene bg LolaBed
    show LanaTalk at default_sprite
    lola "Good, you're here. Now change from those rags and come join us."
    linc "Sorry Lola, you know I love your tea parties but I'm kind of busy."
    lola "Aww come on, Linky."
    lola "Would you really leave your cutest, most fragile sister all alone?"
    "Lola approaches Lincoln, grabs his shirt and make puppy eyes at him"
    linc "...I think I can move something around in my schedule"
    lola "Yay!"
    lola "Now hurry hurry hurry. I got the juiciest story to tell you."
    linc "Are you gonna gossip on one of the girls again?"
    lola "....Do you want me to?"
    linc "....I'll think about it."
    hide LanaTalk
    $ DayPhase += 1
    jump LanaLolaRoom
    return

label LolaMondayAfternoon2:
    return


label LolaMondayEvening:
    scene bg LivingRoomCenter
    "Lola is just checking herself out in her hand mirror"
    linc "Hey, Lola."
    lola "Can't you see I'm VERY busy, at the moment?"
    linc "Well, all I wanted to ask was if you needed another pair of hands to hold your mirror so that you don't have to tire yourself."
    linc "But if you're so busy I guess{nw}"
    lola "*gasp*"
    lola "Linky, that would be amazing."
    lola "I'm sorry I said anything, would you please please please?"
    linc "If you insist"
    $ DayPhase += 1
    if DayPhase == 10:
        hide screen LivingRoom
        jump NightPhase
        return
    return

label LisaMondayMorning1:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

label LisaMondayMorning2:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

label LisaMondayMorning3:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

label LisaMondayAfternoon1:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

label LisaMondayAfternoon2:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

label LisaMondayEvening:
    scene bg LilyLisaRoom
    "Lisa is of little importance or she'll be some sort of \"shop\" so she'll always be in her room for the sake of convenience"
    "With a few exceptions"
    call screen Hall
    return

#===========
###     Tuesday
label LoriTuesdayMorning1:

label LoriTuesdayMorning2:
    scene bg LeniLoriBeds
    "{i}Guess Leni is getting ready for her show{/i}"
    linc "You two need a hand?"
    leni "Oh yes, please."
    lori "Here, take these to the van."
    lori "And be careful."
    linc "No problem."
    leni "Thanks Linky"
    jump LeniLoriRoom
    return
label LoriTuesdayMorning3:

label LoriTuesdayAfternoon1:

label LoriTuesdayAfternoon2:
    scene bg LivingRoomCenter
    "Lori is resting on the couch, with her eyes glued on the phone."
    return
label LoriTuesdayEvening:


label LeniTuesdayMorning1:
    scene bg BathroomEntrance
    "Leni is in the bathroom"
    call screen Hall
    return
label LeniTuesdayMorning2:
    scene bg LeniLoriBeds
    "{i}Guess Leni is getting ready for her show{/i}"
    linc "You two need a hand?"
    leni "Oh yes, please."
    lori "Here, take these to the van."
    lori "And be careful."
    linc "No problem."
    leni "Thanks Linky"
    jump LeniLoriRoom
    return
label LeniTuesdayMorning3:

label LeniTuesdayAfternoon1:

label LeniTuesdayAfternoon2:
    scene bg LeniLoriBeds
    "Leni is changing her clothes and left the door wide open"
    jump LeniLoriRoom
    return
label LeniTuesdayEvening:


label LunaTuesdayMorning1:

label LunaTuesdayMorning2:

label LunaTuesdayMorning3:

label LunaTuesdayAfternoon1:

label LunaTuesdayAfternoon2:

label LunaTuesdayEvening:


label LuanTuesdayMorning1:

label LuanTuesdayMorning2:

label LuanTuesdayMorning3:

label LuanTuesdayAfternoon1:

label LuanTuesdayAfternoon2:

label LuanTuesdayEvening:


label LynnTuesdayMorning1:

label LynnTuesdayMorning2:

label LynnTuesdayMorning3:

label LynnTuesdayAfternoon1:

label LynnTuesdayAfternoon2:

label LynnTuesdayEvening:


label LucyTuesdayMorning1:

label LucyTuesdayMorning2:

label LucyTuesdayMorning3:

label LucyTuesdayAfternoon1:

label LucyTuesdayAfternoon2:

label LucyTuesdayEvening:


label LanaTuesdayMorning1:

label LanaTuesdayMorning2:

label LanaTuesdayMorning3:

label LanaTuesdayAfternoon1:

label LanaTuesdayAfternoon2:

label LanaTuesdayEvening:


label LolaTuesdayMorning1:

label LolaTuesdayMorning2:

label LolaTuesdayMorning3:

label LolaTuesdayAfternoon1:

label LolaTuesdayAfternoon2:

label LolaTuesdayEvening:



label LisaTuesdayMorning1:

label LisaTuesdayMorning2:

label LisaTuesdayMorning3:

label LisaTuesdayAfternoon1:

label LisaTuesdayAfternoon2:

label LisaTuesdayEvening:

#===========
###     Wednesday
label LoriWednesdayMorning1:

label LoriWednesdayMorning2:

label LoriWednesdayMorning3:

label LoriWednesdayAfternoon1:

label LoriWednesdayAfternoon2:

label LoriWednesdayEvening:


label LeniWednesdayMorning1:

label LeniWednesdayMorning2:

label LeniWednesdayMorning3:

label LeniWednesdayAfternoon1:

label LeniWednesdayAfternoon2:

label LeniWednesdayEvening:
    return


label LunaWednesdayMorning1:
    scene bg BathroomEntrance
    "Luna is in the bathroom"
    call screen Hall
    return
label LunaWednesdayMorning2:

label LunaWednesdayMorning3:

label LunaWednesdayAfternoon1:

label LunaWednesdayAfternoon2:

label LunaWednesdayEvening:


label LuanWednesdayMorning1:

label LuanWednesdayMorning2:

label LuanWednesdayMorning3:

label LuanWednesdayAfternoon1:

label LuanWednesdayAfternoon2:

label LuanWednesdayEvening:


label LynnWednesdayMorning1:

label LynnWednesdayMorning2:

label LynnWednesdayMorning3:

label LynnWednesdayAfternoon1:

label LynnWednesdayAfternoon2:

label LynnWednesdayEvening:


label LucyWednesdayMorning1:

label LucyWednesdayMorning2:

label LucyWednesdayMorning3:

label LucyWednesdayAfternoon1:

label LucyWednesdayAfternoon2:

label LucyWednesdayEvening:


label LanaWednesdayMorning1:

label LanaWednesdayMorning2:

label LanaWednesdayMorning3:

label LanaWednesdayAfternoon1:

label LanaWednesdayAfternoon2:

label LanaWednesdayEvening:


label LolaWednesdayMorning1:

label LolaWednesdayMorning2:

label LolaWednesdayMorning3:

label LolaWednesdayAfternoon1:

label LolaWednesdayAfternoon2:

label LolaWednesdayEvening:



label LisaWednesdayMorning1:

label LisaWednesdayMorning2:

label LisaWednesdayMorning3:

label LisaWednesdayAfternoon1:

label LisaWednesdayAfternoon2:

label LisaWednesdayEvening:


#===========
###     Thursday
label LoriThursdayMorning1:

label LoriThursdayMorning2:

label LoriThursdayMorning3:

label LoriThursdayAfternoon1:

label LoriThursdayAfternoon2:

label LoriThursdayEvening:

label LeniThursdayMorning1:

label LeniThursdayMorning2:

label LeniThursdayMorning3:

label LeniThursdayAfternoon1:

label LeniThursdayAfternoon2:

label LeniThursdayEvening:

label LunaThursdayMorning1:

label LunaThursdayMorning2:

label LunaThursdayMorning3:

label LunaThursdayAfternoon1:

label LunaThursdayAfternoon2:

label LunaThursdayEvening:
    return

label LuanThursdayMorning1:
    scene bg BathroomEntrance
    "Luan is in the bathroom"
    call screen Hall
    return
label LuanThursdayMorning2:

label LuanThursdayMorning3:

label LuanThursdayAfternoon1:

label LuanThursdayAfternoon2:

label LuanThursdayEvening:


label LynnThursdayMorning1:

label LynnThursdayMorning2:

label LynnThursdayMorning3:

label LynnThursdayAfternoon1:

label LynnThursdayAfternoon2:

label LynnThursdayEvening:


label LucyThursdayMorning1:

label LucyThursdayMorning2:

label LucyThursdayMorning3:

label LucyThursdayAfternoon1:

label LucyThursdayAfternoon2:

label LucyThursdayEvening:


label LanaThursdayMorning1:

label LanaThursdayMorning2:

label LanaThursdayMorning3:

label LanaThursdayAfternoon1:

label LanaThursdayAfternoon2:

label LanaThursdayEvening:


label LolaThursdayMorning1:

label LolaThursdayMorning2:

label LolaThursdayMorning3:

label LolaThursdayAfternoon1:

label LolaThursdayAfternoon2:

label LolaThursdayEvening:



label LisaThursdayMorning1:

label LisaThursdayMorning2:

label LisaThursdayMorning3:

label LisaThursdayAfternoon1:

label LisaThursdayAfternoon2:

label LisaThursdayEvening:


#===========
###     Friday
label LoriFridayMorning1:

label LoriFridayMorning2:

label LoriFridayMorning3:

label LoriFridayAfternoon1:

label LoriFridayAfternoon2:

label LoriFridayEvening:


label LeniFridayMorning1:

label LeniFridayMorning2:

label LeniFridayMorning3:

label LeniFridayAfternoon1:

label LeniFridayAfternoon2:

label LeniFridayEvening:


label LunaFridayMorning1:

label LunaFridayMorning2:

label LunaFridayMorning3:

label LunaFridayAfternoon1:

label LunaFridayAfternoon2:

label LunaFridayEvening:


label LuanFridayMorning1:

label LuanFridayMorning2:

label LuanFridayMorning3:

label LuanFridayAfternoon1:

label LuanFridayAfternoon2:

label LuanFridayEvening:


label LynnFridayMorning1:

label LynnFridayMorning2:

label LynnFridayMorning3:

label LynnFridayAfternoon1:

label LynnFridayAfternoon2:

label LynnFridayEvening:
    return


label LucyFridayMorning1:
    scene bg BathroomEntrance
    "Lucy is in the bathroom"
    call screen Hall
    return
label LucyFridayMorning2:

label LucyFridayMorning3:

label LucyFridayAfternoon1:

label LucyFridayAfternoon2:

label LucyFridayEvening:


label LanaFridayMorning1:

label LanaFridayMorning2:

label LanaFridayMorning3:

label LanaFridayAfternoon1:

label LanaFridayAfternoon2:

label LanaFridayEvening:


label LolaFridayMorning1:

label LolaFridayMorning2:

label LolaFridayMorning3:

label LolaFridayAfternoon1:

label LolaFridayAfternoon2:

label LolaFridayEvening:



label LisaFridayMorning1:

label LisaFridayMorning2:

label LisaFridayMorning3:

label LisaFridayAfternoon1:

label LisaFridayAfternoon2:

label LisaFridayEvening:


#===========
###     Saturday
label LoriSaturdayMorning1:

label LoriSaturdayMorning2:

label LoriSaturdayMorning3:

label LoriSaturdayAfternoon1:

label LoriSaturdayAfternoon2:

label LoriSaturdayEvening:


label LeniSaturdayMorning1:

label LeniSaturdayMorning2:

label LeniSaturdayMorning3:

label LeniSaturdayAfternoon1:

label LeniSaturdayAfternoon2:

label LeniSaturdayEvening:


label LunaSaturdayMorning1:

label LunaSaturdayMorning2:

label LunaSaturdayMorning3:

label LunaSaturdayAfternoon1:

label LunaSaturdayAfternoon2:

label LunaSaturdayEvening:


label LuanSaturdayMorning1:

label LuanSaturdayMorning2:

label LuanSaturdayMorning3:

label LuanSaturdayAfternoon1:

label LuanSaturdayAfternoon2:

label LuanSaturdayEvening:


label LynnSaturdayMorning1:

label LynnSaturdayMorning2:

label LynnSaturdayMorning3:

label LynnSaturdayAfternoon1:

label LynnSaturdayAfternoon2:

label LynnSaturdayEvening:


label LucySaturdayMorning1:

label LucySaturdayMorning2:

label LucySaturdayMorning3:

label LucySaturdayAfternoon1:

label LucySaturdayAfternoon2:

label LucySaturdayEvening:



label LanaSaturdayMorning2:

label LanaSaturdayMorning3:

label LanaSaturdayAfternoon1:

label LanaSaturdayAfternoon2:

label LanaSaturdayEvening:



label LolaSaturdayMorning2:

label LolaSaturdayMorning3:

label LolaSaturdayAfternoon1:

label LolaSaturdayAfternoon2:

label LolaSaturdayEvening:



label LisaSaturdayMorning1:

label LisaSaturdayMorning2:

label LisaSaturdayMorning3:

label LisaSaturdayAfternoon1:

label LisaSaturdayAfternoon2:

label LisaSaturdayEvening:


label TwinsSaturdayMorning:



#===========
###     Sunday
label LoriSundayMorning1:

label LoriSundayMorning2:

label LoriSundayMorning3:

label LoriSundayAfternoon1:

label LoriSundayAfternoon2:

label LoriSundayEvening:


label LeniSundayMorning1:

label LeniSundayMorning2:

label LeniSundayMorning3:

label LeniSundayAfternoon1:

label LeniSundayAfternoon2:

label LeniSundayEvening:


label LunaSundayMorning1:

label LunaSundayMorning2:

label LunaSundayMorning3:

label LunaSundayAfternoon1:

label LunaSundayAfternoon2:

label LunaSundayEvening:


label LuanSundayMorning1:

label LuanSundayMorning2:

label LuanSundayMorning3:

label LuanSundayAfternoon1:

label LuanSundayAfternoon2:

label LuanSundayEvening:


label LynnSundayMorning1:

label LynnSundayMorning2:

label LynnSundayMorning3:

label LynnSundayAfternoon1:

label LynnSundayAfternoon2:

label LynnSundayEvening:


label LucySundayMorning1:

label LucySundayMorning2:

label LucySundayMorning3:

label LucySundayAfternoon1:

label LucySundayAfternoon2:

label LucySundayEvening:


label LanaSundayMorning1:

label LanaSundayMorning2:

label LanaSundayMorning3:

label LanaSundayAfternoon1:

label LanaSundayAfternoon2:

label LanaSundayEvening:


label LolaSundayMorning1:

label LolaSundayMorning2:

label LolaSundayMorning3:

label LolaSundayAfternoon1:

label LolaSundayAfternoon2:

label LolaSundayEvening:



label LisaSundayMorning1:

label LisaSundayMorning2:

label LisaSundayMorning3:

label LisaSundayAfternoon1:

label LisaSundayAfternoon2:

label LisaSundayEvening:

    #Just in case
    return
