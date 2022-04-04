import sys

import pygame

from settings import Settings
from rocket import Rocket

class RocketLauncher:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Launcher")

        self.rocket = Rocket(self)
        


    def run_game(self):
        """Start the main loop for the game"""
        while True:  
            self.check_events()

            self.update_events()
            
    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                 sys.exit()
            
    def update_events(self):
        # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.rocket.blit()        

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    rocket = RocketLauncher()
    rocket.run_game()