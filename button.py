from pygame import MOUSEBUTTONDOWN, sprite, mouse, BLEND_RGBA_ADD
from common import WINDOW, WINDOW_HEIGHT, WINDOW_WIDTH
from pipe import start_pipe, end_pipe
from button_callback import *
from assets import wall_button_image, play_button_image, pipe_sprites, find_button_image, reset_button_image, start_game_button_image

buttons = sprite.Group()

class Button(sprite.Sprite):
    def __init__(self, position, image, callback):
        super().__init__()
        self.image_copy = image
        self.image = self.image_copy.copy()
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
                    if self == button:
                        continue
                    button.isActive = False
                    button.image = button.image_copy.copy()

                self.isActive = not self.isActive

            if self.isActive:
                self.callback()
                self.image = self.image_copy.copy()
                self.image.fill((100,100,100,0),None,BLEND_RGBA_ADD)

            else:
                self.image = self.image_copy.copy()
                

    def draw(self):
        WINDOW.blit(self.image, self.rect)

start_game_button = Button((WINDOW_WIDTH //2, WINDOW_HEIGHT // 2), start_game_button_image, lambda: ())
buttons.remove(start_game_button)

reset_button = Button((900, 100), reset_button_image, lambda: handle_reset())
play_button = Button((900, 150), play_button_image, lambda: handle_play(start_pipe))
find_button = Button((900, 200), find_button_image, lambda: handle_find())
add_wall_button = Button((900, 250), wall_button_image, handle_wall)

Button((875, 350), pipe_sprites.get("DL")[0], lambda: handle_pipe("D", "L"))
Button((925, 350), pipe_sprites.get("LD")[0], lambda: handle_pipe("L", "D"))
Button((875, 400), pipe_sprites.get("DR")[0], lambda: handle_pipe("D", "R"))
Button((925, 400), pipe_sprites.get("RD")[0], lambda: handle_pipe("R", "D"))
Button((875, 450), pipe_sprites.get("DU")[0], lambda: handle_pipe("D", "U"))
Button((925, 450), pipe_sprites.get("UD")[0], lambda: handle_pipe("U", "D"))
Button((875, 500), pipe_sprites.get("LR")[0], lambda: handle_pipe("L", "R"))
Button((925, 500), pipe_sprites.get("RL")[0], lambda: handle_pipe("R", "L"))
Button((875, 550), pipe_sprites.get("LU")[0], lambda: handle_pipe("L", "U"))
Button((925, 550), pipe_sprites.get("UL")[0], lambda: handle_pipe("U", "L"))
Button((875, 600), pipe_sprites.get("UR")[0], lambda: handle_pipe("U", "R"))
Button((925, 600), pipe_sprites.get("RU")[0], lambda: handle_pipe("R", "U"))