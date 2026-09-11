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
    hero = Hero("Sir Smiting")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"And {hero.name} has returned his call!")

    while Gamerun == True:
        handleResponseToScreen(showscreen(hero, goblin))



if __name__ == "__main__":
    main()