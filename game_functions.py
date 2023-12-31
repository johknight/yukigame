
import pygame
from config import *
from buttons import Button 

background_image = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH), (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_background(screen, alpha=100):
    temp_background = background_image.copy()
    temp_background.set_alpha(alpha)
    screen.blit(temp_background, (0, 0))

#in the main.py the game_over = False is for this
def reduce_player_health(player, amount):
    player.health -= amount
    if player.health <= 0:
        return True
    return False

def start_game(main):
    main()

def main_menu(images, screen, clock, start_game):
    start_button = Button(images["start_button"], 200, 300, start_game)
    exit_button = Button(images["exit_button"], 200, 400, pygame.quit)
    yuki = Button(images["yuki"], 200, 350, start_game)

    menu_running = True
    while menu_running:
        draw_background(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            start_button.is_clicked(event)
            exit_button.is_clicked(event)
        start_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        
class GameState:
    def __init__(self):
        self.ENEMY_SPEED = ENEMY_SPEED  # Set initial enemy speed
        self.score = 0
        self.kill_counter = 0
        self.speed_level = 1
        self.last_bullet_fire_time = 0
        self.BULLET_COOLDOWN = BULLET_COOLDOWN  # Set initial bullet cooldown

    def update_enemy_speed(self, increment):
        self.ENEMY_SPEED += increment