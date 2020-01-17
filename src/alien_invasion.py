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
        self.ufo = Ufo(self)
        self.missile = Missile(self, self.ship)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            
            self._check_events()
            self.ship.update()
            self.ufo.update()
            self.missile.update()
            self._update_screen()


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
        if event.key == pygame.K_a:
            self.ufo.moving_left =True
        if event.key == pygame.K_SPACE:
            self.missile.shooting_missile = True
        elif event.key ==pygame.K_q:
            sys.exit()
    
    def _check_keyup_event(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_a:
            self.ufo.moving_left = False

    def _update_screen(self):
        """Redraw screen during each pass through loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.ufo.blitme()
        if self.missile.shooting_missile or self.missile.missile_shot:
            self.missile.blitme()

        pygame.display.flip()
    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()