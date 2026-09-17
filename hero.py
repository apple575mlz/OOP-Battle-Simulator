import random
from levelrequirements import *

class Hero:
    def __init__(self, name, hands):
        self.name = name
        self.health = 300
        self.attack_power = 75
        self.level = 1
        self.xpneeded = 200
        self.overflowxp = 0
        self.currentmoney = 100000
        self.critchance = 2

        self.backpackitems = {"Weapons": [], "Heals": [], "Potions": [], "Armor": []}

        self.equippedweapon = hands

    def testattack(self):
        return 100000
        
    def attack(self):
        return random.randint((self.attack_power + self.equippedweapon.attack)//2, self.attack_power + self.equippedweapon.attack)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
    
    def is_alive(self):
        return self.health > 0

    def doilevel(self, xpgained):
        tempxpneeded = self.xpneeded - xpgained
        if tempxpneeded <= 0:
            return True
        else:
            return False

    def addnonlevel(self, xpadd):
        self.xpneeded -= xpadd

    def levelup(self, xp):
        self.level += 1
        self.addnonlevel(xp)

        if self.xpneeded < 0:
            self.overflowxp = (self.xpneeded - (self.xpneeded * 2))

        self.xpneeded = int(returnlevels()[str(self.level)])
        self.addnonlevel(self.overflowxp)
        self.overflowxp = 0

    def handlexp(self, xp):
        if self.doilevel(xp):
            self.levelup(xp)
            print(f"You leveled up! You are now level {self.level}!")
            print(f"Xp needed to get to the next level: {self.xpneeded}")
        else:
            self.addnonlevel(xp)

    def additem(self, type, item):
        if type == "Weapon":
            self.backpackitems["Weapons"].append(item)

    def equipweapon(self, item):
        self.equippedweapon.equipped = False
        self.equippedweapon = item
        self.equippedweapon.equipped = True