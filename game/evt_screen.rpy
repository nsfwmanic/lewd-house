
screen explore():
    tag explore
    use MyRoom
##      Room Screens
screen MyRoom():
    tag explore
    add "MyRoomExit.jpg"
    imagebutton auto "MyRoomDoor_%s.png" pos 374, 0 action Show ("MyRoomDoor")
    imagebutton auto "MyRoomBed_%s.png" pos 0, 156 action Show("Bed")
    imagebutton auto "MyRoomDesk_%s.png" pos 870, 0 action Show("Desk")
screen Bed():
    tag explore
    add "MyRoom.jpg"
    imagebutton auto "BedMatress_%s.png" pos 188, 266 action Show("BedTop")
    imagebutton auto "BedUnder_%s.png" pos 181, 570 action Jump("UnderBed")
    imagebutton auto "BedDoor_%s.png" pos 1088, 0 action Show("MyRoomDoor")
screen BedTop():
    tag explore
    add "MyRoom.jpg"
    imagebutton auto "BedButtonWait_%s.png" pos 210, 245 action Jump("BedWait")
    imagebutton auto "BedButtonNight_%s.png" pos 410, 245 action  SetVariable('act', 'night'), Jump("BedNight")
    imagebutton auto "BedButtonSleep_%s.png" pos 610, 245 action Jump("BedMorning")
    imagebutton auto "BedButtonNap_%s.png" pos 810, 245 action Jump("BedNap")
    imagebutton auto "ButtonBack_%s.png" pos 530, 430 action Jump("MyRoom")
screen Desk():
    tag explore
    add "DeskA.png"
    imagebutton auto "deskMirror_%s.png" pos 367, 0 action Jump("Mirror")
    imagebutton auto "desklaptop_%s.png" pos 496, 289 action Jump("Laptop")
    imagebutton auto "deskLeftDrawer_%s.png" pos 301, 555 action Jump("LeftDrawer")
    imagebutton auto "deskRightDrawers_%s.png" pos 682, 554 action Jump("RightDrawers")
    imagebutton auto "deskDoor_%s.png" pos 0, 0 action Show("MyRoomDoor")
screen MyRoomDoor():
    tag explore
    add "MyRoomExit.jpg"
    imagebutton auto "MyRoomCalendarButton_%s.png" pos 540, 60 action Call("Calendar")
    imagebutton auto "MyRoomLeaveButton_%s.png" pos 540, 240 action Jump("MyRoomLeave")
    imagebutton auto "MyRoomStayButton_%s.png" pos 540, 420 action Show("MyRoom")
####|---------------------------------------------|
## Hallway and rooms
screen Hall():
    tag explore
    add "Hallway.png"
    imagebutton auto "images/Hallway/LilyLisaRoom_%s.png" pos 98, 8 action Jump("LilyLisaRoom")
    imagebutton auto "images/Hallway/Stairs_%s.png" pos 365, 99 action Show("Stairs")
    imagebutton auto "images/Hallway/LeniLoriRoom_%s.png" pos 497, 255 action Show("LeniLoriRoom")
    #imagebutton auto "images/Hallway/BathroomDoor_%s.png" pos 585, 297 action [(Hide("Hall")), (Jump("Bathroomenter")
    imagebutton auto "images/Hallway/LuanLunaRoom_%s.png" pos 694, 255 action Show("LuanLunaRoom")
    imagebutton auto "images/Hallway/LucyLynnRoom_%s.png" pos 770, 161 action Show("LucyLynnRoom")
    imagebutton auto "images/Hallway/LanaLolaRoom_%s.png" pos 1004, 0 action Show("LanaLolaRoom")
    #imagebutton auto "images/Hallway/Attic_%s.png" pos 545, 154 action [(Hide("Hall")), (Jump("Attic")
    imagebutton auto "ButtonBack_%s.png" pos 560, 560 action Show("MyRoom")
screen Rooms():
    imagebutton auto "ButtonBack_%s.png" pos 550, 600 action Show("Hall")

