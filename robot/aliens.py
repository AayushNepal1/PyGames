import pygame


class Alien:
    """Creating the character."""

    def __init__(self, ai_game):
        """Initialize the character and set the character to the center of the screen."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the image of the alien character
        self.image = pygame.image.load('images/aliens.bmp')
        self.rect = self.image.get_rect()

        # Placing the alien character to the center
        self.rect.center = self.screen_rect.center

    def blit(self):
        """Draw the alien character to its current location."""
        self.screen.blit(self.image, self.rect)
