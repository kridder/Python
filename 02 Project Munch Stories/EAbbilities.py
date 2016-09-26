import ECard

def Init(E):

    EA = ['Enemy Abbilities:']

    for (e, line) in enumerate(E):
        if not E[e].Abbility == '' and not E[e].Abbility == 'Abbility':
            if E[e].Frequency > 0:
                X = 0
                for (ea, line) in enumerate(EA):
                    if EA[ea] == E[e].Abbility:
                        X = 1
                if X == 0:
                    EA.append(E[e].Abbility)

    
    return EA

def Read(EC, EA, AEA):
    
    for (ec, line) in enumerate(EC):
        for (ea, line) in enumerate(EA):
            if EC[ec].Abbility == EA[ea]:
                AEA[ea] = EA[ea]

    return AEA
                
