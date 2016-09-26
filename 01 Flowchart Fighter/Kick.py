import random
import Strike
import Grabbing

Limit = lambda x: max(1, min(6, x))
    
def Groin(skip, HITpenalty, DMGpenalty, attacker, defender, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Kick to the groin.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 4 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 4:
            OutputLines.append(' Missed.')
        elif d6 == 4:
            OutputLines.append(' You missed the groin, hitting the left upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines) 
        elif d6 == 5:
            OutputLines.append(' You missed the groin, hitting the right upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        else:
            DMGpenalty -= 1
            OutputLines.append(' You missed the groin, hitting the belly instead.')
            OutputLines.append('')
            return Strike.Belly(True, HITpenalty, DMGpenalty, attacker, defender, 0, OutputLines)

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 7:
            OutputLines.append(' Hit groin.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Legs.Groin < 4:
                DamageBonus = 0
            elif defender.Legs.Groin < 7:
                DamageBonus = 1
            elif defender.Legs.Groin < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 < 4 - DamageBonus:
                OutputLines.append('  Bruised groin.')
                defender.Legs.Groin += 1
                    
            elif d6 < 7 - DamageBonus:
                OutputLines.append('  Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)

            else:
                OutputLines.append('  Stunned opponent.')
                defender.Stunned = 4
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

    return OutputLines

def UpperLeg(skip, HITpenalty, DMGpenalty, attacker, defender, side, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Kick to the '+side+' upper leg.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 3 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 4:
            OutputLines.append(' Missed.')
        elif d6 == 4 and side == 'left':
            OutputLines.append(' You missed the '+side+' upper leg, hitting the right upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        elif d6 == 4 and side == 'right':
            OutputLines.append(' You missed the '+side+' upper leg, hitting the left upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)
        elif d6 == 5 and side == 'left':
            OutputLines.append(' You missed the '+side+' upper leg, hitting the left lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines) 
        elif d6 == 5 and side == 'right':
            OutputLines.append(' You missed the '+side+' upper leg, hitting the right lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        else:
            OutputLines.append(' You missed the '+side+' upper leg, hitting the groin instead.')
            OutputLines.append('')
            return Groin(True, HITpenalty, DMGpenalty, attacker, defender, OutputLines)   

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 5:
            OutputLines.append(' Hit '+side+' upper leg.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                ULeg = defender.Legs.LULeg
            else:
                ULeg = defender.Legs.RULeg

            if ULeg < 4:
                DamageBonus = 0
            elif ULeg < 7:
                DamageBonus = 1
            elif ULeg < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if ULeg < 10:
                    OutputLines.append('  Bruised '+side+' upper leg.')
                    ULeg += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' upper leg muscle was already torn.')

            else:
                if ULeg < 10:
                    OutputLines.append('  Tore the muscle on '+side+' upper leg.')
                    ULeg = 10
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' upper leg muscle was already torn.')

            if side == 'left':
                defender.Legs.LULeg = ULeg
            else:
                defender.Legs.RULeg = ULeg

        elif d6 == 5:
            OutputLines.append(' Hit '+side+' hip.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Hip = defender.Legs.LHip
            else:
                Hip = defender.Legs.RHip

            if Hip < 4:
                DamageBonus = 0
            elif Hip < 7:
                DamageBonus = 1
            elif Hip < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if Hip < 10:
                    OutputLines.append('  Bruised '+side+' hip.')
                    Hip += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' hip was already dislocated.')

            else:
                if Hip < 10:
                    OutputLines.append('  Dislocated '+side+' hip, opponent fell down.')
                    Hip = 10
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' hip was already dislocated.')

            if side == 'left':
                defender.Legs.LHip = Hip
            else:
                defender.Legs.RHip = Hip

        elif d6 == 6:
            OutputLines.append(' Hit '+side+' knee.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Knee = defender.Legs.LKnee
            else:
                Knee = defender.Legs.RKnee

            if Knee < 4:
                DamageBonus = 0
            elif Knee < 7:
                DamageBonus = 1
            elif Knee < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if Knee < 10:
                    OutputLines.append('  Bruised '+side+' knee.')
                    Knee += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' knee was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Opponent fell down.')
                defender.Stance = 2
                defender.Stunned += 2
                Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                
            else:
                if Knee < 10:
                    OutputLines.append('  Broke '+side+' knee, opponent fell down.')
                    Knee = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 1, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' knee was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LKnee = Knee
            else:
                defender.Legs.RKnee = Knee
                            
    return OutputLines

def LowerLeg(skip, HITpenalty, DMGpenalty, attacker, defender, side, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Kick to the '+side+' lower leg.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 4 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 4:
            OutputLines.append(' Missed.')
        elif d6 == 4 and side == 'left':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the right lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        elif d6 == 4 and side == 'right':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the left lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)
        elif d6 == 5 and side == 'left':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the left upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines) 
        elif d6 == 5 and side == 'right':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the right upper leg instead.')
            OutputLines.append('')
            return UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        elif d6 == 6 and side == 'left':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the left foot instead.')
            OutputLines.append('')
            return Foot(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines) 
        elif d6 == 6 and side == 'right':
            OutputLines.append(' You missed the '+side+' lower leg, hitting the right foot instead.')
            OutputLines.append('')
            return Foot(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)    

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 5:
            OutputLines.append(' Hit '+side+' lower leg.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                LLeg = defender.Legs.LLLeg
            else:
                LLeg = defender.Legs.RLLeg

            if LLeg < 6:
                DamageBonus = 0
            elif LLeg < 9:
                DamageBonus = 1
            else:
                DamageBonus = 3

            if d6 < 6 - DamageBonus - DamageBonus:
                if LLeg < 10:
                    OutputLines.append('  Bruised '+side+' lower leg.')
                    LLeg += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' lower leg was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 7 - DamageBonus:
                OutputLines.append('  Opponent fell down.')
                defender.Stance = 2
                defender.Stunned += 2
                Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
            else:
                if LLeg < 10:
                    OutputLines.append('  Broke '+side+' lower leg, opponent fell down.')
                    LLeg = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 1, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' lower leg was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LLLeg = LLeg
            else:
                defender.Legs.RLLeg = LLeg

        elif d6 == 5:
            OutputLines.append(' Hit '+side+' ankle.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Ankle = defender.Legs.LAnkle
            else:
                Ankle = defender.Legs.RAnkle

            if Ankle < 4:
                DamageBonus = 0
            elif Ankle < 7:
                DamageBonus = 1
            elif Ankle < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if Ankle < 10:
                    OutputLines.append('  Bruised '+side+' ankle.')
                    Ankle += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' ankle was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Opponent fell down.')
                defender.Stance = 2
                defender.Stunned += 2
                Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                
            else:
                if Ankle < 10:
                    OutputLines.append('  Broke '+side+' ankle, opponent fell down.')
                    Ankle = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 1, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' ankle was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LAnkle = Ankle
            else:
                defender.Legs.RAnkle = Ankle

        elif d6 == 6:
            OutputLines.append(' Hit '+side+' knee.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Knee = defender.Legs.LKnee
            else:
                Knee = defender.Legs.RKnee

            if Knee < 4:
                DamageBonus = 0
            elif Knee < 7:
                DamageBonus = 1
            elif Knee < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if Knee < 10:
                    OutputLines.append('  Bruised '+side+' knee.')
                    Knee += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' knee was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Opponent fell down.')
                defender.Stance = 2
                defender.Stunned += 2
                Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                
            else:
                if Knee < 10:
                    OutputLines.append('  Broke '+side+' knee, opponent fell down.')
                    Knee = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 1, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' knee was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LKnee = Knee
            else:
                defender.Legs.RKnee = Knee
                
    return OutputLines

def Foot(skip, HITpenalty, DMGpenalty, attacker, defender, side, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Kick to the '+side+' foot.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 5 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 5:
            OutputLines.append(' Missed.')
        elif d6 == 5 and side == 'left':
            OutputLines.append(' You missed the '+side+' foot, hitting the right foot instead.')
            OutputLines.append('')
            return Foot(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines) 
        elif d6 == 5 and side == 'right':
            OutputLines.append(' You missed the '+side+' foot, hitting the left foot instead.')
            OutputLines.append('')
            return Foot(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)
        elif d6 == 6 and side == 'left':
            OutputLines.append(' You missed the '+side+' foot, hitting the left lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines) 
        elif d6 == 6 and side == 'right':
            OutputLines.append(' You missed the '+side+' foot, hitting the right lower leg instead.')
            OutputLines.append('')
            return LowerLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)    

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 4:
            OutputLines.append(' Hit '+side+' foot.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                MFoot = defender.Legs.LFoot
            else:
                MFoot = defender.Legs.RFoot

            if MFoot < 4:
                DamageBonus = 0
            elif MFoot < 7:
                DamageBonus = 1
            elif MFoot < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if MFoot < 10:
                    OutputLines.append('  Bruised '+side+' foot.')
                    MFoot += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' foot was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)

            else:
                if MFoot < 10:
                    OutputLines.append('  Broke '+side+' foot, opponent fell down.')
                    MFoot = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' foot was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LFoot = MFoot
            else:
                defender.Legs.RFoot = MFoot

        elif d6 < 6:
            OutputLines.append(' Hit toes on '+side+' foot.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                BToe = defender.Legs.LBToe
                Toes0 = defender.Legs.LToes0
                Toes1 = defender.Legs.LToes1
            else:
                BToe = defender.Legs.RBToe
                Toes0 = defender.Legs.RToes0
                Toes1 = defender.Legs.RToes1

            if Toes1 < 4:
                DamageBonus = 0
            elif Toes1 < 7:
                DamageBonus = 1
            elif Toes1 < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4


            if d6 < 5 - DamageBonus:
                if Toes0 < 4:
                    OutputLines.append('  Bruised a toe on '+side+' foot.')
                    Toes1 += 1
                else:
                    OutputLines.append('  Toes on '+side+' foot were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)

                    
            elif d6 < 6:
                if Toes0 < 4:
                    if Toes0 > 1:
                        OutputLines.append('  Broke a toe on '+side+' foot, opponent fell down.')
                        Toes0 += 1
                        defender.Crippled = 10
                        defender.Stance = 2
                        defender.Stunned += 2
                        Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                    else:
                        OutputLines.append('  Broke a toe on '+side+' foot.')
                        Toes0 += 1
                else:
                    OutputLines.append('  Toes on '+side+' foot were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if BToe < 10:
                    OutputLines.append('  Broke big toe on '+side+' foot, opponent fell down.')
                    BToe = 10
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Big toe on '+side+' foot was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                 defender.Legs.LBToe = BToe
                 defender.Legs.LToes0 = Toes0
                 defender.Legs.LToes1 = Toes1
            else:
                 defender.Legs.RBToe = BToe
                 defender.Legs.RToes0 = Toes0
                 defender.Legs.RToes1 = Toes1
                    

        elif d6 == 6:
            OutputLines.append(' Hit '+side+' ankle.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Ankle = defender.Legs.LAnkle
            else:
                Ankle = defender.Legs.RAnkle

            if Ankle < 4:
                DamageBonus = 0
            elif Ankle < 7:
                DamageBonus = 1
            elif Ankle < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if Ankle < 10:
                    OutputLines.append('  Bruised '+side+' ankle.')
                    Ankle += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' ankle was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Opponent fell down.')
                defender.Stance = 2
                defender.Stunned += 2
                Grabbing.Attacked ('kick', 2, attacker, defender, OutputLines)
                
            else:
                if Ankle < 10:
                    OutputLines.append('  Broke '+side+' ankle, opponent fell down.')
                    Ankle = 10
                    defender.NumBroken += 1
                    defender.Crippled = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    Grabbing.Attacked ('kick', 1, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' ankle was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Legs.LAnkle = Ankle
            else:
                defender.Legs.RAnkle = Ankle
                
    return OutputLines
