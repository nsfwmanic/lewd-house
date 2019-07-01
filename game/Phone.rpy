##################Smartphone screen#######################
#screen ToggleButtons:
#    imagebutton auto "images/Smartphone/SmartIcon_%s.png" xpos 1100 ypos 515 action [ (Show("Smartphone")), (Hide("ToggleButtons"))]
 #   zorder 100
####    WeekDay
##      weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
screen WeekDay():
    tag btns
    zorder 100
    if weekdays[date.weekday()]=="Monday" and act == 'morning':
        add MondayM1
    elif weekdays[date.weekday()]=="Monday" and act == 'afternoon':
        add MondayA1
    elif weekdays[date.weekday()]=="Monday" and act == 'evening':
        add MondayEve
    elif weekdays[date.weekday()]=="Monday" and act == 'night':
        add MondayMidnight
    elif  weekdays[date.weekday()]=="Tuesday" and act == 'morning':
        add TuesdayM1
    elif  weekdays[date.weekday()]=="Tuesday" and act == 'afternoon':
        add TuesdayA1
    elif  weekdays[date.weekday()]=="Tuesday" and act == 'evening':
        add TuesdayEve
    elif  weekdays[date.weekday()]=="Tuesday" and act == 'night':
        add TuesdayMidnight
    elif  weekdays[date.weekday()]=="Wednesday" and act == 'morning':
        add WednesdayM1
    elif  weekdays[date.weekday()]=="Wednesday" and act == 'afternoon':
        add WednesdayA1
    elif  weekdays[date.weekday()]=="Wednesday" and act == 'evening':
        add WednesdayEve
    elif  weekdays[date.weekday()]=="Wednesday" and act == 'night':
        add WednesdayMidnight
    elif  weekdays[date.weekday()]=="Thursday" and act == 'morning':
        add ThursdayM1
    elif  weekdays[date.weekday()]=="Thursday" and act == 'afternoon':
        add ThursdayA1
    elif  weekdays[date.weekday()]=="Thursday" and act == 'evening':
        add ThursdayEve
    elif  weekdays[date.weekday()]=="Thursday" and act == 'night':
        add ThursdayMidnight
    elif  weekdays[date.weekday()]=="Friday" and act == 'morning':
        add FridayM1
    elif  weekdays[date.weekday()]=="Friday" and act == 'afternoon':
        add FridayA1
    elif  weekdays[date.weekday()]=="Friday" and act == 'evening':
        add FridayEve
    elif  weekdays[date.weekday()]=="Friday" and act == 'night':
        add FridayMidnight
    elif  weekdays[date.weekday()]=="Saturday" and act == 'morning':
        add SaturdayM1
    elif  weekdays[date.weekday()]=="Saturday" and act == 'afternoon':
        add SaturdayA1
    elif  weekdays[date.weekday()]=="Saturday" and act == 'evening':
        add SaturdayEve
    elif  weekdays[date.weekday()]=="Saturday" and act == 'night':
        add SaturdayMidnight
    elif  weekdays[date.weekday()]=="Sunday" and act == 'morning':
        add SundayM1
    elif  weekdays[date.weekday()]=="Sunday" and act == 'afternoon':
        add SundayA1
    elif  weekdays[date.weekday()]=="Sunday" and act == 'evening':
        add SundayEve
    elif  weekdays[date.weekday()]=="Sunday" and act == 'night':
        add SundayMidnight
