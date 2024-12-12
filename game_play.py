import pygame
from common import WINDOW
from scene import Scene
from pipe import start_pipe, end_pipe, pipes
from wall import walls
from button import buttons
from assets import back_ground_image

class GamePlay(Scene):
    def __init__(self):
        super().__init__()

        start_pipe.change_position((0, 0))
        end_pipe.change_position((15, 15))

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

    def render(self):
        WINDOW.blit(back_ground_image, (0, 0))

        for pipe in pipes.values():
            pipe.draw()
        start_pipe.draw()
        end_pipe.draw()

        buttons.draw(WINDOW)
        walls.draw(WINDOW)
        pass