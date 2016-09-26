import Human
import Grabbing

def Totals (attacker, defender):
    attacker.Head.DMG = attacker.Head.LSkull + attacker.Head.RSkull + attacker.Head.LEyeSocket + attacker.Head.LEye + attacker.Head.REyeSocket + attacker.Head.REye + attacker.Head.Nose + attacker.Head.Jaw
    defender.Head.DMG = defender.Head.LSkull + defender.Head.RSkull + defender.Head.LEyeSocket + defender.Head.LEye + defender.Head.REyeSocket + defender.Head.REye + defender.Head.Nose + defender.Head.Jaw

    attacker.Chest.DMG = attacker.Chest.Breastbone + attacker.Chest.LLRibs + attacker.Chest.RLRibs + attacker.Chest.LURibs + attacker.Chest.LLung + attacker.Chest.RURibs + attacker.Chest.RLung + attacker.Chest.SolarPlexus
    defender.Chest.DMG = defender.Chest.Breastbone + defender.Chest.LLRibs + defender.Chest.RLRibs + defender.Chest.LURibs + defender.Chest.LLung + defender.Chest.RURibs + defender.Chest.RLung + defender.Chest.SolarPlexus

    attacker.Arms.DMG = attacker.Arms.LUArm + attacker.Arms.RUArm + attacker.Arms.LShoulder + attacker.Arms.RShoulder + attacker.Arms.LElbow + attacker.Arms.RElbow + attacker.Arms.LHand + attacker.Arms.RHand
    defender.Arms.DMG = defender.Arms.LUArm + defender.Arms.RUArm + defender.Arms.LShoulder + defender.Arms.RShoulder + defender.Arms.LElbow + defender.Arms.RElbow + defender.Arms.LHand + defender.Arms.RHand

    attacker.Legs.DMG = attacker.Legs.Groin + attacker.Legs.LHip + attacker.Legs.RHip + attacker.Legs.LULeg + attacker.Legs.RULeg + attacker.Legs.LKnee + attacker.Legs.RKnee + attacker.Legs.LLLeg + attacker.Legs.RLLeg + attacker.Legs.LAnkle + attacker.Legs.RAnkle + attacker.Legs.LFoot + attacker.Legs.RFoot + attacker.Legs.LBToe + attacker.Legs.RBToe + attacker.Legs.LToes0 + attacker.Legs.RToes0 + attacker.Legs.LToes1 + attacker.Legs.RToes1
    defender.Legs.DMG = defender.Legs.Groin + defender.Legs.LHip + defender.Legs.RHip + defender.Legs.LULeg + defender.Legs.RULeg + defender.Legs.LKnee + defender.Legs.RKnee + defender.Legs.LLLeg + defender.Legs.RLLeg + defender.Legs.LAnkle + defender.Legs.RAnkle + defender.Legs.LFoot + defender.Legs.RFoot + defender.Legs.LBToe + defender.Legs.RBToe + defender.Legs.LToes0 + defender.Legs.RToes0 + defender.Legs.LToes1 + defender.Legs.RToes1

    attacker.UBDMG = attacker.Head.DMG + attacker.Chest.DMG + attacker.Arms.DMG
    defender.UBDMG = defender.Head.DMG + defender.Chest.DMG + defender.Arms.DMG

    attacker.LBDMG = attacker.Legs.DMG
    defender.LBDMG = defender.Legs.DMG

    attacker.TBDMG = attacker.Head.DMG + attacker.Chest.DMG + attacker.Arms.DMG + attacker.Legs.DMG
    defender.TBDMG = defender.Head.DMG + defender.Chest.DMG + defender.Arms.DMG + defender.Legs.DMG


def ArmCrip (attacker, defender):
    if attacker.Arms.LShoulder == 10 or attacker.Arms.LElbow == 10 or attacker.Arms.LHand > 2:
        attacker.LArmCrip = 10
    else:
        attacker.LArmCrip = 0

    if defender.Arms.LShoulder == 10 or defender.Arms.LElbow == 10 or defender.Arms.LHand > 2:
        defender.LArmCrip = 10
    else:
        defender.LArmCrip = 0
        
    if attacker.Arms.RShoulder == 10 or attacker.Arms.RElbow == 10 or attacker.Arms.RHand > 2:
        attacker.RArmCrip = 10
    else:
        attacker.RArmCrip = 0

    if defender.Arms.RShoulder == 10 or defender.Arms.RElbow == 10 or defender.Arms.RHand > 2:
        defender.RArmCrip = 10
    else:
        defender.RArmCrip = 0


def WinCheck (P1, P2, attacker, defender, run, OutputLines):    
    if defender.NumBroken == 3 or defender.NumPierced == 2 or defender.KO == 10 or defender.Brain == 10 or defender.Yield == 10:
        run = False

        if defender.NumPierced == 2 or defender.Brain == 10:
            OutputLines.append('   '+defender.Name+' died.')
            defender.Stance = 2
        elif defender.NumBroken == 3:
            OutputLines.append('   '+defender.Name+' passed out from the pain.')
            defender.Stance = 2
        elif defender.Yield == 10:
            OutputLines.append('')
            OutputLines.append(defender.Name+' yielded.')
        
        Grabbing.Attacked ('strike', 0, attacker, defender, OutputLines)

        OutputLines.append('')
        OutputLines.append(attacker.Name+' won!')


    if attacker.NumBroken == 3 or attacker.NumPierced == 2 or attacker.KO == 10 or attacker.Brain == 10 or attacker.Yield == 10:
        run = False

        if attacker.NumPierced == 2 or attacker.Brain == 10:
            OutputLines.append('   '+attacker.Name+' died.')
            attacker.Stance = 2
        elif attacker.NumBroken == 3:
            OutputLines.append('   '+attacker.Name+' passed out from the pain.')
            attacker.Stance = 2
        elif attacker.Yield == 10:
            OutputLines.append(attacker.Name+' yielded.')
        
        Grabbing.Attacking ('strike', 0, attacker, defender, OutputLines)

        OutputLines.append('')
        OutputLines.append(defender.Name+' won!')


    return run