screen WeekDays():
    tag btns
    zorder 100
    if Monday and DayPhase == 1:
        add MondayM1
    if Monday and DayPhase == 3:
        add MondayM2
    if Monday and DayPhase == 4:
        add MondayM3
    if Monday and DayPhase == 6:
        add MondayA1
    if Monday and DayPhase == 7:
        add MondayA2
    if Monday and act == 'evening':
        add MondayEve
    if Monday and act == 'night':
        add MondayMidnight
    if Tuesday and DayPhase == 1:
        add TuesdayM1
    if Tuesday and DayPhase == 3:
        add TuesdayM2
    if Tuesday and DayPhase == 4:
        add TuesdayM3
    if Tuesday and DayPhase == 6:
        add TuesdayA1
    if Tuesday and DayPhase == 7:
        add TuesdayA2
    if Tuesday and act == 'evening':
        add TuesdayEve
    if Tuesday and act == 'night':
        add TuesdayMidnight
    if Wednesday and DayPhase == 1:
        add WednesdayM1
    if Wednesday and DayPhase == 3:
        add WednesdayM2
    if Wednesday and DayPhase == 4:
        add WednesdayM3
    if Wednesday and DayPhase == 6:
        add WednesdayA1
    if Wednesday and DayPhase == 7:
        add WednesdayA2
    if Wednesday and act == 'evening':
        add WednesdayEve
    if Wednesday and act == 'night':
        add WednesdayMidnight
    if Thursday and DayPhase == 1:
        add ThursdayM1
    if Thursday and DayPhase == 3:
        add ThursdayM2
    if Thursday and DayPhase == 4:
        add ThursdayM3
    if Thursday and DayPhase == 6:
        add ThursdayA1
    if Thursday and DayPhase == 7:
        add ThursdayA2
    if Thursday and act == 'evening':
        add ThursdayEve
    if Thursday and act == 'night':
        add ThursdayMidnight
    if Friday and DayPhase == 1:
        add FridayM1
    if Friday and DayPhase == 3:
        add FridayM2
    if Friday and DayPhase == 4:
        add FridayM3
    if Friday and DayPhase == 6:
        add FridayA1
    if Friday and DayPhase == 7:
        add FridayA2
    if Friday and act == 'evening':
        add FridayEve
    if Friday and act == 'night':
        add FridayMidnight
    if Saturday and DayPhase == 1:
        add SaturdayM1
    if Saturday and DayPhase == 3:
        add SaturdayM2
    if Saturday and DayPhase == 4:
        add SaturdayM3
    if Saturday and DayPhase == 6:
        add SaturdayA1
    if Saturday and DayPhase == 7:
        add SaturdayA2
    if Saturday and act == 'evening':
        add SaturdayEve
    if Saturday and act == 'night':
        add SaturdayMidnight
    if Sunday and DayPhase == 1:
        add SundayM1
    if Sunday and DayPhase == 3:
        add SundayM2
    if Sunday and DayPhase == 4:
        add SundayM3
    if Sunday and DayPhase == 6:
        add SundayA1
    if Sunday and DayPhase == 7:
        add SundayA2
    if Sunday and act == 'evening':
        add SundayEve
    if Sunday and act == 'night':
        add SundayMidnight
screen ToggleButtons():
    tag btn
    zorder 101
    imagebutton auto "images/DayUI/ToggleUI_%s.png" xpos 150 ypos 80
    imagebutton auto "images/Smartphone/PhoneToggle_%s.png" xpos 215 ypos 83 action [(Show("Smartphone"))]
    imagebutton auto "images/DayUI/MapToggle_%s.png" xpos 166 ypos 85 action ToggleVariable('MapShow')
screen Smartphone():
    modal True
    add "images/Smartphone/Smartphone.png" # the background
    imagebutton auto "images/Smartphone/ReturnButton_%s.png" xpos 23 ypos 280 action [ (Hide ("Smartphone")), hide_screens, hide_stats, (Hide("gui_tooltip")), (Show("ToggleButtons"))]
    imagebutton auto "images/Smartphone/Inventory/InventoryIcon_%s.png" xpos 135 ypos 334 action [ (Show("inventory_screen")), hide_stats, (Hide("MapUpstairs")), (Hide("MapDownstairs")), (Hide("StatScreen"))]
    imagebutton auto "images/Smartphone/Map/HouseMapIcon_%s.png" xpos 135 ypos 214 action [ (Show ("MapUpstairs")), hide_stats, (Hide("inventory_sreen")), (Hide("StatScreen"))]
    imagebutton auto "images/Smartphone/Stats/StatsIcon_%s.png" xpos 135 ypos 90 action [(Show("StatScreen")), (Hide("MapUpstairs")), (Hide("MapDownstairs")), (Hide("inventory_screen")), (Hide("gui_tooltip"))]

