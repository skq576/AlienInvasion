from os.path import dirname, join
import pygame


class Ufo:
    """create UFO"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.dir_path = dirname(__file__)
        self.file_path = join(self.dir_path, "./ufo.bmp")
        
        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left == True and self.rect.left > 0:
            self.rect.x -= self.settings.ufo_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
