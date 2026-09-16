from goblin import Goblin
from hero import Hero
import random

#----------Opener----------------
goblin = Goblin("Goblinstein", 75, 1000)
goblin2 = Goblin("Goblinberg", 75, 1000)
openingenemies = [goblin, goblin2]

hero = Hero("Sir Smiting")
def returnhero():
    return hero

#-----------First Level------------
placeholdergob = Goblin("placeholder", 10, 100)
stage1enemies = [placeholdergob]



def returnenemies(stage):
    if stage == 0:
        return openingenemies
    elif stage == 1:
        return stage1enemies