####    Maps
screen MapUpstairs():
    add "images/Smartphone/Map/MapUpstairs_Idle.png"
    if NightTime == True:
        imagemap:
            ground "images/Smartphone/Map/MapUpstairs_Idle.png"
            hover "images/Smartphone/Map/MapUpstairs_Hover.png"

            hotspot (343, 243, 107, 156) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("BathroomNight"))]
            hotspot (455, 92, 195, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LuanLunaNight"))]
            hotspot (655, 92, 135, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LynnLucyNight"))]
            hotspot (796, 92, 188, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LolaLanaNight"))]
            hotspot (991, 239, 89, 164) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("NightPhase"))]
            hotspot (776, 357, 209, 193) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LisaLilyNight"))]
            hotspot (455, 358, 227, 192) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LoriLeniNight"))]
            hotspot (687, 353, 83, 122) clicked [ (Show("MapDownstairs")), (Hide("MapUpstairs"))]
    else:
        imagemap:
            ground "images/Smartphone/Map/MapUpstairs_Idle.png"
            hover "images/Smartphone/Map/MapUpstairs_Hover.png"

            hotspot (343, 243, 107, 156) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("Bathroomenter"))]
            hotspot (455, 92, 195, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LuanLunaRoom"))]
            hotspot (655, 92, 135, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LucyLynnRoom"))]
            hotspot (796, 92, 188, 194) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LanaLolaRoom"))]
            hotspot (991, 239, 89, 164) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("MyRoom"))]
            hotspot (776, 357, 209, 193) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LilyLisaRoom"))]
            hotspot (455, 358, 227, 192) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("LeniLoriRoom"))]
            hotspot (343, 404, 107, 146) clicked [ (Hide ("Smartphone")), hide_screens, hide_stats, (Show("ToggleButtons")), (Jump("Attic"))]
            hotspot (687, 353, 83, 122) clicked [ (Show("MapDownstairs")), (Hide("MapUpstairs"))]
screen MapDownstairs():
    add "images/Smartphone/Map/MapDownstairs_Idle.png"
    if NightTime == True:
        imagemap:
            ground "images/Smartphone/Map/MapDownstairs_Idle.png"
            hover "images/Smartphone/Map/MapDownstairs_Hover.png"

            hotspot (689, 267, 80, 130) clicked [ (Show("MapUpstairs")), (Hide("MapDownstairs"))]
            hotspot (343, 95, 272, 220) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("ParentsNight"))]
            hotspot (342, 323, 321, 230) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("LivingRoomNight"))]
            hotspot (776, 322, 304, 231) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("DiningNight"))]
            hotspot (797, 95, 284, 220) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("KitchenNight"))]

    else:
        imagemap:
            ground "images/Smartphone/Map/MapDownstairs_Idle.png"
            hover "images/Smartphone/Map/MapDownstairs_Hover.png"

            hotspot (689, 267, 80, 130) clicked [ (Show("MapUpstairs")), (Hide("MapDownstairs"))]
            hotspot (343, 95, 272, 220) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("Parentsroom"))]
            hotspot (342, 323, 321, 230) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("LivingRoom"))]
            hotspot (776, 322, 304, 231) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("DiningRoom"))]
            hotspot (797, 95, 284, 220) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("Kitchen"))]
            hotspot (687, 95, 89, 86) clicked [ (Hide ("Smartphone")), (Show("ToggleButtons")), hide_screens, (Jump("RearEntrance"))]
####|---------------------------------------------|

####    Stats
screen StatScreen():
    add "images/Smartphone/Stats/StatScreen_Idle.png"

    imagemap:
        ground "images/Smartphone/Stats/StatScreen_Idle.png"
        hover "images/Smartphone/Stats/StatScreen_Hover.png"

        hotspot (274, 460, 73, 72) clicked [ hide_stats, (Show("StatsLori")), (Show("LoriAffectionBar"))]
        hotspot (349, 460, 73, 72) clicked [ hide_stats, (Show("StatsLeni")), (Show("LeniAffectionBar"))]
        hotspot (424, 460, 74, 73) clicked [ hide_stats, (Show("StatsLuna")), (Show("LunaAffectionBar"))]
        hotspot (499, 460, 74, 73) clicked [ hide_stats, (Show("StatsLuan")), (Show("LuanAffectionBar"))]
        hotspot (574, 460, 74, 73) clicked [ hide_stats, (Show("StatsLynn")), (Show("LynnAffectionBar"))]
        hotspot (650, 460, 74, 73) clicked [ hide_stats, (Show("StatsLucy")), (Show("LucyAffectionBar"))]
        hotspot (726, 460, 74, 73) clicked [ hide_stats, (Show("StatsLana")), (Show("LanaAffectionBar"))]
        hotspot (801, 460, 74, 73) clicked [ hide_stats, (Show("StatsLola")), (Show("LolaAffectionBar"))]
        hotspot (876, 460, 74, 73) clicked [ hide_stats, (Show("StatsLisa")), (Show("LisaAffectionBar"))]
        hotspot (953, 460, 74, 73) clicked [ hide_stats, (Show("StatsRonnie")), (Show("RonnieAffectionBar"))]
        hotspot (1028, 460, 74, 73) clicked [ hide_stats, (Show("StatsCarol")), (Show("CarolAffectionBar"))]
screen StatsLori():
    add "images/Smartphone/Stats/StatsLori.png"
