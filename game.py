import pygame
pygame.init()
from scene_manager import SceneManager
from common import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from level1 import Level1
from game_play import GamePlay

level1 = Level1()
game_play = GamePlay()

class Game:
    def __init__(self):
        self.scene_manager = SceneManager()
        self.scene_manager.add_scene("level1", level1)
        self.scene_manager.add_scene("game play", game_play)
        self.scene_manager.set_scene(level1)

        self.clock = pygame.time.Clock()
        pass

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.scene_manager.handle_event()
            self.scene_manager.update()
            self.scene_manager.render()

            pygame.display.update()
            pass