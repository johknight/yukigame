import pygame

class Button:
    def __init__(self, image_path, x, y, callback):
        self.image = image_path
        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()