from os.path import dirname, join
import pygame

class Ship:
    """ A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.dir_path = dirname(__file__)
        #self.current_dir = dirname(__file__)
        self.file_path = join(self.dir_path, "./ship.bmp")
        self.moving_right = False
        self.moving_left = False
        print(self.file_path)

        #Load the ship image and get its rect
        self.image = pygame.image.load(self.file_path)
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center fo the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

    def update(self):
        #move right
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_speed
        #move left
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)


# if __name__ == "__main__":
#     ship = Ship()