screen LeniLoriRoom():
    tag explore
    add "images/LeniLoriRoom/LeniLoriRoom.jpg"
    imagebutton auto "images/LeniLoriRoom/LeniLoriDrawer_%s.png" pos 79, 288 action Jump("LeniLoriMirror")
    imagebutton auto "images/LeniLoriRoom/LeniLoriCloset_%s.png" pos 286, 223 action Jump("LeniLoriCloset")
    imagebutton auto "images/LeniLoriRoom/LoriBed_%s.png" pos 771, 387 action Show("LoriSide")
    imagebutton auto "images/LeniLoriRoom/LeniBed_%s.png" pos 896, 508 action Show("LeniSide")
    imagebutton auto "images/LeniLoriRoom/LeniLoriVent_%s.png" pos 246, 106 action Jump("LeniLoriVent")
    imagebutton auto "images/LeniLoriRoom/LeniLoriSewingMachine_%s.png" pos 378, 310 action Jump("SewingMachine")
    use Rooms
screen LuanLunaRoom():
    tag explore
    add "images/LuanLunaRoom/LuanLunaRoom.jpg"
    if MapShow == True:
        imagebutton auto "images/LuanLunaRoom/minimapLuanLuna_%s.png" pos 310, 20
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaLeft_%s.png" pos 310, 77 action Show("LuanLunaLeft")
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaRight_%s.png" pos 387, 77 action Show("LuanLunaRight")
    use Rooms
screen LucyLynnRoom():
    tag explore
    add "images/LucyLynnRoom/LucyLynnRoom.jpg"
    imagebutton auto "images/LucyLynnRoom/LucyBedButton_%s.png" pos 0, -4 action Show("LucyBed")
    imagebutton auto "images/LucyLynnRoom/LynnBedButton_%s.png" pos 752, 280 action Show("LynnBed")
    if MapShow == True:
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynn_%s.png" pos 310, 20
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnDesk_%s.png" pos 310, 102 action Show("LucyDesk")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnCloset_%s.png" pos 366, 102 action Show("LucyLynnCloset")
    use Rooms
screen LanaLolaRoom():
    tag explore
    add "images/LanaLolaRoom/LanaLolaRoom.jpg"
    imagebutton auto "images/LanaLolaRoom/LanaBedButton_%s.png" pos 0, 101 action Show("LanaBed")
    imagebutton auto "images/LanaLolaRoom/LolaBedButton_%s.png" pos 730, 0 action Show("LolaBed")
    if MapShow == True:
        imagebutton auto "images/LanaLolaRoom/minimapLolaLana_%s.png" pos 310, 20
        imagebutton auto "images/LanaLolaRoom/minimapLanaLolaEntrance_%s.png" pos 310, 91 action Jump ("ExitHall")
        imagebutton auto "images/LanaLolaRoom/minimapLolaTea_%s.png" pos 380, 91 action Show("LolaTea")
    use Rooms

screen Bathroom():
    tag explore
    add "images/Bathroom/Bathroom.jpg"
    imagebutton auto "images/Bathroom/BathroomVent_%s.png" pos 59, 554 action Jump("BathroomVent")
    imagebutton auto "images/Bathroom/BathroomSink_%s.png" pos 99, 0 action Jump ("BathroomSink")
    imagebutton auto "images/Bathroom/Shower_%s.png" pos 428, 52 action Jump ("BathTub")
    imagebutton auto "images/Bathroom/Toilet_%s.png" pos 887, 179 action Jump ("Toilet")
    imagebutton auto "images/Bathroom/BathroomExit_%s.png" pos 1132, 0 action Show("Hall")
    use Rooms
####|---------------------------------------------|
#### Down Stairs
screen Stairs():
    tag explore
    add "Stairs.png"
    imagebutton auto "StairsButtonLiving_%s.png" pos 530 , 90 action Show("LivingRoom")
    imagebutton auto "StairsButtonDining_%s.png" pos 530 , 310 action Show("DiningRoom")
    imagebutton auto "StairsButtonKitchen_%s.png" pos 530 , 530 action Show("Kitchen")
    use Rooms
