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