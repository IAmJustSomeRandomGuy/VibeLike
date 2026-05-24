from rooms.room import Room
from settings import *


class Dungeon:
    def __init__(self):
        self.rooms = {}

        for y in range(ROOM_GRID_H):
            for x in range(ROOM_GRID_W):
                self.rooms[(x, y)] = Room(x, y)