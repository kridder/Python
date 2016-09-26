import ECard
import random

def Create(E):

    ED = []

    for (e, line) in enumerate(E):
        while E[e].Frequency > 0:
            ED.append(E[e])
            E[e].Frequency -= 1

    random.shuffle(ED)
    return [E[0]] + ED

        
            
