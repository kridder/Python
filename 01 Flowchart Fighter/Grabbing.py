import random
import Strike
import Kick
import Deviant

Limit = lambda x: max(1, min(6, x))

def Grab (HITpenalty, attacker, defender, OutputLines):

    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 3 and attacker.Grabbed == 0:
        OutputLines.append(attacker.Name+' failed to grab '+defender.Name+'.')
    else:
        OutputLines.append(attacker.Name+' grabbed '+defender.Name+'.')
        attacker.Grabbing = 1
        defender.Grabbed = 1

    return OutputLines

        
def Release (DMGpenalty, attacker, defender, OutputLines):

    if attacker.Grabbed > 0:
        d6 = Limit(random.randint(1, 6) - DMGpenalty)

        if d6 < 5:
            msg1 = ' failed to break the hold of '+defender.Name
            msg2 = ', but he'
        else:
            msg1 = ' broke the hold of '+defender.Name
            msg2 = ' and he'
            defender.Grabbing = 0
            attacker.Grabbed = 0

    else:
        msg1 =''
        msg2 =''
            
    if attacker.Grabbing > 0:
        attacker.Grabbing = 0
        defender.Grabbed = 0
        OutputLines.append(attacker.Name+' released his hold on '+defender.Name+msg2+msg1+'.')
    else:
        OutputLines.append(attacker.Name+msg1+'.')


def Attacked (attmove, chance, attacker, defender, OutputLines):
    if attacker.Grabbed > 0:
        if attmove == 'strike':
            d6 = random.randint(1, 6)
            if d6 > chance:
                defender.Grabbing = 0
                attacker.Grabbed = 0
                OutputLines.append('   Opponent released his hold on you.')
        if attmove == 'kick':
            d6 = random.randint(1, 6)
            if d6 > chance:
                OutputLines.append('   Opponent released his hold on you.')
            else:
                OutputLines.append('   Opponent pulled you down.')
                attacker.Stance = 2
                attacker.Stunned += 2

            defender.Grabbing = 0
            attacker.Grabbed = 0
            attacker.Grabbing = 0
            defender.Grabbed = 0

    elif attmove == 'kick':
        attacker.Grabbing = 0
        defender.Grabbed = 0

    return OutputLines


def Attacking (attmove, chance, attacker, defender, OutputLines):
    if attacker.Grabbing > 0:
        if attmove == 'strike':
            d6 = random.randint(1, 6)
            if d6 > chance:
                defender.Grabbed = 0
                attacker.Grabbing = 0
                OutputLines.append('   You released your hold on your opponent.')
        if attmove == 'kick':
            d6 = random.randint(1, 6)
            if d6 > chance:
                OutputLines.append('   You released your hold on your opponent.')
            else:
                OutputLines.append('   You pulled your opponent down.')
                defnder.Stance = 2
                defender.Stunned += 2

            defender.Grabbing = 0
            attacker.Grabbed = 0
            attacker.Grabbing = 0
            defender.Grabbed = 0

    elif attmove == 'kick':
        attacker.Grabbed = 0
        defender.Grabbing = 0

    return OutputLines

                
def Knee (HITpenalty, DMGpenalty, attacker, defender, side, OutputLines):
    OutputLines.append('')
    OutputLines.append('Pull down and knee with '+side+' knee.')
    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 4:
        OutputLines.append(' Failed to pull down head of opponent.')
        OutputLines.append('')
        d6 = random.randint(1, 6)
        
        if d6 < 2:
            DMGpenalty += 1
            return Kick.UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'left', OutputLines)
        elif d6 < 3:
            DMGpenalty += 1
            return Kick.UpperLeg(True, HITpenalty, DMGpenalty, attacker, defender, 'right', OutputLines)
        elif d6 < 5:
            return Strike.Belly(True, HITpenalty, DMGpenalty, attacker, defender, 0, OutputLines)
        else:
            return Kick.Groin(True, HITpenalty, DMGpenalty, attacker, defender, OutputLines)
        

    else:
        OutputLines.append(' Pulled down head of opponent.')
        OutputLines.append('')
        d6 = random.randint(1, 6)

        if d6 < 2:
            DMGpenalty -= 1
            return Strike.Belly(True, HITpenalty, DMGpenalty, attacker, defender, 0, OutputLines)
        elif d6 < 5:
            return Strike.Chest(True, HITpenalty, DMGpenalty, attacker, defender, 0, OutputLines)
        else:
            return Deviant.Kneehead(True, HITpenalty, DMGpenalty, attacker, defender, side, OutputLines)
            
    return OutputLines


def Headbutt (HITpenalty, DMGpenalty, attacker, defender, OutputLines):
    OutputLines.append('')
    OutputLines.append('Headbutt to head.')
    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 3:
        OutputLines.append(' Missed.')
    else:
        return Deviant.Butthead(True, HITpenalty, DMGpenalty, attacker, defender, 0, OutputLines)

    return OutputLines


