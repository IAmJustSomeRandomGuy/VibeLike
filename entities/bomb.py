import pygame
from settings import *
from entities.explosion import Explosion
from entities.entity import Entity

class Bomb(Entity):
    def __init__(self, x, y, detonation_delay):
        super().__init__(x, y, 26, BOMB_COLOR)
        self.detonation_delay = detonation_delay
        self.knockback = 750
    
    def update(self, delta):
        self.detonation_delay -= 1

    def explode(self):
        return Explosion(self.rect.centerx, self.rect.centery)