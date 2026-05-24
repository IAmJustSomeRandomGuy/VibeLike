import pygame

from settings import *
from entities.player import Player
from systems.combat import handle_bullets
from systems.dungeon import Dungeon


class Game:
    def __init__(self):
        self.dungeon = Dungeon()

        self.room_x = START_ROOM[0]
        self.room_y = START_ROOM[1]

        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.bullets = []

    @property
    def room(self):
        return self.dungeon.rooms[(self.room_x, self.room_y)]

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.update(keys)

        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_UP]:
            direction.y = -1
        elif keys[pygame.K_DOWN]:
            direction.y = 1
        elif keys[pygame.K_LEFT]:
            direction.x = -1
        elif keys[pygame.K_RIGHT]:
            direction.x = 1

        bullet = self.player.shoot(direction)

        if bullet:
            self.bullets.append(bullet)

        for enemy in self.room.enemies:
            enemy.update(self.player)

        handle_bullets(self.bullets, self.room.enemies)
        self.room.update()

    def draw(self, screen):
        screen.fill(BG)

        for bullet in self.bullets:
            bullet.draw(screen)

        for enemy in self.room.enemies:
            enemy.draw(screen)

        for pickup in self.room.pickups:
            pickup.draw(screen)

        self.player.draw(screen)