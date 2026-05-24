import pygame
from settings import *


class Explosion:
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 222, 222)
        self.rect.center = (round(x), round(y))
        self.life = 30

    def draw(self, screen):
        pygame.draw.rect(screen, EXPLOSION_COLOR, self.rect)

    def update(self):
        self.life -= 1