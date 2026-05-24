import pygame
from settings import *
from entities.entity import Entity


class Explosion(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 222, EXPLOSION_COLOR)
        self.life = 30



    def update(self, delta):
        self.life -= 1