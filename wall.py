from common import WINDOW, toWorldPoint, grid
from assets import wall_button_image

walls = {}

class Wall:
    def __init__(self, position):

        self.position = position
        self.image = wall_button_image
        self.rect = self.image.get_rect()
        self.rect.topleft = toWorldPoint(position)

        walls[self.position] = self
        grid[self.position] = self

    def draw(self):
        WINDOW.blit(self.image, self.rect)