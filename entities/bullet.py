import pygame
from settings import *
from entities.entity import Entity


class Bullet(Entity):
    def __init__(self, x, y, direction):
        super().__init__(x, y, BULLET_SIZE, BULLET_COLOR)
        self.direction = pygame.Vector2(direction).normalize()
        self.life = 35
        self.knockback = 250

    def update(self, delta):
        self.pos += self.direction * BULLET_SPEED
        self.life -= 1