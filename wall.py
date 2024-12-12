from pygame import sprite
from common import WINDOW, toWorldPoint, grid
from assets import wall_button_image

walls = sprite.Group()

class Wall(sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = wall_button_image
        self.rect = self.image.get_rect()
        self.rect.topleft = toWorldPoint(position)

        walls.add(self)
        grid[position] = self

    def draw(self):
        WINDOW.blit(self.image, self.rect)