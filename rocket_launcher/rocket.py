import pygame

class Rocket:
    """A class to manage a rocket."""

    def __init__(self, rocket):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket.screen
        self.screen_rect = rocket.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Setting a rocket image to center
        self.rect.center = self.screen_rect.center
    
    def blit(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
        