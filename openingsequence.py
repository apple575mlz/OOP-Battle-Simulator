from enemydefiner import *
import time

def runopening():
    ARENA_NAME = "The Gates of Hades"

    """Open the arena and intrerooduce its first opponent."""
    print(f"Be prepared for {ARENA_NAME}!")
    time.sleep(1)
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    time.sleep(1)
    print("The gates are opening...")
    time.sleep(0.5)

    for enemy in returnenemies(0):
        print(f"{enemy.name} enters the arena with {enemy.health} health!")
        time.sleep(0.5)
    time.sleep(1)
    print(f"And {returnhero().name} has returned their call!")

def runnewenemies(enemies):
    print()
    time.sleep(1)
    print("The gates are opening...")
    time.sleep(1)
    
    for enemy in enemies:
        print(f"{enemy.name} enters the arena with {enemy.health} health!")
        time.sleep(0.5)
    time.sleep(1)