def Legthrow (HITpenalty, DMGpenalty, attacker, defender, OutputLines):
    OutputLines.append('')
    OutputLines.append('Leg throw.')
    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 5:
        OutputLines.append(' Failed to throw opponent.')
        d6 = random.randint(1, 6)

        if d6 < 2:
            OutputLines.append('  You fell down.')
            attacker.Stance = 2
            attacker.Stunned += 1
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        elif d6 < 4:
            OutputLines.append('  You fell and pulled your opponent down.')
            attacker.Stance = 2
            attacker.Stunned += 2
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            OutputLines.append('  Nothing happened.')


    else:
        OutputLines.append(' You throw your opponent.')
        d6 = random.randint(1, 6)

        if d6 < 2:
            OutputLines.append('  Opponent fell and pulled you down.')
            attacker.Stance = 2
            attacker.Stunned += 1
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        elif d6 < 6:
            OutputLines.append('  Opponent fell down.')
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            OutputLines.append('  Opponent fell down and is stunned.')
            defender.Stance = 2
            defender.Stunned = 3
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

    return OutputLines
            

def Hipthrow (HITpenalty, DMGpenalty, attacker, defender, OutputLines):
    OutputLines.append('')
    OutputLines.append('Hip throw.')
    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 5:
        OutputLines.append(' Failed to throw opponent.')
        d6 = random.randint(1, 6)

        if d6 < 4:
            OutputLines.append('  You fell and pulled your opponent down.')
            attacker.Stance = 2
            attacker.Stunned += 2
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            OutputLines.append('  Nothing happened.')


    else:
        OutputLines.append(' You throw your opponent.')
        d6 = random.randint(1, 6)

        if d6 < 3:
            OutputLines.append('  Opponent fell and pulled you down.')
            attacker.Stance = 2
            attacker.Stunned += 1
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        elif d6 < 5:
            OutputLines.append('  Opponent fell down.')
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            OutputLines.append('  Opponent fell down and is stunned.')
            defender.Stance = 2
            defender.Stunned = 3
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

    return OutputLines


def Bearhug (HITpenalty, DMGpenalty, attacker, defender, OutputLines):
    OutputLines.append('')
    OutputLines.append('Bear hug.')
    d6 = Limit(random.randint(1, 6) - HITpenalty)

    if d6 < 6:
        OutputLines.append(' Failed to throw opponent.')
        d6 = random.randint(1, 6)

        if d6 < 3:
            OutputLines.append('  You fell down.')
            attacker.Stance = 2
            attacker.Stunned += 1
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        elif d6 < 6:
            OutputLines.append('  You fell and pulled your opponent down.')
            attacker.Stance = 2
            attacker.Stunned += 2
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            OutputLines.append('  Nothing happened.')


    else:
        OutputLines.append(' You throw your opponent.')
        d6 = random.randint(1, 6)

        if d6 < 3:
            OutputLines.append('  Opponent fell down.')
            defender.Stance = 2
            defender.Stunned += 2
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        elif d6 < 6:
            OutputLines.append('  Opponent fell down and is stunned.')
            defender.Stance = 2
            defender.Stunned = 3
            attacker.Grabbing = 0
            defender.Grabbed = 0
            defender.Grabbing = 0
            attacker.Grabbed = 0

        else:
            d6 = random.randint(1, 6)

            if d6 < 2:
                if defender.Chest.LLRibs < 10:
                    OutputLines.append('  Opponent fell down and broke his left lower ribs.')
                    defender.Chest.LLRibs = 10
                    defender.NumBroken += 1
                    defender.Stance = 2
                    defender.Stunned += 2
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0
                else:
                    OutputLines.append('  Opponent fell down on his broken left lower ribs.')
                    defender.Stance = 2
                    defender.Stunned = 3
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0

            elif d6 < 4:
                if defender.Chest.LURibs < 10:
                    OutputLines.append('  Opponent fell down and broke his left upper ribs.')
                    defender.Chest.LURibs = 10
                    defender.NumBroken += 1
                    defender.Stance = 2
                    defender.Stunned += 2
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0
                else:
                    OutputLines.append('  Opponent fell down on his broken upper ribs.')
                    defender.Stance = 2
                    defender.Stunned = 3
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0

            elif d6 < 5:
                if defender.Arms.LShoulder < 10:
                    OutputLines.append('  Opponent fell down and dislocated his left shoulder.')
                    defender.Arms.LShoulder = 10
                    defender.Stance = 2
                    defender.Stunned += 2
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0
                    
                else:
                    OutputLines.append('  Opponent fell down on his dislocated left shoulder.')
                    defender.Stance = 2
                    defender.Stunned = 3
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0

            elif d6 < 6:
                if defender.Arms.LElbow < 10:
                    OutputLines.append('  Opponent fell down and broke his left elbow.')
                    defender.Arms.LElbow = 10
                    defender.NumBroken += 1
                    defender.Stance = 2
                    defender.Stunned += 2
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0
                    
                else:
                    OutputLines.append('  Opponent fell down on his broken left elbow.')
                    defender.Stance = 2
                    defender.Stunned = 3
                    attacker.Grabbing = 0
                    defender.Grabbed = 0
                    defender.Grabbing = 0
                    attacker.Grabbed = 0

            else:
                OutputLines.append('  Opponent fell down and broke the left side of his skull.')
                defender.Head.LSkull = 10
                defender.NumBroken += 1
                defender.Brain = 10
                defender.Stance = 2
                defender.Stunned += 2
                attacker.Grabbing = 0
                defender.Grabbed = 0
                defender.Grabbing = 0
                attacker.Grabbed = 0

    return OutputLines
