import pygame
from os.path import dirname, join

class Ship:
    """ A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.dir_path = dirname(__file__)
        #self.current_dir = dirname(__file__)
        self.file_path = join(self.dir_path, "./ship.bmp")
        print(self.dir_path)

        #Load the ship image and get its rect
        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center fo the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)


# if __name__ == "__main__":
#     ship = Ship()
