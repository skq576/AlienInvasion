import sys

import pygame
from settings import Settings
from ship import Ship
from ufo import Ufo
from missile import Missile

class AlienInvasion:
    """Over Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.ufos = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()

        # self.available_width = self.settings.screen_width
        # self.available_ufos = (self.available_width // (self.ufo_example.rect.width * 2))
        # self.available_height = self.settings.screen_height
        # self.available_rows = (self.available_height // (self.ufo_example.rect.height * 2) // 2)

        self.initial_ufo_location = 0

    def run_game(self):
        """Start the main loop for the game."""
        #create ufos
        self.creat_fleet_ufos()
        
        while True:
            
            self._check_events()
            self.ship.update()
            self.ufos.update()
            self.missiles.update()
            self._update_screen()
            self.delete_missiles()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_missile()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_event(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def creat_fleet_ufos(self):
        "Determine avaialable space for UFOs"
        ufo_example = Ufo(self)
        available_width = self.settings.screen_width
        available_ufos = (available_width // (ufo_example.rect.width * 2))
        available_height = self.settings.screen_height
        available_rows = (available_height // (ufo_example.rect.height * 2) // 2)

        """create ufos"""
        for row in range(1, available_rows):
            print(row)
            for ufo_number in range(1, available_ufos):
                self._create_ufo_row(ufo_number, row)
                #print(ufo_number)
            
    def _create_ufo_row(self, ufo_number, row):
            new_ufo = Ufo(self)
            new_ufo.rect.x = new_ufo.rect.x * (ufo_number * 2)
            new_ufo.rect.y = new_ufo.rect.y * (row * 2)
            self.ufos.add(new_ufo)
            #print(new_ufo.rect.x)
    
    def _fire_missile(self):
        """create a new missile and add it to the missile group"""
        new_missile = Missile(self)
        self.missiles.add(new_missile)

    def delete_missiles(self):
        for missile in self.missiles.copy():
            if missile.rect.bottom <= 0:
                self.missiles.remove(missile)
        #print(len(self.missiles))

    def _update_screen(self):
        """Redraw screen during each pass through loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for ufo in self.ufos.sprites():
            ufo.blitme()
        #if self.missile.shooting_missile or self.missile.missile_shot:
        for missile in self.missiles.sprites():
            missile.blitme()

        pygame.display.flip()
    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()