import pygame
from settings import *
from entities.explosion import Explosion

class Bomb:
    def __init__(self, x, y, detonation_delay):
        self.detonation_delay = detonation_delay
        self.rect = pygame.Rect(x, y, 26, 26)

    def draw(self, screen):
        pygame.draw.rect(screen, BOMB_COLOR, self.rect)
    
    def update(self):
        self.detonation_delay -= 1

    def explode(self):
        return Explosion(self.rect.centerx, self.rect.centery)