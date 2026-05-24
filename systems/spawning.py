import random
from entities.enemy import Enemy
from settings import *



def spawn_wave(count):
    enemies = []

    for _ in range(count):
        side = random.choice(["top", "bottom", "left", "right"])

        if side == "top":
            x = random.randint(0, WIDTH)
            y = -50

        elif side == "bottom":
            x = random.randint(0, WIDTH)
            y = HEIGHT + 50

        elif side == "left":
            x = -50
            y = random.randint(0, HEIGHT)

        else:
            x = WIDTH + 50
            y = random.randint(0, HEIGHT)

        enemies.append(Enemy(x, y))

    return enemies