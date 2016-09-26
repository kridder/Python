import random
import Human
import DMGCalc

def Personality(attacker):

    d7 = random.randint(1, 7)
    if d7 < 2:
        attacker.personality0 = 1
    elif d7 < 3:
        attacker.personality0 = 2
    elif d7 < 4:
        attacker.personality0 = 3
    elif d7 < 5:
        attacker.personality0 = 4
    elif d7 < 6:
        attacker.personality0 = 5
    elif d7 < 7:
        attacker.personality0 = 6
    else:
        attacker.personality0 = 7

    d7 = random.randint(1, 7)
    if d7 == 1:
        attacker.personality1 = 1
    elif d7 == 2:
        attacker.personality1 = 2
    elif d7 == 3:
        attacker.personality1 = 3
    elif d7 == 4:
        attacker.personality1 = 4
    elif d7 == 5:
        attacker.personality1 = 5
    elif d7 == 6:
        attacker.personality1 = 6
    else:
        attacker.personality1 = 7


def Key(personality, attacker, defender):

    move = 0
    DMGCalc.ArmCrip (attacker, defender)
    DMGCalc.Totals (attacker, defender)

   
    if attacker.Stance == 2 and attacker.Crippled < 10 and attacker.Hit < 1:
        key = 's'
    elif attacker.Stance == 2 and attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
        key = 's'



    elif personality[0] == 1:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1 and attacker.Arms.LUArm < 10 and attacker.Arms.RUArm < 10 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif defender.Stunned > 1 and attacker.Arms.LUArm < 10 and attacker.Arms.RUArm < 10 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        else:
            move = 'strike'
        
       
        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                key = 'a'
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
                if attacker.Arms.LHand > 1:
                    key = 'a'
                elif attacker.Arms.RHand > 1:
                    key = 'b'
                else:
                    key = 'a'
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            elif attacker.Arms.LHand > 1:
                key = 'a'
            elif attacker.Arms.RHand > 1:
                key = 'b'
            else:
                key = 'a'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'c'
                
            

    elif personality[0] == 2:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10 and defender.Stunned > 0:
            if attacker.NumBlinded > 0:
                key = 'g'
            else:
                key = 'r'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.Arms.LHand > 1 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.LArmCrip == 10 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.LArmCrip == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        else:
            move = 'strike'
        
       
        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                key = 'a'
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    key = 'a'
                elif attacker.Arms.RUArm == 10:
                    key = 'b'
                else:
                    key = 'a'
            elif attacker.Arms.LHand > 1:
                key = 'a'
            elif attacker.Arms.RHand > 1:
                key = 'b'
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            else:
                key = 'random'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'random'
                    


    elif personality[0] == 3:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10 and defender.Stunned > 0:
            if attacker.NumBlinded > 0:
                key = 'g'
            else:
                d6 = random.randint(1, 6)
                if d6 < 4:
                    key = 'g'
                else:
                    key = 'r'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10 and attacker.Arms.LUArm < 10 and attacker.Arms.RUArm < 10:
                d6 = random.randint(1, 6)
                if d6 < 4:
                    move = 'kick'
                else:
                    key = 'g'
            else:
                move = 'kick'
        elif attacker.Arms.LHand > 1 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.LArmCrip == 10 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10 and attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            d6 = random.randint(1, 6)
            if d6 < 4:
                move = 'kick'
            else:
                move = 'strike'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.LArmCrip == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        else:
            d6 = random.randint(1, 6)
            if d6 < 3:
                move = 'kick'
            elif d6 < 5:
                move = 'strike'
            else:
                key = 'g'


        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                if attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                    key = 'random'
                else:
                    key = 'a'            
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    if attacker.Arms.RUArm == 10:
                        key = 'random'
                    else:
                        key = 'a'
                elif attacker.Arms.RUArm == 10:
                    key = 'b'
                else:
                    key = 'random'
            elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
                if attacker.Arms.LHand > 1:
                    if attacker.Arms.RHand > 1:
                        key = 'random'
                    else:
                        key = 'a'
                elif attacker.Arms.RHand > 1:
                    key = 'b'
                else:
                    key = 'random'            
            elif attacker.Arms.LHand > 1:
                if attacker.Arms.RUArm == 10:
                    key = 'random'
                else:
                    key = 'a'            
            elif attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    key = 'random'
                else:
                    key = 'b'             
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            else:
                key = 'random'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'random'
            elif attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'random'



    elif personality[0] == 4:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.Grabbed == 0:
            if attacker.NumBlinded > 0:
                key = 'g'
            else:
                key = 'r'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        else:
            if attacker.LBDMG > attacker.UBDMG:
                move = 'kick'
            else:
                move = 'strike'


        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                key = 'a'
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    key = 'a'
                elif attacker.Arms.RUArm == 10:
                    key = 'b'
                else:
                    key = 'a'
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            elif attacker.Arms.LHand > 1:
                key = 'a'
            elif attacker.Arms.RHand > 1:
                key = 'b'
            else:
                key = 'random'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'random'



    elif personality[0] == 5:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            if attacker.Arms.LUArm < 10 and attacker.Arms.RUArm < 10 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif defender.Stunned > 1 and attacker.Arms.LUArm < 10 and attacker.Arms.RUArm < 10 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        else:
            move = 'kick'
        
       
        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                key = 'a'
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
                if attacker.Arms.LHand > 1:
                    key = 'a'
                elif attacker.Arms.RHand > 1:
                    key = 'b'
                else:
                    key = 'a'
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            elif attacker.Arms.LHand > 1:
                key = 'a'
            elif attacker.Arms.RHand > 1:
                key = 'b'
            else:
                key = 'a'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'c'



    elif personality[0] == 6:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10 and defender.Stunned > 0:
            if attacker.NumBlinded > 0:
                key = 'g'
            else:
                key = 'r'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.Grabbed == 0:
            if attacker.NumBlinded > 0:
                key = 'g'
            else:
                key = 'r'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.Arms.LHand > 1 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.LArmCrip == 10 and attacker.Arms.RHand > 1:
            move = 'kick'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        else:
            move = 'kick'
        
       
        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                key = 'a'
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    key = 'a'
                elif attacker.Arms.RUArm == 10:
                    key = 'b'
                else:
                    key = 'a'
            elif attacker.Arms.LHand > 1:
                key = 'a'
            elif attacker.Arms.RHand > 1:
                key = 'b'
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            else:
                key = 'random'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'random'



    elif personality[0] == 7:

        if defender.Stance == 2 or attacker.Stance == 2:
            move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Grabbed > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Grabbing > 0 and attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
            move = 'strike'
        elif attacker.NumBlinded > 0:
            if attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
                key = 'g'
            else:
                move = 'strike'
        elif attacker.LArmCrip == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.RArmCrip == 10:
            move = 'kick'
        elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
            move = 'kick'
        elif attacker.LArmCrip < 10 and attacker.RArmCrip < 10:
            key = 'g'
        else:
            move = 'strike'


        if move == 'strike':

            if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
                if attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                    key = 'random'
                else:
                    key = 'a'            
            elif attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
                key = 'b'
            elif attacker.Arms.LHand > 1 and attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    if attacker.Arms.RUArm == 10:
                        key = 'random'
                    else:
                        key = 'a'
                elif attacker.Arms.RUArm == 10:
                    key = 'b'
                else:
                    key = 'random'
            elif attacker.Arms.LUArm == 10 and attacker.Arms.RUArm == 10:
                if attacker.Arms.LHand > 1:
                    if attacker.Arms.RHand > 1:
                        key = 'random'
                    else:
                        key = 'a'
                elif attacker.Arms.RHand > 1:
                    key = 'b'
                else:
                    key = 'random'            
            elif attacker.Arms.LHand > 1:
                if attacker.Arms.RUArm == 10:
                    key = 'random'
                else:
                    key = 'a'            
            elif attacker.Arms.RHand > 1:
                if attacker.Arms.LUArm == 10:
                    key = 'random'
                else:
                    key = 'b'             
            elif attacker.Arms.LUArm == 10:
                key = 'a'
            elif attacker.Arms.RUArm == 10:
                key = 'b'
            else:
                key = 'random'

        elif move == 'kick':

            if attacker.Legs.RULeg == 10 and attacker.Legs.LULeg == 10:
                key = 'random'
            elif attacker.Legs.LULeg == 10:
                key = 'c'
            elif attacker.Legs.RULeg == 10:
                key = 'd'
            else:
                key = 'random'



    else:
        print 'Personality ERROR'


    if key == 'random':
        d6 = random.randint(1, 6)

        if move == 'strike':
            if d6 < 4:
                key = 'a'
            else:
                key = 'b'

        if move == 'kick':
            if d6 < 4:
                key = 'c'
            else:
                key = 'd'

    return key


