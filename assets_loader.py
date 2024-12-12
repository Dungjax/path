import pygame

pygame.font.init()

def load_image(path):
    return pygame.image.load(path).convert()

def load_alpha_image(path):
    return pygame.image.load(path).convert_alpha()

# 1 dimension only
def load_animated_image(path):
    sheet = pygame.image.load(path).convert_alpha()
    
    width = sheet.get_width()
    height = sheet.get_height()
    columns = width // height
    
    return [sheet.subsurface((i * height, 0, width // columns, height)).convert_alpha() for i in range(columns)]

def load_sound(path):
    return pygame.mixer.Sound(path)

def load_font(path, size):
    return pygame.font.Font(path, size)