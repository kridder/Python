def Check (attacker):
    if attacker.Stunned > 0:
        attacker.Stunned -= 1

        if attacker.Stunned > 2:
            attacker.Stunned = 2

    if attacker.RENerve > 0:
        attacker.RENerve -= 1

    if attacker.LENerve > 0:
        attacker.LENerve -= 1