def Attack(personality, attacker, defender, key):

    if key == 'a':
        Hand = attacker.Arms.RHand
        UArm = attacker.Arms.RUArm
        ULeg = 0
    elif key == 'b':
        Hand = attacker.Arms.LHand
        UArm = attacker.Arms.LUArm
        ULeg = 0
    elif key == 'c':
        Hand = 0
        UArm = 0
        ULeg = attacker.Legs.RULeg
    elif key == 'd':
        Hand = 0
        UArm = 0
        ULeg = attacker.Legs.LULeg
    else:
        Hand = 0
        UArm = 0
        ULeg = 0

    if personality[1] == 1:

        if key == 'a' or key == 'b':        
            if attacker.Stance == 2:
                attack = 'b'
            elif attacker.NumBlinded > 0:
                attack = 'b'
            elif Hand > 1:
                attack = 'b'
            else:
                attack = 'a'
        
        elif key == 'c' or key == 'd':
            attack = 'd'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                        if attacker.Legs.LULeg < 10 and attacker.Legs.RULeg < 10:
                            d6 = random.randint(1, 6)
                            if d6 < 4:
                                attack = 'd'
                            else:
                                attack = 'f'
                        elif attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                            attack = 'e'
                        else:
                            attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        if attacker.Legs.LULeg == 10:
                            attack = 'a'
                        elif attacker.Legs.RULeg == 10:
                            attack = 'b'
                        elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                            attack = 'b'
                        else:
                            attack = 'a'
                    else:
                        attack = 'c'

            else:
                if attacker.Grabbed == 0 or defender.Stunned > 0:
                    if attacker.Legs.LULeg < 10 and attacker.Legs.RULeg < 10:
                        d6 = random.randint(1, 6)
                        if d6 < 4:
                            attack = 'e'
                        else:
                            attack = 'f'
                    elif attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                        attack = 'e'
                    else:
                        attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        if attacker.Legs.LULeg == 10:
                            attack = 'a'
                        elif attacker.Legs.RULeg == 10:
                            attack = 'b'
                        elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                            attack = 'b'
                        else:
                            attack = 'a'
                    else:
                        attack = 'c'

        else:
            attack = 0


    elif personality[1] == 2:

        if key == 'a' or key == 'b':
            if attacker.Stance == 2:
                attack = 'b'
            elif attacker.NumBlinded > 0:
                attack = 'b'
            elif Hand > 1:
                attack = 'b'
            elif UArm == 10:
                attack = 'a'
            else:
                attack = 'b'

            if attack == 'b':
                d10 = random.randint(0, 9)
                if d10 == 9:
                    attack = 'c'

            if attack == 'b' and attacker.Grabbed > 0:
                attack = 'c'

        elif key == 'c' or key == 'd':
            if attacker.NumBlinded > 0:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'b'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif ULeg == 10:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'd'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            else:
                attack = 'd'

            if attack == 'd':
                d6 = random.randint(1, 6)
                if d6 == 6:
                    attack = 'a'

            if attack != 'd' and attacker.Grabbed > 0:
                attack = 'a'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'
            else:
                if attacker.Grabbed == 0 or defender.Stunned > 0:
                    attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'

        else:
            attack = 0


    elif personality[1] == 3:

        if key == 'a' or key == 'b':
            if attacker.NumBroken > 1:
                if attacker.Stance == 2:
                    d6 = random.randint(1, 6)
                    if d6 > 4:
                        attack = 'a'
                    else:
                        attack = 'b'
                else:
                    attack = 'a'
            elif attacker.NumBlinded > 0:
                attack = 'b'
            elif UArm == 10:
                if Hand > 1 or attacker.Stance == 2:
                    attack = 'b'
                else:
                    attack = 'a'
            elif defender.Arms.RUArm == 10 or defender.Arms.RShoulder == 10 or defender.Arms.RElbow == 10 or defender.Arms.RHand > 2:
                if defender.Arms.LUArm == 10 or defender.Arms.LShoulder == 10 or defender.Arms.LElbow == 10 or defender.Arms.LHand > 2:
                    if Hand > 1 or attacker.Stance == 2:
                        attack = 'b'
                    else:
                        attack = 'a'
                else:
                    attack = 'e'
            else:
                attack = 'd'

            if attack == 'b':
                d10 = random.randint(0, 9)
                if d10 == 9:
                    attack = 'c'

            if attack != 'a' and attacker.Grabbed > 0:
                attack = 'c'

        elif key == 'c' or key == 'd':
            if attacker.NumBlinded > 0:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'b'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif ULeg == 10:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'd'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif defender.Legs.RULeg == 10:
                if defender.Legs.LULeg == 10:
                    attack = 'd'
                else:
                    attack = 'c'
            else:
                attack = 'b'

            if attack != 'd' and attacker.Grabbed > 0:
                attack = 'a'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                    attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'
            else:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                    attack = 'f'
                elif attacker.Grabbed == 0 or defender.Stunned > 0:
                    if attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                        attack = 'e'
                    else:
                        attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'

        else:
            attack = 0
        
    
    elif personality[1] == 4:

        if key == 'a' or key == 'b':
            d5 = random.randint(1, 5)
            if d5 < 2:
                attack = 'e'
            elif d5 < 3:
                attack = 'd'
            elif d5 < 4:
                attack = 'c'
            elif d5 < 5:
                attack = 'b'
            else:
                attack = 'a'

        elif key == 'c' or key == 'd':
            d7 = random.randint(1, 7)
            if d7 < 2:
                attack = 'g'
            elif d7 < 3:
                attack = 'f'
            elif d7 < 4:
                attack = 'e'
            elif d7 < 5:
                attack = 'd'
            elif d7 < 6:
                attack = 'c'
            elif d7 < 7:
                attack = 'b'
            else:
                attack = 'a'

        elif key == 'g':
            d6 = random.randint(1, 6)
            if d6 < 2:
                attack = 'f'
            elif d6 < 3:
                attack = 'e'
            elif d6 < 4:
                attack = 'd'
            elif d6 < 5:
                attack = 'c'
            elif d6 < 6:
                attack = 'b'
            else:
                attack = 'a'

        else:
            attack = 0


    elif personality[1] == 5:

        if key == 'a' or key == 'b':
            if attacker.Stance == 2:
                attack = 'b'
            elif attacker.NumBlinded > 0:
                attack = 'b'
            elif Hand > 1:
                attack = 'b'
            elif UArm == 10:
                attack = 'a'
            elif defender.NumBlinded > 0:
                if defender.Arms.RUArm == 10 or defender.Arms.RShoulder == 10 or defender.Arms.RElbow == 10 or defender.Arms.RHand > 2:
                    if defender.Arms.LUArm == 10 or defender.Arms.LShoulder == 10 or defender.Arms.LElbow == 10 or defender.Arms.LHand > 2:
                        attack = 'a'
                    else:
                        attack = 'e'
                else:
                    attack = 'd'
            else:
                attack = 'a'

        elif key == 'c' or key == 'd':
            if attacker.NumBlinded > 0:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'b'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif ULeg == 10:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'd'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif defender.Legs.RULeg == 10:
                if defender.Legs.LULeg == 10:
                    attack = 'd'
                else:
                    attack = 'c'
            else:
                attack = 'b'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                    attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'
            else:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                    attack = 'f'
                elif attacker.Grabbed == 0 or defender.Stunned > 0:
                    if attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                        attack = 'e'
                    else:
                        attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'

        else:
            attack = 0
            

    elif personality[1] == 6:

        if key == 'a' or key == 'b':
            if attacker.Stance == 2:
                attack = 'b'
            elif attacker.NumBlinded > 0:
                attack = 'b'
            elif Hand > 1:
                attack = 'b'
            elif UArm == 10:
                attack = 'a'
            elif defender.Chest.SolarPlexus == 10:
                if defender.Head.Jaw == 10:
                    attack = 'b'
                else:
                    attack = 'a'
            else:
                attack = 'b'

        elif key == 'c' or key == 'd':
            if attacker.NumBlinded > 0:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'b'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            elif ULeg == 10:
                if defender.Legs.RULeg == 10:
                    if defender.Legs.LULeg == 10:
                        attack = 'd'
                    else:
                        attack = 'c'
                else:
                    attack = 'b'
            else:
                attack = 'd'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                    attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    if attacker.Legs.LULeg == 10:
                        attack = 'a'
                    elif attacker.Legs.RULeg == 10:
                        attack = 'b'
                    elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                        attack = 'b'
                    else:
                        attack = 'a'
            else:
                if attacker.Grabbed == 0 or defender.Stunned > 0:
                    attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'd'
                else:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        if attacker.Legs.LULeg == 10:
                            attack = 'a'
                        elif attacker.Legs.RULeg == 10:
                            attack = 'b'
                        elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                            attack = 'b'
                        else:
                            attack = 'a'
                    else:
                        attack = 'd'

        else:
            attack = 0


    elif personality[1] == 7:

        if key == 'a' or key == 'b':        
            if attacker.Stance == 2:
                attack = 'b'
            elif defender.Stunned > 0 or defender.Stance == 2:
                if Hand > 1:
                    attack = 'b'
                else:
                    attack = 'a'
            else: attack = 'c'
        
        elif key == 'c' or key == 'd':
            if defender.Stunned > 0:
                attack = 'd'
            else:
                attack = 'a'

        elif key == 'g':
            if attacker.Arms.LUArm == 10 or attacker.Arms.RUArm == 10:
                if attacker.Grabbed == 0 and defender.Stunned > 0:
                        if attacker.Legs.LULeg < 10 and attacker.Legs.RULeg < 10:
                            d6 = random.randint(1, 6)
                            if d6 < 4:
                                attack = 'e'
                            else:
                                attack = 'f'
                        elif attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                            attack = 'e'
                        else:
                            attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        if attacker.Legs.LULeg == 10:
                            attack = 'a'
                        elif attacker.Legs.RULeg == 10:
                            attack = 'b'
                        elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                            attack = 'b'
                        else:
                            attack = 'a'
                    else:
                        attack = 'c'

            else:
                if attacker.Grabbed == 0 or defender.Stunned > 0:
                    if attacker.Legs.LULeg < 10 and attacker.Legs.RULeg < 10:
                        d6 = random.randint(1, 6)
                        if d6 < 4:
                            attack = 'e'
                        else:
                            attack = 'f'
                    elif attacker.Legs.LULeg < 10 or attacker.Legs.RULeg < 10:
                        attack = 'e'
                    else:
                        attack = 'd'
                elif attacker.Legs.LULeg == 10 and attacker.Legs.RULeg == 10:
                    attack = 'c'
                else:
                    d6 = random.randint(1, 6)
                    if d6 < 4:
                        if attacker.Legs.LULeg == 10:
                            attack = 'a'
                        elif attacker.Legs.RULeg == 10:
                            attack = 'b'
                        elif attacker.Legs.RKnee > attacker.Legs.LKnee:
                            attack = 'b'
                        else:
                            attack = 'a'
                    else:
                        attack = 'c'

        else:
            attack = 0

        
    else:
        print 'Personality ERROR'

    return attack
