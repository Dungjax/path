import pygame
from common import WINDOW, grid
from scene import Scene
from pipe import start_pipe, end_pipe, pipes
from wall import Wall, walls
from button import buttons
from assets import back_ground_image

class Level1(Scene):
    def __init__(self):
        super().__init__()
        start_pipe.change_position((6, 6))
        end_pipe.change_position((11,11))

        Wall((8, 6))
        Wall((8, 7))
        Wall((8, 8))
        Wall((8, 9))
        Wall((8, 10))
        Wall((9, 10))
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        for button in buttons:
            button.handleEvent(event)
        
        start_pipe.handleEvent(event)
        end_pipe.handleEvent(event)

    def update(self):
        start_pipe.update()
        end_pipe.update()
        for pipe in pipes.values():
            pipe.update()
        pass
        
        self.cleanup()
        return "game play"

    def render(self):
        WINDOW.blit(back_ground_image, (0, 0))

        for pipe in pipes.values():
            pipe.draw()
        start_pipe.draw()
        end_pipe.draw()

        buttons.draw(WINDOW)
        walls.draw(WINDOW)
        pass

    def cleanup(self):
        grid.clear()
        pipes.clear()
        walls.empty()