screen DiningRoom():
    tag explore
    add "images/DiningRoom/DiningRoomEnter.png"
    if Tuesday == True and DayPhase == 4:
        imagebutton auto "images/Spirites/Lucy/Lucy_%s.png" pos 300, 200 action Jump("LucyTuesdayMorning3")
    if Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Spirites/Leni/Leni_%s.png" pos 300, 200 action Jump("LeniWednesdayAfternoon1")
    if Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Spirites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnWednesdayMorning3")
    if Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Spirites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnWednesdayAfternoon2")
    if Saturday == True and DayPhase == 6:
        imagebutton auto "images/Spirites/Lucy/Lucy_%s.png" pos 300, 200 action Jump("LucySaturdayAfternoon1")
    if Saturday == True and DayPhase == 7:
        imagebutton auto "images/Spirites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnSaturdayAfternoon2")
    if MapShow == True:
        imagebutton auto "images/DiningRoom/minimapDining_%s.png" pos 310, 20
        imagebutton auto "images/DiningRoom/minimapDiningExits_%s.png" pos 310, 20 action Show("DiningExits")
screen DiningExits():
    tag explore
    add "images/DiningRoom/DiningRoomExits.png"
    imagebutton auto "images/DiningRoom/DiningKitchenExit_%s.png" pos 693, 0 action Show("Kitchen")
    imagebutton auto "images/DiningRoom/DiningLivingExit_%s.png" pos 0, 106 action Show("LivingRoom")
    if MapShow == True:
        imagebutton auto "images/DiningRoom/minimapDining_%s.png" pos 310, 20
        imagebutton auto "images/DiningRoom/minimapDiningFront_%s.png" pos 386, 20 action Show("DiningRoom")
screen Kitchen():
    tag explore
    add "images/Kitchen/Kitchen.jpg"
    if Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 200 action Jump("LeniMondayMorning2")
    if Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 300, 200 action Jump("LucyMondayAfternoon1")
    if Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 200 action Jump("LunaMondayMorning3")
    if Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanWednesdayMorning3")
    if Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 600, 200 action Jump("LolaWednesdayMorning3")
    if Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 900, 200 action Jump("LanaWednesdayMorning3")
    if Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 200 action Jump("LeniWednesdayAfternoon2")
    if Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 600, 200 action Jump("LuanWednesdayAfternoon2")
    if Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 300, 200 action Jump("LanaWednesdayEvening")
    if Thursday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 200 action Jump("LeniThursdayAfternoon2")
    if Thursday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaThursdayEvening")
    if Friday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 600, 200 action Jump("LeniFridayMorning2")
    if Friday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanFridayMorning2")
    if Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 300, 200 action Jump("LanaFridayEvening")
    if MapShow == True:
        imagebutton auto "images/Kitchen/minimapKitchen_%s.png" pos 310, 20
        imagebutton auto "images/Kitchen/minimapKitchenBackExits_%s.png" pos 310, 20 action Show("Backdoor")
        imagebutton auto "images/Kitchen/minimapKitchenDiningExit_%s.png" pos 310, 93 action Jump("KitchenDiningExit")
screen Backdoor():
    tag explore
    add "images/Kitchen/KitchenDoorways.jpg"
    if MapShow == True:
        imagebutton auto "images/Kitchen/minimapKitchen_%s.png" pos 310, 20
        imagebutton auto "images/Kitchen/minimapKitchenDiningExit_%s.png" pos 310, 93 action Jump("KitchenDiningExit")
        imagebutton auto "images/Kitchen/minimapKitchenFront_%s.png" pos 388, 20 action Show("Kitchen")
    imagebutton auto "images/Kitchen/BasementDoor_%s.png" pos 83, 0 action Jump("Basement")
    imagebutton auto "images/Kitchen/BackyardDoorExit_%s.png" pos 1195, 0 action Jump("Backyard")
