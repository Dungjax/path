from pygame import Surface, mouse, MOUSEBUTTONDOWN
from common import WINDOW, TILE_SIZE, grid, toWorldPoint, directions_match, GRID_SIZE, directions_by_name
from assets import pipe_sprites, start_pipe_sprites, end_pipe_sprites

pipes = {}

class Pipe:
    def __init__(self, position):
        self.position = position
        self.g_cost = float('inf')
        self.h_cost = 0 
        self.f_cost = float('inf')
        self.parent = None
        self.start_direction = None
        self.end_direction = None
        
        self.images = None
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = toWorldPoint(position)

        self.isAnimate = False
        self.image_index = 0
        self.animate_speed = 0.5
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def set_image(self):
        self.images = pipe_sprites.get(self.start_direction + self.end_direction)
        self.image = self.images[0]

    def update(self):
        if self.isAnimate:
            if self.image_index < len(self.images) - 1:
                self.image_index += self.animate_speed
                self.image = self.images[int(self.image_index)]
            else:
                next_position = (
                    self.position[0] + directions_by_name.get(self.end_direction)[0],
                    self.position[1] + directions_by_name.get(self.end_direction)[1]
                    )
                next_pipe = pipes.get(next_position)
                if next_pipe:
                    if self.end_direction == directions_match.get(next_pipe.start_direction):
                        next_pipe.isAnimate = True
                else:
                    for pipe in list(pipes.values()):
                        if pipe.isAnimate == False:
                            return False
                    end_next_position = (
                        end_pipe.position[0] + directions_by_name.get(end_pipe.start_direction)[0],
                        end_pipe.position[1] + directions_by_name.get(end_pipe.start_direction)[1]
                    )
                    if pipes.get(end_next_position):
                        return True

    def draw(self):
        WINDOW.blit(self.image, self.rect)

class StartPipe:
    def __init__(self, position, end_direction):
        self.position = position

        self.start_direction = None
        self.end_direction = end_direction
        
        self.images = end_pipe_sprites.get(self.end_direction)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = toWorldPoint(position)

        self.isAnimate = False
        self.image_index = 0
        self.animate_speed = 1

        grid[position] = self

        self.isDragging = False
    
    def handleEvent(self, event):
        mouse_position = mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_position):
                self.isDragging = not self.isDragging
        
        if self.isDragging:
            position = (mouse_position[0] // TILE_SIZE, mouse_position[1] // TILE_SIZE)
            if position[0] <= GRID_SIZE:
                pipes.clear()

                self.change_position(position)
    
    def draw(self):
        WINDOW.blit(self.image, self.rect)

    def change_position(self, position):
        if grid.get(self.position):
            grid.pop(self.position)
        self.position = position
        grid[self.position] = self
        self.rect.topleft = toWorldPoint(self.position)

class EndPipe(StartPipe):
    def __init__(self, position, start_direction):
        super().__init__(position, start_direction)
        self.position = position

        self.start_direction = start_direction
        self.end_direction = None
        
        self.images = end_pipe_sprites.get(self.start_direction)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = toWorldPoint(position)

        grid[position] = self

        self.isDragging = False

start_pipe = StartPipe((0, 0), "R")
end_pipe = EndPipe((15, 15), "U")