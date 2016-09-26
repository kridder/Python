import ECard

def Init():

    E = [0]

    E[0] = ECard.ECard()

    E.append (ECard.ECard())
    E[1].ID = 'E001'
    E[1].Name = 'Afflicted Mongrel'
    E[1].Type = 'Infected'
    E[1].Size = 'Small'
    E[1].Level = 1
    E[1].Abbility = 'Sense'
    E[1].Text1 = 'Players are detected'
    E[1].Text2 = 'and general combat'
    E[1].Text3 = 'ensues immediatly.'
    E[1].Text4 = ''
    E[1].Text5 = ''
    E[1].Text6 = ''
    E[1].Frequency = 4 #4
    
    E.append (ECard.ECard())
    E[2].ID = 'E002'
    E[2].Name = 'Scrawny Afflicted'
    E[2].Type = 'Infected'
    E[2].Size = 'Medium'
    E[2].Level = 2
    E[2].Abbility = ''
    E[2].Text1 = ''
    E[2].Text2 = ''
    E[2].Text3 = ''
    E[2].Text4 = ''
    E[2].Text5 = ''
    E[2].Text6 = ''
    E[2].Frequency = 9 #9

    E.append (ECard.ECard())
    E[3].ID = 'E003'
    E[3].Name = 'Afflicted Victim'
    E[3].Type = 'Infected'
    E[3].Size = 'Medium'
    E[3].Level = 3
    E[3].Abbility = ''
    E[3].Text1 = ''
    E[3].Text2 = ''
    E[3].Text3 = ''
    E[3].Text4 = ''
    E[3].Text5 = ''
    E[3].Text6 = ''
    E[3].Frequency = 11 #11

    E.append (ECard.ECard())
    E[4].ID = 'E004'
    E[4].Name = 'Big Boned Afflicted'
    E[4].Type = 'Infected'
    E[4].Size = 'Medium'
    E[4].Level = 3
    E[4].Abbility = 'Layered'
    E[4].Text1 = '+1 to self when blunt'
    E[4].Text2 = 'weapons are used in'
    E[4].Text3 = 'this fight.'
    E[4].Text4 = ''
    E[4].Text5 = ''
    E[4].Text6 = ''
    E[4].Frequency = 4 #4

    E.append (ECard.ECard())
    E[5].ID = 'E005'
    E[5].Name = 'Afflicted Brute'
    E[5].Type = 'Mutant'
    E[5].Size = 'Large'
    E[5].Level = 4
    E[5].Abbility = ''
    E[5].Text1 = ''
    E[5].Text2 = ''
    E[5].Text3 = ''
    E[5].Text4 = ''
    E[5].Text5 = ''
    E[5].Text6 = ''
    E[5].Frequency = 4 #4

    E.append (ECard.ECard())
    E[6].ID = 'E006'
    E[6].Name = 'Afflicted Home Guard'
    E[6].Type = 'Infected'
    E[6].Size = 'Medium'
    E[6].Level = 3
    E[6].Abbility = 'Armour'
    E[6].Text1 = '-1 on ammo rolls for'
    E[6].Text2 = 'all weapons used in'
    E[6].Text3 = 'this fight.'
    E[6].Text4 = ''
    E[6].Text5 = ''
    E[6].Text6 = ''
    E[6].Frequency = 2 #2
    
    E.append (ECard.ECard())
    E[7].ID = 'E007'
    E[7].Name = 'Scabby Afflicted'
    E[7].Type = 'Mutant'
    E[7].Size = 'Medium'
    E[7].Level = 2
    E[7].Abbility = 'Plated'
    E[7].Text1 = '+1 to self when sharp'
    E[7].Text2 = 'weapons are used in'
    E[7].Text3 = 'this fight.'
    E[7].Text4 = ''
    E[7].Text5 = ''
    E[7].Text6 = ''
    E[7].Frequency = 4 #4

    E.append (ECard.ECard())
    E[8].ID = 'E008'
    E[8].Name = 'Afflicted Breaker'
    E[8].Type = 'Mutant'
    E[8].Size = 'Medium'
    E[8].Level = 3
    E[8].Abbility = 'Thick Skinned'
    E[8].Text1 = '-1 on durability rolls'
    E[8].Text2 = 'for all weapons used'
    E[8].Text3 = 'in this fight.'
    E[8].Text4 = ''
    E[8].Text5 = ''
    E[8].Text6 = ''
    E[8].Frequency = 2 #2

    E.append (ECard.ECard())
    E[9].ID = 'E009'
    E[9].Name = 'Afflicted Scientist'
    E[9].Type = 'Mutant'
    E[9].Size = 'Medium'
    E[9].Level = 2
    E[9].Abbility = 'Lurk'
    E[9].Text1 = '+1 to self for each'
    E[9].Text2 = 'infected in combat.'
    E[9].Text3 = ''
    E[9].Text4 = ''
    E[9].Text5 = ''
    E[9].Text6 = ''
    E[9].Frequency = 2 #2

    E.append (ECard.ECard())
    E[10].ID = 'E010'
    E[10].Name = 'Afflicted Commander'
    E[10].Type = 'Mutant'
    E[10].Size = 'Medium'
    E[10].Level = 3
    E[10].Abbility = 'Inspire'
    E[10].Text1 = '+1 to each infected'
    E[10].Text2 = 'in combat.'
    E[10].Text3 = ''
    E[10].Text4 = ''
    E[10].Text5 = ''
    E[10].Text6 = ''
    E[10].Frequency = 1 #1

    E.append (ECard.ECard())
    E[11].ID = 'E011'
    E[11].Name = 'Flatulent Afflicted'
    E[11].Type = 'Mutant'
    E[11].Size = 'Medium'
    E[11].Level = 2
    E[11].Abbility = 'Shroud'
    E[11].Text1 = 'Draw next enemy card'
    E[11].Text2 = 'face down. Reveal'
    E[11].Text3 = 'when combat begins.'
    E[11].Text4 = ''
    E[11].Text5 = ''
    E[11].Text6 = ''
    E[11].Frequency = 3 #3

    E.append (ECard.ECard())
    E[12].ID = 'E012'
    E[12].Name = 'Afflicted Alley Cat'
    E[12].Type = 'Infected'
    E[12].Size = 'Small'
    E[12].Level = 1
    E[12].Abbility = 'Stalk'
    E[12].Text1 = 'Fights player who'
    E[12].Text2 = 'entered last one on'
    E[12].Text3 = 'one. Afterwards roll'
    E[12].Text4 = 'a D6, if 1-3 general'
    E[12].Text5 = 'combat ensues'
    E[12].Text6 = 'instantly.'
    E[12].Frequency = 0 #0

    E.append (ECard.ECard())
    E[13].ID = 'E013'
    E[13].Name = 'Afflicted K9'
    E[13].Type = 'Infected'
    E[13].Size = 'Small'
    E[13].Level = 3
    E[13].Abbility = 'Ambush'
    E[13].Text1 = 'Fights player who'
    E[13].Text2 = 'entered first one on'
    E[13].Text3 = 'one. Afterwards'
    E[13].Text4 = 'general combat'
    E[13].Text5 = 'ensues instantly.'
    E[13].Text6 = ''
    E[13].Frequency = 0 #0

    E.append (ECard.ECard())
    E[14].ID = 'E014'
    E[14].Name = 'Afflicted Pitcher'
    E[14].Type = 'Infected'
    E[14].Size = 'Medium'
    E[14].Level = 2
    E[14].Abbility = 'Ranged'
    E[14].Text1 = '-1 level on all melee'
    E[14].Text2 = ' weapons used in'
    E[14].Text3 = 'this fight.'
    E[14].Text4 = ''
    E[14].Text5 = ''
    E[14].Text6 = ''
    E[14].Frequency = 0 #0

    E.append (ECard.ECard())
    E[15].ID = 'E015'
    E[15].Name = 'Afflicted K9'
    E[15].Type = 'Infected'
    E[15].Size = 'Small'
    E[15].Level = 3
    E[15].Abbility = 'Sense'
    E[15].Text1 = 'Players are detected'
    E[15].Text2 = 'and general combat'
    E[15].Text3 = 'ensues immediatly.'
    E[15].Text4 = ''
    E[15].Text5 = ''
    E[15].Text6 = ''
    E[15].Frequency = 2 #2
   
    #E.append (ECard.ECard())
    #E[X].ID = 'E00X'
    #E[X].Name = 'Afflicted'
    #E[X].Type = ''
    #E[X].Size = ''
    #E[X].Level = 0
    #E[X].Abbility = ''
    #E[X].Text1 = ''
    #E[X].Text2 = ''
    #E[X].Text3 = ''
    #E[X].Text4 = ''
    #E[X].Text5 = ''
    #E[X].Text6 = ''
    #E[X].Frequency = 0 #0

    return E
