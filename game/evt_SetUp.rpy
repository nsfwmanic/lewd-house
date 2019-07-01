##  Stats defaults
##  Places, People, and Activities
default acom        = "Acommon"
default aloc        = "Alocation"
default aper        = "Aperson"
default period      = acom
default act         = "room"

## Declare characters used by this game. The color argument colorizes the name
## of the character.
define me = Character('Me', color='#F4F4F5')
define linc = Character('Lincoln', color='#F4F4F5')
define lucy = Character('Lucy', color='#231F20')
define lori = Character('Lori', color='#ADDDF3')
define leni = Character('Leni', color='#A3D7B1')
define luna = Character('Luna', color='#62457A')
define luan = Character('Luan', color='#EEE563')
define lynn = Character('Lynn', color='#BE1F2F')
define lucy = Character('Lucy', color='#231F20')
define lana = Character('Lana', color='#41566B')
define lola = Character('Lola', color='#F56598')
define lisa = Character('Lisa', color='#92B945')
define Ri = Character('Mom', color='#F97363')
define Ra = Character('Ronnie Anne', color='#E0AD76')
define Carol = Character('Carol', color='#7599CF')
define You = Character ('You', color = '#be860d')
define wiperight = CropMove(0.3, "wiperight")

##Flags
define TalkedLori = False
define TalkedLeni = False
define TalkedLuan = False
define TalkedLuna = False
define TalkedLynn = False
define TalkedLucy = False
define TalkedLana = False
define TalkedLola = False
define LoriAffection = 0
define LeniAffection = 0
define LunaAffection = 0
define LuanAffection = 0
define LynnAffection = 0
define LucyAffection = 0
define LanaAffection = 0
define LolaAffection = 0
define LisaAffection = 0
define RonnieAffection = 0
define CarolAffection = 0


##Week
define weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
default time_of_day = 'morning'     ## DayPhase = morning,afternoon,evening,night
define Monday = True
define Tuesday = False
define Wednesday = False
define Thursday = False
define Friday = False
define Saturday = False
define Sunday = False
define DayPhase = 0
define SmartShow = False
define MapShow = False