screen LivingRoom():
    tag explore
    add "images/LivingRoom/LivingRoomView.png"
    imagebutton auto "images/LivingRoom/LivingRoomStairs_%s.png" pos 458, 0 action Jump("Upstairs")
    imagebutton auto "images/LivingRoom/LivingDiningEntrance_%s.png" pos 1088, 0 action Show("DiningRoom")
    if Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 380, 200 action Jump("LynnMondayAfternoon1")
    if Monday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriMondayAfternoon2")
    if Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriTuesdayAfternoon2")
    if Monday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 200 action Jump("LunaMondayAfternoon2")
    if Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 380, 200 action Jump("LunaMondayEvening")
    if Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 500, 200 action Jump("LuanMondayEvening")
    if Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 200, 200 action Jump("LolaMondayEvening")
    if Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 500, 200 action Jump("LuanTuesdayAfternoon2")
    if Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriWednesdayEvening")
    if Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 200 action Jump("LunaWednesdayEvening")
    if Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 380, 200 action Jump("LanaWednesdayAfternoon1")
    if Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 500, 200 action Jump("LolaWednesdayAfternoon1")
    if Thursday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriThursdayMorning3")
    if Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriThursdayAfternoon1")
    if Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 500, 200 action Jump("LeniThursdayAfternoon1")
    if Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 200, 200 action Jump("LunaThursdayAfternoon1")
    if Thursday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 380, 200 action Jump("LeniThursdayEvening")
    if Thursday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 200 action Jump("LunaThursdayEvening")
    if Thursday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 380, 200 action Jump("LanaThursdayMorning2")
    if Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriFridayEvening")
    if Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 500, 200 action Jump("LeniFridayEvening")
    if Friday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 380, 200 action Jump("LuanFridayMorning3")
    if Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 200, 200 action Jump("LynnFridayEvening")
    if Saturday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 380, 200 action Jump("LoriSaturdayAfternoon2")
    if Saturday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 200, 200 action Jump("LeniSaturdayAfternoon2")
    if Saturday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 380, 200 action Jump("LuanSaturdayAfternoon1")
    if Saturday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 500, 200 action Jump("LynnSaturdayAfternoon1")
    if Saturday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 200, 200 action Jump("LolaSaturdayAfternoon1")
    if Saturday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 600, 200 action Jump("LanaSaturdayAfternoon1")
    #imagebutton auto "images/LivingRoom/MasterBedroomEntrance_%s.png" pos 0, 0 action Jump("Parentsroom")
    if MapShow == True:
        imagebutton auto "images/LivingRoom/minimapLivingRoom_%s.png" pos 310, 20
        imagebutton auto "images/LivingRoom/minimapLivingRoomFireplace_%s.png" pos 310, 45 action Jump("Fireplace")
        imagebutton auto "images/LivingRoom/minimapLivingRoomTV_%s.png" pos 346, 129 action Jump("TV")
        imagebutton auto "images/LivingRoom/minimapLivingRoomExit_%s.png" pos 459, 102 action Jump("LivingRoomExit")
####|---------------------------------------------|
#### Lori Leni Room
screen LoriSide():
    tag explore
    add "images/LeniLoriRoom/LoriBed.png"
    if Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriMondayMorning2")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriMondayMorning3")
    elif Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriMondayAfternoon1")
    elif Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriMondayEvening")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriTuesdayMorning1")
    elif Tuesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriTuesdayMorning2")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriWednesdayMorning2")
    elif Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriWednesdayMorning3")
    elif Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriWednesdayAfternoon2")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriThursdayMorning1")
    elif Thursday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriThursdayEvening")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriFridayMorning1")
    elif Friday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriFridayMorning2")
    elif Friday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriFridayMorning3")
    elif Friday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriFridayAfternoon1")
    elif Friday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriFridayAfternoon2")
    elif Saturday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lori/Lori_%s.png" pos 500, 90 action Jump("LoriSaturdayMorning1")
    imagebutton auto "ButtonBack_%s.png" pos 550, 600 action Show("LeniLoriRoom")
screen LeniSide():
    tag explore
    add "images/LeniLoriRoom/LeniBed.png"
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniMondayMorning1")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniMondayMorning3")
    elif Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniMondayEvening")
    elif Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniMondayAfternoon1")
    elif Monday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniMondayAfternoon2")
    elif Tuesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniTuesdayMorning2")
    elif Tuesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniTuesdayMorning3")
    elif Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LenTuesdayAfternoon2")
    elif Tuesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniTuesdayEvening")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniWednesdayMorning2")
    elif Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniWednesdayAfternoon1")
    elif Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniWednesdayEvening")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniThursdayMorning1")
    elif Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniThursdayAfternoon1")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniFridayMorning1")
    elif Friday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniFridayMorning3")
    elif Friday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniFridayAfternoon1")
    elif Friday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniFridayAfternoon2")
    elif Saturday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniSaturdayMorning1")
    elif Saturday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Leni/Leni_%s.png" pos 300, 90 action Jump("LeniSaturdayAfternoon1")
    imagebutton auto "ButtonBack_%s.png" pos 550, 600 action Show ("LeniLoriRoom")
