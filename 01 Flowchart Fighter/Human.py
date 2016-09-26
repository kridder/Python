class Human:
    Name = 'Human'
    
    AI = False
    personality0 = 0
    personality1 = 0
    
    Stance = 0
    NumBroken = 0
    NumPierced = 0
    NumBlinded = 0
    KO = 0
    Brain = 0
    Crippled = 0
    Stunned = 0
    RArmCrip = 0
    LArmCrip = 0
    RENerve = 0
    LENerve = 0
    Yield = 0

    UBDMG = 0
    LBDMG = 0
    TBDMG = 0
    
    Hit = 0
    Attacked  = 0
    PastBroken = 0

    Grabbing = 0
    Grabbed = 0

    def __init__(this):
        this.Head = Head()
        this.Chest = Chest()
        this.Arms = Arms()
        this.Legs = Legs()

    def Health1(this):
        HPLines1 = ['NumBroken: '+str(this.NumBroken)]
        HPLines1.append('NumPierced: '+str(this.NumPierced))
        HPLines1.append('NumBlinded: '+str(this.NumBlinded))
        HPLines1.append('K.O.: '+str(this.KO))
        HPLines1.append('Brain: '+str(this.Brain))
        HPLines1.append('Crippled: '+str(this.Crippled))
        HPLines1.append('RArmCrip: '+str(this.RArmCrip))
        HPLines1.append('LArmCrip: '+str(this.LArmCrip))
        HPLines1.append('')
        this.Head.Health(HPLines1)
        HPLines1.append('')
        this.Chest.Health(HPLines1)
        HPLines1.append('')
        HPLines1.append('')
        HPLines1.append('')
        HPLines1.append('Stunned: '+str(this.Stunned))
        HPLines1.append('Stance: '+str(this.Stance))
        HPLines1.append('Grabbing: '+str(this.Grabbing))
        HPLines1.append('Grabbed: '+str(this.Grabbed))
        

        return HPLines1

    def Health2(this):
        HPLines2 = ['']
        this.Arms.Health(HPLines2)
        HPLines2.append('')
        this.Legs.Health(HPLines2)
        HPLines2.append('')
        HPLines2.append('Upper Body Damage: '+str(this.UBDMG))
        HPLines2.append('Lower Body Damage: '+str(this.LBDMG))
        HPLines2.append('Total Damage: '+str(this.TBDMG))
        if this.AI:
            HPLines2.append('')
            HPLines2.append('')
            personality = [0, 0]
            personality[0] = this.personality0
            personality[1] = this.personality1
            HPLines2.append('AI Personality: '+str(personality))

        return HPLines2

class Head:
    LSkull = 0
    RSkull = 0
    LEyeSocket = 0
    LEye = 0
    REyeSocket = 0
    REye = 0
    Nose = 0
    Jaw = 0
    DMG = 0

    def Health(this, HPLines1):
        HPLines1.append('Total Head Damage: '+str(this.DMG))
        HPLines1.append('Left Skull: '+str(this.LSkull))
        HPLines1.append('Right Skull: '+str(this.RSkull))
        HPLines1.append('Left Eye Socket: '+str(this.LEyeSocket))
        HPLines1.append('Left Eye: '+str(this.LEye))
        HPLines1.append('Right Eye Socket: '+str(this.REyeSocket))
        HPLines1.append('Right Eye: '+str(this.REye))
        HPLines1.append('Nose: '+str(this.Nose))
        HPLines1.append('Jaw: '+str(this.Jaw))

class Chest:
    Breastbone = 0
    LLRibs = 0
    RLRibs = 0
    LURibs = 0
    LLung = 0
    RURibs = 0
    RLung = 0
    SolarPlexus = 0
    DMG = 0

    def Health(this, HPLines1):
        HPLines1.append('Total Chest Damage: '+str(this.DMG))
        HPLines1.append('Breastbone: '+str(this.Breastbone))
        HPLines1.append('Left Lower Ribs: '+str(this.LLRibs))
        HPLines1.append('Right Lower Ribs: '+str(this.RLRibs))
        HPLines1.append('Left Upper Ribs: '+str(this.LURibs))
        HPLines1.append('Left Lung: '+str(this.LLung))
        HPLines1.append('Right Upper Ribs: '+str(this.RURibs))
        HPLines1.append('Right Lung: '+str(this.RLung))
        HPLines1.append('Solar Plexus: '+str(this.SolarPlexus))

class Arms:
    LUArm = 0
    RUArm = 0
    LShoulder = 0
    RShoulder = 0
    LElbow = 0
    RElbow = 0
    LHand = 0
    RHand = 0
    DMG = 0

    def Health(this, HPLines2):
        HPLines2.append('Total Arm Damage: '+str(this.DMG))
        HPLines2.append('Left Upper Arm: '+str(this.LUArm))
        HPLines2.append('Right Upper Arm: '+str(this.RUArm))
        HPLines2.append('Left Shoulder: '+str(this.LShoulder))
        HPLines2.append('Right Shoulder: '+str(this.RShoulder))
        HPLines2.append('Left Elbow: '+str(this.LElbow))
        HPLines2.append('Right Elbow: '+str(this.RElbow))
        HPLines2.append('Left Hand: '+str(this.LHand))
        HPLines2.append('Right Hand: '+str(this.RHand))

class Legs:
    Groin = 0
    LHip = 0
    RHip = 0
    LULeg = 0
    RULeg = 0
    LKnee = 0
    RKnee = 0
    LLLeg = 0
    RLLeg = 0
    LAnkle = 0
    RAnkle = 0
    LFoot = 0
    RFoot = 0
    LBToe = 0
    RBToe = 0
    LToes0 = 0
    RToes0 = 0
    LToes1 = 0
    RToes1 = 0
    DMG = 0

    def Health(this, HPLines2):
        HPLines2.append('Total Leg Damage: '+str(this.DMG))
        HPLines2.append('Groin: '+str(this.Groin))
        HPLines2.append('Left Hip: '+str(this.LHip))
        HPLines2.append('Right Hip: '+str(this.RHip))
        HPLines2.append('Left Upper Leg: '+str(this.LULeg))
        HPLines2.append('Right Upper Leg: '+str(this.RULeg))
        HPLines2.append('Left Knee: '+str(this.LKnee))
        HPLines2.append('Right Knee: '+str(this.RKnee))
        HPLines2.append('Left Lower Leg: '+str(this.LLLeg))
        HPLines2.append('Right Lower Leg: '+str(this.RLLeg))
        HPLines2.append('Left Ankle: '+str(this.LAnkle))
        HPLines2.append('Right Ankle: '+str(this.RAnkle))
        HPLines2.append('Left Foot: '+str(this.LFoot))
        HPLines2.append('Right Foot: '+str(this.RFoot))
        HPLines2.append('Left Big Toe: '+str(this.LBToe))
        HPLines2.append('Right Big Toe: '+str(this.RBToe))
        HPLines2.append('Left Toes: '+str(this.LToes0)+' '+str(this.LToes1))
        HPLines2.append('Right Toes: '+str(this.RToes0)+' '+str(this.RToes1))
        
