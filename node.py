from pygame import Surface
from common import WINDOW, TILE_SIZE, grid, toWorldPoint

class Node:
    def __init__(self, position):
        self.position = position
        self.g_cost = float('inf')
        self.h_cost = 0 
        self.f_cost = float('inf')
        self.start_direction = None
        self.end_direction = None
        self.parent = None
        self.image = Surface((TILE_SIZE, TILE_SIZE))

    # able to compare node with node now
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    
    def draw(self):
        WINDOW.blit(self.image, toWorldPoint(self.position))