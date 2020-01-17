import pygame
from os.path import dirname, join

class Missile():
    def __init__(self, ai_game, ship):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ship = ship

        self.dir_path = dirname(__file__)
        self.file_path = join(self.dir_path, "./missile.bmp")

        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()
        self.shooting_missile = False
        self.missile_shot = False

        #draw missile at the top of ship
        self.rect.bottom = self.ship.rect.top
        self.rect.x = self.ship.x

    def update(self):
        if self.shooting_missile == True:
            #self.rect = self.ship.rect.top
            self.shooting_missile = False
            #self.blitme()
            self.missile_shot = True
        if self.missile_shot == True:
            self.rect.y -= self.settings.missile_speed
            #self.blitme()
        else:
            self.rect.x = self.ship.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        


    