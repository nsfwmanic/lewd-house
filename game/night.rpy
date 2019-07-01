define NightTime = False

label NightPhase:
    scene bg MyRoomNight
    $ NightTime = True
    "This is the night phase."
    "In the demo you will only be able to walk around the house and check up on your sleeping siblings."
    "In the future, however, we will implement as many nightly activities as possible."
    menu:
        "Go out in the hallway":
            call screen HallNight
        "Sleep until morning.":
            $ NightTime = False
            scene bg BedSleep
            "You decide to rest until morning."
            scene bg Morning with Fade(0.5, 1.0, 0.2)
            $ DayPhase = 1
            if Sunday == True:
                $ Sunday = False
                $ Monday = True
            elif Monday == True:
                $ Monday = False
                $ Tuesday = True
            elif Tuesday == True:
                $ Tuesday = False
                $ Wednesday = True
            elif Wednesday == True:
                $ Wednesday = False
                $ Thursday = True
            elif Thursday == True:
                $ Thursday = False
                $ Friday = True
            elif Friday == True:
                $ Friday = False
                $ Saturday = True
            elif Saturday == True:
                $ Saturday = False
                $ Sunday = True
            "It is now morning."
            scene bg Morning
            call screen MyRoom

screen HallNight():
    imagemap:
        ground "images/Night/HallwayRoomNight_Idle.png"
        hover "images/Night/HallwayRoomNight_Hover.png"

        hotspot (153, 0, 104, 631) clicked Jump("LisaLilyNight")
        hotspot (510, 251, 28, 196) clicked Jump("LoriLeniNight")
        hotspot (689, 260, 30, 199) clicked Jump("LuanLunaNight")
        hotspot (779, 173, 56, 376) clicked Jump("LynnLucyNight")
        hotspot (951, 7, 116, 705) clicked Jump("LolaLanaNight")
        hotspot (585, 292, 55, 130) clicked Jump("BathroomNight")
        hotspot (348, 66, 95, 459) clicked Jump("LivingRoomNight")
        hotspot (537, 619, 99, 98) clicked Jump("NightPhase")

label LisaLilyNight:
    scene bg LisaSleep
    linc "We're a couple of weirdos, aren't we Lisa?"
    linc "Sleep tight... Sure hope nothing bad comes out of this."
    call screen HallNight

label LoriLeniNight:
    scene bg LeniLoriRoomNight
    menu:
        "Check on Lori":
            scene bg LoriSleep
            linc "Lori seems to be having a bad dream?"
            linc "Or that's just her sleeping face. Either way, best be careful and not wake her up."
            jump LoriLeniNight
        "Check on Leni":
            scene bg LeniSleep1
            leni "Nngh."
            scene bg LeniSleep2
            leni "Ugh scrunchies."
            linc "I think she's having a nightmare."
            scene bg LeniSleep3
            leni "Ugghh legwarmers."
            linc "A fashion nightmare. I would wake her up but her cries are too cute."
            linc "Sorry, Leni, I'll make it up to you sometime."
            jump LoriLeniNight
        "Leave":
            call screen HallNight
label LuanLunaNight:
    scene bg LuanLunaRoomNight
    menu:
        "Check on Luan":
            scene bg LuanSleep
            linc "I shouldn't let that cute sleeping face fool me, she's probably planning her next prank on me."
            linc "Along with several puns to last the day."
            jump LuanLunaNight
        "Check on Luna":
            scene bg LunaSleep
            linc "She seems way tired. She was probably practicing a lot of moves for her stage."
            linc "Her passion is admirable."
            jump LuanLunaNight
        "Leave":
            call screen HallNight

label LynnLucyNight:
    scene bg LucyLynnSleep
    linc "They're both sleeping soundly."
    linc "Best not bother them right now."
    call screen HallNight

label LolaLanaNight:
    scene bg LolaLanaRoomNight
    menu:
        "Check on Lana":
            scene bg LanaSleep
            linc "Too dangerous to get close to Lana right now, with all her pets sleeping next to her."
            jump LolaLanaNight
        "Check on Lola":
            scene bg LolaSleep
            linc "Lola is equally as dangerous to wake up as Lana's pets... If not more. Maybe when you warm up to her that will change"
            jump LolaLanaNight
        "Leave":
            call screen HallNight


label BathroomNight:
    scene bg BathroomNightLights
    "This will most likely be another secluded meeting place for you and your siblings in the night."
    scene bg NightBathroomClosed
    "Perhaps even take a bath together under the moonlight."
    call screen HallNight

label LivingRoomNight:
    scene bg LivingRoomNight
    menu:
        "Upstairs":
            scene bg NightUpstairs
            $ renpy.pause(1.0)
            call screen HallNight
        "Parent's room":
            scene bg ParentsNight
            linc "Nothing I can do here right now."
            jump LivingRoomNight
        "Dining Room":
            jump DiningNight

        "Go Outside":
            jump OutsideNight

label DiningNight:
    scene bg DiningRoomNight
    menu:
        "Living room":
            jump LivingRoomNight
        "Hide under table":
            scene bg DiningWindowNight
            $ renpy.pause(1.0)
            scene bg UnderTableNight
            menu:
                "Get out":
                    jump DiningNight
        "Kitchen":
            jump KitchenNight

label KitchenNight:
    scene bg KitchenNightInside
    menu:
        "Dining room":
            jump DiningNight
        "Basement":
            jump Basement

label ParentsNight:
    scene bg ParentsNight
    linc "Nothing I can do here right now."
    jump LivingRoomNight

label OutsideNight:
    scene bg NightFrontDoorClosed
    $ renpy.pause(1.0)
    scene bg NightFrontDoorOpen
    $ renpy.pause(1.0)
    scene bg NightNeighborhood2
    "This will either be a meeting place with another character, such as Ronnie Anne, or a place you can sneak out with a sister."
    "For now, this is all we'll see, sadly."
    jump LivingRoomNight
