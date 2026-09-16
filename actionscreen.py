from stage import *
from enemydefiner import *
from attackhandler import *
from actionscreenenemyhandler import *
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