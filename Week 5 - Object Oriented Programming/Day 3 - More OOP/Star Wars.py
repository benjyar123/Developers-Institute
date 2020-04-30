# DECLARATIONS

from W5D3XPG import ForceWielder, Jedi, Sith
from random import randint
import time

luke = Jedi("Luke Skywalker", 10, 11)
obi_wan = Jedi("Obi-Wan Kenobi", 8, 14)
yoda = Jedi("Yoda", 12, 14)
maul = Sith("Maul", 10, 13)
bane = Sith("Bane", 10, 10)
vader = Sith("Vader", 14, 12)

all_characters = [luke, obi_wan, yoda, maul, bane, vader]
jedis = [luke, obi_wan, yoda]
siths = [maul, bane, vader]

def battle_round (jedis, siths, round):
    jedi_fighter = jedis[randint(0, len(jedis)-1)]
    sith_fighter = siths[randint(0, len(siths)-1)]
    print("Round " + str(round) + ": " + jedi_fighter.name + " vs. " + sith_fighter.name + "\n")
    time.sleep(2)
    print("***FIGHT***\n")
    time.sleep(2)
    winner = jedi_fighter.fight(sith_fighter)

    if winner == jedi_fighter.name:
        print(f"{jedi_fighter.name} DESTROYS {sith_fighter.name}! That's gonna sting in the morning.\n{sith_fighter.name} is out of the fight. GET SOME ICE ON THAT!\n")
        time.sleep(2)
        jedi_fighter.train()
        time.sleep(2)
        siths.remove(sith_fighter)
    elif winner == sith_fighter.name:
        print(f"{sith_fighter.name} CRUNCHES {jedi_fighter.name}! The force is strong with this one!\n{jedi_fighter.name} took a real beating!\n")
        time.sleep(2)
        jedi_fighter.train()
        time.sleep(2)
        sith_fighter.train()
        time.sleep(2)
    elif winner == "tie":
        print("It's a tie! Nothing to separate these two galacticos.\nThey're both exhausted and training is cancelled!")
        time.sleep(2)

    return jedis, siths


def battle(jedis, siths):
    round = 1
    print("***ALL-STAR INTERGALACTIC CLASH JEDIS VS. SITHS***\n")
    time.sleep(2)
    print("Jedi Team News:\n")
    for fighters in jedis:
        print(f"Name: {fighters.name}\nPower: {fighters.power}\nWisdom: {fighters.wisdom}\n")
    time.sleep(5)
    print("Siths Team News:\n")
    for fighters in siths:
        print(f"Name: {fighters.name}\nPower: {fighters.power}\nWisdom: {fighters.wisdom}\n")
    time.sleep(5)
    while (len(jedis) > 0) and (len(siths) > 0):
        battle_round(jedis, siths, round)
        round += 1
        time.sleep(4)
    if len(siths) == 0:
        print("BATTLE OVER. THE DARK SIDE HAVE BEEN DEFEATED!\n")
    elif len(jedis) == 0:
        print("Something has gone wrong it shouldn't be possible for Jedis to lose according to these rules!\n")


# EXECUTIONS

battle(jedis, siths)






