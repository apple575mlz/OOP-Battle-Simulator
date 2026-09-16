import random

class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name, xpreturn, coindrop):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.xpreturn = xpreturn
        self.coindrop = coindrop
        
        self.triprate = 5
        self.spawnrate = 10
        self.critrate = 1

    def attack(self):
        return random.randint(self.attack_power//3, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0