####|---------------------------------------------|
#### Luan Luna
screen LuanLunaRight():
    tag explore
    add "images/LuanLunaRoom/LuanWall.jpg"
    if MapShow == True:
        imagebutton auto "images/LuanLunaRoom/minimapLuanLuna_%s.png" pos 310, 20
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaLeft_%s.png" pos 310, 77 action Show("LuanLunaLeft")
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaDefault_%s.png" pos 310, 20 action Show("LuanLunaRoom")
    imagebutton auto "images/LuanLunaRoom/LuanLunaRightExit_%s.png" pos 967, 26 action Show ("Hall")
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanMondayMorning1")
    elif Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanMondayMorning2")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanMondayMorning3")
    elif Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanMondayAfternoon1")
    elif Monday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanMondayAfternoon2")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanTuesdayMorning1")
    elif Tuesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanTuesdayMorning2")
    elif Tuesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanTuesdayAfternoon1")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanWednesdayMorning2")
    elif Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanWednesdayAfternoon1")
    elif Thursday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanThursdayMorning2")
    elif Thursday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanThursdayMorning3")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanFridayMorning1")
    elif Friday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanFridayAfternoon1")
    elif Friday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanFridayAfternoon2")
    elif Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanFridayEvening")
    elif Saturday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanSaturdayMorning1")
    elif Saturday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luan/Luan_%s.png" pos 300, 200 action Jump("LuanSaturdayMorning3")
screen LuanLunaLeft():
    tag explore
    add "images/LuanLunaRoom/LuanLunaLeftSide.png"
    imagebutton auto "images/LuanLunaRoom/LuanLunaLeftExit_%s.png" pos 57, 0 action Show ("Hall")
    imagebutton auto "images/LuanLunaRoom/LuanLunaCloset_%s.png" pos 329, 144 action Jump("LuanLunaCloset")
    imagebutton auto "images/LuanLunaRoom/LunaDrums_%s.png" pos 264, 334 action Jump("LunaDrums")
    imagebutton auto "images/LuanLunaRoom/LuanLunaLeftBeds_%s.png" pos 776, 119 action Show("LuanLunaBeds")
    imagebutton auto "images/LuanLunaRoom/LuanLunaLadder_%s.png" pos 933, 173 action Jump("LunaBed")
    if MapShow == True:
        imagebutton auto "images/LuanLunaRoom/minimapLuanLuna_%s.png" pos 310, 20
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaRight_%s.png" pos 387, 77 action Show("LuanLunaRight")
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaDefault_%s.png" pos 310, 20 action Show("LuanLunaRoom")
screen LuanLunaBeds():
    tag explore
    add "images/LuanLunaRoom/LuanLunaBeds.png"
    if MapShow == True:
        imagebutton auto "images/LuanLunaRoom/minimapLuanLuna_%s.png" pos 310, 20
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaRight_%s.png" pos 387, 77 action Show("LuanLunaRight")
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaLeft_%s.png" pos 310, 77 action Show("LuanLunaLeft")
        imagebutton auto "images/LuanLunaRoom/minimapLuanLunaDefault_%s.png" pos 310, 20 action Show("LuanLunaRoom")
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaMondayMorning1")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaMondayMorning2")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaTuesdayMorning1")
    elif Tuesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaTuesdayMorning2")
    elif Tuesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaTuesdayMorning3")
    elif Tuesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaTuesdayAfternoon1")
    elif Tuesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaTuesdayEvening")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaWednesdayMorning2")
    elif Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaWednesdayAfternoon1")
    elif Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaWednesdayAfternoon2")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaThursdayMorning1")
    elif Thursday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaThursdayMorning2")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaFridayMorning1")
    elif Friday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaFridayMorning2")
    elif Saturday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Luna/Luna_%s.png" pos 500, 210 action Jump("LunaSaturdayMorning1")
