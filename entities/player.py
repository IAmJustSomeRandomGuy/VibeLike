import pygame
from settings import *
from entities.bullet import Bullet


class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.rect = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
        self.health = PLAYER_MAX_HEALTH
        self.cooldown = 0
        self.sync()

    def sync(self):
        self.rect.center = self.pos

    def update(self, keys):
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            move.y -= 1
        if keys[pygame.K_s]:
            move.y += 1
        if keys[pygame.K_a]:
            move.x -= 1
        if keys[pygame.K_d]:
            move.x += 1

        if move.length_squared() > 0:
            move = move.normalize() * PLAYER_SPEED
            self.pos += move

        self.sync()

        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self, direction):
        if self.cooldown > 0:
            return None

        if direction.length_squared() == 0:
            return None

        self.cooldown = 12

        return Bullet(
            self.rect.centerx,
            self.rect.centery,
            direction
        )

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)