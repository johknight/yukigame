import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed):
        super().__init__()
        self.image = images
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.health = 5

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed

        self.rect.x = max(self.rect.x, 0)
        self.rect.x = min(self.rect.x, SCREEN_WIDTH - self.rect.width)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def display_health(self, surface):
        health_text = pygame.font.SysFont(None, 36).render(f'Health: {self.health}', True, WHITE)
        surface.blit(health_text, (10, 10))