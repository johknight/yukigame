import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        super().__init__()  
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
