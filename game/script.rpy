## The script of the game goes in this file.
label splashscreen:
    scene black
    with Pause(1)

    play sound "music/Logo.mp3"

    show Splash with dissolve
    with Pause(2)

    scene black with dissolve
    show Disclaimer with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(.5)
    stop sound
    return

#--------------------------------------------#
#Manic's change to the daily stuff goes here #
#--------------------------------------------#
label start:
    jump night
label morning:
    python:
        DayPhase = 4
        act = "morning"
    while DayPhase > 0:
        call show_screens
        call events_run_period()
        "DayPhase [DayPhase]."
        $ DayPhase -= 1
label afternoon:
    python:
        DayPhase = 3
        act = "afternoon"
    while DayPhase > 0:
        call show_screens
        call events_run_period()
        "DayPhase [DayPhase]."
        $ DayPhase -= 1
label evening:
    python:
        DayPhase = 2
        act = "evening"
    while DayPhase > 0:
        call show_screens
        call events_run_period()
        "DayPhase [DayPhase]."
        $ DayPhase -= 1
label night:
    #call screen MyRoom
    #"Night time"
    python:
        act = "night"
        date += day1
    call show_screens
    call events_run_period()
    call show_screens
    jump morning

label show_screens:
    show screen WeekDay
    show screen ToggleButtons
    return
label room:
    call show_screens
    call screen MyRoom
    return
#--------------------------------------------#
#--------------------------------------------#
#--------------------------------------------#
