from pygame import mouse
from common import TILE_SIZE, GRID_SIZE, grid, directions_match, directions_by_name
from pipe import Pipe, pipes
from wall import Wall, walls
from astar import find_using_astar

def handle_reset():
    pipes.clear()
    walls.clear()
    grid.clear()

def handle_play(start_pipe):
    if len(pipes):
        next_position = (
            start_pipe.position[0] + directions_by_name.get(start_pipe.end_direction)[0],
            start_pipe.position[1] + directions_by_name.get(start_pipe.end_direction)[1]
            )
        next_pipe = pipes.get(next_position)
        if next_pipe:
            if start_pipe.end_direction == directions_match.get(next_pipe.start_direction):
                next_pipe.isAnimate = True

def handle_find():
    find_using_astar()

def handle_wall():
    mouse_position = mouse.get_pos()

    position = (mouse_position[0] // TILE_SIZE, mouse_position[1] // TILE_SIZE)

    if position[0] <= GRID_SIZE:

        instance = grid.get(position)

        if instance == None:
            wall = Wall(position)
            grid[position] = wall

        elif instance.__class__ == Wall:
            walls.pop(instance.position)
            grid.pop(instance.position)

def handle_pipe(start_direction, end_direction):
    mouse_position = mouse.get_pos()

    position = (mouse_position[0] // TILE_SIZE, mouse_position[1] // TILE_SIZE)

    if position[0] <= GRID_SIZE:
        instance = pipes.get(position)

        if instance == None:
            pipe = Pipe(position)
            pipe.start_direction = start_direction
            pipe.end_direction = end_direction

            pipe.set_image()

            pipes[pipe.position] = pipe
            grid[position] = pipe

        elif instance.__class__ == Pipe:
            pipes.pop(instance.position)
            grid.pop(instance.position)