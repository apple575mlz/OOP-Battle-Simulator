from weapons import *

sword1 = CopperDullBlade()
sword2 = IronShortSword()

def shop():
    print()
    print("----- Welcome to the Shop! -----")
    print("1: Weapons")
    print("2: Healing Items")
    print("3: Potions")
    print("4: Armor")
    print("0: Back")

    return int(input())

def doshopselection(selection, mainchar):
    if selection == 1:
        weaponshophandler(weaponshop(), mainchar)

    elif selection == 0:
        pass

def weaponshophandler(selection, mainchar):
    if selection == 1:
        copperdullbladebuyscreen(mainchar)

    elif selection == 0:
        doshopselection(shop(), mainchar)

def weaponshop():
    print()
    print("----- Welcome to the weapons shop! -----")
    print(f"1: {sword1.name} - {sword1.cost}. {sword1.attack} Attack.")
    print(f"2: {sword2.name} - {sword2.cost}. {sword2.attack} Attack.")

    print("0. Back")

    return int(input())

def copperdullbladebuyscreen(mainchar):
    if mainchar.currentmoney - sword1.cost >= 0 and sword1.owned == False:
        mainchar.currentmoney -= sword1.cost
        mainchar.additem(sword1)
        sword1.owned = True
        print()
        print(f"Purchase successful! New balance: {mainchar.currentmoney} coins.")
        input("Press anything to continue...")
        weaponshophandler(weaponshop(), mainchar)

    elif mainchar.currentmoney - sword1.cost < 0:
        print("Sorry! You do not have enough money for that!")
        input("Press anything to continue...")
        weaponshophandler(weaponshop(), mainchar)

    elif sword1.owned == True:
        print("You already own that item!")
        weaponshophandler(weaponshop(), mainchar)