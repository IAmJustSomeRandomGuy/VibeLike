import pygame, math
from entities.entity import Entity
from settings import FRICTION

class DamageableEntity(Entity):
    def __init__(self, x, y, size, color, max_health):
        super().__init__(x, y, size, color)
        self.speed = pygame.Vector2(0, 0)
        self.MAX_HEALTH = max_health
        self.health = max_health

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def sync(self):
        self.rect.center = (round(self.pos.x), round(self.pos.y))
    
    def take_damage(self, damage, pos, knockback):
        direction = self.pos - pos
        direction = direction.normalize()*knockback

        self.health -= damage
        self.speed += direction
    
    def heal(self, amount):
        self.health = min(self.MAX_HEALTH, self.health + amount)
    
    def _physics_update(self, delta: float, *args, **kwargs):
        self.pos += self.speed * delta
        self.speed = self.speed/(1+FRICTION*delta)
        self.speed = pygame.Vector2(round(self.speed.x, 1), round(self.speed.y, 1))

        self.update(delta, *args, **kwargs)

        self.sync()