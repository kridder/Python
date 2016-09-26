import ECard
import ICard

def Calc(EC, ec, P1A, P2A, AEA):
    EBonus = 0
    
    if EC[ec].Abbility == 'Layered':
        PA = P1A + P2A
        for (pa, line) in enumerate(PA):
            if PA[pa].Type == 'Blunt':
                EBonus += 1
                break

    if EC[ec].Abbility == 'Plated':
        PA = P1A + P2A
        for (pa, line) in enumerate(PA):
            if PA[pa].Type == 'Sharp':
                EBonus += 1
                break

    if EC[ec].Abbility == 'Lurk':
        PA = P1A + P2A
        for (ec2, line) in enumerate(EC):
            if EC[ec2].Type == 'Infected':
                EBonus += 1

    for (aea, line) in enumerate(AEA):
        if AEA[aea] == 'Inspire':
            if EC[ec].Type == 'Infected':
                EBonus += 1


    return EBonus

def CheckPen(AEA, PA, pa):
    PCheckPen = 0

    for (aea, line) in enumerate(AEA):
        if AEA[aea] == 'Armour':
            if PA[pa].CheckType == 'Ammo':
                PCheckPen = 1
            
        if AEA[aea] == 'Thick Skinned':
            if PA[pa].CheckType == 'Durability':
                PCheckPen = 1


    return PCheckPen
