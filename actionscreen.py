def showscreen(player, enemy):
    print(f"So {player.name}, what will you do?")
    print(f"1: Swing at {enemy.name}")
    print(f"2: Inspect {enemy.name}")
    print(f"3: Review {player.name}'s stats")
    return int(input())

def handleResponseToScreen(selection):
    if selection == 1:
        print("selection registered as one.")