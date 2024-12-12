from pygame import MOUSEBUTTONDOWN, sprite, mouse
from common import WINDOW
from pipe import start_pipe, end_pipe
from button_callback import *
from assets import wall_button_image, play_button_image, pipe_sprites, find_button_image

buttons = sprite.Group()

class Button(sprite.Sprite):
    def __init__(self, position, image, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.isActive = False
        self.callback = callback

        buttons.add(self)
        pass

    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:

            if self.rect.collidepoint(mouse.get_pos()):
                for button in buttons:
                    if button == self:
                        continue
                    button.isActive = False

                self.isActive = True

            if self.isActive:
                self.callback()

    def draw(self):
        WINDOW.blit(self.image, self.rect)

next_button = Button((850, 50), play_button_image, lambda: handle_play(start_pipe))
play_button = Button((850, 100), play_button_image, lambda: handle_play(start_pipe))
find_button = Button((850, 150), find_button_image, lambda: handle_find(start_pipe, end_pipe))
add_wall_button = Button((850, 200), wall_button_image, handle_wall)

Button((850, 300), pipe_sprites.get("DL")[0], lambda: handle_pipe("D", "L"))
Button((900, 300), pipe_sprites.get("LD")[0], lambda: handle_pipe("L", "D"))
Button((850, 350), pipe_sprites.get("DR")[0], lambda: handle_pipe("D", "R"))
Button((900, 350), pipe_sprites.get("RD")[0], lambda: handle_pipe("R", "D"))
Button((850, 400), pipe_sprites.get("DU")[0], lambda: handle_pipe("D", "U"))
Button((900, 400), pipe_sprites.get("UD")[0], lambda: handle_pipe("U", "D"))
Button((850, 450), pipe_sprites.get("LR")[0], lambda: handle_pipe("L", "R"))
Button((900, 450), pipe_sprites.get("RL")[0], lambda: handle_pipe("R", "L"))
Button((850, 500), pipe_sprites.get("LU")[0], lambda: handle_pipe("L", "U"))
Button((900, 500), pipe_sprites.get("UL")[0], lambda: handle_pipe("U", "L"))
Button((850, 550), pipe_sprites.get("UR")[0], lambda: handle_pipe("U", "R"))
Button((900, 550), pipe_sprites.get("RU")[0], lambda: handle_pipe("R", "U"))
