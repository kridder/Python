import ICard
import random

def Create(I):

    ID = []

    for (i, line) in enumerate(I):
        while I[i].Frequency > 0:
            ID.append(I[i])
            I[i].Frequency -= 1

    random.shuffle(ID)
    return [I[0]] + ID