##WeekUI
define MondayM1 = "images/DayUI/Monday/MondayM1.png"
define MondayM2 = "images/DayUI/Monday/MondayM2.png"
define MondayM3 = "images/DayUI/Monday/MondayM3.png"
define MondayA1 = "images/DayUI/Monday/MondayA1.png"
define MondayA2 = "images/DayUI/Monday/MondayA2.png"
define MondayEve = "images/DayUI/Monday/MondayEve.png"
define MondayNight = "images/DayUI/Monday/MondayNight.png"
define MondayMidnight = "images/DayUI/Monday/MondayMidnight.png"
define TuesdayM1 = "images/DayUI/Tuesday/TuesdayM1.png"
define TuesdayM2 = "images/DayUI/Tuesday/TuesdayM2.png"
define TuesdayM3 = "images/DayUI/Tuesday/TuesdayM3.png"
define TuesdayA1 = "images/DayUI/Tuesday/TuesdayA1.png"
define TuesdayA2 = "images/DayUI/Tuesday/TuesdayA2.png"
define TuesdayEve = "images/DayUI/Tuesday/TuesdayEve.png"
define TuesdayNight = "images/DayUI/Tuesday/TuesdayNight.png"
define TuesdayMidnight = "images/DayUI/Tuesday/TuesdayMidnight.png"
define WednesdayM1 = "images/DayUI/Wednesday/WednesdayM1.png"
define WednesdayM2 = "images/DayUI/Wednesday/WednesdayM2.png"
define WednesdayM3 = "images/DayUI/Wednesday/WednesdayM3.png"
define WednesdayA1 = "images/DayUI/Wednesday/WednesdayA1.png"
define WednesdayA2 = "images/DayUI/Wednesday/WednesdayA2.png"
define WednesdayEve = "images/DayUI/Wednesday/WednesdayEve.png"
define WednesdayNight = "images/DayUI/Wednesday/WednesdayNight.png"
define WednesdayMidnight = "images/DayUI/Wednesday/WednesdayMidnight.png"
define ThursdayM1 = "images/DayUI/Thursday/ThursdayM1.png"
define ThursdayM2 = "images/DayUI/Thursday/ThursdayM2.png"
define ThursdayM3 = "images/DayUI/Thursday/ThursdayM3.png"
define ThursdayA1 = "images/DayUI/Thursday/ThursdayA1.png"
define ThursdayA2 = "images/DayUI/Thursday/ThursdayA2.png"
define ThursdayEve = "images/DayUI/Thursday/ThursdayEve.png"
define ThursdayNight = "images/DayUI/Thursday/ThursdayNight.png"
define ThursdayMidnight = "images/DayUI/Thursday/ThursdayMidnight.png"
define FridayM1 = "images/DayUI/Friday/FridayM1.png"
define FridayM2 = "images/DayUI/Friday/FridayM2.png"
define FridayM3 = "images/DayUI/Friday/FridayM3.png"
define FridayA1 = "images/DayUI/Friday/FridayA1.png"
define FridayA2 = "images/DayUI/Friday/FridayA2.png"
define FridayEve = "images/DayUI/Friday/FridayEve.png"
define FridayNight = "images/DayUI/Friday/FridayNight.png"
define FridayMidnight = "images/DayUI/Friday/FridayMidnight.png"
define SaturdayM1 = "images/DayUI/Saturday/SaturdayM1.png"
define SaturdayM2 = "images/DayUI/Saturday/SaturdayM2.png"
define SaturdayM3 = "images/DayUI/Saturday/SaturdayM3.png"
define SaturdayA1 = "images/DayUI/Saturday/SaturdayA1.png"
define SaturdayA2 = "images/DayUI/Saturday/SaturdayA2.png"
define SaturdayEve = "images/DayUI/Saturday/SaturdayEve.png"
define SaturdayNight = "images/DayUI/Saturday/SaturdayNight.png"
define SaturdayMidnight = "images/DayUI/Saturday/SaturdayMidnight.png"
define SundayM1 = "images/DayUI/Sunday/SundayM1.png"
define SundayM2 = "images/DayUI/Sunday/SundayM2.png"
define SundayM3 = "images/DayUI/Sunday/SundayM3.png"
define SundayA1 = "images/DayUI/Sunday/SundayA1.png"
define SundayA2 = "images/DayUI/Sunday/SundayA2.png"
define SundayEve = "images/DayUI/Sunday/SundayEve.png"
define SundayNight = "images/DayUI/Sunday/SundayNight.png"
define SundayMidnight = "images/DayUI/Sunday/SundayMidnight.png"


## Sprites.
image Lana = "images/Sprites/Lana.png"
image LanaNeutral = "images/Sprites/Lana/Lana_Idle.png"
image LanaTalk = "images/Sprites/Lana/Lana_Hover.png"
image LanaNeutralBlush = "images/Sprites/Lana/LanaNeutralBlush.png"
image LanaTalkBlush = "images/Sprites/Lana/LanaTalkBlush.png"
image LanaDialogueSprite = "images/Sprites/Lana/LanaDialogueSprite.png"
image LanaDialogueSpriteb = "images/Sprites/Lana/LanaDialogueSpriteb.png"

image Leni = "images/Sprites/Leni.png"
image LeniNeutral = "images/Sprites/Leni/Leni_Idle.png"
image LeniTalk = "images/Sprites/Leni/Leni_Hover.png"
image LeniTalkOwnRoom = "images/Sprites/Leni/LeniTalkOwnRoom.png"
image LeniNeutralOwnRoom = "images/Sprites/Leni/LeniNeutralOwnRoom.png"
image LeniTalkOwnRoomBlush = "images/Sprites/Leni/LeniTalkOwnRoomBlush.png"
image LeniNeutralOwnRoomBlush = "images/Sprites/Leni/LeniNeutralOwnRoomBlush.png"