screen LoriAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LoriAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLeni():
    add "images/Smartphone/Stats/StatsLeni.png"
screen LeniAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LeniAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLuna():
    add "images/Smartphone/Stats/StatsLuna.png"
screen LunaAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LunaAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLuan():
    add "images/Smartphone/Stats/StatsLuan.png"
screen LuanAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LuanAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLynn():
    add "images/Smartphone/Stats/StatsLynn.png"
screen LynnAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LynnAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLucy():
    add "images/Smartphone/Stats/StatsLucy.png"
screen LucyAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LucyAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLana():
    add "images/Smartphone/Stats/StatsLana.png"
screen LanaAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LanaAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLola():
    add "images/Smartphone/Stats/StatsLola.png"
screen LolaAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LolaAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsLisa():
    add "images/Smartphone/Stats/StatsLisa.png"
screen LisaAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(LisaAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsRonnie():
    add "images/Smartphone/Stats/StatsRonnie.png"
screen RonnieAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(RonnieAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
screen StatsCarol():
    add "images/Smartphone/Stats/StatsCarol.png"
screen CarolAffectionBar():
    label "Affection: " at Position(xpos=700, ypos=150, xanchor=0, yanchor=0)
    bar value StaticValue(CarolAffection, 100):
        at Position(xpos=700, ypos=200, xanchor=0, yanchor=0)
        xmaximum 400
        ymaximum 15
####|---------------------------------------------|

####    Inventory
screen inventory_screen():
    add "images/Smartphone/Inventory/Inventory.png"
    $ x = 280 # coordinates of the top left item position
    $ y = -75
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'))
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/10):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*10 and i+1>inv_page*10:
            $ x += 150
            if i%5==0:
                $ y += 160
                $ x = 280
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("images/Smartphone/Inventory/inv_", "").replace(".png", "")
            imagebutton idle pic hover pic xpos x ypos y clicked [Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=420) ]
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .700 ypos .65
screen gui_tooltip(my_picture="", my_tt_xpos=310, my_tt_ypos=-190):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
##style tooltip:
    ##background Frame("gui/Tooltip.png", gui.tooltip_border)

##################Defining the tooltips/item descriptions#########################:
image tooltip_inventory_FBHelmet=LiveComposite((550, 115), (3,0),  Text("Football Helmet.", color='#000000'))
image tooltip_inventory_SunGlasses=LiveComposite((550, 115), (3,0), Text("Leni's sunglasses",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_walkietalkie=LiveComposite((550, 115), (3,0), Text("A walkietalkie.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_bat=LiveComposite((550, 115), (3,0), Text("A baseball bat.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_camera=LiveComposite((550, 115), (3,0), Text("Old Camera.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_comix=LiveComposite((550, 115), (3,0), Text("Comix boox.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_flowers=LiveComposite((550, 115), (3,0), Text("Flower bouquet.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_football2=LiveComposite((550, 115), (3,0), Text("Hand egg ball.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_golfclub=LiveComposite((550, 115), (3,0), Text("Gold Club.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_gum=LiveComposite((550, 115), (3,0), Text("Gum gum.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_plunger=LiveComposite((550, 115), (3,0), Text("Plungie.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_potion=LiveComposite((550, 115), (3,0), Text("Potion.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_soccerball=LiveComposite((550, 115), (3,0), Text("Football.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_ticket=LiveComposite((550, 115), (3,0), Text("Ticket.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_videocamera=LiveComposite((550, 115), (3,0), Text("Video camera.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_VR=LiveComposite((550, 115), (3,0), Text("Virtual Reality Goggles.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_drumsticks=LiveComposite((550, 115), (3,0), Text("Drumsticks.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_hockeystick=LiveComposite((550, 115), (3,0), Text("Hockey stick.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_horn=LiveComposite((550, 115), (3,0), Text("Honk Honk.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_microphone=LiveComposite((550, 115), (3,0), Text("Mike.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_money=LiveComposite((550, 115), (3,0), Text("I need $$$.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_purse=LiveComposite((550, 115), (3,0), Text("Purse.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_weight=LiveComposite((550, 115), (3,0), Text("Dumbbell.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_baseball=LiveComposite((550, 115), (3,0), Text("Baseball.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_basketball=LiveComposite((600,73), (3,0), Text("Basketball.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_beachball=LiveComposite((600,73), (3,0), Text("Beachball.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
image tooltip_inventory_creampie=LiveComposite((600,73), (3,0), Text("Creampie.",  font="fonts/animeace2_reg.ttf", color='#000000' ))
