from enemydefiner import *
from shopscreen import *
from actionscreen import *
from stage import *
from openingsequence import *
from backpackhandler import *
import time

def selectionscreen():
    print()
    print("----- What would you like to do? -----")
    print("1: Go to shop")
    print("2: Go gambling")
    print("3: Review your stats")
    print("4: Review your items")
    print("0: Go to next level!")
    return int(input())

def dointerselection(select):
    global movingon
    if select == 1:
        doshopselection(shop(), returnhero())


    elif select == 3:
        checkingself(returnhero())

    elif select == 4:
        backpackselection(openbackpack(returnhero()), returnhero())

    elif select == 0:
        movingon = True
        increasestage()
        runnewenemies(returnenemies(returnstage()))

def handleintermission():
    movingon = False
    print("Congrats! You have cleared all of the enemies on this stage.")
    time.sleep(1)

    while not movingon:
        dointerselection(selectionscreen())