image Lisa = "images/Sprites/Lisa.png"
image LisaNeutral = "images/Sprites/Lisa/LisaTalk.png"
image LisaTalk = "images/Sprites/Lisa/LisaTalk.png"
image LisaSmile = "images/Sprites/Lisa/LisaSmile.png"
image LisaSmileBlush = "images/Sprites/Lisa/LisaSmileBlush.png"
image LisaSmileTalk = "images/Sprites/Lisa/LisaSmileTalk.png"
image LisaTalkSpit = "images/Sprites/Lisa/LisaTalkSpit.png"


image Lola = "images/Sprites/Lola.png"
image LolaNeutral = "images/Sprites/Lola/Lola_Idle.png"
image LolaTalk = "images/Sprites/Lola/Lola_Hover.png"
image LolaAnnoyedTalkBlush = "images/Sprites/Lola/LolaAnnoyedTalkBlush.png"
image LolaAnnoyedNeutralBlush = "images/Sprites/Lola/LolaAnnoyedNeutralBlush.png"
image LolaDialogueSprite = "images/Sprites/Lola/LolaDialogueSprite.png"
image LolaDialogueSpriteb = "images/Sprites/Lola/LolaDialogueSpriteb.png"

image Lori = "images/Sprites/Lori.png"
image LoriNeutral = "images/Sprites/Lori/Lori_Idle.png"
image LoriTalk = "images/Sprites/Lori/Lori_Hover.png"
image LoriTalkOwnRoom = "images/Sprites/Lori/LoriTalkOwnRoom.png"
image LoriNeutralOwnRoom = "images/Sprites/Lori/LoriNeutralOwnRoom.png"
image LoriTalkOwnRoomBlush = "images/Sprites/Lori/LoriTalkOwnRoomBlush.png"
image LoriNeutralOwnRoomBlush = "images/Sprites/Lori/LoriNeutralOwnRoomBlush.png"
image LoriTalkOwnRoomBlush2 = "images/Sprites/Lori/LoriTalkOwnRoomBlush2.png"

image Luan = "images/Sprites/Luan.png"
image LuanNeutral = "images/Sprites/Luan/Luan_Idle.png"
image LuanTalk = "images/Sprites/Luan/Luan_Hover.png"
image LuanNeutralBlush = "images/Sprites/Luan/LuanNeutralBlush.png"
image LuanTalkBlush = "images/Sprites/Luan/LuanTalkBlush.png"
image LuanDialogueSprite = "images/Sprites/Luan/LuanDialogueSprite.png"
image LuanDialogueSpriteb = "images/Sprites/Luan/LuanDialogueSpriteb.png"

image Lucy = "images/Sprites/Lucy.png"
image LucyNeutral = "images/Sprites/Lucy/Lucy_Idle.png"
image LucyTalk = "images/Sprites/Lucy/Lucy_Hover.png"
image LucyNeutralBlush = "images/Sprites/Lucy/LucyNeutralBlush.png"
image LucyTalkBlush = "images/Sprites/Lucy/LucyTalkBlush.png"
image LucySmileTalkBlush = "images/Sprites/Lucy/LucySmileTalkBlush.png"
image LucySmileBlush = "images/Sprites/Lucy/LucySmileBlush.png"
image LucyDialogueSprite = "images/Sprites/Lucy/LucyDialogueSprite.png"
image LucyDialogueSpriteb = "images/Sprites/Lucy/LucyDialogueSpriteb.png"

