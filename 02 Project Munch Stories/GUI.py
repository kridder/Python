import pygame as GUI
import random
import ECard
import ECardInit
import EDeck
import EAbbilities
import ICard
import ICardInit
import IDeck
import EBonusCalc

run = True
GO = 0
Turn = [0]
Fight = -2
AP = 1
Debug = 0
SDebug = 0
Wait = 0

P1Level = 0
P2Level = 0

PELevel = 0

D6 = 6
PR = 0
P1R = 0
P2R = 0
FR = 0

SC = [1, 2, 1]
HSC = 0

Swap = ICard.ICard()
Swap.Name = 'Swap'
SWP = 0

Shroud = ECard.ECard()
Shroud.ID = 1
Shroud.Name = 'Shroud'
Shroud.Type = ''
Shroud.Size = ''
#Shroud.Level = ''
Shroud.Abbility = ''
Shroud.Text1 = ''
Shroud.Text2 = ''
Shroud.Text3 = ''
Shroud.Text4 = ''
Shroud.Text5 = ''
Shroud.Text6 = ''
Shrouded = [0]

Skipd = 0

MaxP1A = 0
MaxP2A = 0
MaxP1B = 0
MaxP2B = 0
MaxPC = 0


# Initialize Cards
E = ECardInit.Init()
I = ICardInit.Init()


# Initialze Enemy Abbilities
EA = EAbbilities.Init(E)
AEA = []
for (ea, line) in enumerate(EA):
    AEA.append(0)


# Make 21 Empty Enemy Card Templates
EC = [E[0]]
EBonus = [0]
cards = 0
while True:
	if cards < 21:
		EC.append (E[0])
		EBonus.append (0)
		cards += 1
	else:
		break


# Make Empty Player Card Templates
P1A = [I[0]]
P2A = [I[0]]
P1B = [I[0]]
P2B = [I[0]]
P1C = [I[0]]
P2C = [I[0]]

	    
# Construct Enemy Deck
ED = EDeck.Create(E)


# Construct Item Deck
ID = IDeck.Create(I)

        
# Initialize GUI
GUI.init()
font = GUI.font.Font(None, 14)
Mfont = GUI.font.Font(None, 31)
Nfont = GUI.font.Font(None, 50)
GTitle = font.render('Project Munch Stories 0.00.16', True, (0, 0, 0))
EvSc = font.render('Event Screen', True, (0, 0, 255))

resolution = (1200,800)
screen = GUI.display.set_mode( resolution )


