import pygame
from settings import *


class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.rect = pygame.Rect(0, 0, ENEMY_SIZE, ENEMY_SIZE)
        self.health = 2
        self.sync()

    def sync(self):
        self.rect.center = self.pos

    def update(self, player):
        direction = player.pos - self.pos

        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * ENEMY_SPEED

        self.sync()

    def draw(self, screen):
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)