image Luna = "images/Sprites/Luna.png"
image LunaNeutral = "images/Sprites/Luna/Luna_Idle.png"
image LunaTalk = "images/Sprites/Luna/Luna_Hover.png"
image LunaDialogueSprite = "images/Sprites/Luna/LunaDialogueSprite.png"
image LunaDialogueSpriteb = "images/Sprites/Luna/LunaDialogueSpriteb.png"
image LunaNeutralBlush = "images/Sprites/Luna/LunaNeutralBlush.png"
image LunaTalkBlush = "images/Sprites/Luna/LunaTalkBlush.png"
image LunaTalkBlush2 = "images/Sprites/Luna/LunaTalkBlush2.png"
image LunaNude = "images/Sprites/Luna/LunaNude.png"

image Lynn = "images/Sprites/Lynn.png"
image LynnNeutral = "images/Sprites/Lynn/Lynn_Idle.png"
image LynnTalk = "images/Sprites/Lynn/Lynn_Hover.png"
image LynnNeutralBlush = "images/Sprites/Lynn/LynnNeutralBlush.png"
image LynnTalkBlush = "images/Sprites/Lynn/LynnTalkBlush.png"
image LynnDialogueSprite = "images/Sprites/Lynn/LynnDialogueSprite.png"
image LynnDialogueSpriteb = "images/Sprites/Lynn/LynnDialogueSpriteb.png"

image Rita = "images/Sprites/Rita.png"

image Ronnie Anne = "images/Sprites/Ronnie Anne.png"
image RonnieAnneNeutral = "images/Sprites/RonnieAnne/RonnieAnneTalk.png"
image RonnieAnneTalk = "images/Sprites/RonnieAnne/RonnieAnneTalk.png"

image Carol = "images/Sprites/Carol.png"
image CarolNeutral = "images/Sprites/Carol/CarolTalk.png"
image CarolTalk = "images/Sprites/Carol/CarolTalk.png"
define default_sprite = Position(xpos=800, ypos=615)

## Day Phases.
image bg Morning = "Morning.jpg"
image bg HouseDay = "HouseDay.jpg"
image bg HouseSunset = "HouseSunset.jpg"
image bg HouseNight = "Night/HouseNight.jpg"