# Run Game
while run:

    GUI.event.pump()
    keys = GUI.key.get_pressed()


    # Main Screen
    screen.fill((255,255,255))
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 5), (1190, 790)), 1)
    
    if Fight == -2:
        MMessage = Nfont.render('Press Space to Start', True, (0, 0, 0))
        screen.blit(MMessage, (400 , 180))


    # Event Screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 5), (155, 390)), 1)
    screen.blit(EvSc, (9, 9))


    # Check Enemy Abbilities
    #AEA = EAbbilities.Read(EC, EA, AEA)  


    # Enemy Screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 5), (1190, 390)), 1)
    for (ec, line) in enumerate(EC):
        if EC[ec].ID > 0:
            EBonus[ec] = EBonusCalc.Calc(EC, ec, P1A, P2A, AEA)
            
            # Cards 1 - 14
            if ec < 15:
                GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((49 + 120*(ec-7*(ec/8)), 15 + 125*(ec/8)), (110, 120)), 1)
                Name = font.render(EC[ec].Name, True, (0, 0, 0))
                Type = font.render(EC[ec].Type, True, (0, 0, 0))
                Size = font.render(EC[ec].Size, True, (0, 0, 0))
                if EBonus[ec]:
                    Level = font.render(str(EC[ec].Level)+' + '+str(EBonus[ec]), True, (255, 0, 0))
                else:
                    Level = font.render(str(EC[ec].Level), True, (255, 0, 0))
                Abbility = font.render(EC[ec].Abbility, True, (0, 0, 0))
                Text1 = font.render(EC[ec].Text1, True, (70, 70, 70))
                Text2 = font.render(EC[ec].Text2, True, (70, 70, 70))
                Text3 = font.render(EC[ec].Text3, True, (70, 70, 70))
                Text4 = font.render(EC[ec].Text4, True, (70, 70, 70))
                Text5 = font.render(EC[ec].Text5, True, (70, 70, 70))
                Text6 = font.render(EC[ec].Text6, True, (70, 70, 70))
                screen.blit(Name, (54 + 120*(ec-7*(ec/8)), 17 + 125*(ec/8)))
                screen.blit(Type, (54 + 120*(ec-7*(ec/8)), 27 + 125*(ec/8)))
                screen.blit(Size, (54 + 120*(ec-7*(ec/8)), 37 + 125*(ec/8)))
                if not EC[ec].Name == 'Shroud':
                    screen.blit(Level, (54 + 120*(ec-7*(ec/8)), 47 + 125*(ec/8)))
                screen.blit(Abbility, (54 + 120*(ec-7*(ec/8)), 57 + 125*(ec/8)))
                screen.blit(Text1, (54 + 120*(ec-7*(ec/8)), 67 + 125*(ec/8)))
                screen.blit(Text2, (54 + 120*(ec-7*(ec/8)), 77 + 125*(ec/8)))
                screen.blit(Text3, (54 + 120*(ec-7*(ec/8)), 87 + 125*(ec/8)))
                screen.blit(Text4, (54 + 120*(ec-7*(ec/8)), 97 + 125*(ec/8)))
                screen.blit(Text5, (54 + 120*(ec-7*(ec/8)), 107 + 125*(ec/8)))
                screen.blit(Text6, (54 + 120*(ec-7*(ec/8)), 117 + 125*(ec/8)))

            # Cards 15 - 21
            else:
                GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((49 + 120*(ec-14), 265), (110, 120)), 1)
                Name = font.render(EC[ec].Name, True, (0, 0, 0))
                Type = font.render(EC[ec].Type, True, (0, 0, 0))
                Size = font.render(EC[ec].Size, True, (0, 0, 0))
                if EBonus[ec]:
                    Level = font.render(str(EC[ec].Level)+' + '+str(EBonus[ec]), True, (255, 0, 0))
                else:
                    Level = font.render(str(EC[ec].Level), True, (255, 0, 0))
                Abbility = font.render(EC[ec].Abbility, True, (0, 0, 0))
                Text1 = font.render(EC[ec].Text1, True, (70, 70, 70))
                Text2 = font.render(EC[ec].Text2, True, (70, 70, 70))
                Text3 = font.render(EC[ec].Text3, True, (70, 70, 70))
                Text4 = font.render(EC[ec].Text4, True, (70, 70, 70))
                Text5 = font.render(EC[ec].Text5, True, (70, 70, 70))
                Text6 = font.render(EC[ec].Text6, True, (70, 70, 70))
                screen.blit(Name, (54 + 120*(ec-14), 267))
                screen.blit(Type, (54 + 120*(ec-14), 277))
                screen.blit(Size, (54 + 120*(ec-14), 287))
                if not EC[ec].Name == 'Shroud':
                    screen.blit(Level, (54 + 120*(ec-14), 297))
                screen.blit(Abbility, (54 + 120*(ec-14), 307))
                screen.blit(Text1, (54 + 120*(ec-14), 317))
                screen.blit(Text2, (54 + 120*(ec-14), 327))
                screen.blit(Text3, (54 + 120*(ec-14), 337))
                screen.blit(Text4, (54 + 120*(ec-14), 347))
                screen.blit(Text5, (54 + 120*(ec-14), 357))
                screen.blit(Text6, (54 + 120*(ec-14), 367))

        else:
            EBonus[ec] = 0


    # Enemy Info Screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1040, 5), (155, 390)), 1)
    
        # Count Enemy Level
    CELevel = font.render('Combined Enemy Level', True, (255, 0, 0))
    screen.blit(CELevel, (1065, 29))
    
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1096, 44), (52, 52)), 1)
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1097, 45), (50, 50)), 1)
    ELevel = 0
    for (ec, line) in enumerate(EC):
        ELevel += EC[ec].Level
        ELevel += EBonus[ec]
    if ELevel > 0:
        DELevel = Nfont.render(str(ELevel), True, (255, 0, 0))
        if ELevel < 10:
            screen.blit(DELevel, (1113, 55))
        else:
            screen.blit(DELevel, (1102, 55))

        # Count cards in Enemy Deck
    count = 0
    for (ed, line) in enumerate(ED):
        if ED[ed].ID > 0:
            count += 1

    LEDeck = font.render('Cards left in enemy deck: '+str(count), True, (0, 0, 0))
    screen.blit(LEDeck, (1045, 10))

        # Display Enemy Abbilities        
    for (ea, line) in enumerate(EA):
        if EA[ea] == AEA[ea]:
            EAColour = [255, 0, 0]
        elif ea > 0:
            EAColour = [200, 200, 200]
        else:
            EAColour = [0, 0, 0]

        if ea == 0:
            DEAbbilities = font.render(EA[ea], True, (EAColour))
        else:
            DEAbbilities = font.render('- '+EA[ea], True, (EAColour))
        screen.blit(DEAbbilities, (1045, 115 + 10*ea))


    # Menu
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 405), (155, 390)), 1)

        # Fight Button
    if Fight == 1:
        FColour = [0, 0, 0]
    else:
        FColour = [200, 200, 200]
    FButton = Nfont.render('FIGHT', True, (FColour))
    screen.blit(FButton, (30, 430))

    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((24, 424), (116, 43)), 2)

        # Descend Button
    if Fight == 0:
        DColour = [0, 0, 0]
    else:
        DColour = [200, 200, 200]
    DButton = Mfont.render('DESCEND', True, (DColour))
    screen.blit(DButton, (30, 500))

    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((24, 489), (116, 43)), 2)

        # Wait Button
    #if Fight == 1 and not Wait:
        #WColour = [0, 0, 0]
    #else:
        #WColour = [200, 200, 200]
    #WButton = Nfont.render('WAIT', True, (WColour))
    #screen.blit(WButton, (35, 560))

    #GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((24, 554), (116, 43)), 2)

        # Debug Display
    if Debug:
        DDebug = font.render('DEBUG', True, (0, 0, 0))
        screen.blit(DDebug, (15, 608))

        DPELevel = font.render('PELevel', True, (0, 0, 0))
        screen.blit(DPELevel, (15, 623))
        DPELevel = font.render(str(PELevel), True, (0, 0, 0))
        screen.blit(DPELevel, (15, 633))

        DSDebug = font.render('Shroud Reveal', True, (0, 0, 0))
        screen.blit(DSDebug, (15, 648))
        DSDebug = font.render(str(SDebug), True, (0, 0, 0))
        screen.blit(DSDebug, (15, 658))

        for (shrouded, line) in enumerate(Shrouded):
            if shrouded < 1:
                DShrouded = font.render('Shrouded:', True, (0, 0, 0))
            else:
                DShrouded = font.render(Shrouded[shrouded].Name, True, (0, 0, 0))
            screen.blit(DShrouded, (15, 673 + 10*shrouded))


    # Player Screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 405), (1190, 390)), 1)
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((159, 405), (442, 131)), 1)
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((600, 535), (441, 131)), 1)
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((159, 665), (882, 130)), 1)

        # Player 1 Active Cards
    if AP == 1:
        P1Colour = [0, 0, 175]
    else:
        P1Colour = [0, 0, 0]
    DP1 = font.render('PLAYER 1', True, (P1Colour))
    DP1Level = font.render('Level: '+str(P1Level), True, (0, 0, 0))
    screen.blit(DP1, (174, 412))
    screen.blit(DP1Level, (174, 422))

    P1CheckPen = []

    for (p1a, line) in enumerate(P1A):
        P1CheckPen.append(0)
        
        if SC[0] == 1 and SC[1] == 0 and SC[2]== p1a:
            if FR:
                Selected = [255, 0, 0]
            else:
                Selected = [0, 0, 175]
                Thickness = 2
        else:
            Selected = [0, 0, 0]
            Thickness = 1
            
        if P1A[p1a].ID > 0:
            P1CheckPen[p1a] = EBonusCalc.CheckPen(AEA, P1A, p1a)
            
            if p1a < 4:
                GUI.draw.rect(screen, (Selected), GUI.Rect((169 + 120*p1a, 410), (110, 120)), Thickness)
                Name = font.render(P1A[p1a].Name, True, (0, 0, 0))
                Range = font.render(P1A[p1a].Range, True, (0, 0, 0))
                Type = font.render(P1A[p1a].Type, True, (0, 0, 0))
                Size = font.render(P1A[p1a].Size, True, (0, 0, 0))
                Bonus = font.render(str(P1A[p1a].Bonus), True, (0, 125, 0))
                CheckType = font.render(P1A[p1a].CheckType, True, (0, 0, 0))
                if P1CheckPen[p1a]:
                    Penalty = [255, 0 , 0]
                else:
                    Penalty = [0, 0, 0]
                if P1A[p1a].CheckVal + P1CheckPen[p1a] < 6:
                    CheckVal = font.render(str(P1A[p1a].CheckVal + P1CheckPen[p1a])+'+', True, (Penalty))
                else:
                    CheckVal = font.render(str(P1A[p1a].CheckVal + P1CheckPen[p1a]), True, (Penalty))
                Text1 = font.render(P1A[p1a].Text1, True, (70, 70, 70))
                Text2 = font.render(P1A[p1a].Text2, True, (70, 70, 70))
                Text3 = font.render(P1A[p1a].Text3, True, (70, 70, 70))
                Text4 = font.render(P1A[p1a].Text4, True, (70, 70, 70))
                screen.blit(Name, (174 + 120*p1a, 412))
                screen.blit(Range, (174 + 120*p1a, 422))
                screen.blit(Type, (174 + 120*p1a, 432))
                screen.blit(Size, (174 + 120*p1a, 442))
                screen.blit(Bonus, (174 + 120*p1a, 452))
                screen.blit(CheckType, (174 + 120*p1a, 462))
                screen.blit(CheckVal, (174 + 120*p1a, 472))
                screen.blit(Text1, (174 + 120*p1a, 482))
                screen.blit(Text2, (174 + 120*p1a, 492))
                screen.blit(Text3, (174 + 120*p1a, 502))
                screen.blit(Text4, (174 + 120*p1a, 512))
        elif P1A[p1a].Name == 'Swap':
            if p1a < 4:
                if not Selected[2]:
                    Selected = [255, 0, 0]
                GUI.draw.rect(screen, (Selected), GUI.Rect((169 + 120*p1a, 410), (110, 120)), Thickness)

        # Player 2 Active Cards
    if AP == 2:
        P2Colour = [0, 0, 175]
    else:
        P2Colour = [0, 0, 0]
    DP1 = font.render('PLAYER 2', True, (P2Colour))
    DP1Level = font.render('Level: '+str(P2Level), True, (0, 0, 0))
    screen.blit(DP1, (615, 412))
    screen.blit(DP1Level, (615, 422))

    P2CheckPen = []

    for (p2a, line) in enumerate(P2A):
        P2CheckPen.append(0)
        
        if SC[0] == 2 and SC[1] == 0 and SC[2]== p2a:
            if FR:
                Selected = [255, 0, 0]
            else:
                Selected = [0, 0, 175]
                Thickness = 2
        else:
            Selected = [0, 0, 0]
            Thickness = 1
            
        if P2A[p2a].ID > 0:
            P2CheckPen[p2a] = EBonusCalc.CheckPen(AEA, P2A, p2a)
            
            if p2a < 4:
                GUI.draw.rect(screen, (Selected), GUI.Rect((610 + 120*p2a, 410), (110, 120)), Thickness)
                Name = font.render(P2A[p2a].Name, True, (0, 0, 0))
                Range = font.render(P2A[p2a].Range, True, (0, 0, 0))
                Type = font.render(P2A[p2a].Type, True, (0, 0, 0))
                Size = font.render(P2A[p2a].Size, True, (0, 0, 0))
                Bonus = font.render(str(P2A[p2a].Bonus), True, (0, 125, 0))
                CheckType = font.render(P2A[p2a].CheckType, True, (0, 0, 0))
                if P2CheckPen[p2a]:
                    Penalty = [255, 0 , 0]
                else:
                    Penalty = [0, 0, 0]
                if P2A[p2a].CheckVal + P2CheckPen[p2a] < 6:
                    CheckVal = font.render(str(P2A[p2a].CheckVal + P2CheckPen[p2a])+'+', True, (Penalty))
                else:
                    CheckVal = font.render(str(P2A[p2a].CheckVal + P2CheckPen[p2a]), True, (Penalty))
                Text1 = font.render(P2A[p2a].Text1, True, (70, 70, 70))
                Text2 = font.render(P2A[p2a].Text2, True, (70, 70, 70))
                Text3 = font.render(P2A[p2a].Text3, True, (70, 70, 70))
                Text4 = font.render(P2A[p2a].Text4, True, (70, 70, 70))
                screen.blit(Name, (615 + 120*p2a, 412))
                screen.blit(Range, (615 + 120*p2a, 422))
                screen.blit(Type, (615 + 120*p2a, 432))
                screen.blit(Size, (615 + 120*p2a, 442))
                screen.blit(Bonus, (615 + 120*p2a, 452))
                screen.blit(CheckType, (615 + 120*p2a, 462))
                screen.blit(CheckVal, (615 + 120*p2a, 472))
                screen.blit(Text1, (615 + 120*p2a, 482))
                screen.blit(Text2, (615 + 120*p2a, 492))
                screen.blit(Text3, (615 + 120*p2a, 502))
                screen.blit(Text4, (615 + 120*p2a, 512))
        elif P2A[p2a].Name == 'Swap':
            if p2a < 4:
                if not Selected[2]:
                    Selected = [255, 0, 0]
                GUI.draw.rect(screen, (Selected), GUI.Rect((610 + 120*p2a, 410), (110, 120)), Thickness)

        # Player 1 Belt
    for (p1b, line) in enumerate(P1B):
        
        if SC[0] == 1 and SC[1] == 1 and SC[2]== p1b:
            Selected = [0, 0, 175]
            Thickness = 2
        else:
            Selected = [0, 0, 0]
            Thickness = 1
            
        if P1B[p1b].ID > 0:
            if p1b < 5:
                GUI.draw.rect(screen, (Selected), GUI.Rect((49 + 120*p1b, 540), (110, 120)), Thickness)
                Name = font.render(P1B[p1b].Name, True, (0, 0, 0))
                Range = font.render(P1B[p1b].Range, True, (0, 0, 0))
                Type = font.render(P1B[p1b].Type, True, (0, 0, 0))
                Size = font.render(P1B[p1b].Size, True, (0, 0, 0))
                Bonus = font.render(str(P1B[p1b].Bonus), True, (0, 125, 0))
                CheckType = font.render(P1B[p1b].CheckType, True, (0, 0, 0))
                if P1B[p1b].CheckVal < 6:
                    CheckVal = font.render(str(P1B[p1b].CheckVal)+'+', True, (0, 0, 0))
                else:
                    CheckVal = font.render(str(P1B[p1b].CheckVal), True, (0, 0, 0))
                Text1 = font.render(P1B[p1b].Text1, True, (70, 70, 70))
                Text2 = font.render(P1B[p1b].Text2, True, (70, 70, 70))
                Text3 = font.render(P1B[p1b].Text3, True, (70, 70, 70))
                Text4 = font.render(P1B[p1b].Text4, True, (70, 70, 70))
                screen.blit(Name, (54 + 120*p1b, 542))
                screen.blit(Range, (54 + 120*p1b, 552))
                screen.blit(Type, (54 + 120*p1b, 562))
                screen.blit(Size, (54 + 120*p1b, 572))
                screen.blit(Bonus, (54 + 120*p1b, 582))
                screen.blit(CheckType, (54 + 120*p1b, 592))
                screen.blit(CheckVal, (54 + 120*p1b, 602))
                screen.blit(Text1, (54 + 120*p1b, 612))
                screen.blit(Text2, (54 + 120*p1b, 622))
                screen.blit(Text3, (54 + 120*p1b, 632))
                screen.blit(Text4, (54 + 120*p1b, 642))
        elif P1B[p1b].Name == 'Swap':
            if p1b < 5:
                if not Selected[2]:
                    Selected = [255, 0, 0]
                GUI.draw.rect(screen, (Selected), GUI.Rect((49 + 120*p1b, 540), (110, 120)), Thickness)

            # Player 2 Belt
    for (p2b, line) in enumerate(P2B):
        
        if SC[0] == 2 and SC[1] == 1 and SC[2]== p2b:
            Selected = [0, 0, 175]
            Thickness = 2
        else:
            Selected = [0, 0, 0]
            Thickness = 1
            
        if P2B[p2b].ID > 0:
            if p2b < 5:
                GUI.draw.rect(screen, (Selected), GUI.Rect((490 + 120*p2b, 540), (110, 120)), Thickness)
                Name = font.render(P2B[p2b].Name, True, (0, 0, 0))
                Range = font.render(P2B[p2b].Range, True, (0, 0, 0))
                Type = font.render(P2B[p2b].Type, True, (0, 0, 0))
                Size = font.render(P2B[p2b].Size, True, (0, 0, 0))
                Bonus = font.render(str(P2B[p2b].Bonus), True, (0, 125, 0))
                CheckType = font.render(P2B[p2b].CheckType, True, (0, 0, 0))
                if P2B[p2b].CheckVal < 6:
                    CheckVal = font.render(str(P2B[p2b].CheckVal)+'+', True, (0, 0, 0))
                else:
                    CheckVal = font.render(str(P2B[p2b].CheckVal), True, (0, 0, 0))
                Text1 = font.render(P2B[p2b].Text1, True, (70, 70, 70))
                Text2 = font.render(P2B[p2b].Text2, True, (70, 70, 70))
                Text3 = font.render(P2B[p2b].Text3, True, (70, 70, 70))
                Text4 = font.render(P2B[p2b].Text4, True, (70, 70, 70))
                screen.blit(Name, (495 + 120*p2b, 542))
                screen.blit(Range, (495 + 120*p2b, 552))
                screen.blit(Type, (495 + 120*p2b, 562))
                screen.blit(Size, (495 + 120*p2b, 572))
                screen.blit(Bonus, (495 + 120*p2b, 582))
                screen.blit(CheckType, (495 + 120*p2b, 592))
                screen.blit(CheckVal, (495 + 120*p2b, 602))
                screen.blit(Text1, (495 + 120*p2b, 612))
                screen.blit(Text2, (495 + 120*p2b, 622))
                screen.blit(Text3, (495 + 120*p2b, 632))
                screen.blit(Text4, (495 + 120*p2b, 642))
        elif P2B[p2b].Name == 'Swap':
            if p2b < 5:
                if not Selected[2]:
                    Selected = [255, 0, 0]
                GUI.draw.rect(screen, (Selected), GUI.Rect((490 + 120*p2b, 540), (110, 120)), Thickness)
    
        # Active Player Hand / Cards
    if AP == 1:
        PC = P1C
    else:
        PC = P2C
    for (pc, line) in enumerate(PC):
        
        if SC[0] == AP and SC[1] == 2 and SC[2]== pc:
            Selected = [0, 0, 175]
            Thickness = 2
        else:
            Selected = [0, 0, 0]
            Thickness = 1
            
        if PC[pc].ID > 0:
            if pc < 10:
                GUI.draw.rect(screen, (Selected), GUI.Rect((49 + 120*pc, 670), (110, 120)), Thickness)
                Name = font.render(PC[pc].Name, True, (0, 0, 0))
                Range = font.render(PC[pc].Range, True, (0, 0, 0))
                Type = font.render(PC[pc].Type, True, (0, 0, 0))
                Size = font.render(PC[pc].Size, True, (0, 0, 0))
                Bonus = font.render(str(PC[pc].Bonus), True, (0, 125, 0))
                CheckType = font.render(PC[pc].CheckType, True, (0, 0, 0))
                if PC[pc].CheckVal < 6:
                    CheckVal = font.render(str(PC[pc].CheckVal)+'+', True, (0, 0, 0))
                else:
                    CheckVal = font.render(str(PC[pc].CheckVal), True, (0, 0, 0))
                Text1 = font.render(PC[pc].Text1, True, (70, 70, 70))
                Text2 = font.render(PC[pc].Text2, True, (70, 70, 70))
                Text3 = font.render(PC[pc].Text3, True, (70, 70, 70))
                Text4 = font.render(PC[pc].Text4, True, (70, 70, 70))
                screen.blit(Name, (54 + 120*pc, 672))
                screen.blit(Range, (54 + 120*pc, 682))
                screen.blit(Type, (54 + 120*pc, 692))
                screen.blit(Size, (54 + 120*pc, 702))
                screen.blit(Bonus, (54 + 120*pc, 712))
                screen.blit(CheckType, (54 + 120*pc, 722))
                screen.blit(CheckVal, (54 + 120*pc, 732))
                screen.blit(Text1, (54 + 120*pc, 742))
                screen.blit(Text2, (54 + 120*pc, 752))
                screen.blit(Text3, (54 + 120*pc, 762))
                screen.blit(Text4, (54 + 120*pc, 772))
        elif PC[pc].Name == 'Swap':
            if pc < 10:
                if not Selected[2]:
                    Selected = [255, 0, 0]
                GUI.draw.rect(screen, (Selected), GUI.Rect((49 + 120*pc, 670), (110, 120)), Thickness)
            

    # Player Info Screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1040, 405), (155, 390)), 1)

        # Count Turns
    #for (turn, line) in enumerate(Turn):
            #Karel = 12
    turn = len(Turn) - 1
    DTurn = font.render('Turn: '+str(turn), True, (0, 0, 0))
    screen.blit(DTurn, (1045, 410))

    # Count cards in Item Deck
    #count = 0
    #for (id, line) in enumerate(ID):
        #if ID[id].ID > 0:
            #count += 1

    #LIDeck = font.render('Cards left in item deck: '+str(count), True, (0, 0, 0))
    #screen.blit(LIDeck, (1045, 420))

        # Count Player Level
    CPLevel = font.render('Combined Player Level', True, (0, 0, 0))
    screen.blit(CPLevel, (1065, 429))
    
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1096, 444), (52, 52)), 1)
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1097, 445), (50, 50)), 1)
    PLevel = P1Level + P2Level
    for (p1a, line) in enumerate(P1A):
        PLevel += P1A[p1a].Bonus
    for (p2a, line) in enumerate(P2A):
        PLevel += P2A[p2a].Bonus
    DPLevel = Nfont.render(str(PLevel), True, (0, 0, 0))
    if PLevel < 10:
        screen.blit(DPLevel, (1113, 455))
    else:
        screen.blit(DPLevel, (1102, 455))

        # Dice
    CPLevel = font.render('Dice:', True, (0, 0, 0))
    screen.blit(CPLevel, (1065, 520))
    
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1096, 535), (51, 51)), 2)

    DD6 = Nfont.render(str(D6), True, (0, 0, 0))
    screen.blit(DD6, (1113, 545))

        # Roll Button
    if Fight == -1:
        RColour = [0, 0, 0]
    else:
        RColour = [200, 200, 200]
    RButton = Nfont.render('ROLL', True, (RColour))
    screen.blit(RButton, (1070, 614))
    
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((1059, 608), (116, 43)), 2)

        # Blit Title
    screen.blit(GTitle, (1045, 782))


    # Blit Overlay Messages
    if MaxP1A > 0: 
        screen.blit(MaxP1A, (250, 441))
    if MaxP2A > 0: 
        screen.blit(MaxP2A, (691, 441))
    if MaxP1B > 0: 
        screen.blit(MaxP1B, (250, 572))
    if MaxP2B > 0: 
        screen.blit(MaxP2B, (691, 572))
    if MaxPC > 0: 
        screen.blit(MaxPC, (500, 702))

    if GO:
        GOM = Nfont.render('GAME OVER', True, (255, 0, 0))
        screen.blit(GOM, (490 , 180))

    if Fight == -1:
        RM = Mfont.render('Enemies defeated, make rolls.', True, (255, 0, 0))
        screen.blit(RM, (445 , 310))

    
    # Draw Screen
    GUI.display.flip()


    # Descend
    if keys[GUI.K_d] and Fight == 0 and not HSC or Skipd == 1 and Fight == 0 and not HSC:
        while keys[GUI.K_d]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        # Check Item Cards in Hand
        p1c = len(P1C) - 1
        p2c = len(P2C) - 1
        if p1c > 5 or p2c > 5:
            Fight = 0
            MaxPC = Nfont.render('Max 5 Cards', True, (255, 0, 0))
        else:
            Fight = 1
            MaxPC = 0

        # Draw New Enemy Cards
        turn = len(Turn) - 1

        if turn < 21 and Fight == 1:
            Turn.append (turn + 1)

            for (turn, line) in enumerate(Turn):
                if turn > 0:
                    if turn == 1:
                        pick = turn
                        ed = len(ED) - 1
                
                    while True:
                        if pick > ed:
                            pick = 1
                            # Construct New Enemy Deck
                            ED = EDeck.Create(E)
                        elif ED[pick].ID == 0:
                            pick += 1
                        else:
                            break
                    EC[turn] = ED[pick]
                    ED[pick] = E[0]

            # Check Enemy Abbilities
            for (ec, line) in enumerate(EC):
                if EC[ec].ID > 0 and EC[ec-1].Abbility == 'Shroud':
                    Shrouded.append(EC[ec])
                    EC[ec] = Shroud
            
            AEA = EAbbilities.Read(EC, EA, AEA)  

        else:
            Fight = 0

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0

                    
    # Fight
    if keys[GUI.K_f] and Fight == 1 and not HSC and not GO:
        while keys[GUI.K_f]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        # Reveal Shrouded Cards
        shrouded = len(Shrouded) - 1
        if shrouded:
            for (ec, line) in enumerate(EC):
                if EC[ec].Name == 'Shroud':
                    EC[ec] = Shrouded.pop(1)

            # Recalculate Enemy Level
            AEA = EAbbilities.Read(EC, EA, AEA)
            ELevel = 0
            for (ec, line) in enumerate(EC):
                EBonus[ec] = EBonusCalc.Calc(EC, ec, P1A, P2A, AEA)
                ELevel += EC[ec].Level
                ELevel += EBonus[ec]
            PELevel = ELevel

        # Calculate Win
        if PLevel > ELevel:

            Fight = -1

            # Check if Rolls are Required
            p1a = len(P1A) - 1
            p2a = len(P2A) - 1
            
            P1R = p1a
            P2R = p2a

        else:
            GO = 1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0


    # Roll Dice
    if keys[GUI.K_r] and not HSC and not GO and not FR:
        while keys[GUI.K_r]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        D6 = random.randint(1, 6)

        if Fight == -1:

            if SC[0] == 1:
                if SC[1] == 0:
                    PC = P1A
                    PCheckPen = P1CheckPen
                elif SC[1] == 1:
                    PC = P1B
                else:
                    PC = P1C
                
            else:
                if SC[1] == 0:
                    PC = P2A
                    PCheckPen = P2CheckPen
                elif SC[1] == 1:
                    PC = P2B
                else:
                    PC = P2C

            pc = len(PC) - 1
            if not SC[2] > pc:
                if D6 < PC[SC[2]].CheckVal + PCheckPen[SC[2]]:
                    #PC[SC[2]].Frequency += 1
                    #PC.pop(SC[2])
                    FR = 1
                else:
                    if AP == 1:
                        P1R -= 1
                    else:
                        P2R -= 1

    # Debug Fight
    if keys[GUI.K_HOME] and Fight == 1 and not HSC and not GO and Debug:
        while keys[GUI.K_HOME]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        # Reveal Shrouded Cards
        shrouded = len(Shrouded) - 1
        if shrouded:
            for (ec, line) in enumerate(EC):
                if EC[ec].Name == 'Shroud':
                    EC[ec] = Shrouded.pop(1)

            # Recalculate Enemy Level
            AEA = EAbbilities.Read(EC, EA, AEA)
            ELevel = 0
            for (ec, line) in enumerate(EC):
                EBonus[ec] = EBonusCalc.Calc(EC, ec, P1A, P2A, AEA)
                ELevel += EC[ec].Level
                ELevel += EBonus[ec]
            PELevel = ELevel

        Fight = -1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0


    # Debug
    if keys[GUI.K_BACKQUOTE] and not HSC:
        while keys[GUI.K_BACKQUOTE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        Debug = (Debug + 1) % 2

    # Shroud Debug
    if keys[GUI.K_s] and Debug and not HSC:
        while keys[GUI.K_s]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        SDebug = (SDebug + 1) % 2

    # Unshroud Cards
    if Debug and SDebug:
        # Reveal Shrouded Cards
        shrouded = len(Shrouded) - 1
        if shrouded:
            for (ec, line) in enumerate(EC):
                if EC[ec].Name == 'Shroud':
                    EC[ec] = Shrouded.pop(1)

            # Recalculate Enemy Level
            AEA = EAbbilities.Read(EC, EA, AEA)
            ELevel = 0
            for (ec, line) in enumerate(EC):
                EBonus[ec] = EBonusCalc.Calc(EC, ec, P1A, P2A, AEA)
                ELevel += EC[ec].Level
                ELevel += EBonus[ec]
            PELevel = ELevel
    elif Fight == 1 and not GO:
        # Reshroud Cards
        for (ec, line) in enumerate(EC):
            if EC[ec].ID > 0 and not EC[ec].Name == 'Shroud' and EC[ec-1].Abbility == 'Shroud':
                Shrouded.append(EC[ec])
                EC[ec] = Shroud

            # Remove Active Enemy Abbilities
        AEA = []
        for (ea, line) in enumerate(EA):
            AEA.append(0)

        AEA = EAbbilities.Read(EC, EA, AEA)


    # Wait
    if keys[GUI.K_w] and not HSC:
        while keys[GUI.K_w]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        Wait = (Wait + 1) % 2


    # Skip d
    if keys[GUI.K_RETURN] and not HSC and Debug:
        while keys[GUI.K_RETURN]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        Skipd = 1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0


    # Change Active Player
    if keys[GUI.K_c] and not HSC and not FR:
        while keys[GUI.K_c]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if AP == 1:
            AP = 2
            SC = [2, 2, 1]
        else:
            AP = 1
            SC = [1, 2, 1]

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0


    # Start
    if keys[GUI.K_SPACE] and Fight == -2:
        while keys[GUI.K_SPACE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        Fight = 0

        # Players Draw 3 Items
        Card = 1
        PC = P1C
        while Card < 4:
            if Card == 1:
                pick = Card
                id = len(ID) - 1
                    
            while True:
                if pick > id:
                    pick = 1
                    # Construct New Item Deck
                    ID = IDeck.Create(I)
                elif ID[pick].ID == 0:
                    pick += 1
                else:
                    break
            PC.append(ID[pick])
            ID[pick] = I[0]

            Card += 1

            if Card == 4 and PC == P1C:
                Card = 1
                PC = P2C


    # Select Card
        # Up
    if keys[GUI.K_UP]:
        while keys[GUI.K_UP]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        SC[1] -= 1
        if SC[1] < 0:
            SC[1] = 0

        timer = 0
        while timer < 2:
            if SC[0] == 1:
                if SC[1] == 0:
                    PC = P1A
                elif SC[1] == 1:
                    PC = P1B
                else:
                    PC = P1C
            else:
                if SC[1] == 0:
                    PC = P2A
                elif SC[1] == 1:
                    PC = P2B
                else:
                    PC = P2C

            pc = len(PC) - 1
            if pc < 1:
                SC[1] -= 1
            else:
                break

            if SC[1] < 0:
                SC[1] = 0

            timer += 1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0

        # Down
    if keys[GUI.K_DOWN]:
        while keys[GUI.K_DOWN]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        SC[1] += 1
        if SC[1] > 2:
            SC[1] = 2

        timer = 0
        while timer < 2:
            if SC[0] == 1:
                if SC[1] == 0:
                    PC = P1A
                elif SC[1] == 1:
                    PC = P1B
                else:
                    PC = P1C
            else:
                if SC[1] == 0:
                    PC = P2A
                elif SC[1] == 1:
                    PC = P2B
                else:
                    PC = P2C

            pc = len(PC) - 1
            if pc < 1:
                SC[1] += 1
            else:
                break

            if SC[1] > 2:
                SC[1] = 2

            timer += 1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0
    
        # Right
    if keys[GUI.K_RIGHT]:
        while keys[GUI.K_RIGHT]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[0] == 1 and SC[1] == 0:
            PC = P1A
        elif SC[0] == 2 and SC[1] == 0:
            PC = P2A
        elif SC[0] == 1 and SC[1] == 1:
            PC = P1B
        elif SC[0] == 2 and SC[1] == 1:
            PC = P2B
        elif SC[0] == 1 and SC[1] == 2:
            PC = P1C
        else:
            PC = P2C
            
        pc = len(PC) - 1
                
        if SC[2] < pc:
            SC[2] += 1
        else:
            SC[2] = 1

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0

        # Left
    if keys[GUI.K_LEFT]:
        while keys[GUI.K_LEFT]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[0] == 1 and SC[1] == 0:
            PC = P1A
        elif SC[0] == 2 and SC[1] == 0:
            PC = P2A
        elif SC[0] == 1 and SC[1] == 1:
            PC = P1B
        elif SC[0] == 2 and SC[1] == 1:
            PC = P2B
        elif SC[0] == 1 and SC[1] == 2:
            PC = P1C
        else:
            PC = P2C
            
        pc = len(PC) - 1
                
        if SC[2] > 1:
            SC[2] -= 1
        else:
            SC[2] = pc

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0


    # Avoid Player Hand / Cards when preparing for fight
    if Fight == 1 and SC[1] == 2:
        SC[1] =  1


    # Swap Cards
    if keys[GUI.K_INSERT] and not PR:
        while keys[GUI.K_INSERT]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[0] == 1:
            if SC[1] == 0:
                PC = P1A
            elif SC[1] == 1:
                PC = P1B
            else:
                PC = P1C
        else:
            if SC[1] == 0:
                PC = P2A
            elif SC[1] == 1:
                PC = P2B
            else:
                PC = P2C

        pc = len(PC) - 1
        if not SC[2] > pc and not HSC:
            HSC = [PC, SC[2], SC[1]]
            S1PC = PC[SC[2]]
            PC[SC[2]] = Swap

            MaxP1A = 0
            MaxP2A = 0
        elif not SC[2] > pc and HSC:
            hpc = len(HSC[0]) - 1
            if SC[1] == 0 and pc > 1 or HSC[2] == 0 and hpc > 1:
                if PC[SC[2]].Size == 'Small' and S1PC.Size == 'Small':
                    if SC[1] == 0:
                        if S1PC.Range == 'Melee' or PC[SC[2]+(SC[2] % 2)-(1 % SC[2])].Range == 'Melee' or PC[SC[2]+(SC[2] % 2)-(1 % SC[2])] == Swap:
                            SWP = 1
                    else:
                        if PC[SC[2]].Range == 'Melee' or HSC[0][HSC[1]+(HSC[1] % 2)-(1 % HSC[1])].Range == 'Melee':
                            SWP = 1
            else:
                SWP = 1

            if PC[SC[2]] == Swap and HSC or SWP:
                S2PC = PC[SC[2]]
                PC[SC[2]] = S1PC
                if not HSC[0][HSC[1]].ID:
                    HSC[0][HSC[1]] = S2PC
        
                HSC = 0
                MaxP1A = 0
                MaxP2A = 0
                SWP = 0
            else:
                if AP == 1:
                    MaxP1A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                else:
                    MaxP2A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                
               
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0


    # Move Card Up
    if keys[GUI.K_PAGEUP] and not HSC and not PR:
        while keys[GUI.K_PAGEUP]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[1] == 2:
            if SC[0] == 1:
                p1c = len(P1C) - 1
                p1b = len(P1B) - 1
                if not SC[2] > p1c and not p1b > 2:
                    P1B.append(P1C.pop(SC[2]))
                    
                if p1b > 2:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = Nfont.render('Max 3 Cards', True, (255, 0, 0))
                    MaxP2B = 0
                else:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = 0
                    
            else:
                p2c = len(P2C) - 1
                p2b = len(P2B) - 1
                if not SC[2] > p2c and not p2b > 2:
                    P2B.append(P2C.pop(SC[2]))
                    
                if p2b > 2:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = Nfont.render('Max 3 Cards', True, (255, 0, 0))
                else:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = 0

        elif SC[1] == 1:
            if SC[0] == 1:
                p1b = len(P1B) - 1
                p1a = len(P1A) - 1
                if not SC[2] > p1b and not p1a > 2:
                    if p1a < 1:
                        P1A.append(P1B.pop(SC[2]))
                        MaxP1A = 0
                        MaxP2A = 0
                        MaxP1B = 0
                        MaxP2B = 0
                    elif p1a < 2 and P1A[1].Size == 'Small' and P1B[SC[2]].Size == 'Small':
                        if not P1A[1].Range == 'Melee' and not P1B[SC[2]].Range == 'Melee':
                            MaxP1A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                            MaxP2A = 0
                            MaxP1B = 0
                            MaxP2B = 0
                        else:
                            P1A.append(P1B.pop(SC[2]))
                            MaxP1A = 0
                            MaxP2A = 0
                            MaxP1B = 0
                            MaxP2B = 0
                    elif p1a > 0:
                        MaxP1A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                        MaxP2A = 0
                        MaxP1B = 0
                        MaxP2B = 0
                    
            else:
                p2b = len(P2B) - 1
                p2a = len(P2A) - 1
                if not SC[2] > p2b and not p2a > 2:
                    if p2a < 1:
                        P2A.append(P2B.pop(SC[2]))
                        MaxP1A = 0
                        MaxP2A = 0
                        MaxP1B = 0
                        MaxP2B = 0
                    elif p2a < 2 and P2A[1].Size == 'Small' and P2B[SC[2]].Size == 'Small':
                        if not P2A[1].Range == 'Melee' and not P2B[SC[2]].Range == 'Melee':
                            MaxP1A = 0
                            MaxP2A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                            MaxP1B = 0
                            MaxP2B = 0
                        else:
                            P2A.append(P2B.pop(SC[2]))
                            MaxP1A = 0
                            MaxP2A = 0
                            MaxP1B = 0
                            MaxP2B = 0
                    elif p2a > 0:
                        MaxP1A = 0
                        MaxP2A = Nfont.render('Max 1 Card', True, (255, 0, 0))
                        MaxP1B = 0
                        MaxP2B = 0
                    
        MaxPC = 0


    # Move Card Down
    if keys[GUI.K_PAGEDOWN] and not HSC and not PR:
        while keys[GUI.K_PAGEDOWN]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[1] == 1 and not Fight == 1:
            if SC[0] == 1:
                p1b = len(P1B) - 1
                if not SC[2] > p1b:
                    P1C.append(P1B.pop(SC[2]))
                    
            else:
                p2b = len(P2B) - 1
                if not SC[2] > p2b:
                    P2C.append(P2B.pop(SC[2]))

            MaxP1A = 0
            MaxP2A = 0
            MaxP1B = 0
            MaxP2B = 0
            MaxPC = 0

        elif SC[1] == 0:
            if SC[0] == 1:
                p1a = len(P1A) - 1
                p1b = len(P1B) - 1
                if not SC[2] > p1a and not p1b > 2:
                    P1B.append(P1A.pop(SC[2]))
                    
                if p1b > 2:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = Nfont.render('Max 3 Cards', True, (255, 0, 0))
                    MaxP2B = 0
                else:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = 0
                    
            else:
                p2a = len(P2A) - 1
                p2b = len(P2B) - 1
                if not SC[2] > p2a and not p2b > 2:
                    P2B.append(P2A.pop(SC[2]))
                    
                if p2b > 2:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = Nfont.render('Max 3 Cards', True, (255, 0, 0))
                else:
                    MaxP1A = 0
                    MaxP2A = 0
                    MaxP1B = 0
                    MaxP2B = 0

        MaxPC = 0


    # Discard Cards
    if keys[GUI.K_DELETE] and not HSC:
        while keys[GUI.K_DELETE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[1] == 2:
            if SC[0] == 1:
                p1c = len(P1C) - 1
                if not SC[2] > p1c:
                    P1C[SC[2]].Frequency += 1
                    P1C.pop(SC[2])
            else:
                p2c = len(P2C) - 1
                if not SC[2] > p2c:
                    P2C[SC[2]].Frequency += 1
                    P2C.pop(SC[2])

        elif SC[1] == 1:
            if SC[0] == 1:
                p1b = len(P1B) - 1
                if not SC[2] > p1b:
                    P1B[SC[2]].Frequency += 1
                    P1B.pop(SC[2])
            else:
                p2b = len(P2B) - 1
                if not SC[2] > p2b:
                    P2B[SC[2]].Frequency += 1
                    P2B.pop(SC[2])

        elif SC[1] == 0:
            if SC[0] == 1:
                p1a = len(P1A) - 1
                if not SC[2] > p1a:
                    P1A[SC[2]].Frequency += 1
                    P1A.pop(SC[2])
            else:
                p2a = len(P2A) - 1
                if not SC[2] > p2a:
                    P2A[SC[2]].Frequency += 1
                    P2A.pop(SC[2])
                    
        if FR:
            if AP == 1:
                P1R -= 1
            else:
                P2R -= 1

        FR = 0

        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0


    # Trade Cards
    if keys[GUI.K_END] and not HSC and not PR and not Fight == 1:
        while keys[GUI.K_END]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if SC[1] == 2:
            if SC[0] == 1:
                p1c = len(P1C) - 1
                if not SC[2] > p1c:
                    P2C.append(P1C.pop(SC[2]))
                    
            else:
                p2c = len(P2C) - 1
                if not SC[2] > p2c:
                    P1C.append(P2C.pop(SC[2]))

        elif SC[1] == 1:
            if SC[0] == 1:
                p1b = len(P1B) - 1
                if not SC[2] > p1b:
                    P2C.append(P1B.pop(SC[2]))
                    
            else:
                p2b = len(P2B) - 1
                if not SC[2] > p2b:
                    P1C.append(P2B.pop(SC[2]))

        elif SC[1] == 0:
            if SC[0] == 1:
                p1a = len(P1A) - 1
                if not SC[2] > p1a:
                    P2C.append(P1A.pop(SC[2]))
                    
            else:
                p2a = len(P2A) - 1
                if not SC[2] > p2a:
                    P1C.append(P2A.pop(SC[2]))
               
        MaxP1A = 0
        MaxP2A = 0
        MaxP1B = 0
        MaxP2B = 0
        MaxPC = 0
    

    # Check if Selected Card Exists
    timer = 0
    while timer < 3:
        if SC[0] == 1:
            if SC[1] == 0:
                PC = P1A
            elif SC[1] == 1:
                PC = P1B
            else:
                PC = P1C
        else:
            if SC[1] == 0:
                PC = P2A
            elif SC[1] == 1:
                PC = P2B
            else:
                PC = P2C

        pc = len(PC) - 1
        if pc < 1:
            SC[1] += 1
        else:
            break

        if Fight == 1:
            if SC[1] > 1:
                SC[1] = 1
        else:
            if SC[1] > 2:
                SC[1] = 2

        timer += 1

    if pc < 1:
        timer = 0
        while timer < 3:
            if SC[0] == 1:
                if SC[1] == 0:
                    PC = P1A
                elif SC[1] == 1:
                    PC = P1B
                else:
                    PC = P1C
            else:
                if SC[1] == 0:
                    PC = P2A
                elif SC[1] == 1:
                    PC = P2B
                else:
                    PC = P2C

            pc = len(PC) - 1
            if pc < 1:
                SC[1] -= 1
            else:
                break

            if SC[1] < 0:
                SC[1] = 0

            timer += 1
                
    if SC[2] > pc:
        SC[2] = pc

    if SC[2] == 0:
        if Fight == 1:
            SC = [AP, 1, 1]
        else:
            SC = [AP, 2, 1]


    # Check if All Rolls Are Done
    if P1R or P2R:
        PR = 1
    else:
        PR = 0
            
    if Fight == -1:
        p1a = len(P1A) - 1
        p2a = len(P2A) - 1
        if p1a > 0 and P1R and p2a > 0 and P2R:
            if AP == 1 and p1a == 2 and P1R == 1:
                SC[1] = 0
                SC[2] = 2
            elif AP == 2 and p2a == 2 and P2R == 1:
                SC[1] = 0
                SC[2] = 2
            else:
                SC[1] = 0
                SC[2] = 1
        elif p1a > 0 and P1R:
            AP = 1
            if p1a == 2 and P1R == 1:
                SC = [1,0,2]
            else:
                SC = [1,0,1]
        elif p2a > 0 and P2R:
            AP = 2
            if p2a == 2 and P2R == 1:
                SC = [2,0,2]
            else:
                SC = [2,0,1]
        else:
            Fight = 0
            PR = 0
            P1R = 0
            P2R = 0

            # Remove Old Enemy Cards
            for (ec, line) in enumerate(EC):
                if EC[ec].ID > 0:
                    EC[ec].Frequency += 1
                    EC[ec] = E[0]
            
            # Remove Active Enemy Abbilities
            AEA = []
            for (ea, line) in enumerate(EA):
                AEA.append(0)

            # Level Up Players
            turn = len(Turn) - 1

            P1Level += turn % 2
            P2Level += turn % 2

            # Players Draw 2 Items
            Card = 1
            PC = P1C
            while Card < 3:
                if Card == 1:
                    pick = Card
                    id = len(ID) - 1
                        
                while True:
                    if pick > id:
                        pick = 1
                        # Construct New Item Deck
                        ID = IDeck.Create(I)
                    elif ID[pick].ID == 0:
                        pick += 1
                    else:
                        break
                PC.append(ID[pick])
                ID[pick] = I[0]

                Card += 1

                if Card == 3 and PC == P1C:
                    Card = 1
                    PC = P2C
        

    # Quit Game
    if keys[GUI.K_ESCAPE]:
        run = False


#Quit Game
GUI.quit()
