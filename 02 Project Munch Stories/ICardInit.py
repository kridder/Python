import ICard

def Init():

    I = [0]

    I[0] = ICard.ICard()

    I.append (ICard.ICard())
    I[1].ID = 'I001'
    I[1].Name = 'Revolver'
    I[1].Range = 'Ranged'
    I[1].Type = 'Gun'
    I[1].Size = 'Small'
    I[1].Bonus = 3
    I[1].CheckType = 'Ammo'
    I[1].CheckVal = 6
    I[1].Text1 = ''
    I[1].Text2 = ''
    I[1].Text3 = ''
    I[1].Text4 = ''
    I[1].Frequency = 4 #4

    I.append (ICard.ICard())
    I[2].ID = 'I002'
    I[2].Name = 'Handgun'
    I[2].Range = 'Ranged'
    I[2].Type = 'Gun'
    I[2].Size = 'Small'
    I[2].Bonus = 3
    I[2].CheckType = 'Ammo'
    I[2].CheckVal = 5
    I[2].Text1 = ''
    I[2].Text2 = ''
    I[2].Text3 = ''
    I[2].Text4 = ''
    I[2].Frequency = 5 #5

    I.append (ICard.ICard())
    I[3].ID = 'I003'
    I[3].Name = 'Rifle'
    I[3].Range = 'Ranged'
    I[3].Type = 'Gun'
    I[3].Size = 'Large'
    I[3].Bonus = 4
    I[3].CheckType = 'Ammo'
    I[3].CheckVal = 5
    I[3].Text1 = ''
    I[3].Text2 = ''
    I[3].Text3 = ''
    I[3].Text4 = ''
    I[3].Frequency = 3 #3

    I.append (ICard.ICard())
    I[4].ID = 'I004'
    I[4].Name = 'Sawn-off Shotgun'
    I[4].Range = 'Ranged'
    I[4].Type = 'Gun'
    I[4].Size = 'Small'
    I[4].Bonus = 4
    I[4].CheckType = 'Ammo'
    I[4].CheckVal = 6
    I[4].Text1 = ''
    I[4].Text2 = ''
    I[4].Text3 = ''
    I[4].Text4 = ''
    I[4].Frequency = 1 #1

    I.append (ICard.ICard())
    I[5].ID = 'I005'
    I[5].Name = 'Magnum'
    I[5].Range = 'Ranged'
    I[5].Type = 'Gun'
    I[5].Size = 'Small'
    I[5].Bonus = 5
    I[5].CheckType = 'Ammo'
    I[5].CheckVal = 6
    I[5].Text1 = ''
    I[5].Text2 = ''
    I[5].Text3 = ''
    I[5].Text4 = ''
    I[5].Frequency = 2 #2

    I.append (ICard.ICard())
    I[6].ID = 'I006'
    I[6].Name = 'Shotgun'
    I[6].Range = 'Ranged'
    I[6].Type = 'Gun'
    I[6].Size = 'Large'
    I[6].Bonus = 5
    I[6].CheckType = 'Ammo'
    I[6].CheckVal = 5
    I[6].Text1 = ''
    I[6].Text2 = ''
    I[6].Text3 = ''
    I[6].Text4 = ''
    I[6].Frequency = 4 #4

    I.append (ICard.ICard())
    I[7].ID = 'I007'
    I[7].Name = 'Submachine Gun'
    I[7].Range = 'Ranged'
    I[7].Type = 'Gun'
    I[7].Size = 'Small'
    I[7].Bonus = 5
    I[7].CheckType = 'Ammo'
    I[7].CheckVal = 4
    I[7].Text1 = ''
    I[7].Text2 = ''
    I[7].Text3 = ''
    I[7].Text4 = ''
    I[7].Frequency = 2 #2

    I.append (ICard.ICard())
    I[8].ID = 'I008'
    I[8].Name = 'Assault Rifle'
    I[8].Range = 'Ranged'
    I[8].Type = 'Gun'
    I[8].Size = 'Large'
    I[8].Bonus = 7
    I[8].CheckType = 'Ammo'
    I[8].CheckVal = 4
    I[8].Text1 = ''
    I[8].Text2 = ''
    I[8].Text3 = ''
    I[8].Text4 = ''
    I[8].Frequency = 1 #1

    I.append (ICard.ICard())
    I[9].ID = 'I009'
    I[9].Name = 'Flame Thrower'
    I[9].Range = 'Ranged'
    I[9].Type = 'Special'
    I[9].Size = 'Large'
    I[9].Bonus = 12
    I[9].CheckType = 'Fuel'
    I[9].CheckVal = 6
    I[9].Text1 = ''
    I[9].Text2 = ''
    I[9].Text3 = ''
    I[9].Text4 = ''
    I[9].Frequency = 1 #1

    I.append (ICard.ICard())
    I[10].ID = 'I010'
    I[10].Name = 'Kitchen Knife'
    I[10].Range = 'Melee'
    I[10].Type = 'Sharp'
    I[10].Size = 'Small'
    I[10].Bonus = 1
    I[10].CheckType = 'Durability'
    I[10].CheckVal = 3
    I[10].Text1 = ''
    I[10].Text2 = ''
    I[10].Text3 = ''
    I[10].Text4 = ''
    I[10].Frequency = 9 #9

    I.append (ICard.ICard())
    I[11].ID = 'I011'
    I[11].Name = 'Broom Handle'
    I[11].Range = 'Melee'
    I[11].Type = 'Blunt'
    I[11].Size = 'Large'
    I[11].Bonus = 1
    I[11].CheckType = 'Durability'
    I[11].CheckVal = 4
    I[11].Text1 = ''
    I[11].Text2 = ''
    I[11].Text3 = ''
    I[11].Text4 = ''
    I[11].Frequency = 9 #9

    I.append (ICard.ICard())
    I[12].ID = 'I012'
    I[12].Name = 'Night Stick'
    I[12].Range = 'Melee'
    I[12].Type = 'Blunt'
    I[12].Size = 'Medium'
    I[12].Bonus = 2
    I[12].CheckType = 'Durability'
    I[12].CheckVal = 3
    I[12].Text1 = ''
    I[12].Text2 = ''
    I[12].Text3 = ''
    I[12].Text4 = ''
    I[12].Frequency = 1 #1

    I.append (ICard.ICard())
    I[13].ID = 'I013'
    I[13].Name = 'Kukri'
    I[13].Range = 'Melee'
    I[13].Type = 'Sharp'
    I[13].Size = 'Small'
    I[13].Bonus = 3
    I[13].CheckType = 'Durability'
    I[13].CheckVal = 2
    I[13].Text1 = ''
    I[13].Text2 = ''
    I[13].Text3 = ''
    I[13].Text4 = ''
    I[13].Frequency = 1 #1

    I.append (ICard.ICard())
    I[14].ID = 'I014'
    I[14].Name = 'Sabre'
    I[14].Range = 'Melee'
    I[14].Type = 'Sharp'
    I[14].Size = 'Medium'
    I[14].Bonus = 4
    I[14].CheckType = 'Durability'
    I[14].CheckVal = 2
    I[14].Text1 = ''
    I[14].Text2 = ''
    I[14].Text3 = ''
    I[14].Text4 = ''
    I[14].Frequency = 2 #2

    I.append (ICard.ICard())
    I[15].ID = 'I015'
    I[15].Name = 'Longsword'
    I[15].Range = 'Melee'
    I[15].Type = 'Sharp'
    I[15].Size = 'Medium'
    I[15].Bonus = 5
    I[15].CheckType = 'Durability'
    I[15].CheckVal = 2
    I[15].Text1 = ''
    I[15].Text2 = ''
    I[15].Text3 = ''
    I[15].Text4 = ''
    I[15].Frequency = 1 #1

    I.append (ICard.ICard())
    I[16].ID = 'I016'
    I[16].Name = 'Ice Hockey Stick'
    I[16].Range = 'Melee'
    I[16].Type = 'Blunt'
    I[16].Size = 'Large'
    I[16].Bonus = 2
    I[16].CheckType = 'Durability'
    I[16].CheckVal = 5
    I[16].Text1 = ''
    I[16].Text2 = ''
    I[16].Text3 = ''
    I[16].Text4 = ''
    I[16].Frequency = 5 #5

    I.append (ICard.ICard())
    I[17].ID = 'I017'
    I[17].Name = 'Baseball Bat'
    I[17].Range = 'Melee'
    I[17].Type = 'Blunt'
    I[17].Size = 'Medium'
    I[17].Bonus = 3
    I[17].CheckType = 'Durability'
    I[17].CheckVal = 3
    I[17].Text1 = ''
    I[17].Text2 = ''
    I[17].Text3 = ''
    I[17].Text4 = ''
    I[17].Frequency = 3 #3

    I.append (ICard.ICard())
    I[18].ID = 'I018'
    I[18].Name = 'Brick'
    I[18].Range = 'Melee'
    I[18].Type = 'Blunt'
    I[18].Size = 'Small'
    I[18].Bonus = 1
    I[18].CheckType = 'Durability'
    I[18].CheckVal = 2
    I[18].Text1 = ''
    I[18].Text2 = ''
    I[18].Text3 = ''
    I[18].Text4 = ''
    I[18].Frequency = 4 #4

    I.append (ICard.ICard())
    I[19].ID = 'I019'
    I[19].Name = 'Bowie Knife'
    I[19].Range = 'Melee'
    I[19].Type = 'Sharp'
    I[19].Size = 'Small'
    I[19].Bonus = 2
    I[19].CheckType = 'Durability'
    I[19].CheckVal = 2
    I[19].Text1 = ''
    I[19].Text2 = ''
    I[19].Text3 = ''
    I[19].Text4 = ''
    I[19].Frequency = 4 #4

    I.append (ICard.ICard())
    I[20].ID = 'I020'
    I[20].Name = 'Pitch Fork'
    I[20].Range = 'Melee'
    I[20].Type = 'Sharp'
    I[20].Size = 'Large'
    I[20].Bonus = 2
    I[20].CheckType = 'Durability'
    I[20].CheckVal = 4
    I[20].Text1 = ''
    I[20].Text2 = ''
    I[20].Text3 = ''
    I[20].Text4 = ''
    I[20].Frequency = 1 #1

    I.append (ICard.ICard())
    I[21].ID = 'I021'
    I[21].Name = 'Battle-axe'
    I[21].Range = 'Melee'
    I[21].Type = 'Sharp'
    I[21].Size = 'Large'
    I[21].Bonus = 6
    I[21].CheckType = 'Durability'
    I[21].CheckVal = 3
    I[21].Text1 = ''
    I[21].Text2 = ''
    I[21].Text3 = ''
    I[21].Text4 = ''
    I[21].Frequency = 1 #1

    I.append (ICard.ICard())
    I[22].ID = 'I022'
    I[22].Name = 'Axe'
    I[22].Range = 'Melee'
    I[22].Type = 'Sharp'
    I[22].Size = 'Medium'
    I[22].Bonus = 4
    I[22].CheckType = 'Durability'
    I[22].CheckVal = 3
    I[22].Text1 = ''
    I[22].Text2 = ''
    I[22].Text3 = ''
    I[22].Text4 = ''
    I[22].Frequency = 2 #2

    I.append (ICard.ICard())
    I[23].ID = 'I023'
    I[23].Name = 'Hatchet'
    I[23].Range = 'Melee'
    I[23].Type = 'Sharp'
    I[23].Size = 'Small'
    I[23].Bonus = 2
    I[23].CheckType = 'Durability'
    I[23].CheckVal = 3
    I[23].Text1 = ''
    I[23].Text2 = ''
    I[23].Text3 = ''
    I[23].Text4 = ''
    I[23].Frequency = 3 #3

    I.append (ICard.ICard())
    I[24].ID = 'I024'
    I[24].Name = 'Coat Hanger'
    I[24].Range = 'Melee'
    I[24].Type = 'Sharp'
    I[24].Size = 'Small'
    I[24].Bonus = 1
    I[24].CheckType = 'Durability'
    I[24].CheckVal = 5
    I[24].Text1 = ''
    I[24].Text2 = ''
    I[24].Text3 = ''
    I[24].Text4 = ''
    I[24].Frequency = 6 #6

    I.append (ICard.ICard())
    I[25].ID = 'I025'
    I[25].Name = 'Screwdriver'
    I[25].Range = 'Melee'
    I[25].Type = 'Sharp'
    I[25].Size = 'Small'
    I[25].Bonus = 1
    I[25].CheckType = 'Durability'
    I[25].CheckVal = 3
    I[25].Text1 = ''
    I[25].Text2 = ''
    I[25].Text3 = ''
    I[25].Text4 = ''
    I[25].Frequency = 3 #3

    I.append (ICard.ICard())
    I[26].ID = 'I026'
    I[26].Name = 'Claw Hammer'
    I[26].Range = 'Melee'
    I[26].Type = 'Blunt'
    I[26].Size = 'Small'
    I[26].Bonus = 1
    I[26].CheckType = 'Durability'
    I[26].CheckVal = 3
    I[26].Text1 = ''
    I[26].Text2 = ''
    I[26].Text3 = ''
    I[26].Text4 = ''
    I[26].Frequency = 3 #3

    I.append (ICard.ICard())
    I[27].ID = 'I027'
    I[27].Name = 'Mallet'
    I[27].Range = 'Melee'
    I[27].Type = 'Blunt'
    I[27].Size = 'Medium'
    I[27].Bonus = 3
    I[27].CheckType = 'Durability'
    I[27].CheckVal = 3
    I[27].Text1 = ''
    I[27].Text2 = ''
    I[27].Text3 = ''
    I[27].Text4 = ''
    I[27].Frequency = 3 #3

    I.append (ICard.ICard())
    I[28].ID = 'I028'
    I[28].Name = 'Maul'
    I[28].Range = 'Melee'
    I[28].Type = 'Blunt'
    I[28].Size = 'Large'
    I[28].Bonus = 5
    I[28].CheckType = 'Durability'
    I[28].CheckVal = 3
    I[28].Text1 = ''
    I[28].Text2 = ''
    I[28].Text3 = ''
    I[28].Text4 = ''
    I[28].Frequency = 2 #2

    I.append (ICard.ICard())
    I[29].ID = 'I029'
    I[29].Name = 'Chainsaw'
    I[29].Range = 'Melee'
    I[29].Type = 'Sharp'
    I[29].Size = 'Medium'
    I[29].Bonus = 8
    I[29].CheckType = 'Fuel'
    I[29].CheckVal = 5
    I[29].Text1 = ''
    I[29].Text2 = ''
    I[29].Text3 = ''
    I[29].Text4 = ''
    I[29].Frequency = 2 #2

    I.append (ICard.ICard())
    I[30].ID = 'I030'
    I[30].Name = 'Crutch'
    I[30].Range = 'Melee'
    I[30].Type = 'Blunt'
    I[30].Size = 'Large'
    I[30].Bonus = 1
    I[30].CheckType = 'Durability'
    I[30].CheckVal = 3
    I[30].Text1 = ''
    I[30].Text2 = ''
    I[30].Text3 = ''
    I[30].Text4 = ''
    I[30].Frequency = 4 #4

    I.append (ICard.ICard())
    I[31].ID = 'I031'
    I[31].Name = 'Flintlock Pistol'
    I[31].Range = 'Melee'
    I[31].Type = 'Blunt'
    I[31].Size = 'Small'
    I[31].Bonus = 3
    I[31].CheckType = 'Durability'
    I[31].CheckVal = 2
    I[31].Text1 = ''
    I[31].Text2 = 'This does not shoot'
    I[31].Text3 = 'anymore but it can'
    I[31].Text4 = 'still pack a punch.'
    I[31].Frequency = 1 #1

    #I.append (ICard.ICard())
    #I[X].ID = 'I00X'
    #I[X].Name = ''
    #I[X].Range = ''
    #I[X].Type = ''
    #I[X].Size = ''
    #I[X].Bonus = 0
    #I[X].CheckType = ''
    #I[X].CheckVal = 0
    #I[X].Text1 = ''
    #I[X].Text2 = ''
    #I[X].Text3 = ''
    #I[X].Text4 = ''
    #I[X].Frequency = 0 #0

    return I
