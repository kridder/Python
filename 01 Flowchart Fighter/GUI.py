import pygame as GUI
import random
import time
import Human
import Strike
import Kick
import Grabbing
import ArtInt
import DMGCalc
import Stunned
import InputKeys

run = True
#play = True
EndTurn = 0
P1 = Human.Human()
P2 = Human.Human()

P1.Name = 'P1'
P2.Name = 'P2'

#player = 'P1'
#nplayer = 'P2'
attacker = P1
defender = P2

personality = [0, 0]

OldOutputLines = []
OldOutputLines2 = []
OldOutputLines3 = []
OldOutputLines4 = []
OldOutputLines5 = []

GUI.init()
font = GUI.font.Font(None, 14)
GTitle = font.render('Flowchart Fighter 0.04.0', False, (0, 0, 0))
HP1 = font.render('Health P1', True, (0, 0, 0))
HP2 = font.render('Health P2', True, (0, 0, 0))

resolution = (1200,800)
screen = GUI.display.set_mode( resolution )

while run:

    # TEST
    #P2.Legs.RFoot = 10
    #attacker.Stance = 2
    #attacker.Crippled = 10
    #attacker.Arms.LShoulder = 10
    # TEST    

    GUI.event.pump()
    keys = GUI.key.get_pressed()

    if keys[GUI.K_ESCAPE]:
        run = False

    #player = attacker.Name
    #nplayer = defender.Name

    OutputLines = ['']
    InputLines = [attacker.Name+'.']
    InputKey = False

    key = ''
    attack = ''

    #InputLines[0] = player+'.'

    if attacker.NumBlinded > 0:
        HITpenalty = 1
        if attacker.Grabbing > 0 or attacker.Grabbed > 0:
            HITpenalty = 0
            if attacker.NumBlinded > 1:
                HITpenalty = 1
    else:
        HITpenalty = 0

    if attacker.Stance < 2 and defender.Stance == 2:
        HITpenalty -= 1

    if defender.Stunned > 0:
        HITpenalty -= 1

    personality[0] = attacker.personality0
    personality[1] = attacker.personality1
    DMGpenalty = 0
    hand = 0
    leg = 0
    

    # Check if input required
    Stunned.Check (attacker)
    
    if attacker.Stunned > 0:
        InputLines.append('')
        InputLines.append('You are stunned.')
        OutputLines.append(attacker.Name+' is stunned.')
        #key = ''
        #attack = ''

    elif attacker.AI == True:

        if attacker.NumBroken > attacker.PastBroken and attacker.NumBroken > defender.NumBroken and personality[1] == 5:

            ArtInt.Personality(attacker)

            personality[0] = attacker.personality0
            personality[1] = attacker.personality1

        #pers = str(personality)

        InputLines.append('')
        InputLines.append('AI '+str(personality))

        key = ArtInt.Key(personality, attacker, defender)
        attack = ArtInt.Attack(personality, attacker, defender, key)
        
    else:
        InputKey = True
        if attacker.RArmCrip < 10:
            InputLines.append('a. Strike with right hand.')
        if attacker.LArmCrip < 10:
            InputLines.append('b. Strike with left hand.')
        if attacker.Stance < 2 and defender.Stance < 2:
            InputLines.append('c. Kick with right leg.')
            InputLines.append('d. Kick with left leg.')
        if attacker.Stance == 0 and defender.Stance == 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            InputLines.append('')
            if attacker.Grabbing == 0:
                InputLines.append('g. Grab opponent.')
            elif attacker.Grabbing > 0:
                InputLines.append('g. Wrestle with your opponent.')
        if attacker.Grabbing > 0 or attacker.Grabbed > 0:
            if attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                InputLines.append('r. Break hold.')
            else:
                InputLines.append('r. Release hold.')
        if attacker.Stance > 0 and attacker.Crippled == 0:
            InputLines.append('')
            InputLines.append('s. Stand up.')
        InputLines.append('')
        InputLines.append('y. Yield.')
        InputLines.append('z. Let A.I. take over.')

        
    # Main screen
    screen.fill((255,255,255))
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((5, 5), (1190, 790)), 1)
    screen.blit(GTitle, (9, 9))

    # Output screen
    NewOutputLines = OldOutputLines5 + OldOutputLines4 + OldOutputLines3 + OldOutputLines2 + OldOutputLines + OutputLines
    for (i, line) in enumerate(NewOutputLines):
        Output = font.render(NewOutputLines[i], True, (0, 0, 0))
        screen.blit(Output, (19, 29 + 10*i))

    # Input screen
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((10, 450), (790, 340)), 1)
    for (i, line) in enumerate(InputLines):
    #for each i in range(0,9):
        Input = font.render(InputLines[i], True, (0, 0, 0))
        screen.blit(Input, (14, 454 + 10*i))
    
    # Health P1
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((805, 10), (385, 388)), 1)
    screen.blit(HP1, (809, 14))

    #HP1Lines = ['NumBroken: '+str(P1.NumBroken), 'NumPierced: '+str(P1.NumPierced), 'NumBlinded: '+str(P1.NumBlinded), 'K.O.: '+str(P1.KO), 'Crippled: '+str(P1.Crippled), 'RArmCrip: '+str(P1.RArmCrip), 'LArmCrip: '+str(P1.LArmCrip), '', 'Total Head Damage: '+str(P1.Head.DMG)]
    HP1Lines1 = P1.Health1()
    for (i, line) in enumerate(HP1Lines1):    
        #Input = font.render(HP1Lines1[i], True, (0, 0, 255))
        #screen.blit(Input, (809, 34 + 10*i))

        for s in str.split(HP1Lines1[i]):
            if s.isdigit():
                if i < 5:
                    a = min(255, int(s) * 85)
                else:
                    a = min(255, int(s) * 20)
        
        Input = font.render(HP1Lines1[i], True, (0, 0, 255 - a))
        screen.blit(Input, (809, 34 + 10*i))

    HP1Lines2 = P1.Health2()
    for (i, line) in enumerate(HP1Lines2):
        for s in str.split(HP1Lines2[i]):
            if s.isdigit():
                a = min(255, int(s) * 20)
        
        Input = font.render(HP1Lines2[i], True, (0, 0, 255 - a))
        screen.blit(Input, (1003, 24 + 10*i))
    
    # Health P2
    GUI.draw.rect(screen, (0, 0, 0), GUI.Rect((805, 403), (385, 387)), 1)
    screen.blit(HP2, (809, 407))

    HP2Lines1 = P2.Health1()
    for (i, line) in enumerate(HP2Lines1):
        for s in str.split(HP2Lines1[i]):
            if s.isdigit():
                if i < 5:
                    a = min(255, int(s) * 85)
                else:
                    a = min(255, int(s) * 20)
        
        Input = font.render(HP2Lines1[i], True, (0, 0, 255 - a))
        screen.blit(Input, (809, 427 + 10*i))

    HP2Lines2 = P2.Health2()
    for (i, line) in enumerate(HP2Lines2):
        for s in str.split(HP2Lines2[i]):
            if s.isdigit():
                a = min(255, int(s) * 20)
        
        Input = font.render(HP2Lines2[i], True, (0, 0, 255 - a))
        screen.blit(Input, (1003, 417 + 10*i))
    
    GUI.display.flip()


    # Input key
    if InputKey:
        while run:
            GUI.event.pump()
            keys = GUI.key.get_pressed()
            
            key = InputKeys.key(run)

            if key == 'z':
                break
            if key == 'ESCAPE':
                break
            if key == 'a':
                break
            if key == 'b':
                break
            if key == 'c':
                break
            if key == 'd':
                break
            if attacker.Stance == 0 and defender.Stance == 0:
                if key == 'g':
                    break
            if attacker.Grabbing > 0 or attacker.Grabbed > 0:
                if key == 'r':
                    break
            if attacker.Stance > 0:
                if key == 's':
                    break
            if key == 'y':
                break
            if key == 'SPACE':
                break


    # Compute input
    if key == 'z':
        attacker.AI = True
        #OutputLines.append(player+' is now controlled by AI.')

        ArtInt.Personality(attacker)

        personality[0] = attacker.personality0
        personality[1] = attacker.personality1

        #pers = str(personality)

        OutputLines.append(attacker.Name+' is now controlled by AI '+str(personality)+'.')
        OutputLines.append('')
        InputLines = [attacker.Name+'.']

        key = ArtInt.Key(personality, attacker, defender)
        attack = ArtInt.Attack(personality, attacker, defender, key)

    if key == 'ESCAPE':
        run = False

    # Strike with right hand.
    if key == 'a':
        hand = 'right'

        if attacker.Stance == 2:
            DMGpenalty += 1
        if attacker.Arms.RUArm == 10:
            DMGpenalty += 1
        if attacker.Grabbed > 0:
            DMGpenalty += 1
            
        if attacker.RENerve > 1:
            DMGpenalty += 2
        elif attacker.RENerve > 0:
            DMGpenalty += 1

        if attacker.Arms.RElbow == 10:
            OutputLines.append('Cannot attack with your right arm because your elbow is broken.')
            hand = 0
        elif attacker.Arms.RShoulder == 10:
            OutputLines.append('Cannot attack with your right arm because your shoulder is dislocated.')
            hand = 0
        elif attacker.Arms.RHand > 2:
            OutputLines.append('Cannot attack with your right hand because your fingers are broken.')
            hand = 0
        elif attacker.Grabbing > 0:
            OutputLines.append('Cannot strike while grabbing')
            hand = 0

    # Strike with left hand.
    if key == 'b':
        hand = 'left'

        if attacker.Stance == 2:
            DMGpenalty += 1
        if attacker.Arms.LUArm == 10:
            DMGpenalty += 1
        if attacker.Grabbed > 0:
            DMGpenalty += 1

        if attacker.LENerve > 1:
            DMGpenalty += 2
        elif attacker.LENerve > 0:
            DMGpenalty += 1

        if attacker.Arms.LElbow == 10:
            OutputLines.append('Cannot attack with your left arm because your elbow is broken.')
            hand = 0   
        elif attacker.Arms.LShoulder == 10:
            OutputLines.append('Cannot attack with your left arm because your shoulder is dislocated.')
            hand = 0
        elif attacker.Arms.LHand > 2:
            OutputLines.append('Cannot attack with your left hand because your fingers are broken.')
            hand = 0
        elif attacker.Grabbing > 0:
            OutputLines.append('Cannot strike while grabbing')
            hand = 0

    # Check if further input required (only when striking)
    if hand == 'right' or hand == 'left':
        OutputLines.append(attacker.Name+' strikes with '+hand+' hand.')
        defender.Attacked = 1

        InputKey = False

        if attacker.NumBlinded > 1:
            InputLines = [attacker.Name+'.']
            InputLines.append('')
            InputLines.append('You are blind.')
            d6 = random.randint(1, 6)

            if d6 < 2:
                attack = 'e'
            elif d6 < 3:
                attack = 'd'
            elif d6 < 4:
                attack = 'c'
            elif d6 < 6:
                attack = 'b'
            else:
                attack = 'a'

        elif attacker.AI == False:
            #attack = raw_input('> ')
            InputKey = True
            InputLines = [attacker.Name+'.']
            InputLines.append('a. Strike to the head.')
            InputLines.append('b. Strike to the chest.')
            InputLines.append('c. Strike to the belly.')
            InputLines.append('d. Strike to the right upper arm.')
            InputLines.append('e. Strike to the left upper arm.')

        #else:
            #print '> AI'

        # Print New Output
        screen.fill((255,255,255), (10, 25, 795, 425))
        
        NewOutputLines = OldOutputLines4 + OldOutputLines3 + OldOutputLines2 + OldOutputLines + OutputLines
        for (i, line) in enumerate(NewOutputLines):
            Output = font.render(NewOutputLines[i], True, (0, 0, 0))
            screen.blit(Output, (19, 29 + 10*i))

        screen.fill((255,255,255), (11, 451, 788, 338))
        
        for (i, line) in enumerate(InputLines):
            Input = font.render(InputLines[i], True, (0, 0, 0))
            screen.blit(Input, (14, 454 + 10*i))        

        GUI.display.flip()
        

        # Input attack
        if InputKey:
            while run:
                GUI.event.pump()
                keys = GUI.key.get_pressed()
                
                attack = InputKeys.key(run)
            
                if attack == 'ESCAPE':
                    break
                if attack == 'a':
                    break
                if attack == 'b':
                    break
                if attack == 'c':
                    break
                if attack == 'd':
                    break
                if attack == 'e':
                    break
                if attack == 'SPACE':
                    break
            
        # Compute input
        if attack == 'a':
            OutputLines = Strike.Head(False, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)

        if attack == 'b':
            OutputLines = Strike.Chest(False, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)

        if attack == 'c':
            OutputLines = Strike.Belly(False, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)

        if attack == 'd':
            OutputLines = Strike.UpperArm(False, HITpenalty, DMGpenalty, attacker, defender, hand, 'right', OutputLines)

        if attack == 'e':
            OutputLines = Strike.UpperArm(False, HITpenalty, DMGpenalty, attacker, defender, hand, 'left', OutputLines)

    # Kick with right leg.
    if key == 'c':
        leg = 'right'

        if attacker.Legs.RULeg == 10:
            DMGpenalty += 1
        if attacker.Grabbed > 0:
            DMGpenalty += 1

        if attacker.Stance == 2:
            OutputLines.append('Cannot kick while on the ground.')
            leg = 0
        elif defender.Stance == 2:
            OutputLines.append('Not allowed to kick a prone opponent.')
            leg = 0

    # Kick with left leg.
    if key == 'd':
        leg = 'left'

        if attacker.Legs.LULeg == 10:
            DMGpenalty += 1
        if attacker.Grabbed > 0:
            DMGpenalty += 1

        if attacker.Stance == 2:
            OutputLines.append('Cannot kick while on the ground.')
            leg = 0
        elif defender.Stance == 2:
            OutputLines.append('Not allowed to kick a prone opponent.')
            leg = 0

    # Check if further input required (only when kicking)
    if leg == 'right' or leg == 'left':
        OutputLines.append(attacker.Name+' kicks with '+leg+' leg.')
        defender.Attacked = 1

        InputKey = False

        if attacker.NumBlinded > 1:
            InputLines = [attacker.Name+'.']
            InputLines.append('')
            InputLines.append('You are blind.')
            d11 = random.randint(1, 11)

            if d11 < 2:
                attack = 'g'
            elif d11 < 3:
                attack = 'f'
            elif d11 < 5:
                attack = 'e'
            elif d11 < 7:
                attack = 'd'
            elif d11 < 9:
                attack = 'c'
            elif d11 < 11:
                attack = 'b'
            else:
                attack = 'a'

        elif attacker.AI == False:
            InputKey = True
            InputLines = [attacker.Name+'.']
            InputLines.append('a. Kick to the groin.')
            InputLines.append('b. Kick to the right upper leg.')
            InputLines.append('c. Kick to the left upper leg.')
            InputLines.append('d. Kick to the right lower leg.')
            InputLines.append('e. Kick to the left lower leg.')
            InputLines.append('f. Kick to the right foot.')
            InputLines.append('g. Kick to the left foot.')

        # Print New Output
        screen.fill((255,255,255), (10, 25, 795, 425))
        
        NewOutputLines = OldOutputLines4 + OldOutputLines3 + OldOutputLines2 + OldOutputLines + OutputLines
        for (i, line) in enumerate(NewOutputLines):
            Output = font.render(NewOutputLines[i], True, (0, 0, 0))
            screen.blit(Output, (19, 29 + 10*i))

        screen.fill((255,255,255), (11, 451, 788, 338))
        
        for (i, line) in enumerate(InputLines):
            Input = font.render(InputLines[i], True, (0, 0, 0))
            screen.blit(Input, (14, 454 + 10*i))        

        GUI.display.flip()
        

        # Input attack
        if InputKey:
            while run:
                GUI.event.pump()
                keys = GUI.key.get_pressed()
                
                attack = InputKeys.key(run)
            
                if attack == 'ESCAPE':
                    break
                if attack == 'a':
                    break
                if attack == 'b':
                    break
                if attack == 'c':
                    break
                if attack == 'd':
                    break
                if attack == 'e':
                    break
                if attack == 'f':
                    break
                if attack == 'g':
                    break
                if attack == 'SPACE':
                    break
            
        # Compute input
        if attack == 'a':
            OutputLines = Kick.Groin(False, HITpenalty, DMGpenalty, attacker, defender, OutputLines)   

        if attack == 'b':
            OutputLines = Kick.UpperLeg(False, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)

        if attack == 'c':
            OutputLines = Kick.UpperLeg(False, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)

        if attack == 'd':
            OutputLines = Kick.LowerLeg(False, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)

        if attack == 'e':
            OutputLines = Kick.LowerLeg(False, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)

        if attack == 'f':
            OutputLines = Kick.Foot(False, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)

        if attack == 'g':
            OutputLines = Kick.Foot(False, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)

    # Grab
    if attacker.Stance == 0 and defender.Stance == 0:
        if key == 'g':
            DMGCalc.ArmCrip (attacker, defender)
            if attacker.LArmCrip == 10 or attacker.RArmCrip == 10:
                OutputLines.append('Cannot grab with a crippled arm.')
            elif attacker.Grabbing == 0:
                OutputLines = Grabbing.Grab (HITpenalty, attacker, defender, OutputLines)
            elif attacker.Grabbing > 0:
                OutputLines.append(attacker.Name+' wrestles with '+defender.Name+'.')
                
                if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                    DMGpenalty += 1
                    HITpenalty += 1
                if attacker.Grabbed == 0:
                    HITpenalty -= 1
                
                InputKey = False

                if attacker.AI == False:
                    InputKey = True
                    InputLines = [attacker.Name+'.']
                    InputLines.append('a. Pull down and knee with right knee.')
                    InputLines.append('b. Pull down and knee with left knee.')
                    InputLines.append('c. Headbutt to head.')
                    InputLines.append('d. Leg throw.')
                    InputLines.append('e. Hip throw.')
                    InputLines.append('f. Bear hug.')

                # Print New Output
                screen.fill((255,255,255), (10, 25, 795, 425))
                
                NewOutputLines = OldOutputLines4 + OldOutputLines3 + OldOutputLines2 + OldOutputLines + OutputLines
                for (i, line) in enumerate(NewOutputLines):
                    Output = font.render(NewOutputLines[i], True, (0, 0, 0))
                    screen.blit(Output, (19, 29 + 10*i))

                screen.fill((255,255,255), (11, 451, 788, 338))
                
                for (i, line) in enumerate(InputLines):
                    Input = font.render(InputLines[i], True, (0, 0, 0))
                    screen.blit(Input, (14, 454 + 10*i))        

                GUI.display.flip()
                    
                
                # Input attack
                if InputKey:
                    while run:
                        GUI.event.pump()
                        keys = GUI.key.get_pressed()
                        
                        attack = InputKeys.key(run)
                    
                        if attack == 'ESCAPE':
                            break
                        if attack == 'a':
                            break
                        if attack == 'b':
                            break
                        if attack == 'c':
                            break
                        if attack == 'd':
                            break
                        if attack == 'e':
                            break
                        if attack == 'f':
                            break
                        if attack == 'SPACE':
                            break
                                
                # Compute input
                if attack == 'a':
                    if attacker.Legs.RULeg == 10:
                        DMGpenalty += 1
                    OutputLines = Grabbing.Knee (HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)
                if attack == 'b':
                    if attacker.Legs.LULeg:
                        DMGpenalty += 1
                    OutputLines = Grabbing.Knee (HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)
                if attack == 'c':
                    OutputLines = Grabbing.Headbutt (HITpenalty, DMGpenalty, attacker, defender, OutputLines)
                if attack == 'd':
                    OutputLines = Grabbing.Legthrow (HITpenalty, DMGpenalty, attacker, defender, OutputLines)
                if attack == 'e':
                    if attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                        HITpenalty += 1
                    OutputLines = Grabbing.Hipthrow (HITpenalty, DMGpenalty, attacker, defender, OutputLines)
                if attack == 'f':
                    if attacker.Legs.LULeg == 10 or attacker.Legs.RULeg == 10:
                        HITpenalty += 1
                    OutputLines = Grabbing.Bearhug (HITpenalty, DMGpenalty, attacker, defender, OutputLines)

    # Release
    if attacker.Grabbing > 0 or attacker.Grabbed > 0:
        if key == 'r':
            DMGCalc.ArmCrip (attacker, defender)
            if attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
                OutputLines.append('Cannot break hold of opponent with crippled arms.')
            else:
                if attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
                    DMGpenalty += 1
                if defender.Arms.LUArm == 10 and defender.Arms.RUArm == 10:
                    DMGpenalty -= 1
                if defender.Stunned > 0:
                    DMGpenalty -= 2
                Grabbing.Release (DMGpenalty, attacker, defender, OutputLines)

    # Stand
    if attacker.Stance > 0:
        if key == 's':
            if attacker.Legs.RHip == 10 or attacker.Legs.LHip == 10:
                OutputLines.append('Cannot stand up because your hip is dislocated.')
            elif attacker.Legs.RKnee == 10 or attacker.Legs.LKnee == 10:
                OutputLines.append('Cannot stand up because your knee is broken.')
            elif attacker.Legs.RAnkle == 10 or attacker.Legs.LAnkle == 10:
                OutputLines.append('Cannot stand up because your ankle is broken.')
            elif attacker.Legs.RFoot == 10 or attacker.Legs.LFoot == 10:
                OutputLines.append('Cannot stand up because your foot is broken.')
            elif attacker.Legs.RBToe == 10 or attacker.Legs.LBToe == 10:
                OutputLines.append('Cannot stand up because your big toe is broken.')
            elif attacker.Legs.RToes0 > 2 or attacker.Legs.LToes0 > 2:
                OutputLines.append('Cannot stand up because your toes are broken.')
            elif attacker.Crippled > 0:
                OutputLines.append('Cannot stand up because you are crippled.')
            else:

                if defender.Stance == 2:
                    OutputLines.append(attacker.Name+' stands up.')
                    attacker.Stance = 0
                    
                elif attacker.Hit > 0:
                    d6 = random.randint(1, 6)
                    if d6 < 5:
                        OutputLines.append(attacker.Name+' failed to stand up.')
                    else:
                        OutputLines.append(attacker.Name+' stands up.')
                        attacker.Stance = 0
                        
                elif attacker.Attacked > 0:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        OutputLines.append(attacker.Name+' failed to stand up.')
                    else:
                        OutputLines.append(attacker.Name+' stands up.')
                        attacker.Stance = 0

                else:
                    d6 = random.randint(1, 6)
                    if d6 < 3:
                        OutputLines.append(attacker.Name+' failed to stand up.')
                    else:
                        OutputLines.append(attacker.Name+' stands up.')
                        attacker.Stance = 0

    # Yield
    if key == 'y':
        attacker.Yield = 10

    # Skip turn
    if key == 'SPACE':
        OutputLines.append(attacker.Name+' Skipped a turn.')


    # Damage and win calculations
    DMGCalc.Totals (attacker, defender)
    DMGCalc.ArmCrip (attacker, defender)
    

    run = DMGCalc.WinCheck (P1, P2, attacker, defender, run, OutputLines)


    attacker.Hit = 0
    attacker.Attacked = 0
    attacker.PastBroken = attacker.NumBroken
    

    # Print New Output
    # Output Lines
    screen.fill((255,255,255), (10, 25, 795, 425))
    
    NewOutputLines = OldOutputLines4 + OldOutputLines3 + OldOutputLines2 + OldOutputLines + OutputLines
    for (i, line) in enumerate(NewOutputLines):
        Output = font.render(NewOutputLines[i], True, (0, 0, 0))
        screen.blit(Output, (19, 29 + 10*i))

    # Input Lines
    screen.fill((255,255,255), (11, 451, 788, 338))
    
    if InputKey:
            InputLines = [attacker.Name+'.']

    InputLines.append('')
    if run:
        InputLines.append('Press SPACE to end turn.')
    if not run:
        InputLines.append('Press ESCAPE to end game.')
        
    for (i, line) in enumerate(InputLines):
        Input = font.render(InputLines[i], True, (0, 0, 0))
        screen.blit(Input, (14, 454 + 10*i))

    # HP1 Lines
    screen.fill((255,255,255), (806, 24, 383, 373))
    
    HP1Lines1 = P1.Health1()
    for (i, line) in enumerate(HP1Lines1):    
        for s in str.split(HP1Lines1[i]):
            if s.isdigit():
                if i < 5:
                    a = min(255, int(s) * 85)
                else:
                    a = min(255, int(s) * 20)
        
        Input = font.render(HP1Lines1[i], True, (0, 0, 255 - a))
        screen.blit(Input, (809, 34 + 10*i))

    HP1Lines2 = P1.Health2()
    for (i, line) in enumerate(HP1Lines2):    
        for s in str.split(HP1Lines2[i]):
            if s.isdigit():
                a = min(255, int(s) * 20)
        
        Input = font.render(HP1Lines2[i], True, (0, 0, 255 - a))
        screen.blit(Input, (1003, 24 + 10*i))

    # HP2 Lines
    screen.fill((255,255,255), (806, 417, 383, 372))
    
    HP2Lines1 = P2.Health1()
    for (i, line) in enumerate(HP2Lines1):    
        for s in str.split(HP2Lines1[i]):
            if s.isdigit():
                if i < 5:
                    a = min(255, int(s) * 85)
                else:
                    a = min(255, int(s) * 20)
        
        Input = font.render(HP2Lines1[i], True, (0, 0, 255 - a))
        screen.blit(Input, (809, 427 + 10*i))

    HP2Lines2 = P2.Health2()
    for (i, line) in enumerate(HP2Lines2):    
        for s in str.split(HP2Lines2[i]):
            if s.isdigit():
                a = min(255, int(s) * 20)
        
        Input = font.render(HP2Lines2[i], True, (0, 0, 255 - a))
        screen.blit(Input, (1003, 417 + 10*i))

    GUI.display.flip()


    # Save Output
    OutputLines.append('')

    OldOutputLines5 = OldOutputLines4
    OldOutputLines4 = OldOutputLines3
    OldOutputLines3 = OldOutputLines2
    OldOutputLines2 = OldOutputLines
    OldOutputLines = OutputLines


    # Space to end turn
    if EndTurn < 2:
        if EndTurn < 1 or not InputKey and not attacker.AI:
            while run:
                GUI.event.pump()
                keys = GUI.key.get_pressed()
                
                if keys[GUI.K_SPACE]:
                        while keys[GUI.K_SPACE]:
                            GUI.event.pump()
                            keys = GUI.key.get_pressed()              

                    
                        break

                if keys[GUI.K_RETURN]:
                        while keys[GUI.K_RETURN]:
                            GUI.event.pump()
                            keys = GUI.key.get_pressed()              


                        EndTurn += 1
                        break

                if keys[GUI.K_ESCAPE]:
                    run = False

    while not run:
        GUI.event.pump()
        keys = GUI.key.get_pressed()

        if keys[GUI.K_ESCAPE]:
            break
    
    if defender == P2:
        #player = 'P2'
        #nplayer = 'P1'
        attacker = P2
        defender = P1
          
    else:
        #player = 'P1'
        #nplayer = 'P2'
        attacker = P1
        defender = P2

GUI.quit()
