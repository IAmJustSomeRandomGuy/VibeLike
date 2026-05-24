import pygame
from settings import *
from entities.damagable_entity import DamageableEntity


class Enemy(DamageableEntity):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_SIZE, ENEMY_COLOR, 4)
    
    def update(self, delta, player):
        direction = player.pos - self.pos

        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * ENEMY_SPEED