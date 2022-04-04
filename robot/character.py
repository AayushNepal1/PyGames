import sys

import pygame

from aliens import Alien


class Character:
    """Overall class to manage the game assets and behaviour."""

    def __init__(self):
        """Initializing the game and creating the resources."""
        pygame.init()
        # Setting the screen size
        self.screen = pygame.display.set_mode((1200, 800))
        # Setting the game title
        pygame.display.set_caption('Robot')
        self.alien = Alien(self)
        self.bg_color = (0,0,255)

        
    def run_game(self):
        while True:
            self.check()
            self.screen.fill(self.bg_color)
            self.alien.blit()
            # Make most recently drawn screen visible
            pygame.display.flip()

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
if __name__ == '__main__':
    ai = Character()
    ai.run_game()