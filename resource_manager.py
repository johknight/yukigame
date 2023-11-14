import pygame
from config import *

def load_images():
    image_paths = {
        "player": PLAYER_IMAGE_PATH,
        "bullet": BULLET_IMAGE_PATH,
        "enemy": ENEMY_IMAGE_PATH,
        "start_button": START_BUTTON_IMAGE_PATH,
        "exit_button": EXIT_BUTTON_IMAGE_PATH,
        "resart_button": START_BUTTON_IMAGE_PATH,
        "yuki": YUKI_IMAGE_PATH
    }
    images = {}
    for name, path in image_paths.items():
        images[name] = pygame.image.load(path).convert_alpha()
    #scaling for images
    images["bullet"] = pygame.transform.scale(images["bullet"], (9, 27)).convert_alpha()
    images["start_button"] = pygame.transform.scale(images["start_button"], (192, 78)).convert_alpha()
    images["exit_button"] = pygame.transform.scale(images["exit_button"], (192, 78)).convert_alpha()
    images["enemy"] = pygame.transform.scale(images["enemy"], (30, 80)).convert_alpha() # (5*16)
    images["player"] = pygame.transform.scale(images["player"], (64, 44)).convert_alpha()
    return images

