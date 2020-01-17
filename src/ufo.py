import pygame
from os.path import dirname, join

class Ufo:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.dir_path = dirname(__file__)
        self.file_path = join(self.dir_path, "./ufo.bmp")
        
        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