####|---------------------------------------------|
#### Lucy Lynn
screen LucyDesk():
    tag explore
    add "images/LucyLynnRoom/LucyDesk.jpg"
    if MapShow == True:
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynn_%s.png" pos 310, 20
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnBeds_%s.png" pos 310, 20 action Jump("LucyLynnRoom")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnCloset_%s.png" pos 366, 102 action Show ("LucyLynnCloset")
    imagebutton auto "images/LucyLynnRoom/LucyDeskDoor_%s.png" pos 0, 0 action Show ("Hall")
screen LucyLynnCloset():
    tag explore
    add "images/LucyLynnRoom/LucyLynnCloset.jpg"
    imagebutton auto "images/LucyLynnRoom/LucyLynnCloset_%s.png" pos 62, 27 action Jump("LucyLynnCloset")
    imagebutton auto "images/LucyLynnRoom/LynnDoorExit_%s.png" pos 507, 34 action Show ("Hall")
    if MapShow == True:
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynn_%s.png" pos 310, 20
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnBeds_%s.png" pos 310, 20 action Jump("LucyLynnRoom")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnDesk_%s.png" pos 310, 102 action Show ("LucyDesk")
screen LucyBed():
    tag explore
    add "images/LucyLynnRoom/LucyBed.jpg"
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyMondayMorning1")
    elif Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyMondayMorning2")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyMondayMorning3")
    elif Monday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyMondayAfternoon2")
    elif Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyMondayEvening")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyTuesdayMorning1")
    elif Tuesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyTuesdayMorning2")
    elif Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyTuesdayAfternoon2")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyWednesdayMorning2")
    elif Wednesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyWednesdayMorning3")
    elif Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyWednesdayAfternoon1")
    elif Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyWednesdayEvening")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyThursdayMorning1")
    elif Thursday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyThursdayMorning3")
    elif Thursday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lucy/Lucy_%s.png" pos 400, 215 action Jump("LucyThursdayAfternoon2")
    if MapShow == True:
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynn_%s.png" pos 310, 20
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnBeds_%s.png" pos 310, 20 action Jump("LucyLynnRoom")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnDesk_%s.png" pos 310, 102 action Show("LucyDesk")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnCloset_%s.png" pos 366, 102 action Show("LucyLynnCloset")
screen LynnBed():
    tag explore
    add "images/LucyLynnRoom/LynnBed.jpg"
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnMondayMorning1")
    elif Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnMondayMorning2")
    elif Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnMondayEvening")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnTuesdayMorning1")
    elif Tuesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnTuesdayMorning3")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnWednesdayMorning1")
    elif Wednesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnWednesdayAfternoon1")
    elif Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnWednesdayEvening")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnThursdayMorning1")
    elif Thursday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnThursdayMorning3")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnFridayMorning1")
    elif Saturday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnSaturdayMorning1")
    elif Saturday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lynn/Lynn_%s.png" pos 300, 200 action Jump("LynnSaturdayMorning2")
    if MapShow == True:
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynn_%s.png" pos 310, 20
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnBeds_%s.png" pos 310, 20 action Jump("LucyLynnRoom")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnDesk_%s.png" pos 310, 102 action Show("LucyDesk")
        imagebutton auto "images/LucyLynnRoom/minimapLucyLynnCloset_%s.png" pos 366, 102 action Show("LucyLynnCloset")
####|---------------------------------------------|
#### Lana Lola
screen LanaBed():
    tag explore
    add "images/LanaLolaRoom/LanaBed.jpg"
    if Monday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaMondayMorning1")
    elif Monday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaMondayEvening")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaTuesdayMorning1")
    elif Tuesday == True and DayPhaose == 9:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaTuesdayEvening")
    elif Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaTuesdayAfternoon2")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaWednesdayMorning1")
    elif Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaWednesdayAfternoon2")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaThursdayMorning1")
    elif Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaThursdayAfternoon1")
    elif Thursday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaThursdayEvening")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaFridayMorning1")
    elif Friday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaFridayAfternoon1")
    elif Friday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaFridayAfternoon2")
    elif Saturday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lana/Lana_%s.png" pos 580, 320 action Jump("LanaSaturdayMorning3")
    if MapShow == True:
        imagebutton auto "images/LanaLolaRoom/minimapLolaLana_%s.png" pos 310, 20
        imagebutton auto "images/LanaLolaRoom/minimapLolaLanaDefault_%s.png" pos 310, 20 action Show("LanaLolaRoom")
        imagebutton auto "images/LanaLolaRoom/minimapLanaLolaEntrance_%s.png" pos 310, 91 action Jump("ExitHall")
        imagebutton auto "images/LanaLolaRoom/minimapLolaTea_%s.png" pos 380, 91 action Show("LolaTea")