## Locations.
image bg MyRoom = "MyRoom.jpg"
image bg = "MyRoom.jpg"
image bg MyRoomNight= "images/Night/MyRoomNight.jpg"
image bg MyRoomExit = "MyRoomExit.jpg"
image bg BedEnter = "BedEnter.jpg"
image bg BedSleep = "BedSleep.png"
image bg Desk = "Desk.jpg"
image bg MyMirror = "MyMirror.jpg"
image bg Laptop = "Laptop.jpg"
image bg Laptopb = "Laptopb.jpg"
#image bg Phone = "Phone.jpg"
image bg Drawer = "Drawer.jpg"
#image bg Trunk = "Trunk.jpg"
image bg Calendar = "Calendar.jpg"
image bg Underbed = "Underbed.jpg"
image bg OutsideMyRoomHall = "OutsideMyRoomHall.jpg"
image bg DiningRoom = "DiningRoom.jpg"
image bg UnderTable = "UnderTable.jpg"
image bg DiningRoomWindow = "DiningRoomWindow.jpg"
image bg TrophyCase = "TrophyCase.jpg"
image bg Kitchen = "images/Kitchen/Kitchen.jpg"
image bg KitchenFridge = "images/Kitchen/KitchenFridge.jpg"
image bg KitchenDoorways = "images/Kitchen/KitchenDoorways.jpg"
image bg KitchenDiningExit = "images/Kitchen/KitchenDiningExit.png"
image bg DiningRoomEntrance = "images/DiningRoom/DiningRoomEnter.png"
image bg DiningRoomExits = "images/DiningRoom/DiningRoomExits.png"
image bg Backyard = "images/Backyard/Backyard.jpg"
image bg BackdoorOutside = "images/Backyard/BackdoorOutside.jpg"
image bg BasementSteps = "images/Basement/BasementSteps.jpg"
image bg BasementBoiler = "images/Basement/BasementBoiler.jpg"
image bg CircuitBreaker = "images/Basement/CircuitBreaker.jpg"
image bg LaundryPile = "images/Basement/LaundryPile.jpg"
image bg LaundryMachines = "images/Basement/LaundryMachines.jpg"
image bg LivingRoomCenter = "images/LivingRoom/LivingRoomCenter.jpg"
image bg TV = "images/LivingRoom/TV.jpg"
image bg Fireplace = "images/LivingRoom/Fireplace.jpg"
image bg LivingRoomArmchair = "images/LivingRoom/LivingRoomArmchair.jpg"
image bg LivingRoomEnter = "images/LivingRoom/LivingRoomEnter.png"
image bg LivingRoomCouch = "images/LivingRoom/LivingRoomCouch.jpg"
image bg StairsGoingUp = "images/LivingRoom/StairsGoingUp.jpg"
image bg ParentsRoomOpen = "ParentsRoomOpen.jpg"
image bg ParentsRoomClosetOpen = "ParentsRoomClosetOpen.jpg"
image bg ParentsClosetInside = "ParentsClosetInside.jpg"
image bg FrontDoorInside = "images/LivingRoom/FrontDoorInside.jpg"
image bg FrontDoorDining = "images/LivingRoom/FrontDoorDining.png"
image bg FrontPorch = "FrontPorch.jpg"
image bg LilyLisaRoom = "images/LisaLilyRoom/LilyLisaRoom.png"
image bg Stairs = "Stairs.png"
image bg LoriBed = "images/LeniLoriRoom/LoriBed.png"
image bg LeniBed = "images/LeniLoriRoom/LeniBed.png"
image bg LeniLoriRoom = "images/LeniLoriRoom/LeniLoriRoom.jpg"
image bg LeniLoriBeds = "images/LeniLoriRoom/LeniLoriBeds.jpg"
image bg LoriVentClosed = "images/LeniLoriRoom/LoriVentClosed.jpg"
image bg LeniLoriMirror = "images/LeniLoriRoom/LeniLoriMirror.jpg"
image bg LoriUnderBedA = "images/LeniLoriRoom/LoriUnderBedA.jpg"
image bg LoriUnderBedB = "images/LeniLoriRoom/LoriUnderBedB.jpg"
image bg SewingMachine = "images/LeniLoriRoom/SewingMachine.jpg"
image bg LeniLoriCloset = "images/LeniLoriRoom/LeniLoriCloset.jpg"
image bg LeniLoriRoomExit = "images/LeniLoriRoom/LeniLoriRoomExit.jpg"
image bg BathroomEntrance = "images/Bathroom/BathroomEntrance.jpg"
image bg BathroomSink = "images/Bathroom/BathroomSink.jpg"
image bg Bathroom = "images/Bathroom/Bathroom.jpg"
image bg BathTub = "images/Bathroom/BathTub.jpg"
image bg ShowerInUse = "images/Bathroom/ShowerInUse.jpg"
image bg Toilet = "images/Bathroom/Toilet.jpg"
image bg BathroomVent = "images/Bathroom/BathroomVent.jpg"
image bg VentsSideLight = "VentsSideLight.jpg"
image bg VentsTurn = "VentsTurn.jpg"
image bg VentsSide = "VentsSide.jpg"
image bg VentEnd = "VentEnd.jpg"
image bg LuanLunaRoom = "images/LuanLunaRoom/LuanLunaRoom.jpg"
image bg LuanLunaLeftSide ="images/LuanLunaRoom/LuanLunaLeftSide.png"
image bg LuanLunaBeds = "images/LuanLunaRoom/LuanLunaBeds.png"
image bg LuanWall = "images/LuanLunaRoom/LuanWall.jpg"
image bg LunaBed = "images/LuanLunaRoom/LunaBed.jpg"
image bg LuanBed = "images/LuanLunaRoom/LuanBed.jpg"
#image bg LuanLunaRoomCloset = "images/LuanLunaRoom/LuanLunaRoomCloset.jpg"
image bg LuanLunaClosetInside = "images/LuanLunaRoom/LuanLunaClosetInside.jpg"
image bg LucyLynnRoom = "images/LucyLynnRoom/LucyLynnRoom.jpg"
image bg LucyBed = "images/LucyLynnRoom/LucyBed.jpg"
image bg LynnBed = "images/LucyLynnRoom/LynnBed.jpg"
image bg LucyDesk = "images/LucyLynnRoom/LucyDesk.jpg"
image bg LucyLynnCloset = "images/LucyLynnRoom/LucyLynnCloset.jpg"
image bg LucyLynnClosetOpen = "images/LucyLynnRoom/LucyLynnClosetOpen.jpg"
image bg LanaLolaRoom = "images/LanaLolaRoom/LanaLolaRoom.jpg"
image bg LanaBed = "images/LanaLolaRoom/LanaBed.jpg"
image bg LolaBed = "images/LanaLolaRoom/LolaBed.png"
#image bg LolaPlayKitchen = "images/LanaLolaRoom/LolaPlayKitchen.jpg"
image bg LolaCloset = "images/LanaLolaRoom/LolaCloset.jpg"
image bg LolaClosetOpen = "images/LanaLolaRoom/LolaClosetOpen.jpg"
image bg LanaLolaRoomExit = "images/LanaLolaRoom/LanaLolaRoomExit.jpg"
image bg AtticEntrance = "images/Attic/AtticEntrance.jpg"
image bg AtticFull = "images/Attic/AtticFull.jpg"
image bg AtticBoxes = "images/Attic/AtticBoxes.jpg"
image bg AtticLamp = "images/Attic/AtticLamp.jpg"
image bg AtticTV = "images/Attic/AtticTV.jpg"
image bg AtticExit = "images/Attic/AtticExit.jpg"
image bg LisaLilyDoor = "LisaLilyDoor.png"
image bg DoorClosed = "DoorClosed.png"
image bg HouseLightsOff = "images/Night/HouseLightsOff.png"
image bg HallwayRoomNightIdle = "images/Night/HallwayRoomNight_Idle.png"
image bg HallwayRoomNightHover = "images/Night/HallwayRoomNight_Hover.png"
image bg LuanLunaRoomNight = "images/Night/LuanLunaRoomNight.png"
image bg LuanSleep = "images/Night/LuanSleep.png"
image bg LunaSleep = "images/Night/LunaSleep.png"
image bg LucyLynnSleep = "images/Night/LucyLynnSleep.png"
image bg LolaLanaRoomNight = "images/Night/LolaLanaRoomNight.png"
image bg LolaSleep = "images/Night/LolaSleep.png"
image bg LanaSleep = "images/Night/LanaSleep.png"
image bg LisaSleep = "images/Night/LisaSleep.png"
image bg LeniLoriRoomNight = "images/Night/LeniLoriRoomNight.png"
image bg LeniSleep1 = "images/Night/LeniSleep1.png"
image bg LeniSleep2 = "images/Night/LeniSleep2.png"
image bg LeniSleep3 = "images/Night/LeniSleep3.png"
image bg LeniSleep4 = "images/Night/LeniSleep4.png"
image bg LoriSleep = "images/Night/LoriSleep.png"
image bg BathroomNightLights = "images/Night/BathroomNightLights.png"
image bg NightBathroomClosed = "images/Night/NightBathroomClosed.png"
image bg LivingroomNightDownstairs = "images/Night/LivingRoomNight.png"
image bg LivingRoomNight = "images/Night/LivingRoomNight.png"
image bg NightUpstairs = "images/Night/NightUpstairs.png"
image bg ParentsNight = "images/Night/ParentsNight.png"
image bg DiningRoomNight = "images/Night/DiningRoomNight.png"
image bg DiningWindowNight = "images/Night/DiningWindowNight.png"
image bg UnderTableNight = "images/Night/UnderTableNight.png"
image bg KitchenNightInside = "images/Night/KitchenNightInside.png"
image bg NightFrontDoorClosed = "images/Night/NightFrontDoorClosed.png"
image bg NightFrontDoorOpen = "images/Night/NightFrontDoorOpen.png"
image bg NightSteps = "images/Night/NightSteps.png"
image bg NightNeighborhood2 = "images/Night/NightNeighborhood2.png"
image bg NightNeighborhood1 = "images/Night/NightNeighborhood1.png"
image bg Garage = "Garage.png"
image bg DeskA = "DeskA.png"
image bg DeskB = "DeskB.png"
image bg LeftDrawer = "LeftDrawer.png"
image bg RightDrawers = "RightDrawers.png"
image bg Hallway = "Hallway.png"
image bg LolaTea = "images/LanaLolaRoom/LolaTea.png"

