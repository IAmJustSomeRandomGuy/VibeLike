import pygame
from settings import *
from entities.entity import Entity


class HeartPickup(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 22, HEART_COLOR)