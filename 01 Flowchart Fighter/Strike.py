import random
import Kick
import Grabbing

Limit = lambda x: max(1, min(6, x))
    
def Head(skip, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Strike to the head.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if attacker.Stance == 2 and defender.Stance < 2 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)
        
        if d6 < 6:
            OutputLines.append(' Missed, cannot reach head.')
        else:
            OutputLines.append(' You missed the head, hitting the chest instead.')
            OutputLines.append('')
            return Chest(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)        

    elif d6 < 4 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 6:
            OutputLines.append(' Missed.')
        else:
            OutputLines.append(' You missed the head, hitting the chest instead.')
            OutputLines.append('')
            return Chest(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)
            
    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 == 1:
            OutputLines.append(' Hit left side of skull.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.LSkull < 4:
                DamageBonus = 0
            elif defender.Head.LSkull < 7:
                DamageBonus = 1
            elif defender.Head.LSkull < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3
            
            if d6 < 3:
                OutputLines.append('  Broke a finger on your '+hand+' hand.')
                if hand == 'right':
                    attacker.Arms.RHand += 1                    
                else:
                    attacker.Arms.LHand += 1
                                
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Bruised left side of the skull.')
                defender.Head.LSkull += 1
            elif d6 < 7 - DamageBonus:
                if defender.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning opponent.')
                    defender.Brain += 1
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)

                elif defender.Brain < 2:
                    if defender.Stance < 2:
                        OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                    else:
                        OutputLines.append('  Caused concussion, opponent is stunned.')
                    defender.Brain += 1
                    defender.Stance = 2
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked out opponent.')
                    defender.Brain += 1
                    defender.KO = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
            else:
                OutputLines.append('  Broke left side of the skull.')
                defender.Head.LSkull = 10
                defender.NumBroken += 1
                defender.Brain = 10
                Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

        elif d6 == 2:
            OutputLines.append(' Hit right side of skull.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.RSkull < 4:
                DamageBonus = 0
            elif defender.Head.RSkull < 7:
                DamageBonus = 1
            elif defender.Head.RSkull < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 < 3:
                OutputLines.append('  Broke a finger on your '+hand+' hand.')
                if hand == 'right':
                    attacker.Arms.RHand += 1                    
                else:
                    attacker.Arms.LHand += 1
                        
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Bruised right side of the skull.')
                defender.Head.RSkull += 1
            elif d6 < 7 - DamageBonus:
                if defender.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning opponent.')
                    defender.Brain += 1
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)

                elif defender.Brain < 2:
                    if defender.Stance < 2:
                        OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                    else:
                        OutputLines.append('  Caused concussion, opponent is stunned.')
                    defender.Brain += 1
                    defender.Stance = 2
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked out opponent.')
                    defender.Brain += 1
                    defender.KO = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
            else:
                OutputLines.append('  Broke right side of the skull.')
                defender.Head.RSkull = 10
                defender.NumBroken += 1
                defender.Brain = 10
                Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

        elif d6 == 3:
            OutputLines.append(' Hit left eye.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.LEyeSocket < 4:
                DamageBonus = 0
            elif defender.Head.LEyeSocket < 7:
                DamageBonus = 1
            elif defender.Head.LEyeSocket < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 == 1:
                OutputLines.append('  Broke a finger on your '+hand+' hand.')
                if hand == 'right':
                    attacker.Arms.RHand += 1                    
                else:
                    attacker.Arms.LHand += 1
                        
            elif d6 < 5 - DamageBonus:
                if defender.Head.LEyeSocket < 10:
                    OutputLines.append('  Bruised left eye.')
                    defender.Head.LEyeSocket += 1
                else:
                    OutputLines.append('  Left eye socket was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Head.LEyeSocket < 10:
                    OutputLines.append('  Broke left eye socket.')
                    defender.Head.LEyeSocket = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Left eye socket was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Head.LEye < 10:
                    OutputLines.append('  Blinded left eye.')
                    defender.Head.LEye = 10
                    defender.NumBlinded += 1
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Left eye was already blinded.')

        elif d6 == 4:
            OutputLines.append(' Hit right eye.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.REyeSocket < 4:
                DamageBonus = 0
            elif defender.Head.REyeSocket < 7:
                DamageBonus = 1
            elif defender.Head.REyeSocket < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 == 1:
                OutputLines.append('  Broke a finger on your '+hand+' hand.')
                if hand == 'right':
                    attacker.Arms.RHand += 1                    
                else:
                    attacker.Arms.LHand += 1
                                            
            elif d6 < 5 - DamageBonus:
                if defender.Head.REyeSocket < 10:
                    OutputLines.append('  Bruised right eye.')
                    defender.Head.REyeSocket += 1
                else:
                    OutputLines.append('  Right eye socket was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                
            elif d6 > 6:
                if defender.Head.REyeSocket < 10:
                    OutputLines.append('  Broke right eye socket.')
                    defender.Head.REyeSocket = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Right eye socket was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                
            else:
                if defender.Head.REye < 10:
                    OutputLines.append('  Blinded right eye.')
                    defender.Head.REye = 10
                    defender.NumBlinded += 1
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Right eye was already blinded.')

        elif d6 == 5:
            OutputLines.append(' Hit nose.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.Nose < 4:
                DamageBonus = 0
            elif defender.Head.Nose < 7:
                DamageBonus = 1
            elif defender.Head.Nose < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 < 2 - DamageBonus:
                if defender.Head.Nose < 10:
                    OutputLines.append('  Bruised nose.')
                    defender.Head.Nose += 1
                else:
                    OutputLines.append('  Nose was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 4 - DamageBonus:
                if defender.Head.Nose < 10:
                    OutputLines.append('  Caused nosebleed.')
                    defender.Head.Nose += 1
                else:
                    OutputLines.append('  Nose was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Head.Nose < 10:
                    OutputLines.append('  Broke nose.')
                    defender.Head.Nose = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Nose was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Head.Nose < 10:
                    OutputLines.append('  Broke nosebone, jamming it into the brain.')
                    defender.Head.Nose = 10
                    defender.NumBroken += 1
                    defender.Brain = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Nose was already broken, but you jammed the broken pieces into the brain.')
                    defender.Head.Nose = 10
                    defender.Brain = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

        elif d6 == 6:
            OutputLines.append(' Hit jaw.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Head.Nose < 4:
                DamageBonus = 0
            elif defender.Head.Nose < 7:
                DamageBonus = 1
            elif defender.Head.Nose < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 < 4 - DamageBonus:
                if defender.Head.Jaw < 10:
                    OutputLines.append('  Bruised jaw.')
                    defender.Head.Jaw += 1
                else:
                    OutputLines.append('  Jaw was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Head.Jaw < 10:
                    OutputLines.append('  Broke jaw.')
                    defender.Head.Jaw = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Jaw was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Head.Jaw < 10:
                    OutputLines.append('  Knocked out opponent.')
                    defender.KO = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Jaw was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

    return OutputLines

def Chest(skip, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Strike to the chest.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 3 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 3:
            OutputLines.append(' Missed.')
        elif d6 == 3:
            OutputLines.append(' You missed the chest, hitting the left upper arm instead.')
            OutputLines.append('')
            return UpperArm(True, HITpenalty, DMGpenalty, attacker, defender, hand, 'left', OutputLines)
        elif d6 == 4:
            OutputLines.append(' You missed the chest, hitting the right upper arm instead.')
            OutputLines.append('')
            return UpperArm(True, HITpenalty, DMGpenalty, attacker, defender, hand, 'right', OutputLines)    
        elif d6 == 5:
            OutputLines.append(' You missed the chest, hitting the belly instead.')
            OutputLines.append('')
            return Belly(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)
        elif d6 == 6 and attacker.Stance == 2 and defender.Stance < 2 :
            OutputLines.append(' Missed.')
        else:
            OutputLines.append(' You missed the chest, hitting the head instead.')
            OutputLines.append('')
            return Head(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)   

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 == 1:
            OutputLines.append(' Hit breastbone.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.Breastbone < 4:
                DamageBonus = 0
            elif defender.Chest.Breastbone < 7:
                DamageBonus = 1
            elif defender.Chest.Breastbone < 9:
                DamageBonus = 2
            else:
                DamageBonus = 3

            if d6 < 3:
                OutputLines.append('  Nothing happened.')
            elif d6 < 6 - DamageBonus:
                if defender.Chest.Breastbone < 10:
                    OutputLines.append('  Bruised breastbone.')
                    defender.Chest.Breastbone += 1
                else:
                    OutputLines.append('  Breastbone was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.Breastbone < 10:
                    OutputLines.append('  Broke breastbone.')
                    defender.Chest.Breastbone = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Breastbone was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

        elif d6 == 2:
            OutputLines.append(' Hit left lower ribs.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.LLRibs < 4:
                DamageBonus = 0
            elif defender.Chest.LLRibs < 7:
                DamageBonus = 1
            elif defender.Chest.LLRibs < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if defender.Chest.LLRibs < 10:
                    OutputLines.append('  Bruised left lower ribs.')
                    defender.Chest.LLRibs += 1
                else:
                    OutputLines.append('  Left lower ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.LLRibs < 10:
                    OutputLines.append('  Broke left lower ribs.')
                    defender.Chest.LLRibs = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Left lower ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

        elif d6 == 3:
            OutputLines.append(' Hit right lower ribs.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.RLRibs < 4:
                DamageBonus = 0
            elif defender.Chest.RLRibs < 7:
                DamageBonus = 1
            elif defender.Chest.RLRibs < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if defender.Chest.RLRibs < 10:
                    OutputLines.append('  Bruised right lower ribs.')
                    defender.Chest.RLRibs += 1
                else:
                    OutputLines.append('  Right lower ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.RLRibs < 10:
                    OutputLines.append('  Broke right lower ribs.')
                    defender.Chest.RLRibs = 10
                    defender.NumBroken += 1
                                       
                else:
                    OutputLines.append('  Right lower ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

        elif d6 == 4:
            OutputLines.append(' Hit left upper ribs.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.LURibs < 4:
                DamageBonus = 0
            elif defender.Chest.LURibs < 7:
                DamageBonus = 1
            elif defender.Chest.LURibs < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if defender.Chest.LURibs < 10:
                    OutputLines.append('  Bruised left upper ribs.')
                    defender.Chest.LURibs += 1
                else:
                    OutputLines.append('  Left upper ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Chest.LURibs < 10:
                    OutputLines.append('  Broke left upper ribs.')
                    defender.Chest.LURibs = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Left upper ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.LURibs < 10:
                    OutputLines.append('  Broke left upper ribs, piercing the left lung.')
                    defender.Chest.LURibs = 10
                    defender.Chest.LLung = 10
                    defender.NumBroken += 1
                    defender.NumPierced += 1
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                elif defender.Chest.LURibs == 10 and defender.Chest.LLung == 10:
                    OutputLines.append('  Left upper ribs were already broken and the left lung was already pierced.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Left upper ribs were already broken, but the broken fragments pierced the left lung.')
                    defender.Chest.LLung = 10
                    defender.NumPierced += 1
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)

        elif d6 == 5:
            OutputLines.append(' Hit right upper ribs.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.RURibs < 4:
                DamageBonus = 0
            elif defender.Chest.RURibs < 7:
                DamageBonus = 1
            elif defender.Chest.RURibs < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if defender.Chest.RURibs < 10:
                    OutputLines.append('  Bruised right upper ribs.')
                    defender.Chest.RURibs += 1
                else:
                    OutputLines.append('  Right upper ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Chest.RURibs < 10:
                    OutputLines.append('  Broke right upper ribs.')
                    defender.Chest.RURibs = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Right upper ribs were already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.RURibs < 10:
                    OutputLines.append('  Broke right upper ribs, piercing the right lung.')
                    defender.Chest.RURibs = 10
                    defender.Chest.RLung = 10
                    defender.NumBroken += 1
                    defender.NumPierced += 1
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                elif defender.Chest.RURibs == 10 and defender.Chest.RLung == 10:
                    OutputLines.append('  Right upper ribs were already broken and the right lung was already pierced.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Right upper ribs were already broken, but the broken fragments pierced the right lung.')
                    defender.Chest.RLung = 10
                    defender.NumPierced += 1
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

        elif d6 == 6:
            OutputLines.append(' Hit solar plexus.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if defender.Chest.SolarPlexus < 4:
                DamageBonus = 0
            elif defender.Chest.SolarPlexus < 7:
                DamageBonus = 1
            elif defender.Chest.SolarPlexus < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if defender.Chest.SolarPlexus < 10:
                    OutputLines.append('  Bruised solar plexus.')
                    defender.Chest.SolarPlexus += 1
                else:
                    OutputLines.append('  Solar plexus was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6:
                if defender.Chest.SolarPlexus < 10:
                    OutputLines.append('  Broke solar plexus.')
                    defender.Chest.SolarPlexus = 10
                    defender.NumBroken += 1
                else:
                    OutputLines.append('  Solar plexus was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)
                    
            else:
                if defender.Chest.SolarPlexus < 10:
                    OutputLines.append('  Knocked out opponent.')
                    defender.KO = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  Solar plexus was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

    return OutputLines

def Belly(skip, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Strike to the belly.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 3 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 5:
            OutputLines.append(' Missed.')
        elif d6 == 5:
            DMGpenalty += 1
            OutputLines.append(' You missed the belly, hitting the groin instead.')
            OutputLines.append('')
            return Kick.Groin(True, HITpenalty, DMGpenalty, attacker, defender, OutputLines)
        else:
            OutputLines.append(' You missed the belly, hitting the chest instead.')
            OutputLines.append('')
            return Chest(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)   

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 7:
            OutputLines.append(' Hit belly.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if d6 < 5:
                OutputLines.append('  Nothing happened.')
            else:
                OutputLines.append('  Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)

    return OutputLines

def UpperArm(skip, HITpenalty, DMGpenalty, attacker, defender, hand, side, OutputLines):

    if skip == False:
        OutputLines.append('')
        OutputLines.append('Strike to the '+side+' upper arm.')

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 4 and skip == False:

        DMGpenalty += 1
        d6 = random.randint(1, 6)

        if d6 < 6:
            OutputLines.append(' Missed.')
        else:
            OutputLines.append(' You missed the '+side+' upper arm, hitting the chest instead.')
            OutputLines.append('')
            return Chest(True, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines)   

    else:
        d6 = random.randint(1, 6)
        defender.Hit = 1
        if d6 < 5:
            OutputLines.append( ' Hit '+side+' upper arm.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                UArm = defender.Arms.LUArm
            else:
                UArm = defender.Arms.RUArm

            if UArm < 4:
                DamageBonus = 0
            elif UArm < 7:
                DamageBonus = 1
            elif UArm < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if UArm < 10:
                    OutputLines.append('  Bruised '+side+' upper arm.')
                    UArm += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' upper arm muscle was already torn.')
                    
            else:
                if UArm < 10:
                    OutputLines.append('  Tore the muscle on '+side+' upper arm.')
                    UArm = 10
                    Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' upper arm muscle was already torn.')

            if side == 'left':
                defender.Arms.LUArm = UArm
            else:
                defender.Arms.RUArm = UArm

        elif d6 == 5:
            OutputLines.append(' Hit '+side+' shoulder.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Shoulder = defender.Arms.LShoulder
            else:
                Shoulder = defender.Arms.RShoulder

            if Shoulder < 4:
                DamageBonus = 0
            elif Shoulder < 7:
                DamageBonus = 1
            elif Shoulder < 9:
                DamageBonus = 2
            else:
                DamageBonus = 5

            if d6 < 6 - DamageBonus:
                if Shoulder < 10:
                    OutputLines.append('  Bruised '+side+' shoulder.')
                    Shoulder += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' shoulder was already dislocated.')
                
            else:
                if Shoulder < 10:
                    OutputLines.append('  Dislocated '+side+' shoulder.')
                    Shoulder = 10
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' shoulder was already dislocated.')

            if side == 'left':
                defender.Arms.LShoulder = Shoulder
            else:
                defender.Arms.RShoulder = Shoulder

        elif d6 == 6:
            OutputLines.append(' Hit '+side+' elbow.')
            d6 = Limit(random.randint(1, 6) - DMGpenalty)

            if side == 'left':
                Elbow = defender.Arms.LElbow
            else:
                Elbow = defender.Arms.RElbow

            if Elbow < 4:
                DamageBonus = 0
            elif Elbow < 7:
                DamageBonus = 1
            elif Elbow < 9:
                DamageBonus = 2
            else:
                DamageBonus = 4

            if d6 < 5 - DamageBonus:
                if Elbow < 10:
                    OutputLines.append('  Bruised '+side+' elbow.')
                    Elbow += 1
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' elbow was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned += 2
                    Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
            elif d6 < 6 - DamageBonus:
                OutputLines.append('  Hit nerve on '+side+' elbow.')
                Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                if side == 'left':
                    defender.LENerve = 3
                else:
                    defender.RENerve = 3
            else:
                if Elbow < 10:
                    OutputLines.append('  Broke '+side+' elbow.')
                    Elbow = 10
                    defender.NumBroken += 1
                    Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)
                else:
                    OutputLines.append('  '+side[0:1].upper() + side [1::]+ ' elbow was already broken.')
                    OutputLines.append('   Stunned opponent.')
                    defender.Stunned = 3
                    Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

            if side == 'left':
                defender.Arms.LElbow = Elbow
            else:
                defender.Arms.RElbow = Elbow

    return OutputLines