## Movie.
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0,loops=0)

## Clickable.
image bg MyRoomExitb = "MyRoomExitb.jpg"

##Stat defines

## SFX.
define audio.Sink = "music/SFX/Sink.mp3"
define audio.Shower = "music/SFX/Shower.mp3"
define audio.Toilet = "music/SFX/Toilet.mp3"
define audio.Fap = "music/SFX/Fap.mp3"

## Music.

## Intro
image Splash = "Splash.jpg"
image Disclaimer = "Disclaimer.jpg"



##      Init
init -1 python:
    from operator import attrgetter
    import datetime

init python:
    date = datetime.date(2,4,30)
    startdate = datetime.date(2,5,1)
    year = datetime.timedelta(days=365)
    day1 = datetime.timedelta(days=1)
    week1 = datetime.timedelta(weeks=1)
    enddate = datetime.date(2,8,1)
    style.say_dialogue.drop_shadow = [(1, 1)]
    style.say_dialogue.outlines = [(1, "#000000", 0, 0)]
    style.say_dialogue.line_spacing = 5
    style.confirm_prompt_text.outlines = [(2, "#000000", 0, 0 )]

    ## Classes and other init processes
    inv_page = 0
    item = []
    class Item:
        def __init__(self, name, image, cost=0):
            self.image = image
            self.name = name
            self.cost = cost
    class Inventory(store.object):
        def __init__(self, money = 10):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False
        def earn(self, amount):
            self.money += amount
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False

    def item_use():
        item.use()
    def scenes(bg):
        renpy.scene()
        renpy.show(bg)
        #Tooltips:


    style.button.background=Frame("gui/FrameItem.png", 25, 25)
    style.button.yminimum=None
    style.button.xminimum=None
    style.button_text.color="000"




    ##########Hiding the smartphone screens when we close it#################
    def hide_screens():
        renpy.hide_screen("inventory_screen")
        renpy.hide_screen("MapUpstairs")
        renpy.hide_screen("MapDownstairs")
        renpy.hide_screen("StatScreen")
        renpy.hide_screen("gui_tooltip")

    def hide_stats():
        renpy.hide_screen("StatsLori")
        renpy.hide_screen("StatsLeni")
        renpy.hide_screen("StatsLuna")
        renpy.hide_screen("StatsLuan")
        renpy.hide_screen("StatsLynn")
        renpy.hide_screen("StatsLucy")
        renpy.hide_screen("StatsLana")
        renpy.hide_screen("StatsLola")
        renpy.hide_screen("StatsLisa")
        renpy.hide_screen("StatsRonnie")
        renpy.hide_screen("StatsCarol")
        renpy.hide_screen("LoriAffectionBar")
        renpy.hide_screen("LeniAffectionBar")
        renpy.hide_screen("LunaAffectionBar")
        renpy.hide_screen("LuanAffectionBar")
        renpy.hide_screen("LynnAffectionBar")
        renpy.hide_screen("LucyAffectionBar")
        renpy.hide_screen("LanaAffectionBar")
        renpy.hide_screen("LolaAffectionBar")
        renpy.hide_screen("LisaAffectionBar")
        renpy.hide_screen("RonnieAffectionBar")
        renpy.hide_screen("CarolAffectionBar")

    #################Defining and adding items in the trunk#################:
    helmet = Item("Football Helmet.", image="images/Smartphone/Inventory/inv_FBHelmet.png")
    sunglasses = Item("SunGlasses", image="images/Smartphone/Inventory/inv_SunGlasses.png")
    walkietalkie = Item("WalkieTalkie", image="images/Smartphone/Inventory/inv_walkietalkie.png")
    baseball = Item("Baseball", image="images/Smartphone/Inventory/inv_baseball.png")
    bat = Item("Bat", image="images/Smartphone/Inventory/inv_bat.png")
    camera = Item("Camera", image="images/Smartphone/Inventory/inv_camera.png")
    comix = Item("Comix", image="images/Smartphone/Inventory/inv_comix.png")
    flowers = Item("Flowers", image="images/Smartphone/Inventory/inv_flowers.png")
    football2 = Item("Football", image="images/Smartphone/Inventory/inv_football2.png")
    golfclub = Item("Golf Club", image="images/Smartphone/Inventory/inv_golfclub.png")
    gum = Item("Gum", image="images/Smartphone/Inventory/inv_gum.png")
    plunger = Item("Plunger", image="images/Smartphone/Inventory/inv_plunger.png")
    potion = Item("Potion", image="images/Smartphone/Inventory/inv_potion.png")
    soccerball = Item("soccerball", image="images/Smartphone/Inventory/inv_soccerball.png")
    ticket = Item("Ticket", image="images/Smartphone/Inventory/inv_ticket.png")
    videocamera = Item("Video Camera", image="images/Smartphone/Inventory/inv_videocamera.png")
    VR = Item("VR Goggles", image="images/Smartphone/Inventory/inv_VR.png")
    drumsticks = Item("Drumsticks", image="images/Smartphone/Inventory/inv_drumsticks.png")
    hockeystick = Item("Hockey Stick", image="images/Smartphone/Inventory/inv_hockeystick.png")
    horn = Item("Horn", image="images/Smartphone/Inventory/inv_horn.png")
    microphone = Item("Microphone", image="images/Smartphone/Inventory/inv_microphone.png")
    money = Item("Money", image="images/Smartphone/Inventory/inv_money.png")
    purse = Item("Purse", image="images/Smartphone/Inventory/inv_purse.png")
    weight = Item("Weight", image="images/Smartphone/Inventory/inv_weight.png")
    basketball = Item("Basketball", image="images/Smartphone/Inventory/inv_basketball.png")
    beachball = Item("Beachball", image="images/Smartphone/Inventory/inv_beachball.png")
    creampie = Item("Creampie", image="images/Smartphone/Inventory/inv_creampie.png")
    inventory = Inventory()
    inventory.add(helmet)
    inventory.add(comix)
    inventory.add(money)
    inventory.add(sunglasses)
    inventory.add(walkietalkie)
    inventory.add(baseball)
    inventory.add(bat)
    inventory.add(camera)
    inventory.add(flowers)
    inventory.add(football2)
    inventory.add(golfclub)
    inventory.add(gum)
    inventory.add(plunger)
    inventory.add(potion)
    inventory.add(soccerball)
    inventory.add(ticket)
    inventory.add(videocamera)
    inventory.add(VR)
    inventory.add(drumsticks)
    inventory.add(hockeystick)
    inventory.add(horn)
    inventory.add(money)
    inventory.add(purse)
    inventory.add(weight)
    inventory.add(basketball)
    inventory.add(beachball)
    inventory.add(creampie)
    ## Oofs
