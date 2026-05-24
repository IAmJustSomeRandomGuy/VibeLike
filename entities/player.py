import pygame
from settings import *
from entities.bullet import Bullet
from entities.bomb import Bomb
from entities.damagable_entity import DamageableEntity

class Player(DamageableEntity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SIZE, PLAYER_COLOR, PLAYER_MAX_HEALTH)
        self.shoot_cooldown = 0
        self.bomb_cooldown = 0
        self.bomb_detonation_delay = 120
    

    def update(self, delta: float, keys):
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
            self.speed += move

        self.sync()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        if self.bomb_cooldown > 0:
            self.bomb_cooldown -= 1

    def shoot(self, direction):
        if self.shoot_cooldown > 0:
            return None

        if direction.length_squared() == 0:
            return None

        self.shoot_cooldown = 20

        return Bullet(
            self.rect.centerx,
            self.rect.centery,
            direction
        )
    
    def drop_bomb(self):
        if self.bomb_cooldown > 0:
            return None

        self.bomb_cooldown = 90

        return Bomb(
            self.rect.centerx,
            self.rect.centery,
            self.bomb_detonation_delay
        )