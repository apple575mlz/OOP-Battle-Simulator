import time

def openbackpack(mainchar):
    print()
    print("----- Backpack -----")
    counter = 1
    for category, items in mainchar.backpackitems.items():
        if items:
            print(f"{counter}: {category}")
            counter += 1
    if counter == 1:
        print("There's nothing in here!")
    print("0: Go back")

    return int(input())

def backpackselection(selection, mainchar):
    if selection == 0:
        pass

    elif selection == 1:
        weaponinspector(mainchar)

def weaponinspector(mainchar):
    inweapon = True

    while inweapon == True:
        print()
        print("----- Weapons -----")

        county = 0
        for weapon in mainchar.backpackitems["Weapons"]:
            print(f"{county+1}: {weapon.name}")
            county += 1
        print("0: Back")

        weaponselect = int(input())
        if not weaponselect == 0:
            selectedweapon = mainchar.backpackitems["Weapons"][weaponselect-1]
        else:
            inweapon = False

        if not weaponselect == 0:
            inspector = True
        else:
            inspector = False

        while inspector == True:
            print(f"----- {selectedweapon.name} -----")
            print(f"Attack: {selectedweapon.attack}")
            print(f"Equipped: {selectedweapon.equipped}")

            print()
            print("1: Equip Weapon")
            print("0: Back")

            wepp = int(input())

            if wepp == 1:
                weppyloop = True
            elif wepp == 0:
                weppyloop = False
                inspector = False

            while weppyloop == True:
                if selectedweapon.equipped == False and not mainchar.equippedweapon == selectedweapon:
                    mainchar.equippedweapon.equipped = False
                    mainchar.equippedweapon = selectedweapon
                    mainchar.equippedweapon.equipped = True

                    time.sleep(0.5)
                    print("Weapon equipped successfully!")

                    inspector = False
                    weppyloop = False

                elif selectedweapon.equipped == True:
                    print("You already have that weapon equipped!")
                    time.sleep(1)
                    weppyloop = False

                elif mainchar.equippedweapon == selectedweapon:
                    print("You already have that weapon equipped!")
                    time.sleep(1)
                    weppyloop = False