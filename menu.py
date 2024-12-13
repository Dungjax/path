from scene import Scene
from common import WINDOW
from assets import back_ground_image
from button import start_game_button

class Menu(Scene):
    def __init__(self):
        super().__init__()

        self.next_scene = None

    def handle_event(self, event):
        start_game_button.handleEvent(event)
        pass

    def update(self):
        if start_game_button.isActive:
            return "level1"
    
    def render(self):
        print(9)
        WINDOW.blit(back_ground_image, (0, 0))
        start_game_button.draw()
    
    def cleanup(self):
        pass