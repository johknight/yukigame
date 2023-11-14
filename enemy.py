import pygame, random
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0]), -ENEMY_SIZE[1]))
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            return True
        return False
            
    @staticmethod
    def spawn_enemy(image):
        return Enemy(image)