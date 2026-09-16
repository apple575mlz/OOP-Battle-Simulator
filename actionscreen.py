from stage import *
from enemydefiner import *
import random
import time

def showscreen():
    print()
    print(f"----- So, {returnhero().name}, what will you do? -----")
    print("1: Mercilessly Swing Your Sword")
    print("2: Inspect Opponents")
    print("3: Review your stats")
    print("4: Open Backpack")
    return int(input())

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
    attkdmg = mainchar.testattack()
    whichattack.take_damage(attkdmg)
    print(f"You dealt {attkdmg} to {whichattack.name}!")
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
            mainchar.take_damage(attkdmg)
            print(f"{enemy.name} has attacked you for {attkdmg} damage!")
            time.sleep(0.5)
            print(f"Remaining health: {mainchar.health}.")
            time.sleep(1)
            print()

def inspecting(enemies):
    print()
    print("----- Current Enemies -----")
    for enemy in enemies:
        print(f"{enemy.name}, {enemy.health} health.")
    input("Press anything to continue...")

def openbackpack(mainchar):
    print()
    print("----- Backpack -----")
    if not mainchar.backpackitems == []:
        for thingy in mainchar.backpackitems:
            print(thingy.name)
    else:
        print("There's nothing in here!")
    input("Press anything to continue...")


def checkingself(mainchar):
    print()
    print("---- Stats -----")
    print(f"You have {mainchar.attack_power} attack.")
    print(f"You have {mainchar.health} health.")
    print(f"You have {mainchar.currentmoney} coins.")
    print(f"Current Level: {mainchar.level}")
    print(f"XP needed to level up: {mainchar.xpneeded}")
    input("Press anything to continue...")

def handleResponseToScreen(selection):
    allenemies = handlelist(returnenemies(returnstage()))

    if selection == 1:
        heroattacking(allenemies, returnhero())

    elif selection == 2:
        inspecting(allenemies)

    elif selection == 3:
        checkingself(returnhero())

    elif selection == 4:
        openbackpack(returnhero())

def handlelist(enemies):
    currentemmies = enemies
    counter = 0
    for enemy in currentemmies:
        if not enemy.is_alive():
            currentemmies.pop(counter)
        else:
            pass
        counter += 1
    return currentemmies

def checkalive(enemies):
    counter = 1
    for enemy in enemies:
        counter += 1
        if not enemy.is_alive():
            counter -= 1
    if counter == 1:
        return False
    else:
        return True

def addcoins(deadenemy, mainchar):
    rngcoins = random.randint(deadenemy.coindrop//3, deadenemy.coindrop)
    mainchar.currentmoney += rngcoins
    print(f"{deadenemy.name} dropped {rngcoins} coins!")
    time.sleep(0.5)
    print(f"Your current balance: {mainchar.currentmoney}")
    time.sleep(0.5)