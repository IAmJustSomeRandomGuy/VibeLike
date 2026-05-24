import random
from entities.enemy import Enemy
from entities.pickup import HeartPickup
from settings import *


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.cleared = False

        self.enemies = []
        self.pickups = []

        self.generate()

    def generate(self):
        count = random.randint(2, 5)

        for _ in range(count):
            ex = random.randint(100, WIDTH - 100)
            ey = random.randint(100, HEIGHT - 100)
            self.enemies.append(Enemy(ex, ey))

    def update(self):
        if not self.cleared and len(self.enemies) == 0:
            self.cleared = True

            if random.random() < 0.5:
                self.pickups.append(
                    HeartPickup(WIDTH // 2, HEIGHT // 2)
                )