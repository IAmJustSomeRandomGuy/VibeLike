import pygame
from settings import *


class Bullet:
    def __init__(self, x, y, direction):
        self.pos = pygame.Vector2(x, y)
        self.direction = pygame.Vector2(direction).normalize()
        self.rect = pygame.Rect(0, 0, BULLET_SIZE, BULLET_SIZE)
        self.life = 35
        self.sync()

    def sync(self):
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def update(self):
        self.pos += self.direction * BULLET_SPEED
        self.life -= 1
        self.sync()

    def draw(self, screen):
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)