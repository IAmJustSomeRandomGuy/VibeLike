import pygame


class Entity:
    def __init__(self, x, y, size, color):
        self.pos = pygame.Vector2(x, y)
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.color = color
        self.sync()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def sync(self):
        self.rect.center = (round(self.pos.x), round(self.pos.y))
    
    def _physics_update(self, delta: float, *args, **kwargs):
        self.update(delta, *args, **kwargs)
        self.sync()
    
    def update(self, delta: float, *args, **kwargs):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)