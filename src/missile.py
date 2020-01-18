from os.path import dirname, join
import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """MISSILE to shoot enemies"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        self.dir_path = dirname(__file__)
        self.file_path = join(self.dir_path, "./missile.bmp")

        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()
        self.shooting_missile = False
        self.missile_shot = False

        #draw missile at the top of ship
        self.rect.midtop = self.ship.rect.midtop
        self.rect.x = self.ship.x

    def update(self):
        self.rect.y -= self.settings.missile_speed

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        


    