screen LolaBed():
    tag explore
    add "images/LanaLolaRoom/LolaBed.png"
    if Monday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaMondayMorning2")
    elif Monday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaMondayMorning3")
    elif Monday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaMondayAfternoon1")
    elif Tuesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayMorning1")
    elif Tuesday == True and Dayphase == 3:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayMorning2")
    elif Tuesday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayMorning3")
    elif Tuesday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayAfternoon1")
    elif Tuesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayAfternoon2")
    elif Tuesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaTuesdayEvening")
    elif Wednesday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaWednesdayMorning1")
    elif Wednesday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaWednesdayMorning2")
    elif Wednesday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaWednesdayAfternoon2")
    elif Wednesday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaWednesdayEvening")
    elif Thursday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaThursdayMorning1")
    elif Thursday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaThursdayAfternoon2")
    elif Thursday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaThursdayMorning3")
    elif Thursday == True and DayPhase == 6:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaThursdayAfternoon1")
    elif Friday == True and DayPhase == 1:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaFridayMorning1")
    elif Friday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaFridayMorning2")
    elif Friday == True and DayPhase == 4:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaFridayMorning3")
    elif Friday == True and DayPhase == 7:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaFridayAfternoon2")
    elif Friday == True and DayPhase == 9:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaFridayEvening")
    elif Saturday == True and DayPhase == 3:
        imagebutton auto "images/Sprites/Lola/Lola_%s.png" pos 300, 200 action Jump("LolaSaturdayMorning2")
    imagebutton auto "images/LanaLolaRoom/LanaLolaCloset_%s.png" pos 945, 0 action Jump("LanaLolaCloset")
    if MapShow == True:
        imagebutton auto "images/LanaLolaRoom/minimapLolaLana_%s.png" pos 310, 20
        imagebutton auto "images/LanaLolaRoom/minimapLolaLanaDefault_%s.png" pos 310, 20 action Show("LanaLolaRoom")
        imagebutton auto "images/LanaLolaRoom/minimapLanaLolaEntrance_%s.png" pos 310, 91 action Jump("ExitHall")
        imagebutton auto "images/LanaLolaRoom/minimapLolaTea_%s.png" pos 380, 91 action Show("LolaTea")
screen LolaTea():
    tag explore
    add "images/LanaLolaRoom/LolaTea.png"
    imagebutton auto "images/LanaLolaRoom/kitchenplaysetdoor_%s.png" pos 941, 0 action Jump("ExitHall")
    imagebutton auto "images/LanaLolaRoom/kitchenplaysetoven_%s.png" pos 481, 282 action Jump("LolaKitchenSet")
    imagebutton auto "images/LanaLolaRoom/LolaTable_%s.png" pos 15, 437 action Jump("LolaTableSet")
    if MapShow == True:
        imagebutton auto "images/LanaLolaRoom/minimapLolaLana_%s.png" pos 310, 20
        imagebutton auto "images/LanaLolaRoom/minimapLolaLanaDefault_%s.png" pos 310, 20 action Show("LanaLolaRoom")
        imagebutton auto "images/LanaLolaRoom/minimapLanaLolaEntrance_%s.png" pos 310, 91 action Jump("ExitHall")
screen LolaSide():
    tag explore
    imagemap:
        ground "LolaCloset.jpg"
        hover "LolaClosetb.jpg"

        hotspot (939, 0, 303, 695) clicked Jump("LolaCloset")
####|---------------------------------------------|
