import pygame
from settings import *


class HeartPickup:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 22, 22)

    def draw(self, screen):
        pygame.draw.rect(screen, HEART_COLOR, self.rect)