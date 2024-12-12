from pygame import display

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

TILE_SIZE = 50
GRID_SIZE = 15

FPS = 60

directions_by_position = {
    (-1, 0) : "L",
    (1, 0) :  "R",
    (0, -1) : "U",
    (0, 1) : "D",
}

directions_by_name = {
    "L" : (-1, 0),
    "R" : (1, 0),
    "U" : (0, -1),
    "D" : (0, 1)
}

directions_match = {
    "L": "R",
    "R": "L",
    "U": "D",
    "D": "U"
}

grid = {}

def toWorldPoint(position):
    return (position[0] // TILE_SIZE, position[1] // TILE_SIZE)

def toWorldPoint(position):
    return (position[0] * TILE_SIZE, position[1] * TILE_SIZE)
