from stage import *
from enemydefiner import *
from actionscreenenemyhandler import *
import time
import random

def heroattacking(enemies, mainchar):
    print()
    print("--- Which Enemy do you Attack? -----")
    county = 0
    for enemy in enemies:
        print(f"{county}) {enemy.name}, {enemy.health} health")
        county += 1
    whichnumber = int(input())
    whichattack = enemies[whichnumber]
    print()
    print(f"You have chosen to swing at {whichattack.name}...")
    time.sleep(0.5)
    attkdmg = mainchar.attack()

    critrng = random.randint(1, 20)
    if critrng <= mainchar.critchance:
        attkdmg *= 2.5
        print("You have landed a critical hit!")
        time.sleep(1)

    whichattack.take_damage(attkdmg)
    print(f"You dealt {attkdmg} damage to {whichattack.name}!")
    time.sleep(0.5)
    print(f"{whichattack.name} has {whichattack.health} health left.")
    time.sleep(1)

    if not whichattack.is_alive():
        levelbefore = mainchar.level

        print(f"You have slain {whichattack.name}!")
        time.sleep(0.5)
        addcoins(whichattack, mainchar)
        print()
        print(f"You have gained {whichattack.xpreturn} xp!")

        mainchar.handlexp(whichattack.xpreturn)
        levelafter = mainchar.level
        time.sleep(0.5)

        if levelbefore == levelafter:
            print(f"XP needed to level up: {mainchar.xpneeded}")
        input("Press anything to continue...")
        
    print()
    if not handlelist(returnenemies(returnstage())) == []:
        print("----- Enemy's Turn to Attack! -----")
        handleenemyattack(handlelist(returnenemies(returnstage())), mainchar)
    else:
        print("No enemies are left to attack.")

    input("Press anything to continue...")

def handleenemyattack(enemies, mainchar):
    for enemy in enemies:
        print(f"{enemy.name} is attacking you!")
        time.sleep(0.5)
        rng = random.randint(0, 20)
        if rng <= enemy.triprate:
            print(f"{enemy.name} has tripped and fell, dealing 0 damage.")
        else:
            attkdmg = enemy.attack()

            enemycritrng = random.randint(1, 20)
            if enemycritrng <= enemy.critrate:
                attkdmg *= 2.5
                print(f"{enemy.name} Landed a critical hit!")
                time.sleep(1)

            mainchar.take_damage(attkdmg)
            print(f"{enemy.name} has attacked you for {attkdmg} damage!")
            time.sleep(0.5)
            print(f"Remaining health: {mainchar.health}.")
            time.sleep(1)
            print()

def addcoins(deadenemy, mainchar):
    rngcoins = random.randint(deadenemy.coindrop//3, deadenemy.coindrop)
    mainchar.currentmoney += rngcoins
    print(f"{deadenemy.name} dropped {rngcoins} coins!")
    time.sleep(0.5)
    print(f"Your current balance: {mainchar.currentmoney} coins")
    time.sleep(0.5)