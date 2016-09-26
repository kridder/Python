import random
import Grabbing

Limit = lambda x: max(1, min(6, x))

def Kneehead (skip, HITpenalty, DMGpenalty, attacker, defender, side, OutputLines):
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
            if side == 'left':
                Knee = attacker.Legs.LKnee
            else:
                Knee = attacker.Legs.RKnee

            if Knee < 9:
                OutputLines.append('  Bruised own '+side+' knee.')
                Knee += 1
            else:
                OutputLines.append('  Broke own '+side+' knee, you fell down.')
                Knee = 10
                attacker.NumBroken += 1
                attacker.Crippled = 10
                attacker.Stance = 2
                attacker.Stunned += 2
                Grabbing.Attacking ('kick', 2, attacker, defender, OutputLines)

            if side == 'left':
                attacker.Legs.LKnee = Knee
            else:
                attacker.Legs.RKnee = Knee
                                    
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
                OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                defender.Brain += 1
                defender.Stance = 2
                defender.Stunned = 3
                Grabbing.Attacked ('kick', 0, attacker, defender, OutputLines)

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
            if side == 'left':
                Knee = attacker.Legs.LKnee
            else:
                Knee = attacker.Legs.RKnee

            if Knee < 9:
                OutputLines.append('  Bruised own '+side+' knee.')
                Knee += 1
            else:
                OutputLines.append('  Broke own '+side+' knee, you fell down.')
                Knee = 10
                attacker.NumBroken += 1
                attacker.Crippled = 10
                attacker.Stance = 2
                attacker.Stunned += 2
                Grabbing.Attacking ('kick', 2, attacker, defender, OutputLines)

            if side == 'left':
                attacker.Legs.LKnee = Knee
            else:
                attacker.Legs.RKnee = Knee
                            
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
                OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                defender.Brain += 1
                defender.Stance = 2
                defender.Stunned = 3
                Grabbing.Attacked ('kick', 0, attacker, defender, OutputLines)

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
            if side == 'left':
                Knee = attacker.Legs.LKnee
            else:
                Knee = attacker.Legs.RKnee

            if Knee < 9:
                OutputLines.append('  Bruised own '+side+' knee.')
                Knee += 1
            else:
                OutputLines.append('  Broke own '+side+' knee, you fell down.')
                Knee = 10
                attacker.NumBroken += 1
                attacker.Crippled = 10
                attacker.Stance = 2
                attacker.Stunned += 2
                Grabbing.Attacking ('kick', 2, attacker, defender, OutputLines)

            if side == 'left':
                attacker.Legs.LKnee = Knee
            else:
                attacker.Legs.RKnee = Knee
                            
        elif d6 < 5 - DamageBonus:
            if defender.Head.LEyeSocket < 10:
                OutputLines.append('  Bruised left eye.')
                defender.Head.LEyeSocket += 1
            else:
                OutputLines.append('  Left eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned += 2
                Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                        
        else:
            if defender.Head.LEyeSocket < 10:
                OutputLines.append('  Broke left eye socket.')
                defender.Head.LEyeSocket = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Left eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

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
            if side == 'left':
                Knee = attacker.Legs.LKnee
            else:
                Knee = attacker.Legs.RKnee

            if Knee < 9:
                OutputLines.append('  Bruised own '+side+' knee.')
                Knee += 1
            else:
                OutputLines.append('  Broke own '+side+' knee, you fell down.')
                Knee = 10
                attacker.NumBroken += 1
                attacker.Crippled = 10
                attacker.Stance = 2
                attacker.Stunned += 2
                Grabbing.Attacking ('kick', 2, attacker, defender, OutputLines)

            if side == 'left':
                attacker.Legs.LKnee = Knee
            else:
                attacker.Legs.RKnee = Knee
                                                
        elif d6 < 5 - DamageBonus:
            if defender.Head.REyeSocket < 10:
                OutputLines.append('  Bruised right eye.')
                defender.Head.REyeSocket += 1
            else:
                OutputLines.append('  Right eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned += 2
                Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
        else:
            if defender.Head.REyeSocket < 10:
                OutputLines.append('  Broke right eye socket.')
                defender.Head.REyeSocket = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Right eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

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
                        
        else:
            if defender.Head.Jaw < 10:
                OutputLines.append('  Broke jaw.')
                defender.Head.Jaw = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Jaw was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

    return OutputLines


def Butthead (skip, HITpenalty, DMGpenalty, attacker, defender, hand, OutputLines):
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

        if d6 < 2:
            OutputLines.append('  You stunned yourself.')
            attacker.Stunned += 2
            Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)
                
        elif d6 < 3:
            if attacker.Head.LSkull < 9:
                OutputLines.append('  Bruised own skull on the left side.')
                attacker.Head.LSkull += 1
            else:
                if attacker.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning yourself.')
                    attacker.Brain += 1
                    attacker.Stunned = 3
                    Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)

                elif attacker.Brain < 2:
                    OutputLines.append('  Caused concussion, you fell down and are stunned.')
                    attacker.Brain += 1
                    attacker.Stance = 2
                    attacker.Stunned = 3
                    Grabbing.Attacking ('kick', 1, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked yourself out.')
                    attacker.Brain += 1
                    attacker.KO = 10
                    Grabbing.Attacking ('strike', 0, attacker, defender, OutputLines)

        elif d6 < 4:
            OutputLines.append('  Stunned opponent')
            defender.Stunned += 2
            Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                                    
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
                OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                defender.Brain += 1
                defender.Stance = 2
                defender.Stunned = 3
                Grabbing.Attacked ('kick', 0, attacker, defender, OutputLines)

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

        if d6 < 2:
            OutputLines.append('  You stunned yourself.')
            attacker.Stunned += 2
            Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)
                
        elif d6 < 3:
            if attacker.Head.RSkull < 9:
                OutputLines.append('  Bruised own skull on the right side.')
                attacker.Head.RSkull += 1
            else:
                if attacker.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning yourself.')
                    attacker.Brain += 1
                    attacker.Stunned = 3
                    Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)

                elif attacker.Brain < 2:
                    OutputLines.append('  Caused concussion, you fell down and are stunned.')
                    attacker.Brain += 1
                    attacker.Stance = 2
                    attacker.Stunned = 3
                    Grabbing.Attacking ('kick', 1, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked yourself out.')
                    attacker.Brain += 1
                    attacker.KO = 10
                    Grabbing.Attacking ('strike', 0, attacker, defender, OutputLines)

        elif d6 < 4:
            OutputLines.append('  Stunned opponent')
            defender.Stunned += 2
            Grabbing.Attacked ('strike', 5, attacker, defender, OutputLines)
                            
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
                OutputLines.append('  Caused concussion, opponent fell down and is stunned.')
                defender.Brain += 1
                defender.Stance = 2
                defender.Stunned = 3
                Grabbing.Attacked ('kick', 0, attacker, defender, OutputLines)

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
            if attacker.Head.LSkull < 9:
                OutputLines.append('  Bruised own skull on the left side.')
                attacker.Head.LSkull += 1
            else:
                if attacker.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning yourself.')
                    attacker.Brain += 1
                    attacker.Stunned = 3
                    Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)

                elif attacker.Brain < 2:
                    OutputLines.append('  Caused concussion, you fell down and are stunned.')
                    attacker.Brain += 1
                    attacker.Stance = 2
                    attacker.Stunned = 3
                    Grabbing.Attacking ('kick', 1, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked yourself out.')
                    attacker.Brain += 1
                    attacker.KO = 10
                    Grabbing.Attacking ('strike', 0, attacker, defender, OutputLines)
                            
        elif d6 < 5 - DamageBonus:
            if defender.Head.LEyeSocket < 10:
                OutputLines.append('  Bruised left eye.')
                defender.Head.LEyeSocket += 1
            else:
                OutputLines.append('  Left eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned += 2
                Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                        
        else:
            if defender.Head.LEyeSocket < 10:
                OutputLines.append('  Broke left eye socket.')
                defender.Head.LEyeSocket = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Left eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

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
            if attacker.Head.RSkull < 9:
                OutputLines.append('  Bruised own skull on the right side.')
                attacker.Head.RSkull += 1
            else:
                if attacker.Brain < 1:
                    OutputLines.append('  Caused concussion, stunning yourself.')
                    attacker.Brain += 1
                    attacker.Stunned = 3
                    Grabbing.Attacking ('strike', 4, attacker, defender, OutputLines)

                elif attacker.Brain < 2:
                    OutputLines.append('  Caused concussion, you fell down and are stunned.')
                    attacker.Brain += 1
                    attacker.Stance = 2
                    attacker.Stunned = 3
                    Grabbing.Attacking ('kick', 1, attacker, defender, OutputLines)

                else:
                    OutputLines.append('  Knocked yourself out.')
                    attacker.Brain += 1
                    attacker.KO = 10
                    Grabbing.Attacking ('strike', 0, attacker, defender, OutputLines)
                                                
        elif d6 < 5 - DamageBonus:
            if defender.Head.REyeSocket < 10:
                OutputLines.append('  Bruised right eye.')
                defender.Head.REyeSocket += 1
            else:
                OutputLines.append('  Right eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned += 2
                Grabbing.Attacked ('strike', 4, attacker, defender, OutputLines)
                    
        else:
            if defender.Head.REyeSocket < 10:
                OutputLines.append('  Broke right eye socket.')
                defender.Head.REyeSocket = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Right eye socket was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

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
                        
        else:
            if defender.Head.Jaw < 10:
                OutputLines.append('  Broke jaw.')
                defender.Head.Jaw = 10
                defender.NumBroken += 1
            else:
                OutputLines.append('  Jaw was already broken.')
                OutputLines.append('   Stunned opponent.')
                defender.Stunned = 3
                Grabbing.Attacked ('strike', 3, attacker, defender, OutputLines)

    return OutputLines
