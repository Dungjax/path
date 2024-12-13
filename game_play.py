from common import WINDOW, grid
from scene import Scene
from pipe import start_pipe, end_pipe, pipes
from wall import walls
from button import buttons
from assets import back_ground_image

class GamePlay(Scene):
    def __init__(self):
        super().__init__()

    def initialize(self):
        start_pipe.change_position((0, 0))
        end_pipe.change_position((15, 15))

    def handle_event(self, event):
        
        for button in buttons:
            button.handleEvent(event)
        
        start_pipe.handleEvent(event)
        end_pipe.handleEvent(event)

    def update(self):
        #print(len(grid))
        for pipe in pipes.values():
            pipe.update()
        pass

    def render(self):
        WINDOW.blit(back_ground_image, (0, 0))

        for pipe in pipes.values():
            pipe.draw()
        start_pipe.draw()
        end_pipe.draw()
        
        for wall in walls.values():
            wall.draw()

        buttons.draw(WINDOW)
        
        pass

    def cleanup(self):
        grid.clear()
        pipes.clear()
        walls.clear()