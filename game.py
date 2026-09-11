from goblin import Goblin
from hero import Hero
from actionscreen import handleResponseToScreen, showscreen


ARENA_NAME = "The Gates of Hades"
Gamerun = True


def main():
    """Open the arena and intrerooduce its first opponent."""
    print(f"Be prepared for {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Goblinstein")
    goblin2 = Goblin("Goblinberg")
    hero = Hero("Sir Smiting")

    totalenemies = [goblin, goblin2]

    for enemy in totalenemies:
        print(f"{enemy.name} enters the arena with {enemy.health} health.")
    print(f"And {hero.name} has returned his call!")

    while Gamerun == True:
        handleResponseToScreen(showscreen(hero, goblin))



if __name__ == "__main__":
    main()